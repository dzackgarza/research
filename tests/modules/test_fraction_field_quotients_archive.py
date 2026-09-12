r"""Archive reconciliation for ``QQ / n ZZ`` as an owned module quotient."""

from dzack_research.preamble.all import QQ, ZZ, FractionFieldQuotient


def test_fraction_field_quotient_retains_projection_lift_and_factorial_framing() -> None:
    quotient = FractionFieldQuotient(ZZ, 6)
    projection = quotient.projection_from_fraction_field()

    assert quotient.modulus() == QQ(6)
    assert projection.domain() is QQ
    assert projection.codomain() is quotient
    assert quotient.lift(projection(QQ(1) / 2)) == QQ(1) / 2

    labels = quotient.module_generating_set()
    assert quotient.divisibility_chain(labels(0)) == 1
    assert quotient.divisibility_chain(labels(1)) == 2
    assert quotient.divisibility_chain(labels(2)) == 6
    assert quotient.module_generator(labels(2)) == projection(QQ(1) / 6)


def test_fraction_field_quotient_submodules_are_actual_cyclic_subobjects() -> None:
    quotient = FractionFieldQuotient(ZZ, 6)

    order_two = quotient.subobject_on((quotient(3),))
    order_three = quotient.subobject_on((quotient(2),))

    assert order_two.ambient_module() is quotient
    assert order_three.ambient_module() is quotient
    assert order_two.cardinality() == 2
    assert order_three.cardinality() == 3

    inclusion_two = order_two.inclusion()
    inclusion_three = order_three.inclusion()
    assert inclusion_two(order_two.module_generator(0)) == quotient(3)
    assert inclusion_three(order_three.module_generator(0)) == quotient(2)
    assert inclusion_two.lift(quotient(3)) == order_two.module_generator(0)
    assert inclusion_three.lift(quotient(4)) == 2 * order_three.module_generator(0)
