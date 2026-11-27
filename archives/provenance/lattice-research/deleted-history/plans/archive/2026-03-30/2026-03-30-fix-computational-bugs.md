# Plan: Fix Computational Bugs in Task 1.2 and 1.3

**Created**: 2026-03-30 **Status**: Active

## Context

Prover verification discovered 2 computational bugs:
1. Task 1.2: T_Co Gram diagonal has `[-1,-1]` instead of `[-2,-2]` (det 1024 vs -2048)
2. Task 1.3: T_Co from embedding may not be isometric to correct T_Co (needs
   discriminant form verification)

Both bugs are isolated to their respective scripts.
Most downstream work uses correct T_Co from `coble_geometry.sage`.

## Goal

Fix both computational bugs so all computation scripts produce mathematically correct
results.

## Phase 1 — Fix Task 1.2 T_Co Gram matrix bug

- [x] Read `computations/task1_2_gram_matrices.sage` (or task1_2_fixed.sage)
- [x] Identify where orthogonal complement is computed
- [x] Root cause: embedding used pairs `(1,1)` producing norm -4 in
  `diagonal_matrix([-2]*16)`
- [x] Fix the computation to produce correct diagonal
  `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]`
- [x] Verify determinant is -2048
- [x] Regenerate output file
- [x] Delegate to Prover subagent to verify fix

**Result**: FIXED. Changed line 110 and embedding construction (lines 127-133). T_Co
Gram now correct.

## Phase 2 — Verify Task 1.3 T_Co embedding

- [x] Delegate to Prover: verify discriminant form of computed T_Co matches expected q_T
- [x] Note: Signature + determinant do NOT imply isometry for indefinite lattices
- [x] Discriminant form matches exactly (|A_T| = 2048, Brown invariant correct, q_T ≅
  -q_S)
- [x] Conclusion: Bug 2 is NOT A BUG - non-diagonal Gram is different basis
  representation

**Result**: NOT A BUG. Discriminant form verification confirms computed T_Co is correct.

## Phase 3 — Update BUGS.md

- [x] Mark Bug 1 as FIXED
- [x] Add Bug 2 entry as NOT A BUG with discriminant form verification results

**Status**: Complete

## Verification

Success: Both bugs resolved, all computation scripts produce correct results, Prover
verification passes.
