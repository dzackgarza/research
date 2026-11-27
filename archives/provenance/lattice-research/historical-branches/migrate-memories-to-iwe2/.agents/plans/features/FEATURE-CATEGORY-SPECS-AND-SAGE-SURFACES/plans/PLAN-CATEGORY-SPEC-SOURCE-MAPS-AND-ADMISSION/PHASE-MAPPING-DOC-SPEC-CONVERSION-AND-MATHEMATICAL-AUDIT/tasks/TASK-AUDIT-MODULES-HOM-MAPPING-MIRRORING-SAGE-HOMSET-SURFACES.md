---
id: TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-MODULES]]'
title: Audit Modules hom mapping for mirrored Sage homset surfaces
status: complete
priority: critical
description: Audit `category_specs/modules/homsets.py` and the Modules mapping/spec
  surface so retained Sage module-hom container methods such as `zero()`,
  identity/coercion constructors, and homspace operations are explicitly mirrored,
  rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Modules hom mapping records the retained Sage homset/container methods relevant to module homs, endomorphisms, and automorphisms.
- Each retained method is assigned to a Modules hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 44
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Modules hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Modules hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`
- `category_specs/modules/homsets.py`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- Sage docs/source for `sage.categories.modules.Homsets`, `Endset`, and concrete module homspace containers

## Context

Modules is the richest current homset-bearing subtree in repo specs. It already
declares project-owned `zero()` and related surfaces, so this audit must decide
which Sage homset/container methods remain part of the project contract and which
are merely backend convenience.

## Acceptance Criteria

- [x] The Modules mapping/spec identifies Sage homset/container methods relevant to module hom objects, constructors, and endomorphism structure.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not treat Sage coercive convenience as automatic mathematical admission.
- Keep this card on `modules/homsets.py` and the Modules mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Modules homset mirroring audit to `[[SPEC-MAPPING-MODULES]]`,
  covering Sage `Modules(R).Homsets()` parent methods, concrete free-module
  homspace constructors, finite/free matrix-space and basis operations, identity
  and generic Hom infrastructure routing, module endset algebra structure,
  morphism element methods, and automorphism witness routing. No new follow-up
  card was required beyond existing generic Hom/End/Aut and downstream subtree
  audit cards.
- 2026-05-17: Fresh-context agent review recommended `complete` with no material
  findings. The card is now human-gated; do not mark `complete` without human
  approval.

## Review Log

### Fresh-Context Agent Review - 2026-05-17

Recommendation: `complete`; routed to `needs-human-input` for the required human gate.

- Gate 1: Source grounding checked against `[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]`, `category_specs/modules/docs/SAGE_INVENTORY.md`, `category_specs/modules/homsets.py`, and installed Sage homset/module-hom sources.
- Gate 2: Acceptance criteria are covered by the new `[[SPEC-MAPPING-MODULES]]` Modules homset mirroring audit.
- Gate 3: Diff review found no deleted obligations, narrowed surfaces, or Sage-gap-driven spec weakening.
- Gate 4: Review found the mapping consistent with project-owned Hom/End/Aut vocabulary rather than unexamined Sage generic inheritance.
- Gate 5: Retained method families are mirrored, routed, or rejected as interop-only with source evidence.
- Gate 6: `just plan-validate` passed; no plugin-owned source or fixture paths were changed.
- Red flag log: no introspection red flags were found in changed spec/card content; upstream Sage evidence contains ordinary `isinstance`, `hasattr`, `getattr`, `issubclass`, and `callable` checks that are not defects of this card.
