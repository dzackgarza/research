---
id: SPEC-01KQN9J3WQDJ0Z27BXTY67HA72-DEFINE-DISCRIMINANTGROUP-HOM-END-AUT-STANDARD-NAMES-SO-DISCRIMINANTGROUP
trackerStatus:
  type: spec
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut
  can be exported
status: complete
priority: critical
requirement: The deleted Lattices triage recorded the top-level lattice subtree admission,
  current category-obligation example coverage, constructor admission boundary, and DiscriminantGroupAut
  blocker.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance. No new implementation blocker was discovered; the recorded
  blocker was stale.
- Run just category-obligation-file lattices/chain_category_obligations.sage and just category-obligation-file lattices/category_obligations.sage
  for lattice-surface changes.
- Do not admit lattice constructors without completing Sage constructor inventory
  mapping.
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut can be exported
## Summary

The deleted Lattices triage recorded the top-level lattice subtree admission, current
category-obligation example coverage, constructor admission boundary, and DiscriminantGroupAut blocker.

## Source Provenance

- `category_specs/lattices/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/lattices/docs/TRIAGE.md`.
- Original migrated line: `Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut can be exported from category_specs/lattices/docs/TRIAGE.md`

## Context

- Lattice category-obligation examples cover Cat registration, the ambient module chain, Hom/End/Aut construction, Subobjects, DualObjects/DualLattices vocabulary, and Even predicate surface.
- Constructor admission remains outside the current category-obligation example and must enter through Lattices(R).Constructors() after Sage constructor inventory mapping.
- LatticeOrthogonalGroup is Lattices(R).AutCategory().Of(L), specializing the formed-module aut surface.
- DiscriminantGroupAut export is blocked until discriminant_groups.py defines Hom, End, and Aut standard names.

## Grounded Review Outcome

Grounded target for this card:

- Source anchors:
  - `category_specs/lattices/docs/MAPPING.md`;
  - `category_specs/homsets/docs/MAPPING.md`;
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`;
  - `theory/foundations/bilinear-forms-duals-morphisms.md`;
  - `theory/references/index.md` for literature-backed discriminant-form claims.
- Mathematical object: for a lattice `L`, the discriminant object is the quotient
  `A_L = L^*/L`, with the descended quotient-valued bilinear or quadratic form when the
  ambient formed-module data provides one.
- Hom/End/Aut contract: `DiscriminantGroupHom`, `DiscriminantGroupEnd`, and
  `DiscriminantGroupAut` name the morphism, endomorphism, and automorphism parents for
  form-preserving morphisms of `A_L`; they classify categorical morphisms, not raw
  generators, matrices, or Sage torsion backends.
- Concrete dependency: this leaf is blocked on the discriminant-group owner file
  defining the standard Hom/End/Aut type package and export surface consistent with the
  generic hom/end/aut hierarchy. Until that owner exists, do not export
  `DiscriminantGroupAut` from the lattice subtree.
- Work this card can still do while blocked: pin the exact names, object definition,
  preservation law, and migration consequence against the mapping docs so the eventual
  owner implementation is a direct wiring task rather than another definition-mining
  pass.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance. No new implementation blocker was discovered; the recorded blocker was stale.
- [ ] Run just category-obligation-file lattices/chain_category_obligations.sage and just category-obligation-file lattices/category_obligations.sage for lattice-surface changes.
- [ ] Do not admit lattice constructors without completing Sage constructor inventory mapping.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

- 2026-05-04: Marked `status: unstarted` because the card body already records the DiscriminantGroupAut prerequisite; continue other approved phase-01 leaves until that prerequisite is available.
- 2026-05-05: Rechecked `category_specs/lattices/subcategories/constructions/discriminant_groups.py`
  and `category_specs/types.py`; the standard Hom/End/Aut names already exist and are
  exported. Added the missing mapping note to `category_specs/lattices/docs/MAPPING.md`
  and moved this card to `in-review` because the prior blocker is stale. This was a
  mapping/card update only; lattice category-obligation commands were not run because no code surface
  changed.

## 6-Gate Protocol Review Log

Review date: 2026-05-07
Reviewer: Hermes Agent (subagent)
Card path: plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/specs/SPEC-01KQN9J3WQDJ0Z27BXTY67HA72-DEFINE-DISCRIMINANTGROUP-HOM-END-AUT-STANDARD-NAMES-SO-DISCRIMINANTGROUP.md

### G1 Source Grounding

Verify referenced files/cards exist and paths are correct.

| Source Anchor | Path | Status | Evidence |
|---|---|---|---|
| Lattice mapping doc | `category_specs/lattices/docs/MAPPING.md` | EXISTS (redirect) | File present; body migrated to `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md` in commit 13bf697. The discriminant-group type package note (added in commit 6b07341) is preserved at lines 558-565 of the tracked spec. |
| Homsets mapping doc | `category_specs/homsets/docs/MAPPING.md` | EXISTS (redirect) | File present; canonical spec at `SPEC-MAPPING-HOMSETS.md`. |
| Category ABC spec | `.agents/skills/lattice-redesign/references/category-abc-spec.md` | EXISTS | 938-line authoritative spec for ModulesWithForms category contracts. |
| Bilinear forms theory | `theory/foundations/bilinear-forms-duals-morphisms.md` | MISSING | Created in commit f3c2a1b (2026-05-03), deleted in checkpoint commit 221fc78 (2026-05-06). File no longer exists at HEAD. |
| Theory references | `theory/references/index.md` | EXISTS | 133-line canonical reference map. Nikulin (1979) cited for discriminant-form arguments. |
| Discriminant groups owner | `category_specs/lattices/subcategories/constructions/discriminant_groups.py` | EXISTS | 87 lines. Defines Hom/End/Aut type aliases at lines 80-87. |
| Types re-export layer | `category_specs/types.py` | EXISTS | 843 lines. Re-exports all DiscriminantGroup* names at lines 566-577 and defines DiscriminantGroupTypes class at lines 831-843. |
| TRIAGE.md (removed) | `category_specs/lattices/docs/TRIAGE.md` | WRONG PATH | Actual path was `plans/category_specs/lattices/docs/TRIAGE.md`, deleted in commit 8d1c21c. Recovery command `git show 8d1c21c^:category_specs/lattices/docs/TRIAGE.md` fails. Correct command: `git show 8d1c21c^:plans/category_specs/lattices/docs/TRIAGE.md`. TRIAGE content confirmed: "DiscriminantGroupAut type package is still blocked because discriminant_groups.py does not yet define Hom, End, Aut standard names." |
| Parent feature | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` | EXISTS | At `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`, status: in-progress. |
| Dependency phase | `PHASE-HOM-END-AUT-WORK-QUEUE` | EXISTS | At `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/.../PHASE-HOM-END-AUT-WORK-QUEUE.md`, status: needs-agent-review. Note: this phase lives under a different feature root (FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES) than this spec (FEATURE-MODULES-WITH-FORMS-AND-LATTICES). Cross-feature dependency is valid but unusual. |
| Category-obligation example: chain | `category_specs/lattices/chain_category_obligations.sage` | EXISTS | 31 lines; covers Cat registration, lattice chain, Even predicate. |
| Category-obligation example: full | `category_specs/lattices/category_obligations.sage` | EXISTS | Lattice category-obligation examples. |

G1 Findings:
- 10 of 12 source anchors verified existing at correct paths.
- 1 anchor MISSING: `theory/foundations/bilinear-forms-duals-morphisms.md` was deleted after spec creation. The content (dual basis, adjoint map, discriminant descent) is partially recoverable from git. Recommendation: either restore the file or update the spec to reference a surviving source (e.g., `theory/references/index.md` Nikulin entry).
- 1 anchor has WRONG PATH: TRIAGE.md recovery command uses `category_specs/lattices/docs/TRIAGE.md` instead of `plans/category_specs/lattices/docs/TRIAGE.md`. The spec's Source Provenance section should be corrected.

### G2 Sage Surface Completeness

All inventoried surfaces accounted.

Evidence:
- `discriminant_groups.py` lines 77-87: Defines `LatticeDiscriminantGroupsHom`, `End`, `Aut`, `Endomorphism`, `Automorphism` as aliases of `ModulesHom`, `ModulesEnd`, `ModulesAut`, `ModulesEndomorphism`, `ModulesAutomorphism`. Also defines `HomCategory`, `EndCategory`, `AutCategory` aliases.
- `types.py` lines 566-577: Re-exports short names `DiscriminantGroup`, `DiscriminantGroupElement`, `DiscriminantGroupMorphism`, `DiscriminantGroupHom`, `DiscriminantGroupEnd`, `DiscriminantGroupAut`, plus corresponding Category, Endomorphism, and Automorphism names.
- `types.py` lines 831-843: Provides `DiscriminantGroupTypes` named-tuple-style namespace.
- SPEC-MAPPING-LATTICES.md lines 558-565: Records the full type package owner and re-export surface.

No missing surfaces. The Hom/End/Aut contract is complete: morphism parents use the generic Modules Hom/End/Aut machinery, with containment interpreted in the finite torsion formed-module category.

### G3 Constructor Route Justification

Mathematical route verified as valid.

Object definition: For a lattice L over a PID R, the discriminant group is A_L = L^*/L (the cokernel of the natural map L -> L^* induced by the bilinear form). This is a finite torsion R-module. When the ambient form data provides bilinear/quadratic structure, the form descends to a quotient-valued form on A_L.

Hom/End/Aut construction: `Lattices(R).DiscriminantGroups()` is a subcategory of `Modules(R).Torsion()` with Bilinear and Quadratic form structure. The Hom/End/Aut categories inherit from `ModulesHomCategory`/`ModulesEndCategory`/`ModulesAutCategory` respectively (discriminant_groups.py lines 80-85). This follows the standard categorical pattern: morphisms are form-preserving module homomorphisms between discriminant groups.

Chain: `Lattices(R) -> DiscriminantGroups() -> Hom/End/Aut` is a standard Sage category construction path. The Aut surface specializes `Modules(R).AutCategory()` applied to discriminant group objects, which are finite torsion formed modules. This is mathematically rigorous: automorphisms of the discriminant form are precisely automorphisms of A_L preserving the descended bilinear/quadratic form.

### G4 Nonmathematical Rejection

Explicit rejections verified.

The spec body (line 62-65) explicitly rejects:
- Raw generators: "they classify categorical morphisms, not raw generators"
- Matrices: "not raw ... matrices"
- Sage torsion backends: "not ... Sage torsion backends"

The mapping spec (lines 563-565) reinforces: "containment is interpreted in the finite torsion formed-module category, not as raw matrices or Sage torsion backends."

These rejections are properly grounded in the categorical hierarchy: morphism parents are defined via the Module Hom/End/Aut machinery, not by exposing Sage's internal FGP_Module representation. The orthogonal_group() method on discriminant groups is admitted as constructor input to the Aut parent, not as an element before containment.

### G5 Ambiguity Routing

No unresolved ambiguities.

The card's sole blocker was the missing DiscriminantGroup Hom/End/Aut standard names. Work log entry 2026-05-05 confirms: names already exist and are exported in both discriminant_groups.py and types.py. The blocker was stale. The mapping note was added to record the owner, surface, and migration consequence (now in SPEC-MAPPING-LATTICES.md lines 558-565).

No new ambiguities or blocked sub-questions were discovered during review. No decision cards need to be routed.

### G6 Obligation Preservation

No weakening detected.

Original TRIAGE obligation: "Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut can be exported." The current state satisfies this fully:
- Hom, End, Aut standard names are defined (discriminant_groups.py lines 80-87)
- All names are re-exported through types.py (lines 566-577)
- DiscriminantGroupAut is exportable

No obligations were weakened, deleted, or moved without replacement. The mathematical contract (categorical morphisms of discriminant forms, not raw matrices) is preserved and strengthened by explicit rejection of nonmathematical targets.

### Summary Verdict

PASS with 2 non-blocking findings:
1. **FINDING-01 (Source rot):** `theory/foundations/bilinear-forms-duals-morphisms.md` no longer exists at HEAD. The spec should either restore this file or replace the reference with an existing source (e.g., `theory/references/index.md` Nikulin entry or `SPEC-MAPPING-LATTICES.md` section on discriminant descent).
2. **FINDING-02 (Wrong path):** The TRIAGE.md recovery command in Source Provenance uses path `category_specs/lattices/docs/TRIAGE.md` but the actual pre-deletion path was `plans/category_specs/lattices/docs/TRIAGE.md`. The spec should correct the recovery command.

The core mathematical work of this spec is complete and verified. DiscriminantGroup Hom/End/Aut standard names are defined, exported, and grounded in the categorical hierarchy. The prior blocker is confirmed stale.
