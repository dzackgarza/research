# Projective scheme-framework test scaffold (certificate-based)

This subtree contains **concept-partitioned** test scaffolds (not generic implementation checks).
Files are grouped by mathematical object type / concept to avoid mixed-purpose test files.

The framework tests load `computations/notebooks/Projective_Scheme_Framework.ipynb` through `projective_framework_loader.py` in a session fixture, so individual tests can assume patched Sage objects and methods are already available.

Planned groups (derived from `~/Downloads/Mathematical-Certification-Corpus.md`):

- `test_schemes_pullback.sage`: categorical scheme constructions (pullbacks, graphs, diagonals, fixed loci, scheme-theoretic image).

- `test_projective_products_picard.sage`: projective products, Picard groups, divisors.

- `test_chow_cohomology_intersections.sage`: cohomology / intersection data / Chow structure.

- `test_graded_algebra_sections.sage`: Cox ring and section/ring-graded algebra certificates.

- `test_base_change_and_bundles.sage`: line bundles, vector bundles, relative spectra, base-change compatibility.

- `test_linear_systems_restrictions.sage`: complete linear systems, base loci, restrictions, jets, Bertini.

- `test_group_actions_and_isotypics.sage`: group actions, linearizations, representation/isotypic/projector structure.

- `test_fixed_loci.sage`: fixed-point/fixed-subscheme tests and factorization by automorphism constraints.

- `test_curves_and_singularities.sage`: curve invariants and local-ring ADE singularity fixtures.

- `test_cyclic_covers_and_involutions.sage`: cyclic-cover datum, K3/K3-cover constructions, deck/ramification/involution lifts.

- `test_quotients_and_complete_intersections.sage`: quotients, invariant rings, complete-intersection formulas and images.

- `test_blowups_and_non_toric_families.sage`: non-toric benchmark families and blow-up geometry.

- `test_external_databases.sage`: LMFDB/OEIS/other database-backed certificates.

- `test_composite_certificates.sage`: cross-construction equivalence cycles (fixed-locus + Lefschetz, cyclic-cover cycle, quotient cycle, gluing cycle, etc.).

`scenario_manifest.sage` stores the canonical section mapping used by the scaffold while the implementation is being migrated into executable tests.
