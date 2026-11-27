# Task 5.1 theta verification from the primitive decomposition

## Goal

- Current defect/state: commit `480f35d` verified an exact primitive `S_Co` embedding,
  computed the true orthogonal complement, and stopped before constructing `θ`.
- Target state: extend that exact slice to define `θ = (+1)|_T \oplus (-1)|_S` on the
  verified decomposition and prove that the induced matrix is integral and lies in
  `O(\Lambda_{K3})`.
- Why this mattered: the corrected Task 5.1 route had reached the decisive remaining
  gate. This plan is now complete because the sign action preserves the glued overlattice
  exactly.

## Constraints

- Required:
  - Treat `audit/task5_1_route_reset.md` as the canonical route order.
  - Reuse the verified primitive/complement construction in
    `computations/task5_1_involution.sage`; do not reintroduce the disproved eigenspace
    splice route.
  - Keep all arithmetic exact.
- Forbidden:
  - No guessed `θ` from ad hoc eigenspace bases.
  - No claims that `θ` is valid unless the script verifies integrality and `θ^T G θ = G`
    exactly.
  - No broad cleanup drift beyond directive updates required by the completed primitive
    gate.

## Scope

- Included targets:
  - `PLAN.md`
  - `GAPS.md`
  - `plans/2026-03-28-task5_1-theta-verification.md`
  - `computations/task5_1_involution.sage`
  - `justfile`
  - `computations/task5_1_theta_output.txt`
  - `computations/task5_1_theta_results.txt`
- Excluded for this slice:
  - `GOAL.md`
  - broad literature rewrites
  - Lean formalization
  - CARAT integration unless theta verification explicitly reduces to a finite
    positive-definite subproblem

## Phase 0: Repoint directives after the completed primitive gate

Goal: make the active docs describe the current post-gate state exactly.

- Location: `PLAN.md`, `GAPS.md`, this plan file
- Description:
  - mark the primitive/complement gate as completed;
  - state that the next Task 5.1 slice is theta verification from the verified
    decomposition.
- Dependencies: none.
- Acceptance criteria: `PLAN.md` and `GAPS.md` no longer say the primitive gate is still
  pending or blocked.
- Validation: inspect
  `git diff -- PLAN.md GAPS.md plans/2026-03-28-task5_1-theta-verification.md`.

## Phase 1: Construct theta from the verified decomposition

Goal: define the sign action on the actual computed `S` and `T` and test whether it is
an integral ambient automorphism.

- Location: `computations/task5_1_involution.sage`
- Description:
  - extend the existing primitive/complement script with a theta phase;
  - build the ambient linear map that acts by `-I` on `S` and `+I` on `T`;
  - verify exact integrality, involutivity, and isometry.
- Dependencies: Phase 0.
- Acceptance criteria:
  - the script checks `θ^2 = I`, integrality in the ambient basis, `θ^T G θ = G`,
    `θ|_S = -I`, and `θ|_T = +I`;
  - the script hard-fails if any check fails.
- Validation: `just task5_1-theta`.

## Phase 2: Publish a narrow Task 5.1 theta interface

Goal: expose the new exact theta check without obscuring the primitive-only gate.

- Location: `justfile`, `computations/task5_1_theta_output.txt`,
  `computations/task5_1_theta_results.txt`
- Description:
  - add dedicated `just` recipes for the theta verification slice and its results file;
  - write a concise exact results artifact recording pass/fail data.
- Dependencies: Phase 1.
- Acceptance criteria:
  - `just task5_1-theta` runs the theta phase;
  - `just task5_1-theta-results` prints the theta results file;
  - the primitive-only recipes still work.
- Validation:
  - `just task5_1-primitive`
  - `just task5_1-primitive-results`
  - `just task5_1-theta`
  - `just task5_1-theta-results`

## System-Level Validation

- `PLAN.md` moves this file into the completed-plan list.
- `GAPS.md` no longer names theta integrality/isometry as the next exact Task 5.1 gap.
- `just task5_1-primitive` still reproduces the completed gate.
- `just task5_1-theta` now proves the exact involution on the glued ambient lattice.

## Risks / Rollback

- Risks:
  - the sign action may preserve the rational decomposition but fail to preserve the
    glued overlattice integrally;
  - a superficial success check could silently test only the split model rather than the
    actual glued ambient basis.
- Mitigations:
  - perform every theta check in the ambient basis produced by the current glued model;
  - keep the primitive-only phase intact so failures remain reproducible.
- Rollback path:
  - if the theta phase proves too entangled, keep the verified primitive/complement gate
    and revert only the added theta layer in a follow-up commit.

## Stop Rules

- Do not treat Brown invariant agreement alone as proof that `θ` preserves the
  overlattice.
- Do not export `θ` as a valid Task 5.1 result unless integrality and isometry checks
  pass.
- If the sign action is rational but not integral, stop and record that as the new
  blocker instead of papering over it.

## Execution Progress

### Phase 0

- [x] Repoint `PLAN.md` to the theta-verification thread
- [x] Update `GAPS.md` so the primitive gate is recorded as complete

### Phase 1

- [x] Add the theta verification phase to `computations/task5_1_involution.sage`
- [x] Hard-fail on nonintegral or nonisometric theta output

### Phase 2

- [x] Add `just task5_1-theta`
- [x] Add `just task5_1-theta-results`
- [x] Write checked theta output/result artifacts

### Quality Gates

- [x] Directive files reflect the post-gate state
- [x] Theta checks run in the actual glued ambient basis
- [x] Primitive-only and theta recipes both verify cleanly
