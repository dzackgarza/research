r"""Graph and labelled-graph owners distinguish adjacency and labels."""

import pytest

from dzack_research.preamble.categories.graph_categories import (
    Digraphs,
    Graphs,
    LabelledDigraphs,
    LabelledGraphs,
)


def test_undirected_graphs_are_symmetric_digraphs() -> None:
    graph = Graphs().from_edges((0, 1), ((0, 1),))

    assert graph in Graphs()
    assert graph in Digraphs()
    assert graph.has_edge(0, 1)
    assert graph.has_edge(1, 0)


def test_digraph_mor_rejects_a_vertex_map_that_destroys_an_arc() -> None:
    source = Digraphs().from_edges((0, 1), ((0, 1),))
    target = Digraphs().from_edges((0, 1), ())

    with pytest.raises(ValueError, match="preserve directed adjacency"):
        Digraphs().Mor(source, target)(lambda vertex: vertex)


def test_labelled_graph_mor_preserves_edge_labels() -> None:
    source = LabelledGraphs().an_object()
    target = LabelledGraphs().from_labels(
        (0, 1),
        ((0, 1),),
        {0: "left", 1: "right"},
        {(0, 1): "different"},
    )

    with pytest.raises(ValueError, match="preserve edge labels"):
        LabelledGraphs().Mor(source, target)(lambda vertex: vertex)


def test_labelled_graphs_are_labelled_digraphs() -> None:
    graph = LabelledGraphs().an_object()

    assert graph in LabelledGraphs()
    assert graph in LabelledDigraphs()
