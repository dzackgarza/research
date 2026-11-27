---
id: TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Triage category_specs Ruff normalization blocker for implementation validation
status: complete
priority: high
description: '`just test` reaches the global quality-control Ruff normalization stage
  but fails on repo-wide `category_specs` findings. This blocks validation evidence
  for implementation cards even when the implementation diff is narrower than the
  QC backlog.'
successCriteria:
- Reproduce the current `just test` Ruff blocker and preserve a concise failure summary
  in this card.
- Classify remaining findings by owner surface and rule family without weakening global
  QC.
- Split owner-specific cards for independent cleanup surfaces that are not one coherent
  patch.
- Carry forward formatter/linter auto-fixes already produced by repository tooling.
- Either make `just test` pass or record exactly which linked cards remain validation
  blockers.
complexity: 78
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Triage category_specs Ruff normalization blocker for implementation validation

## Summary

`just test` reaches the global quality-control Ruff normalization stage but fails on
repo-wide `category_specs` findings. This blocks validation evidence for implementation
cards even when the implementation diff is narrower than the QC backlog.

## Source Provenance

- Triggered while validating
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION/tasks/TASK-1777748120649-EQPN1A-ADD-MISSING-FINAL-MARKERS-AND-RETURN-ANNOTATIONS-ON-CAT-METHODS.md`.
- `just test` output on 2026-05-03: Ruff auto-fixed 80 findings, then reported 534
  remaining findings across `category_specs`.
- `.agents/current-goal-phase.md` says QC is a gate for implementation surfaces and
  phase transitions, while incidental QC cleanup should not steer churn-heavy spec
  work.
- Owning plan: `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`, under `PLAN-CATEGORY-OBLIGATION-EXAMPLES`.

## Context

The blocker is larger than the Cat final-marker task. The first non-obvious routing
choice is to avoid burying hundreds of Ruff findings inside an unrelated Cat card.
The correct next step is a triage pass that separates validation-blocking cleanup from
spec-phase noise and opens owner-specific work when the findings are not one coherent
fix.

Observed representative finding classes include:

- `E402` import placement findings in package initialization/type aggregation surfaces.
- `F401` re-export/import findings where public re-export intent must be made explicit
  or the import removed.
- `E501` long-line findings across generated or broad subcategory import surfaces.
- `UP047` type-parameter modernization findings in utility helpers.

## Triage Result

Codex Spark read-only triage on 2026-05-03 reproduced the blocker and reported that
the current `just test` normalization pass still fails with 534 Ruff errors after the
previous auto-fixes. The remaining rule-family summary was:

- `E501`: 420 line-length findings.
- `F401`: 87 unused-import findings.
- `E402`: 25 import-placement findings.
- `UP047`: 2 generic-type-parameter modernization findings.

The triage found no single coherent implementation patch. The blocker should be
resolved through these leaf cards:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-IMPORT-HYGIENE-RUFF-F401-E402.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-E501-LONG-LINE-NORMALIZATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-UTILS-UP047-MODERNIZATION.md`

After resolving the `UP047` utility leaf locally, `just test` still fails in the same
global QC Ruff normalization stage with 532 remaining findings, all in the import
hygiene and long-line cleanup surfaces.

After resolving the import-hygiene leaf, `uvx --from ruff ruff check --select
F401,E402,F821 category_specs` passes. `just test` now reaches the same Ruff
normalization stage and reports 424 remaining `E501` findings, all owned by the linked
long-line normalization card.

After resolving the long-line normalization leaf, the Ruff normalization stage passes.
`just test` now fails later in global vulture dead-code detection; that is tracked
separately in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.

Current 2026-05-07 validation after the reopened E501 cleanup: `uvx --from ruff ruff
check --select E501 category_specs --output-format json | jq 'length'` reports `0`.
`just test` now passes Python syntax validation and Sage syntax validation, then fails
earlier than Ruff at the global mypy stage with broad existing Sage/pytest import-stub
and category typing errors. The active validation blocker is therefore not a Ruff
normalization blocker. It is a global type-checking/QC issue already noted in adjacent
validation cards, and it does not block DAG-ready spec-phase leaves unless the user is
attempting a QC/phase-transition gate.

2026-05-07 review rerun of full `uvx --from ruff ruff check category_specs` found
that the prior Ruff-normalization claim was still stale: `I001` import-order findings,
several compatibility-alias `E501` lines, and seven `E741` ambiguous single-letter
parameters remained. The import-order findings were fixed with
`uvx --from ruff ruff check --select I001 --fix category_specs`; the residual
compatibility aliases and mathematical parameter names were fixed manually without
removing public re-export names. Full `uvx --from ruff ruff check category_specs`
now passes.

## Complexity And Ownership

- Owner role: audit/validation worker, with parent-agent review.
- Complexity: 78, high band.
- Rationale: the work touches many category-spec surfaces and validation policy, but
  the first deliverable is triage plus bounded owner-specific splits, not a single
  repo-wide rewrite. If the triage shows the blocker requires several independent
  cleanups, split those cards before implementation.

## Acceptance Criteria

- [x] Reproduce the current `just test` Ruff blocker and preserve a concise failure
  summary in this card.
- [x] Classify remaining findings by owner surface and rule family without weakening
  global QC.
- [x] Split owner-specific cards for independent cleanup surfaces that are not one
  coherent patch.
- [x] Carry forward formatter/linter auto-fixes already produced by repository tooling.
- [x] Either make `just test` pass or record exactly which linked cards remain
  validation blockers.

## Dependencies And Boundaries

- Do not add project-local QC bypasses, Ruff ignores, local whitelists, or quality-control
  overrides.
- Do not fold this broad cleanup into the Cat final-marker task.
- Do not rewrite mathematical specs only to satisfy formatting if the rewrite changes
  source meaning.
- Use `just test`; do not substitute ad hoc Ruff-only success for full validation.

## Validation Requirements

- Run `just test` after any attempted cleanup.
- If `just test` still fails, record the first blocking stage and representative rule
  families with enough detail to route the next card.

## Work Log

- 2026-05-03: Created after Cat implementation validation exposed a repo-wide Ruff
  normalization blocker.
- 2026-05-03: Codex Spark read-only triage reproduced the blocker, classified the
  remaining findings, and recommended splitting by import hygiene, line-length
  normalization, and `UP047` utility modernization.
- 2026-05-03: Resolved the `UP047` utility leaf locally; targeted Ruff and compileall
  pass for `category_specs/utils.py`. Full `just test` remains blocked by the linked
  import-hygiene and `E501` leaf cards.
- 2026-05-03: Resolved the import-hygiene leaf enough for full category-spec
  `F401`/`E402`/`F821` Ruff diagnostics to pass. Full `just test` remains blocked by
  424 `E501` long-line findings, delegated to Codex Spark under the linked long-line
  leaf card.
- 2026-05-03: Resolved the long-line leaf enough for Ruff format/check to pass inside
  `just test`. Validation now advances to and fails at global vulture dead-code
  detection, so the remaining validation gate is no longer a Ruff-normalization
  blocker.
- 2026-05-07: Re-ran validation after the reopened E501 cleanup. `uvx --from ruff
  ruff check --select E501 category_specs --output-format json | jq 'length'` reports
  `0`. `just test` passes Python and Sage syntax validation, then fails at global
  mypy before Ruff with broad existing Sage/pytest import-stub and category typing
  errors. The Ruff-normalization blocker remains cleared; the current full-QC blocker
  is not phase-local Ruff work.
- 2026-05-07: Re-ran full `uvx --from ruff ruff check category_specs` and found 76
  current Ruff findings. Applied the mechanical `I001` import-order fixes and
  manually resolved the remaining `E501` compatibility-alias lines plus `E741`
  ambiguous parameter names (`ideal` for ideals and `ell` for tensor rank). Full
  `uvx --from ruff ruff check category_specs` now passes.
- 2026-05-07: `python -m compileall -q category_specs` passed after the Ruff
  normalization cleanup.
- 2026-05-07: `git diff --check -- category_specs` passed.
- 2026-05-07: `just test` still passes Python and Sage syntax validation, then fails
  at global mypy before reaching Ruff. Representative first errors remain missing
  Sage stubs in `category_specs/rings/subcategories/_sage_ring_classes.py` and
  `_lazy_subcategories.py`, missing `pytest` stubs in `tests/conftest.py`, and broad
  existing annotation/type-surface errors. The first full-QC blocker is therefore
  still mypy, not Ruff normalization.

## Review Log

### Self-Review - 2026-05-07

Outcome: revision was required, then fixed in scope. The card remains
`needs-agent-review`; human acceptance is still required before completion.

Findings and resolution:

- Gate 2 initially failed on current evidence: direct full Ruff still reported 76
  findings, so the card's claim that Ruff normalization was cleared was stale.
- Gate 3 passed after rework: the cleanup did not delete category obligations,
  constructor surfaces, abstract methods, or category assertions. Compatibility names
  were preserved through import-safe aliases or module-backed assignments.
- Gate 6 passed after rework: `uvx --from ruff ruff check category_specs`,
  `python -m compileall -q category_specs`, and `git diff --check -- category_specs`
  pass. Full `just test` remains stopped by global mypy before Ruff.

### Independent Review - 2026-05-07

Reviewer: Carver.

Outcome: revision required on the pre-fix working tree, then fixed in scope. Do not
mark complete without human approval.

Findings and resolution:

- Gate 2 failed in the pre-fix working tree: targeted Ruff still reported live
  `E501` failures in `category_specs/cat/__init__.py`,
  `category_specs/lattices/subcategories/alternating.py`, and
  `category_specs/lattices/subcategories/nondegenerate.py`, contradicting the
  then-current claim that the Ruff-normalization blocker was cleared.
- The reviewer also confirmed that `just test` failed before Ruff at global mypy, so
  the first full-QC blocker was correctly non-Ruff once direct Ruff is clean.
- The reviewer found no local QC bypasses and no evidence of spec weakening in the
  inspected cleanup path.
- The live post-fix check now passes the reviewer-targeted command:
  `uvx --from ruff ruff check --select E501,F401,E402,F821,UP047 category_specs
  --output-format concise`.
