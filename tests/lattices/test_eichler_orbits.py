r"""Eichler's criterion as a decision about stable orbits of primitive vectors.

Eichler, *Quadratische Formen und orthogonale Gruppen*, Springer 1952,
section 10: on an even lattice splitting two hyperbolic planes, the stable
orthogonal group is transitive on primitive vectors of a given square and a
given divided discriminant class.  The invariants therefore decide an orbit
question about an infinite group with no enumeration.

``U + U + E8(-2)`` is the specimen that separates the invariants.  Its
discriminant group is ``(Z/2)^8`` and each ``E8(-2)`` basis vector has
divisibility two, so two different such vectors share a square and a
divisibility while their divided classes differ.  On a unimodular lattice
every divided class is trivial and the square alone decides.

The hypothesis is read off the presented decomposition, so the K3 lattice
appears here twice: once built as ``U^3 + E8^2``, where the three hyperbolic
planes are summands, and once as the catalogue's ``LK3``, which is presented
by a Gram matrix and therefore answers that it splits nothing.
"""

from dzack_research.preamble.all import (
    NamedLattices,
    are_in_one_stable_orbit,
    eichler_criterion_applies,
    hyperbolic_plane_summand_count,
    splits_two_hyperbolic_planes,
)


def _decomposed_k3():
    return NamedLattices.U ** 3 + NamedLattices.E8 ** 2


def _two_elementary_specimen():
    lattice = NamedLattices.U + NamedLattices.U + NamedLattices.E8_2
    return lattice, lattice.module_generators()


def test_the_criterion_reads_its_hypothesis_off_the_decomposition() -> None:
    decomposed = _decomposed_k3()
    assert decomposed.indecomposable_summands().cardinality() == 5
    assert hyperbolic_plane_summand_count(decomposed) == 3
    assert splits_two_hyperbolic_planes(decomposed)
    assert eichler_criterion_applies(decomposed)

    # E10 = U + E8 splits one hyperbolic plane, not two.
    assert hyperbolic_plane_summand_count(NamedLattices.E10) == 1
    assert not splits_two_hyperbolic_planes(NamedLattices.E10)
    assert not eichler_criterion_applies(NamedLattices.E10)

    # The catalogue's K3 lattice is isometric to the decomposed one but is
    # presented by a Gram matrix, so no decomposition is readable from it.
    assert NamedLattices.LK3.is_isometric(decomposed)
    assert not NamedLattices.LK3.is_decomposable()
    assert not eichler_criterion_applies(NamedLattices.LK3)


def test_on_a_unimodular_lattice_the_square_decides() -> None:
    lattice = _decomposed_k3()
    generators = lattice.module_generators()
    first_plane = generators.unrank(0) + generators.unrank(1)
    second_plane = generators.unrank(2) + generators.unrank(3)
    opposite = generators.unrank(0) - generators.unrank(1)

    assert lattice.discriminant_group().cardinality() == 1
    assert first_plane.q() == 2
    assert second_plane.q() == 2
    assert opposite.q() == -2
    assert first_plane.div() == 1
    assert are_in_one_stable_orbit(first_plane, second_plane)
    assert not are_in_one_stable_orbit(first_plane, opposite)


def test_the_divided_discriminant_class_separates_two_elementary_vectors() -> None:
    lattice, generators = _two_elementary_specimen()
    assert eichler_criterion_applies(lattice)
    assert lattice.discriminant_group().cardinality() == 256

    first_root = generators.unrank(4)
    second_root = generators.unrank(5)
    assert first_root.q() == -4
    assert second_root.q() == -4
    assert first_root.div() == 2
    assert second_root.div() == 2
    assert (
        first_root.divided_discriminant_class()
        != second_root.divided_discriminant_class()
    )

    # Same square and divisibility, different divided class: different orbits.
    assert not are_in_one_stable_orbit(first_root, second_root)
    # Negation preserves all three invariants in a two-group.
    assert are_in_one_stable_orbit(first_root, -first_root)
    assert first_root != -first_root


def test_a_vector_with_divisibility_one_has_a_trivial_divided_class() -> None:
    lattice, generators = _two_elementary_specimen()
    isotropic = generators.unrank(0)
    assert isotropic.div() == 1
    assert isotropic.divided_discriminant_class() == lattice.discriminant_group().zero()
    assert are_in_one_stable_orbit(isotropic, generators.unrank(2))
