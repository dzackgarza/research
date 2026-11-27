---
trackerStatus:
  type: plan
title: Sprint ring axiom identity mismatch q-adic precision frontier and matrix algebra surface split
status: approved
planId: SPR-RINGS-PADIC-01KQN9
planType: sprint-plan
priority: high
parentPlan: PLN-SAGE-000
tags:
- category-specs
- plan
- sprint
- rings
- precision
- algebras
- matrix
- theme-plan-control
---

# Sprint ring axiom identity mismatch q-adic precision frontier and matrix algebra surface split

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`.
- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Sprint ring axiom identity mismatch q-adic precision frontier and matrix algebra surface split from category_specs/rings/docs/TRIAGE.md and category_specs/rings/docs/MAPPING.md`

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- [ ] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

