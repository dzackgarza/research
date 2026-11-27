# Hom Category Mapping

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
| `C.HomCategory().Of(A, B)` | `Hom_C(A, B)` for objects `A, B in C`. | Parent: `domain`, `codomain`, `identity`, `__call__`; element: morphism predicates and composition. |
| `C.EndCategory().Of(A)` | `End_C(A) = Hom_C(A, A)`. | Parent: endomorphism identity; element: endomorphism predicates. |
| `C.AutCategory().Of(A)` | `Aut_C(A)`, the invertible part of `End_C(A)`. | Parent: `end_category`, `domain`, `codomain`, `identity`; element: `is_invertible`, `is_isomorphism`, `inverse`, `order`. |
| `AutCategory.from_end_category` | Generic construction of `Aut_C(A)` from `End_C(A)`. | Builds a Sage `ConditionSet` over the end object using the aut predicate, then refines through the requested aut category. |

Because `End_C(A)` is `Hom_C(A, A)`, the object `A` is already represented by the
generic hom-object methods `domain()` and `codomain()`. Subtree aliases such as
`base_set()` or `base_space()` are redundant and map to `domain()` for migration.

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
