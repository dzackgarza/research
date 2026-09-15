r"""Value objects of represented forms stay inside the owned module universe."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormValueObjects,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_form_value_category_has_an_owned_scalar_witness_and_owned_module_values() -> None:
    values = FormValueObjects()
    module = ZZ.free_module(finite_ordered_set(("e",)))

    assert values.an_object() is ZZ
    assert ZZ in values
    assert module in values


def test_form_value_category_does_not_admit_a_raw_engine_ring() -> None:
    assert SageZZ not in FormValueObjects()
