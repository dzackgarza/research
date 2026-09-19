from dzack_research.preamble.all import NN, ZZ
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.tensors.tensor import tensor


def test_repeated_tensor_slots_remain_distinct_owned_index_families() -> None:
    value = tensor(ZZ, (2, 2), (3,), range(12))
    indices = value.tensor_indices()
    upper, lower = indices

    assert indices.category().first_category() is Objects()
    assert indices.category().second_category() is Objects()
    assert upper is indices.first() and lower is indices.second()
    assert upper.cardinality() == 2
    assert lower.cardinality() == 1
    assert upper.index_set().cardinality() == 2
    assert tuple(upper[0]) == tuple(upper[1]) == (0, 1)
    assert tuple(lower[0]) == (0, 1, 2)


def test_infinite_rank_pairing_keeps_the_actual_owned_basis_set_per_slot() -> None:
    module = ZZ.free_module(NN)
    gram = module.diagonal_gram({})
    indices = gram.tensor_indices()
    upper, lower = indices

    assert indices.category().first_category() is Objects()
    assert indices.category().second_category() is Objects()
    assert upper is indices.first() and lower is indices.second()
    assert upper.cardinality() == 0
    assert lower.cardinality() == 2
    assert lower[0] is lower[1]
    assert not lower[0].cardinality().is_finite()


def test_tensor_engine_uses_the_existing_module_category() -> None:
    import pytest
    from dzack_research.preamble.all import Modules
    from dzack_research.preamble.tensors.tensor import TensorModule

    module = TensorModule(ZZ, (2,), (2,))
    assert module in Modules(ZZ)
    assert module is TensorModule(ZZ, (2,), (2,))
    value = module((1, 2, 3, 4))
    assert module(value) is value
    assert value[0, 1] == 2
    assert value.is_equal_tensor(0) is False
    with pytest.raises((TypeError, ValueError)):
        TensorModule(ZZ, (1.5,), ())
