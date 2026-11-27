---
id: TASK-01KQN9J3WZDBZ8D0BPGG8AKVXH-IMPLEMENT-MISSING-SYMPY-SURFACE-FOR-REFINED-RING-CONSTRUCTOR-OUTPUTS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Implement missing _sympy_ surface for refined ring constructor outputs
status: complete
priority: high
description: 'The deleted Rings triage recorded ring smoke blockers: nested axiom
  category identity mismatches, missing _sympy_ methods on refined parents, and the
  matrix-ring surface split.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- Confirm failures are reduced without weakening constructor membership assertions.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Implement missing _sympy_ surface for refined ring constructor outputs

## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- Archived Rings triage content from commit `8d1c21c` lives at
  `plans/category_specs/rings/docs/TRIAGE.md`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Implement missing _sympy_ surface for refined ring constructor outputs from category_specs/rings/docs/TRIAGE.md`

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- [ ] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06: Audited the current ready leaf against the regenerated DAG and current
  `rings/smoketest.sage` output. The cited `category_specs/rings/docs/TRIAGE.md` path
  was not present at `8d1c21c^`, and a broader search found no live `_sympy_` failure
  in the current ring smoke frontier. The current failures are earlier or separate
  surfaces: `hilbert_polynomial`, finite-ring `completion`, complex interval/ball
  `algebraic_closure`, p-adic `_change_print_mode`, deferred q-adic precision-cap
  constructors, and related ring-frontier failures preserved in neighboring tracker
  items.
- 2026-05-06: No implementation patch was made for this card because the named
  `_sympy_` target is no longer present in current ring smoke output. This is not a
  blocked dependency state; it is a stale migrated leaf whose current smoke frontier is
  represented by linked successor work rather than by a live `_sympy_` leaf:
  `[[TASK-01KQN9J3WY0J7VF8KEY1X7496H-FIX-RINGS-CATEGORY-BASE-CLASS-IDENTITY-MISMATCH-IN-NESTED-AXIOM-REFINEME]]`,
  `[[TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED]]`,
  `[[TASK-01KQN9YGCQA3E2Y2RAMA2EHZPR-RESEARCH-UPSTREAM-SAGE-SUPPORT-OR-ISSUES-FOR-Q-ADIC-UNRAMIFIED-EXTENSION]]`,
  `[[TASK-01KQN9YGCKBZM1PG5YYQW5A8M6-IMPLEMENT-MATRIX-RING-REFINEMENT-INTO-ALGEBRAS-R-AND-MODULES-R-FREE-FINI]]`,
  and
  `[[TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI]]`.
  Moved to `needs-review` so a reviewer can decide whether to retire or merge the
  stale migrated card into those successor items.
- 2026-05-06: Reworked the archived triage provenance after Gate 1 review found that
  the recoverable source path is `plans/category_specs/rings/docs/TRIAGE.md` in
  `8d1c21c^`, not `category_specs/rings/docs/TRIAGE.md`.
- 2026-05-06: Reworked the successor and smoke-frontier record after re-review found
  that the finite-ring frontier is now `completion`, not `ideal_monoid`, and that the
  stale-card successor items must be linked explicitly.

## Review Log

### Review 2026-05-06 (Newton)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Findings: Definition Grounding

- The card cited `category_specs/rings/docs/TRIAGE.md` as the recovery path for the
  deleted Rings triage, but `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`
  fails because that path did not exist in the historical tree. The archived source
  content exists at `plans/category_specs/rings/docs/TRIAGE.md`, whose Missing
  `_sympy_` section lists the original refined ring constructor frontier.

### Re-review 2026-05-06 (Ptolemy)

**Gates passed:** Gate 1 Definition Grounding
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 2 Findings: Acceptance Criteria

- The stale smoke-frontier note still said finite-ring `ideal_monoid`, but the current
  `rings/smoketest.sage` output reports finite-ring `completion` failures for
  `IntegerModRing`, `Zmod`, and `Integers`.
- The card said successor work was represented by neighboring tracker items but did
  not link those successor items, even though the parent phase requires superseded
  child work to have linked successors.

### Focused Re-review 2026-05-06 (Leibniz)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** review passed; human approval still required before completion,
retirement, or merge into successor work

#### Residual Risks

- The focused re-review verified the prior Gate 2 findings were resolved: the finite
  ring frontier now records `completion`, and every successor item named in the stale
  card resolution resolves to a real task file.
- The reviewer did not rerun smoke in this focused read-only pass. Current smoke
  frontier evidence remains the earlier recorded `rings/smoketest.sage` run in this
  card and successor ring-frontier cards.
