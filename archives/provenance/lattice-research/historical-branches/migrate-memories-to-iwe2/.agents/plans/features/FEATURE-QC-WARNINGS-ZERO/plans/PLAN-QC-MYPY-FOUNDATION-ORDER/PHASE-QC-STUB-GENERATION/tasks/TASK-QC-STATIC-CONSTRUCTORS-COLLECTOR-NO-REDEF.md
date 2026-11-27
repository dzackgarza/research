---
id: TASK-QC-STATIC-CONSTRUCTORS-COLLECTOR-NO-REDEF
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-STUB-GENERATION]]'
dependsOn:
- '[[TASK-QC-GENERATE-TYPE-STUBS]]'
title: Model Constructors collector static no-redef surface
status: unstarted
priority: high
description: 'Resolve the category-spec `Constructors` class/method static no-redef
  errors without renaming away the style-required nested constructor collector.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- The nested `Constructors` class and public `Constructors()` method remain available as required by category-spec style.
- The chosen static-surface fix uses stubs, generated static surfaces, plugin support, or global QC configuration with justification.
- No local type-ignore comment, private-class/public-alias workaround, or constructor-surface weakening is introduced.
- The eight affected category surfaces from the triage decision are covered by focused validation.
complexity: 45
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-STUB-GENERATION
---
# Task: Model Constructors Collector Static No-Redef Surface

## Summary

Resolve the `Constructors` class/method `no-redef` findings recorded in
`DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP` without applying the
superseded private-class rename. The category-spec style requires the explicit nested
`Constructors` class as the constructor collector declaration.

## Source Provenance

- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`, compliance correction.
- `category-spec-style/references/style.md`, constructor collector rules.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`, stub-generation phase boundaries.

## Context

The affected files define a nested `Constructors` class and a cached public
`Constructors()` method. Mypy reports `no-redef`, but renaming the class only to satisfy
static analysis would violate the constructor collector style rule and risks weakening
the public category surface.

## Acceptance Criteria

- Preserve the constructor collector semantics and public navigation surface.
- Reproduce the static error on at least one affected file before implementing a fix.
- Choose a global static-surface remedy rather than a local suppression.
- Validate the remedy against the affected category surfaces named in the decision.

## Dependencies And Boundaries

Depends on the general stub-generation task because this is a static-surface problem.
It must not be used to hide unresolved plugin MRO/base-injection failures.

## Complexity And Ownership

Complexity: 45. The work spans several category roots but has one repeated static
shape and a clear no-suppression boundary.

## Work Log

- Created 2026-05-14 after the triage decision was corrected to preserve nested
  constructor collectors.
