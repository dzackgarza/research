---
title: Object Method Resolution Phase - Source Repair
status: active
tags: [goal-phase, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Phase - Source Repair

## Phase objective

Edit source so the object-method relation reconstructed in the previous phase is true
without cache priming, spec implementations, obligation deletion, or refinement-time
validation.

## Entry condition

Do not enter this phase unless `provider-satisfaction-goal-state` contains the filled
source-reconstruction synthesis statement and names the exact relation the edit must
change.

## Edit gate

Before each source edit, state the object-level delta:

> This edit makes concrete object method ___ available to refined object ___ under
> category contract ___, while preserving abstract requirement ___ and missing
> requirement ___ as visible to category-obligation examples and later implementation
> work.

If the edit cannot be stated this way, it is not authorized by this phase.

## Required behavior

The repair must preserve these facts:

- specs may declare Sage-provided operations as abstract obligations;
- concrete Sage or project object methods satisfy requirements only when they are real
  mathematical operations on the object;
- Python `abc.abstractmethod` and Sage `abstract_method` markers do not count as
- object methods;
- concrete object methods are resolved before abstract requirements with the same name;
- missing obligations remain visible; refinement does not reject them;
- `ParentMethods` is the method surface of objects in a category, not a generic
  engineering method-supply layer;
- `refine_category` declares category view and must not become an object-satisfaction
  validator;
- cache, `_cached_methods`, performance, and lookup-priming mechanisms are absent unless
  a source-grounded theorem in the state proves they are mathematically necessary.

## Banned edit shapes

Stop and return to `SYNTHESIZE` or `DECOMPOSE` if the proposed patch:

- adds method bodies to spec obligations merely to call Sage;
- deletes an abstract obligation because Sage implements it;
- makes `refine_category` check abstract method completeness;
- changes a category-obligation example to assert only name or file existence;
- adds casts, ignores, `NotImplementedError`, local QC bypasses, or report-only fixes;
- improves hooks, reports, ledgers, or mypy output before changing the object-method
  relation;
- introduces helpers whose names read like engineering policy rather than mathematical
  object/category facts;
- performs metaclass manipulation, dynamic-class splicing, MRO surgery, descriptor
  replacement, or post-hoc method installation inside spec code without a
  source-grounded proof that the existing Sage integration boundary owns that exact
  mechanism.

## Advancement evidence

To advance to verification/review:

- source diff shows the reconstructed relation changed;
- no unrelated dirty work was reverted or overwritten;
- targeted runtime witness exercises object-method resolution rather than source text;
- state is updated with the exact commands to rerun.

Then load `provider-satisfaction-phase-verification-review`.

## Reference skills

Load for this phase:

- `category-spec-style`
- `research-code-style`
- `research-state-machine`
- `research-proof-auditing`
- `anti-slop`

Load before any mathematical implementation work:

- `research-software-wiring`

Load on failed repair attempt:

- `hard-problem-decomposition`
