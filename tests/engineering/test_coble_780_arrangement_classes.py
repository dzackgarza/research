"""Red test first: which classes gamma cut the discriminant, and which can matter.

lem:d2-vanishing-reflections shows H_T is strictly larger than the square-(-2)
arrangement (the isotropic class e-perp).  This lemma classifies the gamma that occur
(gamma = 2s with lambda = 2t in L and lambda^2 + gamma^2 = -8) and uses the Hodge index
theorem on the orthogonal complement of the ample class H to decide which of them can
carry monodromy of the family: those with gamma^2 >= 0 cannot, since every algebraic
gamma in Q is orthogonal to the ample H and therefore has gamma^2 < 0.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LA = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

LEMMA = "lem:d2-arrangement-classes"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_classes_are_classified():
    body = _block(LA.read_text(encoding="utf-8"), LEMMA)
    assert "\\sum_i n_i^2" in body or "\\Sigma" in body
    assert "-8" in body


def test_hodge_index_decides_which_matter():
    text = LA.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    assert "Hodge index" in body or "negative definite" in body
    assert "@Huy05, Ch. 3" in body or "@Voi07" in body
    assert "ample" in body


def test_the_generated_subgroup_stays_in_the_stable_group():
    text = LA.read_text(encoding="utf-8")
    body = _block(text, LEMMA)
    assert "W(T_\\Co)" in body
    assert "\\widetilde\\Orth^+(T_\\Co)" in body


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
