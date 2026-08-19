---
description: Track planning work items as markdown files under root `.agents/plans/`.
---

# Tracking Work Items

Create tracking items as markdown files under `.agents/plans/features/` using registered
standard types and tags.

## Registered Types

Read `.nimbalyst/trackers/*.yaml` before creating an item. Use one of the registered
planning types: `feature`, `spec`, `plan`, `phase`, `decision`, or `task`.

Use schema fields, not tags, for co-mathematician workflow dimensions. Substantial
research tasks classify `activityType`, `workstreamRole`, `claimStatus`,
`uncertaintyState`, `paperAnchors`, and `reportArtifacts`. Use tags only for feature,
plan, phase, and theme ancestry.

## Destination Rules

- `.agents/plans/features/FEATURE-ID/FEATURE-ID.md`: feature cards.
- `.agents/plans/features/FEATURE-ID/specs/SPEC-ID.md`: spec cards owned by a feature.
- `.agents/plans/features/FEATURE-ID/decisions/DECISION-ID.md`: decision cards owned by a feature.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PLAN-ID.md`: plan cards.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/PHASE-ID.md`: phase cards.
- `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/TASK-ID.md`: executable task cards.

Use phase cards with `phaseKind: workstream` for co-mathematician workstreams. Do not
create a separate plan-level `workstreams/` hierarchy unless the validator and schema
are migrated first.

Before creating a task, explicitly identify the owning feature, plan, and phase. The
phase card must already exist at the phase path and declare `trackerStatus.type: phase`.
If no phase owner exists, stop and create or repair the phase card first. Never create
`.agents/plans/features/FEATURE-ID/plans/PLAN-ID/tasks/TASK-ID.md`; a plan-level `tasks/`
directory is evidence that the phase gate was skipped.

Do not create aggregate tracker indexes. The GUI is the index. There is no separate
backlog; active tracked cards under `.agents/plans/features/` are the outstanding work set.

## Frontmatter

Use `trackerStatus`, not `trackingStatus`. Card IDs must match filename stems.

```markdown
---
id: TASK-EXAMPLE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: Brief executable description
status: unstarted
priority: medium
description: Brief executable description.
activityType: source-mining
workstreamRole: literature
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- Observable acceptance criterion.
complexity: 40
---
```

The `trackerStatus.type` value must match a registered schema. Keep metadata compact;
put detailed grounding, acceptance criteria, examples, audit notes, and work logs in
the body.

For category-spec cards, load `category-spec-priority-rubric` before setting `priority`
and `category-spec-complexity-rubric` before setting `complexity`. Do not encode
priority or complexity as tags.

## Body Requirements

Full-document bodies must include enough context for another agent to act without chat
recovery. Use at least:

- `Summary`
- `Source Provenance`
- `Context`
- `Acceptance Criteria`
- `Dependencies And Boundaries`
- `Work Log`

Inline tracker syntax is only for temporary discovery placeholders. Convert anything
ready for assignment or execution into a full markdown file under `.agents/plans/features/`.

## Execution Steps

1. Read `.nimbalyst/trackers/*.yaml`.
2. Select a registered standard type.
3. Convert workflow words such as spec, implementation, research, or sprint into tags
   and destination path.
4. For `task` cards, confirm the owning phase exists and that the destination is the
   phase's `tasks/` directory.
5. For substantial research tasks, choose the `activityType`, `workstreamRole`,
   `claimStatus`, and `uncertaintyState` from the task schema.
6. Generate the item file under `.agents/plans/features/` with `trackerStatus` frontmatter.
7. Preserve source provenance and enough execution context in the body.
8. Confirm the destination file.
9. Update `.agents/memories/current-goal-handoff.md` — the new task altered the
   resumption path. Handoff update is not optional; do it before reporting in chat.

## Hard Constraint

Never call `tracker_create` or `create_task`. The markdown file is the source of truth;
calling a tracker tool creates duplicates.

## Sizing

A task is atomic when a subagent with zero repo context, given only the card
body and artifact paths, can complete it in one pass without discovering scope,
making classification decisions, or synthesizing cross-subtree findings.

Before creating a task, ask: can the subagent start work immediately after
reading the card? Or does it first need to figure out what to do?

**Not atomic:** "Audit all super_categories() in category_specs/" — this is a
plan-level objective (it's the purpose of the entire PLAN-STATIC-CATEGORY-
REFINEMENT-ORDER). A task card that restates the plan's objective as a single
task is a category error — the task is pretending to be the plan.

**Atomic:** "Grep category_specs/rings/ for super_categories(, extract each
returned list, write a table into the plan body" — the subagent reads the card,
runs the grep, writes the table. No discovery, no classification, no synthesis.

**Concrete test:** if the card body contains the word "all" followed by a
directory path spanning multiple subtrees, it's a survey. Split by subtree.
If the card asks the subagent to "determine," "classify," "decide whether,"
or "cross-reference," those are coordinator-level judgments — the coordinator
does that work, the subagent executes the mechanical step.
