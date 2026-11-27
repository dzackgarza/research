---
id: PLAN-CATEGORY-SPEC-PROGRAM
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Category spec program — spec authorship and subcategory admission workflow
status: complete
priority: critical
owner: Zack
description: 'Govern the overall category-spec authorship workflow: how new category
  surfaces are admitted, how existing Sage methods are mapped to project owners,
  and how subcategory hierarchies are approved. This plan coordinates the spec-writing
  discipline that all child cards must follow.'
phases: []
successCriteria:
- All active spec-writing under this feature follows the spec authorship workflow.
- Spec cards record definition grounding before spec edits.
- Source-mining precedes spec drafting when Sage/backend evidence is needed.
- The subcategory admission criteria are checked before a new spec surface is admitted.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Category spec program — spec authorship and subcategory admission workflow

## Objective

Define and enforce the overall workflow for creating, reviewing, and admitting
category-spec surfaces. This plan is the process authority for spec authorship,
not the mathematical definition authority — those live in the child spec, mapping,
and decision cards under the owning feature.

## Scope

- Spec authorship workflow: how new category surfaces get from research to admitted spec.
- Subcategory admission: what evidence a new subcategory needs before it enters the project surface.
- Spec structure conventions: required sections, grounding requirements, and acceptance criteria format.
- Source-mining workflow: when to mine Sage source, backend docs, or literature before writing a spec surface.
- Review and acceptance gates between spec stages.

## Relationship to other plans

- `PLAN-CATEGORY-FOUNDATION-KERNEL` owns the foundational category vocabulary,
  method ownership, and category refinement order that every spec surface depends on.
- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` owns the Sage source-map and
  admission discipline for concrete constructors.
- `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` owns Hom/End/Aut surface admissions.
- `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` owns constructor admission and
  concrete family specs.
- `PLAN-CATEGORY-OBLIGATION-EXAMPLES` owns category-obligation examples and failed assertions and audit workflows.

This plan provides the meta-workflow that those plans follow. It does not own
executable cards directly; executable spec-writing work lives under the phase/task
trees of the plans listed above.

## Spec authorship workflow

1. **Research phase**: identify source-backed definitions, Sage/mapping evidence,
   backend capability, and unresolved decisions. Output is a research card or TODO entry.
2. **Definition grounding**: record canonical source, exact definition, hypotheses,
   codomain/return object, and proof/equivalence obligations.
3. **Spec drafting**: write the spec surface with required sections (Summary,
   Source Provenance, Context, Acceptance Criteria, Dependencies, Work Log).
4. **Review gate**: apply the 6-gate protocol from the review kernel.
5. **Admission**: spec is accepted by human approval and tracked as complete.

## Subcategory admission criteria

A new subcategory (e.g. `Modules(R).Torsion()`) is admitted only when:

- The mathematical definition and hypotheses are source-grounded (literature, Sage docs, or approved decision card).
- The supercategory chain is explicit and each step is justified.
- The constructor routing (how parents enter this category) is specified.
- The method ownership (which methods become abstract/concrete at this level) is specified.
- At least one category-obligation example or test assertion verifies the category membership chain works.

## Spec structure conventions

Every spec file (`SPEC-*.md`) should include:

- **Summary**: one-paragraph description of what the spec defines.
- **Source Provenance**: paths to SAGE_INVENTORY.md, MAPPING.md, Sage source, or literature.
- **Context**: design decisions, boundary conditions, and relationship to sibling specs.
- **Required Row Format** (for inventory specs): literal surface, object level, minimal owner,
  inherited categories, meaning, hypotheses, codomain, source paths, decision status.
- **Acceptance Criteria**: checkable items that define when the spec is complete.
- **Dependencies And Boundaries**: what this spec depends on and what is out of scope.
- **Work Log**: dated entries recording progress.

## Acceptance Criteria

- [ ] All active spec-writing under this feature follows the spec authorship workflow.
- [ ] Spec cards record definition grounding before spec edits.
- [ ] Source-mining precedes spec drafting when Sage/backend evidence is needed.
- [ ] The subcategory admission criteria are checked before a new spec surface is admitted.

## Source corpus

- `GOAL.md` — overall staged program.
- `.agents/current-goal-phase.md` — active phase marker.
- `.agents/skills/research-state-machine/references/review-kernel.md` — review gate protocol.
- `category_specs/AGENTS.md` — category-spec project invariants.

## Work Log

- 2026-05-07: Created as missing skeleton plan referenced in current-goal-phase.md.
  Sources the spec authorship workflow from existing practice in the feature's child plans.

## 6-Gate Protocol Review Log

### Independent Review - 2026-05-07

**Gates passed:** Gate 1 Source Grounding, Gate 2 Exit Criteria, Gate 3 Task/Phase Inventory, Gate 4 Scope Containment, Gate 5 Dependencies, Gate 6 Preservation

**Gates failed:** none

**Outcome:** complete. All six gates pass.

- **Gate 1 (Source Grounding):** All 4 source corpus files verified on disk: `GOAL.md`, `.agents/current-goal-phase.md`, `.agents/skills/research-state-machine/references/review-kernel.md`, `category_specs/AGENTS.md`. The plan correctly sources its authority from existing repo-level documents.

- **Gate 2 (Exit Criteria):** 4 success criteria are concrete, falsifiable, and appropriate for a meta-workflow plan. They describe process gates (spec authorship workflow, definition grounding, source-mining, subcategory admission checks) that are observable in child card bodies.

- **Gate 3 (Task/Phase Inventory):** Plan explicitly declares `phases: []` and states it "does not own executable cards directly." This is correct — it is a meta-workflow authority, not a task-coordination plan. Executable work lives under the child plans listed in §Relationship.

- **Gate 4 (Scope Containment):** Well-contained to meta-workflow governance. Five scope bullets match the plan body. No implementation, no construction details, no mathematical definitions — appropriate for a process-level plan.

- **Gate 5 (Dependencies):** `dependsOn: []` is correct. The plan references 5 child plans as "related" but does not block on them — those are sibling plans, not prerequisites. Plan is a process authority that sits above them.

- **Gate 6 (Preservation):** No weakening. Plan adds governance without deleting or narrowing existing obligations. The spec structure conventions align with observed card formats across the feature tree.

Verification: all source corpus files confirmed present. Plan structure follows repo conventions. No issues found.
