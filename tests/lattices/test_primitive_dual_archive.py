r"""Archive reconciliation for primitive dual lattice vectors."""

import pytest

from dzack_research.preamble.all import NamedLattices


def test_primitive_dual_retains_the_actual_dual_lattice_element() -> None:
    lattice = NamedLattices.U_2
    vector = lattice.module_generators()[0]
    dual = vector.primitive_dual()

    assert vector.div() == 2
    assert dual.parent() is lattice.dual_lattice()
    assert lattice.dual_lattice().scalar_multiple(2, dual) == lattice.correlation_morphism()(vector)
    assert lattice.discriminant_class(dual) == vector.divided_discriminant_class()


def test_primitive_dual_projects_to_both_supported_discriminant_forms() -> None:
    lattice = NamedLattices.U_2
    vector = lattice.module_generators()[0]
    dual = vector.primitive_dual()

    bilinear = vector.primitive_dual_in_discriminant_bilinear_form()
    quadratic = vector.primitive_dual_in_discriminant_quadratic_form()

    assert bilinear == lattice.discriminant_bilinear_form().discriminant_class(dual)
    assert quadratic == lattice.discriminant_quadratic_form().discriminant_class(dual)
    assert quadratic == vector.divided_discriminant_class()


def test_zero_vector_has_zero_primitive_dual_but_no_divided_discriminant_class() -> None:
    lattice = NamedLattices.U
    zero = lattice.zero()

    assert zero.primitive_dual() == lattice.correlation_morphism()(zero)
    with pytest.raises(ValueError):
        zero.divided_discriminant_class()
