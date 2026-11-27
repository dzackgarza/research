---
id: PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Hom End Aut structural admission
status: complete
priority: critical
owner: Zack
description: Admit Homsets, Endsets, Autsets, dual objects, and automorphism groups
  through the category framework instead of ad hoc group or ConditionSet surfaces.
successCriteria:
- '`Aut(X)` and `End(X)` are category-recognized surfaces, not isolated helper factories.'
- Automorphism groups have domain/codomain semantics and categorical coercion to End.
- Public APIs return project-owned aut/subobject surfaces; Sage `ConditionSet` remains
  an implementation bridge only.
phases:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Hom End Aut structural admission

## Objective

Admit Homsets, Endsets, Autsets, dual objects, and automorphism groups through the category framework instead of ad hoc group or ConditionSet surfaces.


## Grounded Implementation Contract

Source anchors for this plan:

- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/MAPPING.md`

The structural admission target for this plan is:

- `C.HomCategory().Of(A, B)` is `Hom_C(A, B)` with `domain`, `codomain`, construction,
  containment, and composition owned by the hom-category hierarchy.
- `C.EndCategory().Of(A)` is `End_C(A) = Hom_C(A, A)`; it is the endomorphism monoid
  carried by the same hom-object semantics, with extra algebra structure only where the
  module mapping admits it.
- `C.AutCategory().Of(A)` is the invertible part of `End_C(A)`; it is a project-owned
  aut object whose elements are endomorphisms with `inverse()` and other aut predicates.
- `AutCategory.from_end_category` may use Sage `ConditionSet` internally, but the public
  object returned on the category-spec surface is the project aut/subobject object.
- For formed modules and lattices, `Aut(M, b)` is the orthogonal-group surface because
  form-preserving automorphisms are exactly the invertible endomorphisms in the forms
  category.

Matrix, function, and predicate calculations remain implementation evidence only after
the categorical Hom/End/Aut parent and element meanings above are fixed.

## Admitted Definitions

Hom/End/Aut child cards may use these definitions without re-deriving them:

- `C.HomCategory().Of(A, B)` is the hom object `Hom_C(A, B)` for objects `A, B` of
  `C`; it owns `domain`, `codomain`, identity/zero where valid, and morphism
  construction/containment for the category. Source:
  `category_specs/homsets/docs/MAPPING.md`.
- `C.EndCategory().Of(A)` is `End_C(A) = Hom_C(A, A)`. Domain and codomain are already
  the generic hom-object methods, so subtree aliases such as `base_set()` or
  `base_space()` are migration conveniences, not new definitions. Source:
  `category_specs/homsets/docs/MAPPING.md`.
- `C.AutCategory().Of(A)` is the invertible part of `End_C(A)`. The generic aut
  construction is a project extension over Sage's audited generic homset surface;
  child work must not duplicate aut construction with raw `ConditionSet` surfaces.
  Source: `category_specs/homsets/docs/MAPPING.md`.
- For modules, `Hom_R(M,N)` carries `R`-module structure, and `End_R(M)` carries
  algebra structure where the module mapping doc admits it. For formed modules,
  orthogonal groups are `Aut(M,b)` in the category of modules with forms. Sources:
  `category_specs/modules/docs/MAPPING.md`, `category_specs/forms/docs/MAPPING.md`,
  `category_specs/lattices/docs/MAPPING.md`.

## Source corpus

- `plans/homsets_structural_core.md`
- `plans/autset_categories_path.md`
- `plans/autset_integration_plan.md`
- `plans/axioms_with_generators_finitely_presented.md`
- Deleted source holder: `plans/todo.md`

## Structural target

- Homsets carry module structure where mathematically valid.
- Endsets are endomorphism monoids and can specialize to algebra objects.
- Autsets are invertible endomorphism subsets with group structure.
- Dual objects are connected to Homsets when `M* = Hom_R(M, R)` is the mathematical meaning.
- Public category surfaces do not expose raw `ConditionSet` as the final API.

## Owned existing cards

- `spec_01KQN9J3WJE9W76X72DAT10H4Y`: dual-object Hom routing and method ownership.
- `spec_01KQN9J3WQDJ0Z27BXTY67HA72`: DiscriminantGroup Hom/End/Aut standard names.
- `task_1777748120385_rrvdig`: remove raw ConditionSet from public Aut-category surface.

## Acceptance Criteria

- [ ] `Aut(X)` and `End(X)` are category-recognized surfaces, not isolated helper factories.
- [ ] Automorphism groups have domain/codomain semantics and categorical coercion to End.
- [ ] Public APIs return project-owned aut/subobject surfaces; Sage `ConditionSet` remains an implementation bridge only.


## Migrated Source Bodies

### Former `plans/homsets_structural_core.md`

# Homsets — the Structural Core

This is where the key relationships live:

```python
class Homsets(HomsetsCategory):

    def extra_super_categories(self):
        # Hom_R(M, N) is itself a finitely generated R-module
        return [MyFGModules(self.base_category().base_ring())]

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
```

## Pattern Parallels

The `extra_super_categories` on `Homsets` is the same pattern as `Modules.Homsets`:

**File:** `src/sage/categories/modules.py` (L728-735)
```python
    def extra_super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.homsets import Homsets
            sage: from sage.categories.modules import Modules
            sage: Homsets(Modules(ZZ)).extra_super_categories()
            [Category of modules over Integer Ring]
        """
        return [self.base_category()]
```

The `Endset.extra_super_categories` mirrors `Modules.Homsets.Endset`:

**File:** `src/sage/categories/modules.py` (L813-833)
```python
        class Endset(CategoryWithAxiom_over_base_ring):
            """
            The category of endomorphism sets `End(X)` for `X`
            a module (this is not used yet)
            """
            def extra_super_categories(self):
                """
                Implement the fact that the endomorphism set of a module is an algebra.

                .. SEEALSO:: :meth:`CategoryWithAxiom.extra_super_categories`

                EXAMPLES::

                    sage: Modules(ZZ).Endsets().extra_super_categories()
                    [Category of magmatic algebras over Integer Ring]

                    sage: End(ZZ^3) in Algebras(ZZ)                                     # needs sage.modules
                    True
                """
                from .magmatic_algebras import MagmaticAlgebras
                return [MagmaticAlgebras(self.base_category().base_ring())]
```

The `Autset` layer is the new piece (discussed in the earlier conversation about autset
categories).

* * *

## Why Elements of Hom Sets Are Also Module Elements

When `Homsets.extra_super_categories()` returns `[MyFGModules(R)]`, the homset
`Hom_R(M, N)` is a parent in `MyFGModules(R)`. The framework builds a dynamic element
class that inherits from both `Morphism` and `MyFGModules(R).element_class`.

So every morphism `f: M → N` simultaneously has:

- `MorphismMethods` (`kernel`, `image`, `cokernel`)
- `ElementMethods` from `MyFGModules(R)` (`lmul`, `rmul`, `additive_order`)

This is automatic — no extra code needed.

* * *

## DualObjects — Dual Modules

```python
class DualObjects(DualObjectsCategory):
    def extra_super_categories(self):
        # M* = Hom_R(M, R) is a finitely generated R-module
        return [MyFGModules(self.base_category().base_ring())]
```

This mirrors `ModulesWithBasis.DualObjects`:

**File:** `src/sage/categories/modules_with_basis.py` (L2776-2789)
```python
class DualObjects(DualObjectsCategory):
    def extra_super_categories(self):
        """
        Return the category of modules over the base ring.

        EXAMPLES::

            sage: from sage.categories.modules_with_basis import ModulesWithBasis
            sage: ModulesWithBasis(ZZ).DualObjects().extra_super_categories()
            [Category of modules over Integer Ring]
        """
        return [self.base_category()]
```

The dual `M* = Hom_R(M, R)` is simultaneously:

1. A parent in `MyFGModules(R).DualObjects()` (it is a dual object)
2. A parent in `MyFGModules(R)` (it is a finitely generated R-module)
3. A homset `Hom_R(M, R)` (its elements are morphisms `M → R`)

Its elements are simultaneously morphisms `M → R` and elements of the R-module `M*`.
This triple nature is captured entirely by the category framework through the
`extra_super_categories` chain — no ad-hoc code.

* * *

## Rank of Projective Modules over Integral Domains

The rank is a **function** on `Spec(R)` defined by:

```
rank_p(M) := dim_{k(p)}(M ⊗_R k(p))
```

where `k(p) := Frac(R/p)` is the residue field at the prime `p`.

For a **finitely generated projective** module over a **Dedekind domain**:
- The rank function is **locally constant** on `Spec(R)`
- The rank is **finite** at every point

When `R` is an **integral domain**, `Spec(R)` is connected, so the locally constant rank
function is actually **globally constant**. This yields a well-defined number
`rank_R(M) = dim_K(M ⊗_R K)` where `K = Frac(R)`.

This is the generic rank of the associated coherent sheaf `M̃` on `Spec(R)` — the
dimension of the fiber at the generic point.

```python
class ParentMethods:
    @cached_method
    def rank(self):
        """
        Return the rank of ``self``.

        For a finitely generated projective module over a Dedekind domain,
        this returns the locally constant rank function on Spec(R).
        When R is an integral domain, this is a single integer.

        EXAMPLES::
            sage: R = ZZ
            sage: M = MyFGModule(R, 3)  # rank 3 projective module
            sage: M.rank()
            3
        """
        R = self.base_ring()
        if R in PrincipalIdealDomains() or R in DedekindDomains():
            K = R.fraction_field()
            return self.change_ring(K).dimension()
        # Otherwise return the rank function on Spec(R)
        return RankFunction(self)
```

### Former `plans/autset_categories_path.md`

# How Endset Categories Are Constructed

The endset machinery is built on three interlocking pieces:

**1. The axiom registration.** `"Endset"` is listed in `all_axioms` in
`src/sage/categories/category_with_axiom.py`. [1](#0-0)

**2. `Homsets` as a singleton category with `Endset` as a `CategoryWithAxiom` nested
inside it.** `Homsets().Endset()` is reached via `self._with_axiom("Endset")` on any
homset category. The key structural fact is encoded in `extra_super_categories`:
[2](#0-1)

This says: every endset is a monoid (under composition).
The `SubcategoryMethods.Endset()` method makes `SomeCategory().Homsets().Endset()` work
uniformly. [3](#0-2)

**3. Per-category specialization via nested `Endset` classes.** Individual categories
override `extra_super_categories` inside their own `Homsets.Endset` to encode
domain-specific facts:

- `Modules(R).Homsets().Endset()` → endomorphism ring of a module is a
  `MagmaticAlgebra`: [4](#0-3)

- `AbelianVarieties(k).Homsets().Endset()` → endomorphism ring of an abelian variety is
  a `Ring`: [5](#0-4)

**4. Automatic dispatch in `Homset.__init__`.** When `X is Y`, the homset is placed in
`category.Endsets()` automatically: [6](#0-5)

* * *

## Existing Automorphism Group Implementations

Currently, automorphism groups are implemented in a completely ad-hoc way, disconnected
from the homset/endset framework:

- `FreeModuleLinearGroup` in `src/sage/tensor/modules/free_module_linear_group.py` is a
  standalone `Parent` with `category=Groups()`, with no connection to
  `Homsets`/`Endsets`: [7](#0-6)

- `AbelianGroupAutomorphismGroup` in `src/sage/groups/abelian_gps/abelian_aut.py`
  similarly inherits from `Group` directly: [8](#0-7)

- `FiniteFieldHomset` in `src/sage/rings/finite_rings/homset.py` calls itself
  "Automorphism group" in its repr when `domain == codomain`, but is still just a
  `Homset` with no autset category: [9](#0-8)

* * *

## The Correct Path Forward for Autsets

The pattern is clear by analogy.
Aut(X) is to End(X) as End(X) is to Hom(X,Y): it is a distinguished subset with extra
algebraic structure.
The hierarchy is:

```
Homsets  →  Endsets (axiom: Endset, extra_super: Monoids)
                  →  Autsets (axiom: Autset, extra_super: Groups)
```

This mirrors the algebraic chain Sets → Monoids → Groups.

### Step 1: Register the `Autset` axiom

Add `"Autset"` to `all_axioms` in `src/sage/categories/category_with_axiom.py`, placed
after `"Endset"` in the ordering.
[10](#0-9)

### Step 2: Add `Autset` as a `CategoryWithAxiom` inside `Homsets.Endset`

Since Aut(X) ⊆ End(X), the `Autset` axiom belongs on `Endsets`, not on `Homsets`
directly. Inside `Homsets.Endset`:

```python
class SubcategoryMethods:
    def Autset(self):
        return self._with_axiom("Autset")

class Autset(CategoryWithAxiom):
    def extra_super_categories(self):
        from .groups import Groups
        return [Groups()]  # every autset is a group under composition
```

This is the exact structural parallel to how `Homsets.Endset.extra_super_categories`
returns `[Monoids()]`. [11](#0-10)

### Step 3: Per-category specialization

Categories that know more about their autsets implement a nested `Autset` class inside
their `Homsets.Endset`:

- `Modules(R).Homsets().Endset().Autset()` → `extra_super_categories` returns
  `[Groups()]` (already the default, but could encode that it is the group of units of
  the endomorphism algebra)
- `AbelianVarieties(k).Homsets().Endset().Autset()` → could return `[Groups().Finite()]`
  for curves over finite fields

This is exactly how `AbelianVarieties.Homsets.Endset` overrides the base
`Homsets.Endset`. [12](#0-11)

### Step 4: Add repr handling

Just as `_repr_object_names_static` has a special case replacing `"homsets"` with
`"endsets"` for the `Endset` axiom, a parallel case replacing `"endsets"` with
`"autsets"` is needed: [13](#0-12)

### Step 5: Add an `Aut()` top-level function

Analogous to `End()` in `src/sage/categories/homset.py`:

```python
def Aut(X, category=None):
    return Hom(X, X, category).autset()
```

where `autset()` on an endset returns the autset subcategory (the invertible elements).
[14](#0-13)

### Step 6: Refactor existing implementations

`FreeModuleLinearGroup`, `AbelianGroupAutomorphismGroup`, and similar classes should be
refactored so their `category()` is `SomeCategory().Endsets().Autsets()` rather than
just `Groups()`. This would:

- Give them group structure automatically via `extra_super_categories` (no need to
  hardcode `category=Groups()`)
- Give them proper `domain()` and `codomain()` pointing to the object they act on
- Make `Aut(M)` return the same object as `M.automorphism_group()` (via
  `UniqueRepresentation`)
- Allow coercion maps `Aut(M) → End(M)` to be declared categorically rather than via
  ad-hoc `_coerce_map_from_` overrides

The key insight is that `FreeModuleLinearGroup` already conceptually *is* an autset — it
is the group of invertible elements of `End(M)` — but it is not *recognized* as one by
the category framework.
The refactoring is about making that recognition explicit.
[15](#0-14) [16](#0-15)

### Citations

**File:** src/sage/categories/category_with_axiom.py (L1675-1698)
```python
all_axioms = AxiomContainer()
all_axioms += ("Flying", "Blue",
               "Compact",
               "Differentiable", "Smooth", "Analytic", "AlmostComplex",
               "FinitelyGeneratedAsMagma",
               "WellGenerated",
               "Bounded",
               "Facade", "Finite", "Infinite", "Enumerated",
               "Complete",
               "Nilpotent",
               "FiniteDimensional", "FinitelyPresented", "Connected",
               "FinitelyGeneratedAsLambdaBracketAlgebra",
               "WithBasis",
               "Irreducible",
               "Supercommutative", "Supercocommutative",
               "Commutative", "Cocommutative", "Associative",
               "Inverse", "Unital", "Division", "NoZeroDivisors", "Cellular",
               "AdditiveCommutative", "AdditiveAssociative", "AdditiveInverse", "AdditiveUnital",
               "Extremal", "Trim", "Semidistributive", "CongruenceUniform",
               "ChainGraded", "Distributive", "Stone",
               "Endset",
               "Pointed",
               "Stratified"
               )
```

**File:** src/sage/categories/category_with_axiom.py (L2295-2297)
```python
            elif axiom == "Endset" and "homsets" in result:
                # Without the space at the end to handle Homsets().Endset()
                result = result.replace("homsets", "endsets", 1)
```

**File:** src/sage/categories/homsets.py (L282-296)
```python
    class SubcategoryMethods:

        def Endset(self):
            """
            Return the subcategory of the homsets of ``self`` that are endomorphism sets.

            EXAMPLES::

                sage: Sets().Homsets().Endset()
                Category of endsets of sets

                sage: Posets().Homsets().Endset()
                Category of endsets of posets
            """
            return self._with_axiom("Endset")
```

**File:** src/sage/categories/homsets.py (L298-326)
```python
    class Endset(CategoryWithAxiom):
        """
        The category of all endomorphism sets.

        This category serves too purposes: making sure that the
        ``Endset`` axiom is implemented in the category where it's
        defined, namely ``Homsets``, and specifying that ``Endsets``
        are monoids.

        EXAMPLES::

            sage: from sage.categories.homsets import Homsets
            sage: Homsets().Endset()
            Category of endsets
        """
        def extra_super_categories(self):
            """
            Implement the fact that endsets are monoids.

            .. SEEALSO:: :meth:`CategoryWithAxiom.extra_super_categories`

            EXAMPLES::

                sage: from sage.categories.homsets import Homsets
                sage: Homsets().Endset().extra_super_categories()
                [Category of monoids]
            """
            from .monoids import Monoids
            return [Monoids()]
```

**File:** src/sage/categories/modules.py (L813-833)
```python
        class Endset(CategoryWithAxiom_over_base_ring):
            """
            The category of endomorphism sets `End(X)` for `X`
            a module (this is not used yet)
            """
            def extra_super_categories(self):
                """
                Implement the fact that the endomorphism set of a module is an algebra.

                .. SEEALSO:: :meth:`CategoryWithAxiom.extra_super_categories`

                EXAMPLES::

                    sage: Modules(ZZ).Endsets().extra_super_categories()
                    [Category of magmatic algebras over Integer Ring]

                    sage: End(ZZ^3) in Algebras(ZZ)                                     # needs sage.modules
                    True
                """
                from .magmatic_algebras import MagmaticAlgebras
                return [MagmaticAlgebras(self.base_category().base_ring())]
```

**File:** src/sage/categories/schemes.py (L268-306)
```python
    class Homsets(HomsetsCategory):
        r"""
        Overloaded ``Homsets`` class to register the homset
        as an additive abelian group.

        EXAMPLES::

            sage: AbelianVarieties(QQ).Homsets().is_subcategory(CommutativeAdditiveGroups())
            True
        """
        def extra_super_categories(self):
            r"""
            Register the homset as an additive abelian group.

            EXAMPLES::

                sage: Hom(EllipticCurve(j=1), EllipticCurve(j=2)) in CommutativeAdditiveGroups()
                True
            """
            return [CommutativeAdditiveGroups()]

        class Endset(CategoryWithAxiom):
            r"""
            Overloaded ``Endset`` class to register the endset
            as a ring.

            sage: AbelianVarieties(QQ).Endsets().is_subcategory(Rings())
            True
            """
            def extra_super_categories(self):
                r"""
                Register the endset as a ring.

                EXAMPLES::

                    sage: End(EllipticCurve(j=1)) in Rings()
                    True
                """
                return [Rings()]
```

**File:** src/sage/categories/homset.py (L505-566)
```python
def End(X, category=None):
    r"""
    Create the set of endomorphisms of ``X`` in the category category.

    INPUT:

    - ``X`` -- anything

    - ``category`` -- (optional) category in which to coerce ``X``

    OUTPUT: a set of endomorphisms in category

    EXAMPLES::

        sage: V = VectorSpace(QQ, 3)                                                    # needs sage.modules
        sage: End(V)                                                                    # needs sage.modules
        Set of Morphisms (Linear Transformations)
         from Vector space of dimension 3 over Rational Field
         to Vector space of dimension 3 over Rational Field

    ::

        sage: # needs sage.groups
        sage: G = AlternatingGroup(3)
        sage: S = End(G); S
        Set of Morphisms
         from Alternating group of order 3!/2 as a permutation group
         to Alternating group of order 3!/2 as a permutation group
         in Category of finite enumerated permutation groups
        sage: S.domain()
        Alternating group of order 3!/2 as a permutation group

    To avoid creating superfluous categories, a homset in a category
    ``Cs()`` is in the homset category of the lowest full super category
    ``Bs()`` of ``Cs()`` that implements ``Bs.Homsets`` (or the join
    thereof if there are several). For example, finite groups form a
    full subcategory of unital magmas: any unital magma morphism
    between two finite groups is a finite group morphism. Since finite
    groups currently implement nothing more than unital magmas about
    their homsets, we have::

        sage: # needs sage.groups
        sage: G = GL(3, 3)
        sage: G.category()
        Category of finite groups
        sage: H = Hom(G, G)
        sage: H.homset_category()
        Category of finite groups
        sage: H.category()
        Category of endsets of unital magmas

    Similarly, a ring morphism just needs to preserve addition,
    multiplication, zero, and one. Accordingly, and since the category
    of rings implements nothing specific about its homsets, a ring
    homset is currently constructed in the category of homsets of
    unital magmas and unital additive magmas::

        sage: H = Hom(ZZ,ZZ,Rings())
        sage: H.category()
        Category of endsets of unital magmas and additive unital additive magmas
    """
    return Hom(X, X, category)
```

**File:** src/sage/categories/homset.py (L694-695)
```python
        Parent.__init__(self, base=base,
                        category=category.Endsets() if X is Y else category.Homsets())
```

**File:** src/sage/tensor/modules/free_module_linear_group.py (L1-11)
```python
r"""
General linear group of a free module

The set `\mathrm{GL}(M)` of automorphisms (i.e. invertible endomorphisms) of a
free module of finite rank `M` is a group under composition of automorphisms,
named the *general linear group* of `M`. In other words, `\mathrm{GL}(M)` is
the group of units (i.e. invertible elements) of `\mathrm{End}(M)`, the
endomorphism ring of `M`.

The group `\mathrm{GL}(M)` is implemented via the class
:class:`FreeModuleLinearGroup`.
```

**File:** src/sage/tensor/modules/free_module_linear_group.py (L39-88)
```python
class FreeModuleLinearGroup(UniqueRepresentation, Parent):
    r"""
    General linear group of a free module of finite rank over a commutative
    ring.

    Given a free module of finite rank `M` over a commutative ring `R`, the
    *general linear group* of `M` is the group `\mathrm{GL}(M)` of
    automorphisms (i.e. invertible endomorphisms) of `M`. It is the group of
    units (i.e. invertible elements) of `\mathrm{End}(M)`, the endomorphism
    ring of `M`.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.tensor.modules.free_module_automorphism.FreeModuleAutomorphism`.

    INPUT:

    - ``fmodule`` -- free module `M` of finite rank over a commutative ring
      `R`, as an instance of
      :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`

    EXAMPLES:

    General linear group of a free `\ZZ`-module of rank 3::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e')
        sage: from sage.tensor.modules.free_module_linear_group import FreeModuleLinearGroup
        sage: GL = FreeModuleLinearGroup(M) ; GL
        General linear group of the Rank-3 free module M over the Integer Ring

    Instead of importing FreeModuleLinearGroup in the global name space, it is
    recommended to use the module's method
    :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.general_linear_group`::

        sage: GL = M.general_linear_group() ; GL
        General linear group of the Rank-3 free module M over the Integer Ring
        sage: latex(GL)
        \mathrm{GL}\left( M \right)

    As most parents, the general linear group has a unique instance::

        sage: GL is M.general_linear_group()
        True

    `\mathrm{GL}(M)` is in the category of groups::

        sage: GL.category()
        Category of groups
        sage: GL in Groups()
        True
```

**File:** src/sage/groups/abelian_gps/abelian_aut.py (L436-458)
```python
    def __init__(self, AbelianGroupGap):
        """
        Constructor.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.aut()
            sage: TestSuite(aut).run()
        """
        self._domain = AbelianGroupGap
        if not isinstance(AbelianGroupGap, AbelianGroup_gap):
            raise ValueError("not an abelian group with GAP backend")
        if not self._domain.is_finite():
            raise ValueError("only finite abelian groups are supported")
        category = Groups().Finite().Enumerated()
        G = libgap.AutomorphismGroup(self._domain.gap())
        AbelianGroupAutomorphismGroup_gap.__init__(self,
                                                   self._domain,
                                                   gap_group=G,
                                                   category=category,
                                                   ambient=None)
```

**File:** src/sage/rings/finite_rings/homset.py (L130-148)
```python
    def _repr_(self):
        """
        Return a string representation of ``self``.

        EXAMPLES::

            sage: Hom(GF(4, 'a'), GF(16, 'b'))._repr_()
            'Set of field embeddings from Finite Field in a of size 2^2 to Finite Field in b of size 2^4'
            sage: Hom(GF(4, 'a'), GF(4, 'c'))._repr_()
            'Set of field embeddings from Finite Field in a of size 2^2 to Finite Field in c of size 2^2'
            sage: Hom(GF(4, 'a'), GF(4, 'a'))._repr_()
            'Automorphism group of Finite Field in a of size 2^2'
        """
        D = self.domain()
        C = self.codomain()
        if C == D:
            return "Automorphism group of %s" % D
        else:
            return "Set of field embeddings from %s to %s" % (D, C)
```

**File:** src/sage/tensor/modules/free_module_homset.py (L471-504)
```python
    def _coerce_map_from_(self, other):
        r"""
        Determine whether coercion to ``self`` exists from other parent.

        EXAMPLES:

        The module of type-`(1,1)` tensors coerces to ``self``::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: End(M)._coerce_map_from_(M.tensor_module(1,1))
            True
            sage: End(M).has_coerce_map_from(M.tensor_module(1,1))
            True
            sage: End(M)._coerce_map_from_(M.tensor_module(1,2))
            False

        The general linear group coerces to the endomorphism ring::

            sage: End(M)._coerce_map_from_(M.general_linear_group())
            True
        """
        from sage.tensor.modules.tensor_free_module import TensorFreeModule
        from sage.tensor.modules.free_module_linear_group import \
                                                          FreeModuleLinearGroup
        if isinstance(other, TensorFreeModule):
            # Coercion of a type-(1,1) tensor to an endomorphism:
            if other.tensor_type() == (1,1):
                return self.is_endomorphism_set() and \
                                           other.base_module() is self.domain()
        if isinstance(other, FreeModuleLinearGroup):
            # Coercion of an automorphism to an endomorphism:
            return self.is_endomorphism_set() and \
                                           other.base_module() is self.domain()
```

* * *

## Alternative: Runtime Extension of `all_axioms`

`all_axioms` is explicitly designed to be extended at runtime from external code.
The docs show this as the canonical pattern for defining new axioms without modifying
core Sage.

### Monkey-patching `all_axioms`

`all_axioms` is a module-level mutable `AxiomContainer` (a `dict` subclass).
The docs explicitly state:

> During a Sage session, new axioms should only be added at the *end* of `all_axioms`

and show the exact pattern:

```python
all_axioms = sage.categories.category_with_axiom.all_axioms
all_axioms += ("Green",)
```

The `AxiomContainer.add()` and `__iadd__` methods are documented public API.

So from your external package's init code:

```python
import sage.categories.category_with_axiom as _cwa
_cwa.all_axioms += ("Autset",)
```

This is safe as long as it happens before any category using `Autset` is constructed.

### Why `all_axioms` registration is mandatory

Two places in the framework hard-assert that an axiom is in `all_axioms`:

1. `axiom_of_nested_class` — when the framework infers the axiom name from a nested
   class, it checks `nested_cls_name in all_axioms` and then asserts
   `axiom in all_axioms`

2. `_repr_object_names_static` — calls `canonicalize_axioms(all_axioms, axioms)` which
   uses the rank dict

Without registration, you'd hit assertion errors the moment the framework tries to
introspect your axiom class.

### Defining the axiom entirely in your own category

Since you're not hooking into `Homsets`/`Endsets`, you define the axiom on your own root
category. The minimal structure is:

```python
# yourpackage/autsets.py
import sage.categories.category_with_axiom as _cwa
_cwa.all_axioms += ("Autset",)

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.category import Category

class MyEndsets(Category):
    def super_categories(self):
        from sage.categories.monoids import Monoids
        return [Monoids()]

    class SubcategoryMethods:
        def Autset(self):
            """Return the subcategory of automorphism sets."""
            return self._with_axiom("Autset")

    class Autset(CategoryWithAxiom):
        def extra_super_categories(self):
            from sage.categories.groups import Groups
            return [Groups()]
```

The nested `class Autset(CategoryWithAxiom)` is **mandatory** even if empty — the
framework requires it.

### What you don't need to touch

- **`_repr_object_names_static`**: The default `else` branch produces
  `uncamelcase("Autset") + " " + result` = `"autset ..."`, which is acceptable.
  You only need to patch that method if you want the `"endsets" → "autsets"` style
  substitution behavior (which requires editing core).

- **`_base_category_class_and_axiom`**: Since `Autset` is a nested class of your own
  category, `__classget__` will set this automatically the first time
  `MyEndsets().Autset()` is called.

### Summary of Runtime Extension

The only "core touch" required is the single `all_axioms += ("Autset",)` line, which is
explicitly documented as the supported runtime extension mechanism.
Everything else — the `SubcategoryMethods.Autset()` method, the nested
`Autset(CategoryWithAxiom)` class, and `extra_super_categories` — lives entirely in your
own package.

### Citations (Runtime Extension)

**File:** src/sage/categories/category_with_axiom.py (L340-353)
```python
With the current implementation, the name of the axiom must also be
added to a global container::

    sage: all_axioms = sage.categories.category_with_axiom.all_axioms
    sage: all_axioms += ("Green",)

We can now use the axiom as usual::

    sage: Cs().Green()
    Category of green cs

    sage: P = Parent(category=Cs().Green())
    sage: P.foo()
    I am a method on green C's
```

**File:** src/sage/categories/category_with_axiom.py (L375-378)
```python
.. NOTE::

    The presence of the nested class ``Green`` in ``Cs`` is currently
    mandatory even if it is empty.
```

**File:** src/sage/categories/category_with_axiom.py (L1847-1858)
```python
        if nested_cls_name in all_axioms:
            axiom = nested_cls_name
        else:
            cls_name = cls.__name__.split(".")[-1]
            if nested_cls_name.startswith(cls_name):
                axiom = nested_cls_name[len(cls_name):]
            elif nested_cls_name.endswith(cls_name):
                axiom = nested_cls_name[:-len(cls_name)]
            else:
                raise ValueError("could not infer axiom for the nested class {} of {}".format(nested_cls, cls))
    assert axiom in all_axioms, \
        "Incorrect deduction ({}) for the name of the axiom for the nested class {} of {}".format(axiom, nested_cls, cls)
```

**File:** src/sage/categories/category_with_axiom.py (L2071-2073)
```python
        if "_base_category_class_and_axiom" not in cls.__dict__:
            cls._base_category_class_and_axiom = (base_category_class, axiom_of_nested_class(base_category_class, cls))
            cls._base_category_class_and_axiom_origin = "set by __classget__"
```

**File:** src/sage/categories/category_with_axiom.py (L2266-2267)
```python
        from sage.categories.additive_magmas import AdditiveMagmas
        axioms = canonicalize_axioms(all_axioms,axioms)
```

**File:** src/sage/categories/category_with_axiom.py (L2295-2304)
```python
            elif axiom == "Endset" and "homsets" in result:
                # Without the space at the end to handle Homsets().Endset()
                result = result.replace("homsets", "endsets", 1)
            elif axiom == "FinitelyGeneratedAsMagma" and \
                 not base_category.is_subcategory(AdditiveMagmas()):
                result = "finitely generated " + result
            elif axiom == "FinitelyGeneratedAsLambdaBracketAlgebra":
                result = "finitely generated " + result
            else:
                result = uncamelcase(axiom) + " " + result
```

**File:** src/sage/categories/category_cy_helper.pyx (L230-266)
```text
    def add(self, axiom):
        """
        Add a new axiom name, of the next rank.

        EXAMPLES::

            sage: all_axioms = sage.categories.category_with_axiom.all_axioms
            sage: m = max(all_axioms.values())
            sage: all_axioms.add('Awesome')
            sage: all_axioms['Awesome'] == m + 1
            True

        To avoid side effects, we remove the added axiom::

            sage: del all_axioms['Awesome']
        """
        self[axiom] = len(self)

    def __iadd__(self, L):
        """
        Inline addition, which means to add a list of axioms to the container.

        EXAMPLES::

            sage: all_axioms = sage.categories.category_with_axiom.all_axioms
            sage: m = max(all_axioms.values())
            sage: all_axioms += ('Fancy', 'Awesome')
            sage: all_axioms['Awesome'] == m + 2
            True

        To avoid side effects, we delete the axioms that we just added::

            sage: del all_axioms['Awesome'], all_axioms['Fancy']
        """
        for axiom in L:
            self.add(axiom)
        return self
```

### Former `plans/autset_integration_plan.md`

# Autset Integration Plan

## Overview

This document outlines a systematic approach to integrate **autset** categories into
SageMath's categorical framework, aligning with the existing homset/endset hierarchy.

## Structural Hierarchy

```
Homsets  →  Endsets (axiom: Endset, extra_super: Monoids)
                  →  Autsets (axiom: Autset, extra_super: Groups)
```
- **Endsets** represent endomorphism monoids.
- **Autsets** represent groups of invertible endomorphisms (automorphism groups).

## Implementation Steps

### 1. Register the `Autset` Axiom

- **Location**: `src/sage/categories/category_with_axiom.py`
- **Action**: Add `"Autset"` to `all_axioms` after `"Endset"` in the ordering.
- **Impact**: Enables the axiom system to recognize autsets as a distinct categorical
  concept.

### 2. Define Autset Category Within Endsets

- **Location**: `src/sage/categories/homsets.py`
- **Structure**:
  ```python
  class SubcategoryMethods:
      def Autset(self):
          return self._with_axiom("Autset")

  class Autset(CategoryWithAxiom):
      def extra_super_categories(self):
          from .groups import Groups
          return [Groups()]  # Every autset is a group under composition
  ```
- **Rationale**: Mirrors the relationship where `Endset.extra_super_categories` returns
  `[Monoids()]`.

### 3. Per-Category Specialization

- **Location**: Category-specific modules (e.g., `Modules`, `AbelianVarieties`)
- **Action**: Override `extra_super_categories` in nested `Autset` classes to encode
  domain-specific algebraic structure.
  - Example: `Modules(R).Homsets().Endset().Autset()` could return `[UnitsOfRing]` or
    similar specialized constraints.
  - Example: `AbelianVarieties(k).Homsets().Endset().Autset()` could return
    `[FiniteGroups]` for finite fields.

### 4. Representation Handling

- **Location**: `_repr_object_names_static` handling
- **Action**: Add a rule replacing `"endsets"` with `"autsets"` analogous to the
  existing `"homsets"` → `"endsets"` replacement.

### 5. Top-Level `Aut()` Function

- **Location**: `src/sage/categories/homset.py`
- **Implementation**:
  ```python
  def Aut(X, category=None):
      return Hom(X, X, category).autset()
  ```
- **Function**: Returns the autset subcategory (invertible elements) of an endset.

### 6. Refactor Existing Automorphism Implementations

- **Target Classes**:
  - `FreeModuleLinearGroup` (`src/sage/tensor/modules/free_module_linear_group.py`)
  - `AbelianGroupAutomorphismGroup` (`src/sage/groups/abelian_gps/abelian_aut.py`)
  - `FiniteFieldHomset` (`src/sage/rings/finite_rings/homset.py`)
- **Refactoring Goals**:
  - Change category assignment from `Groups()` to `SomeCategory().Endsets().Autsets()`
 - `extra_super_categories` for automatic group structure
  - Ensure proper `domain()` and `codomain()` pointing to the acting object
  - Enable categorical coercion maps `Aut(M) → End(M)`
  - Make `Aut(M)` return the same object as `M.automorphism_group()` via
    `UniqueRepresentation`

### 7. Categorical Coercions

- **Implementation**: Use categorical `_coerce_map_from_` mechanisms instead of ad-hoc
  overrides.
- **Benefit**: Cleaner integration with the category framework and automatic adherence
  to algebraic laws.

## Key Files to Modify

1. `src/sage/categories/category_with_axiom.py` - Add `"Autset"` axiom
2. `src/sage/categories/homsets.py` - Define `Autset` category and `Aut()` function
3. Category modules with `Homsets.Endset` specializations (e.g.,
   `src/sage/categories/modules.py`, `src/sage/categories/schemes.py`)
4. Representation utilities (`_repr_object_names_static`)
5. Automorphism group implementations in:
   - `src/sage/tensor/modules/free_module_linear_group.py`
   - `src/sage/groups/abelian_gps/abelian_aut.py`
   - `src/sage/rings/finite_rings/homset.py`

## Verification Strategy

- Ensure existing automorphism group functionality remains intact
- Verify that new autset categories properly inherit algebraic structures
- Test categorical coercions and dispatch mechanisms
- Validate that representation strings correctly reflect autset contexts

## Dependencies

- Requires proper implementation of `CategoryWithAxiom` pattern
- Relies on existing `Endset` infrastructure
- Needs coordination with `SubcategoryMethods` and axiom registration system

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Plan-Card Review)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Exit Criteria, Gate 3 Phase Inventory, Gate 4 Scope Containment, Gate 5 Dependencies, Gate 6 Feature-Criteria Preservation
**Gates failed:** none
**Outcome:** plan-card is well-formed; structurally sound; the single phase under this plan has its own independent 6-gate review (passed with one Gate 5 finding on a child task self-reference)

---

#### Gate 1: Definition Grounding (source anchors grounded)

**Verdict:** PASS.

Source anchors declared in the plan frontmatter body:

- `category_specs/homsets/docs/MAPPING.md` — exists on disk at `/home/dzack/research/category_specs/homsets/docs/MAPPING.md`
- `category_specs/cat/docs/MAPPING.md` — exists on disk at `/home/dzack/research/category_specs/cat/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md` — exists on disk at `/home/dzack/research/category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md` — exists on disk at `/home/dzack/research/category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/MAPPING.md` — exists on disk at `/home/dzack/research/category_specs/lattices/docs/MAPPING.md`

All five source mapping files verified present. The plan's "Grounded Implementation Contract" (lines 33-57) provides concrete structural targets referencing these anchors. The "Admitted Definitions" section (lines 59-79) gives canonical definitions that child cards may use without re-deriving them.

Source corpus files:

- `plans/homsets_structural_core.md` — migrated into plan body as "Former `plans/homsets_structural_core.md`" (lines 112-297)
- `plans/autset_categories_path.md` — migrated into plan body (lines 299-439)
- `plans/autset_integration_plan.md` — migrated into plan body (lines 1037-1152)
- `plans/axioms_with_generators_finitely_presented.md` — referenced as supplementary source; not migrated but still available as related context
- `plans/todo.md` — marked as "Deleted source holder"

The plan provides extensive Sage source citations with file paths and line numbers (e.g., `src/sage/categories/modules.py` L728-735, L813-833; `src/sage/categories/homsets.py` L282-326; `src/sage/categories/homset.py` L505-566, L694-695; `src/sage/tensor/modules/free_module_linear_group.py` L1-11, L39-88; etc.). These citations anchor the plan's structural claims in real Sage source evidence.

**Recommendation:** None. Source grounding is thorough and verifiable.

#### Gate 2: Exit Criteria (checkability of success criteria)

**Verdict:** PASS.

Plan frontmatter success criteria:

1. "`Aut(X)` and `End(X)` are category-recognized surfaces, not isolated helper factories."
   - **Checkability:** Verifiable by runtime category inspection: `Aut(X).category().is_subcategory(Endsets().Autsets())` or equivalent. The concrete expected behavior is that Aut/End objects carry category membership in the Hom/End/Aut hierarchy rather than bare `Groups()` or `Monoids()`.

2. "Automorphism groups have domain/codomain semantics and categorical coercion to End."
   - **Checkability:** Direct method inspection — `Aut(X).domain()` and `Aut(X).codomain()` must return the underlying object X. A coercion path `Aut(X) → End(X)` must be registered categorically (via `_coerce_map_from_` within the category framework, not ad-hoc overrides). The plan's body (lines 1107-1119) specifies the refactoring target in detail.

3. "Public APIs return project-owned aut/subobject surfaces; Sage `ConditionSet` remains an implementation bridge only."
   - **Checkability:** Static code audit — grep for `SageConditionSet` or `ConditionSet` in public method signatures and return types. The concrete boundary is defined in the plan body (line 51): "may use Sage `ConditionSet` internally, but the public object returned ... is the project aut/subobject object." The child task TASK-1777748120385 addresses this directly with specific file targets.

Body acceptance criteria (lines 105-107) mirror the frontmatter criteria in checkbox form.

**Recommendation:** None. All criteria are specific, falsifiable, and scoped to concrete API surfaces.

#### Gate 3: Phase Inventory (completeness of phase coverage)

**Verdict:** PASS.

The plan declares one phase: `[[PHASE-HOM-END-AUT-WORK-QUEUE]]`.

Phase card location: `PHASE-HOM-END-AUT-WORK-QUEUE/PHASE-HOM-END-AUT-WORK-QUEUE.md` — present and well-formed.

Phase child task inventory (3 tasks under `tasks/`):

| Card ID | Title | Status |
|---|---|---|
| TASK-01KQN9J3W... | Fix Cat smoke Hom End Aut ObjectsOver... | `complete` (passed Gates 1-6, Russell re-review) |
| TASK-1777748120385 | Remove raw ConditionSet from public Aut-category surface | `needs-human-input` (passed Gates 1-6, Fermat re-review; awaiting human approval) |
| TASK-WRAPUP | Phase wrap-up | `unstarted` (gated behind two work tasks) |

Coverage assessment:

- The Cat smoke task addresses plan criterion 1 (category-recognized Hom/End/Aut surfaces) by fixing interop aliases, slice/coslice dispatch, and WithForms PID specialization.
- The ConditionSet task addresses plan criterion 3 (ConditionSet as implementation bridge) by privatizing raw `SageConditionSet` construction and preserving the project-owned aut-object surface.
- The wrap-up task provides phase-closure hygiene.

The plan also records two owned downstream spec cards in its body:

- `SPEC-01KQN9J3WJE9W76X72DAT10H4Y` (dual-object Hom routing) — exists at `specs/SPEC-01KQN9J3WJE9...`, `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]`, status `unstarted`. Correct: dual-object routing through Homsets requires stable Hom/End/Aut surfaces.
- `SPEC-01KQN9J3WQDJ0Z27BXTY67HA72` (DiscriminantGroup Hom/End/Aut) — exists in `FEATURE-MODULES-WITH-FORMS-AND-LATTICES/specs/`, `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]`, status `complete`. Correct: discriminant-group naming should follow the structural admission patterns established by this plan.

**Finding (minor):** The phase card status is `complete`, but two of its three child tasks are not yet complete (TASK-1777748120385 is `needs-human-input`, TASK-WRAPUP is `unstarted`). The phase status should remain `in-progress` or `needs-review` until child tasks resolve. This does not affect plan-level validity — the phase card has its own independent 6-gate review covering this issue.

**Recommendation:** Consider updating the phase card status from `complete` to `in-progress` until TASK-1777748120385 receives human approval and TASK-WRAPUP executes.

#### Gate 4: Scope Containment (no scope creep)

**Verdict:** PASS.

The plan's objective is tightly scoped: admit Homsets, Endsets, Autsets, dual objects, and automorphism groups through the category framework. The plan body explicitly partitions the boundary:

- **In scope:** Category-recognized Hom/End/Aut surfaces, domain/codomain semantics, categorical coercion, ConditionSet privatization, dual objects as Hom objects, formed-module automorphism groups as orthogonal-group surfaces.
- **Out of scope (explicitly deferred):** "Matrix, function, and predicate calculations remain implementation evidence only" (line 56-57); functor/autofunctor modeling is recorded as future work in TASK-01KQN9J3W... (body: "natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors"); full category-spec smoke beyond Hom/End/Aut is outside this plan's scope.

The phase's child tasks respect these boundaries:

- TASK-01KQN9J3W... limits to Cat smoke frontier interop (Homsets/Endsets aliases, ObjectsOver/ObjectsUnder, WithForms PID specialization). Does not expand into functor or natural transformation modeling.
- TASK-1777748120385 limits to a single file (`category_specs/homsets/autsets.py`) for ConditionSet privatization and aut-object surface preservation.
- TASK-WRAPUP is a process meta-task, not implementation work.

The Deleted source holder `plans/todo.md` and the migrated source bodies are correctly confined to the plan's scope domain.

**Recommendation:** None.

#### Gate 5: Dependencies (correctness of dependency declarations)

**Verdict:** PASS.

Upstream (plan → feature):

- Plan `dependsOn: []` — correct. No cross-plan prerequisites.
- Plan `parents: [[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]` — correct. The plan lives under the feature's `plans/` directory.

Internal (plan → phase):

- Plan `phases: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` — correct. Single phase, exists on disk.
- Phase `parents: [[PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION]]` — correct.
- Phase `dependsOn: []` — correct. No cross-phase dependencies needed.

Downstream (spec cards depending on this plan's phase):

- `SPEC-01KQN9J3WJE9...` (dual-object Hom routing) `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` — verified via file read; correct.
- `SPEC-01KQN9J3WQDJ...` (DiscriminantGroup Hom/End/Aut) `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` — verified via file read; correct.

The phase card's own 6-gate review identified one dependency finding at the task level: TASK-WRAPUP lists itself in its own `dependsOn` field (self-reference). This is a phase-level hygiene issue that does not affect plan-level correctness. The phase review already recommends removing the self-referential entry before phase closure.

No missing dependency declarations. No undeclared upstream blocking. The DAG is consistent from plan through phase through downstream specs.

**Recommendation:** None at plan level. The TASK-WRAPUP self-reference is a phase-level finding already documented in the phase review.

#### Gate 6: Feature-Criteria Preservation (no weakening)

**Verdict:** PASS.

Parent feature `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` establishes the top-level scope. The plan's success criteria are a direct refinement of the feature's category-specs-and-Sage-surfaces mandate:

1. Category-recognized Aut/End surfaces → implements the "category specs" half
2. Domain/codomain semantics and categorical coercion → implements the "Sage-compatible constructors" half
3. ConditionSet as implementation bridge only → implements the "Sage surfaces" boundary

The phase card's success criteria are operational gates (child task completion discipline, source citation requirements, follow-up card hygiene) that layer on top of the plan's mathematical criteria without weakening or replacing them.

Child task acceptance criteria directly enforce plan criteria:

- TASK-1777748120385 ACs (ConditionSet removal, private helper routing, public aut-object surface preservation, mapping documentation) directly implement plan criterion 3.
- TASK-01KQN9J3W... ACs (category vocabulary, Cat smoke verification, Hom shadowing audit) directly implement plan criterion 1.

No acceptance criteria have been weakened, replaced, or diluted at any level of the plan→phase→task hierarchy. The three-tier structure (plan mathematical targets → phase operational gates → task concrete deliverables) is coherent and progressive.

**Recommendation:** None.

---

#### Summary

`PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` passes all six gates. The plan is firmly grounded in five MAPPING.md source files (all verified on disk), its success criteria are checkable and specific, its single phase provides complete work coverage, scope boundaries are explicit and respected, the dependency graph is correct (one phase-level self-reference finding is documented downstream), and no feature criteria have been weakened.

The plan is ready to proceed. The phase `PHASE-HOM-END-AUT-WORK-QUEUE` has its own independent 6-gate review (passed with one Gate 5 finding on TASK-WRAPUP self-reference). Once the `needs-human-input` task receives approval and the wrap-up task executes, the plan can be marked complete.
