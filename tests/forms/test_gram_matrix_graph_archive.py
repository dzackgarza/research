from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.tensors.tensor import tensor

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/forms/gram_matrices.sage",
    "live_owner": "src/dzack_research/preamble/categories/forms/gram_matrices.py",
    "owner_overrides": {
        "gram_tensor_graph": "src/dzack_research/preamble/tensors/tensor.py",
        "gram_tensor_from_graph": "src/dzack_research/preamble/categories/forms/gram_matrices.py",
        "tensor_connected_component_cuts": "src/dzack_research/preamble/tensors/tensor.py",
    },
    "disposition": "reconciled-live-owner",
}


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

    graph = gram.gram_graph()
    assert graph.has_edge(0, 0)
    assert graph.edge_weight(0, 0) == integers(2)
    assert graph.has_edge(0, 1)
    assert graph.edge_weight(0, 1) == integers(1)
    assert not graph.has_edge(0, 2)

    recovered = graph.tensor()
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

    assert tuple(consecutive.gram_connected_component_cuts()) == (2,)
    assert interlaced.gram_connected_component_cuts().cardinality() == 0
