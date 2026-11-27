---
id: DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[TASK-INTEGRATE-VARIETIES-CATEGORY]]'
- '[[TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY]]'
title: Decide Picard group and Picard lattice method ownership
status: decided
options:
- name: Picard group is primary and Picard lattice is a refinement
  pros:
  - Matches the general Picard group meaning as line bundles or divisor classes.
  - Avoids treating every variety Picard object as a lattice.
  cons:
  - Requires an explicit bridge surface for surfaces with an admitted intersection pairing.
- name: Picard lattice is primary for surface workflows
  pros:
  - Matches the dominant Coble, K3, and reflection-group source material.
  cons:
  - Conflates a surface-specific lattice with the general Picard group of a variety.
- name: Separate PicardGroup and PicardLattice owners with explicit bridge methods
  pros:
  - Preserves the distinct mathematical objects and prevents downstream conflation.
  - Lets `picard_group()` and lattice intersection methods cite different hypotheses.
  cons:
  - Requires both geometry and lattice vocabulary before implementation cards can use the bridge.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide Picard group and Picard lattice method ownership

## Summary

Decide how the method inventory should route `picard_group()`, `intersection_matrix()`,
and `underlying_picard_group()` without collapsing the general Picard group into a
surface-specific Picard lattice.

## Source Provenance

- `theory/backends/abstract-to-external-mapping.md`: source rows for
  `Variety.picard_group()`, `PicardGroup.intersection_matrix()`, and malformed
  `PicardeLattice.underlying_picard_group()`.
- `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`: current checked
  path for the migrated backend rows above.
- `theory/foundations/reflective-two-elementary-lattices.md`: local definition section
  `Picard lattice`.
- `theory/foundations/coble-task-background.md`: Coble blowup Picard lattice source
  material.
- `theory/references/literature/pieroni_2026_coble_surfaces.md`: Picard group, divisor,
  canonical class, and surface intersection context.
- `theory/references/literature/huybrechts_k3_lectures.md`: K3 Picard group and
  Neron-Severi/Picard lattice context.
- Geometry source-admission cards
  `TASK-INTEGRATE-VARIETIES-CATEGORY` and
  `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`.

## Decision

Choose: **Separate PicardGroup and PicardLattice owners with explicit bridge methods.**

`picard_group()` returns a `PicardGroup` object for the admitted scheme/variety Picard
surface. Surface categories inherit this method. Its codomain is not a lattice, even
when downstream surface workflows eventually construct a Picard lattice from it.

`PicardGroup` represents line-bundle or divisor-class data with its maps and
generators. A `PicardLattice` is a formed lattice object obtained only after the
surface side has supplied algebraic/divisor classes, quotient conventions, and an
intersection pairing. The source-admission owner for this bridge is the
dimension-two smooth proper/projective surface refinement, with stricter K3, Coble,
Enriques, rational-surface, or blowup refinements supplying specialized constructors
and backend routes. This follows the `Method Ownership Guidance` section of
`TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`, together with
`TASK-INTEGRATE-VARIETIES-CATEGORY` under `Method Ownership Guidance`, which states
that `picard_group()` is owned by a variety/scheme Picard surface and that Picard
lattices remain separate bridge objects requiring surface/intersection-form
hypotheses.

`intersection_matrix()` is therefore not admitted on arbitrary `PicardGroup`. The
public owner is `PicardLattice` or a stricter Picard-lattice refinement. A backend row
written as `PicardGroup.intersection_matrix()` maps to the project path
`picard_group().picard_lattice(...).intersection_matrix()` or to a construction that
returns a `PicardLattice` first. The matrix is evidence/output of the lattice object,
not a substitute for the Picard group, divisor generators, or surface pairing.

Admit `underlying_picard_group()` only on `PicardLattice` as a bridge back to the
source `PicardGroup`. It returns the Picard group together with enough provenance to
recover the divisor generators, quotient convention, and pairing used to build the
lattice. Do not expose the malformed `PicardeLattice` spelling. Do not admit a general
`PicardGroup.as_lattice()` method; use an explicitly named Picard-lattice construction
under the surface/intersection-pairing hypotheses.

Backend consequence: Sage/Macaulay2/Oscar rows may help compute Picard groups or
divisor classes, and Oscar/Hecke-style integer-lattice routes may realize the final
formed lattice after the pairing is known. No backend row may collapse the two public
objects.

## Context

The assembled method inventory has two nearby but distinct source surfaces:

- `picard_group()` on varieties or surfaces, whose general meaning is a Picard group
  of line bundles or divisor classes.
- Picard-lattice methods such as `intersection_matrix()` and
  `underlying_picard_group()`, whose meaning requires a surface, an intersection
  pairing, and a lattice realization.

The backend map also contains the malformed spelling `PicardeLattice`, already blocked
by `DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`. This decision is
about the mathematical owner split, not merely the typo.

## Acceptance Criteria

- [x] State whether `picard_group()` returns a `PicardGroup` object for general
  varieties, a surface-specific lattice object, or another named object.
- [x] State the minimal owner and hypotheses for `intersection_matrix()` on Picard data.
- [x] State whether `underlying_picard_group()` is an admitted public bridge method,
  and if so on which Picard-lattice owner.
- [x] Cite the exact geometry source-admission card or source section that justifies
  the chosen owner.
- [x] Update the literal method ownership inventory before any implementation card uses
  these surfaces.

## Dependencies And Boundaries

- Do not implement Picard group or Picard lattice methods until this decision is made.
- Do not use the malformed `PicardeLattice` spelling as a public API.
- Do not assume the Picard group and Picard lattice coincide outside the hypotheses
  recorded by this decision.

## Work Log

- 2026-05-06: Created by the literal method inventory gap audit as the one remaining
  mathematical owner split not covered by existing source-admission cards.
- 2026-05-06: Decided to keep `PicardGroup` and `PicardLattice` separate, with
  `picard_group()` returning the group object and `PicardLattice` owning
  `intersection_matrix()` plus `underlying_picard_group()` under surface
  intersection-pairing hypotheses.
