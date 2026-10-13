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


def test_infinite_group_cone_factors_as_an_additive_group_morphism() -> None:
    from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
    from dzack_research.preamble.categories.functors.core import NaturalTransformation

    groups = AdditiveGroups()
    index = DiscreteCategory(NN)
    constant = Cat().Mor(index, groups).constant_functor(ZZ)
    identity = groups.Mor(ZZ, ZZ).identity()
    legs = NaturalTransformation(constant, constant, lambda _index: identity)
    product = Sets().product(indexed_family(NN, ZZ))
    diagonal = product.from_maps(ZZ, legs)
    assert diagonal.parent() is groups.Mor(ZZ, product)
    for position in (0, 3, 9):
        projection = product.projection(NN(position))
        assert projection(diagonal(ZZ(-5))) == ZZ(-5)
        assert projection(diagonal(-ZZ(5))) == -projection(diagonal(ZZ(5)))


def test_group_product_retains_monoid_universal_property() -> None:
    product = Sets().product((ZZ, ZZ))
    source = NN
    additive = AdditiveMonoids()
    inclusion = additive.Mor(source, ZZ)(lambda n: ZZ(int(n)))
    induced = product.from_maps(source, lambda _index: inclusion)
    assert induced.parent() is additive.Mor(source, product)
    for label in product.index_set():
        assert product.projection(label)(induced(source(3))) == ZZ(3)
