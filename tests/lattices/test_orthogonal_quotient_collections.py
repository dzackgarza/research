r"""Finite-character quotient representatives are owned mathematical collections."""

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.sets.finite_ordered_sets import FiniteOrderedSets


def test_double_coset_splitting_is_an_owned_finite_set_of_live_isometries() -> None:
    lattice = Lattices(ZZ)("A2")
    special = lattice.SO()
    quotient = special.finite_character_quotient()
    root = lattice.basis_vector(0)
    stabilizer = lattice.O().vector_stabilizer_generators(root)

    representatives = quotient.splitting_isometries(stabilizer)

    assert representatives in FiniteOrderedSets()
    assert representatives.cardinality().is_finite()
    assert all(representative.parent() is lattice.O() for representative in representatives)
