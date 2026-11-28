# Task T-0002: Invariant And Predicate Primitives For 2-Elementary Lattices

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 0.

## Origin

- GOAL.md source: lines 15-19 define (r,a,δ) invariants for S_Co, T_Co, T_En, T_dP
- GOAL.md line 34: "Nikulin's classification (Nikulin 1.5.2)"
- GOAL.md line 37: "primitive isotropic vector v with div(v)=d... image v/d + T ∈ A_T"
- GOAL.md Task 1.2: "verify their (r,a,δ) invariants and genus cardinality"
- GOAL.md Task 2.1: "Enumerate isotropic vectors in A_{T_Co}"

## Objective

Expose invariant and predicate primitives for 2-elementary lattices:
- rank(L) → Integer
- signature(L) → (p,q) tuple
- determinant(L) → Integer
- (r, a, δ) invariants per Nikulin (r=rank, a=length of discriminant form, δ∈{0,1})
- discriminant_form(L) → finite quadratic form on A_L = L*/L
- brown_invariant(L) → Integer (for 2-elementary lattices)
- divisibility(v) → Integer (for lattice vectors v)
- is_isotropic(v, L) → Boolean
- is_primitive(v, L) → Boolean (vector is not divisible in L)

## Deliverable Type

shared tool — reusable primitives with explicit contracts.

## Acceptance Criteria

1. **Core invariants**: Functions return correct values for known fixtures
   - S_Co: rank=11, signature=(1,10), det=2¹⁰
   - T_Co: rank=11, signature=(2,9), det=2¹¹
   - T_En: (r,a,δ) = (12,10,0)
   - T_dP: (r,a,δ) = (20,2,0)
   - Λ_K3: unimodular (det=1)

2. **(r,a,δ) implementation**: Implement Nikulin's formulas for 2-elementary lattices:
   - r = rank of lattice
   - a = length of discriminant group (rank of A_L as F_2-vector space)
   - δ = 0 if discriminant form is of type I, 1 if type II

3. **Brown invariant**: Compute B(L) = sum_{x∈A_L} q(x) mod 2 for 2-elementary lattices

4. **Isotropic predicate**: For a vector v in lattice L, verify v² = 0 in Z

5. **Primitivity predicate**: For a vector v, verify v is not divisible by any integer
   >1 in L

6. **Discriminant group**: Return A_L = L*/L as finite abelian group with quadratic form

7. **Import test**: All functions importable from coble_geometry_foundation

## Non-Goals

- Does not enumerate orbits or compute stabilizers (T-0004)
- Does not construct embeddings (T-0003)
- Does not compute indefinite isotropic planes (T-0005)
- Does not prove uniqueness of isometry classes (mathematical claim)
- Does not compute Vinberg chambers or Coxeter data (T-0006)

## Allowed Dependencies

- Prerequisite tasks: T-0001 (uses its lattice constructors)
- Local sources:
  - src/coble_geometry_foundation.sage (extend with invariants)
  - theory/mathematical_background.md (Nikulin formulas)
  - theory/oscar_lattices.md (Oscar API for quadratic forms)

## Required Conventions

- Function naming: `<property>_invariant()` or `<property>_predicate()`
- All functions accept IntegralLattice objects from foundation library
- (r,a,δ) returns tuple of three integers
- signature returns (positive, negative) tuple
- discriminant form returns sage structure with q: A_L → Q/2Z

## Failure Conditions

1. If any invariant returns wrong value for known fixtures → fail
2. If (r,a,δ) computation doesn't match Nikulin's definition → fail
3. If Brown invariant computation is incorrect mod 2 → fail
4. If isotropic/primitive predicates give wrong answers for test vectors → fail
5. If discriminant group computation doesn't produce correct A_L → fail
6. If any function raises exception on valid input → fail

## Parent Sufficiency Map

Supplies the invariant layer needed for:
- T-2001: gates lattice constructors using invariants
- T-2002: gates discriminant-form primitives using (r,a,δ)
- T-3002: verifies S_Co, T_Co invariants against fixtures
- T-3005: enumerates isotropic vectors in A_T using divisibility

Discharges no GOAL.md burden by itself.
