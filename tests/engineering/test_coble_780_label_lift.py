"""Red test first: item 4, the path from s to sigma(s).

The review at 2c899f1da6 left one point of the labelling lemma open: the page used a
constant path to represent every sigma in S_10, which is impossible unless sigma s = s.
What the argument needs, and what connectivity of B supplies (lem:d2-incidence-connected),
is a path of B from s to sigma s for every sigma.

LEMMA (to be proved).  Let B = V/PGL_3 be the labelled base, a connected complex
analytic space on which S_10 acts, and let Bbar = [B/S_10] be the quotient stack.  Then

  (1) for every sigma in S_10 there is a path of B from s to sigma s;
  (2) the resulting homomorphism pi_1(Bbar, [s]) -> S_10 is surjective with kernel the
      image of pi_1(B, s), so 1 -> pi_1(B,s) -> pi_1(Bbar,[s]) -> S_10 -> 1 is exact.

This test is RED until the lemma is on the page and the labelling lemma cites it.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
MC = ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md"

LEMMA = "lem:d2-label-lift"


def _block(text: str, label: str) -> str:
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_lift_lemma_exists_with_the_two_clauses():
    text = MC.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "item 4 is not a lemma of its own"
    body = _block(text, LEMMA)
    assert "S_{10}" in body
    assert "kernel" in body or "ker" in body


def test_the_lift_uses_connectivity_and_not_a_constant_path():
    text = MC.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "the lift lemma is not on the page"
    start = text.index("#" + LEMMA)
    proof = text[start:]
    proof = proof[proof.index("::: {.proof}"):]
    proof = proof[:proof.index("\n:::", proof.index("::: {.proof}") + 10)]
    assert "@lem:d2-incidence-connected" in proof, "the path must come from connectivity"


def test_no_constant_path_represents_a_nontrivial_label():
    text = MC.read_text(encoding="utf-8")
    assert "the constant path at $s$ representing" not in text
    # and the labelling lemma hands the path question to the lift lemma
    head = text.index("::: {.lemma #lem:d2-labelling-cover")
    after = text.index("\n::: ", head)
    cover_proof = text[after:]
    cover_proof = cover_proof[cover_proof.index("::: {.proof}"):]
    cover_proof = cover_proof[:cover_proof.index("\n:::", 10)]
    assert "@" + LEMMA in cover_proof, "the labelling cover must cite the lift lemma"


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
