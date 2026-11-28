# Task T-0011: Foundation Library Decontamination And Trusted-Base Admission

## Status

Selected as a natural-extension prerequisite on 2026-04-03. TASK_SPECIFICATION in
progress; this task exists because `src/coble_geometry_foundation.sage` is
blocked for downstream dependency use until a separate decontamination and admission
process completes.

## Tier

Tier 0.

## Origin

- GOAL.md lines 15-19 define the lattice objects used across Tasks 1.2, 1.3, and 5.1.
- `tasks/goal_expansion.md:36-58` routes lattice work through mature exact backends and
  forbids hand-rolled replacements for shared primitives.
- `STATE_MACHINE.md:127-137` requires trusted-base admission to be a separate
  high-burden process.
- `STATE_MACHINE.md:1128-1129` forbids reuse of quarantined artifacts until a separate
  decontamination audit clears them.
- `AGENTS.md:26` requires excision and delegated rewrite of poisoned shared code rather
  than polishing audited-bad code.

## Objective

Decontaminate `src/coble_geometry_foundation.sage` against the fixed candidate
admission target recorded in `tasks/T-0011/admission_target.md` and, if that exact
candidate surface survives the full state-machine workflow, emit the trusted-base
admission record that defines what future tasks may assume from the admitted version.

The candidate admitted surface must:
- expose only object-level exact primitives for canonical lattice objects and exact
  transforms,
- align its construction and computation paths to the mature backends documented in the
  local theory notes,
- replace task-shaped helpers and bounded-search stand-ins with backend-backed exact
  operations or remove them from the shared base,
- use a common vocabulary in which mathematical objects are nouns and operations are
  verbs or methods on those objects.

## Deliverable Type

infrastructure prerequisite

## Acceptance Criteria

1. **Excised poisoned surface**: every quarantine indicator already identified in the
   current foundation file is either removed from the admitted shared surface or
   replaced by a backend-backed exact primitive within this task's isolated worktree.

2. **Shared-boundary compliance**: the admitted shared API exposes only constructors,
   coercions, exact predicates, exact transforms, and invariant extractors; task-shaped
   `assert_*` / `verify_*` helpers do not remain in the admitted shared surface.

3. **Backend alignment**: each admitted primitive cites and uses the mature exact
   backend routed by the local theory docs:
   - Oscar/Hecke for lattice construction, genus data, embeddings, invariant and
     coinvariant lattices, and discriminant-side lattice operations,
   - GAP for finite orbit and stabilizer computations,
   - Indefinite.jl and/or `buildings.sage` for indefinite isotropic orbit problems,
   - CARAT only for finite positive-definite auxiliary group problems when explicitly in
     scope.

4. **Object/method vocabulary**: shared primitives operate on explicit mathematical
   objects rather than raw attribute-probed containers; contract assertions are encoded
   as reusable functions in gate tasks, not hidden inside the shared base.

5. **Trusted-base admission artifact**: the task emits the admission record required by
   `STATE_MACHINE.md:131-137`, stating exact admitted item, allowed future scope,
   justification for trust, validity limits, theorem burden moved into the trusted base,
   prior admissions relied on, anti-laundering rationale, and affected downstream tasks.

6. **Replay contract**: the admitted candidate surface is checked through the exact
   replay route fixed in `tasks/T-0011/replay_contract.md`, with emitted certificate
   artifacts in the task-local outcomes directory.

7. **Full machine passage**: no downstream task may reuse the file unless this task
   produces a complete pre-audit bundle, isolated implementation artifacts, non-author
   self-check, independent adversarial audit, acceptance bundle, and archive bundle.

## Non-Goals

- Does not discharge any GOAL.md theorem-level burden directly.
- Does not prove downstream lattice claims for `T-0001`, `T-0002`, `T-0003`, or
  `T-0008`.
- Does not allow ordinary downstream tasks to absorb shared-base repair implicitly.
- Does not preserve poisoned helper APIs for compatibility if they violate the shared
  boundary.

## Allowed Dependencies

- Prerequisite tasks: none; this is the prerequisite.
- Local sources:
  - src/coble_geometry_foundation.sage
  - AGENTS.md
  - STATE_MACHINE.md
  - PROOF_AUDITING.md
  - theory/library_integration.md
  - theory/oscar_lattices.md
  - theory/gap_orbits.md
  - theory/indefinite_jl.md
  - theory/buildings.md
  - tasks/goal_expansion.md
- justfile
- tasks/T-0011/conventions.md
- tasks/T-0011/admission_target.md
- tasks/T-0011/attack_surface.md
- tasks/T-0011/replay_contract.md

## Required Conventions

- `tasks/T-0011/conventions.md` is the conventions file for this task.
- Shared primitives expose mathematical nouns and verbs, not opaque task verdicts.
- Exact backend usage must be documented at the primitive boundary.
- Reusable contract assertions belong in gate tasks, not the admitted shared base.
- All computation and replay routes go through `just`.

## Failure Conditions

1. If any bounded enumeration, fail-open exception path, print-theater proof surface,
   raw ad-hoc lattice construction, or task-shaped verdict helper survives in the
   admitted shared surface → fail.
2. If any admitted primitive relies on undocumented hand-rolled mathematics where a
   mature exact backend is routed by the theory docs → fail.
3. If the task cannot emit the trusted-base admission record required by
   `STATE_MACHINE.md:131-137` together with the theorem-burden and anti-laundering
   statements required by the trusted-base admission rules → fail.
4. If the implemented shared surface differs from the frozen candidate inventory in
   `tasks/T-0011/admission_target.md` without a prior replan → fail.
5. If implementation, self-check, or audit occurs outside isolated worktrees with the
   full artifact bundle → fail.
6. If any downstream task reuses the file before this prerequisite is accepted → fail.

## Parent Sufficiency Map

This task is a prerequisite for every task whose dependency cone begins at the shared
foundation file, including `T-0001`, `T-0002`, `T-0003`, `T-0005`, `T-0006`, and
`T-0008`, and therefore their downstream gates and Tier-3 applications.

It legalizes no downstream mathematical claim by itself; it only establishes whether the
shared lattice base may be reused at all.
