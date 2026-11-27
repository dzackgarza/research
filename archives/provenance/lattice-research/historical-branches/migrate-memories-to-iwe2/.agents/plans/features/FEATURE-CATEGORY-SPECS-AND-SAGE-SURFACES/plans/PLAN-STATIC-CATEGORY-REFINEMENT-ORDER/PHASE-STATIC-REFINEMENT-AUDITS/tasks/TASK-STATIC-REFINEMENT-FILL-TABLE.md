---
id: TASK-STATIC-REFINEMENT-FILL-TABLE
trackerStatus:
  type: task
parents:
- '[[PHASE-STATIC-REFINEMENT-AUDITS]]'
dependsOn:
- '[[TASK-STATIC-REFINEMENT-AUDIT-RINGS]]'
- '[[TASK-STATIC-REFINEMENT-AUDIT-SETS-MODULES]]'
- '[[TASK-STATIC-REFINEMENT-AUDIT-REMAINING]]'
title: Fill admitted-edges table from audit results and add source citations
status: complete
priority: critical
description: Using the 3 audit inventory sections now in the plan body, add every
  undocumented super_categories() edge to the admitted-edges table, add source citations
  (MAPPING.md or Sage source) to every row, resolve the PartitionedSets contradiction,
  and remove or decision-card unsettled edges.
successCriteria:
- Every documented edge has a traceable source citation.
- PartitionedSets contradiction resolved (fix code or fix table, with justification).
- Unsettled edges removed or linked to decision cards.
- No prose-only justifications remain ("Free modules are modules" without a file path).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
- PHASE-STATIC-REFINEMENT-AUDITS
---
# Fill admitted-edges table from audit results

The 3 audit tasks have written inventory sections into the plan body. This task
reads those sections and brings the admitted-edges table into agreement.

For each undocumented edge: add a row with subcategory, supercategories, and a
source citation. For the PartitionedSets contradiction: inspect
`category_specs/sets/subcategories/partitioned.py` and fix either the code or
the table. Remove unsettled edges or link to decision cards.
