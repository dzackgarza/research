---
id: TASK-RESEARCH-ISOTROPIC-ORBIT-ENUMERATION
trackerStatus:
  type: task
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]'
title: Research isotropic orbit enumeration in finite discriminant groups
status: needs-review
priority: medium
description: Research exact backend and theory routes for enumerating isotropic discriminant-form orbits in the Coble 2-elementary finite quadratic group.
successCriteria:
- The output records which backend or theorem route can compute O(A,q)-orbits for the specific Coble discriminant group.
- The recommendation states feasibility, expected inputs, and any blockers for implementation without replacing exhaustive orbit work by bounded search.
complexity: 30
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Research: Isotropic orbit enumeration in finite discriminant groups

## Summary

Survey existing software capabilities for computing orbits of isotropic (norm-0)
elements under the orthogonal group O(A, q) of a finite quadratic form over Z/2^kZ,
specifically for discriminant groups of 2-elementary lattices A ≅ (Z/2Z)^11.

## Input

- A finite quadratic form q: A → Q/2Z on A ≅ (Z/2Z)^11 (order 2048).
- The orthogonal group O(A, q) as a finite matrix group.
- The set of isotropic elements {x ∈ A : q(x) = 0 mod 2Z} (known count: 528
  elements for the standard form).

## Questions

1. **GAP**: Can `OrbitsDomain(O, elements)` handle a group of size |O(A,q)| on 528
   points? Is the group small enough to compute directly? What's the expected orbit
   count and stabilizer structure?

2. **Sage**: Does `QuadraticForm.automorphism_group()` produce the full O(q)?
   Can its output be used with Sage's `PGroup` or `MatrixGroup` orbit methods?

3. **Oscar/Hecke**: What discriminant-form orbit methods exist?

4. **Burnside**: Can the orbit count be derived from character theory or invariant
   theory without enumerating the full group?

## Output

A brief report (theory note or decision card body) recording:
- Which backends handle this computation for the specific discriminant group
- Feasibility (can we compute all orbits directly, or do we need theory)
- Recommended implementation route
