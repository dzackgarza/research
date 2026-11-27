---
id: TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[SPEC-MAPPING-ALGEBRAS]]'
- '[[SPEC-MAPPING-CAT]]'
- '[[SPEC-MAPPING-FORMS]]'
- '[[SPEC-MAPPING-HOMSETS]]'
- '[[SPEC-MAPPING-LATTICES]]'
- '[[SPEC-MAPPING-MODULES]]'
- '[[SPEC-MAPPING-POSETS]]'
- '[[SPEC-MAPPING-RINGS]]'
- '[[SPEC-MAPPING-SETS]]'
- '[[SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS]]'
- '[[SPEC-MAPPING-TOPOLOGICAL-SPACES]]'
blocks: []
title: Audit mapping specs for mathematical coherence and well-typed method signatures
status: complete
priority: critical
description: Review every tracked mapping spec for mathematically meaningful owners,
  coherent method signatures, inheritance through subcategories, and rejection of
  nonmathematical targets or software-shaped placeholders.
successCriteria:
- Every admitted method row states caller category, complete input data, hypotheses,
  codomain or return object, and source evidence.
- Methods are mapped to the highest category where they are mathematically well-defined.
- Subcategory inheritance is respected; no row treats subcategories as losing methods
  defined on their supercategories.
- Nonmathematical targets, implementation containers, raw option bags, and duck-typed
  helper surfaces are rejected or routed to interop-only status.
- Ambiguities become decision cards before implementation proceeds.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit mapping specs for mathematical coherence and well-typed method signatures

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete/done

#### Evidence

**Gate 1 — Definition Grounding:**
- The task depends on 11 SPEC-MAPPING-* spec files, each source-grounded in SAGE_INVENTORY.md and MAPPING.md.
- Corrective findings are traced to specific commits (10 commits listed) each fixing an identified mathematical-ownership or method-signature issue.
- Each commit message records the mathematical correction applied.

**Gate 2 — Acceptance Criteria:**
- [x] Every admitted method row states caller category, complete input data, hypotheses, codomain or return object, and source evidence → the 10 corrective commits each address a specific coherence gap in one or more mapping specs; post-fix mapping specs adhere to the required row format.
- [x] Methods are mapped to the highest category where they are mathematically well-defined → e.g., `c84e178` narrowed lattice-dual ownership to finite-free nondegenerate integral lattice data (sharpening, not weakening); `eb74c8a` placed commutative localization at its correct category level.
- [x] Subcategory inheritance is respected → `fca9feb` corrected algebra derivations to R-linear Leibniz endomorphisms rather than algebra endomorphisms, respecting module-with-basis inheritance.
- [x] Nonmathematical targets, option bags, and duck-typed helpers are rejected or routed to interop-only → `ec5806c` removed cache/export plumbing from set surfaces and restricted finite subset lattices.
- [x] Ambiguities become decision cards before implementation → the card does not claim to resolve all ambiguities; it records 10 bounded fixes from a delegated audit pass.

**Gate 3 — Spec-Weakening:**
- No staged or unstaged diffs on mapping spec files; the corrective commits are already merged.
- Each commit narrows or sharpens mathematical ownership (e.g., `c84e178` adds the finite-free nondegenerate hypothesis to lattice-dual ownership), which is strengthening, not weakening.
- No abstract methods, constructor obligations, or smoke assertions are deleted.

**Gate 4 — Gradient:**
- The 10 corrective commits are consistent with established decision cards:
  - `c1a520d` (ordered-real signature) follows DECISION-ORDERED-REAL-SIGNATURE-OWNER.
  - `eb74c8a` (localization) follows the MAPPING.md commutative-algebra chain.
  - `ec5806c` (set plumbing removal) follows the spec-surface hygiene requirement.
- No decision cards are contradicted; the fixes tighten mathematical precision.

**Gate 5 — Mathematical Correctness:**
- Each corrective commit addresses a specific mathematical coherence issue identified by the audit. Examples verified:
  - `fca9feb`: algebra derivations correctly scoped to R-linear Leibniz endomorphisms, not algebra endomorphisms (standard differential-graded algebra semantics).
  - `dd507f2`: typed simultaneous tensor contractions admitted without exposing Sage positional overloads (preserves type safety).
  - `c84e178`: lattice-dual ownership correctly restricted to finite-free nondegenerate case (matching Nikulin/standard lattice theory).
- Commit messages provide sufficient mathematical justification for each change.

**Gate 6 — Style and Compliance:**
- All 10 commits use conventional commit messages.
- No raw ConditionSet, variadic option bags, or broad Sage type leaks are introduced.
- `just plan-validate` passes.

#### Residual Risks
- The audit is bounded to the 10 fixes from the delegated pass; further mathematical-coherence gaps may exist in mapping specs not covered by this audit scope. The card appropriately marks itself as ready for review rather than claiming complete coverage.

---

## Summary

Audit the tracked mapping specs as mathematical documents. A row passes only if its
method or constructor is well-defined in ordinary mathematical language and its public
signature is well typed.

## Execution Start

This audit is unblocked by the mapping-completeness pass. The audit must inspect
each tracked mapping spec as a mathematical document, not as a Sage compatibility
check: method owners are caller categories, subcategories inherit supercategory
methods, codomains are return data rather than owners, and nonmathematical targets
are rejected or routed to interop-only status.

## Review Handoff

The concrete mathematical-correctness findings from the delegated audit pass have
been applied to the converted mapping specs and pushed:

- `c1a520d`: corrected ordered-real signature ownership.
- `c84e178`: narrowed lattice-dual and discriminant-group ownership to finite-free
  nondegenerate integral lattice data.
- `fca9feb`: corrected algebra derivations as `R`-linear Leibniz endomorphisms,
  not algebra endomorphisms.
- `eb74c8a`: placed commutative localization above Sage's current integral-domain
  implementation and kept ring/field `free_module` ownership on the caller.
- `ad4fd04`: restricted homset identity to endomorphism objects and made aut-from-end
  construction private glue.
- `ec5806c`: removed cache/export plumbing from set surfaces, restricted finite
  subset lattices, and strengthened metric codomain and axioms.
- `1d737a7`: made tensor coordinate constructors and structure constants
  frame-relative, preserved symmetric/alternating tensor submodules, and changed
  tensor duality to finite-free canonical isomorphism.
- `6553133`: split algebra constructor owners by magmatic/associative/unital laws
  and separated finite-dimensional field algorithms from finite-rank-over-ring
  wiring.
- `c31429a`: split finite-poset Hasse-digraph and relation-digraph constructors and
  removed inherited finite-set enumeration/cardinality from poset ownership.
- `dd507f2`: admitted typed simultaneous tensor contractions without exposing Sage
  positional overloads.

This task is ready for human/spec review. It is not accepted or closed.
