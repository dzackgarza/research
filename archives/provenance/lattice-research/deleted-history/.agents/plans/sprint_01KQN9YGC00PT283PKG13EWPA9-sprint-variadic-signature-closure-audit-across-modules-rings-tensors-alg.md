---
trackerStatus:
  type: plan
title: Sprint variadic signature closure audit across modules rings tensors algebras
  lattices posets sets and real-set constructors
---
# Sprint variadic signature closure audit across modules rings tensors algebras lattices posets sets and real-set constructors
## Summary

The deleted variadic inventory records the scoping pass for public surfaces that had
collapsed Sage casework or raw coordinate interop into broad signatures.

## Source Provenance

- `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Sprint variadic signature closure audit across modules rings tensors algebras lattices posets sets and real-set constructors from plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`

## Context

- Module constructors and quotient inputs were split and mapped in modules docs/code.
- Ring constructors, p-adic precision tuples, series factories, matrix element construction, and number-field optional arguments were split and mapped in rings docs/code.
- Tensor component catch-all data was removed from public surface in favor of named constructors.
- Algebra subalgebra and ideal option bags were split into named methods.
- Lattice short_vectors kwargs were split into short_vectors(bound) and short_vectors_up_to_sign(bound).
- Poset, set iterator, element-class forwarding, and RealSet variadics were mapped or excluded from public specs.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Audit public signatures for remaining *args, **kwargs, option bags, and placeholder union data shapes.
- [ ] Open owner-specific tasks for any remaining collapsed Sage casework rather than restoring the inventory doc.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

