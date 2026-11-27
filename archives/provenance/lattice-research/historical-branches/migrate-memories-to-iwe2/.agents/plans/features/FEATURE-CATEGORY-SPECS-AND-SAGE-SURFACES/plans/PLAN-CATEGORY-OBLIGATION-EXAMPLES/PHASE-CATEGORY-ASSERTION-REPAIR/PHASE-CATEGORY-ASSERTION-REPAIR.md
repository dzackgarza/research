---
id: PHASE-CATEGORY-ASSERTION-REPAIR
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-OBLIGATION-EXAMPLES]]'
dependsOn:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
title: Category assertion repair — G1/G3/G4/G5 fixes
status: complete
priority: critical
description: >-
  Apply the concrete fixes required by the 6-gate review of
  PLAN-CATEGORY-OBLIGATION-EXAMPLES: remove dead source links
  (G1), fix phase inventory mismatch (G3), narrow scope description (G4),
  and remove circular self-dependency from wrapup task (G5).
successCriteria:
- All G1, G3, G4, G5 review findings resolved.
- Plan body and child cards updated to match actual phase inventory.
- Circular self-dependency in wrapup task removed.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-OBLIGATION-EXAMPLES
---
# Category assertion repair

## Objective

Apply the 4 concrete fixes identified by the 6-gate review of
PLAN-CATEGORY-OBLIGATION-EXAMPLES: dead links (G1), phase inventory
(G3), scope description (G4), circular dependency (G5).

## Child Cards

- `PHASE-CATEGORY-ASSERTION-REPAIR/tasks/TASK-CATEGORY-OBLIGATION-PLAN-FIX-DEAD-LINKS.md`
- `PHASE-CATEGORY-ASSERTION-REPAIR/tasks/TASK-CATEGORY-OBLIGATION-PLAN-FIX-PHASE-INVENTORY.md`
- `PHASE-CATEGORY-ASSERTION-REPAIR/tasks/TASK-CATEGORY-OBLIGATION-PLAN-FIX-SCOPE.md`
- `PHASE-CATEGORY-ASSERTION-REPAIR/tasks/TASK-CATEGORY-OBLIGATION-PLAN-FIX-CIRCULAR-DEP.md`
