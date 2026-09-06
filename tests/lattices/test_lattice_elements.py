r"""What a lattice vector answers about itself.

A vector knows its covector under the correlation, whether it is isotropic,
whether the line it spans is primitive, the ideal it pairs \(L\) into, and the
subobjects it cuts out.  The specimens below fix each of those against a
value computed another way, so an implementation that returned the transpose,
the inverse Gram, or the wrong index would fail.
"""

from dzack_research.preamble.all import ZZ, Lattices


def test_the_correlation_of_a_hyperbolic_plane_swaps_the_dual_framing() -> None:
    r"""\(b(e,-)=f^\vee\) and \(b(f,-)=e^\vee\), because \(b(e,e)=0\) and \(b(e,f)=1\).

    A correlation that read the Gram row at the wrong index would send each
    generator to its own dual generator instead.
    """
    plane = Lattices(ZZ)("U")
    first, second = plane.module_generators()
    dual = plane.dual_module()
    first_label, second_label = tuple(dual.module_generating_set())

    assert first.to_covector().parent() is dual
    assert first.to_covector() == dual.module_generator(second_label)
    assert second.to_covector() == dual.module_generator(first_label)


def test_the_gram_matrix_holds_the_pairings_and_its_determinant_is_the_discriminant() -> None:
    lattice = Lattices(ZZ)([[2, 1], [1, -4]])
    gram_matrix = lattice.gram_matrix()
    labels = tuple(lattice.module_generating_set())

    assert all(
        gram_matrix[row, column]
        == lattice.b(lattice.module_generator(row), lattice.module_generator(column))
        for row in labels
        for column in labels
    )
    assert gram_matrix.determinant() == -9
    assert gram_matrix.determinant() == lattice.determinant()


def test_isotropy_is_the_vanishing_of_the_quadratic_value() -> None:
    plane = Lattices(ZZ)("U")
    first, second = plane.module_generators()

    assert first.is_isotropic()
    assert second.is_isotropic()
    assert not (first + second).is_isotropic()
    assert (first + second).q() == 2


def test_primitivity_is_a_property_of_the_line_the_vector_spans() -> None:
    plane = Lattices(ZZ)("U")
    first, second = plane.module_generators()

    assert first.is_primitive()
    assert not (2 * first).is_primitive()
    assert (2 * first + 3 * second).is_primitive()
    assert not (6 * first + 4 * second).is_primitive()
    assert (3 * first + 2 * second).is_primitive()


def test_the_divisibility_ideal_is_generated_by_the_pairings_against_the_framing() -> None:
    r"""On \(\langle 2\rangle\oplus\langle-6\rangle\) the two generators pair
    \(L\) into \((2)\) and \((6)\); over \(\mathbb Z\) the positive generator
    of that ideal is the divisibility.
    """
    lattice = Lattices(ZZ)([[2, 0], [0, -6]])
    first, second = lattice.module_generators()
    integers = lattice.base_ring()

    assert lattice.divisibility_ideal(first) == integers.ideal(2)
    assert lattice.divisibility_ideal(second) == integers.ideal(6)
    assert first.div() == 2
    assert second.div() == 6
    assert (first + second).div() == 2


def test_a_vector_cuts_out_its_line_and_the_complement_of_that_line() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic = lattice.module_generator(0)

    line = isotropic.sublattice()
    complement = isotropic.orthogonal_complement()

    assert line.rank() == 1
    assert line.inclusion().codomain() is lattice
    assert line.inclusion()(line.module_generator(0)) == isotropic
    # e is isotropic, so e lies in its own complement and the rank drops by one.
    assert complement.rank() == 3
    assert complement.inclusion().codomain() is lattice


def test_the_complement_of_an_anisotropic_vector_splits_off_its_line() -> None:
    r"""For \(q(r)\neq0\) the vector is not in \(r^\perp\), so the rank drops
    by one, and in \(A_2\) the surviving line has norm \(-6\).
    """
    root_lattice = Lattices(ZZ)("A2")
    root = root_lattice.module_generator(0)

    complement = root.orthogonal_complement()

    assert complement.rank() == 1
    # r^perp in A_2 is spanned by e_0 + 2 e_1, of norm -6.
    assert complement.determinant() == -6
    assert all(
        root_lattice.b(root, complement.inclusion()(generator)) == 0
        for generator in complement.module_generators()
    )


def test_a_lattice_is_totally_isotropic_exactly_when_its_form_vanishes() -> None:
    plane = Lattices(ZZ)("U")
    isotropic_line = plane.module_generator(0).sublattice()

    assert not plane.is_totally_isotropic()
    assert isotropic_line.is_totally_isotropic()
    assert plane.radical().is_totally_isotropic()
    assert plane.radical().rank() == 0
