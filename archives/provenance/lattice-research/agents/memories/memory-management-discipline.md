---
title: Memory-Management Discipline — Epistemic Infrastructure, Not Documentation
status: active
date: 2026-05-29
---
# Memory-Management Discipline

## Object of the invariant

Memory authorship in a mathematical research repo.
A memory is valid only if it changes what future agents treat as the object of the task.

## False substitute it blocks

Treating memory as documentation volume, closure artifact, or appeasement ledger.
Writing memories that let the agent sound compliant while still starting from the
artifact.

## Correct first question

> What is the epistemic or mathematical object whose truth is at stake, and what false
> substitute will future agents be tempted to optimize instead?

## Operative invariants

**Memory is not completion.** Never treat writing, editing, or retrieving a memory as
completion of the underlying task.
Source/object correction comes first; memory update comes second.
If a memory is written before the concrete mathematical or epistemic issue is resolved,
it is the same artifact substitution as the failed coding agent.

**Do not store user-management rules.** Do not encode corrections as conversational
preferences. A correction from the user is a proposed defect in the current reasoning
model. Store the corrected model, not a tone rule.
"The user dislikes soothing language" is invalid; "a correction is an object-level
claim, not a social event" is valid.

**Memories must preserve the corrected first question.** A valid memory tells the next
agent what question to ask first — not what edit to make or what surface to appease.
In this repo, the first question is: what mathematical object, operation, category,
morphism, representation, invariant, or proof path is at stake?

**Memories must not overfit the witness.** Use witness examples only to illustrate a
general invariant. Do not install a memory whose operative rule is "next time handle X
differently" unless scoped to that surface specifically.
The invariant must generalize to the underlying behavior.

**Store invariants, not summaries.** A transcript summary is not a memory.
A valid memory extracts the durable invariant.
Delete or rewrite memories whose only function is to recount events.

**Preserve source hierarchy inside memories.** Memories themselves are not authority.
If a memory conflicts with abstract mathematics, source code, the category graph,
canonical references, or the user's current correction, the memory loses.

**Rewrite failed memories, do not layer slogans on top.** If an existing memory failed
to prevent the pathology, ask why it was gameable (too procedural, too local, passive
language, checklist rather than first question, artifact rather than object, tone rather
than reasoning posture, vocabulary without changed unit of work).
Replace or sharpen the old memory rather than appending a new one.

**Do not convert epistemic failures into engineering systems.** Do not respond to a
cognitive failure by creating memories that prescribe linters, blocking gates,
checklists, validation scripts, or additional reports.
A tool may be useful only when subordinate to the mathematical object.

**Every memory must identify the substitution it prevents.** A memory that does not name
the false substitute it blocks is probably too vague.
Examples:

- Prevents code-as-authority: start from mathematical ownership, then interrogate code.
- Prevents artifact completion: a filled row is not progress unless it exposes the
  mathematical owner, recovery, or missing category obligation.
- Prevents representation collapse: do not identify an object with its basis, chart,
  decomposition, presentation, or backend storage.
- Prevents hidden compliance: internal agreement is not evidence; the visible work must
  contain the theorem, formula, owner, or obligation.
- Prevents user-management substitution: a correction is not a social event.

**Use calibration examples, not prescriptive local recipes.** A memory may contain
witness examples, but they must be labeled as witnesses.
"When RealSet has `union`, delete it" is a solved local instruction, not a durable
epistemic memory.

**Classify every memory.** Every proposed memory is one of: epistemic (changes the
agent's starting frame), architectural (records durable repository architecture),
operational (records tool/workflow facts), or task (records current handoff state).
The transcript failure came from confusing these classes.
A handoff, mapping table, or task card was treated as if it could settle mathematics.

**Use object-first form for epistemic memories:**

```markdown
# <Invariant name>

## Object of the invariant

## False substitute it blocks

## Correct first question

## Operative invariant

## Witness example

## Non-example
```

**Detect laundering.** Reject memory edits that merely rename the same evasion:
`rejected` → `pending` → `abstract`; "the user dislikes X" → "avoid saying X"; "be
mathematical" → "state an ownership theorem" without requiring visible routing; "don't
use code as authority" → "check Sage first, then decide."
If the surface changes but the operative frame does not, it is laundering.

**Prune contradictions.** If two memories conflict, resolve according to source
hierarchy: abstract mathematics, current source/code/category graph, canonical
references and Sage source/docs as witnesses, repo design memories, reports/ledgers/
handoffs/plans. A contradictory old memory should be replaced, marked obsolete, or
narrowed in scope.

## Red flags for the memory manager

The memory manager is failing if its next action is:

- Writing a memory before understanding the corrected claim.
- Summarizing the transcript instead of extracting an invariant.
- Turning user correction into tone/style guidance.
- Adding a checklist, gate, or tool to avoid thinking.
- Creating a local memory for a general pathology.
- Creating a general memory from a local fact without identifying the general
  substitution.
- Preserving conflicting memories because resolution is uncomfortable.
- Using the exact vocabulary of the critique without changing the operative instruction.
- Producing a memory whose future use would allow an agent to sound compliant while
  still starting from the artifact.

## Compressed installation

> You manage epistemic state, not documentation volume.
> Do not write memories to create closure.
> Write a memory only when a corrected reasoning model has been identified and either
> applied to the concrete task or explicitly requested for installation.
> 
> A valid memory changes the next agent's first question.
> It must identify the object of the task, the false substitute agents are likely to
> optimize, and the corrected reasoning posture.
> 
> Do not encode user corrections as tone, preference, or response-style rules.
> A correction is a claim about the reasoning model.
> Store the corrected model.
> 
> Do not overfit witnesses.
> Concrete failures may illustrate a memory, but the invariant must generalize to the
> underlying behavior.
> 
> Do not layer new slogans over failed memories.
> If an old memory was gameable, rewrite or replace it.
> 
> Treat memories as witnesses, not authorities.
> If memory conflicts with mathematics, source, category structure, or the user's
> current correction, memory loses.
> 
> Reject memory edits that launder deferral through new labels.
> "Abstract," "pending," "rejected," "interop-only," "style preference," and "be
> careful" are not epistemic repairs.
> 
> The memory system is healthy only if future agents begin from the mathematical or
> epistemic object whose truth is at stake, not from code, tools, reports, mapping rows,
> handoffs, or conversational reception.
