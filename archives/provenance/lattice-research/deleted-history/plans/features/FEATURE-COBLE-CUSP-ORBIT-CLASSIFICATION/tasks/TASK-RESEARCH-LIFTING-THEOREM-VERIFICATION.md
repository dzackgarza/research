---
id: TASK-RESEARCH-LIFTING-THEOREM-VERIFICATION
trackerStatus:
  type: task
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]'
- '[[TASK-RESEARCH-ISOTROPIC-ORBIT-ENUMERATION]]'
title: Verify Nikulin 1.5.2 and Eichler criterion for lattice T_Co
status: needs-review
priority: medium
description: Verify the theorem hypotheses needed to lift discriminant-form isotropic orbits to primitive isotropic vector orbits in T_Co.
successCriteria:
- A durable theory note records the exact Nikulin and Eichler statements, their hypotheses, and whether they apply to the computed Coble lattice.
- Any orbit-lifting conclusion states the required group, divisibility, discriminant class, and remaining blockers without relying on notation alone.
complexity: 35
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Research: Verify Nikulin surjectivity and orbit lifting for T_Co

## Summary

The isotropic orbit analysis (Tasks 2.1-2.2) requires lifting O(q_T)-orbits in
the discriminant group A_{T_Co} to O^*(T_Co)-orbits of primitive isotropic vectors
in the lattice T_Co. This uses Nikulin's surjectivity theorem (Prop. 1.5.2)
and the Eichler criterion. Verify that the hypotheses hold for T_Co.

## Hypothesis check

T_Co has the following known/expected properties:
- Rank 11, signature (2, 9)
- 2-elementary discriminant group A ≅ (Z/2Z)^11
- Even lattice (all inner products even)
- Discriminant form q_T: A → Q/2Z

Nikulin 1.5.2 gives conditions under which the map O(L) → O(A_L, q_L) is
surjective. For an even 2-elementary lattice:

1. The spinor norm on O(L) must be computed (or its image in O(A) via the
   connecting homomorphism).
2. The Eichler criterion states that for an indefinite lattice of rank ≥ 3,
   the spinor norm kernel acts transitively on primitive vectors of given
   divisibility and given discriminant class, provided the discriminant class
   is nonzero. For T_Co of rank 11 ≥ 3, this should apply.

## Questions

1. Does Nikulin 1.5.2 apply to T_Co given its signature (2, 9) and (r, a, δ)?
   What are the precise conditions?

2. Is the spinor norm surjectivity known for the Coble lattice? Is O(T_Co) →
   O(A_{T_Co}) surjective, and if not, what is the image?

3. Does the Eichler criterion apply to vectors of divisibility 2 in T_Co?
   (The predicted divisibility for primitive isotropic vectors in the even model.)

4. Are the isotropic orbits in A_{T_Co} in bijection with the O^*(T_Co)-orbits
   of primitive isotropic vectors with divisibility 2? Or does the stable
   orthogonal group O^* need more careful definition here?

## Output

A theory note under `theory/foundations/` recording:
- The relevant theorem statements
- The verification (or blocking issues) for T_Co
- The orbit-count prediction and its theoretical basis
