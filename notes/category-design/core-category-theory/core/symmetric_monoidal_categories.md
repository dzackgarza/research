<!--
Origin: gitclones/Coxeter/implementation/planning/core/symmetric_monoidal_categories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: SymmetricMonoidalCategories

The metacategory of symmetric monoidal categories, providing tensor product structure with coherent isomorphisms.

## Category Definition

```python
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom

class MonoidalCategories(Category):
    """
    The category of monoidal categories.
    
    A monoidal category is a category C equipped with:
    - A bifunctor ⊗: C × C → C (tensor product)
    - A unit object I
    - Natural isomorphisms for associativity and unit laws
    - Coherence conditions (pentagon and triangle axioms)
    
    EXAMPLES::
    
        sage: from sage.categories.monoidal_categories import MonoidalCategories
        sage: C = MonoidalCategories()
        sage: C
        Category of monoidal categories
        
        sage: from sage.categories.vector_spaces import VectorSpaces
        sage: VectorSpaces(QQ) in MonoidalCategories()
        True  # With tensor product of vector spaces
    """
    
    def super_categories(self):
        """
        Monoidal categories are categories with extra structure.
        
        EXAMPLES::
        
            sage: MonoidalCategories().super_categories()
            [Category of categories]
        """
        return [Category.category_of_categories()]
    
    class ParentMethods:
        """
        Methods for objects in a monoidal category.
        """
        
        def tensor_product(self, *others):
            r"""
            Return the tensor product with other objects.
            
            The tensor product ⊗ is associative up to natural isomorphism.
            Multiple arguments associate to the left: A⊗B⊗C = (A⊗B)⊗C.
            
            EXAMPLES::
            
                sage: V = VectorSpace(QQ, 2)
                sage: W = VectorSpace(QQ, 3)
                sage: V.tensor_product(W)
                Vector space of dimension 6 over Rational Field
                
                sage: # Multiple tensor products
                sage: U = VectorSpace(QQ, 1)
                sage: V.tensor_product(W, U).dimension()
                6  # (2 × 3) × 1 = 6
            """
            raise NotImplementedError
        
        def tensor_unit(self):
            """
            Return the unit object for tensor products in this category.
            
            The unit I satisfies I⊗A ≅ A ≅ A⊗I for all objects A.
            
            EXAMPLES::
            
                sage: VectorSpaces(QQ).tensor_unit()
                Vector space of dimension 1 over Rational Field
                
                sage: Modules(ZZ).tensor_unit()
                Ambient free module of rank 1 over Integer Ring
            """
            raise NotImplementedError
        
        def associator(self, B, C):
            r"""
            The associator isomorphism α: (A⊗B)⊗C → A⊗(B⊗C).
            
            This natural isomorphism provides coherent reassociation
            of tensor products.
            
            EXAMPLES::
            
                sage: A = VectorSpace(QQ, 2)
                sage: B = VectorSpace(QQ, 3) 
                sage: C = VectorSpace(QQ, 1)
                sage: alpha = A.associator(B, C)
                sage: alpha.domain() == A.tensor_product(B).tensor_product(C)
                True
                sage: alpha.codomain() == A.tensor_product(B.tensor_product(C))
                True
            """
            raise NotImplementedError
        
        def left_unitor(self):
            r"""
            The left unitor isomorphism λ: I⊗A → A.
            
            EXAMPLES::
            
                sage: V = VectorSpace(QQ, 3)
                sage: I = VectorSpaces(QQ).tensor_unit()
                sage: lam = V.left_unitor()
                sage: lam.domain() == I.tensor_product(V)
                True
                sage: lam.codomain() == V
                True
            """
            raise NotImplementedError
        
        def right_unitor(self):
            r"""
            The right unitor isomorphism ρ: A⊗I → A.
            
            EXAMPLES::
            
                sage: V = VectorSpace(QQ, 3)
                sage: I = VectorSpaces(QQ).tensor_unit()
                sage: rho = V.right_unitor()
                sage: rho.domain() == V.tensor_product(I)
                True
                sage: rho.codomain() == V
                True
            """
            raise NotImplementedError
    
    class HomsetMethods:
        """
        Methods for morphisms in a monoidal category.
        """
        
        def tensor_product(self, other):
            r"""
            Tensor product of morphisms.
            
            For f: A → B and g: C → D, returns f⊗g: A⊗C → B⊗D.
            
            EXAMPLES::
            
                sage: V = VectorSpace(QQ, 2)
                sage: W = VectorSpace(QQ, 3)
                sage: f = V.hom(matrix([[1, 0], [0, -1]]))  # V → V
                sage: g = W.hom(matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))  # W → W
                sage: h = f.tensor_product(g)  # V⊗W → V⊗W
                sage: h.domain() == V.tensor_product(W)
                True
            """
            raise NotImplementedError
    
    class Symmetric(CategoryWithAxiom):
        """
        The axiom for symmetric monoidal categories.
        
        A symmetric monoidal category has a braiding natural isomorphism
        β: A⊗B → B⊗A that satisfies β_{B,A} ∘ β_{A,B} = id.
        """
        
        class ParentMethods:
            def braiding(self, B):
                r"""
                The braiding isomorphism β: A⊗B → B⊗A.
                
                In the symmetric case: β_{B,A} ∘ β_{A,B} = id_{A⊗B}.
                
                EXAMPLES::
                
                    sage: V = VectorSpace(QQ, 2)
                    sage: W = VectorSpace(QQ, 3)
                    sage: beta_VW = V.braiding(W)
                    sage: beta_WV = W.braiding(V)
                    
                    sage: # Symmetry property
                    sage: (beta_WV * beta_VW).is_identity()
                    True
                """
                raise NotImplementedError
    
    class Braided(CategoryWithAxiom):
        """
        The axiom for braided monoidal categories.
        
        A braided monoidal category has a braiding natural isomorphism
        β: A⊗B → B⊗A that satisfies the hexagon axioms but not
        necessarily β_{B,A} ∘ β_{A,B} = id.
        """
        pass
    
    class Rigid(CategoryWithAxiom):
        """
        The axiom for rigid monoidal categories.
        
        A rigid monoidal category is one where every object has
        both left and right duals.
        """
        
        class ParentMethods:
            def dual(self):
                """
                Return the dual object A*.
                
                The dual satisfies adjunction properties with evaluation
                and coevaluation morphisms.
                
                EXAMPLES::
                
                    sage: V = VectorSpace(QQ, 3)
                    sage: V_dual = V.dual()
                    sage: V_dual.dimension() == V.dimension()
                    True
                    
                    sage: # Double dual for finite dimensional
                    sage: V.dual().dual().is_isomorphic(V)
                    True
                """
                raise NotImplementedError
            
            def evaluation_morphism(self):
                r"""
                Return the evaluation morphism ev: A* ⊗ A → I.
                
                EXAMPLES::
                
                    sage: V = VectorSpace(QQ, 2)
                    sage: ev = V.evaluation_morphism()
                    sage: ev.domain() == V.dual().tensor_product(V)
                    True
                    sage: ev.codomain() == VectorSpaces(QQ).tensor_unit()
                    True
                """
                raise NotImplementedError
            
            def coevaluation_morphism(self):
                r"""
                Return the coevaluation morphism coev: I → A ⊗ A*.
                
                EXAMPLES::
                
                    sage: V = VectorSpace(QQ, 2)
                    sage: coev = V.coevaluation_morphism()
                    sage: coev.domain() == VectorSpaces(QQ).tensor_unit()
                    True
                    sage: coev.codomain() == V.tensor_product(V.dual())
                    True
                """
                raise NotImplementedError
    
    class Closed(CategoryWithAxiom):
        """
        The axiom for closed monoidal categories.
        
        A closed monoidal category has internal hom objects [A,B]
        satisfying the tensor-hom adjunction.
        """
        
        class ParentMethods:
            def internal_hom(self, B):
                r"""
                Return the internal hom object [A,B].
                
                Satisfies adjunction: Hom(C⊗A, B) ≅ Hom(C, [A,B]).
                
                EXAMPLES::
                
                    sage: V = VectorSpace(QQ, 2)
                    sage: W = VectorSpace(QQ, 3)
                    sage: Hom_VW = V.internal_hom(W)
                    sage: Hom_VW.dimension()
                    6  # dim([V,W]) = dim(V) × dim(W)
                """
                raise NotImplementedError


class SymmetricMonoidalCategories(MonoidalCategories):
    """
    The category of symmetric monoidal categories.
    
    These are monoidal categories with a symmetric braiding.
    
    EXAMPLES::
    
        sage: from sage.categories.symmetric_monoidal_categories import SymmetricMonoidalCategories
        sage: C = SymmetricMonoidalCategories()
        sage: C
        Category of symmetric monoidal categories
        
        sage: VectorSpaces(QQ) in SymmetricMonoidalCategories()
        True
        
        sage: Modules(ZZ) in SymmetricMonoidalCategories()
        True
    """
    
    def super_categories(self):
        """
        Symmetric monoidal categories are braided monoidal categories.
        
        EXAMPLES::
        
            sage: SymmetricMonoidalCategories().super_categories()
            [Category of braided monoidal categories]
        """
        return [MonoidalCategories().Braided()]
    
    def additional_structure(self):
        """
        Return the additional structure of symmetric monoidal categories.
        
        EXAMPLES::
        
            sage: SymmetricMonoidalCategories().additional_structure()
            CategoryWithAxiom(base_category=Category of monoidal categories,
                            axiom='Symmetric')
        """
        return MonoidalCategories().Symmetric()
```

## Coherence Conditions

A monoidal category must satisfy:

### Pentagon Axiom (Associativity Coherence)
For any objects A, B, C, D, the following diagram commutes:
```
((A⊗B)⊗C)⊗D ----α⊗1----> (A⊗(B⊗C))⊗D ----α----> A⊗((B⊗C)⊗D)
      |                                                    |
      α                                                    1⊗α
      |                                                    |
      v                                                    v
(A⊗B)⊗(C⊗D) -----------α-----------> A⊗(B⊗(C⊗D))
```

### Triangle Axiom (Unit Coherence)
For any objects A, B, the following diagram commutes:
```
(A⊗I)⊗B ----α----> A⊗(I⊗B)
    |                  |
   ρ⊗1               1⊗λ
    |                  |
    v                  v
   A⊗B <-----------> A⊗B
           id
```

### Hexagon Axioms (Braiding Coherence)
For braided categories, two hexagon diagrams must commute relating the braiding to the associator.

### Symmetry Axiom
For symmetric monoidal categories: β_{B,A} ∘ β_{A,B} = id_{A⊗B}

## Key Properties

1. **Mac Lane's Coherence Theorem**: Any two morphisms built from associators and unitors between the same objects are equal.

2. **Every symmetric monoidal category is enriched**: Hom-sets have a natural monoid structure via tensor product.

3. **Tensor-Hom Adjunction** (for closed categories): Hom(A⊗B, C) ≅ Hom(A, [B,C])

4. **Rigid categories generalize finite-dimensional vector spaces**: Every object has a dual with perfect pairing.