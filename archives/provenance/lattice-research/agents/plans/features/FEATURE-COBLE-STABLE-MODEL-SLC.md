---
id: FEATURE-COBLE-STABLE-MODEL-SLC
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION]]'
- '[[FEATURE-COBLE-MODULI-COMPARISON]]'
plans: []
title: Coble stable model slc verification
status: unstarted
priority: high
description: Verify the Coble stable-model and slc conditions using geometric arguments
  and semantic surface/pair vocabulary rather than hardcoded booleans.
---
# Feature: Coble stable model slc verification

## Summary

Verify the stable-model and slc conditions for the Coble KSBA construction. The trivial
surgery-vector calculation belongs in the argument, but the nontrivial feature is the
geometric verification of the pair $(Z,\epsilon C)$ with $Z=X/\iota_{\mathrm{Enr}}$.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 6.1: Surgery Vector and
  slc Stability`.
- AEGS (2023), Nikulin (1979), Kollar (2013), and Pieroni (2026), through
  `theory/references/index.md`.

## Scope

- Compute the surgery vector from the Coble polarization and root data through semantic
  intersection operations.
- Represent the downstairs Coble polarization as `h_Co in K_S^perp subset Pic(S)` with
  square `2`, and use `tilde h_Co = f^*h_Co` with square `4` for K3-side
  intersection computations.
- Construct the dual complex model associated with the computed surgery vector.
- Construct the quotient $Z=X/\iota_{\mathrm{Enr}}$ and the relevant boundary curve data
  in a geometry vocabulary rich enough to state pair properties.
- Verify the KSBA conditions for $(Z,\epsilon C)$: $S_2$, nodal singularities,
  $\mathbb{Q}$-Cartier ampleness, avoidance, and quotient structure.

## Non-Goals

- Do not replace slc verification with hardcoded booleans, print statements, or prose
  theater.
- Do not count the orthogonality calculation $l=0$ as the whole stable-model proof.
- Do not implement local ad hoc singularity or surface-pair checks before source/backend
  routing is settled.

## Acceptance Criteria

- [ ] The surgery vector is computed from constructed lattice and root data.
- [ ] The dual complex model is derived from the computed vector.
- [ ] $Z$, $C$, and $(Z,\epsilon C)$ are represented through semantic geometry objects.
- [ ] Each KSBA condition is verified by a sourced theorem, exact backend computation, or
  explicit geometric argument with hypotheses checked.
- [ ] The proof artifact contains failing assertions or formal checks for every claimed
  condition; it contains no hardcoded success flags.
