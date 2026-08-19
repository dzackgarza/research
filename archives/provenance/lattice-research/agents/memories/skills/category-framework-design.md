---
title: Category Framework Design
status: active
date: 2026-05-29
---
# Category Framework Design

This skill owns Sage category-framework design references migrated from the retired
`.agents/plans/` directory.

## Load references by task

- `references/category-refinement-phases.md`: load before staging category hierarchy,
  concrete interceptors, or top-level constructor redefinitions.
- `references/category-creation-notes.md`: load for `_refine_category_`,
  `Category_singleton`, `Category_over_base_ring`, and category cache behavior.
- `references/axioms-with-generators-finitely-presented.md`: load for WithGenerators,
  FinitelyPresented, Dedekind/PID module categories, Homsets, Endsets, Autsets, and
  corrected axiom hierarchy.
- `references/homsets-structural-core.md`: load for Homsets as module objects, dual
  modules, Endset algebra structure, and rank semantics.
- `references/autset-categories-path.md`: load for source-backed Autset admission and
  Endset construction path.
- `references/autset-integration-plan.md`: load when decomposing Autset implementation
  cards.

## Hard rules

- Static hierarchy and method surface come before constructor interception.
- Runtime inspection may inform the source map but must not become generic runtime
  discovery in the spec.
- Autsets are structural category objects below Endsets, not ad hoc group wrappers.
- Dual-object routing must reflect the mathematical Hom object when applicable.
- Dynamic inheritance of specs and implementation providers is intentional.
  Do not replace it with explicit subclassing, trivial re-call wrappers, local casts, or
  provider-splicing merely because a static checker cannot see the category graph.
  Route those conflicts to the static-model/plugin/stub/QC lane unless they expose a
  real mathematical owner, codomain, hypothesis, or constructor-boundary defect.
- Repeated casts around inherited category results are evidence that the framework
  design needs agent review.
  Decide whether the spec implementation belongs at a downstream ABC implementation
  boundary or whether QC tooling must model inherited category promotion; do not
  normalize local cast patterns as framework glue.

## Referenced documents

[How Endset Categories Are Constructed](category-framework-design/autset-categories-path)

[Autset Integration Plan](category-framework-design/autset-integration-plan)

[Axioms: WithGenerators, FinitelyPresented, and Structural Patterns](category-framework-design/axioms-with-generators-finitely-presented)

[Category Creation: Base Rings and Module Categories](category-framework-design/category-creation-notes)

[Category Refinement Phases](category-framework-design/category-refinement-phases)

[Homsets — the Structural Core](category-framework-design/homsets-structural-core)
