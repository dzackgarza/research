r"""Archive reconciliation for the selected integral form of a number field."""

from dzack_research.preamble.all import QQ, ZZ, NumberField


def _quadratic_field():
    polynomial_ring = QQ.polynomial_ring("x")
    x = polynomial_ring.algebra_generator("x")
    return NumberField(x**2 - 5, "a")


def test_selected_integral_form_is_the_power_order_not_the_maximal_order() -> None:
    field = _quadratic_field()
    selected = field.underlying_algebra(ZZ)
    maximal = field.ring_of_integers()

    assert selected is not maximal
    assert selected.base_ring() is ZZ
    assert selected.fraction_field() is field
    assert field.primitive_element() in selected


def test_selected_integral_form_base_changes_back_to_the_number_field_algebra() -> None:
    field = _quadratic_field()
    selected = field.underlying_algebra(ZZ)
    scalar_extension = field.base_change_functor(ZZ)
    extended = scalar_extension(selected)
    field_algebra = field.as_algebra()

    assert extended.base_ring() is QQ
    assert extended.module_rank() == field_algebra.module_rank()
    assert extended.relations().cardinality() == field_algebra.relations().cardinality()


def test_number_field_base_change_functor_acts_on_a_nonidentity_order_map() -> None:
    field = _quadratic_field()
    selected = field.underlying_algebra(ZZ)
    scalar_extension = field.base_change_functor(ZZ)
    conjugation = selected.Mor(selected)(-field.primitive_element())
    extended = scalar_extension(conjugation)

    source = scalar_extension(selected)
    generator = source.algebra_generator(source.algebra_generating_set()[0])
    assert extended.domain() is source
    assert extended.codomain() is source
    assert extended(generator) == -generator
