---
id: TASK-MYPY-DEPS-DIAGNOSTICS
trackerStatus:
  type: task
parents:
- '[[PHASE-MYPY-SIDE-HARNESS]]'
dependsOn:
- '[[TASK-MYPY-PLUGIN-CLASS]]'
title: Implement dependency tracking and diagnostic error codes
status: complete
priority: high
description: 'Implement get_additional_deps via module_method_container_dependencies. Register
  four Sage-specific mypy error codes for failure diagnostics.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- get_additional_deps returns ancestor module names for incremental mode
- sage-category-unresolved diagnostic fires when category can't be instantiated
- sage-category-parameterized fires when parameterized and unconfigured
- sage-category-base-unmapped fires when dynamic base has no source container
- sage-category-typeinfo-missing fires when source fullname not in mypy
complexity: 15
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-MYPY-SIDE-HARNESS
---
# Task: Implement Dependencies and Diagnostics

## Summary

Wire `get_additional_deps` so mypy's incremental mode correctly invalidates
dependent files. Register diagnostic error codes for the four failure modes.

## Context

`get_additional_deps(file)` must return the modules containing ancestor method
containers. This ensures changing `A.ParentMethods.f` invalidates checks of
`B.ParentMethods.@override f`.

Four diagnostic error codes per the spec:
- `sage-category-unresolved`
- `sage-category-parameterized`
- `sage-category-base-unmapped`
- `sage-category-typeinfo-missing`

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Dependency Handling", "Diagnostic Policy"

## Acceptance Criteria

- `get_additional_deps` returns correct module list for a file containing Sage method containers
- Error codes registered and documented
- In strict mode, unresolved cases are hard errors
- In non-strict mode, unresolved cases are skipped with optional note

## Current Status

Ready for review. `get_additional_deps()` calls `module_method_container_dependencies()`, incremental reactivity is covered by a real in-place ancestor-change test, `report_config_data()` includes plugin version, Sage version, strict mode, and configured representatives, and all four Sage-specific diagnostic codes are emitted under strict tests.
