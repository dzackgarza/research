---
id: PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
dependsOn:
- '[[PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION]]'
title: Sprint module wrapper migration phase one through category graph constructor
  routing method coverage and deletion gates
status: complete
priority: critical
description: 'The deleted module wrapper migration plan is a phased migration contract:
  map methods first, define the category graph, rewrite constructors, move methods
  to real owners, then delete wrappers.'
successCriteria:
- The sprint has a bounded set of child tracker items and an explicit scope statement.
- Completion requires each child item to be done or explicitly superseded by a linked
  successor; blocked child cards do not satisfy phase acceptance.
- The sprint closing note records category-obligation example/test commands run and any unresolved blockers.
- Use the phase-specific validation commands from the deleted plan when implementing
  a child item.
- Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
---
# Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and category-obligation example findings identify work, but
they do not define the mathematical surface being repaired.

Every child card in this phase must reread `category-spec-style` just in time before
editing a module spec or method surface. The local task must preserve the ideal
mathematical interface inside Sage's category/object universe: current Sage coverage
is not the adequacy standard, Sage interop remains a design constraint where
mathematically appropriate, Sage method presence is evidence for mapping and
feasibility, Sage method absence is implementation-gap evidence, and category-obligation example progress is
never a reason to delete or weaken a spec obligation.

Before advancing this phase or any child task, review the staged diff, unstaged diff,
and any commits created during the work for spec weakening. In particular, check for
deleted abstract methods, removed constructor/category obligations, narrowed category-obligation example
assertions, or moved method owners without source-grounded replacement owners.

Before implementing a method move in this phase, perform a mathematical review of the
proposed owner. The review must state the caller object, required data, hypotheses,
construction or predicate, and codomain/result in ordinary mathematical language.
Rows copied from Sage inventory or mapping tables do not pass unless that statement is
coherent independently of the source-map wording.

## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done or explicitly superseded by a
      linked successor; blocked child cards do not satisfy phase acceptance.
- [ ] Each child item that edits module specs or method surfaces states how the ideal
      interface obligation is preserved when Sage category-obligation examples fail.
- [ ] The sprint closing note records category-obligation example/test commands run and any unresolved blockers.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Phase Card Review)

**Gates passed:** G1, G2, G3, G4, G6
**Gates passed with findings:** G5
**Gates failed:** None
**Outcome:** PASS WITH FINDINGS (see G5 note below)

---

#### G1 — Source Grounding: PASS

- Source provenance is explicitly recorded: lines 67-68 cite the deleted
  `SAGE_WRAPPER_MIGRATION_PLAN.md` with the exact git recovery command
  (`git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`).
- The "Sprint Grounding Requirements" section (lines 31-46) imposes a rigorous
  grounding contract on every child card: canonical source path, exact definition,
  owner category, hypotheses, codomain/return object, and proof/Sage-evidence
  obligations must be cited before any spec or method-surface edit.
- References `category-spec-style` (verified as a canonical skill in
  `category_specs/AGENTS.md`), `modules/docs/MAPPING.md`, and the deleted migration
  plan — all exist and are reachable.
- The card correctly self-identifies as a coordination/sprint card, not a definition
  authority, delegating source grounding to child tasks.

#### G2 — Exit Criteria Checkable: PASS

All success/acceptance criteria are specific and independently verifiable:

| # | Criterion | Verification method |
|---|-----------|-------------------|
| 1 | Bounded set of child items + explicit scope statement | Count task children under phase directory; read scope statement |
| 2 | Each child done or superseded by linked successor | Check child card statuses and dependsOn edges |
| 3 | Child items editing specs state how ideal interface is preserved when category-obligation examples fail | Spot-check child card bodies for ideal-interface preservation statements |
| 4 | Sprint closing note records category-obligation example/test commands and unresolved blockers | Verify closing note exists in card body or wrap-up task |
| 5 | Use phase-specific validation commands from deleted plan | Recover deleted plan via `git show`; verify commands cited in child work logs |
| 6 | Parent not closed until MAPPING.md has no unmapped wrapper methods | Scan MAPPING.md for unmapped entries |

One minor concern: criterion 5 depends on git history being intact to recover the
deleted plan. The recovery command is provided, so this is a recoverable reference
rather than a lost artifact. Acceptable for phase-level criteria.

#### G3 — Task Inventory Complete: PASS

The phase has 4 child tasks covering the required migration phases:

1. **TASK-01KQN9J3X5APK7MNNH5N1W5XW5** — Fix forms category-obligation exampletest / confirm forms owner identity (status: `needs-human-input`)
2. **TASK-01KQXXWCG8P47C9ZVPFBWJF640** — Ground root module abstract-method ownership (status: `complete`)
3. **TASK-01KQN9YGCMD0K84CK3BKZH0Z8Z** — Implement module category graph phase (status: `complete`)
4. **TASK-WRAPUP** — Phase wrap-up, card status audit, meta-review (status: `unstarted`)

Coverage against the migration contract (map methods → define category graph →
rewrite constructors → move methods → delete wrappers):

- Method mapping/ownership grounding: covered by Task 2 and its linked spec
  `SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING`
- Category graph definition: covered by Task 3
- Constructor routing: covered by Task 3 (work log records constructor exposure fixes)
- Method moves: covered by Tasks 2 and 3 (is_submodule_of moved, modify_module_structure
  rejected with decision grounding)
- Forms owner identity: covered by Task 1
- Wrapper deletion: mentioned in description as final step but no dedicated child
  task exists. This is deferred to downstream — the phase card description says
  "Wrapper deletion comes last and requires references to deleted wrappers to
  disappear." The phase AC "no unmapped wrapper methods in MAPPING.md" gates
  this implicitly. Acceptable for phase scope.

The wrap-up task is correctly `unstarted` since Task 1 (forms) is still
`needs-human-input`. The phase status `in-progress` is accurate.

#### G4 — No Scope Creep: PASS

- The scope statement (line 13) is explicit: "phased migration contract: map methods
  first, define the category graph, rewrite constructors, move methods to real owners,
  then delete wrappers."
- "Dependencies And Boundaries" (lines 90-93) enforces: keep SAGE_INVENTORY.md and
  MAPPING.md as provenance, do not create subtree-local TRIAGE.md files, split
  missing owners/constructors/category-graph edges as new items.
- The child tasks honor these boundaries: Task 3's work log documents 7 cross-subtree
  gap items that are **routed to downstream features** rather than locally patched.
  Task 2's work log shows ambiguous surfaces became decision cards
  (`DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES`) rather than
  speculative code.
- No evidence of extraneous work or boundary violations.

#### G5 — Dependencies Correct: PASS WITH FINDINGS

**Phase-level dependencies:**
- `parents`: `PLAN-CATEGORY-FOUNDATION-KERNEL` — verified, the plan lists this phase
  (line 24).
- `dependsOn`: `[]` — the parent plan lists 3 phases without explicit ordering
  constraints between them. Empty dependsOn is plausible if phases operate on
  disjoint surfaces. The plan's acceptance criteria (constructor-interception work
  must not precede category hierarchy review) is honored by child task ordering
  within this phase, not inter-phase dependencies.

**Child task dependency chain:**
```
TASK-...640 (method owners)
  dependsOn: [SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]
  blocks: [TASK-...8Z]

TASK-...8Z (category graph)
  dependsOn: [TASK-...640]  ← correctly blocked by method-owner grounding

TASK-...5W5 (forms)
  dependsOn: []  ← independent; forms owner was pre-decided

TASK-WRAPUP
  dependsOn: [TASK-...5W5, TASK-...8Z, TASK-...640, TASK-WRAPUP]
```

**Finding — Self-referential dependency in TASK-WRAPUP:** The wrap-up task lists
itself in its own `dependsOn` array. This creates a circular dependency that would
prevent any automated dependency resolver from unblocking it. Since the wrap-up task
is designed to run after all sibling tasks complete, listing itself as a dependency
is incorrect.

**Severity:** Low. The self-dependency is harmless in practice (a human reviewer
would ignore it), but it violates clean dependency graph hygiene.

**Recommendation:** Remove `TASK-WRAPUP-PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE`
from the dependsOn list in the wrap-up task's frontmatter.

#### G6 — No Weakening: PASS

The phase card contains exceptionally strong anti-weakening guards:

- Lines 48-51: Explicit spec-weakening review gate before phase advancement —
  check staged diff, unstaged diff, and commits for deleted abstract methods,
  removed constructor/category obligations, narrowed category assertions, or Sage-gap-driven
  interface shrinkage.
- Lines 53-57: Mathematical review requirement before method moves — must state
  caller object, required data, hypotheses, construction/predicate, and codomain/result
  in ordinary mathematical language. Sage inventory rows alone do not pass.
- Line 46: "category-obligation example progress is never a reason to delete or weaken a spec obligation."
- Lines 41-45: Sage method absence is implementation-gap evidence, Sage method
  presence is mapping/feasibility evidence — neither justifies weakening.

The child tasks demonstrate compliance: Task 3's only abstract-method removal
(modify_module_structure) is grounded in an approved decision card. Task 2
redirected from pattern-matching to proper mathematical review after catching
an invalid owner-table draft.

No weakening signals detected in the phase card or its language.

---

#### Summary

The phase card passes all 6 gates. One finding (G5): the TASK-WRAPUP child has a
self-referential `dependsOn` entry that should be cleaned up. This does not block
phase advancement but should be corrected before the phase closes.

**Child task status at review time:**
- complete: 2 (TASK-...640, TASK-...8Z)
- needs-human-input: 1 (TASK-...5W5)
- unstarted: 1 (TASK-WRAPUP)

Phase cannot close until TASK-...5W5 receives human approval and TASK-WRAPUP executes.
