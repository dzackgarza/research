---
trackerStatus:
  type: plan
title: Category-spec program organization and work graph
status: approved
planId: PLN-CAT-000
planType: program
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
- category-specs
- plan
- theme-plan-control
- theme-category-core
parentPlan: PLN-PHASE-01
---

# Category-spec program organization and work graph

## Objective

Make the `plans/` corpus navigable as one Nimbalyst-backed work graph: source specifications feed high-level plans, high-level plans split into subplans, and subplans own leaf task, research, bug, feature, and decision cards.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Corpus-level analysis

The old `plans/` tree was not one backlog. It contained six different things:

- Canonical source specifications: `CATEGORY_ABC_SPEC.md`, `LATTICE_STYLE_GUIDE.md`, and `lattice_redesign_corrections_spec.md`.
- Operative phase plans: `PHASE_0_SAGE_PATCHES.md`, `PHASE_2_CORE_OBJECTS.md`, `PHASE_3_MORPHISMS.md`, `PHASE_4_DISCRIMINANT_DESCENT.md`, and `PHASE_5_ORTHOGONAL_GROUPS.md`.
- Superseded provenance: `PHASE_1_BILINEAR_MODULES.md`, now deleted because the active split is Phases 2-5 and the crosswalk is captured here and in the phase plans.
- Sage/source maps: `CATEGORY_REFINEMENT_PHASES.md`, `RING_INTEGRATION.md`, `SET_SPEC.md`, `autset_categories_path.md`, `autset_integration_plan.md`, `axioms_with_generators_finitely_presented.md`, `category_creation_notes.md`, and `homsets_structural_core.md`.
- Executable spec files and tool support: `test_spec.sage`, `test_spec2.sage`, `test_spec3.sage`, and `vulture_whitelist.py`.
- Loose process holders and generated debris: `todo.md`, `category_specs/TODO.md`, `category_specs/NEEDS_DECISIONS.md`, `.ruff_cache/`, and `__pycache__/`. These have been removed or folded into tracked cards.

## Plan tree

- `PLN-CAT-010`: source maps, constructor routing, and admission research.
- `PLN-CAT-100`: category foundation kernel and method ownership.
- `PLN-AUDIT-000`: smoke, audit, and uniformity stabilization.

Leaf task ownership is encoded by each card's `planId`. Parent plans own only
subplans, not executable cards.

## Operating rule

The old `plans/` directory has been retired. Active work is represented by `.agents` plans and cards; reusable doctrine lives in skills; executable specs live under `tests/`; category-spec source lives under `category_specs/`.

## Source mapping

| Old material | New owner | Disposition |
| --- | --- | --- |
| `CATEGORY_ABC_SPEC.md` | `lattice-redesign` skill and `PLN-LAT-000` | Migrated, old copy removed |
| `LATTICE_STYLE_GUIDE.md` | `lattice-redesign` skill and `PLN-AUDIT-000` | Migrated, old copy removed |
| `lattice_redesign_corrections_spec.md` | `lattice-redesign` skill | Migrated, old copy removed |
| `PHASE_0_SAGE_PATCHES.md` | `PLN-LAT-010` | Decomposed into leaf cards |
| `PHASE_1_BILINEAR_MODULES.md` | `PLN-LAT-000` | Superseded crosswalk, deleted |
| `PHASE_2_CORE_OBJECTS.md` | `PLN-LAT-020` | Decomposed into leaf cards |
| `PHASE_3_MORPHISMS.md` | `PLN-LAT-030` | Decomposed into leaf cards |
| `PHASE_4_DISCRIMINANT_DESCENT.md` | `PLN-LAT-040` | Decomposed into leaf cards |
| `PHASE_5_ORTHOGONAL_GROUPS.md` | `PLN-LAT-050` | Decomposed into leaf cards |
| `CATEGORY_REFINEMENT_PHASES.md` | `PLN-CAT-110` | Decomposed into category-refinement subplan |
| `autset_categories_path.md`, `autset_integration_plan.md` | `PLN-CAT-120` | Decomposed into Hom/End/Aut subplan |
| `axioms_with_generators_finitely_presented.md`, `category_creation_notes.md`, `homsets_structural_core.md` | `PLN-CAT-100`, `PLN-CAT-110`, `PLN-CAT-120` | Source maps for foundation cards |
| `RING_INTEGRATION.md`, `SET_SPEC.md` | `PLN-SAGE-000` | Source maps for constructor and family admission |
| `test_spec.sage`, `test_spec2.sage`, `test_spec3.sage` | `tests/sage_spec/category_*` | Migrated executable specs |
| `vulture_whitelist.py` | `/home/dzack/ai/quality-control/vulture_whitelist.py` | Migrated tooling support |
| `todo.md` | Existing critical cards under `PLN-CAT-100` and `PLN-LAT-030` | Folded and deleted |
| `category_specs/TODO.md`, `category_specs/NEEDS_DECISIONS.md` | `.agents/TODO.md` and `.agents/decisions/` policy | Empty/stale holders deleted |

## Acceptance Criteria

- [ ] No new work is added to loose root `plans` TODO files.
- [ ] New work is filed as `.agents` cards under the owning plan.
- [ ] Category vocabulary and method ownership cards are resolved before dependent implementation work proceeds.
- [ ] Sage/source-map claims are researched before constructor admission or implementation.
- [ ] Completed cards are retired rather than retained as a permanent backlog.
