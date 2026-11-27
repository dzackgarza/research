---
id: TASK-SMOKE-PLAN-FIX-SCOPE
trackerStatus:
  type: task
parents:
- '[[PHASE-SMOKE-PLAN-REMEDIATION]]'
dependsOn: []
title: Narrow plan description to match actual phase inventory
status: complete
priority: high
description: 'Resolve G4 scope gap: the plan description promises "import hygiene,
  wrapper, type, and anti-slop compliance" but no phases exist for these areas.  Narrow
  the description to reflect only what is actually planned.'
successCriteria:
- Plan description narrowed from "smoke-frontier, audit, variadic-signature, import
  hygiene, wrapper, type, and anti-slop compliance" to "smoke-audit and object-shape
  probe governance."
- 'Body adds a note: import hygiene is handled by ruff/isort enforcement; wrapper/type
  compliance lives under PLAN-CATEGORY-FOUNDATION-KERNEL; anti-slop patterns are caught
  by style compliance gates.'
- Objective sentence updated to match narrowed scope.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
- PHASE-SMOKE-PLAN-REMEDIATION
---
# Narrow plan description to match actual phase inventory

The plan's description promises seven areas of compliance work but only one
(duck-type object-shape probe audit) has an active phase. The variadic audit lives
under a sibling plan. Import hygiene, wrapper, type, and anti-slop are not tracked
as phases here.

Edit the plan body: narrow the description to "smoke-audit and object-shape probe
governance." Note where the other areas are handled (ruff/isort for imports,
PLAN-CATEGORY-FOUNDATION-KERNEL for wrapper/type work, style compliance gates for
anti-slop). Update the Objective sentence accordingly.
