---
id: TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn: []
title: Build source corpus for literal method ownership inventory
status: complete
priority: critical
owner: Zack
description: Enumerate the local inventory, mapping, theory, backend, and spec-backup
  sources that must be mined before method-owner rows are written.
successCriteria:
- The target method-inventory spec records the complete source corpus with paths and
  per-source scope.
- Every `category_specs/*/docs/SAGE_INVENTORY.md` and `category_specs/*/docs/MAPPING.md`
  file is assigned to a topical inventory task.
- Backend and external software notes under `.agents/memories/theory/backends/` are assigned to the
  backend mapping task, including Julia/Oscar, GAP, Singular, Macaulay2, CARAT, and
  Indefinite.jl material where present.
- '`src.bak/spec-backups/*` is marked as mineable source material with the explicit
  warning that it is not current API authority.'
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Build source corpus for literal method ownership inventory

## Summary

Enumerate the source corpus for the method ownership inventory before writing method
rows. This card is the only corpus-building leaf. Later leaves must use its assignment
rather than rediscovering sources ad hoc.

## Source Provenance

- `category_specs/cat/docs/SAGE_INVENTORY.md`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- `category_specs/rings/docs/SAGE_INVENTORY.md`
- `category_specs/rings/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- `category_specs/algebras/docs/MAPPING.md`
- `category_specs/homsets/docs/SAGE_INVENTORY.md`
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/forms/docs/SAGE_INVENTORY.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `category_specs/lattices/docs/MAPPING.md`
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- `category_specs/posets/docs/SAGE_INVENTORY.md`
- `category_specs/posets/docs/MAPPING.md`
- `.agents/memories/theory/backends/software-capability-map.md`
- `.agents/memories/theory/backends/abstract-to-external-mapping.md`
- `.agents/memories/theory/backends/library-integration.md`
- `.agents/memories/theory/backends/comprehensive-tool-docs.md`
- `.agents/memories/theory/backends/oscar-lattices.md`
- `.agents/memories/theory/backends/gap-orbits.md`
- `.agents/memories/theory/backends/indefinite-jl.md`
- `.agents/memories/theory/backends/carat.md`
- `.agents/memories/theory/backends/vinberg-algorithm.md`
- `.agents/memories/theory/backends/buildings.md`
- `.agents/memories/theory/backends/indefinite-isometry.md`
- `.agents/memories/theory/backends/foliation-lib-reusable-procedures.md`
- `.agents/memories/theory/backends/index.md`
- `src.bak/spec-backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`
- `src.bak/spec-backups/lattices_written_spec_backup.py`

## Context

The user asked for all literal expected methods and the subcategory that introduces
each method. The work therefore starts with a corpus map. A method row without a source
path is not acceptable.

## Complexity And Ownership

- Owner/role: category-spec source-mining implementer.
- Complexity: `55` (moderate).
- Rationale: the work touches many files but produces a bounded source assignment,
  not mathematical ownership decisions.
- Split/promote note: do not split unless new inventory families are discovered outside
  the listed corpus.

## Acceptance Criteria

- [x] The target method-inventory spec records the complete source corpus with paths and per-source scope.
- [x] Every `category_specs/*/docs/SAGE_INVENTORY.md` and `category_specs/*/docs/MAPPING.md` file is assigned to a topical inventory task.
- [x] Backend and external software notes under `.agents/memories/theory/backends/` are assigned to the backend mapping task, including Julia/Oscar, GAP, Singular, Macaulay2, CARAT, and Indefinite.jl material where present.
- [x] `src.bak/spec-backups/*` is marked as mineable source material with the explicit warning that it is not current API authority.

## Dependencies And Boundaries

- Do not write final method-owner rows here unless they are needed to illustrate the
  corpus assignment format.
- Do not use `src.bak/spec-backups/*` as current API authority. Treat it as mathematical
  source material requiring later reconciliation.
- If another inventory root is found, add it to the corpus and assign it to exactly one
  topical task.

## Work Log

- 2026-05-05: Created as first leaf for the literal method ownership inventory phase.
- 2026-05-06: Enumerated 22 category-spec inventory/mapping docs, 12 backend notes,
  and two lattice spec-backup files. Added the corpus assignment to
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` and moved this task to
  needs-review.
- 2026-05-06: Gate 1 review found stale source roots from the old `theory/backends/`
  and `theory/spec_backups/` paths. Updated this card and the target spec to point to
  the visible `.agents/memories/theory/backends/` and `src.bak/spec-backups/`
  roots, including the backend routing index and the buildings, indefinite-isometry,
  and foliation notes found by broad source search.
- 2026-05-06: Repaired the spec-backup source root after the method-inventory spec
  re-review found that the old `.agents/theory/spec-backups/` path is stale. The
  current mineable source files live under `src.bak/spec-backups/`.

## Review Log

### Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding and path provenance for the source
corpus; markdown diff check; tracker validation.
**Gates failed:** None in the reviewed scope.
**Outcome:** no concrete revision findings; human approval remains required before
marking the card complete.

Findings:

- Verified 22 actual `category_specs/*/docs/{SAGE_INVENTORY,MAPPING}.md` files and
  confirmed they are assigned exactly once in
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`.
- Verified all 15 backend/spec-backup paths cited in the assignment exist under
  `.agents/memories/theory/backends/` and the current `src.bak/spec-backups/`
  source root after the path repair above.
- Verified the rework is provenance-only and does not weaken acceptance criteria or
  move method ownership claims.

Residual gap: dependent inventory tasks remain DAG-gated until this card receives
human approval and can be marked complete.

### Re-Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance.
**Gates failed:** None.
**Outcome:** no concrete revision findings; human approval remains required before
marking the card complete.

Findings: none. The review found the parent phase, this task, and the target spec now
agree on the current `src.bak/spec-backups/` source root. The old
`.agents/theory/spec-backups/` string remains only in historical notes describing the
repaired defect.

### Re-review 2026-05-06 (James)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- The target method-inventory spec records the source assignment for category docs,
  spec backups, and backend notes, including the warning that spec backups are
  mineable source material rather than current API authority.
- `git diff --cached` and `git diff` on the task/spec surface were empty during the
  read-only review, so no spec weakening or backsliding was found.
- `just plan-validate` passed with `Validated 224 root planning cards.`

#### Residual Risks

- Smoke tests were not run because this is a planning/spec-corpus card, not an
  implementation validation card.
- Downstream geometry/backend source admission remains delegated to dependent
  inventory cards.
