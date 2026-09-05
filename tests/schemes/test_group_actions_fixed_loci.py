r"""Affine group actions and their scheme-theoretic fixed loci."""

import pytest

from dzack_research.preamble.all import (
    AffineSchemes,
    GObjects,
    Groups,
    PolynomialRing,
    QQ,
    Schemes,
    Spec,
    SpecFunctor,
)


def _coordinate_swap_action() -> tuple:
    group = Groups.C(2)
    algebra = PolynomialRing(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = Spec(algebra)
    swap = SpecFunctor(QQ)(algebra.Mor(algebra)({"x": y, "y": x}))
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(QQ))(
        scheme,
        lambda element: identity if element == group.one() else swap,
    )
    return group, algebra, x, y, scheme, acted


def test_affine_scheme_action_is_a_fresh_g_object_with_represented_pullbacks() -> None:
    group, algebra, x, y, scheme, acted = _coordinate_swap_action()
    generator = group.group_generators().unrank(0)
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


def test_coordinate_swap_fixed_subscheme_is_the_diagonal_equalizer() -> None:
    group, algebra, x, y, _scheme, acted = _coordinate_swap_action()
    generator = group.group_generators().unrank(0)

    assert acted.fixed_ideal() == algebra.ideal(x - y)

    fixed = acted.fixed_subscheme()
    inclusion = fixed.inclusion()
    quotient = inclusion.coordinate_algebra_morphism()

    assert fixed.ambient_scheme() is acted
    assert inclusion.domain() is fixed
    assert inclusion.codomain() is acted
    assert quotient(x) == quotient(y)
    assert acted.action_of(generator) * inclusion == inclusion


def test_affine_scheme_action_rejects_generator_images_that_violate_relators() -> None:
    group = Groups.C(2)
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    dilation = SpecFunctor(QQ)(algebra.Mor(algebra)({"x": x + x}))
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(QQ))(
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
