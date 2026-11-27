---
id: SPEC-01KQN9YGCCQ9EDZWW6H98WDY3X-AUDIT-THE-VARIADIC-SIGNATURE-SCOPING-RESULT-AND-OPEN-OWNER-SPECIFIC-FOLL
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
title: Audit the variadic signature scoping result and open owner-specific follow-ups
  for any public surface still using placeholder collapsed Sage casework
status: complete
priority: critical
requirement: The deleted variadic inventory records the scoping pass for public surfaces
  that had collapsed Sage casework or raw coordinate interop into broad signatures.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created.
- No implementation blocker was discovered in this audit pass.
- Public signatures were audited for remaining `*args`, `**kwargs`, option bags, and
  placeholder union data shapes from the recovered inventory.
- No owner-specific tasks were opened because the only remaining `*args`/`**kwargs`
  hits are private Cat aggregation hooks, now mapped as nonpublic infrastructure.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework
## Summary

The deleted variadic inventory records the scoping pass for public surfaces that had
collapsed Sage casework or raw coordinate interop into broad signatures.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file
  actually lived at `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`
  and was removed in commit `8d1c21c`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework from category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`
- Recovery check: the recovered inventory records the scoping result as already split
  across modules, rings, tensor algebra components, algebras, lattices, posets, sets,
  and topological spaces.

Stale-path check:

- Searched: `git show 8d1c21c^:category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`,
  then broadened with `git ls-tree -r --name-only 8d1c21c^ | rg 'VARIADIC_SIGNATURE_INVENTORY|category_specs/docs|plans/category_specs/docs'`.
- Found: the `category_specs/...` path is absent at `8d1c21c^`; the recoverable file
  is `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Conclusion: inference - the card's migrated source path was stale, but the exact
  source inventory is recoverable from the deleted `plans/` tree.
- Confidence: High.
- Gaps: none for the existence and location of this deleted source file.

## Context

- Module constructors and quotient inputs were split and mapped in modules docs/code.
- Ring constructors, p-adic precision tuples, series factories, matrix element construction, and number-field optional arguments were split and mapped in rings docs/code.
- Tensor component catch-all data was removed from public surface in favor of named constructors.
- Algebra subalgebra and ideal option bags were split into named methods.
- Lattice short_vectors kwargs were split into short_vectors(bound) and short_vectors_up_to_sign(bound).
- Poset, set iterator, element-class forwarding, and RealSet variadics were mapped or excluded from public specs.

## Source-Mining Contract

This card is an audit card. Its job is to identify public surfaces that still collapse
finite Sage casework into placeholder signatures and to pin each one to its real owner.

- Primary source anchors:
  - `.agents/skills/category-spec-style/references/style.md`, especially the no-variadic
    and overload rules;
  - `category_specs/modules/docs/MAPPING.md`;
  - `category_specs/forms/docs/MAPPING.md`;
  - `category_specs/lattices/docs/MAPPING.md`;
  - `category_specs/cat/docs/MAPPING.md`;
  - `category_specs/homsets/docs/MAPPING.md`;
  - Sage written docs/source for the exact public surface under audit.
- For each audited surface, record the closed set of mathematical input patterns Sage
  actually supports, the owner category or constructor namespace, the codomain/return
  object, and any compatibility obligation to preserve already-mapped call routes.
- Placeholder unions, `*args`, `**kwargs`, and option bags stay out of the public spec
  unless the source material proves a genuinely open-ended mathematical family. Finite
  Sage casework must be restated as named constructors or explicit overload families.
- When an audited surface crosses module, forms, lattice, or hom/end/aut boundaries,
  use the existing mapping docs to pin the owner instead of re-opening the owner
  question in this card.
- If audit work hits a surface whose owner or definition is still unresolved, record
  that concrete blocker here rather than papering it over with another generic grounding
  gate.

## Audit Result

The current public category-spec surfaces match the recovered scoping result:

| Surface family | Current owner and result |
| --- | --- |
| Module constructors and quotient inputs | `category_specs/modules/docs/MAPPING.md` records named constructors for rank, basis-key, inner-product, FPModule, integer-lattice, torsion-quadratic, ring-as-module, and quotient input shapes. Current module code uses named methods such as `FreeModuleWithBasisKeys`, `FPModuleFromCokernelMap`, `quotient_by_relation_matrix`, and series/ring bridge methods instead of the recovered collapsed signatures. |
| Ring constructors, p-adic precision, series factories, matrix element construction, and number-field optional arguments | `category_specs/rings/docs/MAPPING.md` records the closed constructor split. Current ring code has named number-field tower, p-adic cap/relaxed/prime-power/factorization, polynomial, series, matrix-element, discriminant, integral-basis, and order/maximal-order surfaces rather than the recovered collapsed inputs. |
| Tensor component data | `category_specs/tensor_algebra_components/docs/MAPPING.md` rejects the catch-all component constructor and admits only named tensor constructors plus explicit `trace(...)` and `contract(...)`. |
| Algebra subalgebra and ideal option bags | `category_specs/algebras/docs/MAPPING.md` maps Sage option bags to `subalgebra(generators)`, left/right/two-sided ideal methods, and principal left/right/two-sided ideal methods. |
| Lattice `short_vectors(..., **kwargs)` | `category_specs/lattices/docs/MAPPING.md` splits the only sourced keyword case into `short_vectors(bound)` and `short_vectors_up_to_sign(bound)`. |
| Poset, set, and RealSet variadics | `category_specs/posets/docs/MAPPING.md`, `category_specs/sets/docs/MAPPING.md`, and `category_specs/topological_spaces/docs/MAPPING.md` keep raw variadic constructors private or rejected and expose named constructor families. |
| Cat constructor aggregation | `category_specs/cat/docs/MAPPING.md` now records that generated `Cat().Constructors()` forwarding hooks are private Python/Sage dispatch glue, not public variadic mathematical surfaces. |

Remaining public-variadic check:

- Searched: recovered variadic inventory; `.agents/skills/category-spec-style/references/style.md`;
  current module, ring, tensor, algebra, lattice, poset, set, topological-space, and
  Cat mapping files; `rg -n "def .*\\*args|def .*\\*\\*kw|def .*\\*\\*kwargs|def .*kwds|args:|kwargs:" category_specs -g '*.py'`; and targeted reads of the current files named in the recovered inventory.
- Found: no remaining public constructor or method from the recovered inventory still
  exposes raw `*args`, `**kwargs`, `kwds`, or an unresolved placeholder union. The only
  live code hits are Cat internal generated forwarding/subclass-registration hooks,
  now mapped as private aggregation plumbing in `category_specs/cat/docs/MAPPING.md`.
- Conclusion: inference - this audit leaf has no owner-specific follow-up tasks to
  open for remaining collapsed Sage casework.
- Confidence: Medium.
- Gaps: this audit covers the recovered inventory plus current textual signature
  searches; it is not a fresh exhaustive semantic review of every finite union in every
  typed collection signature.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] No implementation blocker was discovered in this audit pass.
- [x] Public signatures were audited for remaining `*args`, `**kwargs`, option bags, and placeholder union data shapes from the recovered inventory.
- [x] No owner-specific tasks were opened because the only remaining `*args`/`**kwargs` hits are private Cat aggregation hooks, now mapped as nonpublic infrastructure.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted variadic inventory from `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` after the migrated `category_specs/...` provenance path proved stale.
- Audited the recovered inventory against current module, ring, tensor, algebra, lattice, poset, set, topological-space, and Cat mapping/code surfaces.
- Added Cat mapping for generated constructor aggregation forwarders so future audits do not mistake private dispatch glue for a public variadic constructor.
- Skipped subtree category-obligation examples and global QC intentionally; this was a documentation/source-map audit, not implementation integration or phase transition.

## 6-Gate Protocol Review Log

**Reviewer:** Hermes Agent subagent
**Date:** 2026-05-07

### G1 — Source Grounding

| Check | Result | Evidence |
|-------|--------|----------|
| Deleted inventory file recoverable | PASS | `git show 8d1c21c^:plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` returns 406 lines of inventory content. Commit `8d1c21c` exists in repo. |
| Stale-path correction accurate | PASS | The card correctly identifies the migrated `category_specs/...` path as stale and provides the correct `plans/`-prefixed recovery command. |
| Primary source anchors valid | PASS | `.agents/skills/category-spec-style/references/style.md` lines 52-92 contain the exact "No Variadic Signatures" rule (line 57) and "Sage Interop Uses Overloads, Not Variadics" rule (line 76). All referenced MAPPING.md files exist (as redirects to tracked spec files). |
| Reference chain intact | PASS | `style.md` → MAPPING redirects → tracked SPEC-MAPPING-*.md files form a verifiable source chain. SPEC-MAPPING-MODULES.md lines 217-242 document the explicit constructor split from variadic to named forms. |

**G1 Verdict: PASS.** Source grounding is verifiable, correct, and the stale-path remediation is properly documented.

### G2 — Sage Surface Completeness

| Check | Result | Evidence |
|-------|--------|----------|
| All 8 surface families covered | PASS | The audit table covers modules, rings, tensors, algebras, lattices, posets, sets, topological-spaces, plus Cat constructor aggregation. This matches the recovered inventory scope exactly. |
| Each surface mapped to owner | PASS | Every row names a `category_specs/.../docs/MAPPING.md` (or its tracked spec successor) as the owning document. |
| Cat private dispatch documented | PASS | `category_specs/cat/docs/MAPPING.md` redirects to SPEC-MAPPING-CAT.md, which records that generated Cat constructor forwarding hooks are private aggregation plumbing. |

**G2 Verdict: PASS.** No Sage surface family from the recovered inventory is unaccounted for.

### G3 — Mathematical Correctness

| Check | Result | Evidence |
|-------|--------|----------|
| No public `*args`/`**kwargs` remaining | PASS | `rg "def .*\*args\|def .*\*\*kw" category_specs -g '*.py'` returns hits only in `cat/base_category_types.py`. |
| Cat hits are private infrastructure | PASS | Lines 204-209: `_cat_constructor_forwarder` (underscore prefix, `_cat_constructor_generated_forwarder = True`). Lines 411-424: `__init_subclass__` metaclass hook and `initialize_and_register` wrapper (underscore-prefixed private `__init__` wrapper). All three are category framework plumbing, not public mathematical surfaces. |
| No placeholder unions found | PASS | The recovered inventory's replacement surfaces use named constructors (`FreeModuleWithBasisKeys`, `FPModuleFromCokernelMap`, `short_vectors(bound)`, `short_vectors_up_to_sign(bound)`, etc.) — all mathematically grounded types, not software-engineering shortcuts. |
| Overload rule compliance | PASS | The constructor splits follow the style reference's overload rule (lines 65-71): finite input patterns are split into explicit `@overload` cases; `*args`/`**kwargs` catch-all forwarding is absent from public surfaces. |

**G3 Verdict: PASS.** The central mathematical claim — no remaining public variadic surface from the recovered inventory — is verified by code search and the documented private nature of the only code hits.

### G4 — Nonmathematical Rejection

| Check | Result | Evidence |
|-------|--------|----------|
| Variadics rejected from public spec | PASS | The card enforces the style rule: variadic signatures, option bags, and placeholder unions are kept out of public specs. |
| No engineering-only data shapes | PASS | All replacement constructors use mathematically meaningful types (Matrix, Sequence[RingElement], etc.), not shortcut wrapper types. |
| Sage implementation containers rejected | PASS | The mapping specs explicitly reject nonmathematical targets and raw Sage implementation containers (per Review Gates in SPEC-MAPPING-MODULES.md line 39). |

**G4 Verdict: PASS.** The audit does not introduce or preserve nonmathematical constructs.

### G5 — Ambiguity Routing

| Check | Result | Evidence |
|-------|--------|----------|
| Confidence stated with caveats | PASS | Card states "Confidence: Medium" with explicit gap: "this audit covers the recovered inventory plus current textual signature searches; it is not a fresh exhaustive semantic review of every finite union." |
| Unresolved ownership routed properly | PASS | Ore module ownership is deferred to tracked decisions rather than resolved in-place (SPEC-MAPPING-MODULES.md line 131). |
| No papering-over detected | PASS | The gap is acknowledged transparently; no attempt to inflate confidence or claim exhaustive coverage. |

**G5 Verdict: PASS.** Ambiguity is properly acknowledged and routed, not hidden.

### G6 — Obligation Preservation

| Check | Result | Evidence |
|-------|--------|----------|
| Acceptance criteria met | PASS | All 5 acceptance criteria are marked `[x]` with verifiable evidence in the body. |
| No subtree-local TRIAGE created | PASS | Card body and work log confirm no new process documents were created. |
| Source provenance preserved | PASS | Card preserves the stale source path alongside the corrected recovery path for future traceability. |
| Cat mapping added preventively | PASS | Work log records that Cat constructor aggregation forwarders were mapped to prevent future audits from misclassifying them. |
| No implementation blocker | PASS | Card explicitly states no blocker was discovered. |

**G6 Verdict: PASS.** All obligations from the audit contract are preserved and satisfied.

### Overall 6-Gate Verdict

**ALL GATES PASS.** The VARIADIC-SIGNATURE-SCOPING spec is source-grounded, Sage-surface-complete, mathematically correct, free of nonmathematical constructs, appropriately routes ambiguity, and preserves all obligations. The one caveat — that this is a textual signature audit rather than an exhaustive semantic review of every typed collection — is transparently acknowledged with Medium confidence, and is properly scoped to the card's stated purpose (documentation/source-map audit, not implementation integration).
