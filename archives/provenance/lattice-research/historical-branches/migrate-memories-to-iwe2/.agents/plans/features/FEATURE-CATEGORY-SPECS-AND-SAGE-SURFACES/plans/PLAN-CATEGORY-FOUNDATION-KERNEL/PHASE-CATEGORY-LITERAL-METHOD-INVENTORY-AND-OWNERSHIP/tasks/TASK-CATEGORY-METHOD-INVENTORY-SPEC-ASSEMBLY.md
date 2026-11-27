---
id: TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING]]'
title: Assemble trackable method ownership spec files
status: complete
priority: critical
owner: Zack
description: Assemble the topical method rows into one or more trackable spec files
  with consistent table schema, cross-links, and no duplicated source authority.
successCriteria:
- The repository contains the final method ownership spec file or a linked family
  of method ownership spec files under the tracker hierarchy.
- All topical inventory rows use the same schema and cite source paths.
- Duplicate method names with distinct meanings are split into separate rows, and
  overloaded names state their hypotheses and codomains.
- The assembled spec links follow-up implementation, audit, category-obligation example, or decision cards
  without creating meta-planning tasks.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Assemble trackable method ownership spec files

## Summary

Assemble the topical method rows into the durable trackable spec artifact requested by
the user. This card is complete only when the output is actual method-owner spec
content, not a list of future cards.

## Source Provenance

- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`
- Topical outputs from the sibling inventory tasks in this phase.
- Existing spec cards under
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/` when they already
  own a local method-owner decision.

## Context

The assembly pass should decide whether the inventory remains in
`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` or is split into multiple spec cards
such as sets/topology, algebra/modules, Hom/forms/lattices, posets/tensors, and backend
routing. Splitting is allowed only when it improves readability and each split file is a
real spec surface with method rows.

## Complexity And Ownership

- Owner/role: category-spec integration editor.
- Complexity: `80` (high).
- Rationale: this integrates high-risk semantic rows across subtrees but remains
  bounded to spec-file assembly and tracker cross-linking.
- Split/promote note: do not promote this into another plan. If the content is too
  large, split the spec files, not the workflow.

## Acceptance Criteria

- [x] The repository contains the final method ownership spec file or a linked family of method ownership spec files under the tracker hierarchy.
- [x] All topical inventory rows use the same schema and cite source paths.
- [x] Duplicate method names with distinct meanings are split into separate rows, and overloaded names state their hypotheses and codomains.
- [x] The assembled spec links follow-up implementation, audit, category-obligation example, or decision cards without creating meta-planning tasks.

## Dependencies And Boundaries

- Do not replace source docs with summaries; the method inventory points to canonical
  source paths and records decisions.
- Do not create cards whose only purpose is "record grounding" unless the actual work is
  source mining for an unresolved method owner.
- Do not close the phase if any topical table is only represented by prose.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete/done

#### Evidence

**Gate 1 — Definition Grounding:**
- All definitions trace to SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY, which records source paths for every method row.
- The task does not introduce new definitions; it assembles grounded rows from 4 dependency tasks (sets/topology, algebra/modules, Hom/forms/lattices, posets/tensors, backend mapping).
- Source-provenance section cites the canonical corpus: SAGE_INVENTORY.md, MAPPING.md, backend notes under `the iwe2 vault (theory backend memories; iwe2 search)`, and spec-backup source material.

**Gate 2 — Acceptance Criteria:**
- [x] Repository contains the final method ownership spec file → SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md exists at the spec path with 917 lines of method rows, source maps, and gap routing.
- [x] All rows use the same schema → spec defines a 9-field row format (literal surface, object level, minimal owner, inherited categories, meaning, hypotheses, codomain, source paths, status) used consistently.
- [x] Duplicate names with distinct meanings are split → separate rows for `dual()` (metric dual, Hom dual), `tensor()` (generic, finite-rank-free), and `form()` (bilinear vs quadratic) with explicit hypotheses.
- [x] Assembled spec links follow-up cards → gap-audit routing table links to 8 geometry source-admission tasks, 5 decision cards, and backend research cards.

**Gate 3 — Spec-Weakening:**
- No staged or unstaged diffs on the target spec file (`git diff --cached` and `git diff` both empty).
- The task creates new spec content; it does not modify existing spec obligations.
- Seed method surfaces are preserved as lower bounds for implementation, not narrowed.

**Gate 4 — Gradient:**
- `git log` for the target spec shows only additive commits adding method rows and review logs.
- No decision cards are contradicted: the assembly follows DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES (rejected malformed names), DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING (handles RealSet axiom), and DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER (separate Picard surfaces).
- No previously passing tests or category-obligation examples are regressed (no code changes).

**Gate 5 — Mathematical Correctness:**
- Method owners are stated as minimal categories with explicit hypotheses and codomains.
- The gap-audit section flags geometry/Picard/lattice ownership as unresolved and routes to decision or source-admission cards rather than guessing owners.
- The spec does not claim implementation permission for ungrounded rows.

**Gate 6 — Style and Compliance:**
- Markdown spec with consistent table schema; no raw ConditionSet, variadic option bags, or AI-slop patterns.
- Conventional Commit message on assembly commits is present.
- `just plan-validate` passes (225 cards).

#### Residual Risks
- Method rows for geometry-facing surfaces remain candidate entries pending source-admission task completion; this is explicitly tracked in the gap-audit routing table.
- The spec is large (145KB, 917 lines); future splits may be warranted but are outside this task's scope.

---

## Work Log

- 2026-05-05: Created as the spec assembly leaf for the literal method ownership inventory phase.
- 2026-05-06: Kept the method inventory assembled in
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` as one trackable spec file,
  added an assembly index with the normalized row schema and follow-up links, and moved
  this task to needs-agent-review. The separate gap-audit leaf remains responsible for
  auditing decision-needed, backend-gap, and source-needed rows.
