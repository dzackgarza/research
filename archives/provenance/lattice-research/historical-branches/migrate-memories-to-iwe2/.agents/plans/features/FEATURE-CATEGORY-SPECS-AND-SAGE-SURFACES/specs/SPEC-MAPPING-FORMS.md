---
id: SPEC-MAPPING-FORMS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track forms mapping spec
status: complete
priority: critical
requirement: Convert category_specs/forms/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  bilinear, quadratic, form-codomain, Hom, End, and Aut signatures.
acceptanceCriteria:
- Source paths category_specs/forms/docs/MAPPING.md and category_specs/forms/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Forms Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/forms/docs/MAPPING.md`.

Source inventory: `category_specs/forms/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and category-obligation example-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/forms/docs/SAGE_INVENTORY.md`.
- Cross-inventory source files checked because the forms inventory is an ownership
  pointer rather than an independent Sage category inventory:
  - `category_specs/modules/docs/SAGE_INVENTORY.md`
  - `category_specs/lattices/docs/SAGE_INVENTORY.md`
  - `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- Installed Sage source files checked or named by those inventories for this forms pass:
  - `sage/modules/free_quadratic_module.py`
  - `sage/modules/free_quadratic_module_integer_symmetric.py`
  - `sage/modules/torsion_quadratic_module.py`
  - `sage/tensor/modules/tensor_free_module.py`
  - `sage/tensor/modules/free_module_tensor.py`
  - `sage/quadratic_forms/quadratic_form.py`
  - `sage/quadratic_forms/quadratic_form__automorphisms.py`
  - `sage/quadratic_forms/quadratic_form__genus.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the forms
  cross-inventory reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Forms Cross-Inventory

The forms inventory names five Sage evidence families: `FreeQuadraticModule_generic`,
`FreeQuadraticModule_integer_symmetric`, `TorsionQuadraticModule`,
`TorsionQuadraticForm(q)`, and `TensorFreeModule` dual components. The converted
mapping assigns all five to explicit forms, modules, lattices, or tensor-component
owners:

- free quadratic modules map to free bilinear or quadratic formed-module structure,
  with Gram, determinant, discriminant, and inner-product surfaces first owned by
  free bilinear modules;
- integral symmetric Sage lattices map through the forms-owned nondegenerate symmetric
  integral chain, with the named `Lattices(R)` endpoint adding only lattice-specific
  specializations;
- torsion quadratic modules map to
  `forms.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory`,
  while the old module route remains constructor compatibility;
- tensor dual components remain tensor-component objects until attached as form data
  to a module;
- symmetric bilinear element divisibility is the pairing-image submodule
  `<b(v, M)> <= S`, not a free-module coordinate-gcd surface.

Negative source finding for a separate Sage forms category:

- Searched: `category_specs/forms/docs/SAGE_INVENTORY.md`, `category_specs/forms/*`,
  `category_specs/modules/docs/SAGE_INVENTORY.md`,
  `category_specs/lattices/docs/SAGE_INVENTORY.md`,
  `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`, installed Sage
  paths matching forms, free-quadratic modules, torsion-quadratic modules, tensor
  modules, and quadratic-form files under `/home/dzack/miniforge3/envs/sage`.
- Found: the local forms inventory intentionally delegates Sage evidence to the
  modules, lattices, and tensor-component inventories; installed Sage exposes the
  relevant form-bearing objects through module, tensor, and quadratic-form sources,
  not through a distinct `sage.categories.forms` owner.
- Conclusion: inference -- this pass found no separate installed Sage forms category
  that should add a new forms-local mapping surface beyond the cross-inventory
  families listed above.
- Confidence: Medium.
- Gaps: Sage upstream issue discussions, unreleased Sage branches, and a full
  method-by-method reconciliation of every quadratic-form algorithm file remain
  outside this forms-local pass and continue under the active completeness task.

## Converted Mapping Content

`FormedModules(R)` is the forms-subtree owner for modules equipped with forms.
It is the named spelling of `Modules(R, dispatch=False).WithForms()`.

## Ownership

| Surface | Owner | Notes |
| --- | --- | --- |
| `Modules(R).WithForms()` | `forms.subcategories.with_forms.FormedModulesCategory` | Modules keeps the Sage-compatible route; forms owns the class and method surface. |
| `Modules(R).WithForms().Bilinear()` | `forms.subcategories.bilinear.BilinearModulesCategory` | Owns bilinear evaluation and generic bilinear predicates. |
| `Modules(R).WithForms().Quadratic()` | `forms.subcategories.quadratic.QuadraticModulesCategory` | Owns quadratic evaluation. |
| Symmetric, alternating, nondegenerate, integral, rational bilinear axioms | `forms.subcategories.*` | These are formed-module properties, not lattice-only properties. |
| Definite and indefinite bilinear axioms | finite free symmetric formed modules with selected ordered real realization | Definiteness and signature need a signed scalar context; `[[DECISION-ORDERED-REAL-SIGNATURE-OWNER]]` rejects bare integral-domain ownership and admits the ordered-real-realization refinement. |
| `divisibility(v)` for symmetric bilinear elements | `forms.subcategories.symmetric.SymmetricBilinearModulesCategory.ElementMethods` | The invariant definition is the pairing-image submodule `<b(v, M)>` of the form codomain `S`; for `S = R`, this is an ideal. |
| Form-preserving morphisms between formed modules | `C.HomCategory().Of(M, N)` for `C <= FormedModules(R)` | A candidate map preserves form data exactly when it is contained in the Hom object of the formed-module category. |
| Isometries of formed modules | `C.HomCategory().Of(M, N)` plus generic isomorphism; automorphism case `C.AutCategory().Of(M)` | Form preservation is already Hom containment. The isometry question is invertibility or isomorphism inside that category. |
| Formed-module cokernel of a morphism | `C.HomCategory().ElementMethods.cokernel()` for `C <= FormedModules(R)` | Caller is a formed morphism `f: M -> N`. The returned carrier is `Q = codomain(f) / image(f)` with projection. If the form has codomain map `h: S_M -> S_N`, first form `N_0 = coker(h)`, then quotient `N_0` by the images of cross terms `b_N(image(f), codomain(f))`; the descended form has codomain that quotient. Source basis: `category_specs/forms/subcategories/with_forms.py:100-119`, `mem:projects/github.com__dzackgarza__lattice-research/context/bilinear-forms-duals-morphisms`, and `[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]`. |
| Free bilinear modules | `forms.subcategories.free_bilinear.FreeBilinearModulesCategory` | First tier where Gram matrices, determinant, and discriminant are universally meaningful. |
| Finite-rank free formed-module chain used by `Lattices(R)` | `forms.chain` | Lattices imports this chain and adds only the named `Lattice` endpoint. |
| Finite torsion quadratic modules | `forms.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory` | Modules keeps `TorsionQuadraticModules()` as a compatibility constructor route. |
| `Lattices(R)` | `lattices.LatticesCategory` | Lattice-specific endpoint and lattice construction categories remain in `lattices`. |

## Compatibility Routes

The module and lattice import paths remain valid:

- `category_specs.modules.subcategories.with_forms.FormedModulesCategory`
- `category_specs.modules.subcategories.bilinear.BilinearModulesCategory`
- `category_specs.modules.subcategories.quadratic.QuadraticModulesCategory`
- `category_specs.modules.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory`
- `category_specs.lattices.subcategories.symmetric.SymmetricBilinearModulesCategory`
- analogous lattice paths for alternating, nondegenerate, definite, indefinite,
  integral, rational, and free bilinear categories.

Those files are shims. New specs should import or document formed-module ownership
through `forms`.

## Boundary With Tensor Components

`TensorAlgebraComponents(R)` owns tensor component modules and tensor elements.
A scalar-valued bilinear form may be constructed there as a `(0,2)` tensor. The object
becomes a formed module only when attached as form data to a module category in this
subtree.

## Twisted And Semilinear Form Data

No separate `TwistedForms` category is admitted at this time.

The grounded form-object contract already records the relevant data on the form object:
the tensor-degree source, codomain module, and scalar-action endomorphism `sigma`.
`ModulesWithForms(R)` therefore remains the owner for pairs `(M, f)` with semilinear
form data, while the named forms subcategories own the cases currently admitted by the
mapping:

- bilinear forms use tensor degree `2` and `sigma = id_R`;
- quadratic forms use tensor degree `1` with the current quadratic scalar action;
- alternating, symmetric, integral, rational, finite-torsion, and quotient-valued cases
  refine the existing formed-module chain.

Tensor-component duals remain tensor-component objects until attached as form data to a
module. A future twisted-form subcategory may be admitted only if a concrete public
method or constructor is mathematically wrong without a distinct owner beyond
`FormedModules(R)` plus tensor-component/Hom-category structure.

## Form-Preserving Morphisms And Isometries

For `C <= FormedModules(R)`, the form-preserving maps from `M` to `N` are the elements
of `C.HomCategory().Of(M, N)`. A plain `R`-module morphism belongs to
`Modules(R).HomCategory()` first; it is promoted into the formed-module Hom object only
when it satisfies the defining form-compatibility equation.

Consequences:

- do not introduce a standalone public `is_form_preserving()` predicate as the owner of
  form preservation;
- `is_isometry()` on a formed-module morphism is only a compatibility query for
  isomorphism inside an already form-preserving Hom object;
- `orthogonal_group()` is `C.AutCategory().Of(M)` for the relevant formed-module
  category `C`;
- matrix equations are implementation checks under explicit presentations, not the
  public definition of preservation or isometry.

Metric-space isometries in `TopologicalSpaces().HomCategory()` are a separate surface
and must not be routed through this formed-module owner.

## Symmetric Bilinear Divisibility

For a symmetric bilinear module `(M, b)` with `b: M x M -> S`, the element
divisibility surface is:

`divisibility(v) = < b(v, w) : w in M > <= S`.

This is a submodule of the form codomain `S`. In the scalar-valued case `S = R`, it is
an ideal of `R`. Coordinate gcds, principal generators, or old Sage lattice
presentations are only possible representations after extra hypotheses are recorded;
they are not the mathematical definition and do not create a free-module owner.

## Boundary With Lattices

Lattices are integral, nondegenerate, symmetric, finite-rank free bilinear modules with
the additional named `Lattice` axiom. Formed-module methods such as `b`, `gram_matrix`,
and `orthogonal_group` remain owned by forms. The lattice-specific `dual_lattice()`
surface is the metric-dual construction `L^# = {v in L_K : b(v,L) subset R}` inside
scalar extension, not the category-theoretic Hom dual object `Hom_R(L,R)`. The quotient
class map `L^# -> L^#/L` belongs to elements of the metric-dual lattice returned by
`L.dual_lattice()`; ordinary elements of `L` map to zero after inclusion `L -> L^#`.
Lattice-specific specializations such as `OverIntegers`, `Even`, `Unimodular`, and
lattice construction categories remain owned by `lattices`.

## 6-Gate Protocol Review Log

Review date: 2026-05-07.  Reviewer: automated 6-gate audit pass.  Result: PASS
with two advisory findings (see G2 Finding 1, G2 Finding 2 below).  No gate failures.

### G1 — Source Grounding

Every referenced file, card, and Sage source path was verified on-disk.

| Reference | Path | Exists |
| --- | --- | --- |
| Forms MAPPING (now redirect) | `/home/dzack/research/category_specs/forms/docs/MAPPING.md` | YES |
| Forms SAGE_INVENTORY | `/home/dzack/research/category_specs/forms/docs/SAGE_INVENTORY.md` | YES |
| Modules SAGE_INVENTORY | `/home/dzack/research/category_specs/modules/docs/SAGE_INVENTORY.md` | YES |
| Lattices SAGE_INVENTORY | `/home/dzack/research/category_specs/lattices/docs/SAGE_INVENTORY.md` | YES |
| Tensor-components SAGE_INVENTORY | `/home/dzack/research/category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` | YES |
| `FreeQuadraticModule_generic` source | `.../sage/modules/free_quadratic_module.py` (line 258) | YES |
| `FreeQuadraticModule_integer_symmetric` source | `.../sage/modules/free_quadratic_module_integer_symmetric.py` (line 625) | YES |
| `TorsionQuadraticModule` source | `.../sage/modules/torsion_quadratic_module.py` (line 188) | YES |
| `TorsionQuadraticForm(q)` constructor | `.../sage/modules/torsion_quadratic_module.py` (line 35) | YES |
| `TensorFreeModule` source | `.../sage/tensor/modules/tensor_free_module.py` (line 74) | YES |
| `free_module_tensor.py` | `.../sage/tensor/modules/free_module_tensor.py` | YES |
| `quadratic_form.py` | `.../sage/quadratic_forms/quadratic_form.py` | YES |
| `quadratic_form__automorphisms.py` (`automorphisms()` at line 335) | `.../sage/quadratic_forms/quadratic_form__automorphisms.py` | YES |
| `quadratic_form__genus.py` | `.../sage/quadratic_forms/quadratic_form__genus.py` | YES |
| Parent feature card | `.../FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md` | YES |
| Depends-on phase card | `.../PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT/PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT.md` | YES |
| Completeness task card | `.../TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.md` | YES |
| Signature decision card | `.../DECISION-ORDERED-REAL-SIGNATURE-OWNER.md` | YES |
| Compatibility shim: `modules/subcategories/with_forms.py` | Imports from `forms.subcategories.with_forms` | YES |
| Compatibility shim: `modules/subcategories/bilinear.py` | Imports from `forms.subcategories.bilinear` | YES |
| Compatibility shim: `modules/subcategories/quadratic.py` | Exists | YES |
| Compatibility shim: `modules/subcategories/torsion_quadratic_modules.py` | Exists | YES |
| Compatibility shim: `lattices/subcategories/symmetric.py` | Imports from `forms.subcategories.symmetric` | YES |

Source-grounding verdict: PASS.  Every named file and card resolves to an existing
on-disk artifact.

### G2 — Sage Surface Completeness

The forms inventory (SAGE_INVENTORY.md) names five Sage evidence families.  The spec
accounts for all five:

1. **FreeQuadraticModule_generic** — mapped to free bilinear/quadratic formed-module
   structure in `FreeBilinearModulesCategory` (confirmed: class at
   `free_quadratic_module.py:258`, Gram/determinant/discriminant/inner_product_matrix
   methods at lines 389-473).  CORRECT.

2. **FreeQuadraticModule_integer_symmetric** — mapped through
   `IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory` chain
   (confirmed: class at `free_quadratic_module_integer_symmetric.py:625`, category
   chain at `forms/chain.py:189-250`).  The lattice `LatticesCategory` extends this
   class with the `Lattice` axiom only (confirmed: `lattices/__init__.py:62-71`,
   `_base_category_class_and_axiom` references the forms chain class).  CORRECT.

3. **TorsionQuadraticModule** — mapped to `TorsionQuadraticModulesCategory`
   (confirmed: class at `torsion_quadratic_modules.py:17-61`).  CORRECT.

4. **TorsionQuadraticForm(q)** — Sage constructor at
   `torsion_quadratic_module.py:35`, noted as remaining under modules constructor
   compatibility routing.  CORRECT.

5. **TensorFreeModule dual components** — mapped to tensor-component boundary
   (confirmed: `TensorFreeModule` at `tensor_free_module.py:74`).  Boundary
   statement is correct: tensor duals remain tensor-component objects until
   attached as form data.  CORRECT.

**G2 Finding 1 (advisory):** The spec's Source Coverage Ledger lists
`quadratic_form.py` and `quadratic_form__automorphisms.py` but does not list
`quadratic_form__local_field_invariants.py`, which contains the
`signature_vector()` method (line 298) that is the actual Sage evidence cited by
DECISION-ORDERED-REAL-SIGNATURE-OWNER.md for the `signature_pair() -> signature_vector()`
call chain.  The decision card cites the correct Sage path; the spec ledger should
include it for completeness.

**G2 Finding 2 (advisory):** The Sage `QuadraticForm` class (in `quadratic_form.py`)
and its method files (`__automorphisms`, `__genus`, `__local_field_invariants`) are
in the source ledger but not explicitly mapped to formed-module surfaces.  The spec
correctly treats them as Sage implementation evidence rather than spec owners, but
a row stating that `QuadraticForm` methods are implementation-check surfaces under
formed-module categories (not spec owners themselves) would improve audit
traceability.

Sage-surface verdict: PASS with two advisory findings.  All five inventoried families
are accounted; the advisories concern ledger completeness, not spec correctness.

### G3 — Constructor Route Justification

Every mathematical route in the ownership table was verified against actual category
source:

- `FormedModulesCategory._base_category_class_and_axiom = (Modules, "WithForms")`
  (confirmed: `forms/subcategories/with_forms.py:25`).  The spec's
  `Modules(R, dispatch=False).WithForms()` spelling is correct.

- `BilinearModulesCategory._base_category_class_and_axiom = (FormedModulesCategory, "Bilinear")`
  (confirmed: `forms/subcategories/bilinear.py:24`).

- `FreeBilinearModulesCategory._base_category_class_and_axiom = (BilinearModulesCategory, "Free")`
  (confirmed: `forms/subcategories/free_bilinear.py:70`).  This is the first tier
  where Gram matrices, determinant, and discriminant are universally meaningful
  because a basis exists.  Mathematically valid.

- `SymmetricBilinearModulesCategory._base_category_class_and_axiom = (BilinearModulesCategory, "Symmetric")`
  (confirmed: `forms/subcategories/symmetric.py:35`).  The divisibility surface
  (`ElementMethods.divisibility()` at line 81) is correctly placed here — it
  requires symmetry (`b(v,w)` and `b(w,v)` generate the same submodule).

- `LatticesCategory._base_category_class_and_axiom = (IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory, "Lattice")`
  (confirmed: `lattices/__init__.py:68-71`).  This is the named endpoint; all
  preceding chain links are forms-owned.  Mathematically valid.

- `TorsionQuadraticModulesCategory.super_categories()` returns the single chain
  `FinitelyPresented().OverPID().Torsion().WithForms().Quadratic()` (confirmed:
  `forms/subcategories/torsion_quadratic_modules.py:24-35`).  The old module
  `TorsionQuadraticModules()` route remains as constructor compatibility.  Valid.

- Definite/indefinite ownership through ordered-real-realization: the spec correctly
  delegates to DECISION-ORDERED-REAL-SIGNATURE-OWNER, which rejects bare
  integral-domain ownership and admits only finite free symmetric formed modules
  with a selected ordered real realization.  The Sage evidence
  (`free_quadratic_module_integer_symmetric.py:868-869`:
  `QuadraticForm(QQ, self.gram_matrix()).signature_vector()[:2]`) confirms the
  `ZZ -> QQ -> RR` path used by integral lattices.  Mathematically valid.

Constructor-route verdict: PASS.  All routes are justified by category source;
no mathematically invalid placements found.

### G4 — Nonmathematical Rejection

The spec explicitly rejects several nonmathematical targets:

1. **Coordinate-gcd as free-module owner for bilinear divisibility** (lines 84-85,
   193-202): REJECTED.  The mathematical definition is the pairing-image submodule
   `<b(v, M)> <= S`.  Confirmed in source at
   `forms/subcategories/symmetric.py:81-93` (`ElementMethods.divisibility()`).
   Coordinate gcds are noted as representation-level computations, not the definition.
   Rejection is mathematically sound.

2. **Standalone `is_form_preserving()` predicate** (lines 173-176, 180-181):
   REJECTED.  Form preservation is owned by containment in the formed-module
   Hom object.  Confirmed in `forms/subcategories/free_bilinear.py:32-41`:
   "Morphisms in this formed-module category are already the R-module maps
   contained in the formed Hom object, hence already preserve b."
   Rejection is mathematically sound.

3. **`TwistedForms` category** (lines 152-169): REJECTED until a concrete public
   method or constructor is mathematically wrong without a distinct owner.
   Semilinear form data is carried on the form object; the current formed-module
   chain handles bilinear, quadratic, alternating, symmetric, integral, rational,
   finite-torsion, and quotient-valued cases.  Rejection with stated admission
   criteria is sound.

4. **Raw Sage implementation containers** (acceptance criteria and review gates):
   REJECTED as spec surfaces.  The spec treats Sage source as evidence, not as
   owners.  Sound.

5. **Metric-space isometries through formed-module owner** (line 189-190):
   REJECTED.  `TopologicalSpaces().HomCategory()` is the separate owner.
   Sound separation.

Nonmathematical-rejection verdict: PASS.  All rejections have explicit rationale,
most have replacement owners, and none weaken mathematical obligations.

### G5 — Ambiguity Routing

Identified ambiguities are routed to tracked decision/task cards:

1. **Definite/indefinite and signature ownership** (lines 120, plus spec update
   note at DECISION-ORDERED-REAL-SIGNATURE-OWNER.md:113): routed to
   DECISION-ORDERED-REAL-SIGNATURE-OWNER, status `decided`.  The spec row
   (line 120) correctly reflects the decided owner.  RESOLVED.

2. **Sage import probe caveat** (lines 60-62): documented with explicit environment
   description.  The spec correctly notes that `sage -python` imports of
   `sage.categories.*` raise `ImportError` and that installed source files plus
   inventories are the durable evidence surface.  Documented, not blocking.

3. **Remaining completeness gaps** (lines 103-105): routed to
   TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.  Active tracking, not orphaned.

4. **Negative source finding for separate Sage forms category** (lines 87-105):
   explicitly documented with confidence level (Medium) and enumerated gaps.
   Appropriate for a spec-level negative finding.

Ambiguity-routing verdict: PASS.  All identified gaps have resolution paths;
no orphaned ambiguities.

### G6 — Obligation Preservation

The spec does not weaken any mathematical obligation without a replacement owner:

1. **`dual_lattice()`** (lines 206-212): The spec clarifies it is the metric-dual
   construction `L^# = {v in L_K : b(v,L) subset R}`, not the Hom-dual object
   `Hom_R(L,R)`.  Confirmed in source at
   `forms/chain.py:215-224` (`IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.dual_lattice()`)
   which includes a diagnostic distinguishing metric-dual from Hom-dual.  No
   weakening — this is a precision improvement.

2. **`orthogonal_group()`** (lines 123, 183-186): Defined as
   `C.AutCategory().Of(M)` for the formed-module category `C`.  Confirmed in
   `forms/subcategories/with_forms.py:44-46` and `forms/chain.py:54-60`.
   The definition is category-theoretic; no weakening.

3. **`is_isometry()`** (line 182, `free_bilinear.py:218-225`): Defined as
   `is_isomorphism()` on an already form-preserving morphism.  Form preservation is
   Hom-containment, not a separate predicate.  This is a precision improvement,
   not weakening.

4. **Bilinear divisibility** (lines 84-85, 193-202): The invariant definition
   (`<b(v, M)> <= S`) is stronger and more general than coordinate-gcd approaches.
   No weakening.

5. **Compatibility routes** (lines 131-142): All module and lattice shims exist as
   import redirects pointing to `forms`.  Old paths remain valid; new specs use
   `forms`.  This preserves backward compatibility while establishing canonical
   ownership.  No weakening — old paths are not removed.

Obligation-preservation verdict: PASS.  No mathematical obligations are weakened,
deleted without replacement, or narrowed to Sage-implementation-only surfaces.

### Summary

| Gate | Verdict | Evidence |
| --- | --- | --- |
| G1 Source grounding | PASS | 23/23 referenced artifacts verified on disk |
| G2 Sage surface completeness | PASS | 5/5 inventoried families accounted; 2 advisory findings |
| G3 Constructor route justification | PASS | All 7 category routes verified against source `_base_category_class_and_axiom` |
| G4 Nonmathematical rejection | PASS | 5 explicit rejections, all with rationale and replacement owners |
| G5 Ambiguity routing | PASS | 4 identified gaps, all routed to tracked cards or documented |
| G6 Obligation preservation | PASS | 5 surface audits; no weakening without replacement |

Overall: SPEC-MAPPING-FORMS.md is mathematically sound, source-grounded, and
category-hierarchy consistent.  The two G2 advisory findings (missing
`quadratic_form__local_field_invariants.py` in ledger; no explicit mapping row for
`QuadraticForm` methods) are ledger-completeness items, not correctness defects.
Recommend adding those two items to TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.
