---
id: TASK-SPEC-CORE-REGISTRY-REPORT-KERNEL
trackerStatus:
  type: task
parents:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn: []
title: Create typed spec registry and report kernel
status: complete
priority: critical
description: Add the minimal typed spec-core data layer for obligations, providers,
  construction witnesses, and reports needed by the vertical slice.
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- A minimal `category_specs/spec_core/` package represents obligations, providers,
  construction witnesses, and reports as typed data.
- The kernel can report declared category, inherited obligations, satisfied providers,
  construction witnesses, computed values, and missing obligations.
- The code is strict enough to support focused mypy or py_compile checks inside the
  new package without requiring all Sage method-container code to type-check.
- No Sage category wrapper is rewritten wholesale to make the kernel exist.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SPEC-CORE-VERTICAL-SLICE
- PHASE-SPEC-CORE-VERTICAL-SLICE
---
# Create typed spec registry and report kernel

## Summary

Create the small typed data layer that lets later slice tasks ask what an object claims,
which obligations follow, which providers or construction witnesses satisfy them, and
what remains missing.

## Source Provenance

- `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`
- `/home/dzack/vault/projects/research/Spec Enforcement in Sage.md`
- `[[SPEC-MAPPING-CAT]]`
- `category_specs/types.py`
- `category_specs/utils.py`

## Context

The feedback identified that Sage wrappers alone are too implicit as the spec source of
truth. This task introduces the smallest declarative kernel needed by the slice while
leaving existing category wrapper behavior intact.

## Acceptance Criteria

- [x] `category_specs/spec_core/` contains typed definitions for obligations,
  providers, construction witnesses, check results, and reports.
- [x] The report shape can express `declared_category`, `inherited_obligations`,
  `satisfied_by_provider`, `satisfied_by_witness`, `computed_values`, and
  `missing_obligations`.
- [x] The kernel has focused validation that does not require importing every
  category-spec subtree.
- [x] No broad category expansion, mypy-plugin work, or global QC routing is counted as
  completion evidence.

## Dependencies And Boundaries

This task owns only the typed data/report kernel. It must not implement module-specific
GF(5) or `ZZ` witness logic; that belongs to the next task.

## Complexity And Ownership

Owner role: implementation agent. Complexity: 75. This is high-complexity foundational
surface work because later slice tasks depend on the data contract, but it is bounded
to a new package and should not change existing category behavior.

## Work Log

- Created as the first executable leaf of the pivot plan.
- Started implementation on branch `dzack/spec-core-vertical-slice-kernel`.
- Added the spec-core report kernel and focused test, then moved the card to
  `needs-agent-review`.
- Validation evidence:
  - `python -m py_compile category_specs/spec_core/__init__.py
    category_specs/spec_core/reports.py tests/category_specs/test_spec_core_reports.py`
    passed.
  - `sage -python -m pytest tests/category_specs/test_spec_core_reports.py` passed.
  - `just plan-validate` passed after activating the parent plan and phase.
- Validation gaps:
  - Focused mypy is blocked by the local Sage mypy plugin config: mypy reports missing
    `[sage-mypy-category-plugin]` in `/home/dzack/.config/mypy/config`.
  - Normal `category_specs.spec_core` import still executes the eager parent package and
    reaches the existing Sage category import failure, `cannot import name Category`.
    Focused validation loads `category_specs/spec_core/reports.py` directly to test the
    new kernel without importing every category-spec subtree.
- PR review follow-up:
  - Addressed Gemini review comments by caching registry indices, raising `ValueError`
    for unknown inherited obligation IDs, and rejecting duplicate provider or witness
    claims for one obligation.
  - Removed the direct file-loader test bypass; the focused test now imports
    `category_specs.spec_core` through the normal package path after initializing
    `sage.all`.
  - Added `SpecCheckResult` validation so status, provider, and witness fields cannot
    encode contradictory report results.
  - Review placement decision: the Qodo `src/` placement comment conflicts with this
    card's explicit acceptance path, `category_specs/spec_core/`. Moving the package
    would fail the approved slice task and should be a separate repo-structure decision
    if the project wants to migrate category-spec code into `src/`.
- Accepted after PR #3 was merged on 2026-05-18; the merged PR is the human gate for
  this card, so its dependent vertical-slice task can start.

## Review Log

### Review 2026-05-18 (Fresh-context Spark review)

Reviewed in fresh context under the research review kernel.

- Synthesis: the work adds a minimal, isolated declarative core (`SpecObligation`,
  `SpecProvider`, `ConstructionWitness`, `SpecReport`, `SpecRegistry`) that models the
  pivot goal from `Spec Enforcement in Sage.md`: obligation inheritance, construction
  witnesses, and an explicit report surface (`category hierarchy = obligation
  inheritance`, `construction witnesses = implementation by composition`, `Spec registry =
  inspectable, testable, generatable truth`).

- Gate 1 pass: model-level definitions are scoped to the declared card objective and
  grounded by task provenance plus pivot text lines 66-69 and 108-125 of
  `Spec Enforcement in Sage.md`.

- Gate 2 pass: all card acceptance criteria are satisfied; the leaf does not claim to
  satisfy module-specific GF(5)/ZZ witness obligations.

- Gate 3 pass: no `spec`/`category-obligation example` weakening or scope drift was introduced in this
  patch; all changed code files are within `category_specs/spec_core/` and the dedicated
  focused test path.

- Gate 4 pass: no decided card reversal or prior source-map/phase requirement change
  was detected in this commit.

- Gate 5 pass: `python -m py_compile ...`, `sage -python -m pytest tests/category_specs/test_spec_core_reports.py`,
  and `just plan-validate` were re-run successfully.

- Gate 6 pass: no style or compliance rule violations are introduced by this minimal
  kernel package and test, and there are no orthogonal cleanup edits.

- Evidence gap (non-blocking): package-level import of `category_specs.spec_core` is still
  coupled to eager parent imports and not yet validated end-to-end.
  - Pass condition: once upstream eager import issue is fixed, execute the same focused test
    by importing from `category_specs.spec_core` and confirm identical results.

- Evidence gap (non-blocking): focused mypy remains blocked by missing
  `[sage-mypy-category-plugin]` in `/home/dzack/.config/mypy/config`.
  - Pass condition: restore plugin configuration and run focused typing check for
    `category_specs/spec_core/`.

- Outcome: PASS, no blocking defects; frontmatter status is `complete`.
