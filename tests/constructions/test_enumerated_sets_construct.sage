r"""A finite ordinal is an enumerated set ranked by its own order."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_finite_ordinal_is_enumerated() -> None:
    ordinal_two = EnumeratedSets().an_object()

    assert ordinal_two in EnumeratedSets()
    assert ordinal_two.cardinality() == cardinal(2)
    assert ordinal_two.ranking_map()(ordinal_two[1]) == NN(1)


def test_fixed_size_selection_constructions() -> None:
    points = Sets.Δ[3]
    subsets = points.fixed_size_selections(2, repetition=False)
    multisets = points.fixed_size_selections(2, repetition=True)

    assert subsets is points.ordered_subsets_of_size(2)
    assert multisets is points.multisets_of_size(2)
    assert subsets.cardinality() == cardinal(6)
    assert multisets.cardinality() == cardinal(10)
    assert points.ordered_subsets_of_size(0).cardinality() == cardinal(1)
    assert points.ordered_subsets_of_size(5).cardinality() == cardinal(0)
