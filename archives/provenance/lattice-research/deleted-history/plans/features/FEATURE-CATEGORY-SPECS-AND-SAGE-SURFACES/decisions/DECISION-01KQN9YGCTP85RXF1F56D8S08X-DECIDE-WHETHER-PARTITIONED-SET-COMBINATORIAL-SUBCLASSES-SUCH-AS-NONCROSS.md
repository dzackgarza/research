---
id: DECISION-01KQN9YGCTP85RXF1F56D8S08X-DECIDE-WHETHER-PARTITIONED-SET-COMBINATORIAL-SUBCLASSES-SUCH-AS-NONCROSS
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide whether partitioned-set combinatorial subclasses such as noncrossing
  and atomic become axiomatic subcategories in the current set-partition pass or a
  later pass
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide whether partitioned-set combinatorial subclasses such as noncrossing and atomic become axiomatic subcategories in the current set-partition pass or a later pass
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Decide whether partitioned-set combinatorial subclasses such as noncrossing and atomic become axiomatic subcategories in the current set-partition pass or a later pass from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Decision Grounding Required

This decision cannot be settled from migrated backlog text alone. Before moving to `decided`, record the source paths inspected, the exact mathematical or category-theoretic alternatives, hypotheses and owner categories, consequences for public methods/constructors/types, and any proof or Sage-evidence obligations. Negative Sage-source findings must use the five-field search format.

## Acceptance Criteria

- [x] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [x] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [x] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Promoted the already-grounded spec decision into this decision record.

## Sources Reviewed

- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/condition.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/sets/subcategories/totally_ordered_finite.py`
- Sage reference manual:
  `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`

## Alternatives

- Admit `Noncrossing`, `Nonnesting`, and `Atomic` now as global axioms directly under
  `Sets().Partitioned()`.
- Keep all five Sage surfaces only as element methods on
  `Sets().Partitioned().ElementMethods`, and delay all subclass-category admission.
- Admit the finite-total-order base-set owner now, keep the five surfaces as element
  methods, and allow later subclass owners only above
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Decision

Do not admit noncrossing, nonnesting, or atomic partitioned-set subclasses as global
axioms in the current pass.

The current owner for `crossings()`, `nestings()`, `is_noncrossing()`,
`is_nonnesting()`, and `is_atomic()` is `Sets().Partitioned().ElementMethods`.
These methods are single-partition element surfaces, not parent constructors and not
category predicates.

The category graph must first encode the required finite totally ordered base-set
hypothesis. That owner is `Sets().Partitioned().FiniteTotallyOrderedBase()`, recorded
in `category_specs/sets/docs/MAPPING.md` and
`plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`.
If future work admits subclass categories, those owners must sit over
`Sets().Partitioned().FiniteTotallyOrderedBase()`, not over bare
`Sets().Partitioned()`.

## Rationale

Sage's crossing and nesting definitions use an arc diagram: the finite base-set
elements are placed in their order on a line, and arcs connect consecutive elements
inside each block. Therefore `crossings()`, `nestings()`, `is_noncrossing()`, and
`is_nonnesting()` require an ordered finite base set.

Sage's `is_atomic()` is also not a generic partition-parent predicate. It is
pipe-indecomposability for a nonempty standard set partition, with blocks ordered by
minimal element and the partition tested against a split `B | C`.

Bare `Sets().Partitioned()` only says "partitions of a fixed base set"; it does not
record the finite total order needed by those notions. Admitting global subclass
axioms there would erase a real hypothesis.

## Consequences

- `category_specs/sets/subcategories/partitioned.py` may expose the five methods as
  element methods with docstrings stating the finite-total-order hypothesis.
- `category_specs/sets/docs/MAPPING.md` is already updated to state that any later
  subclass category must sit above `Sets().Partitioned().FiniteTotallyOrderedBase()`.
- The implementation card should not add `_base_category_class_and_axiom` entries for
  noncrossing, nonnesting, or atomic partitioned sets in this pass.
- Predicate-defined subobjects of a fixed partition parent may be used later through
  the existing `Sets().Subobjects().Of(...)` or `condition_subset(...)` route if a
  concrete subset object is needed before subclass-category admission.

## Affected Tracker Items

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES/tasks/TASK-01KQN9YGCFADA7QY26RA2KSVX3-IMPLEMENT-FIXED-BASE-SETPARTITIONS-CONSTRUCTOR-REFINEMENTS-INTO-SETS-PAR.md`
