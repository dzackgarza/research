---
trackerStatus:
  type: plan
title: Sprint Cat category-object surface uniformization and constructor aggregation
  cleanup
---
# Sprint Cat category-object surface uniformization and constructor aggregation cleanup
## Summary

The deleted Cat triage recorded structural Cat smoke scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- `plans/category_specs/cat/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md`.
- `plans/category_specs/AGENTS.md`
- Original migrated line: `Sprint Cat category-object surface uniformization and constructor aggregation cleanup from plans/category_specs/cat/docs/TRIAGE.md and plans/category_specs/AGENTS.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat smoke is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change.
- [ ] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

