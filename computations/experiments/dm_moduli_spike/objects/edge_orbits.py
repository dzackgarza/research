r"""Automorphism orbits of internal edges on a stable graph."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .automorphism_action import AutomorphismAction
from .records import StableGraph

if TYPE_CHECKING:
    from .contraction_orbits import ContractionOrbit
    from .contractions import StableGraphContraction
    from .graph_types import StableGraphType


def _is_identity_permutation(image: tuple[int, ...]) -> bool:
    return all(image[index] == index for index in range(len(image)))


def _edge_orbit_groups(action: AutomorphismAction, num_edges: int) -> tuple[tuple[int, ...], ...]:
    r"""Partition ``0, ..., num_edges - 1`` into orbits under ``Aut(\Gamma)``."""
    if num_edges == 0:
        return ()
    if int(action.group().order()) == 1:
        return tuple((index,) for index in range(num_edges))
    from sage.combinat.permutation import Permutation
    from sage.groups.perm_gps.permgroup import PermutationGroup

    generators = [Permutation([value + 1 for value in image]) for image in action.on_edges() if not _is_identity_permutation(image)]
    if not generators:
        return tuple((index,) for index in range(num_edges))
    group = PermutationGroup(generators)
    orbits = group.orbits()
    edge_orbits = tuple(
        tuple(sorted(int(index) - 1 for index in orbit if 1 <= int(index) <= num_edges)) for orbit in orbits if any(1 <= int(index) <= num_edges for index in orbit)
    )
    covered = {index for orbit in edge_orbits for index in orbit}
    singletons = tuple((index,) for index in range(num_edges) if index not in covered)
    return tuple(sorted(edge_orbits + singletons, key=lambda orbit: orbit[0]))


def automorphism_edge_orbits(record: StableGraph) -> tuple[tuple[tuple[int, int], ...], ...]:
    r"""Return internal edges grouped by the action of ``Aut(\Gamma)``."""
    edges = record.internal_edges()
    if not edges:
        return ()
    action = AutomorphismAction.from_graph(record)
    groups = _edge_orbit_groups(action, len(edges))
    return tuple(tuple(edges[index] for index in group) for group in groups)


def automorphism_edge_orbit_indices(record: StableGraph) -> tuple[tuple[int, ...], ...]:
    r"""Edge-index orbits aligned with :meth:`StableGraph.internal_edges`."""
    edges = record.internal_edges()
    if not edges:
        return ()
    action = AutomorphismAction.from_graph(record)
    return _edge_orbit_groups(action, len(edges))


def _contraction_witness_from_decorated(
    graph: StableGraph,
    edge: tuple[int, int],
    g: int,
    n: int,
) -> StableGraphContraction:
    from ..backends.admcycles_decorated import (
        _record_to_decorated_graph,
        contraction_from_decorated_morphism,
    )

    decorated = _record_to_decorated_graph(graph, g, n)
    u = graph.flag_vertex[edge[0]]
    v = graph.flag_vertex[edge[1]]
    key_u, key_v = (u, v) if u <= v else (v, u)
    morphism = decorated.edge_contraction_morphism([(key_u, key_v, 1)])  # type: ignore[attr-defined]
    return contraction_from_decorated_morphism(morphism, g, n, domain_graph=graph)


def elementary_contraction_orbits(source: StableGraphType) -> tuple[ContractionOrbit, ...]:
    r"""Elementary Aut edge orbits with optional ``admcycles`` morphism witnesses."""
    from .contraction_orbits import ContractionOrbit

    parent = source.parent()
    g = parent.genus()
    n = parent.number_of_markings()
    graph = source.canonical_representative()
    edges = graph.internal_edges()
    use_decorated = False
    try:
        from ..backends.admcycles_decorated import _require_decorated_module

        _require_decorated_module()
        use_decorated = True
    except ImportError:
        pass

    orbits: list[ContractionOrbit] = []
    for group in automorphism_edge_orbit_indices(graph):
        representative = edges[group[0]]
        if use_decorated:
            contraction = _contraction_witness_from_decorated(graph, representative, g, n)
        else:
            _, contraction = graph.contract(representative)
        target = parent(contraction.target_type())
        orbits.append(ContractionOrbit(source, target, contraction, len(group)))
    return tuple(orbits)
