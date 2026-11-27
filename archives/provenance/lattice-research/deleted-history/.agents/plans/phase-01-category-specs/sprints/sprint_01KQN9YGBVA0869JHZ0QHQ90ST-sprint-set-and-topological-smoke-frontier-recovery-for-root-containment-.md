---
trackerStatus:
  type: plan
title: Sprint set and topological smoke frontier recovery for root containment rich comparison Primes iteration RealSet ambient methods and topological axiom warning
status: approved
planId: SPR-SETS-TOPO-01KQN9
planType: sprint-plan
priority: high
parentPlan: PLN-SAGE-000
tags:
- category-specs
- plan
- sprint
- smoke
- sets
- realset
- topology
- primes
- theme-plan-control
---

# Sprint set and topological smoke frontier recovery for root containment rich comparison Primes iteration RealSet ambient methods and topological axiom warning

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

The deleted Sets triage recorded the mapped enumeration smoke surface and current
failures for containment, rich comparison, Primes iteration, RealSet element
construction, and topological axiom resolution.

## Source Provenance

- `category_specs/sets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/sets/docs/TRIAGE.md`.
- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Sprint set and topological smoke frontier recovery for root containment rich comparison Primes iteration RealSet ambient methods and topological axiom warning from category_specs/sets/docs/TRIAGE.md and category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- sets/smoketest.sage uses indexed access, rank, iteration, cardinality, and Python conversion protocols rather than Sage first/next/unrank/list/tuple helpers.
- ZZ in Sets() currently fails at the root containment statement.
- Most refined set constructors expose missing __richcmp__; Primes() exposes missing __iter__.
- RealSet interval input exposes missing _element_constructor_.
- SetPartitions(s) maps to Sets().Partitioned(), while SetPartitions() remains countable-only because it lacks a fixed powerset ambient.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Run just smoke-file sets/smoketest.sage after set constructor or comparison changes.
- [ ] Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback helper names.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

