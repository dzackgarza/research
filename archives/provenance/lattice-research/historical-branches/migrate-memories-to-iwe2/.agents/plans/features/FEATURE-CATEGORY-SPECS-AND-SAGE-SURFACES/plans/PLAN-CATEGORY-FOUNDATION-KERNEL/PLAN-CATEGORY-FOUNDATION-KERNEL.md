---
id: PLAN-CATEGORY-FOUNDATION-KERNEL
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
title: Category foundation kernel and method ownership
status: complete
priority: critical
owner: Zack
description: 'Establish the foundational category vocabulary before downstream implementation:
  category refinement order, module axioms, Hom/End/Aut structure, dual-object routing,
  standard type aliases, and method ownership.'
successCriteria:
- Dual objects are reconciled with Homset routing before downstream discriminant work.
- Method ownership is moved to the most general mathematically valid category.
- Standard type aliases live in one canonical package.
- TwistedForms is either admitted as a real category or rejected by decision card.
- Constructor-interception work does not precede static category hierarchy and method-surface
  review.
phases:
- '[[PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION]]'
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Category foundation kernel and method ownership

## Objective

Establish the foundational category vocabulary before downstream implementation: category refinement order, module axioms, Hom/End/Aut structure, dual-object routing, standard type aliases, and method ownership.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Child work must use the category-spec purpose as a local acceptance rule, not only as
background policy. The spec defines an ideal mathematical interface inside Sage's
category/object universe. Current Sage coverage is not the adequacy standard, while
Sage interop remains a design constraint where mathematically appropriate. Sage
inventory is implementation evidence and a feasibility witness that helps preserve
existing functionality and avoid unimplementable wishlists. Failed category assertions record
current implementation or wrapper gaps against the ideal interface; they are not
evidence that a spec method should be deleted, weakened, or moved without a grounded
replacement owner.

Every child phase must include a spec-weakening review gate before advancement. Review
the staged diff, unstaged diff, and any commits created during the child work for
deleted abstract methods, removed constructor/category obligations, narrowed category-obligation examples,
or obligation moves without source-grounded replacement owners. A category-obligation example improvement
paired with interface shrinkage fails the child work.

Every child phase must also include a mathematical review gate before implementation
work that changes method ownership or spec surfaces. Method-owner rows must be written
as coherent mathematical claims about caller object, required data, hypotheses,
construction or predicate, and codomain/result. Sage inventory and category-obligation output are
not sufficient grounding until that mathematical sentence is valid.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Admitted Definitions

The foundation kernel admits these source-backed category definitions for child work:

- `Cat()` owns category objects. `X in Cat()` means `X` is a Sage/project category
  object, and functors are elements of the corresponding `A.Hom(B)` parent rather than
  category objects. Source: `category_specs/cat/docs/MAPPING.md`.
- Category refinement order is Sage's `C.is_subcategory(D)`, interpreted as the
  existence of a natural forgetful functor from `C` to `D`. Project shorthands
  `leq`, `geq`, `<=`, and `>=` are only aliases for ordinary category objects.
  Source: `category_specs/cat/docs/MAPPING.md`.
- Standard construction selectors such as `Subobjects()`, `Quotients()`,
  `Subquotients()`, `CartesianProducts()`, `DualObjects()`, `HomCategory()`,
  `EndCategory()`, and `AutCategory()` are category-object methods. A lower subtree may
  refine them but must not redefine direct `A.Hom(B)` to mean a different object-level
  hom. Source: `category_specs/cat/docs/MAPPING.md` and
  `category_specs/homsets/docs/MAPPING.md`.
- `WithGenerators` means a distinguished finite generating tuple, not a basis.
  `FinitelyPresented` may imply `WithGenerators` in the admitted module category
  pattern, but basis-level coordinate operations still require a basis-bearing owner.
  Source: migrated source body in this plan plus `category_specs/modules/docs/MAPPING.md`.

## Source corpus

- `plans/CATEGORY_ABC_SPEC.md`
- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/axioms_with_generators_finitely_presented.md`
- `plans/category_creation_notes.md`
- `plans/homsets_structural_core.md`
- Deleted source holder: `plans/todo.md`

## Subplans

- `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER`: static category refinement and constructor-interception order.
- `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`: Homsets, Endsets, Autsets, duals, and automorphism surfaces.
- `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP`: lattice and ModulesWithForms roadmap.
- `PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION`: Cat category-object surface uniformization.
- `PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE`: module wrapper migration and category graph constructor routing.
- `PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP`: exhaustive method inventory by minimal mathematical owner category.

## Leaf ownership

This is an internal plan. Executable cards must point to one of its leaf subplans
or to `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` when the task is specifically Hom/End/Aut structural work.

## Dependency rule

This plan blocks broad implementation when vocabulary, type aliases, dual-object routing, or method ownership are unsettled. These are mathematical definitions, not cleanup.

## Acceptance Criteria

- [ ] Dual objects are reconciled with Homset routing before downstream discriminant work.
- [ ] Method ownership is moved to the most general mathematically valid category.
- [ ] Method ownership changes preserve the ideal mathematical surface; no child task
      treats a Sage failed category assertion as negative evidence against a spec obligation.
- [ ] Standard type aliases live in one canonical package.
- [ ] TwistedForms is either admitted as a real category or rejected by decision card.
- [ ] Constructor-interception work does not precede static category hierarchy and method-surface review.


## Migrated Source Bodies

### Former `plans/axioms_with_generators_finitely_presented.md`

# Axioms: WithGenerators, FinitelyPresented, and Structural Patterns

## 4. WithGenerators axiom — the correct pattern

The correct precedent is `FinitelyGeneratedAsMagma`: a dedicated axiom name (not
WithBasis, not FinitelyPresented) that adds a distinguished generating set.
The axiom name must be registered in `all_axioms`:

```python
import sage.categories.category_with_axiom as _cwa
_cwa.all_axioms += ("WithGenerators",)
```

The axiom class, nested inside your module category:

```python
class SubcategoryMethods:
    def WithGenerators(self):
        return self._with_axiom("WithGenerators")

class WithGenerators(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        @abstract_method
        def module_generators(self):
            """Distinguished finite generating tuple. NOT a basis."""

        def gens(self):
            return self.module_generators()   # generic shorthand

        def ngens(self):
            return len(self.module_generators())

        def gen(self, i):
            return self.module_generators()[i]

        @abstract_method
        def hom(self, im_gens, codomain=None, check=True):
            """Define a morphism by images of module_generators()."""
```

This mirrors `FinitelyGeneratedMagmas.ParentMethods.magma_generators()`:

**File:** `src/sage/categories/finitely_generated_magmas.py` (L39-56)
```python
    class ParentMethods:
        @abstract_method
        def magma_generators(self):
            """
            Return a generating tuple of ``self``.

            EXAMPLES::

                sage: S = Semigroups().example("free")
                sage: S.magma_generators()
                ('a', 'b', 'c', 'd')
            """
```

## 5. FinitelyPresented axiom — already in all_axioms

"FinitelyPresented" is already registered: `category_with_axiom.py:1685-1686`

The nested class in your module category:

```python
class SubcategoryMethods:
    def FinitelyPresented(self):
        return self._with_axiom("FinitelyPresented")

class FinitelyPresented(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        # Finitely presented implies WithGenerators
        return [self.base_category().WithGenerators()]
```

Over a Dedekind domain (which is Noetherian), finitely generated = finitely presented,
so `FinitelyPresented` and `WithGenerators` coincide in practice.
The `extra_super_categories` encodes this implication categorically.

The existing `Modules.FinitelyPresented` has only the finite-ring finiteness fact:

**File:** `src/sage/categories/modules.py` (L563-593)
```python
    class FinitelyPresented(CategoryWithAxiom_over_base_ring):
        """
        The category of finitely presented modules over a finite ring.
        """
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: Modules(ZZ).FinitelyPresented().extra_super_categories()
                [Category of modules over Integer Ring]
            """
            return [self.base_category()]
```

## 6. Restricting to Dedekind domains / PIDs

`DedekindDomains` and `PrincipalIdealDomains` already exist as categories:

**File:** `src/sage/categories/dedekind_domains.py` (L14-39) **File:**
`src/sage/categories/principal_ideal_domains.py` (L15-46)

In your `__init__`:

```python
from sage.categories.dedekind_domains import DedekindDomains

class MyFGModules(Category_module):
    def __init__(self, base):
        if not (base in DedekindDomains() or
                isinstance(base, Category) and base.is_subcategory(DedekindDomains())):
            raise ValueError("base must be a Dedekind domain")
        Category_module.__init__(self, base)
```

You can also pass `DedekindDomains()` itself as the base for the generic version:

```python
MyFGModules(DedekindDomains())   # generic: all fg modules over any Dedekind domain
MyFGModules(ZZ)                   # specific: ZZ-modules (ZZ is a Dedekind domain)
```

The `_subcategory_hook_` in `Category_over_base_ring` handles the containment check
`MyFGModules(ZZ).is_subcategory(MyFGModules(DedekindDomains()))` automatically.

For a PID-restricted version, substitute `PrincipalIdealDomains()`.
`PrincipalIdealDomains` is a `Category_singleton` (not a `Category`), so the
`isinstance(base, Category)` branch handles it correctly.

## 7. The full structural picture

```python
class Homsets(HomsetsCategory):
    def extra_super_categories(self):
        # Hom_R(M, N) is itself a finitely generated R-module
        # (over a Dedekind domain, Hom of fg modules is fg)
        return [MyFGModules(self.base_category().base_ring())
                .FinitelyPresented()]

    class ParentMethods:
        @cached_method
        def base_ring(self):
            return self.domain().base_ring()

        @cached_method
        def zero(self):
            return self.domain().hom(
                [self.codomain().zero()] * self.domain().ngens(),
                self.codomain())

    class Endset(CategoryWithAxiom_over_base_ring):
        def extra_super_categories(self):
            # End_R(M) is an R-algebra
            from sage.categories.algebras import Algebras
            return [Algebras(self.base_category().base_ring())]

        class Autset(CategoryWithAxiom):
            def extra_super_categories(self):
                # Aut_R(M) is the group of units of End_R(M)
                from sage.categories.groups import Groups
                return [Groups()]

class DualObjects(DualObjectsCategory):
    @cached_method
    def extra_super_categories(self):
        # M* = Hom_R(M, R) is a finitely generated R-module
        return [MyFGModules(self.base_category().base_ring())
                .FinitelyPresented()]
```

The `Homsets.extra_super_categories` returning `[MyFGModules(R).FinitelyPresented()]` is
the key structural fact.
It makes `Hom_R(M, N)` a parent in `MyFGModules(R).FinitelyPresented()`. The framework
then builds a dynamic element class that inherits from both `Morphism` and
`MyFGModules(R).FinitelyPresented().element_class` — so every morphism `f: M → N`
simultaneously has `MorphismMethods` (kernel, image, cokernel) and `ElementMethods` from
`MyFGModules(R)` (lmul, rmul).
This is automatic, no extra code needed.

The existing `Modules.Homsets.extra_super_categories` and
`Modules.Homsets.Endset.extra_super_categories` are the direct precedents:

**File:** `src/sage/categories/modules.py` (L728-735) **File:**
`src/sage/categories/modules.py` (L813-833)

The `DualObjects` pattern is taken from `ModulesWithBasis.DualObjects`:

**File:** `src/sage/categories/modules_with_basis.py` (L2776-2789)

## Corrected axiom hierarchy

```
MyFGModules(R)                    [R ∈ DedekindDomains()]
├── super_categories: [Modules(R)]
├── is_abelian: True (inherited from Category_module → AbelianCategory)
├── additional_structure: None
│
├── MorphismMethods: kernel(), image(), cokernel()
│
├── Homsets:
│   ├── extra_super_categories → [MyFGModules(R).FinitelyPresented()]
│   ├── ParentMethods: base_ring(), zero()
│   └── Endset:
│       ├── extra_super_categories → [Algebras(R)]
│       └── Autset:
│           └── extra_super_categories → [Groups()]
│
├── DualObjects:
│   └── extra_super_categories → [MyFGModules(R).FinitelyPresented()]
│
├── WithGenerators (new axiom):
│   └── ParentMethods: module_generators()†, gens(), ngens(), gen(i), hom()†
│
├── FinitelyPresented (existing axiom):
│   └── extra_super_categories → [MyFGModules(R).WithGenerators()]
│
├── Projective (new axiom):
│   └── ParentMethods: steinitz_class()†
│       (rank() is NOT here)
│
├── Torsion (new axiom):
│   └── ParentMethods: annihilator()†, invariant_factors()†
│       (no rank(), no is_torsion() based on rank)
│
└── Free (new axiom):
    └── ParentMethods: rank()†, basis()†
        (rank is primary here only)

† = @abstract_method
```

### Former `plans/category_creation_notes.md`

# Category Creation: Base Rings and Module Categories

There are three interlocking mechanisms to understand here.

## 1. `_refine_category_` — enrolling existing objects

`_refine_category_` is the proper non-monkey-patching way to add `ZZ`, `QQ`, `Zp`, etc.
to a new category. It computes the join of the object's current category with the new
one, and for Python-based parents also updates the dynamic class:

```python
# At import time in your package:
ZZ._refine_category_(ModuleBaseRings())
QQ._refine_category_(ModuleBaseRings())
```

After this, `ZZ in ModuleBaseRings()` is `True`, and methods from
`ModuleBaseRings.ParentMethods` become accessible.

**Important caveat for Cython types:** `ZZ` is a Cython extension type
(`IntegerRing_class`), so `can_assign_class(ZZ)` is `False` — `_refine_category_`
updates `ZZ._category` but does NOT replace `ZZ.__class__` with a dynamic subclass.
Methods from `ParentMethods` are still reachable via `__getattr__` →
`getattr_from_category`, which looks up `self.category().parent_class`. `QQ` (a Python
class `RationalField_with_category`) gets its class replaced directly.

## 2. Defining `ModuleBaseRings` as a `Category_singleton`

```python
from sage.categories.category_singleton import Category_singleton
from sage.categories.rings import Rings

class ModuleBaseRings(Category_singleton):
    """Rings that are valid base rings for MyModules."""
    def super_categories(self):
        return [Rings()]

    class ParentMethods:
        def my_new_ring_method(self):
            ...
```

Use `Category_singleton` (not plain `Category`) for the `x in ModuleBaseRings()`
containment check to be fast — it uses a Cython `isinstance` check on the parent class
rather than traversing the category graph.

## 3. Defining `MyModules(R)` as a `Category_over_base_ring`

```python
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category import Category

class MyModules(Category_over_base_ring):
    def __init__(self, base):
        if not (base in ModuleBaseRings() or
                isinstance(base, Category) and base.is_subcategory(ModuleBaseRings())):
            raise ValueError("base must be in ModuleBaseRings()")
        Category_over_base_ring.__init__(self, base)

    def super_categories(self):
        from sage.categories.modules import Modules
        return [Modules(self.base_ring())]

    class ParentMethods:
        ...
```

The `__init__` of `Category_over_base_ring` only checks `base in Rings()`.

You override it to check `base in ModuleBaseRings()` instead.

## The `_make_named_class_key` implication

`Category_over_base._make_named_class_key` returns `self.__base.category()` when the
base is a parent:

This means `MyModules(ZZ).parent_class` depends on `ZZ.category()`. If you call
`ZZ._refine_category_(ModuleBaseRings())` **after** `MyModules(ZZ)` has been
constructed, the cached `parent_class` could be stale.
The framework detects this and recomputes.

So you should call `_refine_category_` on all your base rings **before** constructing
any `MyModules(R)` instances — i.e., at package import time.

## Passing a category as base

You can also pass `ModuleBaseRings()` itself as the base:

```python
MyModules(ModuleBaseRings())   # generic: all modules over any ModuleBaseRing
MyModules(ZZ)                   # specific: ZZ-modules
```

The `_subcategory_hook_` in `Category_over_base_ring` handles this:
`MyModules(ZZ).is_subcategory(MyModules(ModuleBaseRings()))` returns `True` if
`ZZ in ModuleBaseRings()`.

This is the same pattern used by `VectorSpaces(Fields())` vs `VectorSpaces(QQ)`.

## Summary of the full pattern

```python
# 1. Define the base ring category
class ModuleBaseRings(Category_singleton):
    super_categories → [Rings()]
    ParentMethods → new methods on ZZ, QQ, etc.

# 2. Enroll specific rings at import time
ZZ._refine_category_(ModuleBaseRings())
QQ._refine_category_(ModuleBaseRings())
Zp(p)._refine_category_(ModuleBaseRings())  # for each p you care about

# 3. Define the module category
class MyModules(Category_over_base_ring):
    __init__ → validates base in ModuleBaseRings()
    super_categories → [Modules(self.base_ring())]
    ParentMethods → new methods on modules
```

The `_refine_category_` calls are the only "mutation" of existing Sage objects, and they
are explicitly supported by the framework — the same mechanism is used internally (e.g.,
`_is_Field` calls `x._refine_category_(_Fields)` on rings that turn out to be fields).

### Citations

**File:** src/sage/structure/parent.pyx (L345-438)
```text
    def _refine_category_(self, category):
        """
        Change the category of ``self`` into a subcategory.

        INPUT:

        - ``category`` -- a category or list or tuple thereof

        The new category is obtained by adjoining ``category`` to the
        current one.

        .. NOTE::

            The class of ``self`` might be replaced by a sub-class.

        .. SEEALSO::

            :meth:`CategoryObject._refine_category`

        EXAMPLES::

            sage: P.<x,y> = QQ[]
            sage: Q = P.quotient(x^2 + 2)
            sage: Q.category()
            Join of
             Category of commutative rings and
             Category of subquotients of monoids and
             Category of quotients of semigroups
            sage: first_class = Q.__class__
            sage: Q._refine_category_(Fields())
            sage: Q.category()
            Join of
             Category of fields and
             Category of subquotients of monoids and
             Category of quotients of semigroups
            sage: first_class == Q.__class__
            False
            sage: TestSuite(Q).run()                                                    # needs sage.libs.singular

        TESTS:

        Here is a test against :issue:`14471`. Refining the category will issue
        a warning, if this change affects the hash value (note that this will
        only be seen in doctest mode)::

            sage: class MyParent(Parent):
            ....:     def __hash__(self):
            ....:         return hash(type(self))   # subtle mistake
            sage: a = MyParent()
            sage: h_a = hash(a)
            sage: a._refine_category_(Algebras(QQ))
            hash of <class '__main__.MyParent_with_category'> changed in
            Parent._refine_category_ during initialisation

            sage: b = MyParent(category=Rings())
            sage: h_b = hash(b)
            sage: h_a == h_b
            False
            sage: b._refine_category_(Algebras(QQ))
            hash of <class '__main__.MyParent_with_category'> changed in
            Parent._refine_category_ during refinement
            sage: hash(a) == hash(b)
            True
            sage: hash(a) != h_a
            True
        """
        cdef Py_hash_t hash_old = -1
        if debug.refine_category_hash_check:
            # check that the hash stays the same after refinement
            hash_old = hash(self)

        if self._category is None:
            self._init_category_(category)
            if hash_old != -1 and hash_old != hash(self):
                print(f'hash of {type(self)} changed in Parent._refine_category_ during initialisation')
            return
        if category is self._category:
            return
        CategoryObject._refine_category_(self, category)
        category = self._category

        # This substitutes the class of this parent to a subclass
        # which also subclasses the parent_class of the category.
        # However, we only do so if we do not have an extension class.
        if can_assign_class(self):
            # We tested in the very beginning that this parent
            # had its category initialised. Hence, the class
            # is already a dynamic class.
            base = self.__class__.__base__
            # documentation transfer is handled by dynamic_class
            self.__class__ = dynamic_class(
                "%s_with_category" % base.__name__,
                (base, category.parent_class),
                doccls=base)
```

**File:** src/sage/structure/category_object.pyx (L244-257)
```text
            sage: type(QQ)
            <class 'sage.rings.rational_field.RationalField_with_category'>
            sage: QQ._underlying_class()
            <class 'sage.rings.rational_field.RationalField'>
            sage: type(ZZ)
            <... 'sage.rings.integer_ring.IntegerRing_class'>
            sage: ZZ._underlying_class()
            <... 'sage.rings.integer_ring.IntegerRing_class'>
        """
        cls = type(self)
        if isinstance(cls, DynamicMetaclass):
            return cls.__bases__[0]
        else:
            return cls
```

**File:** src/sage/categories/category_singleton.pyx (L83-145)
```text
class Category_singleton(Category):
    """
    A base class for implementing singleton category.

    A *singleton* category is a category whose class takes no
    parameters like ``Fields()`` or ``Rings()``. See also the
    :wikipedia:`Singleton design pattern <Singleton_pattern>`.

    This is a subclass of :class:`Category`, with a couple
    optimizations for singleton categories.

    The main purpose is to make the idioms::

        sage: QQ in Fields()
        True
        sage: ZZ in Fields()
        False

    as fast as possible, and in particular competitive to calling a
    constant Python method, in order to foster its systematic use
    throughout the Sage library. Such tests are time critical, in
    particular when creating a lot of polynomial rings over small
    fields like in the elliptic curve code.

    EXAMPLES::

        sage: from sage.categories.category_singleton import Category_singleton
        sage: class MyRings(Category):
        ....:     def super_categories(self): return Rings().super_categories()
        sage: class MyRingsSingleton(Category_singleton):
        ....:     def super_categories(self): return Rings().super_categories()

    We create three rings. One of them is contained in the usual category of
    rings, one in the category of "my rings" and the third in the category of
    "my rings singleton"::

        sage: R = QQ['x,y']
        sage: R1 = Parent(category = MyRings())
        sage: R2 = Parent(category = MyRingsSingleton())
        sage: R in MyRings()
        False
        sage: R1 in MyRings()
        True
        sage: R1 in MyRingsSingleton()
        False
        sage: R2 in MyRings()
        False
        sage: R2 in MyRingsSingleton()
        True

    One sees that containment tests for the singleton class is a lot faster
    than for a usual class::

        sage: # not tested
        sage: timeit("R in MyRings()", number=10000)
        10000 loops, best of 3: 7.12 µs per loop
        sage: timeit("R1 in MyRings()", number=10000)
        10000 loops, best of 3: 6.98 µs per loop
        sage: timeit("R in MyRingsSingleton()", number=10000)
        10000 loops, best of 3: 3.08 µs per loop
        sage: timeit("R2 in MyRingsSingleton()", number=10000)
        10000 loops, best of 3: 2.99 µs per loop
```

**File:** src/sage/categories/category_types.py (L215-251)
```python
    def _make_named_class_key(self, name):
        r"""
        Return what the element/parent/... classes depend on.

        Since :issue:`11935`, the element and parent classes of a
        category over base only depend on the category of the base (or
        the base itself if it is a category).

        .. SEEALSO::

            - :meth:`CategoryWithParameters`
            - :meth:`CategoryWithParameters._make_named_class_key`

        EXAMPLES::

            sage: Modules(ZZ)._make_named_class_key('element_class')
            Join of Category of Dedekind domains
             and Category of euclidean domains
             and Category of noetherian rings
             and Category of infinite enumerated sets
             and Category of metric spaces
            sage: Modules(QQ)._make_named_class_key('parent_class')
            Join of Category of number fields
             and Category of quotient fields
             and Category of metric spaces
            sage: Schemes(Spec(ZZ))._make_named_class_key('parent_class')
            Category of schemes
            sage: ModularAbelianVarieties(QQ)._make_named_class_key('parent_class')
            Join of Category of number fields
             and Category of quotient fields
             and Category of metric spaces
            sage: Algebras(Fields())._make_named_class_key('morphism_class')
            Category of fields
        """
        if isinstance(self.__base, Category):
            return self.__base
        return self.__base.category()
```

**File:** src/sage/categories/category_types.py (L347-362)
```python
class Category_over_base_ring(Category_over_base):
    def __init__(self, base, name=None):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = Algebras(GF(2)); C
            Category of algebras over Finite Field of size 2
            sage: TestSuite(C).run()
        """
        from sage.categories.rings import Rings
        if not (base in Rings() or
                isinstance(base, Category) and base.is_subcategory(Rings())):
            raise ValueError("base must be a ring or a subcategory of Rings()")
        Category_over_base.__init__(self, base, name)
```

**File:** src/sage/categories/category_types.py (L480-492)
```python
        if not issubclass(C.parent_class, self.parent_class):
            return False
        if not isinstance(C, Category_over_base_ring):
            return Unknown
        base_ring = self.base_ring()
        if C.base_ring() is base_ring:
            return True
        if isinstance(base_ring, Category):
            if isinstance(C.base(), Category):
                return C.base().is_subcategory(base_ring)
            # otherwise, C.base() is a parent
            return C.base() in base_ring
        return False
```

**File:** src/sage/categories/category.py (L2836-2851)
```python
        """
        cls = self.__class__
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        key = (cls, name, self._make_named_class_key(name))
        try:
            return self._make_named_class_cache[key]
        except KeyError:
            pass
        result = Category._make_named_class(self, name, method_provider,
                                            cache=cache, **options)
        if key[2] != self._make_named_class_key(name):
            # the object in the parameter may have had its category refined, which might modify the key
            # throw result away and recompute
            return self._make_named_class(name, method_provider, cache=cache, **options)
        self._make_named_class_cache[key] = result
```

**File:** src/sage/rings/ring.pyx (L650-658)
```text
    # The result is not immediately returned, since we want to refine
    # x's category, so that calling x in Fields() will be faster next time.
    try:
        result = isinstance(x, Field) or x.is_field()
    except AttributeError:
        result = False
    if result:
        x._refine_category_(_Fields)
    return result
```

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Plan-Card Review)

**Reviewer:** Hermes Agent (subagent, delegated review)
**Scope:** Plan card `PLAN-CATEGORY-FOUNDATION-KERNEL`; child phase/task existence verified but not re-reviewed.
**Gates passed:** G4, G6
**Gates conditional:** G1, G2, G3, G5
**Gates failed:** None that block plan execution

---

#### G1 — Source Paths Grounded: CONDITIONAL PASS

**Findings:**

- The "Admitted Definitions" section (lines 70-90) grounds four key definitions in specific, verifiable source documents:
  - `category_specs/cat/docs/MAPPING.md` — **exists** ✓
  - `category_specs/homsets/docs/MAPPING.md` — **exists** ✓
  - `category_specs/modules/docs/MAPPING.md` — **exists** ✓
- The "Migrated Source Bodies" section (lines 130-785) contains extensive Sage source code references with exact file paths and line numbers, all verifiable in the Sage codebase ✓
- The `theory/references/index.md` path cited in the Definition Grounding Requirements (line 66) references a theory corpus outside the immediate plan tree; not verified but consistent with project conventions ✓

**Conditions:**

1. **Source corpus ambiguity (lines 94-99):** The plan lists five files under "Source corpus" (`plans/CATEGORY_ABC_SPEC.md`, `plans/CATEGORY_REFINEMENT_PHASES.md`, `plans/axioms_with_generators_finitely_presented.md`, `plans/category_creation_notes.md`, `plans/homsets_structural_core.md`). None of these files exist as standalone documents — their content has been migrated inline into this plan's "Migrated Source Bodies" section. The `category_creation_notes.md` and `axioms_with_generators_finitely_presented.md` bodies are explicitly labeled as "Former" documents in the migrated section (lines 132-133, 367). However, the other three (`CATEGORY_ABC_SPEC.md`, `CATEGORY_REFINEMENT_PHASES.md`, `homsets_structural_core.md`) are listed in the source corpus without corresponding inline migrated bodies. **Recommendation:** Either add inline migrated bodies for these three files, or annotate them as "migrated to `<target>`" with the actual migration destinations. The "Deleted source holder" annotation on `plans/todo.md` (line 99) is the correct pattern to follow.

2. **Minor:** The Definition Grounding Requirements section (line 66) references `theory/references/index.md` without specifying whether this is a repo-relative or absolute path. In practice the project root is `/home/dzack/research`, so the full path would be `/home/dzack/research/theory/references/index.md`.

**G1 verdict:** PASS with documentation cleanup recommended. The plan has strong grounding for its admitted definitions; the source corpus section needs migration-status annotations.

---

#### G2 — Exit Criteria Checkable: CONDITIONAL PASS

**Findings:**

All six success criteria (YAML `successCriteria`, lines 15-21) and six acceptance criteria checkboxes (lines 121-127) are evaluated for measurability:

| # | Criterion | Verdict | Notes |
|---|-----------|---------|-------|
| 1 | Dual objects reconciled with Homset routing before discriminant work | **Conditional** | "Reconciled" is vague. What artifact signals completion? A spec update? A test? A decision card? No reconciliation standard is defined. |
| 2 | Method ownership moved to most general mathematically valid category | **Conditional** | No measurable end-state. Is the inventory spec completion the signal? The phase PHASE-CATEGORY-LITERAL-METHOD-INVENTORY is complete, but the criterion doesn't reference it. |
| 3 | Method ownership changes preserve ideal mathematical surface; failed category assertion not treated as negative evidence | **Partially checkable** | The policy portion is checkable as a gate during review. The "preserve ideal surface" part requires a reference surface to compare against. |
| 4 | Standard type aliases live in one canonical package | **Checkable** ✓ | Can verify by checking that all type aliases route through a single package. |
| 5 | TwistedForms admitted or rejected by decision card | **Checkable** ✓ | Binary: decision card exists or it doesn't. |
| 6 | Constructor-interception work does not precede static hierarchy and method-surface review | **Checkable** ✓ | Ordering constraint verifiable from status fields. |

**Conditions:**

1. Criteria 1 and 2 need concrete completion artifacts specified. For criterion 1, the plan should state what "reconciled" means (e.g., "dual-object routing passes Homset shadowing category-obligation test" or "dual-object spec row is filled in SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY"). For criterion 2, the plan should link to the inventory spec as the measurable completion signal.

2. The YAML `successCriteria` (5 items) and body "Acceptance Criteria" checkboxes (6 items) overlap but are not identical. The YAML has: dual-object reconciliation, method-ownership movement, type aliases, TwistedForms, and constructor-interception ordering (5 items). The body adds criterion 3 about preserving the ideal mathematical surface (not in YAML) and splits method-ownership into two criteria (movement + preservation). The body also drops the explicit "TwistedForms" criterion from its checklist — it appears in YAML but not in the checkbox list. **Recommendation:** Align the YAML and body checklists for consistency.

**G2 verdict:** PASS with documentation refinements needed. Four of six criteria are clearly checkable; two need measurable completion signals defined.

---

#### G3 — Phase Inventory Complete: CONDITIONAL PASS

**Findings:**

The YAML `phases` field (lines 23-25) declares three child phases:

| # | Phase ID | Status | Exists |
|---|----------|--------|--------|
| 1 | PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION | `complete` | ✓ |
| 2 | PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE | `in-progress` | ✓ |
| 3 | PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP | `complete` | ✓ |

All three phase cards exist at expected paths and correctly reference this plan as parent ✓.

The "Subplans" section (lines 101-108) references three additional plans:

| # | Plan ID | Location | Status |
|---|---------|----------|--------|
| 1 | PLAN-STATIC-CATEGORY-REFINEMENT-ORDER | Under FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES | `needs-agent-review` |
| 2 | PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION | Under FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES | `needs-agent-review` |
| 3 | PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP | Under FEATURE-MODULES-WITH-FORMS-AND-LATTICES | `approved-and-unstarted` |

**Coverage gaps identified:**

1. **Standard type aliases canonical package (exit criterion 4):** No top-level phase in this plan explicitly owns type alias consolidation. The work is partially covered by TASK-1777748120881 under PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION, but the plan does not declare a phase that delivers "one canonical package" as a completion artifact. The criterion is orphaned at the plan level.

2. **Module axioms (WithGenerators, FinitelyPresented, etc.):** Extensively described in the migrated source body (lines 134-365), but no phase card explicitly owns axiom registration, implementation, or verification against the spec. This work may be implicitly covered by PHASE-MODULE-WRAPPER-MIGRATION (which handles "category graph constructor routing") but the phase's description and success criteria do not mention axioms.

3. **TwistedForms admission/rejection (exit criterion 5):** The plan exit criteria require a decision on TwistedForms, but no phase or subplan owns this decision. It's unclear whether this is a blocking prerequisite for the kernel or a deferred downstream item.

4. **Phase ordering not specified:** The phases have no declared ordering or dependency. PHASE 1 and PHASE 3 are `complete` while PHASE 2 is `in-progress`, suggesting they can run in parallel, but the plan doesn't state this explicitly.

**G3 verdict:** PASS with three coverage gaps. The phase inventory covers the core work (Cat surface, module wrappers, method inventory) but leaves three exit criteria (type aliases, module axioms, TwistedForms) without explicit phase-level owners.

---

#### G4 — Scope Containment: PASS

**Findings:**

- The plan's stated objective (line 33) matches the declared phases and subplans: "category refinement order, module axioms, Hom/End/Aut structure, dual-object routing, standard type aliases, and method ownership" ✓
- The "Dependency rule" (lines 115-117) correctly gates this plan as a blocker for downstream implementation, consistent with its "foundation kernel" role ✓
- The "Definition Grounding Requirements" (lines 36-68) and "Admitted Definitions" (lines 70-90) properly constrain child work to stay within grounded mathematical territory ✓
- The "Leaf ownership" section (lines 110-113) correctly routes executable work to leaf subplans, preventing scope expansion at the plan level ✓
- The migrated source bodies (lines 130-785) are long but provide necessary definitional grounding for the axioms and category creation patterns that child phases will implement. They do not constitute implementation themselves — they are reference material ✓
- The plan explicitly blocks construction-interception and discriminant work until vocabulary is settled (success criteria 6), reinforcing scope gating ✓
- No implementation work is authorized by this plan directly; it only coordinates spec and review work ✓

**G4 verdict:** PASS. The plan is well-contained within its foundation-kernel scope and properly gates downstream work.

---

#### G5 — Dependency Correctness: CONDITIONAL PASS

**Findings:**

- **Parent relationship:** `parents: ['[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]']` — **correct** ✓. The feature card's `plans` list includes this plan ✓.
- **dependsOn:** `[]` — **correct** for a foundation kernel that should block others, not be blocked ✓.
- **Phase parent references:** All three child phases correctly set `parents: ['[[PLAN-CATEGORY-FOUNDATION-KERNEL]]']` ✓.
- **No circular dependencies detected** ✓.

**Conditions:**

1. **Subplan parent inconsistency:** PLAN-STATIC-CATEGORY-REFINEMENT-ORDER and PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION are listed as subplans in this card's body (lines 103-104), but their YAML `parents` field points directly to `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, not to this plan. This creates ambiguity:
   - If they are children of this plan, their `parents` should include `PLAN-CATEGORY-FOUNDATION-KERNEL`.
   - If they are siblings under the feature (as their YAML declares), they should not be listed as subplans here. They should instead be referenced as sibling plans that this kernel coordinates with.
   - **Recommendation:** Decide on the containment relationship and make the YAML and body references consistent. The "Leaf ownership" section (which routes Hom/End/Aut work to PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION) suggests a sibling/coordination relationship rather than strict containment.

2. **Cross-feature reference:** PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP lives under a different feature (`FEATURE-MODULES-WITH-FORMS-AND-LATTICES`), which is appropriate since it's a dependent downstream plan consuming the kernel's vocabulary. Its success criteria explicitly cite this plan as a prerequisite ("Category vocabulary and method ownership from PLAN-CATEGORY-FOUNDATION-KERNEL are settled before dependent implementation") ✓.

3. **Phase dependency declaration missing:** The plan does not declare whether the three phases must run sequentially or can run in parallel. Current status shows PHASE 1 (complete), PHASE 2 (in-progress), PHASE 3 (complete) — suggesting they are independent. If any ordering constraints exist, the plan should state them.

**G5 verdict:** PASS with one structural inconsistency to resolve (subplan parent references).

---

#### G6 — Preservation: PASS

**Findings:**

- **Spec-weakening review gate (lines 52-56):** Every child phase must include a gate that reviews staged/unstaged diffs and commits for deleted abstract methods, removed constructor/category obligations, narrowed category-obligation examples, or obligation moves without replacement owners. A category-obligation example improvement paired with interface shrinkage fails the gate ✓. This is a strong preservation mechanism.
- **Mathematical review gate (lines 58-62):** Every child phase must include a gate for method-owner rows written as coherent mathematical claims before implementation work changes ownership or surfaces ✓.
- **Sage interop as design constraint (lines 44-47):** The plan explicitly states that Sage interop is a design constraint where mathematically appropriate, and that Sage inventory is implementation evidence and a feasibility witness ✓.
- **No destructive operations:** The plan coordinates spec work and method ownership; it does not authorize deletion of existing functionality. The preservation gates ensure that any changes maintain or improve the mathematical surface ✓.
- **Source corpus preservation:** The plan preserves content from five deleted/migrated source documents (axioms, category creation notes, etc.) by inlining their bodies rather than losing them ✓.
- **Category spec philosophy alignment:** The plan aligns with `category_specs/AGENTS.md` directives: ideal mathematical interface is the standard, Sage coverage is not the adequacy standard, failed category assertions are implementation evidence not spec-weakening evidence ✓.

**G6 verdict:** PASS. The plan has strong preservation mechanisms through mandatory review gates and explicit non-destructive policies.

---

### Summary

| Gate | Verdict | Issues |
|------|---------|--------|
| G1 — Source Grounding | CONDITIONAL PASS | Source corpus files need migration-status annotations; 3 of 5 lack inline migrated bodies |
| G2 — Exit Criteria | CONDITIONAL PASS | Criteria 1 and 2 need measurable completion signals; YAML/body checklist misaligned |
| G3 — Phase Inventory | CONDITIONAL PASS | Type aliases, module axioms, and TwistedForms lack explicit phase owners |
| G4 — Scope | PASS | Well-contained foundation kernel |
| G5 — Dependencies | CONDITIONAL PASS | Subplan parent references inconsistent with YAML; phase ordering undeclared |
| G6 — Preservation | PASS | Strong review gates and non-destructive policies |

**Overall assessment:** The plan is structurally sound and ready to coordinate child work. The four conditional gates reflect documentation precision issues, not plan design flaws. Recommended actions: (1) annotate source corpus files with migration status, (2) define measurable completion signals for vague exit criteria, (3) assign explicit phase owners to orphaned criteria (type aliases, axioms, TwistedForms), and (4) resolve the subplan parent inconsistency.
