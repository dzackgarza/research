---
trackerStatus:
  type: plan
title: Phase 01 category specs and semantic vocabulary
status: approved
planId: PLN-PHASE-01
planType: phase-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-RESEARCH-000
tags:
  - plan
  - phase-control
  - category-specs
  - spec
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

## Current plan groups

- `category-core/`: phase-01 program control, source-map admission, category foundation, Hom/End/Aut, Sage admission, and audit control.
- `lattice/`: ModulesWithForms and lattice roadmap plans expressed as spec-phase dependency plans.
- `geometry/`: geometric source-admission and curve/monodromy backend research plans.
- `sprints/`: leaf sprint plans that own executable cards by `planId`.

The connected plan spine is `PLN-RESEARCH-000` -> `PLN-PHASE-01` ->
`PLN-CAT-000`; all active phase-01 tasks and decisions now point to leaf plans
under that spine.

## Exit criteria

- [ ] Core categorical vocabulary is specified enough to express later implementation cards.
- [ ] Lattice specs can state Picard, discriminant, isometry, Hom, End, Aut, base-change, and morphism semantics without raw matrix fallbacks.
- [ ] Active mathematical spec leaves either contain a definition-grounding record or
  are explicitly blocked/split on the missing source, decision, or proof obligation.
- [ ] Backend/source gaps are filed as research cards rather than hidden inside implementation work.
- [ ] Future phase plans have enough prerequisites to block premature downstream work.
