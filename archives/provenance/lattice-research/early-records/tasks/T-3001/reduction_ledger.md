# Reduction Ledger: T-3001

This file documents how each exact computation in T-3001 strengthens a GOAL.md claim.

## GOAL.md Linkage

- **GOAL.md Item**: Task 1.1: "Derive an explicit equation F(x,y,z)=0 for a rational
  sextic with 10 nodes and the corresponding K3 surface w^2 = F(x,y,z)."
- **GOAL.md Section**: 1. Foundation: Coble Curves and Picard Lattices

## Necessity Statement

Exact computation is required because:
- The sextic equation must have exact rational coefficients to verify nodal conditions
  precisely.
- The K3 cover is a algebraic surface; exact equations are required for singularity
  classification.
- The nodal profile verification requires precise polynomial evaluation, not numerical
  approximation.
- Rationality/birationality checks depend on exact geometric properties.

## Computed Values

1. **Sextic polynomial F(x,y,z)**: Explicit homogeneous degree-6 polynomial with exact
   rational coefficients.
2. **Nodal positions**: 10 specific points in P^2 where F and its derivatives vanish.
3. **Singularity types**: Verification that each node is an A_1 singularity (type A_1).
4. **K3 cover equation**: w^2 = F in weighted projective space P(1,1,1,3).
5. **K3 singularities**: 10 A_1 singularities in the double cover above the nodal
   points.
6. **Rationality confirmation**: Evidence that the base is a rational surface.

## Strengthening Claim

This explicit example verifies that GOAL.md's theoretical description of 10-nodal Coble
surfaces can be realized with concrete equations.
This concrete realization is necessary for:
- Verifying the lattice invariants in T-3002 using the actual blown-up surface
- Providing a test case for the primitive embedding verification in T-3003
- Serving as a concrete example for the involution construction in T-3011

Without an explicit sextic and K3 cover, the project remains at the level of abstract
theory without computational verification.
