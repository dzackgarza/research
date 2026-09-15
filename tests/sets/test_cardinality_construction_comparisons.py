r"""Archive reconciliation for cardinality comparison maps of set constructions."""

from dzack_research.preamble.all import (
    CC,
    QQ,
    RR,
    ZZ,
    PolynomialRing,
    QQbar,
    Sets,
    aleph0,
    cardinal,
    continuum,
)
from dzack_research.preamble.categories.functors.cardinality import cardinality_functor


def test_cardinality_compares_a_product_with_the_product_of_factor_cardinals() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    product = left.product_with(right)
    comparison = cardinality_functor().cartesian_product_comparison(product)

    assert comparison.domain() == cardinal(6)
    assert comparison.codomain() == product.cardinality() == cardinal(6)


def test_cardinality_compares_a_coproduct_with_the_sum_of_cofactor_cardinals() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    coproduct = left.coproduct_with(right)
    comparison = cardinality_functor().coproduct_comparison(coproduct)

    assert comparison.domain() == cardinal(5)
    assert comparison.codomain() == coproduct.cardinality() == cardinal(5)


def test_cardinality_compares_a_countable_power_set_with_two_to_aleph_zero() -> None:
    naturals = Sets.Δ[aleph0]
    power_set = naturals.power_set()
    comparison = cardinality_functor().power_set_comparison(power_set)
    expected = cardinal(2) ** aleph0

    assert comparison.domain() == expected
    assert comparison.codomain() == power_set.cardinality() == expected


def test_cardinality_comparisons_retain_countable_and_continuum_factor_arithmetic() -> None:
    polynomial = PolynomialRing(QQ, "y")
    countable_product = ZZ.product_with(polynomial)
    continuum_product = ZZ.product_with(RR)
    continuum_coproduct = QQbar.coproduct_with(CC)
    cardinality = cardinality_functor()

    countable_comparison = cardinality.cartesian_product_comparison(countable_product)
    assert countable_comparison.domain() == aleph0
    assert countable_comparison.codomain() == aleph0

    continuum_product_comparison = cardinality.cartesian_product_comparison(continuum_product)
    assert continuum_product_comparison.domain() == continuum
    assert continuum_product_comparison.codomain() == continuum

    continuum_coproduct_comparison = cardinality.coproduct_comparison(continuum_coproduct)
    assert continuum_coproduct_comparison.domain() == continuum
    assert continuum_coproduct_comparison.codomain() == continuum
