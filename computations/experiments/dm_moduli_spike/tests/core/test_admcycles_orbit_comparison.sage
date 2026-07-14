r"""Tier-3 differential check: admcycles edge-orbit comparison (not tier-1 literature)."""

from __future__ import annotations

from collections import Counter

from admcycles.decorated_graph import DecoratedGraph

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.backends.admcycles_decorated import (
    _record_from_decorated_graph,
    _record_to_decorated_graph,
)
from dm_moduli_spike.objects.edge_orbits import (
    automorphism_edge_orbit_indices,
    edges_are_in_same_orbit,
)
from dm_moduli_spike.testing_support.support.fixtures import genus_six_counterexample


def _spike_orbit_sizes(record):
    return sorted(len(group) for group in automorphism_edge_orbit_indices(record))


def _adm_orbit_sizes(dg):
    return sorted(int(size) for _u, _v, size in dg.edge_orbit_representatives())


def _adm_contraction_multiset(dg, g, n):
    from dm_moduli_spike.backends.admcycles_decorated import contraction_from_decorated_morphism

    parent = StableGraphs(g, n)
    entries: list[tuple[object, int]] = []
    for u, v, size in dg.edge_orbit_representatives():
        morphism = dg.edge_contraction_morphism([(u, v, 1)])
        contraction = contraction_from_decorated_morphism(morphism, g, n)
        entries.append((parent(contraction.target_type()).canonical_key(), int(size)))
    return Counter(entries)


def test_decorated_orbit_representatives_match_spike_edge_orbits():
    fixtures = [
        (0, 4, DecoratedGraph([0, 0], [[1, 2], [3, 4]], [(0, 1, 1)])),
        (1, 1, DecoratedGraph([0], [[1]], [(0, 0, 1)])),
        (1, 2, DecoratedGraph([0, 1], [[1, 2], []], [(0, 1, 1)])),
    ]
    for g, n, dg in fixtures:
        record = _record_from_decorated_graph(dg, g, n)
        assert _spike_orbit_sizes(record) == _adm_orbit_sizes(dg)
        assert len(automorphism_edge_orbit_indices(record)) == len(dg.edge_orbit_representatives())
        assert sum(_spike_orbit_sizes(record)) == record.num_edges()


def test_spike_m11_loop_branch_swap_orbit_sizes():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    record = loop.canonical_representative()
    decorated = _record_to_decorated_graph(record, 1, 1)
    assert _spike_orbit_sizes(record) == _adm_orbit_sizes(decorated)
    loop_flags = [flag for flag in record.flags_at(0) if record.flag_involution[flag] != flag]
    assert edges_are_in_same_orbit(record, (loop_flags[0], loop_flags[1]), (loop_flags[0], loop_flags[1]))


def test_spike_m12_banana_has_one_edge_orbit_class():
    types = StableGraphs(1, 2)
    banana = types.from_vertices(
        genera=(0, 0),
        markings=((1,), (2,)),
        edges=((0, 1), (0, 1)),
    )
    record = banana.canonical_representative()
    decorated = _record_to_decorated_graph(record, 1, 2)
    assert record.num_edges() == 2
    assert len(automorphism_edge_orbit_indices(record)) == 1
    assert len(decorated.edge_orbit_representatives()) == 1
    edges = record.internal_edges()
    assert edges_are_in_same_orbit(record, edges[0], edges[1])


def test_spike_m12_true_dumbbell_has_two_singleton_orbits():
    types = StableGraphs(1, 2)
    dumbbell = types.from_vertices(
        genera=(0, 0),
        markings=((), (1, 2)),
        edges=((0, 0), (0, 1)),
    )
    record = dumbbell.canonical_representative()
    decorated = _record_to_decorated_graph(record, 1, 2)
    assert _spike_orbit_sizes(record) == [1, 1]
    assert _adm_orbit_sizes(decorated) == [1, 1]
    edges = record.internal_edges()
    assert not edges_are_in_same_orbit(record, edges[0], edges[1])


def test_genus_six_orbits_match_admcycles_roundtrip():
    gamma = genus_six_counterexample()
    record = gamma.canonical_representative()
    decorated = _record_to_decorated_graph(record, 6, 0)
    spike_sizes = _spike_orbit_sizes(record)
    assert len(automorphism_edge_orbit_indices(record)) == len(decorated.edge_orbit_representatives()) == 8
    assert Counter(spike_sizes) == Counter(_adm_orbit_sizes(decorated))
    spike_multiset = Counter(
        (target.canonical_key(), size) for target, size in gamma.contraction_target_multiset()
    )
    assert spike_multiset == _adm_contraction_multiset(decorated, 6, 0)
    assert max(Counter(target.canonical_key() for target, _size in gamma.contraction_target_multiset()).values()) == 2
    assert len(gamma.covers()) == 7
