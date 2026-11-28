# Task T-1002: Literature-Backed Invariant Ledger For Coble Lattices

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 1.

## Origin

- GOAL.md source: lines 15-19 define S_Co, T_Co, T_En, T_dP with exact Gram matrices
- GOAL.md line 17: "T_Co = S_Co^{⊥ Λ_K3} ≅ (11, 11, 1)_2" signature (2,9)
- GOAL.md line 18: "discriminant groups (Z/2Z)^11, q_S = -q_T mod 2Z"
- GOAL.md Task 1.2: "verify their (r,a,δ) invariants and genus cardinality"
- GOAL.md references: Nikulin (1979), Dolgachev & Kondyrev (2013), Sterk (1991)

## Objective

Assemble literature-backed invariant ledger for Coble lattices:
- S_Co: (r,a,δ) = (11,11,1), signature (1,10), det = -2^10, discriminant form q_S
- T_Co: (r,a,δ) = (11,11,1), signature (2,9), det = 2^11, discriminant form q_T
- T_En: (r,a,δ) = (12,10,0), signature (2,10), det = 2^10
- T_dP: (r,a,δ) = (20,2,0), signature (2,20), det = 2^2

Including claimed (r,a,δ), signatures, determinant data, and discriminant-form relations
q_S = -q_T (mod 2Z).

## Deliverable Type

fixture data — canonical expected values for downstream verification.

## Acceptance Criteria

1. **Invariant ledger**: Document each lattice with:
   - rank (r), length (a), δ
   - signature (p,q)
   - determinant |det|
   - discriminant group A_L ≅ (Z/2Z)^a
   - discriminant quadratic form q_L: A_L → Q/2Z

2. **Literature source**: Each invariant value traces to GOAL.md text or cited reference
   (Nikulin, Dolgachev-Kondyrev, Sterk, AEGS)

3. **Discriminant form relation**: Verify q_S = -q_T mod 2Z for S_Co, T_Co pair

4. **Test harness**: Create Sage script that computes invariants for each lattice and
   prints vs expected

5. **Fixture file**: Save as YAML/JSON in theory/computations/fixtures/

6. **Import test**: Fixtures loadable without error

## Non-Goals

- Does not verify correctness (that's T-2002)
- Does not prove genus uniqueness (just provides fixtures)
- Does not compute embeddings
- Does not enumerate orbits or isotropy

## Allowed Dependencies

- Prerequisite tasks: none
- Local sources:
  - GOAL.md (canonical values)
  - REFERENCES.md (literature spine)
  - theory/mathematical_background.md (Nikulin invariants)
  - theory/literature_claim_map.md (claim traceability)

## Required Conventions

- Fixture format: YAML with lattice name keys, nested invariant fields
- Each entry includes: r, a, delta, signature, det, discriminant_group, reference_source
- Test harness uses asserts

## Failure Conditions

1. If any fixture value doesn't match GOAL.md specification → fail
2. If discriminant form relation q_S = -q_T not documented → fail
3. If test harness fails on any lattice → fail
4. If fixture file doesn't parse → fail

## Parent Sufficiency Map

Provides fixtures for:
- T-2001: gates S_Co, T_Co invariants against these values
- T-2002: gates discriminant-form computation against these fixtures
- T-3002: verifies S_Co, T_Co invariants using this ledger
- T-3003: uses T_Co fixture for embedding target

This is fixture collection only — no verification performed.
