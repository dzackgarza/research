"""Shared operations on finite Gram tensors."""

from itertools import accumulate

import networkx as nx


def gram_tensor_graph(gram):
    r"""Return the weighted undirected graph presented by a symmetric Gram tensor."""
    if gram.tensor_valence() != (0, 2):
        raise TypeError("a Gram object is a type-(0,2) tensor")
    n, m = gram.tensor_shape()
    if n != m:
        raise ValueError("a Gram tensor is square")
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_weighted_edges_from(
        (i, j, gram[i, j])
        for i in range(n)
        for j in range(i, n)
        if gram[i, j] != 0
    )
    return graph


def gram_tensor_from_graph(graph, base_ring):
    r"""Recover the type-``(0,2)`` Gram tensor presented by a weighted graph."""
    from dzack_research.preamble.tensors.tensor import tensor

    vertices = sorted(graph.nodes)
    if vertices != list(range(len(vertices))):
        raise ValueError(
            "a Gram tensor graph uses framing positions 0,...,n-1; "
            f"got {vertices}"
        )
    values = [[base_ring.zero() for _ in vertices] for _ in vertices]
    for i, j, weight in graph.edges.data("weight"):
        values[i][j] = base_ring(weight)
        values[j][i] = base_ring(weight)
    return tensor(base_ring, (), (len(vertices), len(vertices)), values)


def tensor_connected_component_cuts(gram) -> list[int]:
    r"""Return cuts between consecutive connected diagonal blocks."""
    if gram.tensor_order() != 2:
        raise TypeError("connected block cuts require a two-index tensor")
    n = gram.tensor_shape()[0]
    if n <= 1:
        return []
    graph = gram_tensor_graph(gram)
    graph.remove_edges_from(list(nx.selfloop_edges(graph)))
    components = sorted(
        (sorted(component) for component in nx.connected_components(graph)),
        key=lambda component: component[0],
    )
    if [index for component in components for index in component] != list(range(n)):
        return []
    return list(accumulate(len(component) for component in components[:-1]))
