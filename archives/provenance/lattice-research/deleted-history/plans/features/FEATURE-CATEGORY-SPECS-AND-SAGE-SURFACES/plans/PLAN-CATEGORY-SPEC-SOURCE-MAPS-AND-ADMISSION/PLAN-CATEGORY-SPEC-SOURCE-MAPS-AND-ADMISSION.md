---
id: PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Category spec source maps and admission
status: complete
priority: critical
owner: Zack
description: Preserve and route the non-lattice root `plans` source maps into an approved
  research/admission workflow before they drive implementation.
successCriteria:
- The human approves this source-map plan before decomposition.
- Each source map is classified as canonical reference, research input, phase dependency,
  or retired provenance.
- Work that blocks vocabulary or method ownership becomes critical or high-priority
  cards.
- External/Sage-source claims cite source paths or docs before implementation.
- Constructor admission cards identify the mathematical owner and the Sage constructor
  surface separately.
- Every `category_specs/*/docs/MAPPING.md` file is represented by a tracked `spec`
  card with completeness and mathematical-correctness review criteria.
phases:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Category-spec source maps constructor routing and admission research

## Objective

Preserve and route the non-lattice root `plans` source maps into an approved research/admission workflow before they drive implementation.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Current State

Several root plan files are source maps or design notes rather than executable implementation plans. They are valuable, but they should not remain free-floating planning authorities outside Nimbalyst.

## Source Provenance

- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/RING_INTEGRATION.md`
- `plans/SET_SPEC.md`
- `plans/autset_categories_path.md`
- `plans/autset_integration_plan.md`
- `plans/axioms_with_generators_finitely_presented.md`
- `plans/category_creation_notes.md`
- `plans/homsets_structural_core.md`

## Scope

This plan owns research and admission around:

- Static category hierarchy and method-surface phases.
- Ring construction entry points and constructor routing.
- Set category hierarchy and concrete set implementation surfaces.
- Autset admission as an axiom/refinement below Endsets.
- WithGenerators, FinitelyPresented, Dedekind/PID module axioms, and structural patterns.
- Category creation and `_refine_category_` mechanics.
- Homsets as the structural core for modules, duals, endsets, and autsets.

## Subplans

- `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION`: Sage surface constructor admission and concrete category families.
- `PLAN-GEOMETRIC-SOURCE-ADMISSION` (under `FEATURE-GEOMETRY-CATEGORY-INTERFACES`): geometric category source admission research.

## Non-goals

- Do not implement directly from source-map notes.
- Do not convert every source-map heading into a card.
- Do not create duplicate cards when active category-spec tasks already cover the work.

## Acceptance Criteria

- [ ] The human approves this source-map plan before decomposition.
- [ ] Each source map is classified as canonical reference, research input, phase dependency, or retired provenance.
- [ ] Work that blocks vocabulary or method ownership becomes critical or high-priority cards.
- [ ] External/Sage-source claims cite source paths or docs before implementation.
- [ ] Constructor admission cards identify the mathematical owner and the Sage constructor surface separately.
- [ ] Every `category_specs/*/docs/MAPPING.md` file has a tracked spec card and a
      mathematical review path for completeness, well-typedness, and coherent
      highest-category method placement.

## Decomposition Boundary

After approval, split into research cards for source-map verification and decision cards for unresolved ownership or admission choices. Only create implementation cards after the relevant vocabulary and ownership are fixed.

## Visual Window

See `.agents/visuals/category-spec-plan-hierarchy.mmd` for the current plan hierarchy and dependency sketch.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate review)

**Gates passed:** G2, G3, G4, G6
**Gates failed:** G1, G5
**Outcome:** CONDITIONAL PASS — G1 and G5 have blocking issues; see findings.

#### G1 — Source Grounding: FAIL

The plan cites 8 source maps in its "Source Provenance" section (lines 55–62):

- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/RING_INTEGRATION.md`
- `plans/SET_SPEC.md`
- `plans/autset_categories_path.md`
- `plans/autset_integration_plan.md`
- `plans/axioms_with_generators_finitely_presented.md`
- `plans/category_creation_notes.md`
- `plans/homsets_structural_core.md`

**None of these 8 files exist on disk.** Full-repo search confirmed zero matches for every filename. The root `plans/` directory contains only `card-progress-report.md`, `plan-dag.md`, and `AGENTS.md`.

The plan's "Current State" section acknowledges these are "free-floating planning authorities outside Nimbalyst," which may explain their absence (possibly ingested/migrated or not yet imported). However, for G1 purposes, the listed source provenance cannot be confirmed, and any card that depends on their content has unverifiable grounding.

**Confirmed present:**
- Parent `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` — exists, lists this plan in its `plans` array.
- Phase `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT` — exists with 2 child tasks (`TASK-MAPPING-DOC-COMPLETENESS-RESEARCH`, `TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT`).
- 11 `category_specs/*/docs/MAPPING.md` files — all confirmed present.
- `theory/references/index.md` — confirmed present.

**Dangling reference:** Subplan `PLAN-GEOMETRIC-CATEGORY-EXPANSION` (line 79) does not exist on disk. `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` (line 78) does exist.

#### G2 — Exit Criteria Checkable: PASS

All 6 YAML success criteria (lines 14–24) and 6 acceptance criteria checkboxes (lines 89–96) are concrete and verifiable:

| Criterion | Verification method |
|---|---|
| Human approves before decomposition | Binary human gate |
| Source maps classified (canonical/reference/research/retired) | Audit classification table |
| Blocking work → critical/high-priority cards | Priority field audit |
| Sage-source claims cite paths/docs | Grep/body audit |
| Constructor admission cards separate mathematical owner vs Sage surface | Card content audit |
| Every MAPPING.md → tracked spec card with review criteria | Count mapping docs vs spec cards |

No hand-wavy or unmeasurable criteria. Criterion 6 has a slight wording mismatch between YAML frontmatter ("completeness and mathematical-correctness review criteria") and acceptance checkbox ("mathematical review path for completeness, well-typedness, and coherent highest-category method placement") — the checkbox is more specific but consistent in intent.

#### G3 — Phase Inventory Complete: PASS

The plan declares exactly 1 phase: `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`. This is appropriate for a research/admission coordination plan that routes source maps into a tracked workflow. The phase exists on disk with 2 child tasks that exhaust its exit criteria. The "Decomposition Boundary" section (lines 98–100) explicitly gates further decomposition on plan approval — the work after approval (research cards, decision cards, implementation cards) is appropriately deferred.

No missing phases. The single-phase inventory is correct for the plan's stated scope.

#### G4 — Scope Containment: PASS

Scope is well-defined in 7 enumerated bullet points (lines 66–74). Non-goals (lines 81–85) are explicit:
- Do not implement directly from source-map notes.
- Do not convert every source-map heading into a card.
- Do not create duplicate cards when active category-spec tasks already cover the work.

The plan coordinates research and admission; it does not authorize implementation. Definition grounding requirements (lines 37–45) act as a hard stop for spec edits without source evidence. No leaked concerns (performance, deployment, UX, Sage version upgrades). Scope is tightly contained to a routing/classification workflow.

#### G5 — Dependencies Correct: FAIL

- `dependsOn: []` — **correct**; this plan has no prerequisite plans.
- Parent `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` — confirmed bidirectional (parent lists this plan).
- Subplan `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` — exists.
- Subplan `PLAN-GEOMETRIC-CATEGORY-EXPANSION` — **does not exist**. This is a dangling reference in the "Subplans" section. Either the file is missing or the reference is stale.

No circular references detected in the DAG (plan → phase → tasks → specs, all leaf nodes). The phase's `dependsOn: []` is correct for a plan's only phase.

#### G6 — No Weakening: PASS

- Plan status is `needs-review` — not prematurely accepted.
- Success criteria use strong language: "must," "reject," "become," "every."
- Acceptance criteria are in checkbox format — properly trackable.
- No criterion has been relaxed, deleted, or replaced with weaker language.
- Definition grounding requirements (lines 37–45) reinforce rather than weaken the feature's grounding control (FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES lines 31–46).

#### Blocking Issues

1. **G1 — 8 source map files missing.** Either ingest the files into the tracked planning workspace or update the "Source Provenance" section to clarify their status (historical references, already ingested under different IDs, intentionally not imported, etc.).

2. **G5 — Dangling subplan reference.** `PLAN-GEOMETRIC-CATEGORY-EXPANSION` does not exist. Either create the plan card or remove the reference from "Subplans."

#### Non-blocking Observations

- The phase card status is `complete` while the plan card status is `needs-review`. The phase card's own 6-gate review log (2026-05-07) notes that both child tasks are complete but awaiting review. No inconsistency — the phase can be execution-complete while awaiting approval of the plan that owns it.
- The plan's acceptance criteria checkbox 6 is slightly more detailed than the corresponding YAML success criterion. This is a clarification, not a weakening.
- Recommendation: resolve the two blocking issues, then re-run gates. The plan's structure, scope, and criteria are otherwise sound.
