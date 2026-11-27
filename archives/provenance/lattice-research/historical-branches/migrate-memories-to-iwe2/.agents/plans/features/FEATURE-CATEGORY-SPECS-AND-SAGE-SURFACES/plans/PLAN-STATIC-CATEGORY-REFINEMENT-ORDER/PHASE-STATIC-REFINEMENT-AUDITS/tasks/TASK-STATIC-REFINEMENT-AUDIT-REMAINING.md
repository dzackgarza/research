---
id: TASK-STATIC-REFINEMENT-AUDIT-REMAINING
trackerStatus:
  type: task
parents:
- '[[PHASE-STATIC-REFINEMENT-AUDITS]]'
dependsOn: []
title: Audit super_categories() returns in remaining subtrees
status: complete
priority: critical
description: Grep all super_categories() calls in algebras/ (11), posets/ (9), topological_spaces/
  (10), lattices/ (7), cat/ (4), homsets/ (3), tensor_algebra_components/ (1), forms/
  (1). Extract returned lists, cross-reference against the admitted-edges table, write
  findings into the plan body.
successCriteria:
- >-
  Every super_categories() return in all 8 subtrees is inventoried.
- >-
  Each hit classified as in table, missing, or exempt.
- >-
  Findings written as per-subtree inventory sections in the plan body.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
- PHASE-STATIC-REFINEMENT-AUDITS
---
# Audit super_categories() returns in remaining subtrees

Grep the 8 smaller subtrees (~46 files total) for `super_categories(`, extract
returned lists, cross-reference against the admitted-edges table.

Subtrees: algebras (11), posets (9), topological_spaces (10), lattices (7),
cat (4), homsets (3), tensor_algebra_components (1), forms (1).

Write per-subtree inventory sections into the plan body.
