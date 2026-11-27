---
id: TASK-POSET-DEFERRED-OWNER-ASSIGNMENT
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
dependsOn: []
title: Assign per-method owners for poset deferred non-core surfaces
status: complete
priority: medium
description: Complete the source-mining contract from the deferred poset surfaces
  spec by assigning each deferred method to a specific category owner with hypotheses
  and codomain.
successCriteria:
- Each of the 5 deferred surface groups (graph, polytope, order-complex, algebra/polynomial,
  Coxeter) has per-method owner assignments recorded in the parent spec
- Per-method rows state literal surface, minimal owner, hypotheses, and codomain
- No method remains in summary-grouping-only form
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS
---
# Assign per-method owners for poset deferred non-core surfaces

## Summary

The deferred poset surfaces spec (SPEC-01KQN9YGC9K980Y33NVZSTP4Z7) identified 5 groups
of deferred non-core surfaces but did not complete per-method owner assignment. This
task completes that contract.

## Source

- `SPEC-MAPPING-POSETS.md` lines 325-355: Deferred Non-Core Surfaces table
- `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7`: parent spec with source-mining contract

## Work Log

- 2026-05-07: Created from G5 review finding on SPEC-POSET-DEFERRED.
