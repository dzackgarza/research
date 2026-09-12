r"""Equivariant vector orbits are computed under the actual lattice centralizer."""

from dzack_research.preamble.all import ZZ, Lattices


def _swap_equipped_a1_squared():
    lattice = Lattices(ZZ)("A1") + Lattices(ZZ)("A1")
    first = lattice.module_generator(0)
    second = lattice.module_generator(1)
    swap = lattice.O()({0: second, 1: first})
    return lattice.with_isometry(swap), first, second


def test_equivariant_vector_orbits_retain_stabilizers_and_transporters() -> None:
    decorated, first, second = _swap_equipped_a1_squared()
    decomposition = decorated.equivariant_vector_orbit_decomposition(first.q())

    orbit = decomposition.orbit_of(first)
    stabilizer = orbit.stabilizer()
    transporter = decomposition.transporter(first, second)

    assert first in orbit
    assert second in orbit
    assert stabilizer.supergroup() is decorated.centralizer_group()
    assert all(element(first) == first for element in decorated.centralizer_group().supergroup() if element in stabilizer)

    assert transporter is not None
    assert transporter in decorated.centralizer_group()
    assert transporter(first) == second
    assert transporter * decorated.isometry() == decorated.isometry() * transporter


def test_representatives_are_the_same_live_orbit_package() -> None:
    decorated, first, _second = _swap_equipped_a1_squared()
    decomposition = decorated.equivariant_vector_orbit_decomposition(first.q())

    assert tuple(decorated.equivariant_vector_orbit_representatives(first.q())) == tuple(
        decomposition.representatives()
    )
    assert decomposition.orbits().cardinality() == 1
