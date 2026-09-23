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

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/refine.sage",
        "live_owner": "src/dzack_research/preamble/refine.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_preamble_refine.sage",
        "live_owner": "tests/foundations/test_refine_archive.py",
        "owner_overrides": {
            "test_unequal_rank_hom_from_generator_images": "tests/modules/test_morphism_matrices_archive.py",
            "test_cython_parents_refuse_refinement_and_so_keep_their_underlying_set": "tests/foundations/test_canonical_object_identity_archive.py",
            "test_a_polynomial_ring_is_the_free_algebra_the_notebook_receives": "tests/algebras/test_framed_free_algebra_comparisons_archive.py",
            "test_real_roots_come_from_the_algebraic_closure": "tests/foundations/test_refine_archive.py",
            "test_the_noncrystallographic_coxeter_groups_have_their_orders": "tests/foundations/test_refine_archive.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


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
    from dzack_research.preamble.all import AA, QQ

    polynomial_ring = QQ.polynomial_ring("x")
    x = polynomial_ring.algebra_generator("x")

    # The archive named Sage's AA directly.  The public boundary now exposes
    # the same algebraic-real field as an owned ring, and roots are the owned
    # root-indexed family rather than a backend list of pairs.
    roots = (x**2 - 5).roots(ring=AA)
    assert tuple(roots) == (1, 1)
    assert tuple(root**2 for root in roots.index_set()) == (5, 5)
    assert roots.index_set()[0] < 0 < roots.index_set()[1]

    repeated = ((x - 1) ** 2 * (x - 2)).roots(ring=AA)
    assert tuple(repeated.index_set()) == (AA(1), AA(2))
    assert tuple(repeated) == (2, 1)
    assert (x**2 + 1).roots(ring=AA).cardinality() == 0


def test_archived_noncrystallographic_H4_group_has_order_14400() -> None:
    from sage.combinat.root_system.coxeter_group import CoxeterGroup

    assert CoxeterGroup(["H", 4]).cardinality() == 14400


def test_module_zero_and_unequal_rank_mor_survive_owned_refinement() -> None:
    from dzack_research.preamble.all import ZZ
    from dzack_research.preamble.categories.sets import finite_ordered_set

    source = ZZ.free_module(finite_ordered_set(("x", "y")))
    target = ZZ.free_module(finite_ordered_set(("a", "b", "c")))
    morphism = source.module_category().Mor(source, target)(
        {
            "x": target.module_generator("b"),
            "y": target.module_generator("a") + target.module_generator("c"),
        }
    )

    assert source(0) == source.zero()
    assert target(0) == target.zero()
    assert morphism.domain() is source
    assert morphism.codomain() is target
    assert morphism(source.module_generator("x")) == target.module_generator("b")
    assert morphism(source.module_generator("y")) == (
        target.module_generator("a") + target.module_generator("c")
    )
