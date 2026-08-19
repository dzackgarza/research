---
title: Category Spec Triage
status: active
date: 2026-05-29
---
# Category Spec Triage

Use this skill for project-management triage of `category_specs` work.
This skill routes agents to the canonical workflow skill.

## Required references

Read `mem:skills/category-spec-workflow` before changing card metadata.

Use the workflow reference for:

- Theme grouping for `theme-*` workstream tags.
- TODO scratchpad and inline task marker policy.
- Retired-card holding policy.
- Human-facing visual artifact policy.

Load rubric skills directly when scoring cards:

- Read `mem:skills/category-spec-priority-rubric` for `priority`.
- Read `mem:skills/category-spec-complexity-rubric` for `complexity` and split/promote
  decisions.

## Rules

- Encode priority only in the `priority` field.
- Encode complexity only in the `complexity` field.
- Do not create `priority-*` or `complexity-*` tags.
- Use tags for topic, domain, workstream, and workflow class.
- Use `.agents/visuals/` for high-level dependency views.
- Keep active cards forward-facing; move resolved cards to `.agents/retired/` only
  temporarily.
- Do not create a separate backlog.

## Triage steps

- Confirm every active card has `trackerStatus`, `status`, and topic/workstream tags.
- Confirm task-like cards have `priority` and `complexity` metadata.
- Group cards with `theme-*` tags when free-floating work becomes hard to review.
- Update or create a high-level dependency graph when priority depends on workstream
  ordering.
- Convert clear `.agents/TODO.md` entries into real cards.
- Retire or delete resolved cards after durable history is recorded elsewhere.
