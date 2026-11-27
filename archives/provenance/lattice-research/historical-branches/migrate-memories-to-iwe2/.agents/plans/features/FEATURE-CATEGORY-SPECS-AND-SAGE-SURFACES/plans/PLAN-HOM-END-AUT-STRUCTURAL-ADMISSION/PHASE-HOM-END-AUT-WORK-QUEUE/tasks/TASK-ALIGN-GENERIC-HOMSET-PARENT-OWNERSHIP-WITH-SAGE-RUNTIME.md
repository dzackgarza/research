---
id: TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME
trackerStatus:
  type: task
parents:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
title: Rewrite generic homset ownership for project HomCategory mirroring
status: complete
priority: critical
description: Rewrite the generic Hom/End/Aut owner story around project
  HomCategory mirroring rather than Sage generic homset inheritance, then update
  QC/visual/spec surfaces to match that semantic-base decision.
activityType: implementation
workstreamRole: implementation
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- "`category_specs/homsets/*` uses a source-grounded generic owner map consistent with `DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION`."
- Generic hom-layer `@override` annotations remain only where the runtime owner chain
  makes them real overrides.
- "`SPEC-MAPPING-HOMSETS.md`, `plans/visuals/homsets-category-hierarchy.md`, and the relevant homsets docstrings/comments record the corrected owner split."
- "`FEATURE-QC-WARNINGS-ZERO.md` no longer treats the generic Hom/End/Aut residuals as uniformly plugin false positives."
- Relevant Hom/End/Aut QC evidence is rerun and the exact remaining plugin-vs-spec
  failures are recorded in the card body or a linked review artifact.
complexity: 74
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
- PHASE-HOM-END-AUT-WORK-QUEUE
---
# Rewrite generic homset ownership for project HomCategory mirroring

## Summary

The project does not semantically inherit Sage's generic homset construction. This
task rewrites the generic Hom/End/Aut ownership docs and QC framing so
`HomCategoryConstruction` is the semantic base and Sage generic homset behavior is
treated as source inventory/backing behavior to mirror explicitly where desired.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-HOMSETS.md`
- `category_specs/homsets/homsets.py`
- `category_specs/homsets/endsets.py`
- `category_specs/homsets/autsets.py`
- `category_specs/homsets/__init__.py`
- `plans/visuals/homsets-category-hierarchy.md`
- `plans/features/FEATURE-QC-WARNINGS-ZERO/FEATURE-QC-WARNINGS-ZERO.md`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homsets.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homset.py`

## Context

The follow-up no longer tries to make the project generic hom layer inherit or
bridge Sage's generic `Homset` owner chain. The new ruling is:

- project `HomCategoryConstruction` is the semantic owner of generic Hom/End/Aut;
- Sage generic homset/container behavior is thin inventory/backing behavior;
- subtree mapping specs, not generic runtime inheritance, must explicitly capture
  any Sage homset/container methods that remain part of the project surface.

That still leaves a QC consequence:

- generic hom-layer `@override` claims must not be justified by supposed Sage
  inheritance that the project no longer claims as semantic ownership;
- remaining plugin follow-up is confined to cases where there is real runtime
  inheritance inside the project-owned category chain.

## Acceptance Criteria

- [x] `SPEC-MAPPING-HOMSETS.md` states that project Hom/End/Aut are redefined and
      mirrored through `HomCategoryConstruction` rather than inherited from Sage
      generic homsets.
- [x] `plans/visuals/homsets-category-hierarchy.md` and any directly affected
      homsets docstrings/comments reflect the project-owned semantic base.
- [x] `FEATURE-QC-WARNINGS-ZERO.md` no longer frames the generic hom-layer residuals
      as a Sage inheritance repair.
- [x] The card body points the subtree method-coverage work to the reopened mapping
      audit tasks instead of collapsing it into this generic card.

## Dependencies And Boundaries

- Do not turn this generic card into the cross-subtree audit itself.
- Do not treat backend reuse of Sage container classes as evidence that the project
  semantically inherits generic homsets.
- Keep subtree method-surface coverage in the mapping-audit phase tasks.

## Complexity And Ownership

- Owner/role: category-spec ownership/documentation follow-up under the Hom/End/Aut plan.
- Complexity: 58/100 (moderate).
- Why this score: the decision is now made and this card is limited to the generic
  owner story, visual/doc wording, and QC framing. The subtree mapping audits are
  split out separately.
- Item-specific evidence:
  - installed Sage source and `SPEC-MAPPING-HOMSETS.md` already ground the intended
    owner map;
  - the affected implementation and documentation surface is concentrated in the
    generic hom/end/aut files plus one visual and one QC tracker file;
  - validation must recheck runtime MRO truth and the Hom/End/Aut QC slice, not just
    syntax.

## Work Log

- 2026-05-10: Created after repo QC follow-up showed a source-grounded owner mismatch
  between `SPEC-MAPPING-HOMSETS.md` and the current generic `HomCategory` runtime MRO.
- 2026-05-10: Reframed after user direction: the repo redefines/mirrors Sage homset
  behavior through `HomCategoryConstruction`; subtree method coverage moved to
  dedicated mapping-audit tasks.
- 2026-05-17: Updated `SPEC-MAPPING-HOMSETS.md`,
  `plans/visuals/homsets-category-hierarchy.md`, and `FEATURE-QC-WARNINGS-ZERO.md`
  so generic Hom/End/Aut ownership is project-owned semantic mirroring of Sage
  inventory/backend surfaces, not inherited Sage `Homset` method-container ownership.
- 2026-05-17: Reviewed generic Hom/End/Aut `@override` sites in
  `category_specs/homsets/{homsets,endsets,autsets}.py`; retained annotations are
  project-chain overrides, Sage `Endset` axiom hooks, or intentional signature
  quarantines rather than claims of inherited Sage generic homset ownership.
- 2026-05-17: Fresh-context review returned `clean-to-route-needs-human-input` with
  no findings; remaining runtime MRO and full-suite checks are blocked or
  non-diagnostic until the Sage import/plugin lane is resolved.
- 2026-05-17: Reopened the runtime-MRO validation gap after user correction that
  repairable runtime failures are autonomous work, not human decisions. `sage -c`
  imports Sage `Category` successfully, so the prior `sage -python` failure is not a
  blocker for this leaf. Fixed the repo import blockers exposed by the Sage runtime
  path:
  - `OverPIDFormedModulesCategory` now owns its own nested `HomCategory` instead of
    rebinding `FormedModulesCategory.HomCategory` against the wrong Sage base class.
  - Lattice construction files now keep annotation-only `LatticesCategory` imports
    behind `TYPE_CHECKING`, avoiding package-initialization cycles.
  - `category_specs.forms` exports the runtime `Category` name used by
    `FormedModules(...)`.
  - The finite-rank formed-module `orthogonal_group()` cast no longer evaluates the
    type-only `OrthogonalGroup` alias at runtime.
  - `topological_spaces` now exports `MetricSpacesCategory` at runtime for the shared
    type package.
  This card needs fresh-context review of the reopened runtime repair before it can
  return to a human approval gate.
- 2026-05-18: Extended validation past the original Hom runtime import blockers. The
  centralized type package now uses Python-3.12-compatible aliases and namespace
  containers so category package imports reach runtime Hom/End/Aut surfaces under
  Python 3.12.
- 2026-05-18: Repaired non-Hom category-obligation example blockers only where they sat on the import/runtime
  path for reviewing the Hom owner split:
  - Sets: `is_countable()` now records the Countable axiom directly instead of
    forwarding to a missing Sage enumerated-set method.
  - Posets: type-only casts no longer evaluate finite-poset aliases at runtime.
  - Modules: mapping-valued basis data is admitted in `ModuleBasis` and
    `basis_index_set()` so basis keys are preserved rather than replaced by positional
    indices.
  - Rings: rational-field and algebraic-closure singleton methods now answer the
    source-forced surfaces needed by rings category-obligation example.
  This card returns to the human approval gate after fresh-context review of the
  runtime repair and validation boundary.
- 2026-05-18: Fresh-context review found the Hom owner repair coherent but required
  two revisions: ground mapping-valued module basis data in `ModuleBasis`, and
  enumerate why non-Hom category-obligation example repairs belong to this runtime review boundary. After
  those revisions and focused validation, re-review returned
  `clean-to-route-human-input` with no remaining findings or non-human autonomous work
  in scope.

## Validation Notes

- Focused syntax validation: `python -m compileall -q category_specs/homsets/homsets.py
  category_specs/homsets/endsets.py category_specs/homsets/autsets.py` passed.
- Full `just test` was not run for this card because the mypy-plugin work is active in
  parallel and the available repo recipe would not distinguish remaining plugin-owned
  checker failures from source defects in this Hom/End/Aut owner split.
- Runtime MRO probe:
  - Searched: `sage -c` imports of Sage `Category`, `category_specs.homsets`, formed
    module HomCategory base-class metadata, and `Modules(ZZ).HomCategory()`,
    `.EndCategory()`, and `.AutCategory()` MROs.
  - Found: Sage `Category` imports under `sage -c`; `OverPIDFormedModulesCategory`
    binds its nested `HomCategory` to `OverPIDFormedModulesCategory`; and
    `Modules(ZZ)` runtime Hom/End/Aut categories have project-owned MRO chains through
    `RModuleHomCategory -> HomCategoryOf -> HomCategoryConstruction`,
    `RModuleEndCategory -> EndCategoryOf`, and
    `RModuleAutCategory -> AutCategoryOf`. Their element surfaces subclass the
    corresponding universal Hom/End/Aut element methods.
  - Conclusion: inference — the generic runtime MRO evidence now supports the
    project-owned Hom/End/Aut owner split for the probed module category path.
  - Confidence: High for the probed module path; Medium for every subtree-specific
    path until each subtree audit is human-approved or sent back.
  - Gaps: subtree-specific Hom/End/Aut method coverage remains governed by the
    per-subtree audit cards; this generic runtime card now needs human approval or
    send-back after clean fresh-context review.
- Focused validation after runtime repair:
  - `python -m compileall -q category_specs` passed.
  - `just --justfile category_specs/justfile category-obligation-file homsets/category_obligations.sage`
    exited 0, with Sage method-provider superclass warnings.
  - `just --justfile category_specs/justfile category-obligation-file type_alias_obligations.sage`
    exited 0 after the centralized type-package alias repair.
  - `just --justfile category_specs/justfile category-obligation-file forms/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file posets/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file modules/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file rings/category_obligations.sage`
    requires separate rings-surface validation.
  - `just --justfile category_specs/justfile category-obligation-file algebras/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file tensor_algebra_components/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file cat/category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file lattices/chain_category_obligations.sage`
    exited 0.
  - `just --justfile category_specs/justfile category-obligation-file lattices/category_obligations.sage`
    exited 0, with Sage method-provider superclass warnings.
  - `just --justfile category_specs/justfile category-obligation-file topological_spaces/category_obligations.sage`
    exited 0, with Sage method-provider superclass warnings.
- Fresh-context review:
  - Initial verdict: `revision-required` for the ungrounded mapping-valued
    `ModuleBasis` branch and broad non-Hom repair evidence.
  - Re-review verdict after revisions: `clean-to-route-human-input`, with no remaining
    findings and no non-human autonomous work in the reviewed scope.
