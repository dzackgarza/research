# Category Spec Subtree Ownership

This reference replaces the deleted nested `category_specs/**/AGENTS.md` files. It records durable local ownership rules without forcing every agent to load every subtree note.

## Global category-spec entry

Agents working under `category_specs/` must obey the root repo `AGENTS.md` and `category_specs/AGENTS.md`. Load `category-spec-style` before touching specs, method surfaces, constructors, morphisms, Hom/End/Aut surfaces, Sage wrappers, type annotations, test files, category-obligation examples, implementations, Sage inventory, or mapping documents. Load `category-spec-workflow` before changing tracking, status, plans, delegation, PR metadata, validation handoff, failed-assertion classification, or stale-document migration.

## Cat

`cat/` owns the category of categories, written `Cat()`.

Rules:

- `Cat()` is intentionally barebones. Do not build a deep subcategory hierarchy here.
- `Cat()` is the ambient category of 1-categories at this spec level. It is not an object of itself. Do not make `Cat` inherit from Cat-backed wrappers, and do not assert `Cat() in Cat()` or `Cat().Hom(Cat())`.
- Every project category and subcategory below this root is an object of `Cat()`.
- Every project category class must inherit from registered re-exported bases in `category_specs.cat`, not directly from `sage.categories.*`.
- `base_category_types.py` is the only Sage category-base touch point. If a Sage category base has no registered re-export, add that re-export in `cat/base_category_types.py` first.
- Prefer the smallest wrapper that lets Sage do its usual work: inherit the wrapped Sage base, register the category object with `Cat()` at the wrapper boundary, and let Sage resolve `_with_axiom`, subcategory methods, and method providers.
- Extensive class manipulation is a design smell. Do not add helper registries, classcall indirection, post-hoc splicing, fallback logic, source-shape registries, class mutation, or custom mixin routing unless local comments prove why the simpler Sage wrapper cannot work.
- `Cat` uniformizes category-object constructions below the root. Object-level methods shared by ordinary category objects belong on `Cat.ParentMethods` only when they are really methods of an object `C in Cat()`.
- Category-level construction methods on `Cat()` itself belong in `Cat.SubcategoryMethods`.
- `Cat().join(...)` and `Cat().meet(...)` are thin category-order entry points over Sage's `Category.join` and `Category.meet`. The empty meet is the local bottom category exposed as `Cat().Constructors().EmptyCategory()`.
- Keep `EmptyCategory` separate from join-category logic. The constructor namespace owns it; `join_categories.py` owns only the Sage `JoinCategory` predicate/subcategory surface.
- Category-object method rules live here first. Other subtrees should reuse `Cat.ParentMethods` instead of duplicating category-object operations.
- Category objects expose private hooks for containment: `_sage_super_categories()`, `_sage_object_classes()`, and `_sage_morphism_classes()`.
- For `C = Cat()`, membership is category-object membership at this level; functors live in `A.Hom(B)` for category objects `A, B in Cat()`. Endofunctors live in `A.Hom(A)`.
- `leq` and `geq` are readable shorthands for Sage's subcategory relation between ordinary category objects. Do not re-export those aliases on `Cat()` itself.
- If `A, B in Cat()`, then `A.Hom(B)` is the object-level homspace of functors from `A` to `B`. `Cat().HomCategory()` is the category-level construction whose objects are functor categories `A.Hom(B)`.
- Standard construction selectors (`Subobjects`, `Quotients`, `Subquotients`, `ObjectsOver`, `ObjectsUnder`, `CartesianProducts`, `HomCategory`, `EndCategory`, `AutCategory`) are defined once in `universal_subcategory_methods.py` and mixed into ordinary category `SubcategoryMethods` by the wrapped base-category layer.
- `cat/homsets.py`, `cat/endsets.py`, and `cat/autsets.py` are separate files. Do not fold end/aut category classes into `cat/homsets.py`.
- In the `Cat` hom layer, `AutCategory` is based on `CatEndCategory`, not directly on `CatHomCategory`.
- Sage functors and Sage construction functors are morphism-like objects here. Sage `ConstructionFunctor` methods such as `pushout`, `merge`, `commutes`, `expand`, and `common_base` belong to actual functors from `sage.categories.pushout`, not to Sage `FunctorialConstructionCategory` category objects.
- `Constructors` classes are plain opt-in constructor collectors, not category objects or construction categories. They advertise named constructors for the category surface that owns them. Do not add a separate public registration method or construction category.
- `Cat().Constructors()` owns `EmptyCategory()` and constructor collection. Generic constructor names must not repeat the category noun.
- Nontrivial algorithms belong under `implementations/`; trivial Sage wiring stays on the category surface.

`cat/implementations/` is intentionally empty unless a nontrivial algorithm is needed.

Cat tests:

- `cat/tests/new_spec/`: new `Cat()` category surface.
- `cat/tests/regression/`: Sage category/functor behavior regression.
- `cat/tests/sage_gaps/`: raw Sage category or functor gaps without `category_specs`.

## Homsets, endsets, and autsets

`homsets/` owns the generic hom, end, and aut category specs.

Rules:

- Extend Sage's `HomsetsCategory`, `Homsets`, and `Homsets.Endset` through registered re-exports in `category_specs.cat`; do not inherit raw Sage category bases directly or create a parallel model.
- If a hom/end/aut failure suggests new local plumbing, first ask whether the object is using raw Sage construction or the wrong base category.
- Domain, codomain, call, identity, composition, inverse, and invertibility are universal morphism/hom-category concerns. Put them in generic `homsets.py`, `endsets.py`, or `autsets.py`, not lower subtrees.
- Subtree hom-category specs own only structure that first appears there: set maps, linear maps, ring maps, continuous maps, etc.
- Do not let set, module, ring, or algebra hom-category specs own bare facts that `End(X)` is a monoid or `Aut(X)` is a group. Specialized subtrees may add extra structure, such as `End_R(M)` as an `R`-algebra.
- Keep root spec categories separate: `homsets.py` owns `HomCategory`, `endsets.py` owns `EndCategory`, and `autsets.py` owns `AutCategory`.
- Use `C.HomCategory().Of(A, B)`, `C.EndCategory().Of(A)`, and `C.AutCategory().Of(A)`.
- `HomCategoryOf`, `EndCategoryOf`, and `AutCategoryOf` are construction classes that set supercategories so Sage mixes in root specs.
- Generic method surfaces are public universal classes: `UniversalHomObjectMethods`, `UniversalHomElementMethods`, `UniversalEndObjectMethods`, `UniversalEndElementMethods`, `UniversalAutObjectMethods`, and `UniversalAutElementMethods`.
- Keep generic `Aut(X)` construction here. Subtrees must not recreate `ConditionSet`-based aut wiring.
- Sage still names axiom hooks `Endset` and `Autset`; concrete classes may attach them only for `_with_axiom(...)` interop. Do not expose project-facing `Homsets()`, `Endsets()`, or `Autsets()` selectors.
- A hom object has a domain and codomain. `End_C(A)` is `Hom_C(A, A)`. `Aut_C(A)` is the invertible part of `End_C(A)`.
- Element surfaces distinguish morphisms, endomorphisms, and automorphisms.

Hom-category tests verify the generic hom/end/aut surface only. Category-specific morphism laws belong in the corresponding subtree tests.

## Sets

`sets/` maps Sage set methods into mathematical category specs on specific subcategories.

Tasks:

- Ensure all named sets have specific one-object or parameterized subcategories when appropriate.
- Expose named Sage set constructors through `Sets().Constructors()`.
- Spot-check runtime methods on constructible set objects and represent mathematically meaningful set-specific methods in the spec or mark them inventory-only in `docs/MAPPING.md`.
- Do not add Sage fallback/cache helpers or enumeration convenience names as project abstract methods when standard iteration, indexing, rank, cardinality, or Python conversion protocols recover the behavior.
- Ring-theoretic methods do not go here. Only methods depending on the underlying set belong here.
- Ensure set axioms are composable and mathematically meaningful.

Set tests must use `Sets().Constructors()`. `sets/tests/new_spec/` specifies local set surfaces; `sets/tests/regression/` covers admitted constructors; `sets/tests/sage_gaps/` records genuine Sage gaps.

## Topological spaces

`topological_spaces/` owns topological-space and metric-space method surfaces.

Rules:

- A topological space is a set equipped with a topology. `Sets().Topological()` is the category of topological spaces, not a set-local implementation detail.
- `Sets().Metric()` is the metric-space subcategory.
- Keep topological and metric method surfaces here.
- Let set, real-set, ring, module, and algebra categories refer here when objects carry topology.
- Keep constructors separate from subcategories. Add concrete constructors only after Sage topological-space constructor inventory.

Topological-space tests should use named set constructors such as `Sets().Constructors().RealLine()` or `Sets().Constructors().OpenRealInterval(...)` when the object is a named set that refines into `TopologicalSpaces()`. Use `TopologicalSpaces().Constructors()` only when the primary output is a topological space.

## Rings

`rings/` records Sage ring methods as ABC specs on specific subcategories.

Tasks:

- Ensure all named rings have specific one-object or parameterized subcategories, such as `Rings.ZZ()` or `Rings.Zp()`.
- Expose named Sage ring constructors through `Rings().Constructors()` for `PolynomialRing`, `MatrixRing`, `ZZ`, `Zp`, `QQ`, `Qp`, `QQbar`, `RR`, `CC`, and related constructors.
- Spot-check runtime methods on ring objects and represent ring-specific methods as abstract methods in the appropriate subcategory.
- Check upstream concrete ring implementations and ring-specific Sage subcategories for methods/properties that belong in the hierarchy.

Ring tests must use `Rings().Constructors()`. `NamedRings()` is not part of the forward spec surface.

## Modules

`modules/` records Sage module methods as ABC specs on specific subcategories.

Tasks:

- Ensure all named module constructors appear as methods on `Modules(R).Constructors()`.
- Map known Sage module types to specific subcategories that spec their object,
  element, and Hom-category element method surfaces.
- Include constructions regarding rings as rank-one free modules, fractional ideals as submodules, invertible ideals as projective submodules, polynomial rings as modules, power series rings, matrix rings, and related constructions.
- Collect Sage constructions here by calling existing Sage constructors and refining the result category.
- Interoperate explicitly with the new Rings subcategories without bypassing native Sage categories.
- Spot-check runtime methods on constructible module objects and represent module-specific methods in the spec.
- Check upstream concrete ring implementations for module-related methods and downstream classes such as lattices.
- Ensure refined syntax sugar such as `ZZ^n` lands in the refined free module category when `ZZ` is refined.

Module tests must use `Modules(R).Constructors()`. `NamedModules()` is not part of the forward spec surface.

## Forms and lattices

`forms/` owns categories for modules equipped with forms.

Rules:

- `FormedModules(R)` is the named owner for `Modules(R).WithForms()`.
- Keep generic formed-module structure here: `WithForms`, `Bilinear`, `Quadratic`, symmetry, alternating, nondegeneracy, definiteness, integrality, rationality, and free bilinear modules.
- Modules may route or re-export these categories, but they do not own the form method surface.
- Lattices own only the lattice endpoint and lattice-specific refinements.
- Tensor algebra components own tensor objects. Scalar-valued bilinear forms may be constructed as `(0,2)` tensors there and then interpreted through this subtree.

`lattices/` specifies module lattices: finite-rank modules equipped with bilinear forms and their lattice-theoretic refinements. It is unrelated to order-theoretic lattices in `posets/`.

Lattice rules:

- Keep generic form evaluation in `modules/`; lattice files only refine lattice-theoretic vocabulary.
- Preserve mathematical nouns in public names: `Lattice`, `LatticeMorphism`, `LatticeHomCategory`, `DiscriminantGroup`, `Overlattice`, and `DualLattice`.
- Every subcategory file must expose explicit `ParentMethods` and `ElementMethods`
  classes when those surfaces apply. Morphism behavior belongs on Hom-category
  `ElementMethods`, usually in `homsets.py` or a nested `HomCategory` refinement.
- Hom, end, and aut refinements live in `homsets.py` and use `HomCategory`, `EndCategory`, and `AutCategory` vocabulary.
- Construction categories live under `subcategories/constructions/`.
- Concrete constructors are admitted only through `Lattices(R).Constructors()` after Sage constructor inventory has been mapped.

## Algebras

`algebras/` records algebra-specific method surfaces as ABC specs on subcategories of `Algebras(R)`.

Rules:

- Define `Algebras(R)` as the category of `R`-algebras in the local spec.
- Keep algebra-specific parent methods here: `subalgebra`, `center`, `radical`, `derivations_basis`, `hochschild_complex`, and related structure maps.
- Ring constructions that are naturally `R`-algebras refine into this subtree rather than defining algebra surface ad hoc.
- Specialized ring/algebra categories inherit from this subtree plus their ring/module surfaces instead of redeclaring inherited methods.

Algebra tests must use `Algebras(R).Constructors()` once concrete algebra constructors are admitted.

## Tensor algebra components

`tensor_algebra_components/` owns tensor-algebra component modules and tensor elements.

Rules:

- Objects are graded pieces `T_R(M)[p,q]` for finite-rank free modules `M`; elements are tensors in those parents.
- Parent categories are `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()`.
- Keep Sage inventory and mapping before adding new spec surface.
- Do not model all tensor calculus here. Add only methods needed to identify tensor component modules, tensor elements, and tensor type.
- Do not make `TensorAlgebraComponents` a Sage axiom.
- Constructor methods may accept interop component shapes such as nested lists and lists of matrices, but they return tensor elements. The component module is recoverable as `tensor.parent()`.
- Interop component shapes are interpreted through the base module's preferred generating set. Do not expose a separate `basis` argument and never forward basis/table/list/matrix shapes into algebra constructors.
- Use standard Sage tensor type order: `(p,q)` means `p` contravariant and `q` covariant slots. `tensor_type()` is the only public tuple-valued type method.
- `DualObjects()` stays here: `T_R(M)[p,q]^* = T_R(M)[q,p]`.
- `from_matrix` is the scalar-valued bilinear-form constructor and returns a `(0,2)` tensor. `from_module_element_matrix` is the multiplication-table constructor and returns a `(1,2)` tensor for `M \otimes_R M -> M`.

## Posets

`posets/` specifies order-theoretic categories promoted out of `sets/`.

Rules:

- A lattice here is a poset in which every pair of elements has a meet and a join. It is unrelated to module lattices or quadratic-form lattices.
- HomCategory, EndCategory, and AutCategory refinements live in `homsets.py`.
- Hom elements are order-preserving maps, poset endomorphisms, and poset automorphisms. Generic aut-category construction is inherited from root `homsets/`.

Poset tests: `new_spec/` exercises the project poset surface, `regression/` maps Sage constructors to the spec, and `sage_gaps/` records genuine upstream gaps only.
