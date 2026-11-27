---
id: TASK-20260601-RECONSTRUCT-TENSOR-COMPONENT-CONSTRUCTOR-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Reconstruct tensor component constructor inventory from Sage tensor calculus
  source
status: unstarted
priority: high
description: Mine Sage tensor calculus constructor routes before repairing TensorAlgebraComponents
  collector names.
activityType: source-mining
uncertaintyState: ordinary-open
workstreamRole: implementation
claimStatus: source-backed
successCriteria:
- Sage tensor calculus source/docs are cited for each admitted tensor component constructor
  shape.
- SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS records constructorNameInventories for every
  exposed tensor component collector.
- Matrix/list/module-element routes are enumerated as named-only overloads or removed
  if not Sage-grounded.
- check-constructor-name-inventory no longer reports tensor component constructor
  collector failures.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Reconstruct tensor component constructor inventory from Sage tensor calculus source

## Summary

The constructor-name validator reports public methods on
`category_specs.tensor_algebra_components.TensorAlgebraComponents._Constructors`,
including `component_module`, `tensor`, `from_matrix`,
`from_module_element_matrix`, `from_multidimensional_list`, and `from_matrices`.
These names must be justified from Sage tensor calculus construction semantics before
they are admitted or renamed.

## Source Provenance

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS.md`
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- `category_specs/tensor_algebra_components/__init__.py`
- Sage tensor module, tensor field, free-module tensor, and algebra tensor component
  constructor docs/source as applicable.

## Context

Algebra construction delegates finite-dimensional multiplication data to tensor
component constructors.
That means tensor component constructor inventory is upstream of algebra
`from_multiplication_tensor` correctness.
Do not use generic matrix/list routes as placeholders unless Sage source establishes
the exact input shape and the mapping names the mathematical data being supplied.

## Acceptance Criteria

- [ ] Enumerate each Sage-backed tensor component construction route and its accepted
      input data.
- [ ] Decide which routes are Sage constructor names and which are project-owned
      named data-shape constructors.
- [ ] Add or correct `constructorNameInventories` in
      `SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS`.
- [ ] Align implementation names only after the mapping inventory is explicit.
- [ ] Re-run constructor-name QC and record remaining non-tensor failures separately.

## Dependencies And Boundaries

- Do not broaden into all tensor calculus API mapping; this card is only constructor
  inventory and collector alignment.
- Do not patch algebra constructors to bypass missing tensor constructor provenance.

## Work Log

- Created from constructor-name inventory QC output after the anti-polishing constructor
  source gate was added.
