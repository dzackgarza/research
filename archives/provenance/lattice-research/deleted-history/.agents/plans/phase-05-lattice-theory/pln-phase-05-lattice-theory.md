---
trackerStatus:
  type: plan
title: Phase 05 lattice-theoretic implementation
status: blocked
planId: PLN-PHASE-05
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
  - lattices
  - implementation
  - lean
  - formalization
---

# Phase 05 lattice-theoretic implementation

## Objective

Build the genuinely lattice-theoretic layer once universal category boilerplate is in
place: discriminant forms, primitive embeddings, local invariants, orthogonal groups,
base change, and Nikulin-style criteria expressed semantically.


## Mathematical Grounding Gate

Lattice-theoretic work must cite primary mathematical sources before implementation or
claim promotion. Cards touching discriminant forms, primitive embeddings, local
invariants, orthogonal complements, genus criteria, or Nikulin-style results must record
exact definitions, hypotheses, return objects, and proof or literature obligations.

Use `theory/references/index.md`, `theory/foundations/bilinear-forms-duals-morphisms.md`,
`.agents/skills/lattice-redesign/references/category-abc-spec.md`, and backend capability
notes. Computations are supporting evidence unless the card states the exact theorem or
certificate being proved and routes it through proof audit.

## Lean and Aristotle thread

Start formalizing small lattice definitions and lemmas once the corresponding semantic
interfaces are stable. Targets should be local and library-building: basic statements
about forms, discriminant groups, primitive embeddings, base change, and hypotheses used
by Nikulin-style criteria. Do not attempt a major Coble theorem here.

Aristotle may be run asynchronously for bounded Lean tasks, but the accepted artifact is
checked Lean code plus a reviewed link to the source-backed mathematical statement.

## Entry criteria

- [ ] Phase 03 and Phase 04 provide the module, form, Hom/End/Aut, and enumeration surfaces needed by lattices.
- [ ] Backend routing is documented for Oscar, Indefinite.jl, CARAT, GAP, Sage, and related systems.

## Exit criteria

- [ ] Lattice results are expressed through typed lattice objects and morphisms.
- [ ] Primary-source lattice criteria are implemented or wired with traceable evidence.
- [ ] Small lattice lemmas suitable for later Coble arguments have Lean statements or tracked formalization cards.
- [ ] QC gates the committed implementation surface before phase transition.
