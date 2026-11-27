---
id: TASK-QC-PLUGIN-CLASSCALL-PRIVATE-KWARGS
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Teach plugin classcall_private keyword signatures
status: unstarted
priority: high
description: 'Teach the plugin or global QC path that Sage `__classcall_private__`
  parameters are public constructor keyword arguments where Sage exposes them.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- A focused reproduction covers `Modules(base_ring, dispatch=False)` from lattices/forms.
- The repair models `__classcall_private__` keyword propagation or proves the source constructor call is wrong.
- No local type-ignore comment, wrapper bypass, or repo-local QC override is introduced.
- Focused validation shows the targeted keyword findings are resolved or correctly rerouted.
complexity: 45
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Teach Plugin Classcall Private Keyword Signatures

## Summary

Resolve the `dispatch=False` constructor findings from the triage decision. Sage
declares public constructor keyword behavior through `__classcall_private__`; mypy does
not currently propagate those keyword parameters to the callable class surface.

## Source Provenance

- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`, classcall-private
  keyword plugin-gap entry.
- `SPEC-MAPPING-LATTICES`, which records `Modules(R, dispatch=False)` as the canonical
  undecorated module-category construction.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`, dynamic-inheritance plugin phase.

## Context

The affected call sites are `lattices/__init__.py:223` and `forms/__init__.py:160`.
The task must resolve the mismatch through plugin/global QC support or prove the calls
are source defects.

## Acceptance Criteria

- Reproduce the keyword mismatch with a focused mypy command.
- Implement or specify the plugin/global QC behavior for `__classcall_private__`
  keyword propagation.
- Do not add local suppressions or wrapper bypasses.
- Validate the targeted call sites after repair.

## Dependencies And Boundaries

Depends on the dynamic-inheritance review task. This does not own ordinary overload
cleanup or generated stubs.

## Complexity And Ownership

Complexity: 45. This is a narrow constructor-signature plugin repair with two known
repo call sites and one Sage mechanism.

## Work Log

- Created 2026-05-14 to replace the missing plugin task named by the triage decision.
