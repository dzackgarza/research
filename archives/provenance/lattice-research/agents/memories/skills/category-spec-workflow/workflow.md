# Category Spec Workflow Reference

This is the canonical detailed workflow reference for category-spec work.

Internal historical mentions of `WORKFLOW.md` refer to this skill reference unless they explicitly name another path.

## Contents

- [Tracking and planning](#tracking-and-planning)
- [Theme grouping](#theme-grouping)
- [Agent skill factoring](#agent-skill-factoring)
- [Rubric skills](#rubric-skills)
- [Plan creation workflow](#plan-creation-workflow)
- [Plan files are the planning system](#plan-files-are-the-planning-system)
- [Human-facing visual artifacts](#human-facing-visual-artifacts)
- [TODO scratchpad and inline task markers](#todo-scratchpad-and-inline-task-markers)
- [Retired card holding area](#retired-card-holding-area)
- [Full task card requirements](#full-task-card-requirements)
- [Tangential discovery procedure](#tangential-discovery-procedure)
- [Delegation contracts](#delegation-contracts)
- [Bug workflow](#bug-workflow)
- [Agent execution workflow](#agent-execution-workflow)
- [Branch and PR policy](#branch-and-pr-policy)
- [Worktree policy](#worktree-policy)
- [PR lifecycle](#pr-lifecycle)
- [AI-slop risk](#ai-slop-risk)
- [Commit discipline](#commit-discipline)
- [Documentation lifecycle](#documentation-lifecycle)
- [Completed-work migration](#completed-work-migration)
- [Category obligation examples and failed-assertion classification](#category-obligation-examples-and-failed-assertion-classification)

## Reference Body

# WORKFLOW.md - category_specs

Read this file before planning, delegating, creating tracker items, classifying failed
category assertions, preparing PRs, migrating docs, or changing workflow state in this
subtree.

Simple implementation agents usually do not need this file unless their task includes
tracking, delegation, failed-assertion classification, branch/PR policy, or status
changes.

This file contains workflow rules extracted from `AGENTS.md`. Category-spec style,
mathematical naming, banned implementation patterns, and compliance rules live in
`STYLE.md`.

## Tracking and planning

Use Nimbalyst tracker files as the central durable record for planning, ongoing work,
follow-ups, blockers, decisions, and deferred compliance findings in this subtree. Do
not create ad hoc planning, status, audit, or TODO markdown files when a tracked file is
the appropriate artifact.

Sage constructor/method inventory and mapping work has one canonical mathematical
document: `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]`. That spec owns the
source-backed mathematical operation map. A row is complete when it translates Sage
method body/docs/examples into a mathematical operation under hypotheses, the weakest
category owner or refinement claimed, witnesses required by that structure, the
codomain/return object, and source evidence.

The semantic extraction step is not optional setup. The first work product for a
category family is the method-cluster behavior record: inputs, outputs, examples,
branch cases, return objects, conventions, and helper/backend/display behavior observed
in Sage. Mathematical vocabulary is introduced after that behavior is known, not before.
Sage method placement, helper exports, package imports, display hooks, backend
branches, and generic category primers do not determine mathematical ownership.

Compatibility, runtime, display, private, test-helper, package-export, and backend
plumbing methods are not a parallel progress object. Discard them after a one-line
residue classification unless they change the mathematical interface or block
construction of a required spec object.

Before a session edits subtree `SAGE_INVENTORY.md`, subtree `MAPPING.md`, method-owner
spec rows, or mapping cards, it must identify whether it is performing semantic
extraction, adding or correcting a source-backed mathematical assertion, rejecting a
Sage method, constructor, or class as nonmathematical residue, or recording an
unresolved mathematical question.
Mapping docs, cards, decisions, review logs, handoffs, and commits are evidence or
source pointers; they are not mathematical progress evidence unless the operation map
changes.

There is no separate backlog. The active tracked cards are the outstanding work set.
When work is implemented, resolved, rejected, or superseded, move the card out of active
paths and retire or delete it according to the retired-card policy.

Approved plans and active tracked cards are the concrete continuation set. During
the spec phase, do not replace execution with abstract blocker discussion. Select an
approved active spec leaf and advance it unless that leaf has a concrete current-phase
blocker.

Spec leaves must be definition-grounded before execution. A card migrated from old
plans, deleted triage files, category-test output, or chat context may identify an area of
work, but it does not by itself authorize a mathematical definition or method owner.
Before a spec edit, the card or working note must name the canonical source path,
definition, hypotheses, return object/codomain, and any invariance or equivalence proof
obligation. If that record is missing, the correct action is source mining, decision
capture, or card splitting, not speculative spec writing.

Human input is reserved for decisions that remain after this grounding work. Do not
mark a card `needs-human-input` because the implementing agent is unsure, because a
plan has dead links, because a review found fixable structural debris, or because a
downstream task depends on incomplete vocabulary. Source-forced facts become agent
action. Planned prerequisites become `dependsOn` plus `unstarted`. Fixable review
findings become `in-progress`, `needs-agent-review`, or `revision-required` where the schema
supports it.

Do not mark a card `needs-human-input` merely because clean reviewed work has not been
human-accepted yet. Parent-plan acceptance, feature approval, or phase transition
approval is a separate promotion prerequisite; it is not a task-level blocker and must
not be used as an early-exit condition. If the only question is "approve this reviewed work,"
the card needs agent-owned closure or continued operation-map execution, not human
input.

If a trivial mathematical fact, obvious category edge, or already sourced owner reaches
the user as a decision, treat that as workflow breakage. Inspect why the escalation
happened: missing owner row, unrecorded subcategory relation, stale migrated status,
weak review rubric, missing `dependsOn`, or a report that listed paths without the
source content that controls the conclusion. Patch the workflow document so the same
non-decision is not presented again.

Tracker items that touch category specs must carry the project purpose into the local
task statement. Do not rely on a distant global reminder when the task is likely to see
Sage failures. Plan, phase, and task bodies should state the applicable ideal-interface
rule in their acceptance or grounding section:

- category specs define the ideal mathematical interface;
- category specs extend Sage's category/object universe without treating current
  Sage coverage as the adequacy standard;
- Sage interop is a design constraint where mathematically appropriate;
- Sage is implementation evidence and a realization witness;
- Sage inventory helps preserve existing functionality and avoid unimplementable
  wishlists, but it is not a ceiling on mathematically required category operations;
- category-obligation examples expose gaps between current Sage/refined objects and
  the ideal spec;
- a failed category assertion is not evidence for deleting, weakening, or moving a spec
  obligation;
- an obligation may move only when the replacement weakest category is source-grounded
  and the replacement path preserves the mathematical statement.

Tracker items that touch type checking, method inheritance, constructor collectors, or
implementation providers must also include a design-direction check. Mathematical
subcategory obligations are not ordinary software substitutability obligations:
subcategories inherit upstream specs, but their refined operations may take more
structured inputs and return more structured outputs. Static checkers can object to
that covariance or to dynamic Sage/category inheritance even when the spec is
mathematically aligned. The workflow response is to classify the finding: source
defect when an owner, codomain, hypothesis, constructor boundary, or named type is
actually missing; checker-education work when the code already expresses the intended
category structure and the tool lacks the provider model. The latter must be routed to
dedicated plugin, generated-stub, static-model, global-QC, or focused-reproducer work
whose acceptance teaches QC to enforce the convention. Do not file these as ignorable
expected failures, and do not convert them into local casts, trivial re-call wrappers,
explicit subclassing, or provider-splicing in the mathematical category definition. Zero warnings
is an enforcement target, not permission to distort the codebase into a form the
checker happens to understand.

Casts are review triggers in tracker work. A single cast may be justified at a true
untyped interop boundary, validated constructor point, or documented promotion point,
but non-isolated casts and repeated cast patterns normally indicate QC-silencing or
code-contortion behavior. Tracker acceptance must force a decision: keep a narrow
promotion exception with proof obligations, move the type refinement to the downstream
implementation boundary that actually implements the ABC contract, or create dedicated
QC-tooling/static-model work that teaches the checker to enforce inherited-category
promotion globally.

Constructor definition cards must first identify the construction being performed and
the category structure that owns it. Do not create constructor-placement reports unless
two mathematically distinct constructions compete for the same public name or return
contract. A specific named object may naturally carry several structures: for example,
a finite field is a field, ring, module, and algebra in different contexts. That alone
does not create a placement decision. Constructor namespaces such as `Cat().Constructors()`
can collect canonical user-facing entry points when the mathematical owner is already
determined.

For category-obligation and wrapper-migration cards, local acceptance must explicitly
reject test-driven spec weakening. A failed assertion asks which mathematical claim
failed: false, under-hypothesized, unrealized by the implementation, missing
constructor/refinement, missing source evidence, or blocked by backend/tooling. Route
the answer to the spec, implementation, or backend task. Passing an example by
shrinking the ideal interface is a failed task, even if the command output improves.

Before advancing any category-spec task, phase, or plan, run a spec-weakening review
over the actual repository changes. Inspect `git diff --cached`, `git diff`, and any
commits created during the work with a patch view. The review fails if it finds deleted
abstract methods, removed constructor/category obligations, narrowed category
assertions, weakened acceptance criteria, moved obligations without a source-grounded
replacement weakest category, or any Sage-gap-driven interface shrinkage. Record the
review result in the task/phase/plan acceptance notes or leave the item unadvanced.

Before creating or migrating a tracker item, read `.agents/skills/track/SKILL.md` and
inspect `.nimbalyst/trackers/*.yaml` for the registered schemas.

Use the central planning tracker types only for active category-spec work: `feature`,
`spec`, `plan`, `phase`, `task`, and `decision`. Executable implementation, research,
bug-fix, failed-assertion classification, and audit work uses `task`; do not create active executable
cards with legacy `bug`, `feature`, `idea`, or `automation` types.

Do not create or use custom task-like types such as `spec-work`,
`implementation-work`, `research-work`, `sprint-work`, `task-work`, or `agent-work`.
Use containment, `dependsOn`, priority, and complexity as primary workflow metadata.
Tags such as `category-specs`, `spec`, `implementation`, `research`, `validation`, and
`docs-migration` are secondary grouping aids.

All active Nimbalyst-backed planning and work files live under root `.agents/plans/`:

- `.agents/plans/features/FEATURE-ID/FEATURE-ID.md` for feature roots.
- `.agents/plans/features/FEATURE-ID/specs/SPEC-ID.md` for feature-owned specs.
- `.agents/plans/features/FEATURE-ID/decisions/DECISION-ID.md` for durable decisions.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PLAN-ID.md` for approved plans.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/PHASE-ID.md` for plan phases.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/TASK-ID.md` for executable
  tasks, including implementation, research, bug-fix, failed-assertion classification,
  and audit work.
- `.agents/retired/` only for completed or retired legacy cards kept temporarily before
  deletion.

Create full-document tracker files with `trackerStatus` frontmatter. Keep metadata such
as `id`, `parents`, `dependsOn`, `title`, `status`, `priority`, `tags`, `complexity`,
`owner`, and `successCriteria` at the top level of the frontmatter. Card IDs must match
their filename stems.

Never use `trackingStatus`. Never call `tracker_create` or `create_task` for
markdown-backed items. The markdown file is the source of truth and syncs into
Nimbalyst.

## Theme grouping

Use theme tags to group active cards into human-reviewable workstreams. Theme tags are
not priority tags; they answer "what kind of work is this?" and make the GUI easier to
filter.

Current category-spec theme tags:

- `theme-category-core`: category objects, Hom objects, End objects, Aut groups,
  standard type packages, and foundational vocabulary.
- `theme-audit-uniformity`: variadic closure, typing uniformity, wrapper cleanup,
  anti-slop checks, import hygiene, and audit cleanup.
- `theme-constructor-routing`: Sage constructor definitions, named constructors,
  refinement declarations, and constructor-obligation recovery.
- `theme-rings-algebras`: rings, fields, algebras, q-adic precision, matrix rings, and
  algebra constructors.
- `theme-modules-tensors`: modules, tensors, lattices, forms, discriminant groups, and
  related methods.
- `theme-sets-topology`: sets, topological spaces, RealSet, ImageSets, Primes, and
  topology-bearing objects.
- `theme-posets-partitions`: posets, semilattices, partitions, set partitions, and
  combinatorial subclass decisions.
- `theme-research-sources`: upstream Sage/source research, theoretical background, and
  backend/library investigation.
- `theme-decisions`: unresolved mathematical or organizational decisions.
- `theme-plan-control`: human-approved plans and sprint-plan coordination.
- `theme-local-cleanup`: isolated local cleanup with limited downstream effect.

Maintain a high-level workstream dependency diagram when many cards are active. The
diagram should live under `.agents/visuals/` and should group dependencies by
workstream or plan, not every individual card.

## Agent skill factoring

Some repeated procedures should live as local agent skills under `.agents/skills/`.
Skills make the procedure partially visible through their descriptions and load the full
instructions only when relevant.

Use this split:

- Keep policy, source-of-truth rules, rubric routing, and current project structure in
  `AGENTS.md`, the canonical category-spec skills, and canonical tracked docs.
- Move repeated operational procedures into skills when agents need to discover and
  execute them on demand.
- Keep skill descriptions specific enough that agents can choose the right skill from
  the available-skill list without loading every document.
- Keep skill bodies procedural and compact. Link back to canonical docs instead of
  duplicating long policy sections.

Good candidates for local skills:

- Creating and normalizing Nimbalyst cards.
- Triage of `.agents/TODO.md` into real cards.
- Applying the category-spec priority and complexity rubrics.
- Preparing high-level workstream dependency visuals.
- Auditing category-spec work against the `category-spec-style` skill.
- Retiring completed cards.
- Preparing plan decomposition after human plan approval.
- Spec authoring and subcategory-definition procedures.
- Sage constructor inventory and mapping workflows.
- Failed category-assertion classification workflows.
- Visual artifact creation for complex system orientation.

Do not factor volatile source-of-truth content into skills. A skill should encode how to
perform a repeatable procedure, not become a second copy of the current plan, current
priority queue, or current mathematical decision.

## Rubric skills

Use the rubric skills instead of duplicating scoring rules in workflow docs:

- Load `category-spec-priority-rubric` before setting or reviewing `priority`.
- Load `category-spec-complexity-rubric` before setting or reviewing `complexity`,
  deciding whether a card is atomic, or promoting/splitting cards.

Priority orders work. Complexity measures execution burden and decomposition pressure.

## Plan creation workflow

Plans are strictly human + LLM collaborative artifacts. An agent may not create an
operative plan unilaterally, hide a plan inside its harness, or proceed from a
chat-local plan into implementation.

Creating or materially revising a plan requires this sequence:

- Switch to planning mode.
- Use the project planning tools and root `.agents/plans/` hierarchy.
- Draft the plan with objective, scope, phases, risks, validation strategy, and known
  task boundaries.
- Iterate with the user until the user explicitly approves the plan.
- Store the approved plan as a tracked `plan` file under the owning feature's
  `.agents/plans/PLAN-ID/` directory.
- Decompose the approved plan into concrete tracked `phase`, `task`, `spec`, and
  `decision` files.
- Move implementation to a separate execution stage, usually delegated for complex
  work.

Use a plan when work is multi-phase, cross-cutting, risky, ambiguous, or too large for
one agent to execute from one card. Use a card directly when the work is clear, bounded,
and independently executable.

## Plan files are the planning system

Trackable plan files are the project planning documents. If an agent harness creates or
stores a plan internally, copy the plan into the project planning system under root
`.agents/plans/`, register it with the plan tracker, and get user approval before enacting it.

Use the built-in `plan` tracker schema for durable initiatives and sprint plans. Keep
plan metadata aligned with `.nimbalyst/trackers/plan.yaml`.

A plan defines the durable objective, phases, milestones, risks, and validation
strategy. Executable units belong in dedicated tracked `task` files under plan phases;
category definitions and operations belong in `spec` files, and unresolved definitions
or owner choices belong in `decision` files.

Do not duplicate one initiative as both a plan and a task. Task files link to the plan;
they do not replace it.

## Human-facing visual artifacts

Use visual artifacts as windows into complex systems. They crystallize structure that is
too hard to understand from code, cards, or kanban alone. Their primary purpose is
orientation: help a human see the shape of a complex codebase, spec tree, plan,
dependency graph, or audit data quickly enough to provide high-level organizational
and directional input.

Visuals support plans, task cards, decisions, audits, and reviews; they do not replace
those tracked files.

Store durable project visuals under `.agents/visuals/` unless Nimbalyst requires a
specific colocated asset path. Link each visual from the plan, task, bug, feature,
decision, or PR it supports.

Use this routing:

- Markdown WYSIWYG red/green diff approval: recommend this when the user and agent need
  several rounds of edits on one document, especially plans, decisions, durable docs,
  organizational policy, and source-of-truth rewrites.
- Mermaid diagrams: use for versionable diagrams that should stay readable in markdown,
  including category inheritance, subcategory-spec organization, constructor routing,
  plan-to-task breakdowns, sprint timelines, dependency digraphs, state machines,
  sequence diagrams, and entity relationships.
- Excalidraw diagrams: use for spatial understanding, ambiguous architecture,
  whiteboarding, decision trees, or diagrams where grouping and visual layout matter
  more than text diff readability.
- Data models: use for structured models that benefit from schema-like editing or
  export, including tracker metadata models, plan/task relationships, dependency
  entities, category/spec object relationships, and audit-state models.
- Mockups: use for cheap HTML views that make a complex system browsable, including
  sprint dashboards, plan decomposition views, audit status pages, category-inheritance
  views, constructor-routing explorers, and review checklists.

Use visuals when they answer one of these questions:

- How does this plan break into tasks, bugs, decisions, and audits?
- Which tasks depend on which decisions or research cards?
- Which subcategories inherit from which category definitions?
- Where does a Sage constructor route in the project model?
- What is blocked, validating, accepted, or awaiting human input?
- Which docs are canonical, superseded, or waiting for migration?
- What high-level organizational or directional question should the human answer before
  agents continue into details?

Keep visual artifacts simple:

- One visual should support one plan, decision, audit, or task cluster.
- Every visual must link back to the tracked file that owns it.
- Do not create visual-only outstanding-work, status, or sprint systems.
- Update or delete visuals when their owning plan/card/decision changes.
- Prefer Mermaid when the diagram should survive code review as plain text.
- Prefer Excalidraw or mockups when spatial understanding or browsability matters more
  than textual diff readability.

## TODO scratchpad and inline task markers

Avoid inline task markers wherever possible. Use `.agents/TODO.md` as the scratchpad
inbox for discoveries that need investigation before they can become real cards.

`.agents/TODO.md` is not an outstanding-work inventory, not a kanban lane, and not an
execution queue. It is a receptacle for unresolved observations that need triage.

Use TODO entries for:

- Tangential inconsistencies discovered during work.
- Smells that may indicate future noncompliance.
- Bugs that need evidence before a bug card can be written.
- Possible decisions whose ownership or stakes are unclear.
- Follow-up research that is too far from the current task.

Do not write TODO entries as executable assignments such as "fix the bug in X". Real
work requires a full task card with context, source provenance, ownership, complexity,
boundaries, and acceptance criteria.

Inline `#task` markers inside other markdown files are allowed only when moving the note
to `.agents/TODO.md` would destroy useful local context. Prefer a TODO entry with source
provenance over inline markers.

Periodically triage `.agents/TODO.md`:

- Convert clear, bounded work into `task`, `spec`, or `decision` files under
  `.agents/plans/features/`.
- Promote multi-phase or ambiguous work into a human-approved plan.
- Keep unresolved observations only when they still need investigation.
- Delete resolved or invalid observations through normal git-reviewed edits.

## Retired card holding area

Keep active repo-local docs forward-facing. Completed cards, rejected cards, superseded
cards, and cards that no longer represent actionable work should leave active task
paths.

Use `.agents/retired/` as a temporary holding area, not a permanent archive. Move a card
there only after one of these is true:

- The work was approved and merged or otherwise accepted by the human.
- The work was rejected and the rejection is recorded in the card, PR, decision, or plan.
- The work was superseded by another card, plan, decision, or canonical doc.
- The card is kept briefly because reviewers may still need local context.

Before retiring a card:

- Record the durable outcome in git commit messages, PR body, linked plan history, or a
  canonical decision/doc.
- Update linked plans, decisions, and follow-up cards.
- Set a terminal status supported by the tracker schema, and add `retired` or
  `superseded` tags when useful.
- Add a short pointer to the merge commit, PR, replacement card, or decision that now
  carries the durable record.

Do not retire durable decisions that still prevent backsliding. Keep active policy,
architecture, naming, workflow, and mathematical-ownership decisions in
`.agents/plans/features/*/decisions/` or promote them into canonical docs. Retire only
decisions whose usefulness is historical and whose effect is already preserved
elsewhere.

Delete retired cards when they no longer answer an active review, recovery, or migration
question. Git history is the archive.

## Full task card requirements

A real executable item must be a full `task` markdown file under
`.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/`. The file must include enough
context for a subagent to execute the work without recovering chat history or guessing
hidden assumptions.

Use these body sections unless a stricter local template applies:

- `Summary`
- `Source Provenance`
- `Context`
- `Mathematical Grounding` for category-spec cards that can affect definitions,
  ownership, invariants, predicates, or morphism semantics
- `Complexity And Ownership`
- `Acceptance Criteria`
- `Dependencies And Boundaries`
- `Validation Requirements`
- `Work Log`

For category-spec cards that can change mathematical meaning, the `Mathematical
Grounding` section must record canonical sources consulted, the exact definition being
specified, owner category or object/morphism, hypotheses and choice-dependence,
return object/codomain, proof obligations for invariance or equivalence claims, and
unresolved decisions or source gaps.

If the grounding section cannot be filled, set the affected card to `blocked` when the
schema supports it and create the decision/source-mining leaf. Do not treat the parent
plan, a vague TODO, a source inventory row, or a plausible common meaning as enough.

Every sprint-scoped task should include `sprintCode`, `planCode`, `workCode`,
`ownerAgent`, `agentRole`, `branchPolicy`, `branch`, `worktree`, `validationStatus`,
`prStatus`, `reviewTier`, `mergeStrategy`, `mergeCommit`, and `slopRisk` when those
values are known. If a value is unknown, explain the blocker in the body rather than
inventing a placeholder.

## Tangential discovery procedure

During work, agents often find inconsistencies, bugs, missing decisions, architectural
smells, stale docs, or possible follow-up research. Handle these findings without
derailing the assigned task.

Use this routing:

- Direct blocker: stop the affected card/path, create or update the relevant `bug`,
  `task`, or `decision` file, set the affected leaf card to `status: blocked` when
  the tracker schema supports it, record the blocking reason in the card body, and
  continue another approved active leaf unless every remaining leaf is also blocked in
  the current phase.
- Clear bounded follow-up: create the full card immediately with source provenance,
  observed evidence, boundaries, and acceptance criteria.
- Vague or investigative follow-up: add a concise entry to `.agents/TODO.md` with the
  source path, observed symptom, why it matters, and what investigation would decide.
- Ambiguous ownership or policy: create a `decision` file if the decision is already
  clear enough to state; otherwise add a TODO entry requesting decision research.
- High-value but tangential investigation: delegate a cheap branching subagent to
  investigate and file the appropriate card, then continue the original task.
- Spec/code mismatch: do not rewrite the spec. Record the mismatch as a `task`,
  `decision`, or TODO entry depending on how well understood it is.

The default is to preserve momentum on the assigned task while making the new work
durable enough that another agent can recover it.

False global blockers during spec work include downstream research guards, QC failures
outside a phase transition or requested QC pass, implementation-only validation checks,
missing backend implementations that can be filed as research/implementation-gap work, and
overscoped cards that can be split or promoted through the approved planning process.

## Delegation contracts

Subagents do not know what a tracker key, task ID, plan label, or chat-local name means
unless the delegation contract provides that meaning or points to a durable artifact
that defines it.

Before delegating, provide:

- The exact task statement or tracker body, not only an identifier.
- The concrete files or directories in scope.
- The allowed and forbidden actions.
- The required source docs to read.
- The expected output format.
- The exit condition.
- The distinction between card-local blockers and global goal exit criteria.

Implementation agents should receive one executable task card and one clear branch or
worktree context. Validators and reviewers should receive the diff, acceptance criteria,
linked plan, and validation expectations.

## Bug workflow

Before fixing a bug:

- Search existing `bug` and relevant `task` files.
- Create a `bug` file if no existing item captures the defect.
- Link the bug to the relevant plan, sprint, source artifact, and failing evidence when
  those exist.

Do not fix a nontrivial bug from chat context alone. The bug card must explain the
observed failure, affected files, expected behavior, boundaries, and validation.

## Agent execution workflow

Each sprint-scoped agent session should link to exactly one tracked task, bug, feature,
or research file.

During execution:

- Record branch and worktree before implementation starts.
- Update `status`, `progress`, `filesChanged`, validation notes, and session IDs as work
  progresses.
- Use `status: blocked` on the affected leaf card when execution cannot proceed until a
  named prerequisite, decision, source, backend, or human input exists. Record the
  exact blocker and the follow-up card/decision/source needed to unblock it.
- Use `validating` or `needs-agent-review` when the implementation appears complete and
  the remaining check is agent-executable. Use `needs-human-input` only when the card
  records an exact human-only decision that remains after source grounding, repo
  policy, and DAG checks.
- Never mark work `accepted`, native items `done`, or sprint plans `closed` without
  human approval.

## Branch and PR policy

Nimbalyst plans and tracks work. GitHub PRs control reviewed merges. Use Nimbalyst
worktrees, file-change tracking, visual diffs, and AI-assisted commit drafting to
prepare clean branches; do not use them to bypass review.

Use `branchPolicy` on every sprint-scoped executable item:

| Policy | Use |
| --- | --- |
| `direct-main` | Tiny reversible administrative changes that are not canonical docs, production logic, active sprint deliverables, or code-path-critical. |
| `local-branch` | Spike, experiment, discarded prototype, or exploratory session. |
| `branch-no-pr` | Throwaway branch used to prepare a later grouped branch. |
| `draft-pr` | Useful but incomplete work needing early reviewer visibility. |
| `formal-pr` | Normal mergeable feature, bug fix, refactor, docs update, or test update. |
| `external-review-pr` | High-risk, ambiguous, security-sensitive, architecture-changing, generated, or AI-slop-prone work. |

Use `formal-pr` or stricter for production logic, future-agent docs, normal docs
updates, tests, refactors, bug fixes, or changes that touch more than one subsystem.

Use `external-review-pr` for public API, schema, data model, permissions, auth,
billing, security, migration logic, canonical-doc rewrites, generated migrations,
generated prose, large diffs, unrelated files, or work that tests alone cannot verify.

Branch names use this form:

```text
spr-YY.NN/<plan-code>/<work-code>-<short-slug>
```

Use this form for spikes:

```text
spike/YY.NN/<work-code>-<short-slug>
```

A branch may contain multiple work items only when the PR says it is grouped and lists
each item.

## Worktree policy

Use a worktree for nontrivial code work, parallel agent sessions, high-risk
implementation, large refactors, experiments, and PR preparation.

Record `branch`, `worktree`, `branchPolicy`, `githubPr`, `prStatus`, `reviewTier`,
`mergeStrategy`, and `mergeCommit` in the linked tracker file as values become known.

## PR lifecycle

Every reviewed PR follows this lifecycle:

```text
branch created
  -> agent implements
  -> local diff reviewed in Nimbalyst
  -> commits cleaned
  -> draft PR opened
  -> CI/checks run
  -> independent review
  -> changes addressed
  -> final docs migration check
  -> human merge
  -> tracker/plan updated
  -> worktree removed or archived
```

A draft PR may become ready only when:

- The branch has no unrelated changes.
- The PR body is complete.
- Acceptance criteria are checked.
- Validation results are listed.
- Stale-document effects are declared.
- Nimbalyst tracker metadata has branch, PR, validation status, and files changed
  populated.

The implementing agent must not self-certify high-risk work. Review high or severe
slop-risk work with a human reviewer, a code owner, or an independent agent session
that receives the PR diff and acceptance criteria rather than the implementation
transcript.

## AI-slop risk

Every executable item should set `slopRisk` when agent-generated implementation,
prose, tests, migration, or policy is involved.

| Risk | Meaning | Required process |
| --- | --- | --- |
| `low` | Small, narrow, easily verified change. | Local diff review or normal PR. |
| `medium` | Bounded generated code or docs. | Formal PR plus tests or documented validation. |
| `high` | Generated refactor, generated docs, migration, public behavior, or ambiguous requirements. | External-review PR. |
| `severe` | Security, auth, data loss, destructive migration, legal/compliance text, or architectural rewrite. | External reviewer, code owner, and explicit human approval. |

Use this validator stance for high-risk reviews:

```text
Review this PR for hallucinated requirements, overbroad implementation, incorrect
assumptions, stale documentation, fake tests, hidden behavior changes, and mismatch with
the linked Nimbalyst plan. Do not assume the implementing agent was correct. Verify from
code, docs, tests, and the PR diff.
```

## Commit discipline

Use Conventional Commit first lines:

```text
<type>(<scope>): <description>
```

Allowed types are `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`, `ci`,
`style`, and `revert`.

Commit bodies should state why the change exists, what changed, validation performed,
and references to sprint, plan, work item, and PR. Keep each commit to one semantic
change unless the PR will squash noisy intermediate commits into a detailed final
message.

Before each commit:

- Review every changed file in the Nimbalyst visual diff.
- Separate unrelated changes.
- Stage only intended files or hunks.
- Let an agent draft the commit message only after staging is correct.
- Human-edit the final message.

Agents must not commit unreviewed generated files, unrelated edits, secrets, temporary
scratch files, obsolete docs without a supersession marker, or unexplained snapshot
updates.

## Documentation lifecycle

Before using a plan or docs file as authority, check its frontmatter. Treat only active
canonical guidance as current. Use archived, superseded, deprecated, and draft files
only as historical context.

Every documentation-changing PR must answer: will this confuse a future agent?

Before merge:

- Search for old names, old commands, old file paths, and obsolete workflow steps.
- Update canonical docs first.
- Move historical docs to archive paths when they should no longer guide new work.
- Add `supersededBy` pointers when preserving history.
- Delete duplicate drafts when they have no archival value.
- Update root `.agents/plans/` and relevant navigation documents.
- Update root `AGENTS.md`, subtree `AGENTS.md`, or the relevant category-spec skill if agent
  behavior changed.
- Update tracker files with final PR and merge metadata.
- Add a `decision` file if the migration changes project policy.

## Completed-work migration

When a PR is merged:

- Set `prStatus: merged`.
- Record `mergeCommit`.
- Set `validationStatus: approved` after approval.
- Mark `status: accepted` only after human approval.
- Append the PR and merge commit to the linked plan history.
- Move completed plans out of active planning only when they no longer control ongoing
  work.
- Remove or archive the worktree.
- Delete the remote branch unless release support needs it.
- Close or defer remaining tracker items.
- Record carryover as new work items, not vague leftovers in old docs.

## Category obligation examples and failed-assertion classification

If design, architectural, layout, or spec violations are known, do not run
category-obligation examples. Resolve those violations first. Example runs against a
flawed architecture produce noise that causes thrash.

Passing status is not the goal. A category-obligation example run exhibits how current
Sage/project implementations satisfy or fail the declared category obligations. Passing
by weakening a spec, bypassing a constructor, catching away an error, or checking a
shallow implementation detail is a regression.

Category assertions should exercise the mathematical claim directly. Prefer
construction calls such as `C.AutCategory().Of(A)` or `C.Constructors().ZZ()` over
proxy checks such as `hasattr(C, "AutCategory")`.

Each subtree's `category_obligations.sage` must:

- Add the repo root to `sys.path` so `category_specs` is importable.
- Import only from this spec hierarchy.
- Declare labeled mathematical statements using `assert_category_statements` from
  `utils.py`.
- Include a statement for every constructor in the subtree's `Constructors()` namespace.
- Let assertion failures exit nonzero.

Failed category assertions and blockers:

- Are recorded as Nimbalyst tracker files, not subtree-local `TRIAGE.md` files.
- Use `task` files under the relevant plan phase for missing methods, failed category
  assertions, structural blockers, and missing category methods or constructors.
- Use `decision` files under the owning feature's `decisions/` directory for unresolved
  definitions or owner choices.
- Cite the source category-obligation file or mapping/inventory document in the
  tracker file.
- Update the tracker file whenever `category_obligations.sage` output changes.

Every subtree's `category_obligations.sage` must be listed in the
`category-obligations` recipe in `category_specs/justfile`.
`just category-obligations` runs all category-obligation example files.
`just test` runs `category-obligations` first, then all `regression/` and `new_spec/`
files.
