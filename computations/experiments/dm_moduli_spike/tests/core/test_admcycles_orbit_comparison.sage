r"""Independent admcycles edge-orbit comparison."""

from __future__ import annotations

from admcycles.decorated_graph import DecoratedGraph

from dm_moduli_spike import DMCompactificationModel
from dm_moduli_spike.backends.admcycles_decorated import _record_from_decorated_graph
from dm_moduli_spike.objects.edge_orbits import automorphism_edge_orbit_indices


def test_decorated_orbit_representatives_match_spike_edge_orbits():
    for g, n, dg in [
        (0, 4, DecoratedGraph([0, 0], [[1, 2], [3, 4]], [(0, 1, 1)])),
        (1, 1, DecoratedGraph([0], [[1]], [(0, 0, 1)])),
        (1, 2, DecoratedGraph([0, 0], [[1], [2]], [(0, 1, 2)])),
    ]:
        record = _record_from_decorated_graph(dg, g, n)
        gamma = DMCompactificationModel(g, n).curve_types()(record)
        spike_groups = automorphism_edge_orbit_indices(record)
        adm_reps = dg.edge_orbit_representatives()
        assert len(spike_groups) == len(adm_reps)
        assert sum(len(group) for group in spike_groups) == record.num_edges()
        assert sum(len(group) for group in spike_groups) == dg.num_edges()

        internal = record.internal_edges()
        for u, v, _size in adm_reps:
            matching = [
                index
                for index, (flag, partner) in enumerate(internal)
                if {record.flag_vertex[flag], record.flag_vertex[partner]} == {int(u), int(v)}
            ]
            assert matching, f"no spike edge matches admcycles orbit {(u, v, _size)}"
            orbit_index = next(index for index, group in enumerate(spike_groups) if matching[0] in group)
            group = spike_groups[orbit_index]
            assert all(index in group for index in matching)
