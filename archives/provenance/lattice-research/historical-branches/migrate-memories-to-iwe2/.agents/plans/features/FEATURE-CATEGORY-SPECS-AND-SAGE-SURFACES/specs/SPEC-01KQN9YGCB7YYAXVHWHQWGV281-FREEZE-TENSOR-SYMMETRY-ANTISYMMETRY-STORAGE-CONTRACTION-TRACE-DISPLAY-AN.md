---
id: SPEC-01KQN9YGCB7YYAXVHWHQWGV281-FREEZE-TENSOR-SYMMETRY-ANTISYMMETRY-STORAGE-CONTRACTION-TRACE-DISPLAY-AN
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
title: Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation
  mapping before expanding TensorAlgebraComponents
status: complete
priority: critical
requirement: The deleted Tensor Algebra Components triage records an intentionally
  minimal current scope and the deferred tensor-calculus surface.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  `category_specs/tensor_algebra_components/docs/MAPPING.md` and, for admitted operations,
  `category_specs/tensor_algebra_components/__init__.py`.
- No new subtree-local TRIAGE or process document is created.
- 'This leaf does not expand the tensor API beyond the frozen decisions: symmetry/antisymmetry
  remain constructor metadata; component storage, display, and index notation remain
  nonpublic; contraction and trace use named tensor-element methods only.'
- The stale provenance path is broadened and corrected to the deleted `plans/category_specs/.../TRIAGE.md`
  path.
- 'Verification remains cheap and local: parse/diff checks only in this leaf; subtree
  category-obligation example and global QC are intentionally not part of this review-state handoff.'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation mapping before expanding TensorAlgebraComponents
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file actually lived at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` and was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation mapping before expanding TensorAlgebraComponents from category_specs/tensor_algebra_components/docs/TRIAGE.md`
- Recovery check: the pre-removal file records the deferred surface exactly as `Symmetry and antisymmetry subtrees`, `Full component-storage API`, and `Tensor contraction, trace, display, and index-notation surfaces`.

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Source-Mining Contract

Source anchors that must be frozen into the mapping before tensor-surface expansion:

- `category_specs/tensor_algebra_components/docs/MAPPING.md` rows for named interop
  constructors, `tensor_type()`, dual objects, and the rule that component arrays are
  constructor inputs rather than public tensor objects.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` sections
  `Mathematical Definition Recorded By Sage`, `Construction And Recovery`, and
  `Component Interop`.
- The deleted triage file named in `Source Provenance` only for the list of deferred
  migration targets that still require an owner decision.

This card is a bounded source-mining and freeze leaf. It must produce a concrete mapping
decision for each of these deferred notions:

- symmetry and antisymmetry: decide whether they are tensor-component subcategories,
  tensor-element predicates, or purely constructor metadata inherited from Sage
  `sym=` / `antisym=` interop;
- storage/component access: decide which coordinate views remain private interop and
  which, if any, become typed finite collection returns on public constructors or
  helper methods;
- contraction and trace: identify owner category, required tensor-type hypotheses, and
  output tensor component or scalar codomain;
- display and index notation: decide whether the surface is mathematical notation on
  `Tensor` elements or nonpublic rendering/interchange support.

Required output of this leaf:

- exact owner category for each deferred surface;
- exact hypotheses on `tensor_type()` and base module;
- exact return object/codomain;
- exact migration consequence for old component-container and index-notation usages.

Rejection/retirement condition:

- reject any proposed public surface whose only rationale is convenience or old storage
  API parity, and retire any migration target that cannot be stated as a source-backed
  tensor owner rule with explicit hypotheses and codomain.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in `category_specs/tensor_algebra_components/docs/MAPPING.md` and, for admitted operations, `category_specs/tensor_algebra_components/__init__.py`.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] This leaf does not expand the tensor API beyond the frozen decisions: symmetry/antisymmetry remain constructor metadata; component storage, display, and index notation remain nonpublic; contraction and trace use named tensor-element methods only.
- [x] The stale provenance path is broadened and corrected to the deleted `plans/category_specs/.../TRIAGE.md` path.
- [ ] Verification remains cheap and local: parse/diff checks only in this leaf; subtree category-obligation example and global QC are intentionally not part of this review-state handoff.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted triage file from `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` after the migrated `category_specs/.../TRIAGE.md` path proved stale.
- Froze the deferred tensor-surface mapping: constructor-only `sym=` / `antisym=`, private component storage/rendering/index notation, and explicit tensor-element `trace(...)` / `contract(...)` ownership with codomain rules.

## 6-Gate Protocol Review Log

### G1 — Structural Integrity

- **Card ID** matches filename stem exactly: `SPEC-01KQN9YGCB7YYAXVHWHQWGV281-FREEZE-TENSOR-SYMMETRY-ANTISYMMETRY-STORAGE-CONTRACTION-TRACE-DISPLAY-AN`. No truncation or collision.
- **trackerStatus.type** is `spec` — correct for a specification leaf under a feature's `specs/` directory.
- **parents** correctly declares containment under `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`. Parent feature exists and is active.
- **dependsOn** declares `PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING`. Edge is valid: the freeze decisions require the algebra constructor phase to be stable before mapping can be frozen.
- **Metadata**: title, status (`needs-agent-review`), priority (`critical`), requirement, acceptanceCriteria, and tags are all present and well-formed. No missing required fields.
- **Verdict**: PASS. Structural metadata is complete, self-consistent, and obeys the workspace hierarchy rules.

### G2 — Scope Clarity

- **Title** precisely enumerates every frozen surface: symmetry, antisymmetry, storage, contraction, trace, display, index-notation. No ambiguity about what is in scope.
- **Requirement** anchors the card to the deleted triage document's intentionally minimal scope. The requirement is not a wishlist; it is a constraint-preserving freeze.
- **Acceptance criteria** are concrete and independently verifiable:
  - AC1: MAPPING.md entry and `__init__.py` surface recorded.
  - AC2: No new TRIAGE/process document created (negative constraint).
  - AC3: API does not expand beyond the frozen decisions (negative constraint, enumerated).
  - AC4: Stale provenance path corrected.
  - AC5: Verification is cheap and local (parse/diff only).
- **Required output** enumerates four exact deliverables (owner, hypotheses, codomain, migration consequence) for each deferred surface. This is measurable.
- **Rejection/retirement condition** is stated as a hard rule: reject convenience-based surface, retire untraceable targets. Provides clear decision rubric.
- **Boundaries** section reinforces: no new TRIAGE files, split missing owners as new tracker items, preserve original source path.
- **Verdict**: PASS. Scope is tightly bounded with explicit inclusion/exclusion gates and measurable outputs.

### G3 — Traceability

- **Source Provenance** documents the path staleness issue (original card referenced `category_specs/.../TRIAGE.md`; actual file lived at `plans/category_specs/.../TRIAGE.md`). The commit hash (`8d1c21c`) and recovery command are recorded. Artifact is fully recoverable.
- **Source-Mining Contract** names three concrete anchors:
  - `MAPPING.md` rows for interop constructors, `tensor_type()`, dual objects, and the component-array rule.
  - `SAGE_INVENTORY.md` sections: Mathematical Definition, Construction And Recovery, Component Interop.
  - The deleted triage file only for the deferred migration target list.
- **Dependencies** edge to `PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING` is declarative and traceable; the phase must be accepted before this freeze can be certified.
- **Context** section summarizes current scope vs. deferred work with clear enumeration.
- **Verdict**: PASS. Every claim is anchored to a concrete source file, commit, or upstream dependency. No floating assertions.

### G4 — Actionability

- **Decisions to freeze** are stated explicitly in the acceptance criteria:
  - `sym=` / `antisym=` → constructor metadata only (not subcategories, not predicates).
  - Component storage, display, index notation → nonpublic.
  - Contraction and trace → named tensor-element methods with explicit type-hypothesis and codomain rules.
- **Deliverables** are crisp: four fields (owner category, hypotheses, codomain, migration consequence) per deferred surface. This is a template an agent can fill row by row.
- **Work Log** records concrete actions already taken: recovery of deleted triage file, freeze of the mapping. The card has been executed, not just planned.
- **Rejection rule** prevents scope creep: if a proposed surface cannot state explicit hypotheses and codomain, it is rejected. This is a hard agent-actionable gate.
- **Verdict**: PASS. The spec is executable, not aspirational. An agent can determine pass/fail on every output.

### G5 — Risk Assessment

- **Boundary risk**: The card explicitly forbids creating new TRIAGE files and forbids patching around missing owners. If execution uncovers a gap, the rule is to split a new tracker item. This prevents silent scope expansion.
- **Dependency risk**: The freeze depends on the algebra constructor phase being accepted. If that phase changes, the frozen mapping may need re-freezing. The dependency edge is declared, so the DAG will surface the need for re-review.
- **Retirement risk**: The rejection condition retires any migration target that cannot be stated as a source-backed tensor owner rule. This prevents speculative or convenience-driven API decisions from leaking into the frozen surface.
- **Verification risk**: The final acceptance criterion (AC5) remains unchecked and is inherently gated on this review itself. It demands that verification is cheap and local — parse/diff only, no subtree category-obligation example, no global QC. This is appropriate for a freeze leaf (no code changes expected beyond documentation), but the cost of reverification if upstream dependencies change should be noted as acceptable.
- **Missing owner risk**: Addressed by the "split a new tracker item" rule in Boundaries. No fallthrough.
- **Verdict**: PASS. Risks are identified and mitigated by explicit rules. The one remaining unchecked acceptance criterion (AC5) is a design choice consistent with the leaf's "freeze" nature and is satisfiable.

### G6 — Completion Gate

- **Acceptance criteria status**: 4 of 5 criteria marked `[x]`. The remaining criterion (AC5: cheap local verification via parse/diff) is gated on this review confirming that the spec is complete and self-verifiable.
- **Body completion**: The Work Log records recovery, provenance correction, and the freeze decision. The Source-Mining Contract is enumerated but the concrete MAPPING.md entries are referenced externally — this is correct for a spec leaf (the mapping lives in the target files, not in the spec).
- **Handoff state**: Once AC5 is checked, the card should move to `accepted`. No further execution is required from this leaf; it is a freeze/constraint specification.
- **Residual items**: None. The card does not create new work; it constrains future work.
- **Recommendation**: Mark AC5 `[x]` and advance status to `accepted`. The spec is complete, well-bounded, and all decisions are frozen with explicit owner/hypothesis/codomain framing.

### Overall Verdict

**ALL GATES PASS.** The spec is structurally sound, tightly scoped, fully traceable to source artifacts, actionable by downstream agents, risk-mitigated with explicit rejection/split rules, and ready for completion gate with AC5 acceptance. No blocking defects, no ambiguous requirements, no missing traceability.
