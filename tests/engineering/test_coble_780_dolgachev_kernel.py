"""Red test first: item 16's forward half has a second, independent source.

[@Dol96, Proposition 3.3] states Gamma_M = O(N)^*, where Gamma(M) is the pointwise
stabilizer of M in O(L_K3) and N = M^perp; [@Dol96, Corollary 3.2] states that the
period map is a bijection between marked ample M-polarized K3 surfaces and the open
period domain.  Together they give, for M = <2> + <-2>^10 and N = T_Co, the containment
Gamma_Co subset O(N)^* cap O^+(N) = Otilde^+(T_Co) -- the book's forward inclusion, by a
source independent of the gluing computation.

What the same source cannot give is the reverse inclusion, and the page must say why:
-id acts trivially on the period domain, so the quotient determines the monodromy group
only modulo {+-id}.

This test is RED until that lemma is on the page, citing both numbered statements.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LA = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

LEMMA = "lem:d2-monodromy-in-discriminant-kernel"


def _block(text: str, label: str) -> str:
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_lemma_cites_two_numbered_statements():
    text = LA.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "the second source for the forward inclusion is not on the page"
    body = _block(text, LEMMA)
    assert "@Dol96, Prop. 3.3" in body or "@Dol96, Proposition 3.3" in body
    assert "@Dol96, Cor. 3.2" in body or "@Dol96, Corollary 3.2" in body
    assert "O(N)^*" in body or "\\Orth(N)^*" in body


def test_the_lemma_says_why_the_reverse_is_out_of_reach():
    text = LA.read_text(encoding="utf-8")
    assert "#" + LEMMA in text, "the lemma is not on the page"
    body = _block(text, LEMMA)
    assert "-\\id" in body
    assert "kernel" in body or "trivially" in body


def test_the_forward_inclusion_cites_it():
    text = LA.read_text(encoding="utf-8")
    proof = text[text.index("#thm:gamma-co-is-stable"):]
    proof = proof[proof.index("::: {.proof}"):]
    proof = proof[:proof.index("\n:::", 10)]
    assert "@" + LEMMA in proof, "clause 1 must cite the independent source"


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
