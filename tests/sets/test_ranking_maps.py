r"""The ranking of an enumerated set is one isomorphism onto its ordinal.

Ranking and unranking are that arrow and its inverse.  What has to be proved
is therefore what a pair of methods kept inverse by convention could never
state: that the two directions really are mutually inverse, that they land in
the ordinal that counts the set, and that the enumeration is the intended one
rather than some bijection that happens to round-trip.
"""

import pytest

from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import (
    CartesianProductOfSets,
    CoproductOfSets,
    NN,
    Sets,
    counting_ordinal,
    finite_ordinal_set,
)


def test_a_ranking_map_lands_in_the_ordinal_that_counts_its_set() -> None:
    r"""$X \to \operatorname{Ord}(|X|)$, and equinumerous sets share that target."""
    letters = finite_ordered_set(("a", "b", "c"))
    assert letters.cardinality() == 3
    assert letters.ranking_map().codomain() is finite_ordinal_set(3)

    # One ordinal per cardinality, not one per set: two enumerations of
    # equinumerous sets have to be composable, which they are not if each set
    # builds a private copy of {0,1,2}.
    assert counting_ordinal(letters) is counting_ordinal(finite_ordinal_set(3))
    assert counting_ordinal(letters) is Sets.Δ[2]

    # A countably infinite set is counted by omega, which is N itself.
    assert NN.ranking_map().codomain() is NN


def test_both_composites_of_a_ranking_map_are_identities() -> None:
    r"""The claim a method pair cannot make: the two directions are inverse."""
    letters = finite_ordered_set(("a", "b", "c"))
    ranking = letters.ranking_map()
    ordinal = ranking.codomain()

    assert ranking.inverse() * ranking.forward() == Sets().Mor(letters, letters).identity()
    assert ranking.forward() * ranking.inverse() == Sets().Mor(ordinal, ordinal).identity()


def test_ranking_then_unranking_returns_the_element_it_started_from() -> None:
    letters = finite_ordered_set(("a", "b", "c"))
    ranking = letters.ranking_map()

    # A position is an element of the ordinal, not a bare Python integer.
    assert ranking("b") in ranking.codomain()
    assert int(ranking("b")) == 1
    assert ranking.inverse()(1) == "b"
    assert all(ranking.inverse()(ranking(letter)) == letter for letter in letters)


def test_the_naturals_are_enumerated_by_omega_through_the_identity() -> None:
    r"""The infinite case, where the composites are not a decidable question."""
    ranking = NN.ranking_map()
    assert int(ranking(NN(7))) == 7
    assert ranking.inverse()(7) == NN(7)


def test_a_finite_product_is_enumerated_in_mixed_radix_order() -> None:
    r"""Position $= d_0 r_1 + d_1$: the first factor is the leading digit."""
    left = finite_ordinal_set(2)
    right = finite_ordinal_set(3)
    product = CartesianProductOfSets(left, right)
    ranking = product.ranking_map()
    assert product.cardinality() == 6

    assert int(ranking(product([left[1], right[2]]))) == 5
    assert int(ranking(product([left[0], right[1]]))) == 1
    section = ranking.inverse()(5)
    assert section.component(0) == left[1]
    assert section.component(1) == right[2]


def test_a_finite_coproduct_is_enumerated_by_rank_layer() -> None:
    r"""The summands interleave; they are not concatenated one after the other.

    Layer $k$ emits position $k$ of every summand that has one, so the order is
    $\iota_0(0), \iota_1(0), \iota_0(1), \iota_1(1), \iota_1(2)$.  A
    concatenating enumeration would put $\iota_1(0)$ at position 2.
    """
    left = finite_ordinal_set(2)
    right = finite_ordinal_set(3)
    coproduct = CoproductOfSets(left, right)
    ranking = coproduct.ranking_map()
    assert coproduct.cardinality() == 5

    assert int(ranking(coproduct.injection(0)(left[0]))) == 0
    assert int(ranking(coproduct.injection(1)(right[0]))) == 1
    assert int(ranking(coproduct.injection(0)(left[1]))) == 2
    assert int(ranking(coproduct.injection(1)(right[2]))) == 4
    assert ranking.inverse()(1) == coproduct.injection(1)(right[0])


def test_a_product_of_infinite_factors_refuses_the_arrow_it_cannot_represent() -> None:
    r"""$\mathbb N \times \mathbb N$ is countable, but mixed radix does not enumerate it.

    The counting ordinal exists here, so an isomorphism exists; the represented
    construction is not it.  The arrow is refused when it is asked for, rather
    than handed back with both directions raising the moment anyone applies
    them.
    """
    with pytest.raises(AssertionError):
        CartesianProductOfSets(NN, NN).ranking_map()
