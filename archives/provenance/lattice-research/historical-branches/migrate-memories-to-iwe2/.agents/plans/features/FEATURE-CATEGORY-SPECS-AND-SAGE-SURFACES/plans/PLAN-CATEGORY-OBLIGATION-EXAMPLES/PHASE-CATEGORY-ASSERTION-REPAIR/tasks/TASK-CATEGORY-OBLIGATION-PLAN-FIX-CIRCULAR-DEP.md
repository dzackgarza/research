---
id: TASK-CATEGORY-OBLIGATION-PLAN-FIX-CIRCULAR-DEP
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-ASSERTION-REPAIR]]'
dependsOn: []
title: Remove circular self-dependency from wrapup task
status: complete
priority: medium
description: 'Fix G5 inherited circular dependency: TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
  lists itself in its own dependsOn array.'
successCriteria:
- TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT no longer lists itself in its
  dependsOn array.
- Wrapup task dependsOn now correctly lists only the sibling work tasks in its phase.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-OBLIGATION-EXAMPLES
- PHASE-CATEGORY-ASSERTION-REPAIR
---
# Remove circular self-dependency from wrapup task

The 6-gate review G5 found that the wrapup task for the duck-type probe audit phase
lists itself in its own `dependsOn` array. This is a mechanical bug.

Edit `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT/tasks/TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT.md`:
remove the self-reference from the `dependsOn` frontmatter array.
