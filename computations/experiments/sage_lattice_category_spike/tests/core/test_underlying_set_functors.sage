r"""Real-boundary proofs for the lattice-to-owned-Sets functor.

The form on a based lattice is forgotten before generic set operations are
computed.  The resulting set is transported from the coordinate product of
the scalar set; it is not the original lattice relabelled as a Sage set.
"""

from __future__ import annotations

from sage.all import ZZ, matrix

from sage_lattice_category_spike import Lattice, Lattices, Sets


def test_a2_underlying_set_is_transport_of_the_integer_coordinate_square():
    r"""The owned functor derives ``|A2|`` from ``|ZZ x ZZ|``."""
    lattice = Lattice("A2")
    underlying_set = Lattices(ZZ).canonical_functor(Sets())(lattice)
    assert underlying_set is not lattice

    from sage_lattice_category_spike import (
        ALEPH_ZERO,
        IndexedProductSet,
        IntegerSet,
        KnownCardinality,
        TransportedSet,
    )

    presentation = underlying_set.presentation()
    coordinates = underlying_set.presentation_equivalence()
    integers = IntegerSet()
    expected_cardinality = KnownCardinality(ALEPH_ZERO)

    assert isinstance(underlying_set, TransportedSet)
    assert isinstance(presentation, IndexedProductSet)
    assert tuple(presentation.index_set()) == (0, 1)
    assert presentation.factor(0) == integers
    assert presentation.factor(1) == integers
    assert integers.cardinality_knowledge() == expected_cardinality
    assert presentation.cardinality_knowledge() == expected_cardinality
    assert underlying_set.cardinality_knowledge() == expected_cardinality
    assert underlying_set.cardinality() == ALEPH_ZERO

    lattice_element = lattice([ZZ(2), ZZ(-3)])
    coordinate_element = (ZZ(2), ZZ(-3))
    assert coordinates.forward(lattice_element) == coordinate_element
    assert coordinates.inverse(coordinate_element) == lattice_element


def test_rank_zero_lattice_underlying_set_is_the_empty_product():
    r"""The empty coordinate product has exactly one element."""
    lattice = Lattice(matrix(ZZ, 0, 0, []), label="zero")
    underlying_set = Lattices(ZZ).canonical_functor(Sets())(lattice)
    assert underlying_set is not lattice

    from sage_lattice_category_spike import FiniteCardinal, KnownCardinality

    presentation = underlying_set.presentation()
    coordinates = underlying_set.presentation_equivalence()
    expected_cardinality = FiniteCardinal(1)

    assert tuple(presentation.index_set()) == ()
    assert presentation.cardinality_knowledge() == KnownCardinality(expected_cardinality)
    assert underlying_set.cardinality_knowledge() == KnownCardinality(expected_cardinality)
    assert underlying_set.cardinality() == expected_cardinality
    assert coordinates.forward(lattice([])) == ()
    assert coordinates.inverse(()) == lattice([])


def test_lattice_underlying_set_functor_maps_a_nonidentity_isometry():
    r"""The functor sends the A2 coordinate swap to its actual set map."""
    lattice = Lattice("A2")
    forgetful = Lattices(ZZ).canonical_functor(Sets())
    underlying_set = forgetful(lattice)
    assert underlying_set is not lattice

    coordinates = underlying_set.presentation_equivalence()
    swap = lattice.hom(matrix(ZZ, [[0, 1], [1, 0]]))
    mapped_swap = forgetful(swap)
    source = lattice([ZZ(2), ZZ(-3)])
    expected_image = lattice([ZZ(-3), ZZ(2)])

    assert mapped_swap.domain() == underlying_set
    assert mapped_swap.codomain() == underlying_set
    assert mapped_swap(source) == expected_image
    assert coordinates.forward(mapped_swap(source)) == (ZZ(-3), ZZ(2))
