r"""Shared Gram-matrix operations."""

from typing import Any

import networkx as nx


def _matrix_connected_component_cuts(G: Any) -> list[int]:
    r"""Return the cuts between consecutive connected diagonal blocks of \(G\)."""
    n = G.nrows()
    if n <= 1:
        return []

    adjacency = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if G[i, j] != 0:
                adjacency[i].append(j)
                adjacency[j].append(i)

    components = sorted(
        (sorted(component) for component in nx.connected_components(nx.Graph(adjacency))),
        key=lambda component: component[0],
    )
    if [i for component in components for i in component] != list(range(n)):
        return []

    cuts = []
    position = 0
    for component in components[:-1]:
        position += len(component)
        cuts.append(position)
    return cuts
