---
id: TASK-01KQN9YGCPGDG2XCR55YCTXR53-IMPLEMENT-POSET-CERTIFICATE-METHODS-AS-SEPARATE-WITNESS-RETURNING-METHOD
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
dependsOn: []
title: Implement poset certificate methods as separate witness-returning methods while
  keeping boolean predicates boolean
status: complete
priority: high
description: Posets mapping owns constructor names, finite surface methods, certificate
  method split, deferred non-core surface ownership, and slice/coslice structure methods.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- When closing deferred surface mapping, place each method by target mathematical
  object or display/interop status.
- Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS
---
# Implement poset certificate methods as separate witness-returning methods while keeping boolean predicates boolean
## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Implement poset certificate methods as separate witness-returning methods while keeping boolean predicates boolean from category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [x] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [x] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Implemented the mapped certificate split as named final
  project methods. Finite-poset certificate methods now delegate to Sage's
  documented `certificate=True` behavior: `height_certificate`,
  `width_certificate`, `meet_semilattice_certificate`, and
  `join_semilattice_certificate`.
- 2026-05-05: Implemented finite order-theoretic lattice certificate methods
  by delegating to Sage's documented `certificate=True` predicate variants:
  `atomic_certificate`, `coatomic_certificate`, `complemented_certificate`,
  `distributive_certificate`, `modular_certificate`, and
  `modular_elements_certificate`. Boolean predicate surfaces remain boolean.
- 2026-05-05: While wiring Sage-backed finite lattice methods, corrected the
  return annotations for `join_irreducibles_poset`,
  `meet_irreducibles_poset`, and `irreducibles_poset` from lattice-poset to
  poset. Sage's `FiniteLatticePosets.ParentMethods` source returns induced
  subposets of irreducible elements, not generally lattices.
- 2026-05-05 validation: `just --justfile category_specs/justfile category-obligation-file
  posets/category_obligations.sage` passed; `just --justfile category_specs/justfile
  check-abstract-redefinitions` passed; `git diff --check` passed.

## Review Log

- 2026-05-07 dependency-ready leaf check: this card has no unmet `dependsOn` edges and
  was selected from the DAG frontier; dependency-waiting tasks were not attempted or
  marked blocked.
- Source and mapping review: `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7-MAP-POSET-DEFERRED-GRAPH-POLYTOPE-ORDER-COMPLEX-ALGEBRA-POLYNOMIAL-COXET`
  records the deferred graph/display/polytope/order-complex/algebra/polynomial/Coxeter
  surfaces by target mathematical object or display/interop exclusion, so the deferred
  acceptance item is covered without adding a second mapping document.
- Focused verification passed:
  `just --justfile category_specs/justfile category-obligation-file posets/category_obligations.sage` and
  `just --justfile category_specs/justfile check-abstract-redefinitions`.
- Spec-weakening review: certificate-bearing Sage predicates are preserved as named
  witness-returning methods, while boolean predicates remain boolean; order-theoretic
  lattice vocabulary remains separated from module/quadratic lattice vocabulary.
