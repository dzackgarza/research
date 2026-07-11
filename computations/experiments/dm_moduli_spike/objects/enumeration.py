r"""Enumeration of stable curve types by one-edge degeneration.

Starting from the unique smooth graph, every stable curve type is reached by a
sequence of one-edge degenerations.  There are exactly two forms, the reverses
of the two forms of a single-edge contraction:

* **nonseparating** -- pick a vertex ``v`` with ``w(v) > 0``, drop its genus by
  one and add a loop at ``v`` (reverse of contracting a loop);
* **vertex split** -- replace ``v`` by ``v1, v2`` with ``w(v1) + w(v2) = w(v)``,
  distribute the incident flags (including the two branches of existing loops)
  and the markings between them, and join ``v1, v2`` by a new edge (reverse of
  contracting a non-loop edge).

Every result is canonicalised and deduplicated by canonical key.  Completeness
follows by induction on the number of edges: contracting any edge of a graph
with ``r + 1`` edges gives a stable ``r``-edge graph already enumerated, and the
reverse operation is one of the two above.
"""

from __future__ import annotations

from collections.abc import Iterator
from itertools import combinations
from typing import TYPE_CHECKING

from .records import StableGraphRecord

if TYPE_CHECKING:
    from .curve_types import StableCurveType, StableCurveTypes


def _loop_degenerations(record: StableGraphRecord) -> Iterator[StableGraphRecord]:
    r"""Nonseparating degenerations: add a loop at a vertex of positive genus."""
    num_flags = record.num_flags()
    for vertex in range(record.num_vertices()):
        if record.vertex_genera[vertex] < 1:
            continue
        new_genera = list(record.vertex_genera)
        new_genera[vertex] -= 1
        new_flag_vertex = list(record.flag_vertex) + [vertex, vertex]
        new_flag_involution = list(record.flag_involution) + [num_flags + 1, num_flags]
        yield StableGraphRecord(
            vertex_genera=tuple(new_genera),
            flag_vertex=tuple(new_flag_vertex),
            flag_involution=tuple(new_flag_involution),
            marking_to_flag=record.marking_to_flag,
        )


def _split_degenerations(record: StableGraphRecord) -> Iterator[StableGraphRecord]:
    r"""Vertex-split degenerations: split a vertex into two joined by an edge."""
    num_flags = record.num_flags()
    for vertex in range(record.num_vertices()):
        weight = record.vertex_genera[vertex]
        flags_here = record.flags_at(vertex)
        other_vertices = [u for u in range(record.num_vertices()) if u != vertex]
        base_index = {u: i for i, u in enumerate(other_vertices)}
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
                    yield StableGraphRecord(
                        vertex_genera=tuple(new_genera),
                        flag_vertex=tuple(new_flag_vertex),
                        flag_involution=tuple(new_flag_involution),
                        marking_to_flag=record.marking_to_flag,
                    )


def one_edge_degenerations(gamma: StableCurveType) -> tuple[StableCurveType, ...]:
    r"""All rank ``+1`` degenerations of ``gamma``, deduplicated by canonical key."""
    parent = gamma.parent()
    record = gamma.record()
    seen: dict[object, StableCurveType] = {}
    for degeneration in (*_loop_degenerations(record), *_split_degenerations(record)):
        candidate = parent.from_record(degeneration)
        seen[candidate.canonical_key()] = candidate
    return tuple(seen.values())


def stable_curve_type_levels(parent: StableCurveTypes) -> list[dict[object, StableCurveType]]:
    r"""Rank buckets ``levels[r]`` (indexed by number of edges), each a mapping
    ``canonical_key -> StableCurveType``, generated rank by rank from the smooth
    graph up to codimension ``3g - 3 + n``."""
    dimension = parent.dimension()
    smooth = parent.smooth()
    levels: list[dict[object, StableCurveType]] = [{smooth.canonical_key(): smooth}]
    for _ in range(dimension):
        current = levels[-1]
        nxt: dict[object, StableCurveType] = {}
        for gamma in current.values():
            for delta in one_edge_degenerations(gamma):
                nxt[delta.canonical_key()] = delta
        if not nxt:
            break
        levels.append(nxt)
    return levels


def all_stable_curve_types(parent: StableCurveTypes) -> Iterator[StableCurveType]:
    for level in stable_curve_type_levels(parent):
        yield from level.values()
