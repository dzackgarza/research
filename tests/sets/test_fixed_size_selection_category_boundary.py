r"""Fixed-size selections use only owned set-category placement."""

import pytest

from dzack_research.preamble.categories.sets.enumerated.enumerated_sets import EnumeratedSets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import FiniteSets, TotallyOrderedSets


def test_finite_fixed_size_selection_retains_owned_finite_enumerated_ordered_structure() -> None:
    source = finite_ordered_set(("a", "b", "c"))
    pairs = source.fixed_size_selections(2, repetition=False)

    assert pairs in EnumeratedSets()
    assert pairs in TotallyOrderedSets()
    assert pairs in FiniteSets()
    assert pairs.cardinality() == 3
    first = pairs[0]
    assert first.degree() == 2
    assert first.support() in FiniteSets()


def test_repeated_selection_keeps_multiplicity_as_selection_data() -> None:
    source = finite_ordered_set(("a", "b"))
    multisets = source.fixed_size_selections(2, repetition=True)
    repeated = multisets.from_source_rank_positions((0, 0))

    assert repeated.multiplicity("a") == 2
    assert repeated.multiplicity("b") == 0
    assert repeated.support().cardinality() == 1


def test_selection_ingress_does_not_truncate_sizes_ranks_or_multiplicities() -> None:
    from dzack_research.preamble.all import NN, QQ, ZZ

    source = finite_ordered_set(("a", "b", "c"))
    singletons = source.fixed_size_selections(1, repetition=False)
    with pytest.raises(TypeError):
        source.fixed_size_selections(1.5, repetition=False)
    assert source.fixed_size_selections(1, repetition=False) is singletons
    assert source.fixed_size_selections(NN(1), repetition=False) is singletons
    assert source.fixed_size_selections(ZZ(1), repetition=False) is singletons
    with pytest.raises(TypeError):
        source.fixed_size_selections(QQ(3) / 2, repetition=False)

    with pytest.raises(TypeError):
        singletons.from_source_rank_positions((1.5,))
    with pytest.raises(TypeError):
        singletons.from_multiplicities({"a": 1.5})

    pairs = source.fixed_size_selections(2, repetition=True)
    with pytest.raises(ValueError, match="nonnegative"):
        pairs.from_multiplicities({"a": 3, "b": -1})


def test_empty_selection_does_not_need_the_source_cardinality(monkeypatch) -> None:
    source = finite_ordered_set(("a", "b", "c"))

    def unavailable_cardinality(_self):
        raise AssertionError("this query is not needed to construct the empty selection")

    monkeypatch.setattr(type(source), "cardinality", unavailable_cardinality)
    selections = source.fixed_size_selections(0, repetition=False)
    assert selections.cardinality() == 1
    empty = selections.from_source_rank_positions(())
    assert empty.degree() == 0
    assert tuple(empty) == ()


def test_infinite_selections_retain_the_source_and_combinadic_enumeration() -> None:
    from dzack_research.preamble.categories.sets.set_categories import NN

    pairs = NN.fixed_size_selections(2, repetition=False)
    assert pairs.source() is NN
    assert pairs.cardinality() == NN.cardinality()
    pair = pairs.from_source_rank_positions((2, 5))
    assert tuple(map(int, pair)) == (2, 5)
    assert pairs.ranking_map().inverse()(pairs.ranking_map()(pair)) == pair
