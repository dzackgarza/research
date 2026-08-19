---
name: research-state-machine
description: Use when moving research work from plan to execution, deciding whether
  a card is atomic, routing implementation/self-check/adversarial audit, promoting
  or rejecting results, or claiming GOAL.md discharge.
---

# Research State Machine

This skill is the canonical execution-state authority for the research repo.

## Canonical source

The source of truth is this skill plus `references/execution-kernel.md`, `references/review-kernel.md`, and `references/upstream-gates.md`.

For substantial mathematical research directions, interpret this state machine through
`research-co-mathematician-workflow`: intake, workstreams, living-paper artifacts,
uncertainty lifecycle, and failed-exploration records are part of execution state.

Read `references/execution-kernel.md` before moving work from planning into execution, delegating implementation, judging whether a card is atomic, routing replay/attack, accepting/rejecting/splitting work, or claiming parent-plan or `GOAL.md` discharge.

Read `references/review-kernel.md` before reviewing any card in `needs-agent-review` or `needs-human-input` status, applying the ordered gate protocol, or moving a card to `revision-required`, `complete`/`done`, or `blocked`.

Read `references/upstream-gates.md` before approving a feature, spec, or plan. These gates ensure each card is complete enough to unambiguously drive the next stage: feature → spec → plan → autonomous task execution.


## Core model

- Nimbalyst plans and cards are the task specs. IWE is the markdown query and resume layer over those specs, memories, and handoff notes; it is not a replacement tracker.
- Git branches, PRs, commits, and worktrees are the provenance and review layer.
- Produced proof/computation/code artifacts live in their natural durable roots.
- Proof and evidence sufficiency is governed by `research-proof-auditing`.
- Heavy controls trigger only when theorem burden, parent-plan discharge, or `GOAL.md` discharge is being promoted.

## Live stages

- Plan: collaborate with the human and approve complex plans before decomposition.
- Intake: for substantial research directions, settle the user's question, goals,
  non-goals, success criteria, hard constraints, branch structure, and uncertainty
  policy before opening workstreams.
- Specify card: create a tracked card with exact claim/work target, scope, provenance, dependencies, acceptance criteria, and verification plan.
- Preflight: reject or split hidden-major-work cards before execution.
- Execute: run scoped implementation or one linear research workstream in the required
  branch/worktree, produce native artifacts, and update card metadata.
- Review: apply the six ordered gates from `references/review-kernel.md`. Determine whether the card is `complete`/`done`, `needs-human-input` (human decision needed), `revision-required` (rework needed), or `blocked` (prerequisite missing).
- Promote, reject, split, or retire: human-gated promotion; otherwise split or reject and keep active paths forward-facing.

Failed branches are outcomes. Preserve failed proof strategies, false conjectures,
exhausted searches, missing-source dead ends, and reviewer non-termination in the card,
workstream report, or living paper instead of silently restarting.

## Hard stops

- Do not execute an unapproved complex plan.
- Do not one-shot an overscoped card that hides major theorem, algorithm, convention, classification, or trusted-base work.
- Do not execute a mathematical spec card whose definitions, hypotheses, return
  objects, and invariance/equivalence obligations are not grounded in canonical repo
  theory, references, Sage docs/source, spec backups, or an approved decision.
- Do not patch around missing mathematical vocabulary or missing trusted-base operations.
- Do not let an implementing agent mark work accepted, done, or closed.
- Do not claim `GOAL.md` discharge without final composed-goal audit and human approval.
- Do not treat ordinary DAG sequencing as blockage. If a card still has incomplete
  declared dependencies, it remains `unstarted`; `blocked` applies only when a ready
  leaf cannot proceed because of an external unsatisfied prerequisite.

Hard stops are scoped to the affected card, path, or promotion claim unless the current
approved phase has no other executable leaves. When a hard stop fires, file or update
the prerequisite card/decision/research item, then continue another approved active
leaf. Do not exit the user's active goal merely because one path is blocked.

Before reporting that all paths are blocked, enumerate the approved active plans and
leaf cards considered, name each current-phase blocker, and exclude downstream guards,
non-transition QC failures, and implementation-only gates that do not apply to current
spec work.

## Load with

- Load `research-project-workflow` for Nimbalyst plan/card mechanics.
- Load `research-co-mathematician-workflow` before opening or reshaping substantial
  mathematical research workstreams.
- Load `research-proof-auditing` for proof, evidence, formal verification, and fraud checks within the review kernel's Gate 5.
- Load `research-orchestration` for subagent contracts, worktrees, self-check, adversarial audit, and durable artifact handoff.
- Load `research-math-boundary` when preflight reveals missing foundational mathematical nouns, methods, conventions, or backend bridges.
- Load `research-planning-cleanup` for post-hoc meta-review of completed cards — scanning for shallow work, confabulation, and Jerry-behaviour that survived gate review.
