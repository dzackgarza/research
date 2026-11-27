---
id: TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-RINGS]]'
title: Source-ground Rings hom section ownership
status: complete
priority: high
description: Audit whether `section()` belongs on generic project ring homomorphisms,
  generic map sections, quotient/subquotient lifts, split injection refinements, or
  specific ring-family hom surfaces.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- Sage generic map/morphism `section()` surfaces and ring-family specializations are
  inventoried with source paths.
- '`category_specs/rings/homsets.py` has a source-grounded owner outcome for `_RingHomomorphisms.section`.'
- '`SPEC-MAPPING-RINGS` records the final owner, reroute, or removal consequence without
  duplicating generic Hom/End/Aut vocabulary.'
complexity: 44
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Source-ground Rings hom section ownership

## Summary

Determine the source-grounded owner for `section()` on project ring homomorphism
surfaces.

## Source Provenance

- `category_specs/rings/homsets.py`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
- `sage/categories/map.pyx`
- `sage/categories/morphism.pyx`
- `sage/rings/morphism.pyx`
- Sage ring-family sources that define or use `section()`, including fraction-field,
  finite-field, number-field, residue-field, p-adic, and Ore/skew polynomial surfaces

## Context

The Rings homset mirroring audit found that installed Sage exposes generic map and
morphism `section()` methods plus many ring-family section implementations, while the
core Sage ring homset/morphism files do not provide a ring-generic `section()` method
parallel to `kernel()`, `lift()`, or fraction-field extension. The owner outcome is to
remove `section()` from the generic project `Rings().HomCategory().ElementMethods`
surface and leave section vocabulary to generic maps, quotient/subquotient lifts,
split/coercion maps, or family-specific hom surfaces.

## Acceptance Criteria

- [x] The generic Sage `Map`, `Morphism`, and identity/morphism section surfaces are
  inventoried with exact source paths and mathematical hypotheses.
- [x] Ring-family `section()` surfaces are grouped by owner: generic map section,
  quotient/subquotient lift, split injection/coercion section, or family-specific hom
  construction.
- [x] `_RingHomomorphisms.section` is either retained with a precise ring-hom owner,
  moved to a better generic/family owner, or removed/rerouted with source evidence.
- [x] `[[SPEC-MAPPING-RINGS]]` records the final owner outcome and any source-code
  follow-up needed to keep the spec and `category_specs/rings/homsets.py` aligned.

## Dependencies And Boundaries

- This card is a sibling correction leaf for the Rings homset mirroring audit, not a
  downstream task. It must be reviewed with the Rings audit because the original
  review found unresolved `section()` ownership blocking approval.
- Do not merge quotient lifts, generic map sections, invertible morphism inverses,
  and family-specific coercion sections under one ring-generic method without a
  source-backed equivalence under explicit hypotheses.
- Do not edit `/home/dzack/sage-mypy-plugin` or route this through checker fixtures.

## Complexity And Ownership

- Owner role: category-spec source auditor.
- Complexity: 44, moderate. The scope is one method name, but the source evidence is
  split across generic Sage map/morphism surfaces and several ring-family
  implementations.

## Work Log

- 2026-05-17: Created from the Rings homset mirroring audit after source mining found
  a current project `section()` declaration with no matching core Sage ring-generic
  source owner.
- 2026-05-17: Resolved the owner by removing `_RingHomomorphisms.section` from
  `category_specs/rings/homsets.py` and recording `section()` as generic map,
  quotient/subquotient lift, split/coercion-map, or family-specific vocabulary in
  `[[SPEC-MAPPING-RINGS]]`. This card now needs fresh-context review together with
  the Rings homset mirroring audit.
- 2026-05-17: Fresh-context review recommended `needs-human-input` with no blocking
  findings after the owner correction.

## Review Log

### Fresh-Context Agent Review - 2026-05-17

Recommendation: `needs-human-input`.

- Blocking findings: none.
- Review checked that `category_specs/rings/homsets.py` no longer declares
  `_RingHomomorphisms.section`.
- Source evidence checked: Sage `Map.section`, composite-map `section`, identity
  morphism `section`, and set-isomorphism `section` are generic map/morphism surfaces;
  checked core ring homset/morphism sources do not define a ring-generic `section()`
  method.
- Routing: this card is human-gated with the Rings homset mirroring audit.
