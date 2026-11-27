---
id: TASK-20260601-RECONSTRUCT-CAT-CONSTRUCTOR-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Reconstruct Cat constructor inventory for EmptyCategory
status: unstarted
priority: high
description: Verify whether EmptyCategory is Sage-backed, project-owned, or mislocated
  before admitting it to the constructor inventory.
activityType: source-mining
uncertaintyState: ordinary-open
workstreamRole: implementation
claimStatus: unexamined
successCriteria:
- Sage category docs/source are checked for EmptyCategory construction semantics.
- SPEC-MAPPING-CAT records the source-grounded constructor inventory or explains the
  corrected non-constructor owner.
- The Cat constructor collector exposes no un-inventoried public method.
- check-constructor-name-inventory no longer reports Cat constructor collector failures.
complexity: 35
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Reconstruct Cat constructor inventory for EmptyCategory

## Summary

The constructor-name validator reports
`category_specs.cat.Cat.Constructors.EmptyCategory` with no mapping inventory.
Do not simply whitelist the name.
Determine from Sage source whether `EmptyCategory` is an existing Sage constructor
route, a legitimate project-owned category constructor, or a misplaced internal helper.

## Source Provenance

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md`
- `category_specs/cat/__init__.py`
- Sage category docs/source for category construction and empty categories.

## Context

Cat is a top-level mathematical category surface, so a constructor here affects
discoverability for the entire spec layer.
If `EmptyCategory` is project-owned rather than Sage-backed, the mapping must say so
explicitly.
If it is not a constructor at all, remove or relocate the surface instead of inventing
provenance.

## Acceptance Criteria

- [ ] Read Sage written docs and installed Sage source for empty category construction.
- [ ] Record whether `EmptyCategory` is Sage-backed, project-owned, or mislocated.
- [ ] Add `constructorNameInventories` to `SPEC-MAPPING-CAT` only for admitted
      constructor names.
- [ ] Repair `category_specs/cat/__init__.py` only after the mapping decision is
      explicit.
- [ ] Re-run constructor-name QC and record remaining failures outside Cat separately.

## Dependencies And Boundaries

- Do not broaden into category graph validation unless the `EmptyCategory` source
  route itself depends on a graph edge.
- Do not treat an implementation class name as mathematical constructor provenance.

## Work Log

- Created from constructor-name inventory QC output after the anti-polishing constructor
  source gate was added.
