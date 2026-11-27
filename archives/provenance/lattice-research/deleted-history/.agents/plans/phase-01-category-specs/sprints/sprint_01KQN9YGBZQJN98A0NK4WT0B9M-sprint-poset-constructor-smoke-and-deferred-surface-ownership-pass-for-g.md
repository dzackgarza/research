---
trackerStatus:
  type: plan
title: Sprint poset constructor smoke and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces
status: approved
planId: SPR-POSETS-PART-01KQN9
planType: sprint-plan
priority: high
parentPlan: PLN-SAGE-000
tags:
- category-specs
- plan
- sprint
- smoke
- constructors
- sets
- algebras
- posets
- theme-plan-control
---

# Sprint poset constructor smoke and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Sprint poset constructor smoke and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces from category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [ ] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

