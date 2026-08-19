---
id: FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER]]'
- '[[FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS]]'
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
plans: []
title: Coble geometric lattice foundation
status: unstarted
priority: critical
description: Construct the rational 10-nodal sextic, Coble blowup, K3 double cover, Picard pullback lattice, discriminant/complement data, and primitive embedding chain required before downstream Coble orbit, group, Coxeter, involution, and stable-model verification.
---
# Feature: Coble geometric lattice foundation

## Summary

Own the foundational Coble geometry and lattice pipeline from `GOAL.md` Tasks 1.1-1.3. Downstream Coble features must consume this feature's constructed objects and verified lattice data instead of treating standard presentations or expected invariants as inputs.

## Source Provenance

- `GOAL.md`, section "Foundation: Coble Curves and Picard Lattices".
- `theory/foundations/coble-task-background.md`, sections `Task 1.1`, `Task 1.2`, and `Task 1.3`.
- `theory/references/index.md`, claim families for Coble curve/blowup/K3 cover, Coble/Enriques moduli, and lattice-theoretic structure and embeddings.

## Scope

- Derive or source an explicit rational plane sextic with ten ordinary nodes and construct the corresponding K3 double cover.
- Construct the blowup Picard lattice of the Coble surface through semantic geometry objects and maps.
- Compute the K3 pullback lattice `S_Co = f^*Pic(S)` from the constructed cover, not by postulating the target Gram matrix.
- Compute discriminant group data, Nikulin invariants, primitive closure when needed, and the orthogonal complement `T_Co` inside `Lambda_K3`.
- Derive the primitive embedding chain into the Enriques, del Pezzo, and K3 comparison lattices with explicit source-backed hypotheses.

## Non-Goals

- Do not use `I_{1,10}(2)`, `N = <2> + E_10(2)`, or any named standard presentation as the input proof of the Coble pipeline.
- Do not perform ad hoc polynomial, Jacobian, Gram-matrix, or embedding calculations outside typed geometry and lattice objects.
- Do not treat downstream cusp, arithmetic-group, Coxeter, involution, or stable-model features as complete until they consume this foundation.

## Acceptance Criteria

- [ ] A rational sextic with ten ordinary nodes is constructed or sourced with enough data to verify the node and rationality conditions.
- [ ] The Coble blowup, canonical class, boundary divisor, Picard generators, and intersection pairing are produced through geometry interfaces.
- [ ] The K3 double cover and pullback map produce `S_Co = f^*Pic(S)` as a computed lattice object.
- [ ] The expected presentation `I_{1,10}(2)` is verified as an isometry target, not assumed as input.
- [ ] Discriminant group, discriminant form, Nikulin invariants, primitive closure, and `T_Co = S_Co^perp` are computed with source-backed checks.
- [ ] Primitive embedding matrices or morphisms for the comparison chain are derived from the computed lattices and theorem hypotheses.

## Dependencies And Boundaries

This feature is downstream of the semantic substrate in the dependency DAG: category specs, ModulesWithForms/lattice surfaces, geometry category interfaces, categorical implementation, and universal categorical algorithms. It is the required direct dependency for downstream Coble feature roots that need `S_Co`, `T_Co`, discriminant forms, polarization data, or primitive embeddings.

## Work Log

- Created as the missing GOAL.md Task 1 feature card and wired downstream Coble feature roots through it.
