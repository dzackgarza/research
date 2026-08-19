<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RMod_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: RModules(R)

The category of R-modules with symbolic-first computation. This refactored structure separates the category definition from parent/element implementations following SageMath best practices.

## Category Definition

```python
from sage.categories.category_types import Category_module
from sage.categories.modules import Modules
from sage.categories.category_with_axiom import CategoryWithAxiom

# Independent SymmetricMonoidal axiom for any category
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
    
    EXAMPLES::
    
        sage: from sage.categories.rmodules import RModules
        sage: # R-modules with tensor product monoidal structure
        sage: C_tensor = RModules(ZZ).SymmetricMonoidal(
        ....:     monoidal_product='tensor_product',
        ....:     unit=ZZ  # ZZ as a ZZ-module
        ....: )
        sage: C_tensor
        Category of symmetric monoidal R-modules over Integer Ring with tensor product
        
        sage: # R-modules with direct sum monoidal structure
        sage: C_sum = RModules(ZZ).SymmetricMonoidal(
        ....:     monoidal_product='direct_sum',
        ....:     unit=ZeroModule(ZZ)  # Zero module is unit for direct sum
        ....: )
        
        sage: # For homotopy theory: pointed spaces with smash product
        sage: # (when PointedSpaces category exists)
        sage: # C_smash = PointedSpaces().SymmetricMonoidal(
        sage: #     monoidal_product='smash_product',
        sage: #     unit=S0  # 0-sphere is unit for smash
        sage: # )
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
    
    def _repr_(self):
        """
        String representation showing the monoidal structure.
        
        EXAMPLES::
        
            sage: RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
            Category of symmetric monoidal R-modules over Integer Ring with tensor product
        """
        base = self.base_category()
        product_name = self._monoidal_product
        if isinstance(product_name, str):
            product_name = product_name.replace('_', ' ')
        return f"Category of symmetric monoidal {base._repr_object_names()} with {product_name}"
    
    def monoidal_product_name(self):
        """
        Return the name/identifier of the monoidal product operation.
        
        EXAMPLES::
        
            sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
            sage: C.monoidal_product_name()
            'tensor_product'
        """
        return self._monoidal_product
    
    def monoidal_unit(self):
        """
        Return the unit object for this monoidal structure.
        
        EXAMPLES::
        
            sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
            sage: C.monoidal_unit()
            Integer Ring
        """
        return self._monoidal_unit
    
    class ParentMethods:
        """
        Methods for parents in symmetric monoidal categories.
        """
        
        def monoidal_product(self, other):
            """
            Compute the monoidal product with another object.
            
            The specific product used depends on how the SymmetricMonoidal
            axiom was initialized for this category.
            
            INPUT:
            - other -- another object in the same symmetric monoidal category
            
            OUTPUT:
            The monoidal product of self and other
            
            EXAMPLES::
            
                sage: # Tensor product monoidal structure
                sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: M.monoidal_product(N)  # Uses tensor_product internally
                Free module over Integer Ring with basis {a⊗x, a⊗y, b⊗x, b⊗y}
                
                sage: # Direct sum monoidal structure  
                sage: C_sum = RModules(ZZ).SymmetricMonoidal('direct_sum', ZeroModule(ZZ))
                sage: M_sum = M.with_category(C_sum)
                sage: M_sum.monoidal_product(N)  # Uses direct_sum internally
                Free module over Integer Ring with basis {a, b, x, y}
            """
            product_op = self.category()._monoidal_product
            if isinstance(product_op, str):
                # Look up method by name
                method = getattr(self, product_op, None)
                if method is None:
                    raise NotImplementedError(f"Monoidal product '{product_op}' not implemented")
                return method(other)
            else:
                # Callable was provided
                return product_op(self, other)
        
        def associator(self, B, C):
            """
            Return the associator isomorphism (A⊗B)⊗C → A⊗(B⊗C).
            
            EXAMPLES::
            
                sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
                sage: A = RMod(ZZ).WithBasis(['a'])
                sage: B = RMod(ZZ).WithBasis(['b']) 
                sage: C = RMod(ZZ).WithBasis(['c'])
                sage: alpha = A.associator(B, C)
                sage: alpha.domain() == (A.monoidal_product(B)).monoidal_product(C)
                True
                sage: alpha.codomain() == A.monoidal_product(B.monoidal_product(C))
                True
            """
            raise NotImplementedError
        
        def left_unitor(self):
            """
            Return the left unitor isomorphism I⊗A → A.
            
            EXAMPLES::
            
                sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
                sage: M = RMod(ZZ).WithBasis(['x', 'y'])
                sage: lambda_M = M.left_unitor()
                sage: I = C.monoidal_unit()
                sage: lambda_M.domain() == I.monoidal_product(M)
                True
                sage: lambda_M.codomain() == M
                True
            """
            raise NotImplementedError
        
        def right_unitor(self):
            """
            Return the right unitor isomorphism A⊗I → A.
            
            EXAMPLES::
            
                sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
                sage: M = RMod(ZZ).WithBasis(['x', 'y'])
                sage: rho_M = M.right_unitor()
                sage: I = C.monoidal_unit()
                sage: rho_M.domain() == M.monoidal_product(I)
                True
                sage: rho_M.codomain() == M
                True
            """
            raise NotImplementedError
        
        def braiding(self, other):
            """
            Return the braiding isomorphism A⊗B → B⊗A.
            
            For symmetric monoidal categories, β_{B,A} ∘ β_{A,B} = id.
            
            EXAMPLES::
            
                sage: C = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: beta_MN = M.braiding(N)
                sage: beta_MN.domain() == M.monoidal_product(N)
                True
                sage: beta_MN.codomain() == N.monoidal_product(M)
                True
                
                sage: # Symmetry: double braiding is identity
                sage: beta_NM = N.braiding(M)
                sage: (beta_NM * beta_MN).is_identity()
                True
            """
            raise NotImplementedError

# Natural operations for R-modules capturing split Grothendieck ring structure

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
    
        sage: from sage.categories.rmodules import RModules
        sage: C = RModules(ZZ)
        sage: C
        Category of R-modules over Integer Ring
        sage: C.super_categories()
        [Category of modules over Integer Ring]
        
        sage: # Base category works for any R-module
        sage: M = RMod(ZZ).WithBasis(['a', 'b', 'c'])  # Free module with basis
        sage: M in RModules(ZZ)
        True
        
        sage: # Symmetric monoidal structure can be made explicit
        sage: C_tensor = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
        sage: C_tensor
        Category of symmetric monoidal R-modules over Integer Ring with tensor product
        
        sage: # For homotopy theory: track smash product structure
        sage: # C_smash = PointedModules(ZZ).SymmetricMonoidal('smash_product', S0_mod)
        
        sage: TestSuite(C).run()
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
        from sage.categories.abelian_categories import AbelianCategories
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
            
            sage: # Can apply to modules to get monoidal operations
            sage: M = RMod(ZZ).WithBasis(['a', 'b'])
            sage: M_tensor = M.with_category(C_tensor)
            sage: # Now M_tensor has monoidal_product, associator, etc.
        """
        return SymmetricMonoidal(self, monoidal_product, unit)
    
    class ParentMethods:
        """
        Methods available on ALL R-module parent objects.
        
        These methods are automatically available on any parent
        in the category RModules(R), whether free, torsion, or mixed.
        
        Some methods (subobject, quotient) come from AbelianCategories,
        while others are specific to modules over rings.
        
        Methods requiring bases are in RModules(R).WithBasis().ParentMethods.
        """
        
        # Note: subobject() and quotient() are inherited from
        # AbelianCategories.ParentMethods, but we specialize them
        # for the module context
        
        def submodule(self, generators, check=True):
            """
            Return the submodule generated by the given elements.
            
            This specializes the general subobject() method from abelian
            categories to the R-module context where we generate by elements.
            
            INPUT:
            - generators -- list of elements of this module
            - check -- whether to verify generators are in this module
            
            EXAMPLES::
            
                sage: # Works for free modules
                sage: M = RMod(ZZ).WithBasis(['e1', 'e2', 'e3'])
                sage: e1, e2, e3 = M.gens()
                sage: S = M.submodule([e1 + e2, e2 + e3])
                sage: S.rank()  # Free submodule has well-defined rank
                2
                
                sage: # Would also work for torsion modules
                sage: # T = ZZ/6  # as ZZ-module (when implemented)
                sage: # S = T.submodule([3])  # submodule <3> = {0, 3}
            """
            # This would call the more general subobject() with
            # module-specific generation
            raise NotImplementedError
        
        def quotient(self, submodule):
            """
            Return the quotient module by a submodule.
            
            This inherits from AbelianCategories but ensures the result
            remains in the appropriate module category.
            
            INPUT:
            - submodule -- submodule to quotient by
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                sage: x, y, z = M.gens()
                sage: S = M.submodule([x + y])
                sage: Q = M.quotient(S)
                sage: # Q is isomorphic to ZZ^2 (free module of rank 2)
                sage: Q in RModules(ZZ)
                True
            """
            # Inherited from AbelianCategories but ensures correct category
            raise NotImplementedError
        
        def hom(self, codomain, images_of_generators):
            """
            Create a module homomorphism.
            
            Universal for all R-modules - homomorphisms determined by 
            images of any generating set.
            
            INPUT:
            - codomain -- target R-module
            - images_of_generators -- list of images (implementation-dependent)
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                sage: a, b = M.gens()
                sage: x, y, z = N.gens()
                sage: phi = M.hom(N, [2*x + y, x - 3*z])
                sage: phi(a)
                2*x + y
            """
            raise NotImplementedError
        
        def direct_sum(self, *others):
            """
            Direct sum with other modules.
            
            The direct sum M ⊕ N is the biproduct in the abelian category
            of R-modules (both product and coproduct).
            
            This inherits the general biproduct from AbelianCategories but
            ensures proper module structure.
            
            INPUT:
            - others -- other R-modules to form direct sum with
            
            OUTPUT:
            The direct sum module
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                sage: MN = M.direct_sum(N)
                sage: MN.rank()
                5  # 2 + 3 = 5
                
                sage: # Has both projections and injections
                sage: pi1 = MN.projection(0)  # MN → M
                sage: pi2 = MN.projection(1)  # MN → N
                sage: i1 = M.injection(MN)    # M → MN
                sage: i2 = N.injection(MN)    # N → MN
            """
            # Calls the biproduct from AbelianCategories
            raise NotImplementedError
        
        def cartesian_product(self, *others):
            """
            Cartesian product with other modules.
            
            The cartesian product M × N has underlying set M × N with
            componentwise operations.
            
            INPUT:
            - others -- other R-modules to form product with
            
            OUTPUT:
            The cartesian product module
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: MN = M.cartesian_product(N)
                sage: MN.rank()
                4  # 2 + 2 = 4
            """
            raise NotImplementedError
        
        def tensor_product(self, *others):
            """
            Tensor product with other modules.
            
            The tensor product M ⊗_R N satisfies the universal property
            for bilinear maps.
            
            INPUT:
            - others -- other R-modules to tensor with
            
            OUTPUT:
            The tensor product module
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: MN = M.tensor_product(N)
                sage: MN.rank()
                4  # 2 × 2 = 4
            """
            raise NotImplementedError
        
        def is_free(self):
            """
            Test if this module is free.
            
            A module is free if it is isomorphic to a direct sum of
            copies of R (has a basis).
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b', 'c'])
                sage: M.is_free()
                True
                
                sage: # Torsion module example (when implemented)
                sage: # T = ZZ.quotient(6*ZZ)  # Z/6Z as ZZ-module
                sage: # T.is_free()
                sage: # False
                
                sage: # Submodules of free modules over PIDs are free
                sage: N = M.submodule([M.basis()[0] + M.basis()[1]])
                sage: N.is_free()
                True  # Over a PID
            """
            raise NotImplementedError
        
        def is_torsion(self):
            """
            Test if this module is a torsion module.
            
            A module M is torsion if for every m in M, there exists
            a non-zero r in R such that r*m = 0.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: M.is_torsion()
                False  # Free modules are torsion-free
                
                sage: # Finite abelian groups are torsion ZZ-modules
                sage: # T = ZZ.quotient(12*ZZ)  # Z/12Z
                sage: # T.is_torsion()
                sage: # True
                
                sage: # Mixed modules have torsion submodule
                sage: # M_mixed = ZZ^2 + ZZ/6  # Free ⊕ Torsion
                sage: # M_mixed.is_torsion()
                sage: # False
                sage: # M_mixed.torsion_submodule().is_torsion()
                sage: # True
            """
            raise NotImplementedError
        
        def is_projective(self):
            """
            Test if this module is projective.
            
            A module P is projective if every epimorphism onto P splits,
            equivalently if P is a direct summand of a free module.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['x', 'y'])
                sage: M.is_projective()
                True  # Free implies projective
                
                sage: # Over PIDs, projective = free
                sage: # But over general rings, projective ⊃ free
                
                sage: # Example over non-PID (when implemented)
                sage: # R = ZZ[x,y]  # Not a PID
                sage: # I = R.ideal([x,y])  # Projective but not free
                sage: # I.is_projective()
                sage: # True
                sage: # I.is_free()
                sage: # False
            """
            raise NotImplementedError
        
        def is_injective(self):
            """
            Test if this module is injective.
            
            A module I is injective if every monomorphism from I extends,
            equivalently if Hom(-, I) is exact.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: # Over ZZ, Q and Q/Z are injective
                sage: # Q_mod = QQ.as_ZZ_module()  # When implemented
                sage: # Q_mod.is_injective()
                sage: # True
                
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: M.is_injective()
                False  # ZZ is not injective as ZZ-module
                
                sage: # Over fields, every module is injective
                sage: V = RMod(QQ).WithBasis(['x', 'y'])
                sage: V.is_injective()
                True  # Vector spaces are injective
            """
            raise NotImplementedError
        
        def is_finitely_generated(self):
            """
            Test if this module is finitely generated.
            
            A module is finitely generated if it has a finite generating set.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b', 'c'])
                sage: M.is_finitely_generated()
                True  # Has finite basis
                
                sage: # Polynomial ring as module over itself
                sage: # R = PolynomialRing(QQ, 'x')
                sage: # R_mod = R.as_module()  # When implemented
                sage: # R_mod.is_finitely_generated()
                sage: # True  # Generated by 1
                
                sage: # Infinite direct sum is not f.g.
                sage: # M_inf = DirectSum([ZZ for i in Naturals()])
                sage: # M_inf.is_finitely_generated()
                sage: # False
            """
            raise NotImplementedError
        
        def dual(self):
            """
            Return the dual module Hom(M, R).
            
            The dual of any R-module M is the module of R-linear
            homomorphisms from M to R, with pointwise operations.
            
            OUTPUT:
            The dual module M* = Hom_R(M, R)
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: M_dual = M.dual()
                sage: # M* has dual basis {a*, b*} with a*(a)=1, a*(b)=0, etc.
                
                sage: # For f.g. free modules, M** ≅ M
                sage: M_double_dual = M_dual.dual()
                sage: M_double_dual.is_isomorphic(M)
                True  # Natural isomorphism for f.g. free
                
                sage: # Torsion modules can have zero dual
                sage: # T = ZZ.quotient(6*ZZ)  # Z/6Z
                sage: # T_dual = T.dual()
                sage: # T_dual.is_zero()
                sage: # True  # Hom(Z/6Z, Z) = 0
                
                sage: # Evaluation pairing M* × M → R
                sage: # <f, m> = f(m) for f in M*, m in M
            """
            raise NotImplementedError
        
        def __add__(self, other):
            """
            Syntactic sugar: M + N for direct sum M ⊕ N.
            
            Direct sum monoidal structure with unit 0. This captures the
            additive structure in the split Grothendieck ring K₀(R).
            
            INPUT:
            - other -- another R-module
            
            OUTPUT:
            The direct sum self ⊕ other
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                sage: MN = M + N  # Direct sum M ⊕ N
                sage: MN.rank()
                5  # rank(M) + rank(N) = 2 + 3 = 5
                
                sage: # Equivalent to explicit method
                sage: MN_explicit = M.direct_sum(N)
                sage: MN.is_isomorphic(MN_explicit)
                True
                
                sage: # Chain multiple direct sums
                sage: P = RMod(ZZ).WithBasis(['u'])
                sage: MNP = M + N + P  # M ⊕ N ⊕ P
                sage: MNP.rank()
                6  # 2 + 3 + 1 = 6
                
                sage: # Split Grothendieck ring equations work naturally
                sage: # M = M/N + N  (when N ⊆ M)
                sage: N_sub = M.submodule([M.basis()[0]])  # Submodule <a>
                sage: Q = M / N_sub
                sage: M.is_isomorphic(Q + N_sub)
                True
            """
            return self.direct_sum(other)
        
        def __mul__(self, other):
            """
            Syntactic sugar: M * N for cartesian product M × N.
            
            Cartesian product monoidal structure with unit 0 (terminal object).
            This is the third monoidal structure on R-modules.
            
            INPUT:
            - other -- another R-module
            
            OUTPUT:
            The cartesian product self × other
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: MN = M * N  # Cartesian product M × N
                sage: MN.rank()
                4  # rank(M) + rank(N) = 2 + 2 = 4
                
                sage: # Has projection maps
                sage: pi1 = MN.projection(0)  # M × N → M
                sage: pi2 = MN.projection(1)  # M × N → N
                
                sage: # Universal property: for any f: X → M, g: X → N
                sage: # there exists unique h: X → M × N with π₁∘h = f, π₂∘h = g
                
                sage: # Equivalent to explicit method
                sage: MN_explicit = M.cartesian_product(N)
                sage: MN.is_isomorphic(MN_explicit)
                True
                
                sage: # Chain multiple cartesian products
                sage: P = RMod(ZZ).WithBasis(['u'])
                sage: MNP = M * N * P  # M × N × P
                sage: MNP.rank()
                4  # 2 × 2 × 1 = 4
            """
            return self.cartesian_product(other)
        
        def __matmul__(self, other):
            """
            Syntactic sugar: M @ N for tensor product M ⊗ N.
            
            Tensor product monoidal structure with unit R. This captures the
            multiplicative structure in the split Grothendieck ring K₀(R).
            
            INPUT:
            - other -- another R-module
            
            OUTPUT:
            The tensor product self ⊗ other
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: MN = M @ N  # Tensor product M ⊗ N
                sage: MN.rank()
                4  # rank(M) × rank(N) = 2 × 2 = 4
                
                sage: # Equivalent to explicit method
                sage: MN_explicit = M.tensor_product(N)
                sage: MN.is_isomorphic(MN_explicit)
                True
                
                sage: # Chain multiple tensor products
                sage: P = RMod(ZZ).WithBasis(['u'])
                sage: MNP = M @ N @ P  # (M ⊗ N) ⊗ P
                sage: MNP.rank()
                4  # 2 × 2 × 1 = 4
                
                sage: # Unit law: M @ R ≅ M
                sage: R_mod = RMod(ZZ).WithBasis(['1'])  # R as module
                sage: MR = M @ R_mod
                sage: MR.is_isomorphic(M)
                True
            """
            return self.tensor_product(other)
        
        def __truediv__(self, submodule):
            """
            Syntactic sugar: M / N for quotient module M/N.
            
            Quotient by submodule. This enables split Grothendieck ring
            equations like M = M/N + N to be written naturally.
            
            INPUT:
            - submodule -- a submodule of this module to quotient by
            
            OUTPUT:
            The quotient module self/submodule
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                sage: x, y, z = M.gens()
                sage: N = M.submodule([x + y, z])  # Submodule <x+y, z>
                sage: Q = M / N  # Quotient module M/N
                sage: Q.rank()
                1  # dim(M) - dim(N) = 3 - 2 = 1
                
                sage: # Split Grothendieck ring equation: M = M/N + N
                sage: M.is_isomorphic((M / N) + N)
                True
                
                sage: # Equivalent to explicit method
                sage: Q_explicit = M.quotient(N)
                sage: Q.is_isomorphic(Q_explicit)
                True
                
                sage: # Chain quotients (when well-defined)
                sage: P = M.submodule([x])
                sage: R = N.submodule([z])  # R ⊆ N ⊆ M
                sage: # (M/R)/(N/R) ≅ M/N by third isomorphism theorem
                sage: MR = M / R
                sage: NR = N / R  # N/R as submodule of M/R
                sage: Q_iso = MR / NR
                sage: Q_iso.is_isomorphic(M / N)
                True
            
            WARNING:
            The submodule must actually be a submodule of self.
            Otherwise, the quotient is not well-defined.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])  # Not a submodule of M
                sage: M / N
                Traceback (most recent call last):
                ...
                ValueError: N is not a submodule of M
            """
            return self.quotient(submodule)
    
    class ElementMethods:
        """
        Methods available on ALL R-module elements.
        
        These methods are automatically available on any element
        of a parent in RModules(R), whether in free, torsion, or mixed modules.
        
        Methods requiring basis coordinates are in RModules(R).WithBasis().ElementMethods.
        """
        
        def is_zero(self):
            """
            Check if this is the zero element.
            
            Fundamental operation valid for all R-module elements.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['e', 'f'])
                sage: e, f = M.gens()
                sage: (e - e).is_zero()
                True
                sage: e.is_zero()
                False
                
                sage: # Would also work for torsion module elements
                sage: # (when torsion modules are implemented)
            """
            raise NotImplementedError
        
        def __add__(self, other):
            """
            Addition of R-module elements.
            
            Universal for all R-modules - abelian group operation.
            Usually inherited from base element classes.
            """
            raise NotImplementedError
        
        def __rmul__(self, scalar):
            """
            Scalar multiplication by ring elements.
            
            Universal R-module operation: r * v for r in R, v in module.
            Usually inherited from base element classes.
            """
            raise NotImplementedError
    
    class HomsetMethods:
        """
        Methods for morphisms between R-modules.
        
        Most morphism methods (kernel, cokernel, image, etc.) are inherited
        from AbelianCategories. Here we add R-module specific operations.
        """
        
        # Note: kernel(), cokernel(), image(), is_monomorphism(), 
        # is_epimorphism(), is_isomorphism() are all inherited from
        # AbelianCategories.HomsetMethods
        
        def tensor_product(self, other):
            """
            Tensor product of morphisms.
            
            For f: M → N and g: P → Q, returns f ⊗ g: M ⊗ P → N ⊗ Q.
            
            This is specific to modules (not general abelian categories).
            
            INPUT:
            - other -- another R-module morphism
            
            OUTPUT:
            The tensor product morphism
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: f = M.hom(N, [x + y, x - y])
                sage: g = N.hom(M, [a, b])
                sage: h = f.tensor_product(g)  # (M ⊗ N) → (N ⊗ M)
                sage: # h sends a ⊗ x ↦ (x+y) ⊗ a, etc.
            """
            raise NotImplementedError
        
        def hom_tensor_adjunction(self, other):
            """
            The tensor-hom adjunction isomorphism.
            
            For modules M, N, P, gives the natural isomorphism:
            Hom(M ⊗ N, P) ≅ Hom(M, Hom(N, P))
            
            This is specific to the monoidal structure of R-modules.
            
            EXAMPLES::
            
                sage: M = RMod(ZZ).WithBasis(['a', 'b'])
                sage: N = RMod(ZZ).WithBasis(['x', 'y'])
                sage: P = RMod(ZZ).WithBasis(['u', 'v'])
                sage: # Morphism f: M ⊗ N → P corresponds to
                sage: # Morphism g: M → Hom(N, P) via adjunction
            """
            raise NotImplementedError
    
```

## Axioms: Free, FinitelyGenerated, and WithBasis Objects

The RModules category provides three key axioms that capture different module properties:

1. **FinitelyGenerated**: Module has a finite generating set (may include torsion)
2. **Free**: Module satisfies the universal property (is projective, has some basis)
3. **WithBasis**: Free module with distinguished basis (additional structure)

Key relationships:
- Free + FinitelyGenerated = has finite basis (over nice rings)
- WithBasis ⊆ Free (having a basis implies being free)
- WithBasis + finite basis ⊆ FinitelyGenerated
- WithBasis + infinite basis ⊈ FinitelyGenerated

```python
class RModules(Category_module):
    # ... (base category definition above) ...
    
    class Free(CategoryWithAxiom):
        """
        The axiom of Free objects in RModules(R).
        
        Free R-modules are characterized by the universal property:
        For any R-module M and any function f: S → M from a set S,
        there exists a unique R-module homomorphism φ: R^(S) → M
        extending f, where R^(S) is the free R-module on S.
        
        Note: Having a basis implies being free, but being free doesn't
        specify a particular basis. The WithBasis axiom adds a distinguished
        basis as additional data.
        
        Free R-modules over nice rings (PIDs, fields) satisfy:
        - Every submodule of a free module is free (over PIDs)
        - Well-defined rank (cardinality of any basis)
        - Direct sums of free modules are free
        - Free modules are projective
        
        EXAMPLES::
        
            sage: C = RModules(ZZ).Free()
            sage: C
            Category of free R-modules over Integer Ring
            
            sage: # Free modules have well-defined rank
            sage: M = RMod(ZZ).Free(rank=3)
            sage: M.rank()
            3
            
            sage: # Without WithBasis, no specific basis is chosen
            sage: M.basis()
            Traceback (most recent call last):
            ...
            AttributeError: Free module needs WithBasis axiom for basis access
            
            sage: # Universal property: any map from generators extends uniquely
            sage: # (This would be implemented via hom() method)
        """
        
        class ParentMethods:
            """Methods specific to free R-modules."""
            
            def rank(self):
                """
                Return the rank of this free R-module.
                
                The rank is well-defined for free modules over PIDs.
                For general rings, this is the cardinality of any basis.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).Free(rank=5)
                    sage: M.rank()
                    5
                    
                    sage: # All bases have the same cardinality
                    sage: N = RMod(QQ).WithBasis(['a', 'b', 'c'])
                    sage: N.rank()
                    3
                """
                raise NotImplementedError
    
    class FinitelyGenerated(CategoryWithAxiom):
        """
        The axiom of finitely generated objects in RModules(R).
        
        An R-module M is finitely generated if there exists a finite subset
        S ⊂ M such that M = ⟨S⟩_R (the R-span of S).
        
        Key properties:
        - Over Noetherian rings, submodules of f.g. modules are f.g.
        - Quotients of f.g. modules are f.g.
        - Finite direct sums of f.g. modules are f.g.
        - Over a PID, f.g. modules satisfy the structure theorem
        
        Note: Finitely generated does NOT imply free! Examples:
        - Z/nZ is f.g. as Z-module but not free
        - k[x,y]/(x,y) is f.g. as k[x,y]-module but not free
        
        EXAMPLES::
        
            sage: C = RModules(ZZ).FinitelyGenerated()
            sage: C
            Category of finitely generated R-modules over Integer Ring
            
            sage: # Free modules with finite basis are finitely generated
            sage: M = RMod(ZZ).WithBasis(['a', 'b', 'c'])
            sage: M in C
            True
            
            sage: # Torsion modules can be finitely generated
            sage: # T = ZZ.quotient(6*ZZ)  # Z/6Z
            sage: # T in C
            sage: # True
            
            sage: # Infinite direct sums are not finitely generated
            sage: # M_inf = DirectSum([ZZ for i in Naturals()])
            sage: # M_inf in C
            sage: # False
        """
        
        class ParentMethods:
            """Methods specific to finitely generated R-modules."""
            
            def generators(self):
                """
                Return a finite generating set for this module.
                
                Note: The generating set may not be minimal or unique.
                For free modules with basis, returns the basis.
                For general f.g. modules, returns any finite generating set.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).WithBasis(['x', 'y'])
                    sage: M.generators()
                    [x, y]  # Basis is a generating set
                    
                    sage: # For quotients
                    sage: # Q = M.quotient(M.submodule([x + y]))
                    sage: # Q.generators()
                    sage: # [x_bar, y_bar]  # Images of original generators
                """
                raise NotImplementedError
            
            def number_of_generators(self):
                """
                Return the minimum number of generators needed.
                
                For free modules, this is the rank.
                For general modules, this is the minimal cardinality
                of any generating set.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).WithBasis(['a', 'b', 'c'])
                    sage: M.number_of_generators()
                    3
                    
                    sage: # Cyclic modules need only one generator
                    sage: # C = ZZ.quotient(12*ZZ)
                    sage: # C.number_of_generators()
                    sage: # 1
                """
                raise NotImplementedError

    class WithBasis(CategoryWithAxiom):
        """
        The axiom of WithBasis objects in RModules(R).
        
        These are free R-modules equipped with a distinguished basis.
        Having a basis is additional structure/data on a free module,
        analogous to a basepoint on a topological space.
        
        Mathematically: A module with basis = (Free module, chosen basis)
        
        This axiom provides:
        - Access to the chosen basis
        - Coordinate representations relative to this basis
        - Conversions between symbolic and numerical representations
        
        Important: Over nice rings (fields, PIDs), having a finite basis
        implies being finitely generated. For infinite basis, the module
        is NOT finitely generated.
        
        EXAMPLES::
        
            sage: C = RModules(ZZ).WithBasis() 
            sage: C
            Category of free R-modules with basis over Integer Ring
            
            sage: M = RMod(ZZ).WithBasis(['e1', 'e2', 'e3'])
            sage: M in C
            True
            
            sage: # The basis is the additional data
            sage: list(M.basis())
            [e1, e2, e3]
            
            sage: # Different bases give different WithBasis structures
            sage: # on the same underlying free module
            sage: N = RMod(ZZ).WithBasis(['a', 'b', 'c']) 
            sage: # M and N are isomorphic as free modules but have different basis data
            
            sage: # Finite basis implies finitely generated
            sage: M in RModules(ZZ).FinitelyGenerated()
            True
            
            sage: # Infinite basis means NOT finitely generated
            sage: # M_inf = RMod(ZZ).WithBasis(Naturals())  # Basis indexed by ℕ
            sage: # M_inf in RModules(ZZ).Free()
            sage: # True
            sage: # M_inf in RModules(ZZ).FinitelyGenerated()
            sage: # False
        """
        
        def extra_super_categories(self):
            """
            Modules with basis are free modules with additional structure.
            
            Having a basis implies being free (by definition).
            If the basis is finite, also implies finitely generated.
            
            EXAMPLES::
            
                sage: RModules(ZZ).WithBasis().super_categories()
                [Category of free R-modules over Integer Ring, ...]
            """
            # Always free
            cats = [self.base_category().Free()]
            
            # Check if we should add FinitelyGenerated
            # This would be determined at parent construction time
            # based on whether the basis is finite
            # For now, we just note this in documentation
            
            return cats
        
        class ParentMethods:
            """Methods for free R-modules with chosen basis."""
            
            def basis(self):
                """
                Return the chosen basis of this R-module.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                    sage: list(M.basis())
                    [x, y, z]
                """
                raise NotImplementedError("Implement in parent class")
            
            def _from_vector(self, vec):
                """
                Internal: Create a module element from a coordinate vector.
                
                Uses the chosen basis for coordinate interpretation.
                This is an internal method - users should use M([...]) syntax.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).WithBasis(['x', 'y'])
                    sage: # Internal method, not for users:
                    sage: M._from_vector([3, -1])  # Don't use directly
                    3*x - y
                """
                raise NotImplementedError
            
            def _element_constructor_(self, x):
                """
                Construct elements from various representations.
                
                This enables M([1, 2, 3]) notation for coordinate vectors.
                Automatically converts entries to base ring elements.
                
                INPUT:
                - x -- Can be:
                  * list or tuple of coordinates
                  * vector over any ring (will convert to base ring)
                  * existing module element
                  * 0 for zero element
                
                EXAMPLES::
                
                    sage: M.<e,f> = RMod(ZZ)
                    sage: M([1, 0])
                    e
                    sage: M([2, 3])
                    2*e + 3*f
                    sage: M([-1, 4])
                    -e + 4*f
                    
                    sage: # Automatic conversion to base ring
                    sage: M([1/2, 3/4])  # Fractions to ZZ fails
                    Traceback (most recent call last):
                    ...
                    TypeError: no conversion of this rational to integer
                    
                    sage: N.<a,b> = RMod(QQ)
                    sage: N([1/2, 3/4])  # Works for QQ-modules
                    1/2*a + 3/4*b
                    sage: N([1, 2])  # Integers coerce to QQ
                    a + 2*b
                    
                    sage: # From vectors
                    sage: v = vector(ZZ, [3, -1])
                    sage: M(v)
                    3*e - f
                    sage: w = vector(QQ, [1/2, 2])  # Different ring
                    sage: N(w)  # Converts to base ring
                    1/2*a + 2*b
                    
                    sage: # Lists are converted to module elements
                    sage: M([1, 0]) == e
                    True
                    sage: M([2, 3]) == 2*e + 3*f
                    True
                    
                    sage: # But raw lists are not module elements
                    sage: [1, 0] in M
                    False
                    sage: M([1, 0]) in M
                    True
                    sage: 2*e != [2, 0]
                    True
                    
                    sage: # Cannot mix symbolic and coordinate notation
                    sage: 2*e + [0, 2]
                    Traceback (most recent call last):
                    ...
                    TypeError: unsupported operand parent(s) for +
                """
                if x == 0:
                    return self.zero()
                    
                if isinstance(x, (list, tuple)):
                    # Convert list/tuple to vector over base ring
                    R = self.base_ring()
                    try:
                        # Try to convert each entry to base ring
                        vec = vector(R, [R(c) for c in x])
                        return self._from_vector(vec)
                    except (TypeError, ValueError) as err:
                        # Provide helpful error message
                        raise TypeError(f"Cannot convert coordinates to {R}: {err}")
                        
                # Handle vectors (from any ring)
                if hasattr(x, 'parent') and hasattr(x.parent(), 'is_vector_space'):
                    R = self.base_ring()
                    try:
                        # Convert vector entries to base ring
                        vec = vector(R, [R(c) for c in x])
                        return self._from_vector(vec)
                    except (TypeError, ValueError) as err:
                        raise TypeError(f"Cannot convert vector entries to {R}: {err}")
                
                # Default element construction for other types
                return super()._element_constructor_(x)
            
            def _to_vector(self, element):
                """
                Internal: Convert a module element to coordinate vector.
                
                This is an internal method - users should use element.to_vector().
                
                EXAMPLES::
                
                    sage: M = RMod(QQ).WithBasis(['a', 'b', 'c'])
                    sage: a, b, c = M.gens()
                    sage: v = 2*a - 3*b + c
                    sage: # Internal use only:
                    sage: M._to_vector(v)
                    (2, -3, 1)
                """
                raise NotImplementedError
            
            def coordinate_module(self):
                """
                Return the coordinate module (isomorphic FreeModule).
                
                EXAMPLES::
                
                    sage: M = RMod(QQ).WithBasis(['a', 'b'])
                    sage: F = M.coordinate_module()
                    sage: F.rank() == M.rank()
                    True
                """
                raise NotImplementedError
        
        class ElementMethods:
            """Methods for elements of modules with basis."""
            
            def to_vector(self):
                """
                Convert this element to a coordinate vector.
                
                Returns a vector over the base ring with coordinates
                relative to the module's basis.
                
                EXAMPLES::
                
                    sage: M = RMod(QQ).WithBasis(['a', 'b', 'c'])
                    sage: a, b, c = M.gens()
                    sage: v = a + 2*b - 3*c
                    sage: v.to_vector()
                    (1, 2, -3)
                    
                    sage: # Type is vector over base ring
                    sage: type(v.to_vector())
                    <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>
                    sage: v.to_vector().parent()
                    Vector space of dimension 3 over Rational Field
                """
                return self.parent()._to_vector(self)
            
            def _numerical_(self):
                """
                Numerical representation via n() function.
                
                This allows using n(element) to get coordinate vector.
                
                EXAMPLES::
                
                    sage: M.<e,f> = RMod(ZZ)
                    sage: n(e)
                    (1, 0)
                    sage: n(2*e + 3*f)
                    (2, 3)
                    sage: n(e - f)
                    (1, -1)
                    
                    sage: # The n() function calls _numerical_
                    sage: (3*e + 2*f)._numerical_()
                    (3, 2)
                """
                return self.to_vector()
            
            def coefficient(self, basis_key):
                """
                Return the coefficient of a basis element.
                
                EXAMPLES::
                
                    sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
                    sage: x, y, z = M.gens()
                    sage: v = 3*x - 2*y + 5*z
                    sage: v.coefficient('y')
                    -2
                """
                raise NotImplementedError
            
            def support(self):
                """
                Return the support (non-zero basis elements).
                
                EXAMPLES::
                
                    sage: M = RMod(QQ).WithBasis(['a', 'b', 'c'])
                    sage: a, b, c = M.gens()
                    sage: v = 2*a - 3*c
                    sage: v.support()
                    ['a', 'c']
                """
                raise NotImplementedError
```

## Parent Class: RModule_with_basis

```python
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.indexed_generators import IndexedGenerators

class RModule_with_basis(UniqueRepresentation, Parent, IndexedGenerators):
    """
    An R-module with symbolic basis.
    
    This is the concrete parent class for R-modules. It provides:
    - Symbolic basis with natural notation
    - Efficient conversion to numerical representations
    - Integration with the category framework
    
    INPUT:
    - base_ring -- the base ring R
    - basis -- list of basis element names (optional)
    - category -- the category (defaults to RModules(base_ring))
    - prefix -- prefix for basis elements
    - **kwds -- additional options for IndexedGenerators
    
    EXAMPLES::
    
        sage: from sage.modules.rmodule_with_basis import RModule_with_basis
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
        sage: M
        Free module over Integer Ring with basis {a, b, c}
        
        sage: M.an_element()
        2*a + 3*b + c
        
        sage: M in RModules(ZZ)
        True
    """
    
    def __init__(self, base_ring, basis=None, category=None, prefix=None, **kwds):
        """
        Initialize an R-module with symbolic basis.
        
        TESTS::
        
            sage: M = RModule_with_basis(QQ, basis=['x', 'y'])
            sage: TestSuite(M).run()
        """
        # Set up category
        if category is None:
            from sage.categories.rmodules import RModules
            category = RModules(base_ring)
        
        # Initialize parent
        Parent.__init__(self, base=base_ring, category=category)
        
        # Set up basis
        if basis is not None:
            self._basis_keys = basis
        else:
            # Will be set by _first_ngens for generator assignment
            self._basis_keys = None
            
        # Initialize generators
        if self._basis_keys is not None:
            IndexedGenerators.__init__(self, self._basis_keys, prefix=prefix, **kwds)
    
    def _element_constructor_(self, x=None):
        """
        Construct a module element.
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(QQ, basis=['a', 'b', 'c'])
            sage: M(0)
            0
            sage: M({0: 1, 2: -1})  # By index
            a - c
            sage: M({'a': 2, 'c': 3})  # By name
            2*a + 3*c
            sage: M([1, 0, -1])  # From list
            a - c
        """
        from sage.modules.rmodule_element import RModuleElement
        
        if x is None or x == 0:
            return self.zero()
            
        if isinstance(x, RModuleElement) and x.parent() is self:
            return x
            
        # Handle various input formats
        # ... implementation details ...
        
    def _first_ngens(self, n):
        """
        Used by the preparser for generator assignment.
        
        EXAMPLES::
        
            sage: M.<x,y,z> = RMod(ZZ)  # Calls this method
            sage: M._first_ngens(3)
            (x, y, z)
        """
        if self._basis_keys is None:
            # Set up basis from generator assignment
            self._basis_keys = [f'e{i}' for i in range(n)]
            IndexedGenerators.__init__(self, self._basis_keys)
            
        return self.gens()[:n]
    
    # Implement the required ParentMethods
    def basis(self):
        """
        Return the basis of this module.
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(ZZ, basis=['x', 'y', 'z'])
            sage: list(M.basis())
            [x, y, z]
        """
        from sage.sets.family import Family
        return Family(self._indices, self.monomial)
    
    def _from_vector(self, vec):
        """
        Internal: Create element from coordinate vector.
        
        This is an internal method - users should use M([...]) syntax.
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(ZZ, basis=['a', 'b'])
            sage: # Internal use only:
            sage: M._from_vector(vector(ZZ, [3, -1]))
            3*a - b
        """
        # Implementation creates element from coordinates
        coeffs = {i: c for i, c in enumerate(vec) if c != 0}
        return self._element_constructor_(coeffs)
    
    def _to_vector(self, element):
        """
        Internal: Convert element to coordinate vector.
        
        This is an internal method - users should use element.to_vector().
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(QQ, basis=['x', 'y'])
            sage: x, y = M.gens()
            sage: v = 2*x - 3*y
            sage: # Internal use only:
            sage: M._to_vector(v)
            (2, -3)
        """
        # Implementation extracts coordinates
        from sage.modules.free_module import FreeModule
        V = FreeModule(self.base_ring(), len(self._basis_keys))
        coords = [element.coefficient(key) for key in self._basis_keys]
        return V(coords)
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
            Free module over Integer Ring with basis {a, b, c}
        """
        return f"Free module over {self.base_ring()} with basis {{{', '.join(map(str, self._basis_keys))}}}"
```

## Element Class: RModuleElement

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class RModuleElement(IndexedFreeModuleElement):
    """
    Element of an R-module with symbolic and numerical representations.
    
    Supports natural arithmetic and efficient conversion.
    
    EXAMPLES::
    
        sage: M.<e,f> = RMod(ZZ)
        sage: v = 2*e + 3*f
        sage: w = e - f
        sage: v + w
        3*e + 2*f
        sage: 4*v
        8*e + 12*f
    """
    
    def to_vector(self):
        """
        Convert this element to a coordinate vector.
        
        EXAMPLES::
        
            sage: M.<a,b,c> = RMod(QQ)
            sage: v = a + 2*b - 3*c
            sage: v.to_vector()
            (1, 2, -3)
        """
        return self.parent()._to_vector(self)
    
    def coefficient(self, basis_key):
        """
        Return the coefficient of a basis element.
        
        EXAMPLES::
        
            sage: M.<x,y,z> = RMod(ZZ)
            sage: v = 3*x - 2*y + 5*z
            sage: v.coefficient('y')
            -2
            sage: v.coefficient('w')  # Not a basis element
            0
        """
        return self.get(basis_key, self.base_ring().zero())
    
    def support(self):
        """
        Return the support (non-zero basis elements).
        
        EXAMPLES::
        
            sage: M.<a,b,c> = RMod(QQ)
            sage: v = 2*a - 3*c
            sage: v.support()
            ['a', 'c']
        """
        return [key for key in self._monomial_coefficients if self[key] != 0]
    
    def is_zero(self):
        """
        Check if this is the zero element.
        
        EXAMPLES::
        
            sage: M.<e,f> = RMod(ZZ)
            sage: (e - e).is_zero()
            True
            sage: e.is_zero()
            False
        """
        return len(self._monomial_coefficients) == 0
```

## Factory Functions

```python
def RMod(base_ring, *args, **kwds):
    """
    Factory function for constructing R-modules.
    
    This function provides access to the axiom-based RModules category structure.
    By default, creates free R-modules with chosen basis (WithBasis axiom).
    
    USAGE PATTERNS:
    
    1. RMod(R) - Returns category factory for further axiom specification
    2. RMod(R).WithBasis(...) - Creates free R-module with chosen basis  
    3. RMod(R).Free(...) - Creates free R-module (no specific basis)
    4. Direct construction with basis - Shorthand for WithBasis
    
    INPUT:
    - base_ring -- the base ring R
    - args/kwds -- depends on usage pattern (see examples)
    
    EXAMPLES::
    
    Category factory usage::
    
        sage: # Get category factory
        sage: factory = RMod(ZZ)
        sage: factory
        RMod category factory over Integer Ring
        
        sage: # Create free module with basis
        sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
        sage: M.category()
        Category of free R-modules with basis over Integer Ring
        sage: list(M.basis())
        [x, y, z]
        
        sage: # Create free module (no specific basis)
        sage: F = RMod(ZZ).Free(rank=3)
        sage: F.category() 
        Category of free R-modules over Integer Ring
        sage: F.rank()
        3
    
    Shorthand for WithBasis (maintains current API)::
    
        sage: # Generator assignment - creates WithBasis
        sage: M.<e,f,g> = RMod(ZZ)
        sage: M.category()
        Category of free R-modules with basis over Integer Ring
        
        sage: # Explicit basis list
        sage: M = RMod(ZZ, basis=['x', 'y', 'z'])
        sage: list(M.basis())
        [x, y, z]
        
        sage: # Rank specification  
        sage: M = RMod(QQ, 3)
        sage: M.rank()
        3
    
    Mathematical correctness::
    
        sage: # Base category contains both
        sage: M = RMod(ZZ).WithBasis(['a', 'b'])
        sage: F = RMod(ZZ).Free(rank=3)
        sage: M in RModules(ZZ)
        True
        sage: F in RModules(ZZ)
        True
        sage: M in RModules(ZZ).Free()  # WithBasis implies Free
        True
    """
    if len(args) == 0 and len(kwds) == 0:
        # Pattern: RMod(R) - return category factory
        return RModCategoryFactory(base_ring)
    else:
        # Pattern: RMod(R, ...) - shorthand for WithBasis construction
        return RMod(base_ring).WithBasis(*args, **kwds)


class RModCategoryFactory:
    """
    Factory for creating R-modules with specific axioms.
    
    Provides access to the axiom-based category structure.
    """
    
    def __init__(self, base_ring):
        self.base_ring = base_ring
    
    def __repr__(self):
        return f"RMod category factory over {self.base_ring}"
    
    def Free(self, rank=None, **kwds):
        """
        Create a free R-module (no specific basis chosen).
        
        INPUT:
        - rank -- rank of the free module (optional)
        - **kwds -- additional options
        
        EXAMPLES::
        
            sage: F = RMod(ZZ).Free(rank=3)
            sage: F.rank()
            3
            sage: F.category()
            Category of free R-modules over Integer Ring
            
            sage: # Finite rank implies finitely generated
            sage: F in RModules(ZZ).FinitelyGenerated()
            True
        """
        from sage.modules.rmodule_free import RModule_free
        category = RModules(self.base_ring).Free()
        
        # If rank is finite, also add FinitelyGenerated
        if rank is not None and rank < infinity:
            category = category & RModules(self.base_ring).FinitelyGenerated()
            
        return RModule_free(self.base_ring, rank=rank, category=category, **kwds)
    
    def FinitelyGenerated(self, generators=None, **kwds):
        """
        Create a finitely generated R-module.
        
        This is a general constructor that can create both free and
        non-free finitely generated modules.
        
        INPUT:
        - generators -- finite list of generators (optional)
        - **kwds -- additional options
        
        EXAMPLES::
        
            sage: # Finitely generated free module
            sage: M = RMod(ZZ).FinitelyGenerated().WithBasis(['a', 'b'])
            sage: M in RModules(ZZ).FinitelyGenerated()
            True
            sage: M.is_free()
            True
            
            sage: # Future: finitely generated torsion module
            sage: # T = RMod(ZZ).FinitelyGenerated(relations=[(6, 'a')])
            sage: # T.is_free()
            sage: # False
        """
        category = RModules(self.base_ring).FinitelyGenerated()
        # Actual implementation would handle various f.g. module types
        raise NotImplementedError("General f.g. module construction not yet implemented")
    
    def WithBasis(self, basis_spec=None, **kwds):
        """
        Create a free R-module with chosen basis.
        
        INPUT:
        - basis_spec -- Can be:
          * list of basis element names (finite basis)
          * integer n (creates basis ['e0', 'e1', ..., 'e_{n-1}'])
          * infinite set/family (creates infinite basis - NOT f.g.)
          * None (inferred from generator assignment)
        - **kwds -- additional options (prefix, etc.)
        
        EXAMPLES::
        
            sage: M = RMod(ZZ).WithBasis(['x', 'y', 'z'])
            sage: list(M.basis())
            [x, y, z]
            sage: M in RModules(ZZ).FinitelyGenerated()
            True  # Finite basis implies f.g.
            
            sage: N = RMod(QQ).WithBasis(3)  # Creates ['e0', 'e1', 'e2']
            sage: N.rank()
            3
            sage: N in RModules(QQ).FinitelyGenerated()
            True
            
            sage: # Infinite basis example (when implemented)
            sage: # M_inf = RMod(ZZ).WithBasis(Naturals())
            sage: # M_inf in RModules(ZZ).Free()
            sage: # True  # Still free
            sage: # M_inf in RModules(ZZ).FinitelyGenerated()
            sage: # False  # But NOT finitely generated!
        """
        from sage.modules.rmodule_with_basis import RModule_with_basis
        
        # Parse basis specification and determine if finite
        is_finite = True
        
        if isinstance(basis_spec, (int, Integer)):
            basis = [f'e{i}' for i in range(basis_spec)]
            is_finite = True
        elif isinstance(basis_spec, (list, tuple)):
            basis = basis_spec
            is_finite = True  # Lists/tuples are finite
        elif basis_spec is None:
            basis = None  # Will be set by _first_ngens
            is_finite = None  # Unknown until construction
        elif hasattr(basis_spec, 'cardinality'):
            # Handle infinite sets/families
            basis = basis_spec
            is_finite = basis_spec.cardinality() < infinity
        else:
            raise TypeError(f"Invalid basis specification: {type(basis_spec)}")
        
        # Start with WithBasis category
        category = RModules(self.base_ring).WithBasis()
        
        # Add FinitelyGenerated if basis is finite
        if is_finite is True:
            category = category & RModules(self.base_ring).FinitelyGenerated()
        elif is_finite is None:
            # Will be determined at construction time
            pass
        # If is_finite is False, do NOT add FinitelyGenerated
        
        return RModule_with_basis(self.base_ring, basis=basis, category=category, **kwds)

def RModWithBilinearForm(base_ring, basis=None, form=None, gram_matrix=None, **kwds):
    """
    Construct an R-module equipped with a bilinear form.
    
    This is a compatibility wrapper that constructs an R-module
    in the BilinearModules category.
    
    INPUT:
    - base_ring -- the base ring
    - basis -- basis names (optional)
    - form -- dictionary specifying form values
    - gram_matrix -- matrix representation of the form
    - **kwds -- additional arguments
    
    EXAMPLES::
    
        sage: # Hyperbolic plane
        sage: H = RModWithBilinearForm(ZZ, basis=['e', 'f'],
        ....:                         form={'ef': 1, 'fe': 1})
        sage: e, f = H.gens()
        sage: H.bilinear_form(e, f)
        1
        
        sage: # From Gram matrix
        sage: M = RModWithBilinearForm(QQ, basis=['x', 'y', 'z'],
        ....:                         gram_matrix=matrix(QQ, [[2, 1, 0],
        ....:                                               [1, 3, 1],
        ....:                                               [0, 1, 2]]))
        sage: M.gram_matrix()
        [2 1 0]
        [1 3 1]
        [0 1 2]
    """
    # This will be implemented as part of the bilinear modules integration
    # For now, raise NotImplementedError
    raise NotImplementedError("RModWithBilinearForm will be implemented with BilinearModules category")
```

## Mathematical Properties and Integration

The refactored RModules category cleanly separates inherited vs specific properties:

### Inherited from AbelianCategories:
1. **Homological Structure**:
   - Kernels, cokernels, images (morphism methods)
   - Subobjects and quotients (parent methods)
   - Exact sequences and homological algebra
   - Biproducts (direct sums as both product and coproduct)
   - All finite limits and colimits

2. **Morphism Properties**:
   - is_monomorphism() (injective = zero kernel)
   - is_epimorphism() (surjective = zero cokernel)
   - is_isomorphism() (bijective morphism)

### Specific to RModules:
1. **Module Operations**:
   - Tensor products (⊗) with universal property
   - Cartesian products (×) as R-modules
   - Hom modules and internal hom
   - Duality functor M* = Hom(M, R)
   - Module homomorphisms via generator images

2. **Natural Operations**: +, *, @, / capturing split Grothendieck ring K₀(R)

3. **Explicit Monoidal Structure**: Via SymmetricMonoidal axiom for tracking

4. **Axiom Hierarchy**:
   - **FinitelyGenerated**: Module has finite generating set (may include torsion)
   - **Free**: Module satisfying universal property (has some basis, but none specified)
   - **WithBasis**: Free module with distinguished basis (additional data)

5. **Computational Features**:
   - Symbolic computation with natural notation
   - Numerical efficiency via coordinate conversion
   - Integration with bilinear forms and lattices

### The Axiom Relationships

This design reflects mathematical reality with three key axioms:

1. **FinitelyGenerated**: The module can be generated by finitely many elements.
   - Includes both free and torsion modules
   - Examples: Z^n, Z/nZ, k[x,y]/(x,y)
   - Closed under quotients, finite direct sums
   
2. **Free**: The module satisfies the universal property for free modules.
   - Is projective (direct summand of some free module)
   - Has a basis (but none is specified)
   - Examples: Z^n, Z^(∞) (countably infinite free)
   
3. **WithBasis**: A free module equipped with a chosen basis.
   - The basis is additional structure/data
   - Enables coordinate representations
   - Finite basis → FinitelyGenerated
   - Infinite basis → NOT FinitelyGenerated

Key relationships:
- WithBasis ⊆ Free (having a basis implies being free)
- Free ∩ FinitelyGenerated = Free modules of finite rank (over nice rings)
- FinitelyGenerated ⊈ Free (torsion modules are f.g. but not free)
- WithBasis with finite basis ⊆ FinitelyGenerated
- WithBasis with infinite basis ⊈ FinitelyGenerated

This is analogous to:
- **Topological space** vs **Pointed topological space** (space + basepoint)
- **Vector space** vs **Vector space with ordered basis**
- **Group** vs **Group with generators**

The basis is additional structure/data, not just a property.

This design optimizes for:
- Indefinite bilinear forms and lattice computations
- Coxeter group representations
- Hyperbolic geometry calculations
- General multilinear algebra
- Homotopy theory (tracking monoidal structures explicitly)
- **Infinite lattices** (via WithBasis without FinitelyGenerated)

### Handling Infinite Lattices

The axiom structure elegantly handles both finite and infinite lattices:

```sage
# Finite lattice (most common case)
sage: L = RMod(ZZ).WithBasis(['e1', 'e2', 'e3'])
sage: L in RModules(ZZ).Free()
True
sage: L in RModules(ZZ).FinitelyGenerated()
True  # Finite basis → f.g.

# Infinite lattice (e.g., for limit constructions)
sage: # When implemented:
sage: # L_inf = RMod(ZZ).WithBasis(Naturals())  # Basis {e_0, e_1, e_2, ...}
sage: # L_inf in RModules(ZZ).Free()
sage: # True  # Still free
sage: # L_inf in RModules(ZZ).FinitelyGenerated()
sage: # False  # Infinite basis → NOT f.g.

# This distinction is crucial for:
# - Limit objects in category theory
# - Infinite Coxeter groups (affine types)
# - Completion constructions
# - Pro-finite modules
```

The key insight: WithBasis doesn't require finite generation, allowing us to work with infinite-dimensional free modules while maintaining coordinate access for any finite subset of basis elements.

## Relationship Between Natural Operations and SymmetricMonoidal

The RModules category provides two ways to work with monoidal structures:

1. **Natural Operations** (+, *, @): Convenient syntax for computations
2. **SymmetricMonoidal Axiom**: Explicit tracking of monoidal structure with coherence

```sage
# Natural operations - always available
sage: M = RMod(ZZ).WithBasis(['a', 'b'])
sage: N = RMod(ZZ).WithBasis(['x', 'y'])
sage: M + N  # Direct sum via __add__
sage: M * N  # Cartesian product via __mul__
sage: M @ N  # Tensor product via __matmul__

# Explicit monoidal structure - for when you need coherence isomorphisms
sage: C_tensor = RModules(ZZ).SymmetricMonoidal('tensor_product', ZZ)
sage: M_tensor = M.with_category(C_tensor)
sage: N_tensor = N.with_category(C_tensor)

# Now have access to coherence morphisms
sage: alpha = M_tensor.associator(N_tensor, P_tensor)  # Associator
sage: lambda_M = M_tensor.left_unitor()                # Left unitor
sage: beta = M_tensor.braiding(N_tensor)               # Braiding

# The monoidal_product method uses the specified operation
sage: M_tensor.monoidal_product(N_tensor)  # Calls tensor_product internally
# Equivalent to M @ N but with category tracking
```

This dual approach allows:
- Quick computations with natural syntax
- Rigorous categorical constructions when needed
- Flexibility for different mathematical contexts
- Preparation for homotopy-theoretic constructions (smash products, etc.)

## Usage Examples

```sage
# Basic construction patterns all work
sage: M.<x,y,z> = RMod(ZZ)
sage: M
Free module over Integer Ring with basis {x, y, z}

sage: v = 2*x + 3*y - z
sage: w = x - 2*y + 4*z
sage: v + w
3*x + y + 3*z

sage: v.to_vector()
(2, 3, -1)

# Interface for coordinate vector construction
sage: M.<e,f> = RMod(ZZ)

sage: # Basic symbolic arithmetic
sage: 2*e + 3*f + e == 3*e + 3*f
True

sage: # Construct from coordinates using M([...])
sage: M([1, 0]) == e
True
sage: M([2, 3]) == 2*e + 3*f
True

sage: # Cannot mix symbolic and coordinate directly
sage: 2*e + [0, 2]
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for +

sage: # Lists are not module elements
sage: [1, 0] in M
False
sage: M([1, 0]) in M
True

sage: # Different types are not equal
sage: 2*e != [2, 0]
True

sage: # Use n() for numerical representation
sage: n(e)
(1, 0)
sage: n(2*e + 3*f)
(2, 3)

sage: # Round-trip conversions
sage: M(n(2*e + 3*f)) == 2*e + 3*f
True
sage: n(M([1, -2])) == vector([1, -2])
True

# Category framework integration
sage: M in RModules(ZZ)
True
sage: M in Modules(ZZ)
True

# Morphisms
sage: N.<a,b> = RMod(ZZ)
sage: phi = M.hom([a + b, 2*a, -b])
sage: phi(x + y)
3*a + b

# Quotient modules with / operator
sage: N = M.submodule([x + y, z])  # Submodule <x+y, z>
sage: Q = M / N  # Quotient M/N using / syntax
sage: Q.rank()
1  # rank(M) - rank(N) = 3 - 2 = 1

sage: # Equivalent to explicit method
sage: Q.is_isomorphic(M.quotient(N))
True

# Three natural monoidal structures with split Grothendieck ring syntax
sage: M = RMod(ZZ).WithBasis(['a', 'b'])
sage: N = RMod(ZZ).WithBasis(['x', 'y'])

sage: # Direct sum monoidal structure: M + N (additive)
sage: MN_sum = M + N  # M ⊕ N
sage: MN_sum.rank()
4  # 2 + 2 = 4 for direct sum

sage: # Cartesian product monoidal structure: M * N (product)
sage: MN_cartesian = M * N  # M × N
sage: MN_cartesian.rank()
4  # 2 + 2 = 4 for cartesian product

sage: # Tensor product monoidal structure: M @ N (multiplicative)
sage: MN_tensor = M @ N  # M ⊗ N
sage: MN_tensor.rank()
4  # 2 × 2 = 4 for tensor product

sage: # Split Grothendieck ring equations work naturally
sage: P = M.submodule([M.basis()[0]])  # Submodule
sage: Q = M / P  # Quotient
sage: M.is_isomorphic(Q + P)  # M = M/P + P (direct sum)
True

sage: # Chain operations naturally
sage: R = RMod(ZZ).WithBasis(['u'])
sage: # Different operations chain according to their precedence
sage: result1 = M * N @ R  # Cartesian product of M with (tensor product N⊗R)
sage: result2 = (M * N) @ R  # Tensor product of (cartesian product M×N) with R
sage: result3 = M + N * R  # Direct sum of M with (cartesian product N×R)

sage: # Chain multiple operations of same type
sage: P = RMod(ZZ).WithBasis(['u', 'v'])
sage: sum_chain = M + N + P    # M ⊕ N ⊕ P (direct sum)
sage: sum_chain.rank()
6  # 2 + 2 + 2 = 6

sage: cartesian_chain = M * N * P  # M × N × P (cartesian product)
sage: cartesian_chain.rank()
8  # 2 × 2 × 2 = 8

sage: tensor_chain = M @ N @ P  # (M ⊗ N) ⊗ P (tensor product)
sage: tensor_chain.rank()
8  # 2 × 2 × 2 = 8

sage: # All operations preserve the category
sage: MN_sum in RModules(ZZ)
True
sage: MN_tensor in RModules(ZZ)
True
sage: MN_cartesian in RModules(ZZ)
True
```

## Subcategory Migration Strategy

The axiom-based RModules design requires careful migration of existing subcategories to maintain mathematical correctness while preserving functionality. This strategy outlines how dependent categories should be updated.

### 1. BilinearModules Migration

**Current Dependencies**: BilinearModules implicitly works with free, finitely generated all R-modules.
**Required Changes**:
- Base BilinearModules should inherit from RModules (general case)
- BilinearModules.WithBasis should inherit from RModules.WithBasis ∩ BilinearModules
- Only WithBasis version gets `from_vector()`, `to_vector()`, `gram_matrix()` from coordinates

**Migration Pattern**:
```python
class BilinearModules(Category):
    def super_categories(self):
        return [RModules(self.base_ring())]
    
    class WithBasis(CategoryWithAxiom):
        def extra_super_categories(self):
            return [self.base_category().WithBasis()]
        
        class ParentMethods:
            def gram_matrix(self):
                """Only available for modules with chosen basis."""
                # Implementation using coordinate representation
```

### 2. SymmetricBilinearModules Migration

**Dependencies**: BilinearModules + symmetry constraint
**Required Changes**:
- Inherits axiom structure from BilinearModules
- Adds symmetry-specific methods only where mathematically valid
- `reflection()`, `orthogonal_complement()` only for symmetric forms

**Migration Pattern**:
```python
class SymmetricBilinearModules(BilinearModules):
    class ElementMethods:
        def reflection(self):
            """Only meaningful for symmetric forms."""
            # Implementation for symmetric case only
```

### 3. Signature-Based Categories Migration

**Categories**: PositiveDefinite, NegativeDefinite, Indefinite, Hyperbolic
**Dependencies**: SymmetricBilinearModules + signature constraints
**Required Changes**:
- Each inherits from SymmetricBilinearModules
- Signature computation requires WithBasis axiom
- Specialized algorithms (short vectors, theta series) require basis

**Migration Pattern**:
```python
class PositiveDefiniteBilinearModules(SymmetricBilinearModules):
    class WithBasis(CategoryWithAxiom):
        class ParentMethods:
            def short_vectors(self, bound):
                """Requires coordinate representation for enumeration."""
                # Implementation using gram matrix
```

### 4. CoxeterLattices Migration

**Dependencies**: Assumes indefinite lattices with integral Gram matrices
**Required Changes**:
- Should inherit from appropriate signature category
- Root enumeration requires WithBasis axiom
- Reflection groups require symmetric forms

**Migration Pattern**:
```python
class CoxeterLattices(DefiniteBilinearModules):
    def extra_super_categories(self):
        return [RModules(self.base_ring()).Free().WithBasis()]
    
    class ParentMethods:
        def simple_roots(self):
            """Requires basis for root enumeration."""
            # Implementation using Gram matrix eigenvectors
```

### 5. Factory Function Migration

**Current Pattern**: Single constructors assume basis exists
**New Pattern**: Axiom-aware constructors

```python
# Old pattern
def BilinearModule(gram_matrix):
    # Assumes matrix → basis exists

# New pattern  
def BilinearModule(base_ring, basis=None, gram_matrix=None):
    if basis is not None:
        category = BilinearModules(base_ring).WithBasis()
        # Inherits natural operations: +, *, @, / from RModules
    else:
        category = BilinearModules(base_ring)
        # Still gets quotient and direct sum: /, +
```

### 6. Documentation Migration Strategy

**Phase 1 - Foundation**: Complete RModules axiom implementation
**Phase 2 - Core Extensions**: Migrate BilinearModules, SymmetricBilinearModules  
**Phase 3 - Specialized Categories**: Migrate signature-based categories
**Phase 4 - Applications**: Migrate CoxeterLattices, QuadraticForms integration
**Phase 5 - Factory Integration**: Update all constructor functions

### 7. Backward Compatibility

**Preservation Strategy**:
- All existing factory functions continue to work
- Automatic axiom inference where possible
- Clear error messages when operations require missing axioms

```python
# Automatic inference
M = BilinearModule(matrix([[2,1],[1,3]]))  # Infers WithBasis needed
# → BilinearModules(ZZ).WithBasis() object

# Clear error for invalid operations
M = BilinearModules(ZZ)()  # General R-module, no basis
M.gram_matrix()  # → "gram_matrix() requires WithBasis axiom"
```

### 8. Testing Strategy

**Axiom Correctness Tests**:
- Verify base RModules only provides universally valid methods
- Test that Free axiom adds exactly projective properties
- Verify WithBasis axiom provides coordinate access

**Migration Tests**:
- All existing functionality preserved for WithBasis case
- New general R-module functionality works correctly
- Proper error handling for invalid axiom combinations

**Mathematical Correctness Tests**:
- Verify universal properties hold (Free modules are projective)
- Test categorical structure (abelian category axioms)
- Validate monoidal structure coherence

### 9. Implementation Priority

1. **Critical Path**: BilinearModules migration (most dependent categories)
2. **High Priority**: SymmetricBilinearModules (signature categories depend on this)
3. **Medium Priority**: Signature-based categories (specialized algorithms)
4. **Low Priority**: Application categories (CoxeterLattices, etc.)

This migration strategy ensures mathematical correctness while preserving all existing functionality through proper axiom management.
