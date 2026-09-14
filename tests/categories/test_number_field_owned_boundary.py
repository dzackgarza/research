from dzack_research.preamble.all import AA, ZZ, CommutativeAlgebras, QuadraticField
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.rings.number_fields import (
    NumberFieldsWithChosenPrimitiveElement,
    OrdersWithChosenIntegralBasis,
    OwnedNumberFields,
)


def test_number_field_semantic_categories_are_owned_and_inhabited() -> None:
    fields = OwnedNumberFields()
    primitive_fields = NumberFieldsWithChosenPrimitiveElement()
    orders = OrdersWithChosenIntegralBasis()

    assert isinstance(fields, OwnedCategory)
    assert isinstance(primitive_fields, OwnedCategory)
    assert isinstance(orders, OwnedCategory)
    assert fields.an_object() in fields
    assert primitive_fields.an_object() in primitive_fields
    assert orders.an_object() in orders


def test_number_field_and_order_operations_survive_the_owned_category_boundary() -> None:
    field = QuadraticField(5, "a")
    order = field.ring_of_integers()

    assert field in OwnedNumberFields()
    assert field in NumberFieldsWithChosenPrimitiveElement()
    assert field.primitive_element().parent() is field
    assert field.embeddings(AA).cardinality() == 2
    assert order in OrdersWithChosenIntegralBasis()
    assert order in CommutativeAlgebras(ZZ)
    assert order.base_ring() is ZZ
    assert order.integral_basis().cardinality() == 2
