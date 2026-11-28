# Task T-0001: Canonical Lattice Constructors And Coercions

## Status

Selected in Wave A. REPLAN_REQUIRED as of 2026-04-03 because
`src/coble_geometry_foundation.sage` requires the separate prerequisite task
`T-0011` before this task may rely on or extend any admitted shared-base surface.

## Tier

Tier 0.

## Origin

- GOAL.md source: lines 15-19 define S_Co, T_Co, T_En, T_dP, Lambda_K3 with exact Gram
  matrices
- GOAL.md Task 1.2: "Compute the Gram matrices for S_Co and T_Co"
- GOAL.md Task 1.3: "Derive the explicit primitive embedding matrices for T_Co → T_En →
  T_dP → Λ_K3"
- GOAL.md Task 5.1: "Construct the 22×22 matrix θ" requiring Λ_K3 construction

## Objective

Build canonical lattice constructors and coercions for:
- S_Co = ⟨2⟩ ⊕ ⟨-2⟩¹⁰ (Gram: diag(2, -2¹⁰), signature (1,10))
- T_Co = ⟨2⟩ ⊕ U ⊕ E8(-1) (Gram: diag(2, 2, -2⁹), signature (2,9))
- T_En = U ⊕ U(2) ⊕ E8(-2) (signature (2,10), (r,a,δ) = (12,10,0))
- T_dP = U ⊕ U(2) ⊕ E8(-1)² (signature (2,20), (r,a,δ) = (20,2,0))
- Λ_K3 = U³ ⊕ E8² (rank 22, signature (22,0), unimodular)
- Standard factors: U, A_1 = ⟨-2⟩, E8 (scaled variants)

With exact conversion between the foundation library (coble_geometry_foundation.sage)
and Oscar objects.

## Deliverable Type

shared tool — reusable primitives with explicit contracts.

## Acceptance Criteria

1. **Function inventory**: Each lattice has a constructor function with documented
   signature
   - `S_Co_lattice() → IntegralLattice`
   - `T_Co_lattice() → IntegralLattice`
   - `T_En_lattice() → IntegralLattice`
   - `T_dP_lattice() → IntegralLattice`
   - `Lambda_K3_lattice() → IntegralLattice`
   - `hyperbolic_plane() → IntegralLattice`
   - `E8_lattice(scale=-1) → IntegralLattice`

2. **Invariant verification**: Each constructor returns a lattice with the correct:
   - rank (11, 11, 12, 20, 22, 2, 8 respectively)
   - signature (as documented above)
   - determinant (computed from Gram matrix)

3. **Oscar coercion**: Convert foundation library lattices to Oscar via
   `Oscar.Lattice(ZZ, Gram)` and verify invariants match

4. **Coercion roundtrip**: Lattice → Oscar → Lattice preserves Gram matrix exactly

5. **Import test**: `from coble_geometry_foundation import *` loads all constructors
   without error

## Non-Goals

- Does not compute isotopic vectors or orbit decompositions (T-0002, T-0004)
- Does not construct embeddings or primitivity predicates (T-0003)
- Does not construct involutions (T-0008)
- Does not prove isomorphism to any target lattice (mathematical claim)
- Does not export to external formats (JSON, YAML) — only Python objects

## Allowed Dependencies

- Prerequisite tasks: T-0011 (shared-base decontamination and trusted-base admission)
- Local sources:
  - src/coble_geometry_foundation.sage (admitted version only; blocked pending
    T-0011)
  - theory/oscar_lattices.md (Oscar API conventions)
  - theory/library_integration.md (layer organization)

## Required Conventions

- All constructors return `IntegralLattice` objects
- Gram matrix uses standard basis ordering per GOAL.md notation
- Function naming: `<LatticeName>_lattice()` for constructors
- Scale parameter for E8: default -1 (negative definite for root systems)
- Hyperbolic plane U uses standard Gram [[0,1],[1,0]]

## Failure Conditions

1. If any constructor produces a lattice with incorrect rank, signature, or determinant
   → fail
2. If Oscar coercion fails or produces different invariants → fail
3. If roundtrip does not preserve exact Gram matrix entries → fail
4. If import test fails → fail
5. If any function raises an exception during documented usage → fail

## Parent Sufficiency Map

Supplies the canonical lattice objects for downstream lattice-theoretic tasks:
- T-0002: uses these lattices for invariant computation
- T-0003: uses these as source/target for embeddings
- T-0008: uses Λ_K3 for involution construction
- T-3002: verifies invariants of S_Co, T_Co using these constructors
- T-3003: embeds T_Co into Λ_K3 using these constructors
- T-3011: constructs θ on Λ_K3 using these constructors

Discharges no GOAL.md burden by itself.
