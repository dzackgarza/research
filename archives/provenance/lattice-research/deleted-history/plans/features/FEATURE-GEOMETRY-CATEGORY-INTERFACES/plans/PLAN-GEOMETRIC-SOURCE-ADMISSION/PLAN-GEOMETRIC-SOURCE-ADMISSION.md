---
id: PLAN-GEOMETRIC-SOURCE-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
title: Geometric category source admission research
status: complete
priority: high
owner: Zack
description: Organize the geometry category research cards that identify source-backed
  category vocabulary for schemes, varieties, manifolds, polytopes, and toric interfaces
  before any implementation card is created.
successCriteria:
- Every child card cites the exact sources searched and separates evidence from inference.
- Geometry vocabulary is admitted only after mathematical owner, Sage surface, and
  public category boundary are explicit.
- Toric-variety work records its dependency on the lattice category surface before
  implementation.
- Follow-up implementation or decision work is tracked as new cards rather than left
  in research prose.
phases:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Geometric category source admission research

## Objective

Organize the geometry category research cards that identify source-backed category
vocabulary for schemes, varieties, manifolds, polytopes, and toric interfaces before
any implementation card is created.


## Mathematical Grounding Requirements

This geometry plan is source-admission work, not a license for ad hoc algebraic-geometry
interfaces. Each child card must cite the relevant literature, Sage/Singular/Macaulay2/
Oscar documentation, or local theory note before admitting a category, constructor,
backend, invariant, or morphism.

The grounding record must state the geometric object, morphism or construction,
hypotheses, return object, and backend evidence. If the software only exposes raw
polynomials, matrices, or option bags, the child card must translate them into project
category vocabulary or split a source/backend decision first.

## Source Provenance

- Parent feature: `FEATURE-GEOMETRY-CATEGORY-INTERFACES`.
- Active child cards are contained by this plan's phase cards.
- Current phase boundary: phase-01 category specs and semantic vocabulary only.

## Context

This is a leaf plan. Its child cards are research tasks, not implementation work. They
must return source evidence, Sage or backend surface findings, ownership decisions, and
follow-up cards when the category vocabulary is concrete enough to execute.

## Acceptance Criteria

- [ ] Every child card cites the exact sources searched and separates evidence from inference.
- [ ] Geometry vocabulary is admitted only after mathematical owner, Sage surface, and public category boundary are explicit.
- [ ] Toric-variety work records its dependency on the lattice category surface before implementation.
- [ ] Follow-up implementation or decision work is tracked as new cards rather than left in research prose.

## Dependencies And Boundaries

- Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map and admission discipline.
- Does not authorize phase-06 geometry/Coble implementation.
- Does not replace source-backed mapping docs or future category specs.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate review)

**Gates passed:** G1, G2, G3, G4, G6
**Gates failed:** G5
**Outcome:** CONDITIONAL PASS — G5 has a blocking inconsistency; see findings.

#### G1 — Source Grounding: PASS

The plan's source grounding is adequate for a plan card (not a research/implementation
card). Verified sources:

- Parent feature `FEATURE-GEOMETRY-CATEGORY-INTERFACES` — confirmed present, lists this
  plan in its `plans` array.
- Phase `PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH` — confirmed present with 12 child
  task cards on disk. All child cards cite specific sources (Stacks Project tags, Sage
  docs, OSCAR docs, Macaulay2 docs, installed Sage source files), confirmed by the
  phase's own 6-gate review (2026-05-07).
- Dependency `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` — confirmed present at
  `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/
  PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-
  ADMISSION.md`.

The plan's "Mathematical Grounding Requirements" section (lines 38-47) acts as a
hard gate: child cards must cite literature, Sage/Singular/Macaulay2/Oscar docs, or
local theory notes. The "Source Provenance" section (lines 50-53) references only the
parent feature and child cards — no unverifiable external sources.

No dangling provenance references. The plan itself is a routing/coordination card;
the heavy source-lifting is delegated to child research tasks, which the phase review
confirms have proper grounding.

#### G2 — Exit Criteria Checkable: PASS

All 4 YAML success criteria (lines 15-22) and 4 acceptance checkboxes (lines 63-66)
are concrete and verifiable:

| Criterion | Verification method |
|---|---|
| Every child card cites exact sources, separates evidence from inference | Audit child card bodies for source sections and evidence/inference labels |
| Vocabulary admitted only after owner + Sage surface + category boundary explicit | Per-card content audit for owner/surface/boundary triples |
| Toric-variety work records lattice category dependency before implementation | Inspect TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY for lattice dep |
| Follow-up work tracked as new cards, not left in research prose | Filesystem enumeration: no implementation embedded in research cards |

All criteria are binary (present/absent) and objectively verifiable by file-system or
body-content audit. No hand-wavy criteria detected. The acceptance checkboxes (lines
63-66) are verbatim copies of the YAML success criteria — no drift.

#### G3 — Phase Inventory Complete: PASS

The plan declares exactly one phase: `PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH`
(line 24). This phase exists on disk at the expected path with 12 child task cards:

1. TASK-INTEGRATE-SCHEMES-CATEGORY (substrate)
2. TASK-INTEGRATE-VARIETIES-CATEGORY
3. TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY
4. TASK-INTEGRATE-POLYTOPES-CATEGORY
5. TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY
6. TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY
7. TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY
8. TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY
9. TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY
10. TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY
11. TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY
12. TASK-WRAPUP-PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH

All 12 confirmed present on disk. The phase's own 6-gate review (2026-05-07) confirmed
no gaps — all geometry category vocabularies from the parent plan description (schemes,
varieties, manifolds, polytopes, toric interfaces, curves, surfaces, families) are
covered. Single-phase inventory is correct for a leaf research plan.

#### G4 — Scope Containment: PASS

Scope is tightly bounded:

- **IN**: Organize geometry category research cards identifying source-backed vocabulary
  for schemes, varieties, manifolds, polytopes, and toric interfaces (line 32-34).
- **OUT** (lines 71-72): Does not authorize phase-06 geometry/Coble implementation.
  Does not replace source-backed mapping docs or future category specs.
- **NATURE**: Self-declared "leaf plan" (line 57). Child cards are "research tasks, not
  implementation work" (line 58). Cards "must return source evidence, Sage or backend
  surface findings, ownership decisions, and follow-up cards" (lines 58-59).

The "Dependencies And Boundaries" section (lines 68-72) explicitly fences off
implementation. No scope creep into implementation, deployment, performance, or UX
concerns. The plan stays within its mandate: source-admission research before any
implementation card is created.

No leaked concerns detected.

#### G5 — Dependencies Correct: FAIL

- **YAML `dependsOn: []`** (line 7) — declares no prerequisite plans.
- **Body "Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`"** (line 70) —
  declares a plan-level dependency in prose that is NOT reflected in the YAML
  `dependsOn` field.

**This is a blocking inconsistency.** The YAML `dependsOn` field is the machine-readable
DAG edge. If the geometric source admission plan depends on the category-spec
source-maps plan for "source-map and admission discipline," that dependency must be
recorded in `dependsOn` so that tooling (`just plan-validate`, progress reports) can
enforce the edge.

Additional findings:
- Parent `FEATURE-GEOMETRY-CATEGORY-INTERFACES` — confirmed bidirectional (feature's
  `plans` array includes this plan).
- Phase `PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH` — on disk, `dependsOn: []` (correct
  for a plan's only phase).
- Dependency target `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` — exists but has
  status `needs-human-input` with its own G1 and G5 blocking failures (8 missing source
  map files, 1 dangling subplan reference). This creates transitive risk for any plan
  that depends on it.
- No circular references detected.
- Task-level DAG within the phase is correct per the phase's own G5 review.

#### G6 — No Weakening / Preservation: PASS

- Plan status is `needs-review` — not prematurely accepted or executed.
- Success criteria use strong, obligation-heavy language: "must cite," "admitted only
  after," "records its dependency before."
- Acceptance criteria are in checkbox format — properly trackable and auditable.
- The "Mathematical Grounding Requirements" section (lines 38-47) reinforces rather than
  weakens the feature's grounding discipline. It requires literature/Sage/Oscar/Macaulay2
  citations before admitting any category, constructor, backend, invariant, or morphism.
- No criterion has been relaxed, deleted, or replaced with weaker language.
- The plan preserves the feature's intent: geometry vocabulary stays research-scoped
  until source evidence is explicit.

#### Blocking Issues

1. **G5 — `dependsOn` inconsistency.** The YAML frontmatter declares `dependsOn: []`
   but the body states "Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for
   source-map and admission discipline." Add the dependency to the YAML `dependsOn`
   array so the DAG is machine-enforceable. If the plan does NOT actually depend on
   that plan (i.e., it's a soft reference, not a prerequisite), then clarify the body
   language to avoid the appearance of a hard dependency.

#### Non-blocking Observations

- **Transitive risk**: The dependency target `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-
  ADMISSION` has its own G1 and G5 blocking failures (8 missing source maps, 1 dangling
  subplan). If the geometric source admission plan truly depends on it, those failures
  must be resolved before this plan can exit `needs-review`.
- **Phase already reviewed**: The phase card `PHASE-GEOMETRIC-SOURCE-ADMISSION-
  RESEARCH` has its own 6-gate review (2026-05-07) with all gates passing but 4 of 12
  child cards still `needs-human-input`. The plan-level review does not need to
  re-audit those child cards; the phase review covers them.
- **Status alignment**: Plan status is `needs-review`, phase status is `complete`.
  This is correct — the phase can be execution-complete while the plan awaits review
  approval. No inconsistency.
- **Leaf plan confirmation**: The plan self-describes as a leaf plan, which is correct
  given it has one phase with research tasks and no sub-plans.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.
- 2026-05-07: 6-gate protocol review conducted. G5 failed on `dependsOn` inconsistency between YAML frontmatter and body. All other gates pass.
