r"""Tier-4 internal consistency: half-edge record validation and numerical invariants."""

from __future__ import annotations

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.objects.records import _GraphRecord
import pytest



def test_record_rejects_a_non_involution():
    with pytest.raises(AssertionError):
        _GraphRecord(
            vertex_genera=(1,),
            flag_vertex=(0, 0),
            flag_involution=(1, 0, 0),  # length mismatch / not an involution
            marking_to_flag=(),
        )


def test_record_rejects_an_unstable_vertex():
    # A genus-0 vertex with a single leg is unstable: 2*0 - 2 + 1 = -1.
    with pytest.raises(AssertionError):
        _GraphRecord(
            vertex_genera=(0,),
            flag_vertex=(0,),
            flag_involution=(0,),
            marking_to_flag=(0,),
        )


def test_record_rejects_a_disconnected_graph():
    with pytest.raises(AssertionError):
        _GraphRecord(
            vertex_genera=(1, 1),
            flag_vertex=(0, 1),
            flag_involution=(0, 1),  # two isolated genus-1 vertices, each a leg
            marking_to_flag=(0, 1),
        )


def test_record_requires_markings_to_be_exactly_1_to_n():
    with pytest.raises(AssertionError):
        StableGraphs(0, 4).from_vertices(
            genera=(0,),
            markings=((1, 2, 3, 5),),  # 5 is not in 1..4
            edges=(),
        )


def test_smooth_type_is_edge_free_and_carries_all_markings():
    types = StableGraphs(2, 3)
    smooth = types.smooth()
    assert smooth.is_smooth()
    assert smooth.num_edges() == 0
    assert smooth.total_genus() == 2
    assert smooth.num_markings() == 3
    assert smooth.vertex_genera() == (2,)
    assert smooth.codimension() == 0
    assert smooth.stratum_dimension() == 3 * 2 - 3 + 3


def test_dimension_computed_two_independent_ways():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        for gamma in StableGraphs(g, n):
                by_vertices = gamma.stratum_dimension()
                by_codim = StableGraphs(g, n).dimension() - gamma.num_edges()
                assert by_vertices == by_codim


def test_from_vertices_builds_the_expected_boundary_type():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(
        genera=(0, 0),
        markings=((1, 2), (3, 4)),
        edges=((0, 1),),
    )
    assert gamma.total_genus() == 0
    assert gamma.num_edges() == 1
    assert gamma.codimension() == 1
    assert gamma.stratum_dimension() == 0
    assert gamma.is_stable()
