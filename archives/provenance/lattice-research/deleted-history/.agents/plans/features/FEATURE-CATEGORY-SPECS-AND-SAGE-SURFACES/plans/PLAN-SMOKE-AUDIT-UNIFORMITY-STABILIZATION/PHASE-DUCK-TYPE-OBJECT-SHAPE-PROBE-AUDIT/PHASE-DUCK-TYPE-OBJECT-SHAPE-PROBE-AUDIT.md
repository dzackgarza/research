---
id: PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
trackerStatus:
  type: phase
parents:
- '[[PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION]]'
dependsOn: []
title: Duck-type object-shape probe audit
status: complete
priority: critical
description: Audit category-spec implementation surfaces for object-shape probing
  patterns that use `getattr`, `hasattr`, optional attribute fallbacks, or private-slot
  probes to infer what kind of mathematical/Sage object is present. Such branches
  must be replaced or routed through real Sage/project types, documented wrapper boundaries,
  or category membership.
successCriteria:
- Category-spec implementation files are scanned for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- Each finding is classified as documented Sage interop, real type/category dispatch,
  wrapper-boundary access, or invalid duck-type probing.
- Invalid duck-type probing is fixed in owner-scoped patches or split into concrete
  implementation cards when the remediation is not atomic.
- No unrelated smoke implementation card is blocked merely because this audit work
  remains outstanding.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
---
# Duck-type object-shape probe audit

## Objective

Audit category-spec implementation surfaces for object-shape probing patterns that use
`getattr`, `hasattr`, optional attribute fallbacks, or private-slot probes to infer what
kind of mathematical/Sage object is present. Such branches must be replaced or routed
through real Sage/project types, documented wrapper boundaries, or category membership.

## Scope

This sprint exists to prevent the current implementation pass from expanding into a
repo-wide style audit. Findings discovered during ordinary smoke work may be recorded
here and left for the audit phase unless they are the direct cause of the active smoke
failure being fixed.

## Source Provenance

- Repo style policy in `.agents/skills/category-spec-style/references/style.md`.
- Existing proof-audit warning in
  `.agents/skills/research-proof-auditing/references/proof-auditing.md` for avoiding
  `hasattr` in favor of typed checks.
- Lattice redesign audit criteria in
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- User correction on 2026-05-05: the issue is duck-type patterns instead of matching on
  real types.

## Child Cards

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT/tasks/TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT/tasks/TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES.md`

## Acceptance Criteria

- [ ] Category-spec implementation files are scanned for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- [ ] Each finding is classified as documented Sage interop, real type/category dispatch,
  wrapper-boundary access, or invalid duck-type probing.
- [ ] Invalid duck-type probing is fixed in owner-scoped patches or split into concrete
  implementation cards when the remediation is not atomic.
- [ ] No unrelated smoke implementation card is blocked merely because this audit work
  remains outstanding.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (independent subagent review)

**Gates passed:** G1 (source grounding), G2 (exit criteria checkable), G4 (no scope creep)
**Gates with findings:** G3 (task inventory incomplete), G5 (dependency errors), G6 (no weakening — passed)
**Outcome:** revision-required (fixable in-card; not a DAG exhaustion)

---

#### G1 — Source Grounding: PASS

The phase card cites four source anchors:

- `.agents/skills/category-spec-style/references/style.md` — file exists at expected path. Verified.
- `.agents/skills/research-proof-auditing/references/proof-auditing.md` — file exists at expected path. Verified.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` — file exists at expected path. Verified.
- User correction on 2026-05-05 — recorded in context. Acceptable as human directive.

All source anchors are real and reachable. No dangling references.

#### G2 — Exit Criteria Checkable: PASS

All four success criteria are concrete and falsifiable:

1. **Scan for patterns** — verifiable by static search (`rg getattr`, `rg hasattr`) on `category_specs/`.
2. **Classification** — verifiable by reviewing audit result tables in child tasks, each citing Sage source lines.
3. **Invalid probes fixed or carded** — verifiable by checking patches on implementation files and existence of follow-up card `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES`.
4. **No smoke card blocked** — verifiable by inspecting the dependency graph; `dependsOn: []` on this phase means no downstream smoke cards declare a dependency on this audit phase.

#### G3 — Task Inventory Completeness: FAIL (with finding)

The phase card's Child Cards section (lines 57-59) lists exactly two child tasks:

1. `TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES`
2. `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES`

A third task exists in the tasks directory and declares this phase as its parent:

3. `TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` (status: `unstarted`)

This task is **not listed** in the phase card's Child Cards section. The phase manifest is incomplete.

Additionally, `TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` has a **circular self-dependency** in its `dependsOn` list (line 10 of the wrapup card): it lists itself as a dependency. This is a structural error that would prevent any dependency-resolution engine from ever marking it ready.

**Child task status summary:**

| Task | Status | Review State |
|------|--------|-------------|
| TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES | `needs-agent-review` | Independent re-review passed G1-G6; pending human acceptance |
| TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES | `complete` | Review passed G1-G6 |
| TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT | `unstarted` | Not yet executed; has circular self-dep |

#### G4 — No Scope Creep: PASS

Phase scope states: "This sprint exists to prevent the current implementation pass from expanding into a repo-wide style audit."

Child tasks remain within bounds:
- TASK-20260505 scans `category_specs/` only, not the entire repo.
- TASK-20260506 is confined to three set-wrapper files routed from the first audit.
- The wrapup task is a standard phase-closure procedure, not additional audit scope.

No evidence of scope expansion during implementation.

#### G5 — Dependency Correctness: FAIL (with two findings)

**Finding 1:** `TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` has a circular self-dependency. Its `dependsOn` includes `'[[TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'` (line 10). This must be removed.

**Finding 2:** The phase card's `dependsOn: []` is correct — this phase has no upstream dependencies beyond its parent plan. However, the phase card's `status: needs-agent-review` is ambiguous while child tasks are in mixed states (one `needs-agent-review`, one `complete`, one `unstarted`). The phase cannot close until all children are resolved.

Otherwise, dependency edges are correct:
- Parent plan → Phase: correct (phase listed in plan's `phases` array).
- Phase → TASK-20260505: correct (child lists phase as parent, no deps).
- Phase → TASK-20260506: correct (child lists phase as parent, dependsOn TASK-20260505).
- Phase → TASK-WRAPUP: not recorded in phase manifest (see G3), but child's parents field is correct.

#### G6 — No Weakening: PASS

The phase adds audit coverage and does not delete, relax, or bypass any existing specification, smoke assertion, abstract method, or constructor obligation. Both child tasks explicitly record that no spec/smoke weakening occurred. The wrapup task (when executed) is a meta-review and cleanup task, not a scope-reduction mechanism.

---

#### Residual Risks

- The wrapup task's procedure includes meta-review of completed child cards. Since TASK-20260505 is still `needs-agent-review` (not `complete`/`done`), the wrapup's meta-review section would legitimately skip it — but if the phase is closed with TASK-20260505 still pending human acceptance, the wrapup may need to note that as an open item.
- `TASK-20260506` review log claims `just plan-validate` passes, but the parent audit task notes that full `just test` still lacks a clean signal due to pre-existing Sage/stub/type errors. This is a known residual, not a new finding.

---

#### Required Remediation (before phase can close)

1. **Add `TASK-WRAPUP-PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT` to the phase card's Child Cards section.**
2. **Remove the circular self-dependency from the wrapup task's `dependsOn` list.**
3. After fix, re-validate G3 and G5.
