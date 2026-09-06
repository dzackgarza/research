r"""Cusps: primitive isotropic vectors, their reduction lattices, and the cone character.

A cusp of a lattice of signature ``(1, n)`` is an ``O(L)``-orbit of primitive
isotropic lines, and the lattice in which that cusp's reflection group acts is
the isotropic reduction ``v^perp / v``.

The five Sterk cusps of the Enriques period space are the five primitive
isotropic vectors of ``T_En = U + U(2) + E8(-2)`` recorded in the catalogue.
Their reduction lattices are the rank-ten lattices in which the two competing
simple-root counts of the Sterk discrepancy are taken: the first cusp reduces
to ``E10(2) = U(2) + E8(-2)``, two-elementary of type ``(10, 10, 0)``, and the
other four reduce to ``U + E8(-2)``, of type ``(10, 8, 0)``.  Those isometry
classes are what ``notes/computations/sterk-root-count-discrepancy.md``
records from the in-tree Vinberg runs.

The discrepancy itself compares two group actions on one of these lattices.
Sterk's published counts (12, 10, 12, 11, 14) are wall counts of a fundamental
domain for a reflection *subgroup*; the computed counts (nine or ten) are wall
counts for the full reflection group of the same lattice.  A fundamental
domain for the smaller group is a union of chambers of the larger, so the
published counts are the larger ones, which is the direction observed.  The
lattices below are the objects both counts are taken in; carrying the
published root configurations into them needs the projection
``v^perp ->> v^perp/v``, which the owned isotropic reduction does not return.
"""

import pytest

from dzack_research.preamble.all import (
    NamedLattices,
    Sterk,
    nikulin_invariants,
    primitive_isotropic,
    primitive_isotropic_vectors,
)

# cusp name: (named reduction lattice, Nikulin invariants of the reduction)
STERK_CUSPS = {
    "Sterk_1": (lambda: NamedLattices.E10_2, (10, 10, 0)),
    "Sterk_2": (lambda: NamedLattices.U_E8_2, (10, 8, 0)),
    "Sterk_3": (lambda: NamedLattices.U_E8_2, (10, 8, 0)),
    "Sterk_4": (lambda: NamedLattices.U_E8_2, (10, 8, 0)),
    "Sterk_5": (lambda: NamedLattices.U_E8_2, (10, 8, 0)),
}


@pytest.mark.parametrize("name", sorted(STERK_CUSPS))
def test_a_sterk_cusp_reduces_to_its_recorded_rank_ten_lattice(name) -> None:
    reduction_lattice, (rank, length, delta) = STERK_CUSPS[name]
    period_lattice = NamedLattices.TEn
    vector = Sterk.selected_isotropic_vectors()[name]
    assert vector.q() == 0

    line = primitive_isotropic(period_lattice, (vector,))
    assert line.rank() == 1
    assert line.isotropic_perpendicular().rank() == 11

    reduction = line.isotropic_reduction()
    assert reduction.rank() == 10
    assert reduction.is_even()
    assert reduction.is_p_elementary(2)
    assert reduction.two_elementary_invariants() == nikulin_invariants(
        rank, length, delta
    )
    assert reduction.discriminant_group().cardinality() == 2**length
    assert reduction.is_isometric(reduction_lattice())


def test_the_five_sterk_cusps_split_into_two_reduction_classes() -> None:
    period_lattice = NamedLattices.TEn
    reductions = {
        name: primitive_isotropic(period_lattice, (vector,)).isotropic_reduction()
        for name, vector in Sterk.selected_isotropic_vectors().items()
    }
    assert len(reductions) == 5
    assert not reductions["Sterk_1"].is_isometric(reductions["Sterk_2"])
    assert reductions["Sterk_2"].is_isometric(reductions["Sterk_3"])
    assert reductions["Sterk_2"].is_isometric(reductions["Sterk_4"])
    assert reductions["Sterk_2"].is_isometric(reductions["Sterk_5"])


def test_primitive_isotropic_vectors_are_cut_out_by_their_definition() -> None:
    lattice = NamedLattices.E10
    generators = lattice.module_generators()
    isotropic, partner, root = (generators.unrank(index) for index in range(3))
    vectors = primitive_isotropic_vectors(lattice)

    assert isotropic in vectors
    assert partner in vectors
    assert isotropic + partner not in vectors  # square two, not isotropic
    assert root not in vectors  # square minus two, not isotropic
    assert lattice.zero() not in vectors  # the zero vector is not primitive
    assert 2 * isotropic not in vectors  # isotropic but a proper multiple

    definite = NamedLattices.E8
    assert all(
        vector not in primitive_isotropic_vectors(definite)
        for vector in definite.module_generators()
    )


def test_minus_one_and_the_cone_character_split_a_lorentzian_group() -> None:
    lattice = NamedLattices.E10
    assert lattice.signature_pair().first() == 1
    generators = lattice.module_generators()
    line = primitive_isotropic(lattice, (generators.unrank(0),))
    transvection = line.eichler_transvection(generators.unrank(2))

    minus_identity = lattice.Aut()(
        {
            label: -lattice.module_generator(label)
            for label in lattice.module_generating_set()
        }
    )
    cone_subgroup = lattice.positive_cone_subgroup()

    assert lattice.Aut().one() in cone_subgroup
    assert minus_identity not in cone_subgroup
    # In signature (1, n) the positive cone has two components and -1 exchanges
    # them, so O(L) is the product of the cone subgroup with <-1>: exactly one
    # of g and -g preserves a component.
    assert transvection in cone_subgroup
    assert minus_identity * transvection not in cone_subgroup
