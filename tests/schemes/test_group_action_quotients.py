r"""Supported affine invariant rings and categorical quotient maps."""

from typing import Any, cast

import pytest

from dzack_research.preamble.all import (
    AlgebrasWithChosenFinitePresentation,
    GObjects,
    Groups,
    Schemes,
    Spec,
    SpecFunctor,
)
from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.schemes.schemes import (
    _affine_morphism_from_pullback,
)
from dzack_research.preamble.rings import session_ring_objects

QQ = cast(Any, session_ring_objects()["QQ"])


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
    return group, algebra, x, y, acted


def _central_sign_action() -> tuple:
    group = Groups.C(2)
    algebra = PolynomialRing(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = Spec(algebra)
    sign = SpecFunctor(QQ)(algebra.Mor(algebra)({"x": -x, "y": -y}))
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(QQ))(
        scheme,
        lambda element: identity if element == group.one() else sign,
    )
    return group, algebra, x, y, acted


def _affine_map_from_polynomial(acted: Any, polynomial: Any) -> tuple:
    target_algebra = PolynomialRing(QQ, "t")
    t = target_algebra.algebra_generator("t")
    target = Spec(target_algebra)
    morphism = _affine_morphism_from_pullback(
        acted,
        target,
        target_algebra.Mor(acted.coordinate_algebra())({"t": polynomial}),
    )
    return t, target, morphism


def test_coordinate_swap_has_a_represented_affine_invariant_quotient() -> None:
    group, algebra, x, y, acted = _coordinate_swap_action()
    invariant_algebra = acted.invariant_algebra()
    inclusion = acted.invariant_algebra_inclusion()
    images = tuple(
        inclusion(invariant_algebra.algebra_generator(label))
        for label in invariant_algebra.algebra_generating_set()
    )

    assert inclusion.domain() is invariant_algebra
    assert inclusion.codomain() is algebra
    assert set(images) == {x + y, x**2 + y**2}
    generator = group.group_generators().unrank(0)
    pullback = acted.action_of(generator).coordinate_algebra_morphism()
    assert all(pullback(image) == image for image in images)

    quotient = acted.affine_quotient()
    quotient_map = acted.quotient_morphism()
    assert quotient.coordinate_algebra() is invariant_algebra
    assert quotient_map.domain() is acted
    assert quotient_map.codomain() is quotient
    assert quotient_map.coordinate_algebra_morphism() is inclusion


def test_coordinate_swap_quotient_factors_invariant_affine_maps() -> None:
    _group, _algebra, x, y, acted = _coordinate_swap_action()
    t, target, morphism = _affine_map_from_polynomial(acted, x + y)

    factor = acted.factor_through_affine_quotient(morphism)
    quotient_map = acted.quotient_morphism()
    factor_pullback = factor.coordinate_algebra_morphism()

    assert factor.domain() is acted.affine_quotient()
    assert factor.codomain() is target
    assert factor * quotient_map == morphism
    assert acted.invariant_algebra_inclusion()(factor_pullback(t)) == x + y


def test_coordinate_swap_quotient_rejects_a_noninvariant_affine_map() -> None:
    _group, _algebra, x, _y, acted = _coordinate_swap_action()
    _t, _target, morphism = _affine_map_from_polynomial(acted, x)

    with pytest.raises(ValueError, match="not invariant"):
        acted.factor_through_affine_quotient(morphism)


def test_sign_involution_invariant_ring_keeps_its_quadratic_relation() -> None:
    group, _algebra, x, y, acted = _central_sign_action()
    invariant_algebra = acted.invariant_algebra()
    inclusion = acted.invariant_algebra_inclusion()

    assert invariant_algebra in AlgebrasWithChosenFinitePresentation(QQ)
    relations = tuple(invariant_algebra.relations())
    assert len(relations) == 1
    assert relations[0] != invariant_algebra.presentation_ring().zero()

    images = tuple(
        inclusion(invariant_algebra.algebra_generator(label))
        for label in invariant_algebra.algebra_generating_set()
    )
    assert set(images) == {x**2, x * y, y**2}
    generator = group.group_generators().unrank(0)
    action = acted.action_of(generator).coordinate_algebra_morphism()
    assert all(action(image) == image for image in images)

    t, target, morphism = _affine_map_from_polynomial(acted, x * y)
    factor = acted.factor_through_affine_quotient(morphism)
    assert factor.domain() is acted.affine_quotient()
    assert factor.codomain() is target
    assert factor * acted.quotient_morphism() == morphism
    assert acted.invariant_algebra_inclusion()(
        factor.coordinate_algebra_morphism()(t)
    ) == x * y


def test_order_three_linear_action_uses_the_same_invariant_quotient_backend() -> None:
    group = Groups.C(3)
    generator = group.group_generators().unrank(0)
    algebra = PolynomialRing(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = Spec(algebra)
    rotation = SpecFunctor(QQ)(
        algebra.Mor(algebra)({"x": -y, "y": x - y})
    )
    rotation_squared = rotation * rotation
    identity = scheme.categorical_identity_morphism()

    def action(element: Any) -> Any:
        if element == group.one():
            return identity
        if element == generator:
            return rotation
        return rotation_squared

    acted = GObjects(group, Schemes(QQ))(scheme, action)
    invariant_algebra = acted.invariant_algebra()
    inclusion = acted.invariant_algebra_inclusion()
    generator_pullback = acted.action_of(generator).coordinate_algebra_morphism()
    assert all(
        generator_pullback(inclusion(invariant_algebra.algebra_generator(label)))
        == inclusion(invariant_algebra.algebra_generator(label))
        for label in invariant_algebra.algebra_generating_set()
    )

    invariant = x**2 - x * y + y**2
    t, target, morphism = _affine_map_from_polynomial(acted, invariant)
    factor = acted.factor_through_affine_quotient(morphism)
    assert factor.domain() is acted.affine_quotient()
    assert factor.codomain() is target
    assert factor * acted.quotient_morphism() == morphism
    assert acted.invariant_algebra_inclusion()(
        factor.coordinate_algebra_morphism()(t)
    ) == invariant


def test_zero_dimensional_polynomial_space_is_its_own_invariant_quotient() -> None:
    group = Groups.C(2)
    algebra = PolynomialRing(QQ, ())
    scheme = Spec(algebra)
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(QQ))(scheme, lambda _element: identity)

    assert acted.invariant_algebra() is algebra
    assert acted.invariant_algebra_inclusion() == algebra.Mor(algebra).identity()
    assert acted.affine_quotient().coordinate_algebra() is algebra
    quotient_map = acted.quotient_morphism()
    assert quotient_map.domain() is acted
    assert quotient_map.codomain() is acted.affine_quotient()
    assert quotient_map.coordinate_algebra_morphism() == algebra.Mor(algebra).identity()

    t, target, morphism = _affine_map_from_polynomial(acted, algebra.one())
    factor = acted.factor_through_affine_quotient(morphism)
    assert factor.domain() is acted.affine_quotient()
    assert factor.codomain() is target
    assert factor * quotient_map == morphism
    assert factor.coordinate_algebra_morphism()(t) == algebra.one()


def test_nonlinear_polynomial_action_is_outside_the_selected_invariant_backend() -> None:
    group = Groups.C(2)
    algebra = PolynomialRing(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = Spec(algebra)
    nonlinear = SpecFunctor(QQ)(
        algebra.Mor(algebra)({"x": -x, "y": y + x**3})
    )
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(QQ))(
        scheme,
        lambda element: identity if element == group.one() else nonlinear,
    )

    # This is genuinely an involution, so rejection is by the selected
    # invariant-ring backend's linearity hypothesis rather than by the action
    # verifier.
    generator = group.group_generators().unrank(0)
    generator_action = acted.action_of(generator)
    assert (
        generator_action * generator_action
        == acted.categorical_identity_morphism()
    )
    with pytest.raises(NotImplementedError, match="linear action"):
        acted.invariant_algebra()
