r"""The thin categories of cardinals and of ordinals, and the arithmetic acting on their arrows.

$\mathbf{Card}$ has one arrow $\kappa \to \lambda$ exactly when
$\kappa \le \lambda$, so composites and identities are forced.  Cardinal
sum, product and power with a nonzero base are monotone, so they act on
arrows: $2 \le 3$ and $4 \le 5$ give $6 \le 8$, $8 \le 15$ and
$16 \le 243$.  A finite sum $\sum_{i=0}^{3} (i + 1) = 10$, and
$\sum_{i \in \mathbb{N}} 1 = \aleph_0$.  For ordinals, $\omega + 1 \ne
1 + \omega = \omega$, $2 \cdot \omega = \omega \ne \omega \cdot 2$ and
$2^\omega = \omega$; natural (Hessenberg) sum is commutative.  All of these
are the definitions of the operations on order types.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_comparisons_of_cardinals_compose_and_are_carried_by_the_arithmetic() -> None:
    cardinals = Cardinalities()
    two_three = cardinals.Mor(2, 3).unique_morphism()
    four_five = cardinals.Mor(4, 5).unique_morphism()
    three_five = cardinals.Mor(3, 5).unique_morphism()

    assert three_five * two_three == cardinals.Mor(2, 5).unique_morphism()
    assert cardinals.Mor(3, 3).identity() == cardinals.Mor(3, 3).unique_morphism()
    assert cardinals.sum_morphism(two_three, four_five) == cardinals.Mor(6, 8).unique_morphism()
    assert cardinals.product_morphism(two_three, four_five) == cardinals.Mor(8, 15).unique_morphism()
    assert cardinals.power_morphism(two_three, four_five) == cardinals.Mor(16, 243).unique_morphism()
    assert cardinals.Mor(3, 2).is_empty()
    assert cardinal(2).Mor(3).cardinality() == cardinal(1)


def test_finite_indexed_sums_suprema_and_comparisons_of_cardinals() -> None:
    cardinals = Cardinalities()

    assert cardinals.indexed_sum(Sets.Δ[3], lambda index: cardinal(index + 1)) == cardinal(10)
    assert cardinals.supremum(cardinal(3), aleph0) == aleph0
    assert cardinals.compare(cardinal(3), cardinal(5)) is CardinalComparison.LESS
    assert cardinals.compare(aleph0, cardinal(5)) is CardinalComparison.GREATER
    assert cardinals(Infinity) == aleph0


def test_the_countable_sum_of_ones_is_aleph_zero() -> None:
    assert Cardinalities().indexed_sum(NN, lambda _index: cardinal(1)) == aleph0


def test_a_finite_cardinal_is_the_natural_number_it_counts() -> None:
    r"""$|\{0, 1, 2\}| = 3$, and the finite cardinal $7$ read in $\mathbb{Z}$ and $\mathbb{Q}$ is $7$."""
    assert cardinal(3) == 3
    assert Sets.Δ[2].cardinality() == 3
    assert ZZ(cardinal(7)) == 7
    assert QQ(cardinal(7)) == 7


def test_ordinal_sum_product_and_power_are_not_commutative() -> None:
    ordinals = Ordinals()
    first_infinite = omega(0)

    assert first_infinite.ordinal_sum(1) != first_infinite
    assert ordinals(1).ordinal_sum(first_infinite) == first_infinite
    assert ordinals(2).ordinal_product(first_infinite) == first_infinite
    assert first_infinite.ordinal_product(2) != first_infinite
    assert ordinals(2).ordinal_power(first_infinite) == first_infinite
    assert ordinals.proves_le(3, first_infinite)
    assert not ordinals.proves_le(first_infinite, 3)


def test_ordinary_ordinal_arithmetic_is_canonical_order_type_arithmetic() -> None:
    two = Ordinals()(2)
    first = omega(0)
    second = omega(1)

    assert Ordinals()(1).ordinal_sum(first) == first
    assert two.ordinal_product(first) == first
    assert two.ordinal_power(first) == first

    omega_plus_one = first.ordinal_sum(1)
    omega_times_two = first.ordinal_product(2)
    omega_squared = first.ordinal_power(2)
    assert omega_plus_one.ordinal_sum(first) == omega_times_two
    assert omega_plus_one.ordinal_product(first) == omega_squared
    assert two.ordinal_power(omega_times_two) == omega_squared

    assert two.ordinal_product(second) == second
    assert two.ordinal_power(second) == second
    assert first < omega_plus_one < omega_times_two < omega_squared < second


def test_natural_sums_of_initial_ordinals_commute_and_omega_one_follows_omega() -> None:
    first = omega(0)
    second = omega(1)

    assert first + second == second + first
    assert first + second == second.ordinal_sum(first)
    assert first * second == second.ordinal_product(first)
    assert first.ordinal_sum(second) == second
    assert second > first
    assert second.initial_index() == Ordinals()(1)
    assert Ord.Mor(first, second).unique_morphism().domain() is first
    assert Ord.Mor(second, second).identity().is_identity()


def test_order_type_is_a_functor_from_well_orders_to_ord() -> None:
    labels = finite_ordered_set(("a", "b", "c"))
    standard = Sets.Δ[2]
    well_orders = WellOrderedSets()

    forward = well_orders.Mor(labels, standard)(
        lambda point: labels.ranking_map()(point)
    )
    inverse = well_orders.Mor(standard, labels)(
        lambda position: labels.ranking_map().inverse()(position)
    )
    isomorphism = well_orders.Core().Mor(labels, standard)(forward, inverse)
    order_type = well_orders.order_type_functor()

    assert standard in AugmentedSimplexCategory()
    assert labels in WellOrderedSets()
    assert order_type(labels) is Ordinals()(3)
    assert order_type(standard) is Ordinals()(3)
    assert order_type(isomorphism) == Ord.Mor(3, 3).identity()
