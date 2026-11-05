# `gap` on PATH, `.envrc`, and the `is_isometric_to` call it blocked (2026-11-05)

This is sage#11 on this repository's side of it: `kernel_info()` runs the bare `gap` through
`PATH`, so whichever GAP `PATH` names is the one Sage adopts. Here it was the distribution's.

## Measured, in this session's shell

```
$ command -v sage
/opt/math/bin/sage
$ readlink -f "$(command -v sage)"
/opt/math/bin/sage
$ command -v gap
/opt/math/bin/gap
$ python -c 'import os, shutil; print(shutil.which("gap")); print(os.environ["PATH"])'
/opt/math/bin/gap
/workspace/nucleus/work/home/.local/bin:/workspace/nucleus/work/home/.cargo/bin:/workspace/nucleus/work/home/.elan/bin:/opt/lean/bin:/opt/math/bin:/usr/local/bin:/usr/bin:/bin
```

So on the host, `sage` and `gap` agree: both resolve into the one installation `/opt/math`.
The repository's `.envrc` was nevertheless wrong, in a way that only shows where the two
disagree:

```
$ grep -n 'SAGE_BIN=' .envrc
7:export SAGE_BIN="${SAGE_BIN:-$HOME/.local/bin/sage}"
$ ls -l "$HOME/.local/bin/sage"
ls: cannot access '/workspace/nucleus/work/home/.local/bin/sage': No such file or directory
```

The default is a path that does not exist, so the two directories the block derives from it
were prepended nowhere useful and `PATH` was left as it was. In the runtime that is fatal,
because there `/opt/math/bin` does not exist and `PATH` falls through to `/usr/bin`:

```
$ proot -R <rootfs> ... /sage/.venv/bin/sage -c 'import shutil,os; print(shutil.which("gap"))'
/usr/bin/gap
$ proot ... /bin/sh -c '/usr/bin/gap --version'
GAP 4.14.0 built on 2024-12-29 16:46:20+0000
$ proot ... /bin/sh -c '/sage/.venv/bin/gap --version'
GAP 4.16.1 built on 2026-11-04 16:25:38+0000
```

`/sage/.venv/bin/gap` is the launcher built for this venv — its embedded default root path,
read out of the binary, is `/sage/.venv/lib/gap;/sage/.venv/share/gap` — and it is GAP 4.16.1,
the version `libgap.so.11` and `sysinfo.gap` declare (`GAParch=...-default64-kv11`). The
distribution's 4.14 is not, which is why `lib/oper1.g` and `lib/type1.g` failed their
compiled-checksum check and the interpreter stopped.

## The correction

`.envrc` no longer defaults the driver to a path that need not exist: when `SAGE_BIN` is unset
it takes the launcher `command -v sage` actually resolves, resolves symlinks on it, and
prepends that launcher's directory and its adjacent `.venv/bin` (in that order, so the venv
comes first). Nothing is hard-coded and no GAP root is set by hand.

```
$ bash -c 'unset SAGE_BIN; . ./.envrc >/dev/null 2>&1; echo $SAGE_BIN; command -v gap'
/opt/math/bin/sage
/opt/math/bin/gap
```

In the runtime, where the launcher is `/sage/.venv/bin/sage`, the same derivation puts
`/sage/.venv/bin` first and `gap` becomes the 4.16.1 one.

## The call it was blocking

`C1.is_isometric_to(C2)` on the two complements of the Dawes 2.2 pair
(`computations/reports/coble_dawes-example-2-2_complements.py`), with `PATH` derived from the
resolved launcher:

```
launcher      : /sage/.venv/bin/sage
which gap     : /sage/.venv/bin/gap
C1: det 5 | C2: det 5
calling C1.is_isometric_to(C2) ...
is_isometric_to -> True
```

True, which agrees with the `A_4` conclusion reached there without it: rank 4, negative
definite, determinant 5, twenty roots of type `A_4`. The segfault recorded in that record
under the old `PATH` was the wrong GAP, not a defect of the call.
