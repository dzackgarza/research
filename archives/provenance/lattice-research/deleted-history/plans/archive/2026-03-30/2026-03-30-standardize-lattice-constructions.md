# Plan: Standardize Lattice Constructions

**Created**: 2026-03-30 **Status**: Active

## Context

User correction identified that agents have been constructing lattices inconsistently,
leading to disagreements over Gram matrices.
The core issue: lattices like T_Co are being constructed as ad-hoc diagonal matrices
instead of canonical direct sums.

**Critical example**: T_Co should be `<2> ⊕ U ⊕ E8(-1)`, not
`diagonal_matrix([2,2,-2,...,-2])`.

## Goals

1. Update `coble_geometry.sage` to use canonical direct sum constructions
2. Audit all computation scripts for non-standard constructions
3. Update verification process to include standardization review
4. Verify that standardized constructions produce consistent results

## Phase 1: Update coble_geometry.sage

**Status**: Pending

Update canonical lattice constructors to use direct sums:

- `S_Co()`: `<2> ⊕ <-2>^10` (currently uses diagonal_matrix)
- `T_Co()`: `<2> ⊕ U ⊕ E8(-1)` (currently uses diagonal_matrix)
- `T_En()`: `<2>^2 ⊕ <-2>^8` (currently uses diagonal_matrix)
- `Lambda_K3()`: `U^3 ⊕ E8(-1)^2` (currently uses block_diagonal_matrix, should use
  direct_sum)

Add helper constructors:
- `rank_one(n)`: Rank-1 lattice `<n>`

**Acceptance criteria**:
- All lattices constructed via `IntegralLattice.direct_sum()`
- Gram matrices match expected structure
- Signature, determinant, discriminant group invariants unchanged

## Phase 2: Audit existing scripts

**Status**: Pending

Search for non-standard constructions:
- `grep -r "diagonal_matrix" computations/*.sage`
- `grep -r "IntegralLattice(matrix" computations/*.sage`
- Identify scripts that construct lattices directly instead of using
  `coble_geometry.sage`

**Acceptance criteria**:
- List of all scripts with non-standard constructions
- Assessment of which need updating vs which are intentionally custom

## Phase 3: Update verification process

**Status**: Pending

Add standardization review to `audit/verification_process.md`:
- Phase 0.5: Standardization Review (before Research phase)
- Check that verification plan uses canonical constructors
- Check that Agent A/B implementations use standard methods
- Reject plans that propose custom lattice constructions without justification

**Acceptance criteria**:
- `verification_process.md` updated with standardization review phase
- Checklist includes lattice construction standards

## Phase 4: Verification

**Status**: Pending

Run standardized scripts and verify:
- T_Co signature still (2,9)
- T_Co determinant still -2048
- T_Co discriminant group still (Z/2Z)^11
- All existing verification records still valid

**Acceptance criteria**:
- All scripts run successfully with standardized constructors
- No changes to mathematical results
- Gram matrices may differ (basis change) but invariants match

## Notes

- This is a refactoring task, not new mathematical work
- Focus on standardization, not verification
- Gram matrix changes are expected (different basis), invariants must match
- Document any scripts that legitimately need custom constructions
