r"""Enumeration of stable graphs by one-edge degeneration."""

from __future__ import annotations

from collections.abc import Iterator
from itertools import combinations
from typing import TYPE_CHECKING

from .records import _GraphRecord

if TYPE_CHECKING:
    from .stable_graphs import StableGraph, StableGraphs


def _loop_degenerations(record: _GraphRecord) -> Iterator[_GraphRecord]:
    num_flags = record.num_flags()
    for vertex in range(record.num_vertices()):
        if record.vertex_genera[vertex] < 1:
            continue
        new_genera = list(record.vertex_genera)
        new_genera[vertex] -= 1
        new_flag_vertex = list(record.flag_vertex) + [vertex, vertex]
        new_flag_involution = list(record.flag_involution) + [num_flags + 1, num_flags]
        yield _GraphRecord(
            vertex_genera=tuple(new_genera),
            flag_vertex=tuple(new_flag_vertex),
            flag_involution=tuple(new_flag_involution),
            marking_to_flag=record.marking_to_flag,
        )


def _split_degenerations(record: _GraphRecord) -> Iterator[_GraphRecord]:
    num_flags = record.num_flags()
    for vertex in range(record.num_vertices()):
        weight = record.vertex_genera[vertex]
        flags_here = record.flags_at(vertex)
        other_vertices = [u for u in range(record.num_vertices()) if u != vertex]
        base_index = {u: index for index, u in enumerate(other_vertices)}
        v1 = len(other_vertices)
        v2 = v1 + 1
        for genus_one in range(weight + 1):
            genus_two = weight - genus_one
            for size in range(len(flags_here) + 1):
                for subset in combinations(flags_here, size):
                    on_v1 = set(subset)
                    valence_one = len(on_v1) + 1
                    valence_two = (len(flags_here) - len(on_v1)) + 1
                    if 2 * genus_one - 2 + valence_one <= 0:
                        continue
                    if 2 * genus_two - 2 + valence_two <= 0:
                        continue
                    new_genera = [record.vertex_genera[u] for u in other_vertices] + [genus_one, genus_two]
                    new_flag_vertex = []
                    for flag in range(num_flags):
                        old_vertex = record.flag_vertex[flag]
                        if old_vertex != vertex:
                            new_flag_vertex.append(base_index[old_vertex])
                        else:
                            new_flag_vertex.append(v1 if flag in on_v1 else v2)
                    new_flag_vertex += [v1, v2]
                    new_flag_involution = list(record.flag_involution) + [num_flags + 1, num_flags]
                    yield _GraphRecord(
                        vertex_genera=tuple(new_genera),
                        flag_vertex=tuple(new_flag_vertex),
                        flag_involution=tuple(new_flag_involution),
                        marking_to_flag=record.marking_to_flag,
                    )


def one_edge_degenerations(gamma: StableGraph) -> tuple[StableGraph, ...]:
    parent = gamma.parent()
    record = gamma._canonical_record()
    seen: dict[object, StableGraph] = {}
    for degeneration in (*_loop_degenerations(record), *_split_degenerations(record)):
        candidate = parent.from_graph(degeneration)
        seen[candidate.canonical_key()] = candidate
    return tuple(seen.values())


def stable_curve_type_levels(parent: StableGraphs) -> list[dict[object, StableGraph]]:
    dimension = parent.dimension()
    smooth = parent.smooth()
    levels: list[dict[object, StableGraph]] = [{smooth.canonical_key(): smooth}]
    for _ in range(dimension):
        current = levels[-1]
        nxt: dict[object, StableGraph] = {}
        for gamma in current.values():
            for delta in one_edge_degenerations(gamma):
                nxt[delta.canonical_key()] = delta
        if not nxt:
            break
        levels.append(nxt)
    return levels


def all_stable_curve_types(parent: StableGraphs) -> Iterator[StableGraph]:
    for level in stable_curve_type_levels(parent):
        yield from level.values()
