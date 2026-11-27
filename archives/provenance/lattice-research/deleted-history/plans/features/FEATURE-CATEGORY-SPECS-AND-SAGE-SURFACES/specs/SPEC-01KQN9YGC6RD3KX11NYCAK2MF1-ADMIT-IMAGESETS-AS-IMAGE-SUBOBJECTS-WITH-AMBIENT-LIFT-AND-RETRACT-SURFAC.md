---
id: SPEC-01KQN9YGC6RD3KX11NYCAK2MF1-ADMIT-IMAGESETS-AS-IMAGE-SUBOBJECTS-WITH-AMBIENT-LIFT-AND-RETRACT-SURFAC
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Admit ImageSets as image subobjects with ambient lift and retract surface
status: complete
priority: critical
requirement: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Admit ImageSets as image subobjects with ambient lift and retract surface
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Admit ImageSets as image subobjects with ambient lift and retract surface from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Grounded Spec Contract

Canonical source anchors for this card are:

- `category_specs/sets/docs/MAPPING.md`:
  - local-surface row
    `| _ImageSets | subcategories/image.py | Images are subobjects under a map. |`
  - constructor decision row
    `| ImageSubobject(f, X) | ImageSets | Image subobject under a map; must include ambient, lift, and retract. |`
  - subobject-routing rows for `ConditionSet` and constructive subobjects
- `category_specs/sets/docs/SAGE_INVENTORY.md` if additional Sage surface detail is
  needed for `ImageSubobject`
- `category_specs/topological_spaces/docs/MAPPING.md` only if a future example uses
  image subsets inside a topological ambient; it is not owner authority for the image
  notion itself

Spec decision fixed by those sources:

- owner category: `Sets().Subobjects()` with explicit refinement through
  `Sets().Subquotients()` owns the image notion
- admitted object: `ImageSets` is the public image-subobject category for images of a
  map, not a generic wrapper around arbitrary Sage `Set(X)` values
- required public surface on the image object is `ambient`, `lift`, and `retract`

Required hypotheses and return/codomain obligations:

- input data must include a map `f` and an ambient/source object `X` sufficient to form
  the image subobject
- `ambient()` returns the ambient set containing the image subobject
- `lift(...)` returns an image element viewed in the ambient codomain
- `retract(...)` returns the corresponding image-side object or element when an
  ambient element is in the image, matching the constructive subobject contract
- any further topological or algebraic refinement is inherited from the ambient object;
  it does not redefine the set-level image owner
- Sage's arbitrary callable wrapping and non-parent `Set(X)` fallback are interop
  details; the project constructor surface stays typed as `SetMorphism` plus
  `Subset`

Rejection or retirement condition:

- reject any edit that exposes generic Sage `Set(X)` as the public constructor, drops
  any of `ambient`/`lift`/`retract`, or relocates image ownership away from the
  subobject construction surface without a new mapped source anchor

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Admitted `_ImageSets` as a constructive image subobject/subquotient
  surface, recorded the `ambient`/`lift`/`retract` obligations in mapping docs and
  `image.py`, and rejected Sage's generic callable/`Set(X)` fallback as public project
  API.

## 6-Gate Protocol Review Log

### Independent Review — 2026-05-07

**Status:** PASS — all six gates passed. No implementation blockers.

---

#### G1 — Source Grounding: PASS

All cited source files exist and are accessible:

- `category_specs/sets/docs/MAPPING.md` — exists but is now a redirect to
  `SPEC-MAPPING-SETS.md`. The original mapping content has been converted into
  the tracked spec at
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`,
  which contains all the rows this spec claims. Specifically:
  - Local-surface row at line 226: `_ImageSets | subcategories/image.py | Images are subobjects under a map.`
  - Constructor row at line 300: `ImageSubobject(f, X) | ImageSets | Image subobject under a map; must include ambient, lift, and retract.`
  - Subquotient admission section at lines 324–345 details the full `ambient`/`lift`/`retract` contract.
- `category_specs/sets/docs/SAGE_INVENTORY.md` — exists (742 lines). Confirms
  Sage's `ImageSubobject` at lines 428–437 with documented methods `ambient()`,
  `lift(x)`, `retract(x)`.
- `category_specs/topological_spaces/docs/MAPPING.md` — exists but is also a
  redirect. The spec correctly notes this is auxiliary only and not owner
  authority.
- Implementation file `category_specs/sets/subcategories/image.py` — exists
  (124 lines). Defines `_ImageSets` category with `super_categories =
  [Sets().Subobjects(), Sets().Subquotients()]` and abstract methods
  `ambient`, `lift`, `retract`, `cardinality`, `__iter__`, `__contains__`,
  `_an_element_`, `_sympy_`, plus equality/hash.

**Verdict:** Every source anchor is verifiable. The redirect of MAPPING.md to
a tracked spec is a structural migration, not a grounding failure — the
content exists at the canonical spec location.

---

#### G2 — Completeness: PASS

The spec fully specifies:

- **Owner category:** `Sets().Subobjects()` with refinement through
  `Sets().Subquotients()`.
- **Admitted object:** `_ImageSets` as the public image-subobject category.
- **Required public surface:** `ambient`, `lift`, `retract` — all three
  are named with return types and behavioral contracts.
- **Input data:** map `f` and ambient/source object `X` sufficient to form
  the image subobject.
- **Return/codomain obligations:**
  - `ambient()` → ambient set containing the image subobject.
  - `lift(...)` → image element viewed in ambient codomain.
  - `retract(...)` → image-side object when ambient element is in the image.
- **Inheritance rules:** topological/algebraic refinement inherited from
  ambient; does not redefine set-level image owner.
- **Constructor path:** `Sets().Constructors().ImageSubobject(f, domain_subset)`
  typed as `SetMorphism` plus `Subset`.
- **Acceptance criteria:** 5 items, all checked `[x]`.
- **Dependencies:** documented with explicit boundaries.

No gaps in specification. The constructor path, category refinement chain,
method signatures, and rejection conditions are all explicit.

---

#### G3 — Mathematical Correctness: PASS

The image subobject construction is mathematically sound:

- **Category-theoretic grounding:** In Set, the image of a map
  `f: X → Y` is the subobject of `Y` defined as `{f(x) | x ∈ X}`. This is
  standard: the image is a monomorphism (inclusion) factoring `f` through
  the epi-mono factorization.

- **Subobject/subquotient interface:** The `ambient`/`lift`/`retract` triple
  correctly implements the constructive subquotient pattern:
  - `ambient()`: the codomain `Y` of the defining map — correct: the image is
    a subset of the codomain.
  - `lift(x)`: the inclusion `image ↪ Y` — correct: lifts an element of the
    image into the ambient set.
  - `retract(x)`: partial inverse of lift, defined when `x ∈ Y` lies in the
    image — correct: retracts an ambient element to its preimage
    representation.

- **Category placement:** `_ImageSets` has supercategories
  `[Sets().Subobjects(), Sets().Subquotients()]`. This is correct: an image
  is a subobject of the codomain, and the constructive subquotient machinery
  provides the ambient/lift/retract protocol.

- **Refinement chain verified:** The spec correctly notes that topological or
  algebraic refinement is inherited from the ambient object and does not
  redefine the set-level image owner.

- **Rejection of invalid constructions:** The spec correctly rejects:
  - `ImageSubobject` as a generic wrapper around `Set(X)`.
  - Dropping `ambient`/`lift`/`retract` from the public surface.
  - Relocating ownership without a new mapped source anchor.
  - Sage arbitrary-callable wrapping as a public signature.

No mathematical errors or category-theoretic violations found.

---

#### G4 — Non-Math Rejection: PASS

The spec explicitly rejects four categories of non-mathematical targets:

1. **Generic Sage `Set(X)` wrapping** rejected as public constructor — Sage's
   `Set` factory is an arbitrary wrapper, not a mathematical construction.
2. **Dropping `ambient`/`lift`/`retract`** — these are the defining
   mathematical surface of a constructive subquotient.
3. **Relocating image ownership** without a source-grounded replacement — the
   image notion belongs to subobjects/subquotients; any move requires evidence.
4. **Sage callable/Set(X) fallback** — arbitrary callable wrapping and
   non-parent domains are implementation interop, not public constructor shapes.

Additionally, the mapped spec (`SPEC-MAPPING-SETS.md`) confirms that
`ImageSubobject` must refine through `_ImageSets` with `Sets().Subobjects()`
and `Sets().Subquotients()` supercategories — the Sage generic fallback is not
the project route. No variadic option bags, no implementation-container
exposure, no smoke-driven interface weakening.

---

#### G5 — Ambiguity Routing: PASS

The spec handles ambiguity through:

- **Inheritance rule:** "any further topological or algebraic refinement is
  inherited from the ambient object; it does not redefine the set-level image
  owner" — resolves the question of where topological structure on an image
  subset lives.
- **Dependencies section:** "If execution reveals a missing mathematical owner,
  constructor, or category graph edge, split that as a new tracker item instead
  of patching around it" — clear routing for unforeseen gaps.
- **DAG integration:** `dependsOn` links to `PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY`
  and parent `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, ensuring the spec is
  evaluated in the correct dependency order.
- **Rejection/retirement condition:** provides a clear trigger for when the
  spec should be rejected — if any of `ambient`/`lift`/`retract` are removed
  or ownership is relocated without new evidence.

No unresolved ambiguities remain for the set-level image subobject construction.

---

#### G6 — Preservation: PASS

Provenance is preserved throughout:

- **Source provenance section** cites the original `MAPPING.md` source and
  the migrated line with exact text.
- **Work log** records creation from migration repair and the 2026-05-05
  admission of `_ImageSets` with method surface and rejections documented.
- **Tracker metadata** preserves the SPEC ID, parent feature, dependency
  edges, priority, and tags.
- **Dependencies section** mandates preservation of source paths and
  SAGE_INVENTORY.md/MAPPING.md as provenance documents.
- **Original source** is traceable through the redirect at
  `category_specs/sets/docs/MAPPING.md` → `SPEC-MAPPING-SETS.md`.

No information loss. Migration provenance is fully traceable.

---

#### Summary

| Gate | Result | Notes |
|------|--------|-------|
| G1 Source Grounding | PASS | All 4 source files exist and contain claimed content |
| G2 Completeness | PASS | Owner, constructor, surface, rejection conditions all specified |
| G3 Math Correctness | PASS | Image subobject = epi-mono factorization; ambient/lift/retract correct |
| G4 Non-Math Rejection | PASS | 4 explicit rejection categories; no wrapper/fallback leakage |
| G5 Ambiguity Routing | PASS | Inheritance rule, tracker-split rule, DAG integration |
| G6 Preservation | PASS | Full provenance chain from MAPPING.md through migration to tracked spec |

**Outcome:** The spec is mathematically grounded, source-verified, and
complete. No blockers. Ready for implementation per the constructor path
`Sets().Constructors().ImageSubobject(f, domain_subset)`.
