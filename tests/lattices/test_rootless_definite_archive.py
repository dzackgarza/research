r"""Archive reconciliation for the zero root sublattice of a rootless definite lattice."""

from dzack_research.preamble.all import Lattices, ZZ


def test_rootless_definite_lattice_has_the_zero_embedded_root_sublattice() -> None:
    lattice = Lattices(ZZ)([[4]])

    assert lattice.roots().cardinality() == 0
    root_sublattice = lattice.root_sublattice()
    inclusion = root_sublattice.inclusion()

    assert root_sublattice.module_rank() == 0
    assert inclusion.codomain() is lattice
    assert inclusion.domain() is root_sublattice
    assert root_sublattice.module_generating_set().cardinality() == 0
    assert inclusion(root_sublattice.zero()) == lattice.zero()
