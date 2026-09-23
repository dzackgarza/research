from dzack_research.preamble.all import AA, QQ, ZZ, Algebras, QuadraticField
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.rings.number_fields import (
    NumberFieldsWithChosenPrimitiveElement,
    OrdersWithChosenIntegralBasis,
    OwnedNumberFields,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
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
    assert _own_ring(_engine_ring(field)) is field
    assert field.as_algebra_over(QQ) is field
    assert field.primitive_element().parent() is field
    assert field.embeddings(AA).cardinality() == 2
    assert order in OrdersWithChosenIntegralBasis()
    assert _own_ring(_engine_ring(order)) is order
    assert order.as_algebra_over(ZZ) is order
    assert order in Algebras(ZZ).Associative().Unital().Commutative()
    assert order.base_ring() is ZZ
    assert order.framing_morphism().codomain() is order
    assert order.framing_source().base_ring() is ZZ
    assert order.integral_basis().cardinality() == 2
