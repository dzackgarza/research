r"""Archive reconciliation for the chosen bilinear lift of a quadratic form."""

import pytest

from dzack_research.preamble.all import ZZ, QuadraticMap, ring_as_module


def test_coordinate_quadratic_form_retains_its_bilinear_lift_as_a_form() -> None:
    module = ring_as_module(ZZ)
    generator = module.module_generator(module.module_generating_set()[0])
    quadratic = QuadraticMap(module, ZZ, [[ZZ.one()]])

    lift = quadratic.lift_form()
    polar = quadratic.polar_form()

    assert lift.module() is module
    assert lift.codomain() is ZZ
    assert lift(generator, generator) == ZZ.one()
    assert quadratic(generator) == lift(generator, generator)
    assert polar(generator, generator) == 2 * lift(generator, generator)


def test_callable_quadratic_form_does_not_fabricate_a_chosen_lift() -> None:
    module = ring_as_module(ZZ)
    quadratic = QuadraticMap(
        module,
        ZZ,
        lambda element: element.to_tuple()[0] ** 2,
    )

    with pytest.raises(TypeError, match="no chosen bilinear lift"):
        quadratic.lift_form()
