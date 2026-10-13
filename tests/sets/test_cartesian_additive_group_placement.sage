r"""Additive-group placement requires componentwise inverses, not only zero and addition."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_infinite_constant_additive_group_product_has_pointwise_inverses() -> None:
    product = Sets().product(indexed_family(NN, ZZ))
    assert product in AdditiveGroups()
    section = product(lambda index: ZZ(int(index) + 1))
    opposite = -section
    for position in (0, 1, 5):
        label = NN(position)
        assert product.projection(label)(opposite) == -product.projection(label)(section)
        assert product.projection(label)(section + opposite) == ZZ.zero()


def test_infinite_constant_additive_monoid_does_not_gain_inverses() -> None:
    product = Sets().product(indexed_family(NN, NN))
    assert product in AdditiveMonoids()
    assert product not in AdditiveGroups()
