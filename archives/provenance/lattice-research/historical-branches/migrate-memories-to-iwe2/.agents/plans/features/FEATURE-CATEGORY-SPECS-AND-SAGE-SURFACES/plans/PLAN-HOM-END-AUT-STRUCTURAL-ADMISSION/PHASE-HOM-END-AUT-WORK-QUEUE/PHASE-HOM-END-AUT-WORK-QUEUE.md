---
id: PHASE-HOM-END-AUT-WORK-QUEUE
trackerStatus:
  type: phase
parents:
- '[[PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION]]'
dependsOn: []
title: Hom End Aut work queue
status: in-progress
description: 'This phase groups current cards that were previously attached directly
  to `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` or to the corresponding legacy `.agents`
  work queue. It is a routing phase: executable work remains in child task cards,
  while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete only after blockers are resolved, or after the original
  card is superseded by a linked successor that remains active; blocked child cards
  do not satisfy phase acceptance.
- Any mathematical spec changes cite their source grounding before implementation
  proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tasks:
- '[[TASK-01KQN9J3WWCX4AA36TK4QVCNBK-FIX-CAT-CATEGORY-OBLIGATION-HOM-END-AUT-OBJECTSOVER-OBJECTSUNDER-AND-WITHFORMS-FRONTIE]]'
- '[[TASK-1777748120385-RRVDIG-REMOVE-RAW-CONDITIONSET-FROM-PUBLIC-AUT-CATEGORY-SURFACE]]'
- '[[TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME]]'
- '[[TASK-WRAPUP-PHASE-HOM-END-AUT-WORK-QUEUE]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
---
# Hom End Aut work queue

## Summary

This phase groups current cards that were previously attached directly to `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

Reopened 2026-05-10 after QC/runtime tracing established that the generic
`HomCategory` parent-method owner chain is not currently aligned with the
source-grounded Sage `Homset` / `Homsets.ParentMethods` surface recorded in
`SPEC-MAPPING-HOMSETS`. The new follow-up card fixes that owner mismatch before any
remaining Hom/End/Aut override failures are attributed to plugin debt.

Current routing: `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME` is
human-gated after source/doc review. Runtime MRO validation must be rerun after the
Sage `ImportError: cannot import name Category` gap is resolved; full `just test`
remains non-diagnostic for this leaf while parallel mypy-plugin work is active.

## Acceptance Criteria

- [ ] Child task cards are complete only after blockers are resolved, or after the
      original card is superseded by a linked successor that remains active; blocked
      child cards do not satisfy phase acceptance.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Phase-Card Review)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Exit Criteria, Gate 3 Task Inventory, Gate 4 Scope, Gate 6 Acceptance-Criteria Preservation
**Gates passed with finding:** Gate 5 Dependencies (one child self-reference)
**Outcome:** phase-card is well-formed; one dependency edge in TASK-WRAPUP needs correction before phase closure

---

#### Gate 1: Definition Grounding (source paths grounded)

**Verdict:** PASS with note.

The phase card is a routing phase — it does not itself declare source anchors (its `dependsOn` is empty, its body contains no category-theoretic definitions). This is consistent with its stated role: "executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards."

Source grounding is inherited from the parent plan `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`, which fully grounds itself against:
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/MAPPING.md`

Each child task card also individually grounds its work:
- TASK-1777748120385 (Remove raw ConditionSet): anchors to homsets/cat/modules/forms/lattices MAPPING.md files, plus SPEC-MAPPING-HOMSETS.md
- TASK-01KQN9J3W... (Fix Cat category-obligation example): anchors to cat MAPPING.md, SAGE_INVENTORY.md, forms subcategories, modules MAPPING.md
- TASK-WRAPUP: process card, no mathematical grounding needed

**Recommendation:** None. The phase correctly delegates grounding to parent and children.

#### Gate 2: Exit Criteria (checkability of success criteria)

**Verdict:** PASS.

The three success criteria are operationally checkable:

1. "Child task cards are complete only after blockers are resolved, or after the original card is superseded by a linked successor that remains active; blocked child cards do not satisfy phase acceptance."
   - **Checkability:** Direct status inspection of child cards. Current state: TASK-01KQN9J3W... is `complete`, TASK-1777748120385 is `needs-human-input` (one AC unchecked: "Human review accepts the implementation and closes the card"), TASK-WRAPUP is `unstarted`.
   - **Blocked children check:** No child is currently `blocked`. The criterion's blocked-child guard is correctly specified.

2. "Any mathematical spec changes cite their source grounding before implementation proceeds."
   - **Checkability:** Verifiable by inspecting any spec files modified during this phase for citation of MAPPING.md or equivalent source documents.

3. "Follow-up work is filed as tracked cards under root `plans/features/`."
   - **Checkability:** File-system search for new tracker cards under `plans/features/` created during or after this phase.

**Recommendation:** None. All criteria are specific, falsifiable, and scoped.

#### Gate 3: Task Inventory (completeness of child task coverage)

**Verdict:** PASS.

Child task inventory (3 cards):

| Card ID | Title | Status | Review State |
|---|---|---|---|
| TASK-01KQN9J3W... | Fix Cat category-obligation example Hom End Aut ObjectsOver... | `complete` | Passed Gates 1-6 (Russell re-review) |
| TASK-1777748120385 | Remove raw ConditionSet from public Aut-category surface | `needs-human-input` | Passed Gates 1-6 (Fermat re-review); await human approval |
| TASK-WRAPUP | Phase wrap-up — planning cleanup, skill updates, card status audit | `unstarted` | Depends on above two |

Coverage assessment:
- The two work tasks cover the phase's core scope: (a) Cat failed category assertions alignment for Hom/End/Aut, ObjectsOver/ObjectsUnder, and WithForms and (b) ConditionSet boundary enforcement on Aut surfaces.
- The wrap-up task provides phase-closure hygiene (status audit, meta-review, skill/memory updates, git milestone notes).
- The parent plan `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` references two additional spec cards (`SPEC-01KQN9J3WJE9W76X72DAT10H4Y` and `SPEC-01KQN9J3WQDJ0Z27BXTY67HA72`) as "Owned existing cards," but these are **downstream dependents** (they list this phase in their `dependsOn`), not children of this phase. This is correct: the plan records them as owned work items; the phase groups only the immediate executable tasks.

No missing tasks detected. The inventory covers the structural Cat failed category assertions, ConditionSet leakage fix, and phase closure.

**Recommendation:** None.

#### Gate 4: Scope (no scope creep)

**Verdict:** PASS.

Each child task stays within declared scope:
- TASK-01KQN9J3W... limits itself to Cat failed category assertions: Homsets/Endsets interop aliases, ObjectsOver/ObjectsUnder dispatch, WithForms PID specialization. Does not expand into functor modeling or natural transformations (which are explicitly deferred in the task body).
- TASK-1777748120385 limits itself to a single file (`category_specs/homsets/autsets.py`): ConditionSet privatization, aut-object surface preservation, @final markers. Does not touch End/Aut beyond the documented contract.
- TASK-WRAPUP is a phase-closure meta-task with a fixed four-step procedure; no implementation work.

The phase card's description explicitly partitions work: "executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards." This boundary is respected.

**Recommendation:** None.

#### Gate 5: Dependencies (correctness of dependency declarations)

**Verdict:** PASS with finding.

Upstream (phase → plan):
- Phase `dependsOn: []` — correct. The phase is a structural child of `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` (listed in the plan's `phases:` field). No cross-phase dependencies needed; this is the only phase under this plan.

Child dependencies (tasks within phase):
- TASK-01KQN9J3W... `dependsOn: []` — correct. No upstream work tasks; is a prerequisite for TASK-WRAPUP.
- TASK-1777748120385 `dependsOn: []` — correct. Independent of the Cat category-obligation example task; shares no code surface.
- TASK-WRAPUP `dependsOn:` lists both work tasks — correct. The wrap-up must not execute until work tasks are finalized.

**Finding (Gate 5):** TASK-WRAPUP lists itself in its own `dependsOn` field:
```yaml
dependsOn:
  - '[[TASK-01KQN9J3W...]]'
  - '[[TASK-1777748120385...]]'
  - '[[TASK-WRAPUP-PHASE-HOM-END-AUT-WORK-QUEUE]]'   # <-- self-reference
```
A task cannot depend on itself. This is a malformed edge that would cause a cycle in any dependency resolver. It does not block phase review (the edge is trivially satisfied/ignorable), but it should be removed before phase closure.

Downstream (spec cards depending on this phase):
- `SPEC-01KQN9YGCA0D25CR40N85EHYZ5` (Review subtree direct Hom methods) `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` — correct. The spec's grounded review outcome references the Cat category-obligation work done in TASK-01KQN9J3W....
- `SPEC-01KQN9J3WJE9W76X72DAT10H4Y` (Dual-object Hom routing) `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` — correct. Dual-object Hom routing through Homsets requires the Hom/End/Aut surface to be stable.
- `SPEC-01KQN9J3WQDJ0Z27BXTY67HA72` (DiscriminantGroup Hom/End/Aut) — located in `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`. The plan DAG confirms `PHASE_HOM_END_AUT_WORK_QUEUE → SPEC_01KQN9J3WQDJ...`. Correct: discriminant-group Hom/End/Aut names should follow the same structural admission patterns established by this phase.

No missing dependency declarations. No undeclared upstream blocking.

**Recommendation:** Remove the self-referential `dependsOn` entry from TASK-WRAPUP-PHASE-HOM-END-AUT-WORK-QUEUE.md before closing this phase.

#### Gate 6: Acceptance-Criteria Preservation (no weakening of feature-level criteria)

**Verdict:** PASS.

Parent plan `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` success criteria:
1. `Aut(X)` and `End(X)` are category-recognized surfaces, not isolated helper factories.
2. Automorphism groups have domain/codomain semantics and categorical coercion to End.
3. Public APIs return project-owned aut/subobject surfaces; Sage `ConditionSet` remains an implementation bridge only.

Phase card success criteria:
1. Child task cards are complete only after blockers are resolved...
2. Any mathematical spec changes cite their source grounding...
3. Follow-up work is filed as tracked cards under root `plans/features/`.

The phase criteria are **operational gates** (process hygiene) layered on top of the plan's mathematical criteria. They do not replace, weaken, or conflict with the plan-level acceptance criteria. The plan's criteria remain the feature-level acceptance targets; the phase criteria govern task-completion discipline.

Child task acceptance criteria also preserve and enforce the plan's criteria:
- TASK-1777748120385 ACs directly implement plan criterion #3 (ConditionSet as implementation bridge).
- TASK-01KQN9J3W... ACs enforce plan criterion #1 (category-recognized Hom/End/Aut surfaces through Cat category-obligation example).

**Recommendation:** None.

---

#### Summary

The phase card is structurally sound for its role as a routing phase under `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`. Two of three child tasks have passed full 6-gate review (one pending only human approval); the wrap-up task is correctly gated behind them. One minor dependency hygiene issue (TASK-WRAPUP self-reference) should be corrected. No scope creep, no weakened acceptance criteria, no missing tasks.
