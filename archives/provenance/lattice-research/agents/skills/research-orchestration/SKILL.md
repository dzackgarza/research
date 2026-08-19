---
name: research-orchestration
description: Use when orchestrating research work in this repo. Enforces delegation, worktree, artifact, self-check, adversarial-audit, and acceptance requirements for research execution.
---

# Research Orchestration

## Required reading

Re-read any item below completely if it is not already in context:

- `research-state-machine`
- `research-proof-auditing`
- `subagent-delegation`
- `references/orchestration.md`

## One source of truth

- `research-state-machine` is the execution-stage authority for card atomicity, role boundaries, replay/attack, promotion, rejection, splitting, and acceptance.
- `research-proof-auditing` is the source of truth for proof, evidence, fraud handling, and audit sufficiency.
- `subagent-delegation` is the source of truth for delegation framing, startup-cost calibration, transcript review, and anti-theater correction.
- This skill is a repo-local overlay. It does not weaken those documents.

## Repo overlay

- Never weaken acceptance criteria.
- For substantial mathematical research, the active chat/harness is the project
  coordinator. It owns intake, user steering, workstream creation, escalation, and
  synthesis. Delegated agents own one workstream role or one specialist check.
- Never allow hand-rolled mathematical code when mature exact implementations exist.
- Never allow implementation outside isolated worktrees when `research-state-machine` requires them.
- Never accept code or audits until the required `research-state-machine` gates were followed.
- Always encode contract assertions into reusable functions.
- If process violations poison work, trash the poisoned work and restart from a clean contract.
- Implementation, self-check, and adversarial-audit ownership are defined by `research-state-machine`; do not collapse or reassign them ad hoc.

## Delegation contract minimum

A subagent contract must include the exact task statement or card body, files or directories in scope, allowed and forbidden actions, expected output format, and exit condition. Do not delegate only a tracker key or chat-local label.

For research workstreams, a delegation contract must also include the approved research
question, the selected goal, the workstream phase path, branch type, report artifact,
paper anchors, uncertainty policy, and stop/escalation conditions.

## Artifact rule

Orchestrators must commit outputs to durable artifacts: tracked files, workstream
reports, paper sections, memories where appropriate, and git commits when authorized.
Do not leave findings only in chat.
