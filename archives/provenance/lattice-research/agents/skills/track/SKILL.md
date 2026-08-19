---
name: track
description: Use when creating tracking items from `/track` commands. Map requests to central planning tracker types and write markdown under root `.agents/plans/`.
---

# /track Command

Create a tracking item in the correct `.agents/plans/` location.

## Usage

```text
/track [type] [description]
```

Examples:

- `/track task Remove raw ConditionSet from public Aut surface`
- `/track spec Specify finite ordered partition base-set ownership`
- `/track decision Decide where Hom/End/Aut ownership belongs`

## Registered Types

Read `.nimbalyst/trackers/*.yaml` before creating an item. Use one of the registered
planning types: `feature`, `spec`, `plan`, `phase`, `decision`, or `task`.

## Destination Rules

- Feature cards go under `.agents/plans/features/FEATURE-ID/`.
- Specs go under `.agents/plans/features/FEATURE-ID/specs/`.
- Decisions go under `.agents/plans/features/FEATURE-ID/decisions/`.
- Plans go under `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/`.
- Phases go under the owning plan directory.
- Tasks go under the owning phase directory.

Do not create aggregate index files. The GUI is the index. There is no separate
backlog. Active tracked cards under `.agents/plans/features/` are the outstanding work set.

## Frontmatter

Use `trackerStatus`, not `trackingStatus`.

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
successCriteria:
- Observable acceptance criterion.
complexity: 40
---
```

Card IDs must match filename stems. Put `title`, `status`, `description`,
`successCriteria`, `priority`, `complexity`, and other fields at the top level of the
frontmatter. Keep metadata compact and put detailed evidence in the body.

## Body Requirements

Full-document task bodies must include enough context for another agent to act without
chat recovery. Use at least:

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
2. Map the requested type to a registered standard type.
3. Convert workflow words such as spec, implementation, research, or sprint into tags
   and destination path, not tracker types.
4. Generate the item file under `.agents/plans/features/` with `trackerStatus` frontmatter.
5. Preserve source provenance and enough execution context in the body.
6. Confirm the destination file.

## Migration Requirements

When migrating existing docs, preserve substantive context in the full-document body:
source paths, original heading or line, acceptance criteria, and known boundaries.
Never collapse real work into a one-line tracker row.

## Hard Constraint

Do not call `tracker_create` or `create_task`. The markdown file is the source of truth;
calling a tracker tool creates duplicates.
