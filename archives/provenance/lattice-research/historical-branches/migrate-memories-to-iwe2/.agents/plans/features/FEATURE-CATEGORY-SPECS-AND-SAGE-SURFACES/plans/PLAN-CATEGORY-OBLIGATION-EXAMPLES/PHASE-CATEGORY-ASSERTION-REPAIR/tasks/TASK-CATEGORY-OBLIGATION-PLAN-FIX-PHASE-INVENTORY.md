---
id: TASK-CATEGORY-OBLIGATION-PLAN-FIX-PHASE-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-ASSERTION-REPAIR]]'
dependsOn: []
title: Fix phase inventory mismatch in category-obligation example plan
status: complete
priority: high
description: 'Resolve G3 phase inventory failure: PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
  is listed as a subplan in the body but lives under a sibling plan, not this one.'
successCriteria:
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT removed from the Subplans section of the
  plan body.
- 'A cross-reference note added: the variadic audit is owned by PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION.'
- 'The Subplans section now matches what this plan actually owns: PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
  only.'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-OBLIGATION-EXAMPLES
- PHASE-CATEGORY-ASSERTION-REPAIR
---
# Fix phase inventory mismatch

The plan body's Subplans section lists `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`
as a subplan, but that phase lives under `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION`,
a sibling plan. The frontmatter `phases` array correctly lists only
PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT.

Edit the body: remove the variadic phase from Subplans. Add a note that variadic
signature work is tracked under the sibling plan. The Subplans section should
list only what this plan directly owns.
