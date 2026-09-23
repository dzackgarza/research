r"""Cyclic covers of an affine base, their deck action and their quotient.

The running specimen is the double cover ``z^2 = x^4 - 1`` of the affine line
over the rationals: the affine chart of a genus-one curve, branched at the
four roots of ``x^4 - 1``, with the hyperelliptic involution ``z -> -z`` as
its deck transformation.  Its ramification subscheme is ``V(z)``, its branch
subscheme downstairs is four points, and its quotient by the deck action is
the affine line it covers.  The trivial cover ``z^2 = 1`` is the contrasting
unramified specimen: the deck action is free and there is no branch locus.
"""


from dzack_research.preamble.all import (
    GF,
    QQ,
)
from dzack_research.preamble.categories.schemes.cyclic_covers import CyclicCovers

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_cyclic_covers_and_involutions.sage",
    "live_owner": "tests/schemes/test_cyclic_covers.py",
    "owner_overrides": {
        "test_involution_lifts_of_cyclic_cover": "tests/schemes/test_cyclic_covers_linearization.py",
    },
    "disposition": "reconciled-live-owner",
}


def _hyperelliptic_double_cover():
    r"""``z^2 = x^4 - 1`` over ``QQ``: a genus-one curve branched at four points."""
    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    covers = CyclicCovers(algebra, 2)
    return algebra, x, covers, covers(x**4 - algebra.one())




def test_the_deck_involution_scales_z_and_fixes_the_ramification_subscheme() -> None:
    _algebra, _x, covers, cover = _hyperelliptic_double_cover()
    generator = covers.constant_deck_group().group_generators()[0]
    acted = cover.constant_deck_action()
    involution = acted.action_of(generator)
    z = cover.cover_variable()

    assert cover.deck_root_of_unity() == -QQ.one()
    assert involution.coordinate_algebra_morphism()(z) == -z
    assert involution * involution == acted.categorical_identity_morphism()
    # V(z) is the ramification locus: (zeta - 1) z generates the fixed ideal.
    assert acted.fixed_ideal().contains_ambient_element(z)
    assert not acted.fixed_ideal().contains_ambient_element(cover.coordinate_algebra().one())
    assert acted.action_is_free() is False


def test_the_branch_subscheme_of_the_double_cover_is_four_points() -> None:
    algebra, x, _covers, cover = _hyperelliptic_double_cover()
    branch = cover.branch_subscheme()

    assert cover.relative_dimension() == 1
    assert branch.relative_dimension() == 0
    assert cover.ramification_support_subscheme().relative_dimension() == 0
    assert branch.ambient_scheme() is cover.base_scheme()
    assert branch.defining_ideal_owned() == algebra.ideal(x**4 - algebra.one())
    # k[x]/(x^4 - 1) is free of rank four over the scalars: four branch points.
    assert branch.coordinate_algebra().module_generating_set().cardinality() == 4




def test_degree_three_ramification_retains_the_square_different() -> None:
    finite_line = GF(7).polynomial_ring("x")
    cover = CyclicCovers(finite_line, 3)(finite_line.algebra_generator("x"))
    z = cover.cover_variable()
    ramification_ideal = cover.ramification_subscheme().defining_ideal_owned()

    assert ramification_ideal.contains_ambient_element(z**2)
    assert not ramification_ideal.contains_ambient_element(z)


def test_the_quotient_by_the_deck_action_is_the_base_of_the_cover() -> None:
    algebra, _x, _covers, cover = _hyperelliptic_double_cover()
    quotient_morphism = cover.quotient_morphism()
    action = cover.deck_group_scheme_action().action_morphism()
    product = action.domain()

    assert cover in CyclicCovers(algebra, 2)
    assert cover.coordinate_algebra().algebra_structure_morphism().domain() is algebra
    assert "_preamble_cyclic_branch_section" not in cover.__dict__
    assert "_preamble_cyclic_cover_degree" not in cover.__dict__
    assert "_preamble_deck_group_scheme_action" not in cover.__dict__
    assert cover.invariant_algebra() is algebra
    assert cover.affine_quotient() is (algebra).affine_spectrum(base_ring=algebra)
    assert quotient_morphism.domain() is cover
    assert quotient_morphism.codomain() is cover.affine_quotient()
    # The cover morphism is invariant, which is what makes it the quotient map.
    assert quotient_morphism * action == quotient_morphism * product.projection(1)




def test_the_trivial_cover_is_the_unramified_torsor_with_a_free_deck_action() -> None:
    algebra = QQ.polynomial_ring("x")
    cover = CyclicCovers(algebra, 2)(algebra.one())
    acted = cover.constant_deck_action()
    z = cover.cover_variable()

    assert z**2 == cover.coordinate_algebra().one()
    # z is a unit, so the deck fixed locus is empty and the action is free.
    assert acted.fixed_ideal().contains_ambient_element(cover.coordinate_algebra().one())
    assert acted.action_is_free() is True
    assert cover.is_etale_cover()




