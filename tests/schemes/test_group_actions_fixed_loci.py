r"""Affine group actions and their scheme-theoretic fixed loci."""

import pytest

from dzack_research.preamble.all import (
    QQ,
    AffineGSchemes,
    AffineSchemes,
    GObjects,
    Groups,
    Schemes,
    Algebras,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_fixed_loci.sage",
    "live_owner": "tests/schemes/test_group_actions_fixed_loci.py",
    "disposition": "reconciled-live-owner",
}


def _coordinate_swap_action() -> tuple:
    group = Groups.C(2)
    algebra = QQ.polynomial_ring(("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = (algebra).affine_spectrum()
    swap = Algebras(QQ).Associative().Unital().Commutative().spectrum()(algebra.Mor(algebra)({"x": y, "y": x}))
    identity = scheme.categorical_identity_morphism()
    acted = AffineGSchemes(group, QQ)(
        scheme,
        lambda element: identity if element == group.one() else swap,
    )
    return group, algebra, x, y, scheme, acted


def test_affine_scheme_action_is_a_fresh_g_object_with_represented_pullbacks() -> None:
    group, algebra, x, y, scheme, acted = _coordinate_swap_action()
    generator = group.group_generators()[0]
    pullback = acted.action_of(generator).coordinate_algebra_morphism()

    assert acted is not scheme
    assert acted.unacted_scheme() is scheme
    assert acted in GObjects(group, Schemes(QQ))
    assert acted in AffineSchemes(QQ)
    assert acted.action_of(generator).domain() is acted
    assert acted.action_of(generator).codomain() is acted
    assert pullback.domain() is algebra
    assert pullback.codomain() is algebra
    assert pullback(x) == y
    assert pullback(y) == x
    assert (
        acted.action_of(generator) * acted.action_of(generator)
        == acted.categorical_identity_morphism()
    )


def test_generic_gobjects_constructor_does_not_construct_affine_actions() -> None:
    group = Groups.C(2)
    scheme = (QQ.polynomial_ring("x")).affine_spectrum()
    identity = scheme.categorical_identity_morphism()

    with pytest.raises(TypeError):
        GObjects(group, Schemes(QQ))(scheme, lambda _element: identity)


def test_coordinate_swap_fixed_subscheme_is_the_diagonal_equalizer() -> None:
    group, algebra, x, y, _scheme, acted = _coordinate_swap_action()
    generator = group.group_generators()[0]

    assert acted.fixed_ideal() == algebra.ideal(x - y)

    fixed = acted.fixed_subscheme()
    inclusion = fixed.inclusion()
    quotient = inclusion.coordinate_algebra_morphism()

    assert fixed.inclusion().codomain() is acted
    assert inclusion.domain() is fixed
    assert inclusion.codomain() is acted
    assert quotient(x) == quotient(y)
    assert acted.action_of(generator) * inclusion == inclusion


def test_affine_scheme_action_rejects_generator_images_that_violate_relators() -> None:
    group = Groups.C(2)
    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    dilation = Algebras(QQ).Associative().Unital().Commutative().spectrum()(algebra.Mor(algebra)({"x": x + x}))
    identity = scheme.categorical_identity_morphism()
    acted = AffineGSchemes(group, QQ)(
        scheme,
        lambda element: identity if element == group.one() else dilation,
    )

    with pytest.raises(AssertionError, match="define no left action"):
        acted.action()


def test_gobjects_of_schemes_has_a_trivial_affine_specimen() -> None:
    group = Groups.C(2)
    category = GObjects(group, Schemes(QQ))
    acted = category.an_object()
    algebra = acted.coordinate_algebra()

    assert acted in category
    assert acted in AffineSchemes(QQ)
    assert acted.fixed_ideal() == algebra.ideal(algebra.zero())


def test_projective_product_sign_and_swap_fixed_loci_keep_archive_dimensions() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x0", "x1"))
    product = line.product_with(line)
    x0, x1 = line.coordinate_ring().gens()
    sign = line.projective_morphism_from_coordinates(line, (x0, -x1))

    diagonal_sign = product.from_product_cone(
        (sign * product.projection(0), sign * product.projection(1))
    )
    fixed_sign = diagonal_sign.fixed_subscheme()
    assert fixed_sign.dimension() == 0
    assert len(fixed_sign.rational_points()) == 4

    factor_swap = product.from_product_cone(
        (product.projection(1), product.projection(0))
    )
    fixed_swap = factor_swap.fixed_subscheme()
    assert fixed_swap.dimension() == 1
    assert factor_swap * factor_swap == product.categorical_identity_morphism()
