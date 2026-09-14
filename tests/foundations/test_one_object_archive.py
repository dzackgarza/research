import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleOn,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.set_categories import Sets


def test_free_module_on_one_owned_ring_and_index_set_is_one_object() -> None:
    integers = _own_ring(SageZZ)
    labels = Sets.Δ[2]

    first = FreeModuleOn(integers, labels)
    second = FreeModuleOn(integers, labels)

    assert first is second
    assert first.base_ring() is integers
    assert first.module_generating_set() is labels


def test_public_free_module_constructor_refuses_raw_engine_ring_identity() -> None:
    labels = Sets.Δ[1]

    with pytest.raises(TypeError, match="preamble ring"):
        FreeModuleOn(SageZZ, labels)


def test_commutative_owned_ring_is_its_own_center() -> None:
    integers = _own_ring(SageZZ)

    assert integers.ring_center() is integers
    assert integers.is_central(integers(7))
