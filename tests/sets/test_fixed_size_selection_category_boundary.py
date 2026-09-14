r"""Fixed-size selections use only owned set-category placement."""

from dzack_research.preamble.categories.sets.enumerated.enumerated_sets import EnumeratedSets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.fixed_size_selections import fixed_size_selections
from dzack_research.preamble.categories.sets.set_categories import FiniteSets, TotallyOrderedSets


def test_finite_fixed_size_selection_retains_owned_finite_enumerated_ordered_structure() -> None:
    source = finite_ordered_set(("a", "b", "c"))
    pairs = fixed_size_selections(source, 2, repetition=False)

    assert pairs in EnumeratedSets()
    assert pairs in TotallyOrderedSets()
    assert pairs in FiniteSets()
    assert pairs.cardinality() == 3
    first = pairs[0]
    assert first.degree() == 2
    assert first.support() in FiniteSets()


def test_repeated_selection_keeps_multiplicity_as_selection_data() -> None:
    source = finite_ordered_set(("a", "b"))
    multisets = fixed_size_selections(source, 2, repetition=True)
    repeated = multisets.from_source_rank_positions((0, 0))

    assert repeated.multiplicity("a") == 2
    assert repeated.multiplicity("b") == 0
    assert repeated.support().cardinality() == 1
