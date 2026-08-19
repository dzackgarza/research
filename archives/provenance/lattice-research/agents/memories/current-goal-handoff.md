---
title: Current Goal Handoff
---
# Handoff

## Current Phase

Category-spec vocabulary. The live goal is to define the mathematical language needed
by the later Coble/K3 lattice program: typed modules, formed modules, lattices,
Hom/End/Aut objects, morphisms, discriminant forms, metric duals, embeddings,
orthogonal complements, subgroup objects, and witness data grounded in Sage/source
evidence.

Downstream Coble subgroup, cusp, and orbit computations are not the next action unless
they expose a missing foundational definition. Existing Coble theory notes may be used
as research needs; they are not the active work item.

## Next Mathematical Obligation

The Hom/morphism classification in `SPEC-MAPPING-LATTICES` is now resolved.
The Lattices Homset Mirroring Audit (rows 409-498) and Inherited Module and Hom
Surfaces (rows 292-330) cover the full Sage Hom cluster — generic Hom/End, free-module
and FGP Hom parents, matrix morphisms, formed-module Aut, and lattice-specific
orthogonal-group refinements. The 6-gate review (lines 998-1249) verified source
grounding, completeness, mathematical correctness, and obligation preservation for all
Hom/morphism rows.

What remains in the lattice mapping spec are the non-Hom method clusters that have not
received the same final verification pass:

- `QuadraticForm` algorithm surfaces (theta series, local densities, mass formulas,
  equivalence testing, genus symbols, neighbor enumeration) — these appear in the
  reconciliation tables but as "backend evidence" or "algorithm surface" without the
  theorem-shaped row format the Hom surfaces received.
- Genus, mass, and local-invariant backends from `genera/genus.py`,
  `genera/normal_form.py`, and `genera/spinor_genus.py` — also in reconciliation tables
  as backend evidence but not yet expressed as theorem-shaped rows.
- Short-vector enumeration, LLL reduction, and definite-automorphism computation
  surfaces — classified as algorithm obligations but not yet written as theorem-shaped
  rows.

The statement to settle for any remaining non-Hom cluster:

```text
For objects in the correct category C satisfying hypotheses H,
the Sage method m realizes an operation O,
with codomain or return object Y,
using witness data W.
```

The research need is that later Coble code must express maps such as
`f^*Pic(S) -> H^2(X,Z)`, inclusions `L -> L^#`, embeddings of lattices with forms,
orthogonal projections/complements, discriminant descent, and certified isometries as
typed morphisms rather than raw matrices.

## Source Evidence To Read (remaining clusters)

- `SPEC-MAPPING-LATTICES.md` reconciliation tables for non-Hom surfaces:
  - QuadraticForm algorithm surfaces — `theta_series`, `local_normal_form`,
    `is_globally_equivalent_to`, `siegel_product`, `mass__by_Siegel_densities`,
    `representative`, `representatives`, `genera(...)`, `local_genus_symbol`,
    `global_genus_symbol`, `conway_mass`, `neighbor_iteration`, `short_vectors`,
    `short_vector_list_up_to_length`, `LLL`, `automorphism_group`,
    `basis_of_short_vectors`, `cholesky_decomposition`, `vectors_by_length`,
    `split_local_cover`, `p_adic_normal_form`.
  - Genus and local-invariant backends — `Genus`, `GenusSymbol_p_adic_ring`,
    `GenusSymbol_global_ring`, `LocalGenusSymbol`, `SpinorOperators`,
    `hasse_invariant`, `anisotropic_primes`, `global_genus_symbol`,
    `local_representation_conditions`.
  - Sage installed source for those rows where the reconciliation classification is
    "backend evidence" or "algorithm surface" rather than "theorem-shaped row."
  - The remaining non-Hom rows in the method placement table that do not yet have the
    full theorem-shaped statement format.

## Success Condition For The Next Unit

The remaining non-Hom clusters in `SPEC-MAPPING-LATTICES` are either:

- written as theorem-shaped rows stating the category, hypotheses, return object, and
  source evidence; or
- explicitly classified as "nonmathematical backend residue" with the mathematical
  reason named; or
- routed to a tracked gap where the mathematical claim requires a decision or theorem
  that does not yet exist.

This completes the lattice mapping spec to the same standard as the Hom/morphism pass.

## Non-Goals

- Do not continue Coble primitive-isotropic, Heegner-line, or arithmetic-subgroup orbit
  proofs as the next action.
- Do not treat finite discriminant-form orbit computations as a substitute for
  foundational Hom/morphism vocabulary.
- Do not answer with routes, phases, plans, or status summaries before naming the
  mathematical operation, category, hypotheses, return object, and source evidence.
- Do not use this handoff as a changelog. Git history and the mapping spec carry past
  work.
