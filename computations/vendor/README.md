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

`sage-indefinite-port` owns every indefinite and Lorentzian lattice algorithm
on the owned formed-lattice category.  The preamble calls its functions directly;
when the package or a function is missing, the call fails.  It is a clone whose package sits under `src/`, so it is not vendored here either;
install it with `sage -pip install --no-deps -e <clone>`.  It depends on this
package, so the preamble imports it at the call rather than at module level.

## Current clones

None.
