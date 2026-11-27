---
id: TASK-STATIC-REFINEMENT-FIX-PLAN-HYGIENE
trackerStatus:
  type: task
parents:
- '[[PHASE-STATIC-REFINEMENT-AUDITS]]'
dependsOn: []
title: Fix plan hygiene issues from 6-gate review
status: complete
priority: high
description: 'Apply the non-audit fixes recommended by the 6-gate review: remove dead
  source reference, deduplicate criteria, clarify scope statement, declare soft dependency.'
successCriteria:
- Dead source reference `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  is removed from the source corpus section.
- The duplicate between frontmatter successCriteria and body acceptance criteria is
  resolved (keep one, remove the other, or give them distinct roles).
- The scope statement clarifies whether the admitted-edges table is exhaustive or
  a designated subset, with the remainder explicitly deferred to decision cards.
- A `dependsOn` edge to `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` is added if constructor-interception
  enforcement requires it, or the body explains why the implicit dependency is sufficient.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
- PHASE-STATIC-REFINEMENT-AUDITS
---
# Fix plan hygiene issues from 6-gate review

## Summary

The 6-gate review found four non-audit issues that can be fixed independently
of the super_categories audit work.

## Actions

### 1. Remove dead source reference

The source corpus lists `.agents/skills/lattice-redesign/references/category-abc-spec.md`
which does not exist on disk. Remove it from the Source corpus section.

### 2. Deduplicate criteria

The frontmatter `successCriteria` and body `## Acceptance Criteria` are identical
text (3 items each). Options:
- Remove the body Acceptance Criteria and keep only frontmatter successCriteria
- Keep both but give the body version a distinct role (e.g., verification steps)
- Remove the frontmatter duplicate

The review recommends differentiation. The simplest fix: keep the frontmatter
`successCriteria` as the canonical list, remove the body duplicate, and add a
verification section to the body that describes how each criterion is checked.

### 3. Clarify scope

The admitted-edges table says "Future work may add edges" implying it is NOT
exhaustive, but success criterion #1 demands exhaustive coverage. Add a scope
statement that resolves this: either commit to exhaustive coverage or define
which category subtrees are in scope with the rest deferred.

### 4. Declare soft dependency

The constructor-interception order section references constructor refinement
targets that live under PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION. Either add
a `dependsOn` edge or document why the implicit dependency is sufficient.
