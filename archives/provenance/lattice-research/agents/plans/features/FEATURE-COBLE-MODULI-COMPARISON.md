---
id: FEATURE-COBLE-MODULI-COMPARISON
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION]]'
plans: []
title: Coble moduli comparison
status: unstarted
priority: high
description: Establish the Coble-to-K3 moduli comparison as a computational proof in
  the repo's mathematical vocabulary, after the prerequisite category, lattice, and
  geometry interfaces can express the objects and morphisms involved.
---
# Feature: Coble moduli comparison

## Summary

Establish the comparison between a naively defined Coble moduli problem and the relevant
lattice-polarized K3 period quotient as a computational proof. The proof must be written
in the repo's mathematical vocabulary: curves, blowups, divisors, Picard groups, covers,
pullbacks, primitive closures, orthogonal complements, period domains, moduli spaces, and
comparison maps.

This feature is blocked until the prerequisite category, lattice, and geometry
interfaces can express those objects and morphisms without raw-matrix or ad hoc
polynomial fallbacks.

## Scope

- Define the naive Coble moduli problem from the specific geometric construction under
  study.
- Compute the Coble-side dimension by algebraic-geometry methods: parameter space,
  singularity conditions, quotient by automorphisms, and stack/coarse-space issues.
- Construct the Coble curve, its blowup, the Picard group of the blowup, the K3 double
  cover, and the pullback of the Picard group.
- Distinguish the plane hyperplane class `H` from the degree-2 Coble polarization
  `h_Co`: `H^2 = 1`, `f^*H` has square `2`, while
  `h_Co in K_S^perp subset Pic(S)` has square `2` and
  `tilde h_Co = f^*h_Co` has square `4`.
- Use the explicit blowup formula `K_S = -3H + sum_i E_i`; therefore
  `D = aH - sum_i b_iE_i` is in `K_S^perp` exactly when `sum_i b_i = 3a`.
- Compute the pullback lattice from the constructed geometry, give a canonical
  presentation, and verify any claimed isometry to standard summands.
- State the open locus where the double-cover construction gives a smooth K3 surface.
- Compute the primitive closure of the pullback lattice in the K3 Picard lattice when
  needed, then derive the orthogonal complement used for the period domain.
- State the exact lattice-polarized K3 moduli theorem being used, including its
  hypotheses.
- Construct the rational map or morphism from the Coble moduli problem to the relevant
  arithmetic quotient of the K3 period domain.
- Prove the comparison map is dominant and generically finite, ideally birational.

## Non-Goals

- Do not count the Type IV period-domain dimension calculation as material progress on
  this feature. Once the period lattice is constructed and its rank is known, the
  dimension is immediate.
- Do not cite an authority chain as a substitute for constructing the Coble moduli
  problem, lattice, period map, or comparison morphism.
- Do not make raw matrices, hand-assembled Gram forms, or isolated equations the public
  proof language. They may appear only as internal realizations of mathematical objects.

## Acceptance Criteria

- [ ] The naive Coble moduli problem is defined from the construction under study.
- [ ] The Coble-side dimension is computed from algebraic geometry, not inferred from
  the period-domain dimension.
- [ ] The computational proof constructs the Coble curve, blowup, Picard group, double
  cover, canonical class, structure-sheaf pushforward, Hodge-number calculation, and
  pullback lattice through semantic mathematical operations.
- [ ] The proof identifies `K_S^perp ~= E_10`, the degree-2 polarization
  `h_Co in K_S^perp`, and the K3 pullback `tilde h_Co` with the correct doubled square.
- [ ] The derived lattice data includes the canonical presentation, primitive closure
  when required, discriminant data, orthogonal complement, and verified isometries to
  standard presentations.
- [ ] The K3 period-domain input is stated through the exact lattice-polarized K3 theorem
  and its hypotheses.
- [ ] The comparison between the Coble moduli problem and the period quotient is given by
  an actual rational map or morphism with dominance and generic-finiteness evidence.
