# Task 5.1 primitive embedding and complement gate

## Goal

- Current defect/state: the repo has a canonical reset note for Task 5.1, but the live
  computation entrypoints and some live prose still reflect the disproved direct `θ`
  construction as if it were current or solved.
- Target state: the active work thread is reduced to one exact executable slice — build
  and verify a primitive `S_Co \hookrightarrow \Lambda_{K3}` candidate, compute the true
  orthogonal complement, and stop before any new `θ` reconstruction.
- Why this matters: the next mathematical step must be auditable and exact, and future
  agents should no longer be steered by stale solved-language or invalid route comments.

## Constraints

- Required:
  - Treat `audit/task5_1_route_reset.md` as the canonical Task 5.1 route.
  - Keep `REFERENCES.md`, `audit/literature_claim_map.md`, and
    `audit/carat_capability_audit.md` as the citation/constraint layer.
  - Reuse existing exact Sage helpers where they are correct; prefer exact arithmetic
    throughout.
- Forbidden:
  - No new `θ` matrix construction before primitive embedding and orthogonal complement
    are verified.
  - No broad cleanup drift beyond stale live prose/plan text that directly misstates the
    active route.
  - No claims that Task 5.1 or Task 6.1 is solved in current live docs.

## Scope

- Included targets:
  - `PLAN.md`
  - `GAPS.md`
  - `plans/2026-03-28-task5_1-primitive-complement.md`
  - `audit/final_audit_report.md`
  - `logs/research-log.md`
- Deferred to the execution thread after this plan update:
  - `computations/task1_3_embeddings_fixed.sage`
  - `computations/task5_1_involution.sage`
  - `computations/coble_geometry.sage`
  - `justfile`

## Phase 0: Correct the live narrative

Goal: remove the highest-confusion live prose that still advertises the disproved route
or solved status.

- Location: `audit/final_audit_report.md`, `logs/research-log.md`, `GAPS.md`
- Description:
  - mark the old audit report as superseded by the Task 5.1 reset;
  - rewrite the live Task 5.1 / Task 6.1 log takeaways so the blocked state is explicit;
  - remove stale gap bullets already completed by `59fe521`.
- Dependencies: none.
- Acceptance criteria: no live prose file claims Task 5.1 is solved or says the current
  route already produced a valid `θ \in O(\Lambda_{K3})`.
- Validation: inspect `git diff` for the three files.

## Phase 1: Repoint the active thread to the exact gate

Goal: make the plan index and gaps name the next executable slice precisely.

- Location: `PLAN.md`, `GAPS.md`, this plan file
- Description:
  - switch the active plan from prose cleanup to primitive embedding / complement;
  - record the exact acceptance criteria from the delegated audit: primitive embedding,
    orthogonal complement, determinant/discriminant compatibility, and no `θ` export.
- Dependencies: Phase 0.
- Acceptance criteria: the active thread, immediate next targets, and stop rules all
  name the same Task 5.1 gate.
- Validation: inspect `PLAN.md`, `GAPS.md`, and this file for consistent wording.

## Phase 2: Prepare the implementation handoff

Goal: reduce the next code pass to a narrow, verifiable implementation slice.

- Location: this plan file
- Description:
  - record the intended file set for the next code change;
  - record the delegated acceptance criteria and exact `just` commands the code pass
    must satisfy.
- Dependencies: Phase 1.
- Acceptance criteria: a future implementation pass can work from this file without
  rediscovering the route or acceptance checks.
- Validation: inspect this file and compare against the delegated Task 5.1 audit.

## Implementation handoff for the next code slice

- Primary files:
  - `computations/task1_3_embeddings_fixed.sage`
  - `computations/task5_1_involution.sage`
  - `justfile`
- Optional helper extraction only if needed to avoid duplication:
  - `computations/coble_geometry.sage`
- Required code outcomes:
  - dedicated Task 5.1 primitive/complement entrypoint;
  - hard failure if primitivity, determinant, signature, cross-pairing, or discriminant
    compatibility fails;
  - no export of `theta_matrix.sage` or `task5_1_results.txt` from the disproved route.
- Acceptance criteria for that code pass:
  - exact Gram match for the embedded `S_Co`;
  - computed complement rank `11`, signature `(2,9)`, zero cross-pairing, and
    `|det(T)| = 2048`;
  - discriminant-group compatibility checked on the actual computed complement;
  - `just task5_1-primitive` and `just task5_1-primitive-results` exist and run the new
    gate.
- Stop rule for the code pass:
  - if the current saturation helper does not certify primitivity exactly, stop and
    replace the primitivity check before continuing.

## System-Level Validation

- The active plan index points to this file.
- `GAPS.md` no longer lists already-completed debris deletion as open work.
- `audit/final_audit_report.md` and `logs/research-log.md` no longer state that Task 5.1
  is solved.

## Risks / Rollback

- Risks:
  - over-editing historical log text and losing useful chronology;
  - keeping contradictory audit claims alive by only adding caveats instead of changing
    the operative takeaway.
- Mitigations:
  - preserve chronology but insert supersession language and corrected conclusions;
  - keep the implementation slice explicit and narrow.
- Rollback path:
  - restore any over-pruned prose from git history in a follow-up commit if audit shows
    lost evidence.

## Stop Rules

- Do not edit computation files in this planning/prose pass.
- Do not claim the primitive embedding gate is complete without exact verification
  outputs.
- Do not treat historical output files as canonical proof of current status.

## Execution Progress

### Phase 0

- [x] Correct stale live prose in `audit/final_audit_report.md`
- [x] Correct stale live prose in `logs/research-log.md`
- [x] Remove stale completed-work bullets from `GAPS.md`

### Phase 1

- [x] Repoint `PLAN.md` to this active thread
- [x] Align `GAPS.md` immediate next targets with the primitive/complement gate
- [x] Keep the old prose-cleanup plan as a completed prior thread

### Phase 2

- [x] Record the implementation handoff and acceptance checks in this file

### Quality Gates

- [x] Live prose no longer advertises the invalid direct `θ` route as solved
- [x] Active plan names one exact Task 5.1 gate
- [x] Next code pass has explicit acceptance criteria and stop rules
