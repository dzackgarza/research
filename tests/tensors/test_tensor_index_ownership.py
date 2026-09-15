from dzack_research.preamble.all import NN, ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModule
from dzack_research.preamble.tensors.tensor import tensor


def test_repeated_tensor_slots_remain_distinct_owned_index_families() -> None:
    value = tensor(ZZ, (2, 2), (3,), range(12))
    upper, lower = value.tensor_indices()

    assert upper.cardinality() == 2
    assert lower.cardinality() == 1
    assert upper.index_set().cardinality() == 2
    assert tuple(upper[0]) == tuple(upper[1]) == (0, 1)
    assert tuple(lower[0]) == (0, 1, 2)


def test_infinite_rank_pairing_keeps_the_actual_owned_basis_set_per_slot() -> None:
    module = FreeModule(ZZ, NN)
    gram = module.diagonal_gram({})
    upper, lower = gram.tensor_indices()

    assert upper.cardinality() == 0
    assert lower.cardinality() == 2
    assert lower[0] is lower[1]
    assert not lower[0].cardinality().is_finite()
