---
id: PHASE-SMOKE-PLAN-REMEDIATION
trackerStatus:
  type: phase
parents:
- '[[PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION]]'
dependsOn:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
title: Smoke plan remediation — G1/G3/G4/G5 fixes
status: complete
priority: critical
description: >-
  Apply the concrete fixes required by the 6-gate review of
  PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION: remove dead source links
  (G1), fix phase inventory mismatch (G3), narrow scope description (G4),
  and remove circular self-dependency from wrapup task (G5).
successCriteria:
- All G1, G3, G4, G5 review findings resolved.
- Plan body and child cards updated to match actual phase inventory.
- Circular self-dependency in wrapup task removed.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
---
# Smoke plan remediation

## Objective

Apply the 4 concrete fixes identified by the 6-gate review of
PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION: dead links (G1), phase inventory
(G3), scope description (G4), circular dependency (G5).

## Child Cards

- `PHASE-SMOKE-PLAN-REMEDIATION/tasks/TASK-SMOKE-PLAN-FIX-DEAD-LINKS.md`
- `PHASE-SMOKE-PLAN-REMEDIATION/tasks/TASK-SMOKE-PLAN-FIX-PHASE-INVENTORY.md`
- `PHASE-SMOKE-PLAN-REMEDIATION/tasks/TASK-SMOKE-PLAN-FIX-SCOPE.md`
- `PHASE-SMOKE-PLAN-REMEDIATION/tasks/TASK-SMOKE-PLAN-FIX-CIRCULAR-DEP.md`
