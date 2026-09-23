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


