# Task T-0008: Involution And Polarization Primitives

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 0.

## Origin

- GOAL.md source: line 79 "theta must act on Λ_K3 such that its invariant and
  coinvariant sublattices are correctly identified: Λ_K3^θ ≅ T_Co and Λ_K3^{-θ} ≅ S_Co"
- GOAL.md line 85: "Construct the 22×22 matrix θ"
- GOAL.md Task 5.1: "Construct the 22×22 matrix θ and compute the signature and
  invariants of its fixed sublattice"
- GOAL.md line 49: "Γ_Co = Stab_{O(T_En)}(h_Co) ∩ Z_{O(T_En)}(θ)"
- GOAL.md Task 6.1: "Map the Coble polarization h_Co to the surgery vector ℓ"

## Objective

Expose involution and polarization primitives:
- sign_involution(L, sign_vector) → involution matrix on L
- invariant_sublattice(involution) → fixed-point sublattice (eigenvalue +1)
- coinvariant_sublattice(involution) → -1 eigenspace (orthogonal complement in L)
- eigenspace_decomposition(involution) → (L⁺, L⁻) pair
- transport_polarization(h, from_L, to_L) → vector in target lattice
- discriminant_image(involution) → action on A_L induced by involution
- polarization_class(L) → distinguished generator of Neron-Severi group

## Deliverable Type

shared tool — reusable primitives with explicit contracts.

## Acceptance Criteria

1. **Involution matrix**: Given lattice L and sign vector (±1 per basis vector), produce
   order-2 integer matrix M with M^T G M = G

2. **Eigenspace extraction**: Compute L⁺ = {v ∈ L | θv = v} and L⁻ = {v ∈ L | θv = -v}
   as sublattices

3. **Signature verification**: For horizontal folding involution θ on Λ_K3, L⁺ ≅ T_Co
   has signature (2,9), L⁻ ≅ S_Co has signature (1,10)

4. **Discriminant action**: Compute induced action on A_L = L*/L; verify it respects
   quadratic form

5. **Polarization transport**: Given h in source lattice, find equivalent class in
   target via numerical equivalence

6. **Test case**: Standard horizontal folding θ on Λ_K3 gives L⁺ ≅ T_Co (signature
   (2,9)), L⁻ ≅ S_Co (signature (1,10))

7. **Import test**: All functions importable from coble_geometry_foundation

## Non-Goals

- Does not compute full Γ_Co generator set (that's T-3007, T-3008)
- Does not prove uniqueness of involution (theorem claim)
- Does not compute Vinberg chambers or Coxeter data (T-0006)
- Does not compute automorphism groups (T-0004)
- Does not verify slc stability of B(ℓ) models (that's T-3013)

## Allowed Dependencies

- Prerequisite tasks: T-0003 (uses embedding primitives for eigenspace extraction)
- Local sources:
  - src/coble_geometry_foundation.sage (extend with involution)
  - theory/oscar_lattices.md (Oscar eigenspace computation)
  - theory/library_integration.md

## Required Conventions

- Function naming: `<operation>_involution()` or `<operation>_polarization()`
- Involution returns integer matrix (rank(L) × rank(L))
- Eigenspaces returned as IntegralLattice objects
- Polarization transport returns vector in target lattice

## Failure Conditions

1. If involution matrix doesn't satisfy M² = I → fail
2. If involution doesn't preserve Gram matrix (M^T G M = G) → fail
3. If eigenspace dimensions don't match expected signatures → fail
4. If discriminant image doesn't preserve quadratic form → fail
5. If polarization transport produces non-equivalent class → fail
6. If any function raises exception on valid input → fail

## Parent Sufficiency Map

Supplies involution infrastructure for:
- T-2008: gates involution primitives using fixtures
- T-3011: constructs θ on Λ_K3 and verifies eigenspaces
- T-3007: computes discriminant-image for Γ_Co
- T-3012: maps h_Co to surgery vector ℓ
- T-3008: uses involution for full Γ_Co generator package

Discharges no GOAL.md burden by itself.
