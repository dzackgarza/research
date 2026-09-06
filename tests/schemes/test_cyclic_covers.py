r"""Cyclic covers of an affine base, their deck action and their quotient.

The running specimen is the double cover ``z^2 = x^4 - 1`` of the affine line
over the rationals: the affine chart of a genus-one curve, branched at the
four roots of ``x^4 - 1``, with the hyperelliptic involution ``z -> -z`` as
its deck transformation.  Its ramification subscheme is ``V(z)``, its branch
subscheme downstairs is four points, and its quotient by the deck action is
the affine line it covers.  The trivial cover ``z^2 = 1`` is the contrasting
unramified specimen: the deck action is free and there is no branch locus.
"""

import pytest

from dzack_research.preamble.all import (
    GF,
    PolynomialRing,
    QQ,
    Spec,
)
from dzack_research.preamble.categories.schemes.cyclic_covers import CyclicCovers


def _hyperelliptic_double_cover():
    r"""``z^2 = x^4 - 1`` over ``QQ``: a genus-one curve branched at four points."""
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    covers = CyclicCovers(algebra, 2)
    return algebra, x, covers, covers(x**4 - algebra.one())


def test_the_cover_algebra_is_free_of_rank_two_on_the_powers_of_z() -> None:
    algebra, x, _covers, cover = _hyperelliptic_double_cover()
    cover_algebra = cover.coordinate_algebra()
    z = cover.cover_variable()
    inclusion = cover.invariant_algebra_inclusion()

    assert cover.cover_degree() == 2
    assert cover_algebra.module_generating_set().cardinality() == 2
    assert cover_algebra.module_generator(0) == cover_algebra.one()
    assert cover_algebra.module_generator(1) == z
    # The multiplication, the underlying finite module and the local equation
    # are one construction: z^2 is the branch section, read in the cover.
    assert z**2 == inclusion(x**4 - algebra.one())
    assert cover.branch_section() == x**4 - algebra.one()


def test_the_deck_involution_scales_z_and_fixes_the_ramification_subscheme() -> None:
    _algebra, _x, covers, cover = _hyperelliptic_double_cover()
    generator = covers.deck_group().group_generators().unrank(0)
    involution = cover.action_of(generator)
    z = cover.cover_variable()

    assert cover.deck_root_of_unity() == -QQ.one()
    assert involution.coordinate_algebra_morphism()(z) == -z
    assert involution * involution == cover.categorical_identity_morphism()
    # V(z) is the ramification locus: (zeta - 1) z generates the fixed ideal.
    assert cover.fixed_ideal().contains_ambient_element(z)
    assert not cover.fixed_ideal().contains_ambient_element(cover.coordinate_algebra().one())
    assert cover.action_is_free() is False


def test_the_branch_subscheme_of_the_double_cover_is_four_points() -> None:
    algebra, x, _covers, cover = _hyperelliptic_double_cover()
    branch = cover.branch_subscheme()

    assert branch.ambient_scheme() is cover.base_scheme()
    assert branch.defining_ideal_owned() == algebra.ideal(x**4 - algebra.one())
    # k[x]/(x^4 - 1) is free of rank four over the scalars: four branch points.
    assert branch.coordinate_algebra().module_generating_set().cardinality() == 4


def test_the_quotient_by_the_deck_action_is_the_base_of_the_cover() -> None:
    algebra, _x, covers, cover = _hyperelliptic_double_cover()
    generator = covers.deck_group().group_generators().unrank(0)
    quotient_morphism = cover.quotient_morphism()

    assert cover in CyclicCovers(algebra, 2)
    assert cover.invariant_algebra() is algebra
    assert cover.affine_quotient() is Spec(algebra, base_ring=algebra)
    assert quotient_morphism.domain() is cover
    assert quotient_morphism.codomain() is cover.affine_quotient()
    # The cover morphism is invariant, which is what makes it the quotient map.
    assert quotient_morphism * cover.action_of(generator) == quotient_morphism


def test_the_trivial_cover_is_the_unramified_torsor_with_a_free_deck_action() -> None:
    algebra = PolynomialRing(QQ, "x")
    cover = CyclicCovers(algebra, 2)(algebra.one())
    z = cover.cover_variable()

    assert z**2 == cover.coordinate_algebra().one()
    # z is a unit, so the deck fixed locus is empty and the action is free.
    assert cover.fixed_ideal().contains_ambient_element(cover.coordinate_algebra().one())
    assert cover.action_is_free() is True


def test_a_degree_three_cover_needs_a_primitive_cube_root_of_unity() -> None:
    rational_line = PolynomialRing(QQ, "x")
    with pytest.raises(AssertionError):
        CyclicCovers(rational_line, 3).deck_root_of_unity()

    # 7 = 1 mod 3, so GF(7) holds a primitive cube root of unity.
    finite_line = PolynomialRing(GF(7), "x")
    covers = CyclicCovers(finite_line, 3)
    root = covers.deck_root_of_unity()
    cover = covers(finite_line.algebra_generator("x"))
    z = cover.cover_variable()

    assert root**3 == root.parent().one()
    assert root != root.parent().one()
    assert cover.coordinate_algebra().module_generating_set().cardinality() == 3
    assert z**3 == cover.invariant_algebra_inclusion()(
        finite_line.algebra_generator("x")
    )
