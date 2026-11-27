---
id: TASK-BUG-CATEGORY-SPECS-IMPORT-HYGIENE-RUFF-F401-E402
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Resolve category_specs import-hygiene Ruff F401 and E402 blockers
status: complete
priority: high
description: Resolve the remaining Ruff `F401` and `E402` validation blockers in package
  initialization and type-aggregation surfaces without weakening global QC or changing
  public category-spec meaning.
successCriteria:
- Reproduce the current `F401` and `E402` findings for `category_specs`.
- Preserve intentional public re-export behavior with explicit exports or equivalent
  repo-approved structure.
- Remove accidental unused imports and move imports to compliant positions where doing
  so does not change semantics.
- Do not add local Ruff bypasses, ignores, whitelists, or quality-control exceptions.
- Record any public-surface ambiguity as a linked decision card instead of guessing.
complexity: 72
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Resolve category_specs import-hygiene Ruff F401 and E402 blockers

## Summary

Resolve the remaining Ruff `F401` and `E402` validation blockers in package
initialization and type-aggregation surfaces without weakening global QC or changing
public category-spec meaning.

## Source Provenance

- Split from `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Codex Spark triage on 2026-05-03 reported 87 `F401` findings and 25 `E402`
  findings after `just test` reached the global QC Ruff normalization stage.
- Representative surfaces include `category_specs/__init__.py`,
  `category_specs/cat/__init__.py`, `category_specs/topological_spaces/__init__.py`,
  `category_specs/types.py`, and package `__init__.py` files for algebras, forms,
  homsets, posets, and sets.

## Context

These findings are not ordinary private-code cleanup. Most affected files are public
package aggregation surfaces, so every import change must distinguish accidental unused
imports from intentional re-export surfaces. Prefer explicit public exports or import
placement cleanup over local Ruff bypasses.

## Complexity And Ownership

- Owner role: implementation worker with parent review.
- Complexity: 72, high band.
- Rationale: the patch spans several public aggregation surfaces and can accidentally
  change import availability if handled mechanically. The scope is still one coherent
  import-hygiene cleanup because `F401` and `E402` interact on the same package
  surfaces.

## Acceptance Criteria

- [x] Reproduce the current `F401` and `E402` findings for `category_specs`.
- [x] Preserve intentional public re-export behavior with explicit exports or
  equivalent repo-approved structure.
- [x] Remove accidental unused imports and move imports to compliant positions where
  doing so does not change semantics.
- [x] Do not add local Ruff bypasses, ignores, whitelists, or quality-control
  exceptions.
- [x] Record any public-surface ambiguity as a linked decision card instead of guessing.

## Dependencies And Boundaries

- Parent blocker: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Do not mix broad line-length-only normalization into this card except where required
  to make the same import-hygiene edit readable.
- Do not rewrite category specs or package APIs for style alone.

## Validation Requirements

- Run `just test` after the cleanup attempt.
- If `just test` remains blocked, record the first remaining blocker and representative
  rule families in this card and the parent blocker.

## Work Log

- 2026-05-03: Created from Codex Spark triage of the category-specs Ruff normalization
  blocker.
- 2026-05-03: Reproduced import-hygiene findings with
  `uvx --from ruff ruff check --select F401,E402 category_specs`: remaining findings
  were only in `category_specs/modules/__init__.py` and `category_specs/rings/__init__.py`
  (7 `F401` findings from `typing.Any`, `Cat`, and `RMod*` imports).
- 2026-05-03: Executed scoped import-hygiene check over requested ownership boundary:
  targeted `uvx --from ruff ruff check --select F401,E402` over package aggregation
  files and it passed.
- 2026-05-03: Reviewed the Codex Spark patch, replaced a dynamic `globals().update`
  type-export workaround in `category_specs/types.py` with ordinary top-level imports
  so names remain visible to Ruff, and removed the remaining modules/rings unused
  imports locally.
- 2026-05-03: `uvx --from ruff ruff check --select F401,E402,F821 category_specs`
  now passes. `python -m compileall` passes for the changed import-hygiene files.
  `just test` still fails in global Ruff normalization with 424 `E501` findings,
  now tracked by the linked long-line normalization card.
- 2026-05-05: Forms compatibility shims were restored with the same redundant-alias
  re-export pattern used by package aggregation surfaces. Targeted `ruff check` on
  those shim files passed, and this card is moved to in-review for human closure.
- 2026-05-07: Review rerun of
  `uvx --from ruff ruff check --select F401,E402,F821 category_specs` found 12
  current `F401` findings, so the prior in-review state was stale. Fixed the
  remaining explicit re-export/import-hygiene surface by:
  - preserving long formed-module compatibility names via module-backed public
    assignments in `category_specs/forms/__init__.py`;
  - preserving `category_specs.lattices.chain.LatticesCategory` and
    `category_specs.modules.GradedModulesCategory` with explicit redundant aliases;
  - removing unused lazy-subcategory imports from topological and valued ring
    subcategory files where the string-based `LazyImport` already carries the route.

## Validation

- 2026-05-07: `uvx --from ruff ruff check --select F401,E402,F821 category_specs`
  passed.
- 2026-05-07: `uvx --from ruff ruff check --select E501
  category_specs/forms/__init__.py category_specs/lattices/chain.py
  category_specs/modules/__init__.py category_specs/rings/subcategories/topological.py
  category_specs/rings/subcategories/valued.py` passed.
- 2026-05-07: `python -m py_compile category_specs/forms/__init__.py
  category_specs/lattices/chain.py category_specs/modules/__init__.py
  category_specs/rings/subcategories/topological.py
  category_specs/rings/subcategories/valued.py` passed.
- 2026-05-07: `git diff --check -- category_specs/forms/__init__.py
  category_specs/lattices/chain.py category_specs/modules/__init__.py
  category_specs/rings/subcategories/topological.py
  category_specs/rings/subcategories/valued.py` passed.
- 2026-05-07: `just test` passes Python syntax validation and Sage syntax
  validation, then fails at global mypy before Ruff. Representative first errors
  are missing Sage stubs in
  `category_specs/rings/subcategories/_lazy_subcategories.py`,
  `category_specs/rings/subcategories/_sage_ring_classes.py`, and
  `category_specs/axioms.py`, missing `pytest` stubs in `tests/conftest.py`, and
  broad existing annotation/type-surface errors. This matches the parent
  Ruff-normalization card's current blocker note: the import-hygiene blocker remains
  cleared, and the remaining full-QC failure is not an F401/E402/F821 issue.

## Review Log

### Self-Review - 2026-05-07

Outcome: revision was required, then fixed in scope. The card remains
`needs-agent-review` because independent review and human acceptance are separate gates.

Findings and resolution:

- Gate 2 initially failed: the claimed import-hygiene validation was stale because
  current `F401` findings remained in forms, lattices, modules, topological rings,
  and valued rings surfaces.
- Gate 3 passed after rework: no public aggregation surface was removed. Public
  compatibility names are preserved by explicit aliases or module-backed public
  assignments; the removed ring imports were unused implementation imports, not
  public exports.
- Gate 6 passed after rework: targeted `F401`, `E402`, `F821`, and touched-file
  `E501` checks pass.

### Independent Review - 2026-05-07

Reviewer: Jason.

Outcome: revision required for stale validation routing, then fixed in scope. Do not
mark complete without human approval.

Findings and resolution:

- Gate 2 found stale blocker routing: this card still carried the old note that
  `just test` stopped at global Ruff `E501`, while the parent blocker already records
  that current full validation stops earlier at global mypy.
- The core import-hygiene claim passed review: `uvx --from ruff ruff check --select
  F401,E402,F821 category_specs` passed, and the reviewer found no public-surface
  weakening in the inspected re-export files.
- The validation note above now records the current `just test` first blocker as
  global mypy, keeping this card aligned with the parent blocker.
