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

- Hom-category `ElementMethods` (`kernel`, `image`, `cokernel`)
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
