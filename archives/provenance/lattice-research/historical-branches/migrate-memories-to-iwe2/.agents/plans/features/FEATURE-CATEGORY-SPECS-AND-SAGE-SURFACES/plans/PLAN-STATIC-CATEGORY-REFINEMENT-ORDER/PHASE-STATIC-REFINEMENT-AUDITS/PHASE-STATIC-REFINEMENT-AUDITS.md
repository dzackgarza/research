---
id: PHASE-STATIC-REFINEMENT-AUDITS
trackerStatus:
  type: phase
parents:
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
dependsOn: []
title: Static refinement audits — super_categories() inventory and plan hygiene
status: complete
priority: critical
description: >-
  Audit all super_categories() returns across category_specs/ for
  cross-reference against the admitted-edges table, fill the table with
  source citations, and apply plan-hygiene fixes from the 6-gate review.
successCriteria:
- All super_categories() returns in category_specs/rings/, sets/, modules/,
  algebras/, posets/, topological_spaces/, lattices/, cat/, homsets/,
  tensor_algebra_components/, and forms/ are inventoried.
- Admitted-edges table expanded with source citations.
- Plan-hygiene issues (dead refs, dedup criteria, scope, soft dep) resolved.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
---
# Static refinement audits

## Objective

Audit all super_categories() returns in category_specs/ against the
admitted-edges table, fill in missing edges with source citations, resolve
the PartitionedSets contradiction, and apply plan-hygiene fixes from the
6-gate review.

## Child Cards

- `PHASE-STATIC-REFINEMENT-AUDITS/tasks/TASK-STATIC-REFINEMENT-AUDIT-RINGS.md`
- `PHASE-STATIC-REFINEMENT-AUDITS/tasks/TASK-STATIC-REFINEMENT-AUDIT-SETS-MODULES.md`
- `PHASE-STATIC-REFINEMENT-AUDITS/tasks/TASK-STATIC-REFINEMENT-AUDIT-REMAINING.md`
- `PHASE-STATIC-REFINEMENT-AUDITS/tasks/TASK-STATIC-REFINEMENT-FILL-TABLE.md`
- `PHASE-STATIC-REFINEMENT-AUDITS/tasks/TASK-STATIC-REFINEMENT-FIX-PLAN-HYGIENE.md`
