---
trackerStatus:
  type: plan
title: Sprint poset constructor smoke and deferred surface ownership pass for graph
  polytope algebra polynomial and Coxeter surfaces
---
# Sprint poset constructor smoke and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces
## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `plans/category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Sprint poset constructor smoke and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces from plans/category_specs/posets/docs/MAPPING.md`

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

