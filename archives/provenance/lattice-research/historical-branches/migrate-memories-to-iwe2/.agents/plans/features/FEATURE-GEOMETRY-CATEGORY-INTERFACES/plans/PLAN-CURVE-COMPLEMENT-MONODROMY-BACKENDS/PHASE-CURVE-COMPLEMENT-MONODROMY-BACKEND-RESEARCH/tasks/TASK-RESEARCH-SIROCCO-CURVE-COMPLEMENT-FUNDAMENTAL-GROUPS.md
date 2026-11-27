---
id: TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS
trackerStatus:
  type: task
parents:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
dependsOn: []
title: Research Sirocco integration for curve-complement fundamental groups
status: complete
priority: low
description: Research whether and how `sirocco2` should be integrated for computing
  or representing fundamental groups of curve complements.
successCriteria:
- Read the upstream Sirocco repository and any available documentation.
- 'Identify the exact mathematical object(s) exposed: curve complements, fundamental
  groups, monodromy, or related structures.'
- Decide whether integration requires a spec card, implementation card, decision card,
  or rejection note.
- Record any required follow-up as tracked cards rather than inline TODOs.
complexity: 35
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
- PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
---
# Research Sirocco integration for curve-complement fundamental groups

## Summary

Research whether and how `sirocco2` should be integrated for computing or representing fundamental groups of curve complements.

## Source Provenance

Migrated from `specs/TODO.md`: "Integrate sirocco: https://github.com/miguelmarco/sirocco2" and note "Used to define pi_1 of curve complements."

## Context

This is exploratory category-spec research. The output should determine whether Sirocco belongs in the project vocabulary, whether it should be wrapped, and what category/spec cards or decisions are needed before implementation.

## Acceptance Criteria

- Read the upstream Sirocco repository and any available documentation.
- Identify the exact mathematical object(s) exposed: curve complements, fundamental groups, monodromy, or related structures.
- Decide whether integration requires a spec card, implementation card, decision card, or rejection note.
- Record any required follow-up as tracked cards rather than inline TODOs.

## Dependencies And Boundaries

Do not implement a wrapper in this card. Do not assume Sirocco semantics without reading upstream source/docs. Do not add a dependency until a separate implementation card or decision approves the integration path.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Read upstream SIROCCO2 README/source, Sage Zariski-Van Kampen
  documentation/source, and local Sage import behavior. Recorded the backend
  boundary in
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING.md`.
- 2026-05-06: Independent Gate 2 review found that the required follow-up choices
  were still inline in the mapping spec. Added
  `[[DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE]]` and linked the mapping
  spec's follow-up consequence to that decision card.

## Research Result

This card is ready for review. No dependency or wrapper implementation is
admitted from this pass.

Sirocco itself is a certified homotopy-continuation backend for following roots
of one-dimensional sections of bivariate complex polynomials. In Sage, that
backend is consumed by `sage.schemes.curves.zariski_vankampen` to compute braid
monodromy of a plane-curve projection and then finite presentations of
fundamental groups of affine or projective plane-curve complements by the
Zariski-Van Kampen method.

The mathematical object exposed at the project level should therefore be a
curve-complement fundamental group or braid-monodromy object attached to a
plane curve/projection, not a raw Sirocco wrapper. The local Sage environment has
`sage.libs.sirocco` installed and a small Sage example computed braid monodromy
and a finite group presentation, but public integration still waits on geometry
spec ownership for plane curves, complements, braid monodromy, and finitely
presented groups.

## Tracked Follow-Up

- `[[DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE]]` owns the public
  surface decisions for the Sirocco-backed route: complement-vs-curve method
  owner, public braid-monodromy object status, presentation/meridian typing, and
  affine/projective complement modeling.

## Review Log

### Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding.
**Gates failed:** Gate 2 Acceptance Criteria.
**Outcome:** revision-required, reworked in the work log above, returned to
`needs-agent-review` for another independent pass.

Finding:

- The card required follow-up work to be tracked, but the produced mapping spec
  listed the Sirocco public-surface choices as inline future prose rather than a
  tracked successor card.

### Re-Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance.
**Gates failed:** None.
**Outcome:** no concrete revision findings; human approval remains required before
marking the card complete.

Findings: none. The review found the prior Gate 2 defect resolved by
`[[DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE]]`, which now owns the
public-surface choices that had been left as inline prose.
