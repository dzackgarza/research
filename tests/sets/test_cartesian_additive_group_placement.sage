r"""Additive-group placement requires componentwise inverses, not only zero and addition."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_infinite_constant_additive_group_product_has_pointwise_inverses() -> None:
    product = Sets().product(indexed_family(NN, ZZ))
    assert product in AdditiveGroups()
    assert product in AdditiveGroups().AdditiveCommutative()
    section = product(lambda index: ZZ(int(index) + 1))
    opposite = -section
    other = product(lambda index: ZZ(2 * int(index)))
    assert product.projection(NN(3))(section + other) == product.projection(NN(3))(other + section)
    for position in (0, 1, 5):
        label = NN(position)
        projection = product.projection(label)
        assert projection.parent() is AdditiveGroups().Mor(product, ZZ)
        assert projection(opposite) == -projection(section)
        assert projection(section + opposite) == ZZ.zero()


def test_infinite_constant_additive_monoid_does_not_gain_inverses() -> None:
    product = Sets().product(indexed_family(NN, NN))
    assert product in AdditiveMonoids()
    assert product not in AdditiveGroups()
