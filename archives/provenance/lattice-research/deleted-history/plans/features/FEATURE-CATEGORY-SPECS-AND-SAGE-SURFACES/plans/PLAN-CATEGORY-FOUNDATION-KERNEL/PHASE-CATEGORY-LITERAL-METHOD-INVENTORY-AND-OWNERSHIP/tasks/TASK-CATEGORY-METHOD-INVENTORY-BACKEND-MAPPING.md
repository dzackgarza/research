---
id: TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Translate external software mappings into method ownership rows
status: complete
priority: critical
owner: Zack
description: Convert theory backend and external software maps into method/backend
  ownership rows covering Julia/Oscar, GAP, Singular, Macaulay2, CARAT, Indefinite.jl,
  Sage bridges, and related exact systems.
successCriteria:
- The target method-inventory spec contains backend-routing rows for every method
  in `.agents/memories/theory/backends/abstract-to-external-mapping.md`.
- Backend rows use the routing labels from `software-capability-map.md` and name the
  mature system before any implementation card exists.
- Variety, curve, surface, divisor, sheaf, family, Picard/lattice, group-action, isometry,
  orbit, and embedding methods are attached to mathematical owners and backend codomains.
- Missing or uncertain backend support becomes backend-gap research or decision cards
  instead of bespoke implementation permission.
complexity: 68
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Translate external software mappings into method ownership rows

## Summary

Translate backend and external software mapping notes into method-owner and
backend-routing rows. The output should make visible which mathematical object owns a
method and which mature system should implement it.

## Source Provenance

- `.agents/memories/theory/backends/software-capability-map.md`
- `.agents/memories/theory/backends/abstract-to-external-mapping.md`
- `.agents/memories/theory/backends/library-integration.md`
- `.agents/memories/theory/backends/comprehensive-tool-docs.md`
- `.agents/memories/theory/backends/oscar-lattices.md`
- `.agents/memories/theory/backends/gap-orbits.md`
- `.agents/memories/theory/backends/indefinite-jl.md`
- `.agents/memories/theory/backends/carat.md`
- `.agents/memories/theory/backends/vinberg-algorithm.md`
- `.agents/memories/theory/backends/buildings.md`
- `.agents/memories/theory/backends/indefinite-isometry.md`
- `.agents/memories/theory/backends/foliation-lib-reusable-procedures.md`
- `.agents/memories/theory/backends/index.md`
- Backend notes for Singular, Macaulay2, Sage, GAP, Oscar/Julia, CARAT, and
  Indefinite.jl as linked from those files.

## Context

The seed rows include:

- varieties and surfaces: `blowup`, `resolve_singularities`, `picard_group`,
  `kodaira_dimension`, `hilbert_polynomial`, `hodge_number`,
  `holomorphic_euler_characteristic`, `canonical_class`, `birational_involution`;
- curves and plane curves: `genus`, `arithmetic_genus`, `normalization`,
  `equation`, `dual_curve`, node and singularity methods;
- divisors and sheaves: Riemann-Roch space dimension, ampleness, nefness,
  intersections, sheaf cohomology, Euler characteristic, rank;
- families: `specialization`, `monodromy`;
- Picard and lattice objects: intersection matrices, discriminant groups,
  primitive embeddings, automorphism groups, isometry tests, orbit representatives,
  Vinberg-related surfaces;
- group actions and finite groups: orbit, stabilizer, centralizer, finite group
  action methods;
- backend statuses: `preferred-backend`, `bridge-needed`, `candidate-backend`,
  `true-gap`, `out-of-scope`.

## Complexity And Ownership

- Owner/role: backend-routing source miner.
- Complexity: `68` (high).
- Rationale: the task is mostly source translation, but mistakes can cause local
  bespoke algorithms where mature systems should be wired.
- Split/promote note: split only if a backend note needs its own research card because
  current source coverage is insufficient.

## Acceptance Criteria

- [x] The target method-inventory spec contains backend-routing rows for every method in `.agents/memories/theory/backends/abstract-to-external-mapping.md`.
- [x] Backend rows use the routing labels from `software-capability-map.md` and name the mature system before any implementation card exists.
- [x] Variety, curve, surface, divisor, sheaf, family, Picard/lattice, group-action, isometry, orbit, and embedding methods are attached to mathematical owners and backend codomains.
- [x] Missing or uncertain backend support becomes backend-gap research or decision cards instead of bespoke implementation permission.

## Dependencies And Boundaries

- This task does not approve bespoke algorithms.
- Do not route implementation to proprietary systems unless the repo's backend map
  explicitly authorizes them for comparison only.
- Do not confuse backend method availability with category ownership. The owner row
  names the project object; the backend row names the bridge target.
- If external source support is stale or uncertain, create a research card rather than
  declaring the method unsupported.

## Work Log

- 2026-05-05: Created as the backend/external-software leaf for the literal method ownership inventory phase.
- 2026-05-06: Wrote backend-routing rows into
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`, including all abstract method
  rows from `.agents/memories/theory/backends/abstract-to-external-mapping.md`, additional group-action
  rows from the backend map, and a decision card for malformed source surfaces.
  Moved this task to needs-review.
- 2026-05-06: Updated source provenance to the actual backend memory root and added
  the buildings, indefinite-isometry, foliation, and backend-index files to match the
  broadened source corpus.

## Review Log

### Review 2026-05-07 (Euler)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent review passed; human approval still required before
completion

#### Evidence

- Searched this card, the parent phase, target backend rows in
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`, abstract/backend maps,
  Picard and malformed-name decisions, and git diff/status.
- Found that backend rows cover the abstract map with codomains and routing statuses.
- Found malformed backend surfaces and Picard/lattice owner conflicts are routed
  through decision cards, not implementation guesses:
  `[[DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES]]` and
  `[[DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER]]`.

#### Residual Risk

- Smoke/tests were not run for this review because this is backend-routing spec work.
- Future implementation must re-audit `candidate-backend` rows before wiring a mature
  system bridge.
