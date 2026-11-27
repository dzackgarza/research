# Task 5.1 recovery, prose integration, and cleanup

## Goal

- Current defect/state: the literature-first reset is in place, but the repo still has
  older proof prose that overstates what computations establish, Task 5.1 still lacks
  the first primitive-embedding/complement implementation step, and tracked debris
  remains in the tree.
- Target state: the active prose points back to the literature spine and claim notes,
  obvious tracked debris is removed, and the Task 5.1 follow-up work is reduced to a
  concrete primitive-embedding/complement execution thread.
- Why this matters: the repo should stop repeating unsupported ambient claims and should
  advance the blocked lattice problem only through the corrected route.

## Constraints

- Required:
  - Keep `REFERENCES.md` and the three claim notes as the canonical citation layer.
  - Treat computations as supporting evidence or exact worked examples unless they prove
    a genuinely local claim.
  - Use exact arithmetic and keep Task 5.1 on the primitive-embedding/complement route.
- Forbidden:
  - Reinstating the disproved ad hoc θ construction.
  - Claiming moduli, Torelli, or KSBA background as if the repo newly proved it.
  - Mixing broad debris cleanup into mathematical edits without explicit triage.

## Scope

- Included targets:
  - `PLAN.md`
  - `GAPS.md`
  - `plans/2026-03-28-task5_1-prose-cleanup.md`
  - `proofs/solved/task3_2_isotropic_planes.md`
  - `proofs/solved/task6_1_slc_stability.md`
  - tracked debris explicitly called out in the current work thread
- Excluded for this thread:
  - full Task 5.1 involution reconstruction
  - broad historical-log rewrites
  - new Lean formalization work

## Phase 0: Cleanup the explicit debris targets

Goal: remove the accidental extracted-text artifact and root-level `.orig` leftovers
that no longer belong in the tracked tree.

- Location: `audit/dolgachev_kondo_extracted.txt`, root `*.orig`
- Description: delete the accidental extracted text file and the tracked `.orig` backups
  already superseded by canonical files.
- Dependencies: none.
- Acceptance criteria: the tracked debris files disappear from `git status` as live repo
  content.
- Validation: inspect `git status --short` after deletion.

## Phase 1: Weave the literature notes into main proof prose

Goal: make the long-form proof notes cite the canonical literature/claim-map layer
before leaning on local computation.

- Location: `proofs/solved/task3_2_isotropic_planes.md`,
  `proofs/solved/task6_1_slc_stability.md`
- Description:
  - add explicit references to `REFERENCES.md` and the claim notes where those files use
    standard Coble/K3/moduli background;
  - tighten statements so the repo computations are described as verification within the
    literature-backed framework, not as replacement proofs of the ambient moduli theory.
- Dependencies: Phase 0 optional but independent.
- Acceptance criteria: the main proof prose clearly distinguishes cited background from
  repo-specific computational evidence.
- Validation: inspect the edited sections and `git diff` for those files.

## Phase 2: Prepare the first executable Task 5.1 recovery step

Goal: convert the route reset into a concrete next computation target.

- Location: `GAPS.md`, `PLAN.md`, this plan file
- Description:
  - record the immediate primitive-embedding/complement subproblem as the active blocked
    task;
  - state the stop rule that no new θ reconstruction happens before the embedding and
    orthogonal complement are verified.
- Dependencies: claim-note/prose alignment from Phase 1.
- Acceptance criteria: the active plan and gap files point to one concrete Task 5.1 next
  step rather than a generic “fix Task 5.1” placeholder.
- Validation: inspect `PLAN.md`, `GAPS.md`, and this plan for consistent wording.

## System-Level Validation

- The active plan index points to this file.
- No edited proof file presents standard background as a new repo theorem.
- The cleanup step removes the accidental extracted-text artifact from tracked content.

## Risks / Rollback

- Risks:
  - over-editing solved proof notes and losing specific computational claims;
  - deleting a file that still has a live documentation role.
- Mitigations:
  - keep computational outputs and script references intact;
  - remove only debris explicitly superseded by canonical files or called out by the
    user.
- Rollback path:
  - restore any deleted or rewritten prose from git history with a follow-up commit if
    an audit shows lost value.

## Stop Rules

- Do not attempt a new Task 5.1 θ matrix before the primitive embedding and orthogonal
  complement are explicitly verified.
- Do not generalize computational examples into ambient literature claims.
- Do not broaden cleanup beyond the explicitly triaged debris in this thread.

## Execution Progress

### Phase 0

- [x] Remove `audit/dolgachev_kondo_extracted.txt`
- [x] Remove tracked root `.orig` debris selected for this thread

### Phase 1

- [x] Update `proofs/solved/task3_2_isotropic_planes.md`
- [x] Update `proofs/solved/task6_1_slc_stability.md`

### Phase 2

- [x] Repoint `PLAN.md` to this active thread
- [x] Update `GAPS.md` with the concrete Task 5.1 next step

### Quality Gates

- [x] Canonical literature layer is referenced from main proof prose
- [x] Cleanup scope remains explicit and narrow
- [x] Task 5.1 next step is concrete and no longer vague
