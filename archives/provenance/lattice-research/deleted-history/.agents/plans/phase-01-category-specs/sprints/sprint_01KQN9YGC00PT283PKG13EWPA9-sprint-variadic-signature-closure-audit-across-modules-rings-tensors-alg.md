---
trackerStatus:
  type: plan
title: Sprint variadic signature closure audit across modules rings tensors algebras lattices posets sets and real-set constructors
status: approved
planId: SPR-VARIADIC-AUDIT-01KQN9
planType: sprint-plan
priority: high
parentPlan: PLN-AUDIT-000
tags:
- category-specs
- plan
- sprint
- constructors
- modules
- rings
- precision
- sets
- algebras
- tensors
- posets
- lattices
- signatures
- audit
- theme-plan-control
---

# Sprint variadic signature closure audit across modules rings tensors algebras lattices posets sets and real-set constructors

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

The deleted variadic inventory records the scoping pass for public surfaces that had
collapsed Sage casework or raw coordinate interop into broad signatures.

## Source Provenance

- `category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Sprint variadic signature closure audit across modules rings tensors algebras lattices posets sets and real-set constructors from category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`

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

