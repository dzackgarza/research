---
id: PHASE-QC-STUB-GENERATION
trackerStatus:
  type: phase
parents:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
dependsOn:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Stub generation and static surface material
status: unstarted
priority: high
description: 'Third mypy frontier for Sage/pytest stubs, .pyi files, TypeAlias surfaces,
  and generated static representations. This phase depends on dynamic-inheritance plugin
  review.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-QC-GENERATE-TYPE-STUBS]]'
- '[[TASK-QC-STATIC-CONSTRUCTORS-COLLECTOR-NO-REDEF]]'
successCriteria:
- Dynamic-inheritance plugin review is complete before stub-generation work starts.
- Stub-generation scope excludes plugin/base-injection defects.
- Generated or handwritten static surfaces are validated through the repo-approved QC path.
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
---
# Phase: Stub Generation and Static Surface Material

## Summary

This phase owns static surface material: Sage stubs, pytest stubs, `.pyi` files,
`TypeAlias` intermediaries, and generated representations of dynamic category
surfaces.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`: valid-type and missing-stub triage notes.
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: generated stubs are explicitly out of the
  plugin scope.
- User direction from 2026-05-13: stub-related mypy issues belong under a
  separate phase/task tree that depends on resolving basic plugin issues first.

## Acceptance Criteria

- Plugin review phase is complete.
- Stub-generation candidates are inventoried separately from plugin findings.
- Generated or handwritten stubs are validated without hiding QC findings.

## Dependencies And Boundaries

This phase depends on the dynamic-inheritance plugin review phase. It must not
be used as a workaround for unresolved plugin MRO/base-injection behavior.

## Work Log

- Created 2026-05-13 because no full stub-generation task card existed in the
  QC/plugin DAG.
