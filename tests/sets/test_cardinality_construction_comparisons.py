r"""Archive reconciliation for cardinality comparison maps of set constructions."""

from dzack_research.preamble.all import (
    CartesianProductOfSets,
    CoproductOfSets,
    PowerSet,
    Sets,
    aleph0,
    cardinal,
)
from dzack_research.preamble.categories.functors.cardinality import cardinality_functor


def test_cardinality_compares_a_product_with_the_product_of_factor_cardinals() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    product = CartesianProductOfSets(left, right)
    comparison = cardinality_functor().cartesian_product_comparison(product)

    assert comparison.domain() == cardinal(6)
    assert comparison.codomain() == product.cardinality() == cardinal(6)


def test_cardinality_compares_a_coproduct_with_the_sum_of_cofactor_cardinals() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    coproduct = CoproductOfSets(left, right)
    comparison = cardinality_functor().coproduct_comparison(coproduct)

    assert comparison.domain() == cardinal(5)
    assert comparison.codomain() == coproduct.cardinality() == cardinal(5)


def test_cardinality_compares_a_countable_power_set_with_two_to_aleph_zero() -> None:
    naturals = Sets.Δ[aleph0]
    power_set = PowerSet(naturals)
    comparison = cardinality_functor().power_set_comparison(power_set)
    expected = cardinal(2) ** aleph0

    assert comparison.domain() == expected
    assert comparison.codomain() == power_set.cardinality() == expected
