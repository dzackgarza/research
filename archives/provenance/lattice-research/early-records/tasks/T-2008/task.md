# Task T-2008: Gate Involution Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md line 49: "The arithmetic group $\Gamma_{\mathrm{Co}}$ is the **stabilizer of
    the polarization** $h_{Co}$ within $O(T_{En})$, further constrained by the
    horizontal folding involution $\theta$"
  - GOAL.md line 79: "theta must act on Lambda_K3 such that its invariant and
    coinvariant sublattices are correctly identified"
  - GOAL.md line 85: "Construct the 22x22 matrix theta"
  - GOAL.md Task 6.1: "Verify that the involution $\theta$ on $\Lambda_{K3}$ has the
    expected invariant and coinvariant sublattices"
- GOAL linkage: Gate for T-3011

## Objective

Gate the involution primitives by checking order, isometry, eigensublattice invariants,
transported vectors, and discriminant-image consistency against the standard fixtures.
This gate verifies:

1. **Order verification**: The involution matrix from T-0008 must have order 2 (θ² = I)
2. **Isometry verification**: The involution must preserve the bilinear form on Λ_K3
3. **Eigensublattice invariants**: The +1 eigenspace (invariant sublattice) must have
   rank 11 and signature (1,10); the -1 eigenspace (coinvariant) must have rank 11 and
   signature (2,9)
4. **Discriminant image consistency**: The action on the discriminant group A_Λ must
   match the expected induced action
5. **Transport verification**: Polarization transport from T-0008 must produce the
   expected vector in the invariant sublattice

## Parent Sufficiency Map

Blocks involution-dependent claims until the activated involution primitives are exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0008, T-1001, T-1002, T-1004
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Criteria

1. **Order-2 verification**: θ² must equal the identity matrix
2. **Isometry verification**: For all v, w ∈ Λ_K3, B(θv, θw) = B(v, w)
3. **Eigenspace ranks**: dim(L_+) = 11, dim(L_-) = 11
4. **Eigenspace signatures**: L_+ has signature (1,10), L_- has signature (2,9)
5. **Discriminant action**: The induced action on A_Λ must match the expected involution
6. **Polarization transport**: The transported polarization vector must lie in L_+ with
   correct square length

## Non-Goals

1. **No new involution construction**: This is a gate, uses T-0008 as black box
2. **No full automorphism group**: Does not compute O(Λ_K3)
3. **No proof of uniqueness**: Only verifies consistency with fixtures

## Allowed Dependencies

- **Prerequisite tasks**: T-0008 (involution primitives), T-1001 (standard lattices),
  T-1002 (Coble invariants), T-1004 (embedding fixtures)
- **Local sources** (must cite):
  - tasks/goal_expansion.md — task ordering
  - STATE_MACHINE.md — tier semantics

## Required Conventions

1. **Matrix convention**: θ is a 22×22 integer matrix in the standard basis of Λ_K3
2. **Eigenspace convention**: L_+ = {v | θv = v}, L_- = {v | θv = -v}
3. **Failure format**: Report as `gate_fail: involution - <mismatch-details>`

## Failure Conditions

1. **Order > 2**: If θ² ≠ I, gate fails with `fail_order`
2. **Not isometry**: If bilinear form not preserved, fails with `fail_isometry`
3. **Wrong eigenspace rank**: If ranks differ from 11, fails with `fail_eigenspace_rank`
4. **Wrong signature**: If signatures differ from (1,10)/(2,9), fails with
   `fail_signature`
5. **Discriminant mismatch**: If induced action differs, fails with
   `fail_discriminant_action`
