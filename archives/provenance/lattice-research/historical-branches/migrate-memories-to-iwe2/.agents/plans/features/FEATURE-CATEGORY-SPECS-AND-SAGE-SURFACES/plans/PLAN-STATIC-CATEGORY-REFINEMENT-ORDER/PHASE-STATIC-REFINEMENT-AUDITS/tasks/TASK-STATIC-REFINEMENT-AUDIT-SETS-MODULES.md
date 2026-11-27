---
id: TASK-STATIC-REFINEMENT-AUDIT-SETS-MODULES
trackerStatus:
  type: task
parents:
- '[[PHASE-STATIC-REFINEMENT-AUDITS]]'
dependsOn: []
title: Audit super_categories() returns in category_specs/sets/ and modules/
status: complete
priority: critical
description: Grep all super_categories() calls in category_specs/sets/ (25 files)
  and category_specs/modules/ (20 files), extract returned lists, cross-reference
  against the admitted-edges table, write findings into the plan body.
successCriteria:
- >-
  Every super_categories() return in sets/ and modules/ is inventoried.
- >-
  Each hit classified as in table, missing, or exempt.
- >-
  PartitionedSets contradiction flagged with exact file:line evidence.
- >-
  Findings written as '## Sets super_categories() inventory' and
  '## Modules super_categories() inventory' in the plan body.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
- PHASE-STATIC-REFINEMENT-AUDITS
---
# Audit super_categories() returns in sets/ and modules/

Grep `category_specs/sets/` (25 files) and `category_specs/modules/` (20 files)
for `super_categories(`, extract returned lists, cross-reference against the
admitted-edges table.

**Special attention:** The PartitionedSets row in the table claims
`Sets().Countable()` and `Sets().Subobjects()` but the 6-gate review found
`PartitionedSetsCategory` returns `[]`. Verify and flag.

Write two sections into the plan body:
- `## Sets super_categories() inventory`
- `## Modules super_categories() inventory`
