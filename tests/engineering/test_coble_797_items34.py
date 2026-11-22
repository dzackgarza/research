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
    assert "injectivity on objects" in body.lower()
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
    assert "coble-monodromy-equality" in body


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


FINAL = "conj:gamma-co-orbifold-equality"
IOTA = "rmk:is-iota-a-loop"


def test_the_equality_is_a_conjecture_and_the_inclusion_is_what_is_proved():
    body = _block(MC.read_text(encoding="utf-8"), FINAL)
    assert "\\Gamma_\\Co=\\widetilde\\Orth^+(T_\\Co)" in body
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + FINAL):]
    # what is proved, the four findings, and the conditional assembly are all stated
    for need in ["@thm:gamma-co-is-stable(1)", "@conj:gamma-co-stable",
                 "does not", "Review findings recorded here"]:
        assert need in tail[:8000], need


def test_iota_is_settled_as_isotropy_not_loop():
    body = _block(MC.read_text(encoding="utf-8"), IOTA)
    assert "@thm:sign-is-isotropy" in body
    assert "@thm:no-loop-carries-the-sign" in body
    # the loop reading is stated as smaller, by a quotient, and the transfer is flagged
    assert "isotropy" in body and "loop" in body
    assert "conditional" in body


PSEUDO_AMPLE = "prop:d2a-family-is-pseudo-ample"
SIGN_LOOP = "rmk:where-the-sign-is-a-loop"


def test_the_family_is_pseudo_ample_so_dol96_thm_3_1_applies():
    body = _block(MC.read_text(encoding="utf-8"), PSEUDO_AMPLE)
    assert "nef and big" in body
    assert "pseudo-ample" in body
    assert "@Dol96, Thm. 3.1" in body
    assert "chamber" in body


def test_the_sign_reconciliation_names_both_moduli_problems():
    body = _block(MC.read_text(encoding="utf-8"), SIGN_LOOP)
    assert "@thm:coble-block-sign-in-w" in body
    assert "@lem:d2-vanishing-reflections(4)" in body
    assert "@thm:no-loop-carries-the-sign" in body
    assert "two moduli problems" in body or "different moduli problems" in body


COBLE_LOCUS = "prop:the-coble-locus-in-the-period-domain"


def test_the_bad_locus_is_closed_and_the_coble_locus_is_its_complement():
    body = _block(MC.read_text(encoding="utf-8"), COBLE_LOCUS)
    assert "locally finite" in body
    assert "closed analytic subset" in body
    # the characterization, in both directions
    assert "labelled Coble cover" in body
    assert "not*" in body or "not" in body
    # and the honest note that it is countable, closed only by local finiteness
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + COBLE_LOCUS):]
    assert "local finiteness is doing the work" in tail


TWO_ARR = "rmk:two-arrangements-two-bases"


def test_the_two_arrangements_are_distinguished():
    body = _block(MC.read_text(encoding="utf-8"), TWO_ARR)
    # the Coble locus uses the (-2)-classes of T_Co; the base's arrangement is larger
    assert "(-2)" in body and "larger" in body
    assert "not" in body
    # the closedness mechanism is proper discontinuity
    assert "properly discontinuously" in body
    assert "locally finite" in body


TWO_STEPS = "rmk:the-two-steps-and-where-they-fail"


SURJECTIVITY = "thm:coble-period-surjectivity"


def test_step_one_is_the_surjectivity_theorem_and_step_two_is_open():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, TWO_STEPS)
    # step 1 is the surjectivity theorem, for the functor as it is defined
    assert "@thm:coble-period-surjectivity" in body
    assert "@def:coble-moduli-functor" in body
    # what step 1 does not give is the plane model, and the remark says so
    assert "What step 1 does not give" in body
    assert "ten nodes of an irreducible sextic" in body
    # the second step, the special-member isotropy, is not closed
    assert "special member" in body
    assert "is not closed" in body


def test_the_surjectivity_theorem_states_the_quotient():
    body = _block(MC.read_text(encoding="utf-8"), SURJECTIVITY)
    # the period set, the involution and the three clauses on the quotient
    assert "\\Omega\\sm Z_\\Omega" in body
    assert "\\sigma\\definedas\\id_M\\oplus(-\\id_{T_\\Co})" in body
    assert "one smooth rational curve" in body
    assert "\\abs{-K_S}=\\emptyset" in body
    assert "\\abs{-2K_S}=\\theset{C}" in body
    # the converse, so that the period set is exactly the complement
    assert "Necessity" in body


PLANE_MODEL = "rmk:which-coble-surfaces-have-a-plane-model"


def test_the_subclass_with_a_plane_model_is_named():
    body = _block(MC.read_text(encoding="utf-8"), PLANE_MODEL)
    assert "@DZ99, Rem. 2.9" in body
    # Prop. 6.4(1) is read exactly: its conclusion is about log Enriques resolutions
    assert "Prop. 6.4(1)" in body
    assert "log Enriques" in body
    assert "classical" in body
    assert "not" in body
    # the functor's class is the single-smooth-curve class; every period off Z gives an
    # object of it, and whether each object has a plane model is left undecided
    assert "single smooth curve" in body
    assert "@thm:coble-period-surjectivity" in body
    assert "is not decided here" in body


LABELLABLE = "lem:every-object-of-the-functor-is-labellable"
LABELLED_EQ = "thm:gamma-co-labelled-equality"


def test_every_object_is_labellable():
    body = _block(MC.read_text(encoding="utf-8"), LABELLABLE)
    assert "invariant lattice" in body
    assert "marking" in body
    # the connectedness hypothesis and the n > 1 counterexample are in the statement
    assert "connected" in body
    assert "10+n" in body or "10 + n" in body
    # the count that fixes the rank is in the proof, not the statement
    text = MC.read_text(encoding="utf-8")
    proof = text[text.index("#" + LABELLABLE):]
    assert "rank $11$" in proof[:2500] and ("Nikulin" in proof[:2500] or "@Nik80" in proof[:2500])


def test_the_labelled_equality_and_its_hypothesis():
    body = _block(MC.read_text(encoding="utf-8"), LABELLED_EQ)
    assert "isotropy" in body
    assert "\\widetilde\\Orth^+(T_\\Co)" in body
    # the hypotheses are in the statement, and the generic-to-global inference is withdrawn
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + LABELLED_EQ):]
    assert "gen" in body
    assert "not* a computation of the global group" in tail or "not a computation" in tail


SURJ = "prop:the-generic-locus-sees-the-whole-group"
SPEC = "lem:the-special-isotropy-locus-is-proper"


def test_the_generic_group_is_the_global_group():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, SURJ)
    assert "onto" in body or "onto" in text[text.index("#" + SURJ):text.index("#" + SURJ) + 4000]
    tail = text[text.index("#" + SURJ):]
    # the citation and the S^1 check are in the proof and the trailing paragraph
    assert "SGA 1" in tail[:4000]
    assert "S^1" in tail[:6000] and "codimension $0$" in tail[:6000]
    assert "Gamma_\\Co" in tail[:2000]


def test_the_special_locus_is_proper_and_closed():
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + SPEC):]
    assert "properly discontinuously" in tail[:3000]
    assert "positive codimension" in tail[:3000]


ASSEMBLED = "thm:gamma-co-is-the-stack-monodromy"


def test_the_assembled_theorem_lists_every_input_with_its_status():
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + ASSEMBLED):]
    # the ledger exists and marks the two owed inputs
    assert "Every input, with its status" in tail[:6000]
    assert "owed" in tail[:6000]
    # the SGA 1 statement is kept exact: isomorphism at codimension two, surjectivity used
    assert "SGA 1" in tail[:8000]
    assert "isomorphism" in tail[:8000]


CHAMBER_INJ = "lem:pseudo-ample-injectivity-from-the-chamber"


def test_injectivity_comes_from_the_chamber_not_from_an_ample_class():
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + CHAMBER_INJ):]
    assert "chamber replaces the ample class" in tail[:1200]
    assert "BHPV04, Ch. VIII, Thm. 11.1" in tail[:4000]
    # and the ledger no longer carries the chamber item as owed
    led = text[text.index("#thm:gamma-co-is-the-stack-monodromy"):]
    assert "only item still owed" in led[:6000]


MOVED = "prop:coble-moved-minus-two-class"
FIVE_CLAUSES = "rmk:coble-moduli-functor-five-clauses"


def test_the_picard_general_locus_is_the_complement_of_all_the_heegner_divisors():
    body = _block(MC.read_text(encoding="utf-8"), MOVED)
    # clause 1 names the locus as the complement of the (-2d)-divisors, not of Z alone
    assert "\\bigcup_{d\\ge1}\\mch_{-2d}" in body
    assert "@def:heegner-divisor" in body
    # and both directions of the equivalence, with the negative-square step in the proof
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + MOVED):]
    proof = tail[tail.index("\\begin") if "\\begin" in tail else 0:]
    for need in ["positive index $2$", "U(2)", "primitive", "locally finite"]:
        assert need in proof[:9000], need


def test_a_minus_two_class_is_moved_off_the_minus_two_divisor():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, MOVED)
    # the counterexample: a square -4 class of T_Co, and the square -2 class it makes with e_0
    assert "\\delta^2=-4" in body
    assert "e_0+\\delta" in body and "e_0-\\delta" in body
    # the existence is by the Baire category theorem on one hyperplane, not by a computation
    tail = text[text.index("#" + MOVED):]
    assert "Baire" in tail[:9000]
    assert "@cons:coble-involution" in tail[:9000]


TOR_QUOTED = re.compile(r"every reflection in a \$\(-2\)\$-class of \$\\Pic\(X'\)\$ commutes")
PAIRS = "thm:coble-torelli-for-pairs"


def test_the_refuted_sentence_is_gone_and_the_case_split_is_a_remark():
    text = MC.read_text(encoding="utf-8")
    # the withdrawn justification asserted commutation for every (-2)-class of Pic(X'),
    # which prop:coble-moved-minus-two-class(2) refutes off the Picard-general locus
    assert not TOR_QUOTED.search(text), TOR_QUOTED.search(text).group(0)
    body = _block(text, FIVE_CLAUSES)
    # what stands instead: the unconditional Torelli step, and the two cases as remarks
    assert "@thm:coble-torelli-for-pairs" in body
    assert "The Torelli step is settled." in body
    assert "What the case split added, and why it is no longer needed." in body
    assert "@prop:coble-moved-minus-two-class(2)" in body
    # and the universal property is a paragraph of its own, proved
    assert "\n   *The universal property.*" in body
    assert "5. **Coarse space.** **Proved**" in body


def test_torelli_for_pairs_is_stated_on_the_whole_coble_locus():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, PAIRS)
    # the two clauses: the isomorphism of pairs with its correction element, and bijectivity
    assert "\\varphi\\iota=\\iota'\\varphi" in body
    assert "u\\varphi" in body
    assert "on the image of $\\bD(T_\\Co)\\sm Z$" in body
    # the restriction to Picard-general periods must not appear in the statement
    assert "Picard" not in body, [w for w in body.split(".") if "Picard" in w][:2]
    # the number of the block is the one the remark cites
    assert "@thm:coble-torelli-for-pairs" in _block(text, FIVE_CLAUSES)


def test_torelli_for_pairs_quotes_its_numbered_inputs():
    text = MC.read_text(encoding="utf-8")
    tail = text[text.index("#" + PAIRS):]
    proof = tail[:14000]
    # fundamental domain, simple transitivity, Torelli, and the sign handled by -id
    assert "@PS24, Proposition 19.1.3(2)" in proof
    assert "@PS24, Proposition 17.2.5(3)" in proof
    assert "acts simply transitively on root bases and on Weyl chambers" in proof
    assert "@PS24, Theorem 19.2.2" in proof
    assert "-\\id\\in\\Gamma_\\rho" in proof
    # the conjugation computation is on the page, not only in a report
    assert "(\\iota' u\\iota')\\varphi(\\mathcal A_X)" in proof


HOLOMORPHY = re.compile(r"what is missing is that this map is holomorphic")


def test_the_withdrawn_diagnosis_of_the_universal_property_is_gone():
    text = MC.read_text(encoding="utf-8")
    # the false diagnosis, withdrawn twice: first that the analyticity was missing,
    # then that the descent fails at all
    assert not HOLOMORPHY.search(text), HOLOMORPHY.search(text).group(0)
    assert "What fails is the descent for *families*" not in text
    body = _block(text, FIVE_CLAUSES)
    # what stands: the induced set map is holomorphic, and the descent is proved
    assert "that map is holomorphic" in body
    assert "automatically constant on isomorphism classes" in body


def test_the_universal_property_is_proved_by_descent_to_a_manifold_chart():
    body = _block(MC.read_text(encoding="utf-8"), FIVE_CLAUSES)
    # the two parts of a coarse space, and where each comes from
    assert "@thm:coble-torelli-for-pairs(2) gives for $F=F_S$" in body
    # the descent: equality of morphisms is not taken from agreement at points
    assert "agreement at every point of $Y$ gives equality only when $Y$ is reduced" in body
    # the chart is the universal deformation over its smooth base, quoted from the page
    assert "is the pullback of $\\mathcal Z$ along $h$" in body
    assert "@thm:coble-classical-substack-is-open-dense-and-proper" in body
    # and the conclusion
    assert "So $g=f\\circ p$ on every object, and $F_S$ is a coarse space of $\\mcM_\\Co$." in body


def test_the_period_chart_families_are_not_the_atlas_and_clause_three_is_settled():
    """Clause 5 says the period-chart families are not an atlas; clause 3 is proved.

    An earlier form of clause 5 claimed the disjoint union of those families was a
    smooth atlas while clause 3 said no atlas was exhibited.  The two are now
    consistent: the families are essentially surjective and not a covering, and the
    atlas is the moduli of marked covers.
    """
    text = MC.read_text(encoding="utf-8")
    body = _block(text, FIVE_CLAUSES)
    assert "is therefore a smooth atlas" not in text
    assert "It gives essential surjectivity and only that." in body
    assert "They are not an atlas" in body
    assert "3. **Algebraicity.** **Proved**" in body
    # the coarse-space verdict is untouched by any of this
    assert "5. **Coarse space.** **Proved**" in body


ISOM = "thm:coble-isom-sheaf-representable"
ATLAS = "thm:coble-atlas"


def test_the_isomorphism_sheaf_is_representable_and_no_locus_is_restricted():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, ISOM)
    # the two families, the claim, and the reduction to the K3 covers
    assert "is representable by a complex space over $T$" in body
    proof = text[text.index("#" + ISOM):text.index("#" + ATLAS)]
    assert "@PS24, Lemma 19.2.4" in proof          # faithfulness: the action is injective
    assert "@PS24, Theorem 19.3.1" in proof        # the fine moduli of marked K3 surfaces
    assert "No restriction of the locus" in proof  # no classical/unnodal/Picard-general hypothesis


def test_the_atlas_is_the_marked_moduli_and_algebraicity_follows():
    text = MC.read_text(encoding="utf-8")
    body = _block(text, ATLAS)
    assert "smooth and essentially surjective" in body
    assert "its diagonal is representable by @thm:coble-isom-sheaf-representable" in body
    proof = text[text.index("#" + ATLAS):]
    assert "torsor over" in proof[:3000] and "Gamma_" in proof[:3000]
    # clause 3 no longer calls algebraicity open, and clause 4 is the first open one
    five = _block(text, FIVE_CLAUSES)
    assert "3. **Algebraicity.** **Proved**" in five
    assert "Clause 4 is the first open one." in five
    # and the period-chart families are explicitly not the atlas
    assert "They are not an atlas" in five
