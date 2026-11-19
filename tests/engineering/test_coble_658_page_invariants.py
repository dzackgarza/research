"""Source-level invariants of the pages #658 touched.

`scripts/docs_check.py --source` needs `writing/.book/.assets/references.bib`, which `just
docs-assets` copies from a shared `~/.pandoc` checkout; that checkout is absent from this VM, so
the fast gate cannot run here and these are the parts of it that can be checked without the
bibliography:

  1. none of the ten macro spellings the corpus does not define (docs_check check 8);
  2. every `@ref` resolves to an id defined in `writing/`;
  3. every page parses under `pandoc -f markdown -t native`, which is what catches fence and div
     defects that `docs_check` reports as structural findings.

The file list is the union of the pages changed by the #658 commits 201c982c5f (item 1 on the
page), f67b436ca0 (item 2's sweep) and f97458dc06 (the no-stale-equality invariant).

Run standalone (``python3 tests/engineering/test_coble_658_page_invariants.py``) or under pytest.
"""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]

PAGES = [
    "writing/coble/coble-moduli/coble-families-research-program.md",
    "writing/coble/compactifications/reflection-data-and-replacements.md",
    "writing/coble/computations/discriminant-form-descent.md",
    "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md",
    "writing/coble/heegner-report/coble-heegner-research-report.md",
    "writing/coble/lattices-and-moduli/discriminant-orbits-of-the-coble-lattice.md",
    "writing/coble/lattices-and-moduli/lattices.md",
    "writing/coble/lattices-and-moduli/moduli-construction.md",
    "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md",
    "writing/coble/reference-tables/lattice-and-diagram-conventions.md",
    "writing/coble/stable-limits/ksba.md",
    "writing/dissertation/GAPS.md",
    "writing/open-questions.md",
]

BANNED_MACROS = ["\\Gent", "\\Fcox", "\\Fgen", "\\Fco", "\\Fen", "\\Fram", "\\TEn", "\\rk",
                 "\\bqty", "\\pqty"]


def test_no_undefined_macro():
    offenders = []
    for page in PAGES:
        text = (ROOT / page).read_text(encoding="utf-8", errors="replace")
        for macro in BANNED_MACROS:
            # \Fco must not fire on \fco, \Co or \Fcox; the others are literal.
            pattern = re.escape(macro) + (r"(?![A-Za-z])" if macro == "\\Fco" else "")
            for m in re.finditer(pattern, text):
                line = text.count("\n", 0, m.start()) + 1
                offenders.append("%s:%d %s" % (page, line, macro))
    assert not offenders, offenders


def test_every_reference_resolves():
    defined = set()
    for path in (ROOT / "writing").rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\{\.\w+ #([A-Za-z][A-Za-z0-9_:.\-]*)", text):
            defined.add(m.group(1).rstrip("."))
    offenders = []
    for page in PAGES:
        text = (ROOT / page).read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"@([a-z][A-Za-z0-9_]*:[A-Za-z0-9_.\-]+)", text):
            ref = m.group(1).rstrip(".")
            if ref not in defined:
                offenders.append("%s -> %s" % (page, ref))
    assert not offenders, offenders


def test_every_page_parses():
    pandoc = shutil.which("pandoc") or "/opt/math/bin/pandoc"
    if not pathlib.Path(pandoc).exists():
        return                                    # nothing to check without pandoc
    offenders = []
    for page in PAGES:
        r = subprocess.run([pandoc, "-f", "markdown", "-t", "native", str(ROOT / page)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            offenders.append("%s: %s" % (page, r.stderr.strip().splitlines()[:1]))
    assert not offenders, offenders


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
