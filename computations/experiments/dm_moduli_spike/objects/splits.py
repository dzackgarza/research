r"""Stable split systems for genus-zero phylogenetic dual trees.

For a stable genus-zero dual graph, internal edges induce stable splits of the
marking set.  The implementation is independent of canonical labelling: each
edge is removed combinatorially and the marking labels on each component are
read off directly from the half-edge record.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .stable_graphs import StableGraph


def canonicalize_split(
    side: frozenset[int] | set[int],
    *,
    n: int,
    anchor_marking: int = 1,
) -> frozenset[int]:
    r"""Return the unique representative of a split.

    Each split is stored as the side containing ``anchor_marking``.
    """
    side = frozenset(side)
    ground = frozenset(range(1, n + 1))
    assert side.issubset(ground), f"split side {side} is not contained in {{1, ..., {n}}}"
    complement = ground - side
    if anchor_marking in side:
        return side
    return complement


def split_system(gamma: StableGraph, anchor_marking: int = 1) -> frozenset[frozenset[int]]:
    r"""The stable splits induced by internal edges of a genus-zero dual tree."""
    record = gamma.canonical_representative()
    assert gamma.total_genus() == 0, "split systems are defined for genus-zero stable graphs"
    n = record.num_markings()
    splits: set[frozenset[int]] = set()

    for removed in record.internal_edges():
        adjacency: list[set[int]] = [set() for _ in range(record.num_vertices())]
        for flag, partner in record.internal_edges():
            if (flag, partner) == removed or (partner, flag) == removed:
                continue
            u = record.flag_vertex[flag]
            v = record.flag_vertex[partner]
            if u != v:
                adjacency[u].add(v)
                adjacency[v].add(u)

        seen: set[int] = set()
        for start in range(record.num_vertices()):
            if start in seen:
                continue
            component: set[int] = set()
            stack = [start]
            while stack:
                vertex = stack.pop()
                if vertex in component:
                    continue
                component.add(vertex)
                seen.add(vertex)
                stack.extend(adjacency[vertex] - component)
            side = frozenset(marking for vertex in component for marking in record.markings_at(vertex))
            if 2 <= len(side) <= n - 2:
                splits.add(canonicalize_split(side, n=n, anchor_marking=anchor_marking))

    return frozenset(splits)
