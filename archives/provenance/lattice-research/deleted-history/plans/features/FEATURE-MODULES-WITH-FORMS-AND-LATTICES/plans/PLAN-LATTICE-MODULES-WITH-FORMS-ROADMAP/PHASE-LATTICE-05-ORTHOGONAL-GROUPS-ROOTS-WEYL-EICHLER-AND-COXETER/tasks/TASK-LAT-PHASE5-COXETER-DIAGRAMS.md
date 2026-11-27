---
id: TASK-LAT-PHASE5-COXETER-DIAGRAMS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement Coxeter diagrams and subdiagram posets
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
  is approved.
successCriteria:
- Read the cited source section before implementation.
- Keep changes inside the named target boundary unless a new card or decision expands
  scope.
- Preserve the mathematical semantics from the source plan and category-spec style
  rules.
- Record validation commands and results before handoff.
- Do not mark this card done without human approval.
complexity: 55
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER
---
# Implement Coxeter diagrams and subdiagram posets

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.8: Coxeter Diagrams
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.8),
`theory/backends/vinberg-algorithm.md`, `theory/references/index.md`,
`category_specs/lattices/docs/MAPPING.md`, and `lattice-interface-style-guide.md`.

- A Coxeter diagram is the weighted graph attached to a chosen simple-root set or,
  more generally, to root hyperplanes whose pairwise angles/Coxeter exponents are
  already determined by a backend or finite root-system constructor.
- `CoxeterDiagram` is therefore a local graph/poset object:
  - nodes correspond to chosen simple roots;
  - edge labels/weights encode the Coxeter relation data supplied by the root/Coxeter
    backend;
  - `subdiagram`, `subdiagram_poset`, `Aut`, and connectivity checks are local
    operations on that weighted graph.
- Ownership split:
  - Vinberg-style backend code owns hyperbolic simple-root discovery and Coxeter-matrix
    production for reflective indefinite lattices;
  - `src/lattices/groups/coxeter.py` owns the diagram object, induced-subdiagram
    structure, poset operations, and graph automorphisms after those roots are known.
- For finite crystallographic root lattices, the same local object may be built from
  standard root-system/Cartan data; for indefinite reflective cases it must consume the
  Vinberg backend output rather than reconstructing the hyperbolic algorithm locally.
- Vinberg's algorithm implementation is a wrapping/adaptation task, not a
  reimplementation from scratch. The reference implementations (VinbergsAlgorithmNF in
  Julia, AlVin in C++, vinal in Python/Sage) and the polyhedral_common Lorentzian
  edgewalk (`LORENTZ_RunEdgewalkAlgorithm`) are available as sources. See
  `.agents/memories/theory/backends/vinberg-algorithm.md` for the full survey and
  wrapping strategy.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/coxeter.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.
