"""Preamble owner contracts consumed by lattice-database certification.

These are mathematical tests of the preamble objects themselves.  Lattice-db
only serializes the returned values and never rechecks these formulas.
"""

from dzack_research.preamble.all import *


def test_positive_a2_genus_and_orthogonal_group_are_owned_by_the_lattice() -> None:
    lattice = Lattices(ZZ)([[2, -1], [-1, 2]])

    assert lattice.conway_sloane_genus_symbol() == "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)"
    assert lattice.genus_class_number() == 1
    assert lattice.integral_overlattice_inclusions().cardinality() == 1
    group = lattice.orthogonal_group()
    assert group.order() == 12
    for automorphism in group.group_generators():
        for left in lattice.module_generators():
            for right in lattice.module_generators():
                assert lattice.b(left, right) == lattice.b(
                    automorphism(left), automorphism(right)
                )


def test_integral_hyperbolic_index_is_owned_by_the_lattice() -> None:
    plane = Lattices(ZZ)("U")
    e8 = Lattices(ZZ)("E8")

    assert (plane + plane + e8).integral_hyperbolic_index() == 2
    assert (plane.twist(2) + Lattices(ZZ)([[-2]])).integral_hyperbolic_index() == 0
    assert Lattices(ZZ)([[1, 0], [0, -1]]).integral_hyperbolic_index() == 0
    assert Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, -1]]).integral_hyperbolic_index() == 1


def test_spinor_genus_counts_and_class_numbers_are_owned_by_the_lattice() -> None:
    splag_96 = Lattices(ZZ)([[2, 1, 0], [1, 2, 0], [0, 0, 18]])
    splag_11 = Lattices(ZZ)([[-1, 0, 0], [0, 64, 0], [0, 0, 2]])

    for lattice in (splag_96, splag_11):
        assert lattice.genus_class_number() == 2
        assert lattice.spinor_genus_count() == 2
        assert tuple(lattice.spinor_genus_class_numbers()) == (1, 1)


def test_lattice_isotropy_is_owned_by_the_quadratic_space() -> None:
    assert Lattices(ZZ)("U").is_isotropic()
    assert not Lattices(ZZ)("E8").is_isotropic()
    assert Lattices(ZZ)([[0]]).is_isotropic()
