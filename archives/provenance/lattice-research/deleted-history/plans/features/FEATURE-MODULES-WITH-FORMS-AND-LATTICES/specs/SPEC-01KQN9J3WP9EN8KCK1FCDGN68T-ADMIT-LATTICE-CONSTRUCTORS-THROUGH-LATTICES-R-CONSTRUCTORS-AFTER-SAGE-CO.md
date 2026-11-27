---
id: SPEC-01KQN9J3WP9EN8KCK1FCDGN68T-ADMIT-LATTICE-CONSTRUCTORS-THROUGH-LATTICES-R-CONSTRUCTORS-AFTER-SAGE-CO
trackerStatus:
  type: spec
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Admit lattice constructors through Lattices(R).Constructors after Sage constructor
  inventory mapping
status: complete
priority: critical
requirement: The deleted Lattices triage recorded the top-level lattice subtree admission,
  current smoke coverage, constructor admission boundary, and DiscriminantGroupAut
  blocker.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- Run just smoke-file lattices/chain_smoketest.sage and just smoke-file lattices/smoketest.sage
  for lattice-surface changes.
- Do not admit lattice constructors without completing Sage constructor inventory
  mapping.
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Admit lattice constructors through Lattices(R).Constructors after Sage constructor inventory mapping
## Summary

The deleted Lattices triage recorded the top-level lattice subtree admission, current
smoke coverage, constructor admission boundary, and DiscriminantGroupAut blocker.

## Source Provenance

- `category_specs/lattices/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/lattices/docs/TRIAGE.md`.
- Original migrated line: `Admit lattice constructors through Lattices(R).Constructors after Sage constructor inventory mapping from category_specs/lattices/docs/TRIAGE.md`

## Context

- Lattice smokes cover Cat registration, the ambient module chain, Hom/End/Aut construction, Subobjects, DualObjects/DualLattices vocabulary, and Even predicate surface.
- Constructor admission remains outside the current smoke surface and must enter through Lattices(R).Constructors() after Sage constructor inventory mapping.
- LatticeOrthogonalGroup is Lattices(R).AutCategory().Of(L), specializing the formed-module aut surface.
- DiscriminantGroupAut export is blocked until discriminant_groups.py defines Hom, End, and Aut standard names.

## Grounded Review Outcome

Grounded admission target for this card:

- Source anchors:
  - `category_specs/lattices/docs/MAPPING.md`;
  - `category_specs/modules/docs/MAPPING.md` constructor namespace;
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`;
  - `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`;
  - `theory/spec_backups/lattices_written_spec_backup.py`;
  - Sage written docs/source for constructor behavior only.
- Mathematical admission rule: each constructor admitted through
  `Lattices(R).Constructors()` must state the presented object it builds, its
  presentation data, base ring, form codomain, and the category meet of the resulting
  object. Sage call paths are evidence about behavior, not the public definition.
- Constructor families already implied by the mapping docs stay presentation-sensitive:
  basis matrices, basis rows, quadratic-form presentations, and order-element routes
  are distinct admitted data shapes rather than one variadic catch-all.
- Concrete dependencies: final constructor admission is blocked until the Sage
  constructor inventory mapping is complete and the lattice subtree's discriminant-group
  Hom/End/Aut export gap is resolved. Those are admission blockers, not reasons to stop
  source mining.
- Work this card can still do while blocked: complete the constructor-by-constructor
  source map, pin each target object and category meet, and identify any constructor
  whose semantics still depend on missing base vocabulary instead of forcing admission.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file lattices/chain_smoketest.sage and just smoke-file lattices/smoketest.sage for lattice-surface changes.
- [ ] Do not admit lattice constructors without completing Sage constructor inventory mapping.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

- 2026-05-04: Marked `status: unstarted` because the card body already records the DiscriminantGroupAut prerequisite; continue other approved phase-01 leaves until that prerequisite is available.
