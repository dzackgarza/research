---
id: FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
plans: []
title: Historical lattice presentation method recovery
status: complete
priority: high
description: Recover the useful presented-lattice constructors, invariants, and comparison methods visible in historical src.bak after the ModulesWithForms and lattice vocabulary is stable.
---
# Historical lattice presentation method recovery

## Summary

Recover the useful presented-lattice surface visible in `src.bak/lattices/core/` and
`src.bak/lattices/categories/` after the base lattice vocabulary exists. This feature
is not a request to copy the old implementation. It records the methods and invariants
that should ultimately exist on the correct mathematical nouns.

## Source Provenance

- `src.bak/lattices/core/rational.py`
- `src.bak/lattices/core/integral.py`
- `src.bak/lattices/core/elements.py`
- `src.bak/lattices/validation/presentations.py`
- `src.bak/lattices/categories/modules_with_forms.py`
- `src.bak/lattices/categories/lattices.py`
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`

## Recovery Boundary

The historical code contains real targets: presented lattice construction, element
conversion from coordinates, dual and rational promotion, standard named lattices,
twists, direct sums, genus/local/rational/isometry predicates, Nikulin-style invariants,
and primitive-coordinate checks. These belong on the category-correct lattice and
formed-module nouns once those nouns exist.

The old design is not authority. It mixed Sage ambient-lattice assumptions,
implementation matrices, compatibility aliases, and method placement that must be
rechecked against the current specs.

## Non-Preservation Boundaries

- Do not expose Sage's ambient-vector-space model as public lattice semantics.
- Do not add compatibility shims for old method names unless an approved spec requires
  the exact alias.
- Do not place generic formed-module methods at the lattice-only layer.
- Do not use Coble-named lattice shortcuts as evidence in the feature that derives the
  Coble lattice from geometry. This does not ban a standard lattice library; it bans
  replacing the derivation with a pre-named expected answer.

## Child Specs

- `[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]`
- `[[SPEC-HISTORICAL-LATTICE-CONSTRUCTORS-INVARIANTS-AND-COMPARISONS]]`

## Acceptance Criteria

- [ ] The recoverable lattice presentation surface is specified without copying old
  ambient-module semantics.
- [ ] Standard constructors and comparison methods have explicit owner nouns and source
  grounding.
- [ ] The specs distinguish presentation equality, isometry, and backend
  canonicalization with witness obligations.
