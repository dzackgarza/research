r"""Number-field views use the owned category meet for retained structure."""

from dzack_research.preamble.categories.rings.number_fields import (
    NumberFieldsWithChosenPrimitiveElement,
    OwnedNumberFields,
    QuadraticField,
)
from dzack_research.preamble.rings import session_ring_objects


def test_rationals_are_an_owned_number_field_without_extra_primitive_choice() -> None:
    rationals = session_ring_objects()["QQ"]

    assert rationals in OwnedNumberFields()
    assert rationals not in NumberFieldsWithChosenPrimitiveElement()


def test_quadratic_field_retains_owned_primitive_element_refinement() -> None:
    field = QuadraticField(-1, "i")

    assert field in OwnedNumberFields()
    assert field in NumberFieldsWithChosenPrimitiveElement()
    assert field.primitive_element().parent() is field
