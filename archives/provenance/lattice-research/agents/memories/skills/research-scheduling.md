---
title: Research Scheduling
status: active
date: 2026-05-29
---
# Research Scheduling

This skill is the canonical scheduling and cadence policy for the research repo.

## Canonical source

The source of truth is this skill plus `references/cadence.md`.

Read `references/cadence.md` before creating recurring schedules, replacing daily
rotations, planning autonomous maintenance, waking an agent for follow-up, or deciding
whether a scheduled action should exist.

## Core policy

- Scheduling serves `.agents` plans/cards, git/PR state, and user-approved maintenance.
  It is not a separate authority.
- Fixed wall-clock rotations do not decide priority.
  Active cards, approved plans, dependency structure, proof risk, and human direction
  do.
- One-shot wakeups are acceptable for delayed continuation or external-process polling.
- Recurring schedules require a linked card, plan, PR/check transition, maintenance
  policy, or explicit user-approved automation.
- Every scheduled action needs an owner, purpose, removal condition, and expected next
  action.
- Do not schedule destructive cleanup, proof acceptance, or policy rewrites without
  current authorization and the relevant skill gates.

## Load with

- Load `scheduling-tasks-and-subagents` for concrete `at` or `task-sched` command
  mechanics.
- Load `research-project-workflow` to create or update linked cards/plans.
- Load `research-state-machine` when scheduled work will move a card through execution,
  replay/attack, promotion, rejection, or splitting.
- Load `research-proof-auditing` when the scheduled work audits proof or computation
  evidence.
- Load `research-repo-structure` before scheduled cleanup or pruning.

## Referenced documents

[Research Scheduling Cadence](research-scheduling/cadence)
