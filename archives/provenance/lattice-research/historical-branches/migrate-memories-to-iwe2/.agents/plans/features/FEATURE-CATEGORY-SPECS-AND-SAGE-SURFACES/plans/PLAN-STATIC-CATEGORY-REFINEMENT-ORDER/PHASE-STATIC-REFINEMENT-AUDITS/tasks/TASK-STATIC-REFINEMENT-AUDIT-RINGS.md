---
id: TASK-STATIC-REFINEMENT-AUDIT-RINGS
trackerStatus:
  type: task
parents:
- '[[PHASE-STATIC-REFINEMENT-AUDITS]]'
dependsOn: []
title: Audit super_categories() returns in category_specs/rings/
status: complete
priority: critical
description: Grep all super_categories() calls in category_specs/rings/, extract each
  returned list, cross-reference against the admitted-edges table in the plan, write
  findings into the plan body.
successCriteria:
- >-
  Every super_categories() return in category_specs/rings/ is inventoried.
- >-
  Each hit is classified as in table, missing from table, or exempt.
- >-
  Findings are written as '## Rings super_categories() inventory' in the plan body.
- >-
  Contradictions between table and code are flagged with exact file:line evidence.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
- PHASE-STATIC-REFINEMENT-AUDITS
---
# Audit super_categories() returns in rings

Grep `category_specs/rings/` for `super_categories(`, extract each returned list,
and cross-reference against the admitted-edges table in PLAN-STATIC-CATEGORY-REFINEMENT-ORDER.

65 files (62 in subcategories/, 1 in __init__.py). Mechanical grep — no need to
read every file body, just the super_categories() return lines.

Write a `## Rings super_categories() inventory` section into the plan with a table:
file path, line, returned supercategories, classification (in-table/missing/exempt).
