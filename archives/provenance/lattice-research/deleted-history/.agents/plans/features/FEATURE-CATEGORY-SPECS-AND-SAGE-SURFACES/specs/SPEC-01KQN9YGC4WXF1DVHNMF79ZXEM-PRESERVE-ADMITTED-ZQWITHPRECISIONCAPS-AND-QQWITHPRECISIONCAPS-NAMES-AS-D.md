---
id: SPEC-01KQN9YGC4WXF1DVHNMF79ZXEM-PRESERVE-ADMITTED-ZQWITHPRECISIONCAPS-AND-QQWITHPRECISIONCAPS-NAMES-AS-D
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
title: Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred
  Sage-gap frontiers with exact gap assertions
status: complete
priority: critical
requirement: Rings mapping records constructor namespace decisions, split p-adic and
  q-adic precision routes, matrix-ring ownership, topological ring inheritance, and
  deferred q-adic lattice-precision gaps.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- The implementation blocker is the preserved Sage-gap frontier recorded in `rings/docs/MAPPING.md`;
  no new implementation card was created because this leaf exists to keep the admitted
  names deferred until a real Sage route exists.
- For q-adic precision items, preserve the five-field negative finding format when
  updating evidence.
- This is not topological-ring work; the owner remains the ring constructor namespace.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Grounded Review Outcome

Sources: `category_specs/rings/docs/MAPPING.md`,
`category_specs/rings/docs/SAGE_INVENTORY.md`, and the migrated source line named in
`Source Provenance`.

The naming decision is already grounded and should be preserved: `ZqWithPrecisionCaps`
and `QqWithPrecisionCaps` remain admitted split constructor names under
`Rings().Constructors()` as deferred Sage-gap frontiers, parallel to the concrete
`ZpWithPrecisionCaps` and `QpWithPrecisionCaps` routes.

Grounded owner and hypothesis rule:

- the owner category remains the rings constructor namespace, not a valuation-only
  side API;
- the intended hypotheses are unramified q-adic extension construction with lattice
  relative/absolute precision caps, matching the mathematically meaningful split
  already used for p-adic base constructors;
- the intended codomain is the corresponding q-adic ring or field parent refined into
  the local valued/complete ring surface once Sage exposes a working constructor path.

Deferred review outcome:

- no new public mathematical meaning is needed on this card;
- the exact five-field negative finding already recorded in `rings/docs/MAPPING.md`
  is the source of truth for why these names stay deferred;
- future work on this leaf is limited to replacing the deferred-gap assertion with a
  source-backed working Sage route or upstream fix, not renaming or deleting the split
  names.
- `category_specs/rings/__init__.py` already preserves the admitted public names and
  asserts the installed Sage gap in both `ZqWithPrecisionCaps(...)` and
  `QqWithPrecisionCaps(...)`; this card does not replace those assertions with a fake
  implementation path.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] The implementation blocker is the preserved Sage-gap frontier recorded in `rings/docs/MAPPING.md`; no new implementation card was created because this leaf exists to keep the admitted names deferred until a real Sage route exists.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] This is not topological-ring work; the owner remains the ring constructor namespace.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Confirmed the existing spec state: `rings/docs/MAPPING.md` owns the
  five-field negative finding, `rings/__init__.py` preserves both deferred constructor
  names with explicit gap assertions, and the card is ready for review without
  introducing a fake q-adic lattice-precision implementation path.

## 6-Gate Protocol Review Log

### Review — 2026-05-07 (subagent, 6-gate spec card review)

**Spec card**: SPEC-01KQN9YGC4WXF1DVHNMF79ZXEM-PRESERVE-ADMITTED-ZQWITHPRECISIONCAPS-AND-QQWITHPRECISIONCAPS-NAMES-AS-D
**Parent feature**: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
**Reviewer**: Hermes Agent (independent subagent, deepseek-v4-pro)
**Method**: 6-gate protocol (G1 source grounding, G2 Sage surface completeness, G3 mathematical correctness, G4 nonmathematical rejection, G5 ambiguity routing, G6 obligation preservation)

---

#### G1 — Source Grounding: PASS

**Referenced local files verified present:**

| File referenced in spec | Actual path | Exists | Notes |
|---|---|---|---|
| `category_specs/rings/docs/MAPPING.md` | `/home/dzack/research/category_specs/rings/docs/MAPPING.md` | Yes — 7-line redirect | Redirects to canonical tracked spec `SPEC-MAPPING-RINGS.md`. The canonical spec contains the full five-field negative finding for q-adic lattice precision at lines 378-431. |
| `category_specs/rings/docs/SAGE_INVENTORY.md` | `/home/dzack/research/category_specs/rings/docs/SAGE_INVENTORY.md` | Yes | Rings Sage inventory file exists, documents Sage ring category surfaces. |
| `category_specs/rings/__init__.py` | `/home/dzack/research/category_specs/rings/__init__.py` | Yes — 2048 lines | Contains all four admitted constructor names: `ZpWithPrecisionCaps` (line 968), `QpWithPrecisionCaps` (line 1085), `ZqWithPrecisionCaps` (line 1297), `QqWithPrecisionCaps` (line 1465). |
| SPEC-MAPPING-RINGS.md | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md` | Yes | Line 214 records the deferred split names. Lines 378-431 contain the full five-field negative finding for q-adic lattice precision. Lines 507-548 document verified negative findings and the p-adic/q-adic dispatch split. |

**Verified code state:**

| Constructor | File location | Implementation state | Verified |
|---|---|---|---|
| `ZpWithPrecisionCaps(...)` | `rings/__init__.py` line 968 | Concrete — delegates to Sage `Zp(..., type='lattice-cap')` | Yes — active implementation path |
| `QpWithPrecisionCaps(...)` | `rings/__init__.py` line 1085 | Concrete — delegates to Sage `Qp(..., type='lattice-cap')` | Yes — active implementation path |
| `ZqWithPrecisionCaps(...)` | `rings/__init__.py` line 1297 | **Deferred** — `assert False` with gap message (line 1325-1329) | Yes — asserts "Installed Sage has no unramified Zq extension constructor for split lattice relative/absolute precision caps" |
| `QqWithPrecisionCaps(...)` | `rings/__init__.py` line 1465 | **Deferred** — `assert False` with gap message | Yes — matching gap assertion |

**G1 Verdict**: PASS. All four source files exist and are verifiable. The code preserves both deferred constructor names with explicit gap assertions that match the spec's deferred-gap frontier description exactly. The concrete `ZpWithPrecisionCaps` and `QpWithPrecisionCaps` routes are implemented and working. The five-field negative finding is present in the canonical mapping spec (SPEC-MAPPING-RINGS.md lines 378-431).

---

#### G2 — Sage Surface Completeness: PASS

**Cross-reference: Sage precision-cap surfaces → spec coverage:**

| Sage surface | Status | Spec coverage | Accounted |
|---|---|---|---|
| `Zp(..., type='lattice-cap')` | Concrete in Sage | `ZpWithPrecisionCaps(...)` — concrete project route | Yes |
| `Qp(..., type='lattice-cap')` | Concrete in Sage | `QpWithPrecisionCaps(...)` — concrete project route | Yes |
| `Zq(..., type='lattice-cap')` with split relative/absolute caps | **Gap** — no working Sage route | `ZqWithPrecisionCaps(...)` — deferred admitted name | Yes — gap documented |
| `Qq(..., type='lattice-cap')` with split relative/absolute caps | **Gap** — no working Sage route | `QqWithPrecisionCaps(...)` — deferred admitted name | Yes — gap documented |
| `Zq(..., type='lattice-cap')` scalar precision only | Concrete in Sage | `Zq(...)` — separate scalar route, not this leaf | Yes — split maintained |
| `Qq(..., type='lattice-cap')` scalar precision only | Concrete in Sage | `Qq(...)` — separate scalar route, not this leaf | Yes — split maintained |

**Hypothesis and codomain coverage:**

| Requirement | Spec reference | Verified |
|---|---|---|
| Owner is rings constructor namespace, not valuation-only side API | Spec lines 62-64 | Correct — `Rings().Constructors()` |
| Intended hypotheses: unramified q-adic extension with lattice relative/absolute precision caps | Spec lines 64-67 | Correct — matches p-adic split pattern |
| Intended codomain: q-adic ring or field parent refined into local valued/complete ring surface | Spec lines 67-69 | Correct |
| Split between scalar and lattice-cap routes preserved | Spec line 33, code verification | Correct — separate constructor names |

**G2 Verdict**: PASS. Every Sage precision-cap surface (both concrete p-adic and gapped q-adic) has a documented mapping. The split between scalar precision and lattice-cap routes is properly maintained in both the spec and code.

---

#### G3 — Mathematical Correctness: PASS

**p-adic/q-adic split analysis:**

The mathematical distinction between p-adic (prime base) and q-adic (prime-power base, unramified extension) rings is standard in local/global field theory. The project correctly:
1. Admits `ZpWithPrecisionCaps` and `QpWithPrecisionCaps` as concrete constructors because Sage's `Zp(..., type='lattice-cap')` and `Qp(..., type='lattice-cap')` canonicalize lattice precision pairs
2. Retains `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` as deferred admitted names because installed Sage lacks a working unramified q-adic extension constructor with split lattice relative/absolute precision caps

The five-field negative finding format (SPEC-MAPPING-RINGS.md lines 378-431) correctly records: the Sage upstream evidence collected, the attempted routes that fail, the analogous p-adic routes that work, the exact error messages, and the gap classification. This preserves mathematical correctness without fabricating a false implementation.

**No mathematical error detected.** The split is meaningful: p-adic fields are prime-base completions; q-adic fields are unramified extensions of degree `f` over a p-adic field where `q = p^f`. Sage's concrete lattice-cap support for the prime-base case does not extend to the extension case — this is an upstream Sage gap, not a project mathematical error.

**G3 Verdict**: PASS. The p-adic/q-adic split is mathematically correct. The deferred status is justified by documented Sage upstream gaps, not by mathematical uncertainty.

---

#### G4 — Nonmathematical Rejection: PASS

**Rejected or avoided surfaces verified:**

| Surface | Spec reference | Rationale |
|---|---|---|
| Fake q-adic lattice-precision implementation path | Spec lines 79-81 | "this card does not replace those assertions with a fake implementation path" — VERIFIED: code uses `assert False` with gap message, not a stub that silently returns wrong results |
| Renaming or deleting the split names | Spec lines 76-77 | Future work limited to replacing gap assertion with working Sage route, not renaming |
| New subtree-local TRIAGE or process document | Acceptance criteria line 86, spec line 94 | No new TRIAGE.md created; follow-up as tracker items |
| Topological ring scope creep | Acceptance criteria line 89, spec line 26 | "This is not topological-ring work; the owner remains the ring constructor namespace" |

**G4 Verdict**: PASS. The spec correctly avoids nonmathematical shortcuts: no fake implementation, no renaming, no new process documents, and no scope creep into topological-ring territory. The deferred gap assertion is honest (`assert False`) rather than silently broken.

---

#### G5 — Ambiguity Routing: PASS

**Ambiguities routed:**

| Ambiguity | Routing | Status |
|---|---|---|
| q-adic lattice-precision gap | Five-field negative finding in SPEC-MAPPING-RINGS.md lines 378-431 | Documented with Sage upstream evidence, error messages, and attempted routes |
| Future implementation path | Spec lines 75-77: "limited to replacing the deferred-gap assertion with a source-backed working Sage route or upstream fix" | Clear constraint — no renaming or deletion |
| Missing mathematical owner | Spec lines 95-96: "split that as a new tracker item" | Routing policy stated |
| Constructor routing split (scalar vs lattice-cap) | Spec lines 33-34, code separation of `Zq(...)` scalar and `ZqWithPrecisionCaps(...)` lattice-cap | Clear — separate names, separate routes |

**G5 Verdict**: PASS. All q-adic lattice-precision ambiguities are routed to documented negative findings with explicit upstream Sage evidence. Future implementation path is constrained. No unresolved routing conflicts.

---

#### G6 — Obligation Preservation: PASS

**Checked for weakening patterns:**

- No constructor names deleted: Both `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` remain admitted in `rings/__init__.py`
- No gap assertions weakened: The `assert False` messages are explicit about the Sage gap, not softened to warnings or silent fallbacks
- No mathematical meaning narrowed: The deferred names preserve the full lattice-cap hypothesis (split relative/absolute caps), not downgraded to scalar precision
- No p-adic obligations dropped: `ZpWithPrecisionCaps` and `QpWithPrecisionCaps` remain concrete and working
- Sage compatibility preserved: The concrete routes delegate to Sage's canonicalize methods; the deferred routes would do the same once Sage exposes the extension path
- Five-field negative finding format preserved: SPEC-MAPPING-RINGS.md maintains the structured evidence

**G6 Verdict**: PASS. No constructor names, mathematical hypotheses, or gap assertions are weakened. The deferred status is honest and preserves the full intended mathematical surface.

---

### Summary

The SPEC-ZQWITHPRECISIONCAPS is a well-scoped preservation leaf. It correctly documents the p-adic/q-adic split in precision-cap constructors, keeps the concrete `ZpWithPrecisionCaps`/`QpWithPrecisionCaps` routes active, and preserves `ZqWithPrecisionCaps`/`QqWithPrecisionCaps` as deferred admitted names with honest gap assertions. The five-field negative finding in the canonical mapping provides thorough Sage upstream evidence for why the q-adic routes remain deferred.

**No findings or deficiencies.** All six gates pass. The spec correctly preserves the status quo without introducing fake implementations or losing mathematical obligations.

### Evidence Registry

| Evidence item | Verification method | Result |
|---|---|---|
| rings MAPPING.md | Filesystem check | Exists (redirect to SPEC-MAPPING-RINGS.md) |
| rings SAGE_INVENTORY.md | Filesystem check | Exists |
| rings/__init__.py — ZpWithPrecisionCaps | Direct code read, line 968 | Concrete implementation |
| rings/__init__.py — QpWithPrecisionCaps | Direct code read, line 1085 | Concrete implementation |
| rings/__init__.py — ZqWithPrecisionCaps | Direct code read, line 1297 | Deferred with `assert False` gap message |
| rings/__init__.py — QqWithPrecisionCaps | Direct code read, line 1465 | Deferred with `assert False` gap message |
| SPEC-MAPPING-RINGS.md — five-field finding | Direct read, lines 378-431 | Full Sage upstream evidence documented |
| SPEC-MAPPING-RINGS.md — ZqWithPrecisionCaps row | Direct read, line 214 | Deferred admitted names recorded |
| No new TRIAGE.md created | Filesystem search | Confirmed absent |
