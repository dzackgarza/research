r"""Final source-backed reconciliation of the two broad archived regression suites.

The archived ``test_preamble.sage`` and ``test_known_mathematics.sage`` were
integration/gap-map suites rather than mathematical owners.  Their independent
claims now live at the narrower proof surfaces listed below; this file records
that disposition and keeps two cross-surface oracles that would detect an
accidental collapse back to implementation-only coverage.
"""


from dzack_research.preamble.all import Groups, Lattices, Sterk

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/test_preamble.sage",
        "live_owner": "tests/foundations/test_remaining_archive_suites_reconciliation.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_known_mathematics.sage",
        "live_owner": "tests/foundations/test_remaining_archive_suites_reconciliation.py",
        "disposition": "reconciled-live-owner",
    },
)

PREAMBLE_PROOF_SURFACES = (
    "tests/lattices/test_catalogue.py",
    "tests/lattices/test_catalogue_archive_reconciliation.py",
    "tests/lattices/test_lattice_catalogue_constructors_archive.py",
    "tests/lattices/test_sterk_coble.py",
    "tests/lattices/test_cusp_lattices.py",
    "tests/lattices/test_lattice_embedding_mors_archive.py",
    "tests/lattices/test_catalogue_identities_archive.py",
    "tests/lattices/test_isometry_involution_archive.py",
    "tests/lattices/test_lattice_subobjects_archive.py",
    "tests/lattices/test_tensor_direct_sum_archive.py",
    "tests/lattices/test_reflection_signs_archive.py",
    "tests/lattices/test_isotropic_type_archive.py",
    "tests/foundations/test_session_namespace_archive.py",
    "tests/foundations/test_display_policy_archive.py",
)

KNOWN_MATHEMATICS_PROOF_SURFACES = (
    "tests/groups/test_weyl_orders_archive.py",
    "tests/lattices/test_root_automorphism_orders_archive.py",
    "tests/lattices/test_orthogonal_group_presentation_archive.py",
    "tests/lattices/test_lattice_endomorphism_ring_archive.py",
    "tests/groups/test_group_generator_totality_archive.py",
    "tests/groups/test_arithmetic_finite_generation_archive.py",
    "tests/groups/test_sl2z_serre_archive.py",
    "tests/groups/test_field_absolute_galois_archive.py",
    "tests/groups/test_absolute_galois_category_archive.py",
    "tests/groups/test_galois_characters_archive.py",
    "tests/groups/test_galois_quotient_archive.py",
    "tests/groups/test_galois_extension_coset_archive.py",
    "tests/lattices/test_brown_invariants_archive.py",
    "tests/lattices/test_lagrangian_glue_archive.py",
    "tests/lattices/test_root_gluing_archive.py",
    "tests/lattices/test_voronoi_archive.py",
    "tests/lattices/test_e8_complements_archive.py",
    "tests/lattices/test_k3_even_unimodular_uniqueness_archive.py",
    "tests/lattices/test_k3_polarizations_archive.py",
    "tests/lattices/test_k3_root_complement_archive.py",
    "tests/lattices/test_k3_enriques_summand_archive.py",
    "tests/lattices/test_splag_51ab_genus_archive.py",
    "tests/lattices/test_local_excess_archive.py",
    "tests/lattices/test_genus_existence_archive.py",
    "tests/lattices/test_isometry_torsor_archive.py",
    "tests/lattices/test_catalogue_archive_reconciliation.py",
    "tests/groups/test_group_automorphisms_archive.py",
    "tests/groups/test_mathieu_automorphism_archive.py",
    "tests/schemes/test_curve_intersections_archive.py",
    "tests/lattices/test_reflection_hyperbolic.py",
)




def test_sterk_published_norm_breakdown_survives_the_catalogue_split() -> None:
    expected = {
        "Sterk_1": {-4: 12, -2: 0},
        "Sterk_2": {-4: 9, -2: 1},
        "Sterk_3": {-4: 10, -2: 2},
        "Sterk_4": {-4: 9, -2: 2},
        "Sterk_5": {-4: 10, -2: 4},
    }
    assert {
        name: {norm: sum(root.q() == norm for root in roots) for norm in (-4, -2)}
        for name, roots in Sterk.sterk_roots().items()
    } == expected


def test_literature_group_orders_survive_the_known_mathematics_split() -> None:
    assert Groups.Weyl(["E", 8]).order() == 696729600
    assert Lattices.A4.Aut().order() == 240
