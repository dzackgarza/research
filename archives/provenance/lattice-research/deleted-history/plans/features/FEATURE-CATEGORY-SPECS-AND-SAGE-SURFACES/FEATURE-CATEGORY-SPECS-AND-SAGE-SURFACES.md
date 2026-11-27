---
id: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
trackerStatus:
  type: feature
parents: []
dependsOn: []
plans:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
- '[[PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION]]'
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
- '[[PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION]]'
title: Category specs and Sage surface admission
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

## Definition Grounding Control

Approved plans and migrated cards are routing artifacts, not mathematical definition
authority. Before any spec edit changes a mathematical category, method, predicate,
constructor, invariant, Hom/End/Aut surface, or mapping decision, the executing card
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

- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`: Sage/source mapping and admission discipline.
- `PLAN-CATEGORY-FOUNDATION-KERNEL` and `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`: core category vocabulary and ownership; static refinement-order policy lives in the `category-framework-design` skill and source-backed child cards.
- `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` and `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`: constructor admission, smoke triage, and audit stabilization.
- `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` and the geometry feature plans: cross-feature spec-phase dependencies.

The connected plan spine is `GOAL.md` -> `.agents/current-goal-phase.md` -> active feature plans; active phase-01 tasks are contained by phase cards under their owning plans.

## Exit criteria

- [ ] Core categorical vocabulary is specified enough to express later implementation cards.
- [ ] Lattice specs can state Picard, discriminant, isometry, Hom, End, Aut, base-change, and morphism semantics without raw matrix fallbacks.
- [ ] Active mathematical spec leaves either contain a definition-grounding record or
  are explicitly blocked/split on the missing source, decision, or proof obligation.
- [ ] Backend/source gaps are filed as research cards rather than hidden inside implementation work.
- [ ] Future phase plans have enough prerequisites to block premature downstream work.
