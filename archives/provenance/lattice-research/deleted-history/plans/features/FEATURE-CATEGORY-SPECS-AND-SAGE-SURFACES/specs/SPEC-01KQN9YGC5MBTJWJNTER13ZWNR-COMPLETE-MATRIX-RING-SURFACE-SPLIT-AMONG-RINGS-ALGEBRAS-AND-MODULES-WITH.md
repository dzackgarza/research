---
id: SPEC-01KQN9YGC5MBTJWJNTER13ZWNR-COMPLETE-MATRIX-RING-SURFACE-SPLIT-AMONG-RINGS-ALGEBRAS-AND-MODULES-WITH
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
title: Complete matrix ring surface split among rings algebras and modules without
  weakening the matrix smoke
status: complete
priority: critical
requirement: 'The deleted Rings triage recorded ring smoke blockers: nested axiom
  category identity mismatches, missing _sympy_ methods on refined parents, and the
  matrix-ring surface split.'
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No new implementation blocker was discovered during this docs/spec pass; the existing
  implementation proof remains the matrix smoke frontier.
- No ring constructor or axiom code changed, so the `rings/smoketest.sage` trigger
  did not apply in this pass.
- Constructor membership assertions were not weakened; the docs now preserve simultaneous
  ring/algebra/module refinement as the smoke expectation.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke
## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- The requested recovery path `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`
  fails because the file still lived under `plans/category_specs/rings/docs/TRIAGE.md`
  at that parent commit.
- Exact recovered prior content came from
  `git show 8d1c21c^:plans/category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke from category_specs/rings/docs/TRIAGE.md`
- Sage written-doc and source anchors used for this leaf:
  `https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_space.html`,
  `https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module.html`,
  `https://doc.sagemath.org/html/en/reference/rings/sage/rings/ring.html`,
  `category_specs/modules/docs/SAGE_INVENTORY.md`,
  and the current mapping docs in `rings`, `algebras`, and `modules`.

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/rings/docs/MAPPING.md`, especially the rows for `MatrixRing`,
  `MatrixSpace.matrix(...)`, and the `Matrix ring/algebra surface` organization rule.
- `category_specs/rings/docs/SAGE_INVENTORY.md`, especially the constructor-family row
  for `MatrixRing` and `MatrixSpace` when square.
- `category_specs/algebras/docs/MAPPING.md`, especially the row stating that
  matrix-ring algebra methods belong in `Algebras(R)` plus matrix-algebra
  subcategories.
- `category_specs/modules/docs/MAPPING.md`, especially the owner table for
  `Modules(R).Free().FiniteRank()` and the rule that vector-space/free-module structure
  stays in `modules`.

Grounded owner rule for this leaf:

- `Rings().Constructors().MatrixRing(...)` remains the constructor entry point because
  it creates the ambient square-matrix ring object.
- The constructed parent must refine simultaneously into the ring surface,
  the algebra surface over its base ring, and the free finite-rank module surface over
  that base ring.
- Method placement follows that split: ring operations stay in `rings`, algebra
  operations in `algebras`, and rank/basis/module operations in `modules`.

Required hypotheses and codomains:

- the object under discussion is a square matrix parent over a base ring `R`;
- the ring codomain is the matrix ring parent itself;
- the algebra codomain is the same parent viewed in `Algebras(R)` or the matrix-algebra
  refinement;
- the module codomain is the same parent viewed in `Modules(R).Free().FiniteRank()`.

Rejection/retirement condition:

- reject any spec move that collapses the owner split by relocating all matrix methods
  into one subtree, or that weakens matrix smoke expectations to avoid proving the same
  parent refines into rings, algebras, and modules simultaneously.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass; the existing implementation proof remains the matrix smoke frontier.
- [x] No ring constructor or axiom code changed, so the `rings/smoketest.sage` trigger did not apply in this pass.
- [x] Constructor membership assertions were not weakened; the docs now preserve simultaneous ring/algebra/module refinement as the smoke expectation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the removed rings triage wording from
  `plans/category_specs/rings/docs/TRIAGE.md` at `8d1c21c^` after broadening the path
  search.
- Recorded the owner split in the mapping docs: `Rings().Constructors().MatrixRing(...)`
  remains the constructor owner; the returned square matrix parent simultaneously
  refines into `Rings()`, `Algebras(R)`, and `Modules(R).Free().FiniteRank()`.
- Kept the matrix smoke requirement intact: no constructor relocation and no weakening
  of simultaneous refinement expectations.

## 6-Gate Protocol Review Log

**Reviewer**: subagent
**Date**: 2026-05-07
**Card**: SPEC-01KQN9YGC5MBTJWJNTER13ZWNR-COMPLETE-MATRIX-RING-SURFACE-SPLIT

### G1: Source Grounding — PASS

All claimed source anchors verified as of review date:

- **Git provenance**: Commit `8d1c21c` exists in repository. File `plans/category_specs/rings/docs/TRIAGE.md` at `8d1c21c^` contains the exact original migrated line: "Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke from category_specs/rings/docs/TRIAGE.md". The spec's note that the shorter path `category_specs/rings/docs/TRIAGE.md` fails is confirmed accurate — the file lived under the `plans/` prefix at that commit.

- **Sage documentation URLs**: All three are valid (HTTP 200):
  - `https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_space.html`
  - `https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module.html`
  - `https://doc.sagemath.org/html/en/reference/rings/sage/rings/ring.html`

- **SAGE_INVENTORY.md**: `category_specs/rings/docs/SAGE_INVENTORY.md` line 42 contains the row: `MatrixRing`, `MatrixSpace` when square — "Square matrix spaces with ring, algebra, and module category structure in Sage."

- **MAPPING.md files**: The spec references `category_specs/{rings,algebras,modules}/docs/MAPPING.md` directly. These files now redirect to canonical tracked specs:
  - `rings/docs/MAPPING.md` → `SPEC-MAPPING-RINGS.md` — line 220: MatrixRing constructor entry with explicit note that "refinement into algebra and module categories happens on the returned parent rather than by relocating the constructor."
  - `algebras/docs/MAPPING.md` → `SPEC-MAPPING-ALGEBRAS.md` — line 162: "Matrix-ring algebra methods | Algebras(R) plus matrix-algebra subcategories" confirming algebra methods stay in algebras even though constructor owner stays in rings.
  - `modules/docs/MAPPING.md` → `SPEC-MAPPING-MODULES.md` — line 214: "Square MatrixRing(R, n) / MatrixSpace(R, n, n) viewed over R | The same parent refined into Modules(R).Free().FiniteRank()" confirming free finite-rank module structure on the same parent.

- **Minor staleness note**: The spec cites `category_specs/*/docs/MAPPING.md` as the direct mapping source, but those files now contain only redirect stubs. The actual content lives in the tracked specs listed above. This does not invalidate the grounding — the content exists and is consistent with the spec's claims.

### G2: Completeness — PASS

The spec card is structurally complete:
- Frontmatter: id, trackerStatus, parents, dependsOn, title, status, priority, requirement, acceptanceCriteria, tags — all populated.
- Body sections: Summary, Source Provenance, Context, Grounded Spec Contract (with: grounding anchors, grounded owner rule, required hypotheses/codomains, rejection/retirement condition), Acceptance Criteria (all checked), Dependencies and Boundaries, Work Log, plus this review log.
- The surface split across rings, algebras, and modules is fully specified with clear owner assignments, codomain descriptions, and migration consequences.
- No missing sections or placeholder content.

### G3: Math Correctness — PASS

The mathematical claims are standard and correct:

- **Claim**: A square matrix parent over a base ring R simultaneously refines into Rings(), Algebras(R), and Modules(R).Free().FiniteRank().
- **Verification**: For a commutative ring R, the set M_n(R) of n×n matrices is:
  - A **ring** under matrix addition and multiplication (associative, unital with identity matrix I_n).
  - An **R-algebra** because R embeds as scalar matrices r·I_n, and the multiplication is R-bilinear: (rA)B = r(AB) = A(rB).
  - A **free R-module of finite rank n²** with basis {E_{ij} : 1 ≤ i,j ≤ n} where E_{ij} is the matrix with 1 at position (i,j) and 0 elsewhere. Additive structure and scalar multiplication are entry-wise.
- The owner split is logically sound:
  - Constructor lives in rings (creates the ambient object).
  - Ring operations (multiplication, units, ideals) stay in rings.
  - Algebra operations (R-bilinear product, unit, center, radical) stay in algebras.
  - Module operations (rank, basis, coordinate vectors, submodules) stay in modules.
- No category-theoretic contradiction: a single object can carry multiple category structures. The spec correctly uses Sage's category refinement mechanism where one parent object refines into multiple categories.

### G4: Nonmath Rejection — PASS

The spec includes explicit non-mathematical rejection/retirement conditions:
- Reject any spec move that collapses the owner split by relocating all matrix methods into one subtree.
- Reject any spec move that weakens matrix smoke expectations to avoid proving simultaneous refinement.
- Acceptance criteria forbid: new subtree-local TRIAGE/process documents, implementation blockers, code changes, weakening of constructor membership assertions.
- These are procedural/spec-integrity guards, not mathematical conditions. They are valid and well-scoped.

### G5: Ambiguity Routing — PASS

The spec routes ambiguity proactively:
- "If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it."
- Dependencies section directs: preserve original source path, do not recreate subtree-local TRIAGE.md files, keep SAGE_INVENTORY.md and MAPPING.md as provenance.
- The spec does not attempt to resolve unknown future issues inline — it delegates to the tracker system.

### G6: Preservation — PASS

- Source provenance recorded with exact git commands and commit hash (`8d1c21c`).
- Original migrated line preserved verbatim in the Source Provenance section.
- Work log records the recovery steps taken during migration repair.
- Acceptance criterion 5 confirms: "Constructor membership assertions were not weakened; the docs now preserve simultaneous ring/algebra/module refinement as the smoke expectation."
- The spec explicitly states: "The matrix smoke must not be moved or weakened to hide the surface split."

### Overall Assessment: ALL GATES PASS

The spec is well-grounded in verifiable sources, mathematically correct, complete in structure, and preserves the original smoke requirement without weakening. Minor staleness in the MAPPING.md references (now redirects) does not affect substantive correctness — the content referenced exists in the redirected tracked specs and is fully consistent with the spec's claims.

### Recommendations
- Consider updating the MAPPING.md references in the Grounding Anchors section to point to the canonical tracked spec files (SPEC-MAPPING-RINGS.md etc.) rather than the redirect stubs, to avoid future confusion.
- No blocking issues found. Card is ready for review acceptance.
