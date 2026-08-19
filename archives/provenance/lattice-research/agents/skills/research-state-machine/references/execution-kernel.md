# Research Execution Kernel

This is the canonical simplified state machine for the research repo. It replaces the old ad hoc task-directory machine with a Nimbalyst-integrated workflow.

## Core invariant

No process label creates mathematical trust. Trust comes only from the artifacts that justify the claim: exact statement, sourced proof, replayable computation, formal proof, certificate, counterexample, PR diff, review decision, and linked plan/card history.

## Canonical objects

Use these canonical objects:

- `GOAL.md`: the read-only research objective spine.
- `.agents/plans/features/**`: active feature, spec, plan, phase, task, and decision cards.
- `paper/**`: the living LaTeX working paper that rebuilds the mathematical narrative
  with provenance and margin-note style uncertainty annotations.
- `reports/workstreams/**`: workstream reports and attachments, including failed
  branches that teach future work.
- `.agents/agent-roles/**`: repo-local delegation prompts for the project coordinator
  and specialist research agents.
- `.agents/current-goal-phase.md`, `.agents/TODO.md`, and `.agents/retired/**`: phase marker, scratchpad inbox, and short-term retired legacy cards.
- Git branches, PRs, commits, and worktrees: provenance, review, and merge gates.
- Produced artifacts in their natural durable roots: `src/`, `tests/`, `notes/`, `theory/`, `lean/`, and linked proof/computation outputs.

Do not create a parallel `tasks/T-XXXX` planning universe for new work. A tracked Nimbalyst card is the task spec. Its frontmatter and body must contain enough context for another agent to execute without chat recovery.

## Live stages

### Plan

Use planning only when work is complex, architectural, mathematically foundational, or multi-card. Plans are human + LLM collaborative artifacts. They require explicit human approval before decomposition or execution.

A plan records goal links, phases, dependencies, risks, acceptance strategy, and high-level task inventory. It does not replace task cards.

For substantial research directions, planning starts with intake. The coordinator must
separate the user's question, approved goals, non-goals, success criteria, and hard
constraints into a durable onboarding artifact before opening workstreams. If the user
has not approved that framing, the plan stays in intake rather than drifting into
execution.

Plans that coordinate multiple paths must describe the branch structure explicitly.
Useful branch pairs include prove/disprove, literature/computation, theory/implementation,
source-mining/review, and synthesis/audit. A branch may fail; failure is a reportable
outcome when it rules out a strategy, exposes a missing hypothesis, finds a false
claim, or identifies a computation that cannot currently be made rigorous.

For this repo, a `phase` card may be a milestone or a workstream. Use `phaseKind:
workstream` when the phase represents a single branch with its own report artifact,
agent roster, branch type, uncertainty summary, and failed-exploration list.

### Specify card

Each executable unit becomes a tracked `task` card under `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/`. The card must define the exact claim or work target, source provenance, plan or `GOAL.md` link, accepted scope, owner/role if known, complexity, dependencies, acceptance criteria, verification plan, and branch/PR policy when relevant.

For mathematical claims, the card must state whether it is exploratory, preparatory, local-claim promotion, or `GOAL.md` discharge.

For substantial research work, the task card must also state its `activityType`,
workstream role, claim status, uncertainty state, paper anchors, report artifacts, and
failed explorations using the tracker fields when present. This is the forward card
contract: future agents should be able to tell whether a task is intent refinement,
literature search, source mining, brainstorming, conjecture generation,
counterexample search, proof repair, computation, formalization, implementation,
review, synthesis, exposition, failure analysis, or user escalation without
reconstructing a chat transcript.

### Preflight

Before execution, reject or split any card that hides major work. Hidden major work includes choosing or inventing the core algorithm, building reusable exact infrastructure, proving a new reduction theorem, fixing a convention that changes downstream meaning, or solving a classification/search problem comparable to the nominal task.

For mathematical spec work, preflight must also reject cards whose definitions are not
source-grounded. A card is not ready for spec editing until it records the canonical
source path or reference, exact definition, hypotheses, codomain/return object, and any
proof obligation for choice-independence or equivalence with another notion. Old TODO
lines, migrated cards, common terminology, and plausible special-case intuition do not
meet this bar.

If a term has multiple plausible meanings, or if a familiar special case suggests an
equivalence that has not been proved under explicit hypotheses, split to a decision or
source-mining card. Keep the affected spec leaf blocked until the distinction is
resolved. Do not normalize bespoke project terminology to the most common textbook or
Sage interpretation by default.

If the shared mathematical base lacks the noun, method, morphism, coercion, constructor, or backend bridge needed to express the task cleanly, stop and create the base task. Do not patch around the gap locally.

This stop is path-local. It blocks the current implementation or claim path, not the
active phase. After creating or updating the prerequisite task, continue another
approved active leaf if one exists.

### Continuation and blocker test

An agent may report that there is no path forward only after checking the current
phase marker, approved plans, and active leaf cards. Every remaining active leaf must
have a concrete current-phase blocker.

The following are not global blockers during approved spec-phase work:

- QC failures outside a user-requested QC pass, commit integration pass, or phase
  transition.
- Downstream-phase guards against Coble, lattice implementation, raw matrix, orbit,
  or geometry computations.
- Overscoped cards that can be split, promoted to an approved plan, or decomposed.
- Missing vocabulary or backend bridges when a prerequisite spec, decision, research,
  or implementation-gap card can be filed.
- Human approval gates for parent acceptance, closure, or phase transition when
  ordinary approved leaf execution remains. Do not convert those gates into
  `needs-human-input` blockers for ordinary task cards.

If a spec leaf can advance through source mining, writing/refining a spec, centralizing
terminology, drafting audit criteria, capturing a decision, splitting work, or filing a
prerequisite, continue there.

A card in `needs-agent-review` status is also actionable agent work. `needs-agent-review` means the
implementing work is done and the card is ready for the ordered gate-based protocol
(described in `references/review-kernel.md`). Dispatch a fresh-context subagent to
execute the review gates (never self-review inline, per the review kernel's subagent
isolation requirement). Do not treat `needs-agent-review` as a blocking status, a waiting
state, or a human gate. Only `needs-human-input` and `blocked` statuses represent cards
that cannot currently be advanced by an agent without external input or resolution of an
external prerequisite.

### Execute

Two kinds of cards reach execution stage:

- **Implementation cards** (`unstarted` or `revision-required` → `in-progress`): run nontrivial implementation in the required branch/worktree and within the card's allowed scope. The implementing agent updates the card with files touched, branch, PR, validation notes, blockers, and follow-up findings. The implementing agent does not mark parent work accepted/done/closed. When implementation is complete, set the card to `needs-agent-review` if the next check is agent-executable. Set `needs-human-input` only if the card records an exact human-only decision that source review, repo policy, and the DAG cannot answer.

- **Research workstream cards** (`unstarted` or `revision-required` → `in-progress`):
  pursue one linear branch and produce a native mathematical artifact, such as a
  source-backed note, proof attempt, computation log, notebook, report, or reviewable
  theorem statement. The artifact must link claims to sources, computations, or review
  evidence. If the branch fails, preserve the failure as evidence in the card or a
  linked failure-record task instead of silently restarting from the same assumptions.
  Escalate to `needs-human-input` when the next step depends on mathematical taste,
  area expertise, or a human choice of direction. Do not escalate merely because the
  work passed review or because final parent acceptance is human-gated.

- **Working-paper synthesis**: when a workstream changes the mathematical narrative,
  update `paper/` or create a task that does so. The paper must distinguish theorem,
  conjecture, computation-supported claim, source-backed claim, disputed lemma, failed
  path, and human-review point in the prose or margin notes.

- **Review cards** (`needs-agent-review` → gate-based review → outcome): these are ready for the ordered gate protocol in `references/review-kernel.md`. The reviewer (an independent agent session, not the implementer) applies Gates 1-6 and sets the outcome. Review is execution work: it produces findings, logs, and status changes. Do not stall when the active leaf list includes `needs-agent-review` cards.

  Review must be executed by a **fresh-context subagent**, never by the coordinator
  doing the review inline in its own session. The coordinator already has the
  implementing state in its chat history, which contaminates independent judgment.
  Load `subagent-delegation` and dispatch a review subagent that has never seen the
  implementation session. The subagent prompt must include: the card body, the work
  artifacts (or paths to them), the baseline artifacts, and the requirement to produce
  concrete, falsifiable evidence for every gate check (see the anti-boxchecking rules
  in `references/review-kernel.md`).

  After the subagent completes, the coordinator must verify the review itself:
  - Every gate pass has a concrete artifact (a file path read, a command run, a diff
    inspected, a specific source consulted).
  - The subagent did not accept vague "looks good" or "appears correct" language.
  - Gate failures cite specific code, line numbers, or source paths.
  - The outcome (complete / revision-required / blocked / needs-human-input) is
    supported by the findings.
  If the review is a box-checking exercise, reject it and re-dispatch with a
  tightened prompt.

Small administrative metadata edits can be direct when the repo workflow allows them. Production code, canonical docs, mathematical infrastructure, and agent-guiding docs require branch/PR routing according to the project workflow.

### Replay and attack (formalized by the Review Kernel)

The `references/review-kernel.md` formalizes this stage into a six-gate ordered protocol. See that document for the full procedure.

Replay/attack is required when a card claims mathematical correctness, proof evidence, code correctness, state-machine acceptance, or parent-plan discharge. Use `research-proof-auditing` for proof and evidence sufficiency. Use independent review where failure modes must be separated from the implementation context.

Attack the strongest claim made anywhere: title, card body, plan, PR, filenames, summary, comments, and downstream references.

### Promote, reject, split, or retire

Promotion of parent plans, features, or program-level claims means the linked
artifacts support the exact claim and the applicable human gate has approved that
promotion. Ordinary task-card review does not acquire a human gate merely because its
result may later feed a human-approved parent promotion. Otherwise reject, split, or
send back to planning.

Resolved cards leave active paths and move to `.agents/retired/` only while short-term reference is useful. Durable history belongs in git commits, PR bodies, plan history, canonical decisions, and durable docs.

## Escalation tiers

### Exploratory or preparatory

Requires a tracked card, scoped work, source provenance, and replayable artifacts if any. No theorem-discharge language is allowed.

### Local claim promotion

Requires proof/evidence audit, exact claim-surface alignment, checked dependencies, and a clear parent-sufficiency edge explaining what burden is discharged.

### `GOAL.md` discharge

Requires final composed-goal audit, assumption unification, exact theorem or counterexample statement, provenance for all imported artifacts, and human approval.

## Tangential findings

During work, discoveries route through the lightest safe mechanism:

- File a real tracked card immediately when the finding is concrete enough to execute.
- Add a short entry to `.agents/TODO.md` when it needs investigation before carding.
- Delegate a cheap branching investigator when important but tangential.
- Create a decision card for naming, ownership, mathematical, or organizational choices.

Do not bury follow-up obligations in chat, implementation comments, or PR summaries as the only durable record.

Preserve negative results with the same discipline. A failed proof strategy, false
conjecture, exhausted search path, missing source, or intractable reviewer disagreement
belongs in `failedExplorations`, a report artifact, or a dedicated failure-record task.
Do not erase a failed branch merely because a different branch may now be more
promising.

Reviewer disagreement has two failure modes: false consensus and non-termination. If
reviewers converge only by weakening the claim, record the weakened claim explicitly and
send the card to `revision-required` or `needs-human-input`. If review cycles continue
without progress, stop the loop, record the exact disputed assertion, and escalate.

## Replan rule

Replanning is valid only when it reduces the real burden: clarified claim, exposed hidden major work, separated base admission, discharged prerequisite, or removed ambiguity. Replan churn that only adds paperwork is failure.

## Acceptance rule

A sprint item, task card, theorem claim, or `GOAL.md` item is not complete because an agent says it is complete. It is complete only when the Nimbalyst card, linked plan, artifacts, git/PR evidence, proof-audit evidence when applicable, reviewer decision, and current canonical docs all agree.
