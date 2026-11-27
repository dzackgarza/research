---
id: FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
plans: []
title: Historical orthogonal group and orbit recovery
status: complete
priority: high
description: Recover orthogonal group, subgroup, action, stabilizer, centralizer, isotropic orbit, and discriminant-kernel behavior from historical src.bak with category-correct Aut and subgroup semantics.
---
# Historical orthogonal group and orbit recovery

## Summary

Recover the useful orthogonal-group and orbit behavior from
`src.bak/lattices/groups/orthogonal.py`, `src.bak/backends/dawes_orbit_backend.py`,
and `src.bak/backends/isotropic_gamma_orbit_backend.py`. The recovered surface must be
an Aut/subgroup/action API over lattice and discriminant nouns, not a public
`ConditionSet` wrapper around raw matrices.

## Source Provenance

- `src.bak/lattices/groups/orthogonal.py`
- `src.bak/backends/dawes_orbit_backend.py`
- `src.bak/backends/isotropic_gamma_orbit_backend.py`
- `src.bak/backends/external/py_polyhedral/binaries.py`
- `.agents/memories/bilinear-form-category-semantics.md`
- `.agents/memories/theory-backend-routing.md`
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`

## Recovery Boundary

The historical code records required behavior: `O(L)`, subgroups, `SO`, positive
spinor subgroups, stable orthogonal groups, discriminant preimages, vector stabilizers,
isotropic-line/plane/flag stabilizers, centralizers, vector equivalence, isotropic
orbit representatives, and finite quotient filtering.

These are real targets for later recovery once the lattice, discriminant, Hom, End,
Aut, and backend bridge vocabulary is available.

## Non-Preservation Boundaries

- Do not preserve raw `ConditionSet` union/intersection as the public subgroup model.
- Do not use ambient Sage spans as the public definition of isotropic lines, planes, or
  flags.
- Do not put group-action and stabilizer verbs on the lattice if the mathematical
  owner is `L.orthogonal_group()` or a subgroup of it.
- Do not leak row-action backend matrix conventions into public column-action group
  semantics.

## Child Specs

- `[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]`
- `[[SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE]]`

## Acceptance Criteria

- [ ] Orthogonal groups are recovered as Aut objects with explicit action convention.
- [ ] Subgroup construction and algebra have structured mathematical owners.
- [ ] Orbit and stabilizer methods return typed objects and witness data where needed.
