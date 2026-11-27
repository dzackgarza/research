---
id: TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Write Hom End Aut forms and lattice method ownership rows
status: complete
priority: critical
owner: Zack
description: Mine Hom/End/Aut, forms, and lattice inventories into literal method-owner
  rows, preserving formed-module ownership and lattice-specific endpoint boundaries.
successCriteria:
- The target method-inventory spec contains Hom, End, Aut, forms, symmetric bilinear,
  quadratic, free bilinear, torsion, and lattice method tables.
- Form divisibility is recorded as the pairing-image submodule or ideal on symmetric
  bilinear elements and is not conflated with free-module coordinate gcd notions.
- Orthogonal groups are recorded as automorphism objects in the relevant formed-module
  category, with special or stable refinements placed only where their extra hypotheses
  are sourced.
- Lattice rows distinguish forms-owned methods from lattice endpoint methods and record
  backend routing where an algorithm is involved.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Write Hom End Aut forms and lattice method ownership rows

## Summary

Write the literal method-owner rows for Hom/End/Aut, forms, and lattices. This is the
highest-risk category-method section because it controls morphism semantics,
isometries, divisibility, discriminant objects, and algorithm routing.

## Source Provenance

- `category_specs/homsets/docs/SAGE_INVENTORY.md`
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/forms/docs/SAGE_INVENTORY.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `category_specs/lattices/docs/MAPPING.md`
- `projects/github.com__dzackgarza__lattice-research/context/bilinear-forms-duals-morphisms`
- `src.bak/spec-backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`
- `src.bak/spec-backups/lattices_written_spec_backup.py`
- Lattice memories and cards that state `src.bak/spec-backups/*` files are written
  source material for the redesign, not compatibility-shim targets.

## Context

The seed rows include:

- Hom/End/Aut: `C.HomCategory().Of(A, B)`, `C.EndCategory().Of(A)`,
  `C.AutCategory().Of(A)`, `domain`, `codomain`, `identity`, `zero`, evaluation,
  composition, endomorphism predicates, `is_invertible`, `is_isomorphism`, `inverse`,
  `order`, `AutCategory.from_end_category`;
- forms: `form`, form evaluation, `form_degree`, bilinear evaluation, `self_product`,
  `is_isotropic`, `perp`, `orthogonal_submodule_to`, quadratic evaluation,
  symmetric/alternating/nondegenerate/integral/even predicates, `twist`;
- free bilinear modules: `gram_matrix`, `inner_product_matrix`, determinant,
  discriminant, rank-dependent signatures, direct sums, tensor products,
  base-change, rational span;
- divisibility: for `b: M x M -> S`, `divisibility(v)` is the submodule
  `<b(v, M)> <= S`; when `S = R`, this is an ideal of `R`;
- lattices and discriminant objects: dual lattice, discriminant group, inclusion
  morphism, discriminant class, overlattices, primitive embeddings, genus,
  Nikulin invariants, isometry tests, roots, reflections, short-vector surfaces;
- torsion forms: torsion bilinear/quadratic Gram matrices, value modules,
  primary parts, Brown invariant, normal forms, additive order, lifts;
- groups: `orthogonal_group` as `Aut_C(M)` for a formed-module category, and
  determinant/orientation refinements only where their owner is sourced.

## Complexity And Ownership

- Owner/role: Hom/forms/lattice spec writer with lattice-redesign context.
- Complexity: `80` (high).
- Rationale: the task is still one executable output table, but mistakes here can poison
  the lattice implementation and backend routing.
- Split/promote note: if lattice methods alone become plan-scale, keep Hom/forms rows in
  this task and split lattice algorithms into a follow-up spec card under the lattice
  roadmap.

## Acceptance Criteria

- [x] The target method-inventory spec contains Hom, End, Aut, forms, symmetric bilinear, quadratic, free bilinear, torsion, and lattice method tables.
- [x] Form divisibility is recorded as the pairing-image submodule or ideal on symmetric bilinear elements and is not conflated with free-module coordinate gcd notions.
- [x] Orthogonal groups are recorded as automorphism objects in the relevant formed-module category, with special or stable refinements placed only where their extra hypotheses are sourced.
- [x] Lattice rows distinguish forms-owned methods from lattice endpoint methods and record backend routing where an algorithm is involved.

## Dependencies And Boundaries

- Do not treat a lattice as a positive-definite cryptographic lattice or as an embedded
  vector-space object with a basis chosen by default.
- Do not place Gram matrices or coordinate methods before the free/basis hypotheses
  required by the mapping docs.
- Do not make isometry, automorphism, or orthogonal-group methods return generic groups
  without recording the category whose automorphisms are being taken.
- Do not implement any lattice algorithm in this card.

## Work Log

- 2026-05-05: Created as the Hom/forms/lattice leaf for the literal method ownership inventory phase.
- 2026-05-06: Added Hom/End/Aut, module-hom, formed-module, bilinear/quadratic,
  symmetric divisibility, free/torsion form, lattice, discriminant-object, orthogonal
  group, and algorithm-facing lattice rows to
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`. Moved this task to needs-agent-review.
- 2026-05-07: Repaired stale source-provenance paths after Gate 1 review found this
  card still cited deleted `theory/foundations/...` and `.agents/theory/spec-backups`
  roots. The card now matches the active target spec provenance:
  `projects/github.com__dzackgarza__lattice-research/context/bilinear-forms-duals-morphisms` and
  `src.bak/spec-backups/*`.

## Review Log

### Review 2026-05-07 (Sagan)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope; independent
re-review still required

#### Gate 1 Finding: Stale Source-Provenance Paths

- This task card cited `theory/foundations/bilinear-forms-duals-morphisms.md` and
  `.agents/theory/spec-backups/*` paths that no longer exist.
- The target inventory spec already uses the corrected sources, so the card
  provenance was inconsistent with the source-grounding surface.

#### Rework

- Updated the card source provenance to
  `projects/github.com__dzackgarza__lattice-research/context/bilinear-forms-duals-morphisms`.
- Updated the lattice spec-backup sources to
  `src.bak/spec-backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`
  and `src.bak/spec-backups/lattices_written_spec_backup.py`.

### Re-review 2026-05-07 (Schrodinger)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- Confirmed the stale-path Gate 1 issue is repaired in the live provenance and matches
  target-spec provenance for the bilinear-form memory and `src.bak/spec-backups`
  lattice-source corpus.
- Confirmed stale deleted paths remain only as historical review-log descriptions.
- Spot-checked that Hom/Aut rows preserve categorical owners, form preservation and
  orthogonal groups route through formed-module Hom/Aut, divisibility is
  pairing-image rather than coordinate gcd, and metric dual/discriminant rows keep
  `L^#` separate from Hom dual.
- `just plan-validate` passed with 225 root planning cards.

#### Residual Risk

- This was a review and spot-check of the card and relevant rows, not a full re-audit
  of every target-spec row or human acceptance.
