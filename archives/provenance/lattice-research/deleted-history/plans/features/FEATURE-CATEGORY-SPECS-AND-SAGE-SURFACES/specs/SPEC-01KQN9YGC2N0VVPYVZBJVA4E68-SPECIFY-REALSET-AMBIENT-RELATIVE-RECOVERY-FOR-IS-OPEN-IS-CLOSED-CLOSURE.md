---
id: SPEC-01KQN9YGC2N0VVPYVZBJVA4E68-SPECIFY-REALSET-AMBIENT-RELATIVE-RECOVERY-FOR-IS-OPEN-IS-CLOSED-CLOSURE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Specify RealSet ambient-relative recovery for is_open is_closed closure interior
  and boundary through TopologicalSpaces
status: complete
priority: critical
requirement: The deleted Topological Spaces triage recorded settled topological constructor
  placement and remaining smoke design work for RealSet ambient recovery and metric
  examples.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass.
- Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- Prove RealSet method recovery through the ambient-relative route, not by adding
  pure topological constructors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify RealSet ambient-relative recovery for is_open is_closed closure interior and boundary through TopologicalSpaces
## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining smoke design work for RealSet ambient recovery and metric examples.

## Source Provenance

- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Specify RealSet ambient-relative recovery for is_open is_closed closure interior and boundary through TopologicalSpaces from category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical smoke examples are still needed for Connected, Compact, and Metric().Complete().

## Grounded Spec Contract

Canonical source anchors for this spec are already present:

- `category_specs/topological_spaces/docs/MAPPING.md`, `Root Topological Method Mapping`
  rows for:
  - `RealSet.is_open() -> X.is_open(U: Subset) -> bool`
  - `RealSet.is_closed() -> X.is_closed(U: Subset) -> bool`
  - `RealSet.closure() -> X.closure(U: Subset) -> Subset`
  - `RealSet.interior() -> X.interior(U: Subset) -> Subset`
  - `RealSet.boundary() -> X.boundary(U: Subset) -> Subset`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` rows for:
  - `RealSet.is_open`
  - `RealSet.is_closed`
  - `RealSet.closure`
  - `RealSet.interior`
  - `RealSet.boundary`
  - `RealSet.ambient`
- `category_specs/sets/docs/MAPPING.md` and
  `category_specs/topological_spaces/docs/MAPPING.md` constructor-routing rows keeping
  named real-line subset constructors under `Sets().Constructors()`

Spec decision fixed by these sources:

- owner category: `TopologicalSpaces()` owns the public surfaces
  `is_open`, `is_closed`, `closure`, `interior`, and `boundary`
- subject shape: each method is ambient-relative, taking a subset `U` of an ambient
  topological space `X`; the public recovery route for a `RealSet` subset is
  `U.ambient().method(U)`
- constructor ownership stays in `Sets().Constructors()`; this card must not introduce
  `TopologicalSpaces().Constructors()` or a direct pure-topology `RealSet` constructor

Required hypotheses and return/codomain obligations:

- hypothesis: `U` is a subobject/subset of the ambient topological space `X`
- `X.is_open(U)` and `X.is_closed(U)` return `bool`
- `X.closure(U)`, `X.interior(U)`, and `X.boundary(U)` return subsets of the same
  ambient space `X`, not bare Python containers and not detached set objects
- any convenience method on subset objects must be explicitly documented as delegation,
  not as a second owner for the topological notion

Rejection or retirement condition:

- reject any spec edit from this card that reassigns ownership to `Sets()`, introduces
  a pure topological constructor namespace, or treats `RealSet` no-argument methods as
  definition authority independent of their ambient space

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass.
- [ ] Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- [x] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Grounded Recovery Decision

Decision: RealSet topological methods recover through the ambient-relative
`TopologicalSpaces()` surface.

For a real subset `U`, the migration route is:

- `U.is_open()` becomes `U.ambient().is_open(U)`;
- `U.is_closed()` becomes `U.ambient().is_closed(U)`;
- `U.closure()` becomes `U.ambient().closure(U)`;
- `U.interior()` becomes `U.ambient().interior(U)`;
- `U.boundary()` becomes `U.ambient().boundary(U)`.

This pass recorded that route in `category_specs/topological_spaces/docs/MAPPING.md`
and documented the compatibility boundary in `category_specs/sets/subcategories/real_set.py`.
No `TopologicalSpaces().Constructors()` path or direct pure-topology `RealSet`
constructor was admitted. No `_RealSets` wrapper methods were added, because overriding
Sage's existing no-argument RealSet methods before the ambient methods have concrete
implementations would create a fragile compatibility layer rather than a mathematical
owner.

Validation note: global QC and smoke execution were skipped under the current
user-authorized skip-verification workflow for spec checkpoints.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Hermes Agent (independent reviewer)
**Protocol version:** 6-gate spec review (G1-G6)
**Spec:** SPEC-01KQN9YGC2N0VVPYVZBJVA4E68-SPECIFY-REALSET-AMBIENT-RELATIVE-RECOVERY-FOR-IS-OPEN-IS-CLOSED-CLOSURE

### G1 — Source Grounding

**Referenced local files verified present:**

| File referenced in spec | Actual path | Exists | Notes |
|---|---|---|---|
| TRIAGE.md (deleted, commit `8d1c21c`) | `plans/category_specs/topological_spaces/docs/TRIAGE.md` | Recoverable via `git show 8d1c21c^:plans/category_specs/topological_spaces/docs/TRIAGE.md` | PATH DISCREPANCY: spec line 36 says `category_specs/topological_spaces/docs/TRIAGE.md` (missing `plans/` prefix). The file existed under `plans/category_specs/...`, not directly under `category_specs/...`. Recoverable content confirms: the triage recorded "settled topological constructor placement" and "remaining smoke design work for RealSet ambient recovery" — matching spec lines 13-14. The migration line (spec line 37) accurately quotes the triage content. |
| MAPPING.md (topological_spaces) | `category_specs/topological_spaces/docs/MAPPING.md` | Yes — redirect stub (6 lines) pointing to tracked spec `SPEC-MAPPING-TOPOLOGICAL-SPACES.md` | Spec lines 51-57 reference "Root Topological Method Mapping" rows. Those rows now live in the tracked spec at `plans/features/.../specs/SPEC-MAPPING-TOPOLOGICAL-SPACES.md` lines 135-141. All five ambient-relative method rows confirmed: `is_open`, `is_closed`, `closure`, `interior`, `boundary` each with target shape, justification, and migration consequence. |
| SAGE_INVENTORY.md (topological_spaces) | `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` | Yes — 87 lines, 4 sections | Spec lines 58-64 reference inventoried rows for `RealSet.is_open`, `is_closed`, `closure`, `interior`, `boundary`, and `ambient`. All six confirmed at inventory lines 50-55. |
| MAPPING.md (sets) | `category_specs/sets/docs/MAPPING.md` | Yes — redirect stub (6 lines) pointing to tracked spec `SPEC-MAPPING-SETS.md` | Spec lines 65-67 reference constructor-routing rows. The sets mapping stub confirms the inventory is at `category_specs/sets/docs/SAGE_INVENTORY.md`. Constructor routing is maintained in the tracked sets spec. |
| `real_set.py` subcategory docstring | `category_specs/sets/subcategories/real_set.py` | Yes — 192 lines | Spec line 116: "documented the compatibility boundary in `category_specs/sets/subcategories/real_set.py`." Verified: docstring lines 35-40 explicitly state: "The project owner is the ambient-relative `TopologicalSpaces()` surface: `U.ambient().closure(U)`, `U.ambient().is_open(U)`, and analogous calls. This category records the real-subset representation; it does not create a second topological owner." Matches the spec's rejection condition (lines 88-92). |
| Decision card | `plans/features/.../decisions/DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING.md` | Yes — 199 lines | Cross-reference: confirms the warning-acceptance decision (lines 153-160), keeps `Sets().Constructors()` constructor surface, rejects catch-all `RealSet(...)` route. Independent confirmation that no `TopologicalSpaces().Constructors()` path was admitted. |
| Implementation task | `plans/features/.../tasks/TASK-01KQN9YGCD23ZSZDA3VT3BJ92E-IMPLEMENT-REALSET-NAMED-CONSTRUCTORS-AND-SMOKE-RECOVERY-THROUGH-AMBIENT.md` | Yes | Confirms the follow-up implementation task exists under `PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY`. |

**Referenced installed Sage source verified:**

| File | Path | Verified |
|---|---|---|
| Sage `real_set.py` | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/real_set.py` | Yes — `is_open` at line 2401, `is_closed` at 2422, `closure` at 2443, `interior` at 2458, `boundary` at 2475, `ambient` at 1472. Named constructors: `interval` (1690), `open` (1717), `closed` (1739), `point` (1761), `open_closed` (1782), `closed_open` (1807), `unbounded_below_closed` (1832), `unbounded_below_open` (1855), `unbounded_above_closed` (1878), `unbounded_above_open` (1902), `real_line` (1926). |

**G1 Verdict: PASS.** All referenced source files exist on disk. The TRIAGE.md path in the spec has a minor discrepancy (missing `plans/` prefix) but the content is recoverable and accurately paraphrased. All migration-route claims are backed by verifiable file content in MAPPING.md, SAGE_INVENTORY.md, real_set.py, and the decision card. The six Sage RealSet methods are confirmed in the installed Sage source.

### G2 — Sage Surface Completeness

**Cross-reference: Sage RealSet surfaces → spec coverage:**

| Sage surface (RealSet) | SAGE_INVENTORY line | Spec coverage | Accounted |
|---|---|---|---|
| `RealSet.is_open()` | Inventory line 50 | Spec lines 51-52: `RealSet.is_open() -> X.is_open(U: Subset) -> bool` | Yes — ambient-relative migration |
| `RealSet.is_closed()` | Inventory line 51 | Spec lines 53: `RealSet.is_closed() -> X.is_closed(U: Subset) -> bool` | Yes — ambient-relative migration |
| `RealSet.closure()` | Inventory line 52 | Spec lines 54: `RealSet.closure() -> X.closure(U: Subset) -> Subset` | Yes |
| `RealSet.interior()` | Inventory line 53 | Spec lines 55: `RealSet.interior() -> X.interior(U: Subset) -> Subset` | Yes |
| `RealSet.boundary()` | Inventory line 54 | Spec lines 56: `RealSet.boundary() -> X.boundary(U: Subset) -> Subset` | Yes |
| `RealSet.ambient()` | Inventory line 55 | Spec lines 63: `RealSet.ambient` (inventoried); spec lines 74-76: `U.ambient().method(U)` recovery route | Yes — ambient() is the bridge method |
| Named constructors (open, closed, point, open_closed, closed_open, unbounded_*, real_line, interval) | Inventory lines 39-49 | Spec lines 42-43: "named Sets().Constructors() paths" | Yes — constructor ownership delegated to Sets().Constructors() |
| Variadic `RealSet(*args)` | Inventory line 37 | Spec line 43: "variadic/manifold-producing paths are excluded" | Yes — explicit exclusion with rationale |

**Completeness check against deleted TRIAGE.md blockers:**

| TRIAGE.md item | Addressed in spec? | Evidence |
|---|---|---|
| `TopologicalSpaces().Constructors()` remains empty | Yes | Spec lines 41, 76-77, 119 |
| Root methods use ambient-relative shape | Yes | Spec lines 42, 51-57, 74-76 |
| No implementation/smoke yet proves recovery | Yes | Spec lines 99, 123-124: smoke is acceptance criterion #4 (unchecked) |
| Variadic/manifold paths excluded | Yes | Spec lines 43-44, 92 |
| Ball fields not metric; routed to topological ring/field | Yes | Spec line 45: "Real and complex ball fields are not Sage metric spaces" |

**G2 Verdict: PASS.** Every Sage RealSet topological surface from SAGE_INVENTORY.md is accounted for. All five topological predicates/transforms are mapped to ambient-relative migration routes. The ambient() bridge method is correctly identified as the recovery mechanism. Named constructors are correctly delegated to Sets().Constructors(). The variadic constructor and manifold paths are explicitly excluded. No orphaned Sage surface.

### G3 — Mathematical Correctness

**1. Ambient-relative predicate semantics (spec lines 42, 74-76):**

The spec correctly identifies that openness, closedness, closure, interior, and boundary are defined relative to an ambient topological space, not as intrinsic properties of a subset. For a subset U of a topological space X:
- U is open in X ⇔ U ∈ τ_X (the topology of X)
- U is closed in X ⇔ X\U is open in X
- closure_X(U) = ⋂{C closed in X : U ⊆ C}
- interior_X(U) = ⋃{O open in X : O ⊆ U}
- boundary_X(U) = closure_X(U) \ interior_X(U)

The migration from `U.is_open()` to `U.ambient().is_open(U)` is mathematically correct. Sage's `RealSet.is_open()` implicitly uses the real-line topology as the ambient space; the spec makes this relationship explicit and general.

**2. Hypothesis and codomain obligations (spec lines 80-86):**

All stated obligations are mathematically necessary:
- U must be a subobject of the ambient space X — otherwise the ambient-relative definitions don't apply.
- `is_open`, `is_closed` return `bool` — the truth value of a topological predicate.
- `closure`, `interior`, `boundary` return subsets of the same ambient space X — closure of a subset of X is a subset of X, not a detached object. Verified: Sage's `RealSet.closure()` returns a new `RealSet`, consistent with this requirement.
- Convenience methods on subset objects must be documented as delegation, not as a second owner — prevents ownership ambiguity.

**3. Constructor ownership (spec lines 41-42, 76-77, 88-92):**

The spec correctly enforces that `TopologicalSpaces().Constructors()` stays empty. Named real-line subsets are first sets, then refined into topological subobjects. The hierarchy is:
```
Sets().Constructors().OpenRealInterval(0, 1)  → refines into TopologicalSpaces().Subobjects()
```

This is mathematically sound: a set is constructed first, then acquires structure via category refinement. The spec's rejection conditions (lines 88-92) correctly prevent:
- Reassignment of topological ownership to `Sets()`
- Introduction of a pure topological constructor namespace
- No-argument RealSet methods as definition authority independent of ambient space

**4. Convenience method delegation (spec lines 85-86):**

Any convenience method on subset objects (e.g., `RealSet.is_open()` in Sage) must be documented as delegation to the ambient space's method. The real_set.py docstring (line 35-40) correctly documents this: "The project owner is the ambient-relative `TopologicalSpaces()` surface." This prevents the anti-pattern of two owners for the same mathematical notion.

**5. _RealSets wrapper rejection (spec lines 119-121):**

The spec correctly rejects adding category-level wrapper methods on `_RealSets` that override Sage's existing `RealSet` methods before ambient methods have concrete implementations. This is sound engineering: premature overrides create fragile compatibility layers. The spec instead records the migration route as a conceptual migration, not as an immediate code change.

**6. Return-type consistency:**

The spec correctly requires that `X.closure(U)`, `X.interior(U)`, and `X.boundary(U)` return subsets of X, not bare Python containers or detached set objects (line 83-84). This is consistent with the categorical notion that closure is an operation within the same category of topological spaces.

**G3 Verdict: PASS.** All mathematical claims are correct. The ambient-relative semantics match standard topological definitions. The category hierarchy (sets → construct → refine into topological subobjects) is logically sound. Rejection conditions are mathematically motivated. The migration route preserves mathematical meaning while correctly relocating ownership.

### G4 — Nonmathematical Rejection

| Rejection | Spec lines | Rationale assessment |
|---|---|---|
| Reassign topological ownership to `Sets()` | 88-89 | **Valid.** Openness/closedness are topological, not set-theoretic, notions. `Sets()` doesn't carry topology data. |
| Introduce pure topological constructor namespace | 89-90, 76-77 | **Valid.** `TopologicalSpaces().Constructors()` is empty by design. There is no generic topological-space constructor in Sage (confirmed: `topological_spaces.py` contains no `__init__`). Arbitrary topology data has no canonical constructor shape. |
| Treat RealSet no-argument methods as definition authority independent of ambient space | 91-92 | **Valid.** A subset is open *in* a space. The no-argument `RealSet.is_open()` implicitly queries the real-line topology, but this is a Sage convenience, not the mathematical definition. |
| Add `_RealSets` wrapper methods overriding Sage's existing RealSet methods before ambient implementations exist | 119-121 | **Valid.** Premature overrides without concrete ambient implementations create a fragile compatibility layer and hide the ownership migration. |

**G4 Verdict: PASS.** All four rejections are mathematically grounded and explicitly stated with rationale. The spec does not silently drop surfaces. Every rejection names the target, explains why it's rejected, and states the correct alternative.

### G5 — Ambiguity Routing

| Ambiguity / Gap | Routed to | Assessment |
|---|---|---|
| Smoke execution not yet run (spec line 123-124) | Acceptance criterion #4 (line 99): "Run just smoke-file topological_spaces/smoketest.sage after topological-space work" — currently unchecked | **Correct.** The spec records smoke as a pending acceptance criterion. The validation note (line 123-124) transparently states: "global QC and smoke execution were skipped under the current user-authorized skip-verification workflow." This is not an ambiguity; it's a deferred verification step with a clear criterion. |
| TRIAGE.md path discrepancy | Spec line 36 references `category_specs/topological_spaces/docs/TRIAGE.md` but actual path was `plans/category_specs/topological_spaces/docs/TRIAGE.md` | **Minor.** Content is recoverable via the correct path. The spec's migration line (line 37) accurately quotes the triage content. Does not affect spec correctness. |
| No implementation yet proves ambient-recovery route | The spec is a specification, not an implementation. The ambient-recovery route is recorded in MAPPING.md and real_set.py (lines 35-40). Implementation is tracked separately via TASK-01KQN9YGCD23ZSZDA3VT3BJ92E. | **Adequate.** Spec-card scope is specification, not implementation. Follow-up work is correctly routed to a tracker item (spec line 18). |
| Ball fields as metric spaces | Spec line 45: "Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work." | **Correctly routed.** This is an explicit boundary, not an ambiguity. Ball-field topology is delegated to ring/field recovery path, not this spec. |

**G5 Verdict: PASS.** All gaps and ambiguities are routed to appropriate tracked items or explicitly bounded. The spec is transparent about what is deferred (smoke execution) and what is out of scope (ball fields, manifold paths). The TRIAGE.md path discrepancy is minor and does not affect content validity.

### G6 — Obligation Preservation

**Method surface audit:**

| Sage method | Sage real_set.py line | Preservation in spec | Weakening detected? |
|---|---|---|---|
| `RealSet.is_open()` | 2401 | → `X.is_open(U: Subset) -> bool` (spec line 52) | No — preserved with correct owner (TopologicalSpaces) |
| `RealSet.is_closed()` | 2422 | → `X.is_closed(U: Subset) -> bool` (spec line 53) | No |
| `RealSet.closure()` | 2443 | → `X.closure(U: Subset) -> Subset` (spec line 54) | No |
| `RealSet.interior()` | 2458 | → `X.interior(U: Subset) -> Subset` (spec line 55) | No |
| `RealSet.boundary()` | 2475 | → `X.boundary(U: Subset) -> Subset` (spec line 56) | No |
| `RealSet.ambient()` | 1472 | → `U.ambient()` bridge method (spec lines 63, 74-76) | No — preserved as the recovery bridge |

**Constructor obligation preservation:**

| Sage constructor | SAGE_INVENTORY line | Mapped to | Preserved? |
|---|---|---|---|
| `RealSet.open()`, `closed()`, `point()`, `open_closed()`, `closed_open()`, `unbounded_*()`, `real_line()`, `interval()` | Inventory lines 39-49 | `Sets().Constructors()` paths (spec lines 42-43, 65-67) | Yes — constructor ownership preserved in Sets() |

**Anti-weakening guards:**

- Spec lines 88-92: Explicit rejection conditions prevent future editorial weakening — no reassignment to Sets(), no pure topological constructor namespace, no ambient-independent no-argument methods as definition authority.
- Spec lines 129-131: "If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it." This forces proper tracking rather than ad-hoc weakening.
- Spec line 130: "Preserve the original source path in updates so future agents can trace why this item exists."

**G6 Verdict: PASS.** All six Sage RealSet topological methods are preserved in the spec with their correct mathematical owner (TopologicalSpaces) via the ambient-relative migration route. No method was weakened, deleted, or moved to an incorrect owner. Constructor obligations are preserved in Sets().Constructors(). The rejection conditions provide forward protection against future editorial erosion.

### Summary

| Gate | Description | Verdict | Evidence count |
|---|---|---|---|
| G1 | Source grounding — file existence | PASS | 8 local files + 1 Sage source verified |
| G2 | Sage surface completeness | PASS | 8 Sage surfaces accounted, 5 TRIAGE blockers addressed |
| G3 | Mathematical correctness | PASS | 6 mathematical validity checks |
| G4 | Nonmathematical rejection | PASS | 4 explicit rejections with rationale |
| G5 | Ambiguity routing | PASS | 4 gap/ambiguity routings verified |
| G6 | Obligation preservation | PASS | 6 methods + constructor family preserved |

**Overall: 6/6 gates PASS.**

The spec is mathematically sound, source-grounded, and preserves all Sage RealSet topological surfaces through the ambient-relative migration route. The category hierarchy correctly places topological ownership in `TopologicalSpaces()`, constructor ownership in `Sets().Constructors()`, and the ambient-relative bridge as the recovery mechanism. The real_set.py docstring independently confirms the ownership decision. No obligation was weakened without a grounded replacement.

**Minor finding:** The TRIAGE.md path in spec line 36 is missing the `plans/` prefix (references `category_specs/...` instead of `plans/category_specs/...`). Content is recoverable via the correct path and accurately paraphrased in the spec. Non-blocking; recommend correcting the path or documenting the discrepancy.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recorded the RealSet ambient-relative recovery route in topological-space
  mapping and the real-set spec docstring. Kept Sage no-argument RealSet methods as
  compatibility methods rather than adding overriding wrappers.
