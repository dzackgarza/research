---
id: TASK-VERTICAL-SLICE-SPEC-REPORT-SMOKE
trackerStatus:
  type: task
parents:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn:
- '[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]'
title: Validate the spec report vertical slice
status: complete
priority: critical
description: Add focused validation proving the finite `GF(5)^3`, countable `ZZ^2`,
  and missing-obligation report behavior for the spec-core vertical slice.
activityType: validation
workstreamRole: review
claimStatus: computationally-supported
uncertaintyState: none-recorded
successCriteria:
- Focused validation proves the finite `GF(5)^3` report with cardinality `125`.
- Focused validation proves the countable `ZZ^2` report with infinite cardinality
  and inherited enumeration obligation.
- A deliberately incomplete claimant produces a precise missing-obligations report.
- Validation runs through repo `just` recipes or an added focused recipe, not ad hoc
  one-off commands.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SPEC-CORE-VERTICAL-SLICE
- PHASE-SPEC-CORE-VERTICAL-SLICE
---
# Validate the spec report vertical slice

## Summary

Add the focused checks that make the pivot measurable. This task proves that the new
spec-core and module witness layers produce inspectable reports for the two admitted
examples and for a failing claimant.

## Source Provenance

- `[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]`
- `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`
- `tests/category_specs/test_spec_smoke.py`
- `category_specs/modules/smoketest.sage`
- Root `justfile`

## Context

This task is the success metric for the pivot. Broad smoke recovery, full-suite mypy,
and unrelated constructor fixes are not substitutes for focused report output.

## Acceptance Criteria

- [x] The validation artifact checks the exact report fields for `GF(5)^3`: declared
  category, cartesian-power witness, finite cardinality `125`, and provider provenance.
- [x] The validation artifact checks the exact report fields for `ZZ^2`: declared
  category, cartesian-power witness, infinite cardinality, countability, and
  deterministic-enumeration obligation.
- [x] The validation artifact includes a failing claimant or fixture that reports
  missing obligations without broad smoke noise.
- [x] The validation command is exposed through `just` if no existing focused recipe
  covers it.
- [x] The task records why any skipped full-suite checks are non-diagnostic for this
  slice.

## Dependencies And Boundaries

Do not weaken existing smokes to pass this task. Add focused checks or a focused recipe
that answers the slice question directly.

## Complexity And Ownership

Owner role: validation/review agent. Complexity: 60. The work is moderate because it
depends on the preceding implementation tasks, but its validation surface is narrow and
falsifiable.

## Work Log

- Created as the validation leaf of the pivot plan.
- Started after `TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES` was accepted
  through merged PR #4.
- Added `just test-spec-core-vertical-slice` as the focused validation command for the
  spec-core report kernel and free finite-rank module witness reports.
- Validation evidence:
  - `just test-spec-core-vertical-slice` passed: 9 tests passed.
- Broad `just test` remains non-diagnostic for this slice while parallel mypy-plugin
  work is active; the focused recipe is the slice acceptance command.

## Review Log

### Review 2026-05-18 (Fresh-context Spark review)

- Synthesis: the validation leaf is a narrow completion step. It adds the focused
  `just test-spec-core-vertical-slice` command and records evidence for the existing
  report tests without changing the spec-core or witness implementation surfaces.
- Gate 1 pass: the task introduces no new mathematical definitions; it validates the
  existing spec-core report and free finite-rank module witness machinery.
- Gate 2 pass: the card's acceptance criteria are supported by the focused just recipe
  and the 9 passing tests in `tests/category_specs/test_spec_core_reports.py` and
  `tests/category_specs/test_free_module_witnesses.py`.
- Gate 3 pass: `git show ddeb37e` changes only the task card, `justfile`, generated
  planning artifacts, and the handoff; no spec obligations, methods, or smoke
  assertions were deleted or weakened.
- Gate 4 pass: `just plan-validate` passed after the status transition, and the
  acceptance direction is forward from `in-progress` to `needs-agent-review`.
- Gate 5 pass: `just test-spec-core-vertical-slice` passed with 9 tests, covering the
  `GF(5)^3` cardinality report, `ZZ^2` countability report, and the missing
  deterministic-enumeration obligation.
- Gate 6 pass: the new recipe follows the repo `justfile` convention and keeps broad
  suite execution out of the slice evidence.
- Outcome: PASS; the validation leaf is accepted after direct integration on `main`.
