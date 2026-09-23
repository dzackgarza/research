r"""Morphisms of affine group schemes preserve their actual group diagrams."""

import pytest

from dzack_research.preamble.all import QQ, AffineGroupSchemes
from dzack_research.preamble.categories.schemes.schemes import (
    _affine_morphism_from_pullback,
)


def _power_map(source, target, exponent: int):
    source_algebra = source.scheme().coordinate_algebra()
    target_algebra = target.scheme().coordinate_algebra()
    source_u = source_algebra.algebra_generator("u")
    pullback = target_algebra.Mor(source_algebra)({"u": source_u**exponent})
    return _affine_morphism_from_pullback(
        source.scheme(),
        target.scheme(),
        pullback,
    )


def test_identity_is_an_actual_group_scheme_morphism() -> None:
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)
    identity = mu_two.Mor(mu_two).identity()

    assert identity.underlying_arrow() == mu_two.scheme().categorical_identity_morphism()


def test_squaring_mu_four_to_mu_two_preserves_the_group_scheme_structure() -> None:
    mu_four = AffineGroupSchemes(QQ).roots_of_unity(4)
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)
    squaring = _power_map(mu_four, mu_two, 2)

    morphism = mu_four.Mor(mu_two)(squaring)
    assert morphism.domain() is mu_four
    assert morphism.codomain() is mu_two
    assert morphism.underlying_arrow() is squaring


def test_scheme_automorphism_that_moves_the_unit_is_not_a_group_scheme_morphism() -> None:
    mu_two = AffineGroupSchemes(QQ).roots_of_unity(2)
    algebra = mu_two.scheme().coordinate_algebra()
    u = algebra.algebra_generator("u")
    negation_pullback = algebra.Mor(algebra)({"u": -u})
    negation = _affine_morphism_from_pullback(
        mu_two.scheme(),
        mu_two.scheme(),
        negation_pullback,
    )

    with pytest.raises(ValueError, match="does not preserve"):
        mu_two.Mor(mu_two)(negation)


def test_affine_group_scheme_constructor_rejects_a_wrong_internal_inverse() -> None:
    mu_three = AffineGroupSchemes(QQ).roots_of_unity(3)
    identity = mu_three.scheme().categorical_identity_morphism()

    with pytest.raises(ValueError, match="inverse"):
        AffineGroupSchemes(QQ)(
            mu_three.scheme(),
            mu_three.multiplication(),
            mu_three.unit_morphism(),
            identity,
        )
