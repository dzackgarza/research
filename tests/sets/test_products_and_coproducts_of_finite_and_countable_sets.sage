r"""Cartesian products and disjoint unions of finite and countable sets.

$|X \times Y| = |X| |Y|$ and $|X \sqcup Y| = |X| + |Y|$, so
$\{0, 1\} \times \{0, 1, 2\}$ has $6$ points and $\{0, 1\} \sqcup \{0, 1, 2\}$
has $5$; $\mathbb{N} \times \mathbb{N}$ and $\mathbb{N} \sqcup \{0, 1\}$ are
countably infinite.  An enumeration of $\mathbb{N} \times \mathbb{N}$ by
diagonals lists each pair once, so the rank of the $k$-th listed pair is
$k$.  The product functor sends $(\sigma, \mathrm{id})$ to
$(a, b) \mapsto (\sigma a, b)$.  These are the definitions of cardinal
arithmetic and of the product functor.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_finite_product_of_additive_monoids_has_componentwise_addition() -> None:
    from dzack_research.preamble.categories.group.magmas import AdditiveMonoids
    from dzack_research.preamble.categories.sets.set_categories import (
        CartesianProductsOfAdditiveMonoids,
    )

    factor = AdditiveMonoids().an_object()
    product = Sets().product((factor, factor))
    assert product in CartesianProductsOfAdditiveMonoids()
    assert product in AdditiveMonoids()
    zero = product.zero()
    point = product(lambda index: factor.one())
    assert point + zero == point
    assert zero + point == point
    assert (point + point).component(product.index_set()(0)) == factor.one() + factor.one()
    projection = product.projection(product.index_set()(0))
    assert projection.parent() is AdditiveMonoids().Mor(product, factor)
    assert projection(zero) == factor.zero()
    assert projection(point + point) == projection(point) + projection(point)


def test_infinite_constant_additive_product_retains_its_monoid_and_projections() -> None:
    from dzack_research.preamble.categories.group.magmas import AdditiveMonoids
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family
    from dzack_research.preamble.categories.sets.set_categories import (
        CartesianProductsOfAdditiveMonoids,
    )

    factor = AdditiveMonoids().an_object()
    family = indexed_family(NN, factor)
    product = Sets().product(family)
    assert family.constant_value() is factor
    assert product in CartesianProductsOfAdditiveMonoids()
    assert product in AdditiveMonoids()
    varying = product(lambda index: factor(int(index)))
    unit = product(lambda index: factor.one())
    zero = product.zero()
    projection = product.projection(NN(2))
    assert projection.parent() is AdditiveMonoids().Mor(product, factor)
    assert projection(varying) != projection(product(lambda index: factor.zero()))
    assert projection(varying + zero) == projection(varying)
    assert projection(varying + unit) == projection(varying) + projection(unit)
    assert projection(zero) == factor.zero()

    nonmonoid = Sets().product(indexed_family(NN, Sets.Δ[1]))
    assert nonmonoid not in CartesianProductsOfAdditiveMonoids()
    assert nonmonoid not in AdditiveMonoids()


def test_unproved_infinite_value_category_cannot_place_monoid_product() -> None:
    from dzack_research.preamble.categories.group.magmas import AdditiveMonoids
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family
    from dzack_research.preamble.categories.sets.set_categories import CartesianProductsOfAdditiveMonoids

    factor = AdditiveMonoids().an_object()
    for value in (lambda index: factor, lambda index: factor if int(index) % 2 == 0 else Sets.Δ[1]):
        try:
            indexed_family(NN, value, value_category=AdditiveMonoids())
        except TypeError:
            pass
        else:
            raise AssertionError("unchecked infinite callback falsely established category-valued diagram")
    try:
        indexed_family(Sets.Δ[0], lambda _index: Sets.Δ[1], value_category=AdditiveMonoids())
    except ValueError:
        pass
    else:
        raise AssertionError("nonmonoid set admitted to an additive-monoid diagram")


def test_unchecked_discrete_diagram_cannot_certify_infinite_factors() -> None:
    from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
    from dzack_research.preamble.categories.group.magmas import AdditiveMonoids
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family

    factor = AdditiveMonoids().an_object()
    index_category = DiscreteCategory(NN)
    raw = indexed_family(NN, lambda index: factor if int(index) % 2 == 0 else Sets.Δ[1])
    unchecked = Cat().Mor(index_category, AdditiveMonoids()).discrete_diagram(raw)
    try:
        indexed_family(NN, unchecked)
    except TypeError:
        pass
    else:
        raise AssertionError("unchecked infinite diagram claimed an invalid additive placement")

    selected = Cat().Mor(index_category, AdditiveMonoids()).constant_functor(factor)
    family = indexed_family(NN, selected)
    product = Sets().product(family)
    assert product in AdditiveMonoids()
    assert product.projection(NN(3))(product.zero()) == factor.zero()


def test_finite_diagram_restricted_to_infinite_parity_family() -> None:
    from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
    from dzack_research.preamble.categories.group.magmas import AdditiveMonoids, AdditiveGroups
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family
    from dzack_research.preamble.categories.sets.set_categories import CartesianProductsOfAdditiveMonoids

    labels = Sets.Δ[1]
    finite_index = DiscreteCategory(labels)
    infinite_index = DiscreteCategory(NN)
    even = AdditiveMonoids().an_object()
    odd = AdditiveGroups().an_object()
    diagram = Cat().Mor(finite_index, AdditiveMonoids()).discrete_diagram(
        indexed_family(labels, lambda i: even if i == labels(0) else odd)
    )
    parity = Cat().Mor(infinite_index, finite_index).from_object_map(
        lambda n: labels(int(n) % 2)
    )
    selected = diagram.restrict(parity)
    family = indexed_family(NN, selected)
    product = Sets().product(family)
    assert family.selected_diagram() is selected
    assert product in CartesianProductsOfAdditiveMonoids()
    assert family(NN(0)) is even and family(NN(1)) is odd
    point = product(lambda n: family(n)(int(n)))
    unit = product(lambda n: family(n).one())
    projection = product.projection(NN(3))
    assert projection.parent() is AdditiveMonoids().Mor(product, odd)
    assert projection(point + unit) == projection(point) + projection(unit)
    assert projection(product.zero()) == odd.zero()

    unchecked = Cat().Mor(infinite_index, AdditiveMonoids()).discrete_diagram(
        indexed_family(NN, lambda n: even if int(n) % 2 == 0 else Sets.Δ[1])
    )
    identity = Cat().Mor(infinite_index, infinite_index).from_object_map(lambda n: n)
    for candidate in (unchecked, unchecked.restrict(identity)):
        try:
            indexed_family(NN, candidate)
        except TypeError:
            pass
        else:
            raise AssertionError("unchecked infinite diagram incorrectly certified additive placement")


def test_the_product_of_two_and_three_points_has_six_points() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    product = Sets().product((two, three))
    corner = product((two(1), three(2)))

    assert product.cardinality() == cardinal(6)
    assert sum(1 for _point in product) == 6
    assert corner == product((two(1), three(2)))
    assert corner != product((two(0), three(2)))


def test_the_disjoint_union_of_two_and_three_points_has_five_points() -> None:
    union = Sets().coproduct((Sets.Δ[1], Sets.Δ[2]))

    assert union.cardinality() == cardinal(5)
    assert sum(1 for _point in union) == 5


def test_the_square_of_the_natural_numbers_is_countable_and_listed_by_diagonals() -> None:
    square = Sets().product((NN, NN))
    listing = iter(square)
    first_six = [next(listing) for _step in range(6)]

    assert square.cardinality() == aleph0
    assert first_six[0] == square((NN(0), NN(0)))
    assert all(
        square((NN(a), NN(b))) in first_six for a in range(3) for b in range(3) if a + b <= 2
    )


def test_the_diagonal_enumeration_of_the_square_of_the_naturals_is_ranked() -> None:
    square = Sets().product((NN, NN))
    ranking = square.ranking_map()
    listing = iter(square)

    assert [ranking(next(listing)) for _step in range(6)] == [0, 1, 2, 3, 4, 5]


def test_the_natural_numbers_plus_two_points_are_countable_and_enumerated() -> None:
    union = Sets().coproduct((NN, Sets.Δ[1]))
    listing = iter(union)
    first_five = [next(listing) for _step in range(5)]

    assert union.cardinality() == aleph0
    assert all(first_five[i] != first_five[j] for i in range(5) for j in range(i))


def test_the_product_functor_applies_a_transposition_to_the_first_coordinate() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    pairs = Cat().product([Sets(), Sets()])
    transposition = Sets().Mor(two, two)(lambda x: two(1) if x == 0 else two(0))
    identity = Sets().Mor(three, three).identity()
    induced = Sets().product_functor()(pairs.Mor(pairs(two, three), pairs(two, three))((transposition, identity)))
    product = induced.domain()

    assert induced(product((two(1), three(2)))) == product((two(0), three(2)))
    assert induced(product((two(0), three(0)))) == product((two(1), three(0)))
