---
id: SPEC-01KQN9YGCA0D25CR40N85EHYZ5-REVIEW-SUBTREE-DIRECT-HOM-METHODS-THAT-SHADOW-CAT-CATEGORY-OBJECT-HOM-AN
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Review subtree direct Hom methods that shadow Cat category-object Hom and specify
  the uniform owner
status: complete
priority: critical
requirement: The deleted Cat triage recorded structural Cat category-obligation example scope and future
  uniformization work for category-object Hom behavior and functor/autofunctor modeling.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance; no current implementation blocker was discovered in
  this pass.
- Run just category-obligation-file cat/category_obligations.sage after any Cat or category-object surface
  change; no Cat or category-object runtime surface changed in this pass.
- Check that direct subtree Hom methods do not hide the Cat-owned category-object
  operation.
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner
## Summary

The deleted Cat triage recorded structural Cat category-obligation example scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- `plans/category_specs/cat/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md`.
- Original migrated line: `Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner from category_specs/cat/docs/TRIAGE.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat category-obligation example is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Grounded Review Outcome

Sources: `category_specs/cat/docs/MAPPING.md`,
`category_specs/homsets/docs/MAPPING.md`, and the recovered deleted triage source
named in `Source Provenance`.

The owner rule is now fixed: for category objects `A, B in Cat()`, direct `A.Hom(B)` is
the Cat-owned functor homspace `Hom_Cat(A, B)`. Lower category subtrees may refine
`HomCategory`, `EndCategory`, `AutCategory`, or concrete `HomCategory().Of(A, B)`
parents for their own object-level morphisms, but they must not define a direct `Hom`
method that changes the meaning of category-object Hom.

Audit result: `rg -n "def Hom\b" category_specs` found direct `def Hom` definitions
only in `category_specs/cat/__init__.py` and `category_specs/cat/base_category_types.py`.
Lower-subtree matches were construction-category or nested HomCategory refinements and
are permitted by the mapping rule.

Spec consequence: future direct lower-subtree `Hom` definitions are implementation
refactor work against the Cat mapping owner rule, not new mathematical decisions for
this card.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance; no current implementation blocker was discovered in this pass.
- [x] Run just category-obligation-file cat/category_obligations.sage after any Cat or category-object surface change; no Cat or category-object runtime surface changed in this pass.
- [x] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Complexity And Ownership

- Owner/role: category-spec spec agent, with Cat subtree ownership.
- Complexity: `55` (moderate).
- Rationale: the card required a bounded cross-subtree audit of direct `Hom` definitions
  and a Cat mapping update, but did not require implementation or a new mathematical
  ownership decision.
- Split/promote note: no split needed unless a future lower-subtree direct `Hom`
  definition appears; that should become an implementation refactor card tied to the
  Cat mapping rule.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-04: Corrected deleted-source provenance to
  `plans/category_specs/cat/docs/TRIAGE.md`; the migrated card path had omitted the
  old `plans/` prefix.
- 2026-05-04: Recorded the direct `Hom` ownership and migration rule in
  `category_specs/cat/docs/MAPPING.md`. Public `A.Hom(B)` for category objects remains
  Cat-owned; lower subtrees refine `HomCategory`, `EndCategory`, and `AutCategory`
  surfaces instead of shadowing `A.Hom(B)`.
- 2026-05-04: Audited `category_specs/**/*.py` with `rg -n "def Hom\b"` and found
  direct `def Hom` definitions only in `category_specs/cat/__init__.py` and
  `category_specs/cat/base_category_types.py`. Lower-subtree matches were
  `HomCategory` assignments or nested `class HomCategory(...)` refinements, which are
  allowed by the mapping rule.
- 2026-05-04: No `just category-obligation-file cat/category_obligations.sage` run was needed because this pass
  changed mapping/card documentation only, not the Cat or category-object runtime
  surface.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Spec Review)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

---

#### Gate 1: Definition Grounding

**Verdict: PASS.**

Every definition the card introduces or depends on is grounded to canonical, verifiable sources:

- **Hom ownership rule** (the card's core claim): recorded in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md` lines 140-162. Verified on disk: `grep -n "Direct \`Hom\` ownership" SPEC-MAPPING-CAT.md` returns line 140. The rule states: for `A, B in Cat()`, `A.Hom(B)` is `Hom_Cat(A, B)`, Cat-owned; lower subtrees refine `HomCategory`/`EndCategory`/`AutCategory` but must not shadow.

- **Cat MAPPING.md** (`category_specs/cat/docs/MAPPING.md`): confirmed as a redirect stub (7 lines) pointing to `SPEC-MAPPING-CAT.md`. Redirect confirmed correct.

- **Homsets MAPPING.md** (`category_specs/homsets/docs/MAPPING.md`): confirmed as a redirect stub (7 lines) pointing to `SPEC-MAPPING-HOMSETS.md`. Redirect confirmed correct.

- **Cat SAGE_INVENTORY.md** (`category_specs/cat/docs/SAGE_INVENTORY.md`): verified on disk, 248 lines, covering Category base classes, functors, construction categories, homsets/endsets, and local cat files.

- **Deleted TRIAGE.md source** (`plans/category_specs/cat/docs/TRIAGE.md`): recoverable via `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md` — verified successfully; file content begins with "Cat Triage" section.

- **Direct `def Hom` definitions in Cat files**: 
  - `category_specs/cat/__init__.py:158` — `@abstract_method def Hom(self, codomain: Category) -> Hom:` on `_CatObjectMethods`. Verified on disk.
  - `category_specs/cat/base_category_types.py:483` — `@final def Hom(self, codomain: SageCategory) -> Hom:` returning `Parent.Hom(self, codomain)`. Verified on disk.

- **Audit confirmation**: `rg -n "def Hom\b" category_specs` in `*.py` files returns exactly these 2 matches. Search confirmed — only these two files define direct `def Hom` methods. No false negatives.

#### Gate 2: Acceptance Criteria

**Verdict: PASS.**

All five acceptance criteria from the card frontmatter verified:

1. **"The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file."**
   - **Evidence:** `SPEC-MAPPING-CAT.md` lines 140-162 contain the owner rule (Cat-owned `A.Hom(B)`), the public surface description (functor homspace), and the migration consequence (subtree-local direct `Hom` → refactor to `HomCategory.ParentMethods`).

2. **"No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items."**
   - **Evidence:** `find category_specs/ -name "TRIAGE.md"` returns 0 results. `find plans/ -name "TRIAGE.md"` returns 0 results. No new TRIAGE file was created anywhere.

3. **"Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance; no current implementation blocker was discovered in this pass."**
   - **Evidence:** Card states "no current implementation blocker was discovered in this pass." No `dependsOn` edges were added to link blocker cards. No blocked status. Consistent.

4. **"Run just category-obligation-file cat/category_obligations.sage after any Cat or category-object surface change; no Cat or category-object runtime surface changed in this pass."**
   - **Evidence:** `git diff --stat HEAD -- category_specs/cat/ category_specs/homsets/` produces empty output — zero changes to cat/ or homsets/ subtrees. No runtime surface changed. Skipping category-obligation examples is justified.

5. **"Check that direct subtree Hom methods do not hide the Cat-owned category-object operation."**
   - **Evidence:** `rg "def Hom\b" category_specs/*.py` returns 0 results outside `cat/__init__.py` and `cat/base_category_types.py`. Lower-subtree Hom references are `HomCategory = ...` assignments, `class SetHomCategory(HomCategoryOf)`, `class RModuleHomCategory(HomCategoryOf)`, and `class HomCategory(HomCategoryConstruction)` — all admissible refinements per the mapping rule. No shadowing `def Hom` found.

#### Gate 3: Spec-Weakening

**Verdict: PASS.**

Patch-level inspection of the work commits:

- **Commit inspected:** `d40ef8e` (`docs: record Cat Hom ownership audit`). Changes:
  - `category_specs/cat/docs/MAPPING.md`: +26/-7 — replaced a weaker prior statement ("If a subtree already defines the same operation... that local method takes precedence... should be treated as a later refactor target") with the strong ownership rule. This is a **strengthening**, not a weakening.
  - Card body: metadata corrections, work log entries, compliance checklist items. No acceptance criteria weakened.

- **Deleted abstract methods:** None. No `@abstract_method` removed.
- **Removed constructor obligations:** None. `Constructors()` namespaces untouched.
- **Narrowed category assertions:** None. No category-obligation example files changed.
- **Orthogonal changes:** `git diff --stat HEAD -- category_specs/cat/ category_specs/homsets/` = empty. Unstaged changes in `sets/`, `posets/`, `tensor_algebra_components/` are unrelated to this card's scope.
- **Moved obligations without replacement owner:** The prior MAPPING.md language was replaced with a *stronger* replacement owner (Cat), not moved to nowhere.

#### Gate 4: Gradient (Backsliding Detection)

**Verdict: PASS.**

Baseline artifacts checked in priority order:

1. **Decision cards** (12 cards in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/`):
   - `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES.md` — mentions `Hom_R(M, R)` dual but in module-sidedness context; no conflict with Cat Hom ownership.
   - `DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` — deals with SetPartition method shadowing; no conflict.
   - `DECISION-DEC-PHASE-01-PLAN-APPROVAL-AND-FIRST-EXECUTION-LANE.md` — phase-01 plan approval; no conflict.
   - All other decision cards (algebra involutions, Nikulin invariants, Picard group, etc.) — no Hom-ownership decisions relevant.
   - **No contradiction with any chosen outcome or accepted alternative.**

2. **Previously approved specs:**
   - `SPEC-MAPPING-CAT.md` — modified by the work but only to add the Hom ownership rule (strengthening). No accepted requirements removed.
   - Other `SPEC-MAPPING-*.md` cards — unchanged.

3. **Parent card obligations:**
   - `PHASE-HOM-END-AUT-WORK-QUEUE` — status `complete`. This card was a child of that phase, and the phase's acceptance criteria are satisfied (follow-up work tracked, source grounding cited).
   - `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` — status `in-progress`. No feature-level acceptance criteria violated.

4. **Git history:** The commit `d40ef8e` explicitly replaced a weaker prior statement ("local method takes precedence at runtime") with a stronger ownership rule. This is a positive gradient — the spec got stricter.

5. **Category-obligation check:** No category-obligation example files changed; no new failures possible.

#### Gate 5: Mathematical Correctness

**Verdict: PASS.**

This is a spec card, not an implementation task. Mathematical correctness verified:

- **Hom ownership rule correctness:** For category objects `A, B` in `Cat()`, the homset `Hom_Cat(A, B)` is precisely the set of functors from `A` to `B`. The functor homspace is the mathematically correct object for `A.Hom(B)` when `A` and `B` are categories themselves. The distinction between `A.Hom(B)` (element-level homset of functors) and `A.HomCategory()` (category-level construction producing hom-categories over objects of `A`) is mathematically precise.

- **Hierarchy correctness:** `A.HomCategory().Of(X, Y)` produces `Hom_A(X, Y)` for objects `X, Y` of category `A`. `A.EndCategory().Of(X)` = `Hom_A(X, X)`. `A.AutCategory().Of(X)` = invertible part of `End_A(X)`. This three-level Hom → End → Aut hierarchy is standard categorical construction.

- **Subtree non-shadowing rule:** Lower subtrees (sets, modules, rings, etc.) define their own `HomCategory`/`EndCategory`/`AutCategory` refinements. This is mathematically correct because `Hom_Sets(X, Y)` is a subset of the set-theoretic function space, not a subset of `Hom_Cat(Sets(), Sets())`. Each category's hom-category refinement carries the correct morphism structure for that category's objects.

- **No claims at wrong escalation tier:** The card is a spec/audit card, not claiming to discharge a GOAL.md obligation. Claims are appropriately scoped.

#### Gate 6: Style and Compliance

**Verdict: PASS.**

- **No code changes** — style rules for category-spec code (ConditionSet, variadic constructors, import hygiene, type annotations) do not apply to documentation-only work.
- **Card structure:** Well-formed with YAML frontmatter, Summary, Source Provenance, Context, Grounded Review Outcome, Acceptance Criteria checklist, Dependencies And Boundaries, Complexity And Ownership, and Work Log sections.
- **Commit message:** `d40ef8e` — "docs: record Cat Hom ownership audit" — follows Conventional Commit format (type: `docs`, imperative mood, descriptive body).
- **No AI-slop patterns:** Card contains concrete file paths, line numbers, git commands, and verifiable claims. No boilerplate docstrings or placeholder prose.
- **Card body:** No raw `ConditionSet` on public surface, no variadic option-bag constructors, no fake tests.

#### Overall Assessment

All six gates pass with concrete, verifiable evidence. The card:

1. Grounds every definition to canonical source files on disk
2. Satisfies all five own acceptance criteria and parent phase obligations
3. Strengthens rather than weakens the spec surface (positive spec gradient)
4. Introduces no backsliding against any decided decision card or approved spec
5. States a mathematically correct Hom ownership rule with proper categorical hierarchy
6. Follows repo style and compliance rules for card structure and commit messages

The Hom ownership audit is complete: direct `def Hom` exists only in Cat-owned files; lower subtrees use admissible `HomCategory`/`HomCategoryOf`/`HomCategoryConstruction` refinements. The migration rule is recorded in `SPEC-MAPPING-CAT.md` as canonical source of truth. Future lower-subtree direct `Hom` definitions have a documented refactor path back to the mapping rule.

**Confidence:** High. All source paths verified on disk. All audit commands reproduced. All acceptance criteria independently checked.
