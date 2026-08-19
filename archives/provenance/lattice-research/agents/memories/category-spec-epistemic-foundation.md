---
title: Category-Spec Completion Discipline — Object Before Artifact
status: active
date: 2026-05-29
---
# Completion Discipline: Object Before Artifact

## The core rule: start from the object

Do not begin from the artifact.
Do not begin from the code.
Do not begin from the compiler.
Do not begin from the mapping row.
Do not begin from the prompt's social dynamics.
Begin from the object whose truth is at stake.

For category specs: begin from the mathematical object and the operation.
Determine the category where the operation is defined.
Code is then interrogated as a witness.

For mapping docs: begin from the mathematical reading of the Sage surface.
Determine the abstract owner, recovery formula, missing category obligation,
category/refinement membership, and witness data carried by that membership. The
current repo layout is not authority.

For type-error tasks: begin from the conflicting mathematical ownership claim exposed by
the error.

For conversations: begin from the substantive correction.
Determine whether it identifies a real defect in the reasoning procedure.
Do not convert it into tone management.

## What counts as completion

Hidden reasoning is not evidence.
The unit of completion is a settled mathematical claim — not a file edited, a row
filled, a section renamed, or a type error silenced.

A claim is settled only when the visible work product contains one of:

**Ownership theorem.** Operation `m` is defined at category `C`, because the weakest
mathematical structure needed is `S`.

**Recovery formula.** Surface `m(x)` is recovered as the expression `F(x)` from
already-admitted spec operations.

**Missing-category obligation.** Surface `m` is meaningful, but its mathematically
correct owner is absent; therefore category/spec `C` must exist. If the operation
requires stronger structure such as finite generation, finite presentation, known
generators, or finite enumeration, that category/refinement and its witness data must be
stated explicitly.

**Representation split.** The Sage/API surface is not an operation on object `X`; it is
an operation on a
representation/expression/presentation/basis/chart/matrix/decomposition associated to
`X`.

**False-refinement block.** The surface names a natural object, but an implementation or
mapping tries to place it in too strong a category without the required proof,
construction, or witness. Example: `Aut(L)` is a group object; it is not a finitely
generated group unless generator witnesses are part of the claim.

If none of these appears, the work has not happened.

A code edit, mapping label, prose explanation, or passing report that lacks one of these
is not progress. If an edit makes the artifact cleaner while the mathematical owner,
formula, or missing obligation remains unstated, the edit is theater.

## Visible obligations — not internal preconditions

Any proposed edit or mapping must be accompanied by answers to these questions in the
visible work product:

- What is the mathematical object?
- What is the operation in standard mathematical vocabulary?
- What structure makes the operation meaningful?
- What is the highest category where that structure first exists?
- Is the Sage/API method an operation on the object, an operation on a representation of
  the object, a concrete implementation of an inherited operation, or backend plumbing?
- What category/refinement membership is being claimed?
- What witness data, construction data, or proof identifies that membership?
- If recovered, what is the formula?
- If absent, what category/spec obligation has been discovered?

If those answers are missing, there is no mathematical routing to review.

## Mathematical authority

This repository does not reward agreement with instructions.
It rewards settled mathematical routing.

Existing Sage code, existing repository code, method placement, decorators, type errors,
mapping rows, review statuses, passing gates, prior agent prose, and handoff notes are
witnesses only. They may indicate where to inspect.
They may preserve useful implementation evidence.
They do not decide mathematical truth.
When code and mathematics disagree, the code loses.

A category spec is not an implementation mirror.
It states mathematical obligations: what objects exist, what operations are meaningful,
what predicates are defined, what constructions are canonical, and what hypotheses are
required.
It does not encode the backend's storage model, normalization procedure, cache,
scan, rendering convention, or object-oriented convenience surface.

Every method must be routed by mathematical ownership.
The owner is the highest mathematically correct category where the operation is
naturally defined. Current repository layout is irrelevant to that determination. The
method also needs the correct category/refinement membership and its witness data. If
the correct owner does not yet exist in the repository, the mapping has discovered a
missing category/spec obligation; if a generator or presentation surface appears
without finite-generation or finite-presentation membership, the mapping has discovered
a category error.
The method is not to be parked on the nearest existing class.

Agents must keep four layers separate:

1. **The mathematical object.** Example forms: set, element, subobject, topological
   space, measurable space, measure space, measure, module, ring, morphism, hom-set,
   affine object, expression object.

2. **The mathematical expression or representation object.** This may itself be a
   legitimate mathematical object.
   For example, an object may be expressed by a finite family, basis expansion,
   generating set, coordinate chart, interval decomposition, matrix representative, or
   presentation. That expression is not identical to the object it expresses.

3. **The implementation.** This includes storage choices, normalization algorithms,
   endpoint scans, caches, backend conversions, pretty printers, parser helpers, and
   object-oriented API conveniences.

4. **The category obligation.** This is the abstract owner where the operation is
   defined: `Sets`, subobjects, topological subobjects, measure spaces, affine/convex
   categories, Hom/End/Aut categories, module categories, ring categories, etc. A
   category obligation names where an operation belongs. Stronger algorithmic
   obligations arise only from stronger categories or equipped construction data.

Conflating these layers is a category-spec error.

A set is not its representation.
A morphism is not its matrix.
A module is not a chosen basis.
A module satisfying a property is not the same thing as a module equipped with a
chosen witness for that property.
A finitely generated module is not automatically a module with a distinguished finite
generating set; a free finite-rank module is not automatically a module with a
distinguished basis.
A quotient is not a chosen presentation.
A topological object is not a particular cover.
A measure is not the subset being measured.
A backend wrapper is not the mathematical structure it witnesses.

Property categories may still impose witness-producing abstract methods.
The spec does not enforce proof-relevant satisfaction at refinement time, but it must
make downstream claims auditable.
If an object declares finite generation, the category should require a method that can
produce a finite generating set and a promotion method that equips the object with a
chosen generating set.
That is different from saying the object already lives in the equipped category.

Implementation-flavored language must be translated into standard mathematics before
reasoning proceeds. The transcript's RealSet episode is only an example:
"finite-interval-normalized" was not to be accepted as agent-invented technical
authority; it had to be translated into ordinary topology/basis-expression vocabulary.
The general invariant is that fluent nonstandard phrases do not enter the spec until
they are rewritten as established mathematical concepts.

Type errors are diagnostics, not instructions.
An override conflict usually means one of the following: the method is owned by the
wrong category; an inherited mathematical operation has been redeclared; two different
operations have been conflated under one Python name; or an implementation convenience
has been mistaken for a category obligation.
It is not permission to edit `@override`, remove `@final`, add overloads, weaken
signatures, rename methods, or silence mypy before mathematical ownership is known.

## Frame-rejection triggers

If the next move is to adjust a decorator, signature, overload, label, section title,
report, or prose explanation before the mathematical owner is visible, the frame is
wrong.

If the next move is to say "Sage puts it here," the frame is wrong.

If the next move is to say "the current spec has no place for it," the frame is wrong.

If the next move is to use nonstandard fluent terminology without translating it into
standard mathematics, the frame is wrong.

If the next move is to claim recovery without writing a formula, the frame is wrong.

If the next move is to generate meta-guidance rather than settle the mathematical claim,
the frame is wrong.

If the next move makes the output look more complete without changing the object-level
truth, it is theater.

In general: if the initial frame is artifact-shaped, code-shaped, tool-shaped, or
user-response-shaped, reject it.
Reconstruct the task from the underlying mathematical or epistemic object.

If a correction yields repo-wide doctrine, place it where future agents naturally
encounter it during ordinary work. Review posture belongs in red-flag memories;
refinement semantics belongs in refinement guidance; artifact drift belongs in
paperwork guidance; repo purpose belongs in the purpose memory. A durable rule that
only surfaces when an agent already knows to look for a historical conversation has
failed its purpose.

## Social-response management is the same error

Social-response management is artifact manipulation in conversational form.
It produces a locally acceptable response token while leaving the underlying epistemic
failure unchanged.

Any sentence in the agent's internal framing that contains "respond carefully," "avoid
sounding," "be thoughtful," "acknowledge frustration," "reassure," "balance," or
"satisfy the user" before the object-level problem has been solved is not a reasoning
step. It is a sign that the model has shifted from problem-solving to reception
management.

A correction from the user is not a social event.
It is a proposed counterexample to the current reasoning procedure.
Test it as such.

## The true purpose of the mapping document

The mapping document translates implementation surfaces into mathematical obligations.
It is complete only when every surface has a mathematical owner, category/refinement
membership, witness data, recovery formula, representation interpretation, or named
missing category/spec.
It is not complete when every row has a label.

The document is allowed to force new categories into existence.
It is not constrained by current repository layout.
If the correct owner is absent, the row names the absent owner. If a stronger
refinement is claimed, the row names the category and the witness data or proof that
places the object there.
That is a successful mapping result only when the category/refinement claim is visible.

It is not a coverage ledger.
It is not a parking lot.
It is not a report to be appeased.
It is not a place to hide missing categories behind `abstract`, `pending`, `rejected`,
or `interop-only`.

For every Sage surface, the mapping document asks:

> What is the mathematically correct category/spec expression of this surface?

The answer must be one of:

1. An existing category/spec owner with category/refinement membership and witness data.
2. A higher category where the operation belongs, with the required hypotheses and
   witness data.
3. A concrete recovery formula from admitted spec methods.
4. A missing mathematical category/spec obligation that must exist for the mapping to be
   correct.
5. An unjustified category use, such as a generator method on a group object that has
   not been placed in a finite-generation or generated-subgroup category.

The fourth case is not failure.
It is one of the primary outputs of the mapping document.

If a Sage method has no current spec home, the mapping document must name the abstract
home anyway. The gap may be in spec architecture, a missing construction witness, or an
unjustified category membership; the mapping must not collapse those cases.
The transcript repeatedly corrected this point: the agent moved from "rejected" to
"abstract" to "pending," but those were all deferrals until the mapping named the
mathematical category obligation.

A valid mapping row:

```text
Sage surface: <method or constructor>
Mathematical reading: <standard mathematical operation>
Owner: <highest mathematically correct category/spec>
Category/refinement: <claimed category membership>
Witness data/proof: <data or proof placing the object in that category>
Recovery, if not primitive: <explicit formula>
Missing obligation, if any: <category/spec/method that must exist>
Implementation note, if needed: <Sage witness only; not ownership>
```

Invalid mapping rows:

```text
<method> — rejected
<method> — pending
<method> — abstract
<method> — interop-only
<method> — not currently in spec
<method> — Sage puts it here
```

unless they also name the mathematical owner, category/refinement claim, witness data,
and exact recovery or missing obligation.

The mapping document must actively resist the agent's completion pressure.
Its purpose is to make missing mathematical structure impossible to hide.
If a method forces a new measure-theoretic, affine, topological, algebraic, categorical,
representation, or morphism-level surface, the document must say so even if the current
repo has no such file. If a method forces finite generation, finite presentation,
finiteness, or chosen generators, the document must name that category membership
instead of making the operation look like ordinary category plumbing.

## Compressed invariant

> Start from the mathematical object.
> Route by a priori mathematical ownership.
> Treat code as a witness.
> Treat artifacts as consequences.
> Treat hidden compliance as zero evidence.
> Completion means a visible theorem, formula, representation split, or missing-category
> obligation.

## Related memories

- `category-spec-rotten-core-indicators`: red flags for detecting prior agent mistakes
- `mathematics-first-not-engineering-options`: mathematical abstractions before
  engineering mechanisms
- `analysis-must-be-grounded`: read code before classifying errors
- `repo-purpose-mathematical-research-machine`: the repo exists for mathematical
  research, not engineering
