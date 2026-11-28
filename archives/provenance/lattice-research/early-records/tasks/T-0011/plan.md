# Plan

## Goal

- Current defect/state: `src/coble_geometry_foundation.sage` carries verified
  quarantine indicators and cannot legally serve as shared infrastructure.
- Target state: either a fully re-admitted exact primitive surface with explicit trust
  limits, or a retained quarantine decision with downstream dependencies kept blocked.
- Why this matters: every Wave A lattice task depends directly or transitively on this
  file.

## Pre-Audit Answers

- Exact statement/object/output: attempt admission only of the fixed candidate surface
  recorded in `tasks/T-0011/admission_target.md`, or retain quarantine with an explicit
  non-admission record.
- GOAL justification: `GOAL.md:15-19` plus the Tier-0 routing in
  `tasks/goal_expansion.md`.
- Conventions file: `tasks/T-0011/conventions.md`.
- Deliverable type: infrastructure prerequisite.
- Objective pass/fail criteria: `tasks/T-0011/task.md` Acceptance Criteria and Failure
  Conditions.
- Required prerequisites: exact backend and policy sources listed in
  `tasks/T-0011/dependencies.md`.
- Local availability and auditability: external backend expectations and repo-local
  assumptions are fixed in `tasks/T-0011/dependencies.md` and
  `tasks/T-0011/assumptions.md`; if any required backend cannot be exercised exactly,
  the task must stop in replan/quarantine rather than simulate.
- Hidden major subproblem: fixed by freezing the candidate primitive inventory and
  exclusions before implementation; any primitive outside that inventory requires
  replan.
- Exact verification: only via the replay contract in `tasks/T-0011/replay_contract.md`
  plus later self-check/audit bundles.
- Files that may be changed: `tasks/T-0011/**`,
  `src/coble_geometry_foundation.sage`, and the single replay-binding recipe in
  `justfile` named by the replay contract.
- Independent later attack: fixed in `tasks/T-0011/attack_surface.md`.
- Task failure: defined in `tasks/T-0011/task.md` Failure Conditions.

## Phases

- Phase 0: use the frozen candidate inventory in `tasks/T-0011/admission_target.md` to
  map each admitted primitive and each excluded primitive to its mature backend or
  exclusion rationale.
- Phase 1: delegate isolated rewrite workers to replace or remove poisoned shared
  primitives without polishing the bad implementations.
- Phase 2: delegate a non-author self-check over scope, dependency pinning, artifact
  completeness, and replay route.
- Phase 3: delegate an adversarial audit that attacks the strongest admitted shared-base
  claim and verifies the trusted-base admission record.

## Required Outputs

- a rewritten or reduced foundation file produced only in isolated worktrees,
- a replayable `just t0011-foundation-replay` route backed by the task-local harness
  named in `tasks/T-0011/replay_contract.md`,
- a task-local replay certificate at
  `tasks/T-0011/outcomes/foundation_replay_certificate.md`,
- explicit trusted-base admission artifact,
- downstream task list affected by the admission decision.

## Stop Rules

- Do not proceed to implementation until pre-audit answers all twelve checklist items.
- Do not preserve poisoned helper APIs merely for compatibility.
- Do not reuse the foundation file downstream unless this task reaches acceptance-bundle
  assembly with complete artifacts.
- Do not broaden the candidate admitted surface beyond
  `tasks/T-0011/admission_target.md` without replan.
