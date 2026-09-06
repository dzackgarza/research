r"""Restriction between localizations, and its composition.

Localization is universal among maps out of ``R`` inverting a set of scalars,
so for ``S`` inside ``T`` there is exactly one map ``S^{-1}R -> T^{-1}R`` over
``R``.  Uniqueness makes these maps compose, which is the cocycle condition an
affine cover needs before any sheaf is glued on it.  Localizing a module along
the same restriction gives the map from a section to its restriction, and at a
prime to its germ.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    PolynomialRing,
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_a_localization_restricts_to_a_further_localization_over_the_source() -> None:
    inverted_two = ZZ.localization(2)
    inverted_six = ZZ.localization(2, 3)

    restriction = inverted_two.restriction_to(inverted_six)

    assert restriction.domain() is inverted_two
    assert restriction.codomain() is inverted_six
    assert restriction(inverted_two.localization_map()(ZZ(5))) == inverted_six.localization_map()(ZZ(5))
    assert restriction(inverted_two(1) / 2) == inverted_six(1) / 2


def test_localization_restrictions_compose_along_a_chain_of_inverted_scalars() -> None:
    inverted_two = ZZ.localization(2)
    inverted_six = ZZ.localization(2, 3)
    inverted_thirty = ZZ.localization(2, 3, 5)

    step = inverted_two.restriction_to(inverted_six)
    rest = inverted_six.restriction_to(inverted_thirty)
    whole = inverted_two.restriction_to(inverted_thirty)
    element = inverted_two(1) / 2

    assert rest(step(element)) == whole(element)


def test_a_localization_restricts_into_a_prime_localization_as_a_germ() -> None:
    polynomial = PolynomialRing(QQ, "x")
    x = polynomial.algebra_generator("x")
    away_from_x = polynomial.localization(x)
    at_x_minus_one = polynomial.localize_at_prime(polynomial.ideal(x - 1))

    germ = away_from_x.restriction_to(at_x_minus_one)

    assert germ.codomain() is at_x_minus_one
    assert germ(away_from_x(1) / x) == at_x_minus_one(1) / at_x_minus_one(x)


def test_restricting_a_localized_module_carries_generators_to_generators() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    inverted_two = ZZ.localization(2)
    inverted_six = ZZ.localization(2, 3)
    sections = inverted_two.localize_module(module)

    restriction = sections.restriction_to(inverted_six)
    finer = inverted_six.localize_module(module)

    assert restriction.domain() is sections
    assert restriction(sections.module_generator("u")) == restriction.codomain()(
        finer.module_generator("u")
    )
    assert restriction(sections.module_generator("u")) != restriction.codomain()(
        finer.module_generator("v")
    )
