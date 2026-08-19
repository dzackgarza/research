---
id: FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY]]'
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
plans: []
title: Historical Vinberg and Coxeter recovery
status: complete
priority: medium
description: Recover Vinberg algorithm, Coxeter diagram, reflection group, and fundamental chamber requirements from historical external references and old backend notes after lattice/group vocabulary is stable.
---
# Historical Vinberg and Coxeter recovery

## Summary

Recover the Vinberg and Coxeter obligations visible under
`src.bak/backends/external/vinbergs_algorithm/` as future semantic features. This
feature does not authorize an ad hoc local Vinberg implementation. It records the
required mathematical objects, backend candidates, and output contracts that should
exist once the lattice and orthogonal-group layers can express them.

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/README.md`
- `src.bak/backends/external/vinbergs_algorithm/references/AlVin/README.md`
- `src.bak/backends/external/vinbergs_algorithm/references/sterk-peters_symmetric-quadratic-forms.md`
- `.agents/memories/theory/backends/vinberg-algorithm.md`
- `.agents/memories/theory-backend-routing.md`
- `.agents/memories/theory/backends/library-integration.md`
- `theory/foundations/reflective-two-elementary-lattices.md`
- `.agents/skills/vinberg-algorithm/SKILL.md`

## Recovery Boundary

Historical references identify recoverable targets: hyperbolic lattice inputs,
control vectors, root enumeration, reflection generators, Coxeter diagrams, finite
volume termination checks, fundamental chamber data, and comparison against known
examples. The recovered API must express these through lattice, root, reflection group,
orthogonal group, and polyhedral/chamber nouns.

## Non-Preservation Boundaries

- Do not copy messy reference implementations into first-party code.
- Do not use approximate or floating-point hyperbolic geometry as evidence for exact
  lattice claims.
- Do not expose root lists without the lattice, control vector, ordering, constraints,
  and termination status that make them meaningful.
- Do not treat Coxeter diagram matching as a substitute for verifying the chamber and
  reflection group construction.

## Child Specs

- `[[SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT]]`
- `[[SPEC-HISTORICAL-COXETER-FUNDAMENTAL-DOMAIN-OUTPUT]]`

## Acceptance Criteria

- [ ] Vinberg algorithm inputs and outputs are specified as typed mathematical nouns.
- [ ] Backend candidates and reference examples are recorded without making local
  bespoke implementation the default.
- [ ] Coxeter and chamber outputs have exact verification obligations.
