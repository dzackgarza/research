r"""The Cartesian product of a three-point and two-point set has six elements."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_finite_cartesian_product() -> None:
    three = Set((1, 2, 3))
    two = Sets.Δ[1]
    product = Sets().product((three, two))

    assert product in CartesianProductsOfSets()
    assert product.cardinality() == cardinal(6)
    assert product.factors().cardinality() == cardinal(2)
    assert product.has_finite_index_set()
    assert product.factor(0) is three
    assert product.factor(1) is two

    point = product((three(2), two(1)))
    assert point.component(0) == three(2)
    assert point.component(1) == two(1)
    assert product.projection(0)(point) == three(2)
    assert product.projection(1)(point) == two(1)

    source = Set(("x",))
    source_point = source("x")
    assembled = product.from_maps(
        source,
        lambda index: Sets().Mor(
            source,
            product.factor(index),
        )(
            lambda _value: three(1) if index == 0 else two(0)
        ),
    )
    assert assembled(source_point).component(0) == three(1)
    assert assembled(source_point).component(1) == two(0)
