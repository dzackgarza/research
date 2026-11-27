---
id: PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
trackerStatus:
  type: phase
parents:
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
dependsOn: []
title: Sprint algebra constructor admission and tensor multiplication routing
status: complete
priority: high
description: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
successCriteria:
- The sprint has a bounded set of child tracker items and an explicit scope statement.
- Completion requires each child item to be done or explicitly superseded by a linked
  successor; blocked child cards do not satisfy phase acceptance.
- The sprint closing note records smoke/test commands run and any unresolved blockers.
- Run just smoke-file algebras/smoketest.sage after algebra category initialization
  or constructor changes.
- Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module
  over Modules(R).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
---
# Sprint algebra constructor admission and tensor multiplication routing

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- Original migrated line: `Sprint algebra constructor admission and tensor multiplication routing from category_specs/algebras/docs/TRIAGE.md and category_specs/tensor_algebra_components/docs/MAPPING.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done or explicitly superseded by a
      linked successor; blocked child cards do not satisfy phase acceptance.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Run just smoke-file algebras/smoketest.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes subagent, delegated)

**Gates passed:** G1, G2, G4, G6
**Gates failed:** G3 (partial), G5
**Outcome:** revision-required for dependency corrections; G3 gap noted for human attention

#### G1 — Source Paths: PASS

- Phase card cites `category_specs/algebras/docs/TRIAGE.md` (recoverable via `git show 8d1c21c^:...`) and `category_specs/tensor_algebra_components/docs/MAPPING.md`, plus original migrated line. Both are verifiable.
- All six substantive child tasks carry source provenance. Three cards (TASK-1777748120716, TASK-1777748120751, TASK-01KQN9J3X25735) were originally Gate 1 failures in prior reviews and were reworked to add `SPEC-MAPPING-ALGEBRAS` / `SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS` grounding; the rework is visible in their Review Log sections.
- TASK-WRAPUP (meta-task) lacks explicit source paths but its procedural checklist is self-contained; acceptable for a gatekeeper task.
- No card relies on unresolvable or circular source references.

#### G2 — Exit Criteria Checkability: PASS

- Phase success criteria all map to concrete verifications: bounded child set (7 tasks present, countable), each child done-or-superseded (status fields), smoke commands recorded, specific smoke file run, routing guard checkable by code review.
- Child task criteria are predominantly binary-checkable. The wrapup task has softer criteria ("accurate and up-to-date statuses", "coherent narrative milestone") but these are appropriate for a meta-audit task and can be checked by inspection.
- Guard criteria ("does not weaken smokes", "uses project category vocabulary") are consistently applied and testable via smoke re-runs and code diff review.

#### G3 — Task Inventory Completeness: PARTIAL PASS

- Seven child tasks exist, covering the phase scope: Algebras(ZZ) init fix, constructor routing, tensor component __richcmp__, tensor constructors, nontrivial construction boundary, placeholder/type-leak fixes, and phase wrapup.
- **Gap noted:** The phase Context states "Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations." This obligation appears in the phase Context and in TASK-01KQN9J3X16's Context (line 47) but is **not explicitly owned by any child task's acceptance criteria**. It may be implicitly covered by the constructor routing task (TASK-01KQN9J3X25735), but that task does not name these specific helpers. Recommend either adding an acceptance criterion to TASK-01KQN9J3X25735 or spawning a follow-on task if this work is separately tracked.
- No other orphaned requirements detected.

#### G4 — Scope Containment: PASS

- Phase scope is bounded: algebra constructor admission and tensor multiplication routing.
- Explicit anti-creep guards are present in both the phase and every child task: "Do not route plain-set S.algebra(R) into Algebras(R)", "do not recreate subtree-local TRIAGE.md files", "if execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item".
- The wrapup task is a standard phase-closure meta-task, not scope creep.
- All child tasks address items traceable to the deleted Algebras triage or the tensor mapping surface.

#### G5 — Dependency Correctness: FAIL

Three issues found:

1. **TASK-WRAPUP self-depends (circular).** The wrapup task's `dependsOn` list includes its own ID (`[[TASK-WRAPUP-PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]`). This creates a circular dependency. The self-reference should be removed; the wrapup depends on its six sibling tasks, not on itself.

2. **Missing dependency edge from TASK-01KQN9J3X47WFC to TASK-01KQN9YGCN.** The richcmp task's Work Log (line 69-73) states: "the tensor component constructor frontier was discharged by [[TASK-01KQN9YGCN...]]". This is a substantive dependency — the richcmp smoke passes because the tensor constructor task scoped refinement with `test=False`. The richcmp task should declare `dependsOn: ['[[TASK-01KQN9YGCN...]]']`.

3. **Cross-task dependencies in Work Logs not formalized.** TASK-01KQN9J3X16's Work Log (line 75-78) states work was routed through TASK-01KQN9YGCN. Several tasks reference smoke/validation work done by sibling tasks. While these may be coordination notes rather than hard dependencies, they create ambiguity about execution order. Consider adding `dependsOn` edges where one task's validation evidence depends on another task's code changes.

#### G6 — No Weakening: PASS

- The phase addresses known blockers (Algebras(ZZ) init, DualObjects, constructor admission gaps) without removing or softening existing obligations.
- Three child tasks were Gate 1 failures in prior reviews and were strengthened with proper source grounding — this is a net strengthening of the plan.
- Anti-weakening guards are repeated throughout: "does not weaken smokes or mapping decisions to make failures disappear", "preserve the original source path", "do not recreate subtree-local TRIAGE.md files".
- Smoke test expectations are maintained; cards that passed smoke did so through scoped refinement, not by deleting tests.

#### Summary of Required Actions

| Gate | Action |
|------|--------|
| G3 | Confirm ownership of basis-helper → object-method conversion; add criterion to TASK-01KQN9J3X25735 or create follow-on task |
| G5.1 | Remove self-reference from TASK-WRAPUP's `dependsOn` list |
| G5.2 | Add `dependsOn: ['[[TASK-01KQN9YGCN...]]']` to TASK-01KQN9J3X47WFC |
| G5.3 | Audit cross-task Work Log references and add `dependsOn` edges where validation evidence depends on sibling code changes |

#### Child Task Status Summary (observed 2026-05-07)

| Task | Status | Review State |
|------|--------|-------------|
| TASK-01KQN9J3X16 (Algebras(ZZ) init) | needs-human-input | Prior re-review passed G1-6 |
| TASK-01KQN9J3X25735 (constructor routing) | needs-human-input | Prior re-review passed G1-6 |
| TASK-01KQN9J3X47WFC (richcmp) | needs-human-input | Prior re-review passed G1-6; G5 dep missing |
| TASK-01KQN9YGCN (tensor constructors) | complete | Prior review passed; smoke recorded |
| TASK-1777748120716 (nontrivial construction) | needs-human-input | Prior re-review passed G1-6 |
| TASK-1777748120751 (placeholder/type leaks) | needs-human-input | Prior re-review passed G1-6 |
| TASK-WRAPUP | unstarted | G5 self-dep issue; blocked on siblings |

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-07: 6-gate protocol review by Hermes subagent. G3 partial (basis-helper ownership gap), G5 fail (wrapup self-dep, missing richcmp→tensor-constructors edge, informalized cross-task deps). G1, G2, G4, G6 pass. See Review Log above.
