"""No page of writing/ asserts the falsified equality as a fact.

`thm:gamma-co-not-stable` (lattices.md) refutes Gamma_Co = O~^+(T_Co), and issue #658's second
acceptance item is that every page carrying the open form is updated.  This module is the
invariant that makes the sweep checkable rather than asserted: every occurrence of the equality
must sit either in the withdrawn statement itself or on a line that marks it false.  It also
guards the counts, which were the other half of the open form: no page may attach 527 or 189 720
to F_Co without saying that they are the stable quotient's.

Run standalone (``python3 tests/engineering/test_coble_658_no_stale_equality.py``) or under pytest.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
WRITING = ROOT / "writing"

EQUALITY = [
    r"\Gamma_\Co = \widetilde\Orth^+(T_\Co)",
    r"\Gamma_\Co=\widetilde\Orth^+(T_\Co)",
]

# A line carrying any of these marks the equality as false, quoted, or assumed-for-contradiction.
NEGATIONS = (
    "is false",
    "former",
    "refutes",
    "not contained",
    "exactly when",
    "conjectur",
    "vacuous",
)


def _pages():
    return sorted(WRITING.rglob("*.md"))


def test_the_equality_never_appears_unmarked():
    offenders = []
    for path in _pages():
        text = path.read_text(encoding="utf-8", errors="replace")
        conceded = []
        m = re.search(r"\{\.\w+ #conj:gamma-co-stable\b", text)
        if m:
            end = text.find("\n:::", m.end())
            conceded.append((m.start(), len(text) if end < 0 else end))
        for pattern in EQUALITY:
            for hit in re.finditer(re.escape(pattern), text):
                if any(a <= hit.start() < b for a, b in conceded):
                    continue
                start = text.rfind("\n", 0, hit.start()) + 1
                line = text[start:text.find("\n", hit.end())]
                if any(k in line for k in NEGATIONS):
                    continue
                offenders.append("%s:%d" % (path.relative_to(ROOT), text.count("\n", 0, hit.start()) + 1))
    assert not offenders, "the falsified equality is asserted as fact at: %s" % offenders


def test_the_coble_counts_are_never_read_off_the_stable_quotient():
    offenders = []
    for path in _pages():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if not ("527" in line or "189\\,720" in line):
                continue
            names_coble = ("\\fco" in line) or ("F_{\\Co}" in line) or ("$\\fco$" in line)
            if not names_coble:
                continue
            if any(k in line for k in ("not", "undetermined", "rather", "instead", "and for no smaller",
                                       "names its group", "the stable quotient")):
                continue
            num = 527 if "527" in line else "189720"
            offenders.append("%s: %s" % (path.relative_to(ROOT), num))
    assert not offenders, "a Coble cusp count is read off the stable quotient at: %s" % offenders


def test_the_refutation_is_the_reason():
    lattices = (WRITING / "coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")
    assert "#thm:gamma-co-not-stable" in lattices
    assert "#conj:gamma-co-stable" in lattices and "This statement is false" in lattices


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
