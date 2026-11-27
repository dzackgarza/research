# cat subtree

This subtree owns the category of categories, written `Cat()`.

Rules:

- `Cat()` is intentionally barebones. Do not build a deep subcategory hierarchy here.
- `Cat()` is the ambient category of 1-categories at this spec level. It is not an
  object of itself. Do not make `Cat` inherit from the Cat-backed wrappers, and do not
  assert `Cat() in Cat()` or `Cat().Hom(Cat())`.
- Every project category and subcategory below this root is an object of `Cat()`.
- Every project category class must inherit from the registered re-exported bases in
  `category_specs.cat` (`Category`, `Category_singleton`, `CategoryWithAxiom`,
  `Homsets`, `HomsetsCategory`, etc.), not directly from `sage.categories.*`.
- `base_category_types.py` is the only Sage category-base touch point. It explicitly
  lists Sage base category classes the tree subclasses. Do not add arbitrary Sage
  category objects there merely because a spec names them as supercategories.
- If a Sage category base has no registered re-export here, add that re-export in
  `cat/base_category_types.py` first; do not use the raw Sage base as a superclass in
  another subtree.
- Prefer the smallest wrapper that makes Sage do its usual work: inherit the wrapped
  Sage base, register the category object with `Cat()` at the wrapper boundary, and let
  Sage resolve `_with_axiom`, subcategory methods, and method providers. Do not add
  helper registries, classcall indirection, post-hoc splicing, or fallback logic unless
  the local comments prove why that simpler design cannot work.
- Extensive class manipulation in this subtree is a design smell, not an implementation
  achievement. If Cat or a wrapped base needs generated classes, source-shape
  registries, class mutation, or custom mixin routing to make ordinary category
  behavior work, first assume the wrapper is not using Sage's category base correctly.
- `Cat` uniformizes category-object constructions below the root. If every ordinary
  category object should expose an operation, define the object-level method on
  `Cat.ParentMethods` only when it is really a method of an object `C in Cat()`.
  Category-level construction methods on `Cat()` itself belong in `Cat.SubcategoryMethods`.
- `Cat().join(...)` and `Cat().meet(...)` are thin category-order entry points over
  Sage's `Category.join` and `Category.meet`. The empty meet is the local bottom
  category exposed as `Cat().Constructors().EmptyCategory()`.
- Keep `EmptyCategory` separate from join-category logic. The constructor namespace owns
  it as an inline `Cat.Constructors.EmptyCategory` method delegating to
  `empty_category.py`; `join_categories.py` owns only the Sage `JoinCategory`
  predicate/subcategory surface.
- Maintain the required subtree documentation before extending code:
  - `docs/SAGE_INVENTORY.md` records Sage classes, methods, signatures, and source paths.
  - `docs/MAPPING.md` records the mathematical mapping from Sage's category/functor
    machinery to the project surface.
  - Current blockers, validation scope, and deferred uniformization work belong in
    Nimbalyst tracker items, not subtree-local triage documents.
- Category-object method rules live here first. Other subtrees should eventually reuse
  the `Cat.ParentMethods` surface instead of hand-writing duplicate category-object
  operations.
- Category objects expose private hooks for containment:
  - `_sage_super_categories()`
  - `_sage_object_classes()`
  - `_sage_morphism_classes()`
- For any ordinary category `C`, `X in C` can mean object membership or morphism
  membership according to that category's own containment semantics. For `C = Cat()`,
  membership is category-object membership at this level; functors live in `A.Hom(B)`
  for category objects `A, B in Cat()`. Endofunctors live in `A.Hom(A)`.
- `leq` and `geq` are readable shorthands for Sage's subcategory relation between
  ordinary category objects. Do not re-export those aliases on `Cat()` itself:
  this spec does not place the root infinity-category object inside a larger modeled
  category order.
- Distinguish object-level and category-level Hom notation:
  - If `A, B in Cat()`, then `A.Hom(B)` is the object-level homspace of functors
    from `A` to `B`.
  - `Cat().HomCategory()` is the category-level construction whose objects are
    functor categories `A.Hom(B)` as `A, B` range over objects of `Cat()`.
  - `C.Hom()` does not exist as a category-level selector. Use `C.HomCategory()`.
  For wrapped ordinary categories, `base_category_types._CatObjectMixin.Hom`
  delegates `C.Hom(D)` to Sage's parent Hom implementation for the object-level
  functor category.
- Standard construction selectors (`Subobjects`, `Quotients`, `Subquotients`,
  `ObjectsOver`, `ObjectsUnder`, `CartesianProducts`, `HomCategory`, `EndCategory`,
  `AutCategory`) are defined once in
  `universal_subcategory_methods.py` and mixed into ordinary category
  `SubcategoryMethods` by the wrapped base-category layer. Do not duplicate them in
  lower subtrees unless a category has a genuinely more specific mathematical
  construction to expose.
- Follow the hom-category organization pattern inside this subtree too:
  `cat/homsets.py`, `cat/endsets.py`, and `cat/autsets.py` are separate files. Do not
  fold end/aut category classes into `cat/homsets.py`.
- In the `Cat` hom layer, `AutCategory` is based on `CatEndCategory`, not directly on
  `CatHomCategory`. Audits should ask whether a functor aut category is being treated
  as a direct hom-category axiom; if so, the construction has likely been classified at
  the wrong layer.
- Sage functors and Sage construction functors are morphism-like objects in this
  subtree. Sage `ConstructionFunctor` methods such as `pushout`, `merge`, `commutes`,
  `expand`, and `common_base` belong to actual functors from
  `sage.categories.pushout`, not to Sage `FunctorialConstructionCategory` category
  objects such as `C.Subobjects()`. Keep this distinction explicit before adding
  wrappers elsewhere.
- `Constructors` classes are plain opt-in constructor collectors, not category objects
  or construction categories. They advertise named constructors for the category
  surface that owns them. An explicit nested `Constructors` class is the declaration;
  do not add a separate public registration method or construction category.
- `Cat().Constructors()` owns `EmptyCategory()` as the bottom category entry point and
  owns constructor collection. The Cat backend collects methods from explicit
  `C.Constructors` classes under deterministic prefixed names such as `C_x_y_z`,
  without moving constructor ownership to `Cat` or exposing `Aggregate()`/
  `AggregateFor(...)`. Generic constructor names must not repeat the category noun:
  use `C.Constructors().from_xyz(...)`, so Cat exposes `cat_prefix_from_xyz(...)`,
  rather than `C.Constructors().category_from_xyz(...)`.
- Prefer top-level category constructor collectors in this spec. This is a documented
  placement convention, not a runtime law enforced with assertion guards.
- Nontrivial algorithms belong under `implementations/`; trivial Sage wiring stays
  on the category surface.
