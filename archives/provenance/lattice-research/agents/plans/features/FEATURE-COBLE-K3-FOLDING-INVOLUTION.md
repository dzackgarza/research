---
id: FEATURE-COBLE-K3-FOLDING-INVOLUTION
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION]]'
plans: []
title: Coble K3 folding involution
status: unstarted
priority: high
description: Construct the horizontal folding involution on the K3 lattice and verify
  its eigenspace lattices from primitive embedding and gluing data.
---
# Feature: Coble K3 folding involution

## Summary

Construct the horizontal folding involution $\theta$ on $\Lambda_{\mathrm{K3}}$ and
verify its eigenspace lattices. The feature replaces the old unverified glued-lattice
script obligation with a source-backed lattice construction.

The source-level construction is now fixed at the mathematical level.  For the
primitive embedding

```text
S_Co = f^*Pic(S) <= Lambda_K3,
T_Co = S_Co^perp,
```

Nikulin primitive-unimodular gluing gives an anti-isometry

```text
gamma_Co : A_{S_Co} -> A_{T_Co},      q_T gamma_Co = -q_S.
```

Since both Coble discriminant groups are 2-elementary, the sign map `-id` on `S_Co`
and `id` on `T_Co` preserve the gluing graph.  Therefore the involution is the lattice
automorphism

```text
theta_Co|S_Co = -id,
theta_Co|T_Co = id.
```

The matrix is a realization of this automorphism after choosing a primitive embedding
and basis; it is not the definition of the involution.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 5.1: Involution theta on
  Lambda_K3`.
- Nikulin (1979), Dolgachev-Kondo (2013), Sterk (1991), and Pieroni (2026), through
  `theory/references/index.md`.

## Scope

- Construct the primitive sublattice and orthogonal complement inside
  $\Lambda_{\mathrm{K3}}$.
- Construct the gluing anti-isometry
  $\gamma_{\mathrm{Co}}:A_{S_{\mathrm{Co}}}\to A_{T_{\mathrm{Co}}}$ and verify that the
  sign action preserves its graph.
- Construct the sign involution acting by `-id` on $S_{\mathrm{Co}}$ and `id` on
  $T_{\mathrm{Co}}$.
- Express $\theta$ as a K3-lattice isometry.
- Verify $\theta^2=I$ and $\theta^T G\theta=G$ in the chosen presentation.
- Compute and verify the $+1$ and $-1$ eigenspace lattices, signatures, primitive
  embeddings, and isometry types.

## Relationship to Geometry

The involution θ is naturally described as the sign involution on Λ_K3 given by a
primitive sublattice decomposition: θ acts as +1 on one summand and -1 on its
orthogonal complement, with gluing data fixing the extension. The abstract lattice
theory for θ can be carried out without the geometric Coble surface construction:

- The primitive embedding of the pullback lattice f*Pic(S) into Λ_K3 is a
  classification problem in lattice theory (Nikulin's primitive embedding theory),
  solvable from the abstract isometry types.
- θ is then the involution that restricts to `-id` on `f*Pic(S)=S_Co` and `id` on
  `T_Co=S_Co^perp`.  The existence of this involution follows from the
  primitive-unimodular gluing data because the discriminant groups are 2-elementary.
- The geometric construction (Coble surface → K3 cover → pullback lattice) is a
  logical prerequisite for establishing the Coble narrative from first principles
  and proving that the resulting moduli spaces are the correct ones. It does not
  block the abstract lattice computation of θ's eigenspace signatures, matrix
  realization, and invariant sublattice isometry types — those depend only on
  having the correct spec vocabulary, the abstract primitive embedding, and gluing
  data, not on the geometry being fully constructed first.
- The lattice-level results are then available to verify against the geometric
  construction when the latter is completed.

## Non-Goals

- Do not accept a hand-assembled 22-by-22 matrix without deriving the sublattices and
  gluing data.
- Do not infer eigenspaces from desired signatures alone.
- Do not use a matrix equality as the whole proof if the lattice construction is absent.
- Do not describe θ in terms of raw matrix entries; use the repo's lattice Hom
  vocabulary: construct the involution as a morphism in the Aut category, then
  extract a matrix representation only for verification against backend computations.

## Acceptance Criteria

- [ ] The input primitive embedding and complement are source-grounded.
- [ ] The gluing anti-isometry
  $\gamma_{\mathrm{Co}}:A_{S_{\mathrm{Co}}}\to A_{T_{\mathrm{Co}}}$ is constructed.
- [ ] The sign action on $S_{\mathrm{Co}}\oplus T_{\mathrm{Co}}$ is verified to preserve
  the gluing graph.
- [ ] The involution is constructed as a lattice isometry, not postulated as a matrix.
- [ ] The matrix realization satisfies the involution and isometry equations.
- [ ] The eigenspace lattices are computed from $\theta$.
- [ ] The claimed identifications with $T_{\mathrm{Co}}$ and $S_{\mathrm{Co}}$ are
  verified by explicit isometries under stated hypotheses.
