"""Shared operations on finite Gram tensors."""

from itertools import accumulate

import networkx as nx
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.tensors.tensor import tensor


class GramTensorGraph(SageObject):
    r"""The finite edge-weighted graph presenting one symmetric Gram tensor.

    Vertices are the ordered framing positions ``0,...,n-1``.  A nonzero
    pairing gives one undirected edge, with diagonal pairings represented by
    loops.  NetworkX is retained only as a private connectivity engine; the
    public object exposes the mathematical vertex/edge/weight data directly.

    The object is a graph ``(V, E, w)`` with weights ``w : E -> R``, an object
    of the category of edge-weighted graphs over ``R``; its order ``|V|`` is
    the cardinality of :meth:`vertices`.
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

    def edges(self):
        return finite_ordered_set(tuple(self._edge_weights))

    def has_edge(self, left, right) -> bool:
        key = (min(int(left), int(right)), max(int(left), int(right)))
        return key in self._edge_weights

    def edge_weight(self, left, right):
        r"""Return ``w({left, right})``, defined on the edges of this graph."""
        assert self.has_edge(left, right), "the selected Gram-graph vertices are not joined"
        return self._edge_weights[(min(int(left), int(right)), max(int(left), int(right)))]

    def tensor(self):
        r"""Recover the represented type-``(0,2)`` Gram tensor exactly.

        The entry at ``(i, j)`` is the weight of the edge ``{i, j}``, and zero
        where the two vertices are not joined: an absent edge is a zero
        pairing.
        """
        ring = self.base_ring()
        positions = range(int(self.vertices().cardinality()))
        size = len(positions)
        return tensor(
            ring,
            (),
            (size, size),
            tuple(
                tuple(
                    self.edge_weight(i, j) if self.has_edge(i, j) else ring.zero()
                    for j in positions
                )
                for i in positions
            ),
        )

    def _engine_graph(self):
        r"""Return the private NetworkX graph used for connectivity algorithms.

        Engine adapter (`OWN-06`): the one lowering of this graph into
        ``networkx.Graph``, consumed only by
        :func:`_tensor_connected_component_cuts`; no NetworkX object leaves it.
        """
        graph = nx.Graph()
        graph.add_nodes_from(tuple(self.vertices()))
        graph.add_weighted_edges_from(
            (left, right, weight)
            for (left, right), weight in self._edge_weights.items()
        )
        return graph

    def _repr_(self) -> str:
        return f"Gram graph on {self.vertices().cardinality()} framing positions"


def _gram_tensor_graph(gram):
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


def _tensor_connected_component_cuts(gram) -> list[int]:
    r"""Return cuts between consecutive connected diagonal blocks.

    Engine adapter (`OWN-06`): NetworkX computes the connected components of
    the Gram graph lowered by :meth:`GramTensorGraph._engine_graph`; only
    integer positions leave this function.
    """
    if gram.tensor_order() != 2:
        raise TypeError("connected block cuts require a two-index tensor")
    n = gram.tensor_shape()[0]
    if n <= 1:
        return []
    graph = gram.gram_graph()._engine_graph()
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
]
