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

- `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`: category specs, Sage-compatible constructors, Hom/End/Aut surfaces, source maps, and category-obligation example/audit stabilization.
- `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER`: Sage-backed owned objects, wrappers, coercions, validators, and backend bridges satisfying approved category specs.
- `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS`: inheritable algorithms for countability, enumeration, products, free modules, and other categorical surfaces that must not be lattice-local loops.
- `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`: ModulesWithForms and lattice objects, including duals, discriminant descent, morphisms, and orthogonal-group surfaces.
- `FEATURE-GEOMETRY-CATEGORY-INTERFACES`: geometry-facing category interfaces and backend research for schemes, varieties, manifolds, curves, surfaces, families, and monodromy.
- `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`: Coble curve, blowup, K3 cover, Picard pullback lattice, discriminant/complement, and primitive embedding foundation from `GOAL.md` Tasks 1.1-1.3.
- `FEATURE-COBLE-*`: downstream Coble verification feature roots for `GOAL.md` Tasks 2-6; these remain ordinary feature cards gated by the prerequisite semantic substrate and geometric lattice foundation.

## Rules

- Card IDs must match filename stems.
- `parents` records containment; `dependsOn` records blocking or prerequisite edges.
- Execution follows the DAG. If a card's declared `dependsOn` prerequisites are not
  complete, leave it `unstarted`; do not mark it `blocked` unless it was otherwise
  ready and hit a real external prerequisite outside the satisfiable DAG.
- Priority and continuation analysis follows the first incomplete dependency frontier.
  If `B dependsOn A` and `A` is incomplete, ignore `B`'s internal completion, child
  status, and review state when choosing or describing priority. `B` is simply
  DAG-gated by `A` until all incoming prerequisite paths are complete.
- Do not use `needs-human-input` for source-forced facts, routine cleanup, or ordinary
  dependency order. If work cannot proceed until prerequisite vocabulary or surfaces
  exist, encode the prerequisite in `dependsOn` and leave the downstream card
  `unstarted`.
- Do not use `needs-human-input` for clean agent-reviewed task closure. If review
  evidence, repo policy, source grounding, and the DAG already determine the outcome,
  the card is not a human decision even if parent-plan or feature acceptance later
  requires human approval. Record the review outcome and continue the earliest
  executable frontier.
- Completed feature trees live under `plans/features/completed/`, not beside active
  feature roots.
- Specs live under the owning feature's `specs/` directory.
- Decisions live under the owning feature's `decisions/` directory.
- Executable implementation, research, bug, and audit work uses `trackerStatus.type: task` and lives under a phase's `tasks/` directory.
- A phase can be a milestone or a co-mathematician workstream. Use `phaseKind:
  workstream` when the phase owns a branch type, agent roster, report artifact,
  paper-section links, uncertainty summary, and failed-exploration records.
- Before creating any task card, identify the owning feature, plan, phase, and exact
  phase `tasks/` path. If the phase card does not exist, fix the phase breakdown first.
  A plan-level `tasks/` directory is invalid and indicates a skipped phase gate; do not
  add to it or treat moving its cards as a complete process fix.
- New substantial research tasks must classify `activityType`, `workstreamRole`,
  `claimStatus`, and `uncertaintyState`, and must link report artifacts or paper
  anchors when they affect the mathematical narrative.
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
git diff --check -- .agents/plans .nimbalyst/trackers AGENTS.md .agents/current-goal-phase.md
```

`just plan-validate` delegates to the centralized planning validator in
`/home/dzack/ai/planning/justfile`. Do not add or use a repo-local relaxed validator;
planning validation has one pass/fail authority.
