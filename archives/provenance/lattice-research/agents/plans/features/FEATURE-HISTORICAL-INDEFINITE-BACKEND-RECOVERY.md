---
id: FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
plans: []
title: Historical indefinite backend bridge recovery
status: complete
priority: high
description: Recover exact backend bridge contracts for indefinite isometry, automorphism, vector orbit, isotropic subspace, centralizer, and finite quotient computations exposed by historical src.bak.
---
# Historical indefinite backend bridge recovery

## Summary

Recover the backend bridge obligations visible in historical `src.bak/backends/` and
`src.bak/backends/external/` without turning those wrappers into the public
mathematical API. Backend bridges normalize raw conventions, call mature exact
software, and return data that the public lattice/category layer verifies.

## Source Provenance

- `src.bak/backends/isometry_backend.py`
- `src.bak/backends/dawes_orbit_backend.py`
- `src.bak/backends/isotropic_gamma_orbit_backend.py`
- `src.bak/backends/oscar_centralizer/`
- `src.bak/backends/external/README.md`
- `src.bak/backends/external/py_polyhedral/binaries.py`
- `.agents/memories/theory-backend-routing.md`
- `.agents/memories/theory/backends/indefinite-isometry.md`
- `.agents/memories/theory/backends/indefinite-jl.md`
- `.agents/memories/theory/backends/software-capability-map.md`
- `.agents/memories/theory/backends/carat.md`

## Recovery Boundary

The historical backend layer points to exact computations that should be available
behind public lattice/group methods: indefinite form isometry witnesses, automorphism
generators, vector orbit representatives, isotropic k-plane and k-flag orbits,
stabilizers, centralizer data, invariant/coinvariant sublattices, discriminant action
images, and finite quotient filtering.

The recovered bridge is not the user-facing proof language. The public proof language
remains lattice objects, morphisms, discriminant forms, groups, subgroups, and actions.

## Non-Preservation Boundaries

- Do not expose backend matrix rows, process files, temporary paths, or AST literals as
  public data.
- Do not hide missing binaries or environment failures behind alternate computations.
- Do not treat CARAT as an indefinite lattice backend; keep its positive-definite and
  finite-matrix-group limits explicit.
- Do not use local bespoke algorithms when a mature exact backend exists.

## Child Specs

- `[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]`
- `[[SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS]]`

## Acceptance Criteria

- [ ] Backend wrappers have explicit mathematical input/output contracts.
- [ ] Matrix action conventions are normalized at the backend boundary.
- [ ] Returned backend data is verified by the public noun layer before acceptance.
