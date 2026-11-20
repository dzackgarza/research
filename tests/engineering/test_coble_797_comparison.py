"""Red test first: the Coble stack sits inside the K3-with-involution stack of AE22.

research#797 asks for the comparison.  The claim to pin: the functor of
def:coble-moduli-functor factors through the moduli of K3 surfaces with a nonsymplectic
involution of type (11,11,1) of AE22 Section 2A-2C, by (S -> Y, X -> S, iota) |-> (X -> Y,
iota), and the image is characterised fibrewise by the quotient having |-K| empty.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
MC = ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md"

LEMMA = "lem:d0-coble-stack-in-involution-stack"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_comparison_lemma_exists_and_cites_both_sides():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    # the functor side is kof5's, cited by label
    assert "@def:coble-moduli-functor" in body
    # the involution side is AE22, by section
    assert "@AE22, §2A" in body or "@AE22, §2C" in body


def test_the_functor_is_fully_faithful_with_the_stated_image():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    assert "fully faithful" in body
    assert "\\abs{-K_{X/\\iota}}=\\emptyset" in body or "abs{-K}" in body


def test_openness_is_not_claimed_without_a_citation():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    # the lemma may call the image a substack, but if it says "open" it must say
    # what is missing; the honest form names the semicontinuity input
    if "open" in body:
        assert "semicontinuity" in body or "not proved" in body


def _run_all() -> int:
    items = [(n, f) for n, f in sorted(globals().items())
             if n.startswith("test_") and callable(f)]
    bad = 0
    for n, f in items:
        try:
            f()
        except AssertionError as exc:
            bad += 1
            print(f"FAIL {n}: {exc}")
        else:
            print(f"ok   {n}")
    print(f"\n{len(items) - bad}/{len(items)} checks pass")
    return bad


if __name__ == "__main__":
    raise SystemExit(_run_all())
