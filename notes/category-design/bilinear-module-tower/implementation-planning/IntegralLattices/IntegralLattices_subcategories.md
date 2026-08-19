<!--
Origin: gitclones/Coxeter/implementation/planning/IntegralLattices/IntegralLattices_subcategories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Subcategories: Even, Unimodular, and Root Lattices

Axiom-based subcategories of integral lattices capturing special arithmetic and geometric properties.

## Even Integral Lattices

```python
from sage.categories.category_with_axiom import CategoryWithAxiom

class Even(CategoryWithAxiom):
    """
    The axiom for even integral lattices.
    
    An integral lattice L is even if all norms are even:
    q(v) ∈ 2ℤ for all v ∈ L
    
    Equivalently:
    - All diagonal Gram matrix entries are even
    - L ⊆ (1/√2)L* (contained in scaled dual)
    - The quadratic form is integral on (1/2)L
    
    Even lattices have special properties:
    - Theta series has only even powers of q
    - Root systems are always even
    - Even unimodular lattices exist only in dimensions 8k
    
    EXAMPLES::
    
        sage: from sage.categories.integral_lattices import IntegralLattices
        sage: C = IntegralLattices().Even()
        sage: C
        Category of even integral lattices
        
        sage: # E₈ is even
        sage: E8 = IntegralLattice("E8")
        sage: E8 in C
        True
        sage: E8.is_even()
        True
        
        sage: # Standard ℤⁿ is odd
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L in C
        False
        sage: L.is_even()
        False
    """
    
    def _repr_(self):
        """
        Return string representation.
        
        EXAMPLES::
        
            sage: IntegralLattices().Even()
            Category of even integral lattices
        """
        return "Category of even integral lattices"
    
    class ParentMethods:
        """
        Methods for even integral lattice parents.
        """
        
        def characteristic_vectors(self):
            """
            Return all characteristic vectors.
            
            For even lattices, only 0 is characteristic since
            v·w ≡ w·w ≡ 0 (mod 2) requires v·w ≡ 0 (mod 2).
            
            OUTPUT:
            List containing only the zero vector
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.characteristic_vectors()
                [(0, 0, 0, 0, 0, 0, 0, 0)]
                
                sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
                sage: A2.characteristic_vectors()
                [(0, 0)]
            """
            return [self.zero()]
        
        def theta_series_parity(self):
            """
            Return that theta series has only even powers.
            
            For even lattices, θ_L(q) = Σ_{n even} r_n q^(n/2)
            where r_n counts vectors of norm n.
            
            OUTPUT:
            String 'even'
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.theta_series_parity()
                'even'
                sage: # Theta series: 1 + 240q² + 2160q³ + ...
            """
            return 'even'
        
        def shadow(self):
            """
            Return the shadow of this even lattice.
            
            The shadow S(L) consists of characteristic vectors
            in the dual that are not in L:
            S(L) = {v ∈ L* : v·w ≡ w·w (mod 2) for all w ∈ L} \ L
            
            OUTPUT:
            Coset representatives of shadow
            
            EXAMPLES::
            
                sage: # For E₈, shadow is empty (unimodular)
                sage: E8 = IntegralLattice("E8")
                sage: E8.shadow()
                []
                
                sage: # For D₄⁺ (even but not unimodular)
                sage: D4plus = IntegralLattice(...)  # D₄⁺ construction
                sage: len(D4plus.shadow())
                3  # Three non-trivial cosets
            """
            if self.is_unimodular():
                return []
            
            # Shadow computation for non-unimodular even lattices
            raise NotImplementedError("Shadow computation")
        
        def minimal_norm(self):
            """
            Return minimal non-zero norm (always even).
            
            For even lattices, minimum ∈ {2, 4, 6, ...}.
            
            OUTPUT:
            Even positive integer
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.minimal_norm()
                2
                
                sage: # Leech lattice has minimum 4
                sage: Leech = IntegralLattice("Leech")
                sage: Leech.minimal_norm()
                4
            """
            min_val = self.minimum()
            assert min_val % 2 == 0, "Even lattice must have even minimum"
            return min_val
        
        def type_II_code(self):
            """
            Return associated Type II code if dimension = 8k.
            
            Even self-dual lattices in dimension 8k correspond
            to self-dual Type II codes via Construction A.
            
            OUTPUT:
            BinaryCode object or None
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: C = E8.type_II_code()
                sage: C.length()
                8
                sage: C.is_self_dual()
                True
            """
            if self.rank() % 8 != 0 or not self.is_unimodular():
                return None
            
            # Construction A correspondence
            raise NotImplementedError("Type II code construction")
    
    class ElementMethods:
        """
        Methods for elements in even lattices.
        """
        
        def half_norm(self):
            """
            Return q(v)/2 (always integral for even lattices).
            
            OUTPUT:
            Integer
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: r = E8.simple_root(0)
                sage: r.half_norm()
                1  # norm = 2
                
                sage: v = 2*r
                sage: v.half_norm()
                4  # norm = 8
            """
            return self.norm() // 2
        
        def mod_2_reduction(self):
            """
            Return image in L/2L.
            
            Used for studying the 2-neighbor graph of lattices.
            
            OUTPUT:
            Element of L/2L (vector over 𝔽₂)
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: r = E8.simple_root(0)
                sage: r.mod_2_reduction()
                (1, 0, 0, 0, 0, 0, 0, 0)  # in 𝔽₂⁸
            """
            coords_mod_2 = [c % 2 for c in self.to_vector()]
            return vector(GF(2), coords_mod_2)
```

## Unimodular Integral Lattices

```python
class Unimodular(CategoryWithAxiom):
    """
    The axiom for unimodular integral lattices.
    
    An integral lattice L is unimodular if det(Gram) = ±1.
    
    Equivalently:
    - L = L* (self-dual)
    - L*/L is trivial
    - The bilinear form induces isomorphism L → Hom(L,ℤ)
    
    Classification results:
    - Odd unimodular: exist in all dimensions, unique in each genus
    - Even unimodular: exist only in dimensions 8k
    - Dimension 8: E₈ is unique
    - Dimension 16: E₈ ⊕ E₈ and D₁₆⁺ 
    - Dimension 24: 24 Niemeier lattices including Leech
    
    EXAMPLES::
    
        sage: C = IntegralLattices().Unimodular()
        sage: C
        Category of unimodular integral lattices
        
        sage: # Hyperbolic plane
        sage: H = IntegralLattice(matrix([[0, 1], [1, 0]]))
        sage: H in C
        True
        sage: H.discriminant()
        -1
        
        sage: # E₈ lattice
        sage: E8 = IntegralLattice("E8")
        sage: E8 in C
        True
        sage: E8.discriminant()
        1
    """
    
    def _repr_(self):
        """String representation."""
        return "Category of unimodular integral lattices"
    
    class ParentMethods:
        """
        Methods for unimodular lattice parents.
        """
        
        def dual_lattice(self):
            """
            Return the dual lattice (which equals self).
            
            For unimodular lattices, L = L*.
            
            OUTPUT:
            self
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.dual_lattice() is E8
                True
                
                sage: H = IntegralLattice(matrix([[0, 1], [1, 0]]))
                sage: H.dual_lattice() is H
                True
            """
            return self
        
        def glue_code(self):
            """
            Return the glue code L*/L (trivial for unimodular).
            
            OUTPUT:
            Trivial group
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: G = E8.glue_code()
                sage: G.order()
                1
            """
            from sage.groups.abelian_gps.abelian_group import AbelianGroup
            return AbelianGroup([])
        
        def mass_formula_value(self):
            """
            Compute mass via Siegel's formula.
            
            For unimodular lattices, the mass formula simplifies
            significantly using Minkowski-Siegel mass formula.
            
            OUTPUT:
            Rational number
            
            EXAMPLES::
            
                sage: # Unique lattice in dimension 1
                sage: L1 = IntegralLattice(matrix([[1]]))
                sage: L1.mass_formula_value()
                1/2  # |Aut| = 2
                
                sage: E8 = IntegralLattice("E8")
                sage: E8.mass_formula_value()
                1/696729600  # |Aut(E₈)| = 696729600
            """
            n = self.rank()
            
            # Simplified mass formula for unimodular case
            # Uses Bernoulli numbers and zeta values
            raise NotImplementedError("Siegel mass formula")
        
        def theta_transformation_kernel(self):
            """
            Return the metaplectic representation data.
            
            For unimodular lattices, the theta series transforms
            under SL₂(ℤ) with specific weight and character.
            
            OUTPUT:
            Dictionary with modular form data
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: data = E8.theta_transformation_kernel()
                sage: data['weight']
                4  # Modular form of weight 4
                sage: data['level']
                1  # Level 1 (full modular group)
            """
            n = self.rank()
            
            return {
                'weight': n // 2,
                'level': 1,
                'character': 'trivial' if self.is_even() else 'alternating'
            }
        
        def neighbors(self, prime=2):
            """
            Return p-neighbors of this unimodular lattice.
            
            Two lattices are p-neighbors if their intersection
            has index p in each.
            
            INPUT:
            - prime -- prime number p
            
            OUTPUT:
            List of p-neighbor lattices
            
            EXAMPLES::
            
                sage: # Unimodular lattices have specific neighbor counts
                sage: I16 = IntegralLattice(matrix.identity(16))
                sage: neighbors_2 = I16.neighbors(prime=2)
                sage: len(neighbors_2)
                135  # From Kneser neighbor formula
            """
            # Kneser neighbor theory for unimodular lattices
            raise NotImplementedError("Neighbor enumeration")
        
        def is_indecomposable(self):
            """
            Test if lattice is indecomposable.
            
            Cannot be written as orthogonal direct sum L₁ ⊕ L₂
            with both factors non-trivial.
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: E8.is_indecomposable()
                True
                
                sage: # E₈ ⊕ E₈ is decomposable
                sage: E8_E8 = E8.direct_sum(E8)
                sage: E8_E8.is_indecomposable()
                False
            """
            # Check if Gram matrix is block-decomposable
            # This involves checking connectivity of the form
            raise NotImplementedError("Indecomposability test")
    
    class ElementMethods:
        """
        Methods for elements in unimodular lattices.
        """
        
        def dual_lattice_coordinates(self):
            """
            Return coordinates in dual lattice (same as original).
            
            Since L = L* for unimodular lattices.
            
            OUTPUT:
            Same vector
            
            EXAMPLES::
            
                sage: E8 = IntegralLattice("E8")
                sage: v = E8.simple_root(0)
                sage: v.dual_lattice_coordinates()
                (2, -1, 0, 0, 0, 0, 0, 0)  # Same as v
            """
            return self.to_vector()
```

## Root Lattices

```python
class RootLattice(CategoryWithAxiom):
    """
    The axiom for root lattices.
    
    A root lattice is an even integral lattice with:
    - Minimum norm = 2
    - Generated by vectors of norm 2 (roots)
    - Roots have mutual inner products in {0, ±1, ±2}
    
    Classification (irreducible root lattices):
    - A_n (n ≥ 1): determinant n+1
    - D_n (n ≥ 4): determinant 4  
    - E_6: determinant 3
    - E_7: determinant 2
    - E_8: determinant 1 (unimodular)
    
    Root lattices correspond to:
    - Crystallographic root systems
    - Simple Lie algebras
    - Dynkin diagrams
    - Coxeter groups of crystallographic type
    
    EXAMPLES::
    
        sage: C = IntegralLattices().RootLattices()
        sage: C
        Category of root lattices
        
        sage: # A₂ root lattice
        sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
        sage: A2 in C
        True
        sage: A2.root_system()
        Root system of type ['A', 2]
        
        sage: # E₈ root lattice
        sage: E8 = IntegralLattice("E8")
        sage: E8 in C
        True
        sage: E8.num_roots()
        240
    """
    
    def _repr_(self):
        """String representation."""
        return "Category of root lattices"
    
    def super_categories(self):
        """
        Root lattices are even integral lattices.
        
        EXAMPLES::
        
            sage: IntegralLattices().RootLattices().super_categories()
            [Category of even integral lattices]
        """
        return [IntegralLattices().Even()]
    
    class ParentMethods:
        """
        Methods for root lattice parents.
        """
        
        def root_system(self):
            """
            Return the associated root system.
            
            Identifies the ADE type and constructs root system.
            
            OUTPUT:
            RootSystem object
            
            EXAMPLES::
            
                sage: E6 = IntegralLattice("E6")
                sage: RS = E6.root_system()
                sage: RS
                Root system of type ['E', 6]
                sage: RS.cartan_matrix()
                [ 2 -1  0  0  0  0]
                [-1  2 -1  0  0  0]
                [ 0 -1  2 -1  0 -1]
                [ 0  0 -1  2 -1  0]
                [ 0  0  0 -1  2  0]
                [ 0  0 -1  0  0  2]
            """
            # Identify type from Gram matrix structure
            # This requires root system recognition algorithm
            raise NotImplementedError("Root system identification")
        
        def simple_roots(self):
            """
            Return simple roots (indecomposable roots).
            
            Simple roots form a basis with Cartan matrix entries.
            
            OUTPUT:
            List of simple root vectors
            
            EXAMPLES::
            
                sage: A3 = IntegralLattice("A3")
                sage: simple = A3.simple_roots()
                sage: len(simple)
                3
                sage: all(r.norm() == 2 for r in simple)
                True
                
                sage: # Cartan matrix from simple roots
                sage: matrix([[r.inner_product(s) for s in simple] 
                ....:         for r in simple])
                [ 2 -1  0]
                [-1  2 -1]
                [ 0 -1  2]
            """
            # Find minimal set of norm-2 generators
            roots = self.roots()
            
            # Extract simple system
            # This requires finding positive roots and extracting basis
            raise NotImplementedError("Simple root extraction")
        
        def roots(self):
            """
            Return all roots (vectors of norm 2).
            
            OUTPUT:
            List of all root vectors
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
                sage: roots = A2.roots()
                sage: len(roots)
                6  # 2 * 3 roots for A₂
                sage: set(r.norm() for r in roots)
                {2}
            """
            return [v for v in self.shortest_vectors() if v.norm() == 2]
        
        def positive_roots(self):
            """
            Return positive roots with respect to standard ordering.
            
            OUTPUT:
            List of positive roots
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice("A2")
                sage: pos_roots = A2.positive_roots()
                sage: len(pos_roots)
                3  # Half of all roots
            """
            # Requires choice of positive chamber
            raise NotImplementedError("Positive root determination")
        
        def highest_root(self):
            """
            Return the highest root.
            
            The unique positive root that cannot be written
            as a sum of two positive roots.
            
            OUTPUT:
            Highest root vector
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice("A2")
                sage: theta = A2.highest_root()
                sage: theta
                (1, 1)  # α₁ + α₂ in simple root basis
            """
            # Find maximal positive root
            raise NotImplementedError("Highest root computation")
        
        def weyl_group(self):
            """
            Return the Weyl group W(R).
            
            Generated by reflections through simple roots.
            
            OUTPUT:
            WeylGroup object
            
            EXAMPLES::
            
                sage: A3 = IntegralLattice("A3")
                sage: W = A3.weyl_group()
                sage: W.order()
                24  # = 4!
                
                sage: E8 = IntegralLattice("E8")
                sage: W_E8 = E8.weyl_group()
                sage: W_E8.order()
                696729600
            """
            RS = self.root_system()
            return RS.weyl_group()
        
        def coxeter_number(self):
            """
            Return the Coxeter number h.
            
            h = (number of roots)/(rank)
            
            OUTPUT:
            Integer
            
            EXAMPLES::
            
                sage: A_n has h = n+1
                sage: A5 = IntegralLattice("A5")
                sage: A5.coxeter_number()
                6
                
                sage: E8 = IntegralLattice("E8")
                sage: E8.coxeter_number()
                30  # = 240/8
            """
            return len(self.roots()) // self.rank()
        
        def dual_coxeter_number(self):
            """
            Return the dual Coxeter number.
            
            OUTPUT:
            Integer
            
            EXAMPLES::
            
                sage: # For simply-laced, dual = regular
                sage: E6 = IntegralLattice("E6")
                sage: E6.dual_coxeter_number() == E6.coxeter_number()
                True
            """
            # For root lattices, related to highest root
            raise NotImplementedError("Dual Coxeter number")
        
        def dynkin_diagram(self):
            """
            Return the Dynkin diagram.
            
            Encodes adjacency of simple roots.
            
            OUTPUT:
            DynkinDiagram object
            
            EXAMPLES::
            
                sage: D4 = IntegralLattice("D4")
                sage: DD = D4.dynkin_diagram()
                sage: DD
                    O 4
                    |
                    |
                O---O---O
                1   2   3
                D4
            """
            RS = self.root_system()
            return RS.dynkin_diagram()
        
        def exponents(self):
            """
            Return the exponents of the root system.
            
            Related to invariant theory and Poincaré series.
            
            OUTPUT:
            List of integers
            
            EXAMPLES::
            
                sage: A3 = IntegralLattice("A3")
                sage: A3.exponents()
                [1, 2, 3]
                
                sage: E8 = IntegralLattice("E8")
                sage: E8.exponents()
                [1, 7, 11, 13, 17, 19, 23, 29]
            """
            # Exponents related to degrees of invariants
            raise NotImplementedError("Exponent computation")
    
    class ElementMethods:
        """
        Methods for elements in root lattices.
        """
        
        def is_root(self):
            """
            Test if this is a root (norm 2 vector).
            
            OUTPUT:
            Boolean
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice("A2")
                sage: alpha = A2.simple_root(0)
                sage: alpha.is_root()
                True
                sage: (2*alpha).is_root()
                False  # norm = 8
            """
            return self.norm() == 2
        
        def root_decomposition(self):
            """
            Express as linear combination of simple roots.
            
            OUTPUT:
            Coefficient vector
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice("A2")
                sage: v = A2([1, 1])  # α₁ + α₂
                sage: v.root_decomposition()
                [1, 1]
            """
            simple = self.parent().simple_roots()
            # Solve for coefficients
            raise NotImplementedError("Root decomposition")
        
        def reflection_matrix(self):
            """
            Return the reflection matrix through this root.
            
            For root α: s_α(v) = v - 2(v·α)/(α·α) * α
            
            OUTPUT:
            Matrix representing reflection
            
            EXAMPLES::
            
                sage: A2 = IntegralLattice("A2")
                sage: alpha = A2.simple_root(0)
                sage: R = alpha.reflection_matrix()
                sage: R
                [-1  1]
                [ 0  1]
            """
            if not self.is_root():
                raise ValueError("Reflection defined only for roots")
            
            # Construct reflection matrix
            n = self.parent().rank()
            from sage.matrix.constructor import identity_matrix
            
            R = identity_matrix(QQ, n)
            v = self.to_vector()
            
            for i in range(n):
                for j in range(n):
                    R[i,j] -= 2 * v[i] * v[j] / self.norm()
            
            return R.change_ring(ZZ)
```

## Positive Definite Lattices

```python
class PositiveDefinite(CategoryWithAxiom):
    """
    The axiom for positive definite integral lattices.
    
    The quadratic form is positive definite: q(v) > 0 for v ≠ 0.
    
    Positive definite lattices have:
    - Finite automorphism group
    - Well-defined shortest vectors
    - Convergent theta series
    - Connection to sphere packing
    
    EXAMPLES::
    
        sage: C = IntegralLattices().PositiveDefinite()
        sage: C
        Category of positive definite integral lattices
        
        sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
        sage: L in C
        True
        sage: L.is_positive_definite()
        True
    """
    
    def _repr_(self):
        """String representation."""
        return "Category of positive definite integral lattices"
    
    class ParentMethods:
        """
        Methods specific to positive definite lattices.
        """
        
        def hermite_invariant(self):
            """
            Return the Hermite invariant γ(L).
            
            γ(L) = (min(L)/det(L)^(1/n))^2
            
            Measures how close to optimal sphere packing.
            
            OUTPUT:
            Positive real number
            
            EXAMPLES::
            
                sage: # ℤⁿ achieves Hermite constant for n ≤ 8
                sage: Zn = IntegralLattice(matrix.identity(4))
                sage: Zn.hermite_invariant()
                1.0  # Optimal for dimension 4
            """
            n = self.rank()
            min_norm = self.minimum()
            det = abs(self.determinant())
            
            return (min_norm / det**(1/n))**2
        
        def packing_radius(self):
            """
            Return the packing radius.
            
            Half the minimal distance between distinct points.
            
            OUTPUT:
            Positive real number
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: L.packing_radius()
                1/2  # min distance = 1
            """
            return self.minimum()**(1/2) / 2
        
        def packing_density(self):
            """
            Return the sphere packing density.
            
            Volume fraction covered by spheres centered at points.
            
            OUTPUT:
            Real number between 0 and 1
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: L.packing_density()
                0.906899...  # π/(2√3) for hexagonal packing
            """
            n = self.rank()
            radius = self.packing_radius()
            det = abs(self.determinant())**(1/2)
            
            # Volume of n-sphere of radius r
            from sage.symbolic.constants import pi
            if n % 2 == 0:
                k = n // 2
                ball_volume = pi**k * radius**n / factorial(k)
            else:
                k = (n-1) // 2
                ball_volume = 2**(k+1) * pi**k * radius**n / factorial(2*k+1)
            
            return ball_volume / det
        
        def kissing_configuration(self):
            """
            Return the configuration of minimal vectors.
            
            Describes the "kissing number" arrangement.
            
            OUTPUT:
            Configuration matrix
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: config = L.kissing_configuration()
                sage: config.nrows()
                4  # 4 minimal vectors in ℤ²
            """
            return matrix([v.to_vector() for v in self.shortest_vectors()])
        
        def voronoi_cell(self):
            """
            Return the Voronoi cell (fundamental domain).
            
            V(L) = {x ∈ ℝⁿ : ||x|| ≤ ||x-v|| for all v ∈ L}
            
            OUTPUT:
            Polyhedron object
            
            EXAMPLES::
            
                sage: L = IntegralLattice(matrix.identity(2))
                sage: V = L.voronoi_cell()
                sage: V.volume()
                1  # Unit square for ℤ²
            """
            # Voronoi cell computation
            raise NotImplementedError("Voronoi cell algorithm")
        
        def delaunay_decomposition(self):
            """
            Return the Delaunay decomposition.
            
            Dual to Voronoi, used for theta series.
            
            OUTPUT:
            Simplicial complex
            """
            raise NotImplementedError("Delaunay decomposition")
```

## Mathematical Properties

The subcategory framework ensures:

```python
# Mathematical assertion: Even lattice characterization
# L even ⟺ diag(Gram) ⊆ 2ℤ ⟺ L ⊆ (1/√2)L*

# Mathematical assertion: Unimodular self-duality
# L unimodular ⟺ L = L* ⟺ |det(Gram)| = 1

# Mathematical assertion: Root lattice generation
# L root lattice ⟺ L = ℤ-span{v : ||v||² = 2}

# Mathematical assertion: Even unimodular dimensions
# L even unimodular ⟹ dim(L) ≡ 0 (mod 8)

# Mathematical assertion: Root system correspondence
# Root lattices ↔ Crystallographic root systems

# Mathematical assertion: Hermite constant bound
# min(L) ≤ γₙ · det(L)^(1/n) for positive definite

# Mathematical assertion: Theta modularity
# L even unimodular ⟹ θ_L is modular form

# Mathematical assertion: Mass formula
# Even unimodular lattices satisfy Minkowski-Siegel formula
```

This comprehensive subcategory system captures the major classes of integral lattices with their specific properties and algorithms.