"""Red test first: Gamma_Co is the image of the Enriques divisor stabilizer.

Route.  The Coble locus is the (-2)-Heegner divisor delta-perp of the Enriques period
domain [@DK13, Prop. 3.2 and the sentence after it], and T_Co = delta-perp cap T_En
(@def:gamma-co-groups).  The monodromy of a local system restricted to a Heegner divisor
is the image of the setwise stabilizer of the divisor: a loop of the divisor's image lifts
to a path inside the divisor, hence to an element preserving it, and conversely an element
of the stabilizer is realized by a path inside the divisor that avoids the other Heegner
divisors, whose union is a proper closed analytic subset.  With
R_{Gamma_En} = Otilde^+(T_Co) (@prop:gamma-co-images(1)) this gives Gamma_Co = Otilde^+.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LA = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

LEMMA = "lem:d2-monodromy-is-enriques-stabilizer"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_lemma_states_both_inclusions():
    body = _block(LA.read_text(encoding="utf-8"), LEMMA)
    assert "Stab" in body
    assert "@prop:gamma-co-images" in body


def test_the_reverse_inclusion_uses_the_complement_of_the_other_divisors():
    text = LA.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "the lemma is not on the page"
    start = text.index("#" + LEMMA)
    proof = text[start:]
    proof = proof[proof.index("::: {.proof}"):]
    proof = proof[:proof.index("\n:::", 10)]
    assert "closed analytic" in proof or "proper closed" in proof
    assert "simply connected" in proof or "connected" in proof


def test_the_coble_locus_is_cited_by_number():
    body = _block(LA.read_text(encoding="utf-8"), LEMMA)
    assert "@DK13, Prop. 3.2" in body
    assert "@def:gamma-co-groups" in body


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
