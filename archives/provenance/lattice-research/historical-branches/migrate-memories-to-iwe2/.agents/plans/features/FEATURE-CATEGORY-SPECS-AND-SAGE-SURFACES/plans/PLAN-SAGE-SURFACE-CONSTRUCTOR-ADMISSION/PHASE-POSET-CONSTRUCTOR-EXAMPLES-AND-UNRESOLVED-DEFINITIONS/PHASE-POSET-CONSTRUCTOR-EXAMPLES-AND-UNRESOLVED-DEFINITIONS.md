---
id: PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS
trackerStatus:
  type: phase
parents:
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
dependsOn:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
title: Poset constructor examples and unresolved definitions for graph polytope
  algebra polynomial and Coxeter operations
status: in-progress
priority: high
description: Posets mapping owns constructor names, finite methods, certificate method
  split, unresolved non-core operation definitions, and slice/coslice structure methods.
successCriteria:
- The sprint has a bounded set of child tracker items and an explicit scope statement.
- Completion requires each child item to be done or explicitly superseded by a linked
  successor; blocked child cards do not satisfy phase acceptance.
- The sprint closing note records category-obligation-example/test commands run and any
  unresolved blockers.
- When closing unresolved operation mapping, place each method by target mathematical
  object or display/interop status.
- Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
---
# Poset constructor examples and unresolved definitions for graph polytope algebra polynomial and Coxeter operations

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
definition, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC findings and failed category
assertions identify work, but they do not define the mathematical operation being
repaired.

## Summary

Posets mapping owns constructor names, finite methods, certificate method split,
unresolved non-core operation definitions, and slice/coslice structure methods.

## Source Provenance

- `category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Sprint poset constructor category-obligation example and deferred surface ownership pass for graph polytope algebra polynomial and Coxeter surfaces from category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter
  operations are unresolved mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done or explicitly superseded by a
      linked successor; blocked child cards do not satisfy phase acceptance.
- [ ] The sprint closing note records category-obligation-example/test commands run and any unresolved blockers.
- [ ] When closing unresolved operation mapping, place each method by target mathematical object or display/interop status.
- [ ] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

## 6-Gate Protocol Review Log

### Review Date: 2026-05-07

### Child Task Inventory (6 items)

| # | Task ID | Title | Status |
|---|---------|-------|--------|
| 1 | TASK-01KQN9J3X3Y3S80FYCGEQDEJJZ | Fix Posets constructor refinement __richcmp__ failures | complete |
| 2 | TASK-01KQN9YGCS8P5BYN15M4NKCWCF | Research local Sage poset import failure and import-level category introspection | revision-required |
| 3 | TASK-01KQN9YGCPGDG2XCR55YCTXR53 | Implement poset certificate methods as separate witness-returning methods | complete |
| 4 | TASK-01KQN9YGCFADA7QY26RA2KSVX3 | Implement fixed-base SetPartitions constructor refinements into Sets().Partitioned() | complete |
| 5 | TASK-01KQN9YGCG1916T40B7XTZX9MH | Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs | needs-human-input |
| 6 | TASK-WRAPUP-PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS | Phase wrap-up — planning cleanup, skill updates, and card status audit | unstarted |

#### Status Assessment
4 of 6 child tasks are complete (tasks 1, 3, 4 have Review Logs with concrete category-obligation example/test evidence).
Task 2 is `revision-required` (blocker: stale Sage evidence claim corrected in 2026-05-07 refresh; card awaits re-review).
Task 5 is `needs-human-input` (blocker: implementation done, reviews passed, awaiting human approval to close).
Task 6 (wrapup) is `unstarted` because it depends on tasks 2 and 5 which are not yet done.
Phase cannot satisfy its own success criterion 2 ("each child item to be done or explicitly superseded") until tasks 2 and 5 resolve.

---

### G1 — Source Grounding: PARTIAL PASS

**What passes:**
- The card's "Sprint Grounding Requirements" section correctly requires child items to cite canonical source paths, exact definitions, owner categories, hypotheses, codomain/return objects, and proof/Sage-evidence obligations before changing any surface.
- The card cites `category_specs/posets/docs/MAPPING.md` as source provenance, which anchors the poset constructor/certificate work (tasks 1, 2, 3).

**What needs attention:**
- The phase also contains set-partition work (tasks 4, 5) whose canonical source is `category_specs/sets/docs/MAPPING.md` and `SPEC-MAPPING-SETS.md`. The phase card's Source Provenance does not cite these sets mapping sources.
- The downstream deferred-surface mapping spec `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7-MAP-POSET-DEFERRED-...` lists this phase as a `dependsOn`, but the phase card body does not reference or hand off to this spec.

**Recommendation:** Add `category_specs/sets/docs/MAPPING.md` and `SPEC-MAPPING-SETS.md` to the Source Provenance section, or explicitly state that set-partition child tasks carry their own source grounding. Document the handoff to the deferred-surface mapping spec.

---

### G2 — Exit Criteria Checkability: PASS

All 5 success criteria are binary verifiable:

| Criterion | Checkability | Current Status |
|-----------|-------------|----------------|
| 1. Bounded set of child tracker items + explicit scope statement | Count children + verify scope description exists | 6 children present; scope statement in "Description" frontmatter and "Summary" body section |
| 2. Each child done or superseded; blocked children do not satisfy | Check each child status | Blocked: tasks 2 (revision-required) and 5 (needs-human-input) are not done |
| 3. Closing note records category-obligation example/test commands + unresolved blockers | Verify closing note exists | Not yet applicable (phase not closed); wrapup task 6 will produce this |
| 4. Deferred surface mapping: each method placed by target object or display/interop status | Verify deferred spec resolved | Handoff to `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7` exists (see task 3 review log), but not documented in phase body |
| 5. Order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary | Code/docs audit | Task 3 review log confirms this is maintained |

No criteria are vague or unmeasurable. All five can be objectively confirmed or denied.

---

### G3 — Task Inventory Completeness: PARTIAL PASS

**Covered by child tasks:**
- Poset constructor refinement/richcmp fixes: Task 1 (complete, with category-obligation example validation)
- Certificate method split (boolean predicates → separate witness methods): Task 3 (complete, with category-obligation example validation)
- Fixed-base SetPartitions constructor refinements: Task 4 (complete, with category-obligation example validation)
- Partition refinement/coarsening finite-set methods: Task 5 (implemented, needs-human-input)
- Local Sage import/category introspection research: Task 2 (needs revision)
- Phase cleanup and meta-review: Task 6 (wrapup, unstarted)

**Partially covered or ambiguous:**
- "Deferred non-core surface ownership" (description line 13): The deferred surfaces (graph, polytope, order-complex, algebra, polynomial, Coxeter, display) are mapped in downstream spec `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7` which depends on this phase. The phase does not have its own deferred-mapping task — it treats this as an output handoff. Task 3's review log references this spec. This is acceptable architecture but should be documented in the phase body.
- "Slice/coslice structure methods" (description line 13, context line 44 in task 3): These are mentioned as using `structure_poset` and `structure_map` but there is no dedicated implementation task. They appear to be deferred to the same downstream spec or to future work. If intentionally deferred, this should be stated.

**Recommendation:** Document the deferred-surface handoff to `SPEC-01KQN9YGC9K980Y33NVZSTP4Z7` in the phase body. Clarify whether slice/coslice methods are within this phase's scope or deferred.

---

### G4 — No Scope Creep: MINOR FAIL

**Issue: Set-partition tasks live under a poset-titled phase.**

Tasks 4 and 5 implement set-partition constructor refinements under `Sets().Partitioned()` and cite `category_specs/sets/docs/MAPPING.md` as their source. The phase title and description frame this as poset constructor-example work ("Posets mapping owns..."). The parent plan `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` does cover both sets and posets as workstreams, but set-partition work more naturally belongs under `PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES`.

Mitigating factors:
- Partition refinement is a poset operation (the refinement order forms a poset).
- Tasks 4 and 5 were likely inherited from the original triage migration that spanned both posets and sets.
- The phase card's "Context" section (line 51) does mention "Boolean predicates remain boolean; certificate variants become separately named certificate methods" but does not mention set-partition scope.

**Recommendation:** Either (a) add explicit scope justification in the phase body acknowledging the cross-domain set-partition work and its relationship to poset refinement order, or (b) move tasks 4 and 5 to a sets-focused phase. Option (a) is simpler and justified.

---

### G5 — Dependency Correctness: MINOR FAIL

**What is correct:**
- Phase card `dependsOn: []` — correct; phases are leaf containers under their plan.
- Phase parent: `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` — correct.
- Task 6 (wrapup) depends on all 5 sibling tasks — correct wrapup pattern.
- Tasks 1, 2, 3 are independent of each other — correct (constructor fixes, certificate split, and research are orthogonal).

**What needs attention:**
- Task 5 (partition refinements/coarsenings) builds on the partitioned-set category infrastructure that task 4 (fixed-base SetPartitions constructor) implements. Task 5's `ElementMethods` live on `Sets().Partitioned()` and `Sets().Partitioned().FiniteTotallyOrderedBase()` — categories whose refinement dispatch is centralized by task 4. A `dependsOn` edge from task 5 → task 4 is warranted.
- Task 5's work log references `DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` as resolving a path-local blocker. The task was blocked awaiting that decision. The decision card should be listed as a dependency or at minimum noted in the task's `dependsOn` (if the decision was prerequisite).

**Recommendation:** Add `dependsOn: [[TASK-01KQN9YGCFADA7QY26RA2KSVX3-...]]` to task 5. Consider adding the decision card to task 5's `dependsOn` as a historical record of the blocking prerequisite.

---

### G6 — No Weakening: PASS

**Evidence of standards maintenance:**
- Success criterion 2 explicitly rejects blocked children: "blocked child cards do not satisfy phase acceptance."
- Success criterion 5 enforces vocabulary discipline: "Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary."
- Task 1 review log (2026-05-07): A stale category-obligation example fixture was found and repaired without weakening project-surface assertions. The repair used the public project constructor `Posets().Constructors().from_upper_covers_dict(...)` while preserving `raw_diamond_poset()` for Sage interop testing.
- Task 3 review log: Certificate split preserves boolean predicates; Sage's `certificate=True` behavior is delegated to separately named witness-returning methods. No boolean predicate was altered or removed.
- Task 5: Method shadowing was resolved by adding project-specific method names (`refinement_set()`, `coarsening_set()`, `ordered_coarsening_closure()`) rather than monkeypatching Sage's concrete methods.
- Phase grounding requirements (lines 28-37) explicitly prevent weakening by requiring canonical source citation and forbidding category-obligation example-driven spec relaxation.

No child task shows evidence of weakening specifications, reducing category-obligation example coverage, or relaxing mapping decisions to make failures disappear.

---

### Summary

| Gate | Verdict | Action Required |
|------|---------|-----------------|
| G1 Source Grounding | PARTIAL PASS | Add sets mapping sources to phase provenance; document deferred-spec handoff |
| G2 Exit Criteria Checkability | PASS | None — all criteria are binary verifiable |
| G3 Task Inventory Complete | PARTIAL PASS | Document deferred-surface handoff to SPEC; clarify slice/coslice scope |
| G4 No Scope Creep | MINOR FAIL | Justify or relocate set-partition tasks; add cross-domain acknowledgment to phase body |
| G5 Dependencies Correct | MINOR FAIL | Add task 5 → task 4 dependency edge |
| G6 No Weakening | PASS | None — standards are maintained throughout |

**Phase readiness:** NOT READY FOR CLOSURE. Two child tasks are incomplete (revision-required, needs-human-input) and three gates have findings requiring attention before the phase can satisfy its own success criteria.
