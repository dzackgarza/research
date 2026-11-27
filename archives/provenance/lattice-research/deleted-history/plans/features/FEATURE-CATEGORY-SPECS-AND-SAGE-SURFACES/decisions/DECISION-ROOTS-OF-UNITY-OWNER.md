---
id: DECISION-ROOTS-OF-UNITY-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-RINGS]]'
title: Decide roots-of-unity ownership for zeta and zeta_order on non-finite-field rings
status: decided
priority: medium
description: Resolve where `zeta(n)` and `zeta_order()` live in the category hierarchy
  for rings that are not finite fields.
resolution: |
  - Finite fields own constructive `zeta(n)` and `zeta_order()` via `FiniteFields.ParentMethods`.
    Sage source confirms these are defined on `FiniteFields` with element-factored-order 
    helpers.
  - For arbitrary commutative rings, `zeta(n)` and `zeta_order()` are NOT admitted as 
    general `Rings()` methods. They require a roots-of-unity or torsion-unit structure 
    that is not present for arbitrary rings.
  - If a future phase needs these on broader ring families (e.g., integral domains with 
    a distinguished primitive root), a dedicated `RootsOfUnity` axiom or 
    `Rings().TorsionUnits()` refinement should be source-grounded before admission.
  - Current disposition: deferred. The spec correctly records the finite-field owner 
    and the gap for general rings.
evidence:
- "Sage source: sage/categories/finite_fields.py defines zeta/zeta_order on FiniteFields.ParentMethods"
- "Sage source: sage/rings/qqbar.py defines zeta on algebraic numbers (not a ring category method)"
- SPEC-MAPPING-RINGS.md line 90 documents the gap
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide roots-of-unity ownership

## Question

Where should `zeta(n)` and `zeta_order()` live in the ring category hierarchy? Sage
exposes them on both `Rings.ParentMethods` and `FiniteFields.ParentMethods`. The generic
ring-level methods are too broad to admit without a proper mathematical owner.

## Decision

Finite fields own the constructive implementation. General rings do not admit these
methods. A future `RootsOfUnity` or torsion-unit refinement may add them back with
proper source grounding.

## Work Log

- 2026-05-07: Created from Gate 5 review finding on SPEC-MAPPING-RINGS.
