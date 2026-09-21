r"""Archive reconciliation for mixed tensor contraction, trace and products."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.tensors import tensor

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/test_tensors.sage",
        "live_owner": "tests/tensors/test_tensors.py",
        "owner_overrides": {
            "test_the_gram_matrix_is_the_forms_covariant_tensor": "tests/lattices/test_module_generators.py",
            "test_a_unimodular_form_raises_and_lowers_an_index": "tests/tensors/test_tensor_index_archive_reconciliation.py",
            "test_raising_an_integral_index_requires_unimodularity": "tests/tensors/test_tensor_index_archive_reconciliation.py",
            "test_a_nondegenerate_lattice_raises_indices_after_rationalization": "tests/tensors/test_tensor_index_archive_reconciliation.py",
            "test_the_correlation_is_an_isomorphism_exactly_when_unimodular": "tests/tensors/test_tensor_index_archive_reconciliation.py",
            "test_mixed_tensors_are_the_homogeneous_pieces_of_one_bigraded_algebra": "tests/tensors/test_mixed_tensor_algebra_archive.py",
            "test_covariant_slots_use_the_dual_module": "src/dzack_research/preamble/tensors/tensor.py",
            "test_a_tensor_piece_is_the_tensor_product_of_powers_of_a_module_and_its_dual": "src/dzack_research/preamble/tensors/tensor.py",
            "test_the_degree_two_piece_of_the_tensor_algebra_is_the_tensor_square": "src/dzack_research/preamble/categories/algebras/framed_free_algebras.py",
        },
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/modules/tensors.sage",
        "live_owner": "src/dzack_research/preamble/tensors/tensor.py",
        "owner_overrides": {
            "TensorPower": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "SymmetricPower": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "AlternatingPower": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "DividedPower": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "DividedSquare": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "divided_power_invariant_inclusion": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "tensor_power_polarization": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "tensor_power_permutation": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "divided_square_invariant_inclusion": "src/dzack_research/preamble/categories/modules/pure/modules.py",
            "tensor_square_polarization": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def test_archive_trace_of_identity_is_rank() -> None:
    identity = tensor(ZZ, (2,), (2,), [[1, 0], [0, 1]])
    assert identity.trace() == 2


def test_archive_vector_covector_contraction_is_pairing() -> None:
    vector = tensor.vector(ZZ, [2, 3])
    covector = tensor.covector(ZZ, [5, 7])
    assert vector.contract(covector) == 31
    assert covector.contract(vector) == 31


def test_archive_partial_contraction_preserves_remaining_variance() -> None:
    left = tensor(ZZ, (2, 2), (), [[1, 0], [0, 1]])
    covector = tensor.covector(ZZ, [4, 9])
    contracted = left.contract(covector, slot=1)

    assert contracted.tensor_valence() == (1, 0)
    assert contracted == tensor.vector(ZZ, [4, 9])


def test_archive_tensor_product_orders_upper_slots_before_lower_slots() -> None:
    vector = tensor.vector(ZZ, [2, 3])
    covector = tensor.covector(ZZ, [5, 7])
    product = vector.tensor_product(covector)

    assert product.tensor_valence() == (1, 1)
    assert product == tensor(ZZ, (2,), (2,), [[10, 14], [15, 21]])
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
    assert traced == tensor.vector(ZZ, [1, 1])


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
