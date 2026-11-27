---
id: DECISION-ORE-LOCALIZATION-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Decide noncommutative Ore localization category ownership
status: decided
priority: medium
description: Resolve where noncommutative Ore localization lives in the category
  hierarchy. Sage's localization is commutative-only (on IntegralDomains).
resolution: |
  - Commutative localization at a multiplicative set is owned by `Rings().Commutative()`.
    Sage's current implementation lives on `IntegralDomains` but the mathematical 
    definition works for any commutative ring. SPEC-MAPPING-RINGS correctly insists 
    on commutative-ring localization rather than weakening to domain-only.
  - Noncommutative Ore localization requires an Ore condition (left/right Ore sets) 
    and is a distinct mathematical construction. It does not belong on general `Rings()`.
  - If Ore localization is needed for downstream work (e.g., Ore algebras, D-modules), 
    it should live under an `OreRings()` or `Rings().Ore()` refinement with explicit 
    hypotheses: the ring must satisfy the Ore condition for the chosen multiplicative set.
  - Current disposition: deferred. The ring mapping spec correctly separates commutative 
    and Ore localization. If Ore localization is needed, create a source-grounded 
    `OreRings` owner with the Ore condition as an explicit hypothesis.
evidence:
- "Sage source: sage/rings/localization.py implements commutative localization"
- "Sage source: sage/categories/integral_domains.py is where Sage localization lives, but the mathematical definition generalizes to commutative rings"
- SPEC-MAPPING-RINGS.md line 91 documents the gap
- TASK-RESEARCH-ORE-ALGEBRA-INTERFACE exists for Ore algebra backend research
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide Ore localization ownership

## Question

Where does noncommutative Ore localization live? Sage has commutative localization
only. The spec correctly separates commutative and noncommutative cases.

## Decision

Commutative localization: `Rings().Commutative()`. Ore localization: deferred to a
future `OreRings()` refinement. Not admitted on general `Rings()`.

## Work Log

- 2026-05-07: Created from Gate 5 review finding on SPEC-MAPPING-RINGS.
