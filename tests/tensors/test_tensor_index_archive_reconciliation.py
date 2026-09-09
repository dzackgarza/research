r"""Archive reconciliation for metric raising and lowering of tensor indices."""

import pytest

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.tensors import tensor


def test_archive_unimodular_gram_raises_to_identity_and_lowers_back() -> None:
    plane = Lattices(ZZ)("U")
    gram = plane.gram_tensor()
    identity = gram.raise_index(plane, 0)

    assert identity.tensor_valence() == (1, 1)
    assert identity.components() == [[1, 0], [0, 1]]
    assert identity.lower_index(plane, 0) == gram


def test_archive_integral_raising_refuses_a_nonunimodular_form() -> None:
    a2 = Lattices(ZZ)("A2")
    with pytest.raises(ValueError, match="inverse Gram entries"):
        a2.gram_tensor().raise_index(a2, 0)


def test_archive_index_change_preserves_unselected_slot_order() -> None:
    plane = Lattices(ZZ)("U")
    mixed = plane.gram_tensor().tensor_product(tensor.vector(ZZ, [1, 0]))
    raised = mixed.raise_index(plane, 1)

    assert raised.tensor_valence() == (2, 1)
    lowered = raised.lower_index(plane, 1)
    assert lowered == mixed
