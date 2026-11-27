# Literature-First Reorientation Plan

## Goal

- Current defect/state: the repo contains substantial exact computational work, but the
  planning/docs layer let local recomputation outrun the literature.
  Standard facts about Coble surfaces, the K3 cover, the lattice picture, and the
  9-dimensional period-domain count are not yet centralized in one canonical reference
  spine.
- Target state: a repo in which standard mathematical claims are anchored to canonical
  literature first, computations are clearly labeled as supporting evidence, stale plans
  are archived, and the next 24 hours of work are ordered around that structure.
- Why this matters: the project is supposed to produce numerical evidence, but it should
  do so in a literature-grounded way instead of rediscovering basic facts ad hoc.

## Constraints

- Required:
  - Keep exact arithmetic and audit-grade computation as a core repo objective.
  - Treat literature as the source of truth for standard facts.
  - Keep `PLAN.md`, `GOAL.md`, `GAPS.md`, and `REFERENCES.md` synchronized.
  - Archive stale plans instead of leaving them in active locations.
- Forbidden:
  - Re-deriving standard literature claims before locating and citing canonical sources.
  - Treating computational output as a replacement for a known reference.
  - Starting new formalization work unless the target statement is genuinely local or
    not already available upstream.

## Scope

- Included:
  - `PLAN.md`
  - `plans/`
  - `GOAL.md`
  - `GAPS.md`
  - `REFERENCES.md`
  - audit notes that explain literature/computation/tooling roles
- Excluded for this reset step:
  - new broad computational searches beyond tightly scoped support tasks
  - publication-ready prose outside concise repo-facing claim notes
  - large-scale Lean integration

## Phase 0: Cleanup and archive

Goal: remove plan drift and move stale plans out of active locations.

- Location: `PLAN.md`, `.serena/plans/`, `plans/archive/`
- Description: replace the root plan with an active index, archive superseded planning
  material, and keep only one active work thread.
- Dependencies: none.
- Acceptance criteria: active plan location is unambiguous and superseded plans are
  moved out of active paths.
- Validation: inspect `PLAN.md`, `plans/`, and `plans/archive/`.

## Phase 1: Canonical literature spine

Goal: centralize the references that support the repo's standard claims.

- Location: `REFERENCES.md`
- Description: organize references by claim-family rather than by ad hoc accumulation,
  with explicit mapping from standard statements to canonical sources.
- Dependencies: Phase 0 complete.
- Acceptance criteria: the reference file answers “where should I cite this?”
  for the major recurring claims.
- Validation: each major claim-family in `GOAL.md` and `GAPS.md` points back to a source
  in `REFERENCES.md`.

## Phase 2: Rewrite repo goals and gaps around literature-backed claims

Goal: make the project directives reflect the correct division of labor between
literature, computation, and formalization.

- Location: `GOAL.md`, `GAPS.md`
- Description:
  - rewrite goals as ordered priorities rather than a sprawling derivation dump
  - separate standard literature facts from genuinely open repo tasks
  - state clearly which gaps are citation gaps, which are computation gaps, and which
    are genuinely blocked mathematics
- Dependencies: Phase 1 complete.
- Acceptance criteria: the top-level docs make it obvious what is known from literature,
  what the repo has numerically verified, and what is still unresolved.
- Validation: manual cross-check against `REFERENCES.md` and recent audited computation
  artifacts.

## Phase 3: Next 24h execution order

Goal: orient the next day of work around high-value, literature-grounded outputs.

- Task 3.1 — literature note for the lattice/moduli setup
  - Where: `audit/` or a repo note file
  - What: write a concise claim map for the blowup construction, K3 cover, lattice
    setup, and 9-dimensional period-domain statement.
  - Depends on: Phase 1.
  - Done when: the repo has a short reusable note for these standard facts.
  - Validation: note cites canonical sources and avoids unsupported rediscovery.
- Task 3.2 — Task 1.1 prose note
  - Where: `audit/` or a repo note file
  - What: explain how the exact sextic computations support the literature picture,
    especially birationality and exact node data.
  - Depends on: Phase 2.
  - Done when: Task 1.1 outputs are paired with a short mathematical explanation.
  - Validation: cited against exact output artifacts already in repo.
- Task 3.3 — Task 5.1 route reset
  - Where: `GAPS.md`, `audit/`, computation plan notes
  - What: replace the disproved involution route with a literature-backed route; test
    CARAT only on finite positive-definite auxiliary subproblems.
  - Depends on: Phase 2.
  - Done when: the next route is mathematically coherent and no longer framed as a blind
    search.
  - Validation: route description names the exact target invariant and intended tool.

## System-Level Validation

- `PLAN.md` points to one active plan.
- `REFERENCES.md` is the canonical literature spine.
- `GOAL.md` and `GAPS.md` no longer present literature facts as if they were still open
  computational mysteries.
- Archived plans live under `plans/archive/` rather than active paths.

## Risks / Rollback

- Risks:
  - overcorrecting by demoting computation too far
  - leaving stale planning debris in hidden locations
  - adding references without clarifying which claims they support
- Mitigations:
  - keep “literature first, computation still essential” explicit in every top-level doc
  - archive instead of deleting plans
  - structure references by claim-family, not bibliography bulk
- Rollback path:
  - use git history to restore any superseded planning document if the new structure
    proves less usable.

## Stop Rules

- Do not start new broad computational searches until the literature spine is stable.
- Do not pursue new Aristotle work until the target result is checked against upstream
  mathlib and against the now-centralized literature plan.
- Do not restate a standard claim in repo prose without pointing to a canonical source.

## Execution Progress

### Phase 0

- [x] Archive superseded plans and simplify `PLAN.md`

### Phase 1

- [x] Reorganize `REFERENCES.md` into a literature spine

### Phase 2

- [x] Rewrite `GOAL.md`
- [x] Rewrite `GAPS.md`

### Phase 3

- [x] Prepare the lattice/moduli literature note
- [x] Prepare the Task 1.1 prose note
- [x] Reset the Task 5.1 route description

### Quality Gates

- [x] Literature-first ordering is explicit
- [x] Numerical evidence remains in scope
- [x] Active vs archived plans are unambiguous
- [x] Top-level docs agree with one another
