---
id: FEATURE-COBLE-ARITHMETIC-GROUP-GENERATORS
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-COBLE-MODULI-COMPARISON]]'
- '[[FEATURE-COBLE-K3-FOLDING-INVOLUTION]]'
plans: []
title: Coble arithmetic group generators
status: complete
priority: high
description: Construct Gamma_Co as a stabilizer-centralizer arithmetic subgroup and
  compute explicit generators with exact lattice-group verification.
---
# Feature: Coble arithmetic group generators

## Summary

Construct the Coble arithmetic group
$\Gamma_{\mathrm{Co}}=\mathrm{Stab}_{O(T_{\mathrm{En}})}(h_{\mathrm{Co}})
\cap Z_{O(T_{\mathrm{En}})}(\theta)$ as a real subgroup of the relevant lattice
isometry group, then compute explicit generators.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 3.1: Arithmetic Group
  Gamma_Co`.
- Sterk (1991) and Dolgachev-Kondo (2013), through `theory/references/index.md`.

## Scope

- Represent $T_{\mathrm{En}}$, $h_{\mathrm{Co}}$, and $\theta$ through the repo's lattice
  and morphism vocabulary.
- Construct the stabilizer of $h_{\mathrm{Co}}$ in $O(T_{\mathrm{En}})$.
- Construct the centralizer of $\theta$ in $O(T_{\mathrm{En}})$.
- Compute the intersection defining $\Gamma_{\mathrm{Co}}$.
- Produce a generator set and verify that the generated group has the intended
  stabilizer-centralizer property.

## Non-Goals

- Do not infer generators from notation or from a period-domain quotient statement.
- Do not accept sampled or bounded group elements as a generator computation.
- Do not use raw matrices as the public proof language; matrices are internal
  realizations of lattice isometries and subgroup operations.

## Acceptance Criteria

- [ ] $T_{\mathrm{En}}$, $h_{\mathrm{Co}}$, and $\theta$ are constructed from sourced
  lattice data.
- [ ] The stabilizer and centralizer are computed by exact group methods or a
  source-backed backend.
- [ ] The intersection subgroup is computed as $\Gamma_{\mathrm{Co}}$ with explicit
  membership checks.
- [ ] The claimed generators are verified to generate the same subgroup, not merely to
  satisfy necessary conditions.
- [ ] The result states the theorem or backend guarantee that makes the group computation
  exhaustive.
