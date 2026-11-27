---
id: PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
trackerStatus:
  type: plan
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
- '[[PLAN-GEOMETRIC-SOURCE-ADMISSION]]'
title: Curve complement and monodromy backend research
status: complete
priority: high
owner: Zack
description: Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs,
  and monodromy research cards under one leaf plan so backend evidence is collected
  before geometry-facing implementation work is proposed.
successCriteria:
- Each child card records exact sources searched, backend capabilities, mathematical
  inputs, and mathematical outputs.
- Negative findings use the repository five-field format.
- Any backend admission consequence is linked to a spec, decision, or implementation
  card.
- No child card introduces a public backend wrapper before ownership and source evidence
  are reviewed.
phases:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Curve complement and monodromy backend research

## Objective

Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs, and
monodromy research cards under one leaf plan so backend evidence is collected before
geometry-facing implementation work is proposed.


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
- Related phase boundary: phase-01 source and vocabulary research only.

## Context

This plan collects backend investigations that inform later curve, surface, family,
and monodromy category surfaces. It must not become a shortcut into downstream Coble
experimentation.

## Acceptance Criteria

- [ ] Each child card records exact sources searched, backend capabilities, mathematical inputs, and mathematical outputs.
- [ ] Negative findings use the repository five-field format.
- [ ] Any backend admission consequence is linked to a spec, decision, or implementation card.
- [ ] No child card introduces a public backend wrapper before ownership and source evidence are reviewed.

## Dependencies And Boundaries

- Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map and constructor admission discipline.
- Blocks premature phase-06 implementation until backend capability and vocabulary are explicit.
- Does not authorize Coble orbit, Picard, or surface computations.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.
- 2026-05-06: Started the approved backend-research plan with
  `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]` as the first ready
  source-admission leaf.

---

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate plan card review)

**Gates passed:** G1, G2, G3, G4, G6
**Gates failed:** G5 (one fixable finding)
**Outcome:** PASS WITH FINDINGS — the plan is structurally sound and its single phase has been independently reviewed and passed, but the frontmatter `dependsOn` array is empty while the body declares a dependency. One fix required.

---

#### G1 — Source Grounding / Definition Grounding

PASS.

- Plan ID `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` matches filename stem.
- Parent feature `FEATURE-GEOMETRY-CATEGORY-INTERFACES` confirmed present at `/home/dzack/research/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`.
- Sole phase `PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH` listed in `phases:` (line 24) confirmed present at its expected path under `PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH.md`.
- Phase card's `parents:` correctly points back to this plan.
- Five child tasks under the phase confirmed present:
  - `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE.md`
  - `TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md`
  - `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md`
  - `TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS.md`
  - `TASK-WRAPUP-PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH.md`
- All five backend domains named in the description (curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs, monodromy) have corresponding research task coverage.
- Six follow-up cards (specs and decisions) produced by the research tasks confirmed present in `specs/` and `decisions/` directories.
- Mathematical grounding requirements section (lines 37-47) establishes clear source-citation discipline before any category/constructor/backend admission.
- No orphan references detected.

#### G2 — Exit Criteria Checkable

PASS.

All four success/acceptance criteria are concrete, verifiable, and measurable:

1. **"Each child card records exact sources searched, backend capabilities, mathematical inputs, and mathematical outputs."** — checkable: each child task card can be audited for these four fields. The phase card's existing 6-gate review confirmed this for all five tasks.
2. **"Negative findings use the repository five-field format."** — checkable: any negative finding in a child card can be checked against the five-field format (capability, boundary, evidence, consequence, follow-up). The ore_algebra task already records a concrete negative finding in this format.
3. **"Any backend admission consequence is linked to a spec, decision, or implementation card."** — checkable: cross-references can be verified by resolving wiki-link targets. All five research tasks produced tracked follow-up cards.
4. **"No child card introduces a public backend wrapper before ownership and source evidence are reviewed."** — checkable: each child task can be audited for wrapper code. All research tasks contain explicit "Do not implement" boundaries.

No vague, hand-wavy, or unmeasurable criteria.

#### G3 — Phase Inventory

PASS.

- One phase declared in `phases:` (line 24): `PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH`.
- This is a leaf research plan — a single research phase is appropriate. The plan does not span implementation phases.
- The phase groups five tasks covering all six backend domains named in the plan objective (curve-complement and Sirocco are covered by one combined task; Riemann-surface, ore_algebra, Picard-Fuchs/monodromy each have a dedicated task; plus a wrap-up task).
- Phase card status is `complete` — the phase has been independently 6-gate reviewed and passed with minor findings. Four research tasks are in `needs-human-input` (awaiting human approval) and the wrap-up task is `unstarted` (correctly gated on sibling completion).
- Coverage is 1:1 against the plan's stated objective.

#### G4 — No Scope Creep

PASS.

- Plan explicitly bounds itself to source-admission research: "Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs, and monodromy research cards under one leaf plan so backend evidence is collected before geometry-facing implementation work is proposed." (lines 32-34)
- Clear negative boundaries stated:
  - "It must not become a shortcut into downstream Coble experimentation." (line 58-59)
  - "Does not authorize Coble orbit, Picard, or surface computations." (line 72)
  - "Blocks premature phase-06 implementation until backend capability and vocabulary are explicit." (line 71)
- All five child tasks contain explicit implementation boundaries ("Do not implement a wrapper...", "Do not vend or wrap...", etc.).
- No leaked concerns (performance, deployment, UX) beyond acknowledged environmental gaps.
- Plan scope is one phase deep — appropriate for the problem.

#### G5 — Dependencies Correct

FAIL (one fixable finding).

**Finding:** The frontmatter `dependsOn` array is empty (`dependsOn: []` at line 7), but the body explicitly declares a dependency at line 70:

> "Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map and constructor admission discipline."

The dependency card exists at:
`/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION.md`
with status `needs-human-input`. The dependency is real and legitimate — it provides the source-map discipline that this plan's child tasks follow — but it is not reflected in the machine-readable frontmatter.

**Fix required:** Add `'[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'` to the `dependsOn` array in the YAML frontmatter. Without this, DAG tooling cannot detect the blocking edge, and execution sequencing may not honor it.

Otherwise:
- The plan's phase declares `dependsOn: []` — correct; no prior phase exists within this plan.
- All child research tasks declare `dependsOn: []` — correct; they are independently executable.
- The DAG is acyclic: parent feature → plan → phase → tasks → specs/decisions.
- The wrap-up task's self-reference in its own `dependsOn` was noted during the phase review and is a separate fix (belongs to the task card, not this plan).

#### G6 — No Weakening / Style and Compliance

PASS.

- Plan status is `needs-agent-review` — appropriate; not prematurely accepted.
- No exit criterion was relaxed, deleted, or replaced with weaker language compared to related plans in the repository.
- The phase card has been independently 6-gate reviewed and passed — evidence of gatekeeping discipline.
- The plan's metadata conforms to repository conventions (id matches filename, `trackerStatus.type: plan`, `parents` uses wiki-link syntax, `status` is a valid value).
- Tags are present and reference the parent feature.
- Body sections follow standard plan structure: Objective, Mathematical Grounding Requirements, Source Provenance, Context, Acceptance Criteria, Dependencies And Boundaries, Work Log.

No weakening or compliance issues detected.

---

#### Residual Risks / Observations

- The dependency on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` (status `needs-human-input`) means the source-map discipline this plan relies on has not yet received human approval. If that plan is rejected or significantly changed, this plan's grounding assumptions may need revision. This is not a defect — it is a legitimate DAG edge that should be visible to tooling.
- Four of five child research tasks are in `needs-human-input` status, meaning human approval is still required before the phase can be considered fully closed. The phase card is marked `complete` but this reflects structural completion (all tasks exist and have been reviewed), not that all deliverables are approved.
- The plan's `priority: high` is appropriate given its position as a prerequisite for downstream geometry-facing implementation.

---

#### Summary

The plan card is well-structured: scope is bounded to source-admission research, the single phase covers all five backend domains with one task each plus a wrap-up, and all exit criteria are concrete and verifiable. One fixable issue:

1. **Add the missing dependency** to the frontmatter `dependsOn` array: `'[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'` (line 7, currently `dependsOn: []`).

This is non-blocking but should be fixed before the plan is accepted. The phase has been independently reviewed and passed — no structural rework is needed.
