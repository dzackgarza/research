r"""Archive reconciliation for owned category refinement.

The archive's mathematical operation ``refine`` survives directly: it adds a
verified property/category to the same owned object and refuses false
certificates.  The archived ``hook_post_init``/``hooked_classes`` mechanism
did not describe additional mathematics; it monkey-patched Sage classes so
foreign parents could be adopted after construction.  The live architecture
deliberately retired that global hook registry.  Owned constructors select
their category at ingress, while ``construction_scope`` and
``run_construction_hooks`` run newly reached owned construction hooks during a
local refinement.  The specimens below therefore reconcile the mathematical
refinement behavior without restoring constructor monkey-patching.
"""

import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import (
    EvenLattices,
    FiniteRankLattices,
    Lattices,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.refine import refine

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/refine.sage",
    "live_owner": "src/dzack_research/preamble/refine.py",
    "disposition": "reconciled-live-owner",
}


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

    from dzack_research.preamble.all import QQ, PolynomialRing

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
