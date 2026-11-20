"""Red test first: the Torelli input is cited by an eponym, not by a numbered statement.

The repository's citation standard: every published input is cited by author and
numbered statement (chapter, section, theorem, lemma, definition or exercise), and no
printed page or page offset is written on a page.

PROPOSITION (to be proved).  Item 3 of @prop:coble-period-domain asserts that the
moduli space M_Co of Coble surfaces is an open subset of D(T_Co)/O(T_Co).  The
published statement that carries this is [@DK13, Prop. 3.2], whose hypotheses are the
ones the book already checks in @lem:d2-unpolarised-family(1): the fibre X_b is an
algebraic K3 surface, and its M-lattice is the M of (3.6) with N = <2> + E(2).  The
bare reference [@PS71] names a paper and no statement, so under the standard it is not
a citation of an input at all: DK13 Prop. 3.2 is the numbered statement, and the
Torelli-type theorem of Pyatetskii--Shapiro and Shafarevich enters through DK13's own
proof of it, not as an independent input of this book.

This test is RED until the lemma is on the page, item 3 cites it, and no bare [@PS71]
remains on either D2a page.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
MC = ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md"
LA = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

LEMMA = "lem:d2a-coble-moduli-quotient"


def _block(text: str, label: str) -> str:
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_no_bare_eponymous_torelli_citation():
    for path in (MC, LA):
        text = path.read_text(encoding="utf-8")
        assert "[@PS71]" not in text, f"{path.name} cites [@PS71] with no numbered statement"


def test_the_lemma_is_a_proved_statement_with_a_numbered_source():
    text = MC.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, sorted(re.findall(r"#(lem:[a-z0-9-]*quotient)", text))
    body = _block(text, LEMMA)
    # the source is numbered, and it is the statement that carries the claim
    assert "@DK13, Prop. 3.2" in body
    # the lattice is the published one of (3.6), not one introduced here
    assert "@DK13, (3.6)" in body or "@DK13, §3" in body
    assert "E_{10}(2)" in body or "E(2)" in body


def test_the_lemma_checks_the_hypotheses_of_the_citation():
    text = MC.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "the lemma is not on the page"
    start = text.index("#" + LEMMA)
    proof = text[start:]
    proof = proof[proof.index("::: {.proof}"):]
    proof = proof[:proof.index("\n:::", proof.index("::: {.proof}") + 10)]
    # exactly the hypotheses the book already establishes for the fibres
    assert "@lem:d2-unpolarised-family(1)" in proof
    assert "K3" in proof


def test_item_three_cites_the_lemma():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, "prop:coble-period-domain")
    item = body[body.index("3. The quotient"):]
    assert "@" + LEMMA in item, item[:400]


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
    raise SystemExit(_run_all())
