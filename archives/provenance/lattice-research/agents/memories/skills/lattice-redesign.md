---
title: Lattice Redesign
status: active
date: 2026-05-29
---
# Lattice Redesign

This skill owns the canonical lattice-redesign source doctrine migrated from the retired
`.agents/plans/` directory.

## Load references by task

- `mem:skills/lattice-redesign/category-abc-spec`: load for `ModulesWithForms`, form
  codomains, parent/element/morphism methods, homsets, tensor/cartesian/dual objects,
  cokernels, discriminant descent, and named downstream categories.
- `mem:skills/lattice-redesign/lattice-interface-style-guide`: load before editing or
  reviewing lattice APIs, public mathematical vocabulary, morphism semantics,
  discriminant groups, orthogonal groups, predicates, validation, or anti-wrapper
  compliance.
- `mem:skills/lattice-redesign/lattice-redesign-corrections-spec`: load when resolving
  design disputes, interpreting user corrections, or checking non-negotiable
  preservation/source-of-truth rules.

## Hard rules

- The spec is the target; incomplete implementation is not evidence that the spec is
  stale.
- Use noun-owned mathematical APIs, not helper-function piles.
- Treat lattices as presented modules with forms.
  Changing generators or basis data produces a distinct but possibly isometric object,
  not the same object.
- Do not import Sage's ambient-vector-space lattice convention into public semantics.
- Dual and discriminant semantics must route through real categorical objects and
  morphisms.
- Rational-to-integral promotion is owned by the rational/free-bilinear constructor
  layer; call sites must not each invent their own cast-to-lattice rule.
- Backend group matrices must be normalized once at the backend boundary before they
  enter public orthogonal-group semantics.
- Do not preserve compatibility shims unless explicitly requested.

## Referenced documents

[ModulesWithForms Category: ABC Contracts](lattice-redesign/category-abc-spec)

[Lattice Interface Style Guide](lattice-redesign/lattice-interface-style-guide)

[Lattice Redesign Corrections Spec](lattice-redesign/lattice-redesign-corrections-spec)
