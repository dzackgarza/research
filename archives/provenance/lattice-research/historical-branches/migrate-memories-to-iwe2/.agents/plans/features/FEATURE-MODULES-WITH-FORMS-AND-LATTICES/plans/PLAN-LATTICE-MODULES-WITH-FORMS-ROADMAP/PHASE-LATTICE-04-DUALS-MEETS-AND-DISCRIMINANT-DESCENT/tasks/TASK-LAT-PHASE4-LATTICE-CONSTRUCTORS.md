---
id: TASK-LAT-PHASE4-LATTICE-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
dependsOn: []
title: Admit named lattice constructors through lattice meets
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is
  approved.
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
- PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT
---
# Admit named lattice constructors through lattice meets

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: Named lattice constructors and lattice meets
- Parent plan: `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `theory/spec_backups/lattices_written_spec_backup.py`, `category-abc-spec.md`, `category_specs/lattices/docs/MAPPING.md`, and `pln-lattice-phase-4-discriminant-descent.md` (Step 4.4).

- Lattice constructors are on `Lattice` endpoints and must follow explicit meet names:
  - `Lattice.Z()`, `Lattice.U()`, `Lattice.A(n)`, `Lattice.D(n)`, `Lattice.E(n)`, `Lattice.I(p,q)`, `Lattice.II(p,q)`, `Lattice.k3()`, `Lattice.coble_picard()`, `Lattice.root_lattice(name)`, `Lattice.from_gram(G)`, `Lattice.from_string(s)`.
- Named constructors must return concrete `Lattice` or `RationalLattice` instances under the same constructor logic:
  - `from_gram` builds via `RationalLattice.from_gram` and promotes to `Lattice` only when integral coefficients are integral-valued.
- `twist(n)` is exact form scaling and changes form only.
- Scalar multiple `n * L` is a submodule with `n^2`-scaled Gram matrix and different basis image from twist.
- Direct sum `L1 + L2` returns a lattice with explicit summand embeddings:
  - tuple of summands, embedding maps are subobject morphisms, and `iota_i`/projections participate in orthogonal decomposition checks (`iota_i.image().perp() == iota_j.image()` for `i != j`).
- `discriminant_group()` path must be via `self.dual().inclusion_morphism().cokernel()` (same as plan), not a bypass API.
- `dual()` and `discriminant_group()` must preserve the algebraic-dual versus
  rational-dual split from the theory note: public lattice constructors build the
  presented lattice, while the dual/discriminant constructors build the actual
  dual/cokernel objects with explicit morphisms.
- `from_string("U(2) + A_1")` parses to the above operations, and parser output must respect direct-sum semantics.
- `is_isometric_to(other,witness=False)` returns witness morphism when `witness=True`, and witness lives in `L.Hom(other)`.

Backend routing:
- Constructor internals are local; invariant and comparison calls follow the phase-level backend map:
  - integer-lattice isometry/genus/isotropic queries route to the Julia/Sage/CARAT/Indefinite stack in later cards;
  - this file itself only wires constructor contracts and return-codomain assumptions.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/lattices.py`.

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
  current Sage objects pass category-obligation examples before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.
