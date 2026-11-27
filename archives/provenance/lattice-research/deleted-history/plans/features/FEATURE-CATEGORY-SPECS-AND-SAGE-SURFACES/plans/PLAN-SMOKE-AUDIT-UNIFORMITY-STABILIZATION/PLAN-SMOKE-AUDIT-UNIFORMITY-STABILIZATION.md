---
id: PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Smoke audit uniformity and global stabilization
status: in-progress
priority: critical
owner: Zack
description: Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper,
  type, and anti-slop compliance work so it supports the foundational plan instead
  of becoming a disconnected cleanup backlog.
successCriteria:
- Smoke failures are routed to spec, implementation, research, or decision cards by
  mathematical cause.
- Audit cards link to the plan or source map whose correctness they protect.
- Audit coverage includes duck-typed object-shape probes where category-spec code
  should match real Sage/project types, documented wrappers, or category membership.
- '`/home/dzack/ai/quality-control/vulture_whitelist.py` remains global QC tooling
  support, not a planning document.'
- Compliance findings are not buried in chat or loose TODO files.
phases:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Smoke audit and uniformity stabilization

## Objective

Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper, type, and anti-slop compliance work so it supports the foundational plan instead of becoming a disconnected cleanup backlog.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Source corpus

- `plans/LATTICE_STYLE_GUIDE.md`
- `plans/lattice_redesign_corrections_spec.md`
- `/home/dzack/ai/quality-control/vulture_whitelist.py`
- Existing smoke and variadic sprint plans under `plans/features/`.
- Existing implementation cards under `plans/features/`.

## Priority rule

Audit work is critical when it prevents downstream poisoning: wrong definitions, wrong method ownership, stale docs, broad variadic surfaces, fake wrappers, or public APIs that make future work implement the wrong mathematics. Routine formatting and presentation cleanup is not critical.

## Subplans

- `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`: variadic signature closure across modules, rings, tensors, algebras, lattices, posets, sets, and RealSet constructors.
- `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`: object-shape probing audit for `getattr`/`hasattr`
  patterns that should be real type/category dispatch.

Leaf task ownership is encoded by `parents` containment under phase cards; this parent
plan should not own executable cards directly.

## Acceptance Criteria

- [ ] Smoke failures are routed to spec, implementation, research, or decision cards by mathematical cause.
- [ ] Audit cards link to the plan or source map whose correctness they protect.
- [ ] Audit coverage includes duck-typed object-shape probes where category-spec code
  should match real Sage/project types, documented wrappers, or category membership.
- [ ] `/home/dzack/ai/quality-control/vulture_whitelist.py` remains global QC tooling support, not a planning document.
- [ ] Compliance findings are not buried in chat or loose TODO files.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (independent subagent review)

**Gates passed:** G2 (exit criteria checkable), G4 (scope containment), G6 (no weakening)
**Gates with findings:** G1 (source grounding — 2 dead links), G3 (phase inventory incomplete), G5 (dependencies misaligned)
**Outcome:** revision-required (fixable in-card; not a DAG exhaustion)

---

#### G1 — Source Grounding: FAIL

The plan's Source corpus section (lines 50-54) lists five source anchors:

| Source | Status |
|--------|--------|
| `plans/LATTICE_STYLE_GUIDE.md` | **Not found.** Searched `find /home/dzack/research -name '*LATTICE_STYLE_GUIDE*'` — zero results. |
| `plans/lattice_redesign_corrections_spec.md` | **Not found.** Searched `find /home/dzack/research -name '*lattice_redesign_corrections_spec*'` — zero results. |
| `/home/dzack/ai/quality-control/vulture_whitelist.py` | **Exists.** Verified at 557 lines. |
| "Existing smoke and variadic sprint plans under `plans/features/`" | Vague. Not a specific file citation. |
| "Existing implementation cards under `plans/features/`" | Vague. Not a specific file citation. |

Two of five source citations are dead links (40% failure rate). The two "existing" references lack concrete paths, making them unverifiable. This violates the plan's own Definition Grounding Requirements (lines 38-46) which mandate recording exact source paths.

**Required:** Remove or correct the two dead links. Replace vague "existing" references with specific file paths or explicit wildcards that resolve to real files.

#### G2 — Exit Criteria Checkable: PASS (with note)

All five acceptance criteria (lines 71-76) are concretely verifiable:

1. **Smoke failures routed by mathematical cause** — verifiable by inspecting smoke failure cards and checking that each links to a spec/implementation/research/decision card with a cause statement. Slightly subjective ("mathematical cause") but operationally checkable.
2. **Audit cards link to plan or source map** — verifiable by inspecting `parents`/`dependsOn` fields and body links in audit cards.
3. **Audit coverage includes duck-typed object-shape probes** — verifiable via the phase-level audit results already recorded in child tasks.
4. **vulture_whitelist.py remains global QC tooling** — verifiable by file inspection; the file exists and is not a planning document.
5. **Compliance findings not buried in chat or loose TODOs** — verifiable by checking that findings appear in tracker cards.

_Note:_ Criterion 1 ("by mathematical cause") could use a sharper operational definition (e.g., "each smoke failure card's body contains a `Cause:` section citing a spec line, a Sage source line, or a decision card ID"), but is acceptable as-is.

#### G3 — Phase Inventory Completeness: FAIL

The frontmatter `phases` array (line 24-25) lists exactly one phase:

```yaml
phases:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
```

The Subplans section (lines 62-64) of the body lists two phases:

1. `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`
2. `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`

**Finding 1:** `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` is missing from the frontmatter `phases` array. Either the frontmatter should include it, or the body should not claim it as a subplan.

**Finding 2:** `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` does not exist as a directory or file under this plan's workspace (`.../PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/`). It was found under `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/`, a sibling plan under the same feature. This means:

- If the variadic audit phase is meant to be owned by this plan, its directory must be created here.
- If it is intentionally cross-plan, the plan body should state that explicitly and the dependency edge should be recorded in `dependsOn`, not listed as a subplan.
- The body text says "Leaf task ownership is encoded by parents containment under phase cards; this parent plan should not own executable cards directly" (lines 66-67) — yet the plan currently owns only one phase directory. Listing a phase that lives under another plan as a subplan creates ambiguity about ownership and execution authority.

**Current phase inventory vs. declared scope:** The plan's description promises "smoke-frontier, audit, variadic-signature, import hygiene, wrapper, type, and anti-slop compliance work" but the only active phase is duck-type probe audit. Variadic signature audit lives under a different plan. Import hygiene, wrapper, type, and anti-slop compliance have no phases at all.

#### G4 — Scope Containment: PASS

The plan's scope is defined by:

- **Objective (line 33):** "Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper, type, and anti-slop compliance work so it supports the foundational plan."
- **Priority rule (lines 57-58):** Critical when preventing downstream poisoning; routine formatting/presentation cleanup is not critical.

The existing child phase (`PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`) is clearly within scope — it audits object-shape probing that could cause wrong mathematical dispatch. Its tasks are bounded:
- TASK-20260505: scoped to `category_specs/` only.
- TASK-20260506: scoped to three specific set-wrapper files.
- TASK-WRAPUP: standard phase-closure procedure.

No evidence of scope creep in implemented work. The plan body's scope description is broader than the current phase inventory (see G3), but that's an inventory completeness issue, not a scope containment violation — the existing phase stays within declared bounds.

#### G5 — Dependency Correctness: FAIL

**Finding 1:** The plan's `dependsOn: []` is correct — no upstream plan dependencies beyond the parent feature.

**Finding 2:** The parent feature (`FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`) correctly lists this plan in its `plans` array. The feature declares no `dependsOn`, and the plan is properly contained.

**Finding 3:** The body references `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` as a subplan, but that phase exists under `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION`. This creates an implicit cross-plan dependency that is:
- Not declared in `dependsOn` (the plan says `dependsOn: []`)
- Not tracked as a formal edge
- Ambiguous: does this plan own the variadic work, or does the other plan? If shared, the dependency should be explicit.

**Finding 4 (inherited from child phase):** The child phase `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` has a circular self-dependency in its wrapup task (`TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` line 10 lists itself in `dependsOn`). While not a direct plan-level error, it blocks phase closure and therefore blocks this plan's completion.

#### G6 — No Weakening: PASS

The plan explicitly states it "does not authorize definitions by itself" (lines 36-39) and requires source grounding before any spec edits. It adds audit and stabilization governance without deleting, relaxing, or bypassing any existing:

- Specification definitions
- Smoke assertions
- Abstract method obligations
- Constructor requirements
- Downstream feature exit criteria

The child phase's review log confirms no spec/smoke weakening occurred in its tasks. The plan is additive governance, not scope reduction.

---

#### Residual Risks

- The plan currently owns only one phase (duck-type probe audit). The variadic signature audit is referenced but lives elsewhere. If the variadic audit fails or is abandoned under its owning plan, this plan's scope claim becomes misleading — it would appear to have declared but not executed variadic work.
- The plan description mentions "import hygiene" and "anti-slop compliance" but no phases or tasks address these areas. They may be covered by existing enforcement tooling (linters, `just plan-validate`), but if manual audit work is intended, it is not represented in the phase inventory.
- `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` is in `needs-human-input` status with one child task still `needs-human-input` (TASK-20260505) and a wrapup task with a circular self-dep. The plan cannot close until its sole phase resolves.

---

#### Required Remediation

1. **Fix G1 dead links:** Remove or correct `plans/LATTICE_STYLE_GUIDE.md` and `plans/lattice_redesign_corrections_spec.md`. Replace vague "existing" references with concrete paths.
2. **Resolve G3 inventory:** Either add `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` to the `phases` frontmatter array (and create its directory under this plan, or explicitly document the cross-plan arrangement), or remove it from the Subplans section if it is not owned by this plan.
3. **Address scope gaps:** Either add phases for import hygiene and anti-slop compliance, or narrow the description/objective to reflect only what is actually planned.
4. **Fix inherited G5 circular dependency:** Remove `TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` from its own `dependsOn` list (child phase issue, but blocks this plan's completion).
5. After fixes, re-validate G1, G3, G5.

### Status correction 2026-05-09

Human feedback reclassified these findings as agent-owned plan maintenance. Dead
source links, mismatched phase inventory, and circular dependencies are not user
decisions. Keep this plan `in-progress` while the concrete remediation above is
performed; return to human review only if cleanup exposes a real audit-governance
choice that is not determined by the existing workflow.
