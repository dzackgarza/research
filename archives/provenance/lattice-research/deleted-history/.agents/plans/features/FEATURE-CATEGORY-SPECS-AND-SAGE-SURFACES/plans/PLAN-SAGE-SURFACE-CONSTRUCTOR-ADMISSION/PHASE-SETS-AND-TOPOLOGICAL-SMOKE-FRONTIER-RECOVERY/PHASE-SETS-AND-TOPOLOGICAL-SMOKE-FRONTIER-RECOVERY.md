---
id: PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
trackerStatus:
  type: phase
parents:
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
dependsOn: []
title: Sprint set and topological smoke frontier recovery for root containment rich
  comparison Primes iteration RealSet ambient methods and topological axiom warning
status: in-progress
priority: high
description: The deleted Sets triage recorded the mapped enumeration smoke surface
  and current failures for containment, rich comparison, Primes iteration, RealSet
  element construction, and topological axiom resolution.
successCriteria:
- The sprint has a bounded set of child tracker items and an explicit scope statement.
- Completion requires each child item to be done or explicitly superseded by a linked
  successor; blocked child cards do not satisfy phase acceptance.
- The sprint closing note records smoke/test commands run and any unresolved blockers.
- Run just smoke-file sets/smoketest.sage after set constructor or comparison changes.
- Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback
  helper names.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
---
# Sprint set and topological smoke frontier recovery for root containment rich comparison Primes iteration RealSet ambient methods and topological axiom warning

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

The deleted Sets triage recorded the mapped enumeration smoke surface and current
failures for containment, rich comparison, Primes iteration, RealSet element
construction, and topological axiom resolution.

## Source Provenance

- `category_specs/sets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/sets/docs/TRIAGE.md`.
- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Sprint set and topological smoke frontier recovery for root containment rich comparison Primes iteration RealSet ambient methods and topological axiom warning from category_specs/sets/docs/TRIAGE.md and category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- sets/smoketest.sage uses indexed access, rank, iteration, cardinality, and Python conversion protocols rather than Sage first/next/unrank/list/tuple helpers.
- ZZ in Sets() currently fails at the root containment statement.
- Most refined set constructors expose missing __richcmp__; Primes() exposes missing __iter__.
- RealSet interval input exposes missing _element_constructor_.
- SetPartitions(s) maps to Sets().Partitioned(), while SetPartitions() remains countable-only because it lacks a fixed powerset ambient.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done or explicitly superseded by a
      linked successor; blocked child cards do not satisfy phase acceptance.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Run just smoke-file sets/smoketest.sage after set constructor or comparison changes.
- [ ] Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback helper names.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

## 6-Gate Protocol Review Log

### Review - 2026-05-07 (subagent, 6-gate phase card review)

**Phase card**: PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY  
**Parent plan**: PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION  
**Reviewer**: fresh-context subagent (Hermes Agent, deepseek-v4-pro)  
**Method**: 6-gate protocol (G1 source grounding, G2 exit criteria checkable, G3 task inventory complete, G4 no scope creep, G5 deps correct, G6 no weakening)

---

#### G1 — Source Grounding: PASS

- Source Provenance section cites specific git commits (`8d1c21c`) with exact recovery commands: `git show 8d1c21c^:category_specs/sets/docs/TRIAGE.md` and `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line preserved for traceability: "Sprint set and topological smoke frontier recovery..."
- Sprint Grounding Requirements section establishes authoritative sourcing rules for child cards: canonical source path, exact definition, owner category, hypotheses, codomain/return object, and proof/Sage-evidence obligations.
- Context section grounds five specific technical problems: root containment (`ZZ in Sets()`), `__richcmp__` on refined constructors, `__iter__` on `Primes()`, `_element_constructor_` on RealSet, and `SetPartitions` ambient routing.
- Dependencies and Boundaries section anchors provenance to `SAGE_INVENTORY.md` and `MAPPING.md`, explicitly forbidding subtree-local `TRIAGE.md` recreation.

**Verdict**: Source grounding is thorough. Every claim is traceable to a canonical path or git artifact.

---

#### G2 — Exit Criteria Checkable: PASS (with notes)

Frontmatter successCriteria (5 items):

1. "The sprint has a bounded set of child tracker items and an explicit scope statement." — **Checkable**: count children via filesystem listing (6 substantive tasks + 1 wrapup). Scope statement exists in description and Summary lines.
2. "Completion requires each child item to be done or explicitly superseded by a linked successor..." — **Checkable**: audit child card statuses in trackerStatus frontmatter. Current state: 2 complete, 4 needs-human-input, 1 unstarted (wrapup).
3. "The sprint closing note records smoke/test commands run and any unresolved blockers." — **Checkable**: verify presence of closing note in Work Log or wrapup task Research Log.
4. "Run just smoke-file sets/smoketest.sage after set constructor or comparison changes." — **Checkable**: verify command recorded in work logs.
5. "Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback helper names." — **Checkable**: cross-reference child card implementation notes against Sage fallback names.

**Notes**:
- The phase card does not enumerate its children in frontmatter or body. Child discovery requires filesystem listing of the `tasks/` directory. This is an auditability gap — a `children:` or `tasks:` frontmatter field would make exit criteria verification direct rather than inferential.
- Criteria 1-3 are phase-management (meta) criteria. Criteria 4-5 are technical. Both sets are verifiable but require cross-referencing child cards.

**Verdict**: Criteria are substantively checkable. Minor auditability improvement suggested.

---

#### G3 — Task Inventory Complete: PASS

Child tasks discovered in `tasks/` directory:

| # | Task ID (short) | Status | Review State |
|---|----------------|--------|-------------|
| 1 | TASK-01KQN9J3X04...FIX-SETS-ROOT-CONTAINMENT | `needs-human-input` | Parent review 2026-05-06 passed G1-6 |
| 2 | TASK-01KQN9YGCHDR...IMPLEMENT-TOPOLOGICAL-RING | `needs-human-input` | Parent review 2026-05-06 passed G1-6 |
| 3 | TASK-01KQN9YGCR3D...RESEARCH-SAGE-PRIMES | `needs-human-input` | Re-reviewed 2026-05-06, G1-6 passed |
| 4 | TASK-1777748120612...REMOVE-STRICT-SUPERCATEGORY | `needs-human-input` | Parent review 2026-05-06 passed G1-6 |
| 5 | TASK-01KQN9YGCD23...IMPLEMENT-REALSET-NAMED | `complete` | Independent review 2026-05-07, all 6 gates passed |
| 6 | TASK-01KQN9YGCE6E...IMPLEMENT-IMAGESETS | `complete` | Independent review 2026-05-07, all 6 gates passed |
| 7 | TASK-WRAPUP-PHASE-SETS | `unstarted` | Depends on tasks 1-6 (and self) |

**Coverage mapping** (phase description problem areas → child tasks):
- Containment → Task 1 (root containment), Task 4 (supercategory leaks)
- Rich comparison → Task 1 (`__richcmp__`)
- Primes iteration → Task 1 (`__iter__`), Task 3 (research version skew)
- RealSet element construction → Task 1, Task 5 (named constructors, ambient recovery)
- Topological axiom resolution → Task 1 (warning decision), Task 2 (ring/field refinements), Task 5 (ambient route)
- ImageSets → Task 4 (leak removal), Task 6 (construction, ambient/lift/retract)

**Verdict**: All five problem domains have at least one dedicated child task. No orphaned scope.

---

#### G4 — No Scope Creep: PASS

- Description scope: "containment, rich comparison, Primes iteration, RealSet element construction, and topological axiom resolution" — all covered by child tasks.
- Dependencies and Boundaries explicitly limit scope: no `TRIAGE.md` recreation, no patching around missing owners, preserve original source paths.
- Sprint Grounding Requirements prevent child cards from expanding scope without proper grounding.
- No cross-phase work claimed. The phase is bounded to Sets and Topological Spaces smoke frontier recovery.
- The one scope question — literal `diagram-set`/`schematic-set` surfaces — is handled by Task 4's negative finding, which documents those labels as stale and scopes work to image-subobject/real-subset constructors only.

**Verdict**: Scope is well-bounded and matches the stated description.

---

#### G5 — Dependencies Correct: PARTIAL PASS

**Correct**:
- Phase frontmatter `parents: ['[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]']` — correct parent plan reference.
- All child tasks have `parents: ['[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]']` — correct.
- Wrapup task `dependsOn` lists all 6 substantive child tasks — correct ordering constraint; wrapup must not execute until substantive tasks are done.

**Issues found**:

1. **Phase frontmatter `dependsOn: []` is empty.** The phase card does not formally declare that it depends on its children being complete. While the wrapup task enforces this via its dependsOn, the phase card itself should express this constraint. The empty list means an automated tracker could mark the phase complete without checking child statuses.

2. **Wrapup task self-dependency.** `TASK-WRAPUP-PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY` lists itself in dependsOn (line 14 of wrapup frontmatter). This is a circular dependency. While a planner could resolve it as a no-op, it violates dependency graph cleanliness.

**Recommendation**: 
- Add child task IDs to the phase card's `dependsOn` (or a `children:` field if the tracker schema supports it).
- Remove the self-reference from the wrapup task's dependsOn list.

**Verdict**: Dependencies are logically correct but have two mechanical issues (empty phase dependsOn, wrapup self-reference).

---

#### G6 — No Weakening: PASS

Anti-weakening safeguards in the phase card:

1. Sprint Grounding Requirements: "Before a sprint item changes a spec... its card must cite the canonical source path, exact definition, owner category, hypotheses, codomain/return object, and proof or Sage-evidence obligations."
2. "If a sprint finding lacks that grounding, the sprint action is source mining, decision capture, or splitting into a prerequisite card."
3. "QC and smoke findings identify work, but they do not define the mathematical surface being repaired."
4. Dependencies and Boundaries: "If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it."
5. Success criteria explicitly require preserving mapped enumeration vocabulary and not reintroducing Sage fallback helper names.

**Verification against child tasks**: All child tasks that have been reviewed show evidence of preserving mapping decisions, documenting residual warnings rather than hiding them, and rejecting approaches that would weaken the spec surface (e.g., Task 2's rejected topological-root weakening attempt, Task 1's documented Sage topological-axiom warning decision).

**Verdict**: Strong anti-weakening posture. No evidence of weakening in child task implementations.

---

### Phase Status Assessment

**Current phase status**: `needs-agent-review`

**Assessment**: This status is premature. Only 2 of 6 substantive child tasks are `complete` (Tasks 5 and 6, independently reviewed 2026-05-07). The other 4 are `needs-human-input` — they have passed technical 6-gate review but await human signoff. The wrapup task is `unstarted` and depends on all substantive tasks being done.

**Recommendation**: Phase should be `in-progress` until at minimum all substantive child tasks reach `complete`/`done`/`decided`/`superseded`. The phase card's own success criterion 2 requires "each child item to be done or explicitly superseded."

---

### Summary

| Gate | Result | Notes |
|------|--------|-------|
| G1 Source Grounding | PASS | Concrete git commits and canonical paths cited |
| G2 Exit Criteria Checkable | PASS | Verifiable but children not enumerated in card |
| G3 Task Inventory Complete | PASS | 6 tasks cover all 5 problem domains |
| G4 No Scope Creep | PASS | Bounded to Sets + Topological smoke frontier |
| G5 Dependencies Correct | PARTIAL PASS | Empty phase dependsOn; wrapup self-reference |
| G6 No Weakening | PASS | Strong anti-weakening language, verified in children |

**Blockers for phase completion**: None found. The 4 `needs-human-input` tasks are in valid pending-human-signoff state. The wrapup self-dependency is a cleanliness issue but not a logical blocker.

**Recommended actions**:
1. Add child task enumeration to phase frontmatter (dependsOn or children field).
2. Remove self-reference from TASK-WRAPUP dependsOn list.
3. Change phase status from `needs-agent-review` to `in-progress` until children complete.
4. After all 6 substantive tasks complete, execute wrapup task, then mark phase `complete`.
