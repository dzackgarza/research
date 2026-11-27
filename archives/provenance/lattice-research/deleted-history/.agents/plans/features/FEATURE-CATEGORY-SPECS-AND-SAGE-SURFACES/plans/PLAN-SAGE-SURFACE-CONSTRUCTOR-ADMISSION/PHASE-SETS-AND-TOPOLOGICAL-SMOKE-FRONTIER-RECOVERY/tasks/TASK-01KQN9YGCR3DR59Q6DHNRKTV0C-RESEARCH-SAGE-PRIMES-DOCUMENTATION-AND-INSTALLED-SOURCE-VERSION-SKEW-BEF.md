---
id: TASK-01KQN9YGCR3DR59Q6DHNRKTV0C-RESEARCH-SAGE-PRIMES-DOCUMENTATION-AND-INSTALLED-SOURCE-VERSION-SKEW-BEF
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Research Sage Primes documentation and installed-source version skew before
  admitting congruence-class prime subset vocabulary
status: complete
priority: high
description: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
successCriteria:
- The research result cites the exact sources searched and separates source evidence
  from inference.
- 'Negative findings use the repository five-field format: Searched, Found, Conclusion,
  Confidence, Gaps.'
- Any admitted design consequence is linked to a spec-work or design-decision item
  rather than buried in prose.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Research Sage Primes documentation and installed-source version skew before admitting congruence-class prime subset vocabulary
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- Canonical set mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`,
  especially the `Primes()` row and Sage Primes source note.
- Source inventory: `category_specs/sets/docs/SAGE_INVENTORY.md`.
- Legacy source provenance: `category_specs/sets/docs/MAPPING.md`.
- Original migrated line: `Research Sage Primes documentation and installed-source version skew before admitting congruence-class prime subset vocabulary from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Acceptance Criteria

- [x] The research result cites the exact sources searched and separates source evidence from inference.
- [x] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [x] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary. No set implementation was attempted in this research card; the prerequisite implementation route is the `Primes()` row in `[[SPEC-MAPPING-SETS]]`.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Research Result

Source evidence:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md` maps Sage `Primes()` to `PrimesSets` and records that `Sets().Primes()` is the one-object category for Sage's set of prime integers.
- The same mapping row keeps `PrimeSubset` and `PrimesInArithmeticProgressions` as subobject vocabulary of `Primes()` unless Sage exposes distinct parent objects with required method signatures.
- `category_specs/sets/docs/SAGE_INVENTORY.md` records the installed `Primes()` category as `InfiniteEnumeratedSets().Facade()` and inventories the full-prime-set methods `__contains__`, `__iter__`, `cardinality`, `first`, `next`, `an_element`, and `unrank`.
- Installed Sage source at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/primes.py` defines `class Primes(Set_generic, UniqueRepresentation)`, `__classcall__(cls, proof=True)`, `__init__(self, proof)`, category `InfiniteEnumeratedSets()`, membership in `ZZ`, and the methods `_an_element_`, `first`, `next`, and `unrank`.
- A Sage runtime probe showed signature `Primes(proof)`, category `Category of facade infinite enumerated sets`, available checked methods `__contains__`, `first`, `next`, and `unrank`, and rejection of multi-argument calls such as `Primes(5, [1, 2])`.

Inference:

- The installed Sage surface supports only the full set of prime integers through `Primes(proof=True)`.
- Hosted documentation evidence already recorded in `[[SPEC-MAPPING-SETS]]` mentions congruence-data prime subsets, so the installed source and hosted documentation should be treated as version-skewed until Sage history or package metadata pins the boundary.
- The current project spec should admit `Primes()` as the full-prime-set constructor only. Congruence-class prime subsets should remain subobjects of `Primes()` or a future named refinement only after source-backed signatures require it.

## Negative Finding: Installed Congruence Prime Subsets

- Searched: `category_specs/sets/docs/SAGE_INVENTORY.md`; `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`; installed source `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/primes.py` lines 1-180; Sage runtime signature and constructor calls for `Primes()`, `Primes(5)`, `Primes(5, [1, 2])`, and `Primes(5, [1, 2], [])`; broad `rg` searches in installed `sage/sets` and `sage/rings` for `Primes`, `congruence`, `residue`, `modulus`, and `arithmetic progression`.
- Found: Installed `sage/sets/primes.py` exposes `Primes(proof=True)` for the full prime set and no installed `Primes(modulus, classes, exceptions)` constructor surface in that file. Runtime multi-argument constructor calls fail with `TypeError`. The broad installed-source search did not reveal a relevant congruence-class `Primes` parent under `sage/sets`.
- Conclusion: inference based on the searched local sources: the installed Sage build does not expose a Sage-backed congruence-class prime-subset parent through `Primes`, so the project should not admit that as a current Sage-backed public constructor.
- Confidence: Medium.
- Gaps: Sage git history, release tags, package metadata, and hosted documentation pages were not re-searched in this pass beyond the source note already recorded in `[[SPEC-MAPPING-SETS]]`. The broad installed-source `rg` search was noisy and is not an exhaustive proof that no unrelated Sage module can construct a congruence prime subset by another name.

## Design Consequence

- The implementation route is the existing `Primes()` mapping row in `[[SPEC-MAPPING-SETS]]`: full `Primes()` maps to `PrimesSets`.
- Congruence-class prime subsets remain subobjects of the full prime set, or a future named `PrimesInArithmeticProgressions` refinement if a later source-grounded signature requires that vocabulary.
- Generic Sage `Set(X)` remains rejected as a public project constructor by the same constructor-mapping table; this task does not reopen it.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06: Recorded installed-source and runtime evidence for Sage `Primes()` version skew, linked the design consequence to `[[SPEC-MAPPING-SETS]]`, and left congruence-class prime subsets out of the public constructor surface pending stronger source evidence.

## Review Log

### Review 2026-05-06 (Euclid)

**Gates passed:** Gates 1-2
**Gates failed:** Gate 3 Spec-Weakening
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 3 Finding: Acceptance Criterion Weakening

- The frontmatter criterion required any set implementation to cite the exact mapping
  row and prove behavior through project category vocabulary.
- The body checklist had replaced that criterion with a different research-only
  statement: no set implementation was attempted.

#### Rework

- Restored the body checklist criterion to match the frontmatter requirement.
- Kept the research-only clarification as an explanatory second sentence, not a
  replacement for the criterion.
- Added canonical tracked source provenance for the `Primes()` mapping row and Sage
  Primes source note.

### Re-review 2026-05-06 (Linnaeus)

**Gates passed:** Gates 1-6
**Gates failed:** None
**Outcome:** needs-agent-review evidence ready for human approval; card not marked complete

#### Evidence

- Sources and inference are separated in the Research Result, and the installed
  congruence-prime-subset negative finding uses the required five-field format.
- Frontmatter criteria match the checked body criteria, including the restored
  implementation criterion and the research-only clarification.
- The prior Gate 3 weakening is documented and reworked within this card's scope.
- The design consequence matches `SPEC-MAPPING-SETS.md`, and the installed Sage source
  supports only the limited `Primes(proof=True)` surface found by this research pass.
