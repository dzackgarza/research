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


def test_archived_owned_polynomial_real_roots_keep_exact_multiplicities() -> None:
    from sage.rings.qqbar import AA as AlgebraicReals

    from dzack_research.preamble.all import PolynomialRing, QQ

    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.algebra_generator("x")

    roots = (x**2 - 5).roots(ring=AlgebraicReals)
    assert [multiplicity for _root, multiplicity in roots] == [1, 1]
    assert [root**2 for root, _multiplicity in roots] == [5, 5]
    assert roots[0][0] < 0 < roots[1][0]
    assert ((x - 1) ** 2 * (x - 2)).roots(ring=AlgebraicReals) == [
        (AlgebraicReals(1), 2),
        (AlgebraicReals(2), 1),
    ]
    assert (x**2 + 1).roots(ring=AlgebraicReals) == []


def test_archived_noncrystallographic_H4_group_has_order_14400() -> None:
    from sage.combinat.root_system.coxeter_group import CoxeterGroup

    assert CoxeterGroup(["H", 4]).cardinality() == 14400
