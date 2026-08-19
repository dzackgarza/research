---
id: FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
trackerStatus:
  type: feature
parents: []
dependsOn: []
plans:
- '[[PLAN-MYPY-PLUGIN-IMPLEMENTATION]]'
title: Mypy plugin for Sage category method override checking
status: needs-human-input
priority: high
description: 'Build a Sage-specific mypy plugin that makes @override work for Sage''s dynamic
  category method system (ParentMethods, ElementMethods, MorphismMethods) without requiring
  literal Python inheritance in category source files. The plugin injects static base/MRO
  edges derived from Sage''s runtime category resolution so that standard typing.override
  semantics function correctly during type checking for Sage itself and for third-party
  packages that define Sage category subtrees outside `sage.categories.*`.

  '
---
# Mypy Plugin for Sage Category Method Override Checking

## Objective

Sage's category framework uses metaclass-driven method injection. Categories define
`ParentMethods`, `ElementMethods`, and `MorphismMethods` as inner classes whose
methods genuinely override ancestor methods at runtime — but through metaclass
assembly, not Python class inheritance. Mypy cannot see this. The `@override`
decorator produces ~300 false-positive `misc: override` errors across the
`category_specs/` tree because mypy sees these inner classes as standalone classes
with no base defining the overridden method.

The solution: a mypy plugin that asks Sage what the runtime method-class
linearization is, maps it back to source-level method containers, and injects those
containers as static bases before mypy analyzes the class body. Standard
`@override` checking then works without any per-category protocol generation,
inherited-method enumeration, or source-level inheritance declarations.

## Scope

This feature is a narrow dynamic-inheritance plugin. It is not the root of the
repo's mypy/QC cleanup queue, and its spec/review/implementation work can proceed
independently of repo-local basic hygiene. Repo-side application of the plugin to
the research repo remains ordered by `PLAN-QC-MYPY-FOUNDATION-ORDER`, because
missing annotations, `Any`, untyped fixtures, and ordinary local code hygiene are
the first repo-local QC frontier.

- **In scope**: Mypy plugin that hooks `get_customize_class_mro_hook` to inject
  static bases for Sage category method-container classes (`ParentMethods`,
  `ElementMethods`, `MorphismMethods`, and later `Homsets.ParentMethods`,
  axiom methods, etc.)
- **In scope**: Sage-side invariant-core resolver/oracle/manifest API that maps
  Sage runtime named-class MROs to source-level provider class projections
- **In scope**: Singleton categories (parameter-free, e.g., `Groups()`, `Sets()`)
- **In scope**: Configured representatives for parameterized categories
- **In scope**: namespace-agnostic admission. A category subtree hand-rolled in
  any importable package path must be eligible if it resolves to Sage category
  semantics; source namespace is not the criterion.
- **Out of scope**: `.pyi` generation, protocol generation, IDE completion, stub
  generation as a product surface, and downstream public typing. Test-only visible
  provider stubs used to make manifest projection fixtures importable are validation
  scaffolding, not the delivered mechanism. This feature is strictly about making
  `@override` type-check correctly for Sage category implementations, whether they
  live in Sage's tree or an external package.
- **Out of scope**: basic repo typing hygiene such as missing return annotations,
  missing parameter annotations, untyped pytest fixtures, ordinary `Any`
  cleanup, and post-stub downstream category/type repairs.

## Design Summary

The plugin is a thin static projection layer:

```
Sage source:
    class C(Category):
        class ParentMethods:
            @override
            def f(self): ...

Sage runtime truth:
    C.parent_class.mro()

Plugin projection:
    C.ParentMethods has static bases = source containers from C.parent_class.mro()

Mypy result:
    ordinary @override works
```

Key design constraints from the full spec:

- Sage remains the source of truth. The plugin does not reconstruct the category
  DAG, infer supercategories, or enumerate method contracts.
- No category source file needs to add literal Python bases.
- No per-category protocol or inherited-method stub inventory is generated.
- New singleton categories automatically participate.
- Parameterized categories are explicitly configured or left unresolved — no
  parameter guessing.

## Spec

See `specs/SPEC-SAGE-MYPY-CATEGORY-OVERRIDE.md` for the full acceptance criteria
derived from the greenfield design doc.

## Why Not Alternatives

- **Explicit inheritance** (`class ParentMethods(Sets.ParentMethods)`) is
  architecturally wrong. It requires every new subcategory contributor to remember
  a non-Sage convention. One forgotten inheritance breaks static checking silently.
  The right model is: Sage knows what the ancestor methods are; make the tooling
  ask Sage.
- **Shadow files**: Useful as a debug oracle but not as primary mechanism — they
  create a generated source tree and wrapper around mypy.
- **`# type: ignore[misc]`**: ~300 per-line suppressions. Noise suppression, not a
  fix. Doesn't resolve `attr-defined` errors on `self.base_ring()` etc.

## Location

This is a standalone project on this system, not embedded in the research repo or
Sage's source tree. It imports Sage as a dependency.

- Repo: `~/sage-mypy-plugin/`
- Plugin package: `sage_mypy_category_plugin` (importable via mypy config)
- Registered via: `[mypy] plugins = path.to.plugin` in global mypy config
- QC planning artifact: `~/ai/quality-control/planning/override-sage-categories.md`

## Current Status

All phases 0–9 of the invariant-core rewrite are complete. Plugin HEAD is `8b127fa`
on branch `rewrite/invariant-core` (PR `rewrite/invariant-core → main` open in
`~/sage-mypy-plugin/`). `just test -q` passes with 187 tests across 7 suites:
structural MRO proof, manifest validation, plugin projection, resolver CLI, stubs,
behavior matrix, and automation contract. All Phase 7 cache lifecycle acceptance tests
(E1–E6: fresh/cached/stale-source/negative injection/renamed/corrupt-recovery) pass.
All Gemini HIGH/MEDIUM review comments addressed.

The feature is awaiting the PR merge (human gate via `TASK-MYPY-PARSER`). Once the
PR merges to `main`, `PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` in
`PLAN-QC-MYPY-FOUNDATION-ORDER` becomes selectable.

Repo-side QC work must still follow `PLAN-QC-MYPY-FOUNDATION-ORDER`: complete
basic typing hygiene first (now done: 407 errors, all plugin-shaped), then apply/
review this dynamic-inheritance lane, then stub generation, then downstream type
cleanup. That repo-local ordering does not block this standalone plugin feature.
