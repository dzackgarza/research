r"""Sage reference coverage manifest for the synthetic lattice spike."""

from __future__ import annotations


ACCEPTED_SYNTHETIC_API = frozenset(
    {
        "Lattice",
        "SyntheticLattice.acts_on",
        "SyntheticLattice.action_on_discriminant_group",
        "SyntheticLattice.discriminant_group",
        "SyntheticLattice.finite_quotient",
        "SyntheticLattice.genus",
        "SyntheticLattice.isometry_group",
        "SyntheticDiscriminantGroup.is_genus",
        "SyntheticDiscriminantGroup.orthogonal_quotient",
        "SyntheticDiscriminantGroup.primary_part",
        "SyntheticFiniteQuadraticForm.is_isomorphic_to",
    }
)


REFERENCE_COVERAGE = (
    {
        "sage_locus": "free_quadratic_module_integer_symmetric.py",
        "classification": "adapted",
        "local_tests": (
            "test_cartan_and_hyperbolic_constructors_match_integral_lattice_doctests",
            "test_overlattice_and_maximal_overlattice_follow_integral_lattice_doctests",
            "test_local_modification_uses_sage_gram_matrix_contract_not_discriminant_gens_only",
            "test_explicit_lattice_isometries_induce_discriminant_actions_without_full_indefinite_group",
            "test_explicit_isometry_generators_act_on_lattices_without_full_group_generation",
        ),
        "accepted_symbols": (
            "Lattice",
            "SyntheticLattice.acts_on",
            "SyntheticLattice.action_on_discriminant_group",
            "SyntheticLattice.isometry_group",
        ),
        "rejected_symbols": (),
        "notes": "Constructor, gluing, local modification, and explicit isometry-generator behavior are adapted.",
    },
    {
        "sage_locus": "free_quadratic_module.py",
        "classification": "synthetic-superseded",
        "local_tests": (
            "test_rational_span_and_fractional_dual_follow_free_quadratic_module_doctests",
            "test_lattice_module_wrapper_names_preserve_owned_lattice_contract",
        ),
        "accepted_symbols": (),
        "rejected_symbols": (
            "ambient_module",
            "ambient_space",
            "ambient_quadratic_space",
            "ambient_vector_space",
        ),
        "notes": "Synthetic rationalization replaces Sage ambient module routing.",
    },
    {
        "sage_locus": "torsion_quadratic_module.py",
        "classification": "adapted",
        "local_tests": (
            "test_brown_invariant_and_genus_follow_torsion_quadratic_module_doctests",
            "test_odd_discriminant_form_remains_usable_while_odd_genus_is_unsupported",
            "test_finite_discriminant_form_orthogonal_group_matches_torsion_doctest",
            "test_discriminant_group_isomorphism_kind_distinguishes_group_bilinear_and_quadratic",
            "test_discriminant_group_bilinear_orthogonal_group_can_be_larger_than_quadratic",
        ),
        "accepted_symbols": (
            "SyntheticLattice.discriminant_group",
            "SyntheticLattice.genus",
            "SyntheticDiscriminantGroup.is_genus",
            "SyntheticFiniteQuadraticForm.is_isomorphic_to",
        ),
        "rejected_symbols": (),
        "notes": "Even genus, finite form isomorphism, and orthogonal group surfaces are adapted; odd genus is an explicit limitation.",
    },
    {
        "sage_locus": "fgp_module.py",
        "classification": "adapted",
        "local_tests": (
            "test_discriminant_group_additive_abelian_group_api_matches_fgp_surface",
            "test_discriminant_action_inverse_image_matches_fgp_morphism_doctest",
            "test_discriminant_group_enumerates_all_finite_subgroups",
        ),
        "accepted_symbols": (
            "SyntheticLattice.finite_quotient",
            "SyntheticDiscriminantGroup.primary_part",
            "SyntheticDiscriminantGroup.orthogonal_quotient",
        ),
        "rejected_symbols": (),
        "notes": "Finite Smith quotient methods are adapted on discriminant groups and finite quotients.",
    },
    {
        "sage_locus": "free_module.py",
        "classification": "irrelevant-generic",
        "local_tests": (),
        "accepted_symbols": (),
        "rejected_symbols": (),
        "notes": "Generic free-module APIs are not independently owned except where surfaced through synthetic lattice tests.",
    },
    {
        "sage_locus": "free_module_integer.py",
        "classification": "rejected-parity",
        "local_tests": (),
        "accepted_symbols": (),
        "rejected_symbols": (
            "ordinary_lattice_quotient_module",
            "full_ambient_module_parity",
        ),
        "notes": "Ordinary quotient-module and broad integer free-module parity remain outside the accepted contract.",
    },
)


ALLOWED_CLASSIFICATIONS = frozenset(
    {
        "adapted",
        "synthetic-superseded",
        "rejected-parity",
        "irrelevant-generic",
        "pending-gap",
    }
)
