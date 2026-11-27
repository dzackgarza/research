---
id: SPEC-MAPPING-HOMSETS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track homsets mapping spec
status: complete
priority: critical
requirement: Convert category_specs/homsets/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  Hom, End, Aut, image, kernel, and morphism signatures.
acceptanceCriteria:
- Source paths category_specs/homsets/docs/MAPPING.md and category_specs/homsets/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Hom Category Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/homsets/docs/MAPPING.md`.

Source inventory: `category_specs/homsets/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/homsets/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/homsets.py`
  - `sage/categories/homset.py`
  - `sage/categories/objects.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the generic
  homset reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Generic Homset Surface

This pass checked the Sage generic homset construction and parent-method surface:

- `sage.categories.objects.Objects.SubcategoryMethods.Homsets()` calls
  `HomsetsCategory.category_of(self)`, and `Endsets()` is implemented as the
  `Endset` axiom on that homset category;
- `sage.categories.homsets.HomsetsCategory`, `HomsetsOf`, `Homsets`, and
  `Homsets.Endset` are represented by `C.HomCategory()`, `C.EndCategory()`, and the
  project extension of `C.AutCategory()` as the invertible part of `End_C(A)`;
- `sage.categories.homset.Homset` supplies parent-level `domain()`, `codomain()`,
  `identity()`, call/coercion behavior, reverse homsets, and
  `is_endomorphism_set()`;
- `identity()` is mathematically an endomorphism identity and is admitted on generic
  hom objects only under the endomorphism hypothesis; non-end homsets keep the Sage
  error behavior as interop evidence, not as a separate project method;
- the deprecated Sage helper `is_Endset(x)` remains compatibility evidence only; the
  project surface is categorical containment in the end-category owner.

Negative missing-surface finding for the generic homset pass:

- Searched: `category_specs/homsets/docs/SAGE_INVENTORY.md`, installed Sage
  `sage/categories/homsets.py`, `sage/categories/homset.py`,
  `sage/categories/objects.py`, and the converted generic homset mapping rows above.
- Found: the checked Sage generic surface consists of Homsets category construction,
  the Endset axiom, concrete Homset parent accessors and identity/coercion behavior,
  and a deprecated `is_Endset` compatibility helper. The converted spec represents
  these as generic Hom/End/Aut category surfaces, Hom-object methods, end-category
  identity behavior, or interop-only evidence.
- Conclusion: inference -- this pass found no additional generic Sage homset surface
  requiring a new public project owner outside the existing generic Hom/End/Aut
  mapping.
- Confidence: Medium.
- Gaps: subtree-specific homsets for sets, rings, modules, algebras, posets, and
  topological spaces remain owned by their corresponding mapping specs and are not
  closed by this generic homsets reconciliation.

## Converted Mapping Content

This file records the forward mapping from Sage's generic homset construction to the
project hom/end/aut category hierarchy.

## Sage To Project Mapping

| Sage surface | Project surface | Consequence |
| --- | --- | --- |
| `HomsetsCategory` | `HomCategoryConstruction` | Sage identifies the homsets construction, but project `HomCategoryConstruction` owns the mathematical method surface; Sage `HomsetsCategory` is inventory/interop, not a semantic superclass. |
| `Homsets()` | `HomCategory()` | The project root hom category supplies generic parent and element method surfaces. |
| `HomsetsCategory.category_of(C)` | `C.HomCategory()` | The project makes the base category explicit, so `C.HomCategory()`, `C.EndCategory()`, and `C.AutCategory()` share one generic hierarchy before subtree-specific structure is added. |
| `Homsets().Endset()` | `HomCategory().EndCategory()` | Sage's root endset category remains an interop supercategory for generic ends. |
| Sage has no independent `EndsetsCategory` functorial construction | `EndCategoryConstruction` and `C.EndCategory()` | The project adds this construction layer so `C.EndCategory()` has the same uniform shape as `C.HomCategory()`. |
| Sage has no generic `Autset` axiom in the audited file | `AutCategoryConstruction` and `C.AutCategory()` | The project adds the missing automorphism construction once, as the invertible part of an end category. |

## Project Extension Surface

| Project surface | Mathematical meaning | Method surface to represent |
| --- | --- | --- |
| `C.HomCategory().Of(A, B)` | `Hom_C(A, B)` for objects `A, B in C`. | Parent: `domain`, `codomain`, `__call__`; element: morphism predicates and composition. The identity method is not owned here unless `A = B`. |
| `C.EndCategory().Of(A)` | `End_C(A) = Hom_C(A, A)`. | Parent: endomorphism identity; element: endomorphism predicates. |
| `C.AutCategory().Of(A)` | `Aut_C(A)`, the invertible part of `End_C(A)`. | Parent: `end_category`, `domain`, `codomain`, `identity`; element: `is_invertible`, `is_isomorphism`, `inverse`, `order`. |
| private aut-from-end bridge | Implementation construction of `Aut_C(A)` from `End_C(A)`. | The public mathematical surface is `Aut_C(A)`, the invertible elements of `End_C(A)`. A helper such as `AutCategory.from_end_category` is constructor glue, not a public method obligation. |

Because `End_C(A)` is `Hom_C(A, A)`, the object `A` is already represented by the
generic hom-object methods `domain()` and `codomain()`. Subtree aliases such as
`base_set()` or `base_space()` are redundant and map to `domain()` for migration.

The raw Sage `ConditionSet` is an implementation detail of the generic aut
construction. Public aut objects expose `end_category()`, `domain()`,
`codomain()`, and `identity()`; they do not expose a `condition_set()` method.

## Subtree Contract

Subtree hom-category files use `HomCategoryOf(C)`, `GenericEndCategory`, and
`GenericAutCategory` for generic supercategories instead of constructing their own
`ConditionSet` over an end object. The allowed split is:

| Responsibility | Owner |
| --- | --- |
| Generic `Aut_C(A)` construction from `End_C(A)` | `homsets/autsets.py` |
| Generic hom object and morphism specs | `homsets/homsets.py` |
| Generic end specs | `homsets/endsets.py` |
| Generic aut specs | `homsets/autsets.py` |
| Public re-export surface | `homsets/__init__.py` |
| Set-specific function laws | `sets/homsets.py` |
| Ring-homomorphism laws | `rings/homsets.py` |
| Module-homomorphism laws and the extra `R`-module / `R`-algebra structure on `Hom_R(M, N)` and `End_R(M)` | `modules/homsets.py` |
| Algebra-homomorphism laws | `algebras/homsets.py` |
| Order-preserving-map laws | `posets/homsets.py` |
| Continuous-map and homeomorphism laws | `topological_spaces/homsets.py` |

Subtrees may refine `extra_super_categories()` and add category-specific methods, but
they must not duplicate the generic aut construction or generic aut element predicates.
Construction categories do not define method surfaces; root categories and subtree
categories do. Concrete hom categories attach an `Endset` axiom hook; concrete end
categories attach an `Autset` axiom hook. Those hook names exist for Sage interop only.

Selector ownership:

| Old local surface | Project surface | Rationale |
| --- | --- | --- |
| `HomCategory.SubcategoryMethods.EndCategory()` | inherited `Cat` universal `EndCategory()` selector | The universal selector already detects hom-category objects and applies the `Endset` axiom hook. The local method duplicated that selector. |
| `HomCategory.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | Automorphism selection factors through the universal end selector and the `Autset` axiom hook. |
| `HomCategoryConstruction.SubcategoryMethods.EndCategory()` | inherited `Cat` universal `EndCategory()` selector | Construction categories are still category objects; the universal selector produces the same `Endset` refinement. |
| `HomCategoryConstruction.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The construction-level aut selector is inherited, not locally owned. |
| `EndCategory.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The universal selector already detects end-category objects and applies `Autset`. |
| `EndCategoryOf.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The generic end-category construction has no separate aut-navigation law beyond the universal selector. |

## Extra Structure Pattern

`modules/homsets.py` is the model for this pattern. `Modules(R).HomCategory()`
declares both the generic `HomCategoryOf(Modules(R))` supercategory and the additional
module structure on `Hom_R(M, N)`. Its end subcategory declares the additional
`Algebras(R)` structure on `End_R(M)`, while also retaining Sage's
`MagmaticAlgebras(R)` surface. Its aut subcategory is based on the end subcategory, so
it inherits endomorphism methods instead of re-declaring them.

Other subtrees follow the same rule. A subtree homset file must always declare its hom,
end, and aut categories, even when they currently add only mathematical names and
future method locations. It adds a supercategory only when the hom/end/aut object
genuinely carries that structure.

## Source Note: Generic Sage Autsets

- Searched: Sage develop `src/sage/categories/homsets.py`, installed local
  `sage/categories/homsets.py`, and local subtree hom-category files.
- Found: Sage exposes `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the audited
  Sage file does not define a generic `Autset` category.
- Conclusion: inference -- the project `AutCategory` layer is a deliberate extension of
  Sage's generic homset construction, not a remapping of an existing Sage class.
- Confidence: High.
- Gaps: Sage git history and third-party Sage extensions were not searched.

## 6-Gate Protocol Review Log

### G1: Source Grounding

- **Sage source files verified exist:**
  - `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homsets.py` — 364 lines, SageMath 10.7, exists on disk
  - `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homset.py` — 1337 lines, exists on disk
  - `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/objects.py` — 167 lines, exists on disk
- **Local inventory files verified exist:**
  - `category_specs/homsets/docs/MAPPING.md` — redirect stub pointing to this canonical spec, confirmed exists
  - `category_specs/homsets/docs/SAGE_INVENTORY.md` — 12 lines, 4 Sage surfaces inventoried, confirmed exists
- **Project subtree homset files verified exist (9 total across subtrees):**
  - `category_specs/homsets/__init__.py`, `homsets.py`, `endsets.py`, `autsets.py` — all present
  - `category_specs/sets/homsets.py`, `modules/homsets.py`, `rings/homsets.py`, `algebras/homsets.py`, `posets/homsets.py`, `lattices/homsets.py`, `topological_spaces/homsets.py`, `cat/homsets.py` — all present
- **Referenced task card exists:** `TASK-MAPPING-DOC-COMPLETENESS-RESEARCH` at the expected path
- **Referenced sibling mapping specs exist:** SPEC-MAPPING-SETS.md and 10 other `SPEC-MAPPING-*` cards

**G1 VERDICT: PASS.** All source paths cited in the spec are grounded to real, verifiable files on disk.

### G2: Sage Surface Completeness

- **SAGE_INVENTORY.md (4 surfaces) completeness check:**
  - `sage.categories.homsets.HomsetsCategory` → inventoried with method surface description: "Functorial construction for C.Homsets(), default supercategory computation, _test_homsets_category, base, and named-class key routing" — mapped to HomCategoryConstruction in spec table row 9-10 of inventory
  - `sage.categories.homsets.HomsetsOf` → "Stub homset category for categories that have structure but no specialized homset category" — inventoried
  - `sage.categories.homsets.Homsets` → "Category of all homsets, supercategory Sets(), and generic homset parent method is_endomorphism_set" — mapped to project HomCategory()
  - `Homsets().Endset()` → "Endomorphism-set axiom; Sage adds Monoids() as an extra supercategory" — mapped to HomCategory().EndCategory() and EndCategory layer

- **Deep Sage source verification against installed homsets.py:**
  - `HomsetsCategory` (line 19): confirmed as `FunctorialConstructionCategory, CategoryWithParameters` subclass with `_functor_category = "Homsets"`, methods: `default_super_categories`, `_test_homsets_category`, `base`, `_make_named_class_key`
  - `HomsetsOf` (line 175): confirmed stub with `super_categories()` returning `[Homsets()]`
  - `Homsets` (line 239): confirmed `Category_singleton`, `super_categories()` returns `[Sets()]`, `SubcategoryMethods` has `Endset()` (line 285), nested `Endset` class (line 299) with `extra_super_categories` returning `[Monoids()]` and `ParentMethods.is_endomorphism_set` → `True`
  - No `Autset` class defined in the Sage file — confirmed by reading entire 364-line file

- **Installed homset.py verification:**
  - `Homset.identity()` (line 1161): confirmed — raises TypeError for non-endomorphisms, returns `IdentityMorphism` for endomorphisms
  - `Homset.domain()` (line 1205): confirmed — returns `self._domain`
  - `Homset.codomain()` (line 1220): confirmed — returns `self._codomain`

- **Installed objects.py verification:**
  - `Objects.SubcategoryMethods.Homsets()` (line 83): confirmed — calls `HomsetsCategory.category_of(self)`
  - `Objects.SubcategoryMethods.Endsets()` (line 146): confirmed — calls `self.Homsets()._with_axiom("Endset")`

- **Negative finding (explicitly documented in spec):** The spec's "Negative missing-surface finding" section confirms that no additional generic Sage homset surface exists beyond what's mapped. Confidence: Medium. This is properly qualified.

- **Gap routing:** Subtree-specific homsets (sets, rings, modules, algebras, posets, topological spaces) are explicitly deferred to their own mapping specs — not closed by the generic reconciliation.

**G2 VERDICT: PASS.** Every Sage surface from the inventory is mapped. Deep source verification against installed Sage files confirms the spec's description of `HomsetsCategory`, `Homsets`, `Homsets.Endset`, and the absence of a generic `Autset` in Sage. Homset parent methods (domain, codomain, identity) are verified present with correct semantics.

### G3: Mathematical Correctness of Constructor Routes

- **Hom/End/Aut hierarchy correctness:**
  - `Hom_C(A, B)` is the set of morphisms from A to B in category C — mathematically correct. The spec maps this to `C.HomCategory().Of(A, B)`.
  - `End_C(A) = Hom_C(A, A)` — mathematically this is the specialization of Hom to equal domain/codomain. The spec correctly represents this as `C.EndCategory().Of(A)` building on the Hom construction.
  - `Aut_C(A)` is the invertible part of `End_C(A)` — mathematically correct as the group of units in the endomorphism monoid. The spec's `AutCategoryConstruction` builds from `EndCategoryConstruction`, which is mathematically precise.

- **Project code verification of the hierarchy (from `category_specs/homsets/`):**
  - `HomCategory` (singleton root) inherits from Sage's `Homsets` base and attaches `Endset` axiom hook pointing to `EndCategory`
  - `HomCategoryConstruction` has `Of(A, B)` calling `Parent.Hom(domain, codomain, category=...)` — standard Sage construction
  - `HomCategoryOf` (generic category-level construction) has `Endset` axiom hook pointing to `EndCategoryOf`
  - `EndCategory` (singleton root) has `_base_category_class_and_axiom = (HomCategory, "Endset")` — correct: endsets are a specialization of homsets
  - `EndCategoryConstruction` extends `HomCategoryConstruction`, `Of(domain)` returns `HomCategory().Of(domain, domain)` — mathematically correct as `End_C(A) = Hom_C(A, A)`
  - `EndCategoryOf` has `_base_category_class_and_axiom = (HomCategoryOf, "Endset")`, `Of(domain)` returns `self.base_category().Of(domain, domain)` — correct
  - `AutCategory` (singleton root) has `_base_category_class_and_axiom = (EndCategory, "Autset")` — correct: automorphisms are special endomorphisms
  - `AutCategoryConstruction` extends `EndCategoryConstruction`, `Of(domain)` constructs via `EndCategory().Of(domain)` then applies `from_end_category()` — mathematically correct reuse of the `End_C(A) → Aut_C(A)` refinement
  - `AutCategoryOf` has `_base_category_class_and_axiom = (EndCategoryOf, "Autset")` — correct

- **Higher-category placement verification:**
  - `domain()`, `codomain()`, `__call__` declared on `UniversalHomObjectMethods` — placed at HomCategory, the highest category where they make sense for all hom-objects. Correct.
  - `identity()` declared on `UniversalEndObjectMethods` — placed at EndCategory, the highest category where identity is guaranteed (non-end homsets raise TypeError). Correct.
  - `is_invertible()`, `is_isomorphism()`, `inverse()` declared on `UniversalAutElementMethods` — placed at AutCategory, where invertibility is guaranteed. Correct.
  - `is_endomorphism_set()` declared on both Hom (delegates to `domain() == codomain()`) and End (always returns True) — correctly resolves the two-level semantics.

- **Subtree contract correctness:**
  - The spec's "Subtree Contract" table properly allocates generic aut construction to `homsets/autsets.py` and subtree-specific methods to per-category files. The "Extra Structure Pattern" section uses `modules/homsets.py` as the model. Verification of `sets/homsets.py` (129 lines) confirms it imports `GenericAutCategory, GenericEndCategory, HomCategoryOf` from `..homsets` and does not duplicate the generic aut construction — it only declares set-specific methods (morphism predicates, pre_image, etc.).

- **Selector ownership correctness:**
  - The spec correctly identifies that `EndCategory()` and `AutCategory()` selectors are inherited from the Cat universal selector and should not be locally duplicated. The Sage axiom hooks (`Endset`, `Autset`) exist only for interop compatibility.

**G3 VERDICT: PASS.** The Hom → End → Aut hierarchy is mathematically sound. End_C(A) = Hom_C(A, A) is correctly encoded. Aut_C(A) as the invertible part of End_C(A) is correctly layered. Methods are placed at the mathematically highest appropriate category. The project code confirms the hierarchy.

### G4: Nonmathematical Targets Rejected

- **Explicit rejections found:**
  - "Nonmathematical targets and raw Sage implementation containers are rejected or marked interop-only" (acceptance criteria line 21-22)
  - "Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening" (Review Gates line 39)
  - Raw Sage `ConditionSet` is explicitly documented as "an implementation detail of the generic aut construction" (line 121-123). Public aut objects expose `end_category()`, `domain()`, `codomain()`, `identity()` — they do NOT expose a `condition_set()` method. Confirmed in `autsets.py`: `_condition_aut_object_from_end_category` is a private helper, and `UniversalAutObjectMethods` exposes only mathematical methods.
  - Deprecated Sage helper `is_Endset(x)` is kept as "compatibility evidence only" and "the project surface is categorical containment in the end-category owner" (line 71-72) — not admitted as a public method
  - `HomsetsCategory` is classified as "inventory/interop, not a semantic superclass" in the mapping table (line 101)
  - Selector ownership table rejects local-duplicated `EndCategory()`/`AutCategory()` SubcategoryMethods on HomCategory, HomCategoryConstruction, EndCategory, and EndCategoryOf — all inherited from the Cat universal selector

- **Nonmathematical targets NOT found admitted:**
  - No Sage `__dict__` inspection, no `option` keyword arguments on public surfaces, no variadic `**kwds` pass-through, no `_test_*` methods admitted as mathematical obligations
  - The Sage `_test_homsets_category` is inventoried but not mapped as a mathematical method — it's correctly inventoried as Sage surface without being admitted to the project surface

**G4 VERDICT: PASS.** The spec explicitly rejects Sage implementation containers (ConditionSet), deprecated helpers (is_Endset), and nonmathematical targets. No variadic option bags or smoke-driven interface weakening found. The mapping table clearly distinguishes Sage inventory/interop from project mathematical surfaces.

### G5: Ambiguities Routed to Decision Cards

- **Documented routing of gaps:**
  - Subtree-specific homsets (sets, rings, modules, algebras, posets, topological spaces) are routed to "their corresponding mapping specs" (line 89-90)
  - Missing Sage surfaces/gaps are routed to `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` (line 51) — that task has status `complete`
  - The import probe caveat (line 50) is documented as an environment issue with a clear note: "completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved"

- **Decision card search:** No dedicated `DECISION-*homsets*` card found. This is acceptable because:
  - The generic homset mapping has no unresolved mathematical ownership ambiguities — the hierarchy is clean
  - Subtree gaps are delegated to subtree specs
  - The Sage import environment issue is acknowledged in the source coverage ledger

- **Potential un-routed items checked:**
  - The Sage `Homsets.Endset` adds `Monoids()` as an extra supercategory — the project `EndCategory` returns `[SageHomsets().Endset()]` in `extra_super_categories`, preserving this through interop. This is correct routing.
  - The absence of a Sage generic `Autset` is addressed by the project adding it as a deliberate extension, with the construction documented in `autsets.py`. This is a design decision, not an ambiguity.

**G5 VERDICT: PASS.** Ambiguities are properly routed: subtree gaps to subtree specs, completeness gaps to TASK-MAPPING-DOC-COMPLETENESS-RESEARCH (complete), and environment caveats are documented. No unresolved mathematical ownership or typing ambiguities remain un-routed.

### G6: No Obligation Weakening

- **Obligation integrity check:**
  - The spec does NOT delete or skip Hom, End, or Aut surfaces that exist in Sage — all 4 inventoried surfaces are mapped
  - The spec does NOT narrow the mathematical scope of `identity()` — it's correctly restricted to end objects with non-end homset error behavior preserved as interop evidence
  - The spec does NOT remove the `domain()`/`codomain()` obligations from hom objects
  - The spec does NOT weaken the aut construction obligation — it explicitly documents that the project adds `AutCategory` where Sage has none, and provides the construction in `autsets.py`
  - The spec does NOT replace mathematical methods with Sage wrapper classes — `HomsetsCategory` is inventory/interop, not a semantic superclass; methods are declared on project categories (`HomCategory`, `EndCategory`, `AutCategory`)
  - The spec does NOT remove the module end-structure obligation described in "Extra Structure Pattern" — it correctly documents that `Modules(R).HomCategory()` declares additional module and algebra structure
  - No abstract methods removed, no constructor obligations deleted, no smoke assertions narrowed

- **Weakening signals checked (all negative = good):**
  - No method moved from a higher category to a lower one without justification
  - No mathematical predicate silently dropped
  - No "Sage doesn't have this so we skip it" without a compensating project addition (the AutCategory case is the opposite — Sage doesn't have it, so the project adds it)
  - No Sage-gap-driven interface shrinkage

**G6 VERDICT: PASS.** The spec maintains full mathematical obligation integrity. The Sage→project mapping preserves all mathematical surfaces with correct placement. Where Sage is missing a surface (generic Autset), the project adds it rather than weakening the spec.

### Overall Assessment

All six gates pass with no failures or conditional passes. The spec:

1. Sources are fully grounded to verifiable Sage installation files and local inventory documents
2. All 4 Sage surfaces from SAGE_INVENTORY.md are mapped with deep source verification confirming method signatures
3. The Hom → End → Aut hierarchy is mathematically correct: End_C(A) = Hom_C(A, A), Aut_C(A) = invertible part of End_C(A), with proper category-level layering in the project code
4. Nonmathematical targets (ConditionSet implementation, deprecated is_Endset, Sage HomsetsCategory as interop) are explicitly rejected from the mathematical surface
5. Subtree gaps and completeness research are properly routed to existing cards with known status
6. No mathematical obligations are weakened — the spec adds AutCategory where Sage lacks it and preserves all method surfaces at correct category levels

**Confidence:** High for gates G1-G4 and G6 (source, completeness, correctness, nonmathematical rejection, obligation integrity). Medium for G5 (ambiguity routing) due to the possibility of undiscovered Sage methods in subpackages not inventoried — though the completeness research task is complete and subtree routing is explicit.
