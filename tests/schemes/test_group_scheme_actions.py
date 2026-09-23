r"""Affine group schemes and their scheme-theoretic actions."""

import pytest

from dzack_research.preamble.all import (
    QQ,
    AffineGroupSchemeActions,
    AffineGroupSchemes,
    AffineSpaces,
    Grp,
    Schemes,
)
from dzack_research.preamble.categories.schemes.schemes import (
    _affine_morphism_from_pullback,
)


def _mu_two_scaling_action():
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)
    line = AffineSpaces(QQ)(1, names=("x",))
    line_algebra = line.coordinate_algebra()
    x = line_algebra.algebra_generator("x")
    product = line.scheme_category().product((mu_two.scheme(), line))
    product_algebra = product.coordinate_algebra()
    group_pullback = product.projection(0).coordinate_algebra_morphism()
    point_pullback = product.projection(1).coordinate_algebra_morphism()
    u = mu_two.scheme().coordinate_algebra().algebra_generator("u")
    action_pullback = line_algebra.Mor(product_algebra)(
        {"x": group_pullback(u) * point_pullback(x)}
    )
    action_morphism = _affine_morphism_from_pullback(
        product,
        line,
        action_pullback,
    )
    acted = AffineGroupSchemeActions(mu_two)(line, action_morphism)
    return mu_two, line, x, acted


def test_mu_two_is_a_group_scheme_not_an_abstract_group() -> None:
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)

    assert mu_two in AffineGroupSchemes(QQ)
    assert mu_two.category().is_subcategory(AffineGroupSchemes(QQ))
    assert mu_two.scheme().scheme_base_ring() is QQ
    assert mu_two.multiplication().domain().factors()[0] is mu_two.scheme()
    assert mu_two.multiplication().domain().factors()[1] is mu_two.scheme()
    assert mu_two.multiplication().codomain() is mu_two.scheme()
    assert mu_two.unit_morphism().codomain() is mu_two.scheme()
    assert mu_two.inverse_morphism().domain() is mu_two.scheme()
    assert mu_two.internal_group_object() in Grp(Schemes(QQ).Affine())


def test_mu_two_scales_the_affine_line_by_a_scheme_morphism() -> None:
    mu_two, line, x, acted = _mu_two_scaling_action()
    action = acted.action_morphism()
    product = action.domain()
    product.coordinate_algebra()
    u = mu_two.scheme().coordinate_algebra().algebra_generator("u")
    group_pullback = product.projection(0).coordinate_algebra_morphism()
    point_pullback = product.projection(1).coordinate_algebra_morphism()

    assert acted.group_scheme() is mu_two
    assert acted.category().is_subcategory(AffineGroupSchemeActions(mu_two))
    assert acted.scheme() is line
    assert action.codomain() is line
    assert acted.internal_action().group_object() is mu_two.internal_group_object()
    assert action.coordinate_algebra_morphism()(x) == (
        group_pullback(u) * point_pullback(x)
    )


def test_additive_and_multiplicative_group_schemes_use_internal_group_objects() -> None:
    additive = AffineGroupSchemes(QQ).additive_group()
    multiplicative = AffineGroupSchemes(QQ).multiplicative_group()

    assert additive.internal_group_object() in Grp(Schemes(QQ).Affine())
    assert multiplicative.internal_group_object() in Grp(Schemes(QQ).Affine())

    x = additive.scheme().coordinate_algebra().algebra_generator("x")
    additive_square = additive.multiplication().domain()
    additive_pullback = additive.multiplication().coordinate_algebra_morphism()
    assert additive_pullback(x) == (
        additive_square.projection(0).coordinate_algebra_morphism()(x)
        + additive_square.projection(1).coordinate_algebra_morphism()(x)
    )

    u = multiplicative.scheme().coordinate_algebra().algebra_generator("u")
    multiplicative_square = multiplicative.multiplication().domain()
    multiplicative_pullback = multiplicative.multiplication().coordinate_algebra_morphism()
    assert multiplicative_pullback(u) == (
        multiplicative_square.projection(0).coordinate_algebra_morphism()(u)
        * multiplicative_square.projection(1).coordinate_algebra_morphism()(u)
    )
    assert multiplicative.inverse_morphism().coordinate_algebra_morphism()(u) == u**-1


def test_equivariant_maps_are_the_commutative_action_square() -> None:
    _mu_two, line, x, acted = _mu_two_scaling_action()
    square = line.coordinate_algebra().Mor(line.coordinate_algebra())({"x": x**2})
    squaring = line.Mor(line)(square)

    with pytest.raises(ValueError, match="not equivariant"):
        acted.Mor(acted)(squaring)

    assert acted.Mor(acted).identity().underlying_arrow() == (
        line.categorical_identity_morphism()
    )


def test_affine_group_scheme_action_constructor_rejects_a_wrong_unit_law() -> None:
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)
    line = AffineSpaces(QQ)(1, names=("x",))
    algebra = line.coordinate_algebra()
    product = line.scheme_category().product((mu_two.scheme(), line))
    bad_action = _affine_morphism_from_pullback(
        product,
        line,
        algebra.Mor(product.coordinate_algebra())({"x": product.coordinate_algebra().zero()}),
    )

    with pytest.raises(ValueError, match="unit"):
        AffineGroupSchemeActions(mu_two)(line, bad_action)
