r"""Archive reconciliation for ``QQ / n ZZ`` as an owned module quotient."""

from dzack_research.preamble.all import QQ, ZZ, FractionFieldQuotients, Lattices

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/modules/framed/fraction_field_quotients.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_ring_quotient_value_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py",
        "owner_overrides": {
            "test_the_A2_discriminant_bilinear_scale_is_the_subgroup_of_order_three": "src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py",
            "test_the_A2_discriminant_quadratic_scale_lives_in_Q_mod_2Z": "src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py",
        },
        "disposition": "reconciled-live-owner",
    },
)




def test_fraction_field_quotient_submodules_are_actual_cyclic_subobjects() -> None:
    quotient = FractionFieldQuotients(ZZ)(6)

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


def test_archived_fraction_field_quotient_submodule_generators_keep_exact_orders() -> None:
    rationals_mod_one = FractionFieldQuotients(ZZ)(1)
    order_twelve = rationals_mod_one.subobject_on(
        (rationals_mod_one(QQ(1) / 4), rationals_mod_one(QQ(1) / 6))
    )
    generator = order_twelve.embedded_module_generators()[0]

    assert order_twelve.cardinality() == 12
    assert generator == rationals_mod_one(QQ(1) / 12)
    assert 3 * generator == rationals_mod_one(QQ(1) / 4)
    assert 2 * generator == rationals_mod_one(QQ(1) / 6)

    rationals_mod_two = FractionFieldQuotients(ZZ)(2)
    order_three = rationals_mod_two.subobject_on((rationals_mod_two(QQ(4) / 3),))
    generator_two = order_three.embedded_module_generators()[0]
    assert order_three.cardinality() == 3
    assert generator_two == rationals_mod_two(QQ(2) / 3)


def test_archived_a2_discriminant_scales_are_value_submodules() -> None:
    bilinear = Lattices.A2.discriminant_bilinear_form()
    bilinear_scale = bilinear.scale_submodule()
    bilinear_generator = bilinear_scale.embedded_module_generators()[0]

    assert bilinear_scale.ambient_module() is bilinear.value_module()
    assert bilinear_scale.cardinality() == 3
    assert bilinear_generator == bilinear.value_module()(QQ(1) / 3)

    quadratic = Lattices.A2.discriminant_quadratic_form()
    quadratic_scale = quadratic.scale_submodule()
    quadratic_generator = quadratic_scale.embedded_module_generators()[0]

    assert quadratic.value_module().modulus() == 2
    assert quadratic_scale.ambient_module() is quadratic.value_module()
    assert quadratic_scale.cardinality() == 3
    assert quadratic_generator == quadratic.value_module()(QQ(2) / 3)


