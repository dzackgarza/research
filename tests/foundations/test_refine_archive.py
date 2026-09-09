import pytest

from dzack_research.preamble.categories.lattices import (
    EvenLattices,
    FiniteRankLattices,
    Lattices,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.refine import refine
from sage.rings.integer_ring import ZZ as SageZZ


def test_refinement_preserves_the_owned_parent_identity() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)([[1]])

    refined = refine(lattice, FiniteRankLattices(integers))

    assert refined is lattice
    assert refined in FiniteRankLattices(integers)
    assert refined.module_rank() == 1
    assert refined.module_generator(0).parent() is refined


def test_refinement_requires_the_certifying_mathematical_predicate() -> None:
    integers = _own_ring(SageZZ)
    odd = Lattices(integers)([[1]])

    assert not odd.is_even()
    with pytest.raises(AssertionError, match="is_even"):
        refine(odd, EvenLattices(integers))


def test_successful_property_refinement_keeps_existing_elements_and_operations() -> None:
    integers = _own_ring(SageZZ)
    even = Lattices(integers)([[2]])
    generator = even.module_generator(0)

    refined = refine(even, EvenLattices(integers))

    assert refined is even
    assert refined.module_generator(0) == generator
    assert generator.parent() is refined
    assert generator.q() == 2
