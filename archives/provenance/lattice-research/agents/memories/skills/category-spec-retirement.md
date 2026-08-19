---
title: Category Spec Retirement
status: active
date: 2026-05-29
---
# Category Spec Retirement

Use this skill when active cards no longer represent forward-facing work.

## Required references

Before retirement:

- Read `mem:skills/category-spec-workflow`, especially the retired-card policy.
- Read `.agents/retired/README.md`.

## Rules

- Active paths must stay forward-facing.
- `.agents/retired/` is temporary, not a permanent archive.
- Durable history belongs in git commits, PR bodies, plan history, and canonical
  decisions/docs.
- Do not retire decisions that still prevent backsliding; keep them active or promote
  them into canonical docs.

## Retirement steps

- Confirm the work was accepted, rejected, superseded, or no longer actionable.
- Record the durable outcome outside the card.
- Update linked plans, decisions, and follow-up cards.
- Set terminal status supported by the schema.
- Move the card to `.agents/retired/` only while short-term reference is useful.
