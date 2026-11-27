---
id: PHASE-QC-DOWNSTREAM-TYPE-CLEANUP
trackerStatus:
  type: phase
parents:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
dependsOn:
- '[[PHASE-QC-STUB-GENERATION]]'
title: Downstream category type cleanup
status: unstarted
priority: high
description: 'Final mypy frontier for remaining category/type defects after basic hygiene,
  plugin review, and stub generation are complete.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-QC-DOWNSTREAM-TYPE-CLEANUP]]'
successCriteria:
- Earlier mypy phases are complete before downstream cleanup starts.
- Remaining incompatible signatures, constructor calls, attr-defined findings, and category-specific defects are classified from post-stub output.
- No earlier-phase failure is reclassified as downstream cleanup without evidence.
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
---
# Phase: Downstream Category Type Cleanup

## Summary

This final mypy phase owns remaining ordinary category/type defects only after
basic hygiene, dynamic-inheritance plugin review, and stub generation are
complete.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`: constructor, attribute, and miscellaneous mypy
  categories.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Acceptance Criteria

- Earlier phases are complete.
- Remaining errors are classified from post-stub validation output.
- Each downstream defect is fixed or split into an executable child task.

## Dependencies And Boundaries

This phase depends on stub generation. It cannot be used to start work on
incompatible signatures, constructor calls, or category-specific typing while
basic hygiene, plugin, or stub frontiers remain incomplete.

## Work Log

- Created 2026-05-13 as the last mypy cleanup frontier.
