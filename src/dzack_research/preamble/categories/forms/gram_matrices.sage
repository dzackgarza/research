r"""Shared Gram-matrix operations."""

from itertools import accumulate
import networkx as nx


def _matrix_connected_component_cuts(G: "GramMatrix") -> list[int]:
    r"""Return the cuts between consecutive connected diagonal blocks of \(G\)."""
    n = G.nrows()
    if n <= 1:
        return []

    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if G[i, j] != 0
    )

    components = sorted(
        (sorted(component) for component in nx.connected_components(graph)),
        key=lambda component: component[0],
    )
    if [i for component in components for i in component] != list(range(n)):
        return []

    return list(accumulate(len(component) for component in components[:-1]))
