<!--
Origin: gitclones/Coxeter/implementation/planning/IntegralLattices/IntegralLattices_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: IntegralLattices

Category of integral lattices as symmetric bilinear ℤ-modules with integer-valued forms.

## Mathematical Definition

An integral lattice is a symmetric bilinear ℤ-module (L, b) where:
- L is a free ℤ-module of finite rank
- b: L × L → ℤ is a symmetric bilinear form
- The associated quadratic form q(v) = b(v,v) takes integer values

This specializes SymmetricBilRMod to the case R = ℤ with integrality constraints.

## Category Structure

```python
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.symmetric_bilinear_modules import SymmetricBilinearModules

class IntegralLattices(CategoryWithAxiom):
    """
    The category of integral lattices.
    
    An integral lattice is a free ℤ-module equipped with a symmetric
    bilinear form taking integer values. This is the arithmetic setting
    for quadratic form theory, with applications to:
    - Number theory (quadratic forms over ℤ)
    - Algebraic topology (intersection forms)
    - Lie theory (root lattices)
    - Coding theory (Type II codes)
    - Physics (string theory compactifications)
    
    EXAMPLES::
    
        sage: from sage.categories.integral_lattices import IntegralLattices
        sage: C = IntegralLattices()
        sage: C
        Category of integral lattices
        
        sage: # Standard example: ℤⁿ with dot product
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L in IntegralLattices()
        True
        
        sage: # Root lattice E₈
        sage: E8 = IntegralLattice("E8")
        sage: E8.is_even()
        True
        sage: E8.discriminant()
        1
    """
    
    def __init__(self):
        """
        Initialize the category of integral lattices.
        
        EXAMPLES::
        
            sage: C = IntegralLattices()
            sage: C.base_ring()
            Integer Ring
            sage: C.super_categories()
            [Category of symmetric bilinear modules over Integer Ring]
        """
        super().__init__(
            base_category=SymmetricBilinearModules(ZZ),
            name="integral lattices"
        )
    
    def _repr_object_names(self):
        """
        Return the name of objects in this category.
        
        EXAMPLES::
        
            sage: IntegralLattices()._repr_object_names()
            'integral lattices'
        """
        return "integral lattices"
    
    def super_categories(self):
        """
        Return the super categories.
        
        Integral lattices are symmetric bilinear ℤ-modules that are:
        - Free (have a basis)
        - Finitely generated
        - With integer-valued bilinear form
        
        EXAMPLES::
        
            sage: IntegralLattices().super_categories()
            [Category of symmetric bilinear modules over Integer Ring with basis
             and finitely generated]
        """
        from sage.categories.modules import Modules
        R = ZZ
        return [SymmetricBilinearModules(R).Free().FinitelyGenerated().WithBasis()]
    
    class ParentMethods:
        """
        Methods for integral lattice parents.
        """
        
        def discriminant(self):
            """
            Return the discriminant (determinant of Gram matrix).
            
            The discriminant is a fundamental invariant:
            - disc(L) = det(Gram matrix)
            - Measures the "volume" of fundamental domain
            - disc(L*) = 1/disc(L) for dual lattice
            
            OUTPUT:
            Integer (possibly negative)
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
                sage: L.discriminant()
                5
                
                sage: # Unimodular lattice has discriminant ±1
                sage: E8 = IntegralLattice("E8")
                sage: E8.discriminant()
                1
            """
            return self.gram_matrix().determinant()
        
        def is_integral(self):
            """
            Always True for integral lattices.
            
            This is part of the definition: b(v,w) ∈ ℤ for all v,w.
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix([[1, 0], [0, 1]]))
                sage: L.is_integral()
                True
            """
            return True
        
        def is_even(self):
            """
            Test if lattice is even (all norms are even).
            
            A lattice is even if q(v) ∈ 2ℤ for all v ∈ L.
            Equivalently, diagonal of Gram matrix has even entries.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: # Standard lattice ℤ² is odd
                sage: L = IntegralLattice(matrix.identity(2))
                sage: L.is_even()
                False
                
                sage: # E₈ is even
                sage: E8 = IntegralLattice("E8")
                sage: E8.is_even()
                True
                
                sage: # A₂ root lattice is even
                sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
                sage: A2.is_even()
                True
            """
            G = self.gram_matrix()
            return all(G[i,i] % 2 == 0 for i in range(G.nrows()))
        
        def is_unimodular(self):
            """
            Test if lattice is unimodular (discriminant = ±1).
            
            Unimodular lattices satisfy L = L* (self-dual).
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: # Hyperbolic plane
                sage: H = IntegralLattice(matrix([[0, 1], [1, 0]]))
                sage: H.is_unimodular()
                True
                sage: H.discriminant()
                -1
                
                sage: # E₈ lattice
                sage: E8 = IntegralLattice("E8")
                sage: E8.is_unimodular()
                True
            """
            return abs(self.discriminant()) == 1
        
        def level(self):
            """
            Return the level (exponent of L*/L).
            
            The level N is the smallest positive integer such that
            N·(L*/L) = 0, where L* is the dual lattice.
            
            For unimodular lattices, level = 1.
            For even lattices, level divides discriminant.
            
            OUTPUT:
            Positive integer
            
            EXAMPLES::
            
                sage: # Unimodular lattice has level 1
                sage: E8 = IntegralLattice("E8")
                sage: E8.level()
                1
                
                sage: # Scaled root lattice
                sage: A2 = IntegralLattice(matrix([[4, -2], [-2, 4]]))
                sage: A2.level()
                2
            """
            if self.is_unimodular():
                return ZZ(1)
            
            # General computation via dual lattice
            # Level = lcm of denominators in L*/L
            raise NotImplementedError("Level computation for non-unimodular lattices")
        
        def minimum(self):
            """
            Return the minimum (shortest non-zero vector norm).
            
            For positive definite lattices, this is the minimal value
            of q(v) for non-zero v ∈ L.
            
            OUTPUT:
            Positive integer (or 0 if indefinite)
            
            EXAMPLES::
            
                sage: # Standard cubic lattice
                sage: L = IntegralLattice(matrix.identity(3))
                sage: L.minimum()
                1
                
                sage: # E₈ has minimum 2
                sage: E8 = IntegralLattice("E8")
                sage: E8.minimum()
                2
            """
            if not self.is_positive_definite():
                return ZZ(0)
            
            # This requires sophisticated algorithms (LLL, enumeration)
            raise NotImplementedError("Minimum finding algorithm")
        
        def kissing_number(self):
            """
            Return the kissing number (number of minimal vectors).
            
            This counts vectors v with q(v) = minimum (up to sign).
            Also called the coordination number.
            
            OUTPUT:
            Non-negative integer
            
            EXAMPLES::
            
                sage: # ℤⁿ has 2n minimal vectors (±eᵢ)
                sage: L = IntegralLattice(matrix.identity(3))
                sage: L.kissing_number()
                6
                
                sage: # E₈ has 240 minimal vectors (root system)
                sage: E8 = IntegralLattice("E8")
                sage: E8.kissing_number()
                240
            """
            if not self.is_positive_definite():
                raise ValueError("Kissing number only defined for positive definite lattices")
            
            # Requires finding all minimal vectors
            raise NotImplementedError("Kissing number computation")
        
        def theta_series(self, precision=10):
            """
            Return the theta series of the lattice.
            
            θ_L(q) = Σ_{v ∈ L} q^{q(v)/2}
            
            Encodes the number of vectors of each norm.
            
            INPUT:
            - precision -- number of terms
            
            OUTPUT:
            Power series in q
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: L.theta_series(5)
                1 + 4*q + 4*q^2 + O(q^5)
                
                sage: # E₈ theta series is modular form
                sage: E8 = IntegralLattice("E8")
                sage: E8.theta_series(5)
                1 + 240*q^2 + 2160*q^3 + 6720*q^4 + O(q^5)
            """
            # This requires lattice point enumeration
            raise NotImplementedError("Theta series computation")
        
        def genus(self):
            """
            Return the genus of this lattice.
            
            The genus is the equivalence class of lattices with the
            same local invariants at all primes (including ∞).
            
            OUTPUT:
            Genus object encoding local invariants
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
                sage: L.genus()
                Genus of 2-dimensional integral lattice
                Signature: (2, 0)
                Discriminant: 5
            """
            from sage.quadratic_forms.genera.genus import Genus
            return Genus(self.gram_matrix())
        
        def is_in_same_genus(self, other):
            """
            Test if two lattices are in the same genus.
            
            Same genus means locally isomorphic at all primes.
            
            INPUT:
            - other -- another integral lattice
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: L1 = IntegralLattice(matrix([[2, 0], [0, 3]]))
                sage: L2 = IntegralLattice(matrix([[1, 0], [0, 6]]))
                sage: L1.is_in_same_genus(L2)
                True  # Both have discriminant 6
            """
            return self.genus() == other.genus()
        
        def adjacency_graph(self, max_norm=None):
            """
            Return the adjacency graph of lattice vectors.
            
            Vertices are lattice vectors up to given norm,
            edges connect vectors with minimal inner product.
            
            INPUT:
            - max_norm -- maximum norm for vectors (optional)
            
            OUTPUT:
            Graph with lattice vectors as vertices
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: G = L.adjacency_graph(max_norm=2)
                sage: G.num_verts()
                9  # (0,0), ±(1,0), ±(0,1), ±(1,±1)
            """
            # This builds sphere packing graphs
            raise NotImplementedError("Adjacency graph construction")
        
        def root_system(self):
            """
            Return the root system if this is a root lattice.
            
            A root lattice has minimum 2 and all minimal vectors
            have mutual inner products in {0, ±1, ±2}.
            
            OUTPUT:
            RootSystem object or None
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.root_system()
                Root system of type ['E', 8]
                
                sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
                sage: A2.root_system()
                Root system of type ['A', 2]
            """
            if self.minimum() != 2:
                return None
            
            # Check if minimal vectors form a root system
            raise NotImplementedError("Root system detection")
    
    class ElementMethods:
        """
        Methods for integral lattice elements.
        """
        
        def norm(self):
            """
            Return the norm q(v) of this lattice vector.
            
            This is the quadratic form evaluation, always an integer.
            
            OUTPUT:
            Integer
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
                sage: v = L([1, 2])
                sage: v.norm()
                17  # 2·1² + 2·1·2 + 3·2² = 2 + 4 + 12
            """
            return self.parent().quadratic_form(self)
        
        def is_primitive(self):
            """
            Test if this vector is primitive in the lattice.
            
            A vector v is primitive if gcd of coordinates is 1,
            i.e., v is not a multiple of another lattice vector.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: v = L([2, 3])
                sage: v.is_primitive()
                True
                
                sage: w = L([2, 4])
                sage: w.is_primitive()
                False  # w = 2·(1,2)
            """
            coords = self.to_vector()
            from sage.arith.misc import gcd
            return gcd(coords) == 1
        
        def divisibility(self):
            """
            Return the divisibility of this vector.
            
            The divisibility is gcd(coordinates), measuring how
            many times the vector can be divided in the lattice.
            
            OUTPUT:
            Positive integer
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(3))
                sage: v = L([6, 9, 12])
                sage: v.divisibility()
                3  # v = 3·(2,3,4)
            """
            coords = self.to_vector()
            from sage.arith.misc import gcd
            return gcd(coords)
        
        def height(self):
            """
            Return the height (maximum absolute coordinate).
            
            Useful for enumerating lattice points.
            
            OUTPUT:
            Non-negative integer
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: v = L([3, -5])
                sage: v.height()
                5
            """
            coords = self.to_vector()
            return max(abs(c) for c in coords)
    
    class MorphismMethods:
        """
        Methods for morphisms between integral lattices.
        """
        
        def is_isometry(self):
            """
            Test if this morphism preserves the quadratic form.
            
            An isometry f satisfies q(f(v)) = q(v) for all v.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: # 90-degree rotation
                sage: f = L.hom([[0, -1], [1, 0]])
                sage: f.is_isometry()
                True
            """
            # Check if f^T G f = G
            raise NotImplementedError("Isometry testing")
    
    class SubcategoryMethods:
        """
        Methods for defining subcategories of integral lattices.
        """
        
        def Even(self):
            """
            Return the subcategory of even integral lattices.
            
            EXAMPLES::
            
                sage: IntegralLattices().Even()
                Category of even integral lattices
            """
            return self._with_axiom('Even')
        
        def Unimodular(self):
            """
            Return the subcategory of unimodular lattices.
            
            EXAMPLES::
            
                sage: IntegralLattices().Unimodular()
                Category of unimodular integral lattices
            """
            return self._with_axiom('Unimodular')
        
        def PositiveDefinite(self):
            """
            Return the subcategory of positive definite lattices.
            
            EXAMPLES::
            
                sage: IntegralLattices().PositiveDefinite()
                Category of positive definite integral lattices
            """
            return self._with_axiom('PositiveDefinite')
        
        def RootLattices(self):
            """
            Return the subcategory of root lattices.
            
            EXAMPLES::
            
                sage: IntegralLattices().RootLattices()
                Category of root lattices
            """
            return self._with_axiom('RootLattice')
```

## Mathematical Properties

The category of integral lattices satisfies:

```python
# Mathematical assertion: Integrality
# L ⊆ L* ⊆ (1/disc(L))·L where L* is dual lattice

# Mathematical assertion: Discriminant formula
# disc(L) = det(Gram matrix) = [L* : L]

# Mathematical assertion: Even lattice characterization
# L even ⟺ v·v ∈ 2ℤ for all v ⟺ L ⊆ √2·L*

# Mathematical assertion: Unimodular equivalence
# L unimodular ⟺ L = L* ⟺ disc(L) = ±1

# Mathematical assertion: Genus theory
# Same genus ⟺ locally isomorphic at all primes p and ∞

# Mathematical assertion: Theta series modularity
# For even unimodular lattices, θ_L is a modular form

# Mathematical assertion: Mass formula
# Σ_{L in genus} 1/|Aut(L)| = mass(genus)

# Mathematical assertion: Voronoi theory
# Lattice determined by Voronoi cell up to isometry
```

This category provides the foundation for arithmetic theory of quadratic forms and connects to modular forms, algebraic topology, and sphere packing problems.