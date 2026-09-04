# Preamble Mathematical Constructions Megadoc

Programmatic catalogue of all reusable mathematical categories, subcategories, functors, adjunctions, universal constructions, morphisms, objects, and classification tables owned by `dzack_research.preamble`.

## Executive Summary

- **Total Constructions**: 1091
- **Categories & Subcategories**: 271
- **Functors & Adjunctions**: 163
- **Universal Categorical Constructions**: 15
- **Morphisms & Hom-Sets**: 125
- **Mathematical Objects & Elements**: 130
- **Named Catalogues & Registries**: 7
- **Factory Functions & Constructors**: 380

## Table of Subsystems

| Subsystem | Key Domains | Items |
| :--- | :--- | :--- |
| [Abstract Category Theory & Universal Constructions](#subsystem-abstract-categories) | Category of categories (Cat), Arrow and Slice categories, Limits, Colimits, Biproducts, Subobjects, and Diagram categories. | **135** |
| [Functors & Adjunctions](#subsystem-functors) | Functorial constructions, Adjunctions, Base change, Free/Forgetful, Cohomology, De Rham, Group actions, and Induction. | **139** |
| [Lattices, Quadratic Forms & Invariants](#subsystem-lattices) | Free modules with quadratic forms, Genus, Definite/Root/Rational lattices, Isometries, Embeddings, Orbits, and Diagrams. | **82** |
| [Modules, Complexes & Homological Algebra](#subsystem-modules) | Framed free modules, Finitely presented modules, Formed modules, Group modules, Cochain complexes, Connections, and DG modules. | **201** |
| [Algebras & Differential Graded Algebras](#subsystem-algebras) | Associative/Commutative algebras, DGAs, Cohomology algebras, De Rham algebras, Derivations, and Graded algebras. | **124** |
| [Groups, Profinite Groups & Galois Theory](#subsystem-group) | Groups, Finitely presented groups, G-Sets, Actions, Profinite groups, Absolute Galois groups, Characters, and Inertia. | **105** |
| [Rings, Fields & Commutative Algebra](#subsystem-rings) | Owned rings, Fields, Number fields, Prime spectrum, Completions, Localizations, Exact real field, and Predicate subrings. | **96** |
| [Schemes & Algebraic Geometry](#subsystem-schemes) | Schemes, Affine/Projective schemes, Subschemes, Varieties, Curves, Surfaces, Polytopes, and Structure sheaves. | **47** |
| [Divisors & Picard Theory](#subsystem-divisors) | Divisor groups, Cartier divisors, Weil divisors, Picard groups, Class groups, and Formal divisors. | **13** |
| [Bilinear Forms, Quadratic Forms & Pairings](#subsystem-forms) | Bilinear/Quadratic forms, Pairings, Gram matrices, and Form spaces. | **12** |
| [Function Spaces & Analysis](#subsystem-functions) | Lebesgue modules, Lp, ell, C(X), Graded Lebesgue algebras, and Convolution algebras. | **12** |
| [Sets, Cardinals & Ordinals](#subsystem-sets) | Sets, Cardinalities, Ordinals, Enumerated sets, Fourier characters, Hermite polynomials, and Power sets. | **92** |
| [Named Catalogue & Classification Tables](#subsystem-catalogue) | Named integral lattices (U, E8, LK3, Mukai, etc.), 2-elementary tables, Nikulin involutions, and Primitive embeddings. | **7** |
| [Tensor Calculus](#subsystem-tensors) | Multilinear tensors, Tensor modules, Tensor shapes, and Tensor products. | **2** |
| [Logic & Predicates](#subsystem-logic) | Three-valued logic predicates, queries, and certainty propagation. | **2** |
| [Specialized Geometries (Coble & Sterk)](#subsystem-geometry-specialized) | Coble surfaces, Sterk invariant theory, and Automorphic forms. | **2** |
| [Preamble Entrypoints & Utilities](#subsystem-preamble-root) | Top-level session loaders, environment initializers, and refinement helpers. | **6** |
| [Language Runtime](#subsystem-language-runtime) | Constructions defined in subsystem language_runtime. | **14** |

---

<a id="subsystem-abstract-categories"></a>
## Abstract Category Theory & Universal Constructions

> Category of categories (Cat), Arrow and Slice categories, Limits, Colimits, Biproducts, Subobjects, and Diagram categories.

### 🏛 Categories & Subcategories

#### `ArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L168`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L168)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

The category ``Arr(C)=Fun([1],C)``.

**Category Constructor:**
- `ArrowCategory(self, base_category) -> None`

**Category Instance Methods:**
- `base_category(self)`
- `compose(self, second, first)`
- `hom(self, source, target)`
- `identity(self, arrow_object)`
- `morphism(self, source, target, left, right)`
- `object(self, arrow)`
- `super_categories(self)`

#### `AutCategoryConstruction` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L974`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L974)
- **Bases**: `AutCategoryOf`

#### `AutCategoryOf` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L913`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L913)
- **Bases**: `IsoCategoryOf`
- **Super Categories**: `[packet.Ends(), packet.Isos(), *inherited, HomCategories()]`

The family ``A |-> Aut_C(A)``.


**Category Instance Methods:**
- `Between(self, domain, codomain)`
- `Of(self, obj, codomain=None)`
- `family_over(self, category)`
- `super_categories(self)`

#### `AutomorphismArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L344`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L344)
- **Bases**: `IsoArrowCategory`

The full subcategory of the arrow category on automorphisms.


#### `BiproductCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L305`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L305)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

Objects equipped with the selected finite biproduct structure.

**Category Constructor:**
- `BiproductCategory(self, factors) -> None`

**Category Instance Methods:**
- `factors(self)`
- `super_categories(self)`

#### `Cat` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L89`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L89)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The represented category of categories.

**Category Constructor:**
- `Cat(self) -> None`

**Category Instance Methods:**
- `ArrowCategory(self)`
- `Hom(self, domain, codomain)`
- `arrow(self, functor)`
- `compose(self, second, first)`
- `functor_homset(self, domain, codomain)`
- `identity(self, category)`
- `object(self, category)`
- `super_categories(self)`

#### `CategoricalHomset` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L168`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L168)
- **Bases**: `Homset`, `Category`
- **Super Categories**: `supers or [Objects()]`

A represented Hom object which is both a Sage Homset and a category.

This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.

**Category Constructor:**
- `CategoricalHomset(self, family, domain, codomain) -> None`

**Category Instance Methods:**
- `accepts(self, arrow) -> bool`
- `arrow_set(self)`
- `attach_aut_family(self, family) -> None`
- `attach_end_family(self, family) -> None`
- `aut_family(self)`
- `base_category(self)`
- `codomain_object(self)`
- `domain_object(self)`
- `end_family(self)`
- `hom_family(self)`
- `identity_2(self, arrow)`
- `identity_endomorphism(self)`
- `object(self, arrow)`
- `super_categories(self)`
- `two_hom(self, domain, codomain)`

#### `CategoryPacketMethods` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L49`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L49)

The coordinated ``C/Hom_C/End_C/Iso_C/Aut_C`` construction surface.

This is deliberately a small live analogue of the archived ``Cat``
construction kernel.  It belongs on owned category base classes, not on
arbitrary Sage parents: the category chooses which Hom notion is meant,
and its Hom/End/Aut families then mirror ``super_categories()``.


**Category Instance Methods:**
- `Aut(self, obj)`
- `AutCategory(self)`
- `End(self, obj)`
- `EndCategory(self)`
- `Epi(self, source, target)`
- `EpiCategory(self)`
- `Hom(self, source, target)`
- `HomCategory(self)`
- `Iso(self, source, target)`
- `IsoCategory(self)`
- `Mono(self, source, target)`
- `MonoCategory(self)`

#### `CoconeCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L234`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L234)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The category of cocones under one represented diagram.

**Category Constructor:**
- `CoconeCategory(self, diagram) -> None`

**Category Instance Methods:**
- `ambient_category(self)`
- `cocone(self, apex, components)`
- `diagram(self)`
- `hom(self, domain, codomain)`
- `super_categories(self)`

#### `ColimitsOfCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L293`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L293)
- **Bases**: `LimitsOfCategory`

#### `ConeCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L196`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L196)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The category of cones over one represented diagram.

**Category Constructor:**
- `ConeCategory(self, diagram) -> None`

**Category Instance Methods:**
- `ambient_category(self)`
- `cone(self, apex, components)`
- `diagram(self)`
- `hom(self, domain, codomain)`
- `super_categories(self)`

#### `CoproductCoconeCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L276`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L276)
- **Bases**: `CoconeCategory`

Selected coproduct cocones under one finite discrete diagram.


#### `CoproductsOfCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L301`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L301)
- **Bases**: `ColimitsOfCategory`

#### `CoreCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L631`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L631)
- **Bases**: `Category`
- **Super Categories**: `[self.base_category()]`

The maximal subgroupoid (core) of a represented category.

**Category Constructor:**
- `CoreCategory(self, base_category) -> None`

**Category Instance Methods:**
- `base_category(self)`
- `hom(self, domain, codomain)`
- `identity(self, obj)`
- `super_categories(self)`

#### `CosliceCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L290`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L290)
- **Bases**: `ArrowCategory`

The coslice category \(X/C\).

**Category Constructor:**
- `CosliceCategory(self, base_category, base_object) -> None`

**Category Instance Methods:**
- `base_object(self)`
- `hom(self, source, target)`

#### `DirectSumObjects` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py#L11)
- **Bases**: `Category`
- **Super Categories**: `[SageSets()]`

Objects carrying a selected ordered family of direct summands.


**ParentMethods (Methods on Category Objects):**
- `number_of_summands(self)`
- `summand(self, label)`
- `summand_index_set(self)`
- `summands(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DiscreteCategories` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L286`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L286)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The category of represented discrete categories.


**Category Instance Methods:**
- `super_categories(self)`

#### `DiscreteCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L234`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L234)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The discrete category on one set.

**Category Constructor:**
- `DiscreteCategory(self, object_set) -> None`

**Category Instance Methods:**
- `hom(self, domain, codomain)`
- `identity(self, obj)`
- `object(self, value)`
- `object_set(self)`
- `objects(self)`
- `super_categories(self)`

#### `EndArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L326`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L326)
- **Bases**: `ArrowCategory`

The full subcategory of ``Arr(C)`` on endomorphisms.


#### `EndCategoryConstruction` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L958`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L958)
- **Bases**: `EndCategoryOf`

#### `EpiCategoryConstruction` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L966`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L966)
- **Bases**: `EpiCategoryOf`

#### `EpiCategoryOf` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L878`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L878)
- **Bases**: `_RestrictedCategoryOf`

**Category Instance Methods:**
- `accepts(self, arrow) -> bool`
- `family_over(self, category)`

#### `EpimorphismArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L365`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L365)
- **Bases**: `ArrowCategory`

The full subcategory of the arrow category on represented epimorphisms.


#### `FixedAutCategory` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L558`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L558)
- **Bases**: `FixedIsoCategory`
- **Super Categories**: `[packet.Ends().Of(obj), packet.Isos().Of(obj, obj), *inherited]`

**Category Instance Methods:**
- `identity_automorphism(self)`
- `super_categories(self)`

#### `FixedHomCategory` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L305`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L305)
- **Bases**: `Category`
- **Super Categories**: `supers or [Objects()]`

The category ``Hom_C(A,B)`` of arrows with fixed endpoints.

**Category Constructor:**
- `FixedHomCategory(self, family, domain, codomain) -> None`

**Category Instance Methods:**
- `accepts(self, arrow) -> bool`
- `arrow_set(self)`
- `attach_aut_family(self, family) -> None`
- `attach_end_family(self, family) -> None`
- `aut_family(self)`
- `base_category(self)`
- `codomain_object(self)`
- `domain_object(self)`
- `end_family(self)`
- `hom(self, domain, codomain)`
- `hom_family(self)`
- `identity(self, arrow_object)`
- `identity_endomorphism(self)`
- `object(self, arrow)`
- `objects(self)`
- `super_categories(self)`

#### `HomCategories` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L587`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L587)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The category of represented fixed-endpoint Hom categories.


**Category Instance Methods:**
- `super_categories(self)`

#### `HomCategoryOf` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L695`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L695)
- **Bases**: `Category`
- **Super Categories**: `supers + [HomCategories()]`

The family ``(A,B) |-> Hom_C(A,B)`` attached to one category ``C``.

**Category Constructor:**
- `HomCategoryOf(self, base_category) -> None`

**Category Instance Methods:**
- `Of(self, domain, codomain)`
- `base_category(self)`
- `family_over(self, category)`
- `fixed_category_class(self)`
- `fixed_category_class_for(self, domain, codomain)`
  > Return the represented fixed Hom class for these endpoints.
- `super_categories(self)`

#### `IsoArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L335`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L335)
- **Bases**: `ArrowCategory`

The full subcategory of ``Arr(C)`` on explicitly represented isomorphisms.


#### `IsoCategoryConstruction` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L970`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L970)
- **Bases**: `IsoCategoryOf`

#### `LimitsOfCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L280`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L280)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`
**Category Constructor:**
- `LimitsOfCategory(self, index_category, ambient_category) -> None`

**Category Instance Methods:**
- `super_categories(self)`

#### `MonoCategoryConstruction` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L962`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L962)
- **Bases**: `MonoCategoryOf`

#### `MonoCategoryOf` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L865`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L865)
- **Bases**: `_RestrictedCategoryOf`

**Category Instance Methods:**
- `accepts(self, arrow) -> bool`
- `family_over(self, category)`

#### `MonomorphismArrowCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L353`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L353)
- **Bases**: `ArrowCategory`

The full subcategory of the arrow category on represented monomorphisms.


#### `OppositeCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L78)
- **Bases**: `Category`
- **Super Categories**: `[SageSets()]`

The opposite category ``C^op``.

**Category Constructor:**
- `OppositeCategory(self, base_category) -> None`

**Category Instance Methods:**
- `base_category(self)`
- `hom(self, domain, codomain)`
- `identity(self, obj)`
- `@cached_method` `object(self, underlying_object)`
- `opposite_category(self)`
- `super_categories(self)`

#### `ProductCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L194`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L194)
- **Bases**: `Category`
- **Super Categories**: `[SageSets()]`

The categorical product ``C x D``.

**Category Constructor:**
- `ProductCategory(self, first_category, second_category) -> None`

**Category Instance Methods:**
- `first_category(self)`
- `hom(self, domain, codomain)`
- `identity(self, obj)`
- `@cached_method` `pair(self, first, second)`
- `second_category(self)`
- `super_categories(self)`

#### `ProductConeCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L272`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L272)
- **Bases**: `ConeCategory`

Selected product cones over one finite discrete diagram.


#### `ProductsOfCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L297`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L297)
- **Bases**: `LimitsOfCategory`

#### `SliceCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L248`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L248)
- **Bases**: `ArrowCategory`

The slice category \(C/X\).

**Category Constructor:**
- `SliceCategory(self, base_category, base_object) -> None`

**Category Instance Methods:**
- `base_object(self)`
- `hom(self, source, target)`

#### `SubobjectCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L448`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L448)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

The category of represented subobjects of one fixed object.

An object is an object ``A`` of the base category equipped with its chosen
monomorphism ``A.inclusion(): A -> X``.  Morphisms are the commuting
triangles between those inclusions.

**Category Constructor:**
- `SubobjectCategory(self, base_category, base_object) -> None`

**Category Instance Methods:**
- `as_slice_object(self, subobject)`
- `base_category(self)`
- `base_object(self)`
- `hom(self, domain, codomain)`
- `identity(self, subobject)`
- `leq(self, left, right) -> bool`
- `monomorphism_category(self)`
  > Return the monomorphism subcategory of the ambient arrow category.
- `slice_category(self)`
  > Return the ambient slice ``C/X`` in which subobjects are monomorphisms.
- `super_categories(self)`

#### `SuperobjectCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L521`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L521)
- **Bases**: `CosliceCategory`

The category of represented quotient/superobjects of one object.


#### `TensorProductCategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L331`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L331)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

Objects equipped with a chosen tensor-product universal bilinear map.

**Category Constructor:**
- `TensorProductCategory(self, factors) -> None`

**Category Instance Methods:**
- `super_categories(self)`
- `tensor_factors(self)`

#### `WideSubcategory` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L534`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L534)
- **Bases**: `Category`
- **Super Categories**: `[self.base_category()]`

A category with the same objects as ``C`` and a selected class of arrows.

**Category Constructor:**
- `WideSubcategory(self, base_category, arrow_category) -> None`

**Category Instance Methods:**
- `admits(self, arrow) -> bool`
- `arrow_category(self)`
- `base_category(self)`
- `super_categories(self)`

### 🔄 Functors & Adjunctions

#### `Bifunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L73`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L73)
- **Bases**: `Functor`

A functor ``C x D -> E`` with a two-argument convenience API.

**Constructors / Factory Signatures:**
- `def __init__(self, left_domain, right_domain, codomain) -> None`
- `def __call__(self, left, right=None)`

**Functor / Adjunction Methods:**
- `left_domain(self)`
- `morphism_image(self, left_morphism, right_morphism=None)`
- `object_image(self, left, right=None)`
- `right_domain(self)`

#### `CartesianProductFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L524`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L524)
- **Bases**: `ProductFunctor`

The binary Cartesian-product functor on Set.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `CategoryFunctorHomset` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L68`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L68)
- **Bases**: `Homset`
**Constructors / Factory Signatures:**
- `def __init__(self, category_of_categories, domain, codomain) -> None`
- `def _element_constructor_(self, functor)`

**Functor / Adjunction Methods:**
- `category_of_categories(self)`
- `identity(self)`

#### `CategoryFunctorMorphism` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L35)
- **Bases**: `Morphism`

A live functor regarded as a morphism in ``Cat``.

**Constructors / Factory Signatures:**
- `def __init__(self, parent, functor) -> None`
- `def __call__(self, value)`
- `def _call_(self, value)`

**Functor / Adjunction Methods:**
- `functor(self)`

#### `CodomainFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L165`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L165)
- **Bases**: `Functor`

The codomain functor ``Arr(C) -> C``.

**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

#### `ColimitFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L542`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L542)
- **Bases**: `CoproductFunctor`

The represented binary colimit functor; binary coproducts are its discrete case.


#### `ConstantDiagram` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L360`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L360)
- **Bases**: `Functor`

The constant functor from an index category at one object.

**Constructors / Factory Signatures:**
- `def __init__(self, index_category, codomain, value) -> None`

**Functor / Adjunction Methods:**
- `constant_value(self)`

#### `ContravariantFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L24`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L24)
- **Bases**: `Functor`

A functor ``C^op -> D`` with convenience calls on arrows of ``C``.

**Constructors / Factory Signatures:**
- `def __init__(self, domain, codomain) -> None`

**Functor / Adjunction Methods:**
- `adopt_object_image(self, preimage, image)`
- `base_domain(self)`
- `chosen_preimage(self, image)`
- `morphism_image(self, morphism)`
- `object_image(self, obj)`

#### `CoproductFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L499`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L499)
- **Bases**: `Functor`

The binary categorical coproduct functor ``C x C -> C`` where represented.

**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

#### `DiagonalFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L451`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L451)
- **Bases**: `Functor`

The diagonal functor ``C -> C x C``.

**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

**Functor / Adjunction Methods:**
- `product_category(self)`

#### `DiagramCategory` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L14`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L14)
- **Bases**: `FunctorCategory`

The functor category ``[J,C]`` of diagrams of one shape.

**Constructors / Factory Signatures:**
- `def __init__(self, index_category, ambient_category) -> None`

**Functor / Adjunction Methods:**
- `ambient_category(self)`
- `index_category(self)`

#### `DiscreteDiagram` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L341`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L341)
- **Bases**: `Functor`

A functor from a discrete category, specified on its objects.

**Constructors / Factory Signatures:**
- `def __init__(self, index_category, codomain, values) -> None`

**Functor / Adjunction Methods:**
- `diagram_objects(self)`

#### `DiscreteFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L300`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L300)
- **Bases**: `Functor`

A functor between discrete categories induced by a map of object sets.

**Constructors / Factory Signatures:**
- `def __init__(self, domain, codomain, object_map) -> None`

**Functor / Adjunction Methods:**
- `object_map(self)`

#### `DisjointUnionFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L531`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L531)
- **Bases**: `CoproductFunctor`

The binary disjoint-union functor on Set.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `DomainFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L152`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L152)
- **Bases**: `Functor`

The domain functor ``Arr(C) -> C``.

**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

#### `FunctorCategory` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L218`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L218)
- **Bases**: `Category`

The category ``[C,D]`` of represented functors and natural transformations.

**Constructors / Factory Signatures:**
- `def __init__(self, category_of_categories, domain, codomain) -> None`

**Functor / Adjunction Methods:**
- `codomain_category(self)`
- `domain_category(self)`
- `hom(self, domain, codomain)`
- `identity(self, functor_object)`
- `object(self, functor)`
- `super_categories(self)`

#### `FunctorImageCategories` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L86`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L86)
- **Bases**: `Category`

The category whose objects are represented functor-image categories.


**Functor / Adjunction Methods:**
- `super_categories(self)`

#### `FunctorImageHomset` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L60`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L60)
- **Bases**: `Homset`
**Constructors / Factory Signatures:**
- `def __init__(self, image_category, domain, codomain) -> None`
- `def _element_constructor_(self, codomain_arrow)`

**Functor / Adjunction Methods:**
- `identity(self)`
- `image_category(self)`

#### `FunctorImageMorphism` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L37`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L37)
- **Bases**: `Morphism`

A codomain arrow between two chosen functor-image presentations.

**Constructors / Factory Signatures:**
- `def __init__(self, parent, codomain_arrow) -> None`

**Functor / Adjunction Methods:**
- `codomain_arrow(self)`

#### `FunctorImageObject` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L12`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L12)
- **Bases**: `Parent`

A chosen presentation ``A`` together with its image ``F(A)``.

**Constructors / Factory Signatures:**
- `def __init__(self, image_category, preimage, image_object) -> None`

**Functor / Adjunction Methods:**
- `constructing_functor(self)`
- `image_category(self)`
- `image_object(self)`
- `preimage(self)`

#### `ImageInclusionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L130`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L130)
- **Bases**: `Functor`

Forget the chosen preimage of a presented functor-image object.

**Constructors / Factory Signatures:**
- `def __init__(self, image_category) -> None`

**Functor / Adjunction Methods:**
- `image_category(self)`

#### `ImageOfFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L96`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functor_images.py#L96)
- **Bases**: `Category`

The category of outputs of ``F`` equipped with chosen preimages.

An object is the pair ``(A, F(A))``.  The inclusion/projection to the
codomain forgets only the chosen presentation.  This does not attempt to
recover ``A`` from ``F(A)``, which is impossible for a general functor.

**Constructors / Factory Signatures:**
- `def __init__(self, functor) -> None`

**Functor / Adjunction Methods:**
- `functor(self)`
- `hom(self, domain, codomain)`
- `identity(self, obj)`
- `inclusion(self)`
- `@cached_method` `present(self, preimage)`
- `super_categories(self)`

#### `LimitFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L538`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L538)
- **Bases**: `ProductFunctor`

The represented binary limit functor; binary products are its discrete case.


#### `NaturalIsomorphism` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L275`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L275)

A selected pair of mutually inverse natural transformations.

**Constructors / Factory Signatures:**
- `def __init__(self, forward, inverse) -> None`

**Functor / Adjunction Methods:**
- `component(self, obj)`
- `forward(self)`
- `inverse(self)`

#### `ObjectSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L324`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L324)
- **Bases**: `Functor`

Take the object set of a represented discrete category.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `ProductFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L474`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L474)
- **Bases**: `Functor`

The binary categorical product functor ``C x C -> C`` where represented.

**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

#### `compose_functors` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L379`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L379)

Return ``second ∘ first`` in the current functor core.

**Constructors / Factory Signatures:**
- `def compose_functors(second, first)`
  > Return ``second ∘ first`` in the current functor core.

### ⚙ Universal Categorical Constructions

#### `Biproduct` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L37`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L37)
- **Signature**: `def Biproduct(left, right)`

#### `Cokernel` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L94`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L94)
- **Signature**: `def Cokernel(morphism)`

#### `Coproduct` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L45`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L45)
- **Signature**: `def Coproduct(left, right)`

#### `CosliceUnder` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L672`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L672)
- **Signature**: `def CosliceUnder(base_category, base_object)`

#### `DirectSumDecomposition` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py#L64`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py#L64)

Equip ``underlying_object`` with the selected decomposition ``⊕ M_i``.

This does not construct a new direct sum.  It records a decomposition of an
object already in hand, after verifying the represented binary universal
map when that is the active backend.

- **Signature**: `def DirectSumDecomposition(underlying_object, summands, summand_index_set=None)`

#### `Kernel` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L87)
- **Signature**: `def Kernel(morphism)`

#### `Product` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L41`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L41)
- **Signature**: `def Product(left, right)`

#### `SliceOver` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L668`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L668)
- **Signature**: `def SliceOver(base_category, base_object)`

#### `Subobjects` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L101`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L101)
- **Signature**: `def Subobjects(base_object, category=None)`

#### `TensorProduct` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L29`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L29)
- **Signature**: `def TensorProduct(left, right)`

#### `TensorSquare` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L33)
- **Signature**: `def TensorSquare(obj)`

#### `ambient_category_of` `[CONSTRUCTION]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L354`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L354)
- **Signature**: `def ambient_category_of(objects)`

#### `common_category` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L319`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L319)

Return the greatest Sage category common to the stated objects.

- **Signature**: `def common_category(*objects)`

### ↗ Morphisms & Hom-Sets

#### `ArrowHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L143`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L143)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, arrow_category, source, target) -> None`
- **Constructor**: `def _element_constructor_(self, left, right=None)`

**Public Methods:**
- `arrow_category(self)`
- `identity(self)`

#### `CategoricalIsomorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L570`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L570)
- **Bases**: `Morphism`

An isomorphism represented by mutually inverse arrows.

- **Constructor**: `def __init__(self, parent, forward, inverse) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `forward(self)`
- `inverse(self)`

#### `CoconeHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L182`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L182)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, cocone_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, apex_map)`

**Public Methods:**
- `cocone_category(self)`

#### `CoconeMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L142`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L142)
- **Bases**: `Morphism`

A morphism of cocones, determined by its apex map.

- **Constructor**: `def __init__(self, parent, apex_map) -> None`

**Public Methods:**
- `apex_map(self)`

#### `CommutativeSquare` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L105`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L105)
- **Bases**: `Morphism`

A morphism between two arrow objects, i.e. a commuting square.

- **Constructor**: `def __init__(self, parent, left, right) -> None`

**Public Methods:**
- `components(self)`
- `left(self)`
- `right(self)`

#### `ConeHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L168`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L168)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, cone_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, apex_map)`

**Public Methods:**
- `cone_category(self)`

#### `ConeMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L118`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L118)
- **Bases**: `Morphism`

A morphism of cones, determined by its apex map.

- **Constructor**: `def __init__(self, parent, apex_map) -> None`

**Public Methods:**
- `apex_map(self)`

#### `CoreHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L613`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L613)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, forward, inverse=None)`

**Public Methods:**
- `identity(self)`

#### `CosliceHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L277`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L277)
- **Bases**: `ArrowHomset`

Morphisms in a coslice; the edge at the fixed domain is the identity.

- **Constructor**: `def _element_constructor_(self, factor, left=None)`

#### `DiscreteHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L210`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L210)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, discrete_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, value=None)`

**Public Methods:**
- `cardinality(self)`
- `discrete_category(self)`
- `identity(self)`

#### `DiscreteMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L196`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L196)
- **Bases**: `Morphism`

The unique identity arrow of a discrete-category object.

- **Constructor**: `def __init__(self, parent) -> None`

#### `EndCategoryOf` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L819`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L819)
- **Bases**: `HomCategoryOf`

The family ``A |-> End_C(A)``.


**Public Methods:**
- `Between(self, domain, codomain)`
- `Of(self, obj, codomain=None)`
- `family_over(self, category)`

#### `FixedEndCategory` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L463`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L463)
- **Bases**: `FixedHomCategory`

The category ``End_C(A)`` of endomorphisms of one object.


**Public Methods:**
- `identity_endomorphism(self)`

#### `FixedIsoCategory` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L494`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L494)
- **Bases**: `FixedHomCategory`

**Public Methods:**
- `accepts(self, arrow) -> bool`
- `identity_automorphism(self)`
- `super_categories(self)`

#### `FixedRestrictedHomCategory` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L475`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L475)
- **Bases**: `FixedHomCategory`

**Public Methods:**
- `accepts(self, arrow) -> bool`
- `super_categories(self)`

#### `HomArrowDiscreteHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L147`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L147)
- **Bases**: `Homset`

The discrete 2-Hom between two arrow objects.

- **Constructor**: `def __init__(self, hom_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, value=None)`

**Public Methods:**
- `hom_category(self)`
- `identity(self)`

#### `HomArrowIdentity` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L140)
- **Bases**: `Morphism`

The identity 2-arrow on one arrow object.

- **Constructor**: `def _call_(self, value)`

#### `HomCategoryConstruction` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L954`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L954)
- **Bases**: `HomCategoryOf`

#### `IsoCategoryOf` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L891`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L891)
- **Bases**: `HomCategoryOf`

**Public Methods:**
- `family_over(self, category)`
- `super_categories(self)`

#### `NaturalTransformationHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L180`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L180)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, functor_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, transformation)`

**Public Methods:**
- `functor_category(self)`
- `identity(self)`

#### `NaturalTransformationMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L143`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L143)
- **Bases**: `Morphism`

A natural transformation as a morphism in a functor category.

- **Constructor**: `def __init__(self, parent, transformation) -> None`

**Public Methods:**
- `component(self, obj)`
- `naturality_square(self, morphism)`
- `transformation(self)`

#### `OppositeHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L59`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L59)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, opposite_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, underlying_arrow)`

**Public Methods:**
- `identity(self)`
- `opposite_category(self)`

#### `OppositeMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L37`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L37)
- **Bases**: `Morphism`

An arrow of ``C^op`` represented by the reverse arrow in ``C``.

- **Constructor**: `def __init__(self, parent, underlying_arrow) -> None`

**Public Methods:**
- `underlying_arrow(self)`

#### `ProductHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L173`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L173)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, product_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, first, second=None)`

**Public Methods:**
- `identity(self)`
- `product_category(self)`

#### `ProductMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L147`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L147)
- **Bases**: `Morphism`

A pair of morphisms in a product category.

- **Constructor**: `def __init__(self, parent, first, second) -> None`

**Public Methods:**
- `first(self)`
- `second(self)`

#### `SliceHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L230`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L230)
- **Bases**: `ArrowHomset`

Morphisms in a slice; the edge at the fixed codomain is the identity.

- **Constructor**: `def _element_constructor_(self, factor, right=None)`

**Public Methods:**
- `canonical_morphism(self)`

#### `SubobjectHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L414`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L414)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, subobject_category, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, factor_morphism=None)`

**Public Methods:**
- `canonical_morphism(self)`
- `has_morphism(self) -> bool`
- `identity(self)`
- `subobject_category(self)`

#### `SubobjectMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L382`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L382)
- **Bases**: `Morphism`

The unique commuting-triangle map between two represented subobjects.

- **Constructor**: `def __init__(self, parent, factor_morphism) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `factor_morphism(self)`

### 📦 Mathematical Objects & Parents

#### `ArrowObject` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L81`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L81)
- **Bases**: `Parent`

A morphism of ``C`` regarded as an object of ``Arr(C)``.

- **Constructor**: `def __init__(self, arrow_category, arrow) -> None`

**Public Methods:**
- `arrow(self)`
- `arrow_category(self)`
- `source_object(self)`
- `target_object(self)`

#### `CategoryObject` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/cat.py#L17`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/cat.py#L17)
- **Bases**: `Parent`

A Sage category regarded as an object of ``Cat``.

- **Constructor**: `def __init__(self, category_of_categories, represented_category) -> None`

**Public Methods:**
- `category_of_categories(self)`
- `represented_category(self)`

#### `CategoryPacket` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L597`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L597)
- **Bases**: `SageObject`

The coordinated ``C / Hom_C / End_C / Iso_C / Aut_C`` packet.

- **Constructor**: `def __init__(self, category) -> None`

**Public Methods:**
- `Auts(self)`
- `Ends(self)`
- `Epis(self)`
- `Homs(self)`
- `Isos(self)`
- `Monos(self)`
- `category(self)`
- `super_packets(self)`

#### `CoconeObject` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L68`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L68)
- **Bases**: `Parent`

A cocone ``D => Delta(A)`` under a diagram ``D:J->C``.

- **Constructor**: `def __init__(self, cocone_category, apex, transformation) -> None`

**Public Methods:**
- `apex(self)`
- `cocone_category(self)`
- `costructure_morphism(self, index)`
- `costructure_morphisms(self)`
- `diagram(self)`
- `transformation(self)`

#### `ConeObject` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L35)
- **Bases**: `Parent`

A cone ``Delta(A) => D`` over a diagram ``D:J->C``.

- **Constructor**: `def __init__(self, cone_category, apex, transformation) -> None`

**Public Methods:**
- `apex(self)`
- `cone_category(self)`
- `diagram(self)`
- `structure_morphism(self, index)`
- `structure_morphisms(self)`
- `transformation(self)`

#### `DirectedSystem` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L27`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L27)
- **Bases**: `DiagramCategory`

A diagram category whose index category represents a directed order.


#### `DiscreteObject` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L178`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L178)
- **Bases**: `Parent`

One object of the discrete category on a set.

- **Constructor**: `def __init__(self, discrete_category, value) -> None`

**Public Methods:**
- `discrete_category(self)`
- `value(self)`

#### `HomArrowObject` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L110`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L110)
- **Bases**: `Parent`

An arrow regarded as an object of a fixed-endpoint Hom category.

- **Constructor**: `def __init__(self, arrow) -> None`

**Public Methods:**
- `arrow(self)`

#### `InverseSystem` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L31`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L31)
- **Bases**: `DiagramCategory`

A diagram category read contravariantly as an inverse system.


#### `NaturalTransformationSpace` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L400`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L400)
- **Bases**: `Parent`

The represented Hom-object of natural transformations ``F => G``.

- **Constructor**: `def __init__(self, source, target) -> None`
- **Constructor**: `def _element_constructor_(self, components)`

**Public Methods:**
- `source(self)`
- `target(self)`

#### `OppositeObject` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L19)
- **Bases**: `Parent`

An object of ``C`` regarded as an object of ``C^op``.

- **Constructor**: `def __init__(self, opposite_category, underlying_object) -> None`

**Public Methods:**
- `opposite_category(self)`
- `underlying_object(self)`

#### `ProductObject` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L125`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/category_constructions.py#L125)
- **Bases**: `Parent`

An object ``(X,Y)`` of a product category ``C x D``.

- **Constructor**: `def __init__(self, product_category, first, second) -> None`

**Public Methods:**
- `first(self)`
- `product_category(self)`
- `second(self)`

### 🛠 Helper Functions & Constructors

#### `Cocone` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Cocone(diagram, apex, components)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L365`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L365)

#### `Cone` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Cone(diagram, apex, components)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L361`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L361)

#### `Core` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Core(base_category)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L664`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L664)

#### `FiberProduct` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FiberProduct(left_morphism, right_morphism)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L77`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L77)

#### `Isomorphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Isomorphism(forward, inverse)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L684`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L684)

Return the isomorphism represented by mutually inverse arrows.


#### `NaturalIsomorphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def NaturalIsomorphism(source, target, components, inverse_components)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L418`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L418)

Return mutually inverse natural transformations as a categorical pair.


#### `NaturalTransformations` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def NaturalTransformations(source, target)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/functors.py#L393`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/functors.py#L393)

Return the represented type of natural transformations between parallel functors.


#### `Pushout` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Pushout(left_morphism, right_morphism)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/constructions.py#L67`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/constructions.py#L67)

#### `SubobjectsOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def SubobjectsOf(base_category, base_object)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L676`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L676)

#### `SuperobjectsOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def SuperobjectsOf(base_category, base_object)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L680`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py#L680)

#### `category_packet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def category_packet(category) -> CategoryPacket`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L691`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/hom_categories.py#L691)

#### `coproduct_cocone_category` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def coproduct_cocone_category(factors, ambient_category=None)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L388`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L388)

#### `product_cone_category` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def product_cone_category(factors, ambient_category=None)`
- **Source**: [`src/dzack_research/preamble/categories/abstract_categories/products.py#L384`](file:///home/dzack/research/src/dzack_research/preamble/categories/abstract_categories/products.py#L384)


---

<a id="subsystem-functors"></a>
## Functors & Adjunctions

> Functorial constructions, Adjunctions, Base change, Free/Forgetful, Cohomology, De Rham, Group actions, and Induction.

### 🔄 Functors & Adjunctions

#### `AbelianGroupInclusionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/abelianization.py#L104`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/abelianization.py#L104)
- **Bases**: `Functor`

The full inclusion ``Ab -> Grp``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`

#### `AbelianizationAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/abelianization.py#L125`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/abelianization.py#L125)
- **Bases**: `Adjunction`

``(-)^ab ⊣ i``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `counit(self, abelian_group)`
- `unit(self, group)`

#### `AbelianizationFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/abelianization.py#L29`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/abelianization.py#L29)
- **Bases**: `Functor`

``G -> G/[G,G] : Grp -> Ab``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `quotient_projection(self, group)`
- `quotient_projection_from_image(self, abelianization)`
- `source_group(self, abelianization)`

#### `Adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L250`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L250)
- **Bases**: `SageObject`

An adjunction ``F ⊣ U`` with its unit, counit, and Hom-set bijection.

**Constructors / Factory Signatures:**
- `def __init__(self, left_adjoint: Functor, right_adjoint: Functor) -> None`

**Functor / Adjunction Methods:**
- `counit(self, obj)`
- `counit_transformation(self) -> NaturalTransformation`
- `hom_set_isomorphism_forward(self, morphism, source=None)`
  > Transpose ``f:F(A)->B`` to ``U(f) after eta_A``.
- `hom_set_isomorphism_inverse(self, morphism, codomain=None)`
  > Transpose ``g:A->U(B)`` to ``epsilon_B after F(g)``.
- `left_adjoint(self) -> Functor`
- `right_adjoint(self) -> Functor`
- `unit(self, obj)`
- `unit_transformation(self) -> NaturalTransformation`

#### `AlgebraBaseChangeAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L194`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L194)
- **Bases**: `Adjunction`

The represented algebra adjunction ``S tensor_R - ⊣ Res_f``.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `counit(self, algebra)`
- `unit(self, algebra)`

#### `AlgebraRestrictionOfScalarsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L142`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L142)
- **Bases**: `Functor`

``Res_f : Alg_S -> Alg_R`` along ``f : R -> S``.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `ring_map(self)`

#### `AlgebraScalarExtensionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L76`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L76)
- **Bases**: `Functor`

``S tensor_R - : Alg_R -> Alg_S`` along ``f : R -> S``.

The functor is mathematical on all algebras.  The live object adapter is
deliberately narrower: it materializes chosen finite polynomial
presentations and refuses to advertise an unavailable general tensor
algebra backend as though it had been constructed.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `ring_map(self)`
- `source_algebra(self, extended_algebra)`
  > Return the algebra recorded by this scalar-extension construction.

#### `AlgebraUnderlyingModuleFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_modules.py#L251`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_modules.py#L251)
- **Bases**: `Functor`

\(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\).

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, algebra_category=None) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `AlternatingAlgebraFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L97`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L97)
- **Bases**: `Functor`

Exterior-algebra functor on represented modules.

No ordinary free/forgetful adjunction is asserted for this construction.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `BaseChangeAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/scalar_change.py#L132`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/scalar_change.py#L132)
- **Bases**: `Adjunction`

``S tensor_R - ⊣ Res_f``.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `counit(self, module)`
- `unit(self, module)`

#### `BilinearFreeFormAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L182`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L182)
- **Bases**: `_FreeFormAdjunction`

The tautological bilinear-form classifier adjunction.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `BilinearUnderlyingModuleFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L58`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L58)
- **Bases**: `_UnderlyingFormModuleFunctor`
**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `CardinalityFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cardinality.py#L14`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cardinality.py#L14)
- **Bases**: `Functor`

Send a set to its cardinal and a set isomorphism to the unique order arrow.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `CategoryInclusionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L148`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L148)
- **Bases**: `Functor`

The canonical functor along a declared subcategory inclusion.

If ``C`` is a subcategory of ``D``, every object and morphism of ``C`` is
already an object and morphism of ``D``.  The functor therefore changes
only the category in which the same mathematical data is read.

**Constructors / Factory Signatures:**
- `def __init__(self, subcategory, supercategory) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`

#### `CochainUnderlyingGradedModuleFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cochain_complexes.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cochain_complexes.py#L11)
- **Bases**: `Functor`

Forget the differential while retaining the same graded carrier.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `CofreeGSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L254`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L254)
- **Bases**: `Functor`

``Map(G,-) : FinSet -> FinGSet_G`` with ``(a f)(h)=f(h a)``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `function_point(self, cofree_g_set, function)`
- `function_value(self, cofree_g_set, function_point, group_element)`
- `group(self)`
- `group_points(self)`
- `source_set(self, cofree_g_set)`

#### `CohomologyAlgebraFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L95`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L95)
- **Bases**: `Functor`

The graded cohomology-algebra functor ``H^*`` on strict CDGAs.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `CohomologyFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L19)
- **Bases**: `Functor`

The degree-``p`` cohomology functor ``H^p : Coch_R -> Mod_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, degree) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`
- `degree(self)`

#### `CoinductionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L307`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L307)
- **Bases**: `Functor`

``Coind_H^G : R[H]-Mod_fp -> R[G]-Mod_fp``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, subgroup, supergroup=None) -> None`

**Functor / Adjunction Methods:**
- `element_from_values(self, coinduced, value_function)`
- `identity_representative(self)`
- `inclusion(self)`
- `representatives(self)`
- `source_group_module(self, coinduced)`
- `subgroup(self)`
- `supergroup(self)`
- `value_at(self, coinduced, vector, representative)`

#### `CoinvariantsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L121`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L121)
- **Bases**: `Functor`

``(-)_G`` on represented finitely-presented ``R[G]``-modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, group) -> None`

#### `CoinvariantsTrivialAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L186`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L186)
- **Bases**: `Adjunction`

``(-)_G ⊣ Triv_G``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, module)`
- `unit(self, group_module)`

#### `CokernelArrowFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/linear_constructions.py#L117`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/linear_constructions.py#L117)
- **Bases**: `_ArrowConstructionFunctor`

The cokernel functor from the finite-free module arrow category.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `CompositeAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L302`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L302)
- **Bases**: `Adjunction`

The composite of ``F ⊣ U`` and ``G ⊣ V`` as ``GF ⊣ UV``.

**Constructors / Factory Signatures:**
- `def __init__(self, first: Adjunction, second: Adjunction) -> None`

**Functor / Adjunction Methods:**
- `counit(self, obj)`
- `first(self) -> Adjunction`
- `second(self) -> Adjunction`
- `unit(self, obj)`

#### `CompositeFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L183`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L183)
- **Bases**: `Functor`

The composite ``second ∘ first``.

**Constructors / Factory Signatures:**
- `def __init__(self, first: Functor, second: Functor) -> None`

**Functor / Adjunction Methods:**
- `adopt_object_image(self, preimage, image)`
- `chosen_preimage(self, image)`
- `factors(self)`
- `is_faithful(self) -> bool`

#### `DeRhamAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L144)
- **Bases**: `Adjunction`

The adjunction ``DR_R ⊣ (-)^0``.

On the represented carriers the Hom-set bijection is the universal
extension of an algebra map ``A -> B^0`` by ``da |-> d_B(a)``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`
- `counit(self, dga)`
- `unit(self, algebra)`

#### `DeRhamCohomologyAlgebraFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L128`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L128)
- **Bases**: `CompositeFunctor`

The composite ``H^* ∘ DR_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `DeRhamCohomologyFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L65`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L65)
- **Bases**: `CompositeFunctor`

The literal composite ``H^p ∘ U_Coch ∘ DR_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, degree) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`
- `degree(self)`

#### `DeRhamFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L71`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L71)
- **Bases**: `Functor`

``DR_R : CAlg_R -> SCDGA_R^{>=0}`` on represented affine algebras.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`
- `chosen_preimage(self, image)`

#### `DegreeZeroDGAFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L103`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L103)
- **Bases**: `Functor`

Degree zero ``(-)^0 : SCDGA_R^{>=0} -> CAlg_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `DirectImageSubobjectFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/subobject_images.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/subobject_images.py#L19)
- **Bases**: `Functor`

The monotone map ``f_* : Sub(M) -> Sub(N)``.

**Constructors / Factory Signatures:**
- `def __init__(self, morphism) -> None`

**Functor / Adjunction Methods:**
- `morphism(self)`

#### `DividedPowerAlgebraFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L125`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L125)
- **Bases**: `Functor`

The divided-power algebra functor ``Gamma_R : Mod_R -> DPAlg_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `DualizationFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/linear_constructions.py#L25`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/linear_constructions.py#L25)
- **Bases**: `ContravariantFunctor`

Finite-free duality ``(-)^* : C^op -> C``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `double_dual_morphism(self, module)`
  > Return the canonical finite-free biduality map ``M -> M**``.

#### `ExponentialFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L26)
- **Bases**: `Functor`

The internal-Hom functor ``Set^op x Set -> Set``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `morphism(self, precompose, postcompose)`
  > Return the product-category morphism induced by ``precompose`` and ``postcompose``.
- `opposite_sets(self)`
- `pair(self, exponent, codomain)`

#### `FinitePowerSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L87)
- **Bases**: `Functor`

The covariant finite-power-set functor under direct image.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `FixedCardinalitySubsetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L105`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L105)
- **Bases**: `Functor`

Direct image on ``k``-element subsets, defined on injective set maps.

**Constructors / Factory Signatures:**
- `def __init__(self, subset_cardinality) -> None`

**Functor / Adjunction Methods:**
- `subset_cardinality(self)`

#### `ForgetTheFormFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L46`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L46)
- **Bases**: `_UnderlyingFormModuleFunctor`

Forget the selected form from one represented formed-module category.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, formed_category) -> None`

#### `FractionFieldFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/orders_number_fields.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/orders_number_fields.py#L26)
- **Bases**: `Functor`

``Frac : Orders -> NumberFields``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

#### `FreeBilinearFormFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L76`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L76)
- **Bases**: `Functor`

Send ``M`` to ``(M, M tensor M, universal pure tensor)``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `FreeForgetfulAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forgetful.py#L59`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forgetful.py#L59)
- **Bases**: `Adjunction`

``F_R ⊣ U`` between sets and ``R``-modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `counit(self, module)`
- `unit(self, set_object)`

#### `FreeGSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L165`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L165)
- **Bases**: `Functor`

``G × - : FinSet -> FinGSet_G`` with left translation on ``G``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `free_point(self, free_g_set, group_element, point)`
- `group(self)`
- `source_set(self, free_g_set)`

#### `FreeGSetUnderlyingAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L328`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L328)
- **Bases**: `Adjunction`

``G × - ⊣ U`` on finite sets and represented finite ``G``-sets.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, g_set)`
- `unit(self, set_object)`

#### `FreeGroupFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_groups.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_groups.py#L22)
- **Bases**: `Functor`

``F : Set -> Grp``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `source_set(self, free_group)`

#### `FreeGroupUnderlyingSetAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_groups.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_groups.py#L78)
- **Bases**: `Adjunction`

The adjunction ``F : Set <-> Grp : U``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `counit(self, group)`
- `unit(self, set_object)`

#### `FreeModuleFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forgetful.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forgetful.py#L15)
- **Bases**: `Functor`

``F_R : Set -> Mod_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `FreeQuadraticFormFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L115`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L115)
- **Bases**: `Functor`

Send ``M`` to ``(M, Gamma^2(M), gamma_2)``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `Functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L13`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L13)
- **Bases**: `SageObject`

A functor with explicit actions on objects and morphisms.

**Constructors / Factory Signatures:**
- `def __init__(self, domain, codomain) -> None`
- `def __call__(self, value)`

**Functor / Adjunction Methods:**
- `adopt_object_image(self, preimage, image)`
  > Use a provenance-validated exact image object for ``preimage``.
- `chosen_preimage(self, image)`
  > Return the unique source object recorded for this exact functor image.
- `codomain(self)`
- `domain(self)`
- `factors(self)`
- `is_faithful(self) -> bool`
- `morphism_image(self, morphism)`
- `object_image(self, obj)`
- `on_morphism(self, morphism)`
- `on_object(self, obj)`
- `then(self, other)`
  > Return ``other ∘ self``.

#### `GSetFixedPointsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L102`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L102)
- **Bases**: `Functor`

``(-)^G : FinGSet_G -> FinSet``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `group(self)`

#### `GSetOrbitsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L71`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L71)
- **Bases**: `Functor`

``(-)/G : FinGSet_G -> FinSet``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `group(self)`

#### `GSetOrbitsTrivialAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L124`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L124)
- **Bases**: `Adjunction`

``(-)/G ⊣ Triv_G`` on represented finite ``G``-sets.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, set_object)`
- `unit(self, g_set)`

#### `GSetTrivialFixedAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L146`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L146)
- **Bases**: `Adjunction`

``Triv_G ⊣ (-)^G`` on represented finite ``G``-sets.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, g_set)`
- `unit(self, set_object)`

#### `GroupModuleBaseChangeAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_scalar_change.py#L200`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_scalar_change.py#L200)
- **Bases**: `Adjunction`

``S tensor_R - ⊣ Res_f`` on modules carrying a fixed ``G``-action.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, group_module)`
- `unit(self, group_module)`

#### `GroupModuleRestrictionOfScalarsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_scalar_change.py#L114`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_scalar_change.py#L114)
- **Bases**: `Functor`

``Res_f : S[G]-Mod -> R[G]-Mod``.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `group(self)`
- `ring_map(self)`

#### `GroupModuleScalarExtensionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_scalar_change.py#L50`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_scalar_change.py#L50)
- **Bases**: `Functor`

``S tensor_R - : R[G]-Mod -> S[G]-Mod`` along one scalar map.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `group(self)`
- `ring_map(self)`

#### `GroupUnderlyingSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_groups.py#L52`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_groups.py#L52)
- **Bases**: `Functor`

``U : Grp -> Set``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`

#### `IdentityFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L123`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L123)
- **Bases**: `Functor`
**Constructors / Factory Signatures:**
- `def __init__(self, category) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `factors(self)`
- `is_faithful(self) -> bool`

#### `InducedAutFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L107)
- **Bases**: `Functor`

The functor ``Aut_C(A) -> Aut_D(F(A))`` induced by ``F``.

**Constructors / Factory Signatures:**
- `def __init__(self, functor, obj) -> None`
- `def __call__(self, value)`

**Functor / Adjunction Methods:**
- `base_functor(self)`
- `morphism_image(self, morphism)`
- `object_image(self, arrow_object)`

#### `InducedEndFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L68`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L68)
- **Bases**: `Functor`

The functor ``End_C(A) -> End_D(F(A))`` induced by ``F``.

**Constructors / Factory Signatures:**
- `def __init__(self, functor, obj) -> None`
- `def __call__(self, value)`

**Functor / Adjunction Methods:**
- `base_functor(self)`
- `morphism_image(self, morphism)`
- `object_image(self, arrow_object)`

#### `InducedHomFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L14`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L14)
- **Bases**: `Functor`

The functor ``Hom_C(A,B) -> Hom_D(F(A),F(B))`` induced by ``F``.

**Constructors / Factory Signatures:**
- `def __init__(self, functor, domain_object, codomain_object) -> None`
- `def __call__(self, value)`

**Functor / Adjunction Methods:**
- `base_functor(self)`
- `morphism_image(self, morphism)`
- `object_image(self, arrow_object)`

#### `InductionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L189`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L189)
- **Bases**: `Functor`

``Ind_H^G : R[H]-Mod_fp -> R[G]-Mod_fp``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, subgroup, supergroup=None) -> None`

**Functor / Adjunction Methods:**
- `identity_representative(self)`
- `inclusion(self)`
- `representatives(self)`
- `source_group_module(self, induced)`
- `subgroup(self)`
- `supergroup(self)`

#### `InductionRestrictionAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L463`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L463)
- **Bases**: `Adjunction`

``Ind_H^G ⊣ Res_H^G`` on represented finitely-presented group modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, subgroup, supergroup=None) -> None`

**Functor / Adjunction Methods:**
- `counit(self, group_module)`
- `unit(self, group_module)`

#### `InternalHomFromFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/tensor_hom.py#L54`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/tensor_hom.py#L54)
- **Bases**: `Functor`

The endofunctor ``Hom_R(M,-)`` represented by internal Hom modules.

**Constructors / Factory Signatures:**
- `def __init__(self, fixed_source) -> None`

**Functor / Adjunction Methods:**
- `fixed_source(self)`

#### `InvariantsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L79`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L79)
- **Bases**: `Functor`

``(-)^G`` on represented finitely-presented ``R[G]``-modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`

#### `InverseImagePowerSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L63`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L63)
- **Bases**: `Functor`

The contravariant power-set functor on the opposite of Set.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `opposite_morphism(self, morphism)`
- `opposite_sets(self)`

#### `InverseImageSubobjectFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/subobject_images.py#L39`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/subobject_images.py#L39)
- **Bases**: `Functor`

The monotone map ``f^{-1} : Sub(N) -> Sub(M)``.

**Constructors / Factory Signatures:**
- `def __init__(self, morphism) -> None`

**Functor / Adjunction Methods:**
- `morphism(self)`

#### `KernelArrowFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/linear_constructions.py#L91`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/linear_constructions.py#L91)
- **Bases**: `_ArrowConstructionFunctor`

The kernel functor from the finite-free module arrow category.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `ModuleLocalizationFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/module_localization.py#L16`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/module_localization.py#L16)
- **Bases**: `ScalarExtensionFunctor`

The functor ``S^{-1}R tensor_R - : Mod_R -> Mod_{S^{-1}R}``.

**Constructors / Factory Signatures:**
- `def __init__(self, localization_ring) -> None`

**Functor / Adjunction Methods:**
- `cokernel_comparison(self, morphism)`
  > Return ``S^{-1}coker(f) ~= coker(S^{-1}f)`` in represented regimes.
- `is_exact(self) -> bool`
  > Localization of modules is exact.
- `kernel_comparison(self, morphism)`
  > Return ``S^{-1}ker(f) ~= ker(S^{-1}f)``.
- `localization_ring(self)`
- `localization_submonoid(self)`
- `unit(self, module, *, localized=None)`
  > Return ``M -> Res_R(S^{-1}M)``, the localization unit.

#### `NaturalTransformation` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L219`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L219)
- **Bases**: `SageObject`

A natural transformation ``source => target`` given by its components.

**Constructors / Factory Signatures:**
- `def __init__(self, source: Functor, target: Functor, component) -> None`

**Functor / Adjunction Methods:**
- `component(self, obj)`
- `naturality_square(self, morphism)`
  > Return the two composites that naturality asserts are equal.
- `source(self) -> Functor`
- `target(self) -> Functor`

#### `OrderNumberFieldAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/orders_number_fields.py#L69`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/orders_number_fields.py#L69)
- **Bases**: `Adjunction`

``Frac ⊣ O``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `counit(self, field)`
- `unit(self, order)`

#### `QuadraticFreeFormAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L210`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L210)
- **Bases**: `_FreeFormAdjunction`

The divided-square quadratic-form classifier adjunction.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `QuadraticUnderlyingModuleFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L67`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L67)
- **Bases**: `_UnderlyingFormModuleFunctor`
**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `RestrictionCoinductionAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L503`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L503)
- **Bases**: `Adjunction`

``Res_H^G ⊣ Coind_H^G`` on represented finitely-presented group modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, subgroup, supergroup=None) -> None`

**Functor / Adjunction Methods:**
- `counit(self, group_module)`
- `unit(self, group_module)`

#### `RestrictionOfActingGroupFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L130`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L130)
- **Bases**: `Functor`

``Res_H^G : R[G]-Mod_fp -> R[H]-Mod_fp``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, subgroup, supergroup=None) -> None`

**Functor / Adjunction Methods:**
- `inclusion(self)`
- `original_group_module(self, restricted)`
- `subgroup(self)`
- `supergroup(self)`

#### `RestrictionOfScalarsFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/scalar_change.py#L93`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/scalar_change.py#L93)
- **Bases**: `Functor`

``Res_f : Mod_S -> Mod_R`` along ``f:R -> S``.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `ring_map(self)`

#### `RingOfIntegersFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/orders_number_fields.py#L46`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/orders_number_fields.py#L46)
- **Bases**: `Functor`

``K -> O_K : NumberFields -> Orders``.

**Constructors / Factory Signatures:**
- `def __init__(self) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`

#### `ScalarExtensionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/scalar_change.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/scalar_change.py#L22)
- **Bases**: `Functor`

``S tensor_R - : Mod_R -> Mod_S`` along ``f:R -> S``.

The mathematical functor is defined on every module.  The live computation
presently materializes the represented framed/free/presented cases for
which the module layer has an exact constructor.

**Constructors / Factory Signatures:**
- `def __init__(self, ring_map) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `ring_map(self)`

#### `SubobjectImageAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/subobject_images.py#L59`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/subobject_images.py#L59)
- **Bases**: `Adjunction`

The Galois connection ``f_* ⊣ f^{-1}`` on fixed-ambient subobjects.

**Constructors / Factory Signatures:**
- `def __init__(self, morphism) -> None`

**Functor / Adjunction Methods:**
- `counit(self, subobject)`
- `unit(self, subobject)`

#### `SymmetricAlgebraAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L216`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L216)
- **Bases**: `_ModuleAlgebraAdjunction`

The adjunction \(\operatorname{Sym}_R\dashv U\) for commutative algebras.


#### `SymmetricAlgebraFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L89`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L89)
- **Bases**: `_ModuleAlgebraFunctor`

The functor \(\operatorname{Sym}_R:\mathbf{Mod}_R\to\mathbf{CAlg}_R\).


#### `TautologicalFormFunctor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L151`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L151)
- **Bases**: `Functor`

Abstract base for a free form classified by a functorial square.


#### `TensorAlgebraAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L209`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L209)
- **Bases**: `_ModuleAlgebraAdjunction`

The adjunction \(T_R\dashv U:\mathbf{Mod}_R\leftrightarrows\mathbf{Alg}_R\).


#### `TensorAlgebraFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L81`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L81)
- **Bases**: `_ModuleAlgebraFunctor`

The functor \(T_R:\mathbf{Mod}_R\to\mathbf{Alg}_R\).


#### `TensorByFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/tensor_hom.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/tensor_hom.py#L22)
- **Bases**: `Functor`

The endofunctor ``- tensor_R M`` on finitely presented modules.

**Constructors / Factory Signatures:**
- `def __init__(self, fixed_module) -> None`

**Functor / Adjunction Methods:**
- `fixed_module(self)`

#### `TensorHomAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/tensor_hom.py#L86`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/tensor_hom.py#L86)
- **Bases**: `Adjunction`

The adjunction ``- tensor_R M ⊣ Hom_R(M,-)``.

**Constructors / Factory Signatures:**
- `def __init__(self, fixed_module) -> None`

**Functor / Adjunction Methods:**
- `counit(self, module)`
- `fixed_module(self)`
- `unit(self, module)`

#### `TrivialActionFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L44`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L44)
- **Bases**: `Functor`

``Triv_G`` on represented finitely-presented ``R``-modules.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `group(self)`

#### `TrivialGSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L35)
- **Bases**: `Functor`

``Triv_G : FinSet -> FinGSet_G``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `group(self)`
- `source_set(self, trivial_g_set_object)`

#### `TrivialInvariantsAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L153`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L153)
- **Bases**: `Adjunction`

``Triv_G ⊣ (-)^G``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, group_module)`
- `unit(self, module)`

#### `UnderlyingCofreeGSetAdjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L352`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L352)
- **Bases**: `Adjunction`

``U ⊣ Map(G,-)`` on represented finite ``G``-sets.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `counit(self, set_object)`
- `unit(self, g_set)`

#### `UnderlyingFiniteGSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L227`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L227)
- **Bases**: `Functor`

``U : FinGSet_G -> FinSet``.

**Constructors / Factory Signatures:**
- `def __init__(self, group) -> None`

**Functor / Adjunction Methods:**
- `chosen_preimage(self, image)`
- `group(self)`

#### `UnderlyingSetFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forgetful.py#L39`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forgetful.py#L39)
- **Bases**: `Functor`

``U : Mod_R -> Set``; a module is already a set object.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

#### `abelianization_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/abelianization.py#L162`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/abelianization.py#L162)
**Constructors / Factory Signatures:**
- `@cached_function` `def abelianization_adjunction() -> AbelianizationAdjunction`

#### `algebra_base_change_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L224`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_scalar_change.py#L224)
**Constructors / Factory Signatures:**
- `@cached_function` `def algebra_base_change_adjunction(ring_map) -> AlgebraBaseChangeAdjunction`

#### `algebra_underlying_module_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_modules.py#L303`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_modules.py#L303)
**Constructors / Factory Signatures:**
- `@cached_function` `def algebra_underlying_module_functor(base_ring, algebra_category=None) -> AlgebraUnderlyingModuleFunctor`

#### `alternating_algebra_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L224`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L224)
**Constructors / Factory Signatures:**
- `@cached_function` `def alternating_algebra_functor(base_ring) -> AlternatingAlgebraFunctor`

#### `base_change_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/scalar_change.py#L166`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/scalar_change.py#L166)
**Constructors / Factory Signatures:**
- `@cached_function` `def base_change_adjunction(ring_map) -> BaseChangeAdjunction`

#### `bilinear_free_form_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L237`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L237)
**Constructors / Factory Signatures:**
- `@cached_function` `def bilinear_free_form_adjunction(base_ring) -> BilinearFreeFormAdjunction`

#### `cardinality_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cardinality.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cardinality.py#L35)
**Constructors / Factory Signatures:**
- `@cached_function` `def cardinality_functor() -> CardinalityFunctor`

#### `cochain_underlying_graded_module_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cochain_complexes.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cochain_complexes.py#L26)
**Constructors / Factory Signatures:**
- `@cached_function` `def cochain_underlying_graded_module_functor(base_ring)`

#### `cohomology_algebra_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L158`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L158)
**Constructors / Factory Signatures:**
- `@cached_function` `def cohomology_algebra_functor(base_ring) -> CohomologyAlgebraFunctor`

#### `cohomology_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L148`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L148)
**Constructors / Factory Signatures:**
- `@cached_function` `def cohomology_functor(base_ring, degree) -> CohomologyFunctor`

#### `coinvariants_trivial_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L232`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L232)
**Constructors / Factory Signatures:**
- `@cached_function` `def coinvariants_trivial_adjunction(base_ring, group) -> CoinvariantsTrivialAdjunction`

#### `compose_adjunctions` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L332`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L332)
**Constructors / Factory Signatures:**
- `def compose_adjunctions(first: Adjunction, second: Adjunction) -> CompositeAdjunction`

#### `de_rham_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L186`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L186)
**Constructors / Factory Signatures:**
- `@cached_function` `def de_rham_adjunction(base_ring) -> DeRhamAdjunction`

#### `de_rham_cohomology_algebra_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L163`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L163)
**Constructors / Factory Signatures:**
- `@cached_function` `def de_rham_cohomology_algebra_functor(base_ring) -> DeRhamCohomologyAlgebraFunctor`

#### `de_rham_cohomology_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/cohomology.py#L153`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/cohomology.py#L153)
**Constructors / Factory Signatures:**
- `@cached_function` `def de_rham_cohomology_functor(base_ring, degree) -> DeRhamCohomologyFunctor`

#### `de_rham_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L176`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L176)
**Constructors / Factory Signatures:**
- `@cached_function` `def de_rham_functor(base_ring) -> DeRhamFunctor`

#### `degree_zero_dga_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/de_rham.py#L181`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/de_rham.py#L181)
**Constructors / Factory Signatures:**
- `@cached_function` `def degree_zero_dga_functor(base_ring) -> DegreeZeroDGAFunctor`

#### `divided_power_algebra_functor` `[FUNCTOR]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L229`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L229)
**Constructors / Factory Signatures:**
- `@cached_function` `def divided_power_algebra_functor(base_ring) -> DividedPowerAlgebraFunctor`

#### `exponential_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L135`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L135)
**Constructors / Factory Signatures:**
- `@cached_function` `def exponential_functor() -> ExponentialFunctor`

#### `finite_power_set_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L145`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L145)
**Constructors / Factory Signatures:**
- `@cached_function` `def finite_power_set_functor() -> FinitePowerSetFunctor`

#### `fixed_cardinality_subset_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L150`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L150)
**Constructors / Factory Signatures:**
- `@cached_function` `def fixed_cardinality_subset_functor(subset_cardinality) -> FixedCardinalitySubsetFunctor`

#### `free_forgetful_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forgetful.py#L86`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forgetful.py#L86)
**Constructors / Factory Signatures:**
- `@cached_function` `def free_forgetful_adjunction(base_ring) -> FreeForgetfulAdjunction`

#### `free_g_set_underlying_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L392`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L392)
**Constructors / Factory Signatures:**
- `@cached_function` `def free_g_set_underlying_adjunction(group) -> FreeGSetUnderlyingAdjunction`

#### `free_group_underlying_set_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_groups.py#L103`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_groups.py#L103)
**Constructors / Factory Signatures:**
- `@cached_function` `def free_group_underlying_set_adjunction() -> FreeGroupUnderlyingSetAdjunction`

#### `g_set_orbits_trivial_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L382`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L382)
**Constructors / Factory Signatures:**
- `@cached_function` `def g_set_orbits_trivial_adjunction(group) -> GSetOrbitsTrivialAdjunction`

#### `g_set_trivial_fixed_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L387`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L387)
**Constructors / Factory Signatures:**
- `@cached_function` `def g_set_trivial_fixed_adjunction(group) -> GSetTrivialFixedAdjunction`

#### `group_module_base_change_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_scalar_change.py#L266`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_scalar_change.py#L266)
**Constructors / Factory Signatures:**
- `@cached_function` `def group_module_base_change_adjunction(ring_map, group) -> GroupModuleBaseChangeAdjunction`

#### `induced_aut_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L157`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L157)
**Constructors / Factory Signatures:**
- `def induced_aut_functor(functor, obj) -> InducedAutFunctor`

#### `induced_end_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L153`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L153)
**Constructors / Factory Signatures:**
- `def induced_end_functor(functor, obj) -> InducedEndFunctor`

#### `induced_hom_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/hom_packets.py#L149`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/hom_packets.py#L149)
**Constructors / Factory Signatures:**
- `def induced_hom_functor(functor, domain_object, codomain_object) -> InducedHomFunctor`

#### `induction_restriction_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L551`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L551)
**Constructors / Factory Signatures:**
- `@cached_function` `def induction_restriction_adjunction(base_ring, subgroup, supergroup=None) -> InductionRestrictionAdjunction`

#### `inverse_image_power_set_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/set_constructions.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/set_constructions.py#L140)
**Constructors / Factory Signatures:**
- `@cached_function` `def inverse_image_power_set_functor() -> InverseImagePowerSetFunctor`

#### `module_localization_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/module_localization.py#L314`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/module_localization.py#L314)
**Constructors / Factory Signatures:**
- `@cached_function` `def module_localization_functor(localization_ring)`

#### `order_number_field_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/orders_number_fields.py#L103`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/orders_number_fields.py#L103)
**Constructors / Factory Signatures:**
- `@cached_function` `def order_number_field_adjunction() -> OrderNumberFieldAdjunction`

#### `quadratic_free_form_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_forms.py#L242`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_forms.py#L242)
**Constructors / Factory Signatures:**
- `@cached_function` `def quadratic_free_form_adjunction(base_ring) -> QuadraticFreeFormAdjunction`

#### `restriction_coinduction_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_induction.py#L558`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_induction.py#L558)
**Constructors / Factory Signatures:**
- `@cached_function` `def restriction_coinduction_adjunction(base_ring, subgroup, supergroup=None) -> RestrictionCoinductionAdjunction`

#### `subobject_image_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/subobject_images.py#L79`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/subobject_images.py#L79)
**Constructors / Factory Signatures:**
- `def subobject_image_adjunction(morphism) -> SubobjectImageAdjunction`

#### `symmetric_algebra_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L239`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L239)
**Constructors / Factory Signatures:**
- `@cached_function` `def symmetric_algebra_adjunction(base_ring) -> SymmetricAlgebraAdjunction`

#### `symmetric_algebra_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L156)
**Constructors / Factory Signatures:**
- `@cached_function` `def symmetric_algebra_functor(base_ring) -> SymmetricAlgebraFunctor`

#### `tensor_algebra_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L234`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L234)
**Constructors / Factory Signatures:**
- `@cached_function` `def tensor_algebra_adjunction(base_ring) -> TensorAlgebraAdjunction`

#### `tensor_algebra_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/free_algebras.py#L151`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/free_algebras.py#L151)
**Constructors / Factory Signatures:**
- `@cached_function` `def tensor_algebra_functor(base_ring) -> TensorAlgebraFunctor`

#### `tensor_hom_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/tensor_hom.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/tensor_hom.py#L140)
**Constructors / Factory Signatures:**
- `@cached_function` `def tensor_hom_adjunction(fixed_module) -> TensorHomAdjunction`

#### `trivial_invariants_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/group_actions.py#L227`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/group_actions.py#L227)
**Constructors / Factory Signatures:**
- `@cached_function` `def trivial_invariants_adjunction(base_ring, group) -> TrivialInvariantsAdjunction`

#### `underlying_cofree_g_set_adjunction` `[ADJUNCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/g_sets.py#L397`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/g_sets.py#L397)
**Constructors / Factory Signatures:**
- `@cached_function` `def underlying_cofree_g_set_adjunction(group) -> UnderlyingCofreeGSetAdjunction`

### ↗ Morphisms & Hom-Sets

#### `UnderlyingAlgebraModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/algebra_modules.py#L226`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/algebra_modules.py#L226)
- **Bases**: `ModuleMorphism`

An algebra morphism read as its underlying linear map.

- **Constructor**: `def __init__(self, parent, algebra_morphism) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `algebra_morphism(self)`

### 📦 Mathematical Objects & Parents

#### `BiproductBifunctor` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/linear_constructions.py#L65`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/linear_constructions.py#L65)
- **Bases**: `Bifunctor`

The direct-sum/biproduct bifunctor on finitely presented modules.

- **Constructor**: `def __init__(self, base_ring) -> None`

#### `LocalizationCokernelComparison` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/module_localization.py#L172`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/module_localization.py#L172)
- **Bases**: `SageObject`

The canonical right-exactness comparison for module localization.

- **Constructor**: `def __init__(self, functor, morphism) -> None`

**Public Methods:**
- `cokernel_of_localized_morphism(self)`
- `forward(self)`
- `functor(self)`
- `inverse(self)`
- `localized_cokernel(self)`
- `localized_morphism(self)`
- `morphism(self)`

#### `LocalizationKernelComparison` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functors/module_localization.py#L260`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/module_localization.py#L260)
- **Bases**: `SageObject`

The canonical left-exactness comparison for module localization.

- **Constructor**: `def __init__(self, functor, morphism) -> None`

**Public Methods:**
- `forward(self)`
- `functor(self)`
- `inverse(self)`
- `kernel_of_localized_morphism(self)`
- `localized_kernel(self)`
- `localized_morphism(self)`
- `morphism(self)`

#### `OrthogonalDirectSumBifunctor` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functors/linear_constructions.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/linear_constructions.py#L144)
- **Bases**: `Bifunctor`

The orthogonal-direct-sum bifunctor on finite-rank lattices.

- **Constructor**: `def __init__(self, base_ring) -> None`

### 🛠 Helper Functions & Constructors

#### `category_inclusion` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def category_inclusion(subcategory, supercategory) -> CategoryInclusionFunctor`
- **Source**: [`src/dzack_research/preamble/categories/functors/core.py#L178`](file:///home/dzack/research/src/dzack_research/preamble/categories/functors/core.py#L178)

Return the canonical functor attached to ``subcategory <= supercategory``.



---

<a id="subsystem-lattices"></a>
## Lattices, Quadratic Forms & Invariants

> Free modules with quadratic forms, Genus, Definite/Root/Rational lattices, Isometries, Embeddings, Orbits, and Diagrams.

### 🏛 Categories & Subcategories

#### `CoxeterDiagrams` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/coxeter_diagrams.py#L37`](file:///home/dzack/research/src/dzack_research/preamble/categories/coxeter_diagrams.py#L37)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

**Category Instance Methods:**
- `from_cartan_type(self, cartan_type, names=None, *, rooted=False, positions=None)`
- `from_coxeter_matrix(self, coxeter_matrix, names=None, positions=None)`
- `from_roots(self, roots, names=None, index_set=None, positions=None)`
- `super_categories(self)`

#### `EvenLattices` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2429`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2429)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Lattices(self.base_ring())]`

Lattices satisfying ``b(x,x) in 2R`` for every lattice vector ``x``.


**Category Instance Methods:**
- `super_categories(self)`

#### `FiniteRankLattices` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2396`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2396)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Lattices(self.base_ring()), FinitelyGeneratedFreeModules(self.base_ring())]`

Lattices whose underlying free module has finite rank.


**ParentMethods (Methods on Category Objects):**
- `is_finite_rank(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `LatticeHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L52`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L52)
- **Bases**: `HomCategoryConstruction`

The strict form-preserving Hom categories of lattices.


**Category Instance Methods:**
- `fixed_category_class(self)`

#### `LatticeIsoCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L72`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L72)
- **Bases**: `IsoCategoryConstruction`

The isometries of lattices.


**Category Instance Methods:**
- `fixed_category_class(self)`

#### `LatticeMonoCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L61`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L61)
- **Bases**: `MonoCategoryConstruction`

The form-preserving monomorphisms of lattices.


**Category Instance Methods:**
- `fixed_category_class(self)`

#### `Lattices` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L423`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L423)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FramedFreeModules(self.base_ring()), SymmetricBilinearFormModules(self.base_ring())]`

The category of lattices over a base ring, and the constructor for
its objects.

Sage's ``IntegralLattice`` factory constructs finite nondegenerate
integral forms but does not provide the mathematical category used here.
``Lattices(R)`` owns the broader category of free `R`-modules with an
`R`-valued symmetric form; finite rank and nondegeneracy are refinements,
not hidden constructor assumptions.      Named descriptors (``U``, a finite
simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.

Sage's meet/join lattices are :class:`LatticePosets`, a different
mathematical object.

EXAMPLES::

    sage: from dzack_research.preamble.categories.lattices import Lattices
    sage: Lattices(ZZ)
    Lattices(ZZ)
    sage: Lattices(ZZ).super_categories()
    [Category of framed free modules]

    sage: C = Lattices(ZZ)
    sage: L = C("U")
    sage: L
    Integral lattice of rank 2 and signature (1, 1)
    sage: L in C
    True
    sage: C("A2")
    Integral lattice of rank 2 and signature (0, 2)
    sage: latex(L)
    \begin{gathered}
    L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
    L = U \\
    G_L = \left(\begin{array}{rr}
    \cdot & 1 \\
    1 & \cdot
    \end{array}\right) \\
    \end{gathered}
    sage: latex(Lattices(ZZ))
    \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}

**Category Constructor:**
- `@staticmethod` `Lattices(cls, *args)`
  > Return the category of lattices over a ring.

**Object Constructor (Calling Category on Data):**
- `@overload` `Lattices(...)(self, data: str | Sequence[Sequence[object]], *args: object, **options: object) -> 'FiniteRankLattices.ParentMethods'`
- `@overload` `Lattices(...)(self, data: object, *args: object, **options: object) -> 'Lattices.ParentMethods'`
- `Lattices(...)(self, data: object, *args: object, **options: object) -> 'Lattices.ParentMethods'`
  > Return the lattice that ``data`` presents; a lattice in this category is returned as is.
- `Lattices(...)(self, data: object, basis: None=None, names: str | Sequence[str] | None=None, form: Tensor | None=None, module_generators: Sequence[Hashable] | Parent | None=None) -> 'Lattices.ParentMethods'`
  > Construct a lattice in this category.

**ParentMethods (Methods on Category Objects):**
- `Aut(self)`
  > Return ``Isom(L,L)``, the orthogonal automorphism homset.
- `BKZ(self, block_size=20)`
  > Return the same formed lattice in a BKZ-reduced framing.
- `Emb(self, codomain)`
  > Return the set of form-preserving embeddings into ``codomain``.
- `HKZ(self)`
  > Return the full-block BKZ (HKZ) reframing.
- `Hom(self, codomain, category=None)`
- `Isom(self, codomain)`
  > Return the set of isometries to ``codomain``.
- `LLL(self)`
  > Return the same formed lattice in an LLL-reduced framing.
- `b(self, left, right)`
  > Return the bilinear pairing \(b(v,w)\).
- `babai(self, target)`
- `bilinear_orthogonal_group(self)`
  > Return ``O(L,b)``; explicit name for the lattice pairing.
- `biproduct_factors(self)`
  > Return the two actual factors when this lattice was built by ``+``.
- `bkz_reduction(self, block_size=20)`
- `center_density(self)`
- `closest_vector(self, target)`
- `contact_polytope(self)`
- `correlation(self)`
- `@cached_method` `correlation_morphism(self)`
  > Return ``L -> L^#``, ``v |-> b(v,-)``, whose selected-basis matrix is ``G``.
- `covering_radius(self)`
- `@cached_method` `decomposition(self)`
  > Return the represented direct-sum decomposition, if present.
- `decomposition_names(self)`
  > Return registered names of the recursively represented factors.
- `definite_complement_extensions(self, left, right)`
  > Return all isometries ``g`` with ``g(left)=right`` in the definite-complement regime.
- `delta(self)`
  > Return Nikulin's ``delta`` for an even 2-elementary lattice.
- `determinant(self)`
  > Return the determinant of a finite-rank lattice form.
- `discriminant(self)`
  > Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$, the signed determinant.
- `@cached_method` `discriminant_bilinear_form(self)`
  > Return ``A_L`` with its descended ``K/R``-valued bilinear form.
- `discriminant_class(self, dual_lattice_element)`
  > Project an element of ``L^#`` to its discriminant class.
- `discriminant_group(self)`
  > Return the ``ZZ`` discriminant group with every form supported by ``L``.
- `@cached_method` `discriminant_image(self)`
  > Return the computed image of ``rho_L`` when ``O(L)`` generators are known.
- `discriminant_length(self)`
  > Return the minimal number of generators of ``A_L`` over ``ZZ``.
- `@cached_method` `discriminant_module(self)`
  > Return ``A_L = coker(L -> L^#)`` with the selected dual-basis presentation.
- `discriminant_projection(self)`
  > Return the quotient morphism ``L^# -> A_L``.
- `discriminant_quadratic_form(self)`
  > Return ``A_L`` with its ``K/2R``-valued quadratic form when ``L`` is even.
- `@cached_method` `discriminant_representation(self)`
  > Return ``rho_L:O(L)->O(A_L)`` by functoriality of discriminants.
- `@cached_method` `discriminant_representation_is_surjective(self) -> bool`
  > Return whether the computed discriminant image equals ``O(A_L)``.
- `div(self, element)`
  > Return the divisibility ``gcd{b(element,x): x in L}`` over ``ZZ``.
- `divided_discriminant_class(self, element)`
  > Return the class represented by ``correlation(element)/div(element)``.
- `dual_basis(self)`
  > Return the selected basis of ``L^#`` dual to the selected basis of ``L``.
- `@cached_method` `dual_lattice(self)`
  > Return the metric dual ``L^#`` on the algebraic dual module.
- `@cached_method` `dual_module(self)`
  > Return the algebraic dual module ``Hom_R(L,R)`` in the dual framing.
- `embed_in_even_unimodular(self, positive, negative)`
  > Return one primitive embedding into an even unimodular lattice.
- `embeds_in_even_unimodular(self, positive, negative) -> bool`
  > Decide primitive embeddability into an even unimodular ``II_{p,q}``.
- `@cached_method` `equip_form_morphism(self)`
- `even_overlattice_inclusions(self)`
  > Return all even overlattice inclusions ``L -> L'``.
- `@cached_method` `forget_form_morphism(self)`
- `@cached_method` `form(self)`
  > Return the existing lattice pairing as a bilinear-form morphism.
- `gaussian_heuristic(self, *, exact_form=False)`
- `@cached_method` `genus(self)`
  > Return the genus from signature and discriminant quadratic form.
- `glue_map(self, first, second)`
  > Return the Nikulin glue anti-isometry for a primitive extension.
- `gluing_route_discriminant_classes(self, left, right)`
  > Return admissible ``O(A_L)`` classes from the primitive-extension gluing route.
- `gram_tensor(self)`
  > Return the Gram tensor of the form: type $(0,2)$, not a matrix.
- `hadamard_ratio(self)`
- `hermite_invariant(self)`
- `hkz_reduction(self)`
- `identity_morphism(self)`
  > Return ``id_L`` in the lattice endomorphism homset.
- `indecomposable_name(self)`
- `is_decomposable(self)`
- `is_definite(self) -> bool`
- `is_even(self) -> bool`
  > Return whether ``b(x,x)`` lies in ``2R`` for every lattice vector.
- `is_finite_rank(self) -> bool`
  > Return whether this lattice is free of finite rank.
- `is_isometric(self, other)`
  > Return whether ``self`` and ``other`` are isometric when decidable.
- `is_locally_isometric(self, other, prime) -> bool`
  > Return whether ``self`` and ``other`` are isometric over ``ZZ_p``.
- `is_negative_definite(self) -> bool`
- `is_nondegenerate(self) -> bool`
  > Return whether the correlation map has zero radical.
- `is_p_elementary(self, prime) -> bool`
  > Return whether ``A_L`` is an elementary abelian ``prime``-group.
- `is_positive_definite(self) -> bool`
- `is_similar(self, other, scale)`
  > Return whether a similarity of the stated scale exists.
- `is_unimodular(self) -> bool`
  > Return whether the correlation ``L -> L^#`` is an isomorphism.
- `isotropic_flag(self, *basis)`
- `isotropic_flag_orbit_representatives(self, rank=2)`
- `isotropic_line_orbit_representatives(self)`
- `isotropic_plane_orbit_representatives(self)`
- `kissing_number(self)`
- `lattice_category(self)`
  > Return the base-ring lattice category owning this object.
- `level(self)`
  > Return the level of a finite nondegenerate integral lattice.
- `lll_reduction(self)`
- `local_modification(self, prime, *discriminant_classes)`
  > Return the isotropic ``p``-primary overlattice modification.
- `metric_dual(self)`
  > Return the metric dual ``L^#``; explicit synonym for ``dual_lattice``.
- `minimum(self)`
- `module_generating_set(self)`
  > Return the labels of the distinguished free-module framing.
- `module_generator(self, index)`
  > Return the module generator indexed by ``index``.
- `@cached_method` `module_generators(self)`
- `orthogonal_group(self)`
  > Return ``O(L,b)=Aut(L,b)`` as the owned isometry group.
- `overlattice(self, *discriminant_classes)`
  > Return the inclusion ``L -> L'`` generated by discriminant classes.
- `packing_density(self)`
- `packing_radius(self)`
- `positive_cone_subgroup(self)`
  > Return the positive-cone-preserving subgroup in signature ``(1,n)``.
- `primitive_isotropic_subobject(self, *basis)`
- `q(self, vector)`
  > Return the quadratic form \(q(v)=b(v,v)\).
- `quadratic_orthogonal_group(self)`
  > Return ``O(L,q)`` for ``q(x)=b(x,x)``.
- `radical(self)`
  > Return ``rad(L)=id_L(L)^perp`` as a subobject of ``L``.
- `radical_quotient(self)`
  > Return the nondegenerate quotient ``L/rad(L)``.
- `rank(self)`
  > Return the rank of this lattice as a free module.
- `reflection(self, root)`
  > Return the integral orthogonal reflection in ``root``.
- `root_sublattice(self)`
- `roots(self)`
- `roots_of_square(self, square)`
- `shortest_vectors(self)`
- `signature_pair(self)`
  > Return $(p,q)$: the positive and negative indices of inertia.
- `similarity(self, scale, images=None, codomain=None)`
  > Return an explicit similarity as an isometry from ``L(scale)``.
- `similarity_homset(self, other, scale)`
  > Return similarities of scale ``scale`` as ``Isom(L(scale),other)``.
- `@cached_method` `special_orthogonal_group(self)`
  > Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup.
- `spinor_kernel_subgroup(self)`
  > Return the kernel of the real spinor-norm sign on ``O(L)``.
- `stable_complement_root_reflections(self, element)`
  > Return stable reflections in root-orbit representatives of ``element^perp``.
- `@cached_method` `stable_orthogonal_group(self)`
  > Return ``ker(rho_L)`` as the stable orthogonal subgroup.
- `subobject_on(self, module_generating_set)`
  > Return the span with the restricted lattice form.
- `successive_minima(self)`
- `summands(self)`
- `theta_series(self, precision=20, variable='q')`
- `twist(self, scalar)`
  > Keep the module and rescale its form by ``scalar``.
- `two_elementary_invariants(self)`
  > Return Nikulin's ``(r,a,delta)`` for an even 2-elementary lattice.
- `unformed_module(self)`
  > Read this same parent at its weaker module level.
- `value_module(self)`
- `vector_primitive_extension(self, element)`
  > Return the primitive-extension/gluing datum cut out by ``element``.
- `vectors_of_square(self, square)`
- `vectors_of_square_and_divisibility(self, square, divisibility)`
- `voronoi_cell(self, bound=None)`
- `voronoi_relevant_vectors(self)`

**ElementMethods (Methods on Category Elements):**
- `b(self, other)`
  > Return \(b(v,w)\) by contracting the Gram tensor on \(v\) and \(w\).
- `div(self)`
  > Return the positive integer generator of ``b(v,L)`` over ``ZZ``.
- `divided_discriminant_class(self)`
- `divisibility_ideal(self)`
- `is_root(self) -> bool`
  > Return whether the orthogonal reflection in this vector is integral.
- `monomial_coefficients(self)`
- `norm(self)`
  > Return the form norm ``b(v,v)``.
- `q(self)`
  > Return \(q(v)=b(v,v)\).
- `to_list(self)`
  > Return the coordinates of this element as a Python list.
- `to_tuple(self)`
  > Return the coordinates of this element as a Python tuple.
- `to_vector(self)`
  > Return the coordinates of this element as a vector tensor of type $(1,0)$.

**Category Instance Methods:**
- `colimit(self, stage)`
  > Return \(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).
- `@cached_method` `super_categories(self)`
  > Return the immediate super categories of ``self``.

#### `NondegenerateLattices` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2418`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2418)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Lattices(self.base_ring())]`

Lattices whose correlation map has zero kernel.


**Category Instance Methods:**
- `super_categories(self)`

#### `RationalLattices` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rational_lattices.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/rational_lattices.py#L26)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyGeneratedFreeFormModules(self.base_ring()), SymmetricBilinearFormModules(self.base_ring())]`

Nondegenerate finite free ``R``-modules with ``Frac(R)``-valued form.


**ParentMethods (Methods on Category Objects):**
- `determinant(self)`
- `fraction_field(self)`
- `is_nondegenerate(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `RootLattices` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2440`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2440)
- **Bases**: `Category`
- **Super Categories**: `[FiniteRankLattices(integers), NondegenerateLattices(integers), EvenLattices(integers)]`

Negative-definite ADE root lattices with a chosen simple-root framing.


**ParentMethods (Methods on Category Objects):**
- `cartan_type(self)`
- `coxeter_number(self)`
- `fundamental_weights(self)`
  > Return the weights dual to the simple coroots.
- `highest_root(self)`
  > Return the highest root in the selected simple-root framing.
- `simple_reflections(self)`
- `simple_roots(self)`
  > Return the selected framing, which is the chosen simple system.

**ElementMethods (Methods on Category Elements):**
- `coroot(self)`
  > Return ``alpha^vee = 2*b(alpha,-)/b(alpha,alpha)`` in ``L^#``.
- `height(self)`
- `is_negative_root(self) -> bool`
- `is_positive_root(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `LatticeEmbedding` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L48`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L48)
- **Bases**: `LatticeMorphism`

A form-preserving monomorphism of lattices.

- **Constructor**: `def __init__(self, parent, images, *, verify_injective=True) -> None`

**Public Methods:**
- `discriminant_inclusion(self)`
  > Return ``A_S -> A_L`` for an orthogonal direct-summand embedding.
- `is_injective(self) -> bool`
- `isotropic_reduction(self)`
  > Return ``S^perp/S`` for this isotropic embedding ``S -> L``.

#### `LatticeEmbeddingHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L561`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L561)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `an_element(self)`
- `even_overlattice_inclusions(self)`
  > Return the finite even-overlattice sweep used by Nikulin existence.
- `is_empty(self)`
- `super_categories(self)`

#### `LatticeHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L519`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L519)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `elementwise(self, function)`
- `identity(self)`

#### `LatticeIsometry` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L241`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L241)
- **Bases**: `LatticeEmbedding`

An invertible lattice morphism.

- **Constructor**: `def __init__(self, parent, images) -> None`

**Public Methods:**
- `@cached_method` `centralizer_discriminant_image(self)`
  > Return ``rho_L(Z_{O(L)}(self)) <= O(A_L)`` when OSCAR computes it.
- `cyclic_subgroup(self)`
  > Return the literal subgroup ``<self> <= O(L)``.
- `determinant(self)`
  > Return the determinant of this automorphism/isometry tensor.
- `@cached_method` `discriminant_isometry(self)`
  > Return the induced isometry ``Disc(self): A_L -> A_M``.
- `@cached_method` `discriminant_morphism(self)`
  > Return ``Disc(self)`` parented by ``O(A_L)`` for an automorphism.
- `@cached_method` `formed_coinvariants(self)`
  > Return ``(L^self)^perp`` as a formed subobject of ``L``.
- `@cached_method` `invariant_lattice(self)`
  > Return ``ker(self-id)`` as a formed subobject of the lattice.
- `inverse(self)`
  > Return the inverse isometry.
- `is_surjective(self) -> bool`
- `preserves_positive_cone(self) -> bool`
  > Return whether an isometry preserves a component of the positive cone.
- `@cached_method` `real_spinor_norm_sign(self)`
  > Return the sign of the real spinor norm in Dawes' convention.

#### `LatticeIsometryHomset` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L722`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L722)
- **Bases**: `LatticeEmbeddingHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `act(self, automorphism, isometry)`
  > Postcompose an isometry by a codomain automorphism.
- `acting_group(self)`
  > Return ``O(codomain)`` acting by postcomposition on this homset.
- `an_element(self)`
  > Return an explicit isometry when the exact decision exhibits one.
- `compose(self, second, first)`
  > Return ``second ∘ first`` as an isometry.
- `discriminant_image(self)`
  > Return the subgroup of ``O(A_L)`` generated by the known ``O(L)`` generators.
- `discriminant_preimage(self, subgroup)`
  > Return ``rho_L^{-1}(subgroup)`` as a predicate subgroup of ``O(L)``.
- `@cached_method` `group_generators(self)`
  > Return exact generators of ``O(L)`` when the backend computes them.
- `identity(self)`
- `is_empty(self)`
  > Decide emptiness through exact obstructions and proved classifiers.
- `isotropic_equivalence_witness(self, left, right, *, flag=False)`
- `isotropic_orbit_representatives(self, rank, *, flag=False)`
- `isotropic_stabilizer_generators(self, obj, *, flag=False)`
- `number_of_group_generators(self)`
- `one(self)`
- `super_categories(self)`
- `transporter(self, source, target)`
  > Return the unique ``g in O(M)`` with ``g ∘ source = target``.
- `vector_equivalence_witness(self, left, right)`
  > Return ``g in O(L)`` with ``g(left)=right``, or ``None``.
- `vector_orbit_representatives(self, square)`
  > Return one representative of each ``O(L)``-orbit of square ``square``.
- `vector_stabilizer_generators(self, element)`
  > Return exact generators of ``Stab_{O(L)}(element)`` when finite.
- `vectors_are_equivalent(self, left, right) -> bool`
  > Return whether two vectors lie in the same ``O(L)``-orbit.

#### `LatticeMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L25`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L25)
- **Bases**: `ModuleMorphism`

A module morphism preserving the lattice form.

- **Constructor**: `def __init__(self, parent, images, *, elementwise=False) -> None`

### 📦 Mathematical Objects & Parents

#### `CoxeterDiagram` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/coxeter_diagrams.py#L92`](file:///home/dzack/research/src/dzack_research/preamble/categories/coxeter_diagrams.py#L92)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, coxeter_matrix, names=None, roots=None, root_gram=None, positions=None) -> None`

**Public Methods:**
- `cardinality(self)`
- `connected_components(self)`
- `coxeter_entry(self, left, right)`
- `coxeter_matrix(self)`
- `elliptic_subdiagrams(self, *, connected=False)`
- `graph(self)`
- `index_set(self)`
- `induced_subdiagram(self, vertices)`
- `is_connected(self) -> bool`
- `is_elliptic(self) -> bool`
- `is_hyperbolic(self) -> bool`
- `is_parabolic(self) -> bool`
- `is_rooted(self) -> bool`
- `parabolic_subdiagrams(self, *, connected=False)`
- `preferred_positions(self)`
  > Return stored presentation coordinates, or a computed graph layout.
- `root_gram_tensor(self)`
- `roots(self)`
- `schlafli_tensor(self)`
  > Return the normalized reflection Gram tensor ``S_ii=1``.
- `signature_pair(self)`
- `vertex_names(self)`

#### `Genus` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L242`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L242)

The genus determined by signature and discriminant quadratic form.

- **Constructor**: `def __init__(self, signature_pair, discriminant_quadratic_form) -> None`

**Public Methods:**
- `class_number(self)`
- `determinant(self)`
  > Return the determinant of a representative of this genus.
- `discriminant_form(self)`
  > Return the finite discriminant quadratic form component.
- `excess(self, prime)`
- `exists(self) -> bool`
  > Return whether the signature/discriminant-form datum is realizable.
- `level(self, prime)`
- `local_symbol(self, prime)`
  > Return the owned exact ``ZZ_p`` genus symbol at ``prime``.
- `mass(self)`
  > Return the Smith--Minkowski--Siegel mass for a definite genus.
- `representative(self)`
  > Return one owned integral lattice representing this genus.
- `representatives(self)`
  > Return the owned representatives enumerated by the exact backend.
- `signature_pair(self)`
  > Return the archimedean signature component ``(t_+,t_-)``.

#### `IsotropicFlag` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L31`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L31)

A primitive totally isotropic flag, recorded by its nested lattice subobjects.

- **Constructor**: `def __init__(self, lattice, basis) -> None`

**Public Methods:**
- `basis(self)`
- `lattice(self)`
- `rank(self)`
- `terms(self)`
- `top(self)`

#### `Lattice` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L211`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L211)
- **Bases**: `Parent`, `IndexedGenerators`

A lattice: a free module with a form, as a parent in :class:`Lattices`.

The internal module is an owned free module on a generating
set stored here.  With no generating set given, that set is the
formal symbols \(e_i\in\mathrm{SR}\).  An element prints as a linear
combination of those generators, never as a coordinate tuple.

- **Constructor**: `def __init__(self, module, gram, category: Category, sage_lattice, names=None) -> None`
- **Constructor**: `def _element_constructor_(self, x)`

**Public Methods:**
- `an_element(self)`
  > Return a represented lattice element from the underlying module.
- `zero(self)`
  > Return the additive identity of the underlying free module.

#### `LatticeReduction` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L55`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L55)

#### `LocalGenusSymbol` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L170`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L170)

The Conway--Sloane Jordan-block invariants at one finite prime.

For odd ``p`` each block is ``(m,n,d)``.  At ``p=2`` each block is
``(m,n,s,d,o)``.  These integer tuples are the mathematical local-symbol
data; Sage's ``Genus_Symbol_p_adic_ring`` is reconstructed privately when
one of its exact algorithms is used.

- **Constructor**: `def __init__(self, prime, jordan_blocks) -> None`

**Public Methods:**
- `excess(self)`
- `jordan_blocks(self)`
- `level(self)`
- `norm(self)`
- `number_of_blocks(self)`
- `prime(self)`

#### `OrthogonalCharacterQuotient` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/orthogonal_quotients.py#L4`](file:///home/dzack/research/src/dzack_research/preamble/categories/orthogonal_quotients.py#L4)

The finite image of ``O(L)`` under the characters defining a subgroup.

Components are the discriminant representation and optional determinant /
real-spinor signs.  The finite image is generated from live ``O(L)``
generators, retaining one live lattice isometry above every quotient
element.  This avoids introducing a parallel matrix-group model of the
infinite arithmetic group.

- **Constructor**: `def __init__(self, subgroup) -> None`

**Public Methods:**
- `image(self, isometry)`
- `image_keys(self)`
- `splitting_isometries(self, stabilizer_generators)`
  > Return one lift per ``Stab\image(O(L))/Gamma`` double coset.
- `stabilizer_image_keys(self, stabilizer_generators)`
- `subgroup_image_keys(self)`
- `witness_meets_subgroup(self, witness, stabilizer_generators) -> bool`

#### `VectorPrimitiveExtension` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/vector_orbits.py#L6`](file:///home/dzack/research/src/dzack_research/preamble/categories/vector_orbits.py#L6)

Nikulin's primitive extension cut out by one anisotropic primitive vector.

For ``w in L`` this records

``M = Zw ⊥ w^perp -> L``

together with its finite index, the two discriminant inclusions into
``A_M``, the gluing subgroup ``H=L/M <= A_M``, and representatives of
``A_L`` in ``H^perp``.

- **Constructor**: `def __init__(self, lattice, element) -> None`

**Public Methods:**
- `class_of_representative(self, element)`
  > Return the class of ``A_L`` represented by an element of ``H^perp``.
- `complement_is_definite(self) -> bool`
  > Return whether the orthogonal complement is definite.
- `representative_of(self, discriminant_class)`
  > Return the selected representative in ``A_M`` of a class of ``A_L``.

### 📚 Catalogues & Named Tables

#### `register_indecomposable` `[REGISTRY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L92`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L92)

Register an indecomposable live lattice by exact Gram equality.


#### `register_indecomposable_gram` `[REGISTRY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L87)

Register an exact Gram matrix under its indecomposable display name.


### 🛠 Helper Functions & Constructors

#### `babai` `[FUNCTION]` `[Internal]`

- **Signature**: `def babai(lattice, target)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L336`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L336)

Return Babai's LLL nearest-plane approximation.


#### `bkz_reduction` `[FUNCTION]` `[Internal]`

- **Signature**: `def bkz_reduction(lattice, block_size=20)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L115`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L115)

Return a BKZ-reframed copy with its exact integral isometry witness.


#### `center_density` `[FUNCTION]` `[Internal]`

- **Signature**: `def center_density(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L593`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L593)

#### `closest_vector` `[FUNCTION]` `[Internal]`

- **Signature**: `def closest_vector(lattice, target)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L286`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L286)

Return the exact closest lattice vector to a rational target.


#### `colimit_lattice` `[FUNCTION]` `[Internal]`

- **Signature**: `def colimit_lattice(stage, *, category)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L836`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L836)

\(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

``stage(n)`` is a rank-\(n\) lattice in ``category``.  The colimit
module is the free module on \(\mathbb N\).


#### `contact_polytope` `[FUNCTION]` `[Internal]`

- **Signature**: `def contact_polytope(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L534`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L534)

#### `covering_radius` `[FUNCTION]` `[Internal]`

- **Signature**: `def covering_radius(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L563`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L563)

#### `definite_complement_extensions` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def definite_complement_extensions(lattice, left, right)`
- **Source**: [`src/dzack_research/preamble/categories/vector_orbits.py#L209`](file:///home/dzack/research/src/dzack_research/preamble/categories/vector_orbits.py#L209)

Return every ``g in O(L)`` carrying ``left`` to ``right`` when complements are definite.

This is Dawes' definite-complement route.  An isometry of the two
complements, together with ``left -> right``, defines an isometry
``C:M_left -> M_right`` on the orthogonal sums.  With the finite-index
inclusions ``A_i:M_i -> L``, its rational ambient extension is

``A_right * C * A_left^{-1}``.

Exactly the rational ambient morphisms preserving the integral lattice
belong to ``O(L)``.  Since the complement isometry homset is a finite
torsor in this regime, the returned tuple is exhaustive.


#### `diagonal_gram` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def diagonal_gram(module, exceptions, default=1)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L785`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L785)

The diagonal type-$(0,2)$ tensor on ``module``.

``exceptions`` is the indexed family of diagonal values that differ
from ``default``.  The Lorentz form on \(R^{\mathbb N}\) is
``diagonal_gram(R^NN, {0: -1}, default=1)``.

EXAMPLES::

    sage: from dzack_research.preamble.categories.lattices import Lattices, diagonal_gram
    sage: G = diagonal_gram(ZZ^NN, {0: -1})
    sage: G
    [-1] ⊕ I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
    sage: latex(G)
    [-1]\oplus I_{\infty}
    sage: G.parent()
    (ZZ^NN ⊗ ZZ^NN)*
    sage: Lattices(ZZ)(G)
    Integral lattice of rank +Infinity and signature (+Infinity, 1)


#### `discriminant_of_gram` `[FUNCTION]` `[Internal]`

- **Signature**: `def discriminant_of_gram(gram: Tensor)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L918`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L918)

Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$.


#### `generator_pairings` `[FUNCTION]` `[Internal]`

- **Signature**: `def generator_pairings(lattice, element)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L872`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L872)

The finite family \(i\mapsto b(e_i,v)\) of nonzero pairings against generators.


#### `gluing_route_discriminant_classes` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def gluing_route_discriminant_classes(lattice, left, right)`
- **Source**: [`src/dzack_research/preamble/categories/vector_orbits.py#L351`](file:///home/dzack/research/src/dzack_research/preamble/categories/vector_orbits.py#L351)

Return the finite discriminant classes compatible with ``left -> right``.

For the primitive extensions ``M_i=Zw_i perp w_i^perp`` this enumerates
the full finite-form isometry torsors of the line and complement factors,
retains exactly the assembled maps ``A_{M_1}->A_{M_2}`` carrying
``H_1=L/M_1`` onto ``H_2=L/M_2``, and descends them to
``H_1^perp/H_1 -> H_2^perp/H_2 = A_L``.

These are the admissible classes in ``O(A_L)``.  Lifting such a class to
an actual element of ``O(L)`` is deliberately separate: it is governed by
the image of the discriminant representation and is not assumed here.


#### `hadamard_ratio` `[FUNCTION]` `[Internal]`

- **Signature**: `def hadamard_ratio(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L512`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L512)

#### `hermite_invariant` `[FUNCTION]` `[Internal]`

- **Signature**: `def hermite_invariant(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L634`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L634)

#### `hkz_reduction` `[FUNCTION]` `[Internal]`

- **Signature**: `def hkz_reduction(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L154`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L154)

#### `indecomposable_name` `[FUNCTION]` `[Internal]`

- **Signature**: `def indecomposable_name(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L99`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L99)

Return the registered exact or scalar-twist name, if one exists.


#### `isotropic_equivalence_witness` `[FUNCTION]` `[Internal]`

- **Signature**: `def isotropic_equivalence_witness(orthogonal_group, left, right, *, flag=False)`
- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L149`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L149)

Return an isometry carrying one primitive isotropic subobject/flag to another.


#### `isotropic_orbit_representatives` `[FUNCTION]` `[Internal]`

- **Signature**: `def isotropic_orbit_representatives(orthogonal_group, rank, *, flag=False)`
- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L116`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L116)

Return full-``O(L)`` orbit representatives of primitive isotropic subobjects/flags.


#### `isotropic_stabilizer_generators` `[FUNCTION]` `[Internal]`

- **Signature**: `def isotropic_stabilizer_generators(orthogonal_group, obj, *, flag=False)`
- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L179`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L179)

Return generators of the full-orthogonal-group stabilizer of an isotropic subobject/flag.


#### `kissing_number` `[FUNCTION]` `[Internal]`

- **Signature**: `def kissing_number(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L658`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L658)

#### `lattice` `[FUNCTION]` `[Internal]`

- **Signature**: `def lattice(data, basis=None, names=None, form=None, module_generators=None, *, category: Category) -> Lattice`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L1153`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L1153)

Return an owned lattice in ``category``.

``Lattices(R)(R^n)`` is the standard Euclidean lattice: the identity
Gram tensor on \(R^n\).  ``Lattices(R)(R^{\mathbb N})`` is the colimit
of those, with \(\langle x,y\rangle=\sum_i x_i y_i\) on finite
supports.  A pairing Gram on a free module is itself a lattice:
``Lattices(R)(diagonal_gram(R^NN, {0: -1}))``.  ``form=`` equips a
given free module with such a Gram.  ``module_generators=`` is the
generating set of that free module; when omitted, the generators
are the formal symbols \(e_i\in\mathrm{SR}\).  A matrix (type
$(1,1)$) is refused.  Named descriptors (``'U'``, a finite
simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.


#### `lattice_embedding_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def lattice_embedding_homset(domain, codomain) -> LatticeEmbeddingHomset`
- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L1328`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L1328)

#### `lattice_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def lattice_homset(domain, codomain) -> LatticeHomset`
- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L1320`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L1320)

#### `lattice_isometry_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def lattice_isometry_homset(domain, codomain) -> LatticeIsometryHomset`
- **Source**: [`src/dzack_research/preamble/categories/lattice_morphisms.py#L1336`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_morphisms.py#L1336)

#### `lattice_latex` `[FUNCTION]` `[Internal]`

- **Signature**: `def lattice_latex(lattice: Lattice, ring_tex: str) -> str`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L952`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L952)

The archived lattice display: $L$ with its invariants, then $G_L$.

The Gram tensor is the form of $L$, not $L$; $G_L$ typesets its components.


#### `lll_reduction` `[FUNCTION]` `[Internal]`

- **Signature**: `def lll_reduction(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L62`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L62)

#### `minimum` `[FUNCTION]` `[Internal]`

- **Signature**: `def minimum(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L158`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L158)

#### `orthogonal_sum` `[FUNCTION]` `[Internal]`

- **Signature**: `def orthogonal_sum(left, right, *, category)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L811`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L811)

The orthogonal direct sum, in the concatenated basis.

The left summand must have finite rank, so its basis occupies the
first \(n\) coordinates and the right basis is shifted by \(n\).
That covers finite \(\oplus\) finite and finite \(\oplus\) infinite.
Infinite \(\oplus\) infinite is not this concatenation, and is not
constructed.


#### `oscar_centralizer_discriminant_image` `[FUNCTION]` `[Internal]`

- **Signature**: `def oscar_centralizer_discriminant_image(gram, isometry)`
- **Source**: [`src/dzack_research/preamble/categories/lattice_engines.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_engines.py#L144)

Return OSCAR's image of ``Z_{O(L)}(f)`` in ``O(A_L)``.

The returned generator matrices are private Smith-coordinate data for the
finite discriminant form.  The public caller must transport them through
the owned finite-form engine and verify the resulting live automorphisms.
The lattice-with-isometry input follows OSCAR's right-action convention,
so the owned type-``(1,1)`` isometry tensor is transposed exactly once at
this boundary.


#### `oscar_even_unimodular_primitive_embedding` `[FUNCTION]` `[Internal]`

- **Signature**: `def oscar_even_unimodular_primitive_embedding(gram, positive, negative)`
- **Source**: [`src/dzack_research/preamble/categories/lattice_engines.py#L270`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_engines.py#L270)

Return a typed even-unimodular target Gram and primitive embedding tensor.

OSCAR/Hecke's ``embed_in_unimodular`` constructs the Nikulin complement
and gluing.  Its embedding coordinates are emitted as row images; this
private seam transposes them into the live column-action type-``(1,1)``
tensor before returning.


#### `oscar_rational_spinor_norm_sign` `[FUNCTION]` `[Internal]`

- **Signature**: `def oscar_rational_spinor_norm_sign(gram, isometry)`
- **Source**: [`src/dzack_research/preamble/categories/lattice_engines.py#L65`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_engines.py#L65)

Return the sign of OSCAR's rational spinor norm.

OSCAR's ``ZZLatWithIsom`` uses the right-action matrix convention.  The
owned isometry tensor uses column action ``M*v=M(v)``, so the adapter
transposes exactly once before crossing the boundary.  This function
returns OSCAR's convention; the owned real-spinor character applies the
determinant correction separately.


#### `packing_density` `[FUNCTION]` `[Internal]`

- **Signature**: `def packing_density(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L607`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L607)

#### `packing_radius` `[FUNCTION]` `[Internal]`

- **Signature**: `def packing_radius(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L649`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L649)

#### `primitive_isotropic_subobject` `[FUNCTION]` `[Internal]`

- **Signature**: `def primitive_isotropic_subobject(lattice, basis)`
- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L11)

Return the primitive totally isotropic sublattice spanned by ``basis``.


#### `rational_positive_vector` `[FUNCTION]` `[Internal]`

- **Signature**: `def rational_positive_vector(gram)`
- **Source**: [`src/dzack_research/preamble/categories/lattice_engines.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattice_engines.py#L20)

Return one exact rational positive vector for signature ``(1,n)``.

Sage supplies the rational diagonalization privately.  The returned value
is immediately re-entered into the preamble as a type-``(1,0)`` tensor;
the transformation matrix itself is never public API.


#### `refine_lattice_properties` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_lattice_properties(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2548`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2548)

Attach the finite lattice properties directly decidable from the form.


#### `refine_rational_lattice` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_rational_lattice(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/rational_lattices.py#L50`](file:///home/dzack/research/src/dzack_research/preamble/categories/rational_lattices.py#L50)

Adopt a finite free ``Frac(R)``-valued nondegenerate form as a rational lattice.


#### `refine_root_lattice` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_root_lattice(lattice, cartan_type)`
- **Source**: [`src/dzack_research/preamble/categories/lattices.py#L2543`](file:///home/dzack/research/src/dzack_research/preamble/categories/lattices.py#L2543)

Record the Cartan type whose negative Cartan form built ``lattice``.


#### `root_sublattice` `[FUNCTION]` `[Internal]`

- **Signature**: `def root_sublattice(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L192`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L192)

Return the formed subobject generated by all square-two roots.


#### `roots` `[FUNCTION]` `[Internal]`

- **Signature**: `def roots(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L180`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L180)

#### `roots_of_square` `[FUNCTION]` `[Internal]`

- **Signature**: `def roots_of_square(lattice, square)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L185`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L185)

#### `scale_gram_tensor` `[FUNCTION]` `[Internal]`

- **Signature**: `def scale_gram_tensor(gram, scalar)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L860`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L860)

Return the type-$(0,2)$ tensor \(\mathrm{scalar}\cdot G\).


#### `shortest_vectors` `[FUNCTION]` `[Internal]`

- **Signature**: `def shortest_vectors(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L263`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L263)

#### `signature_pair_of_gram` `[FUNCTION]` `[Internal]`

- **Signature**: `def signature_pair_of_gram(gram: Tensor)`
- **Source**: [`src/dzack_research/preamble/categories/_lattice.py#L911`](file:///home/dzack/research/src/dzack_research/preamble/categories/_lattice.py#L911)

Return $(p,q)$ for a Gram tensor, by Sylvester over $\mathbb Q$.


#### `stable_complement_root_reflections` `[FUNCTION]` `[Internal]`

- **Signature**: `def stable_complement_root_reflections(lattice, element)`
- **Source**: [`src/dzack_research/preamble/categories/vector_orbits.py#L462`](file:///home/dzack/research/src/dzack_research/preamble/categories/vector_orbits.py#L462)

Return root reflections of ``element^perp`` that lie in ``ker(rho_L)``.

For an indefinite complement, one representative of each ``O(element^perp)``
orbit of roots of square ``+2`` and ``-2`` is obtained through the exact
vector-orbit backend.  Each representative is embedded back into ``L`` and
reflected there; only reflections acting trivially on ``A_L`` are retained.
The result is a finite family inside the stable stabilizer of ``element``,
not a claim to generate that stabilizer.


#### `subgroup_isotropic_are_equivalent` `[FUNCTION]` `[Internal]`

- **Signature**: `def subgroup_isotropic_are_equivalent(subgroup, left, right, *, flag=False) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/orthogonal_quotients.py#L236`](file:///home/dzack/research/src/dzack_research/preamble/categories/orthogonal_quotients.py#L236)

#### `subgroup_isotropic_orbit_representatives` `[FUNCTION]` `[Internal]`

- **Signature**: `def subgroup_isotropic_orbit_representatives(subgroup, rank, *, flag=False)`
- **Source**: [`src/dzack_research/preamble/categories/orthogonal_quotients.py#L215`](file:///home/dzack/research/src/dzack_research/preamble/categories/orthogonal_quotients.py#L215)

#### `subgroup_vector_orbit_representatives` `[FUNCTION]` `[Internal]`

- **Signature**: `def subgroup_vector_orbit_representatives(subgroup, square)`
- **Source**: [`src/dzack_research/preamble/categories/orthogonal_quotients.py#L188`](file:///home/dzack/research/src/dzack_research/preamble/categories/orthogonal_quotients.py#L188)

#### `subgroup_vectors_are_equivalent` `[FUNCTION]` `[Internal]`

- **Signature**: `def subgroup_vectors_are_equivalent(subgroup, left, right) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/orthogonal_quotients.py#L204`](file:///home/dzack/research/src/dzack_research/preamble/categories/orthogonal_quotients.py#L204)

#### `successive_minima` `[FUNCTION]` `[Internal]`

- **Signature**: `def successive_minima(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L449`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L449)

Return the exact successive lengths as owned real numbers.


#### `theta_series` `[FUNCTION]` `[Internal]`

- **Signature**: `def theta_series(lattice, precision=20, variable='q')`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L617`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L617)

#### `transport_isotropic_object` `[FUNCTION]` `[Internal]`

- **Signature**: `def transport_isotropic_object(isometry, obj)`
- **Source**: [`src/dzack_research/preamble/categories/isotropic_orbits.py#L97`](file:///home/dzack/research/src/dzack_research/preamble/categories/isotropic_orbits.py#L97)

Transport a primitive isotropic subobject or flag along a lattice isometry.


#### `vectors_of_square` `[FUNCTION]` `[Internal]`

- **Signature**: `def vectors_of_square(lattice, square)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L167`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L167)

#### `vectors_of_square_and_divisibility` `[FUNCTION]` `[Internal]`

- **Signature**: `def vectors_of_square_and_divisibility(lattice, square, divisibility)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L258`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L258)

#### `voronoi_cell` `[FUNCTION]` `[Internal]`

- **Signature**: `def voronoi_cell(lattice, bound=None)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L359`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L359)

Return the owned rational Voronoi cell in lattice coordinates.


#### `voronoi_relevant_vectors` `[FUNCTION]` `[Internal]`

- **Signature**: `def voronoi_relevant_vectors(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/definite_lattices.py#L421`](file:///home/dzack/research/src/dzack_research/preamble/categories/definite_lattices.py#L421)

Return the vectors defining facets of the Voronoi cell.



---

<a id="subsystem-modules"></a>
## Modules, Complexes & Homological Algebra

> Framed free modules, Finitely presented modules, Formed modules, Group modules, Cochain complexes, Connections, and DG modules.

### 🏛 Categories & Subcategories

#### `AlternatingPowerModules` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L53`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L53)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `BilinearFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L844`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L844)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FormModules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `BiproductModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1530`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1530)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `biproduct_factor(self, index)`
- `biproduct_factors(self)`
- `from_summands(self, left_map, right_map)`
  > Return the unique map ``self -> X`` extending both summand maps.
- `left_inclusion(self)`
- `left_projection(self)`
- `right_inclusion(self)`
- `right_projection(self)`
- `to_product(self, left_map, right_map)`
  > Return the unique map ``X -> self`` with the specified projections.

**Category Instance Methods:**
- `super_categories(self)`

#### `CochainComplexes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L30)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedModules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `cohomology(self, degree)`
- `d(self, element)`
- `differential(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `CochainHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L384`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L384)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `CohomologyModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L53`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L53)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedModules(self.base_ring())]`

Cohomology modules retaining their represented cycle quotient.


**ParentMethods (Methods on Category Objects):**
- `class_of_cycle(self, cycle)`
  > Return the cohomology class of a closed element of ``C^p``.
- `cochain_complex(self)`
- `cohomological_degree(self)`
- `cycle_representative(self, cohomology_class)`
  > Return the selected closed representative in ``C^p``.

**Category Instance Methods:**
- `super_categories(self)`

#### `DifferentialGradedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/dg_modules.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/dg_modules.py#L35)
- **Bases**: `Category_over_base`
- **Super Categories**: `[GradedAlgebraModules(dga), CochainComplexes(dga.base_ring())]`

Right differential graded modules over one selected DGA ``(A,d)``.


**ParentMethods (Methods on Category Objects):**
- `dga(self)`
- `is_differential_graded_module(self) -> bool`

**Category Instance Methods:**
- `dga(self)`
- `super_categories(self)`

#### `DiscriminantBilinearModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L98`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L98)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[DiscriminantModules(self.base_ring()), TorsionBilinearFormModules(self.base_ring())]`

Discriminant modules with ``K/R``-valued bilinear form.


**ParentMethods (Methods on Category Objects):**
- `O(self)`
- `@cached_method` `automorphism_group(self)`
  > Return ``O(A,b)`` as live form automorphisms.
- `b(self, left, right)`
- `bilinear_value_module(self)`
- `discriminant_form_of_overlattice(self, subgroup)`
  > Return the Nikulin subquotient ``H^perp/H`` for the glued lattice.
- `@cached_method` `equip_form_morphism(self)`
- `@cached_method` `forget_form_morphism(self)`
- `@cached_method` `form(self)`
- `form_vanishes_on(self, elements) -> bool`
  > Return whether the bilinear form vanishes on all pairs.
- `@cached_method` `invariant_factor_form(self)`
  > Return the bilinear isometry to a normalized framed torsion form.
- `is_anti_isometric(self, other) -> bool`
- `is_isomorphic(self, other) -> bool`
- `orthogonal_group(self)`
- `orthogonal_quotient(self, subgroup)`
  > Return ``H^perp/H`` with its descended bilinear form.
- `orthogonal_subgroup(self, subgroup)`
  > Return ``H^perp`` for a subgroup ``H <= A``.
- `overlattice_from_isotropic_subobject(self, subgroup)`
  > Return ``L -> L'`` for bilinear-isotropic glue ``H <= A_L``.
- `p_adic_jordan_decomposition(self)`
- `p_adic_jordan_form(self)`
- `p_adic_jordan_module_generators(self)`
- `pontryagin_dual_identification(self)`
  > Return ``A -> Hom(A,QQ/ZZ)``, ``x |-> b(x,-)``.
- `twist(self, scalar)`
- `unformed_module(self)`
- `value_module(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DiscriminantModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L17`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L17)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedTorsionModules(self.base_ring())]`

Cokernels ``A_L = coker(L -> L^#)`` of nondegenerate finite lattices.


**ParentMethods (Methods on Category Objects):**
- `discriminant_class(self, dual_lattice_element)`
  > Return the class of an element of ``L^#`` in ``A_L``.
- `dual_lattice(self)`
  > Return the selected metric dual ``L^#`` covering this quotient.
- `dual_lattice_lift(self, element)`
  > Return a representative of ``element`` in the selected metric dual ``L^#``.
- `primary_components(self)`
  > Return the canonical ``p``-primary subgroups indexed by primes dividing ``|A|``.
- `@cached_method` `projection(self)`
  > Return the quotient map ``L^# -> A_L`` on the selected dual basis.
- `source_lattice(self)`
- `subgroup_on(self, generators)`
  > Return the finite subgroup generated by ``generators`` with its inclusion.
- `@cached_method` `subgroups(self)`
  > Return all finite subgroups, exhaustively, for the represented finite module.

**Category Instance Methods:**
- `super_categories(self)`

#### `DiscriminantQuadraticModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L349`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L349)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[DiscriminantBilinearModules(self.base_ring()), TorsionQuadraticFormModules(self.base_ring())]`

Even-lattice discriminant modules with quadratic form in ``K/2R``.


**ParentMethods (Methods on Category Objects):**
- `O(self)`
- `associated_bilinear_form(self)`
  > Return the ``QQ/ZZ``-valued polarization as a distinct object.
- `@cached_method` `automorphism_group(self)`
  > Return ``O(A,q)`` as live quadratic-form automorphisms.
- `@cached_method` `brown_invariant(self)`
  > Return the Brown invariant in ``ZZ/8ZZ`` from the exact Gauss sum.
- `discriminant_form_of_overlattice(self, subgroup)`
  > Return ``H^perp/H``, the discriminant form of the glued overlattice.
- `@cached_method` `form(self)`
- `form_vanishes_on(self, elements) -> bool`
  > Return whether ``q`` vanishes on every supplied element.
- `@cached_method` `invariant_factor_form(self)`
  > Return the quadratic isometry to invariant-factor framing.
- `is_anisotropic(self) -> bool`
- `is_anti_isometric(self, other) -> bool`
- `is_isomorphic(self, other) -> bool`
- `is_metabolic(self) -> bool`
- `@cached_method` `isotropic_elements(self)`
  > Return the classes on which the quadratic form vanishes.
- `@cached_method` `isotropic_subgroups(self)`
  > Return all subgroups on which ``q`` vanishes identically.
- `@cached_method` `lagrangian_subgroups(self)`
  > Return isotropic ``H`` with ``|H|^2=|A|``.
- `orthogonal_group(self)`
- `orthogonal_quotient(self, subgroup)`
  > Return ``H^perp/H`` with its descended quadratic form.
- `overlattice_from_isotropic_subobject(self, subgroup)`
  > Return ``L -> L'`` for q-isotropic glue ``H <= A_L``.
- `p_adic_jordan_decomposition(self)`
- `p_adic_jordan_form(self)`
- `p_adic_jordan_module_generators(self)`
- `q(self, element)`
- `quadratic_value_module(self)`
- `twist(self, scalar)`
- `value_module(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DiscriminantSubmodules` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L668`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L668)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedTorsionModules(self.base_ring())]`

Finite subgroups of a discriminant module with the restricted form.


**ParentMethods (Methods on Category Objects):**
- `ambient_discriminant_module(self)`
- `b(self, left, right)`
- `@cached_method` `embedded_elements(self)`
- `is_isotropic(self) -> bool`
- `q(self, element)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DividedPowerModules` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L64`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L64)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `DividedSquareModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L286`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L286)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[DividedPowerModules(self.base_ring())]`

Degree-two divided powers, classifying quadratic maps.


**ParentMethods (Methods on Category Objects):**
- `divided_square_source(self)`
- `from_quadratic(self, quadratic, codomain)`
  > Factor a quadratic map uniquely through the divided square.
- `polar(self, left, right)`
  > Return ``gamma_2(x+y)-gamma_2(x)-gamma_2(y)``.
- `quadratic(self, element)`
  > Return the universal quadratic value ``gamma_2(element)``.

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyGeneratedFormModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L979`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L979)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FormModules(self.base_ring()), FinitelyGeneratedModules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyGeneratedFreeFormModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L990`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L990)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FreeFormModules(self.base_ring()), FinitelyGeneratedFormModules(self.base_ring()), FinitelyGeneratedFreeModules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `@cached_method` `correlation_morphism(self)`
- `determinant(self)`
  > Return the determinant of the selected scalar-valued form.
- `@cached_method` `dual_module(self)`
- `is_nondegenerate(self) -> bool`
- `is_unimodular(self) -> bool`
  > Return whether the correlation morphism is an isomorphism.
- `scale_submodule(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyGeneratedFreeGroupModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L381`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L381)
- **Bases**: `_CategoryOverRingAndActingGroup`
- **Super Categories**: `[GroupModules(self.base_ring(), self.acting_group()), FinitelyPresentedGroupModules(self.base_ring(), self.acting_group()), FinitelyGeneratedFreeModules(self.base_ring())]`

Group modules whose underlying module is finite free with a chosen basis.


**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyGeneratedFreeModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L712`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L712)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FreeModules(self.base_ring()), FramedModules(self.base_ring()), FinitelyGeneratedModules(self.base_ring()), FinitelyPresentedModules(self.base_ring()), ProjectiveModules(self.base_ring())]`

Finite-rank free modules with a chosen ordered basis.


**ParentMethods (Methods on Category Objects):**
- `dual_module(self)`
- `free_resolution(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyGeneratedModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L459`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L459)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `@cached_method` `fiber(self, point)`
  > Return ``M(p)=M tensor_R kappa(p)`` at ``p in Spec(R)``.
- `fiber_dimension(self, point)`
  > Return ``dim_{kappa(p)} M(p)`` when the finite fiber is represented.
- `generic_rank(self)`
  > Return ``dim_K(M tensor_R K)`` for an integral-domain base ``R``.
- `is_finitely_generated(self) -> bool`
- `local_minimal_generators(self, point)`
  > Return a selected minimal generating set of ``M_p`` when represented.
- `local_number_of_generators(self, point)`
  > Return the minimal number of generators of ``M_p`` by Nakayama.
- `minimal_number_of_generators(self)`
  > Return ``dim_k(M/mM)`` for a finite module over a local ring.
- `rank_at(self, point)`
  > Return the local fiber rank ``dim_{kappa(p)} M(p)``.
- `residue_module(self)`
  > Return ``M/mM = M tensor_R k`` for a represented local base ring.

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedBilinearFormModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L934`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L934)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedFormModules(self.base_ring()), BilinearFormModules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedFormModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L923`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L923)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FormModules(self.base_ring()), FinitelyPresentedModules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedGroupModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L399`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L399)
- **Bases**: `_CategoryOverRingAndActingGroup`
- **Super Categories**: `[GroupModules(self.base_ring(), self.acting_group()), FinitelyPresentedModules(self.base_ring())]`

Group modules with a chosen finite presentation of the underlying module.


**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L619`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L619)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyGeneratedModules(self.base_ring())]`

Modules admitting a finite presentation.


**ParentMethods (Methods on Category Objects):**
- `is_finitely_presented(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedQuadraticFormModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L946`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L946)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedFormModules(self.base_ring()), QuadraticFormModules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedTorsionModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L26)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedModules(self.base_ring()), TorsionModules(self.base_ring())]`

Finitely presented torsion modules over a PID.


**ParentMethods (Methods on Category Objects):**
- `@cached_method` `elements(self)`
  > Return all elements through the private finite Smith workspace.
- `is_torsion(self) -> bool`

**Category Instance Methods:**
- `direct_sum_of_cyclics(self, orders)`
- `super_categories(self)`

#### `FormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L623`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L623)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules over ``R`` equipped with a form.


**ParentMethods (Methods on Category Objects):**
- `b(self, left, right)`
  > Evaluate the (polar) bilinear form on two elements of this module.
- `base_change(self, ring_map)`
  > Base-change a scalar-valued finite free form along ``R -> S``.
- `equip_form_morphism(self)`
  > Return the inverse canonical module identification into the formed copy.
- `fibered_formed_hom(self, codomain, ring_map, module_morphism, value_morphism)`
  > Construct a formed morphism over a coefficient-ring map.
- `forget_form_morphism(self)`
  > Return the canonical module identification from the formed copy.
- `form(self)`
- `formed_hom(self, module_morphism, value_morphism)`
  > Construct the general fixed-fiber formed morphism ``(f,h)``.
- `gram_tensor(self)`
  > Return the scalar Gram as its intrinsic type-``(0,2)`` tensor.
- `norm(self, element)`
  > Return ``q(x)`` for a quadratic form, else ``b(x, x)``.
- `twist(self, scalar)`
- `unformed_module(self)`
  > Return the module used to equip this represented formed object.
- `value_module(self)`

**ElementMethods (Methods on Category Elements):**
- `b(self, other)`
  > Return the polar bilinear value ``b(self, other)``.
- `q(self)`
  > Return the represented quadratic/norm value of this element.

**Category Instance Methods:**
- `super_categories(self)`

#### `FormedModuleHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L294`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L294)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `FormedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L583`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L583)
- **Bases**: `Category_over_base`
- **Super Categories**: `[PairedModules(self.base())]`

Modules equipped with a bilinear form \(M\otimes_R M\to W\).

This is the diagonal of :class:`PairedModules`: a pairing of a module
with itself.


**ParentMethods (Methods on Category Objects):**
- `b(self, left, right)`
- `q(self, element)`

**ElementMethods (Methods on Category Elements):**
- `b(self, other)`
  > Return the bilinear value ``b(self, other)``.
- `q(self)`
  > Return the quadratic value ``q(self)=b(self,self)``.

**Category Instance Methods:**
- `super_categories(self)`

#### `FractionFieldQuotients` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L30)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FramedModules(self.base_ring())]`

Modules ``Frac(R) / a`` for a fractional ideal ``a`` of ``R``.

The active computation engine specializes this construction to
``R = ZZ``, where Sage's :class:`QmodnZ` computes ``QQ / n ZZ``.


**ParentMethods (Methods on Category Objects):**
- `base_ring(self)`
- `divisibility_chain(self, index)`
  > Return the chosen cofinal divisibility chain element ``d_index``.
- `fraction_field(self)`
- `framing_morphism(self)`
- `lift(self, element)`
  > Return the selected representative of ``element`` in the fraction field.
- `@cached_method` `module_generating_set(self)`
- `module_generator(self, label)`
- `modulus(self)`
  > Return a generator of the fractional ideal being quotiented out.
- `projection_from_fraction_field(self)`
  > Return the quotient map ``Frac(R) -> Frac(R) / a`` as an owned set map.

**Category Instance Methods:**
- `super_categories(self)`

#### `FractionalIdeals` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L32`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L32)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring()), ModuleSubobjects(self.base_ring())]`

Fractional ideals of an integral domain, as modules in its fraction field.


**ParentMethods (Methods on Category Objects):**
- `fraction_field(self)`
- `framing_morphism(self)`
- `intersection(self, other)`
  > Return ``I intersect J`` inside the common fraction field.
- `inverse(self)`
  > Return ``I^{-1}={x in K : xI subseteq R}`` for an invertible ideal.
- `is_principal(self) -> bool`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `@cached_method` `module_generators(self)`
- `principal_generator(self)`
  > Return ``a`` with ``I=aR`` when this ideal is principal.
- `scalar_multiple(self, scalar, element)`
- `sum(self, other)`
  > Return ``I+J`` inside the common fraction field.

**Category Instance Methods:**
- `super_categories(self)`

#### `FramedFreeModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L248`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L248)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FreeModules(self.base_ring()), FramedModules(self.base_ring())]`

Free modules equipped with the canonical basis map.


**ParentMethods (Methods on Category Objects):**
- `base_change(self, ring_map)`
  > Return ``S tensor_R M`` along the specified ring map ``R -> S``.
- `base_ring(self)`
- `cardinality(self)`
  > Return ``|R^(S)|``: ``|R|^|S|`` for finite ``S``, else ``max(|R|, |S|)`` by finite support.
- `framing_morphism(self)`
- `is_finite_rank(self) -> bool`
- `is_torsion_free(self) -> bool`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `@cached_method` `module_generators(self)`
- `rank(self)`
- `subobject_on(self, module_generating_set)`
  > Return the submodule spanned by the specified elements.

**Category Instance Methods:**
- `super_categories(self)`

#### `FramedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L798`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L798)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules carrying a specified generating map from a set.


**ParentMethods (Methods on Category Objects):**
- `inject_variables(self, scope=None, verbose=True)`
- `is_framed(self) -> bool`
- `linear_combination(self, coefficients, factor_on_left=True)`
- `module_generator_morphism(self)`
- `@cached_method` `module_generators(self)`
- `number_of_module_generators(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FreeFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L958`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L958)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FormModules(self.base_ring()), FramedFreeModules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `subobject_on(self, module_generating_set)`
  > Return the span equipped with the pulled-back form.

**Category Instance Methods:**
- `super_categories(self)`

#### `FreeModuleBaseRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L35)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

Rings equipped with the selected free-module exponent construction.


**Category Instance Methods:**
- `super_categories(self)`

#### `FreeModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L444`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L444)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules admitting a basis.


**ParentMethods (Methods on Category Objects):**
- `is_free(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `GradedAlgebraModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/dg_modules.py#L8`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/dg_modules.py#L8)
- **Bases**: `Category_over_base`
- **Super Categories**: `[GradedModules(algebra.base_ring(), algebra.grading_monoid())]`

Right graded modules over one selected graded algebra ``A``.


**ParentMethods (Methods on Category Objects):**
- `act(self, module_element, algebra_element)`
- `graded_algebra(self)`
- `right_action(self)`

**Category Instance Methods:**
- `graded_algebra(self)`
- `super_categories(self)`

#### `GradedModuleHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L102`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L102)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `GradedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L107)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules graded by a monoid.

Let \(M\) be a monoid and \(R\) a ring. An \(M\)-graded \(R\)-module is
an \(R\)-module \(N\) together with a direct-sum decomposition
\(N = \bigoplus_{m \in M} N_m\). This is the nLab graded module over an
ungraded ring (an \(M\)-graded object of \(\mathbf{Mod}_R\)).

The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
module axiom. An \(M\)-graded algebra is an \(M\)-graded module whose
product sends \(N_m \times N_{m'}\) into \(N_{mm'}\).

**Category Constructor:**
- `GradedModules(self, base_ring, grading_monoid: Parent) -> None`

**ParentMethods (Methods on Category Objects):**
- `combine_degrees(self, left, right)`
  > The monoid product of two degrees.
- `grading_monoid(self)`
- `is_graded(self) -> bool`

**Category Instance Methods:**
- `grading_monoid(self) -> Parent`
- `super_categories(self)`

#### `GroupLattices` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_lattices.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_lattices.py#L11)
- **Bases**: `_CategoryOverRingAndActingGroup`
- **Super Categories**: `[Lattices(self.base_ring()), GroupModules(self.base_ring(), self.acting_group())]`

Lattices carrying a specified action by lattice isometries.


**ParentMethods (Methods on Category Objects):**
- `act(self, group_element, vector)`
- `action(self)`
- `action_of(self, group_element)`
- `character(self)`
- `formed_coinvariants(self)`
  > Return ``(L^G)^perp`` as a formed subobject of ``L``.
- `group(self)`
- `invariant_lattice(self)`
  > Return ``L^G`` as a formed subobject of this lattice.
- `is_invariant(self, vector) -> bool`
- `module_coinvariants(self)`
  > Return the underlying module quotient by ``(g-1)M``.
- `module_invariants(self)`
  > Return the native fixed submodule of the underlying group module.

**Category Instance Methods:**
- `super_categories(self)`

#### `GroupModuleHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L30)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `GroupModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L60`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L60)
- **Bases**: `CategoryPacketMethods`, `_CategoryOverRingAndActingGroup`
- **Super Categories**: `[Modules(self.base_ring())]`

The category of ``R[G]``-modules for a specified ring and group.


**ParentMethods (Methods on Category Objects):**
- `act(self, group_element, vector)`
  > Return ``group_element * vector`` in this group module.
- `action(self)`
  > Return the chosen action datum used to construct this group module.
- `action_of(self, group_element)`
  > Return the linear automorphism induced by ``group_element``.
- `base_change(self, ring_map)`
  > Transport this group module along ``R -> S`` functorially.
- `brauer_character(self)`
  > Return the Brauer character of a finite-dimensional modular representation.
- `character(self)`
  > Return the ordinary trace character in characteristic zero.
- `equip_action_morphism(self)`
- `forget_action_morphism(self)`
- `group(self)`
- `is_invariant(self, vector) -> bool`
- `is_trivial_action(self) -> bool`
- `isotypic_characters(self)`
  > Return the irreducible-character indices appropriate to the coefficient ring.
- `isotypic_component(self, character)`
  > Return the integral/base-ring isotypic component as a subobject.
- `isotypic_decomposition(self)`
  > Return the sum of isotypic components together with its inclusion in ``M``.
- `module_coinvariants(self)`
  > Return ``M_G = M / <g m - m>`` with the current framing retained.
- `module_invariants(self)`
  > Return ``M^G`` as the equalizer subobject of the action and identity.
- `unacted_module(self)`
  > Return the module from which this chosen action was equipped.

**Category Instance Methods:**
- `is_semisimple(self) -> bool`
  > Return the conclusion of Maschke's theorem when it applies.
- `super_categories(self)`

#### `Ideals` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L229`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L229)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FractionalIdeals(self.base_ring()), CommutativeIdeals(self.base_ring())]`

Integral ideals ``I <= R``.


**ParentMethods (Methods on Category Objects):**
- `ideal_generators(self)`
- `ring(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `InternalHomModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L320`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L320)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[LinearHomModules(self.base_ring())]`

The canonical full enriched Hom modules ``Hom_R(M,N)``.


**ParentMethods (Methods on Category Objects):**
- `inclusion_into_generator_maps(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `IsotypicDecompositions` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L46`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L46)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Submodules equipped with their selected isotypic summands.


**ParentMethods (Methods on Category Objects):**
- `isotypic_characters(self)`
- `isotypic_component(self, character)`
- `nontrivial_components(self)`
- `trivial_component(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `LinearEndCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L78)
- **Bases**: `EndCategoryConstruction`

Endomorphism rings for categories enriched in modules.


**Category Instance Methods:**
- `Of(self, obj, codomain=None)`

#### `LinearHomModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L281`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L281)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Represented Hom parents closed under pointwise ``R``-linear operations.


**ParentMethods (Methods on Category Objects):**
- `as_morphism(self, element)`
- `evaluation(self, map_element, source_element)`
- `from_morphism(self, morphism)`
- `scalar_multiple(self, scalar, morphism)`
- `source_module(self)`
- `target_module(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `LocalizedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/localizations.py#L12`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/localizations.py#L12)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules represented as ``S^{-1}M`` for a chosen localization ``S^{-1}R``.


**ParentMethods (Methods on Category Objects):**
- `localization_functor(self)`
- `localization_prime_point(self)`
- `localization_ring(self)`
- `localization_source_module(self)`
- `localization_submonoid(self)`
- `localization_unit(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `MatrixEndomorphismSpaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L2033`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L2033)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[MatrixSpaces(self.base_ring()), OwnedRings()]`

The matrix realization of ``End_R(F)`` for a finite framed free module ``F``.


**ParentMethods (Methods on Category Objects):**
- `diagonal(self, entries)`
- `identity_matrix(self)`

**ElementMethods (Methods on Category Elements):**
- `trace(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `MatrixSpaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1699`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1699)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[InternalHomModules(self.base_ring()), FinitelyGeneratedFreeModules(self.base_ring())]`

Hom objects between finitely generated framed free ``R``-modules.


**ParentMethods (Methods on Category Objects):**
- `column_index_set(self)`
- `from_flat_entries(self, entries)`
- `from_rows(self, rows)`
  > Construct the matrix morphism with the stated row entries.
- `from_tensor(self, coordinate_tensor)`
  > Read a compatible type-``(1,1)`` tensor as this linear map.
- `matrix_shape(self)`
- `matrix_unit(self, row_label, column_label)`
- `ncols(self)`
- `nrows(self)`
- `row_index_set(self)`

**ElementMethods (Methods on Category Elements):**
- `column(self, column_label)`
- `columns(self)`
- `determinant(self)`
- `invariant_factors(self)`
- `inverse(self)`
  > Return the inverse matrix morphism with reversed endpoints.
- `list(self)`
- `matrix_entry(self, row_label, column_label)`
- `matrix_shape(self)`
- `ncols(self)`
- `nrows(self)`
- `rank(self)`
- `row(self, row_label)`
- `rows(self)`
- `smith_form(self)`
  > Return ``(D,U,V)`` from invariant-factor presentation normalization.
- `smith_normal_form(self)`
- `solve_right(self, target)`
  > Return ``x`` in the domain with ``self(x)=target``.
- `transpose(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `ModuleEndCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L95`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L95)
- **Bases**: `LinearEndCategoryConstruction`

The ring-valued endomorphism family ``M |-> End_R(M)``.


#### `ModuleHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L59`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L59)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`
- `fixed_category_class_for(self, domain, codomain)`

#### `ModuleSubobjects` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L341`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L341)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules carrying a chosen monomorphism into another module.


**ParentMethods (Methods on Category Objects):**
- `embedded_module_generators(self)`
  > Return the indexed family of selected generator images.
- `inclusion(self)`
  > Return the chosen monomorphism representing this subobject.
- `index(self)`
- `intersection(self, other)`
  > Return the meet as the image of the kernel of ``(i,-j)``.
- `is_primitive(self) -> bool`
- `isotropic_reduction(self)`
  > Return the isotropic reduction owned by this chosen inclusion.
- `orthogonal_complement(self)`
  > Return the orthogonal complement by deferring to the inclusion.
- `saturation(self)`
  > Return the primitive closure by deferring to the inclusion.
- `sum(self, other)`
  > Return the join of two subobjects of the same codomain.

**Category Instance Methods:**
- `super_categories(self)`

#### `Modules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L99`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L99)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[CommutativeAdditiveGroups()]`

Modules over a ring, on the owned additive and scalar spines.


**ParentMethods (Methods on Category Objects):**
- `base_ring(self)`
- `is_framed(self) -> bool`
- `is_free(self) -> bool`
- `is_module(self) -> bool`
- `localize(self, *datum)`
  > Return ``S^{-1}M`` by scalar extension to ``S^{-1}R``.
- `localize_at_prime(self, prime)`
  > Return the localized module ``M_p`` at a represented prime.
- `module_category(self)`
- `restrict_scalars(self, ring_map)`
  > Read this module over the domain of ``ring_map``.
- `scalar_action(self)`
- `scalar_multiple(self, scalar, element)`
  > Return ``r*m = rho_M(r)(m)``.
- `twist_scalar_action(self, ring_endomorphism)`
  > Twist this module's scalar action along a base-ring endomorphism.

**Category Instance Methods:**
- `homset(self, domain, codomain)`
  > Return the unique Hom-set ``Hom_R(domain,codomain)``.
- `super_categories(self)`

#### `ModulesWithChosenFinitePresentation` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py#L55`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py#L55)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedModules(self.base_ring()), FramedModules(self.base_ring())]`

Finitely presented modules carrying a selected relation morphism.


**ParentMethods (Methods on Category Objects):**
- `annihilator(self)`
  > Return ``Ann_R(M)`` in exact currently represented regimes.
- `annihilator_support(self)`
  > Return ``V(Ann(M))`` when the annihilator is represented.
- `base_change(self, ring_map)`
  > Transport the selected finite presentation along ``R -> S``.
- `base_ring(self)`
- `cardinality(self)`
  > Return the cardinality of the underlying set, as a cardinal.
- `cokernel_projection(self)`
  > Return the canonical quotient map when this object is a selected cokernel.
- `dimension(self)`
  > Return vector-space dimension when the base ring is a field.
- `exponent(self)`
  > Return the exponent of a finite torsion ``ZZ``-module.
- `fiber_dimension_at_least(self, dimension)`
  > Return the closed locus where ``dim_{kappa(p)} M(p) >= dimension``.
- `fitting_ideal(self, index)`
  > Return ``Fitt_index(M)`` from the selected finite presentation.
- `framing_morphism(self)`
- `free_resolution(self)`
  > Return the selected length-one free resolution over the represented PID.
- `@cached_method` `invariant_factor_form(self)`
  > Return ``self -> M_if`` with only non-unit invariant factors.
- `@cached_method` `invariant_factor_presentation(self)`
  > Normalize the selected presentation through the PID structure theorem.
- `@cached_method` `invariant_factors(self)`
  > Return the indexed family of non-unit invariant factors.
- `is_torsion(self)`
- `is_torsion_free(self)`
- `is_zero(self)`
- `minimal_module_generators(self)`
  > Return a minimal selected generating set over a local base ring.
- `module_generating_set(self)`
- `module_generator(self, label)`
- `@cached_method` `module_generators(self)`
  > Return the indexed family of selected framing images.
- `number_of_module_generators(self)`
- `presentation(self)`
  > Return the selected relation morphism ``F_1 -> F_0``.
- `presentation_matrix(self)`
  > Return its relation rows in the selected target framing.
- `presentation_projection(self)`
  > Return the selected quotient map ``F_0 -> M``.
- `rank(self)`
  > Return the rank of the free summand over a PID.
- `@cached_method` `smith_form_module_generators(self)`
  > Return the invariant-factor framing realized inside ``self``.
- `support(self)`
  > Return ``Supp(M)=V(Fitt_0(M))`` in ``Spec(R)``.
- `tensor_product(self, other)`
- `torsion_free_quotient(self)`
  > Return ``M/Tor(M)``.
- `torsion_free_quotient_projection(self)`
  > Return ``M -> M/Tor(M)`` from invariant-factor coordinates.

**Category Instance Methods:**
- `super_categories(self)`

#### `ModulesWithConnection` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L28`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L28)
- **Bases**: `Category_over_base`
- **Super Categories**: `[Modules(self.algebra())]`

Modules over ``A`` equipped with an ``A/R``-connection.


**ParentMethods (Methods on Category Objects):**
- `connection(self)`

**Category Instance Methods:**
- `algebra(self)`
- `super_categories(self)`

#### `ModulesWithFlatConnection` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L53`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L53)
- **Bases**: `Category_over_base`
- **Super Categories**: `[ModulesWithConnection(self.algebra())]`

Modules whose selected connection has zero curvature.


**ParentMethods (Methods on Category Objects):**
- `is_flat_connection(self) -> bool`

**Category Instance Methods:**
- `algebra(self)`
- `super_categories(self)`

#### `PairedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L529`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L529)
- **Bases**: `Category_over_base`
- **Super Categories**: `[Sets()]`

Pairings \(X\otimes_R Y\to W\).

An object is classified by an element of
\(\operatorname{Hom}_R(X\otimes_R Y,W)\).  The diagonal \(X=Y\) is
:class:`FormedModules`.


**Object Constructor (Calling Category on Data):**
- `PairedModules(...)(self, pairing)`

**ParentMethods (Methods on Category Objects):**
- `left_module(self)`
- `pairing(self, left, right)`
  > Evaluate the pairing on a pair of elements.
- `right_module(self)`
- `value_module(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `ProjectiveModules` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L779`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L779)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `is_projective(self) -> bool`
- `projective_rank(self, point)`
  > Return the local free rank of a finite projective module at ``point``.

**Category Instance Methods:**
- `super_categories(self)`

#### `QuadraticFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L905`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L905)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FormModules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `q(self, element)`
  > Evaluate the equipped quadratic form on ``element``.

**Category Instance Methods:**
- `super_categories(self)`

#### `RestrictedScalarsModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L861`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L861)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules obtained by reading an ``S``-module over ``R`` along ``R -> S``.


**ParentMethods (Methods on Category Objects):**
- `extension_ring(self)`
- `module_over_extension(self)`
  > Return the original ``S``-module before restriction of scalars.
- `ring_map(self)`
  > Return the selected scalar map ``R -> S``.
- `scalar_multiple(self, scalar, element)`

**Category Instance Methods:**
- `super_categories(self)`

#### `SymmetricBilinearFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L855`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L855)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[BilinearFormModules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `algebraic_correlation_morphism(self)`
- `correlation_isomorphism(self)`
- `hodge_discriminant(self, volume)`
- `hodge_star(self, volume, degree)`
- `hodge_star_over_fraction_field(self, volume, degree)`
- `multivector_hodge_star(self, volume, degree)`

**Category Instance Methods:**
- `super_categories(self)`

#### `SymmetricPowerModules` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L42`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L42)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `TensorPowerModules` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L31`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L31)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `TensorProductModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1334`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1334)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Modules carrying a selected tensor-product universal object.


**ParentMethods (Methods on Category Objects):**
- `from_bilinear(self, bilinear)`
- `pure_tensor(self, left_element, right_element)`
  > Return the universal pure tensor of two elements.
- `tensor_factor(self, index)`
- `tensor_factors(self)`
- `universal_bilinear_map(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `TorsionBilinearFormIsoCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1067`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1067)
- **Bases**: `_TorsionFormIsoCategoryConstruction`

#### `TorsionBilinearFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1134`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1134)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedTorsionModules(self.base_ring()), FinitelyPresentedBilinearFormModules(self.base_ring())]`

Finitely presented torsion modules with a bilinear form.


**ParentMethods (Methods on Category Objects):**
- `O(self)`
- `@cached_method` `automorphism_group(self)`
  > Return ``O(A,b)`` as a finite owned group of live automorphisms.
- `form_vanishes_on(self, elements) -> bool`
- `@cached_method` `invariant_factor_form(self)`
  > Return the form-preserving isomorphism to invariant-factor framing.
- `is_anti_isometric(self, other) -> bool`
  > Return whether ``(self,b)`` is isometric to ``(other,-b)``.
- `is_isomorphic(self, other) -> bool`
  > Decide isometry of represented finite symmetric bilinear forms.
- `orthogonal_group(self)`
- `p_adic_jordan_decomposition(self)`
  > Return the chosen Jordan generators indexed by their prime.
- `p_adic_jordan_form(self)`
  > Return the explicit isometry to this form in Jordan framing.
- `p_adic_jordan_module_generators(self)`
  > Return the chosen prime-by-prime Jordan generating family.
- `pontryagin_dual_identification(self)`
  > Return ``A -> Hom(A,K/R)``, ``x |-> b(x,-)``, for perfect ``b``.
- `twist(self, scalar)`
  > Return the same finite module equipped with ``scalar*b``.

**Category Instance Methods:**
- `from_module(self, module, gram, value_module)`
  > Equip ``module`` with the bilinear form represented by ``gram``.
- `from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None)`
  > Construct a torsion bilinear form from presentation and Gram data.
- `super_categories(self)`

#### `TorsionModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L11)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `is_torsion(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `TorsionQuadraticFormIsoCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1071`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1071)
- **Bases**: `_TorsionFormIsoCategoryConstruction`

#### `TorsionQuadraticFormModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1271`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L1271)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedTorsionModules(self.base_ring()), FinitelyPresentedQuadraticFormModules(self.base_ring())]`

Finitely presented torsion modules with a quadratic form.


**ParentMethods (Methods on Category Objects):**
- `O(self)`
- `associated_bilinear_form(self)`
  > Polarize ``q:A->QQ/2ZZ`` to ``b_q:A^2->QQ/ZZ``.
- `@cached_method` `automorphism_group(self)`
  > Return ``O(A,q)`` as a finite owned group of live automorphisms.
- `form_vanishes_on(self, elements) -> bool`
- `@cached_method` `invariant_factor_form(self)`
  > Return the quadratic-form isomorphism to invariant-factor framing.
- `is_anti_isometric(self, other) -> bool`
  > Return whether ``(self,q)`` is isometric to ``(other,-q)``.
- `is_isomorphic(self, other) -> bool`
  > Decide isometry of represented finite quadratic forms.
- `orthogonal_group(self)`
- `p_adic_jordan_decomposition(self)`
  > Return the chosen quadratic Jordan generators indexed by prime.
- `p_adic_jordan_form(self)`
  > Return the explicit isometry to this quadratic form in Jordan framing.
- `p_adic_jordan_module_generators(self)`
  > Return the chosen prime-by-prime quadratic Jordan generators.
- `twist(self, scalar)`
  > Return the same finite module equipped with ``scalar*q``.

**Category Instance Methods:**
- `from_module(self, module, gram, value_module)`
  > Equip ``module`` with ``q(x)=x^T gram x`` valued in ``value_module``.
- `from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None)`
  > Construct a torsion quadratic form from presentation and Gram data.
- `super_categories(self)`

#### `VectorSpaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L433`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L433)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Vector spaces over a field.


**Category Instance Methods:**
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `CochainHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L305`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L305)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, components)`

**Public Methods:**
- `elementwise(self, function)`
- `identity(self)`
- `linear_combination(self, coefficients)`
- `zero(self)`

#### `CochainMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L235`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L235)
- **Bases**: `Morphism`

A degree-zero morphism commuting with the selected differentials.

- **Constructor**: `def __init__(self, parent, components) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `component(self, degree)`

#### `Connection` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L71`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L71)
- **Bases**: `Morphism`

An ``R``-connection ``E -> E tensor_A Omega^1_{A/R}``.

- **Constructor**: `def __init__(self, parent, generator_images) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `algebra(self)`
- `curvature_on_generator(self, label)`
- `curvature_target(self)`
- `de_rham_module(self)`
  > Return the DG-module de Rham complex attached to this flat connection.
- `generator_image(self, label)`
- `is_flat(self) -> bool`
- `module(self)`
- `one_forms(self)`
- `target_module(self)`
- `underlying_linear_morphism(self)`

#### `ConnectionHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L422`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L422)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `identity(self)`

#### `ConnectionMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L377`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L377)
- **Bases**: `ModuleMorphism`

An ``A``-linear map horizontal for the selected connections.

- **Constructor**: `def __init__(self, parent, images, *, verify_horizontality=True) -> None`

#### `ConnectionSpace` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L294`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L294)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, module) -> None`
- **Constructor**: `def _element_constructor_(self, generator_images)`

**Public Methods:**
- `algebra(self)`
- `ambient_hom(self)`
- `inclusion(self)`
- `module(self)`
- `one_forms(self)`
- `restricted_source_module(self)`
- `restricted_target_module(self)`
- `target_module(self)`

#### `FiberedFormedModuleHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L474`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L474)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain, ring_map) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `base_changed_domain(self)`
- `identity(self)`
- `ring_map(self)`

#### `FiberedFormedModuleMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L330`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L330)
- **Bases**: `Morphism`

A formed-module morphism over a coefficient-ring map ``g:S1 -> S2``.

The actual linear data live in the target fiber, exactly as required by
the Grothendieck/fibered-category formulation:

``module_morphism : S2 tensor_S1 L1 -> L2`` and
``value_morphism  : S2 tensor_S1 W1 -> W2``.

The active scalar-extension backend currently materializes this for the
scalar-valued finite-free formed objects supported by ``FormModule``'s
``base_change`` method.  Unsupported scalar extensions fail at object
construction rather than being represented by a semilinear fiction.

- **Constructor**: `def __init__(self, parent, module_morphism, value_morphism) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `base_changed_domain(self)`
- `map_value(self, value)`
- `module_morphism(self)`
- `ring_map(self)`
- `value_morphism(self)`

#### `FormEmbedding` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L45`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L45)
- **Bases**: `FormMorphism`

A form-preserving morphism declared to be a monomorphism.

- **Constructor**: `def __init__(self, parent, images, *, quadratic: bool) -> None`

**Public Methods:**
- `is_injective(self) -> bool`
- `is_quadratic(self) -> bool`

#### `FormMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L41`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L41)
- **Bases**: `ModuleMorphism`

A linear morphism verified to preserve the equipped forms.


#### `FormedModuleHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L233`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L233)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `identity(self)`

#### `FormedModuleMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L144)
- **Bases**: `Morphism`

A morphism of formed modules in one coefficient-ring fiber.

The datum is a pair ``(f,h)`` with a module map on the underlying modules
and a module map on the value objects, satisfying the form square.  The
stricter :class:`FormMorphism` remains the separate notion where ``h`` is
the identity and the form is preserved exactly.

- **Constructor**: `def __init__(self, parent, module_morphism, value_morphism) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `map_value(self, value)`
- `module_morphism(self)`
- `value_morphism(self)`

#### `FractionalIdealInclusion` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L400`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L400)
- **Bases**: `ModuleEmbedding`

The selected monomorphism from an ideal into ``R`` or ``Frac(R)``.

- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `index(self)`
- `is_in_image(self, element) -> bool`
- `is_primitive(self) -> bool`
- `lift(self, element)`
  > Return the ideal element mapping to ``element`` when it belongs to the ideal.

#### `FramingMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L852`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L852)
- **Bases**: `ModuleMorphism`

A declared surjective linear map from a free framed module.


**Public Methods:**
- `is_surjective(self) -> bool`

#### `GradedModuleHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L87)
- **Bases**: `_ModuleHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`

#### `GradedModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L42`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L42)
- **Bases**: `ModuleMorphism`

A degree-zero morphism of graded modules.

- **Constructor**: `def __init__(self, parent, images, *, elementwise=False) -> None`

#### `GroupModuleHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L468`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L468)
- **Bases**: `_ModuleHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`

**Public Methods:**
- `identity(self)`

#### `GroupModuleMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L422`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L422)
- **Bases**: `ModuleMorphism`

An ``R``-linear map commuting with the chosen ``G``-actions.

- **Constructor**: `def __init__(self, parent, images, *, elementwise=False, verify_linearity=True, verify_equivariance=True) -> None`

#### `ModuleEmbedding` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L859`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L859)
- **Bases**: `ModuleMorphism`

A module morphism declared to be a monomorphism.


**Public Methods:**
- `factor_through(self, target_embedding)`
  > Return the unique factor through ``target_embedding`` when it exists.
- `is_injective(self) -> bool`

#### `ModuleHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1062`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1062)
- **Bases**: `_ModuleHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def __call__(self, images)`

**Public Methods:**
- `inclusion_into_generator_maps(self)`
- `internal_hom_model(self)`
- `linear_combination(self, coefficients)`

#### `ModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L201`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L201)
- **Bases**: `Morphism`

The linear extension of a function on a chosen module framing.

- **Constructor**: `def __init__(self, parent, images, *, elementwise=False, verify_linearity=True) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `base_change(self, ring_map)`
  > Extend this represented linear map along ``ring_map : R -> S``.
- `@cached_method` `cokernel(self)`
  > Return the selected quotient ``codomain(self) / image(self)``.
- `image(self)`
  > Return ``im(self)`` as a subobject of the codomain.
- `index(self)`
  > Return the cardinality of the cokernel.
- `is_in_image(self, element) -> bool`
  > Return whether ``element`` has a preimage when the lift is decidable.
- `is_injective(self) -> bool`
  > Return whether ``ker(self)=0`` when the kernel is computable.
- `is_primitive(self) -> bool`
  > Return whether this monomorphism has torsion-free cokernel.
- `is_surjective(self) -> bool`
  > Return whether ``coker(self)=0`` when the cokernel is computable.
- `is_surjective_by_nakayama(self) -> bool`
  > Use Nakayama: a map onto a finite local module is surjective iff its residue map is.
- `is_surjective_mod_maximal_ideal(self) -> bool`
  > Return whether ``f tensor_R k`` is surjective.
- `@cached_method` `kernel(self)`
  > Return ``ker(self)`` as a subobject of the domain.
- `lift(self, element)`
  > Return the unique preimage of ``element`` for an injective free map.
- `matrix(self)`
  > Return the underlying free-module morphism under the matrix-Hom identification.
- `module_generator_morphism(self)`
- `morphisms_agree(self, other) -> bool`
  > Decide equality from this source module's selected finite framing.
- `orthogonal_complement(self)`
  > Return ``im(self)^perp`` inside the formed codomain.
- `residue_morphism(self)`
  > Return ``f tensor_R k`` for a morphism of finite modules over a local ring.
- `saturation(self)`
  > Return the saturation of the image of an injective morphism.
- `stack(self, other)`
  > Return ``(self,other)`` into the biproduct of the codomains.
- `then(self, other)`
  > Return ``other ∘ self``.

#### `QuadraticModuleHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L193`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L193)
- **Bases**: `ModuleHomset`

The ordinary Hom ``Hom_R(Gamma^2(M),W)`` with quadratic-map syntax.

- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `from_quadratic_map(self, quadratic, *, lift_coordinate_values=None)`

#### `QuadraticModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L75`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L75)
- **Bases**: `ModuleMorphism`

A classifier ``Gamma^2(M) -> W``, read as the quadratic map ``M -> W``.

- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `b(self, left, right)`
- `classifying_morphism(self)`
- `gram_tensor(self)`
- `lift_coordinate_values(self)`
- `lift_pairing(self, left, right)`
- `module(self)`
- `polar_coordinate_values(self)`
- `polar_form(self)`
- `pullback(self, morphism)`

#### `TensorProductModuleHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1268`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1268)
- **Bases**: `ModuleHomset`

The ordinary module Hom with tensor-domain bilinear constructor syntax.

- **Constructor**: `def _element_constructor_(self, images)`

#### `TensorProductModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1196`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1196)
- **Bases**: `ModuleMorphism`

A linear map out of a chosen tensor product, hence a bilinear map.

- **Constructor**: `def __call__(self, *arguments)`

**Public Methods:**
- `coordinate_values(self)`
- `left_module(self)`
- `module(self)`
- `norm(self, element)`
- `polar_form(self)`
- `pullback(self, morphism)`
- `right_module(self)`

#### `TorsionFormAutomorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L565`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L565)
- **Bases**: `TorsionFormIsometry`

A live form-preserving automorphism, parented by its orthogonal group.

- **Constructor**: `def __init__(self, parent, forward, inverse, _engine_element) -> None`

**Public Methods:**
- `inverse(self)`
- `inverse_morphism(self)`
  > Return the underlying inverse module morphism.

#### `TorsionFormOrthogonalGroup` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L625`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L625)
- **Bases**: `CategoricalHomset`

The finite group of live automorphisms preserving one finite form.

- **Constructor**: `def __init__(self, hom_family, form, *, quadratic: bool, normalization=None, engine_module=None, engine_group=None, supergroup=None) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `from_morphism(self, morphism)`
  > Return a live form automorphism as an element of this owned group.
- `@cached_method` `group_generators(self)`
- `inclusion(self)`
- `invariant_form(self)`
- `is_quadratic(self) -> bool`
- `normalization_isometry(self)`
- `number_of_group_generators(self)`
- `@cached_method` `one(self)`
- `orbit(self, element)`
- `order(self)`
- `stabilizer_of_element(self, element)`
- `stabilizer_of_subgroup(self, subgroup)`
- `subgroup_on(self, group_generators)`
- `super_categories(self)`
- `supergroup(self)`

### 📦 Mathematical Objects & Parents

#### `BilinearMap` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1198`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1198)
- **Bases**: `SageObject`

A bilinear map specified on the selected product framing.

- **Constructor**: `def __init__(self, left, right, codomain, generator_images) -> None`
- **Constructor**: `def __call__(self, left_element, right_element)`

**Public Methods:**
- `codomain(self)`
- `generator_image(self, left_label, right_label)`
- `generator_index_set(self)`
- `left_factor(self)`
- `right_factor(self)`

#### `CochainComplexElement` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L167`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L167)
- **Bases**: `GradedDirectSumElement`

#### `CochainComplexObject` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L171`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L171)
- **Bases**: `GradedDirectSumModule`

A nonnegative represented cochain complex with selected finite pieces.

- **Constructor**: `def __init__(self, base_ring, pieces, differentials, name=None) -> None`

**Public Methods:**
- `differential_component(self, degree)`
- `selected_degrees(self)`

#### `CochainDifferential` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L140)

The degree-``+1`` differential of a represented cochain complex.

- **Constructor**: `def __init__(self, complex_) -> None`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `complex(self)`
- `component(self, degree)`
- `degree_shift(self)`

#### `ConnectionDeRhamDifferential` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L492`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L492)

The covariant differential on ``E tensor_A Omega^*_{A/R}``.

- **Constructor**: `def __init__(self, module) -> None`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `degree_shift(self)`
- `module(self)`

#### `ConnectionDeRhamModule` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L515`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L515)

Factory namespace for a flat connection's de Rham DG-module.


#### `FractionalIdealElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L269`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L269)
- **Bases**: `ModuleElement`

An element of a fractional ideal, distinct from its image in the fraction field.

- **Constructor**: `def __init__(self, parent, value) -> None`

#### `FractionalIdealModule` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L296`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L296)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, base_ring, fraction_field, module_generator_values, *, integral) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `an_element(self)`
- `zero(self)`

#### `FreeModuleGeneratorSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L617`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L617)
- **Bases**: `Parent`

The image of the canonical basis map of a free module.

- **Constructor**: `def __init__(self, module) -> None`

**Public Methods:**
- `cardinality(self)`
- `position(self, element) -> int`

#### `FreeResolution` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L635`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L635)

The exact resolution ``0 -> F_1 -> F_0 -> M -> 0`` over a PID.


**Public Methods:**
- `augmentation(self)`
- `differential(self, degree)`
- `is_exact(self)`
- `length(self)`
- `module(self)`
- `term(self, degree)`

#### `GeneralLocalizedModuleElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/localizations.py#L46`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/localizations.py#L46)
- **Bases**: `ModuleElement`

A represented fraction ``m/s`` in ``S^{-1}M``.

- **Constructor**: `def __init__(self, parent, numerator, denominator) -> None`

**Public Methods:**
- `denominator(self)`
- `equality_status(self, other)`
  > Return ``True``, ``False``, or ``Unknown`` for fraction equality.
- `numerator(self)`

#### `GeneralLocalizedModuleParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/localizations.py#L115`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/localizations.py#L115)
- **Bases**: `Parent`

The explicit fraction model of ``S^{-1}M`` for a general live module.

- **Constructor**: `def __init__(self, source_module, localization_ring, localization_functor) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `base(self)`
- `base_ring(self)`
- `fraction(self, numerator, denominator=None, *, _trusted_denominator=False)`
- `is_finite(self)`
- `is_zero(self)`
  > Decide whether this localization is zero when the source is finite.
- `module_generating_set(self)`
- `module_generator(self, label)`
- `source_ring(self)`
- `zero(self)`

#### `GeneralModuleElement` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/general_modules.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/general_modules.py#L22)
- **Bases**: `ModuleElement`

One element of a module presented on an arbitrary set carrier.

- **Constructor**: `def __init__(self, parent, value) -> None`

**Public Methods:**
- `underlying_element(self)`

#### `GeneralModuleParent` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/general_modules.py#L69`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/general_modules.py#L69)
- **Bases**: `Parent`

A general ``R``-module carried by a represented set.

The defining data are additive operations on the carrier and a scalar
action.  After construction the action is stored as the actual morphism
``rho : R -> End_R(M)``; it is not merely a callback attached to the
parent.

- **Constructor**: `def __init__(self, ring, carrier, *, addition, zero, negation, scalar_action=None, rho=None, verify=True) -> None`
- **Constructor**: `def _element_constructor_(self, value)`
- **Constructor**: `def __call__(self, value)`

**Public Methods:**
- `annihilator(self)`
  > Return ``Ann_R(M)`` when the carrier and scalar ring are finite.
- `base(self)`
- `base_ring(self)`
- `cardinality(self)`
- `carrier(self)`
- `is_finite(self)`
- `scalar_action_input(self)`
  > Return the supplied ``rho`` when one was given explicitly.
- `zero(self)`

#### `GradedDirectSumElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_direct_sums.py#L24`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_direct_sums.py#L24)
- **Bases**: `ModuleElement`

A finite family of homogeneous components.

- **Constructor**: `def __init__(self, parent, components) -> None`

**Public Methods:**
- `degree(self)`
- `homogeneous_component(self, degree)`
- `homogeneous_components(self)`
- `is_homogeneous(self) -> bool`
- `monomial_coefficients(self)`

#### `GradedDirectSumModule` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/graded_direct_sums.py#L109`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_direct_sums.py#L109)
- **Bases**: `Parent`

The module \(\bigoplus_{d\geq0} M_d\) with finite-support elements.

- **Constructor**: `def __init__(self, base_ring, piece, name=None, realize_generator=None, realized_object=None, from_realization=None, degree_index_set=None) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `base_ring(self)`
- `degree_index_set(self)`
- `from_component(self, degree, component)`
- `from_components(self, components)`
- `from_realization(self, element)`
  > Decompose a realized element into its finite homogeneous support.
- `graded_piece(self, degree)`
- `linear_combination(self, coefficients)`
- `module_component(self, key)`
- `module_component_generator_label(self, label)`
- `module_component_key(self, label)`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `module_label_from_component(self, key, component_label)`
- `realize(self, element)`
  > Realize a finite family of homogeneous components in its target.
- `realize_module_generator(self, label)`
- `realized_object(self)`
- `scalar_multiple(self, scalar, element)`
- `zero(self)`

#### `IsotypicCharacter` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L19)

A coefficient-field irreducible character or a rational Galois orbit.

- **Constructor**: `def __call__(self, group_element)`

**Public Methods:**
- `degree(self)`
- `is_trivial(self) -> bool`

#### `OwnedFractionFieldQuotient` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L168`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L168)
- **Bases**: `Parent`

The preamble module ``QQ / n ZZ`` with a private QmodnZ backend.

- **Constructor**: `def __init__(self, engine: QmodnZ) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `an_element(self)`
- `zero(self)`

#### `RestrictedScalarsModuleView` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L895`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L895)
- **Bases**: `Parent`

A distinct parent for the same additive group with a restricted scalar action.

- **Constructor**: `def __init__(self, module, ring_map) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `an_element(self)`
- `framing_morphism(self)`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `@cached_method` `module_generators(self)`
- `wrap(self, underlying_element)`
  > Read an element of the extension module in this restricted module.
- `zero(self)`

#### `TorsionFormIsometry` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L113`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L113)
- **Bases**: `CategoricalIsomorphism`

An explicit isomorphism of finite framed torsion modules preserving a form.

- **Constructor**: `def __init__(self, parent, forward, inverse, *, quadratic: bool) -> None`

**Public Methods:**
- `is_quadratic(self) -> bool`

### 📚 Catalogues & Named Tables

#### `register_module_scalar_action` `[REGISTRY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L52`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L52)

Register ordinary ``r*m``/``m*r`` syntax for an owned module parent.


### 🛠 Helper Functions & Constructors

#### `AlgebraicCorrelationMorphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AlgebraicCorrelationMorphism(metric)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L214`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L214)

Return ``g^flat : M -> M^vee`` for a scalar-valued bilinear metric.


#### `AlternatingPower` `[FUNCTION]` `[Internal]`

- **Signature**: `def AlternatingPower(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L669`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L669)

Return ``Lambda^degree(module)`` from the selected module presentation.


#### `BasedFreeModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def BasedFreeModule(base_ring, rank_or_labels)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L774`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L774)

Return the selected based free module on a rank or explicit labels.


#### `BilinearForm` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def BilinearForm(module, value_module, datum)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1174`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1174)

Return ``module`` equipped with the stated bilinear form.


#### `Boundaries` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Boundaries(complex_, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L414`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L414)

Return ``im(d^(degree-1))`` as a subobject of ``C^degree``.


#### `CochainComplex` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CochainComplex(base_ring, pieces, differentials, name=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L405`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L405)

#### `Cohomology` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Cohomology(complex_, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L422`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L422)

Return ``H^degree = ker(d)/im(d)`` from finite presentations.

Let ``C^p = R^n/P`` and ``C^(p+1) = R^m/Q`` and let ``F`` be the matrix
of ``d^p`` on the selected generators.  Closed classes are represented by
the projection to ``R^n`` of

``ker [ F  -Q^t ]``.

Inside that free module of closed lifts, the denominator is generated by
the relation rows ``P`` and the columns of ``d^(p-1)``.  Expressing those
generators in a basis of the closed-lift module gives an ordinary finite
presentation of cohomology.  Thus the same construction works for free
complexes and for restricted-scalar de Rham pieces carrying relations.


#### `Connections` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda module: id(module))` `def Connections(module) -> ConnectionSpace`
- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L372`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L372)

#### `CorrelationIsomorphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CorrelationIsomorphism(metric)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L246`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L246)

Return the perfect correlation ``M ~= M^vee`` for a unimodular form.


#### `Cycles` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Cycles(complex_, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L409`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L409)

Return ``ker(d^degree)`` as a subobject of ``C^degree``.


#### `DeterminantLine` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def DeterminantLine(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L47`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L47)

Return ``det(module) = Lambda^rank(module) module``.


#### `DiscriminantModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def DiscriminantModule(lattice)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L828`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py#L828)

Return the literal cokernel of ``L -> L^#`` with descended forms when supported.


#### `DividedPower` `[FUNCTION]` `[Internal]`

- **Signature**: `def DividedPower(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L683`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L683)

Return the divided power ``Gamma^degree(module)``.

Degree two is the existing universal quadratic square; higher degrees use
the same divided-power-ideal presentation.


#### `DividedSquare` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda module: id(module))` `def DividedSquare(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L601`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L601)

Return ``Gamma^2_R(M)``, the universal target for quadratic maps.


#### `ExteriorForms` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ExteriorForms(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L55`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L55)

Return ``Lambda^degree(module^vee)``.


#### `FinitelyPresentedModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FinitelyPresentedModule(presentation)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py#L1585`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py#L1585)

Return ``coker(presentation)`` in ``R-Mod`` with its selected module presentation.


#### `FormModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FormModule(form)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1060`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1060)

Return the same represented module construction equipped with ``form``.

The result remains a module object; it is not a wrapper around an
``underlying`` module.  A distinct represented parent is used so that two
different selected forms on isomorphic modules remain distinct structured
objects.


#### `FractionFieldQuotient` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FractionFieldQuotient(base_ring, modulus=1)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L263`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py#L263)

Return ``Frac(base_ring) / modulus*base_ring`` when natively supported.


#### `FractionalIdeal` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FractionalIdeal(base_ring, module_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L758`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L758)

Return the fractional ideal of ``R`` spanned by the stated elements of ``Frac(R)``.


#### `FramingVolumeTrivialization` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FramingVolumeTrivialization(module, unit=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L89`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L89)

Explicitly trivialize ``det(M)`` using the selected framing.

This is deliberately opt-in: a chosen module framing is not silently
treated as orientation data.  ``unit`` rescales the selected top wedge and
must be a unit of the coefficient ring.


#### `FreeModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FreeModule(base_ring, rank_or_index_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L690`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L690)

Return the free module on a finite rank or an arbitrary index set.


#### `FreeModuleOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FreeModuleOn(base_ring, module_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L746`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L746)

Return \(F_R(S)\), retaining the actual labels in ``S``.


#### `FreshFreeModuleOn` `[FUNCTION]` `[Internal]`

- **Signature**: `def FreshFreeModuleOn(base_ring, module_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L758`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L758)

Return a new free-module parent on the specified basis labels.

Two different actions or forms on isomorphic free modules must remain
different structured objects, so the owned parent is not interned; the
engine underneath may be shared, since it holds no owned data.


#### `GeneralModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def GeneralModule(ring, carrier, *, addition, zero, negation, scalar_action=None, rho=None, verify=True)`
- **Source**: [`src/dzack_research/preamble/categories/modules/general_modules.py#L327`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/general_modules.py#L327)

Construct a general represented ``R``-module from its structure data.


#### `GroupLattice` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def GroupLattice(lattice, group_or_action, action=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_lattices.py#L90`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_lattices.py#L90)

Equip ``lattice`` with a selected action preserving its form.


#### `GroupModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def GroupModule(module, group_or_action, action=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L521`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L521)

Equip a finitely presented module with a specified left group action.

``GroupModule(M, rho)`` accepts a morphism ``rho`` whose domain is the
acting group and whose values act on ``M``.  ``GroupModule(M, G, action)``
accepts the equivalent binary action ``action(g, m)``.  The resulting
parent is a distinct structured module; the selected module labels are
transported unchanged.


#### `HodgeDiscriminant` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def HodgeDiscriminant(metric, volume)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L271`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L271)

Return ``Delta_(g,eps) = det(g) / eps(e_1 wedge ... wedge e_n)^2``.


#### `HodgeStar` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def HodgeStar(metric, volume, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L278`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L278)

Return the Hodge isomorphism on covariant ``degree``-forms.

For a perfect metric this is the categorical composite

``Lambda^k M^vee --Lambda^k(g^sharp)--> Lambda^k M --PD--> Lambda^(n-k) M^vee``.


#### `HodgeStarOverFractionField` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def HodgeStarOverFractionField(metric, volume, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L333`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L333)

Return the covariant-form Hodge isomorphism after ``R -> Frac(R)``.

This is the explicit scalar-extension path for a nondegenerate but
non-unimodular metric.  The returned isomorphism lives over the fraction
field; it is never reported as an integral Hodge star on ``metric``.


#### `Ideal` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Ideal(base_ring, module_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/fractional_ideals.py#L783`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/fractional_ideals.py#L783)

Return the integral ideal of ``R`` generated by the stated elements.


#### `InternalHom` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def InternalHom(source, target)`
- **Source**: [`src/dzack_research/preamble/categories/modules/internal_hom.py#L100`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/internal_hom.py#L100)

Return the enriched Hom object ``source.Hom(target)``.

The categorical Hom-set is always the mathematical carrier.  For a
selected presentation ``F1 -> F0 -> source``, this function additionally
computes the finite presentation
``ker(Hom(F0,target) -> Hom(F1,target))`` and installs that presentation on
the same Hom parent.  The temporary quotient module is only a computational
model for the presentation and never escapes as a second Hom object.


#### `MatrixSpace` `[FUNCTION]` `[Internal]`

- **Signature**: `def MatrixSpace(base_ring, nrows, ncols=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L704`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L704)

Return ``Hom_R(F_R([n]), F_R([m]))`` for ``m=nrows``, ``n=ncols``.


#### `ModuleWithConnection` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ModuleWithConnection(connection)`
- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L454`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L454)

Return a fresh finite-free module carrying the selected connection.


#### `MultivectorHodgeStar` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def MultivectorHodgeStar(metric, volume, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L306`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L306)

Return the integral multivector Hodge map ``Lambda^k M -> Lambda^(n-k) M``.

Unlike the covariant-form Hodge star, this direction uses ``g^flat`` and
therefore does not require the metric to be perfect over the coefficient
ring.  It need not be an isomorphism for a non-unimodular metric.


#### `PoincareDuality` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def PoincareDuality(module, volume, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L142`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L142)

Return ``Lambda^k M ~= Lambda^(n-k) M^vee`` from ``volume``.


#### `QuadraticForm` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def QuadraticForm(module, value_module, datum)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1181`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1181)

Return ``module`` equipped with the stated quadratic form.


#### `SymmetricPower` `[FUNCTION]` `[Internal]`

- **Signature**: `def SymmetricPower(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L655`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L655)

Return ``Sym^degree(module)`` from the selected module presentation.


#### `TensorPower` `[FUNCTION]` `[Internal]`

- **Signature**: `def TensorPower(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L633`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L633)

Return the selected iterated tensor power ``M^{\otimes degree}``.


#### `TorsionModule` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def TorsionModule(presentation)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L169`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L169)

#### `VolumeTrivialization` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def VolumeTrivialization(module, forward, inverse)`
- **Source**: [`src/dzack_research/preamble/categories/modules/hodge.py#L66`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/hodge.py#L66)

Return the stated isomorphism ``det(module) ~= R``.

No orientation or volume is inferred from a framing.  This constructor
merely verifies two already represented mutually inverse module maps.


#### `alternating_power_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def alternating_power_morphism(morphism, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L886`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L886)

#### `alternating_power_product` `[FUNCTION]` `[Internal]`

- **Signature**: `def alternating_power_product(module, left_degree, left, right_degree, right)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L949`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L949)

Multiply homogeneous exterior-power elements by the wedge product.


#### `base_change_codomain` `[FUNCTION]` `[Internal]`

- **Signature**: `def base_change_codomain(module, ring_map)`
- **Source**: [`src/dzack_research/preamble/categories/modules/base_change.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/base_change.py#L11)

Validate ``R -> S`` against ``module`` and return the owned ring ``S``.


#### `base_change_scalar` `[FUNCTION]` `[Internal]`

- **Signature**: `def base_change_scalar(ring_map, scalar)`
- **Source**: [`src/dzack_research/preamble/categories/modules/base_change.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/base_change.py#L22)

Apply ``R -> S`` and return the resulting element of the owned ring ``S``.


#### `biproduct_morphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def biproduct_morphism(left_morphism, right_morphism, source=None, target=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1666`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1666)

#### `cochain_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def cochain_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/modules/cochain_complexes.py#L395`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/cochain_complexes.py#L395)

#### `connection_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def connection_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/modules/connections.py#L450`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/connections.py#L450)

#### `divided_power_element` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_power_element(module, degree, element)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L1026`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L1026)

Return ``gamma_degree(element)`` in ``Gamma^degree(module)``.


#### `divided_power_invariant_inclusion` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_power_invariant_inclusion(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L1064`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L1064)

Return ``Gamma^n M -> M^{tensor n}`` as the symmetric orbit sum.


#### `divided_power_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_power_morphism(morphism, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L890`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L890)

#### `divided_power_product` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_power_product(module, left_degree, left, right_degree, right)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L897`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L897)

Multiply homogeneous divided-power elements into ``Gamma^{a+b} M``.


#### `divided_square_invariant_inclusion` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_square_invariant_inclusion(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L1162`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L1162)

#### `divided_square_morphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def divided_square_morphism(morphism, source=None, target=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L617`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L617)

Return ``Gamma^2(f)`` for a module morphism ``f``.


#### `fibered_formed_module_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def fibered_formed_module_homset(domain, codomain, ring_map) -> FiberedFormedModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L524`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L524)

Return formed morphisms ``domain -> codomain`` lying over ``ring_map``.


#### `form_embedding` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def form_embedding(domain, codomain, images, *, quadratic: bool | None=None) -> FormEmbedding`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L76`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L76)

Construct a form-preserving monomorphism on a chosen framing.

The underlying module homset checks linearity and the selected relations.
The embedding specialization checks preservation of ``b`` or ``q`` on the
finite framing.  This works for both represented :class:`FormModule`
objects and discriminant-form objects, which intentionally have their own
structured-category realization rather than being wrappers around one.


#### `formed_module_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def formed_module_homset(domain, codomain) -> FormedModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L299`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L299)

#### `framing_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def framing_morphism(domain, codomain, images) -> FramingMorphism`
- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1174`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1174)

#### `free_resolution` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def free_resolution(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L703`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L703)

#### `graded_module_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def graded_module_homset(domain, codomain) -> GradedModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L179`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L179)

#### `group_module_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def group_module_homset(domain, codomain) -> GroupModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L513`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L513)

#### `internal_hom_morphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def internal_hom_morphism(source_internal_hom, target_internal_hom, source_map, target_map)`
- **Source**: [`src/dzack_research/preamble/categories/modules/internal_hom.py#L236`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/internal_hom.py#L236)

Return the map on internal Homs induced by pre- and postcomposition.

``source_map`` runs from the new source to the old source and
``target_map`` from the old target to the new target, so the result is
``h |-> target_map * h * source_map``.


#### `is_form_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def is_form_morphism(morphism) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1252`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py#L1252)

#### `isotypic_component` `[FUNCTION]` `[Internal]`

- **Signature**: `def isotypic_component(module, character)`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L202`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L202)

Return ``M ∩ V_character`` as a subobject of ``M``.


#### `isotypic_decomposition` `[FUNCTION]` `[Internal]`

- **Signature**: `def isotypic_decomposition(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L238`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/isotypic.py#L238)

Return ``⊕ M_chi -> M`` with its selected summand structure.


#### `matrix_change_ring` `[FUNCTION]` `[Internal]`

- **Signature**: `def matrix_change_ring(matrix, ring)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L734`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L734)

Return the same finite coordinate matrix over ``ring``.


#### `module_coefficients` `[FUNCTION]` `[Internal]`

- **Signature**: `def module_coefficients(element, module=None) -> dict`
- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L125`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L125)

Return coefficients in the selected framing of the stated module.

``module`` is normally ``element.parent()``.  It is explicit at facade
boundaries such as number-field orders, whose Sage elements retain the
number field as their concrete parent even when regarded as elements of
the order.


#### `module_embedding` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def module_embedding(domain, codomain, images, *, verify_linearity=True) -> ModuleEmbedding`
- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1180`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1180)

Construct a declared module monomorphism on a chosen framing.


#### `module_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def module_homset(domain, codomain) -> ModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1165`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py#L1165)

#### `module_subobject_on` `[FUNCTION]` `[Internal]`

- **Signature**: `def module_subobject_on(module, module_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L480`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L480)

Return the submodule spanned by one explicitly finite family.

The finite PID backend is restricted to the union of supports of the input
elements.  In particular, a finitely generated submodule of an infinitely
generated free module never causes enumeration of the ambient framing.


#### `normalize_grading_monoid` `[FUNCTION]` `[Internal]`

- **Signature**: `def normalize_grading_monoid(monoid: Parent | None) -> Parent`
- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L30)

Return the owned grading monoid, defaulting to \(\mathbb{Z},+\).


#### `p_adic_jordan_module_generators` `[FUNCTION]` `[Internal]`

- **Signature**: `def p_adic_jordan_module_generators(form, *, quadratic: bool)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L505`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L505)

Return the selected Jordan generators, prime by prime, inside ``form``.


#### `refine_finitely_presented_torsion_module` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_finitely_presented_torsion_module(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L179`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/torsion_modules.py#L179)

Attach the torsion intersection after verifying the represented property.


#### `regular_dg_module` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def regular_dg_module(dga)`
- **Source**: [`src/dzack_research/preamble/categories/modules/dg_modules.py#L62`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/dg_modules.py#L62)

Read a DGA as its canonical right DG-module over itself.


#### `require_grading_monoid` `[FUNCTION]` `[Internal]`

- **Signature**: `def require_grading_monoid(monoid: Parent | None) -> Parent`
- **Source**: [`src/dzack_research/preamble/categories/modules/graded_modules.py#L35`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/graded_modules.py#L35)

#### `restrict_scalars` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def restrict_scalars(module, ring_map)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1148`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1148)

Return ``Res_R^S(module)`` along the specified morphism ``R -> S``.


#### `ring_as_module` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def ring_as_module(ring)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L782`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py#L782)

Return the canonical free rank-one module of a ring over itself.


#### `symmetric_power_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def symmetric_power_morphism(morphism, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L882`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L882)

#### `tensor_power_permutation` `[FUNCTION]` `[Internal]`

- **Signature**: `def tensor_power_permutation(module, degree, positions)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L709`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L709)

Return the permutation of tensor factors specified by ``positions``.


#### `tensor_power_polarization` `[FUNCTION]` `[Internal]`

- **Signature**: `def tensor_power_polarization(module, degree)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L1124`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L1124)

Return ``M^{tensor n} -> Gamma^n M`` by divided-power multiplication.


#### `tensor_product_morphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def tensor_product_morphism(left_morphism, right_morphism, source=None, target=None)`
- **Source**: [`src/dzack_research/preamble/categories/modules/tensor_products.py#L56`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/tensor_products.py#L56)

Return ``f tensor g`` on the chosen tensor products.


#### `tensor_square_polarization` `[FUNCTION]` `[Internal]`

- **Signature**: `def tensor_square_polarization(module)`
- **Source**: [`src/dzack_research/preamble/categories/modules/powers.py#L1166`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/powers.py#L1166)

#### `torsion_form_isometry` `[FUNCTION]` `[Internal]`

- **Signature**: `def torsion_form_isometry(forward, inverse, *, quadratic: bool)`
- **Source**: [`src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L142`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py#L142)

Return the form isometry represented by mutually inverse module maps.


#### `trivial_group_action` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def trivial_group_action(module, group)`
- **Source**: [`src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L606`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/group_modules/group_modules.py#L606)

Equip ``module`` with the trivial action of ``group``.


#### `twist_scalar_action` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def twist_scalar_action(module, ring_endomorphism)`
- **Source**: [`src/dzack_research/preamble/categories/modules/pure/modules.py#L1158`](file:///home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.py#L1158)

Twist the scalar action of an ``R``-module along ``R -> R``.

This is restriction of scalars along an endomorphism of the scalar ring;
it is unrelated to ``L.twist(a)``, which rescales a lattice form while
leaving its scalar action unchanged.



---

<a id="subsystem-algebras"></a>
## Algebras & Differential Graded Algebras

> Associative/Commutative algebras, DGAs, Cohomology algebras, De Rham algebras, Derivations, and Graded algebras.

### 🏛 Categories & Subcategories

#### `AlgebraHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L74`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L74)
- **Bases**: `HomCategoryConstruction`

The fixed-endpoint Hom categories of associative unital ``R``-algebras.


**Category Instance Methods:**
- `Of(self, domain, codomain)`

#### `Algebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L93`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L93)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[OwnedRings(), AssociativeAlgebras(self.base_ring()), Modules(self.base_ring())]`

Associative unital algebras over ``R``.

The structure morphism is \(\eta\colon R\to Z(A)\).  The forgetful
functor \(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\) is
:func:`~dzack_research.preamble.categories.functors.algebra_modules.algebra_underlying_module_functor`.
Multiplication is the \(R\)-module morphism
\(m\colon A\otimes_R A\to A\).


**Object Constructor (Calling Category on Data):**
- `Algebras(...)(self, multiplication)`

**ParentMethods (Methods on Category Objects):**
- `Hom(self, codomain, category=None)`
- `algebra_base_ring(self)`
- `@cached_method` `algebra_structure_morphism(self)`
  > The structure morphism \(\eta\colon R\to Z(A)\) of this \(R\)-algebra.
- `base_ring(self)`
- `is_algebra(self) -> bool`
- `@cached_method` `multiplication_morphism(self)`
  > The multiplication \(m\colon A\otimes_R A\to A\) as an \(R\)-module morphism.

**Category Instance Methods:**
- `homset(self, domain, codomain)`
  > Return the unique Hom-set ``Hom_{R-Alg}(domain,codomain)``.
- `super_categories(self)`

#### `AlgebrasWithChosenFinitePresentation` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L420`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L420)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedAlgebras(self.base_ring()), FramedAlgebras(self.base_ring())]`

Finitely presented algebras carrying one selected finite presentation.


**ParentMethods (Methods on Category Objects):**
- `algebra_presentation_morphism(self)`
- `base_change(self, ring_map)`
- `lift_to_presentation(self, element)`
- `presentation(self)`
- `presentation_ideal(self)`
- `presentation_ring(self)`
- `relations(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AlgebrasWithChosenMultiplication` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L221`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L221)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[AssociativeAlgebrasWithChosenMultiplication(self.base_ring()), Algebras(self.base_ring())]`

Unital algebras interned on a chosen morphism \(A\otimes_R A\to A\).


**ParentMethods (Methods on Category Objects):**
- `multiplication_morphism(self)`
- `one(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AlternatingAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L531`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L531)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[StrictlyGradedCommutativeAlgebras(self.base_ring())]`

Exterior/alternating algebras.


**ParentMethods (Methods on Category Objects):**
- `free_source_module(self)`
- `graded_piece(self, degree)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AssociativeAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L30)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Associative \(R\)-algebras, not necessarily unital.

An associative algebra is an \(R\)-module with an associative bilinear
product. A unit is extra structure: the owned unital category is
:class:`Algebras`. Convolution \(L^1(\mathbb R)\) is the standard
non-unital example.


**Object Constructor (Calling Category on Data):**
- `AssociativeAlgebras(...)(self, multiplication)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AssociativeAlgebrasWithChosenMultiplication` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L54`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L54)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[AssociativeAlgebras(self.base_ring())]`

Associative algebras interned on a chosen morphism \(A\otimes_R A\to A\).


**ParentMethods (Methods on Category Objects):**
- `multiplication_morphism(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AugmentedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L23`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L23)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

Associative unital \(R\)-algebras equipped with an augmentation.

An \(R\)-algebra is a ring \(A\) together with a ring homomorphism
\(R\to A\). If it is further equipped with an \(R\)-algebra homomorphism
the other way,
\[
\varepsilon\colon A\to R,
\]
then it is an *augmented* \(R\)-algebra. The kernel of \(\varepsilon\) is
the augmentation ideal. This is the nLab definition of an augmented
algebra (Cartan–Eilenberg: a supplemented algebra).


**Object Constructor (Calling Category on Data):**
- `AugmentedAlgebras(...)(self, augmentation)`

**ParentMethods (Methods on Category Objects):**
- `@cached_method` `augmentation(self)`
- `is_augmented(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `CohomologyAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L16`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L16)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[StrictlyGradedCommutativeAlgebras(self.base_ring())]`

Graded algebras ``H^*(B)`` represented from a DGA ``B``.


**ParentMethods (Methods on Category Objects):**
- `source_dga(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeAlgebraCoproducts` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L519`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L519)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[CommutativeAlgebras(self.base_ring())]`

Commutative ``R``-algebras equipped as selected binary coproducts.


**ParentMethods (Methods on Category Objects):**
- `coproduct_factors(self)`
- `coproduct_injection(self, index)`
- `coproduct_injections(self)`
- `from_cocone(self, left_map, right_map)`
- `left_coproduct_map(self)`
- `right_coproduct_map(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeAlgebraPushouts` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L565`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L565)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[CommutativeAlgebras(self.base_ring())]`

Commutative ``R``-algebras equipped as selected pushouts of one span.


**ParentMethods (Methods on Category Objects):**
- `from_pushout_cocone(self, left_map, right_map)`
- `left_pushout_map(self)`
- `pushout_maps(self)`
- `pushout_span(self)`
- `right_pushout_map(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L260`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L260)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring()), OwnedCommutativeRings()]`

Commutative associative unital algebras over ``R``.


**ParentMethods (Methods on Category Objects):**
- `is_commutative(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeDifferentialGradedAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L128`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L128)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[DifferentialGradedAlgebras(self.base_ring()), GradedCommutativeAlgebras(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutatorLieAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/lie_algebras.py#L28`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/lie_algebras.py#L28)
- **Bases**: `LieAlgebras`
- **Super Categories**: `[LieAlgebras(self.base_ring()), AssociativeAlgebras(self.base_ring())]`

Associative algebras with bracket ``[x,y]=xy-yx``.


**ElementMethods (Methods on Category Elements):**
- `bracket(self, other)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DGAHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L256`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L256)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `DeRhamAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/de_rham_algebras.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/de_rham_algebras.py#L22)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[StrictlyCommutativeDifferentialGradedAlgebras(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `de_rham_source_algebra(self)`
- `kahler_differentials(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `DifferentialGradedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L78)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring()), CochainComplexes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `d(self, element)`
- `differential(self)`
- `differential_component(self, degree)`

**Category Instance Methods:**
- `homset(self, domain, codomain)`
- `super_categories(self)`

#### `DividedPowerAlgebras` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L700`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L700)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring()), CommutativeAlgebras(self.base_ring())]`

Divided-power algebras ``Gamma(M)`` with their canonical grading.


**ParentMethods (Methods on Category Objects):**
- `free_source_module(self)`
- `graded_piece(self, degree)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelyPresentedAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L405`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L405)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

Algebras that admit a finite algebra presentation.


**ParentMethods (Methods on Category Objects):**
- `is_finitely_presented(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `FramedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L310`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L310)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

Algebras carrying a chosen algebra generating set.


**ParentMethods (Methods on Category Objects):**
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`
- `@cached_method` `algebra_generators(self)`
- `number_of_algebra_generators(self)`
- `product_on_algebra_generators(self, left, right)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FreeAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L380`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L380)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `is_free(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `GradedAlgebraHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_algebras.py#L135`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_algebras.py#L135)
- **Bases**: `HomCategoryConstruction`

**Category Instance Methods:**
- `fixed_category_class(self)`

#### `GradedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_algebras.py#L153`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_algebras.py#L153)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[algebra, graded_modules]`

Associative unital algebras graded by a monoid.

Let \(M\) be a monoid. An \(M\)-graded \(R\)-algebra is an associative
unital \(R\)-algebra \(A\) together with a direct-sum decomposition
\(A = \bigoplus_{m \in M} A_m\) of the underlying module such that the
product sends \(A_m \times A_{m'}\) into \(A_{mm'}\).

The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
algebra axiom. The additive monoid \(\mathbb{N}\) is the nonnegative
case. This is the nLab definition of a graded algebra; Stacks Project
tag 00JL is the special case \(M = \mathbb{N}\).

**Category Constructor:**
- `GradedAlgebras(self, base_ring, grading_monoid: Parent) -> None`

**Object Constructor (Calling Category on Data):**
- `GradedAlgebras(...)(self, multiplication)`

**ParentMethods (Methods on Category Objects):**
- `homogeneous_degree(self, element)`
  > Return the selected degree of one nonzero homogeneous element.

**ElementMethods (Methods on Category Elements):**
- `degree(self)`
- `is_homogeneous(self)`

**Category Instance Methods:**
- `grading_monoid(self) -> Parent`
- `homset(self, domain, codomain)`
- `super_categories(self)`

#### `GradedAugmentedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L58`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L58)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring(), self.grading_monoid()), AugmentedAlgebras(self.base_ring())]`

Graded algebras over an augmented \(R\)-algebra.

Let \(B\) be an augmented \(R\)-algebra and let \(A\) be a graded
\(B\)-algebra that is itself augmented over \(B\). The composite of
the two augmentations is an augmentation of \(A\) over \(R\):
\[
A \to B \to R.
\]
For a connected grading, \(B = A_u = R\) and the second map is the
identity. This is the nLab graded-plus-augmented situation
(Cartan–Eilenberg: a supplemented graded algebra).

**Category Constructor:**
- `GradedAugmentedAlgebras(self, base_ring, grading_monoid) -> None`

**ParentMethods (Methods on Category Objects):**
- `ground_ring_augmentation(self)`
  > The composite augmentation \(A\to A_u\to R\).

**Category Instance Methods:**
- `grading_monoid(self)`
- `super_categories(self)`

#### `GradedCommutativeAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py#L20)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring(), self.grading_monoid())]`
**Category Constructor:**
- `GradedCommutativeAlgebras(self, base_ring, grading_monoid) -> None`

**Category Instance Methods:**
- `grading_monoid(self)`
- `super_categories(self)`

#### `GradedFreeAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L398`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L398)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `graded_piece(self, degree)`
  > Return the canonical degree piece of this free construction.

**Category Instance Methods:**
- `super_categories(self)`

#### `KahlerDifferentialModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/kahler_differentials.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/kahler_differentials.py#L20)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FinitelyPresentedModules(self.base_ring()), FramedModules(self.base_ring())]`

Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``.


**ParentMethods (Methods on Category Objects):**
- `derivation_classifier_isomorphism(self, target_module)`
  > Return ``Hom_A(Omega^1_{A/R},M) ~= Der_R(A,M)`` as an ``A``-module isomorphism.
- `differential_generator(self, algebra_generator_label)`
- `from_derivation(self, derivation)`
- `source_algebra(self)`
- `universal_derivation(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `LieAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/lie_algebras.py#L9`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/lie_algebras.py#L9)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Lie algebras over a commutative owned base ring.


**ParentMethods (Methods on Category Objects):**
- `bracket(self, left, right)`

**Category Instance Methods:**
- `super_categories(self)`

#### `MatrixAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L348`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L348)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[MatrixEndomorphismSpaces(self.base_ring()), Algebras(self.base_ring()), FramedAlgebras(self.base_ring())]`

Finite matrix endomorphism Hom objects with their canonical algebra structure.


**ParentMethods (Methods on Category Objects):**
- `algebra_base_ring(self)`
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L992`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L992)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

Algebras carrying their chosen structure map ``R -> Z(A)``.


**Category Instance Methods:**
- `super_categories(self)`

#### `RestrictedScalarsAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/restricted_scalars.py#L40`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/restricted_scalars.py#L40)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Algebras(self.base_ring())]`

``R``-algebras obtained by restricting an algebra along ``R -> S``.


**ParentMethods (Methods on Category Objects):**
- `algebra_over_extension(self)`
  > Return the original ``S``-algebra before scalar restriction.
- `extension_ring(self)`
- `restricted_algebra_generator_labels(self)`
- `restricted_scalar_generator_labels(self)`
- `ring_map(self)`
  > Return the selected scalar map ``R -> S``.

**Category Instance Methods:**
- `super_categories(self)`

#### `StrictlyCommutativeDifferentialGradedAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L142`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L142)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[CommutativeDifferentialGradedAlgebras(self.base_ring()), StrictlyGradedCommutativeAlgebras(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `StrictlyGradedCommutativeAlgebras` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py#L52`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py#L52)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedCommutativeAlgebras(self.base_ring(), self.grading_monoid())]`
**Category Constructor:**
- `StrictlyGradedCommutativeAlgebras(self, base_ring, grading_monoid) -> None`

**Category Instance Methods:**
- `grading_monoid(self)`
- `super_categories(self)`

#### `SymmetricAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L496`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L496)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring()), CommutativeAlgebras(self.base_ring())]`

Symmetric algebras of represented modules.


**ParentMethods (Methods on Category Objects):**
- `free_source_module(self)`
  > Return the module whose symmetric algebra this object represents.

**Category Instance Methods:**
- `super_categories(self)`

#### `TensorAlgebras` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L476`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L476)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[GradedAlgebras(self.base_ring())]`

Tensor algebras of represented modules.


**ParentMethods (Methods on Category Objects):**
- `free_source_module(self)`
  > Return the module whose tensor algebra this object represents.

**Category Instance Methods:**
- `super_categories(self)`

### 🔄 Functors & Adjunctions

#### `RingAdjunctionConstructions` `[ADJUNCTION]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L62`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L62)
- **Bases**: `Category`

Rings equipped with selected polynomial/algebraic adjunction syntax.


**Functor / Adjunction Methods:**
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `AlgebraHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L941`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L941)
- **Bases**: `_AlgebraHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `identity(self)`

#### `AlgebraMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L633`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L633)
- **Bases**: `Morphism`

An ``R``-algebra morphism specified by the images of algebra generators.

- **Constructor**: `def __init__(self, parent, images) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `algebra_generator_morphism(self)`
- `morphisms_agree(self, other) -> bool`

#### `CohomologyAlgebraHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L149`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L149)
- **Bases**: `Homset`
- **Constructor**: `def _element_constructor_(self, dga_morphism)`

**Public Methods:**
- `identity(self)`

#### `CohomologyAlgebraMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L107)
- **Bases**: `Morphism`

The graded algebra morphism induced on cohomology by a DGA morphism.

- **Constructor**: `def __init__(self, parent, dga_morphism) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `underlying_dga_morphism(self)`

#### `ConstructionAlgebraHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L47`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L47)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, evaluator)`

#### `ConstructionAlgebraMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L26)
- **Bases**: `Morphism`

An algebra morphism whose action is determined by a construction map.

- **Constructor**: `def __init__(self, parent, evaluator) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

#### `DGAHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L233`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L233)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, function)`

**Public Methods:**
- `identity(self)`

#### `DGAMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L171`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L171)
- **Bases**: `Morphism`
- **Constructor**: `def __init__(self, parent, function) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `component(self, degree)`
  > Return the degree-``degree`` linear component of this DGA map.

#### `DegreewiseLinearMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L17`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L17)
- **Bases**: `Morphism`

An ``R``-linear map between two represented homogeneous pieces.

This is deliberately independent of a selected finite framing. When the
source and target pieces admit the finite module-morphism backend,
:meth:`represented_module_morphism` exposes it and therefore enables the
usual kernel/image algorithms; otherwise the component remains a genuine
morphism with exact evaluation but no fabricated finite presentation.

- **Constructor**: `def __init__(self, domain, codomain, function) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `image(self)`
- `kernel(self)`
- `represented_module_morphism(self)`

#### `Derivation` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L78)
- **Bases**: `Morphism`

An actual ``R``-linear arrow ``A -> Res_R(M)`` satisfying Leibniz.

The public codomain of a derivation remains the original ``A``-module
``M``.  :meth:`underlying_linear_morphism` is the corresponding element of
the canonical ``Hom_R(A, Res_R(M))`` containing this derivation subobject.

- **Constructor**: `def __init__(self, parent, generator_images) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `codomain(self)`
- `domain(self)`
- `generator_image(self, label)`
- `restricted_codomain(self)`
- `underlying_linear_morphism(self)`

#### `DerivationSpace` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L236`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L236)
- **Bases**: `Homset`

The ``A``-module ``Der_R(A,M)`` with its restricted Hom inclusion.

The actual subobject of ``Hom_R(A,Res_R M)`` is
``Res_R Der_R(A,M)``.  Keeping these two scalar structures distinct is
essential: the derivation module is canonically an ``A``-module, whereas
its inclusion into the ambient Hom is only ``R``-linear.

- **Constructor**: `def __init__(self, algebra, target_module) -> None`
- **Constructor**: `def _element_constructor_(self, generator_images)`

**Public Methods:**
- `algebra(self)`
- `algebra_action(self)`
- `algebra_multiple(self, scalar, derivation)`
- `ambient_hom(self)`
- `base_ring(self)`
- `generator_labels(self)`
- `inclusion(self)`
- `restricted_module(self)`
- `restricted_target_module(self)`
- `scalar_multiple(self, scalar, derivation)`
- `target_module(self)`
- `zero(self)`

#### `DifferentialComponentMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L74`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L74)
- **Bases**: `DegreewiseLinearMorphism`

A degreewise component of a represented DGA differential.


#### `FramedFreeAlgebraHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L857`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L857)
- **Bases**: `_AlgebraHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `identity(self)`

#### `FramedFreeAlgebraMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L744`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L744)
- **Bases**: `AlgebraMorphism`

A generator-defined map from a framed free algebra to any algebra.

- **Constructor**: `def __init__(self, parent, images) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

#### `GradedAlgebraHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_algebras.py#L98`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_algebras.py#L98)
- **Bases**: `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `grading_monoid(self)`
- `identity(self)`

#### `GradedAlgebraMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_algebras.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_algebras.py#L33)
- **Bases**: `Morphism`

An algebra morphism preserving the selected grading.

- **Constructor**: `def __init__(self, parent, images, *, check_degrees=True) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `underlying_algebra_morphism(self)`

#### `GradedDerivation` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L370`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L370)
- **Bases**: `ModuleMorphism`

A homogeneous graded derivation of a represented graded algebra.

For shift ``r`` this represents a map ``D : A^p -> M^(p+r)`` satisfying
``D(ab) = D(a)b + (-1)^(r p) a D(b)`` on homogeneous ``a``.  It is an
actual ``R``-linear morphism, lying in a represented submodule of
``Hom_R(A,M)``.

- **Constructor**: `def __init__(self, parent, function) -> None`

**Public Methods:**
- `algebra(self)`
- `check_on_generators(self) -> bool`
  > Check degree and graded Leibniz on a selected finite algebra framing.
- `degree_shift(self)`
- `target(self)`
- `underlying_linear_morphism(self)`

#### `GradedDerivationSpace` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L445`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L445)
- **Bases**: `Homset`

The ``R``-submodule of degree-``r`` graded derivations in ``Hom_R``.

- **Constructor**: `def __init__(self, algebra, target, shift) -> None`
- **Constructor**: `def _element_constructor_(self, function)`

**Public Methods:**
- `algebra(self)`
- `ambient_hom(self)`
- `base_ring(self)`
- `degree_shift(self)`
- `elementwise(self, function)`
- `inclusion(self)`
- `scalar_multiple(self, scalar, derivation)`
- `target(self)`
- `zero(self)`

#### `PowerAlgebraHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L298`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L298)
- **Bases**: `OwnedHomset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, degree_one_map)`

**Public Methods:**
- `identity(self)`

#### `PowerAlgebraMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L225`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L225)
- **Bases**: `Morphism`

A morphism induced by a linear map on the degree-one generators.

- **Constructor**: `def __init__(self, parent, degree_one_map) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `degree_one_map(self)`

#### `PresentedAlgebraHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L920`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L920)
- **Bases**: `_AlgebraHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `identity(self)`

#### `PresentedAlgebraMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L842`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L842)
- **Bases**: `Morphism`

A map from an algebra with a chosen finite presentation.

The map is defined on the presentation algebra, its selected relations are
checked once, and evaluation descends by the chosen quotient projection.
No Sage target-ring protocol is involved.

- **Constructor**: `def __init__(self, parent, images) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `algebra_generator_morphism(self)`
- `morphisms_agree(self, other) -> bool`

#### `SparseFreeAlgebraHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L840`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L840)
- **Bases**: `_AlgebraHomsetCommonMethods`, `CategoricalHomset`
- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images)`

**Public Methods:**
- `identity(self)`

#### `SparseFreeAlgebraMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L748`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L748)
- **Bases**: `Morphism`
- **Constructor**: `def __init__(self, parent, images) -> None`
- **Constructor**: `def _call_(self, element)`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `morphisms_agree(self, other) -> bool`

### 📦 Mathematical Objects & Parents

#### `CohomologyAlgebraElement` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L33)
- **Bases**: `GradedDirectSumElement`

#### `Differential` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L156)
- **Bases**: `GradedDerivation`

A represented degree-one square-zero graded derivation.

- **Constructor**: `def __init__(self, algebra, function) -> None`

#### `PowerAlgebra` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L54`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L54)
- **Bases**: `GradedDirectSumModule`

The graded algebra ``Lambda(M)`` or ``Gamma(M)``.

- **Constructor**: `def __init__(self, module, flavor) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `algebra_base_ring(self)`
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`
- `augmentation(self, value)`
- `divided_power(self, value, exponent)`
- `flavor(self)`
- `free_source_module(self)`
- `multiply(self, left, right)`
- `number_of_algebra_generators(self)`
- `one(self)`
- `ring_center(self)`

#### `PowerAlgebraElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L47`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L47)
- **Bases**: `GradedDirectSumElement`

An element of a power algebra, using graded-direct-sum storage.


#### `RestrictedGradedAlgebra` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L26)
- **Bases**: `GradedDirectSumModule`

The same graded ring read over the constants of its degree-zero algebra.

- **Constructor**: `def __init__(self, extension_algebra, ring_map) -> None`

**Public Methods:**
- `algebra_base_ring(self)`
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`
- `algebra_structure_morphism(self)`
- `degree_zero_algebra(self)`
- `degree_zero_element(self, element)`
- `extension_algebra(self)`
- `from_degree_zero(self, element)`
- `multiply(self, left, right)`
- `one(self)`
- `realize(self, element)`
  > Return the same finite homogeneous sum in the extension algebra.
- `ring_map(self)`

#### `RestrictedGradedAlgebraElement` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L21`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L21)
- **Bases**: `GradedDirectSumElement`

#### `SparseFreeAlgebra` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L260`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L260)
- **Bases**: `Parent`

A free algebra whose elements are finite sums of sparse monomials.

- **Constructor**: `def __init__(self, module, flavor) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`
- `base_ring(self)`
- `basis_label(self, degree, degree_label)`
- `degree_basis(self, degree)`
- `flavor(self)`
- `free_source_module(self)`
- `graded_piece(self, degree)`
- `linear_combination(self, coefficients)`
- `module_component(self, key)`
- `module_component_generator_label(self, label)`
- `module_component_key(self, label)`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `module_label_from_component(self, key, component_label)`
- `multiply(self, left, right)`
- `one(self)`
- `ring_center(self)`
- `scalar_multiple(self, scalar, element)`
- `zero(self)`

#### `SparseFreeAlgebraDegreeElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L136`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L136)
- **Bases**: `ModuleElement`

An element of one homogeneous piece of a sparse free algebra.

- **Constructor**: `def __init__(self, parent, algebra_element) -> None`

**Public Methods:**
- `algebra_element(self)`
- `monomial_coefficients(self)`

#### `SparseFreeAlgebraDegreeModule` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L188`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L188)
- **Bases**: `Parent`

One exact homogeneous module of a sparse free algebra.

- **Constructor**: `def __init__(self, algebra, degree) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `algebra(self)`
- `base_ring(self)`
- `degree(self)`
- `from_algebra_element(self, element)`
- `linear_combination(self, coefficients)`
- `module_generating_set(self)`
- `module_generator(self, label)`
- `realize(self, element)`
- `scalar_multiple(self, scalar, element)`
- `zero(self)`

#### `SparseFreeAlgebraElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L74`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L74)
- **Bases**: `ModuleElement`
- **Constructor**: `def __init__(self, parent, coefficients) -> None`

**Public Methods:**
- `monomial_coefficients(self)`

### 🛠 Helper Functions & Constructors

#### `AlternatingAlgebraOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AlternatingAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L189`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L189)

#### `AlternatingAlgebraOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AlternatingAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L339`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L339)

#### `AlternatingAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AlternatingAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L33)

#### `AlternatingAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AlternatingAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L347`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L347)

#### `CohomologyAlgebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CohomologyAlgebra(dga)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L171`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L171)

Return the graded algebra ``H^*(dga)`` with descended multiplication.


#### `DeRhamAlgebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda algebra: id(algebra))` `def DeRhamAlgebra(algebra)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/de_rham_algebras.py#L67`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/de_rham_algebras.py#L67)

Return the strictly commutative DGA ``Omega^*_{A/R}``.

The exterior algebra itself is the existing authoritative
``AlternatingAlgebraOf(Omega^1_{A/R})``.  The public DGA is its restriction
from the degree-zero coefficient algebra ``A`` to the differential
constants ``R`` along the selected algebra structure morphism.


#### `Derivations` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda algebra, target_module: (id(algebra), id(target_module)))` `def Derivations(algebra, target_module) -> DerivationSpace`
- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L365`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L365)

#### `DividedPowerAlgebraOf` `[FUNCTION]` `[Internal]`

- **Signature**: `def DividedPowerAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L197`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L197)

#### `DividedPowerAlgebraOf` `[FUNCTION]` `[Internal]`

- **Signature**: `def DividedPowerAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L343`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L343)

#### `DividedPowerAlgebraOn` `[FUNCTION]` `[Internal]`

- **Signature**: `def DividedPowerAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L41`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L41)

#### `DividedPowerAlgebraOn` `[FUNCTION]` `[Internal]`

- **Signature**: `def DividedPowerAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L355`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L355)

#### `FinitelyPresentedAlgebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FinitelyPresentedAlgebra(presentation_ring, relations)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L285`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L285)

Return the selected quotient ``R[S] / (relations)``.


#### `FinitelyPresentedAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FinitelyPresentedAlgebraOn(base_ring, algebra_generating_set, relations)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/finitely_presented_algebras.py#L244`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/finitely_presented_algebras.py#L244)

Construct ``R[S] / (relations)`` with the displayed finite presentation.


#### `FreeAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FreeAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L122`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L122)

Return the free commutative algebra ``R[S] = Sym(F_R(S))``.


#### `GradedCommutator` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def GradedCommutator(left, right)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L57`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L57)

Return the graded commutator of endo-derivations.

For homogeneous derivations of shifts ``p`` and ``q`` this is
``D E - (-1)^(pq) E D`` and has shift ``p+q``.


#### `GradedDerivations` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda algebra, target, shift=0: (id(algebra), id(target) if target is not None else None, int(shift)))` `def GradedDerivations(algebra, target=None, shift=0) -> GradedDerivationSpace`
- **Source**: [`src/dzack_research/preamble/categories/algebras/derivations.py#L533`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/derivations.py#L533)

#### `InteriorProduct` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def InteriorProduct(vector_field)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L100`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L100)

Return contraction ``i_X`` as a degree ``-1`` derivation of ``DR(A)``.


#### `KahlerDifferentials` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda algebra: id(algebra))` `def KahlerDifferentials(algebra)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/kahler_differentials.py#L146`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/kahler_differentials.py#L146)

Return ``Omega^1_{A/R}`` with its universal ``R``-derivation.


#### `LaurentPolynomialRing` `[FUNCTION]` `[Internal]`

- **Signature**: `def LaurentPolynomialRing(base_ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L146`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L146)

#### `LieBracket` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def LieBracket(left, right)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L38`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L38)

Return the commutator ``[left,right]`` of two vector fields.


#### `LieDerivative` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def LieDerivative(vector_field)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L156)

Return ``L_X = [d,i_X]`` as a degree-zero derivation of ``DR(A)``.


#### `PolynomialRing` `[FUNCTION]` `[Internal]`

- **Signature**: `def PolynomialRing(base_ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L127`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L127)

#### `SparseSymmetricAlgebraOf` `[FUNCTION]` `[Internal]`

- **Signature**: `def SparseSymmetricAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L879`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L879)

#### `SparseTensorAlgebraOf` `[FUNCTION]` `[Internal]`

- **Signature**: `def SparseTensorAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L875`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L875)

#### `SymmetricAlgebraOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def SymmetricAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L107)

Return \(\operatorname{Sym}_R(M)\) with ``M``'s linear relations.


#### `SymmetricAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def SymmetricAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L160`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L160)

#### `TensorAlgebraOf` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def TensorAlgebraOf(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L76`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L76)

Return \(T_R(M)\), including the linear relations of ``M``.


#### `TensorAlgebraOn` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def TensorAlgebraOn(base_ring, algebra_generating_set)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/free_algebras.py#L174`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/free_algebras.py#L174)

#### `VectorFields` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def VectorFields(algebra)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cartan_calculus.py#L20)

Return ``Der_R(A,A)`` as the existing derivation module.


#### `algebra_from_multiplication` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def algebra_from_multiplication(multiplication, base_ring=None, unital=True)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L1250`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L1250)

Return the algebra presented by an \(R\)-module morphism \(A\otimes_R A\to A\).


#### `algebra_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def algebra_homset(domain, codomain) -> AlgebraHomset`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L967`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L967)

#### `algebra_morphisms_agree` `[FUNCTION]` `[Internal]`

- **Signature**: `def algebra_morphisms_agree(left, right) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L611`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L611)

Decide equality of represented algebra maps on selected generators.


#### `augmented_algebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def augmented_algebra(augmentation)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L159`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/augmented_algebras.py#L159)

Return the domain of ``augmentation``, as an augmented algebra.

An augmentation of an \(R\)-algebra is an algebra morphism \(A\to R\).
When \(A\) is graded, the unit-degree piece \(A_u\) is a subalgebra, and
\(A\) is an \(A_u\)-algebra; an augmentation of that algebra is a map
\(A\to A_u\).


#### `cohomology_algebra_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def cohomology_algebra_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L164`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/cohomology_algebras.py#L164)

#### `commutative_algebra_coproduct` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def commutative_algebra_coproduct(left, right)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L975`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L975)

Return ``left tensor_R right``, the coproduct in commutative algebras.


#### `commutative_algebra_pushout` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def commutative_algebra_pushout(left_map, right_map)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L984`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L984)

Return the pushout of two commutative-algebra maps with common domain.


#### `compose_with_free_construction` `[FUNCTION]` `[Internal]`

- **Signature**: `def compose_with_free_construction(left, right)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L726`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L726)

Compose through a sparse/free map without assuming a free source.


#### `construction_algebra_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def construction_algebra_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L64`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L64)

#### `dga_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def dga_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L264`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py#L264)

#### `divided_to_symmetric` `[FUNCTION]` `[Internal]`

- **Signature**: `def divided_to_symmetric(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L158`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L158)

Return ``Gamma(M) -> Sym(M)`` when every relevant factorial is invertible.


#### `finite_algebra_generators` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_algebra_generators(algebra)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L1419`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L1419)

Return the chosen finite algebra generating family, when represented.


#### `free_construction_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def free_construction_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L869`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L869)

#### `graded_algebra_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def graded_algebra_homset(domain, codomain) -> GradedAlgebraHomset`
- **Source**: [`src/dzack_research/preamble/categories/algebras/graded_algebras.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/graded_algebras.py#L140)

#### `own_algebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def own_algebra(structure_map)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L1315`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L1315)

Return the algebra object presented by the supplied ring map.


#### `polynomial_ring` `[FUNCTION]` `[Internal]`

- **Signature**: `def polynomial_ring(base_ring, names)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L49`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/framed_free_algebras.py#L49)

Return the symmetric algebra using standard polynomial-ring syntax.


#### `power_algebra_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def power_algebra_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/power_algebras.py#L329`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/power_algebras.py#L329)

#### `refine_algebra` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_algebra(algebra, base_ring, labels=None, *categories)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L1122`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L1122)

Place a native algebra in its owned algebra categories.


#### `refine_matrix_algebra` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_matrix_algebra(homset)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/algebras.py#L391`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/algebras.py#L391)

Attach the canonical ``R``-algebra structure to a square matrix Hom object.


#### `restrict_algebra_scalars` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def restrict_algebra_scalars(algebra, ring_map)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/restricted_scalars.py#L212`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/restricted_scalars.py#L212)

Return ``Res_f(B)`` for ``f : R -> S`` and an ``S``-algebra ``B``.

Scalar restriction itself is global: the returned algebra always retains
the exact underlying computation ring of ``B`` and composes its structure
map with ``f``.  The stronger chosen finite presentation is retained only
when it can be constructed from chosen presentations of both ``S/R`` and
``B/S`` along the selected structure map of ``S``.


#### `restrict_graded_algebra_scalars` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function(key=lambda algebra, ring_map: (id(algebra), id(ring_map)))` `def restrict_graded_algebra_scalars(algebra, ring_map)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L191`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py#L191)

#### `sparse_free_algebra_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def sparse_free_algebra_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L863`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/sparse_free_algebras.py#L863)

#### `symmetric_to_divided` `[FUNCTION]` `[Internal]`

- **Signature**: `def symmetric_to_divided(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L149`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L149)

Return ``Sym(M) -> Gamma(M)``, ``x^n |-> n! gamma_n(x)``.


#### `tensor_to_alternating` `[FUNCTION]` `[Internal]`

- **Signature**: `def tensor_to_alternating(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L140)

Return the quotient morphism ``T(M) -> Lambda(M)``.


#### `tensor_to_symmetric` `[FUNCTION]` `[Internal]`

- **Signature**: `def tensor_to_symmetric(module)`
- **Source**: [`src/dzack_research/preamble/categories/algebras/comparison_maps.py#L131`](file:///home/dzack/research/src/dzack_research/preamble/categories/algebras/comparison_maps.py#L131)

Return the quotient morphism ``T(M) -> Sym(M)``.



---

<a id="subsystem-group"></a>
## Groups, Profinite Groups & Galois Theory

> Groups, Finitely presented groups, G-Sets, Actions, Profinite groups, Absolute Galois groups, Characters, and Inertia.

### 🏛 Categories & Subcategories

#### `AbelianGroupEndomorphismRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1648`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1648)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

Endomorphism rings of abelian groups.


**ParentMethods (Methods on Category Objects):**
- `codomain(self)`
- `domain(self)`
- `one(self)`
- `zero(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AbsoluteGaloisGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L12`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L12)
- **Bases**: `Category_singleton`
- **Super Categories**: `[ProfiniteGroups()]`

Groups (G_K=\operatorname{Aut}_K(\bar K)) with a chosen base point.


**ParentMethods (Methods on Category Objects):**
- `characteristic(self)`
- `is_abelian(self)`
- `is_profinite(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `AbsoluteGaloisGroupsOfFiniteFields` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L33)
- **Bases**: `Category_singleton`
- **Super Categories**: `[AbsoluteGaloisGroups(), OwnedAbelianGroups()]`

The procyclic absolute Galois groups of finite fields.


**ParentMethods (Methods on Category Objects):**
- `is_abelian(self) -> bool`
- `is_finite(self) -> bool`
- `is_finitely_generated(self) -> bool`
- `order(self)`
- `topological_group_generators(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AdditiveGroups` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L58`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L58)
- **Bases**: `Category`
- **Super Categories**: `[AdditiveMonoids()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `AdditiveMagmas` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L39`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L39)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `AdditiveMonoids` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L49`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L49)
- **Bases**: `Category`
- **Super Categories**: `[AdditiveSemigroups()]`

**ParentMethods (Methods on Category Objects):**
- `monoidal_unit(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AdditiveSemigroups` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L44`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L44)
- **Bases**: `Category`
- **Super Categories**: `[AdditiveMagmas()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeAdditiveGroups` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L63`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L63)
- **Bases**: `Category`
- **Super Categories**: `[AdditiveGroups()]`

Additive groups whose addition is commutative.


**Category Instance Methods:**
- `super_categories(self)`

#### `FiniteGSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L81`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L81)
- **Bases**: `Category`
- **Super Categories**: `[GSets(self._group), FiniteSets()]`

The represented finite objects of ``GSets(G)``.

**Category Constructor:**
- `FiniteGSets(self, group)`

**ParentMethods (Methods on Category Objects):**
- `point_set(self)`
  > Return the finite set used to present the points of this ``G``-set.

**Category Instance Methods:**
- `group(self)`
- `super_categories(self)`

#### `GSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L31`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L31)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`
**Category Constructor:**
- `GSets(self, group)`

**ParentMethods (Methods on Category Objects):**
- `act(self, group_element, point)`
- `acting_group(self)`
- `@abstract_method` `action(self)`
  > Return the chosen action morphism ``G -> Sym(X)``.

**Category Instance Methods:**
- `group(self)`
- `super_categories(self)`

#### `GroupAutomorphismGroups` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1172`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1172)
- **Bases**: `Category`
- **Super Categories**: `[OwnedGroups()]`

**ParentMethods (Methods on Category Objects):**
- `@cached_method` `group_generators(self)`
- `number_of_group_generators(self)`
- `one(self)`
- `supergroup(self)`

**ElementMethods (Methods on Category Elements):**
- `inverse(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `GroupEndCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1311`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1311)
- **Bases**: `EndCategoryConstruction`

Endomorphism monoids of groups, on the same underlying set as ``Hom(G,G)``.


**Category Instance Methods:**
- `Of(self, obj, codomain=None)`

#### `GroupHomCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1292`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1292)
- **Bases**: `HomCategoryConstruction`

The represented Hom categories of owned groups.


**Category Instance Methods:**
- `Of(self, domain, codomain=None)`

#### `GroupIsoCategoryConstruction` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1328`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1328)
- **Bases**: `IsoCategoryConstruction`

Group isomorphisms, using the maintained automorphism group on the diagonal.


**Category Instance Methods:**
- `Of(self, domain, codomain=None)`

#### `GroupsWithChosenFiniteGeneratingSet` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1556`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1556)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFinitelyGeneratedGroups()]`

Finitely generated groups carrying a chosen finite generating set.


**ParentMethods (Methods on Category Objects):**
- `conjugation_morphism(self)`
- `@cached_method` `group_generators(self)`
- `number_of_group_generators(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `GroupsWithChosenFinitePresentation` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1619`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1619)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFinitelyPresentedGroups(), GroupsWithChosenFiniteGeneratingSet()]`

Groups carrying a chosen finite presentation.


**ParentMethods (Methods on Category Objects):**
- `@cached_method` `defining_relations(self)`
- `presenting_free_group(self)`
- `quotient_by_relators(self, relators)`
  > Return ``G / <<relators>>``, the quotient by the normal closure of ``relators``.

**Category Instance Methods:**
- `super_categories(self)`

#### `GroupsWithChosenFreeBasis` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1584`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1584)
- **Bases**: `Category`
- **Super Categories**: `[OwnedGroups()]`

Free groups carrying the chosen set they are free on.


**ParentMethods (Methods on Category Objects):**
- `free_basis(self)`
  > Return the set ``S`` this group is the free group on.
- `free_generator(self, index)`
  > Return the free generator indexed by a point of the free basis.
- `reduced_word(self, element)`
  > Return the reduced word of ``element`` as ``(index, sign)`` pairs.

**Category Instance Methods:**
- `super_categories(self)`

#### `Magmas` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L10`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L10)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `Monoids` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L20)
- **Bases**: `Category`
- **Super Categories**: `[Semigroups()]`

**Category Instance Methods:**
- `homset(self, domain, codomain)`
- `super_categories(self)`

#### `OpenAbsoluteGaloisSubgroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L64`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L64)
- **Bases**: `Category_singleton`
- **Super Categories**: `[AbsoluteGaloisGroups()]`

Open subgroups (G_E\subseteq G_K) carrying the embedding (E\to\bar K).


**ParentMethods (Methods on Category Objects):**
- `ambient(self)`
- `embedding(self)`
- `fixed_extension(self)`
- `fixed_field(self)`
- `inclusion(self)`
- `index(self)`
- `supergroup(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedAbelianGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1714`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1714)
- **Bases**: `Category`
- **Super Categories**: `[OwnedGroups()]`

**ParentMethods (Methods on Category Objects):**
- `@cached_method` `endomorphism_ring(self)`
- `is_abelian(self)`
- `@cached_method` `scalar_action(self)`
- `scalar_multiple(self, exponent, element)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedFiniteAbelianGroups` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1813`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1813)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFiniteGroups(), OwnedAbelianGroups()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedFiniteGroups` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1781`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1781)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFinitelyPresentedGroups()]`

**ParentMethods (Methods on Category Objects):**
- `conjugacy_classes_representatives(self)`
- `is_finite(self)`
- `left_cosets(self, subgroup)`
  > Return the set of left cosets ``gH``, each an ordered set of elements.
- `right_cosets(self, subgroup)`
  > Return the set of right cosets ``Hg``, each an ordered set of elements.

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedFinitelyGeneratedGroups` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1541`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1541)
- **Bases**: `Category`
- **Super Categories**: `[OwnedGroups()]`

Groups admitting some finite generating set.


**ParentMethods (Methods on Category Objects):**
- `is_finitely_generated(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedFinitelyPresentedGroups` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1604`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1604)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFinitelyGeneratedGroups()]`

Finitely presented groups, as a property of the group.


**ParentMethods (Methods on Category Objects):**
- `is_finitely_presented(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1355`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1355)
- **Bases**: `CategoryPacketMethods`, `Category`
- **Super Categories**: `[Monoids()]`

Groups whose notebook-facing group interface is owned by the preamble.


**ParentMethods (Methods on Category Objects):**
- `@cached_method` `Aut(self)`
- `End(self)`
- `Hom(self, codomain, category=None)`
- `cardinality(self)`
- `inclusion(self)`
- `is_abelian(self)`
- `is_arithmetic_group(self)`
- `is_finite(self)`
- `is_finitely_generated(self)`
- `is_finitely_presented(self)`
- `is_isomorphic_to(self, other)`
- `order(self)`
  > Return the group order as an integer when finite, else its cardinality.
- `subgroup(self, generators)`
- `supergroup(self)`

**Category Instance Methods:**
- `homset(self, domain, codomain)`
- `super_categories(self)`

#### `OwnedInfiniteGroups` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1526`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1526)
- **Bases**: `Category`
- **Super Categories**: `[OwnedGroups()]`

Groups whose underlying set is known infinite.


**ParentMethods (Methods on Category Objects):**
- `is_finite(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `PredicateSubgroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/predicate_subgroups.py#L27`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/predicate_subgroups.py#L27)
- **Bases**: `CategoryWithParameters`
- **Super Categories**: `[self._host_category]`
**Category Constructor:**
- `PredicateSubgroups(self, host_category)`

**ParentMethods (Methods on Category Objects):**
- `character_data(self)`
- `contains_character_kernel(self) -> bool`
- `defining_predicate(self)`
- `finite_character_quotient(self)`
- `inclusion(self)`
- `intersection(self, other)`
- `isotropic_are_equivalent(self, left, right, *, flag=False) -> bool`
- `isotropic_orbit_representatives(self, rank, *, flag=False)`
- `one(self)`
- `supergroup(self)`
- `vector_orbit_representatives(self, square)`
- `vectors_are_equivalent(self, left, right) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `ProfiniteGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/profinite_groups.py#L10`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/profinite_groups.py#L10)
- **Bases**: `Category_singleton`
- **Super Categories**: `[OwnedGroups(), SageGroups().Topological()]`

**ParentMethods (Methods on Category Objects):**
- `is_profinite(self)`
- `@abstract_method(optional=True)` `topological_group_generators(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `Semigroups` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L15)
- **Bases**: `Category`
- **Super Categories**: `[Magmas()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `Subgroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1753`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1753)
- **Bases**: `CategoryWithParameters`
- **Super Categories**: `[OwnedGroups()]`

Groups represented as a specified subgroup of one ambient owned group.

**Category Constructor:**
- `Subgroups(self, supergroup) -> None`

**ParentMethods (Methods on Category Objects):**
- `inclusion(self)`
- `supergroup(self)`

**Category Instance Methods:**
- `super_categories(self)`
- `supergroup(self)`

#### `Torsors` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L440`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L440)
- **Bases**: `Category`
- **Super Categories**: `[GSets(self._group)]`
**Category Constructor:**
- `Torsors(self, group)`

**ParentMethods (Methods on Category Objects):**
- `@abstract_method` `an_element(self)`
  > Return the chosen point trivializing this torsor.
- `transporter(self, source, target)`
  > Return the unique group element carrying ``source`` to ``target`` when computable.

**Category Instance Methods:**
- `group(self)`
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `AbsoluteGaloisGroup` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L326`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L326)
- **Bases**: `Homset`

The automorphism group of one exact extension object (K\to\bar K).

The extension is an object of the coslice category (K/\mathbf{Fields}),
equivalently an object of the slice of affine schemes over
(\operatorname{Spec}K).  Elements are precisely closure automorphisms
commuting with that structure map.

- **Constructor**: `def __init__(self, field, *, closure=None, embedding=None) -> None`
- **Constructor**: `def _element_constructor_(self, datum=None, **options)`

**Public Methods:**
- `algebraic_closure(self)`
- `an_element(self)`
- `base_embedding(self) -> ExactFieldMorphism`
- `base_field(self)`
- `base_field_order(self)`
- `cyclotomic_character(self, n)`
- `decomposition_group(self, prime, *, prolongation)`
- `decomposition_group_class(self, prime)`
- `extension_data(self, extension, *, embedding=None, base_embedding=None)`
- `extension_object(self)`
- `finite_extension(self, degree)`
  > Return the canonical degree-``degree`` stage for a finite base field.
- `finite_quotient(self, extension)`
- `frobenius(self, prime=None)`
  > Return (x\mapsto x^q) for finite fields, or a local class at ``prime``.
- `frobenius_class(self, prime)`
- `inertia_group(self, prime, *, prolongation)`
- `inertia_group_class(self, prime)`
- `is_abelian(self)`
- `is_finite(self)`
- `is_finitely_generated(self)`
- `is_profinite(self) -> bool`
- `lift(self, finite_automorphism)`
- `lifts(self, finite_automorphism)`
- `one(self)`
- `open_subgroup(self, extension, embedding=None)`
- `open_subgroup_class(self, extension)`
- `order(self)`
- `quadratic_character(self, a)`
- `restriction_map(self, extension)`
- `slice_automorphism(self, element)`
  > Regard ``element`` as the commuting automorphism square of (K\to\bar K).
- `slice_category(self)`
- `topological_group_generators(self)`

#### `AbsoluteGaloisGroupElement` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L45`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L45)
- **Bases**: `Morphism`

A coherent, progressively realized automorphism of the chosen closure.

A global exact map may be supplied directly.  A lift from a finite
quotient instead starts with one exact finite coordinate; additional
coordinates can be installed only after their compatibility is checked.

- **Constructor**: `def __init__(self, parent, *, exact_action: ExactFieldMorphism | None=None, coordinates=(), frobenius_exponent=None) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `as_morphism(self)`
- `conjugacy_class(self)`
- `exact_action(self)`
- `extend_coordinate(self, restriction_map, coordinate) -> None`
  > Install a higher finite coordinate after checking compatibility.
- `fixes_base_field(self) -> bool`
- `frobenius_exponent(self)`
- `inverse(self)`
- `is_globally_evaluable(self) -> bool`
- `realized_stages(self) -> tuple`
- `restrict(self, stage)`
- `restriction_coordinate(self, stage)`

#### `AbsoluteGaloisSliceAutomorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L274`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L274)
- **Bases**: `Morphism`

The commuting square in (K/\mathbf{Fields}) defined by an element of (G_K).

- **Constructor**: `def __init__(self, parent, element) -> None`

**Public Methods:**
- `components(self)`
- `inverse(self)`
- `left(self)`
- `right(self)`

#### `ContinuousGroupHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L349`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L349)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`

#### `ExactFieldHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L146`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L146)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `identity(self)`

#### `ExactFieldMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L47`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L47)
- **Bases**: `Morphism`

A field morphism with owned endpoints and an exact Sage map backend.

- **Constructor**: `def __init__(self, parent, engine_morphism: Map) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `agrees_on_field(self, other) -> bool`
- `is_injective(self) -> bool`

#### `FiniteGroupClassFunction` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/class_functions.py#L10`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/class_functions.py#L10)
- **Bases**: `SetMorphism`

A class function ``G -> A`` stored on chosen conjugacy representatives.

- **Constructor**: `def __init__(self, group, codomain, representatives, values) -> None`

**Public Methods:**
- `conjugacy_class_representatives(self)`
- `values(self)`

#### `GSetHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L191`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L191)
- **Bases**: `Homset`

The actual equivariant Hom-set between represented finite ``G``-sets.

- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, function)`

**Public Methods:**
- `identity(self)`

#### `GSetMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L166`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L166)
- **Bases**: `SetMorphism`

A set map checked to commute with the represented group actions.

- **Constructor**: `def __init__(self, parent, function) -> None`

#### `GaloisRestrictionMap` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L358`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L358)
- **Bases**: `Morphism`

The continuous quotient map (G_K\to\operatorname{Gal}(L/K)).

- **Constructor**: `def __init__(self, domain, codomain: FiniteGaloisQuotient) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `extension(self) -> FiniteGaloisExtension`
- `is_continuous(self) -> bool`
- `is_surjective(self) -> bool`
- `kernel(self)`

#### `GroupAutomorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1168`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1168)
- **Bases**: `GroupHomomorphism`

#### `GroupAutomorphismGroup` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1218`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1218)
- **Bases**: `GroupHomset`
- **Constructor**: `def __init__(self, hom_family, group, engine_subgroup=None)`
- **Constructor**: `def _element_constructor_(self, images, check=True, **options)`

**Public Methods:**
- `identity(self)`
- `set_supergroup(self, supergroup)`
- `super_categories(self)`

#### `GroupHomomorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1020`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1020)
- **Bases**: `GroupMorphism_libgap`

A group homomorphism represented by Sage's maintained GAP morphism.

- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `image(self)`
- `is_injective(self)`
- `is_surjective(self)`
- `kernel(self)`
- `lift(self, element)`
  > Return one preimage of ``element``.

#### `GroupHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1058`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1058)
- **Bases**: `GroupHomset_libgap`, `CategoricalHomset`

The canonical owned homset Hom(G,H).

- **Constructor**: `def __init__(self, hom_family, domain, codomain)`
- **Constructor**: `def _element_constructor_(self, images, check=True, **_options)`

**Public Methods:**
- `morphisms_agree(self, left, right) -> bool`
  > Decide equality from a finite GAP generating family of the source.

#### `IndexedFreeGroupHomomorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L930`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L930)
- **Bases**: `Morphism`

A morphism out of the free group on a chosen set.

The free group on an arbitrary set has no elementwise GAP model.  Its
universal morphisms are therefore evaluated directly on reduced words
instead of forcing this object through the unrelated libGAP path.

- **Constructor**: `def __init__(self, parent, images) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `generator_morphism(self)`
- `postcompose(self, morphism)`

#### `IndexedFreeGroupHomset` `[HOMSET]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L997`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L997)
- **Bases**: `CategoricalHomset`

The canonical Hom-set out of the free group on a chosen set.

- **Constructor**: `def __init__(self, hom_family, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, images, **_options)`

#### `MonoidHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L102`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L102)
- **Bases**: `Homset`

The owned set ``Hom_Mon(A,B)``.

- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def __call__(self, function)`

**Public Methods:**
- `identity(self)`

#### `MonoidMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/magmas.py#L79`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/magmas.py#L79)
- **Bases**: `Morphism`

A morphism in the owned category of monoids.

- **Constructor**: `def __init__(self, parent, function) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

#### `OpenSubgroupInclusion` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L724`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L724)
- **Bases**: `Morphism`

The literal inclusion of a realized open subgroup into its ambient group.

- **Constructor**: `def __init__(self, subgroup) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `is_continuous(self) -> bool`
- `is_injective(self) -> bool`

#### `ProfiniteCharacter` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L49`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L49)
- **Bases**: `Morphism`

A character factoring through one represented finite Galois quotient.

- **Constructor**: `def __init__(self, domain, codomain, extension: FiniteGaloisExtension) -> None`

**Public Methods:**
- `factor_extension(self) -> FiniteGaloisExtension`
- `factorization(self)`
- `is_continuous(self) -> bool`
- `kernel(self)`
- `restrict(self, subgroup)`

#### `RestrictedProfiniteCharacter` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L32`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L32)
- **Bases**: `Morphism`
- **Constructor**: `def __init__(self, character, subgroup) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `is_continuous(self) -> bool`

#### `SubgroupInclusion` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L874`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L874)
- **Bases**: `SetMorphism`

**Public Methods:**
- `is_injective(self)`

#### `SubmonoidInclusion` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/submonoids.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/submonoids.py#L15)
- **Bases**: `MonoidMorphism`

The chosen monomorphism ``S -> M`` representing a submonoid.


**Public Methods:**
- `factor_through(self, target_inclusion)`
- `is_injective(self)`

### 📦 Mathematical Objects & Parents

#### `AbsoluteDecompositionGroup` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L249`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L249)
- **Bases**: `SageObject`
- **Constructor**: `def __init__(self, ambient, prime, prolongation: PrimeProlongation) -> None`

**Public Methods:**
- `ambient(self)`
- `conjugacy_class(self)`
- `image(self, quotient)`
- `prime(self)`
- `prolongation(self)`

#### `AbsoluteInertiaGroup` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L283`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L283)
- **Bases**: `SageObject`
- **Constructor**: `def __init__(self, ambient, prime, prolongation: PrimeProlongation) -> None`

**Public Methods:**
- `ambient(self)`
- `conjugacy_class(self)`
- `image(self, quotient)`
- `prime(self)`
- `prolongation(self)`

#### `CyclicSubgroup` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/cyclic_subgroups.py#L13`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/cyclic_subgroups.py#L13)
- **Bases**: `Parent`

The literal subgroup ``<g> <= G`` generated by one live element.

This is a facade of ``G``: its elements are the actual elements of the
ambient group, not parallel residue classes in an abstract ``C_n``.  The
chosen generator is structure on the subgroup.  Finiteness is inherited
when the ambient group is known finite; otherwise no finite-order claim is
made merely because the subgroup is cyclic.

- **Constructor**: `def __init__(self, supergroup, generator) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `cardinality(self)`
- `generator(self)`
- `@cached_method` `group_generators(self)`
- `inclusion(self)`
- `is_abelian(self)`
- `is_finite(self)`
- `number_of_group_generators(self)`
- `one(self)`
- `order(self)`
- `supergroup(self)`

#### `CyclotomicCharacter` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L87)
- **Bases**: `ProfiniteCharacter`

The continuous character (\chi_n:G_K\to(\mathbb Z/n)^{\times}).

- **Constructor**: `def __init__(self, domain, n) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `modulus(self)`
- `primitive_root(self)`

#### `DecompositionGroupConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L317`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L317)
- **Bases**: `SageObject`
- **Constructor**: `def __init__(self, ambient, prime) -> None`

**Public Methods:**
- `ambient(self)`
- `prime(self)`
- `representative(self, prolongation)`

#### `ElementConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L217`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L217)
- **Bases**: `SageObject`

The conjugacy class of a represented global automorphism.

- **Constructor**: `def __init__(self, ambient, representative) -> None`

**Public Methods:**
- `ambient(self)`
- `representative(self)`

#### `FiniteElementConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L156)
- **Bases**: `SageObject`

The actual conjugacy orbit of an element in a finite quotient.

- **Constructor**: `def __init__(self, ambient, representative) -> None`

**Public Methods:**
- `ambient(self)`
- `elements(self) -> tuple`
- `representative(self)`

#### `FiniteGSet` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L114`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L114)
- **Bases**: `Parent`

A finite set equipped with a group morphism into its permutation group.

- **Constructor**: `def __init__(self, point_set, action) -> None`
- **Constructor**: `def __call__(self, point)`
- **Constructor**: `def _element_constructor_(self, point)`

**Public Methods:**
- `action(self)`
- `cardinality(self)`

#### `FiniteGaloisAutomorphism` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L161`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L161)
- **Bases**: `Element`

An exact (K)-automorphism of a represented finite extension (L/K).

- **Constructor**: `def __init__(self, parent, index: int) -> None`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `action(self) -> ExactFieldMorphism`
- `inverse(self)`
- `multiplicative_order(self)`

#### `FiniteGaloisExtension` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L62`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L62)
- **Bases**: `SageObject`

A finite Galois field (L/K\subset\bar K) with both exact embeddings.

- **Constructor**: `def __init__(self, base_field, field, base_embedding: ExactFieldMorphism, closure, closure_embedding: ExactFieldMorphism) -> None`

**Public Methods:**
- `algebraic_closure(self)`
- `automorphisms(self) -> tuple[ExactFieldMorphism, ...]`
- `base_embedding(self) -> ExactFieldMorphism`
- `base_field(self)`
- `degree(self)`
- `embedding(self) -> ExactFieldMorphism`
- `field(self)`
- `is_galois(self) -> bool`

#### `FiniteGaloisQuotient` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L231`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L231)
- **Bases**: `Parent`

The finite quotient (\operatorname{Gal}(L/K)) as exact field maps.

- **Constructor**: `def __init__(self, extension: FiniteGaloisExtension) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `automorphisms(self) -> tuple[ExactFieldMorphism, ...]`
- `base_field(self)`
- `compose(self, left, right)`
- `extension_data(self) -> FiniteGaloisExtension`
- `group_generators(self)`
- `inverse(self, element)`
- `is_abelian(self) -> bool`
- `one(self)`
- `order(self)`
- `top_field(self)`

#### `FiniteGaloisSubgroup` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L94`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L94)
- **Bases**: `Parent`

A literal finite subgroup represented by selected quotient elements.

- **Constructor**: `def __init__(self, ambient, elements, description) -> None`
- **Constructor**: `def _element_constructor_(self, element)`

**Public Methods:**
- `ambient(self)`
- `group_generators(self)`
- `one(self)`
- `order(self)`

#### `FrobeniusConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L379`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L379)
- **Bases**: `SageObject`

The canonical global Frobenius class at an unramified base prime.

- **Constructor**: `def __init__(self, ambient, prime) -> None`

**Public Methods:**
- `ambient(self)`
- `conjugacy_class(self)`
- `image(self, quotient, prime_above)`
- `prime(self)`

#### `FrobeniusElement` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L210`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L210)
- **Bases**: `AbsoluteGaloisGroupElement`

An integral power of the canonical (q)-Frobenius.

- **Constructor**: `def __init__(self, parent, exponent=1) -> None`

#### `InertiaGroupConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L348`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L348)
- **Bases**: `SageObject`
- **Constructor**: `def __init__(self, ambient, prime) -> None`

**Public Methods:**
- `ambient(self)`
- `prime(self)`
- `representative(self, prolongation)`

#### `LiftCoset` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L401`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L401)
- **Bases**: `SageObject`

The coset of all global extensions of one finite-level automorphism.

- **Constructor**: `def __init__(self, restriction_map: GaloisRestrictionMap, element) -> None`

**Public Methods:**
- `ambient(self)`
- `extension(self) -> FiniteGaloisExtension`
- `finite_automorphism(self)`
- `kernel(self)`
- `representative(self, candidate=None)`
  > Return a supplied representative, or the canonical finite-field one.

#### `OpenAbsoluteGaloisSubgroup` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L752`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L752)
- **Bases**: `AbsoluteGaloisGroup`

The actual subgroup fixing one embedded finite extension (E/K).

- **Constructor**: `def __init__(self, ambient, extension: FiniteGaloisExtension) -> None`
- **Constructor**: `def _element_constructor_(self, datum=None, **options)`

**Public Methods:**
- `ambient(self)`
- `conjugacy_class(self)`
- `core(self)`
- `embedding(self)`
- `fixed_extension(self) -> FiniteGaloisExtension`
- `fixed_field(self)`
- `inclusion(self) -> OpenSubgroupInclusion`
- `index(self)`
- `intersection(self, other)`
- `is_normal(self) -> bool`

#### `OpenGaloisSubgroupConjugacyClass` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L914`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L914)
- **Bases**: `SageObject`

The conjugacy class obtained by forgetting (E\hookrightarrow\bar K).

- **Constructor**: `def __init__(self, ambient, extension_field) -> None`

**Public Methods:**
- `ambient(self)`
- `base_embedding(self)`
- `fixed_field(self)`
- `index(self)`
- `representative(self, embedding=None)`

#### `OrbitClass` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L286`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L286)
- **Bases**: `Element`

One orbit in the quotient set ``X/G``.

- **Constructor**: `def __init__(self, parent, index) -> None`

**Public Methods:**
- `points(self)`
- `representative(self)`

#### `OrbitSet` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L316`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L316)
- **Bases**: `Parent`

The finite orbit quotient ``X/G`` of a represented finite ``G``-set.

- **Constructor**: `def __init__(self, g_set) -> None`

**Public Methods:**
- `cardinality(self)`
- `g_set(self)`
- `orbit_of(self, point)`
- `orbit_points(self, orbit)`
- `rank(self, orbit)`
- `unrank(self, position)`

#### `OwnedGroup` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L515`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L515)
- **Bases**: `Parent`

A preamble group with one private Sage/GAP computational model.

- **Constructor**: `def __init__(self, engine) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `one(self)`

#### `PrimeProlongation` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L10`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L10)
- **Bases**: `SageObject`

A coherent finite-stage oracle for a chosen prolongation (\bar v).

- **Constructor**: `def __init__(self, base_prime, at_stage) -> None`

**Public Methods:**
- `at(self, extension)`
- `base_prime(self)`

#### `QuadraticCharacter` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L165`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_characters.py#L165)
- **Bases**: `ProfiniteCharacter`

The character attached to (K(\sqrt a)/K) in characteristic not two.

- **Constructor**: `def __init__(self, domain, a) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `square_class(self)`
- `square_root(self)`

### 🛠 Helper Functions & Constructors

#### `Submonoids` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Submonoids(ambient_monoid)`
- **Source**: [`src/dzack_research/preamble/categories/group/submonoids.py#L136`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/submonoids.py#L136)

Return the generic subobject category of submonoids of ``ambient_monoid``.


#### `absolute_galois_group_category` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def absolute_galois_group_category(field)`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L97`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py#L97)

#### `centralizer` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def centralizer(containing_group, element)`
- **Source**: [`src/dzack_research/preamble/categories/group/predicate_subgroups.py#L184`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/predicate_subgroups.py#L184)

#### `continuous_group_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def continuous_group_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L354`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L354)

#### `coxeter_presentation` `[FUNCTION]` `[Internal]`

- **Signature**: `def coxeter_presentation(coxeter_matrix, names=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1822`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1822)

#### `cyclic_subgroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def cyclic_subgroup(generator)`
- **Source**: [`src/dzack_research/preamble/categories/group/cyclic_subgroups.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/cyclic_subgroups.py#L140)

Return the literal cyclic subgroup generated by ``generator``.


#### `exact_embeddings` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def exact_embeddings(domain, codomain) -> tuple[ExactFieldMorphism, ...]`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L181`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L181)

Return all exact embeddings of ``domain`` into ``codomain``.


#### `exact_field_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def exact_field_homset(domain, codomain) -> ExactFieldHomset`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L170`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L170)

#### `extensions_along` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def extensions_along(automorphism, embedding, candidates)`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L468`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L468)

Return exactly the candidate automorphisms satisfying (\sigma j=j\tau).


#### `field_generators` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def field_generators(field) -> tuple`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L23`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L23)

Return exact elements which determine a unital map out of ``field``.


#### `finite_decomposition_group` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def finite_decomposition_group(quotient, prime_above) -> FiniteGaloisSubgroup`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L192`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L192)

#### `finite_frobenius_class` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def finite_frobenius_class(quotient, base_prime, prime_above) -> FiniteElementConjugacyClass`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L220`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L220)

#### `finite_g_set` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def finite_g_set(point_set, group, action)`
- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L276`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L276)

Return the finite owned ``G``-set defined by ``action(g,x)``.


#### `finite_group_class_function` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_group_class_function(group, codomain, values, *, representatives=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/class_functions.py#L93`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/class_functions.py#L93)

#### `finite_inertia_group` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def finite_inertia_group(quotient, prime_above) -> FiniteGaloisSubgroup`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L206`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py#L206)

#### `first_exact_embedding` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def first_exact_embedding(domain, codomain) -> ExactFieldMorphism`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L198`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/field_morphisms.py#L198)

Choose the first exact Sage embedding in its deterministic ordering.


#### `fixed_point_set` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def fixed_point_set(g_set)`
- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L422`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L422)

Return the finite fixed-point set ``X^G``.


#### `g_set_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def g_set_homset(domain, codomain) -> GSetHomset`
- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L213`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L213)

#### `generated_submonoid` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def generated_submonoid(ambient, generators, *, description=None, structure_data=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/submonoids.py#L141`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/submonoids.py#L141)

#### `group_homset` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def group_homset(domain, codomain)`
- **Source**: [`src/dzack_research/preamble/categories/group/groups.py#L1164`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/groups.py#L1164)

#### `is_predicate_subgroup` `[FUNCTION]` `[Internal]`

- **Signature**: `def is_predicate_subgroup(group)`
- **Source**: [`src/dzack_research/preamble/categories/group/predicate_subgroups.py#L177`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/predicate_subgroups.py#L177)

#### `open_absolute_galois_subgroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def open_absolute_galois_subgroup(ambient, extension, embedding=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L1003`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py#L1003)

#### `predicate_subgroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def predicate_subgroup(containing_group, predicate, description, *, character_data=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/predicate_subgroups.py#L155`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/predicate_subgroups.py#L155)

#### `predicate_subgroup_category` `[FUNCTION]` `[Internal]`

- **Signature**: `def predicate_subgroup_category()`
- **Source**: [`src/dzack_research/preamble/categories/group/predicate_subgroups.py#L150`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/predicate_subgroups.py#L150)

#### `predicate_submonoid` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def predicate_submonoid(ambient, predicate, description, *, structure_data=None)`
- **Source**: [`src/dzack_research/preamble/categories/group/submonoids.py#L151`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/submonoids.py#L151)

#### `restrict_along` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def restrict_along(automorphism: ExactFieldMorphism, embedding: ExactFieldMorphism) -> ExactFieldMorphism`
- **Source**: [`src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L447`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/profinite/galois_quotient.py#L447)

Solve (j\tau=\sigma j) for the exact restriction ``tau``.


#### `trivial_g_set` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def trivial_g_set(point_set, group)`
- **Source**: [`src/dzack_research/preamble/categories/group/g_sets.py#L281`](file:///home/dzack/research/src/dzack_research/preamble/categories/group/g_sets.py#L281)

Equip a finite set with the trivial ``group``-action.



---

<a id="subsystem-rings"></a>
## Rings, Fields & Commutative Algebra

> Owned rings, Fields, Number fields, Prime spectrum, Completions, Localizations, Exact real field, and Predicate subrings.

### 🏛 Categories & Subcategories

#### `AdicCompletions` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L973`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L973)
- **Bases**: `Category`
- **Super Categories**: `[OwnedAdicallyCompleteRings()]`

Adic completions equipped with source and ideal of definition.


**ParentMethods (Methods on Category Objects):**
- `completion_map(self)`
- `computation_precision(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `CommutativeIdeals` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_ideals.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_ideals.py#L15)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Ideals of ``R``: subobjects of the rank-one ``R``-module ``R``.


**ParentMethods (Methods on Category Objects):**
- `associated_primes(self)`
- `colon(self, other)`
  > Return the ideal quotient ``(self : other)`` when the backend supports it.
- `contains_ambient_element(self, element) -> bool`
  > Return whether an ambient ring element lies in this ideal.
- `contraction_from_localization(self)`
  > Contract this selected localized extension back to its source ring.
- `extension_to_localization(self, localization_ring)`
  > Return ``S^{-1}I <= S^{-1}R`` by localizing the inclusion.
- `ideal_generators(self)`
- `inclusion(self)`
- `intersection(self, other)`
- `is_maximal(self)`
- `is_prime(self)`
- `power(self, exponent)`
- `primary_decomposition(self)`
- `product(self, other)`
- `quotient_ring(self)`
- `radical(self)`
- `ring(self)`
- `saturation(self, other)`
  > Return ``(self : other^infinity)`` when the backend supports it.
- `sum(self, other)`
- `syzygy_matrix(self)`

**Category Instance Methods:**
- `subobject_category(self)`
- `super_categories(self)`

#### `CommutativeRingConstructions` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L47`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L47)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Commutative rings equipped with the represented standard constructions.


**ParentMethods (Methods on Category Objects):**
- `adic_completion(self, ideal, precision=20)`
- `as_ZZ_algebra(self)`
- `as_algebra_over(self, base_ring)`
- `ideal(self, *generators)`
- `localization(self, *elements)`
- `localize_at_prime(self, prime)`
- `quotient_ring(self, ideal)`
- `@cached_method` `spectrum(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FormalPowerSeriesRings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1413`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1413)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[CommutativeAlgebras(self.base_ring()), OwnedAdicallyCompleteRings()]`

Formal power-series rings ``R[[t]]`` over the owned ring ``R``.


**ParentMethods (Methods on Category Objects):**
- `power_series_variable(self)`

**ElementMethods (Methods on Category Elements):**
- `coefficient(self, degree)`

**Category Instance Methods:**
- `super_categories(self)`

#### `LocalizationRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L654`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L654)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Localizations ``S^{-1}R`` equipped with ``S -> (R,*)`` and ``R -> S^{-1}R``.


**ParentMethods (Methods on Category Objects):**
- `inverted_elements(self)`
- `localization_fraction_data(self, element)`
  > Return one represented fraction ``(r,s)`` for ``element=r/s``.
- `localization_map(self)`
- `localization_source(self)`
- `localization_submonoid(self)`
- `localize_module(self, module)`
  > Return ``S^{-1}M`` for this represented localization ``S^{-1}R``.

**Category Instance Methods:**
- `super_categories(self)`

#### `NumberFieldsWithChosenPrimitiveElement` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L232`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L232)
- **Bases**: `Category`
- **Super Categories**: `[OwnedNumberFields()]`

Number fields carrying the primitive element selected by their presentation.


**ParentMethods (Methods on Category Objects):**
- `algebra_generating_set(self)`
- `algebra_generator(self, label)`
- `defining_polynomial(self)`
  > Return the owned defining polynomial of the selected primitive element.
- `embedding_images(self, target)`
  > Return the images of the selected primitive element under ``K -> target``.
- `primitive_element(self)`
  > Return the selected primitive element ``alpha``.

**Category Instance Methods:**
- `super_categories(self)`

#### `OrdersWithChosenIntegralBasis` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L276`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L276)
- **Bases**: `Category`
- **Super Categories**: `[OwnedOrders(), FreeModuleBaseRings(), Algebras(integers), FinitelyGeneratedFreeModules(integers)]`

Number-field orders carrying their selected integral basis.


**ParentMethods (Methods on Category Objects):**
- `base_change(self, ring_map)`
- `base_ring(self)`
- `fractional_ideal(self, *module_generators)`
- `framing_morphism(self)`
- `ideal(self, *module_generators)`
- `integral_basis(self)`
- `@cached_method` `module_generating_set(self)`
- `module_generator(self, label)`
- `@cached_method` `module_generators(self)`
- `rank(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedAdicallyCompleteRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L504`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L504)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Commutative rings represented as complete for a chosen adic topology.


**ParentMethods (Methods on Category Objects):**
- `completion_source(self)`
- `ideal_of_definition(self)`
- `is_adically_complete(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedArtinianRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L455`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L455)
- **Bases**: `Category`
- **Super Categories**: `[OwnedNoetherianRings()]`

Artinian commutative rings.


**ParentMethods (Methods on Category Objects):**
- `is_artinian(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedCategoryOverBaseRing` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L595`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L595)
- **Bases**: `CategoryPacketMethods`, `Category_over_base`

A category over a ring, normalized to the session's owned ring.


**Category Instance Methods:**
- `base_ring(self)`

#### `OwnedCommutativeRings` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L396`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L396)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

Commutative unital rings in the owned mathematical graph.


**ParentMethods (Methods on Category Objects):**
- `is_commutative(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedCompleteLocalRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L527`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L527)
- **Bases**: `Category`
- **Super Categories**: `[OwnedLocalRings(), OwnedAdicallyCompleteRings()]`

Local rings complete for the represented maximal-ideal/adic topology.


**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedDivisionRings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L533`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L533)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedFields` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L538`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L538)
- **Bases**: `Category`
- **Super Categories**: `[OwnedDivisionRings(), OwnedIntegralDomains(), OwnedPrincipalIdealDomains(), OwnedNoetherianRings(), OwnedArtinianRings(), OwnedLocalRings()]`

**ParentMethods (Methods on Category Objects):**
- `maximal_ideal(self)`
- `residue_field(self)`
- `residue_map(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedIntegralDomains` `[SUBCATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L419`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L419)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Commutative rings without zero divisors.


**ParentMethods (Methods on Category Objects):**
- `is_integral_domain(self, *args, **kwargs)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedLocalRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L466`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L466)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Commutative rings equipped with their unique maximal ideal.


**ParentMethods (Methods on Category Objects):**
- `fraction_field(self)`
- `is_local(self)`
- `maximal_ideal(self)`
- `residue_field(self)`
- `residue_map(self)`
  > Return the represented local quotient map ``R -> kappa(m)``.

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedNoetherianRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L437`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L437)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Noetherian commutative rings.


**ParentMethods (Methods on Category Objects):**
- `is_noetherian(self)`
- `krull_dimension(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedNumberFields` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L45`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L45)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFields()]`

Finite extensions of ``QQ``.


**ParentMethods (Methods on Category Objects):**
- `as_algebra(self)`
  > Return this field as the corresponding ``QQ``-algebra object.
- `class_number(self)`
  > Return the class number of the ring of integers.
- `degree(self)`
  > Return ``[K:QQ]`` as an owned integer.
- `discriminant(self)`
  > Return the discriminant of the ring of integers of ``K``.
- `embeddings(self, target)`
  > Return the exact owned field embeddings ``K -> target``.
- `extension(self, polynomial, name='a')`
  > Return the finite extension defined by an owned polynomial over ``self``.
- `galois_group(self)`
  > Return ``Gal(K/QQ)``; this name is reserved for Galois ``K``.
- `is_galois(self) -> bool`
  > Return whether ``K/QQ`` is Galois.
- `normal_closure(self)`
  > Return a chosen normal closure of ``K/QQ``.
- `normal_closure_galois_group(self)`
  > Return the Galois group of a chosen normal closure of ``K``.
- `order_generated_by(self, *generators)`
  > Return the order ``ZZ[generators]`` inside this number field.
- `primes_above(self, prime)`
  > Return the prime ideals of ``O_K`` above a rational prime.
- `ramified_primes(self)`
  > Return the rational primes ramified in ``K``.
- `ring_of_integers(self)`
  > Return the maximal order ``O_K`` as an owned ring.
- `signature(self)`
  > Return ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``.

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedOrderedRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L407`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L407)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

Totally ordered rings in the owned scalar hierarchy.


**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedOrders` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L560`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L560)
- **Bases**: `Category`
- **Super Categories**: `[OwnedIntegralDomains(), OwnedNoetherianRings()]`

Orders in number fields as a ring-theoretic property category.


**ParentMethods (Methods on Category Objects):**
- `cardinality(self)`
- `is_maximal(self) -> bool`
  > Return whether this is the maximal order of its fraction field.

**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedPrincipalIdealDomains` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L430`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L430)
- **Bases**: `Category`
- **Super Categories**: `[OwnedIntegralDomains(), OwnedNoetherianRings()]`

Principal ideal domains in the owned ring hierarchy.


**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedRings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L265`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L265)
- **Bases**: `Category`
- **Super Categories**: `[OwnedSemirings(), OwnedRngs()]`

Unital rings whose notebook-facing ring interface is owned here.


**ParentMethods (Methods on Category Objects):**
- `algebra_structure_morphism(self)`
  > The structure morphism of this ring as an algebra over itself.
- `cardinality(self)`
  > Return the exact represented cardinal of the underlying set.
- `fraction_field(self)`
  > Return the fraction field through the computation ring.
- `is_central(self, element)`
  > Return whether ``element`` is central when this is decidable here.
- `@cached_method` `ring_center(self)`
  > Return the centre ``Z(R)`` as a predicate-defined subring.

**Category Instance Methods:**
- `homset(self, domain, codomain)`
- `super_categories(self)`

#### `OwnedRngs` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L258`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L258)
- **Bases**: `Category`
- **Super Categories**: `[Semigroups(), AdditiveGroups()]`

Rngs on the owned operation spine.


**Category Instance Methods:**
- `super_categories(self)`

#### `OwnedSemirings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L251`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L251)
- **Bases**: `Category`
- **Super Categories**: `[Monoids(), AdditiveMonoids()]`

Semirings on the owned operation spine.


**Category Instance Methods:**
- `super_categories(self)`

#### `PredicateSubrings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L164`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L164)
- **Bases**: `Category`
- **Super Categories**: `[OwnedRings()]`

**ParentMethods (Methods on Category Objects):**
- `ambient_ring(self)`
- `defining_predicate(self)`
- `inclusion(self)`
- `one(self)`
- `zero(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `PrimeFields` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L583`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L583)
- **Bases**: `Category`
- **Super Categories**: `[OwnedFields()]`

Prime fields \(\mathbf F_p\).


**Category Instance Methods:**
- `super_categories(self)`

#### `PrimeLocalizations` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L950`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L950)
- **Bases**: `Category`
- **Super Categories**: `[OwnedLocalRings(), OwnedIntegralDomains()]`

Prime local rings ``R_p`` represented inside ``Frac(R)``.


**ParentMethods (Methods on Category Objects):**
- `is_field(self)`
  > A domain localization ``R_p`` is a field exactly for ``p=(0)``.
- `localization_map(self)`
- `localization_source(self)`
- `localized_prime(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `QuotientRings` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L370`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L370)
- **Bases**: `Category`
- **Super Categories**: `[OwnedCommutativeRings()]`

Commutative quotient rings equipped with their quotient map.


**ParentMethods (Methods on Category Objects):**
- `characteristic(self)`
- `defining_ideal(self)`
- `localization_comparison(self, localization_ring)`
  > Return ``S^{-1}(R/I) ~= S^{-1}R/S^{-1}I`` with both maps.
- `quotient_map(self)`
- `quotient_source(self)`

**Category Instance Methods:**
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `DistinguishedOpenSubobject` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L278`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L278)
- **Bases**: `SetInclusion`

The distinguished open subobject ``D(f) -> Spec(R)``.

- **Constructor**: `def __init__(self, spectrum, function) -> None`

**Public Methods:**
- `coordinate_ring(self)`
- `function(self)`

#### `NumberFieldEmbedding` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L15)
- **Bases**: `Morphism`

An exact field embedding between owned number fields.

- **Constructor**: `def __init__(self, parent, engine_morphism) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `is_injective(self) -> bool`

#### `NumberFieldHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L93`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L93)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `embeddings(self)`
- `identity(self)`

#### `OrderEmbedding` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L144)
- **Bases**: `Morphism`

A unital embedding of orders, represented by its fraction-field extension.

- **Constructor**: `def __init__(self, parent, field_embedding: NumberFieldEmbedding) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `field_embedding(self) -> NumberFieldEmbedding`
- `is_injective(self) -> bool`

#### `OrderHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L197`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L197)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, field_embedding)`

**Public Methods:**
- `identity(self)`

#### `RingHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L100`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L100)
- **Bases**: `Homset`

The owned set ``Hom_Ring(A,B)``.

- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def __call__(self, datum)`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `elementwise(self, function)`
- `identity(self)`
- `is_endomorphism_set(self)`

#### `RingMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L50`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L50)
- **Bases**: `Morphism`

A unital ring morphism in the owned ring category.

- **Constructor**: `def __init__(self, parent, function, *, engine_morphism=None) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `compose(self, before)`
- `is_identity(self) -> bool`

#### `ZariskiClosedSubobject` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L244`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L244)
- **Bases**: `SetInclusion`

The closed subobject ``V(I) -> Spec(R)``.

- **Constructor**: `def __init__(self, spectrum, ideal) -> None`

**Public Methods:**
- `defining_ideal(self)`

### 📦 Mathematical Objects & Parents

#### `ExactRealField` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/rings/real.py#L436`](file:///home/dzack/research/src/dzack_research/preamble/rings/real.py#L436)
- **Bases**: `UniqueRepresentation`, `Field`

The exact field of real numbers represented by closed exact expressions.

- **Constructor**: `def __init__(self) -> None`
- **Constructor**: `def _element_constructor_(self, value) -> ExactRealNumber`

**Public Methods:**
- `cardinality(self)`
- `characteristic(self)`
- `e(self) -> ExactRealNumber`
- `fraction_field(self)`
- `is_exact(self) -> bool`
- `is_finite(self) -> bool`
- `one(self) -> ExactRealNumber`
- `pi(self) -> ExactRealNumber`
- `relation(self, left: ExactRealNumber, right: ExactRealNumber, relation)`
  > Return a decided Boolean or an exact real relation predicate.
- `zero(self) -> ExactRealNumber`

#### `ExactRealNumber` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/rings/real.py#L254`](file:///home/dzack/research/src/dzack_research/preamble/rings/real.py#L254)
- **Bases**: `FieldElement`

An exact, explicitly real number.

- **Constructor**: `def __init__(self, parent: 'ExactRealField', expression: Expression) -> None`

**Public Methods:**
- `cos(self)`
- `exp(self)`
- `expression(self) -> Expression`
  > Return the exact symbolic expression representing this real.
- `is_negative(self)`
- `is_one(self)`
- `is_positive(self)`
- `is_real(self) -> bool`
- `is_zero(self)`
- `log(self, base=None)`
- `n(self, prec: int=53, digits: int | None=None, **kwds)`
  > Return an explicit floating-point approximation of ``self``.
- `sin(self)`
- `sqrt(self)`
- `tan(self)`

#### `GeneralLocalizationRingElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L707`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L707)
- **Bases**: `CommutativeRingElement`

A literal fraction ``r/s`` in a represented commutative localization.

- **Constructor**: `def __init__(self, parent, numerator, denominator) -> None`

**Public Methods:**
- `denominator(self)`
- `equality_status(self, other)`
- `inverse_of_unit(self)`
- `is_unit(self)`
- `numerator(self)`

#### `GeneralLocalizationRingParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L817`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L817)
- **Bases**: `Parent`

The universal fraction model ``S^{-1}R`` for a represented submonoid ``S``.

- **Constructor**: `def __init__(self, source, submonoid, _engine_ring=None) -> None`
- **Constructor**: `def _element_constructor_(self, value)`
- **Constructor**: `def __call__(self, value)`

**Public Methods:**
- `fraction(self, numerator, denominator=None, *, _trusted_denominator=False)`
- `one(self)`
- `zero(self)`

#### `GeneralQuotientRingElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L415`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L415)
- **Bases**: `CommutativeRingElement`

A coset in a represented quotient ``R/I`` without a native CAS parent.

- **Constructor**: `def __init__(self, parent, representative) -> None`

**Public Methods:**
- `inverse_of_unit(self)`
- `is_unit(self)`
- `lift(self)`

#### `GeneralQuotientRingParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L472`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L472)
- **Bases**: `Parent`

The literal quotient ring ``R/I`` using the ideal congruence.

- **Constructor**: `def __init__(self, source, defining_ideal, _engine_ring=None) -> None`
- **Constructor**: `def _element_constructor_(self, value)`
- **Constructor**: `def __call__(self, value)`

**Public Methods:**
- `an_element(self)`
- `cardinality(self)`
- `is_field(self)`
- `is_finite(self)`
- `is_integral_domain(self)`
- `krull_dimension(self)`
- `one(self)`
- `zero(self)`

#### `GeneratedIdealView` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L987`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L987)
- **Bases**: `SageObject`

An ideal remembered by its ambient ring and chosen generators.

- **Constructor**: `def __init__(self, ring, generators, source_ideal=None) -> None`

**Public Methods:**
- `gens(self)`
- `ring(self)`
- `source_ideal(self)`

#### `LocalizedMaximalIdeal` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1010`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1010)
- **Bases**: `GeneratedIdealView`

#### `NonNegativeReal` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/rings/nonnegative_reals.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/rings/nonnegative_reals.py#L26)
- **Bases**: `Element`

An element of \(([0,\infty],+)\).

- **Constructor**: `def __init__(self, parent, value) -> None`

**Public Methods:**
- `as_extended_real(self)`
  > This element as a finite real, or \(+\infty\).

#### `NonNegativeReals` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/rings/nonnegative_reals.py#L78`](file:///home/dzack/research/src/dzack_research/preamble/rings/nonnegative_reals.py#L78)
- **Bases**: `UniqueRepresentation`, `Parent`

The additive monoid \(([0,\infty],+)\).

- **Constructor**: `def __init__(self) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `cardinality(self)`
- `zero(self)`

#### `PrimeIdealPoint` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L181`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L181)
- **Bases**: `Element`

A point ``p in Spec(R)``, represented by its prime ideal ``p <= R``.

- **Constructor**: `def __init__(self, parent, ideal) -> None`

**Public Methods:**
- `ideal(self)`
- `@cached_method` `local_ring(self)`
- `@cached_method` `residue_field(self)`
- `@cached_method` `residue_map(self)`
  > Return the canonical map ``R -> kappa(p)`` attached to this point.
- `specializes_to(self, other) -> bool`

#### `PrimeSpectrum` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L310`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L310)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, ring) -> None`
- **Constructor**: `def __call__(self, ideal)`
- **Constructor**: `def _element_constructor_(self, ideal)`

**Public Methods:**
- `closed_set(self, ideal)`
- `distinguished_open(self, function)`
- `generic_point(self)`
- `le(self, left, right) -> bool`
- `ring(self)`

#### `QuotientLocalizationComparison` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L601`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L601)
- **Bases**: `SageObject`

The canonical compatibility of quotient and localization.

- **Constructor**: `def __init__(self, source_quotient, localization_ring, localized_quotient, quotient_after_localization, forward, inverse, extended_ideal) -> None`

**Public Methods:**
- `extended_ideal(self)`
- `forward(self)`
- `inverse(self)`
- `localization_ring(self)`
- `localized_quotient(self)`
  > Return ``S^{-1}(R/I)``.
- `quotient_after_localization(self)`
  > Return ``S^{-1}R/S^{-1}I``.
- `source_quotient(self)`

#### `RealRelation` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/rings/real.py#L205`](file:///home/dzack/research/src/dzack_research/preamble/rings/real.py#L205)
- **Bases**: `Predicate`

An exact relation between two real numbers awaiting evaluation.

- **Constructor**: `def __init__(self, left: 'ExactRealNumber', right: 'ExactRealNumber', relation)`

**Public Methods:**
- `left(self) -> 'ExactRealNumber'`
- `operator(self)`
- `right(self) -> 'ExactRealNumber'`

#### `UnitInterval` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/rings/unit_interval.py#L59`](file:///home/dzack/research/src/dzack_research/preamble/rings/unit_interval.py#L59)
- **Bases**: `UniqueRepresentation`, `Parent`

The monoid \(([0,1],\oplus)\) with \(s\oplus t=s+t-1\) and identity \(1\).

- **Constructor**: `def __init__(self) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `cardinality(self)`
- `one(self)`
- `zero(self)`
  > The degree of \(L^\infty\), not the monoid identity.

#### `UnitIntervalElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/rings/unit_interval.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/rings/unit_interval.py#L22)
- **Bases**: `Element`

An element of \(([0,1],\oplus)\).

- **Constructor**: `def __init__(self, parent, value) -> None`

**Public Methods:**
- `as_extended_real(self)`
  > This element as a real in \([0,1]\).

### 🛠 Helper Functions & Constructors

#### `AdicCompletion` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AdicCompletion(ring, ideal, *, precision=20)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1361`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1361)

Return a computational realization of the adic completion ``R^``.

The mathematical parent records ``R`` and the ideal of definition;
``precision`` records only the chosen Sage realization.


#### `CommutativeIdeal` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CommutativeIdeal(ring, *generators)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_ideals.py#L324`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_ideals.py#L324)

Return ``(generators) <= R`` with its selected module inclusion.


#### `ComplexField` `[FUNCTION]` `[Internal]`

- **Signature**: `def ComplexField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1132`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1132)

#### `ComplexField` `[FUNCTION]` `[Internal]`

- **Signature**: `def ComplexField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L144`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L144)

#### `CyclotomicField` `[FUNCTION]` `[Internal]`

- **Signature**: `def CyclotomicField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L29`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L29)

#### `CyclotomicField` `[FUNCTION]` `[Internal]`

- **Signature**: `def CyclotomicField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L148`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L148)

#### `DualNumbers` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def DualNumbers(base_ring, name='epsilon')`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1518`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1518)

Return the dual-number algebra ``R[epsilon]/(epsilon^2)``.


#### `FractionField` `[FUNCTION]` `[Internal]`

- **Signature**: `def FractionField(ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L170`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L170)

Return the owned fraction field of ``ring``.


#### `GF` `[FUNCTION]` `[Internal]`

- **Signature**: `def GF(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1101`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1101)

#### `GF` `[FUNCTION]` `[Internal]`

- **Signature**: `def GF(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L117`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L117)

#### `LaurentPolynomialRing` `[FUNCTION]` `[Internal]`

- **Signature**: `def LaurentPolynomialRing(base_ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L164`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L164)

#### `Localization` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Localization(ring, *datum)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1102`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1102)

Return ``S^{-1}R`` from a submonoid ``S -> (R,*)``.

Passing ring elements is convenience syntax for the submonoid they generate.
The mathematical localization datum stored on the result is always the
represented subobject ``S -> (R,*)``.


#### `MatrixSpace` `[FUNCTION]` `[Internal]`

- **Signature**: `def MatrixSpace(base_ring, nrows, ncols=None)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L177`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L177)

Return the public finite matrix Hom, with algebra structure when square.


#### `NumberField` `[FUNCTION]` `[Internal]`

- **Signature**: `def NumberField(polynomial, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L37`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L37)

#### `NumberField` `[FUNCTION]` `[Internal]`

- **Signature**: `def NumberField(polynomial, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L156)

#### `PolynomialRing` `[FUNCTION]` `[Internal]`

- **Signature**: `def PolynomialRing(base_ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L160`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L160)

#### `PowerSeriesRing` `[FUNCTION]` `[Internal]`

- **Signature**: `def PowerSeriesRing(base_ring, *args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1505`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1505)

#### `PrimeField` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def PrimeField(characteristic)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1112`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1112)

#### `PrimeField` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def PrimeField(characteristic)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L124`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L124)

#### `PrimeLocalization` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def PrimeLocalization(ring, prime)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1344`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1344)

Return ``R_p`` using the submonoid ``R \ p -> (R,*)``.


#### `Qp` `[FUNCTION]` `[Internal]`

- **Signature**: `def Qp(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1124`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1124)

#### `Qp` `[FUNCTION]` `[Internal]`

- **Signature**: `def Qp(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L136`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L136)

#### `QuadraticField` `[FUNCTION]` `[Internal]`

- **Signature**: `def QuadraticField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/number_fields.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/number_fields.py#L33)

#### `QuadraticField` `[FUNCTION]` `[Internal]`

- **Signature**: `def QuadraticField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L152`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L152)

#### `QuotientRing` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def QuotientRing(ring, ideal)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1026`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1026)

Return the commutative quotient ring ``R/I`` with its quotient map.


#### `RealApproximation` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def RealApproximation(value)`
- **Source**: [`src/dzack_research/preamble/rings/real.py#L42`](file:///home/dzack/research/src/dzack_research/preamble/rings/real.py#L42)

Return the owned finite-precision real represented by ``value``.


#### `RealField` `[FUNCTION]` `[Internal]`

- **Signature**: `def RealField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1128`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1128)

#### `RealField` `[FUNCTION]` `[Internal]`

- **Signature**: `def RealField(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L140)

#### `ResidueField` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ResidueField(ring, ideal=None)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1229`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1229)

Return ``R/m`` for a maximal ideal, or the represented local residue field.


#### `Zmod` `[FUNCTION]` `[Internal]`

- **Signature**: `def Zmod(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L1116`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L1116)

#### `Zmod` `[FUNCTION]` `[Internal]`

- **Signature**: `def Zmod(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L128`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L128)

#### `Zp` `[FUNCTION]` `[Internal]`

- **Signature**: `def Zp(*args, **kwargs)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1483`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1483)

#### `install_session_rings` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def install_session_rings(scope: dict) -> None`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L243`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L243)

Restore owned scalar objects and public ring constructors in ``scope``.


#### `number_field_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def number_field_homset(domain, codomain) -> NumberFieldHomset`
- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L140`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L140)

#### `order_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def order_homset(domain, codomain) -> OrderHomset`
- **Source**: [`src/dzack_research/preamble/categories/rings/embeddings.py#L228`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/embeddings.py#L228)

#### `predicate_subring` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def predicate_subring(ambient_ring, predicate, description, category=None)`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L240`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L240)

#### `quotient_localization_comparison` `[FUNCTION]` `[Internal]`

- **Signature**: `def quotient_localization_comparison(source_quotient, localization_ring)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1146`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1146)

Return the canonical isomorphism

``S^{-1}(R/I) -> S^{-1}R/S^{-1}I``.

The currently represented comparison requires a chosen finite generating
set of ``S`` so that its image in ``R/I`` is an actual represented
submonoid.


#### `refine_commutative_ring_constructions` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_commutative_ring_constructions(ring)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L92`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L92)

Attach the represented standard construction surface to ``ring``.


#### `refine_power_series_ring` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_power_series_ring(power_series_ring, base_ring, variable=None)`
- **Source**: [`src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1453`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/commutative_algebra.py#L1453)

Record ``R[[t]]`` as a ``(t)``-adically complete ``R``-algebra.


#### `refine_ring_constructions` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_ring_constructions(ring)`
- **Source**: [`src/dzack_research/preamble/categories/rings/rings.py#L28`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/rings.py#L28)

Attach the selected standard construction syntax to an owned ring.


#### `ring_constructor_surface` `[FUNCTION]` `[Internal]`

- **Signature**: `def ring_constructor_surface() -> dict[str, object]`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L213`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L213)

Return the constructors exported into a preamble session.


#### `ring_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def ring_homset(domain, codomain) -> RingHomset`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L151`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L151)

Return the owned Hom-set of unital ring morphisms ``domain -> codomain``.


#### `ring_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def ring_morphism(domain, codomain, function, *, engine_morphism=None) -> RingMorphism`
- **Source**: [`src/dzack_research/preamble/categories/rings/ring_foundation.py#L156`](file:///home/dzack/research/src/dzack_research/preamble/categories/rings/ring_foundation.py#L156)

Construct one owned ring morphism with an optional engine realization.


#### `session_ring_objects` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def session_ring_objects() -> dict[str, object]`
- **Source**: [`src/dzack_research/preamble/rings/__init__.py#L183`](file:///home/dzack/research/src/dzack_research/preamble/rings/__init__.py#L183)

Return the standard session scalar names under their owned parents.



---

<a id="subsystem-schemes"></a>
## Schemes & Algebraic Geometry

> Schemes, Affine/Projective schemes, Subschemes, Varieties, Curves, Surfaces, Polytopes, and Structure sheaves.

### 🏛 Categories & Subcategories

#### `AffineSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L481`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L481)
- **Bases**: `_SchemePropertyCategory`
- **Super Categories**: `[Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `closed_subscheme(self, *equations)`
- `coordinate_algebra(self)`
- `coordinate_ring(self)`
  > Return the owned coordinate ring/algebra of this affine scheme.
- `is_affine(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `AffineSpaces` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L594`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L594)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[AffineSchemes(self.base_ring()), FiniteTypeSchemes(self.base_ring()), SmoothSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `zeta_function(self)`
  > Return ``Z(A^d/F_q,T)=1/(1-q^d T)``.

**Category Instance Methods:**
- `super_categories(self)`

#### `ClosedSubschemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L1056`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L1056)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Schemes(self.base_ring())]`

Closed subschemes equipped with their ambient closed immersion.


**ParentMethods (Methods on Category Objects):**
- `ambient_scheme(self)`
- `codimension(self)`
- `defining_equations(self)`
- `defining_ideal_owned(self)`
- `inclusion(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `ConvexPolygons` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L41`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L41)
- **Bases**: `Category`
- **Super Categories**: `[ConvexPolytopes()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `ConvexPolytopes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L17`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L17)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `Curves` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/varieties.py#L27`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/varieties.py#L27)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Varieties(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `dimension(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `EquationDefinedClosedSubschemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L1113`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L1113)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[ClosedSubschemes(self.base_ring())]`

**Category Instance Methods:**
- `super_categories(self)`

#### `FiberProductSchemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L981`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L981)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[AffineSchemes(self.base_ring())]`

Affine schemes equipped as selected pullbacks of one cospan.


**ParentMethods (Methods on Category Objects):**
- `fiber_product_base(self)`
- `fiber_product_cospan(self)`
- `fiber_product_projections(self)`
- `from_pullback_cone(self, left_map, right_map)`
  > Return the unique represented map into this affine fiber product.
- `left_projection(self)`
- `right_projection(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `FiniteTypeSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L449`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L449)
- **Bases**: `_SchemePropertyCategory`

**ParentMethods (Methods on Category Objects):**
- `is_finite_type(self)`

#### `IntegralSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L457`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L457)
- **Bases**: `_SchemePropertyCategory`

**ParentMethods (Methods on Category Objects):**
- `is_integral(self)`

#### `LatticePolygons` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L53`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L53)
- **Bases**: `Category`
- **Super Categories**: `[ConvexPolygons(), LatticePolytopes()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `LatticePolytopes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L29`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L29)
- **Bases**: `Category`
- **Super Categories**: `[ConvexPolytopes()]`

**Category Instance Methods:**
- `super_categories(self)`

#### `LocallyRingedSpaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L111`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L111)
- **Bases**: `CategoryPacketMethods`, `Category`
- **Super Categories**: `[RingedSpaces()]`

Ringed spaces whose stalks are local rings.


**ParentMethods (Methods on Category Objects):**
- `stalk(self, point)`

**Category Instance Methods:**
- `super_categories(self)`

#### `NormalSchemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L465`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L465)
- **Bases**: `_SchemePropertyCategory`

**ParentMethods (Methods on Category Objects):**
- `is_normal(self)`

#### `OpenSubschemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L1127`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L1127)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Schemes(self.base_ring())]`

Open subschemes equipped with their open immersion.


**Category Instance Methods:**
- `super_categories(self)`

#### `ProductProjectiveSpaces` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L691`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L691)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[ProductSchemes(self.base_ring()), ProjectiveSchemes(self.base_ring()), SmoothSchemes(self.base_ring())]`

Finite products of projective spaces over one base ring.


**Category Instance Methods:**
- `super_categories(self)`

#### `ProductSchemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L660`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L660)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Schemes(self.base_ring())]`

Scheme products equipped with their stated factors and projections.


**ParentMethods (Methods on Category Objects):**
- `factors(self)`
- `number_of_factors(self)`
- `projection(self, index)`
- `projections(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `ProjectiveSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L570`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L570)
- **Bases**: `_SchemePropertyCategory`
- **Super Categories**: `[Schemes(self.base_ring()), QuasiProjectiveSchemes(self.base_ring()), FiniteTypeSchemes(self.base_ring()), SeparatedSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `closed_subscheme(self, *equations)`
- `is_projective(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `ProjectiveSpaces` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L627`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L627)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[ProjectiveSchemes(self.base_ring()), SmoothSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `zeta_function(self)`
  > Return ``Z(P^d/F_q,T)=prod_{i=0}^d(1-q^i T)^(-1)``.

**Category Instance Methods:**
- `super_categories(self)`

#### `QuasiAffineSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L548`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L548)
- **Bases**: `_SchemePropertyCategory`
- **Super Categories**: `[Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `is_quasi_affine(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `QuasiProjectiveSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L559`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L559)
- **Bases**: `_SchemePropertyCategory`
- **Super Categories**: `[Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `is_quasi_projective(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `RingedSpaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L82`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L82)
- **Bases**: `CategoryPacketMethods`, `Category`
- **Super Categories**: `[Sets()]`

Ringed spaces ``(X,O_X)``.


**ParentMethods (Methods on Category Objects):**
- `@cached_method` `structure_sheaf(self)`
- `@cached_method` `underlying_space(self)`

**Category Instance Methods:**
- `LocallyRinged(self)`
- `super_categories(self)`

#### `Schemes` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L201`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L201)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[LocallyRingedSpaces()]`

Schemes over ``Spec(R)`` for the represented base ring ``R``.


**ParentMethods (Methods on Category Objects):**
- `as_slice_object(self)`
- `base_scheme(self)`
- `categorical_identity_morphism(self)`
- `point_count(self, extension_degree=1)`
  > Return ``#X(F_{q^n})`` for the stated extension degree ``n``.
- `point_counts(self, extension_degree)`
  > Return ``(#X(F_q),...,#X(F_{q^n}))`` for a finite base field.
- `point_morphism(self, coordinates)`
- `product(self, *others)`
- `relative_dimension(self)`
- `scheme_base_ring(self)`
- `scheme_category(self)`
- `structure_morphism(self)`

**Category Instance Methods:**
- `Affine(self)`
- `FiniteType(self)`
- `Integral(self)`
- `Normal(self)`
- `Projective(self)`
- `QuasiAffine(self)`
- `QuasiProjective(self)`
- `Separated(self)`
- `Smooth(self)`
- `as_slice_object(self, scheme)`
- `@cached_method` `base_scheme(self)`
- `homset(self, domain, codomain)`
- `product(self, *schemes)`
- `@cached_method` `slice_category(self)`
- `super_categories(self)`

#### `SeparatedSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L441`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L441)
- **Bases**: `_SchemePropertyCategory`

**ParentMethods (Methods on Category Objects):**
- `is_separated(self)`

#### `SmoothSchemes` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L473`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L473)
- **Bases**: `_SchemePropertyCategory`

**ParentMethods (Methods on Category Objects):**
- `is_smooth(self)`

#### `Surfaces` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/varieties.py#L39`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/varieties.py#L39)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Varieties(self.base_ring())]`

**ParentMethods (Methods on Category Objects):**
- `dimension(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `Varieties` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/varieties.py#L12`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/varieties.py#L12)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Schemes(self.base_ring()), IntegralSchemes(self.base_ring()), SeparatedSchemes(self.base_ring()), FiniteTypeSchemes(self.base_ring())]`

Integral separated schemes of finite type over the stated base.


**Category Instance Methods:**
- `super_categories(self)`

### 🔄 Functors & Adjunctions

#### `AffineSpecFunctor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/affine_spec.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/affine_spec.py#L15)
- **Bases**: `ContravariantFunctor`

The contravariant functor ``Spec_R: CAlg_R -> AffSch_R``.

**Constructors / Factory Signatures:**
- `def __init__(self, base_ring) -> None`

**Functor / Adjunction Methods:**
- `base_ring(self)`

#### `affine_spec_functor` `[FUNCTOR]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/affine_spec.py#L41`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/affine_spec.py#L41)
**Constructors / Factory Signatures:**
- `@cached_function` `def affine_spec_functor(base_ring)`

### ⚙ Universal Categorical Constructions

#### `scheme_product` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L896`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L896)

Return the categorical product in the currently supported scheme regimes.

Affine spaces use ``A^m x A^n = A^{m+n}``; products of projective spaces
use Sage's genuine multiprojective scheme backend.  In both cases the
returned scheme retains the stated factors and actual projection
morphisms.  General affine schemes and mixed products belong to the same
surface but require the coordinate-algebra tensor-product/fiber-product
layer and are not silently represented as products of underlying sets.

- **Signature**: `def scheme_product(*schemes)`

### ↗ Morphisms & Hom-Sets

#### `SchemeMorphism` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L33`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L33)
- **Bases**: `Morphism`

Categorical wrapper around one native Sage scheme morphism.

- **Constructor**: `def __init__(self, native_morphism, *, domain=None, codomain=None) -> None`
- **Constructor**: `def _call_(self, value)`

**Public Methods:**
- `codomain(self)`
- `compose(self, before)`
- `coordinate_algebra_morphism(self)`
- `domain(self)`
- `evaluate_at(self, point)`
- `morphisms_agree(self, other) -> bool`
  > Decide equality from represented pullbacks or the native carrier.
- `native_morphism(self)`
- `then(self, after)`

### 📦 Mathematical Objects & Parents

#### `ConvexPolytopeParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L65`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L65)
- **Bases**: `Parent`

A rational convex polytope in a chosen coordinate lattice.

Public coordinate data live in the owned modules ``ZZ^n`` and ``QQ^n``.
Sage's exact ``Polyhedron`` is retained only as the private polyhedral
computation engine.

- **Constructor**: `def __init__(self, vertices, *, lattice=None, require_integral=False) -> None`

**Public Methods:**
- `ambient_lattice(self)`
  > Return the owned coordinate lattice ``ZZ^n``.
- `ambient_space(self)`
  > Return the owned rational coordinate module ``QQ^n``.
- `boundary_integral_points(self)`
- `contains_point(self, point) -> bool`
- `dimension(self)`
- `ehrhart_polynomial(self, variable='t')`
  > Return the exact owned Ehrhart polynomial by interpolation.
- `facets(self)`
  > Return the codimension-one faces as owned polytopes.
- `h_star_vector(self)`
  > Return the owned Ehrhart ``h*`` vector ``(h*_0,...,h*_d)``.
- `integral_points(self)`
- `interior_contains_point(self, point) -> bool`
- `interior_integral_points(self)`
- `is_compact(self) -> bool`
- `is_lattice_polytope(self) -> bool`
- `is_reflexive(self) -> bool`
- `is_smooth(self) -> bool`
- `n_boundary_points(self)`
- `n_integral_points(self)`
- `n_interior_points(self)`
- `n_vertices(self)`
- `normalized_volume(self)`
- `polar_dual(self)`
- `vertices(self)`
- `volume(self)`

#### `SchemeUnderlyingSpace` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L13`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L13)
- **Bases**: `SageObject`

The underlying topological space of a represented ringed space.

Sage's scheme parents do not expose a separate topological-space parent.
The owned API nevertheless keeps the mathematical structure explicit: this
object remembers the represented scheme and is the carrier on which open
and closed-subspace structure can later be attached.

- **Constructor**: `def __init__(self, ringed_space) -> None`

**Public Methods:**
- `ringed_space(self)`

#### `StructureSheaf` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L34`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/ringed_spaces.py#L34)
- **Bases**: `SageObject`

The represented structure sheaf ``O_X`` of a ringed space ``X``.

- **Constructor**: `def __init__(self, ringed_space) -> None`

**Public Methods:**
- `global_sections(self)`
  > Return ``Gamma(X,O_X)`` in the exact cases represented live.
- `ringed_space(self)`
- `sections_on_distinguished_open(self, distinguished_open)`
  > Return ``O_X(D(f)) = Gamma(X,O_X)_f`` for an affine scheme.
- `stalk(self, point)`
  > Return ``O_{X,p}`` for a represented affine prime point.

### 🛠 Helper Functions & Constructors

#### `AffineSpace` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def AffineSpace(dimension, base_ring, names=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L802`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L802)

Return the owned affine space ``A^n_R``.


#### `ConvexPolygon` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ConvexPolygon(vertices, lattice=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L382`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L382)

#### `ConvexPolytope` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ConvexPolytope(vertices, lattice=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L378`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L378)

#### `LatticePolygon` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def LatticePolygon(vertices, lattice=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L393`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L393)

#### `LatticePolytope` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def LatticePolytope(vertices, lattice=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/polytopes.py#L389`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/polytopes.py#L389)

#### `ProjectiveSpace` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ProjectiveSpace(dimension, base_ring, names=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L856`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L856)

Return the owned projective space ``P^n_R``.


#### `Spec` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def Spec(ring_or_algebra)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L719`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L719)

Return the affine scheme ``Spec(A)`` over the represented scalar base.

If ``A`` is an owned commutative ``R``-algebra, the returned object lies in
``Schemes(R)`` and its structure morphism is induced contravariantly by
``R -> A``.  A bare commutative ring ``R`` is read as an ``R``-algebra over
itself, so ``Spec(R)`` remains the terminal affine ``R``-scheme.


#### `affine_spec_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def affine_spec_morphism(algebra_morphism)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L778`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L778)

Return the affine scheme morphism contravariantly induced by an algebra map.


#### `categorical_scheme_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def categorical_scheme_morphism(native_morphism, *, domain=None, codomain=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L148`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L148)

#### `refine_closed_subscheme` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_closed_subscheme(subscheme, ambient=None, *, defining_equations=None)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L1143`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L1143)

#### `refine_scheme` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_scheme(scheme, base_ring=None, categories=())`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L188`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L188)

Adopt a native Sage scheme into the owned scheme hierarchy.


#### `refine_scheme_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine_scheme_morphism(morphism, base_ring)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L182`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L182)

Return a categorical wrapper of the native computational morphism.


#### `scheme_fiber_product` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def scheme_fiber_product(left_map, right_map)`
- **Source**: [`src/dzack_research/preamble/categories/schemes/schemes.py#L1020`](file:///home/dzack/research/src/dzack_research/preamble/categories/schemes/schemes.py#L1020)

Return ``X x_S Y`` for two represented affine scheme maps to ``S``.



---

<a id="subsystem-divisors"></a>
## Divisors & Picard Theory

> Divisor groups, Cartier divisors, Weil divisors, Picard groups, Class groups, and Formal divisors.

### 🏛 Categories & Subcategories

#### `CartierDivisorGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py#L9`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py#L9)
- **Bases**: `Category`
- **Super Categories**: `[FramedModules(_own_ring(SageZZ))]`

**Category Instance Methods:**
- `super_categories(self)`

#### `ClassGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/class_groups.py#L9`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/class_groups.py#L9)
- **Bases**: `Category`
- **Super Categories**: `[FramedModules(_own_ring(SageZZ))]`

**Category Instance Methods:**
- `super_categories(self)`

#### `DivisorGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/divisor_groups.py#L20`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/divisor_groups.py#L20)
- **Bases**: `Category`
- **Super Categories**: `[FramedFreeModules(_own_ring(SageZZ))]`

Free abelian groups on specified prime divisors.


**Category Instance Methods:**
- `super_categories(self)`

#### `FormalDivisorGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/divisor_groups.py#L43`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/divisor_groups.py#L43)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[FramedFreeModules(self.base_ring())]`

Formal divisors with coefficients in a specified ring.


**ParentMethods (Methods on Category Objects):**
- `components(self, divisor)`
- `divisor_latex(self, divisor) -> str`
- `divisor_repr(self, divisor) -> str`
- `terms(self, divisor)`

**Category Instance Methods:**
- `super_categories(self)`

#### `PicardGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/picard_groups.py#L9`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/picard_groups.py#L9)
- **Bases**: `Category`
- **Super Categories**: `[FramedModules(_own_ring(SageZZ))]`

**Category Instance Methods:**
- `super_categories(self)`

#### `WeilDivisorGroups` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py#L10`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py#L10)
- **Bases**: `Category`
- **Super Categories**: `[DivisorGroups()]`

**Category Instance Methods:**
- `super_categories(self)`

### 🛠 Helper Functions & Constructors

#### `CartierDivisorGroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CartierDivisorGroup(module)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py#L21`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py#L21)

#### `ClassGroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ClassGroup(module)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/class_groups.py#L21`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/class_groups.py#L21)

#### `DivisorGroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def DivisorGroup(module)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/divisor_groups.py#L34`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/divisor_groups.py#L34)

#### `FormalDivisor` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def FormalDivisor(coefficient_ring, terms)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/divisor_groups.py#L92`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/divisor_groups.py#L92)

Return the formal linear combination of the stated prime divisors.

The divisor is an element of ``FormalDivisorGroup(R, S)`` for ``S`` the
prime divisors in ``terms``, in order of first appearance; that group
answers ``terms``, ``components`` and printing for it.


#### `FormalDivisorGroup` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function` `def FormalDivisorGroup(coefficient_ring, prime_divisors)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/divisor_groups.py#L83`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/divisor_groups.py#L83)

Return the group of formal divisors on the stated prime divisors, one per ``(R, S)``.


#### `PicardGroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def PicardGroup(module)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/picard_groups.py#L21`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/picard_groups.py#L21)

#### `WeilDivisorGroup` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def WeilDivisorGroup(module)`
- **Source**: [`src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py#L19)


---

<a id="subsystem-forms"></a>
## Bilinear Forms, Quadratic Forms & Pairings

> Bilinear/Quadratic forms, Pairings, Gram matrices, and Form spaces.

### 🏛 Categories & Subcategories

#### `BilinearFormHoms` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L29`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L29)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[InternalHomModules(self.base_ring())]`

Diagonal pairing Hom objects carrying the bilinear-form operations.


**ElementMethods (Methods on Category Elements):**
- `gram_tensor(self)`
- `pullback(self, morphism)`

**Category Instance Methods:**
- `super_categories(self)`

### 🛠 Helper Functions & Constructors

#### `BilinearForms` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def BilinearForms(module, value_module)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L388`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L388)

Return ``Hom_R(M tensor_R M,W)`` whenever that universal object exists.


#### `Pairings` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Pairings(left_module, right_module, value_module)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L371`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L371)

Return ``Hom_R(X tensor_R Y,W)`` whenever that universal object exists.


#### `QuadraticForms` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def QuadraticForms(module, value_module)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L406`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L406)

Return ``Hom_R(Gamma^2(M),W)`` whenever the divided square is represented.


#### `QuadraticMap` `[FUNCTION]` `[Internal]`

- **Signature**: `def QuadraticMap(module, value_module, function)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L434`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L434)

Return the quadratic map ``module -> value_module`` via its classifier.


#### `classifying_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def classifying_morphism(quadratic)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L441`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L441)

Return the unique linear map ``Gamma^2(M) -> W`` classifying ``quadratic``.


#### `gram_tensor_from_graph` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def gram_tensor_from_graph(graph, base_ring)`
- **Source**: [`src/dzack_research/preamble/categories/forms/gram_matrices.py#L26`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/gram_matrices.py#L26)

Recover the type-``(0,2)`` Gram tensor presented by a weighted graph.


#### `gram_tensor_graph` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def gram_tensor_graph(gram)`
- **Source**: [`src/dzack_research/preamble/categories/forms/gram_matrices.py#L8`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/gram_matrices.py#L8)

Return the weighted undirected graph presented by a symmetric Gram tensor.


#### `is_bilinear_form` `[FUNCTION]` `[Internal]`

- **Signature**: `def is_bilinear_form(form) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L348`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L348)

#### `is_quadratic_form` `[FUNCTION]` `[Internal]`

- **Signature**: `def is_quadratic_form(form) -> bool`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L361`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L361)

#### `quadratic_map_from_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def quadratic_map_from_morphism(module, morphism)`
- **Source**: [`src/dzack_research/preamble/categories/forms/forms.py#L454`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/forms.py#L454)

Recover the quadratic map classified by ``morphism: Gamma^2(M) -> W``.


#### `tensor_connected_component_cuts` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def tensor_connected_component_cuts(gram) -> list[int]`
- **Source**: [`src/dzack_research/preamble/categories/forms/gram_matrices.py#L43`](file:///home/dzack/research/src/dzack_research/preamble/categories/forms/gram_matrices.py#L43)

Return cuts between consecutive connected diagonal blocks.



---

<a id="subsystem-functions"></a>
## Function Spaces & Analysis

> Lebesgue modules, Lp, ell, C(X), Graded Lebesgue algebras, and Convolution algebras.

### 🏛 Categories & Subcategories

#### `GradedTensorProductModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L196`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L196)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Tensor squares of Lebesgue graded modules.

Elements are finite sums of homogeneous pure tensors. This is not the
finitely presented tensor product: the summands \(L^{1/s}\) are not
finitely presented \(\mathbb R\)-modules.


**ParentMethods (Methods on Category Objects):**
- `pure_tensor(self, left_element, right_element)`
  > Return the image of \((left, right)\) under \(\otimes\).
- `tensor_factor(self, index)`
- `tensor_factors(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `LebesgueGradedModules` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L107)
- **Bases**: `OwnedCategoryOverBaseRing`
- **Super Categories**: `[Modules(self.base_ring())]`

Graded modules whose homogeneous pieces are Lebesgue spaces \(L^{1/s}\).


**ParentMethods (Methods on Category Objects):**
- `algebra_from_multiplication(self, multiplication, *, unital=True)`
  > Equip this graded Lebesgue module with its represented product.
- `degree_projection(self, degree)`
  > The projection \(\pi_s\colon N\to L^{1/s}\) onto a homogeneous piece.
- `integral_form(self)`
  > The linear form \(\varepsilon=\iota\circ\pi_1\colon N\to\mathbb R\).
- `integral_pairing(self)`
  > The pairing \(B\) as an element of \(\operatorname{Hom}(A\otimes A,\mathbb R)\).
- `integral_pairing_morphism(self)`
  > The pairing \(B=\varepsilon\circ m\colon A\otimes_{\mathbb R}A\to\mathbb R\).
- `integration_of_degree_one(self)`
  > Integration \(\iota\colon L^1\to\mathbb R\) of the degree-\(1\) piece.
- `unit_piece_projection(self)`
  > The graded augmentation \(A\to A_u\), for a unital graded algebra.

**Category Instance Methods:**
- `super_categories(self)`

### ↗ Morphisms & Hom-Sets

#### `LebesgueModuleHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L261`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L261)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, evaluate)`

#### `LebesgueModuleMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L236`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L236)
- **Bases**: `Morphism`

An \(R\)-linear map specified by its action on elements.

- **Constructor**: `def __init__(self, parent, evaluate) -> None`
- **Constructor**: `def _call_(self, element)`

**Public Methods:**
- `then(self, other)`
  > Return ``other ∘ self``.

### 📦 Mathematical Objects & Parents

#### `GradedLebesgueModule` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L518`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L518)
- **Bases**: `UniqueRepresentation`, `Parent`

The \(M\)-graded module \(\bigoplus_{s\in M} L^{1/s}\).

The monoid \(M\) supplies the index of Hölder degrees. The full
family uses \(([0,\infty],+)\); convolution uses \(([0,1],\oplus)\).

- **Constructor**: `def __init__(self, grading_monoid) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `graded_piece(self, degree)`
  > The homogeneous summand \(L^{1/s}\) in Hölder degree \(s\).
- `zero(self)`

#### `GradedTensorSquare` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L396`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L396)
- **Bases**: `UniqueRepresentation`, `Parent`

The tensor square \(N\otimes_{\mathbb R} N\) of a Lebesgue graded module.

- **Constructor**: `def __init__(self, module) -> None`

**Public Methods:**
- `zero(self)`

#### `Lp` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/functions/real_functions.py#L765`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/real_functions.py#L765)
- **Bases**: `_FunctionSpace`

The \(\mathbb R\)-module \(L^p(\mathbb R)\), represented by functions.

\(L^2(\mathbb R)\) is a module with the symmetric bilinear form
\(b(f,g)=\int_{\mathbb R}fg\).  A general \(L^p\) is not: Hölder pairs it
with \(L^{p'}\) as \(L^p * L^{p'}\).

EXAMPLES::

    sage: from dzack_research.preamble.all import (
    ....:     C, FormModules, FormedModules, Lp, PairedModules, RR,
    ....:     SymmetricBilinearFormModules, VectorSpaces, exp,
    ....: )
    sage: L = Lp(2)
    sage: L
    L^2(RR)
    sage: L in VectorSpaces(RR)
    True
    sage: L in SymmetricBilinearFormModules(RR)
    True
    sage: L in FormedModules(RR)
    True
    sage: L in PairedModules(RR)
    True
    sage: Lp(1) in FormModules(RR)
    False
    sage: Maps = C(Infinity, RR)
    sage: gaussian = Maps(exp(-Maps.indeterminate() ** 2))
    sage: L(gaussian)(0)
    1
    sage: L.b(L(gaussian), L(gaussian))
    1/2*sqrt(2)*sqrt(pi)
    sage: L.q(L(gaussian))
    1/2*sqrt(2)*sqrt(pi)
    sage: L.pairing_module() is L
    True
    sage: Lp(1) * Lp(Infinity) in PairedModules(RR)
    True
    sage: Lp(1) * Lp(Infinity) in FormedModules(RR)
    False

- **Constructor**: `def __init__(self, p) -> None`

**Public Methods:**
- `conjugate_lebesgue_space(self)`
  > The space \(L^{p'}\) with \(1/p+1/p'=1\).
- `differentiability(self)`
  > Lebesgue classes are not a \(C^k\) mapping space.
- `integrability_exponent(self)`
- `@cached_method` `pairing_module(self)`
  > The Hölder pairing module \(L^p\otimes L^{p'}\to\mathbb R\).

### 🛠 Helper Functions & Constructors

#### `graded_lebesgue_algebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def graded_lebesgue_algebra()`
- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L608`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L608)

The pointwise algebra \(\bigoplus_s L^{1/s}\), interned from its product.


#### `integration_morphism` `[FUNCTION]` `[Internal]`

- **Signature**: `def integration_morphism(space)`
- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L283`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L283)

Integration \(\iota\colon L^1(\mathbb R)\to\mathbb R\), \(\iota(f)=\int f\).


#### `intern_graded_lebesgue_algebra` `[FUNCTION]` `[Internal]`

- **Signature**: `def intern_graded_lebesgue_algebra(multiplication, ring, unital)`
- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L565`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L565)

Intern a Lebesgue graded module on a morphism of its tensor square.


#### `lebesgue_convolution_algebra` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def lebesgue_convolution_algebra()`
- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L618`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L618)

The convolution algebra \(\bigoplus_{s\in[0,1]} L^{1/s}\), interned from its product.


#### `lebesgue_module_homset` `[FUNCTION]` `[Internal]`

- **Signature**: `def lebesgue_module_homset(domain, codomain) -> LebesgueModuleHomset`
- **Source**: [`src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L279`](file:///home/dzack/research/src/dzack_research/preamble/categories/functions/lebesgue_graded.py#L279)


---

<a id="subsystem-sets"></a>
## Sets, Cardinals & Ordinals

> Sets, Cardinalities, Ordinals, Enumerated sets, Fourier characters, Hermite polynomials, and Power sets.

### 🏛 Categories & Subcategories

#### `Cardinalities` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L99`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L99)
- **Bases**: `Category`
- **Super Categories**: `[Objects()]`

The thin category associated to the represented cardinal order.


**Category Instance Methods:**
- `are_incomparable(self, source, target) -> bool`
- `compare(self, source, target) -> CardinalComparison`
- `ge(self, source, target) -> bool`
- `gt(self, source, target) -> bool`
- `hom(self, domain, codomain) -> CardinalityHomset`
- `indexed_product(self, index_set: Parent, factors: Callable)`
- `indexed_sum(self, index_set: Parent, summands: Callable)`
- `le(self, source, target) -> bool`
- `lt(self, source, target) -> bool`
- `one(self)`
- `power(self, base, exponent)`
- `product(self, *factors)`
- `sum(self, *summands)`
- `super_categories(self)`
- `supremum(self, *cardinal_numbers)`
- `zero(self)`

#### `CartesianProductsOfSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L704`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L704)
- **Bases**: `Category`
- **Super Categories**: `[SageSets()]`

Dependent products of families of sets.


**Category Instance Methods:**
- `super_categories(self)`

#### `CoproductsOfSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L711`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L711)
- **Bases**: `Category`
- **Super Categories**: `[SageSets()]`

Dependent coproducts (disjoint unions) of families of sets.


**Category Instance Methods:**
- `super_categories(self)`

#### `CountableSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1315`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1315)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Sets equipped with a countable enumeration.


**Category Instance Methods:**
- `super_categories(self)`

#### `CountablyInfiniteSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1332`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1332)
- **Bases**: `Category`
- **Super Categories**: `[CountableSets(), InfiniteSets()]`

Countably infinite sets.


**Category Instance Methods:**
- `super_categories(self)`

#### `EnumeratedByIntegers` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L89`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L89)
- **Bases**: `Category`
- **Super Categories**: `[InfiniteEnumeratedSets()]`

Infinite enumerated sets whose functions are indexed by \(\mathbb Z\).

Sage's ranking still runs through \(\mathbb N\); :meth:`function` takes the
integer index, and :meth:`unrank` takes the corresponding natural number.


**ParentMethods (Methods on Category Objects):**
- `function(self, index)`
- `index_set(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `EnumeratedByNaturals` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L75`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L75)
- **Bases**: `Category`
- **Super Categories**: `[InfiniteEnumeratedSets()]`

Infinite enumerated sets ranked by \(\mathbb N\).


**ParentMethods (Methods on Category Objects):**
- `function(self, index)`
- `index_set(self)`

**Category Instance Methods:**
- `super_categories(self)`

#### `EnumeratedSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L31`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L31)
- **Bases**: `Category`
- **Super Categories**: `[SageEnumeratedSets()]`

Sets equipped with a represented ranking/enumeration.


**Category Instance Methods:**
- `super_categories(self)`

#### `FiniteSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1283`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1283)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Sets whose cardinality is finite.


**Category Instance Methods:**
- `super_categories(self)`

#### `FinitelySupportedFunctionSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1478`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1478)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Function sets whose elements have finite support.


**Category Instance Methods:**
- `super_categories(self)`

#### `FunctionEnumeratedSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L68`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L68)
- **Bases**: `Category`
- **Super Categories**: `[EnumeratedSets()]`

Enumerated sets whose elements stand for functions.


**Category Instance Methods:**
- `super_categories(self)`

#### `Homsets` `[CATEGORY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1272`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1272)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Hom objects \(\operatorname{Hom}(X,Y)\), which are sets.


**ParentMethods (Methods on Category Objects):**
- `is_endomorphism_set(self) -> bool`

**Category Instance Methods:**
- `super_categories(self)`

#### `InfiniteEnumeratedSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L38`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L38)
- **Bases**: `Category`
- **Super Categories**: `[SageInfiniteEnumeratedSets(), EnumeratedSets()]`

Countably infinite enumerated sets.


**Category Instance Methods:**
- `super_categories(self)`

#### `InfiniteSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1300`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1300)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Sets whose cardinality is infinite.


**Category Instance Methods:**
- `super_categories(self)`

#### `OrdinalSemirings` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L514`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L514)
- **Bases**: `Category`
- **Super Categories**: `[SageSets(), Semirings().Commutative()]`

The category containing the ordinal semiring under natural operations.


**Category Instance Methods:**
- `super_categories(self)`

#### `PartiallyOrderedSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1366`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1366)
- **Bases**: `Category`
- **Super Categories**: `[Sets()]`

Sets equipped with a partial order.


**Category Instance Methods:**
- `super_categories(self)`

#### `Sets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L149`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L149)
- **Bases**: `Category`
- **Super Categories**: `[SetsWithPartialMaps()]`

The owned category of sets.

All Sage set objects are admitted.  The category owns the mathematical
constructions the preamble adds; Sage remains the implementation of
ordinary set maps.

Every owned object is realised as a Sage ``Parent``, and Sage's coercion
layer states one thing about every parent it converts into: it is an
object of ``SetsWithPartialMaps``, the category of sets whose maps may be
partial.  That is the single crossing between the owned graph and Sage's,
declared once here at the root; no owned category below it names a Sage
category.


**ParentMethods (Methods on Category Objects):**
- `exponential(self, exponent)`
- `finite_subsets(self)`
- `power_set(self)`
- `subsets_of_size(self, size)`

**SubcategoryMethods (Subcategory Refinements):**
- `Homsets(self)`
  > A Hom object of any owned category is a set.

**Category Instance Methods:**
- `Countable(self)`
- `CountablyInfinite(self)`
- `PartiallyOrdered(self)`
- `TotallyOrdered(self)`
- `Uncountable(self)`
- `hom(self, domain, codomain)`
- `identity(self, set_object)`
- `super_categories(self)`

#### `TotallyOrderedSets` `[CATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1373`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1373)
- **Bases**: `Category`
- **Super Categories**: `[PartiallyOrderedSets()]`

Sets equipped with a total order.


**Category Instance Methods:**
- `super_categories(self)`

#### `UncountableSets` `[SUBCATEGORY]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1349`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1349)
- **Bases**: `Category`
- **Super Categories**: `[InfiniteSets()]`

Sets whose represented cardinal is provably uncountable.


**Category Instance Methods:**
- `super_categories(self)`

### ⚙ Universal Categorical Constructions

#### `cartesian_product_of` `[CONSTRUCTION]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L985`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L985)
- **Signature**: `def cartesian_product_of(factors)`

### ↗ Morphisms & Hom-Sets

#### `CardinalityHomset` `[HOMSET]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L74`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L74)
- **Bases**: `Homset`
- **Constructor**: `def __init__(self, domain, codomain) -> None`
- **Constructor**: `def _element_constructor_(self, morphism=None)`

**Public Methods:**
- `cardinality(self)`
- `identity(self)`
- `unique_morphism(self)`

#### `CardinalityMorphism` `[MORPHISM]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L66`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L66)
- **Bases**: `Morphism`
- **Constructor**: `def __init__(self, parent) -> None`

#### `SetInclusion` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L288`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L288)
- **Bases**: `SetMorphism`

A represented subobject inclusion \(A\hookrightarrow X\).

- **Constructor**: `def __init__(self, domain, codomain, characteristic_morphism=None, finite_members=None) -> None`

**Public Methods:**
- `cardinality(self)`
- `characteristic_morphism(self)`
- `complement(self)`
- `difference(self, other)`
- `factor_through(self, target_inclusion)`
  > Return the canonical map of subset objects when this subset is contained.
- `inclusion(self)`
- `intersection(self, other)`
- `is_injective(self) -> bool`
- `symmetric_difference(self, other)`
- `underlying_set(self)`
- `union(self, other)`

#### `SetInjection` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L266`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L266)
- **Bases**: `SetMorphism`

A set morphism supplied with the assertion that it is injective.


**Public Methods:**
- `is_injective(self) -> bool`

#### `SetSurjection` `[MORPHISM]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L273`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L273)
- **Bases**: `SetMorphism`

A set morphism supplied with the assertion that it is surjective.


**Public Methods:**
- `is_surjective(self) -> bool`

### 📦 Mathematical Objects & Parents

#### `Cardinal` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L304`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L304)
- **Bases**: `Parent`

A cardinal number as an object of the thin cardinal-order category.

- **Constructor**: `def __init__(self, expression) -> None`

**Public Methods:**
- `aleph_index(self)`
- `cardinality(self)`
- `expression(self)`
- `finite_value(self)`
  > Return the ordinary nonnegative integer representing this finite cardinal.
- `initial_ordinal(self)`
- `is_aleph(self) -> bool`
- `is_continuum(self) -> bool`
- `is_countable(self) -> bool`
- `is_countably_infinite(self) -> bool`
- `is_finite(self) -> bool`
- `is_infinite(self) -> bool`
- `is_uncountable(self) -> bool`
- `is_uncountably_infinite(self) -> bool`
- `sort_key(self) -> tuple[int, str]`

#### `CardinalComparison` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L57`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L57)
- **Bases**: `Enum`

#### `CartesianProductElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L721`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L721)
- **Bases**: `Element`

A section ``i |-> x_i`` of a family of sets.

- **Constructor**: `def __init__(self, parent, components) -> None`

**Public Methods:**
- `component(self, index)`

#### `CartesianProductOfFamilyParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L773`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L773)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, index_set, family) -> None`
- **Constructor**: `def _element_constructor_(self, components)`

**Public Methods:**
- `cardinality(self)`
- `factor(self, index)`
- `family(self)`
- `from_maps(self, source, maps)`
  > Return the unique map into the product with the stated components.
- `has_finite_index_set(self) -> bool`
- `index_set(self)`
- `projection(self, index)`
- `rank(self, section)`
  > Return the mixed-radix position of a finite product section.
- `unrank(self, position)`
  > Return the finite product section in mixed-radix order.

#### `CoproductElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1001`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1001)
- **Bases**: `Element`

An element of a dependent sum, carrying its summand index.

- **Constructor**: `def __init__(self, parent, index, value) -> None`

**Public Methods:**
- `summand_element(self)`
- `summand_index(self)`

#### `CoproductOfFamilyParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1034`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1034)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, index_set, family) -> None`
- **Constructor**: `def _element_constructor_(self, datum, value=None)`

**Public Methods:**
- `cardinality(self)`
- `cofactor(self, index)`
- `family(self)`
- `from_maps(self, target, maps)`
  > Return the unique map out of the coproduct extending the stated maps.
- `index_set(self)`
- `injection(self, index)`
- `rank(self, element)`
  > Return the lazy enumeration rank of one coproduct element.
- `unrank(self, position)`
  > Return a coproduct element in lazy rank-layer/diagonal order.

#### `FiniteFilteredOrderedSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L253`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L253)
- **Bases**: `OrderedEnumeratedSet`

A finite ordered subset selected lazily by a predicate.

- **Constructor**: `def __init__(self, source, predicate, *, name=None) -> None`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `cardinality(self)`
- `le(self, left, right) -> bool`
- `predicate(self)`
- `rank(self, element)`
- `source(self)`
- `unrank(self, position)`

#### `FiniteOrderedSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L111`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L111)
- **Bases**: `OrderedEnumeratedSet`

A finite ordered set without sequence-valued mathematical storage.

- **Constructor**: `def __init__(self, elements) -> None`

**Public Methods:**
- `@classmethod` `from_indexed(cls, index_set, unrank, *, rank=None, contains=None, name=None)`

#### `FiniteOrdinalSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L45`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L45)
- **Bases**: `Parent`

The canonical finite ordinal ``{0,...,size-1}`` as a lazy owned set.

- **Constructor**: `def __init__(self, size) -> None`
- **Constructor**: `def __call__(self, element)`

**Public Methods:**
- `cardinality(self)`
- `le(self, left, right)`
- `rank(self, element)`
- `unrank(self, position)`

#### `FiniteSubsetsParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L658`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L658)
- **Bases**: `Parent`

The set \(P_{fin}(X)\) of finite subsets of ``X``.

- **Constructor**: `def __init__(self, source) -> None`
- **Constructor**: `def _element_constructor_(self, members)`

**Public Methods:**
- `cardinality(self)`
- `power_set(self)`
- `source(self)`

#### `FixedCardinalitySubsets` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L595`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L595)
- **Bases**: `Parent`

The set \([X]^k\) of subsets of a fixed finite cardinality.

- **Constructor**: `def __init__(self, source, subset_cardinality) -> None`
- **Constructor**: `def _element_constructor_(self, members)`

**Public Methods:**
- `cardinality(self)`
- `power_set(self)`
- `source(self)`
- `subset_cardinality(self)`

#### `FixedSizeSelectionElement` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L53`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L53)
- **Bases**: `Element`

One fixed-size subset/multiset, encoded by its combinatorial rank.

- **Constructor**: `def __init__(self, parent, combinatorial_rank) -> None`

**Public Methods:**
- `add_label(self, label)`
- `allows_repetition(self) -> bool`
- `combinatorial_rank(self) -> int`
- `degree(self) -> int`
- `merged_with(self, other)`
- `multiplicity(self, label) -> int`
- `support(self)`
- `wedge_with(self, other)`
- `word(self)`

#### `FixedSizeSelections` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L202`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L202)
- **Bases**: `Parent`
- **Constructor**: `def __init__(self, source, selection_size, *, repetition) -> None`
- **Constructor**: `def _element_constructor_(self, datum)`

**Public Methods:**
- `allows_repetition(self) -> bool`
- `cardinality(self)`
- `from_labels(self, labels)`
- `from_multiplicities(self, multiplicities)`
- `from_source_rank_positions(self, positions)`
- `rank(self, selection)`
- `selection_size(self) -> int`
- `singleton_power(self, label)`
- `source(self)`
- `unrank(self, position)`
- `with_size(self, selection_size)`

#### `FourierCharacters` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/fourier_characters.py#L18`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/fourier_characters.py#L18)
- **Bases**: `UniqueRepresentation`, `Parent`

The enumerated set \(\{e^{i n x} : n\in\mathbb Z\}\) as symbols \(F_n\in\mathrm{SR}\).

Each character is the formal symbol \(F_n\), not an evaluated
exponential, so \(F_0\) does not collapse to \(1\).

- **Constructor**: `def __init__(self) -> None`

**Public Methods:**
- `cardinality(self)`
- `rank(self, elt)`
- `unrank(self, n)`

#### `FunctionSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L556`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L556)
- **Bases**: `Parent`

The exponential \(Y^X=\operatorname{Hom}_{Set}(X,Y)\).

- **Constructor**: `def __init__(self, codomain, exponent) -> None`
- **Constructor**: `def _element_constructor_(self, definition)`

**Public Methods:**
- `base(self)`
- `cardinality(self)`
- `exponent(self)`
- `homset(self)`

#### `HermitePolynomials` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/hermite_polynomials.py#L21`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/hermite_polynomials.py#L21)
- **Bases**: `UniqueRepresentation`, `Parent`

The enumerated set \(\{H_n : n\in\mathbb N\}\subset\mathrm{SR}\).

- **Constructor**: `def __init__(self) -> None`

**Public Methods:**
- `cardinality(self)`
- `rank(self, elt)`
- `unrank(self, n)`

#### `IndexedFamily` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L6`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L6)
- **Bases**: `SageObject`

A family ``(x_i)_{i in I}`` retaining its indexing set.

A family is not the set of its values: different indices may have equal
values.  It therefore has no inverse ``rank(value)`` operation in general.
Consumers iterate values lazily or address them through ``value(index)``.

- **Constructor**: `def __init__(self, index_set, value, *, name=None) -> None`

**Public Methods:**
- `cardinality(self)`
- `index_set(self)`
- `items(self)`
- `map(self, function, *, name=None)`
- `unrank(self, position)`
- `value(self, index)`

#### `LaurentMonomials` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/laurent_monomials.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/laurent_monomials.py#L22)
- **Bases**: `UniqueRepresentation`, `Parent`

The enumerated set \(\{z^n : n\in\mathbb Z\}\subset\mathrm{SR}\).

- **Constructor**: `def __init__(self) -> None`

**Public Methods:**
- `cardinality(self)`
- `rank(self, elt)`
- `unrank(self, n)`

#### `NaturalNumber` `[ELEMENT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1380`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1380)
- **Bases**: `Element`

An element of the owned natural-number set.

- **Constructor**: `def __init__(self, parent, value) -> None`

#### `NaturalNumbers` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1432`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1432)
- **Bases**: `Parent`

The owned set ``N={0,1,2,...}``.

- **Constructor**: `def __init__(self) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `cardinality(self)`
- `rank(self, value)`
- `unrank(self, index)`
- `zero(self)`

#### `OrderedEnumeratedSet` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L19)
- **Bases**: `Parent`

An ordered set presented by an index set and rank/unrank data.

The mathematical collection remains this parent.  Iteration pulls values
lazily from the index set; no Python sequence of all members is stored.

- **Constructor**: `def __init__(self, index_set, unrank, *, rank=None, contains=None, name=None, finite=False) -> None`
- **Constructor**: `def __call__(self, element)`
- **Constructor**: `def _element_constructor_(self, element)`

**Public Methods:**
- `cardinality(self)`
- `index_set(self)`
- `le(self, left, right) -> bool`
- `rank(self, element)`
- `unrank(self, position)`

#### `Ordinal` `[ELEMENT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L521`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L521)
- **Bases**: `Element`

An ordinal represented by a symbolic arithmetic expression.

- **Constructor**: `def __init__(self, parent, expression) -> None`

**Public Methods:**
- `cardinality(self)`
- `expression(self)`
- `initial_index(self)`
- `is_initial(self) -> bool`
- `ordinal_power(self, exponent)`
- `ordinal_product(self, other)`
- `ordinal_sum(self, other)`

#### `OrdinalSemiring` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L666`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L666)
- **Bases**: `UniqueRepresentation`, `Parent`
- **Constructor**: `def __init__(self) -> None`
- **Constructor**: `def _element_constructor_(self, value)`

**Public Methods:**
- `from_expression(self, expression) -> Ordinal`
- `initial(self, index) -> Ordinal`
- `natural_product(self, *factors) -> Ordinal`
- `natural_sum(self, *summands) -> Ordinal`
- `one(self) -> Ordinal`
- `proves_le(self, left, right) -> bool`
- `zero(self) -> Ordinal`

#### `PowerSetParent` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L419`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L419)
- **Bases**: `Parent`

The power object \(P(X)\), represented by subobjects of ``X``.

- **Constructor**: `def __init__(self, base_set) -> None`
- **Constructor**: `def _element_constructor_(self, candidate)`

**Public Methods:**
- `base_set(self)`
- `bottom(self)`
- `cardinality(self)`
- `cardinality_comparison(self)`
- `characteristic_homset(self)`
- `direct_image_morphism(self, morphism)`
- `from_characteristic_morphism(self, characteristic_morphism)`
- `from_predicate(self, predicate: Callable)`
- `inverse_image_morphism(self, morphism)`
- `top(self)`
- `truth_values(self)`

#### `SetSubcategoryMethods` `[OBJECT]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1506`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1506)

Compatibility name for the owned Set category-navigation surface.


#### `SincTranslates` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/sinc_translates.py#L22`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/sinc_translates.py#L22)
- **Bases**: `UniqueRepresentation`, `Parent`

The enumerated set \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\subset\mathrm{SR}\).

Each translate is the formal symbol \(\mathrm{sinc}_n\), not Sage's
evaluated \(\operatorname{sinc}\).

- **Constructor**: `def __init__(self) -> None`

**Public Methods:**
- `cardinality(self)`
- `rank(self, elt)`
- `unrank(self, n)`

### 📚 Catalogues & Named Tables

#### `register_set_axioms` `[REGISTRY]` `[Internal]`

- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1501`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1501)

Compatibility entry point: the live owned categories need no Sage-global mutation.


### 🛠 Helper Functions & Constructors

#### `CartesianProductMorphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CartesianProductMorphism(source, target, component_morphisms)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L989`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L989)

Return the componentwise map between two dependent products.


#### `CartesianProductOfFamily` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def CartesianProductOfFamily(index_set, family)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L969`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L969)

#### `CartesianProductOfSets` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CartesianProductOfSets(*factors)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L981`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L981)

#### `ConditionSet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ConditionSet(universe, predicate)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L250`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L250)

Return the subset of ``universe`` cut out by ``predicate``.


#### `CoproductMorphism` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CoproductMorphism(source, target, component_morphisms)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1253`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1253)

Return the componentwise map between two dependent coproducts.


#### `CoproductOfFamily` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def CoproductOfFamily(index_set, family)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1237`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1237)

#### `CoproductOfSets` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def CoproductOfSets(*cofactors)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1249`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1249)

#### `ExponentialOfSets` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def ExponentialOfSets(codomain, exponent)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L591`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L591)

#### `FiniteSubsets` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def FiniteSubsets(source)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L700`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L700)

#### `ImageSet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ImageSet(map_, domain_subset, *, category=None, is_injective=None, inverse=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L255`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L255)

Return the image of ``domain_subset`` under ``map_``.


#### `Ordinals` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def Ordinals() -> OrdinalSemiring`
- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L770`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L770)

#### `PowerSet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def PowerSet(base_set)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L552`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L552)

#### `Set` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Set(source)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L245`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L245)

Return ``source`` as a Sage set object.


#### `SubsetsOfSize` `[FUNCTION]` `[Exported Session]`

- **Signature**: `@cached_function` `def SubsetsOfSize(source, subset_cardinality)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L654`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L654)

#### `aleph` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def aleph(index) -> Cardinal`
- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L809`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L809)

#### `cardinal` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def cardinal(value) -> Cardinal`
- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L790`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L790)

#### `coerce_family_value` `[FUNCTION]` `[Internal]`

- **Signature**: `def coerce_family_value(value_module, value)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L113`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L113)

#### `coordinate_family` `[FUNCTION]` `[Internal]`

- **Signature**: `def coordinate_family(left_labels, right_labels, value_module, datum, *, name)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L121`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L121)

Parse finite rectangular data as a family indexed by ``left × right``.


#### `coordinate_family_from_function` `[FUNCTION]` `[Internal]`

- **Signature**: `def coordinate_family_from_function(left_labels, right_labels, value_module, function, *, name)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L188`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L188)

#### `coordinate_index_set` `[FUNCTION]` `[Internal]`

- **Signature**: `def coordinate_index_set(left_labels, right_labels)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L100`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L100)

Return the dependent two-factor index set for a rectangular family.


#### `coordinate_pair` `[FUNCTION]` `[Internal]`

- **Signature**: `def coordinate_pair(values, left_label, right_label)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L181`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L181)

#### `finite_framing` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_framing(module)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L90`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L90)

Return a selected module framing after asserting that it is finite.


#### `finite_ordered_filter` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_ordered_filter(source, predicate, *, name=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L356`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L356)

Return the finite ordered subset cut out by ``predicate`` lazily.


#### `finite_ordered_image` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_ordered_image(index_set, unrank, *, rank=None, contains=None, name=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L345`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L345)

Return a finite ordered image without materializing its members.


#### `finite_ordered_set` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_ordered_set(elements) -> FiniteOrderedSet`
- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L361`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L361)

Transport one known finite ordered enumeration to an owned set.


#### `finite_ordinal_set` `[FUNCTION]` `[Internal]`

- **Signature**: `def finite_ordinal_set(size)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L111`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L111)

#### `fixed_size_selections` `[FUNCTION]` `[Internal]`

- **Signature**: `@cached_function(key=lambda source, selection_size, repetition: (id(source), int(selection_size), bool(repetition)))` `def fixed_size_selections(source, selection_size, *, repetition)`
- **Source**: [`src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L404`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L404)

#### `index_of_symbol` `[FUNCTION]` `[Internal]`

- **Signature**: `def index_of_symbol(elt, prefix: str, latex_prefix: str | None=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L44`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L44)

Return \(n\) when ``elt`` is the indexed symbol of this prefix.


#### `indexed_family` `[FUNCTION]` `[Internal]`

- **Signature**: `def indexed_family(index_set, value, *, name=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/indexed_families.py#L82`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/indexed_families.py#L82)

Return the family ``index |-> value(index)`` over ``index_set``.


#### `indexed_symbol` `[FUNCTION]` `[Internal]`

- **Signature**: `def indexed_symbol(prefix: str, index, latex_prefix: str)`
- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L34`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L34)

The symbol in \(\mathrm{SR}\) for this prefix and integer index.


#### `integer_from_natural` `[FUNCTION]` `[Internal]`

- **Signature**: `def integer_from_natural(n)`
- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L14`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L14)

The bijection \(\mathbb N\to\mathbb Z\) sending \(0,1,2,3,4,\ldots\) to \(0,1,-1,2,-2,\ldots\).


#### `multisets_of_size` `[FUNCTION]` `[Internal]`

- **Signature**: `def multisets_of_size(source, size)`
- **Source**: [`src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L417`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L417)

#### `natural_from_integer` `[FUNCTION]` `[Internal]`

- **Signature**: `def natural_from_integer(k)`
- **Source**: [`src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L24`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/enumerated/function_sets.py#L24)

The inverse of :func:`integer_from_natural`.


#### `omega` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def omega(index) -> Ordinal`
- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L778`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L778)

#### `ordered_enumerated_set` `[FUNCTION]` `[Internal]`

- **Signature**: `def ordered_enumerated_set(index_set, unrank, *, rank=None, contains=None, name=None)`
- **Source**: [`src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L334`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/finite_ordered_sets.py#L334)

Return the ordered image of ``index_set`` under the stated enumeration.


#### `ordered_subsets_of_size` `[FUNCTION]` `[Internal]`

- **Signature**: `def ordered_subsets_of_size(source, size)`
- **Source**: [`src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L413`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/fixed_size_selections.py#L413)

#### `ordinal` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ordinal(value) -> Ordinal`
- **Source**: [`src/dzack_research/preamble/categories/sets/cardinals.py#L774`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/cardinals.py#L774)

#### `placement_of` `[FUNCTION]` `[Internal]`

- **Signature**: `def placement_of(parent)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L1486`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L1486)

Return the strongest represented owned Set cardinality category for ``parent``.


#### `set_injection` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def set_injection(domain, codomain, function)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L280`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L280)

#### `set_surjection` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def set_surjection(domain, codomain, function)`
- **Source**: [`src/dzack_research/preamble/categories/sets/set_categories.py#L284`](file:///home/dzack/research/src/dzack_research/preamble/categories/sets/set_categories.py#L284)


---

<a id="subsystem-catalogue"></a>
## Named Catalogue & Classification Tables

> Named integral lattices (U, E8, LK3, Mukai, etc.), 2-elementary tables, Nikulin involutions, and Primitive embeddings.

### 📚 Catalogues & Named Tables

#### `Embeddings` `[CATALOGUE]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/catalogue.py#L900`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L900)
**Catalogue Entries / Constants:**
- `E8_2_into_TdP`: `NamedLattices.E8_2.Emb(NamedLattices.TdP)(tuple((_TDP_GENS[4 + index] + _TDP_...`
- `TCo_into_TEn`: `NamedLattices.Tco.Emb(NamedLattices.TEn)((_TEN_GENS[0] + _TEN_GENS[1], _TEN_G...`
- `TEn_into_TdP`: `NamedLattices.TEn.Emb(NamedLattices.TdP)((_TDP_GENS[0], _TDP_GENS[1], _TDP_GE...`
- `TdP_into_LK3`: `NamedLattices.TdP.Emb(NamedLattices.LK3)((_LK3_GENS[0], _LK3_GENS[1], _LK3_GE...`
- `TEn_into_LK3`: `TdP_into_LK3 * TEn_into_TdP`
- `U_E8_2_into_TEn`: `NamedLattices.U_E8_2.Emb(NamedLattices.TEn)((_TEN_GENS[0] + _TEN_GENS[2] + _T...`

#### `Involutions` `[CATALOGUE]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/catalogue.py#L871`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L871)

Named involutions of the K3 lattice in its displayed block framing.

**Catalogue Entries / Constants:**
- `I_dP`: `NamedLattices.LK3.Aut()((*(-generator for generator in _LK3_GENS[0:2]), *_LK3...`
- `I_En`: `NamedLattices.LK3.Aut()((*(-generator for generator in _LK3_GENS[0:2]), *_LK3...`
- `I_Nik`: `NamedLattices.LK3.Aut()((*_LK3_GENS[0:6], *(-generator for generator in _LK3_...`

#### `NamedLattices` `[CATALOGUE]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/catalogue.py#L65`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L65)
**Catalogue Entries / Constants:**
- `Zero`: `_C(0)`
- `Z`: `_C(1)`
- `Z_2`: `Z.twist(2)`
- `U`: `_U`
- `H`: `U`
- `U_2`: `U.twist(2)`
- `H_2`: `U_2`
- `E8`: `_E8`
- `E8_2`: `E8.twist(2)`
- `E10`: `U + E8`
- `E10_2`: `U_2 + E8_2`
- `Sdp`: `U_2`
- `SEn`: `E10_2`
- `Tco`: `_C(_block_gram(_rank_one_2, 2 * _Ug, 2 * _E8g), names='h,ep,fp,a1,a2,a3,a4,a5...`
- `Sco`: `_C(_block_gram(_rank_one_m2, 2 * _Ug, 2 * _E8g))`
- `TEn`: `_C(_block_gram(_Ug, 2 * _Ug, 2 * _E8g), names='e,f,ep,fp,a1,a2,a3,a4,a5,a6,a7...`
- `TdP`: `_C(_block_gram(_Ug, 2 * _Ug, _E8g, _E8g), names='e,f,ep,fp,a1,a2,a3,a4,a5,a6,...`
- `L_20_2_0`: `TdP`
- `LK3`: `_C(_block_gram(_Ug, _Ug, _Ug, _E8g, _E8g), names='e1,f1,e2,f2,e3,f3,a1,a2,a3,...`
- `LK3_2`: `_C(_block_gram(_rank_one_m2, _Ug, _Ug, _E8g, _E8g))`
- `LK3_4`: `_C(_block_gram(_rank_one_m4, _Ug, _Ug, _E8g, _E8g))`
- `LpNik`: `_C(_block_gram(_Ug, _Ug, _Ug, 2 * _E8g))`
- `LmNik`: `E8_2`
- `Mukai`: `_C(_block_gram(_Ug, _Ug, _Ug, _Ug, _E8g, _E8g))`
- `MukaiExtended`: `_C(_block_gram(_Ug, _Ug, _Ug, _Ug, _Ug, _E8g, _E8g))`
- `MukaiAbelian`: `_C(_block_gram(_Ug, _Ug, _Ug, _Ug))`
- `MukaiAbelianExtended`: `_C(_block_gram(_Ug, _Ug, _Ug, _Ug, _Ug))`
- `U_E8_2`: `U + E8_2`
- `BogachevKolpakovNonReflective`: `_C([[3, 7, 49], [7, 0, 0], [49, 0, 49]]).twist(-1)`
- `BogachevKolpakovWithoutRoots`: `_C([[0, 0, 49], [0, 49, 7], [49, 7, 3]]).twist(-1)`

### 🛠 Helper Functions & Constructors

#### `signature_orthogonal_sums` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def signature_orthogonal_sums(signature_pair, blocks)`
- **Source**: [`src/dzack_research/preamble/catalogue.py#L829`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L829)

Enumerate multisets of the supplied blocks with the target signature.


#### `two_elementary_orthogonal_sums` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def two_elementary_orthogonal_sums(signature_pair, a, delta)`
- **Source**: [`src/dzack_research/preamble/catalogue.py#L775`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L775)

Return block-orthogonal realizations of the stated 2-elementary invariants.


#### `validate_negative_def_two_elementary_table` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def validate_negative_def_two_elementary_table()`
- **Source**: [`src/dzack_research/preamble/catalogue.py#L708`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L708)

Validate the signature and discriminant invariants of every listed class.


#### `validate_two_elementary_table` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def validate_two_elementary_table()`
- **Source**: [`src/dzack_research/preamble/catalogue.py#L735`](file:///home/dzack/research/src/dzack_research/preamble/catalogue.py#L735)

Validate every row against its signature and Nikulin invariants.



---

<a id="subsystem-tensors"></a>
## Tensor Calculus

> Multilinear tensors, Tensor modules, Tensor shapes, and Tensor products.

### 📦 Mathematical Objects & Parents

#### `Tensor` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/tensors/tensor.py#L251`](file:///home/dzack/research/src/dzack_research/preamble/tensors/tensor.py#L251)

A tensor of type $(p,q)$.

A type-$(p,q)$ tensor on a module \(M\) is an element of
\(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  When the index modules
differ, it is an element of the corresponding mixed tensor product.
At infinite rank a type-$(0,2)$ pairing lives in
\((M\otimes M)^*\), not in \((M^*)^{\otimes 2}\).

This class carries no storage.  Every tensor, of every valence, is an
element of a :class:`TensorModule` over the owned base ring.


**Public Methods:**
- `change_ring(self, ring)`
  > Change coefficients without changing tensor variance.
- `components(self)`
  > Return the finite rectangular component array of this tensor.
- `contract(self, *vectors)`
  > Fully contract a purely covariant tensor with contravariant vectors.
- `dual_tensor(self)`
  > Dualize a nondegenerate pairing or copairing.
- `index_modules(self)`
  > Return the contravariant and covariant index modules.
- `is_equal_tensor(self, other) -> bool`
  > Return whether ``other`` is the same tensor mathematically.
- `is_symmetric(self) -> bool`
  > Return whether a square two-index tensor is symmetric in its slots.
- `list(self)`
  > Return flattened finite components in tensor-index order.
- `lower_ranks(self) -> tuple[int, ...]`
  > Return the dimensions of the covariant indices.
- `pullback(self, morphism)`
  > Pull this covariant tensor back along an owned linear morphism.
- `rows(self)`
  > Return component rows for a finite two-index tensor.
- `tensor_indices(self)`
  > Return the generating set of each index module.
- `tensor_order(self) -> int`
  > Return the number of indices.
- `tensor_shape(self) -> tuple[int, ...]`
  > Return the rank of each tensor index.
- `tensor_space(self)`
  > Return the module of which this tensor is an element.
- `tensor_type(self) -> tuple[int, int]`
  > Return $(p,q)$: $p$ contravariant indices and $q$ covariant indices.
- `tensor_valence(self) -> tuple[int, int]`
  > Return the type $(p,q)$; synonym of :meth:`tensor_type`.
- `upper_ranks(self) -> tuple[int, ...]`
  > Return the dimensions of the contravariant indices.

#### `TensorModule` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/tensors/tensor.py#L1101`](file:///home/dzack/research/src/dzack_research/preamble/tensors/tensor.py#L1101)
- **Bases**: `UniqueRepresentation`, `Parent`

The module of type-$(p,q)$ tensors with the given index ranks.

If every contravariant index is a copy of \(M=R^n\) and every covariant
index is a copy of \(M\), this is
\(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  A type-$(0,q)$ tensor
at infinite rank is an element of \((M^{\otimes q})^*\), not of
\((M^*)^{\otimes q}\).

EXAMPLES::

    sage: from dzack_research.preamble.tensors import tensor
    sage: G = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
    sage: G.parent()
    ((ZZ^2)*)^{⊗2}
    sage: G.tensor_type()
    (0, 2)
    sage: latex(G.parent())
    ((\mathbb{Z}^{2})^{*})^{\otimes 2}

- **Constructor**: `def __init__(self, base_ring: Parent, upper_ranks: tuple[int, ...], lower_ranks: tuple[int, ...]) -> None`
- **Constructor**: `def _element_constructor_(self, entries: tuple) -> _CoordinateTensor`

**Public Methods:**
- `construction(self)`
  > Return no functorial construction.
- `index_modules(self)`
  > Return the contravariant and covariant index modules \(R^{n_i}\).
- `lower_ranks(self) -> tuple`
- `tensor_indices(self)`
  > Return the standard generating set of each finite index module.
- `tensor_shape(self) -> tuple`
- `tensor_type(self) -> tuple[int, int]`
- `tensor_valence(self) -> tuple[int, int]`
- `upper_ranks(self) -> tuple`
- `zero(self) -> _CoordinateTensor`


---

<a id="subsystem-logic"></a>
## Logic & Predicates

> Three-valued logic predicates, queries, and certainty propagation.

### 📦 Mathematical Objects & Parents

#### `Predicate` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/logic.py#L14`](file:///home/dzack/research/src/dzack_research/preamble/logic.py#L14)
- **Bases**: `SageObject`

An unevaluated mathematical proposition.


### 🛠 Helper Functions & Constructors

#### `ask` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ask(statement, *, max_prec: int=4096)`
- **Source**: [`src/dzack_research/preamble/logic.py#L27`](file:///home/dzack/research/src/dzack_research/preamble/logic.py#L27)

Return the truth value of ``statement``, or ``Unknown`` if undecided.

``True`` and ``False`` pass through unchanged.  Predicates own their
evaluation algorithms.  ``Unknown`` also passes through, so callers can
compose this with existing Sage three-valued predicates.



---

<a id="subsystem-geometry-specialized"></a>
## Specialized Geometries (Coble & Sterk)

> Coble surfaces, Sterk invariant theory, and Automorphic forms.

### 📦 Mathematical Objects & Parents

#### `Coble` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/coble.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/coble.py#L11)

**Public Methods:**
- `@staticmethod` `isotropic_vectors()`
- `@staticmethod` `isotropic_vectors_in_TEn()`
- `@staticmethod` `isotropic_vectors_in_TdP()`
- `@staticmethod` `rank_ten_coxeter_roots()`
- `@staticmethod` `rank_ten_diagram()`

#### `Sterk` `[OBJECT]` `[Exported Session]`

- **Source**: [`src/dzack_research/preamble/sterk.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/sterk.py#L87)

**Public Methods:**
- `@staticmethod` `diagram_layouts()`
  > Return copies of the optional exact presentation coordinates.
- `@staticmethod` `diagrams()`
- `@staticmethod` `isotropic_vectors()`
- `@staticmethod` `roots_18_0_0()`
- `@staticmethod` `roots_18_2_0()`
- `@staticmethod` `selected_isotropic_vectors()`
- `@staticmethod` `sterk5_in_U_E8_2()`
  > Return Sterk 5's fourteen roots in ``U + E8(2)`` coordinates.
- `@staticmethod` `sterk_roots()`
- `@staticmethod` `sterks_in_TEn()`
  > Return the alternative Sterk 1--3 roots in ``TEn`` coordinates.


---

<a id="subsystem-preamble-root"></a>
## Preamble Entrypoints & Utilities

> Top-level session loaders, environment initializers, and refinement helpers.

### 🛠 Helper Functions & Constructors

#### `lmap` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def lmap(function: Callable[[T], U], values: Iterable[T]) -> list[U]`
- **Source**: [`src/dzack_research/preamble/utilities.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/utilities.py#L11)

#### `load` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def load(filename: str, globals: dict | None=None, attach: bool=False) -> None`
- **Source**: [`src/dzack_research/preamble/all.py#L841`](file:///home/dzack/research/src/dzack_research/preamble/all.py#L841)

Load a Sage file and restore this session's owned scalar vocabulary.


#### `lzip` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def lzip(*iterables: Iterable[T]) -> list[tuple[T, ...]]`
- **Source**: [`src/dzack_research/preamble/utilities.py#L15`](file:///home/dzack/research/src/dzack_research/preamble/utilities.py#L15)

#### `refine` `[FUNCTION]` `[Internal]`

- **Signature**: `def refine(obj: SageObject, category: Category | Iterable[Category])`
- **Source**: [`src/dzack_research/preamble/refine.py#L99`](file:///home/dzack/research/src/dzack_research/preamble/refine.py#L99)

Join ``category`` into ``obj`` and give owned methods precedence.


#### `to_var_names` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def to_var_names(names: str) -> list[str]`
- **Source**: [`src/dzack_research/preamble/utilities.py#L19`](file:///home/dzack/research/src/dzack_research/preamble/utilities.py#L19)

#### `zipsum` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def zipsum(coefficients: Iterable[C], elements: Iterable[G], zero: T, *, term: Callable[[C, G], T] | None=None) -> T`
- **Source**: [`src/dzack_research/preamble/utilities.py#L23`](file:///home/dzack/research/src/dzack_research/preamble/utilities.py#L23)

Return the sum of pairwise terms from two equally sized iterables.



---

<a id="subsystem-language-runtime"></a>
## Language Runtime

> Constructions defined in subsystem language_runtime.

### 🛠 Helper Functions & Constructors

#### `ComplexNumber` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ComplexNumber(real, imag=None)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L30`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L30)

#### `ConditionSet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ConditionSet(domain, predicate)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L87`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L87)

#### `ImageSet` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ImageSet(function, domain)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L81`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L81)

#### `Integer` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Integer(value=0)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L11`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L11)

#### `RealApproximation` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def RealApproximation(value)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L24`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L24)

#### `RealNumber` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def RealNumber(value)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L18`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L18)

#### `Set` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def Set(iterable)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L75`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L75)

#### `ellipsis_iter` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ellipsis_iter(*args)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L107`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L107)

#### `ellipsis_range` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def ellipsis_range(*args)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L100`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L100)

#### `factorial` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def factorial(value)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L93`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L93)

#### `install` `[FUNCTION]` `[Internal]`

- **Signature**: `def install() -> None`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L145`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L145)

#### `matrix` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def matrix(rows)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L43`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L43)

Construct the owned matrix-Hom represented by a rectangular row family.


#### `symbolic_expression` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def symbolic_expression(*_args, **_kwargs)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L117`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L117)

#### `var` `[FUNCTION]` `[Exported Session]`

- **Signature**: `def var(*_args, **_kwargs)`
- **Source**: [`src/dzack_research/preamble/language_runtime.py#L111`](file:///home/dzack/research/src/dzack_research/preamble/language_runtime.py#L111)


---
