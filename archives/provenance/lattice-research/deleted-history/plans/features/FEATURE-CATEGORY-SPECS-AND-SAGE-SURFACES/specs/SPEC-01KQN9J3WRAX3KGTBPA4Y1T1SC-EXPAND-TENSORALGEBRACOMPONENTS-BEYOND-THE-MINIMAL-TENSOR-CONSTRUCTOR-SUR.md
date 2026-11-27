---
id: SPEC-01KQN9J3WRAX3KGTBPA4Y1T1SC-EXPAND-TENSORALGEBRACOMPONENTS-BEYOND-THE-MINIMAL-TENSOR-CONSTRUCTOR-SUR
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
title: Expand TensorAlgebraComponents beyond the minimal tensor constructor surface
  only after mapping symmetry storage contraction trace display and migration needs
status: complete
priority: critical
requirement: The deleted Tensor Algebra Components triage records an intentionally
  minimal current scope and the deferred tensor-calculus surface.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No new implementation blocker was discovered in this bounded spec pass; the remaining
  work is concrete method implementation and caller migration under already-frozen
  signatures.
- The tensor API was not expanded past the frozen mapping in this pass; the existing
  admitted public surface is `trace(...)` and explicit `contract(...)` only.
- No constructor or refinement changes were made in this pass, so `tensor_algebra_components/smoketest.sage`
  did not apply.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Expand TensorAlgebraComponents beyond the minimal tensor constructor surface only after mapping symmetry storage contraction trace display and migration needs
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file actually lived at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Expand TensorAlgebraComponents beyond the minimal tensor constructor surface only after mapping symmetry storage contraction trace display and migration needs from category_specs/tensor_algebra_components/docs/TRIAGE.md`
- Recovery check: the pre-removal file records the deferred surface exactly as `Exhaustive tensor calculus method mapping`, `Symmetry and antisymmetry subtrees`, `Full component-storage API`, and `Tensor contraction, trace, display, and index-notation surfaces`.

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Source-Mining Contract

Sources to mine before any tensor-surface expansion:

- `category_specs/tensor_algebra_components/docs/MAPPING.md`, especially the rows for
  `tensor_type()`, `base_module()`, named interop constructors, and the dual-object
  rule `T_R(M)[p,q]^* = T_R(M)[q,p]`.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`, especially the
  Sage definition of tensors as multilinear maps `(M*)^k x M^l -> R`, the
  `tensor_type()` and `tensor_rank()` distinction, and the component-assignment
  interop rows.
- The deleted source named in `Source Provenance`, but only as migration context for
  which deferred surfaces still need an owner and return-object decision.

Decisions this leaf must produce before any public expansion beyond the current minimal
constructor surface:

- For each deferred surface named in this card, identify the exact owner category:
  `TensorAlgebraComponents(R)`, a tensor-component subcategory such as a symmetry or
  antisymmetry refinement, `Tensor` element methods, or `Modules(R).HomCategory().Forms()`
  when the surface is evaluation rather than tensor ownership.
- For each deferred surface, state the hypotheses and return object/codomain. At
  minimum this applies to symmetry/antisymmetry refinements, contraction, trace,
  display/index-notation interop, storage/component access, and any migration route
  from old component containers.
- For contraction and trace, decide whether the output is another tensor component
  `T_R(M)[p',q']`, a scalar in `R`, or only an interop/display helper, and record the
  exact tensor-type transformation.
- For storage or display surfaces, decide whether the public result is a tensor object,
  a typed finite collection of coordinates, or private interop only. Do not admit raw
  component-container APIs without a mapped mathematical owner.

Rejection/retirement condition:

- Retire or reject any proposed public tensor surface that cannot be anchored to the
  Sage tensor definition and the current mapping owner rules, or whose only support is
  the deleted triage prose without an exact owner and return-object decision.

## Execution Result

The required deferred-surface owner and codomain decisions now already exist in the
frozen tensor mapping, so this leaf is review-ready without further public API edits:

- `category_specs/tensor_algebra_components/docs/MAPPING.md` already records exact
  owner, hypotheses, codomain, and migration consequences for symmetry metadata,
  component storage, `trace(...)`, `contract(...)`, display, and index notation.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` already records
  the Sage tensor-definition and tensor-calculus facts that ground those decisions.
- `category_specs/tensor_algebra_components/__init__.py` already exposes the minimal
  admitted public tensor-calculus surface via abstract `Tensor.trace(...)` and
  `Tensor.contract(...)` signatures, with the scalar-vs-tensor codomain rule stated
  in the docstrings.

No additional public tensor surface remains missing in this bounded spec pass. The
remaining follow-up is implementation, not further owner mapping:

- concrete Sage-backed tensor wrappers still need method bodies realizing
  `trace(contravariant_position, covariant_position)` and
  `contract(left_position, other, right_position)` under the already-frozen
  signatures;
- any surviving historical index-notation or component-container callers must be
  migrated at call sites to constructor metadata, `trace(...)`, or explicit
  `contract(...)` when those implementation leaves execute.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered in this bounded spec pass; the remaining work is concrete method implementation and caller migration under already-frozen signatures.
- [x] The tensor API was not expanded past the frozen mapping in this pass; the existing admitted public surface is `trace(...)` and explicit `contract(...)` only.
- [x] No constructor or refinement changes were made in this pass, so `tensor_algebra_components/smoketest.sage` did not apply.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Broadened the stale deleted-triage provenance from `category_specs/...`
  to `plans/category_specs/...`, confirmed that the recovered triage target is fully
  covered by freeze commit `1e10d9c`, and moved this expansion leaf to `in-review`
  because the required owner/codomain decisions and minimal public `trace(...)` /
  `contract(...)` tensor surface already exist.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** G1 Source Grounding, G2 Sage Surface Completeness, G3 Mathematical Correctness, G4 Nonmathematical Rejection, G5 Ambiguity Routing, G6 Obligation Preservation
**Gates failed:** None
**Outcome:** Review complete; spec correctly records that all deferred tensor surfaces are already owner-mapped in the frozen MAPPING.md. No further API expansion is needed in this bounded pass.

---

#### Gate 1 — Source Grounding (G1): Sources Exist and Claims Check

**Verified source files (all exist, readable, and match spec claims):**

1. Git-recovered TRIAGE.md: `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` returns exactly the deferred-surface list claimed by the spec (Exhaustive tensor calculus method mapping, Symmetry and antisymmetry subtrees, Full component-storage API, Tensor contraction/trace/display/index-notation surfaces). The spec's Source Provenance (line 38) correctly states the recovery command and the recovered content.

2. `category_specs/tensor_algebra_components/docs/MAPPING.md` — exists (7 lines). Redirects to canonical tracked spec `SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS.md`, which contains the full Deferred Tensor Surface Freeze table (rows 130-138) mapping every deferred surface from the old TRIAGE to owner/codomain/migration decisions.

3. `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` — exists (82 lines). Documents Sage tensor definition, construction/recovery, component interop, and tensor calculus surfaces. The spec correctly claims this grounds the deferred-surface decisions.

4. `category_specs/tensor_algebra_components/__init__.py` — exists (388 lines). Contains `trace(contravariant_position, covariant_position) -> Tensor | RingElement` (line 68-78) and `contract(left_position, other, right_position) -> Tensor | RingElement` (line 80-92) with scalar-vs-tensor codomain rules in docstrings. The spec's Execution Result claims match the code exactly.

5. `category_specs/tensor_algebra_components/smoketest.sage` — exists (90 lines). The spec correctly notes that no constructor or refinement changes were made in this pass, so the smoketest did not apply (acceptance criteria line 116-117).

6. Freeze commit `1e10d9c` — confirmed via `git log --oneline`: `1e10d9c3 docs: freeze deferred tensor surfaces`. The spec's work log correctly states this commit covers the recovered triage target.

7. Depends-on phase `PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING` — exists at `plans/features/.../PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/`. Verifiable prerequisite.

**G1 verdict: PASS.** All six source paths and the git recovery command are verified. The dependent phase exists. Claims in Execution Result are confirmed against MAPPING.md, SAGE_INVENTORY.md, and __init__.py.

---

#### Gate 2 — Sage Surface Completeness (G2): Every Deferred Surface Has an Owner

The old TRIAGE.md deferred five surfaces. The spec's Execution Result (lines 86-98) claims each is now owner-mapped in MAPPING.md. Verification:

| Deferred surface (TRIAGE.md) | Owner/codomain decision (MAPPING.md Freeze table) | Row |
|---|---|---|
| Exhaustive tensor calculus method mapping | Completeness Reconciliation (lines 64-101) maps all 17 inventoried Sage surfaces | 64-101 |
| Symmetry and antisymmetry subtrees | Constructor metadata with `Symmetric(slot_blocks)` and `Alternating(slot_blocks)` refinements; DECISION-01KQN9YGCVRR84SHX4DR1K284C confirms freeze | 132 |
| Full component-storage API | Private coordinate interop only; public routes are named constructors | 133 |
| Tensor contraction, trace, display, and index-notation surfaces | trace admitted (134), contract admitted (135), display rejected (136), index notation rejected (137) | 134-137 |
| Detailed migration guide for old component containers | Execution Result lines 106-109: surviving callers shall be migrated to constructor metadata, `trace(...)`, or `contract(...)` when implementation leaves execute | 106-109 |

The spec's own Source-Mining Contract (lines 47-78) further requires owner/codomain decisions for contraction, trace, storage/display, and migration routes. Each requirement is satisfied by the corresponding MAPPING.md freeze row.

**G2 verdict: PASS.** All five deferred surfaces from the old triage have exact owner, hypotheses, codomain, and migration consequence recorded in the frozen MAPPING.md. The spec correctly identifies that no surface remains unmapped.

---

#### Gate 3 — Mathematical Correctness (G3): Claims Are Mathematically Sound

**3a. Current scope (lines 44-45):** Component modules `T_R(M)[p,q]`, central Tensor type, constructor stubs, scalar matrices as (0,2) tensors, module-element matrices as (1,2) tensors. All verified against `__init__.py` and `SAGE_INVENTORY.md`.

**3b. Trace codomain claim (lines 96-98):** "scalar-vs-tensor codomain rule stated in the docstrings." Verified in `__init__.py` lines 68-78: returns `Tensor | RingElement`, scalar for (1,1), otherwise tensor in `T_R(M)[p-1,q-1]`. Mathematically correct: contracting one contravariant and one covariant slot reduces both p and q by 1; when p=q=1, the result is a (0,0)-tensor, i.e., a scalar in R.

**3c. Contract codomain claim (lines 96-98):** Verified in `__init__.py` lines 80-92: returns `Tensor | RingElement`, scalar when remaining type is (0,0), otherwise tensor on same base module. Mathematically correct: contracting a (p,q) tensor with a (p',q') tensor along one opposite-variance pair yields a (p+p'-1, q+q'-1) tensor; scalar iff the result is type (0,0).

**3d. Tensor type transformation:** The spec references `T_R(M)[p,q]^* = T_R(M)[q,p]` (line 53). Verified in `__init__.py` lines 112-133 (_DualObjects class). For finite-rank free M, the finite-dual tensor-Hom adjunction gives this canonical isomorphism. Mathematically correct.

**3e. Constructor tensor types:** Scalar matrix → (0,2) tensor (bilinear form `M ⊗_R M → R`). Module-element matrix → (1,2) tensor (structure tensor in `M ⊗_R M* ⊗_R M*` for bilinear map `M ⊗_R M → M`). Both mathematically correct under standard tensor-Hom adjunction.

**3f. No mathematical errors found in spec claims.** All deferred-surface codomain rules (trace returns scalar for (1,1); contract returns scalar for resulting (0,0)) are consistent with standard multilinear algebra.

**G3 verdict: PASS.** Tensor types, codomains, dual isomorphism, and constructor interpretations are mathematically correct. The spec accurately reflects the mathematically-sound decisions already recorded in MAPPING.md.

---

#### Gate 4 — Nonmathematical Rejection (G4): Nonmathematical Surfaces Properly Excluded

**The spec's own rejection/retirement condition (lines 79-83):** "Retire or reject any proposed public tensor surface that cannot be anchored to the Sage tensor definition and the current mapping owner rules, or whose only support is the deleted triage prose without an exact owner and return-object decision."

**Verified rejections (all inherited from MAPPING.md freeze table):**
- `t.display()` / `t.display_comp()`: Rejected as basis-dependent rendering, not mathematical tensor structure (MAPPING row 136).
- `TensorWithIndices`, index-notation, Einstein syntax: Rejected as public API (MAPPING row 137).
- Raw `Components`, `comp()`, `set_comp()`, `[:]` indexed assignment: Private coordinate interop only (MAPPING row 133).
- Catch-all component data: No public constructor; private `_from_components()` only (MAPPING row 121).
- Sage variadic `contract()` overloads: Explicitly narrowed to typed `contract(left_position, other, right_position)` (MAPPING row 135).

**No deferred surface in this spec proposes a new nonmathematical API.** The spec explicitly constrains expansion to "only after mapping symmetry storage contraction trace display and migration needs" (title and line 31) — all of which must be anchored to mathematical owners.

**G4 verdict: PASS.** The spec inherits and enforces the nonmathematical rejection decisions from the frozen MAPPING.md. No new nonmathematical surface is proposed.

---

#### Gate 5 — Ambiguity Routing (G5): Ambiguities Properly Routed

**Ambiguities identified and routed by this spec:**

1. Deferred-surface ownership ambiguity: The Source-Mining Contract (lines 63-77) requires explicit owner, hypotheses, and return-object decisions for each deferred surface. This is routed to `category_specs/tensor_algebra_components/docs/MAPPING.md` and `SAGE_INVENTORY.md`, which the Execution Result confirms already contain those decisions.

2. Contraction/trace codomain ambiguity: Lines 73-74 require a decision on whether the output is a tensor, scalar, or interop helper. Routed to MAPPING.md rows 134-135, which state codomain: `RingElement` for (1,1) trace / (0,0) result; otherwise tensor.

3. Storage/display surface ambiguity: Lines 75-77 require a decision on whether the public result is a tensor, typed collection, or private interop. Routed to MAPPING.md rows 133, 136-137, which reject public storage/display APIs.

4. Missing mathematical owner fallback: Lines 79-83 provide a rejection condition for surfaces that lack an owner — this is a routing rule, not an ambiguity left unresolved.

5. Stale source path: The spec (Source Provenance, lines 37-40) acknowledges the migrated path was stale, provides the correct git recovery command, and grounds the content in the recovered file. This is proper historical routing, not an ambiguity.

**Dependencies and Boundaries (lines 119-123):** The spec further routes new discoveries: "If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it." This is a correct ambiguity-routing rule.

**G5 verdict: PASS.** All ownership, codomain, and typing ambiguities are routed to the frozen MAPPING.md decisions. The spec provides clear routing rules for future discoveries. The stale source path is acknowledged and corrected with the git recovery command.

---

#### Gate 6 — Obligation Preservation (G6): No Obligations Weakened

**Checked for weakening patterns (acceptance criteria lines 15-26 and Execution Result lines 85-109):**

1. No abstract methods deleted: The spec does not remove `trace(...)` or `contract(...)`. It confirms they are the admitted public surface.

2. No constructor obligations removed: The spec explicitly states "No constructor or refinement changes were made in this pass" (line 25). The existing constructors (`from_matrix`, `from_module_element_matrix`, etc.) remain intact.

3. No smoke assertions narrowed: Acceptance criterion line 25-26: smoketest did not apply because no constructor/refinement changes were made. This is properly bounded — not a weakening, just inapplicable.

4. No new subtree-local TRIAGE created: Acceptance criterion line 18 explicitly forbids this. The spec records decisions by reference to existing MAPPING.md and SAGE_INVENTORY.md, not by creating new parallel docs.

5. Tensor API not expanded past frozen mapping: Acceptance criterion lines 23-24 explicitly state the existing admitted surface is `trace(...)` and `contract(...)` only. No premature expansion.

6. Sage-gap-driven shrinkage avoided: The spec does not weaken obligations because of Sage limitations. On the contrary, it preserves all deferred surfaces as tracked future work (implementation, not further mapping).

7. Migration consequence preserved: Lines 106-109 record that surviving historical callers must be migrated to constructor metadata, `trace(...)`, or `contract(...)` when implementation leaves execute. This is an obligation preserved, not weakened.

8. Dependencies and Boundaries (lines 119-123): Explicitly preserves `SAGE_INVENTORY.md` and `MAPPING.md` as canonical source/mapping provenance; forbids recreating subtree-local `TRIAGE.md` files.

**G6 verdict: PASS.** No abstract method, constructor obligation, smoke assertion, or mathematical invariant is weakened. The spec correctly constrains this leaf to recording that the deferred decisions already exist, without adjusting any public API.

---

### Summary

The EXPAND-TENSORALGEBRACOMPONENTS spec is a correctly-bounded closure leaf. It records that the deferred tensor surfaces from the deleted TRIAGE.md are already fully owner-mapped in the frozen MAPPING.md (commit `1e10d9c`). The spec's Source-Mining Contract requirements are satisfied by the existing mapping decisions. No new API expansion is proposed; the remaining work is concrete method implementation under already-frozen signatures.

**All six gates pass.** No mathematical errors, source-grounding failures, nonmathematical admissions, unresolved ambiguities, or obligation weakenings were found.

**Residual note (non-blocking):**
- The spec title (line 9-10) carries the trailing clause "only after mapping symmetry storage contraction trace display and migration needs" — this is the original migrated line from TRIAGE.md and is preserved for provenance tracking. It is slightly awkward as a title continuation but correctly reflects the historical constraint. No action needed.
