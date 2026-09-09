r"""Archive reconciliation for reversible weighted Gram-graph presentations."""

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.forms.gram_matrices import (
    GramTensorGraph,
    gram_tensor_from_graph,
    gram_tensor_graph,
)


def test_gram_graph_retains_squares_pairings_and_recovers_the_tensor() -> None:
    lattice = Lattices(ZZ)("A2")
    gram = lattice.gram_tensor()
    graph = gram_tensor_graph(gram)

    assert isinstance(graph, GramTensorGraph)
    assert tuple(graph.vertices()) == (0, 1)
    assert graph.edge_weight(0, 0) == gram[0, 0]
    assert graph.edge_weight(1, 1) == gram[1, 1]
    assert graph.edge_weight(0, 1) == gram[0, 1]
    assert graph.tensor() == gram
    assert gram_tensor_from_graph(graph, ZZ) == gram


def test_absent_edge_means_zero_pairing_and_disconnected_blocks_are_retained() -> None:
    lattice = Lattices(ZZ)("A1") + Lattices(ZZ)("A1")
    graph = gram_tensor_graph(lattice.gram_tensor())

    assert not graph.has_edge(0, 1)
    assert graph.edges().cardinality() == 2
    assert graph.tensor() == lattice.gram_tensor()
