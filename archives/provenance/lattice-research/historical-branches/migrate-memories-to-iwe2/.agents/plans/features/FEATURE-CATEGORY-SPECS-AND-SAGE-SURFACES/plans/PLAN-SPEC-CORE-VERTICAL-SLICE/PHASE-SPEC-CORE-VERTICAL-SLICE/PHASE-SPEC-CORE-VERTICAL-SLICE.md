---
id: PHASE-SPEC-CORE-VERTICAL-SLICE
trackerStatus:
  type: phase
parents:
- '[[PLAN-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn: []
title: Spec core vertical slice
status: complete
priority: critical
phaseKind: milestone
description: Build and validate the declarative spec-core and construction-witness
  slice for finite/countable cartesian products realized as free finite-rank modules.
successCriteria:
- The declarative spec/report kernel exists before module-specific witness logic.
- Module witness logic consumes the spec/report kernel and records finite and countable
  cartesian-product provenance.
- Focused validation proves the `GF(5)^3` finite case and the `ZZ^2` countable case.
tasks:
- '[[TASK-SPEC-CORE-REGISTRY-REPORT-KERNEL]]'
- '[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]'
- '[[TASK-VERTICAL-SLICE-SPEC-REPORT-CATEGORY-OBLIGATIONS]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SPEC-CORE-VERTICAL-SLICE
---
# Spec core vertical slice

## Summary

This phase turns the approved pivot into three executable leaves: a typed spec/report
kernel, module construction witnesses, and focused validation. It is deliberately not a
new broad category-expansion phase.

## Source Provenance

- `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`
- `/home/dzack/vault/projects/research/Spec Enforcement in Sage.md`
- `[[SPEC-MAPPING-CAT]]`
- `[[SPEC-MAPPING-SETS]]`
- `[[SPEC-MAPPING-MODULES]]`
- `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`

## Acceptance Criteria

- [x] The three child tasks are executable without choosing new feature scope.
- [x] The child task dependency order is linear and blocks broad validation until the
  typed report kernel and witness layer exist.
- [x] Every child task rejects broad category expansion, full-suite QC cleanup, or local
  obligation duplication as success evidence.

## Dependencies And Boundaries

Task order is part of the phase contract. Do not run the validation task before the
kernel and module witness tasks have produced inspectable artifacts.

## Work Log

- Created with the pivot plan to keep implementation work atomic and reviewable.
- Activated for the spec-core registry/report kernel implementation leaf.
- Completed after all three child tasks reached `complete` and the focused
  `just test-spec-core-vertical-slice` validation passed.
