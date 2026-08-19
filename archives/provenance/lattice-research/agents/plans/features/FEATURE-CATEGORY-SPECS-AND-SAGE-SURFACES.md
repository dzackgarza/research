---
id: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
trackerStatus:
  type: feature
parents: []
dependsOn: []
plans:
- '[[PLAN-CATEGORY-SPEC-PROGRAM]]'
- '[[PLAN-SPEC-CORE-VERTICAL-SLICE]]'
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
- '[[PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION]]'
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
- '[[PLAN-CATEGORY-OBLIGATION-EXAMPLES]]'
title: Category specs and Sage-grounded operations
status: in-progress
priority: critical
description: 'Specify a Sage-compatible categorical language for downstream research:
  sets, modules, Hom/End/Aut objects, modules with forms, lattices, and preliminary
  geometry interfaces. The goal is a constrained mathematical DSL where later code
  constructs typed objects and morphisms rather than manipulating raw matrices, vectors,
  and equations directly.'
---
# Phase 01 category specs and semantic vocabulary

## Objective

Specify a Sage-compatible categorical language for downstream research: sets, modules,
Hom/End/Aut objects, modules with forms, lattices, and preliminary geometry interfaces.
The goal is a constrained mathematical DSL where later code constructs typed objects and
morphisms rather than manipulating raw matrices, vectors, and equations directly.

## Current Routing Anchor

The active work is governed by `mem:current-goal-handoff`, not by historical plan
names. The live mathematical work is the operation or construction stated in each row:
for each Sage constructor or method under consideration, state the Sage behavior, the
mathematical operation under hypotheses, the weakest category/refinement where that
operation is defined, the witnesses required by that category, the codomain or return
object, and the source evidence. The operation map records those propositions; it is
not itself the mathematical object.

The current concrete target is the lattice Hom/morphism evidence audit around
`FreeModuleHomspace`, `FreeModuleMorphism`, and inherited `MatrixMorphism`, using
`category_specs/lattices/docs/SAGE_INVENTORY.md` and `[[SPEC-MAPPING-LATTICES]]`.
Broad plan-taxonomy cleanup, checked-status repair, category-obligation repair, or
QC routing is not progress unless it adds or corrects a theorem-shaped claim about the
current Hom/morphism operations or fixes a false steering claim in an entrypoint.

## Definition Grounding Control

Approved plans and migrated cards are routing artifacts, not mathematical definition
authority. Before any spec edit changes a mathematical category, method, predicate,
constructor, invariant, Hom/End/Aut object, or mapping decision, the executing card
must record:

- the canonical source path or reference;
- the exact definition and owner category;
- the hypotheses under which the definition is valid;
- the codomain or return object;
- proof obligations for choice-independence or equivalence with another notion.

If that grounding is missing, the next action is source mining, a decision card, or a
split prerequisite, not speculative spec editing. This hard stop is local to the
affected leaf; it does not block other approved phase-01 spec leaves.

## Current Plan Groups

The plan IDs below are historical tracker addresses. Treat terms such as "source map",
"admission", "surface", and "audit" in those IDs as stale labels unless the row or card
states a mathematical operation, hypotheses, category/refinement membership, witnesses,
return object, and source evidence.

- `PLAN-SPEC-CORE-VERTICAL-SLICE`: prior finite/countable free finite-rank module
  witness slice.
- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`: historical shell for source-backed
  mathematical operation rows. It is not definition authority by itself.
- `PLAN-CATEGORY-FOUNDATION-KERNEL` and `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`: core
  category vocabulary. Read the latter as work on `Hom_C(X,Y)`, `End_C(X)`, and
  `Aut_C(X) = End_C(X)^\times`, not as Autset machinery.
- `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` and `PLAN-CATEGORY-OBLIGATION-EXAMPLES`:
  category-owned constructor definitions and representative examples asserting
  category obligations.
- `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` and the geometry feature plans:
  cross-feature spec-phase dependencies.

The connected plan spine is `GOAL.md` -> `.agents/current-goal-phase.md` -> active feature plans; active phase-01 tasks are contained by phase cards under their owning plans.

Reopened 2026-05-10 on the Hom/End/Aut path after runtime auditing showed that the
current generic `HomCategory.parent_class` chain does not inherit Sage's concrete
`sage.categories.homset.Homset` parent methods even though `SPEC-MAPPING-HOMSETS`
records `domain()`, `codomain()`, `identity()`, and `is_endomorphism_set()` as
Sage-backed generic homset behavior. Follow-up now lives under the Hom/End/Aut plan
and the linked ownership decision.

## Current Acceptance Questions

Historical exit checkboxes were not sufficient evidence for this still-active feature.
Do not use a checked plan, review log, or completed source-mining task as completion
evidence unless the underlying mathematical claim is visible and current.

- Does the operation map state the needed lattice Hom/morphism operations under
  hypotheses, with weakest category/refinement, witnesses, return object, and source
  evidence?
- Do Hom/End/Aut specs state `Hom_C(X,Y)`, `End_C(X)`, and
  `Aut_C(X) = End_C(X)^\times` as category objects before discussing representation
  machinery?
- Do category-owned constructors state their mathematical construction, input
  hypotheses, codomain object, witness data, and Sage implementation?
- Do representative examples assert category obligations rather than generic liveness?
- Are unresolved claims recorded as missing definitions, missing source evidence,
  missing implementation, wrong weakest-category claims, or invalid assertions?
