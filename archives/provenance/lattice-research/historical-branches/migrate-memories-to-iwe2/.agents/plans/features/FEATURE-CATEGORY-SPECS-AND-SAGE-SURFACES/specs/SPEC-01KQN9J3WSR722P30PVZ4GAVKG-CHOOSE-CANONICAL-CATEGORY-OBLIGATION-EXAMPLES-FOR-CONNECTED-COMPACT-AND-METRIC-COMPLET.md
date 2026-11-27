---
id: SPEC-01KQN9J3WSR722P30PVZ4GAVKG-CHOOSE-CANONICAL-CATEGORY-OBLIGATION-EXAMPLES-FOR-CONNECTED-COMPACT-AND-METRIC-COMPLET
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES]]'
title: Choose canonical category-obligation examples for Connected Compact and Metric Complete topological
  subcategories
status: complete
priority: critical
requirement: The deleted Topological Spaces triage recorded settled topological constructor
  placement and remaining category-obligation example selection for RealSet ambient recovery and metric
  examples.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- Run just category-obligation-file topological_spaces/category_obligations.sage after topological-space work.
- Prove RealSet method recovery through the ambient-relative route, not by adding
  pure topological constructors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Choose canonical category-obligation examples for Connected Compact and Metric Complete topological subcategories
## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining category-obligation example selection for RealSet ambient recovery and metric examples.

## Source Provenance

- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Choose canonical category-obligation examples for Connected Compact and Metric Complete topological subcategories from category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical category-obligation examples are still needed for Connected, Compact, and Metric().Complete().

## Source-Mining Contract

This leaf is source-mining and decision capture, not a free-form spec gate. The output
of this card must be a bounded example-selection record for the three category-obligation example subcategories
already admitted by the mapping docs:

- `TopologicalSpaces().Connected()`
- `TopologicalSpaces().Compact()`
- `TopologicalSpaces().Metric().Complete()`

Required source anchors for the decision:

- `category_specs/topological_spaces/docs/MAPPING.md`:
  - `TopologicalSpaces.Connected() -> TopologicalSpaces().Connected()`
  - `TopologicalSpaces.Compact() -> TopologicalSpaces().Compact()`
  - `MetricSpaces.Complete() -> TopologicalSpaces().Metric().Complete()`
  - root ambient-relative recovery rows for `is_open`, `is_closed`, `closure`,
    `interior`, and `boundary`
  - constructor-routing rows keeping named examples under `Sets().Constructors()`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`:
  - `RealSet.__init__` category assignment
  - named constructors `RealSet.point`, `RealSet.closed`, `RealSet.real_line`
  - category surfaces for `TopologicalSpaces`, `MetricSpaces`, and
    `MetricSpaces.SubcategoryMethods.Complete()`
- `category_specs/sets/docs/MAPPING.md`:
  - RealSet constructor-routing rows admitting named real-line subset constructors
    through `Sets().Constructors()`

Decision this card must produce:

- exact canonical category-obligation example objects, one per target where possible, or a minimal shared set
  of objects if one example witnesses multiple subcategories
- owner category for each asserted fact:
  - connectedness and compactness under `TopologicalSpaces()`
  - completeness under `TopologicalSpaces().Metric()`
  - constructor ownership under `Sets().Constructors()`
- the precise witness being exercised for each example:
  - object membership in the target subcategory
  - any ambient-relative topological operation needed to justify the example
  - whether the example is Sage-backed today or only mapped/provenanced for future spec

Hypotheses and return-object expectations to record:

- each example must be constructible from an admitted named constructor path or from an
  existing Sage-backed parent named in the inventory
- each topological subset example must have an explicit ambient space
- if a metric example is used, record the metric parent and the subcategory
  codomain being witnessed (`TopologicalSpaces().Metric().Complete()`)

Rejection or retirement condition:

- retire or rewrite this card if the only candidate examples depend on excluded
  variadic `RealSet(...)` shapes, manifold-producing paths, or ring/field topology that
  has not yet been grounded through the ring mapping

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just category-obligation-file topological_spaces/category_obligations.sage after topological-space work.
- [x] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Grounded Example Decision

Decision: use two real-line subset constructors and the Sage real field as the canonical
category-obligation examples.

| Target | Canonical object | Owner and witness |
| --- | --- | --- |
| `TopologicalSpaces().Connected()` | `Sets().Constructors().open(lower=0, upper=1)` | Constructor owner is `Sets().Constructors()` through `RealSet.open(0, 1)`. The witness is object membership in `TopologicalSpaces().Connected()`. |
| `TopologicalSpaces().Compact()` | `Sets().Constructors().closed(lower=0, upper=1)` | Constructor owner is `Sets().Constructors()` through `RealSet.closed(0, 1)`. The witness is object membership in `TopologicalSpaces().Compact()`. |
| `TopologicalSpaces().Metric().Complete()` | `Rings().Constructors().RR()` / Sage `RR` | The Sage witness is `RR.category()` lying in complete metric spaces. Project implementation is routed through the existing topological ring/field recovery cards before this becomes a live category assertion. |

Source observations used in this pass:

- `RealSet.open(0, 1)` lies in Sage connected topological spaces and not compact spaces.
- `RealSet.closed(0, 1)` lies in Sage connected and compact topological spaces.
- `RR.category()` is a join containing complete metric spaces; `RR in Sets().Metric().Complete()` is true in local Sage.
- `RealSet` examples are not Sage metric spaces, so they are not complete-metric category-obligation example
  candidates.

Migration consequence:

- Connected and compact category-obligation examples can be added once the topological category-obligation example file is
  updated for named `Sets().Constructors()` real intervals.
- Complete metric category-obligation example should be held to the topological ring/field recovery path,
  already tracked by
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC3XPWZWJK8QHVE3GGM-SPECIFY-TOPOLOGICAL-RING-AND-FIELD-RECOVERY-THROUGH-TOPOLOGICAL-SPACES-I.md`
  and
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES/tasks/TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI.md`.
- Do not use real/complex interval or ball fields as complete-metric category-obligation examples in
  this subtree; they remain ring/field topology evidence.

Validation note: the local Sage observation command was used for source confirmation.
The topological category-obligation example file itself was not run under the current user-authorized
skip-verification workflow.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Selected `RealSet.open(0, 1)`, `RealSet.closed(0, 1)`, and
  `RR`/`Rings().Constructors().RR()` as the connected, compact, and complete-metric
  category-obligation examples. Recorded the complete-metric implementation dependency on
  topological ring/field recovery.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Hermes Agent (independent subagent)
**Protocol version:** 6-gate spec review (G1-G6)
**Subject:** SPEC-01KQN9J3WSR722P30PVZ4GAVKG — Choose canonical category-obligation examples for Connected, Compact, and Metric Complete

### G1 — Source Grounding

**Referenced documents verified present on disk:**

| Claimed source | Actual path | Exists | Content match |
|---|---|---|---|
| `category_specs/topological_spaces/docs/TRIAGE.md` recovered via `git show 8d1c21c^:...` (spec line 37) | Recoverable via git | Yes (git command valid) | Provenance anchor confirmed |
| MAPPING.md rows for Connected/Compact/Complete (spec lines 61-63) | `category_specs/topological_spaces/docs/MAPPING.md` is a redirect stub (7 lines) pointing to `SPEC-MAPPING-TOPOLOGICAL-SPACES.md` | Yes — redirect | Actual rows live in tracked spec lines 111-113 |
| MAPPING.md rows for `is_open`, `is_closed`, `closure`, `interior`, `boundary` (spec lines 64-65) | Ambiguous: not in redirect stub | Redirect | Actual data in tracked spec lines 137-141 |
| MAPPING.md constructor-routing rows (spec line 66) | Redirect stub | Redirect | Actual data in tracked spec lines 168-193 |
| `SAGE_INVENTORY.md` rows for `RealSet.__init__`, named constructors, category surfaces (spec lines 67-71) | `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` (87 lines) | Yes | Verified: `RealSet.__init__` at line 38; `RealSet.open` at line 40; `RealSet.closed` at line 41; `RealSet.point` at line 42; `RealSet.real_line` at line 49; Connected at line 20; Compact at line 21; Complete at line 29 |
| `sets/docs/MAPPING.md` for RealSet constructor-routing (spec lines 72-74) | `category_specs/sets/docs/MAPPING.md` is a redirect stub (7 lines) pointing to `SPEC-MAPPING-SETS.md` | Yes — redirect | Actual constructor routing in tracked topological-space mapping spec lines 179-190 |
| Dependency: topological ring/field recovery spec (spec line 136) | `SPEC-01KQN9YGC3XPWZWJK8QHVE3GGM-SPECIFY-TOPOLOGICAL-RING-AND-FIELD-RECOVERY...` | Yes — 150 lines, status: needs-agent-review | Verified: exists and depends on same phase |
| Dependency: implementation task (spec line 138) | `TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS...` | Yes — confirmed by filesystem search | Dependency chain intact |

**G1 finding — Minor documentation imprecision (non-blocking):** The spec's Source-Mining Contract (lines 60-74) lists `MAPPING.md` as the primary source anchor for Connected/Compact/Complete routing rows. Both `category_specs/topological_spaces/docs/MAPPING.md` and `category_specs/sets/docs/MAPPING.md` are redirect stubs whose bodies say they have been "converted into the tracked spec file." The actual content lives in `SPEC-MAPPING-TOPOLOGICAL-SPACES.md` (lines 111-113 for subcategory routing, lines 137-141 for ambient-relative methods, lines 179-190 for constructor routing). The `SAGE_INVENTORY.md` is the only non-redirect durable document cited. This does not break grounding — all claimed data exists and is findable through the redirect chain — but the source locator is imprecise. No action required for this pass; the spec could optionally cite the tracked spec file path alongside or instead of the redirect stub.

**G1 Verdict: PASS (with documented imprecision).** All referenced data is findable and verified on disk. The git recovery provenance anchor is valid. Both dependency cards exist.

### G2 — Sage Surface Completeness

This spec's scope is decision capture for three category-obligation example subcategories, not a full mapping spec. The Sage surface completeness gate applies to whether the decision uses admitted surfaces and excludes non-admitted ones.

| Category-obligation example target | Surface used | Admitted in mapping spec? | Evidence |
|---|---|---|---|
| `TopologicalSpaces().Connected()` | `Sets().Constructors().open(lower=0, upper=1)` via `RealSet.open(0, 1)` | Yes — tracked mapping | `RealSet.open` is admitted as `Sets().Constructors().open` |
| `TopologicalSpaces().Compact()` | `Sets().Constructors().closed(lower=0, upper=1)` via `RealSet.closed(0, 1)` | Yes — tracked mapping | `RealSet.closed` is admitted as `Sets().Constructors().closed` |
| `TopologicalSpaces().Metric().Complete()` | `Rings().Constructors().RR()` / Sage `RR` | Yes — tracked ring mapping | `RR` is admitted as a ring constructor and refines into topological spaces through the ring/topological recovery path |

**Exclusion audit — surfaces correctly rejected or deferred:**

| Surface | Spec disposition | Assessment |
|---|---|---|
| Variadic `RealSet(*args)` | Rejected per spec line 99-101 | Correct — admitted mapping spec rejects variadic constructor (line 191) |
| Manifold-producing `RealSet` paths | Excluded per spec line 44 | Correct — admitted mapping spec routes to manifolds (line 192) |
| Real/complex ball fields | Excluded per spec lines 45 and 139-140 | Correct — inventory records `RBF.category()` as `Category of infinite fields`, `RBF in Sets().Metric()` is `False` |
| Ring/field topology not yet grounded | Complete metric category-obligation example deferred to ring/field recovery (spec lines 134-140) | Correct — dependency chain verified |

**G2 Verdict: PASS.** All three canonical objects use admitted mapping surfaces. All excluded surfaces have explicit, mathematically grounded rationale matching the topological spaces mapping spec.

### G3 — Mathematical Correctness

**Claim 1: `RealSet.open(0, 1)` lies in Sage connected topological spaces and not compact spaces (spec lines 124-125).**
- Mathematical truth: The open interval (0,1) in ℝ with the standard topology is connected (no separation into disjoint nonempty open sets) and is not compact (it is not closed in ℝ, so Heine-Borel says it's not compact; alternatively, the open cover {(1/n, 1-1/n)} has no finite subcover).
- Sage source: `RealSet.__init__` category assignment at `real_set.py` lines 891-1010 refines into `Connected` for open intervals and `Compact` only for closed bounded intervals. Confirmed by inventory line 38.
- **Verdict: CORRECT.**

**Claim 2: `RealSet.closed(0, 1)` lies in Sage connected and compact topological spaces (spec line 125).**
- Mathematical truth: The closed interval [0,1] in ℝ is compact (Heine-Borel: closed and bounded in ℝⁿ) and connected.
- Sage source: Same `__init__` category assignment refines closed bounded intervals into both `Connected` and `Compact`.
- **Verdict: CORRECT.**

**Claim 3: `RR.category()` is a join containing complete metric spaces; `RR in Sets().Metric().Complete()` is true in local Sage (spec line 126).**
- Mathematical truth: ℝ with the standard metric d(x,y)=|x−y| is a complete metric space (every Cauchy sequence converges in ℝ).
- Sage source: `metric_spaces.py` line 26-28 states `MetricSpacesCategory.default_super_categories` joins `category.Topological()` with default metric supercategories. The spec reports a local Sage observation confirming `RR in Sets().Metric().Complete()` is `True`.
- **Verdict: CORRECT** — mathematically sound and Sage-confirmed.

**Claim 4: `RealSet` examples are not Sage metric spaces, so they are not complete-metric category-obligation example candidates (spec lines 127-128).**
- Mathematical context: RealSet objects refine into `TopologicalSpaces()` but not into `MetricSpaces()` in Sage's current category graph (inventory line 38 lists `TopologicalSpaces()`, `Connected`, `Compact`, `Subobjects`, `Finite`, `Infinite` — no `Metric`). This is a Sage implementation fact: the metric is not registered on RealSet objects.
- **Verdict: CORRECT** as a Sage implementation observation. The spec correctly excludes RealSet from complete-metric category-obligation example.

**Claim 5: Connected and compact are topological-space axioms; completeness is a metric-space axiom (implicit in routing, spec lines 54-56).**
- Mathematical justification: Connectedness depends only on the topology (no separation into disjoint nonempty open sets). Compactness depends only on open covers. Completeness requires a metric (Cauchy sequences). This is standard mathematical taxonomy.
- **Verdict: CORRECT.**

**Category hierarchy consistency check:**
- Connected and Compact category-obligation example use `TopologicalSpaces()` — the root topological category
- Complete category-obligation example uses `TopologicalSpaces().Metric().Complete()` — correctly nested under metric subcategory
- This matches the mapping spec hierarchy: Connected/Compact are direct subcategories of `TopologicalSpaces()` (tracked spec lines 111-112); Complete is under `TopologicalSpaces().Metric()` (tracked spec line 113)
- **Verdict: Hierarchy is consistent.**

**G3 Verdict: PASS.** All five mathematical claims are correct. The constructors, ambient-relative topology, and Sage category assignments match the mathematical facts. The complete-metric deferral to ring/field recovery is mathematically prudent.

### G4 — Nonmathematical Rejection

| Item | Spec disposition | Assessment |
|---|---|---|
| "Run just category-obligation-file topological_spaces/category_obligations.sage" (acceptance criteria line 24) | Unchecked — pending implementation (spec line 143) | This is a procedural acceptance criterion, not a mathematical claim. It's correctly gated behind implementation. |
| "No new subtree-local TRIAGE or process document" (acceptance criteria line 19) | Tracked as gated acceptance criterion | Correct — process hygiene, not mathematical content |
| Rejection condition: retire or rewrite if only candidates depend on excluded paths (spec lines 99-101) | Safety valve | Correct — procedural guard, not mathematical |

**G4 Verdict: PASS.** The spec contains no nonmathematical content that masquerades as mathematical. Procedural acceptance criteria are clearly separated from mathematical claims.

### G5 — Ambiguity Routing

| Ambiguity / Gap | Routed to | Assessment |
|---|---|---|
| Complete metric category-obligation example not implementable until ring/field recovery (spec lines 134-140) | Two tracked dependency cards: `SPEC-01KQN9YGC3...` (spec) and `TASK-01KQN9YGCHD...` (implementation task) | **Adequate.** Both verified on disk. Chain: this spec → topological ring/field recovery spec → implementation task. |
| Sage observation used for source confirmation; category-obligation example file not run (spec lines 142-143) | Documented as "skip-verification workflow" | **Acceptable.** The spec is a decision capture card, not an implementation card. Running the category-obligation example file is an acceptance criterion for later implementation, not a pre-condition for this spec review. |
| Migration consequence timing (spec lines 132-133) | Connected/compact category-obligation example can be added when category-obligation example file is updated; complete metric category-obligation example held for ring/field recovery | **Adequate.** Timing split is explicit. |

**G5 Verdict: PASS.** Ambiguities are documented and routed. The complete-metric category-obligation example dependency chain is intact with both spec and implementation cards on disk.

### G6 — Obligation Preservation

| Obligation | Preserved? | Evidence |
|---|---|---|
| Connected category-obligation example example | Yes — `Sets().Constructors().open(lower=0, upper=1)` | Spec lines 116-118; matches tracked spec line 260 |
| Compact category-obligation example example | Yes — `Sets().Constructors().closed(lower=0, upper=1)` | Spec lines 116-119; matches tracked spec line 261 |
| Complete metric category-obligation example example | Yes — obligation preserved via dependency routing | Spec lines 116-120 with explicit routing to ring/field recovery cards (lines 134-140); matches tracked spec line 262 |
| Constructor ownership | Preserved under `Sets().Constructors()` | Spec line 118: "Constructor owner is `Sets().Constructors()`" |
| Ambient-relative method recovery | Preserved | Acceptance criterion line 25: "Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors" — checked complete |
| Rejection safety valve | Preserved | Spec lines 99-101: retire/rewrite condition if candidates depend on excluded paths |

**Anti-weakening check:** The spec does not delete, weaken, or move any obligation without a grounded replacement. The complete-metric category-obligation example is explicitly routed with tracked dependency cards rather than silently dropped or replaced with an invalid candidate (like a ball field).

**G6 Verdict: PASS.** All three category-obligation example obligations are preserved. Constructor ownership is correctly placed. The complete-metric obligation is routed through a verified dependency chain, not lost.

### Summary

| Gate | Description | Verdict | Key findings |
|---|---|---|---|
| G1 | Source grounding | PASS (minor imprecision) | All referenced data findable; MAPPING.md redirect stubs are imprecise locators but data exists in tracked specs |
| G2 | Sage surface completeness | PASS | All 3 canonical objects use admitted surfaces; exclusions match mapping spec |
| G3 | Mathematical correctness | PASS | 5/5 claims verified correct; category hierarchy consistent |
| G4 | Nonmathematical rejection | PASS | Procedural criteria separated from mathematical claims |
| G5 | Ambiguity routing | PASS | Complete-metric deferral chain intact; category-obligation example-running deferred to implementation |
| G6 | Obligation preservation | PASS | All 3 category-obligation example obligations preserved with correct ownership |

**Overall: 6/6 gates PASS.** The spec selects mathematically correct canonical examples, uses admitted mapping surfaces, excludes non-admitted surfaces with grounded rationale, and routes the complete-metric obligation through a verified dependency chain. The source-locator imprecision (citing redirect stubs instead of tracked spec files) is a documentation note, not a grounding failure.
