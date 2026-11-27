---
id: DECISION-NIKULIN-INVARIANTS-DISCRIMINANT-FORM-RESEARCH-GAP
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Nikulin invariants discriminant-form research gap
status: decided
chosen: discriminant-form surface, not invariant tuple
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decision: Nikulin invariants discriminant-form research gap

## Problem

The lattice spec surface for `nikulin_invariants()` records a convenience invariant
tuple such as `(r, a, delta)` under the sourced 2-elementary hypotheses. This can support
classification statements, but it is not the discriminant form object.

However, the downstream Coble orbit analysis (GOAL.md Tasks 2.1-2.2, isotropic
vector orbit enumeration under the stable orthogonal group) requires:

- The actual discriminant **form** `q_T: A_T -> Q/2Z`, not just its 2-elementary type.
- The orbit structure of isotropic vectors in `A_T` under `O(q_T)`.
- The lifting of those orbits back to vector orbits in `T_Co`.

The `nikulin_invariants()` surface is therefore too narrow for these needs and must not
own orbit, lifting, or finite quadratic-module semantics.

## Decision

The spec route is object-level discriminant-form machinery, not invariant-tuple
machinery:

- `L.discriminant_group()` returns the finite torsion formed module `A_L = L^#/L`
  carrying the descended quotient-valued bilinear/quadratic form data.
- `discriminant_form()` is named access to that quotient-valued form data, never a
  synonym for `nikulin_invariants()`.
- `DiscriminantGroup`/torsion quadratic-module elements inherit generic formed-module
  evaluation and isotropic predicates, such as `q(x)`, `b(x,y)`, and
  `is_isotropic(x)`.
- Finite discriminant groups add finite carrier enumeration surfaces such as
  `isotropic_elements()`.
- `DiscriminantGroupAut` or a typed finite group-action object owns `orbit(x)`,
  `orbits(S)`, and `orbit_representatives(S)` for actions on typed discriminant-group
  subsets such as isotropic elements.
- `L.orthogonal_group()` owns the bridge to discriminant automorphisms through
  `discriminant_action()`, `image_in_discriminant_orthogonal_group()`, and
  `kernel_of_discriminant_action()`.
- Orbit lifting from discriminant-form data back to lattice vector or submodule orbits
  is theorem-backed lattice orthogonal-group work. It may use Nikulin/Eichler/Sterk
  inputs only after the hypotheses are checked against the actual computed lattice and
  discriminant form.

## Spec Updates

This decision is implemented in `SPEC-MAPPING-LATTICES.md` by adding:

- finite discriminant-form accessors and isotropic-element enumeration surfaces;
- finite group-action orbit methods on the action/group object;
- lattice orthogonal-group methods for the homomorphism `O(L) -> O(A_L,q_L)`;
- an explicit note that `nikulin_invariants()` is only a sourced classification summary
  and cannot replace the discriminant group/form for Coble orbit analysis.

## Sources

- `SPEC-MAPPING-LATTICES.md`: lattice metric dual, discriminant group, torsion
  quadratic-module, and orthogonal-group ownership.
- Sage `torsion_quadratic_module.py`: element `b`/`q`, torsion form matrices,
  `orthogonal_group()`, and examples computing the kernel of the action of `O(L)` on
  `L.discriminant_group()`.
- `theory/foundations/coble-task-background.md`: Task 2.1 requires the actual
  discriminant form and isotropic orbit structure; Task 2.2 requires hypothesis-checked
  orbit lifting.
- `theory/references/index.md`: Nikulin, Sterk, Dolgachev-Kondo, and related orbit and
  boundary references for downstream theorem use.
