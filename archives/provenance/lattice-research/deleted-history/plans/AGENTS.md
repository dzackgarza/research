# Research Planning Workspace

This directory is the active Nimbalyst-backed planning workspace for the research repo. IWE is the preferred query layer over this markdown: use it to find cards, dependencies, and recent handoff context before broad manual scans.

## Hierarchy

Use this containment model:

```text
plans/features/FEATURE-ID/
├── FEATURE-ID.md
├── specs/SPEC-ID.md
├── decisions/DECISION-ID.md
└── plans/PLAN-ID/
    ├── PLAN-ID.md
    └── PHASE-ID/
        ├── PHASE-ID.md
        └── tasks/TASK-ID.md
```

Root features are concrete deliverable buckets, not staged-program mirrors. `GOAL.md`
remains the source for the staged mathematical program, and `.agents/current-goal-phase.md`
records the active phase gate.

## Local Feature Buckets

- `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`: category specs, Sage-compatible constructors, Hom/End/Aut surfaces, source maps, and smoke/audit stabilization.
- `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`: ModulesWithForms and lattice objects, including duals, discriminant descent, morphisms, and orthogonal-group surfaces.
- `FEATURE-GEOMETRY-CATEGORY-INTERFACES`: geometry-facing category interfaces and backend research for schemes, varieties, manifolds, curves, surfaces, families, and monodromy.

## Rules

- Card IDs must match filename stems.
- `parents` records containment; `dependsOn` records blocking or prerequisite edges.
- Execution follows the DAG. If a card's declared `dependsOn` prerequisites are not
  complete, leave it `unstarted`; do not mark it `blocked` unless it was otherwise
  ready and hit a real external prerequisite outside the satisfiable DAG.
- Do not use `needs-human-input` for source-forced facts, routine cleanup, or ordinary
  dependency order. If work cannot proceed until prerequisite vocabulary or surfaces
  exist, encode the prerequisite in `dependsOn` and leave the downstream card
  `unstarted`.
- Completed feature trees live under `plans/features/completed/`, not beside active
  feature roots.
- Specs live under the owning feature's `specs/` directory.
- Decisions live under the owning feature's `decisions/` directory.
- Executable implementation, research, bug, and audit work uses `trackerStatus.type: task` and lives under a phase's `tasks/` directory.
- Do not create new active cards under `.agents/plans`, `.agents/tasks`, or `.agents/decisions`.
- Keep metadata compact; put detailed grounding, acceptance criteria, source evidence, and work logs in the body.
- For constructor and method-owner cards, distinguish the mathematical owner, the
  human-facing constructor convention, and the code-maintenance implementation owner.
  A category can expose an aggregate constructor entry point even when the named
  constructor implementation lives on the most maintainable source category.

## Validation

Run from the repo root:

```bash
just plan-validate
just plan-progress-report
git diff --check -- plans .nimbalyst/trackers AGENTS.md .agents/current-goal-phase.md
```
