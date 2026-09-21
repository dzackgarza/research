from dzack_research.preamble.all import ZZ, Lattices, NamedLattices


def test_divided_class_of_u2_basis_vector_is_not_characteristic() -> None:
    lattice = NamedLattices.U_2
    element = lattice.basis_vector(0)
    divided_class = lattice.divided_discriminant_class(element)

    assert not divided_class.is_characteristic()


def test_diagonal_two_minus_two_has_a_characteristic_divided_class() -> None:
    lattice = Lattices(ZZ)([[2, 0], [0, -2]])
    first, second = lattice.module_generators()
    divided_class = lattice.divided_discriminant_class(first + second)

    assert divided_class.is_characteristic()
