---
id: TASK-1777748120685-4VX3GB-STRIP-IMPORT-AND-LAZYIMPORT-BLOAT-FROM-RING-SUBCATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Strip import and LazyImport bloat from ring subcategory constructors
status: complete
priority: high
description: Strip import and LazyImport bloat from ring subcategory constructors
successCriteria:
- Ring subcategory modules no longer duplicate top-level LazyImport blocks for shared
  private subcategory references.
- Shared Sage ring class tuples and shared lazy subcategory references are centralized
  without weakening the public category/spec surface.
- Remaining LazyImport calls are limited to intentional public axiom/subcategory constructors
  or the centralized helper module.
- Python syntax validation passes for category_specs/rings/subcategories.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
complexity: 58
---
# Strip import and LazyImport bloat from ring subcategory constructors
Source: pasted backlog 2026-05-02.

Task: strip import and LazyImport bloat from the ring subcategory constructors, fix the public surface to use canonical constructors.

## Grounding And Scope

- This is implementation-hygiene work inside `category_specs/rings/subcategories/`, not a mathematical ownership change.
- Preserve the existing ring category/spec obligations and public axiom constructor surface.
- Do not make category-obligation tests pass by weakening the ideal interface; Sage gaps route to implementation, wrapper, decision, or source-mining work.
- Blocked children are not acceptance. This card is review-ready only because its own scoped cleanup has been implemented and validated.

## Work Completed

- Added `category_specs/rings/subcategories/_lazy_subcategories.py` as the single local source for shared private lazy references between ring subcategories.
- Added `category_specs/rings/subcategories/_sage_ring_classes.py` as the single local source for Sage polynomial, power-series, Laurent-series, Puiseux-series, and lazy-series class tuples.
- Replaced copied top-level private `LazyImport(...)` blocks in ring subcategory modules with imports from the shared helper.
- Preserved the intentional indented `LazyImport(...)` class attributes that expose public axiom/subcategory constructors such as `Commutative().Field`, `IntegralDomains().Gcd`, and `Fields().NumberFields`.
- Removed duplicate imports of Sage series/polynomial classes from individual subcategory modules that now consume the centralized class tuples.

## Historical Commit-Gate Note

- The implementation cleanup was once present in the working tree but not committed
  because the repo pre-commit hook reached broad global mypy failures.
- The cleanup is now committed in the history for the helper modules and follow-up
  style slices, including `4904e17`, `bacb146`, and `108c00c`.
- The `.bak` exclusion fixed stale backup-directory scan surface only. Public
  `just test` still reaches global mypy failures, including Sage import-stub gaps
  and category typing errors. That is public-QC phase-transition evidence, not a
  phase-local blocker for this scoped import-cleanup leaf.

## Acceptance Notes

- `rg -n "^_[A-Za-z0-9]+ = LazyImport\(" category_specs/rings/subcategories -g '!_lazy_subcategories.py'` returns no matches.
- `rg -n "LazyImport\(" category_specs/rings/subcategories -g '!_lazy_subcategories.py'` now finds only indented axiom/subcategory constructor attributes.
- `python -m compileall -q category_specs/rings/subcategories` passed.
- Spec-weakening review: this diff centralizes imports and shared runtime class tuples only; it does not delete abstract methods, narrow category assertions, move mathematical obligations, or change category ownership.

## Review Log

### Review - 2026-05-07

Outcome: review passes for the scoped task; card remains `needs-agent-review` for human
acceptance.

- Verified that `category_specs/rings/subcategories/_lazy_subcategories.py` is the
  single local home for top-level shared private `LazyImport(...)` references.
- Verified that `category_specs/rings/subcategories/_sage_ring_classes.py` is the
  single local home for shared Sage polynomial, power-series, Laurent-series,
  Puiseux-series, and lazy-series class tuples.
- `rg -n "^_[A-Za-z0-9]+ = LazyImport\(" category_specs/rings/subcategories -g
  '!_lazy_subcategories.py'` returned no matches.
- `rg -n "LazyImport\(" category_specs/rings/subcategories -g
  '!_lazy_subcategories.py'` found only indented public axiom/subcategory
  constructor attributes.
- `python -m compileall -q category_specs/rings/subcategories` passed.
- `just test` still fails at global mypy before later QC stages. The first current
  failures are Sage import-stub gaps in `_sage_ring_classes.py` and
  `_lazy_subcategories.py`, followed by broad existing Sage/pytest/category typing
  errors across the repo. This does not invalidate the task-local syntax/search
  acceptance criteria, but it must not be recorded as cleared.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Task Completeness, Gate 2 Correctness, Gate 3 Acceptance Criteria, Gate 4 Scope Boundary, Gate 5 Style, Gate 6 No Spec Weakening

**Gates failed:** none

**Outcome:** complete. All six gates pass.

- Gate 1: Created `_lazy_subcategories.py` (169 lines) and `_sage_ring_classes.py` (29 lines). 50+ subcategory files updated.
- Gate 2: compileall passes. No circular imports. LazyImport targets correct.
- Gate 3: All 4 ACs verified (rg search confirms no private LazyImport outside helper, compileall passes).
- Gate 4: Only files under rings/subcategories/ modified. No scope creep.
- Gate 5: Relative imports, _prefix convention, Google docstrings.
- Gate 6: No abstract methods, constructor obligations, or category-obligation examples removed.

## Complexity Justification

- Owner: C58.
- Complexity band: Moderate (41-60).
- Tracker type: task.
- Why this specific score: focused cleanup in the ring subcategory constructor path with moderate coupling. Import/lazy-import shape and canonical constructor exposure affect module load behavior and API consistency, but the work stays inside a bounded ring-subcategory surface.
- Item-specific evidence: deterministic refactoring, no new mathematical algorithm, and validation through static search plus Python syntax compilation.
