r"""Positional access on an owned set whose points are not Sage elements.

An enumerated set answers ``X[k]`` with the point at position ``k``, and that
is the ranking map run backwards.  The map is currently a Sage ``SetMorphism``,
whose application is typed to return a Sage ``Element``, so a set whose points
are Python labels cannot answer at all: the forward direction gives the
position, and the backward direction refuses.

This is red, and the red row is the finding.  The two candidate repairs are
mathematically different and the choice is open: either an owned set owns its
points, so a set of labels has its own elements and this never arises, or a map
of owned sets is applied by owned machinery rather than by Sage's morphism.
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
