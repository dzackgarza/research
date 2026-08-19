---
title: How Category Spec Work Should Proceed — No Bureaucracy, Just Thinking
date: 2026-05-27
status: active
---
# How Category Spec Work Should Proceed

## The graph is a tree

The category inheritance poset should be **mostly a tree**.

- Root entry points (e.g., `Rings`, `Sets`) bridge to Sage.
- Everything below them should inherit through **one immediate local parent**, forming a
  chain.
- Multiple local supercategories are **suspicious** unless they genuinely introduce a
  mixed structure (e.g., a topological ring is both a ring and a topological space).

If a category lists multiple local parents, ask: is this a true intersection of
independent structures, or is one parent a consequence/ancestor of another?
If the latter, fix the graph.

## There are exactly three kinds of problems

When you see a mypy error in `category_specs`:

### 1. Real spec error

**Shape:** `@override` on a subcategory, but no parent category in the local graph
defines the method.

**Action:** Add the method to the correct parent category.
The spec is incomplete.

### 2. Plugin error

**Shape:** `@override` on a subcategory, and the parent category DOES define the method,
but mypy cannot see the inheritance edge.

**Action:** Write a minimal red test for the plugin.
The plugin needs to project the dynamic method-container inheritance into static
visibility.

### 3. True stub need

**Shape:** A direct call to Sage runtime API (constructor, import, explicit method call)
where `category_specs` cannot type the boundary without external type information.

**Action:** Add a stub to `sage-stubs` ONLY for that specific boundary call.

**Everything else is not a stub problem.**

## The stub surface is almost empty

The research repo has **total control** over output types.
`Cat().Constructors()` calls a Sage constructor and then `refine_category(...)` to cast
the result into the local spec surface.
After refinement, the object lives in the internal hierarchy.
Its methods are owned by the internal graph, not by Sage stubs.

Stubs are only needed for the **thin touchpoint** where the raw Sage object enters the
system. Even then, the stub surface should be derived from the explicit constructor
inventory, not from internal method-container diagnostics.

**The inventory of constructors is finite and known.** Collect them on
`Cat().Constructors()`. For each, inventory the exact Sage callable and the local
refined output type.
That is the complete stub surface.
Nothing else belongs in `sage-stubs`.

## How to audit the graph

1. Extract every `super_categories()` return in `category_specs/`.
2. Build the graph.
3. Flag every category with more than one **local** parent.
4. For each multi-parent category: is it a true mixed structure, or is the graph wrong?
5. Flag every category whose parents are not minimal (one parent is an ancestor of
   another).
6. Output a plain tree for human mathematical review.

This is not a complex tool.
It is a simple script.
Without it, the graph will accumulate absurdities.

## Organizational requirements

The repo currently has no clear way to answer these questions:
- What are all the constructors?
- What is the true error signal?
- What is the actual stub surface?

Fix this by making the constructor inventory the single source of truth.
Every constructor should be collected on `Cat().Constructors()`. Every boundary call
should be traceable to that inventory.
Every mypy error should be classified against the three problem types above.

## The anti-pattern

- Adding direct ancestors to make a method available locally instead of fixing the
  intermediate graph.
- Classifying internal `@override` errors as stub work.
- Inventing jargon to obscure simple truths.
- Producing strategy documents instead of concrete audits.
- Treating the ledger as a scoreboard rather than a diagnostic signal.
- Treating engineering-shaped machinery as category-spec progress before it names a
  mathematical delta.
- Polishing a slop-produced artifact instead of redoing the underlying method owner,
  category edge, obligation, or provider relation correctly.

## The core principle

**Think.** Do not checkbox.
Step back and ask if the graph makes sense.
If it does not, fix the graph.
Do not add a workaround.
Do not suppress the error.
Do not write a document explaining why the absurdity is acceptable.

## Ledgers are symptoms, not the task

A ledger row is diagnostic evidence. It is not the mathematical defect.

Do not "work on the ledger" unless the requested deliverable is explicitly a ledger
classification. In ordinary category-spec work, a ledger row only points to a possible
source-level inconsistency. The task is to identify and repair the source-level
mathematical/spec/code problem.

Before touching a ledger, answer:

- What source definitions does this diagnostic point to?
- What mathematical operation, object, category, or interface is actually in conflict?
- Does the apparent engineering problem disappear once the mathematical semantics are
  named correctly?

If the issue is source-level, fix the source. Do not improve the ledger description,
create a goal, or open a decision card as a substitute.

## Do not convert a 5-minute code conflict into artifacts

When the code conflict is local and both sides are controlled by `category_specs`, fix
the code. Do not create a goalcraft goal, decision card, handoff update, memory patch,
or plan bundle before reading the relevant definitions.

Artifact production is allowed only after one of these is true:

1. The relevant code has been read and the conflict is still genuinely undecidable.
2. A human decision is required because multiple mathematically coherent interfaces
   remain.
3. The code fix has been made and the memory records a durable anti-pattern.

Otherwise, artifacts are evasion.

If a discovered lesson affects ordinary category-spec work, update the memory or doc
that ordinary agents already load. Do not create a standalone lesson dump that future
agents will only read if they know the historical conversation exists.

## Category specs are a research foundation, not a paperwork sink

The category-spec layer exists to make mathematical implementations auditable and
transferable to research. It is not a separate engineering deliverable to optimize
indefinitely.

Do not treat mypy ledgers, feature cards, or category coverage reports as the object of
work. They are diagnostic evidence. The defect is always a mathematical/source-level
inconsistency, missing operation, wrong owner category, or unsafe bridge boundary.

If a category-spec task does not clarify mathematical ownership, expose a real
operation, place an obligation correctly, or unblock downstream research vocabulary,
stop and reassess.
