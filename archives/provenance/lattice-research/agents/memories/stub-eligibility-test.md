# stub-eligibility-test

---
title: stub-eligibility-test
tags: [stubs, category-specs, boundary, qc, rules]
status: active
---

## The test

Before ANY row may be classified as `sage-stubs` work, answer exactly:

1. Is the failing expression a **direct** Sage boundary call/import in a local constructor, wrapper, or explicitly named raw-Sage interop gate?
   - If NO → NOT stub work. Stop.
   - If YES → continue to 2.

2. Does the local wrapper already control the public input type, output type, and category refinement by annotation/cast/refine_category?
   - If YES and mypy passes → NOT stub work. Stop.
   - If YES but mypy still fails → continue to 3.

3. Record ALL of the following. If ANY field is missing, the row is NOT eligible:
   - `category_specs` file:line
   - local constructor / wrapper / interop gate name
   - exact Sage symbol imported or called
   - admitted local input shape
   - local refined output category/type
   - current mypy diagnostic message
   - exact missing external type fact
   - why local annotation/cast/refinement/plugin/static-model work is insufficient

## What is NOT stub work (automatic rejection)

- internal @override on ParentMethods/ElementMethods/Hom/End/Aut
- method name also existing on a concrete Sage class
- Sage implementation method being current runtime provider
- local category method surfaces (rank, dual, tensor, span, basis, etc.)
- missing method owner in local spec graph
- redundant or missing supercategory edge
- failed category assertion showing refined object lacks an ABC obligation

## Heuristic for spec-owned vs plugin-owned

- **Spec-owned**: method is about mathematical propositions or computations. You'd expect it in a category theory text. These are CAPABILITIES of mathematical objects in the spec. Must be IN the spec.
- **Plugin-owned**: @override where intended parent method EXISTS locally, graph path is correct, but mypy cannot see it. Output = minimal fixture for plugin repo.
- **Stub-owned**: ONLY direct Sage boundary calls where local refinement cannot provide the type. Must pass the full test above.

## Why this exists

Previous workflow falsely attributed ~50%+ of diagnostics to stub work. The actual stub-eligible surface for this repo is narrow because the spec WRAPS constructors and refines outputs by construction. Internal method inheritance should be entirely self-contained + plugin-supported.
