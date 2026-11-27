# Plan: Fix Arf Invariant Contamination and Mathematical Nonsense

**Created**: 2026-03-30 **Status**: Active **Priority**: CRITICAL

## Context

Multiple mathematical errors discovered:
1. "Arf invariant" used throughout task3_2 work - concept doesn't exist over Z
2. False claim "signature + det + disc form determines isometry class" in
   lattice_construction_standards.md
3. Verification process failed to catch mathematical nonsense
4. task3_2 orbit uniqueness claim is unverified (never actually computed orbits)

## Phase 1: Remove Arf Invariant Contamination

**Status**: Pending

Files contaminated:
- `computations/task3_2_isotropic_planes.sage` (10 occurrences)
- `proofs/solved/task3_2_isotropic_planes.md` (5 occurrences)
- `audit/verification_process.md` (1 occurrence)
- `CHANGELOG.md` (1 occurrence)
- `plans/2026-03-30-lean-formalization-next-steps.md` (2 occurrences)

**Actions:**
- Remove all "Arf invariant" references
- Replace with correct terminology: "orbit computation via GAP"
- Mark task3_2 orbit uniqueness claim as UNVERIFIED until proper computation

**Acceptance criteria:**
- Zero occurrences of "Arf" in codebase
- All references replaced with correct orbit computation language
- No false mathematical claims remain

## Phase 2: Fix False Isometry Claim

**Status**: Pending

**File**: `audit/lattice_construction_standards.md`

**False claim**: "For indefinite lattices, signature + det + disc form determines
isometry class"

**Action:**
- Remove the `lattices_isometric()` function entirely
- Add warning: "Lattice isometry is subtle, use literature-specific criteria"
- Note: Nikulin's classification requires additional data beyond these invariants

**Acceptance criteria:**
- No false isometry claims in standards document
- Clear warning about isometry complexity

## Phase 3: Properly Compute task3_2 Orbits

**Status**: Pending

**Current state**: Code computes meaningless "Arf invariant = 0" for all planes, claims
single orbit without actually computing orbits

**Correct approach:**
1. Use GAP to compute O(q_T) (orthogonal group of discriminant form)
2. Use GAP's orbit functions on the 15 primitive isotropic plane images
3. Count orbits
4. Report actual orbit structure

**Delegation**: Delegate to Prover subagent with explicit instructions:
- Use GAP, not custom code
- Compute orbits of group action on finite set
- No "invariants" - just direct orbit computation

**Acceptance criteria:**
- Actual orbit count computed via GAP
- Code uses standard GAP orbit functions
- Verification note updated with correct reasoning

## Phase 4: Fix Verification Process

**Status**: Pending

**File**: `audit/verification_process.md`

**Add Phase 0: Mathematical Validity Review**

Before any implementation, check:
- Is every concept used actually defined in this setting?
- Does the proposed method match literature techniques?
- Are we invoking theorems that don't apply?
- Mandatory literature check for any "invariant" or "classification theorem"

**Enhance Audit Phase:**
- Mathematical sense check: does the reasoning use concepts correctly?
- Literature alignment: does this match how the literature solves this problem?
- Concept applicability: is this invariant/theorem defined in our setting?
- Reject any work that invokes undefined concepts

**Acceptance criteria:**
- Phase 0 added to verification process
- Audit phase includes mathematical validity checks
- Clear rejection criteria for mathematical nonsense

## Phase 5: Document Failure

**Status**: Pending

Create `audit/arf_invariant_failure.md` documenting:
- What went wrong (Arf invariant over Z)
- How it propagated (no mathematical validity check)
- Why verification failed (focused on code, not mathematics)
- Process fixes implemented

**Acceptance criteria:**
- Failure documented for future reference
- Root cause analysis complete
- Process improvements linked

## Execution Order

1. Phase 4 (fix process) - prevent future failures
2. Phase 1 (remove contamination) - clean up existing mess
3. Phase 2 (fix false claim) - remove other mathematical errors
4. Phase 3 (proper computation) - actually verify the claim
5. Phase 5 (document) - record what happened

## Notes

- This is CRITICAL priority - mathematical correctness failure
- All "verified" task3_2 work is invalid until Phase 3 completes
- Verification process failed catastrophically
- Must fix process before trusting any future verification work
