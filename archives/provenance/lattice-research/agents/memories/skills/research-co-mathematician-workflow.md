---
title: Research Co-Mathematician Workflow
status: active
date: 2026-05-29
---
# Research Co-Mathematician Workflow

This skill makes the AI co-mathematician paper operational in this repo.
It treats the repo as a stateful mathematical workspace, not a task queue with proof
checks attached.

## Core Policy

- Start substantial research with intake: clarify the user's question, goals, non-goals,
  hard constraints, source context, success criteria, and approved initial workstreams.
- Treat mathematics as multi-modal work.
  Literature search, source mining, brainstorming, conjecture formation, counterexample
  search, numerical exploration, simulation, implementation, proof, formalization,
  exposition, review, and failure analysis are first-class activities.
- Maintain native mathematical artifacts.
  Serious claims must flow into a living LaTeX working paper or a linked workstream
  report with provenance and margin-note style uncertainty annotations.
- Organize agents as a hierarchy.
  The active chat/harness is the project coordinator; delegated agents are workstream
  coordinators, literature/source agents, computational explorers, proof strategists,
  implementers, reviewers, and uncertainty auditors.
- Track uncertainty as state.
  A disputed lemma, missing citation, unreplayed computation, stalled review, or human
  judgment point is not a generic blocker; it is a claim-state transition that must be
  visible to the user and future agents.
- Preserve failed explorations when they teach.
  Record false conjectures, exhausted searches, proof gaps, and failed computational
  strategies in cards, workstream reports, or the working paper.
  Do not preserve broken code.

## Required Reading

Read `references/architecture.md` before creating or revising intake artifacts,
workstream phases, report templates, paper sections, agent-role prompts, or uncertainty
rules.

## Decision Procedures

Use intake when:

- the user asks for a new research direction;
- a plan would otherwise encode vague goals or unresolved mathematical intent;
- a source primer, paper, or conjectural direction needs translation into repo work.

Use workstreams when:

- one goal naturally splits into prove/disprove, literature/theory, computation/code,
  formalization/review, or synthesis/audit branches;
- the user needs asynchronous steering without reading execution logs;
- a branch can fail while still producing useful information.

Use the living paper when:

- a claim is meant to shape the mathematical narrative;
- a result, failed strategy, or source synthesis should be readable outside the card
  system;
- margin notes can expose provenance, disputed status, or human-review needs better than
  a task log.

Escalate to the user when:

- workstream review stalls on a precise assertion;
- reviewers only agree after weakening or obscuring the claim;
- the next step depends on mathematical taste, a strategic choice, or area expertise;
- continuing would create a polished-looking artifact whose rigor state is unclear.

## Validation

- Planning/card changes: `just plan-validate`.
- Living paper changes: `just paper-build` when the LaTeX toolchain is available.
- Reports and paper sections must link back to cards, sources, computations, or review
  artifacts; unsupported prose is not a research artifact.

## Referenced documents

[Co-Mathematician Workflow Architecture](research-co-mathematician-workflow/architecture)
