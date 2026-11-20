"""The two statements of research#797, items 3 and 4, and the guard on their form.

Item 3 asks for the quotient presentation of the S_Co-polarized moduli stack with its
hypotheses checked; item 4 for the monodromy exact sequence with the covering it
defines.  Both pins below are on the statements themselves, not on the implementation
of any computation, together with one guard for the failure mode that bit this page:
a doubled control sequence inside math, which pandoc keeps verbatim and TeX then
fails to convert.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
MC = ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md"

QUOTIENT = "prop:coble-quotient-presentation"
MONODROMY = "thm:monodromy-exact-sequence"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_quotient_presentation_is_stated_with_its_hypotheses():
    body = _block(MC.read_text(encoding="utf-8"), QUOTIENT)
    # condition (U) is by [@Dol96, Prop. 5.1], and its disjunct at t = 10 is the one used
    assert "@Dol96, Prop. 5.1" in body
    assert "or** $t\\leq10$" in body or "**or** $t\\leq10$" in body
    assert "U(2)" in body
    # the presentation itself, and the group it is by
    assert "\\widetilde\\Orth^+(T_\\Co)" in body
    # the non-emptiness is NOT claimed from the proposition whose t <= 9 fails
    assert "@Dol96, Cor. 5.2" in body


def test_the_monodromy_sequence_is_stated_with_its_cover():
    body = _block(MC.read_text(encoding="utf-8"), MONODROMY)
    assert "K_\\bL" in body and "\\operatorname{Mon}(\\bL)" in body
    assert "1\\too K_\\bL\\too\\pi_1(X,x)\\too\\operatorname{Mon}(\\bL)\\too1" in body
    assert "Theorem 18.19" in body and "Corollary 18.20" in body
    assert "Definition 18.10" in body
    assert "deck transformations" in body


def test_no_doubled_control_sequence_in_either_block():
    text = MC.read_text(encoding="utf-8")
    for label in (QUOTIENT, MONODROMY):
        body = _block(text, label)
        assert not re.search(r"\\\\+[A-Za-z]+", body), label


TORELLI = "prop:torelli-for-the-coble-lattice"
DEFORMATIONS = "lem:coble-deformations-are-not-all-of-Def-S"


def test_item5_states_the_route_that_supplies_torelli():
    body = _block(MC.read_text(encoding="utf-8"), TORELLI)
    # route (b) is DK13 Prop. 3.2, and the transfer is section 5 there
    assert "@DK13, Prop. 3.2" in body and "@DK13, §5" in body
    # route (a) is recorded as having no object, with the Heegner-divisor reason
    assert "Heegner" in body
    # what is left open is named
    assert "surjectivity" in body


def test_item5_deformations_are_9_into_12_and_not_onto():
    body = _block(MC.read_text(encoding="utf-8"), DEFORMATIONS)
    assert "h^1(S,\\Theta_S)=12" in body
    assert "9" in body and "12" in body
    assert "neither" in body


PERIOD_STACK = "thm:coble-period-map-of-the-stack"
FROM_UNIVERSAL = "prop:gamma-co-from-the-universal-family"


def test_the_transfer_is_proved_at_the_level_of_the_stack():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, PERIOD_STACK)
    # the four clauses: defined, injective on labelled objects, local Torelli, descent
    assert "injectivity on labelled objects" in body.lower()
    assert "Local Torelli" in body or "local Torelli" in body
    assert "fully faithful" in body
    # the two numbered inputs that do the work
    proof = text[text.index("#" + PERIOD_STACK):]
    assert "@BHPV04, Ch. VIII, Thm. 11.1" in proof
    assert "@Dol96, §3" in proof


def test_item6_says_which_group_a_restriction_gives():
    body = _block(MC.read_text(encoding="utf-8"), FROM_UNIVERSAL)
    assert "@lem:coble-family-base-change" in body
    assert "Stab" in body
    assert "not* thereby $\\Gamma_\\Co$" in body or "not" in body
    assert "@qst:coble-monodromy-equality" in body


MAPS = "prop:coble-enriques-maps-and-the-vhs"


def test_item6_the_two_maps_and_what_each_does_to_the_local_system():
    body = _block(MC.read_text(encoding="utf-8"), MAPS)
    # the Enriques map is a normalization of a Heegner divisor, not an open immersion
    assert "@thm:normalization" in body and "Heegner" in body
    assert "normalization" in body
    # the meridian acts trivially on the hyperplane, so the restriction gives a bound
    assert "@lem:d2-vanishing-reflections(3)" in body
    assert "upper bound" in body
    # the K3 map is a quotient and does not move the local system
    assert "sub-local-system" in body


MONODROMY_IS_G = "prop:coble-monodromy-is-the-marking-group"


EVERY_AMPLE = "lem:every-ample-m-polarized-k3-is-a-coble-cover"


def test_reconstruction_of_the_coble_cover_from_the_period():
    body = _block(MC.read_text(encoding="utf-8"), EVERY_AMPLE)
    assert "rank $11$" in body
    assert "Coble surface" in body
    # the count that fixes the rank is in the proof, not the statement
    text = MC.read_text(encoding="utf-8")
    proof = text[text.index("#" + EVERY_AMPLE):]
    assert "Lefschetz" in proof[:4000]


def test_the_monodromy_of_the_labelled_stack_is_the_marking_group():
    body = _block(MC.read_text(encoding="utf-8"), MONODROMY_IS_G)
    assert "G$-torsor" in body or "torsor" in body
    assert "1\\too\\pi_1(U)" in body or "pi_1(U)" in body
    assert "\\Orth^+(T_\\Co)" in body
    # the orbifold reading is asserted, and the loop reading is separated from it
    assert "orbifold" in body
    assert "@thm:no-loop-carries-the-sign" in body or "index-two" in body
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + MONODROMY_IS_G):]
    assert "What this settles" in tail and "@lem:every-ample-m-polarized-k3-is-a-coble-cover" in tail
