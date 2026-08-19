---
title: Analysis Must Be Grounded in Real Repo Data — No Inference, No Guesses
date: 2026-05-27
status: active
---
# Rule: Analysis Must Be Grounded in Real Repo Data

## The principle

Any analysis, audit, classification, or fix must be derived from reading the actual
code, the actual reports, and the actual design documents in the repo.
Inference, speculation, and pattern-matching from partial data are not acceptable
substitutes for reading the source.

## The anti-pattern

Agents frequently produce analyses based on:
- **Inference from bucket names:** assuming `missing sidecar ordinary signature` means
  external stub work without reading the actual error messages.
- **Same-name matching:** searching for method names in Sage source and assuming the
  stub is missing them, without checking whether the override chain is internal.
- **Abstract reasoning from incomplete data:** producing a strategy document, a set of
  acceptance criteria, or a vague issue comment instead of the concrete deliverable
  requested.
- **Delegation to future agents:** writing a comment or issue that tells someone else
  what to do, rather than doing the analysis now.
- **Transcript sampling:** extracting a few obvious correction clusters and calling it
  transcript mining when the full conversation is the source.

## The requirement

Before producing any analysis or deliverable:

1. **Read the actual repo files.** Not summaries, not cross-references, not other
   agents' interpretations.
   The actual code.
2. **Read the actual design documents.** `AGENTS.md`, `category-spec-style`,
   `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`, etc.
3. **Read the actual reports.**
   `reports/workstreams/category-specs-mypy-ledger/latest.json`,
   `reports/workstreams/category-specs-purge-audit/latest.md`, etc.
4. **Produce the concrete deliverable.** If asked for a table, produce the table with
   real data from the repo.
   If asked for a fix, produce the fixed code.
   If asked for a classification, produce the classified rows with evidence.

## What to never do

- **Never produce a strategy document when asked for a concrete output.** A 1500-line
  comment full of "shoulds" and "coulds" is not an audit.
- **Never defer concrete work to future agents or other repos.** If the task is to
  classify rows, classify them.
  Do not write an issue saying "someone should classify these."
- **Never analyze from the sage-stubs repo when the problem is in the research repo.**
  The `sage-stubs` PR, issue, or gap note is downstream evidence.
  It does not substitute for reading the actual `category_specs` code.
- **Never guess at the graph structure.** Read `super_categories()` returns directly.
  Do not infer what the graph probably looks like.

## The concrete failure

In the vault conversation, the user explicitly asked for a new comment on the issue.
The agent produced a 1500-line draft full of strategy, acceptance criteria, and proposed
tables — but no actual classification of any row, no fixed `super_categories()`, and no
concrete stub inventory.
The user had to say: "....you seem to be suggesting making a comment to DELEGATE and
DEFER that work, when I am telling you to DO that work right NOW."

The agent had access to the repo.
It could have read `category_specs/rings/subcategories/*.py`, built the actual graph,
and produced the actual table.
Instead, it wrote a document about what the table should contain.

## The rule

**If you cannot produce the concrete deliverable, stop and say so.** Do not substitute a
strategy document, an issue comment, or a set of acceptance criteria.
These are not the work.
They are containers for the work.
The user asked for the work.

## Category-spec gate: read code before classifying override errors

Before classifying any `category_specs` mypy error, the agent must read:

1. The failing method definition.
2. The supertype/base method definition named in the error.
3. The relevant `super_categories()` chain.
4. Any local file-level comments/docstrings near the method.

For override/signature errors, the first output should be the concrete pair of
signatures, not a classification label. For the RealSet/topological-space incident, the
required first observation was simply:

```python
# ambient/topological-space interface
is_open(self, U: Subset) -> bool

# subspace/self interface
is_open(self) -> bool
```

and similarly for `is_closed`, `closure`, `interior`, and `boundary`. The failure was
that the agent invented categories like "variance," "Liskov audit," and "interface
design question" before displaying the two definitions.

If you cannot quote both conflicting definitions from code, you are not allowed to
classify the error.

## Source-of-truth hierarchy

When a report, ledger, handoff, or plan conflicts with source code or mathematics, the
artifact loses.

Use this order:

1. Abstract mathematics.
2. Repo source code and category graph.
3. Repo design memories/docs.
4. Tests and type errors as diagnostics.
5. Ledgers, handoffs, plans, and decision cards.

A ledger can show where to look. It cannot decide what the operation means.
A handoff can preserve context. It cannot replace reading the code.
A decision card is only valid after the source and mathematics leave a real undecided
choice.

## Artifact-grounded analysis is not grounded analysis

A plan, ledger, handoff, or report is not a source of truth about the mathematics. It
is at most a pointer.

Grounding order:

1. abstract mathematics;
2. repo source code and category graph;
3. canonical source references / papers / Sage docs;
4. tests and type errors as diagnostics;
5. cards, ledgers, handoffs, and plans.

If analysis begins and ends in artifacts, it is not grounded.

When the relevant source is a conversation, read the whole substantive user corpus, not
just recent turns or search hits. Then distribute stable rules into the normal repo
guidance path instead of leaving them in a conversation-specific artifact.
