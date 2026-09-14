"""Shared operations on finite Gram tensors."""

from itertools import accumulate

import networkx as nx
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.tensors.tensor import tensor


class GramTensorGraph(SageObject):
    r"""The finite weighted graph presenting one symmetric Gram tensor.

    Vertices are the ordered framing positions ``0,...,n-1``.  A nonzero
    pairing gives one undirected edge, with diagonal pairings represented by
    loops.  NetworkX is retained only as a private connectivity engine; the
    public object exposes the mathematical vertex/edge/weight data directly.
    """

    def __init__(self, base_ring, vertex_count, edge_weights) -> None:
        self._base_ring = base_ring
        self._vertices = finite_ordered_set(tuple(range(int(vertex_count))))
        normalized = {}
        for pair, weight in dict(edge_weights).items():
            left, right = pair
            if left not in self._vertices or right not in self._vertices:
                raise ValueError("a Gram-graph edge joins two framing positions")
            key = (min(int(left), int(right)), max(int(left), int(right)))
            value = base_ring(weight)
            if value == base_ring.zero():
                continue
            previous = normalized.get(key)
            if previous is not None and previous != value:
                raise ValueError("one Gram-graph edge cannot carry two different weights")
            normalized[key] = value
        self._edge_weights = normalized

    def base_ring(self):
        return self._base_ring

    def vertices(self):
        return self._vertices

    def cardinality(self):
        return self.vertices().cardinality()

    def edges(self):
        return finite_ordered_set(tuple(self._edge_weights))

    def has_edge(self, left, right) -> bool:
        key = (min(int(left), int(right)), max(int(left), int(right)))
        return key in self._edge_weights

    def edge_weight(self, left, right):
        key = (min(int(left), int(right)), max(int(left), int(right)))
        try:
            return self._edge_weights[key]
        except KeyError as error:
            raise ValueError("the selected Gram-graph vertices are not joined") from error

    def tensor(self):
        r"""Recover the represented type-``(0,2)`` Gram tensor exactly."""
        return gram_tensor_from_graph(self, self.base_ring())

    def _engine_graph(self):
        r"""Return the private NetworkX graph used for connectivity algorithms."""
        graph = nx.Graph()
        graph.add_nodes_from(tuple(self.vertices()))
        graph.add_weighted_edges_from(
            (left, right, weight)
            for (left, right), weight in self._edge_weights.items()
        )
        return graph

    def _repr_(self) -> str:
        return f"Gram graph on {self.cardinality()} framing positions"


def gram_tensor_graph(gram):
    r"""Return the owned weighted graph presented by a symmetric Gram tensor."""
    if gram.tensor_valence() != (NN**2)((0, 2)):
        raise TypeError("a Gram object is a type-(0,2) tensor")
    n, m = gram.tensor_shape()
    if n != m:
        raise ValueError("a Gram tensor is square")
    return GramTensorGraph(
        gram.base_ring(),
        n,
        {
            (i, j): gram[i, j]
            for i in range(n)
            for j in range(i, n)
            if gram[i, j] != 0
        },
    )


def gram_tensor_from_graph(graph, base_ring):
    r"""Recover the type-``(0,2)`` Gram tensor presented by a weighted graph."""
    if isinstance(graph, GramTensorGraph):
        vertices = tuple(graph.vertices())
        edges = tuple(
            (left, right, graph.edge_weight(left, right))
            for left, right in graph.edges()
        )
    else:
        vertices = tuple(sorted(graph.nodes))
        edges = tuple(graph.edges.data("weight"))
    if vertices != tuple(range(len(vertices))):
        raise ValueError(
            "a Gram tensor graph uses framing positions 0,...,n-1; "
            f"got {vertices}"
        )
    values = [[base_ring.zero() for _ in vertices] for _ in vertices]
    for i, j, weight in edges:
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
    graph = gram_tensor_graph(gram)._engine_graph()
    graph.remove_edges_from(list(nx.selfloop_edges(graph)))
    components = sorted(
        (sorted(component) for component in nx.connected_components(graph)),
        key=lambda component: component[0],
    )
    if [index for component in components for index in component] != list(range(n)):
        return []
    return list(accumulate(len(component) for component in components[:-1]))


__all__ = [
    "GramTensorGraph",
    "gram_tensor_from_graph",
    "gram_tensor_graph",
    "tensor_connected_component_cuts",
]
