<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RMod_refactored.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: RModules (Refactored)

The category of R-modules, now properly inheriting from abelian and symmetric monoidal categories.

## Category Definition

```python
from sage.categories.category_types import Category_module
from sage.categories.modules import Modules
from sage.categories.abelian_categories import AbelianCategories
from sage.categories.symmetric_monoidal_categories import SymmetricMonoidalCategories
from sage.categories.module_axioms import FinitelyGenerated, Free, WithBasis

class RModules(Category_module):
    """
    The category of R-modules with proper categorical structure.
    
    This implementation:
    - Inherits abelian structure (kernels, cokernels, exact sequences)
    - Inherits symmetric monoidal structure (tensor products with coherence)
    - Provides module-specific axioms (Free, FinitelyGenerated, WithBasis)
    - Supports symbolic computation with natural mathematical notation
    
    EXAMPLES::
    
        sage: from sage.categories.rmodules import RModules
        sage: C = RModules(ZZ)
        sage: C
        Category of R-modules over Integer Ring
        
        sage: # Check categorical structure
        sage: C in AbelianCategories()
        True
        sage: C in SymmetricMonoidalCategories()
        True
        
        sage: # Module-specific axioms
        sage: C.Free()
        Category of free modules over Integer Ring
        sage: C.FinitelyGenerated()
        Category of finitely generated modules over Integer Ring
        sage: C.WithBasis()
        Category of modules with basis over Integer Ring
        
        sage: TestSuite(C).run()
    """
    
    def __init__(self, base_ring):
        """
        Initialize the category of R-modules.
        
        EXAMPLES::
        
            sage: C = RModules(QQ)
            sage: C.base_ring()
            Rational Field
        """
        self._base_ring = base_ring
        super().__init__(base_ring)
    
    def super_categories(self):
        """
        R-modules form an abelian symmetric monoidal category.
        
        We inherit:
        - From AbelianCategories: kernels, cokernels, exact sequences
        - From SymmetricMonoidalCategories: tensor products with coherence
        - From Modules: basic module structure
        
        EXAMPLES::
        
            sage: RModules(ZZ).super_categories()
            [Category of modules over Integer Ring,
             Category of abelian categories,  
             Category of symmetric monoidal categories]
        """
        return [Modules(self.base_ring()),
                AbelianCategories(),
                SymmetricMonoidalCategories()]
    
    def _repr_(self):
        """
        String representation of the category.
        
        EXAMPLES::
        
            sage: RModules(ZZ)
            Category of R-modules over Integer Ring
        """
        return f"Category of R-modules over {self.base_ring()}"
    
    # Module-specific axioms
    class FinitelyGenerated(FinitelyGenerated):
        """
        The axiom for finitely generated R-modules.
        
        Inherited from module_axioms but specialized for R-modules.
        """
        pass
    
    class Free(Free):
        """
        The axiom for free R-modules.
        
        Inherited from module_axioms but specialized for R-modules.
        """
        pass
    
    class WithBasis(WithBasis):
        """
        The axiom for R-modules with distinguished basis.
        
        Inherited from module_axioms but specialized for R-modules.
        """
        pass
    
    class ParentMethods:
        """
        Methods for R-module parent objects.
        
        Most methods are inherited from:
        - AbelianCategories: zero(), direct_sum()
        - SymmetricMonoidalCategories: tensor_product(), tensor_unit()
        - Modules: base_ring(), etc.
        
        Here we add only R-module specific methods.
        """
        
        # The following are inherited from AbelianCategories.ParentMethods:
        # - zero()
        # - direct_sum()
        # - is_zero()
        
        # The following are inherited from SymmetricMonoidalCategories.ParentMethods:
        # - tensor_product()
        # - tensor_unit()
        # - associator()
        # - left_unitor()
        # - right_unitor()
        # - braiding()
        
        def basis(self):
            """
            Return the basis of this R-module if it has one.
            
            This is a convenience method that works for modules
            in the WithBasis subcategory.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ, basis=['x', 'y', 'z'])
                sage: list(M.basis())
                [x, y, z]
                
                sage: # Raises error for non-basis modules
                sage: N = (ZZ^3).quotient([(1,1,0)])
                sage: N.basis()
                Traceback (most recent call last):
                ...
                NotImplementedError: This module does not have a distinguished basis
            """
            if self in RModules(self.base_ring()).WithBasis():
                # Implemented by WithBasis.ParentMethods
                return self.basis()
            else:
                raise NotImplementedError("This module does not have a distinguished basis")
        
        def hom(self, codomain, morphism_data, **kwds):
            """
            Create a module homomorphism.
            
            This extends the basic hom constructor with support for
            various input formats specific to R-modules.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ, basis=['a', 'b'])
                sage: N = RMod(ZZ, basis=['x', 'y', 'z'])
                sage: phi = M.hom([2*N.x + N.y, N.x - 3*N.z])
                sage: phi
                Module morphism:
                  From: Free module with basis {a, b} over Integer Ring
                  To:   Free module with basis {x, y, z} over Integer Ring
            """
            # Implementation details for creating morphisms
            raise NotImplementedError
        
        def submodule(self, generators, check=True):
            """
            Return the submodule generated by the given elements.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ, basis=['e1', 'e2', 'e3'])
                sage: S = M.submodule([M.e1 + M.e2, M.e2 + M.e3])
                sage: S
                Submodule of Free module with basis {e1, e2, e3}
                generated by {e1 + e2, e2 + e3}
            """
            raise NotImplementedError
        
        def quotient(self, submodule):
            """
            Return the quotient module by a submodule.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ, basis=['x', 'y', 'z'])
                sage: S = M.submodule([M.x + M.y])
                sage: Q = M.quotient(S)
                sage: Q
                Quotient of Free module with basis {x, y, z}
                by Submodule generated by {x + y}
            """
            raise NotImplementedError
        
        def dual(self):
            """
            Return the dual module Hom(M, R).
            
            For finitely generated free modules, this is naturally
            isomorphic to a free module of the same rank.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ, basis=['a', 'b', 'c'])
                sage: M_dual = M.dual()
                sage: M_dual
                Dual of Free module with basis {a, b, c} over Integer Ring
                
                sage: # Has natural pairing
                sage: a_dual = M_dual.basis()[0]
                sage: M.a * a_dual  # Evaluation pairing
                1
            """
            raise NotImplementedError
    
    class ElementMethods:
        """
        Methods for R-module elements.
        
        Most are inherited from parent categories.
        """
        
        # Inherited from AbelianCategories.ElementMethods:
        # - is_zero()
        
        def to_vector(self):
            """
            Convert this element to a coordinate vector if possible.
            
            This works for modules in WithBasis() or those that
            can be embedded in a free module.
            
            EXAMPLES::
            
                sage: M = RMod(QQ, basis=['a', 'b', 'c'])
                sage: v = M.a + 2*M.b - 3*M.c
                sage: v.to_vector()
                (1, 2, -3)
            """
            return self.parent().to_vector(self)
    
    class HomsetMethods:
        """
        Methods for morphism sets between R-modules.
        
        Most morphism methods are inherited from AbelianCategories.
        Here we add only R-module specific operations.
        """
        
        # Inherited from AbelianCategories.HomsetMethods:
        # - kernel()
        # - cokernel()
        # - image()
        # - coimage()
        # - is_monomorphism()
        # - is_epimorphism()
        # - is_isomorphism()
        # - canonical_factorization()
        
        # Inherited from SymmetricMonoidalCategories.HomsetMethods:
        # - tensor_product()
        
        def matrix(self, basis_domain=None, basis_codomain=None):
            """
            Return the matrix representation of this morphism.
            
            This requires both domain and codomain to have bases
            (be in WithBasis subcategory).
            
            EXAMPLES::
            
                sage: M = RMod(QQ, basis=['e1', 'e2'])
                sage: N = RMod(QQ, basis=['f1', 'f2', 'f3'])
                sage: phi = M.hom([N.f1 + N.f2, 2*N.f2 - N.f3])
                sage: phi.matrix()
                [ 1  0]
                [ 1  2]
                [ 0 -1]
            """
            raise NotImplementedError
        
        def determinant(self):
            """
            Return the determinant if this is an endomorphism.
            
            Requires domain = codomain with basis.
            
            EXAMPLES::
            
                sage: M = RMod(QQ, basis=['x', 'y'])
                sage: phi = M.hom([2*M.x + M.y, M.x + 3*M.y])
                sage: phi.determinant()
                5  # det([[2,1],[1,3]]) = 6-1 = 5
            """
            raise NotImplementedError
        
        def trace(self):
            """
            Return the trace if this is an endomorphism.
            
            EXAMPLES::
            
                sage: M = RMod(QQ, basis=['a', 'b'])
                sage: phi = M.hom([2*M.a + M.b, M.a + 3*M.b])
                sage: phi.trace()
                5  # tr([[2,1],[1,3]]) = 2+3 = 5
            """
            raise NotImplementedError
```

## Key Design Principles

### 1. Proper Inheritance
- Abelian structure from `AbelianCategories`
- Tensor structure from `SymmetricMonoidalCategories`
- Module basics from `Modules`

### 2. Clean Separation
- External axioms (abelian, monoidal) in separate files
- Module-specific axioms (Free, WithBasis) in `module_axioms.md`
- Only R-module specific code in this file

### 3. No Duplication
- Don't reimplement kernel/cokernel (inherited from abelian)
- Don't reimplement tensor products (inherited from monoidal)
- Only add module-specific operations

### 4. Axiom Combinations
```python
# Examples of axiom combinations
C = RModules(ZZ)

# All finitely generated free modules
C.Free() & C.FinitelyGenerated()

# All modules with finite basis  
C.WithBasis() & C.FinitelyGenerated()

# All infinite-dimensional modules with basis
C.WithBasis() & ~C.FinitelyGenerated()
```

## Benefits of This Refactoring

1. **Clarity**: Clear separation of concerns
2. **Reusability**: Abelian/monoidal structures can be used elsewhere
3. **Correctness**: Inheriting tested implementations
4. **Extensibility**: Easy to add new axioms or structures
5. **Documentation**: Each concept in its proper place

## Migration from Old Structure

```python
# Old way (everything in one file)
class RModules(Category):
    def kernel(self): ...  # Duplicated
    def tensor_product(self): ...  # Duplicated
    class Free(CategoryWithAxiom): ...  # Mixed together

# New way (proper separation)
class RModules(Category_module):
    # Inherits kernel from AbelianCategories
    # Inherits tensor_product from SymmetricMonoidalCategories  
    # References Free from module_axioms
```

This refactoring provides a clean, mathematically correct structure that properly separates categorical properties from module-specific features.