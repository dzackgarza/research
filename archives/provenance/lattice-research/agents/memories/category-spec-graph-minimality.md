---
title: Category Spec Graph Minimality — Immediate Parents Only
date: 2026-05-27
status: active
---
# Rule: `super_categories()` Must List Immediate Mathematical Parents Only

## The principle

A category's `super_categories()` should return only its **immediate** mathematical
parents. It should not list derived ancestors, consequence closures, or compensatory
direct attachments to categories that should be reachable through the graph.

The graph authority is Sage itself. Do not reconstruct a shadow category graph with
AST parsing, string matching, source maps, or sampled edge queries. Sage computes the
runtime category graph and the corresponding dynamic inheritance order; QC must call
Sage's graph machinery directly.

The mandatory validator model is:

- build the project category objects inside Sage;
- call `category.category_graph()` and require Sage to produce a loop-free directed
  graph;
- call `category._test_category_graph()` and require Sage's `_all_super_categories`
  order to match `parent_class.mro()` / `element_class.mro()`;
- print Sage's graph/MRO diagnostics loudly when either check fails.

If Sage reports a graph loop, an impossible MRO, or a mismatch between
`_all_super_categories` and the generated classes, that is a category-spec defect. Do
not replace the Sage check with a local graph parser or a heuristic validator.

## What violates minimality

- Listing `_Fields()` directly when the category is already under `_NumberFields` or
  `_GlobalFields`, and those categories themselves refine `_Fields`.
- Listing multiple direct ancestors that form a chain (e.g., `_QQ` listing `_Fields`,
  `_NumberFields`, `_GlobalFields` when the intended graph is
  `NumberFields <= GlobalFields <= Fields`).
- Listing theorem-level consequences as parents (e.g., `FiniteSets` listing `Countable`
  when finite-implies-countable is a derived property, not a direct parent).
- Including `SageXxx()` categories inside the local spec tree.
  Root entry points (e.g., `Rings`) may legitimately bridge to Sage root categories.
  Internal subcategories should inherit through local parents.

## The test

First run Sage's whole-graph checks for the project category objects. Then, for any
category with more than one project-local supercategory, classify each parent:

- **Valid root Sage bridge**: root entry category attaches to Sage root category.
- **Valid local immediate parent**: ordinary internal spec inheritance.
- **True mixed-structure**: category genuinely combines independent structures.
- **Redundant consequence closure**: lists derived parents that should be inferred.
- **Missing edge**: a required local parent is absent, causing compensatory direct
  attachments.
- **Wrong/misnamed edge**: mathematical inclusion is incorrect (e.g., `QuotientFields`
  for fraction fields/localizations).

## The fix

If a category lists redundant ancestors, the fix is usually in the graph, not in the
category. Add the missing edge to the intermediate category, then remove the redundant
direct attachment.
