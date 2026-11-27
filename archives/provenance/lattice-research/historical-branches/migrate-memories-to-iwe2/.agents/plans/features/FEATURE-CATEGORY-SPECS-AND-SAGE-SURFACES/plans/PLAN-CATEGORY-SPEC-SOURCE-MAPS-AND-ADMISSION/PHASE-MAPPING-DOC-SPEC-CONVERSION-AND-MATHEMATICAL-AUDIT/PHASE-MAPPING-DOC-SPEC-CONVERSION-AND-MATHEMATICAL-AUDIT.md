---
id: PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
dependsOn: []
title: Mapping doc spec conversion and mathematical audit
status: complete
priority: critical
description: Convert every category-spec mapping document into a tracked spec surface
  and audit those specs for Sage-source completeness, mathematical correctness,
  well-typed signatures, and coherent highest-category method placement.
successCriteria:
- Every category_specs subtree mapping document has a feature-owned tracked spec card.
- Each mapping spec records the source MAPPING and SAGE_INVENTORY paths that ground it.
- Completeness review checks Sage written docs and installed Sage source for missing
  constructors, methods, inherited methods, and interop surfaces.
- Mathematical review rejects incoherent ownership, nonmathematical targets, ill-typed
  signatures, and mappings that confuse method definition location with output type.
- Unresolved mathematical choices become decision cards before implementation proceeds.
tasks:
- '[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]'
- '[[TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT]]'
- '[[TASK-AUDIT-ALGEBRAS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-CAT-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-LATTICES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-RINGS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING]]'
- '[[TASK-AUDIT-SETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-AUDIT-TOPOLOGICAL-SPACES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION]]'
- '[[TASK-WRAPUP-PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
---
# Mapping doc spec conversion and mathematical audit

## Summary

This phase makes mapping documents tracked spec surfaces and then reviews them as
mathematical interface specifications. The review must treat every method row as a
claim about where a method is defined, what its full signature is, and why that
signature is mathematically meaningful.

## Audit Standard

- Completeness: compare each mapping spec against Sage written docs, installed Sage
  source, local SAGE_INVENTORY files, and inherited category methods.
- Mathematical correctness: methods are mapped to the highest category where they are
  well-defined; subcategories inherit methods from supercategories; no row may use a
  nonmathematical target or software-shaped placeholder as a public mathematical owner.
- Type correctness: every admitted row states caller category, inputs, hypotheses,
  codomain or return object, and source evidence.
- Review consequence: gaps become tracked specs, tasks, or decision cards, not prose
  TODOs or implementation guesses.

## Review Handoff

The original mapping-doc conversion and mathematical-correctness tasks are complete.
After the 2026-05-10 Hom/End/Aut ownership decision, this phase reopened for the
per-subtree hom-mapping mirror audit: each subtree with a `homsets.py` file must
explicitly account for Sage homset/container methods it keeps, routes elsewhere, or
rejects as interop-only.

Current routing:

- The per-subtree homset mirroring audits and the Rings ownership follow-up are
  human-gated at `needs-human-input`.
- `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION` remains
  `unstarted` because it depends on human approval of the Posets audit; it is a
  downstream source-grounding leaf, not the next autonomous frontier item.
- This phase remains `in-progress` until the human-gated audit cards and the downstream
  Posets source-grounding leaf are resolved.

---

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate review)

**Gates passed:** G1, G2, G3, G4, G5, G6
**Gates failed:** None
**Outcome:** PASS — phase is well-formed, child tasks align with exit criteria, no blockers.

#### G1 — Source Grounding

- Parent plan `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` exists and lists this phase in its `phases` array.
- Both child tasks depend on 11 `SPEC-MAPPING-*` cards (Sets, Rings, Algebras, Modules, HomSets, Forms, Lattices, Posets, TensorAlgebraComponents, TopologicalSpaces, Cat). All 11 files confirmed present at `specs/SPEC-MAPPING-*.md`.
- Each mapping spec is source-grounded per the audit standard (cites SAGE_INVENTORY.md, MAPPING.md, Sage written docs/source).
- No orphan or dangling references detected.

#### G2 — Exit Criteria Checkable

All five phase success criteria are concrete and verifiable:

1. Mapping-doc-to-spec-card conversion → count mapping docs vs spec cards.
2. Each spec records MAPPING and SAGE_INVENTORY paths → grep/audit spec YAML frontmatter or body.
3. Completeness review against Sage docs/source → covered by TASK-MAPPING-DOC-COMPLETENESS-RESEARCH's own success criteria.
4. Mathematical review rejects ill-typed/incoherent rows → covered by TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT's own success criteria.
5. Unresolved mathematical choices → decision cards → emergent checkable deliverable.

No hand-wavy or unmeasurable criteria.

#### G3 — Task Inventory Complete

The phase declares exactly 2 child tasks:
- `TASK-MAPPING-DOC-COMPLETENESS-RESEARCH` (status: complete) — covers criteria 1, 2, 3.
- `TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT` (status: complete) — covers criteria 4, 5.

Both tasks are present, self-contained, have their own success criteria, and together exhaust the phase's exit criteria. No missing task gaps. The completeness task handled the "conversion" half; the mathematical-audit task handled the "audit" half. Coverage is 1:1.

#### G4 — No Scope Creep

Phase scope: convert mapping docs → tracked specs; audit for completeness and mathematical correctness.

- Completeness research task: reconciliation pass against Sage docs/source — within scope.
- Mathematical correctness audit: owner/codomain/signature review — within scope.
- Neither task performs implementation. Both are explicitly research/audit only.
- No leaked concerns (performance, deployment, UX, Sage version upgrades) beyond acknowledged residual risk of Sage version skew.

#### G5 — Dependencies Correct

- Phase `dependsOn: []` — correct; this is the plan's only phase, no prior phase needed.
- Child tasks depend on the same 11 SPEC-MAPPING-* cards — correct; both audits require all mapping specs to exist.
- No circular references: parent plan → phase → tasks → specs (leaf nodes).
- No missing dependency that would block task execution.

#### G6 — No Weakening

- Phase status is `needs-agent-review` — not prematurely accepted.
- Child tasks are both `complete` but explicitly marked "ready for review rather than acceptance."
- No exit criterion was relaxed, deleted, or replaced with weaker language.
- Success criteria are strongly worded ("every," "must," "reject," "become") — no hedging.
- No implementation work proceeds from unreviewed gaps per both task descriptions.

#### Residual Risks / Observations

- Both child tasks acknowledge their audit scope is bounded (completeness depends on Sage version; mathematical audit covers 10 delegated fixes, not exhaustive review). This is transparent and appropriate.
- The phase card itself is a single phase with no sibling phases — serial execution is implicit and correct.
- Recommendation: mark phase `accepted` after human review confirms the two child task audits are satisfactory.
