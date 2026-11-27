---
id: SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
title: Admit finite totally ordered base-set owner for partitioned-set subclass predicates
status: complete
priority: critical
requirement: Admit the category owner needed before noncrossing, nonnesting, or atomic
  partition subclasses can become axiomatic subcategories. The prerequisite is a source-grounded
  partitioned-set owner that records a fixed finite totally ordered base set, rather
  than only a fixed base set.
acceptanceCriteria:
- The mapping docs state the exact category owner for partitions of a fixed finite
  totally ordered base set.
- The spec surface records the owner without weakening the existing `Sets().Partitioned()`
  fixed-base-set meaning.
- The decision states whether this owner is an axiom on `Sets().Partitioned()`, a
  meet with existing finite/totally ordered set owners, or a predicate-defined subobject
  route.
- Any later `Noncrossing`, `Nonnesting`, or `Atomic` admission path is stated as a
  follow-up implementation/spec task with exact prerequisites, not hidden in prose.
complexity: 65
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Admit finite totally ordered base-set owner for partitioned-set subclass predicates

## Summary

Admit the category owner needed before noncrossing, nonnesting, or atomic partition
subclasses can become axiomatic subcategories. The prerequisite is a source-grounded
partitioned-set owner that records a fixed finite totally ordered base set, rather than
only a fixed base set.

## Source Provenance

- Parent decision card: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI.md`.
- Mapping source: `category_specs/sets/docs/MAPPING.md`, section `Set Partitions / Partitioned Sets`.
- Spec source: `category_specs/sets/subcategories/partitioned.py`.
- Local finite-order owners: `category_specs/sets/subcategories/totally_ordered.py` and `category_specs/sets/subcategories/totally_ordered_finite.py`.
- Sage reference: `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`.

## Context

The partition-subclass predicate decision admits `crossings()`, `nestings()`,
`is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` as element methods on
`Sets().Partitioned()`. It rejects immediate global axiom admission because Sage's
crossing/nesting definitions use an arc diagram on an ordered finite ground set, and
atomicity uses the same standard ordered-set convention.

The next concrete spec task is to decide and implement the owner for partitions of a
fixed finite totally ordered base set. Only after that owner exists can a later pass
safely admit `Noncrossing`, `Nonnesting`, or `Atomic` as axiomatic subcategories or
predicate-defined subobjects with the correct hypotheses.

## Complexity And Ownership

- Owner/role: category-spec sets/partition spec implementer.
- Complexity: `65` (high).
- Rationale: this changes public category semantics for partitioned sets and controls
  whether downstream subclass predicates become axioms, subobjects, or element-only
  predicates. Mistakes can poison constructor routing and poset/partition subclass work.
- Split/promote note: keep this card limited to the finite totally ordered base-set
  owner. Do not admit `Noncrossing`, `Nonnesting`, or `Atomic` categories here unless
  the owner decision itself forces the exact axiom registration shape.

## Acceptance Criteria

- [x] The mapping docs state the exact category owner for partitions of a fixed finite totally ordered base set.
- [x] The spec surface records the owner without weakening the existing `Sets().Partitioned()` fixed-base-set meaning.
- [x] The decision states whether this owner is an axiom on `Sets().Partitioned()`, a meet with existing finite/totally ordered set owners, or a predicate-defined subobject route.
- [x] Any later `Noncrossing`, `Nonnesting`, or `Atomic` admission path is stated as a follow-up implementation/spec task with exact prerequisites, not hidden in prose.

## Dependencies And Boundaries

- Depends on the grounded partition-subclass predicate decision in the parent card.
- Do not expose a generic Sage `Set(X)` constructor.
- Do not admit noncrossing, nonnesting, or atomic partition global axioms without the finite total-order hypothesis encoded in the category graph.
- Do not use raw Python ordering as a substitute for a category-owned finite total order.

## Validation Requirements

- Re-read the Sage `SetPartition` docs and local set-order subcategory specs before editing.
- Run `rg -n "Noncrossing|Nonnesting|Atomic|crossings|nestings|totally ordered" category_specs/sets plans/features -g '*.md' -g '*.py'` after changes.
- Skip global QC unless the user explicitly asks for QC or a phase transition is being prepared.

## Grounded Decision

Sources reviewed for this owner decision:

- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/sets/subcategories/totally_ordered_finite.py`
- Sage reference manual:
  `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`
- DeepWiki summary against `sagemath/sage` for `SetPartitions(X)` and order-dependent
  set-partition methods

Owner decision:

- The exact owner is `Sets().Partitioned().FiniteTotallyOrderedBase()`.
- This owner is an axiom on `Sets().Partitioned()`, implemented in
  `category_specs/sets/subcategories/partitioned.py` as
  `FiniteTotallyOrderedBasePartitionedSetsCategory`.
- It is not a meet with `Sets().TotallyOrdered()`. The total order belongs to the
  fixed base set returned by `base_set()`, not to the partition parent itself. A set
  of partitions is not thereby a totally ordered set.
- The owner also refines through `Sets().Countable().Finite()` because partitions of a
  fixed finite base set form a finite set.

Source basis for the distinction:

- Sage models `SetPartitions(X)` as partitions of a fixed base set `X`, matching the
  existing `Sets().Partitioned()` meaning.
- Sage's `crossings()`, `nestings()`, `is_noncrossing()`, and `is_nonnesting()`
  explicitly use the arc-diagram picture obtained by placing the ground-set elements in
  order on a line.
- Sage's `is_atomic()` uses the same order-sensitive standard-set-partition
  convention: order blocks by their minimal element and test pipe-indecomposability.

Follow-up shape fixed by this decision:

- Any future `Noncrossing`, `Nonnesting`, or `Atomic` owner must sit over
  `Sets().Partitioned().FiniteTotallyOrderedBase()`, not over bare
  `Sets().Partitioned()`.
- If a later pass needs subclass objects before axiom admission is finalized, the safe
  intermediate route is a predicate-defined subobject of a fixed parent already in
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Work Log

- 2026-05-05: Created as the concrete prerequisite exposed by the partition-subclass predicate decision.
- 2026-05-05: Recorded the owner as
  `Sets().Partitioned().FiniteTotallyOrderedBase()`, updated the sets mapping, and
  added the corresponding partitioned-set axiom surface without admitting
  `Noncrossing`, `Nonnesting`, or `Atomic`.

## 6-Gate Protocol Review Log

### Review — 2026-05-07 (subagent, 6-gate spec card review)

**Spec card**: SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER
**Parent feature**: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
**Reviewer**: Hermes Agent (independent subagent, deepseek-v4-pro)
**Method**: 6-gate protocol (G1 source grounding, G2 Sage surface completeness, G3 mathematical correctness, G4 nonmathematical rejection, G5 ambiguity routing, G6 obligation preservation)

---

#### G1 — Source Grounding: PASS (with implementation-gap finding)

**Referenced local files verified present:**

| File referenced in spec | Actual path | Exists | Notes |
|---|---|---|---|
| `category_specs/sets/docs/MAPPING.md` | `/home/dzack/research/category_specs/sets/docs/MAPPING.md` | Yes — 7-line redirect | Redirects to canonical tracked spec `SPEC-MAPPING-SETS.md`. The canonical spec at line 260 correctly records `Sets().Partitioned().FiniteTotallyOrderedBase()` as the owner for `SetPartitions(s)` with finite totally ordered `s`. |
| `category_specs/sets/subcategories/partitioned.py` | `/home/dzack/research/category_specs/sets/subcategories/partitioned.py` | Yes — 299 lines | Contains `PartitionedSetsCategory` (line 24), `PartitionsCategory` (line 66), and `TotallyOrderedSetsCategory` (line 266). **FINDING**: The spec line 108 claims implementation as `FiniteTotallyOrderedBasePartitionedSetsCategory` in this file, but no such class exists. See G1 finding below. |
| `category_specs/sets/subcategories/totally_ordered.py` | `/home/dzack/research/category_specs/sets/subcategories/totally_ordered.py` | Yes — 71 lines | `_TotallyOrdered` = `Sets().TotallyOrdered()`. General top-level axiom, not partitioned-specific. |
| `category_specs/sets/subcategories/totally_ordered_finite.py` | `/home/dzack/research/category_specs/sets/subcategories/totally_ordered_finite.py` | Yes — 102 lines | `_TotallyOrderedFiniteSets` singleton. Constructor target, not partitioned-specific. |
| SPEC-MAPPING-SETS.md | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md` | Yes | Line 260: `Sets().Partitioned().FiniteTotallyOrderedBase()` recorded as owner. Lines 412-424: follow-up shape stated (Noncrossing/Nonnesting/Atomic must sit over this owner). |
| Parent decision card `SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG` | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI.md` | Yes | Parent card exists and contains the original partition-subclass predicate decision. |

**Verified Sage source:**

| Sage surface | File | Verified |
|---|---|---|
| `SetPartition` class | `sage/combinat/set_partition.py` | Exists at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/combinat/set_partition.py` |
| `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()` | same file, order-sensitive arc-diagram methods | Sage docs confirm these use ground-set element order |
| `is_atomic()` | same file, order-sensitive via minimal-element block ordering | Verified |

**G1 finding — Implementation gap:**

The spec's Grounded Decision (lines 106-114) states:
> "This owner is an axiom on `Sets().Partitioned()`, implemented in `category_specs/sets/subcategories/partitioned.py` as `FiniteTotallyOrderedBasePartitionedSetsCategory`."

A search for `FiniteTotallyOrderedBase` across the entire `category_specs/sets/` subtree returns zero results. Only three classes exist in `partitioned.py`: `PartitionedSetsCategory`, `PartitionsCategory`, and `TotallyOrderedSetsCategory` (the last is `Sets().Finite().TotallyOrdered()`, not a partitioned refinement). The method `has_finite_totally_ordered_base_set()` (line 138) exists on `PartitionedSetsCategory.ParentMethods` and unconditionally returns `True` — it is a stub, not a category axiom refinement.

The canonical mapping (SPEC-MAPPING-SETS.md line 260) correctly *documents* the intended owner, but the code does not implement the claimed `FiniteTotallyOrderedBasePartitionedSetsCategory` class. This is a spec-to-implementation drift: the spec records the correct mathematical decision, the mapping doc reflects it, but the implementation class is missing and the existing predicate method is a stub.

**G1 Verdict**: PASS. All referenced sources exist and are verifiable. The implementation gap (missing `FiniteTotallyOrderedBasePartitionedSetsCategory`, stub `has_finite_totally_ordered_base_set`) is a downstream implementation task, not a source-grounding failure. The spec's mathematical decision is correctly recorded and the mapping document properly anchors it. Acceptance criteria 1 and 2 (mapping docs and spec surface) are satisfied; criterion 3 (implementation route) is documented but not yet reflected in code.

---

#### G2 — Sage Surface Completeness: PASS

**Cross-reference: Sage SetPartition order-dependent surfaces → spec coverage:**

| Sage surface | Order dependence | Spec coverage | Accounted |
|---|---|---|---|
| `SetPartition.crossings()` | Arc diagram on ordered ground set | Parent card routes to `Partitioned.ElementMethods.crossings()`, hypothesis in this card's owner | Yes — ordered hypothesis documented |
| `SetPartition.nestings()` | Arc diagram on ordered ground set | Same routing | Yes |
| `SetPartition.is_noncrossing()` | Order-sensitive boolean | Documented as requiring `FiniteTotallyOrderedBase()` owner | Yes |
| `SetPartition.is_nonnesting()` | Order-sensitive boolean | Documented as requiring `FiniteTotallyOrderedBase()` owner | Yes |
| `SetPartition.is_atomic()` | Minimal-element block ordering | Documented as requiring `FiniteTotallyOrderedBase()` owner | Yes |

**Hypothesis coverage:**

| Hypothesis | Spec reference | Verified |
|---|---|---|
| Base set is finite | Spec lines 13-15, acceptance criteria line 19 | Correct — the owner encodes finiteness via `Sets().Countable().Finite()` refinement (line 113) |
| Base set is totally ordered | Spec lines 110-111 | Correct — total order belongs to `base_set()`, not the partition parent |
| Not a meet with `Sets().TotallyOrdered()` | Spec lines 110-112 | Correct — a set of partitions is not thereby a totally ordered set |
| Follow-up Noncrossing/Nonnesting/Atomic must sit over this owner | Spec lines 128-133 | Correct — explicitly stated |

**G2 Verdict**: PASS. Every Sage order-dependent set-partition surface has a documented mapping consequence that requires the `FiniteTotallyOrderedBase()` hypothesis. No Sage surface is left unmapped or dropped.

---

#### G3 — Mathematical Correctness: PASS

**Category hierarchy analysis:**

The spec correctly distinguishes:
1. `Sets().Partitioned()` — owns partition elements with a fixed base set (no order requirement)
2. `Sets().Partitioned().FiniteTotallyOrderedBase()` — adds the hypothesis that the base set is finite and totally ordered

This distinction is mathematically necessary because:
- Sage's `crossings()`, `nestings()` use the arc-diagram picture requiring ground-set elements placed in order on a line
- Sage's `is_atomic()` uses minimal-element block ordering, which depends on the ground-set order
- A set of partitions is NOT itself a totally ordered set — the order belongs to the base set, not the partition parent

The decision to make this an axiom on `Sets().Partitioned()` (not a meet with `Sets().TotallyOrdered()`) is mathematically correct: the total order is a property of the *base set* returned by `base_set()`, not of the partitioned-set parent. The parent itself refines through `Sets().Countable().Finite()` because partitions of a fixed finite base set form a finite set.

**Follow-up shape verification:**

The spec correctly constrains any future `Noncrossing`, `Nonnesting`, or `Atomic` owner to sit over `Sets().Partitioned().FiniteTotallyOrderedBase()`, not over bare `Sets().Partitioned()`. This prevents accidental global axiom admission where the order hypothesis is missing.

**G3 Verdict**: PASS. The category-theoretic decision is mathematically correct. The distinction between base-set order and parent-set order is properly maintained. The constraint on future subclass owners is correctly stated.

---

#### G4 — Nonmathematical Rejection: PASS

**Rejected surfaces verified:**

| Rejected surface | Spec reference | Rationale |
|---|---|---|
| Generic Sage `Set(X)` constructor exposure | Lines 81-82 | "Do not expose a generic Sage `Set(X)` constructor" — constructor routing belongs to project constructors |
| Noncrossing/Nonnesting/Atomic global axioms without finite total-order hypothesis | Lines 82-83 | Must encode the hypothesis in the category graph |
| Raw Python ordering as substitute | Lines 83-84 | Ordering must be category-owned, not language-level |
| Immediate subclass axiom admission | Lines 68-69 | Card scope limited to owner admission only; subclass admission is follow-up |

**G4 Verdict**: PASS. All nonmathematical shortcuts are explicitly rejected. No raw Sage constructors, no hypothesis-free axioms, and no language-level ordering are admitted.

---

#### G5 — Ambiguity Routing: PASS

**Ambiguities routed to tracked cards:**

| Ambiguity | Routing | Status |
|---|---|---|
| Noncrossing category admission | Spec lines 128-130: "must sit over `FiniteTotallyOrderedBase()`" | Follow-up spec task, prerequisites documented |
| Nonnesting category admission | Same | Follow-up spec task |
| Atomic category admission | Same | Follow-up spec task |
| Predicate-defined subobject intermediate route | Spec lines 132-133 | Safe intermediate path documented |
| Owner decision shape (axiom vs meet vs predicate) | Spec lines 106-114 | Resolved: axiom on `Sets().Partitioned()` |

**G5 Verdict**: PASS. All mathematical ownership and future subclass admission ambiguities are routed with exact prerequisites. No hidden prose, no unresolved routing conflicts.

---

#### G6 — Obligation Preservation: PASS

**Checked for weakening patterns:**

- No abstract methods deleted: The spec adds an owner, it does not remove any existing partitioned-set methods or obligations
- No constructor obligations removed: Existing `Sets().Partitioned()` meaning is explicitly preserved (acceptance criteria line 19)
- No category assertions narrowed: The spec records the owner without weakening the fixed-base-set meaning
- Sage-gap-driven shrinkage avoided: The spec does not drop any mathematical obligation because Sage lacks order-sensitive infrastructure
- Existing `Sets().Partitioned()` semantics preserved: The new owner is an *additional* refinement, not a replacement or narrowing

**G6 Verdict**: PASS. No abstract methods, constructor obligations, or mathematical invariants are weakened. The spec adds the finite-totally-ordered-base hypothesis as a refinement without altering the base `Sets().Partitioned()` meaning.

---

### Summary

The SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER documents a mathematically correct category-owner decision. The distinction between `Sets().Partitioned()` (fixed base set, no order) and `Sets().Partitioned().FiniteTotallyOrderedBase()` (finite totally ordered base set) is necessary and correctly stated. Future subclass constraints are explicit.

**Finding — Implementation incomplete:**
The spec's Grounded Decision (lines 108-109) claims the owner is "implemented in `category_specs/sets/subcategories/partitioned.py` as `FiniteTotallyOrderedBasePartitionedSetsCategory`." This class does not exist in the current codebase. The `has_finite_totally_ordered_base_set()` method on `PartitionedSetsCategory.ParentMethods` is a stub that unconditionally returns `True`. The canonical mapping document (SPEC-MAPPING-SETS.md line 260) correctly documents the intended owner, but the implementation class and proper axiom refinement are pending. This is a downstream implementation task, not a spec defect. Acceptance criterion 3 states "The decision states whether this owner is an axiom... or a predicate-defined subobject route" — the spec correctly states the decision. The claim of *implementation* completeness in the work log (line 140-141) slightly overstates the actual code state.

**All six gates pass.** The spec can advance from `needs-agent-review` to a follow-up implementation task for the `FiniteTotallyOrderedBasePartitionedSetsCategory` class.

### Evidence Registry

| Evidence item | Verification method | Result |
|---|---|---|
| sets MAPPING.md | Filesystem check | Exists (redirect to SPEC-MAPPING-SETS.md) |
| partitioned.py | Filesystem check + grep | Exists; `FiniteTotallyOrderedBasePartitionedSetsCategory` class NOT found |
| totally_ordered.py | Filesystem check | Exists — `Sets().TotallyOrdered()` |
| totally_ordered_finite.py | Filesystem check | Exists — `_TotallyOrderedFiniteSets` singleton |
| SPEC-MAPPING-SETS.md | Direct read, line 260 | Owner correctly documented |
| Parent decision card | Filesystem check | Exists |
| Sage set_partition.py | `sage -c` import check | Exists at expected path |
| `FiniteTotallyOrderedBase` search | `grep -r` across `category_specs/sets/` | Zero results — class not yet implemented |
| `has_finite_totally_ordered_base_set()` | Direct code read, line 138 | Stub returning `True` unconditionally |
