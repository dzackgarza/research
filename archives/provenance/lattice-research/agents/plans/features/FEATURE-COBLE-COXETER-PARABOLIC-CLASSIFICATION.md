---
id: FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION]]'
plans: []
title: Coble Coxeter parabolic classification
status: unstarted
priority: high
description: Construct the Coble Coxeter diagram from the lattice and classify maximal
  parabolic subdiagrams without hand-coded adjacency data.
---
# Feature: Coble Coxeter parabolic classification

## Summary

Construct the Coxeter diagram $G_{S_{\mathrm{Co}}}$ from the Coble lattice and classify
its maximal parabolic subdiagrams. The target claim is the uniqueness of the maximal
parabolic subdiagram of type $\widetilde{B}_7(2)$ associated with the 0-cusp.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 4.1: Coxeter Diagram and
  Parabolic Subdiagrams`.
- AEGS (2023), Nikulin (1979, 1980), and Bourbaki, through
  `theory/references/index.md`.

## Scope

- Construct $S_{\mathrm{Co}}$ from the Coble/K3 lattice pipeline.
- Construct the $(-2)$-root system and simple roots through Vinberg's algorithm or an
  equivalent source-backed method.
- Build the Coxeter diagram from computed root inner products.
- Enumerate maximal affine Dynkin subdiagrams.
- Verify the claimed $\widetilde{B}_7(2)$ uniqueness statement from the computed diagram.

## Non-Goals

- Do not hand-code the adjacency matrix.
- Do not classify subdiagrams before constructing the diagram from the lattice.
- Do not treat a rendered diagram or manually selected subgraph as proof of uniqueness.

## Acceptance Criteria

- [ ] The root system and simple roots are constructed from $S_{\mathrm{Co}}$.
- [ ] The Coxeter diagram is produced from computed inner products.
- [ ] The affine Dynkin recognition rule is stated and implemented or delegated to a
  source-backed backend.
- [ ] All maximal parabolic subdiagrams are enumerated exhaustively.
- [ ] The uniqueness of the $\widetilde{B}_7(2)$ subdiagram is verified by computation or
  a cited theorem whose hypotheses are checked.
