# vendor

Drop point for third-party code you want importable from Sage notebooks.
This is the *external* tier; see the table in `AGENTS.md` under "Repository layout"
for the other three (published external, spike, graduated `src/`).
Nothing you author belongs here — code you write starts in a spike.

Clone or copy anything here:

    git clone https://github.com/foo/bar computations/vendor/bar
    cp somescript.py computations/vendor/

`dzack_research.preamble.vendor` owns the import paths. `sage-init.sage` calls it,
so every interactive Sage session — REPL and every Jupyter kernel — sees these
with no restart and no per-package step:

    vendor/           ->  loose scripts: vendor/foo.py       imports as `foo`
    vendor/*          ->  flat clones:   vendor/bar/bar/     imports as `bar`
    vendor/*/src      ->  src layouts:   vendor/bar/src/bar/ imports as `bar`

A clone whose module sits deeper than that needs one explicit line from whichever
module imports it — `vendor.activate_clone("pkg", "src", "lib")` — because no
general glob can find `pkg/src/lib/pkg.py`, and adding `pkg/src` would put a
`lib/` directory on `sys.path`.

Non-interactive callers (`sage -c`, `sage -python`, pytest) do **not** get this
automatically, because Sage only reads its startup file for interactive sessions.
They call `vendor.activate()` themselves. This is deliberately narrower than the
`.pth` file that used to live in Sage's venv: that covered every process, but it
was untracked, unreviewable, and destroyed by any Sage rebuild.

Contents are gitignored: these are other people's repos. **A consequence worth
knowing: local edits to vendored code are invisible to git and lost on re-clone.**
If a vendored dependency needs fixing, fix it upstream or record the defect in an
issue — do not quietly patch the working copy.

Third-party *dependencies* still need installing —
`sage -pip install <dep>` — path magic only finds code, not its deps.
Anything with a `pyproject.toml` you intend to hack on is better handled by
`sage -pip install -e <path>` instead of dropping it here.

Check the mechanism:

    sage -c 'from dzack_research.preamble import vendor; vendor.activate(); import _vendor_selfcheck, _srclayout; print(_vendor_selfcheck.ok, _srclayout.ok)'

(`_vendor_selfcheck.py` and `_fakeclone/` here exist only for that check.)

## Current clones

None.
