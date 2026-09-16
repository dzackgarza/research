import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules import (
    Modules,
    PairedModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_pairing_value_parameter_accepts_scalar_rings_and_modules() -> None:
    integers = _own_ring(SageZZ)
    module = integers.free_module(2)

    assert integers.regular_module() in Modules(integers)
    assert module in Modules(integers)
    assert PairedModules(integers).base() is integers.regular_module()
    assert PairedModules(module).base() is module
    assert PairedModules(integers).parameter_category() is Modules(integers)
    assert PairedModules(module).parameter_category() is Modules(integers)


def test_pairing_value_parameter_rejects_an_unstructured_set_at_the_boundary() -> None:
    integers = _own_ring(SageZZ)
    unrelated = finite_ordered_set((0, 1))

    assert unrelated not in Modules(integers)
    with pytest.raises(AssertionError, match="parameterized by"):
        PairedModules(unrelated)
