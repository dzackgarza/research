# Owning-library group operations at the adopted runtime: measurements (2026-11-05)

Read-only. Nothing under `/workspace/nucleus/work/home/sage-image/` was written and `/sage`
was not touched.

Two separate observations are recorded here, and they have different standing.

- **Finding 1** -- `libgap` at the rootfs interpreter `/sage/.venv/bin/python` stops the
  interpreter on any evaluation. This is a measurement with a reproducible recipe and a
  structural localisation, and it is **not** an attribution of a defect: the other
  workspaces on this VM report working `libgap`, I could not reproduce their condition or
  find the installation they use, and reconciling the two is the runtime owner's call. What
  I withdraw is the earlier framing of this as "the runtime's GAP is broken"; what stands is
  the transcript.
- **Finding 2** -- `O_plus()` and `spinor_norm()` refuse every lattice over `ZZ` at the
  provider pin this rootfs carries. This one is independent of GAP, reproduces under a
  clean environment on the provider's own minimal example, and contradicts the provider's
  own tests, so it is a provider regression worth filing.

## Runtime, as adopted

- rootfs `/workspace/nucleus/work/home/sage-image/rootfs`, entered with
  `.scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo`
  -- the recipe of `smw0_maintained-gamma_container.sh`, which is the corpus's own;
- `SageMath version 11.0.beta5`; `SAGE_LOCAL=/sage/.venv`;
- the provider is the image's own checkout `/repos/sage-extensions` at
  `7b222e86214524a53802350f3cfda9c513707600`, which is what `import sage_extensions`
  resolves to inside the rootfs.

## The environment split

`bash computations/reports/coble_owner_gap-envsplit.sh` prints all of the following; the
transcript is `coble_owner_gap-envsplit-run.txt`. It is worth splitting the environment
before any further claim about GAP, and these are the results of doing so.

**1. Which `sage`.** From this project's shell, `command -v sage python` gives
`/opt/math/bin/sage` and `/opt/math/bin/python`, and `readlink -f` resolves to
`/opt/math/bin/sage` -- a Sage installation that is *not* the rootfs one. The repository's
`.envrc:7` sets `SAGE_BIN="${SAGE_BIN:-$HOME/.local/bin/sage}"` and prepends its directories
to `PATH`, so that default is the one to check:

```
ls: cannot access '/workspace/nucleus/work/home/.local/bin/sage': No such file or directory
```

`~/.local/bin` contains no `sage`, so `.envrc` selects nothing on this VM and exports no
`SAGE_*`/`GAP_*` variable. **3. `env | grep -iE 'GAP|SAGE' | sort` prints nothing at all**
-- this shell has no GAP or SAGE variable set. My probes never used `.envrc` either: they
named `/sage/.venv/bin/sage` inside the rootfs explicitly.

**2. `sage.env`.** The two installations answer differently, which is itself part of the
split:

```
# host /opt/math
SAGE_LOCAL= /opt/math
GAP_ROOT_PATHS= /opt/math/lib/gap/;/opt/math/share/gap/
# rootfs /sage/.venv
AttributeError: module 'sage.env' has no attribute 'GAP_ROOT_PATHS'
SAGE_LOCAL= /sage/.venv
```

The rootfs's Sage has no `GAP_ROOT_PATHS` in `sage.env` at all, so on that installation GAP's
root is settled by GAP itself and not by a Sage variable. `kernel_info()` did not return from
either installation either: on the host it raises at import,

```
ImportError: cannot import name GAPError        # sage.libs.gap.util
ImportError: cannot import name libgap          # sage.libs.gap.libgap
```

and on the rootfs it reaches GAP and then stops (step 4). The host Sage's `libgap` is not a
working alternative: it cannot be imported at all. **6. No third installation exists on this
VM**: a whole-filesystem search outside the rootfs finds only `/opt/math/lib/libgap.so.9`
and `/opt/math/lib/libgap.so`.

**4. The asked-for probe.** Clean environment, rootfs interpreter, no GAP or SAGE variable
and no `PATH` inherited from this project's shell:

```
$ proot -R <rootfs> ... /usr/bin/env -i HOME=/root /sage/.venv/bin/python \
      -c "from sage.libs.gap.libgap import libgap; print(libgap.eval('1+1'))"
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
------------------------------------------------------------------------
------------------------------------------------------------------------
cysignals failed to execute cysignals-CSI: No such file or directory
------------------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred.
This probably occurred because a *compiled* module has a bug
------------------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred.
This probably occurred because a *compiled* module has a bug
in it and is not properly wrapped with sig_on(), sig_off().
Python will now terminate.
------------------------------------------------------------------------
```

The probe fails, so per the standing instruction I stopped on #646 rather than continuing to
claim against it. The full 84-line capture, with the
`libgap.so.11(DoOperation1Args+0x80)` -> `EXEC_CURR_FUNC` -> `ReadEvalCommand` ->
`READ_GAP_ROOT` frame sequence, is `coble_owner_gap-envsplit-run.txt` and
`coble_owner_gap-blockers-run.txt`.

**Where the mismatch sits (5).** Not in the environment and not in `proot`:

- GAP initializes and reaches `READ_GAP_ROOT`, so it finds a root and reads library text; it
  is not failing to locate GAP;
- the root that the orchestrator's check names, `/sage/.venv/lib/gap/`, contains `pkg` and
  `sysinfo.gap` and **no `lib/` tree**, so `lib/oper1.g` cannot come from there;
- the tree it does read is `/sage/.venv/share/gap/lib`, and `sysinfo.gap` declares
  `GAP_VERSION="4.16.1"`, `GAP_BUILD_VERSION="4.16.1"`,
  `GAParch=x86_64-pc-linux-gnu-default64-kv11`, matching the `11` in `libgap.so.11`;
- `lib/oper1.g` is 41070 bytes and `lib/type1.g` 27322 there, against 39545 and 26872 in the
  rootfs's distro GAP at `/usr/share/gap`, a third and different tree;
- every one of the 515 files of `share/gap/lib` carries one mtime, `2026-11-04 16:25:57`, the
  same mtime as `libgap.so.11` itself, so the pair came out of one extraction and the skew is
  inside the image rather than introduced by a later edit of one of them;
- `proot` is excluded as the cause: `md5sum` of both files is identical inside the proot view
  and on the host (`9b3375c69be85e8a64dc0130e2af7055`, `9a832c9fd8f4680df4c0d5d2efbd7311`),
  so the bytes GAP reads are the bytes on disk.

So on this rootfs the kernel refuses two library modules on a CRC mismatch -- which is what
GAP prints when the kernel and the library tree it reads come from different GAP versions --
and then stops, because the operations those modules install are absent. That is the whole
of my claim about GAP. Whether the fix is to restore a matching `lib/` tree, to place one at
`/sage/.venv/lib/gap/lib`, or to run this rootfs the way the other workspaces run it, is not
mine to decide and is untouched here.

## Finding 1, as measured: the four probes

`bash computations/reports/coble_owner_gap-blockers.sh` (output
`coble_owner_gap-blockers-run.txt`) runs four probes one process each, because a segfault
ends the interpreter:

```
########## probe 1: libgap itself, no owning library involved
about to evaluate 1+1 in libgap
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
########## probe 2: the finite orthogonal group of a 4-class discriminant form
A_{U(2)} has 4 classes, 3 of them isotropic
about to ask for O(A_{U(2)})
[... the same two warnings, then SIGSEGV]
########## probe 3: membership in ker(rho_T), the matrix #646 turns on
reflection built; asking whether it lies in ker(rho_T)
[... the same two warnings, then SIGSEGV]
########## probe 4: the committed record coble_isotropic_orbits.py, green on 2026-11-04
[... the same two warnings, then SIGSEGV]
```

Probe 4 is the one that bears on provenance: it is a committed, previously green record and
it now stops before printing a line. Probe 1 involves no owning-library code at all.

Ruled out, each by a run rather than by an inference:

| hypothesis | check | outcome |
| --- | --- | --- |
| a stale GAP workspace cached under `~/.sage/gap` | empty `DOT_SAGE` | same stop; a fresh workspace does not help |
| a wrong GAP root on the search path | `GAP_ROOT_PATH=/sage/.venv/share/gap` and `=/usr/share/gap` | same stop under both |
| a user package autoloaded from `/root/.gap/pkg` | an empty directory bound over `/root` | same stop |
| this shell's environment | `env -i` with `HOME` only | same stop (step 4 above) |
| the repository `.envrc` | `SAGE_BIN` default does not exist; no `SAGE_*`/`GAP_*` set | nothing selected |
| the provider pin | probe 1 imports no provider | independent of the provider |
| `proot` corrupting the file reads | `md5sum` inside and outside | identical |

## Finding 2: `O_plus()` and `spinor_norm()` refuse every lattice over `ZZ`

Independent of GAP, of the environment and of this project's shell. On the provider's own
minimal lattice, under `env -i`, with no `SAGE_*` or `GAP_*` variable present:

```
  O_plus()       REFUSED AssertionError: O^+(Integral lattice of rank 2 and signature (1, 1))
                 is the kernel of the real spinor norm at the real place of Frac(R); QQ has
                 exactly one, but Frac(R) = Fraction Field of Integer Ring: pass a real
                 embedding of it to spinor_kernel
  spinor_norm()  REFUSED AssertionError: the spinor norm of Integral lattice of rank 2 and
                 signature (1, 1) is computed here over represented absolute number fields,
                 but Frac(R) = Fraction Field of Integer Ring
```

Both hold with the provider's `ZZ` as well as with Sage's, and both hold for `T_Co`. The
provider's own suite asserts the opposite -- `tests/lattices/test_definite.sage:321`
(`o_plus = lattice.O_plus()`), `tests/lattices/test_definite.sage:315`
(`lattice.spinor_norm(QQ.Mor(RR)(...))`), and
`tests/lattices/test_orthogonal_reduction_sequences.sage:130-134` -- so this is a regression
at pin `7b222e86` and not a contract research is being held to. It is the finding to file,
and it is why `Gamma_Co` cannot be built as an owned object.

## What this leaves available, and what it does not

Available, and used by `coble_gamma_co_reflective_set.py`: building a lattice from its Gram
data; `signature_pair`, `determinant`, `is_even`, `two_elementary_invariants`;
`possible_root_lengths`; `reflective_root_locus` as an object and as a membership test;
`Aut()`, `O_plus`, `stable_orthogonal_group` and their `intersection` **as objects**;
`reflection` and the action of an isometry on a vector; `determinant` of an isometry; and the
discriminant quadratic form with its class count and q-fibres, as re-run in
`coble_528_isotropic_classes-rerun-20261105.txt`.

Not available: the real spinor norm and hence `O^+(T_Co)` as a membership test; the
discriminant action of an isometry and hence `ker(rho_{T_Co})` as a membership test;
`roots`, `roots_of_square`, `root_sublattice` for an indefinite lattice (definite-only by
contract); the orthogonal group of any discriminant form, finite or not; orbit partitions;
and any operation returning generators of, or a finite-index certificate for, a subgroup of
`O(L)` of an indefinite `Z`-lattice.

Consequently #646's generation half, #689 and #688 cannot be settled with what runs here, and
this repository does not substitute a locally implemented group algorithm, orbit enumeration
or subobject enumeration for them. The two semantic handoffs are unchanged in substance:
`generators_or_finite_index_certificate`-style access to `O^+(L) cap ker(rho_L)` for a
`Z`-lattice, and a `block_preserving_subgroup`-style operation for a finite torsion form
computed from the declared decomposition rather than from the subobject family.
