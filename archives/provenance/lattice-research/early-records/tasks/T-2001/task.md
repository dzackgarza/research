# Task T-2001: Gate Canonical Lattice Constructors And Coercions

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md line 15: "**Coble Lattice**: $S_{\mathrm{Co}} \cong \langle 2 \rangle \oplus
    \langle -2 \rangle^{10} \cong (11, 11, 1)_1$. Signature $(1, 10)$."
  - GOAL.md line 17: "**Transcendental Lattice**: $T_{\mathrm{Co}} =
    S_{\mathrm{Co}}^{\perp \Lambda_{\mathrm{K3}}} \cong (11, 11, 1)_2$. Signature $(2,
    9)$."
  - GOAL.md line 19: "**Ambient Lattices**: $T_{\mathrm{En}} \cong (12, 10, 0)*2$,
    $T*{\mathrm{dP}} \cong (20, 2, 0)*2$, and $\Lambda*{\mathrm{K3}} \cong (22, 0,
    0)_1$."
  - GOAL.md Task 1.2: "Compute the Gram matrices for $S_{Co}$ and $T_{Co}$, and verify
    their $(r, a, \delta)$ invariants and **genus cardinality**."
- GOAL linkage: Gate for T-3002, T-3003, and T-3011

## Objective

Gate the lattice constructors and coercions by replaying T-0001 and T-0002 on T-1001 and
T-1002, then matching the exact object identities and invariant outputs.
This gate verifies:

1. **Exact object identity**: Constructed lattices from T-0001 must match the fixture
   data from T-1001 on:
   - Rank (dimension)
   - Signature (numbers of positive/negative eigenvalues)
   - Determinant (discriminant)
   - Discriminant group structure
2. **Invariant consistency**: Invariant outputs from T-0002 (rank, signature,
   determinant, (r,a,δ), discriminant form) must match expected values from T-1002
3. **Gram matrix verification**: The Gram matrix from T-0001 constructor must equal the
   expected matrix from T-1002 fixture

## Parent Sufficiency Map

Blocks downstream lattice results until the activated object constructors and invariant
primitives are exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0001, T-0002, T-1001, T-1002
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Criteria

1. **T-0001 replay passes**: Re-running T-0001 constructors on T-1001 fixture data must
   produce lattices with exact matching invariants
2. **T-0002 invariants match**: The rank, signature, determinant, and (r,a,δ) from
   T-0002 must match the fixture values from T-1002
3. **Gram matrix equality**: Constructed Gram matrix must equal fixture Gram matrix
   entry-by-entry
4. **Discriminant group isomorphism**: The discriminant group $A_L = L^*/L$ from
   constructed lattice must be isomorphic to fixture's discriminant group
5. **Coercion path verification**: Lattice objects created via T-0001 must coerce
   correctly to Oscar lattice types without data loss
6. **Roundtrip serialization**: Lattice objects serialized via T-0001 and re-loaded must
   produce bit-identical objects

## Non-Goals

1. **No new lattice construction**: This is a gate, not a constructor; uses T-0001 and
   T-0002 as black box
2. **No algorithmic verification**: Uses exact equality checks, not probabilistic or
   sampling methods
3. **No proof of correctness**: Assumes T-0001/T-0002 are correct; gate only verifies
   consistency with fixtures
4. **No error handling for T-0001/T-0002**: If primitives fail, this gate fails; error
   propagation is not the gate's concern
5. **No fixture generation**: Uses T-1001/T-1002 fixtures; does not generate new fixture
   data

## Allowed Dependencies

- **Prerequisite tasks**: T-0001 (constructors), T-0002 (invariants), T-1001 (standard
  lattices), T-1002 (Coble invariants)
- **Local sources** (must cite):
  - tasks/goal_expansion.md — task ordering and tier structure
  - STATE_MACHINE.md — tier semantics and gate requirements
  - PROOF_AUDITING.md — audit criteria for verification tasks

## Required Conventions

1. **Gate naming**: Use pattern `gate_<T-0-tool>_<fixture>` for gate implementations
2. **Assertion function**: Create reusable
   `assert_lattice_equals_fixture(lattice, fixture)` function
3. **Error reporting**: Report which specific invariant mismatched (rank, signature,
   determinant, etc.)
4. **Fixture loading**: Load T-1001/T-1002 fixtures via standardized fixture loader, not
   ad-hoc paths
5. **Verification method**: Use exact mathematical equality (==), not approximate or
   numerical methods
6. **Failure format**: Report as `gate_fail: <tool> vs <fixture> - <mismatch-details>`

## Failure Conditions

1. **Rank mismatch**: If constructed lattice rank differs from fixture rank, gate fails
   with `fail_rank`
2. **Signature mismatch**: If signature differs, gate fails with `fail_signature`
3. **Determinant mismatch**: If determinant differs, gate fails with `fail_determinant`
4. **Gram matrix inequality**: If any matrix entry differs, gate fails with
   `fail_gram_matrix`
5. **Discriminant group mismatch**: If discriminant groups are not isomorphic, gate
   fails with `fail_discriminant_group`
6. **Serialization failure**: If roundtrip fails, gate fails with `fail_serialization`
