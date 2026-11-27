---
id: TASK-1777748120816-0ES9M8-FIX-CAT-WRAPPER-TYPING-AND-FINALITY-HOLES
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION]]'
dependsOn: []
title: Fix Cat wrapper typing and finality holes
status: complete
priority: critical
description: Fix Cat wrapper typing and finality holes
successCriteria:
- Concrete Cat wrapper typing/finality holes found in current code are fixed.
- Public Cat option-bag exposure is documented as absent outside private forwarding
  and initialization glue.
- Duplicate active Cat hardening work is consolidated instead of expanding the tracker
  with another parallel implementation path.
- Human review accepts the consolidation and closes or retires the duplicate card.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION
---
# Fix Cat wrapper typing and finality holes
Source: pasted backlog 2026-05-02.

Task: fix Cat wrapper typing (explicit type parameters, correct variance), fill finality holes on concrete Cat subclasses, and excise Sage option bags from the public surface.

## Complexity Justification
- Owner: C70
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Fix Cat wrapper typing and finality holes
- Why this specific score:
  - This item explicitly spans typing semantics (`explicit type parameters`, variance) and class contract enforcement (`@final` gaps) on concrete Cat subclasses, so it touches both static and inheritance behavior in the wrapper layer.
- Item-specific evidence:
  - Multiple coupled remediation vectors are listed in one task, indicating higher coordination than isolated method edits.
  - The coupling to wrapper surfaces justifies the high band because regressions can propagate through consumers of category wrappers.

## Consolidation Result

This card overlaps the already-active Cat hardening card
`plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION/tasks/TASK-1777748120649-EQPN1A-ADD-MISSING-FINAL-MARKERS-AND-RETURN-ANNOTATIONS-ON-CAT-METHODS.md`.
The concrete remaining wrapper holes were fixed there rather than splitting the same
Cat surface across two independent implementation tracks.

Implemented Cat wrapper changes:

- `_CatObjectMixin._make_named_class(...)` now has explicit parameter and return
  annotations and is marked `@final`.
- `_SingletonClasscallMixin.__classcall__(...)` and
  `_SingletonAxiomClasscallMixin.__classcall__(...)` now have explicit `cls` and return
  annotations.
- Public Cat option-bag exposure remains excluded by
  `category_specs/cat/docs/MAPPING.md`: the only live `*args` / `**kwargs` occurrences
  under `category_specs/cat/` are private constructor-forwarding and subclass-init
  plumbing, not mathematical constructor surfaces.

Variance-specific search:

- Searched: this card, the sibling Cat hardening card, `category_specs/cat/docs/MAPPING.md`,
  `category_specs/cat/base_category_types.py`, and textual Cat-surface searches for
  `variance`, `TypeVar`, `ParamSpec`, broad `Callable[..., Any]`, and missing Cat method
  return annotations.
- Found: no documented public Cat wrapper variance contract separate from the concrete
  signature/finality holes fixed in `base_category_types.py`.
- Conclusion: inference - this card is covered by the sibling Cat hardening implementation
  and does not need a separate implementation track unless review identifies a specific
  unresolved generic variance surface.
- Confidence: Medium.
- Gaps: no external type-checker trace naming a variance failure was found in the active
  card text; this is not a fresh full static-type audit of all project type aliases.

## Acceptance Criteria

- [x] Concrete Cat wrapper typing/finality holes found in current code are fixed.
- [x] Public Cat option-bag exposure is documented as absent outside private forwarding
  and initialization glue.
- [x] Duplicate active Cat hardening work is consolidated instead of expanding the
  tracker with another parallel implementation path.
- [ ] Human review accepts the consolidation and closes or retires the duplicate card.

## Review Log

### Review 2026-05-06 (Raman)

**Gates passed:** Gate 1 Definition Grounding
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** human approval gate remains; no agent-local implementation rework found

#### Gate 2 Finding: Acceptance Criteria

- The card's final acceptance criterion requires human review to accept the
  consolidation and close or retire the duplicate card.
- That criterion is intentionally still unchecked, and the sibling Cat hardening card
  remains active in `needs-agent-review`.

#### Routing Note

- This is not an ordinary DAG dependency blocker and does not justify attempting
  downstream work. The card remains in `needs-agent-review` awaiting human acceptance or
  retirement direction.
