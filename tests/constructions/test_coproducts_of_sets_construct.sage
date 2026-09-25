r"""The coproduct of a three-point and two-point set has five tagged elements."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_finite_set_coproduct() -> None:
    three = Set((1, 2, 3))
    two = Sets.Δ[1]
    coproduct = Sets().coproduct((three, two))

    assert coproduct in CoproductsOfSets()
    assert coproduct.cardinality() == cardinal(5)
    assert coproduct.factors().cardinality() == cardinal(2)
    assert coproduct.cofactor(0) is three
    assert coproduct.cofactor(1) is two

    point = coproduct.injection(1)(two(0))
    assert point.summand_index() == 1
    assert point.summand_element() == two(0)

    target = Set(("left", "right"))
    folded = coproduct.from_maps(
        target,
        lambda index: Sets().Mor(
            coproduct.cofactor(index),
            target,
        )(lambda _value: target("left") if index == 0 else target("right")),
    )
    assert folded(coproduct.injection(0)(three(1))) == target("left")
    assert folded(coproduct.injection(1)(two(1))) == target("right")
