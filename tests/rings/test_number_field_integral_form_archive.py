r"""Archive reconciliation for the selected integral form of a number field."""

from dzack_research.preamble.all import OwnedOrders, QuadraticField


def test_selected_primitive_element_order_recovers_the_number_field_by_fraction_field() -> None:
    field = QuadraticField(5, "a")
    primitive = field.primitive_element()
    selected_order = field.order_generated_by(primitive)
    maximal_order = field.ring_of_integers()
    adjunction = OwnedOrders().fraction_field_adjunction()
    fraction_field = adjunction.left_adjoint()

    assert selected_order is not maximal_order
    assert fraction_field(selected_order) is field

    unit = adjunction.unit(selected_order)
    for basis_element in selected_order.integral_basis():
        assert unit(basis_element) == basis_element


def test_selected_order_and_maximal_order_have_the_same_fraction_field_but_are_distinct_integral_forms() -> None:
    field = QuadraticField(5, "a")
    primitive = field.primitive_element()
    selected_order = field.order_generated_by(primitive)
    maximal_order = field.ring_of_integers()
    adjunction = OwnedOrders().fraction_field_adjunction()
    fraction_field = adjunction.left_adjoint()

    assert fraction_field(selected_order) is field
    assert fraction_field(maximal_order) is field

    selected_basis = tuple(selected_order.integral_basis())
    maximal_basis = tuple(maximal_order.integral_basis())
    assert selected_basis != maximal_basis

    counit = adjunction.counit(field)
    assert counit.domain() is fraction_field(maximal_order)
    assert counit.codomain() is field
    assert counit(field.primitive_element()) == field.primitive_element()
