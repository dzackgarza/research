r"""Equivariant vector orbits are computed under the actual lattice centralizer."""

from dzack_research.preamble.all import Sets, ZZ, Lattices


def _swap_equipped_a1_squared():
    lattice = Lattices(ZZ)("A1") + Lattices(ZZ)("A1")
    first = lattice.module_generator(0)
    second = lattice.module_generator(1)
    swap = lattice.O()({0: second, 1: first})
    return swap, first, second


def test_equivariant_vector_orbits_retain_stabilizers_and_transporters() -> None:
    isometry, first, second = _swap_equipped_a1_squared()
    decomposition = isometry.equivariant_vector_orbit_decomposition(first.q())

    assert decomposition in Sets()
    orbit = decomposition.orbit_of(first)
    stabilizer = orbit.stabilizer()
    transporter = decomposition.transporter(first, second)

    assert first in orbit
    assert second in orbit
    assert stabilizer.supergroup() is isometry.centralizer_group()
    assert all(element(first) == first for element in isometry.centralizer_group().supergroup() if element in stabilizer)

    assert transporter is not None
    assert transporter in isometry.centralizer_group()
    assert transporter(first) == second
    assert transporter * isometry == isometry * transporter


def test_representatives_are_the_same_live_orbit_package() -> None:
    isometry, first, _second = _swap_equipped_a1_squared()
    decomposition = isometry.equivariant_vector_orbit_decomposition(first.q())

    assert isometry.equivariant_vector_orbit_representatives(
        first.q()
    ) == decomposition.representatives()
    assert decomposition.orbits().cardinality() == 1
