---
id: DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide HomCategory semantic base and Sage homset mirroring route
status: decided
priority: critical
chosen: Use project HomCategory as the semantic base and mirror Sage homset surfaces explicitly
options:
- name: Treat Sage generic homsets as the semantic base and align project ownership to inherited Sage parent methods
  pros:
  - Keeps the generic owner story closer to Sage runtime inheritance.
  - Reduces duplication if the inherited Sage generic surface is accepted as canonical.
  cons:
  - The project generic hom category is already specified as a separate construction rather than a Sage subclassing story.
  - Overstates the mathematical importance of a mostly thin generic Sage homset root.
  - Obscures the real requirement: each subtree hom spec must explicitly own/mirror the Sage homset methods it keeps.
- name: Use project HomCategory as the semantic base and mirror Sage homset surfaces explicitly
  pros:
  - Matches the project design that `HomCategoryConstruction` is the mathematical owner and Sage `HomsetsCategory` is inventory/interop.
  - Makes subtree obligations explicit: Sage homset methods must appear in the corresponding project hom specs instead of being assumed inherited.
  - Separates semantic ownership from optional backend reuse of Sage container plumbing.
  cons:
  - Reopens the generic homsets mapping and subtree mapping audit path.
  - Requires per-subtree follow-up cards instead of one generic inheritance fix.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide generic homset parent ownership and Sage integration route

## Summary

The repo should not treat Sage generic homsets as the semantic owner of the
project Hom/End/Aut hierarchy. `HomCategoryConstruction` is the project-owned
construction, and Sage homset surfaces are inventory/backing inputs that must be
mirrored explicitly into project hom specs where the project decides to keep
them.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-HOMSETS.md`
- `category_specs/homsets/homsets.py`
- `category_specs/homsets/endsets.py`
- `category_specs/homsets/autsets.py`
- `plans/visuals/homsets-category-hierarchy.md`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homsets.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homset.py`

## Context

The earlier QC trace established two different facts:

- the project category method-container chain for `HomCategory.parent_class`
  does **not** inherit Sage's generic `Homset` parent surface; and
- the concrete objects returned by Sage's `Hom(...)` constructor still use Sage
  homset container classes as backend runtime objects.

Those facts do **not** force Sage generic homsets to be the project semantic
base. The generic Sage layer is relatively thin:

- `sage.categories.homset.Homset` contributes container accessors such as
  `domain()`, `codomain()`, `identity()`, `one()`, `reversed()`, and
  `natural_map()`;
- `sage.categories.homsets.Homsets.ParentMethods` contributes
  `is_endomorphism_set()`;
- `Homsets().Endset()` adds the endset axiom and monoid supercategory.

The project already defines a distinct `HomCategoryConstruction` and has
subtree hom specs for sets, rings, modules, algebras, posets, lattices,
topological spaces, and Cat. The real requirement is therefore not
"inherit Sage's generic homset owner chain", but "audit every subtree mapping so
all Sage homset/container methods that matter for that subtree are mirrored onto
the corresponding project hom specs."

## Decision

Use project `HomCategory` / `EndCategory` / `AutCategory` as the semantic base.
Do **not** frame the project as inheriting or extending Sage generic homset
constructions.

Instead:

- Sage generic homsets remain source inventory and optional backend evidence.
- The project mirrors any retained Sage homset surface through the
  `HomCategoryConstruction` hierarchy and the relevant subtree hom specs.
- Every homset-bearing subtree mapping doc must be audited so that Sage methods
  like `zero()`, `identity()`, constructor/coercion entry points, and other
  hom-container operations are either:
  - admitted on the subtree project hom spec,
  - routed to a more specific owner, or
  - explicitly rejected as Sage interop-only behavior.

Consequences:

- `SPEC-MAPPING-HOMSETS.md` must stop sounding like the project inherits the Sage
  generic homset owner chain;
- the subtree mapping specs become the place where retained Sage homset/container
  methods are explicitly mirrored and grounded;
- many current homset-layer `@override` markers can be relaxed or removed because
  they no longer need to pretend to override Sage generic homset owners; only
  project-internal inheritance chains should keep `@override`;
- plugin/QC follow-up must not assume generic hom-layer methods are inherited
  Sage overrides just because the backend object container happens to be a Sage
  homset class.

## Acceptance Criteria

- [x] The decision states whether project hom categories semantically inherit Sage
      generic homsets or redefine/mirror them.
- [x] The decision records that the generic Sage homset layer is mostly thin
      container behavior rather than the project's mathematical foundation.
- [x] The chosen route explains why subtree mapping docs, not generic inheritance,
      are the follow-up surface.
- [x] Follow-up execution is routed to a tracked task rather than left in chat.

## Dependencies And Boundaries

- Do not treat backend reuse of a Sage container class as semantic inheritance.
- Do not let convenience Sage container methods silently bypass subtree mapping
  ownership.
- Do not collapse the Hom/End/Aut owner distinction merely because Sage exposes a
  generic `Homset` container and an `Endset` axiom layer.

## Work Log

- 2026-05-10: Created during repo QC follow-up after runtime tracing established that
  the generic Hom/End/Aut override failures are mixed rather than plugin-only.
- 2026-05-10: Revised after deeper runtime/source review: the repo does not
  semantically inherit Sage generic homsets, and the correct follow-up is explicit
  subtree homset mirroring audits rather than a generic inheritance repair.
