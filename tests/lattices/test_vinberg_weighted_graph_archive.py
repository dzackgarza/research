r"""Archive-required operations on owned projectively weighted Vinberg graphs."""

from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams
from dzack_research.preamble.categories.vinberg_invariants import (
    VinbergInvariantMatrices,
    projective_weighted_graph,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from sage.rings.integer_ring import ZZ as SageZZ


def test_induced_weighted_subgraph_retains_exact_vertex_and_edge_weights() -> None:
    matrix = VinbergInvariantMatrices().from_coxeter_diagram(
        CoxeterDiagrams().from_cartan_type(["A", 3])
    )
    graph = matrix.weighted_graph()
    vertices = tuple(graph.vertices())
    selected = (vertices[0], vertices[1])
    subgraph = graph.induced_subgraph(selected)

    assert tuple(subgraph.vertices()) == selected
    assert subgraph.is_symmetric()
    assert not subgraph.is_directed()
    for vertex in selected:
        assert subgraph.vertex_weight(vertex) == graph.vertex_weight(vertex)
    assert subgraph.edge_weight(*selected) == graph.edge_weight(*selected)


def test_symmetric_weighted_graph_round_trips_to_its_vinberg_invariants() -> None:
    original = VinbergInvariantMatrices().from_coxeter_diagram(
        CoxeterDiagrams().from_cartan_type(["A", 3])
    )
    reconstructed = original.weighted_graph().vinberg_invariant_matrix()

    assert tuple(reconstructed.index_set()) == tuple(original.index_set())
    for left in original.index_set():
        for right in original.index_set():
            assert (
                reconstructed.vinberg_invariant(left, right)
                == original.vinberg_invariant(left, right)
            )


def test_asymmetric_projective_graph_is_not_silently_read_as_a_vinberg_matrix() -> None:
    integers = _own_ring(SageZZ)
    graph = projective_weighted_graph(
        integers,
        ("a", "b"),
        {("a", "b"): (integers.one(), integers.one())},
        directed=True,
        symmetric=False,
    )

    try:
        graph.vinberg_invariant_matrix()
    except ValueError:
        pass
    else:
        raise AssertionError("an asymmetric weighted graph must not become a Vinberg matrix")
