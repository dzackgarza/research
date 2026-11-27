---
id: DECISION-LAT-PHASE0-QUOTIENT-SYNTAX-DISPATCH
trackerStatus:
  type: decision
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn: []
title: Choose Phase 0 Sage quotient syntax dispatch route
status: unstarted
chosen: ''
options:
- name: Direct Sage-class compatibility patch
  pros:
  - Can satisfy ZZ / n and ZZ.quotient(n*ZZ) syntax expected by tests/sage_spec/misc.sage.
  - Keeps quotient syntax near Sage interop boundary instead of pretending category
    refinement intercepts methods it does not intercept.
  cons:
  - Requires explicit approval because the migrated Phase 0 plan rejected direct monkeypatching
    for this surface.
  - Must be tightly scoped to quotient syntax and preserve native Sage quotient/coercion
    behavior.
- name: Split category-refinable methods from quotient compatibility
  pros:
  - Preserves the no-direct-monkeypatch rule for ModuleBaseRings category refinement
    itself.
  - Makes the unsupported Sage special-method dispatch limitation explicit in card
    structure.
  cons:
  - Requires revising Phase 0 task boundaries before implementation can resume.
  - Leaves tests/sage_spec/misc.sage quotient syntax unavailable until a separate
    compatibility patch is approved.
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Choose Phase 0 Sage quotient syntax dispatch route

## Question

How should Phase 0 implement the integer-ring quotient syntax required by `tests/sage_spec/misc.sage`, given that Sage category refinement does not intercept the relevant existing methods?

## Evidence

A live Sage 10.7 preflight showed:

- `_refine_category_` can add ordinary category methods to `ZZ` and can route `ZZ**3` and `ZZ.ideal(2)` through toy `ModuleBaseRings.ParentMethods`.
- `ZZ / 2` still fails through Sage's existing unsupported division slot even when the refined category defines `ParentMethods.__truediv__`.
- `ZZ.quotient(2*ZZ)` still uses Sage's native ring quotient method rather than a toy refined-category `ParentMethods.quotient`.
- `QQ / ZZ` and `QQ / (n*ZZ)` already route through Sage's `RationalField.__truediv__` to `QmodnZ(n)`, with `base_ring() == ZZ`, quotient-class equality, and canonical `lift()` behavior.

## Affected Cards

- `TASK-LAT-PHASE0-MODULE-BASE-RINGS` is blocked on this decision.
- `TASK-LAT-PHASE0-IDEAL-QUOTIENT-MODULES` and `TASK-LAT-PHASE0-FRACTION-QUOTIENT-CODOMAINS` should not assume `ModuleBaseRings` alone owns quotient syntax until this is decided.

## Decision Criteria

- Preserve the Phase 0 mathematical contract: `R / I` is a quotient module construction and `ZZ / n` must be available for the spec workflow.
- Do not weaken `tests/sage_spec/misc.sage` to match current Sage behavior.
- Keep Sage interop behavior intact where Sage already works, especially native quotient rings and `QmodnZ`.
- Prefer the narrowest approved interop boundary that makes the mathematical syntax executable.
