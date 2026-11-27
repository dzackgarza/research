---
id: TASK-LAT-VINBERG-EDGEWALK-WRAPPER
trackerStatus:
  type: task
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[TASK-LAT-PHASE5-ORTHOGONAL-GROUP]]'
- '[[SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT]]'
title: Wrap polyhedral_common Lorentzian edgewalk for Vinberg algorithm
status: blocked
priority: medium
description: Wrap the polyhedral_common Lorentzian edgewalk backend behind the Vinberg result contract once the backend build and lattice API prerequisites are available.
successCriteria:
- The wrapper accepts typed hyperbolic lattice input and returns a VinbergResult with roots, Coxeter data, control vector, completeness status, and backend provenance.
- The backend route is verified against a sourced worked example or remains explicitly blocked with the missing build/API prerequisite recorded.
complexity: 40
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Wrap polyhedral_common Lorentzian edgewalk for Vinberg algorithm

## Strategy

The polyhedral_common C++ library provides `LORENTZ_RunEdgewalkAlgorithm` which
implements Vinberg's algorithm for hyperbolic (Lorentzian) lattices. This is the
preferred backend because:

1. It is already vendored at `src/external/dutsik_polyhedral/polyhedral_common/`
2. A Python wrapper exists at `src.bak/backends/external/py_polyhedral/` exporting
   `lorentzian_reflective_edgewalk`
3. The indefinite backends isometry/orbit code in `src.bak/` uses the same bridge,
   so infrastructure is shared
4. C++ performance for the root enumeration search

The vinal (Python/Sage) implementation from
`src.bak/backends/external/vinbergs_algorithm/references/vinal/` serves as the
reference/fallback — easier to adapt to the project's category vocabulary but
slower for production.

## Implementation steps

1. Verify the `lorentzian_reflective_edgewalk` export in py_polyhedral accepts
   our spec-level lattice objects (Gram matrix, generators, control vector).

2. Create a wrapper function `L.vinberg_edgewalk(control_vector=None)` on the
   lattice object that:
   - Accepts a hyperbolic lattice object `L` with signature (1, n)
   - Accepts an optional control vector (default: canonical choice via
     `L.positive_cone().canonical_timelike_vector()`)
   - Delegates to the polyhedral_common binary via py_polyhedral
   - Returns a `VinbergResult` object matching the contract in
     SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT

3. The VinbergResult must record:
   - Simple roots as lattice elements
   - Coxeter matrix (Gram matrix of simple roots)
   - Control vector used
   - Completeness status (finite, infinite/cusp detected, or partial)
   - Backend identifier and version

4. Test against the Sterk-Peters worked example (E₈(-1)⊕E₈(-1)⊕U⊕⟨v⟩,
   rank 19, signature (1, 18)) and verify the known simple root set and
   parabolic subdiagrams (Ã₁₇, Ẽ₈+Ẽ₈+Ã₁, Ḍ₁₆+Ã₁, Ḍ₁₀+Ẽ₇).

## Fallback

If `lorentzian_reflective_edgewalk` is insufficient for any target lattice,
adapt vinal's approach (direct quadratic Diophantine solving in the
control-vector orthogonal complement, pure Python/Sage) as a second
implementation path. The fallback must produce the same typed result object.
