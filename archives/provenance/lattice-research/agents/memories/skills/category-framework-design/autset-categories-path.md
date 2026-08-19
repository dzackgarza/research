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
