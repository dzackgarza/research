r"""Value modules of represented pairings stay inside the owned module universe."""

import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import ZZ, Modules, PairedModules
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_pairing_values_are_owned_modules_and_a_ring_names_its_regular_module() -> None:
    values = PairedModules(ZZ)
    module = ZZ.free_module(finite_ordered_set(("e",)))

    assert values.base() is ZZ.regular_module()
    assert values.an_object().value_module() is ZZ.regular_module()
    assert ZZ.regular_module() in Modules(ZZ)
    assert module in Modules(ZZ)
    assert PairedModules(module).base() is module


def test_pairing_values_do_not_admit_a_raw_engine_ring() -> None:
    assert SageZZ not in Modules(ZZ)
    with pytest.raises(AssertionError, match="parameterized by"):
        PairedModules(SageZZ)
