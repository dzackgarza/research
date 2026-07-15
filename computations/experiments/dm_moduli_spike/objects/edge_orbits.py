r"""Automorphism orbits of internal edges on a stable graph."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .._sage_types import SagePermutationGroup
from .._typing_utils import as_int
from .records import _GraphRecord

if TYPE_CHECKING:
    from .contractions import StableGraphContraction
    from .stable_graphs import StableGraph


def automorphism_edge_orbit_indices(record: _GraphRecord) -> tuple[tuple[int, ...], ...]:
    r"""Edge-index orbits aligned with :meth:`StableGraph.internal_edges`."""
    num_edges = record.num_edges()
    if num_edges == 0:
        return ()
    group = record.automorphism_group(on="edges")
    assert isinstance(group, SagePermutationGroup), (
        f"automorphism_group(on='edges') must return a Sage permutation group; found {type(group)!r}; owned boundary=automorphism_edge_orbit_indices"
    )
    if as_int(group.order()) == 1:
        return tuple((index,) for index in range(num_edges))
    orbits = group.orbits()
    edge_orbits = tuple(
        tuple(sorted(as_int(index) - 1 for index in orbit if 1 <= as_int(index) <= num_edges)) for orbit in orbits if any(1 <= as_int(index) <= num_edges for index in orbit)
    )
    covered = {index for orbit in edge_orbits for index in orbit}
    singletons = tuple((index,) for index in range(num_edges) if index not in covered)
    return tuple(sorted(edge_orbits + singletons, key=lambda orbit: orbit[0]))


def automorphism_edge_orbits(record: _GraphRecord) -> tuple[tuple[tuple[int, int], ...], ...]:
    r"""Return internal edges grouped by the action of ``Aut(\Gamma)``."""
    edges = record.internal_edges()
    if not edges:
        return ()
    groups = automorphism_edge_orbit_indices(record)
    return tuple(tuple(edges[index] for index in group) for group in groups)


def edges_are_in_same_orbit(record: _GraphRecord, edge_a: tuple[int, int], edge_b: tuple[int, int]) -> bool:
    r"""Whether two internal edges lie in the same ``Aut(\Gamma)`` orbit."""
    edges = record.internal_edges()
    index_a = edges.index(edge_a)
    index_b = edges.index(edge_b)
    for group in automorphism_edge_orbit_indices(record):
        if index_a in group and index_b in group:
            return True
    return False


def contraction_target_multiset(source: StableGraph) -> tuple[tuple[StableGraph, int], ...]:
    r"""Multiset of distinct targets ``([Gamma/e], |O_e|)`` over Aut edge orbits."""
    parent = source.parent()
    graph = source._canonical_record()
    entries: list[tuple[StableGraph, int]] = []
    for group in automorphism_edge_orbit_indices(graph):
        representative = graph.internal_edges()[group[0]]
        target_type, _ = graph.contract(representative)
        entries.append((parent(target_type), len(group)))
    return tuple(entries)


def _contraction_witness_from_decorated(
    graph: _GraphRecord,
    edge: tuple[int, int],
    g: int,
    n: int,
) -> StableGraphContraction:
    from .._admcycles.admcycles_decorated import (
        _record_to_decorated_graph,
        contraction_from_decorated_morphism,
    )

    decorated = _record_to_decorated_graph(graph, g, n)
    u = graph.flag_vertex[edge[0]]
    v = graph.flag_vertex[edge[1]]
    key_u, key_v = (u, v) if u <= v else (v, u)
    assert hasattr(decorated, "edge_contraction_morphism"), (
        f"decorated graph must expose edge_contraction_morphism; found {type(decorated)!r}; owned boundary=_contraction_witness_from_decorated"
    )
    morphism = decorated.edge_contraction_morphism([(key_u, key_v, 1)])
    return contraction_from_decorated_morphism(morphism, g, n, domain_graph=graph)


def _elementary_contraction_data(source: StableGraph) -> tuple[tuple[StableGraph, StableGraphContraction, int], ...]:
    r"""Internal: one Aut edge orbit -> (target type, witness, orbit size)."""
    parent = source.parent()
    g = parent.genus()
    n = parent.number_of_markings()
    graph = source._canonical_record()
    edges = graph.internal_edges()
    from .._admcycles.admcycles_decorated import AdmcyclesDecoratedGraphs

    use_decorated = AdmcyclesDecoratedGraphs().is_available()

    data: list[tuple[StableGraph, StableGraphContraction, int]] = []
    for group in automorphism_edge_orbit_indices(graph):
        representative = edges[group[0]]
        if use_decorated:
            contraction = _contraction_witness_from_decorated(graph, representative, g, n)
        else:
            _, contraction = graph.contract(representative)
        target = parent(contraction.target_type())
        data.append((target, contraction, len(group)))
    return tuple(data)
