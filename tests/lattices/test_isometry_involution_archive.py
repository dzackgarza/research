r"""Archived involution predicate on live lattice isometries."""

from dzack_research.preamble.all import ZZ, Lattices


def test_identity_and_root_reflection_are_involutions() -> None:
    lattice = Lattices(ZZ)("A2")
    first_root = lattice.basis_vector(0)

    assert lattice.O().one().is_involution()
    assert lattice.reflection(first_root).is_involution()


def test_A2_coxeter_element_is_not_an_involution() -> None:
    lattice = Lattices(ZZ)("A2")
    first_root, second_root = lattice.module_generators()
    coxeter = lattice.reflection(first_root) * lattice.reflection(second_root)

    assert coxeter * coxeter != lattice.O().one()
    assert not coxeter.is_involution()
