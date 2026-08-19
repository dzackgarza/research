---
title: Research Project Workflow
status: active
date: 2026-05-29
---
# Research Project Workflow

This skill is the canonical repo-level workflow authority for Nimbalyst-backed features,
specs, plans, phases, tasks, decisions, and project-management state.

## Canonical source

The source of truth is this skill plus `references/project-workflow.md`, interpreted
against the reusable framework in `/home/dzack/ai/planning/AGENTS.md` and the installed
local schemas in `.nimbalyst/trackers/`.

Read `references/project-workflow.md` before creating, migrating, normalizing, retiring,
or interpreting root `.agents/plans/` tracker files.

## Core policy

- Root `.agents/plans/` is the active repo-local tracker workspace.
  Use IWE as the query layer over this markdown before broad manual scans; do not create
  a separate aggregate status surface.
- Substantial research coordination follows `research-co-mathematician-workflow`: cards
  route workstreams, but reports and the living LaTeX paper carry the mathematical
  narrative.
- The GUI is the index; do not create aggregate tracker indexes.
- Use only registered standard tracker types from `.nimbalyst/trackers/*.yaml`.
- Use the root feature/plan/phase/task hierarchy for workflow dimensions.
  Tags are secondary grouping aids.
- There is no separate backlog; active cards are the outstanding work set.
- Completed feature trees should be moved under `.agents/plans/features/completed/`
  rather than left alongside active feature roots.
- Execute according to the DAG. Unmet declared dependencies mean a card remains
  `unstarted`; `blocked` is reserved for ready leaves stopped by a prerequisite that is
  not currently satisfiable through the DAG.
- Work top-down through feature/spec, plan, phase, and task gates.
  Do not create lower-layer cards before the owning layer is approved.
- Plans are human + LLM collaborative artifacts and must be approved before
  decomposition or execution.
- Task creation has a hard phase-owner preflight: name the owning feature, plan, phase,
  and destination path before writing the card.
  If the phase card does not exist, stop and create or repair the phase first; never
  create plan-level `tasks/` directories.
- Substantial research plans must include intake status, onboarding artifact,
  working-paper path, branch/workstream policy, agent organization, and uncertainty
  policy.
- Workstream phases use `phaseKind: workstream` and record branch type, agent roster,
  report artifact, paper sections, uncertainty summary, and failed explorations.
- Substantial research tasks must record activity type, workstream role, claim status,
  uncertainty state, paper anchors, report artifacts, and failed explorations.
- Executable work belongs in dedicated tracked files, not chat-only plans or inline
  markers.
- Decision cards are feature-level blockers only; do not leave unresolved decision
  language inside feature, spec, plan, phase, or task bodies.
- Validate planning edits with `just plan-validate`, which delegates to the centralized
  planning validator. Do not add repo-local relaxed validators or warning-only schema
  checks.

## Load with

- Load `task` or `track` before creating individual tracker items.
- Load `category-spec-workflow` for category-spec-specific planning, triage, priority,
  visuals, or retirement.
- Load `research-state-machine` when planned work moves into execution, preflight,
  replay/attack, promotion, rejection, splitting, or `GOAL.md` discharge.
  Load `research-orchestration` for delegation, worktrees, self-check, adversarial
  audit, and artifact handoff.
- Load `research-scheduling` when a plan or card needs a delayed wakeup, recurring
  maintenance, autonomous cadence, or migration from fixed schedule thinking.
- Load `research-planning-cleanup` when scanning completed cards for shallow work,
  cleaning up planning debt, or auditing review quality across cards.

## Referenced documents

[Research Project Workflow Reference](research-project-workflow/project-workflow)
