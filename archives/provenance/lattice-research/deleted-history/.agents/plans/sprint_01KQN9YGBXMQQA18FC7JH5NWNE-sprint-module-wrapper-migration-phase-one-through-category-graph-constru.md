---
trackerStatus:
  type: plan
title: Sprint module wrapper migration phase one through category graph constructor
  routing method coverage and deletion gates
---
# Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates
## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates from plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

