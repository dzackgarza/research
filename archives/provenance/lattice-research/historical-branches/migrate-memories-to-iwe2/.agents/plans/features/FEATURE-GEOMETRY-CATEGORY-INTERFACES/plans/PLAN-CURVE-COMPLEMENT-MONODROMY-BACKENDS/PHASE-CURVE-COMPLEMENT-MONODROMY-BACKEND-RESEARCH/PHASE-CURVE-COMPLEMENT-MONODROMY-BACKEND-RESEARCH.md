---
id: PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
trackerStatus:
  type: phase
parents:
- '[[PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS]]'
dependsOn: []
title: Curve complement and monodromy backend research
status: complete
description: 'This phase groups current cards that were previously attached directly
  to `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` or to the corresponding legacy `.agents`
  work queue. It is a routing phase: executable work remains in child task cards,
  while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete only after blockers are resolved, or after the
  original card is superseded by a linked successor that remains active; blocked child
  cards do not satisfy phase acceptance.
- Any mathematical spec changes cite their source grounding before implementation
  proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
---
# Curve complement and monodromy backend research

## Summary

This phase groups current cards that were previously attached directly to `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete only after blockers are resolved, or after the
      original card is superseded by a linked successor that remains active; blocked
      child cards do not satisfy phase acceptance.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

## Work Log

- 2026-05-06: Started phase execution with
  `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`.

---

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate review)

**Gates passed:** G1, G2, G3, G4, G5
**Gates failed:** G6 (partial — fixable findings)
**Outcome:** PASS WITH FINDINGS — phase is structurally sound, child tasks align with exit criteria, but two minor fixable issues identified.

---

#### G1 — Source Grounding / Definition Grounding

PASS.

- Parent plan `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` exists at the expected path, is status `needs-agent-review`, and lists this phase in its `phases` array (line 24).
- All five child tasks reference `PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH` as their sole parent in `parents:`.
- Each research task cites specific upstream sources (Sage RiemannSurface source at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`, ore_algebra clone at `/tmp/tmp.EtH8Hu3zIu/ore_algebra`, Noether-Lefschetz `foliation.lib`, Sirocco upstream README/source).
- Each research task produced a tracked follow-up spec or decision card. All five referenced follow-up cards confirmed present:
  - `specs/SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING.md`
  - `specs/SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP.md`
  - `specs/SPEC-ORE-ALGEBRA-BACKEND-MAPPING.md`
  - `specs/SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md`
  - `specs/SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING.md`
  - `decisions/DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE.md`
- No orphan or dangling references detected.

#### G2 — Exit Criteria Checkable

PASS.

All three phase success criteria are concrete and verifiable:

1. "Child task cards are complete only after blockers are resolved..." — checkable: each child task's `status` and `blocked_reason` can be audited.
2. "Any mathematical spec changes cite their source grounding before implementation proceeds." — checkable: each produced spec can be inspected for source citations.
3. "Follow-up work is filed as tracked cards under root `plans/features/`." — checkable: all follow-ups are in `specs/` or `decisions/` subdirectories of the owning feature.

No hand-wavy or unmeasurable criteria.

#### G3 — Task Inventory Complete

PASS.

Five child tasks exist under `tasks/`:

| Task | Status | Covers |
|------|--------|--------|
| `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE` | `needs-human-input` | Riemann surface / period-lattice backend research |
| `TASK-RESEARCH-ORE-ALGEBRA-INTERFACE` | `needs-human-input` | Ore algebra backend research |
| `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES` | `needs-human-input` | Picard-Fuchs / monodromy JNF research |
| `TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS` | `needs-human-input` | Sirocco curve-complement research |
| `TASK-WRAPUP-PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH` | `unstarted` | Phase wrap-up / audit / cleanup |

The four research tasks cover the five backend domains named in the parent plan: curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs/monodromy. The wrap-up task handles phase closure (status audit, meta-review, skill updates, git organization). Coverage is 1:1 against the parent plan's objective.

Note: the phase card frontmatter does not include a `tasks:` array enumerating its children. The project convention (observed in `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`) is to list child tasks in the frontmatter. This is a minor metadata gap — the linkage is preserved via the `parents` field in each child task, but adding a `tasks:` array would improve machine readability.

#### G4 — No Scope Creep

PASS.

- All four research tasks are explicitly bounded to source-admission research: read upstream docs/source, identify candidate constructors/methods, determine integration need, and create follow-up cards. None performs implementation.
- Each research task contains an explicit boundary: "Do not implement a wrapper in this card" (Sirocco), "Do not vend or wrap ore_algebra" (ore_algebra), "Do not implement monodromy or Picard-Fuchs computation" (Picard-Fuchs), "Do not design a variadic or convenience wrapper. Do not implement code." (Sage Riemann).
- The wrap-up task is audit/cleanup only — no implementation work.
- No leaked concerns (performance, deployment, UX, Sage version upgrades) beyond acknowledged environmental gaps (ore_algebra local import failure, Sage version skew risk).

#### G5 — Dependencies Correct

PASS (with one noted self-reference).

- Phase `dependsOn: []` — correct; no prior phase needed within this plan. The parent plan depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map discipline, which is appropriate.
- Research tasks all have `dependsOn: []` — correct; they are independently executable research tasks.
- DAG is acyclic: parent plan → phase → tasks → specs/decisions (leaf nodes).
- **Finding:** `TASK-WRAPUP-PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH` lists itself in its own `dependsOn` array (line 12: `'[[TASK-WRAPUP-PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'`). This is a circular self-reference. It also correctly depends on the four research tasks. The self-reference should be removed — it is a copy-paste artifact and does not break execution (the task is `unstarted` and explicitly gated on sibling completion), but it violates DAG hygiene.

#### G6 — No Weakening / Style and Compliance

PASS WITH FINDINGS.

- Phase status is `needs-agent-review` — appropriate; not prematurely accepted.
- No exit criterion was relaxed, deleted, or replaced with weaker language.
- Three research tasks are in `needs-human-input` (not `complete`), which is correct — their review logs explicitly state "human approval remains required before marking the card complete."
- The wrap-up task is `unstarted`, which is correct — its body states "Do NOT execute this task while sibling tasks are still in-progress or needs-agent-review."
- **Finding 1 (G6):** Three of four research tasks are in `needs-human-input` status. The wrap-up task gates on `in-progress` or `needs-agent-review` statuses; `needs-human-input` is technically neither, but semantically these tasks are not complete. The wrap-up's gating language should explicitly include `needs-human-input` as a blocking status, or the research tasks should be normalized to `needs-agent-review` to match the phase's convention.
- **Finding 2 (G3/G6):** The phase card lacks a `tasks:` array in its YAML frontmatter. Other phase cards in the repository (e.g., `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`) include this for machine enumeration. This is not a breaking defect but reduces DAG machine-readability.

---

#### Residual Risks / Observations

- All four research tasks underwent independent 6-gate review at the task level and either passed all gates or were reworked and re-reviewed to pass. The review logs in each task card show concrete evidence of gate-level scrutiny.
- The `needs-human-input` status on research tasks means a human must still approve the research findings before the phase can close. This is a deliberate gate, not a defect.
- The ore_algebra research task records a concrete negative finding: local import fails with `ImportError: cannot import name Category`. This satisfies the parent plan's requirement for negative findings in the five-field format (capability, boundary, evidence, consequence, follow-up).
- The Picard-Fuchs research correctly separates two distinct mathematical routes (numerical analytic via Sage RiemannSurface vs. Picard-Fuchs/Gauss-Manin operator route) and records that they should not be conflated.
- The Sirocco and Sage Riemann tasks both required Gate 2 rework (follow-up cards were initially inline prose rather than tracked cards) and were successfully re-reviewed. This demonstrates the review process is working.

---

#### Summary

The phase card is well-structured: all five planned backend domains are covered by research tasks, each task produced tracked follow-up cards, and no implementation work has leaked into the research phase. Two fixable issues:

1. **Remove the self-reference** from `TASK-WRAPUP-PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH`'s `dependsOn` array (line 12).
2. **Add a `tasks:` array** to the phase card frontmatter enumerating the five child tasks for machine readability.

These are non-blocking. The phase can be accepted once the four research tasks receive human approval.
