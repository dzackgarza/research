r"""Archive reconciliation for tensor index operations owned by formed modules."""

import pytest

from dzack_research.preamble.all import QQ, ZZ, BilinearForm, FreeModule, tensor


def test_formed_module_raises_and_lowers_the_same_tensor_indices_as_the_tensor_owner() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[2, 0], [0, 3]])
    covariant = tensor(QQ, (), (2,), [QQ(4), QQ(9)])

    raised = formed.raise_index(covariant)
    assert raised == covariant.raise_index(formed)
    assert raised == tensor(QQ, (2,), (), [QQ(2), QQ(3)])

    lowered = formed.lower_index(raised)
    assert lowered == covariant


def test_fraction_field_index_raising_changes_both_form_and_tensor_coefficients() -> None:
    module = FreeModule(ZZ, 1)
    formed = BilinearForm(module, ZZ, [[2]])
    covariant = tensor(ZZ, (), (1,), [ZZ.one()])

    with pytest.raises(ValueError, match="inverse Gram entries"):
        formed.raise_index(covariant)

    raised = formed.raise_index_over_fraction_field(covariant)
    assert raised.base_ring() is QQ
    assert raised == tensor(QQ, (1,), (), [QQ(1) / 2])


def test_index_owner_rejects_a_slot_of_the_wrong_variance() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[1, 0], [0, 1]])
    covariant = tensor(QQ, (), (2,), [QQ.one(), QQ.zero()])

    with pytest.raises(IndexError, match="upper tensor index"):
        formed.lower_index(covariant)
