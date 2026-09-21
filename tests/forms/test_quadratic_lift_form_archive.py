r"""Archive reconciliation for the chosen bilinear lift of a quadratic form."""

import pytest

from dzack_research.preamble.all import ZZ


def test_coordinate_quadratic_form_retains_its_bilinear_lift_as_a_form() -> None:
    module = ZZ.regular_module()
    generator = module.module_generator(module.module_generating_set()[0])
    quadratic = module.quadratic_map(ZZ, [[ZZ.one()]])

    lift = quadratic.lift_form()
    polar = quadratic.polar_form()

    assert lift.module() is module
    assert lift.codomain() is ZZ
    assert lift(generator, generator) == ZZ.one()
    assert quadratic(generator) == lift(generator, generator)
    assert polar(generator, generator) == 2 * lift(generator, generator)


def test_quadratic_pullback_retains_its_own_selected_lift_without_mutating_the_source() -> None:
    module = ZZ.regular_module()
    generator = module.module_generator(module.module_generating_set()[0])
    quadratic = module.quadratic_map(ZZ, [[ZZ.one()]])
    identity = module.Mor(module).identity()

    pulled = quadratic.pullback(identity)

    assert pulled is not quadratic
    assert pulled.lift_pairing(generator, generator) == ZZ.one()
    assert pulled(generator) == quadratic(generator)


def test_callable_quadratic_form_does_not_fabricate_a_chosen_lift() -> None:
    module = ZZ.regular_module()
    label = module.module_generating_set()[0]
    quadratic = module.quadratic_map(
        ZZ,
        lambda element: module.framing_coefficients(element).get(label, ZZ.zero()) ** 2,
    )

    with pytest.raises(TypeError, match="no chosen bilinear lift"):
        quadratic.lift_form()
