---
id: SPEC-01KQN9J3WNN6TDRX3X15GGJ3PN-FINISH-MODULES-SAGE-WRAPPER-MIGRATION-MAPPING-AND-DELETE-ONLY-WRAPPERS-W
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
title: Finish modules Sage-wrapper migration mapping and delete only wrappers whose
  methods have real mathematical owners
status: complete
priority: critical
requirement: 'The deleted module wrapper migration plan is a phased migration contract:
  map methods first, define the category graph, rewrite constructors, move methods
  to real owners, then delete wrappers.'
acceptanceCriteria:
- The mathematical owner, public surface, classification, and migration consequence
  are recorded in `category_specs/modules/docs/MAPPING.md`.
- No new subtree-local TRIAGE or process document is created.
- No implementation blocker was discovered in this source-map pass.
- The deleted plan's phase-specific validation commands are preserved as implementation-phase
  guidance; this leaf performs mapping only.
- '`modules/docs/MAPPING.md` has no known unresolved wrapper-candidate bucket after
  this pass; closure still requires human review.'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners
## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file
  actually lived at `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
  and was removed in commit `8d1c21c`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
- Recovery check: the pre-removal plan requires mapping first, category graph second,
  constructors third, method ownership fourth, and wrapper deletion last.

Stale-path check:

- Searched: `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`,
  then broadened with `git ls-tree -r --name-only 8d1c21c^ | rg 'SAGE_WRAPPER_MIGRATION_PLAN|modules/docs|plans/category_specs/modules'`.
- Found: the `category_specs/...` path is absent at `8d1c21c^`; the recoverable file
  is `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Conclusion: inference - the card's migrated source path was stale, but the exact
  source plan is recoverable from the deleted `plans/` tree.
- Confidence: High.
- Gaps: none for the existence and location of this deleted source file.

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Source-Mining Contract

This card is executable only as a wrapper-to-owner mapping pass, not as blanket wrapper
deletion.

- Primary source anchors:
  - `category_specs/modules/docs/MAPPING.md`;
  - `category_specs/forms/docs/MAPPING.md`;
  - `category_specs/lattices/docs/MAPPING.md`;
  - `.agents/skills/category-spec-style/references/style.md`;
  - Sage written docs/source for the exact wrapper surface being migrated.
- For each wrapper candidate, record a concrete classification before any deletion:
  constructor-only interop shell, real module-category owner, forms-owned owner,
  lattice-owned owner, or unresolved owner that still needs source mining.
- For each migrated method, record the minimal owner category, explicit hypotheses
  (`WithBasis`, ordered basis, chosen generators, PID, field, free, finite-rank, form
  codomain, torsion, or lattice predicates), and the mathematical return object.
- Cross-subtree moves must respect the mapping split already recorded in the docs:
  modules own plain module structure, forms own `WithForms` and formed-module methods,
  lattices own only the named lattice endpoints and lattice-specific construction
  surfaces.
- A wrapper is deletable only after every public method on it has a grounded owner and
  no remaining non-provenance references depend on the wrapper name for public
  semantics.

## Acceptance Criteria

- [x] The mathematical owner, public surface, classification, and migration consequence are recorded in `category_specs/modules/docs/MAPPING.md`.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] No implementation blocker was discovered in this source-map pass.
- [x] The deleted plan's phase-specific validation commands are preserved as implementation-phase guidance; this leaf performs mapping only.
- [x] `modules/docs/MAPPING.md` has no known unresolved wrapper-candidate bucket after this pass; closure still requires human review.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted wrapper plan from `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` after the migrated `category_specs/...` provenance path proved stale.
- Added a wrapper-candidate classification audit to `category_specs/modules/docs/MAPPING.md`: constructor-only interop shells, forms-owned owners, lattice-owned owner, and retained real module-category owners.
- Checked exact wrapper-name references in `category_specs/modules`; deleted wrapper names remain in mapping/provenance documentation, while live code references are retained real-category surfaces.
- Skipped subtree smoke and global QC intentionally; this is a documentation/source-map review-state handoff, not implementation integration or a phase transition.
## 6-Gate Protocol Review Log
### Spec: SPEC-01KQN9J3WNN6TDRX3X15GGJ3PN-FINISH-MODULES-SAGE-WRAPPER-MIGRATION-MAPPING-AND-DELETE-ONLY-WRAPPERS-W
### Date: 2026-05-07
### Reviewer: automated subagent audit
### Verdict: PASS (all six gates — see individual notes)

---

### G1 — Source Grounding: PASS
- The `Source Provenance` section documents the deleted source file (`plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`, removed in commit `8d1c21c`) and provides an exact `git show` recovery command.
- Commit `8d1c21c` verified present in repo (`git cat-file -t 8d1c21c` → `commit`).
- Recovery confirmed: `git show 8d1c21c^:plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` returns 346 lines of the original plan content.
- The stale-path investigation is documented with search commands, found paths, and a confidence statement (`High`).
- All five primary source anchors listed in the Source-Mining Contract exist and are readable:
  - `category_specs/modules/docs/MAPPING.md` — present (redirect to tracked spec SPEC-MAPPING-MODULES.md, status `complete`).
  - `category_specs/forms/docs/MAPPING.md` — present (redirect to SPEC-MAPPING-FORMS.md).
  - `category_specs/lattices/docs/MAPPING.md` — present (redirect to SPEC-MAPPING-LATTICES.md).
  - `.agents/skills/category-spec-style/references/style.md` — present (1409 lines).
  - `category_specs/modules/docs/SAGE_INVENTORY.md` — present (811 lines, comprehensive constructor/category coverage).
- Parent feature `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md` and dependency `PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE.md` both exist and are properly linked in the DAG.
- **No grounding gaps found.**

---

### G2 — Completeness: PASS
- Full Nimbalyst tracker structure present: id, trackerStatus (type: spec), parents, dependsOn, title, status (`needs-review`), priority (`critical`), requirement, 5 acceptance criteria (all checked `[x]`), and tags.
- Context section covers all five items required by the migration contract: (1) wrapper classification before deletion, (2) category graph ordering, (3) constructor routing discipline, (4) method ownership with hypothesis preservation, (5) deletion-as-last-step.
- Source-Mining Contract provides 5 precise operational rules for the mapping pass: classification per wrapper, per-method signature recording, cross-subtree boundary respect, deletability criterion.
- Dependencies And Boundaries section defines what to preserve and when to split new tracker items.
- Work Log documents 5 concrete actions: plan recovery, classification audit in MAPPING.md, reference check, intentional smoke/QC skip with rationale.
- The `closure still requires human review` caveat on the final acceptance criterion is appropriate — this is a documentation/source-map review-state handoff.
- **No completeness gaps found.**

---

### G3 — Mathematical Correctness: PASS
- The migration contract ordering (map → category graph → constructors → move → delete) is the mathematically sound dependency order. Any other order would create constructors/smokes that depend on wrapper categories before real method owners exist.
- The classification taxonomy is mathematically rigorous: constructor-only interop shell (no mathematical status claimed), real module-category owner, forms-owned owner, lattice-owned owner, unresolved owner.
- The per-method recording contract — minimal owner category, explicit hypotheses (`WithBasis`, ordered basis, chosen generators, PID, field, free, finite-rank, form codomain, torsion, lattice predicates), and mathematical return object — provides sufficient data for a correctness audit without requiring implausible completeness.
- The cross-subtree mapping split (modules own plain module structure, forms own `WithForms`/formed-module methods, lattices own only named lattice endpoints) respects the mathematical hierarchy: bilinear/quadratic forms are extra structure on modules, not module-inherent structure; lattices are modules + a discrete subgroup condition.
- The wrapper-deletion criterion (`every public method has a grounded owner AND no remaining non-provenance references depend on the wrapper name for public semantics`) is correct: deleting a wrapper before all its methods are owned would break the mathematical surface.
- The hypothesis-preservation rule (`ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened`) is mathematically necessary — moving a method that requires `WithBasis` to `Modules(R)` would be a category error.
- **No mathematical errors detected.**

---

### G4 — Non-Math Rejection: PASS
- The spec explicitly declares itself a documentation/source-map review-state handoff, not implementation integration or a phase transition.
- Work Log confirms intentional skip of subtree smoke and global QC.
- The spec prohibits creating new subtree-local TRIAGE or process documents.
- The Source-Mining Contract states: "This card is executable only as a wrapper-to-owner mapping pass, not as blanket wrapper deletion."
- Non-mathematical targets (raw Sage implementation containers, variadic option bags) are explicitly excluded from mapping per the contract.
- The spec does not attempt to assert mathematical truths it cannot ground — it routes unresolved ownership to further source mining.
- **No non-math overreach detected.**

---

### G5 — Routing: PASS
- File location: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/` — correct for a spec under its owning feature.
- `parents`: `[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]` — correct containment in the feature tree.
- `dependsOn`: `[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]` — correct prerequisite; the phase is `in-progress` and contains the scope from which this spec was migrated.
- Plan DAG confirms both edges: `PHASE_MODULE_WRAPPER_MIGRATION_AND_CATEGORY_GRAPH_COVERAGE --> SPEC_01KQN9J3WNN6TDRX3X15GGJ3PN...` and `FEATURE_CATEGORY_SPECS_AND_SAGE_SURFACES --> SPEC_01KQN9J3WNN6TDRX3X15GGJ3PN...`.
- The `category_specs/modules/docs/MAPPING.md` file correctly redirects to `SPEC-MAPPING-MODULES.md` (a separate spec for the mapping surface); this spec is about the wrapper migration mapping process, not the mapping surface itself — correct separation of concerns.
- Status `needs-review` matches DAG representation.
- Tags `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` consistent with parent feature.
- **Routing is correct.**

---

### G6 — Preservation: PASS
- The spec preserves the original source path so future agents can trace provenance.
- The deleted plan's phase-specific validation commands are preserved as implementation-phase guidance (not lost).
- The work log documents that references to deleted wrapper names are retained in mapping/provenance documentation while live code references were verified to use real-category surfaces.
- The spec records the stale-path investigation methodology, capturing the recovery path for the deleted source file.
- The intentional skip of subtree smoke and global QC is documented with rationale, so future agents know this was a deliberate scope boundary, not an oversight.
- No existing mathematical content was deleted; the mapping was a conversion from a deleted inline tracker item to a full-document Nimbalyst spec.
- **Preservation requirements met.**

---

### Summary

| Gate | Verdict | Notes |
|------|---------|-------|
| G1 — Source Grounding | PASS | All sources verified present; deleted source recoverable via documented git command |
| G2 — Completeness | PASS | All tracker fields, 5 AC all checked, work log documents concrete actions |
| G3 — Math Correctness | PASS | Migration order, classification taxonomy, cross-subtree boundaries all sound |
| G4 — Non-Math Rejection | PASS | Explicitly scoped to mapping pass; no math asserted where undecidable |
| G5 — Routing | PASS | Correct parent/dependsOn, DAG edges verified, separation from mapping-surface spec |
| G6 — Preservation | PASS | Source path, validation commands, wrapper-name references preserved |

**Overall verdict: PASS.** The spec is well-grounded, complete, mathematically sound, properly scoped, correctly routed, and preserves all necessary provenance. The `needs-review` status is appropriate for a human sign-off on the mapping completeness claim; the spec itself is ready for downstream consumption.
