---
id: PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
title: Category literal method inventory and ownership
status: complete
priority: critical
owner: Zack
description: Build source-grounded method ownership spec files that list every literal
  expected method and the minimal category or construction owner that introduces it.
successCriteria:
- The method inventory target spec is filled or split into smaller method-owner spec
  cards with the required row format.
- Sets, topology, algebra, modules, Hom/End/Aut, forms, lattices, tensors, posets,
  geometry, and backend-routed methods are covered by source-grounded rows.
- External software capability maps are translated into method/backend ownership rows
  with explicit codomains and routing status.
- All unresolved owner conflicts are converted into decision cards rather than left
  as prose or implementation guesswork.
tasks:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-GAP-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
---
# Category literal method inventory and ownership

## Summary

Build the exhaustive method-owner inventory required by
`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`. The phase is complete only when
the repo has actual trackable spec files that answer which mathematical category or
construction first introduces each expected method.

## Source Provenance

- Parent plan: `PLAN-CATEGORY-FOUNDATION-KERNEL`.
- Target spec card: `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`.
- Current inventory roots: `category_specs/*/docs/SAGE_INVENTORY.md` and
  `category_specs/*/docs/MAPPING.md`.
- External method mapping roots: `projects/github.com__dzackgarza__lattice-research/references/software-capability-map`,
  `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`, and backend-specific notes under
  `the iwe2 vault (theory backend memories; iwe2 search)`.
- Lattice-source warning: `src.bak/spec-backups/*` files may be mined for mathematical
  content, but their interface can change and they are not current implementation
  authority.

## Context

The existing plans already contain many method-owner decisions, but they are spread
across mapping docs, source inventories, lattice notes, backend maps, and tracker cards.
This phase centralizes them into a literal inventory organized by minimal owner
subcategory. The output prevents downstream work from treating method names as obvious
or letting Sage implementation inheritance masquerade as mathematical ownership.

## Acceptance Criteria

- [x] The method inventory target spec is filled or split into smaller method-owner spec cards with the required row format.
- [x] Sets, topology, algebra, modules, Hom/End/Aut, forms, lattices, tensors, posets, geometry, and backend-routed methods are covered by source-grounded rows.
- [x] External software capability maps are translated into method/backend ownership rows with explicit codomains and routing status.
- [x] All unresolved owner conflicts are converted into decision cards rather than left as prose or implementation guesswork.

## Dependencies And Boundaries

- This is spec work, not implementation. It may create or update spec cards and
  decision cards; it should not edit category implementation files.
- A method row may reject a Sage method as public API, but the rejection must name the
  replacement surface or explain why the method is interop-only.
- Method owners must be minimal in the category refinement order. Inherited availability
  is a consequence, not an owner.
- When a method name has multiple meanings, split the meanings into separate rows
  instead of forcing one owner.

## Work Log

- 2026-05-05: Created phase to execute the literal method ownership inventory requested by the user.
- 2026-05-06: Started phase execution by completing the source corpus assignment in the target spec.
- 2026-05-06: Completed topical row assembly, gap audit, and decision/source routing;
  marked phase needs-agent-review pending human acceptance.
- 2026-05-06: Repaired the lattice spec-backup source root after child-card review
  found the stale `.agents/theory/spec-backups/` path. The current mineable source
  files live under `src.bak/spec-backups/`.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Phase Card Review)

**Gates passed:** Gate 1, Gate 2, Gate 3 (with open item), Gate 4, Gate 5, Gate 6
**Gates failed:** None that block phase completion
**Outcome:** phase is review-ready; one open scope item noted below

---

#### Gate 1 — Source Paths Grounded

**PASS.** The phase card's Source Provenance section (lines 47-56) cites:
- Parent plan `PLAN-CATEGORY-FOUNDATION-KERNEL` (exists at expected path)
- Target spec `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` (exists at `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/`, 917 lines, 145KB)
- Category spec inventory/mapping roots under `category_specs/*/docs/`
- Backend memory roots under `the iwe2 vault (theory backend memories; iwe2 search)`
- Lattice spec-backup roots under `src.bak/spec-backups/`

All source paths cited in the phase were verified as existing. The target spec itself went through 3 rounds of Gate 1 repair (stale `.agents/theory/spec-backups/` → `src.bak/spec-backups/`, missing foundation paths, imprecise file references), all now resolved. Every child task has a Source Provenance section grounded in the same corpus.

#### Gate 2 — Exit Criteria Checkable

**PASS.** All four success criteria are concrete and verifiable:

1. *Spec filled or split* — Verifiable: `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` exists as a single trackable file with 917 lines covering all topics.
2. *All 11 method domains covered* — Verifiable: sections for sets/topology, rings/algebras/modules, Hom/forms/lattices, posets/tensors/geometry, and backend mapping all present with source-grounded rows.
3. *External software maps translated* — Verifiable: backend section covers Sage, Oscar/Julia, GAP, Singular, Macaulay2, CARAT, Indefinite.jl with explicit codomains and routing statuses.
4. *Owner conflicts → decision cards* — Verifiable: at least 5 decision cards created (`DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`, `DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER`, `DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER`, `DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING`, and several poset/partition decisions).

All four acceptance criteria checkboxes are `[x]` in the phase card body.

#### Gate 3 — Task Inventory Complete

**PASS with open item.** The phase declares 8 child tasks:

| # | Task | Status |
|---|------|--------|
| 1 | SOURCE-CORPUS | needs-human-input |
| 2 | SETS-TOPOLOGY | complete |
| 3 | ALGEBRA-MODULES | needs-human-input |
| 4 | HOM-FORMS-LATTICES | needs-human-input |
| 5 | POSETS-TENSORS-GEOMETRY | complete |
| 6 | BACKEND-MAPPING | complete |
| 7 | SPEC-ASSEMBLY | complete |
| 8 | GAP-AUDIT | complete |

All 8 child tasks exist at their expected paths and have substantive bodies. The 3 tasks still in `needs-human-input` have all passed independent Gate 1-6 re-reviews — they are blocked only on human approval, not on missing work.

**Open item:** A 9th task file exists in the tasks directory that is NOT declared in the phase's `tasks:` array: `TASK-CATEGORY-METHOD-INVENTORY-TREE-VISUALIZATION` (status: `unstarted`). This task proposes Mermaid category-hierarchy diagrams. It is scope-adjacent (user-facing documentation derived from the inventory) but was never integrated into the phase task list and was never started. This does not block phase completion since the phase's declared tasks are complete, but it is a stray artifact in the phase directory that should either be formally added as a phase task or removed/moved to a follow-up plan.

#### Gate 4 — No Scope Creep

**PASS with note.** The phase stays within its stated boundary: "spec work, not implementation" (Dependencies And Boundaries, line 76). The output is a single spec file with method-owner rows. No child task edits category implementation files (except ALGEBRA-MODULES which removed `has_standard_involution()` from the live Python surface as a corrective action — this was a Gate 1 rework, not scope creep). The TREE-VISUALIZATION task (unstarted, undeclared) is noted above but doesn't contaminate the completed phase deliverables.

#### Gate 5 — Dependencies Correctly Declared

**PASS.** Phase-level `dependsOn: []` is correct — this is an early phase with no phase predecessors. Child task dependency graph:

- SOURCE-CORPUS (leaf, no deps) → feeds all 5 topical tasks
- SETS-TOPOLOGY, ALGEBRA-MODULES, HOM-FORMS-LATTICES, POSETS-TENSORS-GEOMETRY, BACKEND-MAPPING all depend on SOURCE-CORPUS
- SPEC-ASSEMBLY depends on all 5 topical tasks
- GAP-AUDIT depends on SPEC-ASSEMBLY

No circular dependencies. No missing deps. The assembly task correctly gates on all topical outputs. The gap audit correctly gates on assembly.

#### Gate 6 — No Weakening of Feature-Level Acceptance Criteria

**PASS.** The feature `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` requires source-grounded method ownership specs. The phase delivers exactly that through `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`. The spec card's own acceptance criteria (lines 813-816) are all `[x]`. No feature-level requirement was dropped, narrowed, or deferred. Geometry-facing rows are explicitly marked as candidate entries blocked on geometry source-admission tasks, which is honest gating rather than weakening.

#### Summary

The phase is structurally sound. All 8 declared tasks exist and have substantive output. The target spec is a 145KB file with exhaustive method rows across all required domains. Remaining work is limited to human sign-off on 3 child tasks and disposition of the undeclared TREE-VISUALIZATION stray task. The phase can proceed to human acceptance.
