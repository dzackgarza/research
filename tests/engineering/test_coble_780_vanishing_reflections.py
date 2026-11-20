"""The square-(-2) vectors, the discriminant arrangement, and what is withdrawn.

The first version of lem:d2-vanishing-reflections said the square-(-2) vectors of T_Co
are the +-h + v with v^2 = -4, and concluded Gamma_Co = W(T_Co).  Both were wrong: with
x = ah + v one has x^2 = 2a^2 + v^2 and v^2 in 4Z, so x^2 = -2 forces only that a be odd,
and a = 3 with v^2 = -20 also gives -2 (3h + e - 5f).  And the meridians of the
discriminant arrangement are hyperplanes gamma-perp for gamma in Q that need not have
square -2, so no equality with W(T_Co) follows.

These checks pin the corrected statements and guard that the withdrawn ones do not return.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LA = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

LEMMA = "lem:d2-vanishing-reflections"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_square_minus_two_vectors_are_described_correctly():
    body = _block(LA.read_text(encoding="utf-8"), LEMMA)
    # the correct parametrisation: a odd, v^2 = -2(a^2+1)
    assert "odd" in body
    assert "a^2+1" in body
    assert "E_{10}(2)" in body
    # the false one must be gone
    assert "of square $-4$" not in body


def test_the_arrangement_is_computed_not_asserted():
    text = LA.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    # the lattice reduction: r = t + s, gamma = 2s in Q, gamma^2 = 4(-2-t^2)
    assert "2s" in body or "\\gamma" in body
    assert "@YZZ25, §3.3" in body or "§3.3" in body
    # and the containment, not the equality
    assert "W(T_\\Co)\\subseteq\\Gamma_\\Co" in body


def test_the_withdrawn_equality_cannot_return():
    text = LA.read_text(encoding="utf-8")
    assert "\\Gamma_\\Co=W(T_\\Co)" not in text, "the withdrawn equality is back"
    body = _block(text, LEMMA)
    assert "no identification" in body or "not asserted" in body


def test_the_meridian_step_is_not_overstated():
    text = LA.read_text(encoding="utf-8")
    start = text.index("#" + LEMMA)
    proof = text[start:]
    proof = proof[proof.index("::: {.proof}"):]
    proof = proof[:proof.index("\n:::", 10)]
    # the meridian identification lives in the Dolgachev lemma now
    assert "@lem:d2-monodromy-in-discriminant-kernel" in proof
    # the local-monodromy input is cited on the page by number
    assert "@Voi07, Thm. 3.16" in text


def test_the_arrangement_is_strictly_larger_with_an_explicit_root():
    """Item 7 finished: H_T contains a hyperplane from an isotropic class.

    For an isotropic e in U(2) the vector r = l_1 + e has square -2, is orthogonal to H
    and is not in L, so it is one of the roots defining H_T; its hyperplane is e-perp, and
    e is isotropic.  So H_T is strictly larger than the square-(-2) arrangement, and no
    description of the monodromy by the s_delta alone can be complete."""
    text = LA.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    assert "strict" in body
    assert "isotropic" in body
    assert "\\ell_1" in body or "l_1" in body


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
