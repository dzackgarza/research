---
name: coble-inbox-analysis-loop
description: "Use when refining the Coble-Paper mathematical Obsidian inbox-analysis loop, testing repo-local inbox-analysis agents, or updating guidance for CriticMarkup routing of Coble inbox sources."
---

# Coble Inbox Analysis Loop

Use this with `mathematical-obsidian-vault-steward` when working on Coble-Paper
inbox analysis artifacts or the repo-local `obsidian-inbox-analysis*` OpenCode
agents.

## Core Rules

- Optimize artifact quality, not receipts. File existence, hashes, byte counts,
  target lists, and agent self-reports do not show that mathematical extraction
  happened.
- The annotated source is the continuation state. Do not create handoffs,
  progress summaries, routing ledgers, or completion notes for later agents to
  trust.
- A useful partial artifact is acceptable when a fresh agent can read the source,
  inspect local CriticMarkup, and continue improving it without prior transcript
  context.
- Every cold pass should choose one coherent source segment and improve it
  semantically. Do not launch or design a whole-file cleanup pass.
- When testing the loop, use a minimal task prompt that names the artifact. Put
  durable artifact requirements in the skill or agent definition, not in the
  test prompt.

## CriticMarkup Invariants

- Broad umbrella comments over structured claim lists are unresolved work, even
  when all items point to one target note.
- Split structured passages at visible mathematical boundaries: Roman-numeral
  sections, numbered proof-obligation items, bold labels, paragraph clusters, or
  theorem-like claims.
- Leave unhandled structured passages visibly unhandled. Do not add synthetic
  coverage comments to make the artifact look complete.
- Preserve proof status over bookkeeping status. A claim can be already recorded
  in the vault and still be `open`, `conjectural`, `disputed`, or
  `needs-human`.
- Target-note framing overrides source confidence. If the target note says a
  statement is a proof obligation, conjectural package, migrated research claim,
  or awaiting corroboration, do not classify the source assertion as `fact` or
  `duplicate`.
- `reason:` fields describe source and vault semantics only. Do not mention
  prior agents, previous comments, pass history, umbrella splitting, or testing.

## Live Test Method

- Run the repo-local inbox-analysis agent from `/home/dzack/Coble-Paper` with a
  minimal prompt such as: `Continue the annotated inbox-analysis work surface at
  <path>.`
- Observe the transcript and artifact diff. The worker's final message is not
  evidence.
- Accept a trial only when the diff shows source text preserved and the inserted
  comments improve mathematical routing, unit labels, proof status, and verified
  section anchors.
- If a trial needs manual repair, encode the repair as an artifact-facing rule
  before running another cold pass.
