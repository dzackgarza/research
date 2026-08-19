---
title: Object Method Resolution Goal Contract
status: active
tags: [goal-workflow, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Goal Contract

## Purpose

This is the stable contract for the object-method resolution repair goal.
Use it when resuming, advancing, reviewing, decomposing, or claiming completion of the
cache-priming/refinement work.

The key names are legacy. They must not import a "provider satisfaction" or
refinement-enforcement model into the repo. The governing model is:

- specs state object-method obligations;
- refinement declares category view and imposes the category contract;
- refinement does not validate satisfaction;
- Sage objects are expected to be partial relative to project specs;
- category-obligation examples expose the implementation gap.

## Vocabulary Discipline

`ParentMethods` records the method surface of mathematical objects in a category.
Treat each method as a mathematical fact, operation, or requirement on those objects.
Engineering phrases such as "provider satisfaction", "fulfilling project obligations",
"install concrete providers", or "abstract provider" are hard slop signals in this
goal. Do not preserve them with caveats or quotes. If one appears in proposed code,
tests, state, or review, stop and reconstruct the object/category/method sentence.

Any helper, phase sentence, category-obligation example, or review claim whose main noun
is a runtime mechanism rather than an object/category/operation relation is suspect.
Rephrase it as a mathematical statement before editing source.

This is not an optics or naming rule. In mathematical spec code, strange metaclass
manipulation, dynamic-class splicing, MRO surgery, descriptor replacement, or post-hoc
method installation is presumptive evidence of a slop hack. The exception is the
project-owned Sage integration boundary itself: local dynamic metaclasses that minimally
compose Sage's dynamic metaclasses with `ABCMeta` are a valid way to represent project
abstract methods in Python's class system. They are not a refinement validator.

Required sentence shape:

> For object ___ in category ___, method ___ expresses mathematical operation/fact/
> requirement ___ under hypotheses ___.

## Request completion witness

The goal is complete only when committed artifacts show that `category_specs` preserves
this relation:

> Refinement declares that an existing Sage object is viewed as an object of a project
> category. The project category contract is then present on the category method surface:
> every declared object method is either a mathematical requirement still visible as
> abstract, or a concrete object operation supplied by Sage or by a project category
> surface through ordinary lookup. Python `abc.abstractmethod` and Sage
> `abstract_method` markers are requirements, not implementations. Missing requirements
> remain visible to category-obligation examples and later implementation work;
> refinement itself does not validate or reject the object for failing them.

The completion artifacts must let a cold reviewer answer:

- why cache or `_cached_methods` awareness was misaligned with category-spec doctrine;
- which refined object(s), target contract(s), abstract requirements, concrete
  object methods, false abstract method surfaces, and missing requirements were
  involved;
- what relation the source fix makes true;
- how abstract obligations remain in specs without turning into implementations;
- which commands expose the relation and which obligations still fail visibly.

## Canonical state surface

Use project-local IWE memories:

- Contract: `provider-satisfaction-goal-contract`
- State and residue ledger: `provider-satisfaction-goal-state`
- Active source reconstruction phase:
  `provider-satisfaction-phase-source-reconstruction`
- Source repair phase: `provider-satisfaction-phase-source-repair`
- Verification/review phase: `provider-satisfaction-phase-verification-review`

These key names are legacy bootloader identifiers. Treat the titles and current state
text as the semantic authority; do not infer the task frame from the key slug.

Resume from `.agents/memories/` with:

```bash
iwe retrieve -k provider-satisfaction-goal-state
```

Load the active phase named in state only after reconciling state with current
artifacts.
Reload this contract before phase advancement, decomposition parent closure, outside
residue reporting, or final completion.

## Reference skills

Always load before object-level work:

- `handling-corrections` when resuming after user correction or failed alignment.
- `category-spec-style` before category-spec source edits.
- `research-state-machine` before phase advancement or card/status decisions.
- `research-proof-auditing` before accepting evidence or final completion.
- `llm-failure-modes` before accepting a shortcut, artifact summary, or apparently
  successful self-report.
- `addressing-shallow-work` when an approach is structurally wrong or checklist-shaped.
- `anti-slop` before accepting source, test, or documentation artifacts produced by an
  agent.
- `hard-problem-decomposition` before blocker, deferral, narrowed-scope, or
  outside-residue language.

Load for review:

- `reviewing-subagent-work` and `jerry-behaviour` before accepting agent-produced review.
- `research-gate-review` for substantive category-spec review gates.

## State machine

Use this loop:

`RECONCILE -> SYNTHESIZE -> SLOP-REVIEW -> EDIT -> CHECK -> REVIEW/DECOMPOSE`

`RECONCILE`: compare `provider-satisfaction-goal-state` with current source, git diff,
recent commits, and command output. Treat state as a claim.

`SYNTHESIZE`: before any source edit, produce the relation statement:

> This edit changes the category declaration/method-surface relation for refined object
> ___, target category ___, abstract object-method requirement ___, concrete object
> method ___, and missing requirement ___.

If that sentence cannot be filled from source evidence, do not edit source.

`SLOP-REVIEW`: reject approaches whose dominant mechanism is cache priming, lookup
state, test-order dependence, casts, ignores, spec weakening, implementation in spec,
or report/QC polishing without a mathematical delta.

`EDIT`: checkpoint first. Edit only the source needed to make the synthesized relation
true.

`CHECK`: run targeted runtime witnesses and relevant `just` recipes. Passing commands
are evidence only for the relation they actually exercise.

`REVIEW/DECOMPOSE`: if judgment is required, use independent review. If an attempt
fails, decompose the residue into smaller source claims and update the state ledger
before descending.

## Banned substitutions

These do not satisfy the contract:

- adding implementation bodies to spec obligations;
- deleting or weakening abstract obligations because Sage has a method;
- treating abstract markers as concrete object methods;
- making `refine_category` validate, reject, or interrogate object-method satisfaction;
- treating an abstract joined parent class as a refinement blocker;
- priming `_cached_methods`, prefetching lookup state, or depending on test order;
- adding `typing.cast`, `# type: ignore`, `NotImplementedError`, local QC bypasses, or
  static-only reports;
- calling a category-obligation example that asserts code shape, name presence, or file
  existence a proof of object-method correctness;
- editing memories, handoffs, cards, or comments and presenting that as source repair.

## Final review standard

Before completion, an independent review must inspect this contract, the active state,
phase docs, source diff, targeted command output, and any tracked card/report.
The reviewer must lead with any request-witness fact still false.
The worker's summary is not evidence.
