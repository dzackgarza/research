r"""Positional access on an owned set whose points are not Sage elements.

An enumerated set answers ``X[k]`` with the point at position ``k``, and that
is the ranking map run backwards.  Nothing in that says the points have to be
Sage elements: a set of labels, or an index set of generator names, is a set
like any other, and its enumeration is a bijection onto the ordinal counting
it.
"""

import pytest

from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


@pytest.fixture(params=[("a", "b", "c"), (10, 20, 30)], ids=("labels", "numbers"))
def label_set(request):
    return finite_ordered_set(request.param)


def test_the_ranking_map_reads_a_position_off_a_label(label_set):
    members = tuple(label_set)
    assert label_set.ranking_map()(members[1]) == 1


def test_positional_access_returns_the_point_at_that_position(label_set):
    members = tuple(label_set)
    assert label_set[1] == members[1]


def test_the_ranking_map_and_positional_access_are_inverse(label_set):
    members = tuple(label_set)
    for position, member in enumerate(members):
        assert label_set[position] == member
        assert label_set.ranking_map()(member) == position
