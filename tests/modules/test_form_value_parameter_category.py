import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules import (
    FormedModules,
    FormValueObjects,
    PairedModules,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModule
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_form_value_parameter_accepts_scalar_rings_and_modules() -> None:
    integers = _own_ring(SageZZ)
    module = FreeModule(integers, 2)

    assert integers in FormValueObjects()
    assert module in FormValueObjects()
    assert FormedModules(integers).parameter_category() is FormValueObjects()
    assert PairedModules(module).parameter_category() is FormValueObjects()


def test_form_value_parameter_rejects_an_unstructured_set_at_the_boundary() -> None:
    unrelated = finite_ordered_set((0, 1))

    assert unrelated not in FormValueObjects()
    with pytest.raises(AssertionError, match="parameterized by"):
        FormedModules(unrelated)

