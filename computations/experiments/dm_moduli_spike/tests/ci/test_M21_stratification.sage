r"""CI-tier serialization and invariant sweeps over the full Mbar(2, 1) stratification."""

from __future__ import annotations

import json
import pickle

import pytest
from sage.combinat.permutation import Permutations

from dm_moduli_spike._admcycles.admcycles_stable import AdmcyclesStableGraphs
from dm_moduli_spike.objects.records import _GraphRecord
from dm_moduli_spike.objects.stable_graphs import StableGraphs

pytestmark = pytest.mark.ci


def _relabel(record, vertex_perm, flag_perm):
    num_vertices = record.num_vertices()
    num_flags = record.num_flags()
    new_genera = [0] * num_vertices
    for vertex in range(num_vertices):
        new_genera[vertex_perm[vertex]] = record.vertex_genera[vertex]
    new_flag_vertex = [0] * num_flags
    new_flag_involution = [0] * num_flags
    for flag in range(num_flags):
        new_flag_vertex[flag_perm[flag]] = vertex_perm[record.flag_vertex[flag]]
        new_flag_involution[flag_perm[flag]] = flag_perm[record.flag_involution[flag]]
    new_marking_to_flag = tuple(flag_perm[flag] for flag in record.marking_to_flag)
    return _GraphRecord(
        vertex_genera=tuple(new_genera),
        flag_vertex=tuple(new_flag_vertex),
        flag_involution=tuple(new_flag_involution),
        marking_to_flag=new_marking_to_flag,
    )


def test_pickle_round_trip_preserves_parent_and_equality():
    for gamma in StableGraphs(2, 1):
        revived = pickle.loads(pickle.dumps(gamma))
        assert revived == gamma
        assert revived.parent() == gamma.parent()
        assert revived.canonical_key() == gamma.canonical_key()


def test_json_round_trip_preserves_equality():
    types = StableGraphs(2, 1)
    for gamma in types:
        blob = json.dumps(gamma.to_json())
        revived = types.from_json(json.loads(blob))
        assert revived == gamma
        assert revived.canonical_key() == gamma.canonical_key()


def test_every_type_is_connected_stable_correct_genus_and_marking_set():
    for gamma in StableGraphs(2, 1):
        record = gamma._canonical_record()
        assert record.is_stable()
        assert record._is_connected()
        assert gamma.total_genus() == 2
        all_markings = tuple(m for v in range(record.num_vertices()) for m in record.markings_at(v))
        assert sorted(all_markings) == [1]


def test_genus_matches_betti_plus_vertex_genera():
    for gamma in StableGraphs(2, 1):
        record = gamma._canonical_record()
        assert gamma.total_genus() == record.first_betti_number() + sum(record.vertex_genera)


def test_random_relabelings_produce_the_same_canonical_key():
    types = StableGraphs(2, 1)
    for gamma in types:
        record = gamma._canonical_record()
        num_vertices = record.num_vertices()
        num_flags = record.num_flags()
        for vperm in Permutations(num_vertices)[:3]:
            for fperm in Permutations(num_flags)[:3]:
                vmap = {i: int(vperm[i]) - 1 for i in range(num_vertices)}
                fmap = {i: int(fperm[i]) - 1 for i in range(num_flags)}
                relabelled = types.from_graph(_relabel(record, vmap, fmap))
                assert relabelled.canonical_key() == gamma.canonical_key()
                assert relabelled == gamma


def test_automorphism_numbers_agree_with_admcycles_on_M21():
    types = StableGraphs(2, 1)
    backend = AdmcyclesStableGraphs()
    for gamma in types:
        assert gamma.automorphism_number() == backend.admcycles_automorphism_number(types, gamma)


def test_covers_change_edge_count_by_one_and_carry_a_valid_witness():
    for gamma in StableGraphs(2, 1):
        for target, witness, _size in gamma.elementary_contractions():
            assert gamma.codimension() == target.codimension() + 1
            assert witness.num_contracted_edges() == 1
            assert witness.codomain() == target
            assert witness.domain() == gamma
            assert witness.codomain().num_edges() == witness.domain().num_edges() - 1
            assert witness.is_contraction()


@pytest.mark.parametrize("g,n", [(0, 5), (2, 1)])
def test_every_contraction_preserves_total_genus_and_stability_large(g, n):
    for gamma in StableGraphs(g, n):
        graph = gamma._canonical_record()
        for edge in graph.internal_edges():
            image, _ = graph.contract(edge)
            assert image.total_genus() == gamma.total_genus()
            assert image.is_stable()
            assert image.num_edges() == gamma.num_edges() - 1
