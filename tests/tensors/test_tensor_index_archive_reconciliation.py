r"""Archive reconciliation for metric raising and lowering of tensor indices."""

import pytest

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.tensors import tensor


def test_archive_unimodular_gram_raises_to_identity_and_lowers_back() -> None:
    plane = Lattices(ZZ)("U")
    gram = plane.gram_tensor()
    identity = gram.raise_index(plane, 0)

    assert identity.tensor_valence() == (1, 1)
    assert identity == tensor(ZZ, (2,), (2,), [[1, 0], [0, 1]])
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


def test_archive_nondegenerate_form_raises_after_fraction_field_base_change() -> None:
    a2 = Lattices(ZZ)("A2")
    fraction_map = a2.base_ring().fraction_field_map()
    rationalized = a2.base_change(fraction_map)
    raised = a2.raise_index_over_fraction_field(a2.gram_tensor(), 0)

    assert raised.base_ring() is rationalized.base_ring()
    assert raised.tensor_valence() == (1, 1)
    assert raised == tensor(raised.base_ring(), (2,), (2,), [[1, 0], [0, 1]])
    assert rationalized.lower_index(raised, 0) == rationalized.gram_tensor()


def test_archive_correlation_is_an_isomorphism_exactly_when_unimodular() -> None:
    plane = Lattices(ZZ)("U")
    correlation = plane.correlation_isomorphism()
    dual = correlation.forward().codomain()

    for generator in plane.module_generators():
        assert correlation.inverse()(correlation.forward()(generator)) == generator
    for functional in dual.module_generators():
        assert correlation.forward()(correlation.inverse()(functional)) == functional

    a2 = Lattices(ZZ)("A2")
    with pytest.raises(ValueError, match="unimodular"):
        a2.correlation_isomorphism()
