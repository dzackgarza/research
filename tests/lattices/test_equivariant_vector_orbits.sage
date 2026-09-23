r"""Equivariant vector orbits are computed under the actual lattice centralizer."""

from dzack_research.preamble.all import ZZ, Lattices


def _swap_equipped_a1_squared():
    lattice = Lattices(ZZ)("A1") + Lattices(ZZ)("A1")
    first = lattice.basis_vector(0)
    second = lattice.basis_vector(1)
    swap = lattice.O()({0: second, 1: first})
    return swap, first, second




def test_representatives_are_the_same_live_orbit_package() -> None:
    isometry, first, _second = _swap_equipped_a1_squared()
    decomposition = isometry.equivariant_vector_orbit_decomposition(first.q())

    assert isometry.equivariant_vector_orbit_representatives(
        first.q()
    ) == decomposition.representatives()
    assert decomposition.orbits().cardinality() == 1
