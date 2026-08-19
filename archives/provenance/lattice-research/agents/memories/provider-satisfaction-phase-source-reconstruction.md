---
title: Object Method Resolution Phase - Source Reconstruction
status: active
tags: [goal-phase, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Phase - Source Reconstruction

## Phase objective

Produce a source-grounded reconstruction of the cache-priming/refinement defect before
any source edit. Reconstruction must use the corrected model: refinement declares a
category view and does not validate object-method satisfaction.

This phase advances only when the reconstruction identifies, from current artifacts:

- refined object(s);
- target category contract(s);
- abstract object-method requirements;
- concrete object methods already available on Sage/project category surfaces;
- false runtime mechanisms that hide or replace abstract spec obligations;
- missing object-method requirements that should remain visible to category-obligation
  examples;
- the mathematical relation hidden by cache or `_cached_methods` awareness.

## Required source surfaces

Read the current source and current diff for:

- `category_specs/utils.py`
- the category files containing the target contract and abstract obligation;
- the relevant category-obligation example or test files;
- recent commits/diffs that introduced cache, `cached_method`, or `_cached_methods`
  awareness in refinement code.

Use current artifacts as authority.
Prior chat and this state doc are routing hints only.

## Synthesis gate

Do not edit source until this statement can be filled with source references and
runtime evidence:

> Refined object ___ is being viewed as an object of target contract ___. Contract ___
> declares object-method requirement ___. Concrete object method ___ exists at ___.
> Runtime mechanism ___ currently hides, replaces, or misrepresents that obligation at
> ___. Requirements ___ remain missing and should stay visible to category-obligation
> examples. The cache or enforcement-shaped patch hid ___ by ___.

If this statement cannot be filled, enter `DECOMPOSE` from the contract: choose the next
smaller source claim, record it in `provider-satisfaction-goal-state`, and attempt that
claim.

## Slop rejection before phase advancement

Reject reconstruction that:

- only says a function or file exists;
- proves only that the worker's code was present;
- uses name-presence tests such as `abstract_method_has_name` as semantic evidence;
- starts from `_cached_methods`, Cython lookup, or test order before the category
  contract and object-method relation are stated;
- treats refinement as validation, admission control, or enforcement;
- describes `ParentMethods` primarily as an engineering method-supply layer instead of
  the method surface of mathematical objects in a category;
- names helpers or phases around runtime mechanisms instead of object/category/method
  facts, propositions, or requirements;
- treats metaclass manipulation, dynamic-class splicing, MRO surgery, descriptor
  replacement, or post-hoc method installation as normal spec-code repair instead of a
  slop signal requiring source-grounded justification at the Sage integration boundary;
- repeats user critique without adding source evidence.

## Advancement evidence

To advance to source repair, update `provider-satisfaction-goal-state` with:

- the filled synthesis statement above;
- exact source paths and symbols inspected;
- targeted command output or witness notes sufficient to reproduce the defect;
- the next source relation the edit must make true.

Then load `provider-satisfaction-phase-source-repair`.

## Reference skills

Load for this phase:

- `category-spec-style`
- `research-state-machine`
- `research-proof-auditing`
- `llm-failure-modes`
- `addressing-shallow-work`

Load if reconstruction becomes report-shaped rather than source-shaped:

- `paperwork-is-a-routing-layer-not-progress` via `iwe retrieve`
- `analysis-must-be-grounded` via `iwe retrieve`
- `mathematical-sanity-check` via `iwe retrieve`
