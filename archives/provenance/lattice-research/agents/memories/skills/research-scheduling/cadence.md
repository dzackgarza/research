# Research Scheduling Cadence

Scheduling is not a parallel planning system. It is a way to wake agents, run periodic checks, or rotate attention across active `.agents` work without losing the Nimbalyst source of truth.

## Source of truth

Use `.agents` plans, cards, decisions, TODO scratchpad entries, and current git/PR state to decide what should run. Do not use fixed time slots as authority over priorities.

A scheduled action must point to one of:

- an approved plan,
- an active tracked card,
- a concrete PR/check/review transition,
- a maintenance policy in a skill,
- a user-approved recurring automation.

If no source object exists, create or update the card first unless the action is a one-shot wakeup for the current session.

## Cadence model

### Startup steering

At session startup, read `AGENTS.md`, `GOAL.md`, current Nimbalyst state, and the relevant skill index. Load only the skills needed for the chosen work. Do not start a broad repo sweep.

### Card-driven work blocks

Select work from active `.agents` cards by dependency, the relevant priority-rubric
skill, current plan, and human direction. Execute through `research-state-machine` when
work moves from planning to implementation or claim promotion.

### Scheduled wakeups

Use one-shot wakeups for delayed continuation, long-running external processes, or follow-up after expected user/tool availability. Use recurring schedules only for persistent maintenance that has a card or approved automation policy.

Every scheduled wakeup must have an owner, purpose, linked card/plan when applicable, removal condition, and expected next action.

### Maintenance passes

Run maintenance because evidence calls for it, not because a wall-clock slot says so. Valid triggers include repeated agent failure patterns, stale active cards, unresolved TODO scratchpad entries, PR/check transitions, suspected drift from `GOAL.md`, recurring proof-audit failures, and dependency/source freshness risks.

### Audit passes

Audit passes must load `research-proof-auditing` and target claims, scripts, PRs, or cards that are trying to promote evidence. Do not perform destructive audit cleanup from a schedule without provenance and current user authorization.

## What replaced the old fixed rotation

The old schedule encoded useful categories: cleanup, policy improvement, literature, adversarial audit, goal alignment, memory maintenance, foundation work, tooling, transcript review, mathematical work, and Lean formalization.

Those are now work classes, not fixed time slots. Route them through these skills:

- Cleanup and artifact placement: `research-repo-structure`.
- Policy improvement and agent-facing docs: skill-specific editing plus `research-project-workflow`.
- Literature and references: literature-focused skills plus `research-math-boundary`.
- Proof or computation audit: `research-proof-auditing`.
- Goal alignment and plan/card routing: `research-project-workflow` and `research-state-machine`.
- Memory maintenance: `agent-memory` when memory policy applies.
- Foundation and mathematical base work: `research-math-boundary`.
- Tooling or scheduled wakeups: `scheduling-tasks-and-subagents` plus this skill.
- Category-spec work: the relevant `category-spec-*` skill.

## Scheduling hygiene

Do not create orphaned wakeups. Remove recurring schedules when their linked card, PR, or process is resolved.

Do not schedule broad destructive cleanup, unsupervised proof acceptance, or autonomous policy rewrites. Schedule investigation or review, then route findings through cards, PRs, decisions, or skills.

Scheduled commands run in reduced environments. Use the general `scheduling-tasks-and-subagents` skill for concrete `at` or `task-sched` command mechanics.
