---
id: DECISION-20260528-JOIN-MEET-CAT-INSTANCE-OWNERSHIP
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide that join/meet are Cat() instance methods, not Category static methods
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide that join/meet are Cat() instance methods, not Category static methods

## Summary

Sage defines `Category.join` and `Category.meet` as `@staticmethod` on the base
`Category` class. In the project's category-spec layer, `join` and `meet` are
mathematically owned by `Cat()` (the category-of-categories singleton), not by
individual `Category` instances.
Since categories are singletons, a static method makes no sense — the only sensible call
pattern is `Cat().join(C_1, C_2)`.

This implies:

- `Cat().join(categories)` and `Cat().meet(categories)` are instance methods on the
  `Cat` singleton class.
- `Category` (the project's base category class) does not own `join` or `meet`. A stale
  `@staticmethod join` on `Category` in `base_category_types.py` was removed (this
  decision session), and all call sites were migrated to `Cat().join(...)`.
- The mypy `[override]` errors on `Cat.join` and `Cat.meet` (lines `cat/__init__.py:250`
  and `cat/__init__.py:255`) are expected consequences of this design: Sage defines
  these as `@staticmethod` and the project overrides them as instance methods.
  These errors are classified as `category_specs method-owner/spec` and reference this
  decision card.

## Source Provenance

- Discussion in interactive session, 2026-05-28.
- Issue `lattice-research#6`, override ownership audit (Product B).
- Existing code: `cat/__init__.py:250-268` already used instance methods; the
  inconsistency was the stale `@staticmethod` on `base_category_types.py:600-604`.

## Decision

`join` and `meet` are instance methods on `Cat()`. The call surface is
`Cat().join(categories)` and `Cat().meet(categories)`. They delegate internally to
Sage's static methods but are not themselves static.

## Consequences

- `Category` (project base class) no longer defines `join`.
- All 10 call sites migrated from `Category.join(...)` to `Cat().join(...)`.
- The 3 mypy `[override]` errors on `cat/__init__.py` for `join` and `meet` are accepted
  as design-driven and classified `category_specs method-owner/spec` in the diagnostic
  ledger.
- These override errors will not be resolved by the mypy plugin, Sage stubs, or further
  category-spec code changes — the design deliberately differs from Sage.
