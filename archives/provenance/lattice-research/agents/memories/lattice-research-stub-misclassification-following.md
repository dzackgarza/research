# lattice-research-stub-misclassification-following

---
title: lattice-research-stub-misclassification-following
tags: [category-specs, stubs, workflow, plugin, misclassification, boundary]
status: active
---

## Trigger

Any work that classifies `category_specs` mypy diagnostics, produces stub requests, or creates workstream backlog for `sage-stubs`.

## Core correction

The previous workflow (serial row-picking, ledger-driven stub backlogs) was fundamentally flawed. It misclassified internal `category_specs` `@override` errors as missing `sage-stubs` work, then burned enormous token budget chasing phantom stub requirements.

**The fatal error**: treating `@override` failures on local `ParentMethods` / `ElementMethods` method containers as evidence of missing Sage concrete-class stubs. The correct owner is almost always internal spec/plugin/graph, not `sage-stubs`.

The issue is `lattice-research#6` and the analysis note is in `vault/projects/research/5-27-26 Stub Misclassification.md`.

## Rule: three ownership classes

Every diagnostic falls into exactly one of these classes. When in doubt, start from the source location, not from matching method names against Sage.

### Class A: Spec-owned (category_specs)
- Any method whose purpose is checking mathematical propositions or performing mathematical computations.
- Any `@override` where the intended parent does NOT define the method: spec incompleteness or wrong-method-owner.
- Any category graph defect: redundant supercategory lists, missing/minimal edges, misnamed categories.
- Any method in `ParentMethods` / `ElementMethods` / `Hom/End/Aut` that is about mathematical capability.

**Heuristic**: if the method is a mathematical operation you'd expect a category theory text to define, it is spec-owned. Do NOT create stub requests for these.

### Class B: Plugin-owned (sagemath-mypy-plugin)
- Any `@override` where the intended parent method EXISTS in the local spec graph, but mypy cannot see the method-container inheritance edge.
- Category framework/plugin visibility issues: `C.ParentMethods` should override `ParentCategory.ParentMethods` but mypy says "no base method."
- Output must be a **minimal fixture**: a LITERAL chunk of code defining REAL categories and subcategories with REAL methods and `@override`, `@overload`, `@final`, etc., showing the golden case that should pass.
- These fixtures go to the plugin repo's test suite.

### Class C: True Sage boundary stubs (narrow and finite)
- ONLY direct constructor / wrapper / interop-gate calls into Sage runtime.
- The exact Sage symbol imported/called, local wrapper, admitted input shape, refined output type, current diagnostic, and why local refinement cannot provide the type.
- Must be derivable from the constructor inventory of `Cat().Constructors()` and root `Constructors()` surfaces.
- The current stub-eligible surface is much smaller than the old workflow assumed.

## Rule: constructor-derived boundary inventory

Before allowing ANY stub request, produce the finite constructor inventory:
- Enumerate every constructor exposed by `Cat().Constructors()` and each root `Constructors()` surface.
- For each, record: Sage entry point, admitted inputs, local refined output category.
- Only if mypy STILL needs an exact external type fact after local refinement is the row stub-eligible.

## Rule: periodic category tree minimality review

- A subcategory `C` of `B` of `A` must NOT directly declare `A` as supercategory unless there is a recorded mathematical reason.
- Multiple local supercategories are a RED FLAG unless the category is a genuine mixed-structure intersection.
- Look for redundant ancestry / consequence closure lists that compensate for a broken category graph.
- This is not optional cleanup; it is a QC gate.

## Rule: QC errors are plugin issues, not stub work

Any `override` or `attr-defined` error on a local category method container is a **plugin** or **spec** issue by default. The burden of proof is on showing it is a true Sage boundary issue before creating stub work.

## Why this matters

The old workflow deferred hard internal work into a `sage-stubs` sink, rewarded "covering" methods with stubs rather than defining them in the spec/graph/plugin, and produced a contaminated ledger that future agents would have consumed. Stopping this requires durable memory, not just issue comments.

## Verification

- A reviewer must be able to answer from committed repo artifacts:
  1. Which category edges are immediate and mathematically justified?
  2. Which current `@override` errors are true spec errors? Which are plugin red tests?
  3. Which exact Sage boundary calls require stubs?
  4. Which previously exported sage-stubs rows were removed from scope?
- If answers require reading agent summaries or issue comments, the work is incomplete.
