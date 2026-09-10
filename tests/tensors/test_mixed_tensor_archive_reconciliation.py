r"""Archive reconciliation for mixed tensor contraction, trace and products."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.tensors import tensor


def test_archive_trace_of_identity_is_rank() -> None:
    identity = tensor(ZZ, (2,), (2,), [[1, 0], [0, 1]])
    assert identity.trace() == 2


def test_archive_vector_covector_contraction_is_pairing() -> None:
    vector = tensor.vector(ZZ, [2, 3])
    covector = tensor.covector(ZZ, [5, 7])
    assert vector.contract(covector) == 31
    assert covector.contract(vector) == 31


def test_archive_partial_contraction_preserves_remaining_variance() -> None:
    left = tensor(ZZ, (2, 2), (), [[[1, 0], [0, 1]][i][j] for j in range(2)] for i in range(2)])
    covector = tensor.covector(ZZ, [4, 9])
    contracted = left.contract(covector, slot=1)

    assert contracted.tensor_valence() == (1, 0)
    assert contracted.list() == [4, 9]


def test_archive_tensor_product_orders_upper_slots_before_lower_slots() -> None:
    vector = tensor.vector(ZZ, [2, 3])
    covector = tensor.covector(ZZ, [5, 7])
    product = vector.tensor_product(covector)

    assert product.tensor_valence() == (1, 1)
    assert product.components() == [[10, 14], [15, 21]]
    assert product.trace() == 31


def test_trace_can_leave_a_mixed_tensor() -> None:
    tensor_three = tensor(
        ZZ,
        (2, 2),
        (2,),
        [
            [[1, 0], [0, 0]],
            [[0, 0], [0, 1]],
        ],
    )
    traced = tensor_three.trace(slot=1, other_slot=0)
    assert traced.tensor_valence() == (1, 0)
    assert traced.list() == [1, 1]


def test_archive_tensor_evaluation_is_partial_in_covariant_slots() -> None:
    multiplication = tensor(
        ZZ,
        (2,),
        (2, 2),
        [
            [[1, 0], [0, 1]],
            [[0, 1], [1, 0]],
        ],
    )
    vector = tensor.vector(ZZ, [2, 3])

    partially_evaluated = multiplication(vector)
    assert partially_evaluated.tensor_valence() == (1, 1)
    assert multiplication() is multiplication

    fully_evaluated = partially_evaluated(vector)
    assert fully_evaluated.tensor_valence() == (1, 0)
    assert fully_evaluated == multiplication(vector, vector)


def test_archive_covariant_partial_evaluation_stays_a_covector() -> None:
    form = tensor(ZZ, (), (2, 2), [[1, 2], [3, 4]])
    vector = tensor.vector(ZZ, [5, 7])

    covector = form(vector)
    assert covector.tensor_valence() == (0, 1)
    assert covector(vector) == form(vector, vector)
