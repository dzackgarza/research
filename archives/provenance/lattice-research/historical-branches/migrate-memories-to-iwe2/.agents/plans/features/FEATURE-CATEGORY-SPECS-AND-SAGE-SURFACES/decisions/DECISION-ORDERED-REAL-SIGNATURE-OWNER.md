---
id: DECISION-ORDERED-REAL-SIGNATURE-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide ordered real realization owner for signature and definiteness methods
status: decided
chosen: Add ordered-real-realization refinement to formed modules
options:
- name: Add ordered-real-realization refinement to formed modules
  pros:
  - Captures the real mathematical hypothesis needed for signature and definiteness.
  - Lets integral lattices inherit signature through the standard embedding into real
    scalars.
  cons:
  - Requires naming and wiring a new base-scalar refinement before implementation.
- name: Keep signature only on explicit integer and real-field lattice endpoints
  pros:
  - Matches currently visible Sage implementation evidence more closely.
  - Avoids adding a broad refinement before source review.
  cons:
  - Leaves number-field or other ordered-domain cases without a general owner.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide ordered real realization owner for signature and definiteness methods

## Summary

The mathematical-correctness audit found that the Lattices mapping spec placed
`signature_pair()`, `signature()`, `is_positive_definite()`, and
`is_negative_definite()` at `Free + Symmetric + OverIntegralDomain`. That is too broad:
an arbitrary integral domain does not provide signs, eigenvalue ordering, or a chosen
real realization.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- Sage source `sage/modules/free_quadratic_module_integer_symmetric.py`, where the
  visible implementation evidence is `ZZ`-specific.

## Context

Signature data is meaningful for finite free symmetric bilinear data after extension to
a signed scalar context, for example `ZZ -> QQ -> RR`. The current category vocabulary
has `OverIntegralDomain`, but that only supplies a fraction field; it does not supply
an ordered field, a real embedding, or a rule for comparing signs.

## Acceptance Criteria

- Choose the category/refinement owner for signature and definiteness methods.
- Record whether the owner is a new formed-module/lattice refinement or only selected
  endpoint methods such as `OverZZ` and real-field formed modules.
- Update Lattices and Forms mapping specs so method rows state caller category,
  hypotheses, codomain/return object, and source evidence.
- Block implementation of general signature/definiteness surfaces until this decision
  is made.

## Dependencies And Boundaries

This decision does not block ordinary `ZZ` lattice signature interop, but it blocks any
claim that signature or definiteness is owned by all free symmetric bilinear modules
over integral domains.

## Decision

Choose the ordered-real-realization refinement.

The owner is finite free symmetric formed modules equipped with a selected ordered real
realization of their scalar context. Concretely, a caller must have finite free
symmetric bilinear data and either:

- a canonical ordered real realization, such as the `ZZ -> QQ -> RR` path used by
  integral lattice interop; or
- explicit structure naming an ordering or real embedding of the fraction field/base
  field into an ordered real target.

The no-argument methods `signature_pair()`, `signature()`, `is_positive_definite()`,
and `is_negative_definite()` are valid only when that ordered real realization is part
of the object/category context. For fields or domains with multiple orderings, the
method is not owned by the bare base category; either the object must carry a chosen
realization or a separate future surface must expose total-signature data indexed by
orderings.

The owner is not all `OverIntegralDomain` objects. A fraction field alone has no sign
comparison, no eigenvalue ordering, and no selected real closure. The `OverZZ` Sage
surface remains concrete implementation evidence because Sage computes
`signature_pair()` by forming the Gram matrix over `QQ` and taking the positive and
negative eigenvalue counts in the standard real ordering.

## Source Grounding

- `theory/references/literature/milnor1973symmetric.md` §2 defines ordered fields,
  positive and negative subspaces, and the signature at an ordering `P` as
  `rk(X^+) - rk(X^-)`; it also records that the signature at `P` is an isomorphism
  invariant and a Witt-ring homomorphism.
- Installed Sage source
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/free_quadratic_module_integer_symmetric.py`
  defines `signature_pair()` for integral symmetric lattices as the positive and
  negative eigenvalue counts of the Gram matrix via `QuadraticForm(QQ,
  self.gram_matrix()).signature_vector()[:2]`, and `signature()` as their difference.
- `SPEC-MAPPING-LATTICES.md` already records the corrected owner as free symmetric
  data with an ordered real realization, with `OverIntegers` as concrete Sage evidence.

## Spec Updates

- `SPEC-MAPPING-LATTICES.md` now treats the decision as settled: the abstract owner is
  finite free symmetric bilinear data with a selected ordered real realization.
- `SPEC-MAPPING-FORMS.md` now maps definite and indefinite bilinear axioms through the
  same ordered-real-realization owner rather than leaving a pending decision.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` now states that the no-argument
  signature methods require a selected ordered real realization.

## Work Log

- 2026-05-06: Created from the mapping mathematical-correctness audit after detecting
  the over-broad `OverIntegralDomain` owner.
- 2026-05-06: Decided the owner as finite free symmetric formed modules with selected
  ordered real realization; bare integral-domain ownership remains rejected.
