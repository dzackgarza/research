r"""Independent admcycles edge-orbit comparison."""

from __future__ import annotations

from collections import Counter

from admcycles.decorated_graph import DecoratedGraph

from dm_moduli_spike import StableGraphTypes
from dm_moduli_spike.backends.admcycles_decorated import (
    _record_from_decorated_graph,
    _record_to_decorated_graph,
)
from dm_moduli_spike.objects.edge_orbits import automorphism_edge_orbit_indices
from tests.support.fixtures import genus_six_counterexample


def _spike_orbit_sizes(record):
    return sorted(len(group) for group in automorphism_edge_orbit_indices(record))


def _adm_orbit_sizes(dg):
    return sorted(int(size) for _u, _v, size in dg.edge_orbit_representatives())


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


def test_spike_m12_loop_edge_roundtrip_orbit_sizes():
    types = StableGraphTypes(1, 2)
    loop_edge = types.from_vertices(
        genera=(0, 0),
        markings=((), (1, 2)),
        edges=((0, 0), (0, 1)),
    )
    record = loop_edge.canonical_representative()
    decorated = _record_to_decorated_graph(record, 1, 2)
    assert _spike_orbit_sizes(record) == _adm_orbit_sizes(decorated)


def test_spike_m12_dumbbell_has_one_edge_orbit_class():
    types = StableGraphTypes(1, 2)
    dumbbell = types.from_vertices(
        genera=(0, 0),
        markings=((1,), (2,)),
        edges=((0, 1), (0, 1)),
    )
    record = dumbbell.canonical_representative()
    decorated = _record_to_decorated_graph(record, 1, 2)
    assert record.num_edges() == 2
    assert len(automorphism_edge_orbit_indices(record)) == 1
    assert len(decorated.edge_orbit_representatives()) == 1


def test_genus_six_orbits_match_admcycles_roundtrip():
    gamma = genus_six_counterexample()
    record = gamma.canonical_representative()
    decorated = _record_to_decorated_graph(record, 6, 0)
    spike_sizes = _spike_orbit_sizes(record)
    assert len(automorphism_edge_orbit_indices(record)) == len(decorated.edge_orbit_representatives()) == 8
    assert Counter(spike_sizes) == Counter(_adm_orbit_sizes(decorated))
    assert max(Counter(orbit.target().canonical_key() for orbit in gamma.elementary_contraction_orbits()).values()) == 2
    assert len(gamma.covers()) == 7
