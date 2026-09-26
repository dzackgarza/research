r"""Finite ordered sets support order-preserving finite set operations."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_finite_ordered_set_filter_union_intersection_and_difference() -> None:
    four = FiniteOrderedSets()((0, 1, 2, 3))
    evens = four.filtered(lambda value: value % 2 == 0)
    tail = FiniteOrderedSets()((2, 3, 4))

    assert four in FiniteOrderedSets()
    assert tuple(evens) == (0, 2)
    assert tuple(four.intersection(tail)) == (2, 3)
    assert tuple(four.difference(tail)) == (0, 1)
    assert tuple(four.union(tail)) == (0, 1, 2, 3, 4)
