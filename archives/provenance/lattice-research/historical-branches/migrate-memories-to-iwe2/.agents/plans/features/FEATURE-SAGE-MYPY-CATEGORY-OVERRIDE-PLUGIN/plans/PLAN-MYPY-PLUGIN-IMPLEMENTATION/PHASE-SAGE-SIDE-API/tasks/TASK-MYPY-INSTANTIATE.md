---
id: TASK-MYPY-INSTANTIATE
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-PARSER]]'
title: Resolve configured category factories through Sage runtime instances
status: complete
priority: high
description: 'Resolve configured category factories through Sage runtime category instances
  for invariant-core projection. This replaces the obsolete parsed CategoryMethodContainer
  instantiation path.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- resolver/oracle obtains live Sage category instances from configured category
  fullnames
- singleton, functorial/nested, axiom, and parameterized representative categories
  appear in invariant-core projection tests
- failures are surfaced by resolver/oracle assertions or strict plugin diagnostics
- full plugin test suite passes through `just test -q`
complexity: 20
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Resolve Category Factories Through Sage Runtime Instances

## Summary

Validate the invariant-core category resolution path in `~/sage-mypy-plugin`.
The active implementation imports configured category factory fullnames, calls
Sage runtime construction, and records provider projections from the resulting
category instances.

## Context

The legacy parser fed module/category-path tuples into an instantiation helper.
The current resolver/oracle path instead treats configured fullnames and Sage
runtime category objects as the source of truth.

## Source Provenance

- `/home/dzack/sage-mypy-plugin/README.md`
- `/home/dzack/sage-mypy-plugin/.serena/plans/invariant-core-rewrite.md`
- `~/ai/quality-control/planning/override-sage-categories.md`: "Category Instantiation Rule"

## Acceptance Criteria

- Resolver/oracle projection tests cover singleton, nested/functorial, axiom, and
  parameterized category representatives.
- Manifest records enough source metadata for the resulting projection graph.
- Mypy plugin tests pass from manifest evidence without a legacy parser helper.

## Current Status

Needs agent review against the invariant-core resolver/oracle path. The current
plugin branch no longer exposes `instantiate_category_from_source_path`; plugin
commit `bd656d2` passes `just test -q` with `73 passed`.
