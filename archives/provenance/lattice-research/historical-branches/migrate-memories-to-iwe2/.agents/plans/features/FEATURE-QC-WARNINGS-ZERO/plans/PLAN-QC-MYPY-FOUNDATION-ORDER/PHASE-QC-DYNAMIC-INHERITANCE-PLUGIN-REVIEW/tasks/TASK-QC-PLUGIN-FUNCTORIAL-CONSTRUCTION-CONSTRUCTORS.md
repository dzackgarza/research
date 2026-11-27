---
id: TASK-QC-PLUGIN-FUNCTORIAL-CONSTRUCTION-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Teach plugin functorial construction constructors
status: unstarted
priority: high
description: 'Teach the plugin or global QC path Sage functorial construction public
  constructor behavior for Subobjects, Quotients, products, tensor products, and Hom
  categories.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Focused reproductions cover zero- or single-argument `FunctorialConstructionCategory` construction from the triage decision.
- The repair models Sage `__classcall__` public construction behavior or proves a source-side constructor signature is wrong.
- Constructor collector `no-redef` is not handled here except where it survives after `TASK-QC-STATIC-CONSTRUCTORS-COLLECTOR-NO-REDEF`.
- No local suppressions or constructor-surface weakening are introduced.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Teach Plugin Functorial Construction Constructors

## Summary

Resolve the functorial-construction constructor findings from the triage decision:
`HomCategoryOf(self.base_category())`, `Subobjects(category)`,
`CartesianProducts(category)`, `TensorProducts(category)`, and related public
constructor shapes that Sage routes through `FunctorialConstructionCategory`.

## Source Provenance

- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`, functorial
  construction plugin-gap entry.
- `SPEC-MAPPING-CAT` and `SPEC-MAPPING-HOMSETS`, category-level construction surfaces.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`, dynamic-inheritance plugin phase.

## Context

The decision classifies these as static-analysis misses around Sage construction
dispatch, not as an excuse to add local ignores. The task must build focused
reproductions and then repair the plugin/global QC model or identify real source
defects.

## Acceptance Criteria

- Focused reproductions cover each constructor shape or justify grouping them under
  one plugin rule.
- The repair preserves project category construction surfaces.
- No local suppressions, private helper aliases, or weaker constructor APIs are added.
- Post-repair validation covers the affected call sites named in the decision.

## Dependencies And Boundaries

Depends on the dynamic-inheritance review task. The pure `Constructors` class/method
`no-redef` issue belongs to `TASK-QC-STATIC-CONSTRUCTORS-COLLECTOR-NO-REDEF`.

## Complexity And Ownership

Complexity: 55. Several call sites share one Sage construction mechanism, and the fix
belongs at the plugin/global QC boundary rather than in local category code.

## Work Log

- Created 2026-05-14 to replace the missing plugin task named by the triage decision.
