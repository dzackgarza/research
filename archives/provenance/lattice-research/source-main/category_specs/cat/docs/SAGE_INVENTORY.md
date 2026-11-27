# Cat Sage Inventory

This inventory grounds the `cat/` subtree in Sage's installed category, functor,
homset, and functorial-construction machinery. It surveys low-level framework
classes, not the full list of mathematical categories.

Installed Sage source root:

`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/`

## Category Base Classes

### `sage.categories.category.Category`

Source: `category.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 131 | `class Category` | Base class for Sage mathematical categories. |
| 643 | `_subcategory_hook_(self, category)` | Fast path for subcategory checks. |
| 687 | `__contains__(self, x)` | Sage membership checks `x.category().is_subcategory(self)`. |
| 1492 | `_make_named_class(...)` | Builds dynamic parent/element/morphism classes from nested method providers. |
| 1664 | `parent_class(self)` | Exposes `ParentMethods` inheritance for objects in a category. |
| 1714 | `element_class(self)` | Exposes `ElementMethods` inheritance for elements. |
| 1765 | `morphism_class(self)` | Exposes `MorphismMethods` inheritance for morphisms. |
| 1788 | `required_methods(self)` | Reports required and optional abstract parent/element methods. |
| 1803 | `is_subcategory(self, c)` | Sage's category-order predicate. |
| 2089 | `_with_axiom(self, axiom)` | Constructs axiom subcategories. |
| 2332 | `join(categories, ...)` | Join/intersection operation in the category lattice. |
| 2504 | `meet(categories)` | Greatest lower bound operation; installed Sage raises on the empty input. |
| 2536 | `category(self)` | Installed Sage places category objects in `Objects()`. |

### `sage.categories.category.CategoryWithParameters`

Source: `category.py`, line 2717.

Relevant methods: `_make_named_class`, `_make_named_class_key`, `_cmp_key`,
`_subcategory_hook_`.

Use: base for parameterized category classes whose generated classes depend on
parameters such as base rings.

### `sage.categories.category.JoinCategory`

Source: `category.py`, line 3004.

Relevant methods: `super_categories`, `additional_structure`, `_subcategory_hook_`,
`is_subcategory`, `_with_axiom`, `_without_axiom`, `_repr_object_names`, `_repr_`.

Use: Sage's category lattice join object.

### `sage.categories.category_singleton.Category_singleton`

Source: `category_singleton.py`.

Relevant methods: `__classcall__`, `__contains__`.

Use: singleton base for categories such as `Cat()`, `Sets()`, and `Rings()`.

### `sage.categories.category_with_axiom`

Relevant classes:

| Class | Source line | Relevant methods |
| --- | --- | --- |
| `CategoryWithAxiom` | 1861 | `_base_category_class_and_axiom`, `_axiom`, `__classcall__`, `__classget__`, `extra_super_categories`, `super_categories`, `base_category`, `axioms` |
| `CategoryWithAxiom_over_base_ring` | 2504 | Base-ring axiom category class. |
| `CategoryWithAxiom_singleton` | 2528 | Singleton axiom category class. |

Use: axiom restrictions such as `Finite`, `Endset`, and base-ring variants.

### `sage.categories.category_types`

Relevant classes:

| Class | Source line | Relevant methods |
| --- | --- | --- |
| `Category_over_base` | 148 | `base`, `_make_named_class_key`, `_repr_object_names`, `_latex_` |
| `Category_over_base_ring` | 348 | `base_ring`, `_subcategory_hook_`, `__contains__` |
| `Category_module` | 578 | Module-category base marker. |
| `Category_ideal` | 582 | `an_instance`, `ring`, `__contains__`, `__call__` |

Use: base-object and base-ring category families.

## Category-Object Runtime Facts

Installed Sage category instances such as `Sets()`, `Rings()`, and `Modules(ZZ)`
report `category() == Objects()`. Sage gives category-object navigation such as
`Homsets()` and `Endsets()` through generated category classes, not by making
category objects ordinary parents of a separate `Cat` category.

## Functors

### `sage.categories.functor.Functor`

Source: `functor.pyx`.

Relevant methods:

| Method | Cat use |
| --- | --- |
| `__init__(self, domain, codomain)` | Domain and codomain are Sage `Category` instances. |
| `_apply_functor(self, x)` | Object-level functor action. |
| `_apply_functor_to_morphism(self, f)` | Morphism-level functor action. |
| `_coerce_into_domain(self, x)` | Domain membership/coercion hook. |
| `__call__(self, x)` | Dispatches to object or morphism action and checks codomain. |
| `domain(self)` | Source category. |
| `codomain(self)` | Target category. |

Installed subclasses and constructors:

| Class or constructor | Cat use |
| --- | --- |
| `ForgetfulFunctor_generic` | Concrete forgetful functors. |
| `IdentityFunctor_generic` | Identity functors. |
| `IdentityFunctor(C)` | Public identity-functor constructor. |
| `ForgetfulFunctor(domain, codomain)` | Public forgetful-functor constructor for subcategory relations. |

### `sage.categories.pushout.ConstructionFunctor`

Source: `pushout.py`, line 45.

Relevant methods: `__mul__`, `pushout`, `__eq__`, `__hash__`, `_repr_`, `merge`,
`commutes`, `expand`, `common_base`, `_raise_common_base_exception_`, and the
`coercion_reversed` flag.

Runtime fact: `ConstructionFunctor` subclasses Sage `Functor`. It is a functor-like
morphism object with domain/codomain/action semantics.

### `sage.categories.pushout.CompositeConstructionFunctor`

Source: `pushout.py`, line 419.

Relevant methods: `_apply_functor_to_morphism`, `_apply_functor`, `__eq__`,
`__hash__`, `__mul__`, `_repr_`, and `expand`.

## Functorial Construction Categories

### `sage.categories.covariant_functorial_construction.FunctorialConstructionCategory`

Source: `covariant_functorial_construction.py`, line 231.

Relevant methods: `_base_category_class`, `__classcall__`, `__classget__`,
`category_of`, `base_category`, `extra_super_categories`, `super_categories`,
`_repr_object_names`, and `_latex_`.

### `CovariantConstructionCategory`

Source: `covariant_functorial_construction.py`, line 516.

Relevant methods: `default_super_categories`, `is_construction_defined_by_base`,
and `additional_structure`.

### `RegressiveCovariantConstructionCategory`

Source: `covariant_functorial_construction.py`, line 662.

Relevant method: `default_super_categories`.

## Standard Construction Categories

| Sage class | Source | Relevant surface |
| --- | --- | --- |
| `SubobjectsCategory` | `subobjects.py:20` | Base for `C.Subobjects()`; default supers join `C.Subquotients()`. |
| `QuotientsCategory` | `quotients.py:20` | Base for `C.Quotients()`; default supers join `C.Subquotients()`. |
| `SubquotientsCategory` | `subquotients.py:19` | Base for `C.Subquotients()`. |
| `CartesianProductsCategory` | `cartesian_product.py:226` | Base for `C.CartesianProducts()`; includes product repr and idempotence. |

## Homsets And Endsets

### `sage.categories.homsets.HomsetsCategory`

Source: `homsets.py`, line 19.

Relevant methods:

| Line | Method | Cat use |
| --- | --- | --- |
| 24 | `default_super_categories(cls, category)` | Computes homset-category supers; falls back to `HomsetsOf`. |
| 123 | `_test_homsets_category(self, **options)` | Generic homsets-category test. |
| 141 | `base(self)` | Finds a base object for based hom categories. |
| 158 | `_make_named_class_key(self, name)` | Keys generated classes by the base category's corresponding class. |

### `sage.categories.homsets.HomsetsOf`

Source: `homsets.py`, line 175.

Relevant methods: `_repr_object_names`, `super_categories`.

Use: Sage's fallback category for homsets of a category that does not define its own
homset category.

### `sage.categories.homsets.Homsets`

Source: `homsets.py`, line 239.

Relevant surface:

- `super_categories()` returns `[Sets()]`.
- `SubcategoryMethods.Endset()` returns the `Endset` axiom.
- nested `Endset` begins at line 299 and adds monoid structure.
- `Homsets.ParentMethods.is_endomorphism_set()` tests whether a homset has equal
  domain and codomain.

### `sage.categories.homset`

Relevant surface:

| Line | Item | Cat use |
| --- | --- | --- |
| 498 | `End(X, category=None)` | Public endomorphism-set constructor. |
| 580 | `class Homset` | Parent class for morphism collections. |
| 611 | `Homset.__init__(X, Y, category=None, base=None, check=True)` | Stores domain/codomain and assigns `category.Endsets()` when `X is Y`. |
| 1316 | `is_Endset(x)` | Deprecated; use `isinstance(..., Homset)` plus `is_endomorphism_set()`. |

## Autsets

- Searched: installed `sage/categories/homsets.py`, installed
  `sage/categories/homset.py`, official Sage documentation pages for category and
  homset machinery, and local `category_specs/homsets/__init__.py`.
- Found: Sage provides `HomsetsCategory`, `HomsetsOf`, `Homsets`, `Homsets.Endset`,
  `Hom(...)`, `End(...)`, and `Homset`. I found no installed generic Sage `Autset`
  category class.
- Conclusion: inference -- the searched Sage installation has generic homset and
  endset categories, but no generic `Autset` category class.
- Confidence: High.
- Gaps: I did not search Sage's full git history or third-party Sage extensions.

## Local Cat Files

| File | Purpose |
| --- | --- |
| `cat/__init__.py` | Declares `Cat()`, category-object methods, and Cat-specific construction navigation. |
| `cat/base_category_types.py` | Re-exports wrapped Sage category bases and injects universal subcategory methods into wrapped categories. |
| `cat/universal_subcategory_methods.py` | Defines the shared literal `SubcategoryMethods` construction selectors for category objects. |
| `cat/empty_category.py` | Declares the bottom category object, separate from join-category logic. |
| `cat/join_categories.py` | Declares the Sage `JoinCategory` containment predicate and subcategory. |
| `cat/homsets.py` | Declares the `Cat().HomCategory()` refinement and functor method surfaces. |
| `cat/endsets.py` | Declares the `Cat().EndCategory()` refinement. |
| `cat/autsets.py` | Declares the `Cat().AutCategory()` refinement. |
| `cat/subcategories/constructions/subobjects.py` | Category-level subobjects: subcategories. |
| `cat/subcategories/constructions/quotients.py` | Category-level quotients. |
| `cat/subcategories/constructions/subquotients.py` | Category-level subquotients. |
| `cat/subcategories/constructions/objects_over.py` | Slice categories: categories equipped with a functor to a fixed category. |
| `cat/subcategories/constructions/objects_under.py` | Coslice categories: categories equipped with a functor from a fixed category. |
| `cat/subcategories/constructions/cartesian_products.py` | Product categories. |
