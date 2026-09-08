from dzack_research.preamble.categories.forms.gram_matrices import (
    gram_tensor_from_graph,
    gram_tensor_graph,
    tensor_connected_component_cuts,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.tensors.tensor import tensor
from sage.rings.integer_ring import ZZ as SageZZ


def test_archived_gram_graph_round_trip_preserves_loops_and_pairings() -> None:
    integers = _own_ring(SageZZ)
    gram = tensor(
        integers,
        (),
        (3, 3),
        (
            (2, 1, 0),
            (1, 3, 0),
            (0, 0, 5),
        ),
    )

    graph = gram_tensor_graph(gram)
    assert graph.has_edge(0, 0)
    assert graph[0][0]["weight"] == 2
    assert graph.has_edge(0, 1)
    assert graph[0][1]["weight"] == 1
    assert not graph.has_edge(0, 2)

    recovered = gram_tensor_from_graph(graph, integers)
    assert recovered.is_equal_tensor(gram)


def test_archived_connected_block_cuts_require_consecutive_components() -> None:
    integers = _own_ring(SageZZ)
    consecutive = tensor(
        integers,
        (),
        (3, 3),
        (
            (2, 1, 0),
            (1, 2, 0),
            (0, 0, 4),
        ),
    )
    interlaced = tensor(
        integers,
        (),
        (3, 3),
        (
            (2, 0, 1),
            (0, 4, 0),
            (1, 0, 2),
        ),
    )

    assert tensor_connected_component_cuts(consecutive) == [2]
    assert tensor_connected_component_cuts(interlaced) == []
