r"""Archive reconciliation for multiplication endomorphisms of number fields."""

from dzack_research.preamble.all import QQ


def _quadratic_field():
    polynomial_ring = QQ.polynomial_ring("x")
    x = polynomial_ring.algebra_generator("x")
    return (x**2 - 2).number_field("a")


def test_number_field_element_retains_its_multiplication_endomorphism() -> None:
    field = _quadratic_field()
    element = field.primitive_element() + field.one()
    morphism = element.multiplication_morphism()

    assert morphism.domain().base_ring() is QQ
    assert morphism.domain().module_rank() == field.degree()
    assert morphism.codomain() is morphism.domain()
    assert morphism.matrix() == element.multiplication_matrix()
    matrix = element.multiplication_matrix()
    assert matrix[0, 0] == 1
    assert matrix[1, 0] == 1
    assert matrix[0, 1] == 2
    assert matrix[1, 1] == 1


def test_multiplication_matrix_recovers_norm_and_trace() -> None:
    field = _quadratic_field()
    element = field.primitive_element() + field.one()
    matrix = element.multiplication_matrix()

    assert matrix.determinant() == element.norm()
    assert matrix.trace() == element.trace()


