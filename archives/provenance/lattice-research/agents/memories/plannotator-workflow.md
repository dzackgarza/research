---
title: Plannotator Workflow
status: active
date: 2026-05-29
---
# Plannotator Workflow

Core principle: Plans are living documents, revised iteratively through readable diffs.
The user reviews incremental changes in a diff view, not wholesale rewrites.

## CLI-First Architecture

All operations use the `plannotator` CLI via bunx:

```bash
bunx github:dzackgarza/plannotator-dzg-fork#main submit plan.md
bunx github:dzackgarza/plannotator-dzg-fork#main status
bunx github:dzackgarza/plannotator-dzg-fork#main wait
```

The CLI is harness-agnostic — works with Claude Code, OpenCode, or any agent system.

## Plan File Location

Durable plan files must exist on disk.
Plans are markdown documents submitted for human review.

## Workflow

1. Write/revise plan as markdown
2. `submit` the plan for review
3. User reviews diff in their interface
4. `wait` for user decision (approved/rejected/revision)
5. Iterate
