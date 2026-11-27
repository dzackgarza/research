---
id: TASK-QC-PLUGIN-METHOD-CONTAINER-SELF-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Teach plugin method-container self surfaces
status: unstarted
priority: critical
description: 'Repair method-container self typing and category-surface covariance
  findings without local mypy suppressions.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Focused reproductions cover `_base_category_class_and_axiom` covariance, `return self` parent-method narrowing, `SubcategoryMethods.__contains__`, same-container parent methods, element-method alias surfaces such as `RingElement.is_zero()`, and finite/countable method-container narrowing such as iterating a subobject's finite ambient set.
- The plugin or global QC path resolves true dynamic method-container false positives without local suppressions.
- Findings that prove to be real source defects are routed to source repair rather than hidden.
- Validation is run through the approved repo path or a documented focused equivalent.
complexity: 60
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Teach Plugin Method-Container Self Surfaces

## Summary

Repair the dynamic method-container failures that the triage decision originally tried
to suppress: covariant `_base_category_class_and_axiom` refinement, `return self`
inside `ParentMethods`, containment on `SubcategoryMethods`, same-container parent
methods, element-method alias surfaces such as `RingElement.is_zero()`, and
finite/countable category-graph narrowing such as subobject cardinality iterating a
proven finite ambient set.

## Source Provenance

- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`, plugin-gap section.
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`, dynamic-inheritance plugin phase.

## Context

These findings involve Sage category method containers whose runtime `self` is the
actual parent/category object, not merely the nested method class that mypy sees. The
resolution must improve plugin/global QC behavior or prove a source defect. Local
`# type: ignore` comments are forbidden.

## Acceptance Criteria

- Build focused reproductions for each grouped finding before implementation.
- Repair the plugin/global QC model or route real source defects to tracked source
  repair.
- Do not broaden source signatures to `Any` and do not add local suppressions.
- Record validation evidence in the task before moving it to review.

## Dependencies And Boundaries

Depends on the dynamic-inheritance review task. This does not own generated stubs,
constructor collector `no-redef`, or ordinary downstream type cleanup.

## Complexity And Ownership

Complexity: 60. The grouped failures share one method-container self-typing cause but
touch several category surfaces and require plugin-level validation.

## Work Log

- Created 2026-05-14 to replace the superseded local-suppression route.
