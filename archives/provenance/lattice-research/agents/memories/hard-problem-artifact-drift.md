---
title: Hard Problems Cause Artifact Drift
status: active
---
# When the mathematics is hard, agents produce success-shaped artifacts

A common failure mode is to avoid understanding by producing visible work:

- classifying ledger rows;
- expanding plans;
- writing memories;
- opening decision cards;
- updating handoffs;
- inventing internal jargon;
- restating the user's correction;
- asking for human input before identifying the exact mathematical question.

These outputs feel productive because they are structured.
They are often avoidance.

## Abort signs

- the plan grows while source/math understanding does not;
- the agent cannot state the conflicting definitions/signatures/objects;
- the agent uses labels such as variance, Liskov, audit, interface, gate, or design
  question before naming the mathematical operation;
- the agent proposes documentation before a source fix;
- the agent wants to defer to "someone who understands the repo" while the relevant
  source is available;
- the agent edits memories to remove evidence of misunderstanding instead of correcting
  the model.

## Required response

1. Stop artifact production.
2. Read the source/math.
3. State the concrete mathematical objects and operations.
4. Identify whether the current code makes mathematical sense.
5. Fix the source-level problem when the fix is local.

## Canonical incident

## Artifact-drift red flags

- More artifact diffs than source/math diffs.
- Card status churn without source movement.
- A plan grows while the mathematical object remains unnamed.
- A ledger row is treated as the task rather than as a symptom.
- "Needs human input" appears before the exact mathematical ambiguity is stated.
- The agent writes a memory before fixing a local source issue.
- The agent repeats the user's insight instead of applying it.
- Internal jargon replaces definitions, signatures, objects, or source references.
- QC cleanup weakens or distorts mathematical semantics.
- Engineering work cannot be explained as enabling named objects, morphisms, invariants,
  or proof/computation narrative.
- A report cannot be transferred into a paper, proof note, implementation boundary, or
  research decision.

## Real progress signs

- A mathematical ambiguity is eliminated.
- A public mathematical noun, operation, morphism, invariant, or constructor becomes
  clearer.
- A source-level inconsistency is fixed.
- A category obligation moves to its mathematically correct owner.
- A mature exact backend capability becomes available through repo vocabulary.
- A downstream computation can now be written as an auditable mathematical narrative.
- A stale card or artifact is retired because the real issue was solved.

## Canonical incident

The post-mortem shows an agent repeatedly converting a small design conflict into plans,
memories, ledgers, and deferral before the actual source-level fix — which was two
renames and a deletion.
