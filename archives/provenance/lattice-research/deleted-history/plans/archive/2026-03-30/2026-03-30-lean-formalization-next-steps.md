# Plan: Lean Formalization Next Steps

**Created**: 2026-03-30 **Status**: Active

## Context

Repo now has:
- 10 solved proof notes covering all 20 computation scripts
- 3 Lean files with theorem statements and `sorry` placeholders:
  - `IsotropicPlanes.lean`: unique isotropic plane orbit (task3_2)
  - `NodeCriteria.lean`: Hessian rank bound (complete proof)
  - `Basic.lean`: stub file

All computational verification is complete.
Lean formalization remains secondary per GOAL.md Priority 4, but the existing `sorry`
placeholders represent concrete formalization targets.

## Goal

Fill `sorry` placeholders in existing Lean files with formal proofs, starting with the
most tractable targets that have complete computational verification.

## Blocker: Lean toolchain not available

Lean/elan is not installed or not on PATH. Cannot build or verify Lean code.

**Status**: Lean formalization is blocked until toolchain is available.
Per GOAL.md Priority 4, formalization is secondary to literature spine and computational
verification, both of which are complete.

## Phase 1 — Assess formalization readiness (BLOCKED)

- [ ] Review `IsotropicPlanes.lean` theorem statements against
  `proofs/solved/task3_2_isotropic_planes.md`
- [ ] Identify which computational facts are already in mathlib vs need custom
  formalization
- [ ] Check if Nikulin's surjectivity theorem (Prop 1.5.2) has any mathlib analogue
- [ ] Note: task3_2 orbit uniqueness claim is UNVERIFIED (orbit computation never
  performed)

## Phase 2 — Formalize tractable lemmas first

Priority order (easiest to hardest):
1. Basic lattice definitions (T_Co bilinear form, isotropic vectors)
2. Discriminant group computation (A_T_Co ≅ (ℤ/2ℤ)^11)
3. Primitive plane enumeration (15 planes found computationally)
4. Orbit computation via GAP (not yet performed - task3_2 claim unverified)
5. Nikulin surjectivity application (requires mathlib search or custom proof)

## Phase 3 — Verify build and commit

- [ ] Run `lake build` to verify all proofs typecheck
- [ ] Commit each completed lemma separately with descriptive messages
- [ ] Update this plan with progress

## Verification

Success: All `sorry` placeholders in `IsotropicPlanes.lean` replaced with formal proofs
that typecheck under `lake build`.

## Notes

- NodeCriteria.lean already has a complete proof (no `sorry` placeholders)
- Basic.lean is a stub and can be populated with shared definitions as needed
- Lean formalization is secondary to literature spine per GOAL.md, but existing `sorry`
  placeholders represent concrete technical debt
