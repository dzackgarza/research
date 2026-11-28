# Task T-2003: Gate Embedding Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md line 27: "Derive the explicit primitive embedding matrices for
    $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}}
    \hookrightarrow \Lambda_{\mathrm{K3}}$."
  - GOAL.md line 22: "The **primitivity of the lattice embeddings** lack rigorous
    derivation in terms of coordinate bases."
  - GOAL.md Task 1.3: "Derive the explicit primitive embedding matrices for
    $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}}
    \hookrightarrow \Lambda_{\mathrm{K3}}$."
- GOAL linkage: Gate for T-3003 and T-3011

## Objective

Gate the embedding primitives by constructing embeddings with T-0003 and then separately
checking matrices, image lattices, complements, and is_primitive(...) against fixtures.
This gate verifies:

1. **Matrix equality**: The embedding matrix from T-0003 must equal the fixture matrix
   from T-1004 entry-by-entry
2. **Image lattice verification**: The image lattice $i(L) \subset M$ computed by T-0003
   must have the expected rank and discriminant
3. **Complement lattice verification**: The orthogonal complement computed by T-0003
   must match the fixture data from T-1004 (rank, signature, discriminant form)
4. **Primitivity predicate**: The is_primitive(L → M) predicate from T-0003 must return
   true for all fixtures
5. **Composition verification**: Composed embeddings T_Co → T_En → T_dP → Λ_K3 must
   equal the direct composite

## Parent Sufficiency Map

Blocks embedding and involution claims until the matrix-level objects and predicates are
exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0003, T-1002, T-1004
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Criteria

1. **Matrix entry equality**: Each embedding matrix must match the fixture matrix
   entry-by-entry
2. **Image lattice rank**: The rank of $i(L)$ must equal rank($L$) (injective map)
3. **Complement rank verification**: Complement rank must equal rank($M$) - rank($L$)
4. **Complement discriminant**: The discriminant form of the complement must match
   fixture
5. **Primitivity verification**: is_primitive() must return true for all embeddings in
   T-1004 fixtures
6. **Composition correctness**: The composite embedding must equal the product of
   individual matrices
7. **Saturation verification**: The saturated primitive closure must equal the primitive
   image

## Non-Goals

1. **No new embedding computation**: This is a gate, uses T-0003 as black box
2. **No primitivity proof**: Assumes T-0003 is correct; gate verifies consistency with
   fixtures
3. **No automorphism verification**: Does not compute full automorphism groups
4. **No uniqueness proof**: Only verifies consistency, not uniqueness of embeddings

## Allowed Dependencies

- **Prerequisite tasks**: T-0003 (embedding primitives), T-1002 (Coble invariants),
  T-1004 (embedding fixtures)
- **Local sources** (must cite):
  - tasks/goal_expansion.md — task ordering
  - STATE_MACHINE.md — tier semantics
  - PROOF_AUDITING.md — audit criteria

## Required Conventions

1. **Gate naming**: Use pattern `gate_embedding_<source>_<target>`
2. **Matrix comparison**: Use integer matrix equality, not approximate
3. **Complement convention**: Complement computed as orthogonal complement in ambient
   lattice
4. **Failure format**: Report as
   `gate_fail: embedding <source>→<target> - <mismatch-details>`

## Failure Conditions

1. **Matrix mismatch**: If any matrix entry differs, gate fails with `fail_matrix`
2. **Non-injective**: If image rank < source rank, gate fails with `fail_injective`
3. **Complement rank mismatch**: If complement rank differs from expected, gate fails
   with `fail_complement_rank`
4. **Complement discriminant mismatch**: If complement discriminant form differs, fails
   with `fail_complement_discriminant`
5. **Primitivity failure**: If is_primitive returns false for a fixture, gate fails with
   `fail_primitive`
6. **Composition failure**: If composed matrix differs from direct composite, fails with
   `fail_composition`
