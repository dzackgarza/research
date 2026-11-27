---
id: TASK-1777748120440-BRC1SX-SPLIT-BOOLEAN-AND-OPTIONAL-RETURN-SHAPE-SIGNATURES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Split rings boolean and optional return-shape signatures
status: complete
priority: critical
description: Split the source-backed rings boolean and optional return-shape
  signatures for root extraction and number-field Galois closures.
successCriteria:
- Rings root-extraction overloads split `all=False`, `all=True`, and non-literal
  `bool` return shapes without asserting choice-independent equality of selected
  roots.
- Number-field `galois_closure(map=False)`, `galois_closure(map=True)`, and
  non-literal `bool` return shapes are split without asserting uniqueness of the
  selected closure presentation.
- The card records exact Sage source paths, owner categories, hypotheses, codomains,
  and branch-choice obligations for each admitted overload family.
- Out-of-scope Category, Map, matrix, and generic extension boolean surfaces are
  explicitly recorded as non-executed until separately source-grounded.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Split rings boolean and optional return-shape signatures
Source: pasted backlog 2026-05-02.

Task: split the source-backed rings boolean and optional return-shape signatures
for root extraction and number-field Galois closures into explicit `@overload`
declarations. The pasted backlog originally named Category and Map classes broadly;
the executable scope of this card is the rings-only source-backed overload set
identified in the source audit below. Category, Map, matrix, and generic extension
boolean surfaces remain out of scope until separately source-grounded.

## Acceptance Criteria

- [x] Rings root-extraction overloads split `all=False`, `all=True`, and non-literal
  `bool` return shapes without asserting choice-independent equality of selected
  roots.
- [x] Number-field `galois_closure(map=False)`, `galois_closure(map=True)`, and
  non-literal `bool` return shapes are split without asserting uniqueness of the
  selected closure presentation.
- [x] Exact Sage source paths, owner categories, hypotheses, codomains, and
  branch-choice obligations are recorded for each admitted overload family.
- [x] Out-of-scope Category, Map, matrix, and generic extension boolean surfaces are
  recorded as non-executed until separately source-grounded.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`, plus the current sprint plan
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md` requires
  closed overloads for finite Sage casework and source-backed return objects.
- Sage grounding:
  - `NumberField.galois_closure(map=False)` returns the Galois closure field, while
    `map=True` returns the field with an embedding of the source field into it.
  - Algebraic `nth_root(all=False)` and `sqrt(all=False)` return one root; `all=True`
    returns the finite list of all roots. Finite residue, real-field, power-series,
    Laurent-series, and Tate-algebra `nth_root` sources ground the root-level option
    controls `extend`, `algorithm`, `cunningham`, and `prec`.
- Canonical local mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
  records the overload policy, exact Sage source paths, owner categories, hypotheses,
  codomains, and branch-choice obligations for these boolean-controlled return-shape
  methods.
- Exact Sage sources:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/number_field/number_field.py:9177-9219`
  for `NumberField.galois_closure(names=None, map=False)`;
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/structure/element.pyx:3263-3284`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/qqbar.py:4312-4329`,
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/complex_mpfr.pyx:2988-2997`
  for `sqrt(..., all=...)`; and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/qqbar.py:4393-4429`
  plus
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/complex_mpfr.pyx:3058-3079`
  for algebraic and complex `nth_root(n, all=...)`; and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/finite_rings/integer_mod.pyx:1367-1517`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/real_mpfr.pyx:5422-5433`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/power_series_ring_element.pyx:1822-1833`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/laurent_series_ring_element.pyx:1702-1712`,
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/tate_algebra_element.pyx:1666-1676`
  for root-level `nth_root` option shapes.
- Owner/codomain contract: `galois_closure` belongs to number-field parent methods and
  returns either the closure field or `(closure field, source embedding)`;
  `sqrt` and `nth_root` belong to `Rings().ElementMethods` as broad root-extraction
  element surfaces, with subcategory implementations carrying the stronger existence
  and computability hypotheses. `all=False` returns one selected root where the family
  implements it; `all=True` returns the finite list of roots on documented all-roots
  surfaces. `extend`, `algorithm`, `cunningham`, and `prec` are source-backed
  computation or precision controls, not owner changes. The overload split types
  Sage's documented branch behavior; it does not assert choice-independent equality of
  selected roots or Galois-closure presentations, and it does not assert that every
  ring element has every root.

## Result

- Added `Literal[False]`, `Literal[True]`, and non-literal `bool` fallback overloads
  for root-return shapes in `category_specs/rings/__init__.py`.
- Added the same overload split for specialized `nth_root` overrides in
  `category_specs/rings/subcategories/algebraic_closure_of_rational_field.py` and
  `category_specs/rings/subcategories/real_algebraic_field.py`.
- Added `map=False`/`map=True` overloads plus a non-literal `bool` fallback for
  `galois_closure` in `category_specs/rings/subcategories/number_field.py` and
  `category_specs/rings/subcategories/rational_field.py`.

## Review Log

### Review 2026-05-06 (Dirac)

**Gates passed:** None
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Source-Grounding For Boolean Return Shapes

- The card introduced public overloads for `nth_root`/`sqrt` and `galois_closure`, but
  grounded them only in prose behavior and the legacy `category_specs/rings/docs/MAPPING.md`
  redirect.
- The canonical rings spec recorded the return-shape policy but did not yet record exact
  Sage source paths, definitions, owner categories, hypotheses, codomains, or branch
  choice/equivalence obligations for each affected method.

#### Rework

- Added exact installed Sage source paths for `galois_closure`, `sqrt`, and
  `nth_root` to this card and to `SPEC-MAPPING-RINGS.md`.
- Recorded the owner category, hypotheses, codomain/return object, and branch-choice
  obligation for each affected overload family.

### Review 2026-05-06 (Bernoulli)

**Gates passed:** None
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Root-Level `nth_root` Owner And Option Shapes

- The first rework grounded algebraic and complex `nth_root(all=...)` sources, but the
  implemented public overloads live on universal `Rings().ElementMethods` and include
  `extend`, `algorithm`, `cunningham`, and `prec`.
- Those option shapes require direct Sage source grounding for the root element-method
  surface rather than only algebraic/complex all-roots examples.

#### Rework

- Grounded the root-level `nth_root` overload in finite residue ring, real-field,
  power-series, Laurent-series, and Tate-algebra Sage sources.
- Clarified that the broad owner is `Rings().ElementMethods`, while existence,
  computability, branch conventions, precision, and optional algorithm controls are
  family-specific implementation obligations.

### Review 2026-05-06 (Lovelace)

**Gates passed:** Gate 1 Definition Grounding
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 2 Finding: Card Scope Did Not Match Delivered Work

- The migrated task sentence still said "Category and Map classes", while the
  grounded implementation and mapping evidence are rings-only overloads on
  `Rings().ElementMethods` and number-field parent methods.
- The frontmatter success criterion pointed to missing body acceptance criteria.

#### Rework

- Retitled and redescribed the card as the rings boolean/optional return-shape leaf.
- Added explicit frontmatter and body acceptance criteria for root extraction,
  `galois_closure`, source grounding, and out-of-scope boolean surfaces.

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass with concrete falsifiable evidence.

- Gate 1: `nth_root`/`sqrt`/`galois_closure` overloads grounded in SPEC-MAPPING-RINGS.md with exact Sage source paths, owner categories, hypotheses, codomains.
- Gate 2: All 4 ACs satisfied (root overloads split, galois_closure overloads split, source paths recorded, out-of-scope Category/Map surfaces documented).
- Gate 3: Only adds content. No overloads, obligations, or category assertions removed. SPEC-MAPPING-RINGS gained 61 lines. No prior content removed.
- Gate 4: No decision reversal. Git history shows additive commits only.
- Gate 5: `all=False`→RingElement, `all=True`→list[RingElement], `bool`→union. `map=False`→Field, `map=True`→tuple. Correct mathematical semantics. No choice-independent equality asserted.
- Gate 6: `@overload` patterns. No variadic. `Literal` for True/False. Import hygiene.

## Out Of Scope Findings

## Complexity Justification

- Searched: `category_specs/cat/docs/MAPPING.md`, `category_specs/cat/docs/SAGE_INVENTORY.md`,
  `category_specs/cat/*.py`, `category_specs/homsets/*.py`, current `category_specs`
  Python signatures for `map: bool`, `all: bool`, `transformation: bool`, `bool | None`,
  and union return types, plus Sage installed docs/source for number-field closures,
  algebraic roots, and matrix echelon forms.
- Found: no current Cat/functor-hom core method with a closed boolean-controlled return
  shape. Concrete source-backed hits are in ring and algebraic-number surfaces.
  `echelon_form(transformation=True)` is not patched here because Sage matrix docs/source
  allow backend-dependent behavior rather than a clean closed overload contract.
  Generic `extension(..., map=...)` forwarding needs separate source grounding before
  changing its public contract.
- Conclusion: inference - this card's executable scope is the source-backed ring/root
  overload split above, not a broad Cat/homsets rewrite.
- Confidence: Medium-high.
- Gaps: this pass covered current textual signatures and relevant Sage docs/source for
  the found hits; it is not a fresh semantic review of every Sage boolean parameter in
  every possible upstream backend.

## Complexity Justification
- Owner: C55
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Split boolean and optional return-shape signatures
- Why this specific score:
  - This is a typed-API refactor scoped to category/map methods, but it touches many call signatures and forces coherent overload behavior across public methods. The risk is concentrated (typing correctness) rather than runtime behavior, matching a moderate complexity window.
- Item-specific evidence:
  - The task is tightly scoped to `Category` and `Map` return-shape changes and calls out `bool|None` / `T|None` unbundling, indicating a coordinated but bounded interface contract clean-up.
  - No additional files are named, so validation burden is mostly static typing consistency and downstream method callsites.
