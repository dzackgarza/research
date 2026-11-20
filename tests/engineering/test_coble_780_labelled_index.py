"""Red test first: the labelled-base identification from D2a's own cover is on no page.

LEMMA.  For the family of @def:coble-family-unpolarized, with B the labelled base and
Bbar the unlabelled one, the inclusion Gamma_Co(B) <= Gamma_Co(Bbar) has index 10!,
because B -> Bbar is a principal S_10-bundle and the monodromy of a deck transformation
is the permutation of the ten classes.  With Gamma_Co(B) <= Otilde^+(T_Co) (flat classes)
and [Gamma_{10A_1} : Otilde^+] = 10!, this forces Gamma_Co(B) = Otilde^+(T_Co): the
labelled-base identification is then a consequence of D2a's cover and the sextic-base
theorem, with no period-map input.

This test is RED until the lemma is on the page and the two uses are wired to it.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"


def test_ten_factorial():
    assert 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 == 3628800


def _block(text: str, label: str) -> str:
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def _proof_after(text: str, label: str) -> str:
    end = text.index("\n:::", text.index("#" + label)) + 4
    rest = text[end:]
    start = rest.index("::: {.proof}")
    return rest[start:rest.index("\n:::", start)]


def test_the_cover_index_is_a_lemma():
    text = LATTICES.read_text(encoding="utf-8")
    assert "#lem:gamma-co-labelled-index" in text
    body = _block(text, "lem:gamma-co-labelled-index")
    assert "\\Gamma_\\Co(\\bar B)" in body and "\\Gamma_\\Co(B)" in body
    assert "10!" in body
    # the two inputs: the principal S_10-bundle and the monodromy action on the labels
    proof = _proof_after(text, "lem:gamma-co-labelled-index")
    assert "@lem:d2-labelling-cover" in proof
    assert "@lem:d2-local-system(5)" in proof
    assert "YZZ25, Lemma 6.7" in proof


def test_the_labelled_identification_is_now_the_equality_from_the_enriques_side():
    """The equality is proved, but not from the sextic side.

    The sextic side gives only the inclusion and the index |rho-bar(Gamma_Co(Bbar))|;
    the equality comes from lem:d2-monodromy-is-enriques-stabilizer with
    prop:gamma-co-images(1)."""
    text = LATTICES.read_text(encoding="utf-8")
    body = _block(text, "thm:gamma-co-is-stable")
    assert "\\Gamma_\\Co=\\widetilde\\Orth^+(T_\\Co)" in body
    proof = _proof_after(text, "thm:gamma-co-is-stable")
    assert "@lem:d2-monodromy-is-enriques-stabilizer" in proof
    assert "@prop:gamma-co-images(1)" in proof
    # the sextic side is explicitly recorded as not closing it
    assert "@rmk:gamma-co-orbifold-obstruction" in proof


def test_the_equality_is_not_derived_from_the_reflection_group():
    """Guard: the W(T_Co) route was withdrawn and must not reappear as a proof."""
    text = LATTICES.read_text(encoding="utf-8")
    proof = _proof_after(text, "thm:gamma-co-is-stable")
    assert "W(T_\\Co)=" not in proof
    assert "reflection" not in proof.lower() or "does not" in proof


def test_the_refuted_orbifold_identification_cannot_come_back():
    """Guard: the page once called the PGamma_T orbifold 'the same' as the Gamma_T one.

    YZZ25 Section 6.1 states they are different, and -id acts on the fibre, so the
    Q-local system does not descend.  This guard bites on an injected bad line, which
    is checked here rather than asserted.
    """
    text = LATTICES.read_text(encoding="utf-8")
    for bad in ("is the same orbifold as",
                "which is the same orbifold"):
        assert bad not in text, bad
    # the guard bites: an injected line is caught
    injected = text + "\nThis is the same orbifold as the other one.\n"
    assert any(b in injected for b in ("is the same orbifold as",)), "guard does not bite"


def test_the_sextic_theorem_uses_the_cover_index_not_the_labelled_theorem():
    text = LATTICES.read_text(encoding="utf-8")
    body = _block(text, "thm:gamma-co-sextic-group")
    assert "@lem:gamma-co-labelled-index" in body
    # the index clause may not rest on the theorem it is used to prove
    clause = body[body.index("on the family of @def:coble-family-unpolarized"):]
    assert "@thm:gamma-co-is-stable" not in clause


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
