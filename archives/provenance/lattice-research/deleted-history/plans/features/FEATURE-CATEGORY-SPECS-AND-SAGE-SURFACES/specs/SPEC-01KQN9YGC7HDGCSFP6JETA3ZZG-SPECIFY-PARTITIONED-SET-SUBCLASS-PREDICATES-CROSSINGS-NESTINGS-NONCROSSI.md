---
id: SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
title: Specify partitioned-set subclass predicates crossings nestings noncrossing
  nonnesting and atomic only after subcategory admission
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
- No implementation blocker was discovered during this spec pass; the remaining finite-total-order
  prerequisite is represented as a separate spec item.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify partitioned-set subclass predicates crossings nestings noncrossing nonnesting and atomic only after subcategory admission
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Specify partitioned-set subclass predicates crossings nestings noncrossing nonnesting and atomic only after subcategory admission from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Source-Mining Contract

This leaf is truly source-mining because the mapping records the surfaces but does not
yet admit the governing subcategories.

Exact source anchors to mine:

- `category_specs/sets/docs/MAPPING.md:194-216`, especially row `:213`, which records
  `crossings`, `nestings`, `is_noncrossing`, `is_nonnesting`, and `is_atomic` as
  partitioned-set surfaces reserved for future axiomatic subcategory admission.
- `category_specs/sets/docs/MAPPING.md:209-214`, which fixes the surrounding object as
  an ordered finite set partition with arc-diagram and restriction/standardization
  methods on the same partition element surface.
- `.agents/skills/category-spec-style/references/style.md:1160-1169`, which governs how
  any admitted axiomatic subcategory must register `_base_category_class_and_axiom`.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  the final methods and predicates to be placed at the highest mathematically valid
  owner category.

Decision this source-mining pass must produce:

- Object/method/constructor decision: separate the witness-valued surfaces
  `crossings()` and `nestings()` from the boolean/predicate surfaces
  `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()`, and state whether the
  booleans remain element predicates, induce admitted axiomatic subcategories, or both.
- Owner category decision: identify the exact owner under `Sets().Partitioned()` for
  each surface, including any future admitted subcategories such as noncrossing,
  nonnesting, or atomic partitioned sets.
- Hypotheses: record the exact domain assumptions needed for each notion, including
  whether the predicate requires a finite partition, a linearly ordered base set, and
  the arc-diagram interpretation fixed by the partition mapping.
- Return object/codomain: `crossings()` and `nestings()` must land in witness lists of
  crossing/nesting arc pairs, not scalar counts; `is_noncrossing()`,
  `is_nonnesting()`, and `is_atomic()` must land in boolean predicates or in admitted
  axiomatic subcategory membership with the boolean witness spelled out.

Retire this card only when the cited sources produce a grounded owner decision and, if
subcategory admission is chosen, the exact admitted axiom names and registration shape.
Reject this leaf if source review shows these notions should remain only as combinatorial
element methods with no subcategory admission at all.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass; the remaining
  finite-total-order prerequisite is represented as a separate spec item.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Grounded Decision

Sources reviewed for this decision:

- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/condition.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/sets/subcategories/totally_ordered_finite.py`
- Sage reference manual:
  `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`

Owner and codomain decision:

- `crossings()` and `nestings()` are `Sets().Partitioned().ElementMethods` surfaces.
  Sage defines them on `SetPartition` elements and returns witness lists of pairs of
  arcs, not counts and not parent-level data.
- `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` are also
  `Sets().Partitioned().ElementMethods` surfaces. They are boolean predicates on a
  single partition element, not constructors and not parent/category predicates.
- `crossings_iterator()` and `nestings_iterator()` stay implementation helpers, not
  primary project method names. The spec surface keeps the finite witness lists and the
  booleans built from them.

Hypotheses and admission consequence:

- `crossings()`, `nestings()`, `is_noncrossing()`, and `is_nonnesting()` require the
  finite base set to be totally ordered. Sage's definition is the arc-diagram picture
  obtained by placing ground-set elements in order on a line and connecting consecutive
  elements within each block.
- `is_atomic()` is not an arc-count notion. Sage defines it by pipe-indecomposability
  of a nonempty standard set partition: order the blocks by minimal element and ask
  whether the partition splits as `B | C`.
- Because the current `Sets().Partitioned()` axiom captures only "partitions of a
  fixed base set", these predicates are not admitted yet as axiomatic subcategories
  such as `Sets().Partitioned().Noncrossing()`, `.Nonnesting()`, or `.Atomic()`. The
  missing owner is a source-grounded category that records the required finite total
  order on the base set.
- If the project later needs subclass objects before that owner exists, the first
  admissible constructor is a predicate-defined subobject of a fixed partition parent
  via the existing `Sets().Subobjects().Of(...)` / `condition_subset(...)` route, not a
  new global partition axiom.

Acceptance consequence for implementation:

- `category_specs/sets/subcategories/partitioned.py` should carry abstract element
  methods for `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()`, and
  `is_atomic()`, with the finite totally ordered base-set hypothesis stated in the
  docstrings.
- A future admission card is still required before adding `_base_category_class_and_axiom`
  registrations for noncrossing, nonnesting, or atomic partition categories.

## 6-Gate Protocol Review Log

Review date: 2026-05-07
Reviewer: fresh-context subagent (6-gate spec card review)

### Gate 1 — Source Grounding

**Verdict: PARTIAL PASS (substantive claims grounded; line-number references stale)**

Source verification:

| Claim in spec | Cited source | Actual verification |
|---|---|---|
| Row :213 records crossings/nestings/is_noncrossing/is_nonnesting/is_atomic | `MAPPING.md:194-216` | MAPPING.md is now a 7-line redirect stub pointing to `SPEC-MAPPING-SETS.md`. The actual mapping decisions for these five surfaces are in SPEC-MAPPING-SETS.md lines 393-397 and 408-427. The substantive content exists and is correct, but the line-number citation is stale. |
| Arc-diagram and restriction/standardization methods on the partition element surface | `MAPPING.md:209-214` | Same staleness issue. The actual content is in SPEC-MAPPING-SETS.md lines 393-404 under "Sage SetPartition Method Mapping Decisions". The arc-diagram methods (arcs, openers, closers) are documented in SAGE_INVENTORY.md lines 509 and 512-514. |
| `_base_category_class_and_axiom` registration | `style.md:1160-1169` | **Line numbers do not match.** Lines 1160-1169 of style.md discuss constructor-collector guard assertions. The `_base_category_class_and_axiom` guidance actually lives at lines 1258-1268 ("Axiomatic Subcategory Registration"). |
| Highest mathematically valid owner category | `style.md:1229-1242` | Partially correct. Lines 1229-1234 cover Sage Naming Disambiguation. The "methods placed at highest mathematically valid owner" principle is at lines 1221-1224 ("Method surface separation is strict: a method belongs in the category whose axioms are the minimum required for it to be well-defined"). Lines 1235-1242 begin the "Sage Inventory and Mapping" section. The spec's citation window spans two sections. |

Sage source verification (direct inspection): The mathematical definitions of `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` were verified by inspecting the installed Sage 10.7 source at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/combinat/set_partition.py`. All five methods exist, are on the `SetPartition` element class, and match the spec's characterizations.

Remediation: Update the line-number citations in the spec's "Source-Mining Contract" section to reference the canonical locations in SPEC-MAPPING-SETS.md and the correct style.md line ranges. The substantive grounding is sound; only the pointer precision needs correction.

### Gate 2 — Sage Surface Completeness

**Verdict: PASS**

All Sage surfaces relevant to the five partitioned-set subclass predicates are explicitly mapped:

| Sage surface | Mapped in spec? | Project target | Status |
|---|---|---|---|
| `crossings()` | Yes | ElementMethods (returns list of arc-pair tuples) | Correct |
| `nestings()` | Yes | ElementMethods (returns list of arc-pair tuples) | Correct |
| `is_noncrossing()` | Yes | ElementMethods (boolean predicate) | Correct |
| `is_nonnesting()` | Yes | ElementMethods (boolean predicate) | Correct |
| `is_atomic()` | Yes | ElementMethods (boolean predicate) | Correct |
| `crossings_iterator()` | Yes | Explicitly rejected as public name; kept as implementation helper | Correct |
| `nestings_iterator()` | Yes | Explicitly rejected as public name; kept as implementation helper | Correct |
| `number_of_crossings()` | No | Not addressed in this spec card | Minor gap — this is a Sage-compatibility convenience derived from `len(crossings())`. Does not block the five primary surfaces. |

The spec correctly separates witness-valued surfaces (`crossings()`, `nestings()` → list-of-pairs) from boolean surfaces (`is_noncrossing()`, `is_nonnesting()`, `is_atomic()` → bool), matching Sage's actual return types verified via `inspect.getsource`.

### Gate 3 — Mathematical Correctness

**Verdict: PASS with one category-placement discrepancy (see Finding 1 below)**

**Crossing definition (verified from Sage source):** For arcs sorted by minimum endpoint (i1 < i2, i1 < j1, i2 < j2), arcs (i1,j1) and (i2,j2) cross when i2 < j1 < j2 — i.e., the endpoints are interleaved as i1 < i2 < j1 < j2. This is the standard arc-diagram crossing condition for set partitions on a totally ordered ground set. Mathematically correct. ✓

**Nesting definition (verified from Sage source):** For arcs sorted by minimum endpoint, (i1,j1) nests (i2,j2) when i2 < j2 < j1 — i.e., arc (i2,j2) is properly contained inside arc (i1,j1). Mathematically correct and the natural dual of the crossing condition. ✓

**is_noncrossing / is_nonnesting (verified from Sage source):** Boolean predicates returning True exactly when the corresponding iterator is empty. Mathematically correct as predicates on a single partition element. ✓

**is_atomic (verified from Sage source):** Defined by pipe-indecomposability: order blocks by minimal element, check whether `max(blocks[:k]) < min(blocks[k:])` for any split point k. Nonempty and indecomposable = atomic. Empty partition returns False. Mathematically correct — this is the standard definition of atomic set partitions (also called "irreducible" or "connected" in the literature). ✓

**Hypothesis documentation:** The spec correctly identifies that crossings, nestings, is_noncrossing, and is_nonnesting require the base set to be finite and totally ordered (for the arc-diagram interpretation). The spec correctly identifies that is_atomic requires a nonempty standard (min-ordered) finite partition. ✓

**Subcategory admission deferral:** The spec correctly defers `Noncrossing`, `Nonnesting`, and `Atomic` as axiomatic subcategories, pending a source-grounded category that records the finite totally ordered base set. This is mathematically sound: these predicates are not well-defined on arbitrary partitioned sets without the order hypothesis. ✓

**Finding 1 — Category placement discrepancy:** The spec card's "Grounded Decision" (lines 119-127) states that these five methods are `Sets().Partitioned().ElementMethods` surfaces. However:

- The code in `partitioned.py` correctly places them on `PartitionsCategory.ElementMethods` (lines 209-252), NOT on `PartitionedSetsCategory.ElementMethods` (which is empty at line 57).
- The `PartitionedSetsCategory` docstring (line 30-32) itself states: "The partition object itself lives in the `PartitionsCategory` and owns methods such as `crossings()`, `is_noncrossing()`, and `refines()`."
- The smoketest at `smoketest.sage:538-542` verifies these methods on `PartitionsCategory.ElementMethods`.
- Mathematically, a partitioned set `X` in `Sets().Partitioned()` has elements that are elements of the ground set `X`, not partition objects. The partition object is accessed via `X.partition()` and lives in `PartitionsCategory`. So `crossings()` belongs on the partition object's element methods (`PartitionsCategory.ElementMethods`), not on the partitioned set's element methods.

**Severity: Medium.** The spec's conclusion about WHAT the methods are and WHERE they live in the code file (`partitioned.py`) is correct. The error is only in which inner class namespace (`PartitionedSetsCategory.ElementMethods` vs `PartitionsCategory.ElementMethods`). The acceptance-consequence section (lines 150-155) is also affected: it says "partitioned.py should carry abstract element methods" — which it already does, just on the correct `PartitionsCategory.ElementMethods`.

**Recommendation:** Correct the "Grounded Decision" section to state `PartitionsCategory.ElementMethods` (or the navigable path `Sets().Partitioned().Partitions().ElementMethods` if such navigation exists). Update lines 119-127 and 150-155 accordingly.

### Gate 4 — Nonmathematical Rejection

**Verdict: PASS**

The spec correctly rejects or relegates:

- `crossings_iterator()` and `nestings_iterator()`: Explicitly kept as implementation helpers, not primary project method names (line 126-127). ✓
- No variadic option bags, no Sage implementation-container exposure. ✓
- The spec does not propose exposing Sage's internal arc-sorting or generator mechanics as public surfaces. ✓
- Sage's `number_of_crossings()` / `number_of_nestings()` convenience counters are not proposed as independent category methods (they are derivable from `len(crossings())`). If needed, they are implicit in the finite-witness-list design. ✓

### Gate 5 — Ambiguity Routing

**Verdict: PASS**

Remaining ambiguities are properly routed:

| Ambiguity | Routing | Target |
|---|---|---|
| Admitted subcategory axioms for Noncrossing, Nonnesting, Atomic | Deferred | Future admission card after finite-totally-ordered-base owner exists (lines 141-146) |
| Finite totally ordered base set prerequisite | Routed | Tracked in `SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md` (line 164) |
| Subclass objects needed before axiom owner exists | Routed | Predicate-defined subobjects via `Sets().Subobjects().Of(...)` / `condition_subset(...)` (lines 143-146) |
| Exact axiom names and registration shape for later subcategories | Deferred | Future source-grounded pass (lines 84-86) |

No ambiguity is left unaddressed. All gaps have a documented routing path.

### Gate 6 — Obligation Preservation

**Verdict: PASS**

The spec preserves all obligations from the source mapping:

- Five abstract element methods specified: `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()`, `is_atomic()`. ✓
- Each method's return type is specified: witness lists of arc pairs for crossings/nestings, booleans for the three predicates. ✓
- Hypothesis documentation required in docstrings (finite totally ordered base set). ✓
- `_base_category_class_and_axiom` registrations blocked pending prerequisite owner. ✓
- Constructor paths preserved: no weakening of the `Sets().Constructors()` surface. ✓
- No weakening of the spec to match Sage gaps — the spec maintains the ideal mathematical interface while acknowledging Sage interop constraints. ✓

### Overall Assessment

| Gate | Verdict |
|---|---|
| G1 — Source Grounding | PARTIAL PASS (line references stale) |
| G2 — Sage Surface Completeness | PASS |
| G3 — Mathematical Correctness | PASS (category-placement discrepancy noted) |
| G4 — Nonmathematical Rejection | PASS |
| G5 — Ambiguity Routing | PASS |
| G6 — Obligation Preservation | PASS |

**Outcome: needs-revision.** The card passes on mathematical substance, surface completeness, and ambiguity routing. However, G1's stale line-number citations and G3's category-placement discrepancy (`Sets().Partitioned().ElementMethods` → should be `PartitionsCategory.ElementMethods`) require correction before the card can be marked `complete`. These are documentation/precision issues, not mathematical errors.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Grounded the owner decision against Sage's `SetPartition` docs and the
  local partitioned-set mapping. Recorded that the five surfaces belong on
  `Sets().Partitioned().ElementMethods` now, while axiom admission remains blocked on a
  category that records finite totally ordered base sets. That prerequisite is now
  tracked in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`.
