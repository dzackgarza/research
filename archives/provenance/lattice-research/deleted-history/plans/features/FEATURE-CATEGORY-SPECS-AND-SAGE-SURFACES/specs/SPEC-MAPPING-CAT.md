---
id: SPEC-MAPPING-CAT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track cat mapping spec
status: complete
priority: critical
requirement: Convert category_specs/cat/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  category-object, Hom, End, Aut, and construction signatures.
acceptanceCriteria:
- Source paths category_specs/cat/docs/MAPPING.md and category_specs/cat/docs/SAGE_INVENTORY.md
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
# Cat Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/cat/docs/MAPPING.md`.

Source inventory: `category_specs/cat/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.
- When a public method has a convention likely to surprise a mathematically literate user,
  its defining docstring must include a diagnostics paragraph naming the condition, the
  convention, and the adjacent method or object that carries the other common meaning.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/cat/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/category.py`
  - `sage/categories/category_singleton.pyx`
  - `sage/categories/category_with_axiom.py`
  - `sage/categories/category_types.py`
  - `sage/categories/objects.py`
  - `sage/categories/homsets.py`
  - `sage/categories/homset.py`
  - `sage/categories/functor.pyx`
  - `sage/categories/pushout.py`
  - `sage/categories/covariant_functorial_construction.py`
  - `sage/categories/subobjects.py`
  - `sage/categories/quotients.py`
  - `sage/categories/subquotients.py`
  - `sage/categories/cartesian_product.py`
  - `sage/categories/isomorphic_objects.py`
  - `sage/categories/dual.py`
  - `sage/categories/tensor.py`
- Source-visibility gaps from inventory tokens requiring follow-up during completeness audit:
  - `sage/sets/__init__.py`
  - checked construction modules are exposed directly as `sage/categories/*.py`,
    not through `sage/categories/constructions/`; see the Cat core negative finding
    below for the search record.
  - checked local slice/coslice selectors remain project-owned construction surfaces;
    see the Cat core negative finding below for the `objects_over.py` and
    `objects_under.py` source search.
- Reconciled source-path corrections:
  - This install exposes
    standard construction classes directly as `sage/categories/subobjects.py`,
    `sage/categories/quotients.py`, `sage/categories/subquotients.py`, and
    `sage/categories/cartesian_product.py`.
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Cat core
  method reconciliation is recorded in `Completeness Reconciliation: Cat Core` below,
  with remaining gaps routed through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Converted Mapping Content

This file maps Sage's category and functor machinery to the project `Cat()` subtree.

## Category Objects

Sage `sage.categories.category.Category` instances are the objects of `Cat()`.
For `C = Cat()`, the membership check `X in C` means exactly that `X` is a category
object. A functor is not an object of `Cat()`; it is an element of a functor homset
`A.Hom(B)`.

Consequences:

- Every project top-level category and subcategory should satisfy `C in Cat()`.
- Every category object should get shared category-object operations from
  `Cat.ParentMethods`.
- A homset category is itself a category object, so no separate object-membership
  rule is needed for functor categories.

## Category Order

Sage `Category.is_subcategory(self, c)` is the canonical subcategory relation.

Mapping:

- `C.leq(D)` means `C.is_subcategory(D)`.
- `C.geq(D)` means `D.is_subcategory(C)`.
- `C <= D` and `C >= D` are shorthands for the same relation.
- `Cat().join([C, D, ...])` delegates to Sage `Category.join`.
- `Cat().meet([C, D, ...])` delegates to Sage `Category.meet`, except that the empty
  meet returns `Cat().Constructors().EmptyCategory()`.

This follows Sage's own meaning: `C.is_subcategory(D)` asserts that there is a
natural forgetful functor from `C` to `D`. The comparison shorthands are specified
for ordinary category objects only; `Cat()` itself is the root ambient category in
this spec and does not re-export `leq`, `geq`, `<=`, or `>=`.

## Uniform Category-Object Surface

`Cat.ParentMethods` is the single source of truth for operations every category
object should expose:

- `HomCategory()` / `EndCategory()` / `AutCategory()` for category-level hom, end,
  and aut constructions;
- `Hom(D)` for the object-level functor homspace in `Cat`;
- `leq`, `geq`, `<=`, and `>=` for the Sage category order between ordinary
  category objects;
- containment hooks for categories that need object and morphism membership:
  `_sage_super_categories`, `_sage_object_classes`, and `_sage_morphism_classes`.

Wrapped category instances receive ordinary category-object methods through Sage's
generated classes. The wrapper base layer in `base_category_types.py` is the only
place that flattens `UniversalSubcategoryMethods` into Sage's `SubcategoryMethods`
provider path.

Direct `Hom` ownership is intentionally narrow:

- if `A, B in Cat()`, then `A.Hom(B)` is the object-level functor homspace
  `Hom_{Cat}(A, B)`;
- `A.HomCategory()` is the category-level hom-category construction over objects of
  `A`;
- lower subtrees may refine `HomCategory`, `EndCategory`, and `AutCategory`, but they
  must not define a direct `Hom` method on category objects that changes the meaning
  of `A.Hom(B)` for category objects.

The migration rule is: a subtree-local direct `Hom` method that constructs set maps,
module homomorphisms, ring homomorphisms, continuous maps, or other specialized
morphisms belongs on the subtree hom-category surface, not on the category object
itself. Put such constructors on the relevant `HomCategory().ParentMethods`,
`EndCategory().ParentMethods`, `AutCategory().ParentMethods`, or the concrete
`HomCategory().Of(A, B)` parent. Existing `HomCategory = ...` assignments and nested
`class HomCategory(...)` refinements are admissible when they specialize the
category-level hom construction rather than shadowing `A.Hom(B)`.

As of the 2026-05-04 shadowing audit, direct `def Hom` definitions under
`category_specs/` occur only in `cat/__init__.py` and `cat/base_category_types.py`.
Future lower-subtree direct `Hom` definitions should be filed as implementation
refactor work with this mapping section as the owner/migration source.

## Global Category Diagnostics

The category framework must expose one global diagnostic flag and one category-system
diagnostic logger. The flag is disabled by default. Enabling it must not change return
values, dispatch, containment, coercion, or category refinement; it only permits
background diagnostic messages for conventions that are mathematically correct but easy
to misread.

The diagnostic surface is framework-owned rather than subtree-owned. The canonical API
lives in `category_specs.utils` so every subtree can import the same process-local flag
without creating category-specific copies:

- `category_diagnostics_enabled()` reads whether category diagnostics are enabled;
- `set_category_diagnostics_enabled(enabled)` sets the process-local flag;
- `enable_category_diagnostics()` and `disable_category_diagnostics()` are the explicit
  toggles;
- `emit_category_diagnostic(message, *, key=None, once=True)` emits a logging warning
  through the category diagnostic logger only when the flag is enabled;
- `category_diagnostic_logger()` returns the logger named
  `category_specs.diagnostics`;
- `clear_category_diagnostic_history()` clears the once-per-key suppression cache
  without changing mathematical behavior.

Diagnostic messages are appropriate for surprise boundaries such as:

- two standard mathematical meanings sharing a name in nearby software conventions;
- a compatibility spelling whose result is not the object a user might infer from the
  spelling alone;
- inherited Sage behavior that is being preserved as interop evidence, not as a
  mathematical adequacy standard;
- convention-dependent identifications, such as a transported structure that only exists
  after nondegeneracy, freeness, a selected basis, a selected ordering, or another
  recorded hypothesis.

The motivating example is the lattice/module dual boundary. If an implementation
supports a lattice-side compatibility spelling such as `L.dual()`, then for a
degenerate symmetric bilinear object such as a rank-one isotropic sublattice
`L = <e>` inside a hyperbolic plane, diagnostics should be able to warn that the
returned metric dual `L^#` is not the Hom dual `Hom_R(L, R)`. The Hom dual is the
evaluation-bearing dual object; the metric dual is a formed-module construction that
becomes comparable to the Hom dual only through explicit form-induced transport under
the stated hypotheses.

Diagnostic messages are not an error-recovery mechanism. Missing hypotheses,
ill-defined mathematics, failed containment, invalid source grounding, or an
implementation gap should still fail, block the affected spec leaf, or route to a
tracked decision according to the workflow rules.

Any method whose implementation should emit such a diagnostic must say so in the method
definition docstring. The docstring should include:

- the exact condition under which diagnostics should emit;
- the mathematical convention being used;
- the common but different interpretation the user may have expected;
- the method, category, or object that carries that other interpretation when it exists.

## Containment

For an arbitrary category object `C`, `X in C` may mean either:

- `X` is an object of `C`; or
- `X` is a morphism in `C`.

For `C = Cat()`, this specializes to category-object membership only. Functor
membership is expressed by the relevant homset:

- `F in A.Hom(B)` for functors `A -> B`;
- `F in A.Hom(A)` for endofunctors of `A`;
- autofunctors are the invertible elements of `A.Hom(A)`.

## Functors

Sage `Functor` instances are morphisms between category objects.

The project surface records Sage's functor call model:

- `_coerce_into_domain(x)`;
- `_apply_functor(x)`;
- `_apply_functor_to_morphism(f)`;
- `__call__(x)` dispatching through those hooks;
- `domain()` and `codomain()`.

Sage construction functors from `sage.categories.pushout` are still actual functors,
but their extra Sage surface is recorded separately: `pushout`, `merge`, `commutes`,
`expand`, `common_base`, and `coercion_reversed`.

This is distinct from Sage `FunctorialConstructionCategory` classes such as
`SubobjectsCategory` or `QuotientsCategory`. Those are category objects produced by
methods like `C.Subobjects()`, not functors with domains, codomains, and object/morphism
actions.

Sage provides no general computable fixed-point operation for arbitrary endofunctors,
so `fixed_points()` is not a Cat-level functor method surface.

## Standard Constructions

Sage functorial construction categories map directly to category-object methods.  A
selector such as `C.HomCategory()` evaluates the corresponding construction functor at
`C`; the return value is the category object `Hom_C`.

| Sage class | Project method | Local file |
| --- | --- | --- |
| `SubobjectsCategory` | `C.Subobjects()` | `subcategories/constructions/subobjects.py` |
| `QuotientsCategory` | `C.Quotients()` | `subcategories/constructions/quotients.py` |
| `SubquotientsCategory` | `C.Subquotients()` | `subcategories/constructions/subquotients.py` |
| `CartesianProductsCategory` | `C.CartesianProducts()` | `subcategories/constructions/cartesian_products.py` |
| `TensorProductsCategory` | `C.TensorProducts()` where tensor products are defined | `subcategories/constructions/tensor_products.py` |
| `DualObjectsCategory` | `C.DualObjects()` where dual objects are defined | `subcategories/constructions/dual_objects.py` |
| `IsomorphicObjectsCategory` | `C.IsomorphicObjects()` where isomorphic-object transport is defined | `subcategories/constructions/isomorphic_objects.py` |
| Local slice construction | `C.ObjectsOver(T)` | `subcategories/constructions/objects_over.py` |
| Local coslice construction | `C.ObjectsUnder(T)` | `subcategories/constructions/objects_under.py` |
| `HomsetsCategory` | `C.HomCategory()` | `homsets.py` |
| `HomsetsCategory.Endset()` | `C.EndCategory()` | `endsets.py` |
| `HomsetsCategory.Autset()` | `C.AutCategory()` | `autsets.py` |
| `JoinCategory` | `Cat().JoinCategories()` containment | `join_categories.py` |

The universal selectors for `Subobjects`, `Quotients`, `Subquotients`,
`ObjectsOver`, `ObjectsUnder`, and `CartesianProducts` live in
`universal_subcategory_methods.py`. Other standard construction names, such as
`TensorProducts()` and `DualObjects()`, are exposed by the subtrees where the
mathematics is available. Individual category classes still declare their construction
classes, and Sage's `category_of(...)` machinery resolves the specific construction
for the receiver.

For wrapped ordinary category objects, `C.Hom(D)` delegates to Sage's parent homspace
for functors `C -> D`. The category-level construction is `C.HomCategory()`. The
object-level endomorphism functor space is `C.Hom(C)`.

For `Cat()`, `Subobjects` means subcategories, `Quotients` means quotient
categories, `Subquotients` means category-level subquotients, and
`CartesianProducts` means product categories.

## Constructor Aggregation Forwarders

`Cat().Constructors()` is an aggregator over already-scoped constructor namespaces.
The generated forwarding methods in `base_category_types.py` may use Python
`*args`/`**kwargs` internally because they do not define a mathematical constructor
surface. They forward to the owning constructor method, whose signature remains the
single public source of truth.

Mapping rule:

| Implementation hook | Public owner | Consequence |
| --- | --- | --- |
| `_cat_constructor_forwarder(...).forwarded_constructor(self, *args, **kwargs)` | The target subtree constructor, e.g. `Rings().Constructors().PolynomialRing(...)` or `Modules(R).Constructors().FreeModule(...)` | Allowed only as generated private forwarding glue. Do not treat the generated Cat method as evidence that a broad public variadic constructor is admitted. |
| `_CatObjectMixin.__init_subclass__(cls, **kwargs)` and the local `initialize_and_register(self, *args, **kwargs)` wrapper | Python/Sage subclass initialization plumbing | Not a category-spec method surface. The wrapper exists to register constructor owners after Sage/Python initialization and does not create mathematical input casework. |

## Slice and Coslice Categories

Sage does not provide a dedicated installed class for categories over or under a
fixed category in the same way it provides `SubobjectsCategory` and
`QuotientsCategory`. The local mapping is:

- `C.ObjectsOver(T)` means categories `D` equipped with a structure functor
  `D -> T`;
- `C.ObjectsUnder(T)` means categories `D` equipped with a structure functor
  `T -> D`;
- `Slice = ObjectsOver`;
- `Coslice = ObjectsUnder`.

These classes use Sage's `RegressiveCovariantConstructionCategory` plus
`Category_over_base`, so they follow the same `category_of(...)` entry point as
Sage's built-in regressive constructions.

Objects in any slice or coslice construction expose the universal structure-morphism
surface:

- `structure_morphism()` returns the distinguished morphism into or out of the fixed
  object;
- `structure_domain()` is `structure_morphism().domain()`;
- `structure_codomain()` is `structure_morphism().codomain()`.

Set, topological-space, and other lower categories may keep local names such as
`structure_map()` or `structure_functor()` for the category-specific morphism type,
but they do not restate `structure_domain()` or `structure_codomain()`.

## Hom, End, and Aut Categories

`CatHomCategory` is the category of functor categories internal to `Cat()`.  The
functorial construction is `Hom_*: Cat -> Cat`, which sends a category `C` to the
category object `Hom_C`.

Mapping:

- `C.HomCategory()` is the category-level functorial construction whose objects are
  `Hom_C(A, B)` for objects `A, B` of `C`;
- `C.HomCategory().Of(A, B)` is `Hom_C(A, B)`;
- `Cat().HomCategory()` is therefore the category of functor categories;
- `A.Hom(B)` returns Sage's `Hom(A, B, category=Cat())` parent when `A` and `B`
  are category objects;
- `A.Hom(B).category()` is `Cat().HomCategory()`;
- `A.Hom(A)` is the object-level endofunctor parent;
- hom elements are Sage `Functor` instances;
- Sage `ConstructionFunctor` instances have a specialized functor method surface; they
  are not the same object as the construction-category value `Hom_C`.

The repository-level `homsets/` subtree owns generic hom/end/aut vocabulary such as
`domain`, `codomain`, `EndCategory`, and `AutCategory`. The Cat subtree adds only the
functor-specific element surface and the `CatHomCategory`, `CatEndCategory`, and
`CatAutCategory` refinements. These live in separate files:
`cat/homsets.py`, `cat/endsets.py`, and `cat/autsets.py`.

## Constructors

`Constructors` is a plain collection class. A category opts in by defining a
`Constructors` collector that advertises named constructors for objects it owns or
constructs and then refines into its hierarchy. The collector is not a category, not a
functorial construction, and not a subcategory namespace.

`Cat().Constructors()` owns category-object constructor entry points and constructor
collection. It currently exposes:

- `EmptyCategory()`: the bottom category object used by `Cat().meet([])` and by any
  surface that needs the empty category as a category object.

It also exposes constructor discoverability without moving constructor ownership. There
is no public registration call and no separate aggregate object. The declaration is the
existence of an explicit nested `Constructors` class on a category object. During Cat
object initialization, backend code inspects that class and installs deterministic
prefixed forwarding methods on `Cat.Constructors`.

Prefixed names are the category prefix and constructor method name joined by an
underscore. A category-local constructor name must not repeat the category noun in a
`category_from_*` pattern: use `C.Constructors().from_xyz(...)`, so Cat exposes
`cat_prefix_from_xyz(...)`. For example, `Posets().Constructors().from_digraph(...)`
is exposed as `Cat().Constructors().posets_from_digraph(...)`. These methods forward
to the original category-owned constructor collector; they do not move constructor
ownership to `Cat`.

Constructor placement is a style boundary in this spec. Prefer explicit top-level
category collectors because they are easy to audit and collect. Do not enforce that
preference with runtime guards whose only effect is to reject proper subcategories; a
future registered subcategory collector may be valid if it is a deliberate opt-in
surface.

Ordinary category objects are registered by being Sage/project `Category` instances.
Functors are registered by being Sage `Functor` or `ConstructionFunctor` instances and
by lying in the relevant functor homset.

## Completeness Reconciliation: Cat Core

This pass checked the local inventory, the converted mapping body, and the installed
Sage 10.7 category source files listed in the source ledger.

- `Category.__contains__` tests whether `x.category()` is a subcategory of the
  receiver, while `Category.category()` returns `Objects()` for Sage category
  instances. The project `Cat()` membership rule is therefore a deliberate refinement
  of Sage's category-object runtime fact: category instances are the project objects
  of `Cat()`, while arbitrary Sage objects continue to live in their mathematical
  categories such as `Sets()`, `Rings()`, or `Modules(R)`.
- `Category.is_subcategory(self, c)` is source-backed as the category order, with the
  mathematical meaning "there is a natural forgetful functor from `self` to `c`".
  The spec mapping of `leq`, `geq`, `<=`, and `>=` is therefore an order surface on
  category objects, not a morphism-construction surface.
- `Category.join(categories, ...)` is source-backed as Sage's category-lattice join.
  Sage treats the empty join as `Objects()`, so the local `Cat().join([])` behavior
  should remain top-category behavior unless an explicit project decision changes the
  order convention.
- `Category.meet(categories)` is source-backed as Sage's meet for nonempty category
  collections and raises on an empty input. The local mapping that `Cat().meet([])`
  returns `Cat().Constructors().EmptyCategory()` is a project completion of Sage's
  missing bottom-category case, not an upstream Sage behavior claim.
- `JoinCategory` remains a category object that represents an intersection condition
  on objects and morphisms. Mapping it to `Cat().JoinCategories()` containment is
  well-typed: membership is about recognizing join category objects, not about moving
  methods to the constructed join result.
- `Category_singleton` is implemented in this install as `category_singleton.pyx`.
  Singleton status is an implementation/classcall fact for categories such as
  `Sets()` and `Rings()`, not a separate mathematical method surface on `Cat()`.
- `CategoryWithAxiom`, `CategoryWithAxiom_over_base_ring`, and
  `CategoryWithAxiom_singleton` are source-backed as axiom-category implementation
  classes. Their mapping remains style/process guidance for correct wrapper bases;
  an axiom restriction belongs on the category where the axiom is mathematically
  meaningful, not as a generic Cat-level method beyond the category-object machinery.
- `Category_over_base`, `Category_over_base_ring`, `Category_module`, and
  `Category_ideal` are source-backed as parameterized Sage category base classes.
  Their base/base-ring/ambient data are evidence for lower subtree ownership and
  wrapper selection, not extra Cat-level constructors.
- `Functor` is source-backed as a morphism between category objects with domain,
  codomain, object action, morphism action, and domain-coercion hooks. The spec
  mapping to functor homsets is therefore the mathematically coherent owner: functor
  elements live in `A.Hom(B)`, not as objects of `Cat()`.
- `ConstructionFunctor` and `CompositeConstructionFunctor` subclass the Sage functor
  surface and add pushout/coercion-combination methods. The mapped methods
  `pushout`, `merge`, `commutes`, `expand`, `common_base`, and `coercion_reversed`
  remain construction-functor interop surface, not evidence for turning every
  functorial construction category into a functor element.
- `FunctorialConstructionCategory.category_of(category, *args)` is the source-backed
  entry point for categories produced by functorial constructions such as
  `C.Subobjects()` or `C.CartesianProducts()`. These construction categories are
  category objects in the project sense, distinct from `Functor` elements with
  domain/codomain/action.
- `CovariantConstructionCategory.default_super_categories`,
  `RegressiveCovariantConstructionCategory.default_super_categories`,
  `additional_structure`, and `is_construction_defined_by_base` justify the spec's
  inheritance rule for standard construction selectors: a selector method is defined
  on the category where the construction is meaningful, and subcategories inherit the
  resulting method surface through Sage's supercategory machinery.
- `SubobjectsCategory`, `QuotientsCategory`, and `SubquotientsCategory` are installed
  directly under `sage/categories/`. Their source docstrings state that subobjects and
  quotients are subquotients and that regressive constructions keep the constructed
  object in the original category. The mapping to `C.Subobjects()`,
  `C.Quotients()`, and `C.Subquotients()` is therefore a category-object construction
  surface, not an object-local method on the produced subobject or quotient.
- `CartesianProductsCategory` is installed directly under `sage/categories/` and
  exposes idempotent `CartesianProducts()` plus base-ring forwarding. The mapped
  `C.CartesianProducts()` selector is source-backed as a category-level finite product
  construction; product-object operations belong in the owning lower category.
- `IsomorphicObjectsCategory` is source-backed and defaults through subobjects and
  quotients. The project `C.IsomorphicObjects()` selector is well-typed as a
  category-object construction for images under isomorphism; it does not introduce a
  nonmathematical "isomorphic result" owner.
- `DualObjectsCategory` and `TensorProductsCategory` are source-backed Sage
  construction categories, but their mathematical existence depends on the receiver
  category. The Cat spec correctly records these as exposed by lower subtrees where
  duals and tensor products are defined, rather than universal Cat methods.
- `Objects.SubcategoryMethods.Homsets()` and `Endsets()` are source-backed as Sage's
  generated homset/endset category navigation. The Cat mapping to `HomCategory()` and
  `EndCategory()` is a project naming refinement over Sage's plural `Homsets`/
  `Endsets` vocabulary; generic Hom/End/Aut method ownership remains in the
  repository-level homsets spec.
- The prior homsets reconciliation records the negative-finding evidence for Sage's
  generic Autset gap. The Cat `AutCategory()` surface therefore remains a
  project-owned refinement for invertible endomorphisms, with Sage `Homsets.Endset`
  only serving as partial upstream evidence.
- The local `ObjectsOver(T)` and `ObjectsUnder(T)` selectors remain project-owned
  slice/coslice category surfaces. They are mathematically meaningful category-level
  constructions, but not installed Sage standard construction modules in the checked
  source tree.
- `Cat().Constructors()` remains an aggregator over explicit category-owned
  constructor collectors. Generated private forwarders with `*args`/`**kwargs` are
  implementation glue only; they do not create public variadic mathematical
  signatures.

Negative missing-surface finding for this Cat core pass:

- Searched: `category_specs/cat/docs/SAGE_INVENTORY.md`;
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md`;
  installed Sage 10.7 files `category.py`, `category_singleton.pyx`,
  `category_with_axiom.py`, `category_types.py`, `objects.py`, `homsets.py`,
  `homset.py`, `functor.pyx`, `pushout.py`,
  `covariant_functorial_construction.py`, `subobjects.py`, `quotients.py`,
  `subquotients.py`, `cartesian_product.py`, `isomorphic_objects.py`, `dual.py`,
  and `tensor.py`; and a direct file search of the installed `sage/categories/`
  root for category, functor, homset, subobject, quotient, cartesian-product,
  tensor, dual, and object/slice construction modules.
- Found: the checked sources support the current Cat mapping surfaces and identify
  two stale source-path assumptions in the ledger: `category_singleton` is a `.pyx`
  source in this installation, and Sage's standard construction modules are direct
  `sage/categories/*.py` files rather than files under `sage/categories/constructions/`.
  I found no additional installed Sage Cat-core public surface in this pass that
  requires a new Cat mapping row beyond the existing category-object, order,
  functor, standard-construction, Hom/End/Aut, and constructor-aggregation sections.
- Conclusion: inference -- for the checked Cat-core Sage category/functor framework
  surface, the converted Cat mapping spec is source-complete modulo lower-subtree
  mathematical audits for tensor products, duals, slice/coslice implementation, and
  generic Aut-category implementation ownership.
- Confidence: Medium.
- Gaps: this pass did not enumerate every mathematical category module under
  `sage/categories/`; those are owned by the domain mapping specs such as sets, rings,
  modules, algebras, posets, topology, tensors, forms, and lattices. It also did not
  search Sage git history, third-party Sage extensions, or unavailable online HTML docs
  beyond the installed source tree.

## 6-Gate Protocol Review Log

Review conducted 2026-05-07 against Sage 10.7 installed source at
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/`
and local project files under `/home/dzack/research/category_specs/cat/`.

### Gate 1 — Source Grounding: PASS

**Requirement:** Every mapping row must cite proper Sage source paths. Verify
referenced files exist.

**Evidence:**

- All 17 Sage source files listed in the Source Coverage Ledger (lines 50–66)
  are confirmed present on disk:
  `category.py`, `category_singleton.pyx`, `category_with_axiom.py`,
  `category_types.py`, `objects.py`, `homsets.py`, `homset.py`, `functor.pyx`,
  `pushout.py`, `covariant_functorial_construction.py`, `subobjects.py`,
  `quotients.py`, `subquotients.py`, `cartesian_product.py`,
  `isomorphic_objects.py`, `dual.py`, `tensor.py`.
- Every line-number reference in `SAGE_INVENTORY.md` was spot-checked and
  confirmed accurate: `Category` at category.py:131, `__contains__` at :687,
  `_subcategory_hook_` at :643, `is_subcategory` at :1803, `join` at :2332,
  `meet` at :1979, `category()` returning `Objects()` at :2536,
  `CategoryWithParameters` at :2717, `JoinCategory` at :3004,
  `SubobjectsCategory` at subobjects.py:20, `CartesianProductsCategory` at
  cartesian_product.py:226, `HomsetsCategory` at homsets.py:19,
  `ConstructionFunctor` at pushout.py:45,
  `CompositeConstructionFunctor` at pushout.py:419,
  `FunctorialConstructionCategory` at covariant_functorial_construction.py:231,
  `CovariantConstructionCategory` at :516,
  `RegressiveCovariantConstructionCategory` at :662.
- Functor methods `domain`, `codomain`, `__call__`, `_apply_functor`,
  `_coerce_into_domain`, `_apply_functor_to_morphism` all confirmed present in
  `functor.pyx`.
- The `is_subcategory` docstring at category.py:1805 literally matches the
  spec's paraphrase: "Return True if there is a natural forgetful functor from
  self to c."
- The spec's source-path correction from `category_singleton.py` to `.pyx` is
  confirmed correct — only `category_singleton.pyx` exists on disk (alongside
  `.pxd` and `.cpython-312-x86_64-linux-gnu.so`).
- The spec's finding that `sage/categories/constructions/` does not exist and
  standard construction modules live directly under `sage/categories/` is
  confirmed.
- `sage/sets/__init__.py` is confirmed absent (source-visibility gap correctly
  flagged in the ledger).
- The local project files referenced in the construction mapping table were
  verified:
  - 10 of 13 exist under `category_specs/cat/`:
    `subobjects.py`, `quotients.py`, `subquotients.py`, `cartesian_products.py`,
    `objects_over.py`, `objects_under.py`, `homsets.py`, `endsets.py`,
    `autsets.py`, `join_categories.py`.
  - 3 are absent: `tensor_products.py`, `dual_objects.py`,
    `isomorphic_objects.py`. These are acknowledged as owned by lower subtrees
    (modules, algebras, lattices, sets), consistent with the spec's own
    statement (lines 283–284) that `TensorProducts()` and `DualObjects()` are
    "exposed by the subtrees where the mathematics is available."
  - Minor note: the `IsomorphicObjectsCategory` row in the table lists
    `subcategories/constructions/isomorphic_objects.py` relative to `cat/`, but
    the only existing isomorphic_objects construction file lives at
    `sets/subcategories/constructions/isomorphic_objects.py`. This does not
    break the mapping but the table path is ambiguous.
- The diagnostic API specified in the Global Category Diagnostics section
  (lines 164–218) is confirmed implemented at
  `/home/dzack/research/category_specs/utils.py` with all six functions
  (`category_diagnostics_enabled`, `set_category_diagnostics_enabled`,
  `enable_category_diagnostics`, `disable_category_diagnostics`,
  `category_diagnostic_logger`, `emit_category_diagnostic`,
  `clear_category_diagnostic_history`) present and matching the spec signatures.

**Verdict:** All Sage source references are concrete and verified. The three
missing local files are correctly acknowledged as lower-subtree-owned.

### Gate 2 — Sage Surface Completeness: PASS

**Requirement:** Every inventoried Sage surface must be accounted for.

**Evidence:**

The `SAGE_INVENTORY.md` documents the following Sage surfaces, and every one
is accounted for in the spec's Completeness Reconciliation (lines 403–526):

| Sage surface | Accounted in spec |
|---|---|
| `Category.__contains__` → `x.category().is_subcategory(self)` | Refined to Cat() membership rule (lines 91–102, 220–232, 408–413) |
| `Category.category()` → `Objects()` | Acknowledged, Cat() membership is a deliberate refinement (lines 408–413) |
| `Category.is_subcategory` | Mapped to `leq`/`geq`/`<=`/`>=` order surface (lines 106–120, 414–417) |
| `Category.join` | Mapped to `Cat().join()` (lines 113, 418–421) |
| `Category.meet` (raises on empty) | Mapped + project completion for empty case (lines 114–116, 422–426) |
| `JoinCategory` | Mapped to `Cat().JoinCategories()` containment (lines 278, 427–429) |
| `Category_singleton` | Acknowledged as implementation fact, not method surface (lines 430–432) |
| `CategoryWithAxiom` + variants | Acknowledged as axiom-category implementation classes (lines 433–437) |
| `Category_over_base` + variants | Acknowledged as evidence for lower subtree ownership (lines 438–441) |
| `Functor` (7 methods) | Mapped to functor homset elements `A.Hom(B)` (lines 234–248, 442–445) |
| `ConstructionFunctor` (6 extra methods) | Mapped as construction-functor interop surface (lines 246–248, 446–450) |
| `CompositeConstructionFunctor` | Acknowledged as subclass surface (line 448) |
| `FunctorialConstructionCategory.category_of` | Source-backed as construction entry point (lines 451–455) |
| `CovariantConstructionCategory` / `RegressiveCovariantConstructionCategory` | Justifies inheritance rule for selectors (lines 456–461) |
| `SubobjectsCategory` / `QuotientsCategory` / `SubquotientsCategory` | Mapped to `C.Subobjects()` / `C.Quotients()` / `C.Subquotients()` (lines 462–467) |
| `CartesianProductsCategory` | Mapped to `C.CartesianProducts()` (lines 468–471) |
| `IsomorphicObjectsCategory` | Mapped to `C.IsomorphicObjects()` (lines 472–475) |
| `DualObjectsCategory` / `TensorProductsCategory` | Mapped to lower-subtree-exposed selectors (lines 476–479) |
| `HomsetsCategory` / `Objects.SubcategoryMethods.Homsets()` / `Endsets()` | Mapped to `HomCategory()` / `EndCategory()` (lines 480–484) |
| Generic Autset gap (no Sage class) | Routed as project-owned `AutCategory()` refinement (lines 485–488) |
| Slice/coslice (no Sage standard module) | Routed as project-owned `ObjectsOver`/`ObjectsUnder` surfaces (lines 489–492) |
| Constructor aggregation | Mapped to `Cat().Constructors()` aggregator (lines 298–309, 493–496) |

**Verdict:** Complete coverage. No inventoried Sage surface is unaddressed.
The generic Autset gap and slice/coslice gaps are explicitly documented as
project-owned refinements.

### Gate 3 — Constructor Route Justification: PASS

**Requirement:** Routes must be mathematically valid.

**Evidence:**

1. **Functor mapping:** Functors are placed as elements of functor homsets
   `A.Hom(B)`, not as objects of `Cat()`. This is mathematically correct —
   in the category of (small) categories, objects are categories, and
   morphisms are functors. Sage `Functor` instances carry `domain()` and
   `codomain()` methods returning `Category` instances, confirming their
   status as morphisms. The `__call__` dispatch through
   `_coerce_into_domain` → `_apply_functor` / `_apply_functor_to_morphism`
   → codomain check is a faithful implementation of functor application.

2. **Category order:** `is_subcategory` is correctly interpreted as the
   partial order on categories (there exists a natural forgetful functor).
   The `leq`/`geq`/`<=`/`>=` shorthands are order-comparison surface, not
   morphism-construction surface. This is mathematically sound.

3. **Construction categories:** `C.Subobjects()`, `C.Quotients()`, etc.,
   are category-level constructions evaluated at a category object `C`.
   They return a category object (the construction category), not an
   element or morphism. This matches Sage's `category_of()` pattern and is
   mathematically correct — these are functorial constructions, not
   individual objects/morphisms.

4. **Hom construction:** `C.HomCategory()` returns the category-level
   hom-category construction. `C.Hom(D)` returns the object-level functor
   homspace. `C.HomCategory().Of(A, B)` returns `Hom_C(A, B)`. This
   three-level distinction (category-level construction, object-level
   homspace, element-level morphism set) is mathematically precise.

5. **Slice/coslice:** `C.ObjectsOver(T)` returns categories `D` equipped
   with a functor `D → T`. `C.ObjectsUnder(T)` returns categories `D`
   equipped with a functor `T → D`. These are the standard slice/coslice
   constructions in Cat, mathematically well-defined.

6. **Join/meet lattice:** Sage `Category.join` corresponds to intersection
   (objects/morphisms belonging to all supercategories); Sage
   `Category.meet` corresponds to greatest lower bound in the category
   lattice. The spec correctly identifies these as lattice operations, not
   as coproduct/product in Cat. The project completion of empty meet →
   `EmptyCategory()` adds a bottom element to the lattice, which is
   mathematically sound (the empty category is subcategory of every
   category).

7. **Constructor aggregation:** `Cat().Constructors()` is an aggregator
   over category-owned constructor collectors. Generated variadic
   forwarders are explicitly marked as implementation glue, not public
   mathematical signatures. This preserves the mathematical surface while
   allowing discoverability.

**Verdict:** All constructor routes are mathematically valid and grounded in
Sage's actual API semantics.

### Gate 4 — Nonmathematical Rejection: PASS

**Requirement:** Explicitly reject nonmathematical surfaces.

**Evidence:**

The following surfaces are explicitly rejected or marked as non-spec:

| Surface | Disposition | Location |
|---|---|---|
| `*args`/`**kwargs` forwarders on `Cat().Constructors()` | Marked as private implementation glue, not public mathematical signatures | Lines 299–309 |
| `_CatObjectMixin.__init_subclass__` and `initialize_and_register` wrapper | Marked as Python/Sage initialization plumbing, not category-spec method surface | Lines 309–310 |
| `fixed_points()` on endofunctors | Explicitly rejected: "Sage provides no general computable fixed-point operation for arbitrary endofunctors" | Lines 255–256 |
| Raw Sage implementation containers | Rejected per acceptance criteria | Line 21 |
| Variadic option bags | Rejected per review gates | Line 39 |
| Smoke-driven interface weakening | Rejected per review gates | Line 39 |
| `Cat()` re-exporting `leq`/`geq`/`<=`/`>=` | Explicitly excluded: "Cat() itself is the root ambient category ... and does not re-export" | Lines 119–120 |

**Verdict:** Nonmathematical surfaces are explicitly identified and rejected.
No specification surface is being created for implementation-only artifacts.

### Gate 5 — Ambiguity Routing: PASS

**Requirement:** Unresolved issues must have decision cards or explicit routing.

**Evidence:**

| Ambiguity / Gap | Routing |
|---|---|
| Generic Autset gap in Sage | Routed as project-owned `AutCategory()` refinement with Sage `Homsets.Endset` as partial upstream evidence (lines 485–488) |
| Slice/coslice (no installed Sage module) | Routed as project-owned `ObjectsOver`/`ObjectsUnder` with `RegressiveCovariantConstructionCategory` + `Category_over_base` backing (lines 311–326, 489–492) |
| Empty meet behavior | Explicitly acknowledged as project completion, not upstream Sage claim (lines 422–426) |
| Tensor/Dual construction existence depends on receiver category | Routed to lower-subtree mathematical audits (lines 476–479) |
| `sage/sets/__init__.py` source-visibility gap | Flagged as requiring follow-up in completeness research (lines 67–68) |
| Lower-subtree mathematical audits (tensor, dual, slice/coslice implementation, generic Aut-category) | Routed to `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` (line 83) |
| Import probe caveat (`ImportError: cannot import name Category`) | Acknowledged; installed source files and inventories used as durable source surface (lines 80–81) |
| Category-spec vs Sage adequacy boundary | Documented in `category_specs/AGENTS.md` and spec preamble: "Current Sage implementation coverage is not the adequacy standard" |

**Verdict:** All ambiguities and gaps have explicit routing to decision cards,
task cards, or documented project-owned surfaces. No unresolved ambiguity
blocks the spec from being used as a source of truth.

### Gate 6 — Obligation Preservation: PASS

**Requirement:** No weakening without grounded replacement.

**Evidence:**

1. **No deleted abstract methods:** The spec adds project-owned surfaces
   (AutCategory, ObjectsOver, ObjectsUnder, EmptyCategory for empty meet)
   without removing any Sage-backed obligations. The Sage `Functor`,
   `ConstructionFunctor`, `Category.is_subcategory`, `Category.join`,
   `Category.meet`, and construction category surfaces are all preserved.

2. **Hom ownership migration rule preserves obligations:** The rule
   (lines 140–162) explicitly prevents lower subtrees from defining a direct
   `Hom` method that would shadow `A.Hom(B)`. The migration path moves such
   constructors to the hom-category surface rather than deleting them. An
   audit of the 2026-05-04 shadowing check confirms no drift.

3. **Empty meet adds bottom element, does not weaken:** The project
   completion `Cat().meet([]) → EmptyCategory()` adds a bottom category
   object to the lattice. Sage's existing non-empty meet behavior is
   preserved unchanged.

4. **Constructor aggregation preserves ownership:** `Cat().Constructors()`
   forwards to category-owned constructors; it does not move ownership to
   `Cat()`. This preserves the original constructor signatures as the
   single source of truth.

5. **Diagnostic surface is additive:** The global category diagnostics
   (section "Global Category Diagnostics") add opt-in logging without
   changing return values, dispatch, containment, coercion, or category
   refinement (lines 167–169). This is explicitly confirmed as framework-owned
   and implemented in `category_specs/utils.py`.

6. **No Sage-gap-driven interface shrinkage:** The spec does not weaken the
   category-object surface because Sage lacks an Autset. Instead, it creates
   a project-owned `AutCategory()` surface. The same pattern holds for
   slice/coslice.

**Verdict:** No obligation weakening detected. All additions are grounded
replacements or project completions of Sage gaps. The spec is monotonic
with respect to the Sage surface it maps.

### Summary

| Gate | Status | Key Finding |
|---|---|---|
| 1 — Source Grounding | **PASS** | 17/17 Sage files confirmed; all inventory line references verified; 10/13 local files present (3 correctly in lower subtrees) |
| 2 — Sage Surface Completeness | **PASS** | Every inventoried Sage surface in SAGE_INVENTORY.md accounted for in completeness reconciliation |
| 3 — Constructor Route Justification | **PASS** | Functors in homsets, construction categories via category_of(), order via is_subcategory — all mathematically valid |
| 4 — Nonmathematical Rejection | **PASS** | Variadic forwarders, init_subclass plumbing, fixed_points() all explicitly rejected |
| 5 — Ambiguity Routing | **PASS** | Autset gap, slice/coslice, empty meet, tensor/dual, import caveat — all routed to decision/task cards or project-owned surfaces |
| 6 — Obligation Preservation | **PASS** | No weakening detected; all additions are grounded replacements or project completions |

### Status Recommendation

**Ready for acceptance.** The Cat mapping spec is source-complete, mathematically
correct, and preserves all obligations. One minor documentation note: the
`IsomorphicObjectsCategory` row in the construction table lists a `cat/`-relative
path that does not exist; the actual file is at
`sets/subcategories/constructions/isomorphic_objects.py`. This does not affect
the mapping correctness but should be corrected when the table is next updated.

The three lower-subtree-owned construction files (tensor_products, dual_objects,
isomorphic_objects) are correctly absent from the `cat/` subtree and are already
tracked in their respective domain mapping specs (modules, algebras, lattices,
sets). No blocking issues.
