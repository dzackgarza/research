---
trackerStatus:
  type: plan
title: Duck-type object-shape probe audit
status: approved
planId: SPR-DUCKTYPE-AUDIT-20260505
planType: sprint-plan
priority: critical
owner: Zack
created: '2026-05-05'
updated: '2026-05-05'
progress: 0
tags:
- category-specs
- plan
- audit
- implementation
- theme-audit-uniformity
parentPlan: PLN-AUDIT-000
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

- `.agents/tasks/implementation/task_20260505_audit_category_spec_duck_type_object_shape_probes.md`

## Acceptance Criteria

- [ ] Category-spec implementation files are scanned for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- [ ] Each finding is classified as documented Sage interop, real type/category dispatch,
  wrapper-boundary access, or invalid duck-type probing.
- [ ] Invalid duck-type probing is fixed in owner-scoped patches or split into concrete
  implementation cards when the remediation is not atomic.
- [ ] No unrelated smoke implementation card is blocked merely because this audit work
  remains outstanding.
