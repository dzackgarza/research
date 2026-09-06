# vendor

Drop point for third-party Python code you want importable from Sage sessions.
This is the *external* tier; see the table in `AGENTS.md` under "Repository layout"
for the other three (published external, spike, graduated `src/`).
Nothing you author belongs here — code you write starts in a spike.

Copy a loose script or a flat package directory here:

    cp somescript.py computations/vendor/          # imports as `somescript`
    cp -r ~/clones/bar/bar computations/vendor/    # imports as `bar`

`sage-init.sage` appends this directory to `sys.path`, so every interactive Sage
session — REPL and every Jupyter kernel — sees these with no restart and no
per-package step.  Only this directory itself is on the path: a clone whose
package sits deeper (`bar/src/bar/`) is installed instead with
`sage -pip install --no-deps -e <clone>`.

Non-interactive callers (`sage -c`, `sage -python`, pytest) do **not** get this
automatically, because Sage only reads its startup file for interactive sessions.
They put this directory on `PYTHONPATH` themselves.

Contents are gitignored: these are other people's code. **A consequence worth
knowing: local edits to vendored code are invisible to git and lost on re-copy.**
If a vendored dependency needs fixing, fix it upstream or record the defect in an
issue — do not quietly patch the working copy.

Third-party *dependencies* still need installing —
`sage -pip install <dep>` — path magic only finds code, not its deps.

Executables are not vendored here.  The `py_polyhedral` wrapper in `src/`
resolves the `polyhedral_common` programs it wraps from `PATH` at call time;
build them from a clone of github.com/MathieuDutSik/polyhedral_common and link
them into a directory on `PATH`.

## Current clones

None.
