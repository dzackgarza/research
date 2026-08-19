# Research Project Workflow Reference

## Nimbalyst tracker workspace

All active planning, spec, task, and decision documents for this repo live under root
`.agents/plans/` and follow the central planning hierarchy:

```text
.agents/plans/features/FEATURE-ID/
├── FEATURE-ID.md
├── specs/SPEC-ID.md
├── decisions/DECISION-ID.md
└── plans/PLAN-ID/
    ├── PLAN-ID.md
    └── PHASE-ID/
        ├── PHASE-ID.md
        └── tasks/TASK-ID.md
```

Use `.agents/current-goal-phase.md` to identify the active staged-program phase. Use
`.agents/retired/` only for short-lived retired legacy cards. Do not create
`nimbalyst-local/tracker` indexes or parallel task inventories. The GUI is the index.

There is no separate backlog. The active tracked cards under `.agents/plans/features/` are the
outstanding work set. Completed feature trees should be moved under
`.agents/plans/features/completed/` rather than left beside active feature roots. When work is
implemented, resolved, rejected, or superseded, move the card out of active paths and
retire, archive, or delete it according to the retired-card policy for that tracker
layer.

A plan is not a task container. A plan defines high-level phases and milestones. Each
execution item must exist as its own dedicated tracked file under a phase directory.
The path `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/tasks/TASK-ID.md` is forbidden. If a
plan-level `tasks/` directory exists, treat it as a process failure: do not add more
cards there, and do not merely move the symptom without checking the workflow rule that
allowed it. First repair the phase breakdown and process guidance, then migrate cards
with provenance.

## Source order and local choices

Use these sources in order when interpreting or editing planning cards:

- `/home/dzack/ai/planning/AGENTS.md` defines the reusable card framework:
  hierarchy, layer gates, decision-card discipline, generated tags, no-fallback
  validation, and card responsibilities.
- `.agents/plans/AGENTS.md` defines this repo's local feature buckets, active root, and
  validation command.
- `.nimbalyst/trackers/*.yaml` defines the installed schema fields and allowed status
  values.
- `GOAL.md` and `.agents/current-goal-phase.md` define the staged mathematical phase
  gate. They do not become active tracker features.

The local schemas intentionally extend the reusable framework in small ways: blocked
statuses on feature/spec cards, priority and owner metadata on plan/phase/task cards,
and complexity on specs/tasks. Do not overwrite local schemas with central copies
unless the user explicitly asks for a schema migration. If the reusable framework and
local schema disagree, the local schema controls valid frontmatter while the reusable
framework controls workflow semantics unless repo policy is stricter.

## Standard tracker types

Accepted planning `trackerStatus.type` values are the registered central schemas in
`.nimbalyst/trackers/*.yaml`: `feature`, `spec`, `plan`, `phase`, `task`, and
`decision`.

Use containment and `dependsOn` as the primary workflow axes. Generated tags come from
feature, plan, and phase ancestry; do not manually maintain status rollups in card
bodies.

## Tracker frontmatter

Use YAML frontmatter and keep metadata in `trackerStatus`, not `trackingStatus`.

```markdown
---
id: TASK-REMOVE-RAW-CONDITIONSET-FROM-AUT-CATEGORY-SURFACE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: Remove raw ConditionSet from Aut category surface
status: unstarted
priority: medium
description: Replace the public ConditionSet surface with an explicit typed object.
successCriteria:
- Public Aut-category APIs no longer expose raw ConditionSet values.
complexity: 40
---
```

The `trackerStatus.type` value must match a registered schema. Card IDs must match
filename stems. Use `parents` for containment and `dependsOn` for blocking relations.

Metadata fields should stay compact. Put complex explanations, full acceptance
criteria, gates, tables, diagrams, examples, and other structured markdown in the body.

For substantial research plans, treat intake, workstream, paper, agent-organization,
and uncertainty metadata as part of the contract, not as decoration. A plan that opens
a new research direction, changes the active mathematical strategy, or coordinates
multiple agents must record:

- `intakeStatus`: whether the human-approved research question and goals are settled.
- `onboardingArtifact`: the durable intake artifact that records the refined question,
  goals, non-goals, source context, and hard constraints.
- `workingPaper`: the LaTeX paper path that receives synthesized claims and margin
  notes.
- `workstreamPolicy`: how branches divide the work, such as literature/theory,
  prove/disprove, computation/implementation, review, or synthesis.
- `agentOrganization`: which repo-local agent roles may be delegated and what they own.
- `uncertaintyPolicy`: how disputed claims, failed branches, stalled reviews, and
  human-escalation points will be surfaced.

For workstream phases, set `phaseKind: workstream` and record:

- `branchType`: the branch's primary mode, such as prove, disprove, literature,
  theory, computation, implementation, formalization, synthesis, audit, or exploration.
- `agentRoster`: the specialist roles assigned to the branch.
- `reportArtifact`: the workstream report path.
- `paperSections`: paper sections this branch may update.
- `uncertaintySummary`: the branch's current rigor state.
- `failedExplorations`: negative results worth preserving.

For substantial research tasks, record the task's role in the workstream and the
status of its claims:

- `activityType`: the kind of mathematical work being done, including intent
  refinement, literature search, source mining, brainstorming, conjecture generation,
  counterexample search, proof attempt, proof repair, formalization, computation,
  numerical experiment, simulation, implementation, validation, citation check,
  synthesis, exposition, review, failure analysis, or user escalation.
- `workstreamRole`: the task's function in the branch structure.
- `claimStatus`: the strongest claim currently supported by the task's evidence.
- `uncertaintyState`: the current uncertainty lifecycle state.
- `paperAnchors`: paper labels, sections, or margin notes affected by the task.
- `claimRefs`: claim identifiers or local theorem/lemma labels affected by the task.
- `uncertaintyNotes`: specific disputed assumptions, review concerns, missing sources,
  or human questions.
- `reportArtifacts`: durable write-ups, notebooks, proof logs, source maps, or other
  native mathematical artifacts produced by the task.
- `failedExplorations`: failed approaches worth preserving because they constrain the
  next attempt or prevent repeated work.

These fields are forward process requirements for new substantial research work. Do
not omit them merely because older cards predate the schema. Small administrative
cards may mark the fields not applicable in the body when the reason is obvious.

When an active card cannot proceed, set `status: blocked` if its tracker schema
supports that value, record the exact blocker in the body, and link or create the
prerequisite task, research item, or decision. A blocked card remains active until it is
accepted, rejected, or superseded.

Do not mark a card `blocked` merely because one of its declared `dependsOn` edges is
incomplete. That is ordinary DAG ordering, not a blocker. If the dependency chain is
not yet discharged, the downstream card is still `unstarted` and should not be
attempted yet.

Use `blocked` only for a card that would otherwise be the next ready leaf in the
current phase, but cannot proceed because it needs an external decision, unavailable
source, missing credential, unresolved theory obligation, missing backend proof, or
another prerequisite that is not currently satisfiable by simply completing upstream
cards in the DAG.

## Layer-gated workflow

Build and approve cards top-down. Approval is local to the layer being approved.

- Feature/spec gate: write the feature card and durable spec cards before
  implementation planning. The feature defines the user or research outcome, scope,
  non-goals, contracts, and major links. Specs define stable observable requirements
  and verification obligations that remain true if the implementation plan changes.
- Plan gate: after feature/spec approval, create sibling plan cards under the feature.
  A plan designs milestone phases, sequencing, scope boundaries, validation
  expectations, risks, and expected drill-down shape. It must not become a task index.
- Phase gate: after plan approval, create phase cards under the owning plan. A phase
  converts one milestone into task-card design, resolves local operational decisions,
  records ordering constraints, and defines phase acceptance gates.
- Task gate: after the phase breakdown is accepted, create task cards under the
  phase's `tasks/` directory. A task is the executable contract: exact objective,
  allowed scope, dependencies, acceptance checks, and verification command or proof
  artifact.

Task creation has a mandatory phase-owner preflight. Before writing the file, name the
owning feature, owning plan, owning phase, and exact destination path. Confirm the
phase card exists and has `trackerStatus.type: phase`. If that check fails, stop at the
phase gate and create or repair the phase card; do not create a task directly under the
plan.

Execution order is constrained by the DAG. Do not start a task while any declared
dependency remains incomplete. Downstream tasks wait in `unstarted` status until their
incoming dependency edges are discharged.

Do not create tasks first and backfill higher layers. Do not use plans above plans to
simulate feature hierarchy. Do not approve a phase for execution while child tasks
still contain unresolved decisions.

## Decision-card discipline

Unresolved decision language is not durable card content. Phrases such as "decide
whether", "choose an approach", "TBD", "figure out", "investigate and implement", or
"handle appropriately" must be resolved at the current layer or converted into a
feature-level decision card.

Use a decision card only when work cannot continue because the answer does not follow
from approved cards, repo policy, existing contracts, or canonical mathematical
sources. Place it under `.agents/plans/features/FEATURE-ID/decisions/`, parent it to the
feature, link blocked cards with `dependsOn`, and mark only the actually blocked cards
`blocked`.

When a decision is made, record the chosen contract in the dependent feature/spec/plan,
phase, or task body. The decision card stores the decision question, constraints,
options, and chosen answer; it does not become an implementation plan.

## Inline items

Avoid inline items in general. Use inline entries only as temporary placeholders while
a broader task is being discovered and a full tracker file is being prepared.

Inline items define a task but provide little context by construction. Any inline item
that is ready to be solved, assigned, or actively worked on must be converted into a
full markdown file under `.agents/plans/features/.../tasks/` before execution.

Do not call `create_task` or `tracker_create` for inline items. That creates a
database-only entry with no backing file and produces a duplicate.

## Card responsibilities and progressive disclosure

Use root `.agents/plans/` for Nimbalyst-backed planning documents. Plans are strictly human +
LLM collaborative artifacts. To create or materially revise a plan, switch to planning
mode, use the planning tools, iterate with the user until approval, then decompose the
approved plan into tracked phase and task files. Do not enact a chat-only,
harness-local, scratch, or unapproved plan.

Plan placement follows the hierarchy in `.agents/plans/AGENTS.md`. Root features own sibling
plans. Plans own phases. Phases own tasks. Specs live under the owning feature's
`specs/` directory, and decisions live under the owning feature's `decisions/`
directory.

The staged program remains explicit in `GOAL.md` and `.agents/current-goal-phase.md`,
while the active planning corpus lives under `.agents/plans/features/`.

Write each card for its own level:

- Feature cards own the feature boundary, outcome, scope, non-goals, major contracts,
  and links to specs and plans.
- Spec cards own durable requirements, public contracts, acceptance criteria, and
  verification obligations. They must not depend on phase names, phase order, task
  layout, or current implementation sequencing.
- Plan cards own phase design: phase outcomes, scope boundaries, todo clusters,
  dependencies, validation expectations, risks, and drill-down shape. They may mention
  representative task shapes, but they must not author task cards.
- Phase cards own local task design, task links, ordering constraints, phase
  acceptance gates, and audit checks. A phase may also be a workstream; in that case it
  owns branch type, report artifact, agent roster, uncertainty summary, and paper
  section links. It must not manually track child task completion percentage.
- Task cards own executable implementation or research work. They must be specific
  enough that an agent can act without deciding product behavior, mathematical
  definitions, architecture, scope, sequencing, or acceptance criteria.

Use workstreams to keep progressive disclosure real. The project coordinator or plan
card owns the high-level question, goals, branch structure, and escalation policy. A
workstream task owns one linear investigation path and writes a concise report artifact
with internal links to sources, computations, proof attempts, and review notes. Do not
mix low-level agent execution logs into plan prose; link the artifact and summarize the
current claim state.

Failed workstreams are outcomes. If a branch finds a false conjecture, an exhausted
strategy, an unfixable proof gap, or a computational bottleneck, preserve the reason in
`failedExplorations` or a dedicated failure-record task. Do not silently restart a new
branch with the same assumptions.

Avoid inline task markers. Use `.agents/TODO.md` only as a scratchpad inbox for
tangential discoveries that need investigation before they can become real cards.
Convert anything executable into a full tracked file with context, source provenance,
boundaries, and acceptance criteria before assignment.

Subtree `AGENTS.md` files may stay small by delegating detailed policy to local skills
and skill-local references. Agents must load those skills when their task matches the
documented trigger.

## Validation and generated planning data

Run `just plan-validate` from the repo root after editing planning cards, local tracker
schemas, `.agents/plans/AGENTS.md`, or `.agents/current-goal-phase.md`. That recipe must
delegate to `/home/dzack/ai/planning/justfile validate`; the centralized validator is
the only planning validation authority. Do not add repo-local relaxed validators,
alternate pass/fail definitions, or warning-only schema checks.

If validation reports task cards placed directly under a plan-level `tasks/` directory,
treat that as a broken phase-gate process, not as ordinary card cleanup. Repair the
process rule or decomposition gap first, then move the task cards under real phase
owners.

For diagnosis, you may run the reusable framework recipe explicitly with absolute repo
paths. The reusable justfile executes from `/home/dzack/ai/planning`, so relative
project paths will not resolve correctly.

```bash
just --justfile /home/dzack/ai/planning/justfile validate /home/dzack/research/.agents/plans/features /home/dzack/research/.nimbalyst/trackers /home/dzack/research/.agents/plans/plan-dag.md
```

The centralized recipe derives structural tags, checks schemas, and regenerates
`.agents/plans/plan-dag.md`. The local planning workflow also generates
`.agents/plans/card-progress-report.md` as a user-facing Markdown summary of current card
state. During manual validation or report-generation runs, inspect generated tag, DAG,
and report changes before staging them. During commit hooks, generated planning
artifacts are hook-managed and automatically staged into the commit. Do not replace
validation failures with warnings, fallback groups, or project-local quick checks.

Do not add timestamp metadata such as `created` or `updated` to card frontmatter unless
the installed schema declares those fields. Strict validation treats undeclared metadata
as invalid card data; remove the card fields rather than expanding schemas to admit
accidental metadata.

Recommended local hook behavior: run the reusable validation recipe from pre-commit
when staged planning cards or tracker schemas change, and from post-merge/post-checkout
when the changed paths include `.agents/plans/features/`, `.agents/plans/AGENTS.md`,
`.agents/plans/plan-dag.md`, `.nimbalyst/trackers/`, or `.agents/current-goal-phase.md`. Hooks
should fail on validation errors. If a hook regenerates tags, `.agents/plans/plan-dag.md`, or
`.agents/plans/card-progress-report.md`, it should automatically stage those generated changes
so the commit records the canonical planning state.

## Quick card queries

Use these from the repo root for quick status reads. They are suggested ad hoc queries,
not new source-of-truth scripts.

List every card as status, type, id, title, path:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import re,yaml; rows=[(fm.get("status",""),fm.get("trackerStatus",{}).get("type",""),fm.get("id",""),fm.get("title",""),str(p)) for p in sorted(Path(".agents/plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}]]; print("\n".join("\t".join(map(str,row)) for row in rows))'
```

List cards with a specific status; change the `status` literal as needed:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import re,yaml; status="blocked"; rows=[(fm.get("trackerStatus",{}).get("type",""),fm.get("id",""),fm.get("title",""),str(p)) for p in sorted(Path(".agents/plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}] if fm.get("status")==status]; print("\n".join("\t".join(map(str,row)) for row in rows))'
```

Count cards by type and status:

```bash
uvx --with pyyaml python -c 'from pathlib import Path; import collections,re,yaml; counts=collections.Counter((fm.get("trackerStatus",{}).get("type",""),fm.get("status","")) for p in sorted(Path(".agents/plans/features").rglob("*.md")) for m in [re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", p.read_text(encoding="utf-8"), re.S)] if m for fm in [yaml.safe_load(m.group(1)) or {}]); print("\n".join(f"{kind}\t{status}\t{count}" for (kind,status),count in sorted(counts.items())))'
```

List active leaf cards, meaning cards with no child containment references and status
not in a completion status:

```bash
uvx --with pyyaml python -c 'exec("from pathlib import Path\nimport re,yaml\ncomplete={\"complete\",\"done\",\"decided\",\"implemented\"}\nrecords={}\nchildren=set()\ndef ref(v):\n    if isinstance(v,str): vals=[v]\n    elif isinstance(v,list): vals=v\n    else: vals=[]\n    return [x[2:-2] if isinstance(x,str) and x.startswith(\"[[\") and x.endswith(\"]]\") else x for x in vals if isinstance(x,str)]\nfor p in sorted(Path(\".agents/plans/features\").rglob(\"*.md\")):\n    m=re.match(r\"^---\\r?\\n(.*?)\\r?\\n---\\r?\\n?\", p.read_text(encoding=\"utf-8\"), re.S)\n    if not m: continue\n    fm=yaml.safe_load(m.group(1)) or {}\n    cid=fm.get(\"id\")\n    if cid: records[cid]=(p,fm)\nfor cid,(p,fm) in records.items():\n    children.update(parent for parent in ref(fm.get(\"parents\")) if parent in records)\nrows=[]\nfor cid,(p,fm) in records.items():\n    if cid not in children and fm.get(\"status\") not in complete:\n        rows.append((fm.get(\"status\",\"\"),fm.get(\"trackerStatus\",{}).get(\"type\",\"\"),str(fm.get(\"complexity\",\"\")),fm.get(\"priority\",\"\"),cid,fm.get(\"title\",\"\"),str(p)))\nprint(\"\\n\".join(\"\\t\".join(map(str,row)) for row in rows))")'
```

## Visual windows

Use `.agents/visuals/` for optional human-facing windows into complex systems. Visuals
are supporting material only; the operative state remains in tracked feature, spec,
plan, phase, task, and decision files under `.agents/plans/features/`.
