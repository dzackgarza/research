---
id: DECISION-01KQN9J3XCYW748M5V0K2SGJGK-DECIDE-WHETHER-EQUIVALENCE-RELATIONS-AND-SET-PARTITIONS-NEED-A-FIRST-CLA
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide whether equivalence relations and set partitions need a first-class
  set subtree or remain centralized Sage-backed type aliases
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases

## Summary

The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
design decision about equivalence relations/set partitions, and evidence gaps around
semilattice category introspection.

## Source Provenance

- The migrated recovery path `category_specs/posets/docs/TRIAGE.md` is stale.
  The deleted triage file actually lived at
  `plans/category_specs/posets/docs/TRIAGE.md`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/posets/docs/TRIAGE.md`.
- Original migrated line: `Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases from category_specs/posets/docs/TRIAGE.md`

## Context

- Poset constructors are named non-variadic adaptations; acyclic DiGraph is the canonical finite-poset constructor.
- Meet and join expose binary operations plus sequence folds, not optional-argument aggregate signatures.
- Lattice congruences use set-theoretic vocabulary: EquivalenceRelation and SetPartition, with congruence_generated_by(blocks).
- certificate=True Sage paths map to separately named witness-returning certificate methods.
- Sage semilattice category evidence remains incomplete because local Sage imports failed before category introspection.

## Decision Grounding Required

This decision cannot be settled from migrated backlog text alone. Before moving to `decided`, record the source paths inspected, the exact mathematical or category-theoretic alternatives, hypotheses and owner categories, consequences for public methods/constructors/types, and any proof or Sage-evidence obligations. Negative Sage-source findings must use the five-field search format.

## Acceptance Criteria

- [x] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [x] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [x] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [x] Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- [x] Use the five-field negative-finding format for further Sage semilattice evidence gaps.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Promoted the already-grounded partition/equivalence-relation
  ownership split into this decision record.

## Sources Reviewed

- `plans/category_specs/posets/docs/TRIAGE.md` recovered from `8d1c21c^`
- `category_specs/posets/docs/MAPPING.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/constructions/quotients.py`
- `category_specs/types.py`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES/tasks/TASK-01KQN9YGCS8P5BYN15M4NKCWCF-RESEARCH-LOCAL-SAGE-POSET-IMPORT-FAILURE-AND-COMPLETE-IMPORT-LEVEL-CATEG.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-01KQN9YGCTP85RXF1F56D8S08X-DECIDE-WHETHER-PARTITIONED-SET-COMBINATORIAL-SUBCLASSES-SUCH-AS-NONCROSS.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md`

## Source Path Correction

- Searched: `git show 8d1c21c^:category_specs/posets/docs/TRIAGE.md`
- Found: the path is absent at `8d1c21c^`.
- Conclusion: Inference: the migrated source path is stale; the recoverable archived
  triage file is `plans/category_specs/posets/docs/TRIAGE.md` at `8d1c21c^`.
- Confidence: High, because the corrected path was recovered and read.
- Gaps: None for this card's deleted-triage provenance.

## Alternatives

- Create a separate first-class `Sets().EquivalenceRelations()` subtree now, with
  equivalence relations distinct from set partitions as parent objects.
- Keep both equivalence relations and set partitions only as centralized Sage-backed
  type aliases in `types.py`, with no set-subtree owner.
- Use the existing first-class fixed-base partition subtree for set partitions, keep
  `SetPartition` and `EquivalenceRelation` as Sage-backed element/type vocabulary, and
  route quotient-set structure through the existing quotient construction surface.

## Decision

Set partitions have a first-class set subtree for fixed-base parents:
`Sets().Partitioned()`, with the finite-total-order refinement
`Sets().Partitioned().FiniteTotallyOrderedBase()` when the base-set hypothesis is
present.

Do not create a separate `Sets().EquivalenceRelations()` subtree in the current
category-spec pass. For current finite-set and finite-lattice congruence work,
`EquivalenceRelation` is set-theoretic vocabulary represented by Sage's
`SetPartition` element class on a specified base set. The centralized type aliases in
`category_specs/types.py` therefore stay:

- `SetPartition = SageSetPartition`
- `SetPartitionsParent = SageSetPartitions`
- `EquivalenceRelation = SetPartition`

Quotient-set objects and equivalence-class structure are owned by
`Sets().Quotients()` and the subquotient construction surface, not by a new
equivalence-relation subtree.

## Rationale

For a fixed base set, a partition of the base set and an equivalence relation on that
base set carry the same set-theoretic data: the relation sends two elements to the
same block, and the partition is the set of equivalence classes. The fixed-base
hypothesis is essential because `SetPartitions()` with no base set is only the
countable parent of all finite partitions and has no single powerset ambient.

Sage's concrete representation supports this owner split. `SetPartitions(s)` is the
parent of partitions of `s`; `SetPartition` is the element class; and poset lattice
congruence methods return congruence data represented by Sage set partitions. The
project mapping already routes fixed-base `SetPartitions(s)` into
`Sets().Partitioned()`, keeps all finite partitions without a fixed base in
`Sets().Countable()`, and maps finite-lattice `congruence(blocks)` to
`congruence_generated_by(blocks)` returning an `EquivalenceRelation` represented by a
`SetPartition`.

A separate equivalence-relation subtree would duplicate the fixed-base partition
surface without adding a currently needed owner. If future work needs relation-object
methods that are not recovered by partition elements or quotient-set objects, that
work should be grounded from Sage/source/theory evidence and filed as a new decision
or spec card.

## Consequences

- `category_specs/sets/subcategories/partitioned.py` remains the first-class owner for
  fixed-base set partitions.
- `category_specs/types.py` remains the owner for the Sage-backed element aliases
  `SetPartition`, `SetPartitionsParent`, and `EquivalenceRelation`.
- `category_specs/posets/docs/MAPPING.md` can keep using `EquivalenceRelation` as the
  return vocabulary for lattice congruences, with the representation routed through
  `SetPartition` and `Sets().Partitioned()` when a finite lattice base set is fixed.
- `SetPartitions()` without a fixed base remains countable-only, not
  `Sets().Partitioned()`.
- `DisjointSet` remains a mutable union-find implementation source whose
  `set_partition()` method is evidence for conversion to `SetPartition`; it is not a
  public category object or subtree.
- No mapping-file edit is required in this decision commit because
  `category_specs/sets/docs/MAPPING.md` and `category_specs/posets/docs/MAPPING.md`
  already state the selected owner split.
- No poset constructor or method changed in this decision-only update. The linked
  research card records `just --justfile category_specs/justfile smoke-file
  posets/smoketest.sage` passing after the constructor/certificate fixes in commit
  `c74860e`.

## Affected Tracker Items

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES/tasks/TASK-01KQN9J3X3Y3S80FYCGEQDEJJZ-FIX-POSETS-CONSTRUCTOR-REFINEMENT-RICHCMP-FAILURES.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES/tasks/TASK-01KQN9YGCFADA7QY26RA2KSVX3-IMPLEMENT-FIXED-BASE-SETPARTITIONS-CONSTRUCTOR-REFINEMENTS-INTO-SETS-PAR.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI.md`
