---
id: TASK-MYPY-DIRECT-BASES
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-INSTANTIATE]]'
title: Project Sage runtime named-class MROs into manifest provider MROs
status: complete
priority: high
description: 'Implement the invariant-core projection: trace Sage runtime named classes,
  record runtime bases/MROs, project them back to provider classes, and expose dependency
  modules from manifest source-module records.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- oracle projections make provider MROs equal Sage runtime named-class MROs projected
  back to provider classes
- manifest records runtime bases, runtime MROs, provider bases, provider MROs, and
  unprojected runtime classes
- plugin dependency hooks use manifest source modules for ancestor dependencies
- full plugin test suite passes through `just test -q`
complexity: 30
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Project Runtime Named-Class MROs Into Provider MROs

## Summary

Validate the core invariant projection in `~/sage-mypy-plugin`: Sage runtime
named-class MROs are traced by the oracle/resolver, recorded in the manifest, and
projected into mypy TypeInfo MROs by the plugin.

## Context

The legacy helper returned direct base fullnames from an `introspection.py` call.
The active invariant-core architecture records both direct bases and full runtime
MRO evidence in manifest projections, then lets the mypy plugin mutate TypeInfo
MROs from the manifest.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Sage-Side Helper: Direct Dynamic-Base Projection" (full algorithm),
  "Debug Oracle"
- `/home/dzack/sage-mypy-plugin/.serena/plans/invariant-core-rewrite.md`

## Acceptance Criteria

- Provider projections record direct runtime bases and provider bases.
- Provider projections record runtime MRO and provider MRO.
- Plugin tests assert TypeInfo MRO equals manifest provider MRO plus
  `builtins.object`.
- Dependency-module tests use manifest source modules, including nested axiom
  providers.

## Current Status

Needs agent review against the invariant-core projection path. Plugin commit
`bd656d2` passes `just test -q` with `73 passed`.
