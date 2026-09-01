r"""Shared Gram-matrix operations."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import Parent

    from dzack_research.preamble.lexicon import GramMatrix

from itertools import accumulate
import networkx as nx


def gram_matrix_graph(G: "GramMatrix") -> "nx.Graph":
    r"""Return the weighted graph presenting \(G\).

    The vertices are the framing's positions; the edge \(\{i,j\}\) carries
    the pairing \(b(e_i,e_j)\) as its weight and is present exactly when
    that pairing is nonzero, the diagonal appearing as loops carrying the
    squares \(b(e_i,e_i)\).  This is the Coxeter/Dynkin picture read off an
    arbitrary Gram matrix rather than off a root system: the same datum in a
    second presentation, from which :func:`gram_matrix_from_graph` recovers
    the matrix.  Symmetry of the form is what makes the graph undirected --
    the source corpus this came from built a digraph because it also carried
    skew forms, and there the two arcs of a pair carry opposite weights.
    """
    n = G.nrows()
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_weighted_edges_from(
        (i, j, G[i, j])
        for i in range(n)
        for j in range(i, n)
        if G[i, j] != 0
    )
    return graph


def gram_matrix_from_graph(graph: "nx.Graph", base_ring: "Parent") -> "GramMatrix":
    r"""Return the Gram matrix a weighted graph presents, over ``base_ring``.

    Inverse to :func:`gram_matrix_graph` on the graphs it produces: a vertex
    set \(\{0,\dots,n-1\}\), an absent edge meaning a zero pairing, and a
    loop meaning a square.
    """
    from sage.matrix.constructor import matrix

    vertices = sorted(graph.nodes)
    assert vertices == list(range(len(vertices))), (
        "a Gram matrix is presented on the framing positions "
        f"0..n-1; this graph's vertices are {vertices}"
    )
    G = matrix(base_ring, len(vertices))
    for i, j, weight in graph.edges.data("weight"):
        G[i, j] = weight
        G[j, i] = weight
    return G


def _matrix_connected_component_cuts(G: "GramMatrix") -> list[int]:
    r"""Return the cuts between consecutive connected diagonal blocks of \(G\)."""
    n = G.nrows()
    if n <= 1:
        return []

    graph = gram_matrix_graph(G)
    graph.remove_edges_from(list(nx.selfloop_edges(graph)))

    components = sorted(
        (sorted(component) for component in nx.connected_components(graph)),
        key=lambda component: component[0],
    )
    if [i for component in components for i in component] != list(range(n)):
        return []

    return list(accumulate(len(component) for component in components[:-1]))
