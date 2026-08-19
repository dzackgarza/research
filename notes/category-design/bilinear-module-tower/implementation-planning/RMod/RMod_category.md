<!--
Origin: gitclones/Coxeter/implementation/planning/RMod/RMod_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: RModules(R)

The category of R-modules with symbolic-first computation and R-linear morphisms.

## Category Definition

```python
from sage.categories.category_types import Category_module
from sage.categories.modules import Modules
from sage.categories.abelian_categories import AbelianCategories
from sage.categories.category_with_axiom import CategoryWithAxiom

class RModules(Category_module):
    """
    The category of R-modules with symbolic-first computation.
    
    This category provides the foundational structure for R-modules,
    supporting both free and torsion modules. Specific types of modules
    are characterized by axioms (Free, WithBasis) rather than separate categories.
    
    Objects in this category include:
    - Free R-modules (characterized by universal property)
    - Torsion modules (e.g., R/I for ideals I)
    - Mixed modules (free ⊕ torsion via structure theorem)
    
    The category provides:
    - Full abelian category structure (inherited):
      * Subobjects and quotients
      * Kernels, cokernels, images (on morphisms)
      * Biproducts (direct sums)
      * Exact sequences
      * Finite limits and colimits
    - R-module specific features:
      * Module homomorphisms determined by images of generators
      * Tensor products (⊗) with universal property for bilinear maps
      * Cartesian products (×) with componentwise operations
      * Natural operations (+, *, @, /) for split Grothendieck ring K₀(R)
      * Hom modules and tensor-hom adjunction
      * Duality functor Hom(-, R)
    - Optional symmetric monoidal structure via SymmetricMonoidal axiom
    - Integration with bilinear forms and indefinite lattices
    
    EXAMPLES::
    
        sage: C = RModules(ZZ)
        sage: C
        Category of R-modules over Integer Ring
        sage: C.super_categories()
        [Category of modules over Integer Ring, Category of abelian categories]
        
        sage: # Symmetric monoidal structure can be made explicit
        sage: C_tensor = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
        sage: C_tensor
        Category of symmetric monoidal R-modules over Integer Ring with tensor product
    """
    
    def super_categories(self):
        """
        R-modules form an abelian category that is a full subcategory of modules.
        
        The abelian structure provides:
        - Existence of kernels and cokernels for all morphisms
        - Existence of finite limits and colimits
        - Every monomorphism is a kernel, every epimorphism is a cokernel
        - Exact sequences
        
        EXAMPLES::
        
            sage: RModules(QQ).super_categories()
            [Category of modules over Rational Field, 
             Category of abelian categories]
        """
        return [Modules(self.base_ring()), AbelianCategories()]
    
    def _repr_(self):
        """
        String representation of the category.
        
        EXAMPLES::
        
            sage: RModules(ZZ)
            Category of R-modules over Integer Ring
        """
        return f"Category of R-modules over {self.base_ring()}"
    
    def SymmetricMonoidal(self, monoidal_product, unit):
        """
        Return this category equipped with a symmetric monoidal structure.
        
        INPUT:
        - monoidal_product -- string name or callable for the monoidal product
        - unit -- the unit object for this monoidal structure
        
        OUTPUT:
        The category with SymmetricMonoidal axiom applied
        
        EXAMPLES::
        
            sage: # Tensor product monoidal structure
            sage: C_tensor = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
            sage: C_tensor
            Category of symmetric monoidal R-modules over Integer Ring with tensor product
            
            sage: # Direct sum monoidal structure
            sage: from sage.modules.zero_module import ZeroModule
            sage: C_sum = RModules(QQ).SymmetricMonoidal('direct_sum', ZeroModule(QQ))
            sage: C_sum
            Category of symmetric monoidal R-modules over Rational Field with direct sum
        """
        return SymmetricMonoidal(self, monoidal_product, unit)
```

## Universal Properties

- **Abelian category**: Has kernels, cokernels, finite limits/colimits
- **Module universal property**: Morphisms determined by images of generators
- **Tensor-hom adjunction**: Hom(M⊗N, P) ≅ Hom(M, Hom(N, P))

## Natural Operations for Split Grothendieck Ring K₀(R)

The category provides natural syntax for the four fundamental operations:

```python
class ParentMethods:
    """
    Methods available on ALL R-module parent objects.
    
    These methods are automatically available on any parent
    in the category RModules(R), whether free, torsion, or mixed.
    
    Some methods (subobject, quotient) come from AbelianCategories,
    while others are specific to modules over rings.
    """
    
    def hom(self, codomain, images_of_generators):
        """
        Create a module homomorphism.
        
        Universal for all R-modules - homomorphisms determined by 
        images of any generating set.
        
        INPUT:
        - codomain -- target R-module
        - images_of_generators -- list of images (implementation-dependent)
        """
        raise NotImplementedError
    
    def direct_sum(self, *others):
        """
        Direct sum with other modules.
        
        The direct sum M ⊕ N is the biproduct in the abelian category
        of R-modules (both product and coproduct).
        """
        raise NotImplementedError
    
    def tensor_product(self, *others):
        """
        Tensor product with other modules.
        
        The tensor product M ⊗_R N satisfies the universal property
        for bilinear maps.
        """
        raise NotImplementedError
    
    def cartesian_product(self, *others):
        """
        Cartesian product with other modules.
        
        The cartesian product M × N has underlying set M × N with
        componentwise operations.
        """
        raise NotImplementedError
    
    def quotient(self, submodule):
        """
        Return the quotient module by a submodule.
        
        This inherits from AbelianCategories but ensures the result
        remains in the appropriate module category.
        """
        raise NotImplementedError
    
    def __add__(self, other):
        """
        Syntactic sugar: M + N for direct sum M ⊕ N.
        
        Direct sum monoidal structure with unit 0. This captures the
        additive structure in the split Grothendieck ring K₀(R).
        """
        return self.direct_sum(other)
    
    def __mul__(self, other):
        """
        Syntactic sugar: M * N for cartesian product M × N.
        
        Cartesian product monoidal structure with unit 0 (terminal object).
        """
        return self.cartesian_product(other)
    
    def __matmul__(self, other):
        """
        Syntactic sugar: M @ N for tensor product M ⊗ N.
        
        Tensor product monoidal structure with unit R. This captures the
        multiplicative structure in the split Grothendieck ring K₀(R).
        """
        return self.tensor_product(other)
    
    def __truediv__(self, submodule):
        """
        Syntactic sugar: M / N for quotient module M/N.
        
        Quotient by submodule. This enables split Grothendieck ring
        equations like M = M/N + N to be written naturally.
        """
        return self.quotient(submodule)

class ElementMethods:
    """
    Methods available on ALL R-module elements.
    
    These methods are automatically available on any element
    of a parent in RModules(R), whether in free, torsion, or mixed modules.
    """
    
    def is_zero(self):
        """
        Check if this is the zero element.
        
        Fundamental operation valid for all R-module elements.
        """
        raise NotImplementedError

class HomsetMethods:
    """
    Methods for morphisms between R-modules.
    
    Most morphism methods (kernel, cokernel, image, etc.) are inherited
    from AbelianCategories. Here we add R-module specific operations.
    """
    
    def tensor_product(self, other):
        """
        Tensor product of morphisms.
        
        For f: M → N and g: P → Q, returns f ⊗ g: M ⊗ P → N ⊗ Q.
        
        This is specific to modules (not general abelian categories).
        """
        raise NotImplementedError
```

## Symmetric Monoidal Structure (Optional)

```python
class SymmetricMonoidal(CategoryWithAxiom):
    """
    The axiom for symmetric monoidal categories.
    
    A symmetric monoidal category is equipped with:
    - A monoidal product ⊗: C × C → C
    - A unit object I
    - Natural isomorphisms:
      * Associator: (A⊗B)⊗C ≅ A⊗(B⊗C)
      * Left unitor: I⊗A ≅ A
      * Right unitor: A⊗I ≅ A
      * Braiding: A⊗B ≅ B⊗A (symmetric)
    
    The monoidal structure must be specified explicitly when applying this axiom,
    as categories can have multiple monoidal structures.
    """
    
    def __init__(self, base_category, monoidal_product, unit):
        """
        Initialize a symmetric monoidal category with specified structure.
        
        INPUT:
        - base_category -- the underlying category
        - monoidal_product -- string name or callable for the monoidal product
        - unit -- the unit object for this monoidal structure
        """
        self._monoidal_product = monoidal_product
        self._monoidal_unit = unit
        CategoryWithAxiom.__init__(self, base_category)
    
    class ParentMethods:
        """Methods for parents in symmetric monoidal categories."""
        
        def monoidal_product(self, other):
            """
            Compute the monoidal product with another object.
            
            The specific product used depends on how the SymmetricMonoidal
            axiom was initialized for this category.
            """
            product_op = self.category()._monoidal_product
            if isinstance(product_op, str):
                method = getattr(self, product_op, None)
                if method is None:
                    raise NotImplementedError(f"Monoidal product '{product_op}' not implemented")
                return method(other)
            else:
                return product_op(self, other)
        
        def associator(self, B, C):
            """Return the associator isomorphism (A⊗B)⊗C → A⊗(B⊗C)."""
            raise NotImplementedError
        
        def left_unitor(self):
            """Return the left unitor isomorphism I⊗A → A."""
            raise NotImplementedError
        
        def right_unitor(self):
            """Return the right unitor isomorphism A⊗I → A."""
            raise NotImplementedError
        
        def braiding(self, other):
            """Return the braiding isomorphism A⊗B → B⊗A."""
            raise NotImplementedError
```