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
simultaneously has Hom-category `ElementMethods` (kernel, image, cokernel) and
`ElementMethods` from `MyFGModules(R)` (lmul, rmul).
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
├── HomCategory.ElementMethods: kernel(), image(), cokernel()
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
