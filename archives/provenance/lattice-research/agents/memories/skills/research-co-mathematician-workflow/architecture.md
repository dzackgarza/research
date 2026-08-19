# Co-Mathematician Workflow Architecture

This reference adapts the workflow architecture from Zheng et al.,
`AI Co-Mathematician: Accelerating Mathematicians with Agentic AI`
(`arXiv:2605.06651v1`) to this repo.

## Preserved Substrate

Preserve only these substrate choices:

- durable markdown cards under `.agents/plans/`;
- schema validation through `.nimbalyst/trackers/` and `just`;
- IWE/bash-indexable text;
- git provenance;
- a coherent hierarchy.

Everything above that substrate can evolve.

## Workspace Model

The repo is a mathematical workspace with five coordinated surfaces:

- `.agents/plans/`: indexable state, dependencies, workstream structure, and review gates.
- `paper/`: the living LaTeX working paper with margin-note style claim status.
- `reports/workstreams/`: workstream reports and attachments that feed the paper.
- `.agents/agent-roles/`: repo-local prompts and delegation contracts for specialist
  agents.
- source roots such as `theory/`, `notes/`, `src/`, `tests/`, and `lean/`: evidence
  and implementation artifacts.

Cards are not the final mathematical medium. They route work and preserve state. The
working paper and workstream reports rebuild the human mental model.

## Intake

Intake is a durable phase, not a conversation warmup. It must record:

- the user's research question in the user's terms;
- refined goals and non-goals;
- hard constraints and forbidden shortcuts;
- source context and primers supplied by the user;
- candidate workstreams;
- success criteria and uncertainty policy;
- what requires human approval before execution.

Do not open autonomous research workstreams until the intake framing is approved.

## Activity Taxonomy

Research tasks should be classified by `activityType`. First-class activities include:

- intent refinement;
- literature search and source mining;
- brainstorming and conjecture generation;
- counterexample search;
- proof attempt and proof repair;
- formalization;
- computation, numerical experiment, and simulation;
- implementation;
- validation and citation checking;
- synthesis and exposition;
- review;
- failure analysis;
- user escalation.

This taxonomy matters because different activities have different evidence standards.
A numerical experiment builds intuition; it does not prove a theorem. A literature
search supplies exact hypotheses; it does not discharge implementation. A failed proof
can still preserve a useful strategy.

## Workstreams

Use phase cards with `phaseKind: workstream` for substantial branches. A workstream:

- attaches to an approved goal;
- follows one branch type, such as prove, disprove, literature, theory, computation,
  implementation, formalization, synthesis, audit, or exploration;
- has an agent roster;
- produces a report artifact;
- sends serious claims to review;
- updates the living paper when the branch changes the narrative;
- records failed explorations explicitly.

Multiple workstreams may pursue the same goal from different angles. A disproof branch,
source-mining branch, and computational branch can all be live without forcing the user
to read execution logs.

## Agent Organization

The active chat/harness is the project coordinator. It owns:

- intake and user steering;
- goal and non-goal preservation;
- workstream creation and termination;
- escalation to the user;
- synthesis across reports.

Specialist roles live in `.agents/agent-roles/`. Delegation prompts must pass the
approved goal, workstream path, allowed scope, expected report artifact, and stop
conditions. A specialist should not infer the project goal from ambient repo state.

## Native Artifacts

Every substantial workstream produces a report. A report must include:

- exposition of the process, not only the conclusion;
- links to cards, sources, computations, and code;
- claim-status annotations;
- failed or abandoned paths that constrain future work;
- review status and unresolved objections.

The living paper in `paper/` is the synthesis layer. It must use margin-note style
annotations for provenance, contentiousness, computation dependence, and human-review
needs.

## Uncertainty Lifecycle

Uncertainty has three operations:

- Track: record claim status, provenance, version history, and review objections.
- Manage: trade compute for validation through source checks, replayable computation,
  formalization, independent review, and citation checking.
- Communicate: surface stalled reviews, disputed lemmas, missing sources, and human
  judgment points in cards, reports, and paper margin notes.

Do not collapse uncertainty into `blocked`. A blocker stops execution. Uncertainty
describes the rigor state of a claim and may coexist with active work.

## Failure Preservation

Preserve failed explorations when they contain mathematical information:

- a false conjecture with counterexample data;
- a proof strategy with an exact gap;
- an exhausted search path and its bounds;
- a missing theorem/source after a documented search;
- a reviewer disagreement that localizes a disputed assertion.

Do not preserve broken code or dead scripts. Preserve the mathematical lesson and
delete or fix the broken artifact.

## Review Failure Modes

Review loops must detect two pathologies:

- False consensus: the document evolves until reviewers stop noticing a real flaw.
- Non-termination: reviewers and authors cycle without reducing the disputed claim.

When either appears, stop the loop, mark the exact assertion, expose it in the report
or paper, and escalate to the project coordinator or user.
