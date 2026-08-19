<!--
Origin: gitclones/Coxeter/implementation/planning/SymmetricBilRMod/SymmetricBilRMod_subcategories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Subcategories: Symmetric Bilinear Module Axioms and Specializations

Axiom-based subcategories for symmetric bilinear modules with specialized properties based on signature and definiteness.

## Axiom Organization

```python
from sage.categories.category_with_axiom import CategoryWithAxiom

class SymmetricBilinearModulesWithAxiom(CategoryWithAxiom):
    """
    Base class for symmetric bilinear module axioms.
    
    Provides framework for axiom-based specialization focusing on
    signature-based properties and geometric characteristics.
    
    Axiom hierarchy for symmetric forms:
    - PositiveDefinite ⊆ Definite ⊆ Nondegenerate ⊆ SymmetricBilinearModules
    - NegativeDefinite ⊆ Definite ⊆ Nondegenerate ⊆ SymmetricBilinearModules
    - Indefinite ⊆ Nondegenerate ⊆ SymmetricBilinearModules
    - Anisotropic ⊆ Nondegenerate ⊆ SymmetricBilinearModules
    - EvenIntegral ⊆ Integral ⊆ SymmetricBilinearModules
    - Unimodular ⊆ Integral ⊆ SymmetricBilinearModules
    """
    pass
```

## Definite Forms

```python
class PositiveDefinite(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for positive definite symmetric bilinear forms.
    
    A symmetric form is positive definite if q(v) > 0 for all v ≠ 0.
    Equivalently, all eigenvalues of the Gram matrix are positive.
    
    Properties:
    - Defines proper inner product space
    - Euclidean norm: ||v|| = √q(v)
    - Cauchy-Schwarz inequality holds
    - Triangle inequality holds
    - Parallelogram law holds
    - Orthogonal group is compact: O(n)
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(QQ).PositiveDefinite()
        sage: C
        Category of positive definite symmetric bilinear modules over Rational Field
        
        sage: # Standard Euclidean form
        sage: G = matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: M.signature()
        (3, 0, 0)
    """
    
    class ParentMethods:
        def is_positive_definite(self):
            """Always True for positive definite forms."""
            return True
        
        def is_definite(self):
            """Always True for definite forms."""
            return True
        
        def is_anisotropic(self):
            """Always True - no non-zero isotropic vectors."""
            return True
        
        def signature(self):
            """Signature is (n, 0, 0) for rank n."""
            n = self.rank()
            return (n, 0, 0)
        
        def witt_index(self):
            """Witt index is always 0."""
            return 0
        
        def inner_product(self, v, w):
            """Proper inner product for positive definite forms."""
            return self.bilinear_form(v, w)
        
        def norm(self, v):
            """Euclidean norm: ||v|| = √⟨v,v⟩."""
            from sage.functions.other import sqrt
            return sqrt(self.quadratic_form(v))
        
        def orthonormal_basis(self):
            """
            Return orthonormal basis via Gram-Schmidt.
            
            Each basis vector has norm 1 and is orthogonal to others.
            
            EXAMPLES::
            
                sage: G = matrix(QQ, [[2, 1], [1, 2]])
                sage: M = SymmetricBilinearModule(G)
                sage: ortho_basis = M.orthonormal_basis()
                sage: all(M.norm(v) == 1 for v in ortho_basis)
                True
            """
            # Gram-Schmidt orthogonalization followed by normalization
            basis = list(self.gens())
            orthonormal = []
            
            for v in basis:
                # Subtract projections onto previous orthonormal vectors
                orthogonal_v = v
                for u in orthonormal:
                    proj_coeff = self.inner_product(v, u)
                    orthogonal_v = orthogonal_v - proj_coeff * u
                
                # Normalize
                if not orthogonal_v.is_zero():
                    norm = self.norm(orthogonal_v)
                    unit_vector = orthogonal_v / norm
                    orthonormal.append(unit_vector)
            
            return orthonormal
        
        def distance(self, v, w):
            """Euclidean distance between elements."""
            return self.norm(v - w)
        
        def angle(self, v, w):
            """
            Angle between vectors (in radians).
            
            Uses arccos(⟨v,w⟩ / (||v|| ||w||)).
            """
            if v.is_zero() or w.is_zero():
                raise ValueError("Cannot compute angle with zero vector")
            
            cos_angle = self.inner_product(v, w) / (self.norm(v) * self.norm(w))
            from sage.functions.trig import arccos
            return arccos(cos_angle)
    
    class ElementMethods:
        def norm(self):
            """Euclidean norm of this element."""
            return self.parent().norm(self)
        
        def normalize(self):
            """Return unit vector in same direction."""
            norm = self.norm()
            if norm == 0:
                raise ValueError("Cannot normalize zero vector")
            return self / norm
        
        def is_unit_vector(self):
            """Test if this is a unit vector."""
            return self.norm() == 1
        
        def distance_to(self, other):
            """Euclidean distance to another element."""
            return self.parent().distance(self, other)
        
        def angle_with(self, other):
            """Angle with another vector."""
            return self.parent().angle(self, other)
        
        def is_positive(self):
            """Always True for non-zero vectors (q(v) > 0)."""
            return not self.is_zero()
        
        def is_negative(self):
            """Always False for positive definite forms."""
            return False
        
        def is_isotropic(self):
            """Only zero vector is isotropic."""
            return self.is_zero()


class NegativeDefinite(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for negative definite symmetric bilinear forms.
    
    A symmetric form is negative definite if q(v) < 0 for all v ≠ 0.
    Equivalently, all eigenvalues are negative.
    
    Properties:
    - Signature is (0, n, 0) for rank n
    - No proper inner product (all norms are imaginary)  
    - Can define "pseudo-norm" ||v|| = √|q(v)|
    - Isomorphic to negative of positive definite form
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(QQ).NegativeDefinite()
        sage: G = matrix(QQ, [[-1, 0], [0, -2]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: M.signature()
        (0, 2, 0)
    """
    
    class ParentMethods:
        def is_negative_definite(self):
            """Always True for negative definite forms."""
            return True
        
        def is_definite(self):
            """Always True for definite forms."""
            return True
        
        def is_anisotropic(self):
            """Always True - no non-zero isotropic vectors."""
            return True
        
        def signature(self):
            """Signature is (0, n, 0) for rank n."""
            n = self.rank()
            return (0, n, 0)
        
        def witt_index(self):
            """Witt index is always 0."""
            return 0
        
        def pseudo_norm(self, v):
            """Pseudo-norm: ||v|| = √|q(v)|."""
            from sage.functions.other import sqrt
            return sqrt(abs(self.quadratic_form(v)))
    
    class ElementMethods:
        def is_positive(self):
            """Always False for negative definite forms."""
            return False
        
        def is_negative(self):
            """Always True for non-zero vectors."""
            return not self.is_zero()
        
        def is_isotropic(self):
            """Only zero vector is isotropic."""
            return self.is_zero()
        
        def pseudo_norm(self):
            """Pseudo-norm for negative definite forms."""
            return self.parent().pseudo_norm(self)


class Definite(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for definite symmetric bilinear forms.
    
    A form is definite if it's either positive definite or negative definite.
    Equivalently, all eigenvalues have the same sign (all > 0 or all < 0).
    
    Properties:
    - No non-zero isotropic vectors
    - Witt index = 0
    - Signature is either (n, 0, 0) or (0, n, 0)
    - Anisotropic (equivalent for definite forms)
    """
    
    class ParentMethods:
        def is_definite(self):
            """Always True for definite forms."""
            return True
        
        def is_anisotropic(self):
            """Definite forms are always anisotropic."""
            return True
        
        def witt_index(self):
            """Witt index is 0 for definite forms."""
            return 0
        
        def has_isotropic_vectors(self):
            """No non-zero isotropic vectors."""
            return False
    
    class ElementMethods:
        def is_isotropic(self):
            """Only zero vector is isotropic in definite forms."""
            return self.is_zero()
```

## Indefinite Forms

```python
class Indefinite(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for indefinite symmetric bilinear forms.
    
    A symmetric form is indefinite if it has both positive and negative
    eigenvalues. Signature is (p, q, 0) with p, q > 0.
    
    Properties:
    - Mixed signature with p, q > 0
    - Contains isotropic vectors (light cone)
    - Witt index > 0
    - Hyperbolic geometry structure
    - Connection to Lorentz groups O(p,q)
    - Minkowski spacetime (signature (3,1) or (1,3))
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(QQ).Indefinite()
        sage: # Hyperbolic plane
        sage: H = matrix(QQ, [[1, 0], [0, -1]])
        sage: M = SymmetricBilinearModule(H)
        sage: M in C
        True
        sage: M.signature()
        (1, 1, 0)
        sage: M.witt_index()
        1
    """
    
    class ParentMethods:
        def is_indefinite(self):
            """Always True for indefinite forms."""
            return True
        
        def is_anisotropic(self):
            """Always False - indefinite forms have isotropic vectors."""
            return False
        
        def witt_index(self):
            """Witt index > 0 for indefinite forms."""
            p, q, r = self.signature()
            return min(p, q)
        
        def light_cone(self):
            """
            Return description of light cone (isotropic vectors).
            
            Light cone is {v : q(v) = 0}, consisting of vectors with
            zero quadratic form evaluation.
            
            OUTPUT:
            Dictionary describing light cone structure
            """
            p, q, r = self.signature()
            witt_idx = min(p, q)
            
            return {
                'dimension': 2 * witt_idx + r,  # Dimension of light cone
                'witt_index': witt_idx,
                'radical_dimension': r,
                'is_cone': (r == 0),  # True cone vs. degenerate
                'signature': (p, q, r)
            }
        
        def positive_cone(self):
            """Region where q(v) > 0."""
            return {'description': 'Vectors with positive quadratic form'}
        
        def negative_cone(self):
            """Region where q(v) < 0."""
            return {'description': 'Vectors with negative quadratic form'}
        
        def maximal_isotropic_subspace(self):
            """
            Find maximal isotropic subspace.
            
            Dimension equals Witt index.
            """
            # This would implement algorithm to find explicit isotropic basis
            w = self.witt_index()
            return f"Isotropic subspace of dimension {w}"
        
        def hyperbolic_decomposition(self):
            """
            Decompose into hyperbolic planes plus anisotropic part.
            
            M ≅ H^⊕w ⊕ A where H is hyperbolic plane and A is anisotropic.
            """
            p, q, r = self.signature()
            w = min(p, q)
            
            return {
                'hyperbolic_planes': w,
                'anisotropic_signature': (p - w, q - w, r),
                'witt_index': w
            }
    
    class ElementMethods:
        def is_timelike(self):
            """
            Test if vector is timelike (q(v) < 0 in Lorentzian signature).
            
            Convention: timelike vectors have negative norm squared.
            """
            return self.quadratic_form() < 0
        
        def is_spacelike(self):
            """Test if vector is spacelike (q(v) > 0)."""
            return self.quadratic_form() > 0
        
        def is_lightlike(self):
            """Test if vector is lightlike/null (q(v) = 0)."""
            return self.is_isotropic()
        
        def causal_type(self):
            """
            Return causal type for Lorentzian geometry.
            
            OUTPUT:
            'timelike', 'spacelike', 'lightlike', or 'zero'
            """
            if self.is_zero():
                return 'zero'
            elif self.is_isotropic():
                return 'lightlike'
            elif self.quadratic_form() < 0:
                return 'timelike'
            else:
                return 'spacelike'
        
        def proper_time_distance_to(self, other):
            """
            Proper time distance in Lorentzian geometry.
            
            Only defined for timelike separated vectors.
            """
            diff = self - other
            if not diff.is_timelike():
                raise ValueError("Vectors not timelike separated")
            
            from sage.functions.other import sqrt
            return sqrt(-diff.quadratic_form())
```

## Anisotropic and Isotropic

```python
class Anisotropic(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for anisotropic symmetric bilinear forms.
    
    A form is anisotropic if it has no non-zero isotropic vectors.
    Equivalently, Witt index = 0 and the form is non-degenerate.
    
    Properties:
    - No non-zero solutions to q(v) = 0
    - Witt index = 0
    - Either definite or "totally indefinite" (rare)
    - Classification by Hasse invariants (number theory)
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(QQ).Anisotropic()
        sage: # Positive definite is anisotropic
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: M.witt_index()
        0
    """
    
    class ParentMethods:
        def is_anisotropic(self):
            """Always True for anisotropic forms."""
            return True
        
        def witt_index(self):
            """Always 0 for anisotropic forms."""
            return 0
        
        def has_isotropic_vectors(self):
            """No non-zero isotropic vectors."""
            return False
        
        def represents_zero_nontrivially(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            """Test if form represents zero non-trivially."""
            return False  # Anisotropic forms don't represent zero
    
    class ElementMethods:
        def is_isotropic(self):
            """Only zero vector is isotropic."""
            return self.is_zero()


class Isotropic(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for isotropic symmetric bilinear forms.
    
    A form is isotropic if it has non-zero isotropic vectors.
    Equivalently, Witt index > 0 or the form is degenerate.
    
    This is the complement of Anisotropic.
    """
    
    class ParentMethods:
        def is_anisotropic(self):
            """Always False for isotropic forms."""
            return False
        
        def has_isotropic_vectors(self):
            """Always True - has non-zero isotropic vectors."""
            return True
        
        def represents_zero_nontrivially(self):
            """Isotropic forms represent zero non-trivially."""
            return True
```

## Integral Forms

```python
class Integral(SymmetricBilinearModulesWithAxiom):
    """
    Axiom for integral quadratic forms.
    
    A quadratic form is integral if q(v) ∈ Z for all v in some Z-lattice.
    Equivalently, the Gram matrix has integer entries.
    
    Properties:
    - Gram matrix entries in Z
    - Number-theoretic properties
    - Theta series with integer coefficients
    - Connection to lattice theory
    - Classification by genus theory
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(ZZ).Integral()
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: M.discriminant()
        5
    """
    
    class ParentMethods:
        def is_integral(self):
            """Always True for integral forms."""
            return True
        
        def discriminant_group(self):
            """
            Return discriminant group L*/L.
            
            This is the finite abelian group of vectors in dual
            lattice modulo original lattice.
            """
            if self.discriminant() == 0:
                raise ValueError("Discriminant group not defined for degenerate forms")
            
            # |L*/L| = |discriminant|
            return abs(self.discriminant())
        
        def dual_lattice(self):
            """Return dual lattice L* = {v : b(v,L) ⊆ Z}."""
            G = self.gram_matrix()
            if G.determinant() == 0:
                raise ValueError("Dual lattice not defined for degenerate forms")
            
            dual_gram = G.inverse()
            return SymmetricBilinearModule(dual_gram)
        
        def is_self_dual(self):
            """Test if L = L* (self-dual lattice)."""
            return abs(self.discriminant()) == 1
        
        def theta_series(self, precision=10):
            """
            Theta series: θ(q) = Σ q^{n(v)} where sum over lattice.
            
            INPUT:
            - precision -- number of terms
            
            OUTPUT:
            Power series in q
            """
            # This requires sophisticated lattice enumeration
            raise NotImplementedError("Theta series computation")
    
    class ElementMethods:
        def quadratic_form_value(self):
            """Integer value of quadratic form."""
            val = self.quadratic_form()
            if val not in ZZ:
                raise ValueError("Non-integer quadratic form value")
            return ZZ(val)


class EvenIntegral(Integral):
    """
    Axiom for even integral quadratic forms.
    
    A form is even if q(v) ∈ 2Z for all v (diagonal entries even).
    This is stronger than just being integral.
    
    Properties:
    - All diagonal entries of Gram matrix are even
    - q(v) always even for lattice vectors
    - Richer theory than odd integral forms
    - Connection to modular forms (level 1 vs level 2)
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(ZZ).EvenIntegral()
        sage: G = matrix(ZZ, [[2, 1], [1, 2]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: all(G[i,i] % 2 == 0 for i in range(2))
        True
    """
    
    class ParentMethods:
        def is_even(self):
            """Always True for even integral forms."""
            return True
        
        def is_odd(self):
            """Always False for even forms."""
            return False
    
    class ElementMethods:
        def is_even_vector(self):
            """All vectors have even quadratic form in even lattices."""
            return True


class Unimodular(Integral):
    """
    Axiom for unimodular integral forms.
    
    A lattice is unimodular if its discriminant is ±1.
    Equivalently, L = L* (self-dual).
    
    Properties:
    - Discriminant = ±1
    - Self-dual: L = L*
    - Finite classification in low dimensions
    - E₈, Leech lattice examples
    - Connection to exceptional Lie groups
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(ZZ).Unimodular()
        sage: # Hyperbolic plane is unimodular
        sage: H = matrix(ZZ, [[0, 1], [1, 0]])
        sage: M = SymmetricBilinearModule(H)
        sage: M.discriminant()
        -1
        sage: M in C
        True
    """
    
    class ParentMethods:
        def is_unimodular(self):
            """Always True for unimodular forms."""
            return True
        
        def discriminant(self):
            """Discriminant is ±1 for unimodular forms."""
            disc = super().discriminant()
            assert abs(disc) == 1
            return disc
        
        def is_self_dual(self):
            """Unimodular forms are always self-dual."""
            return True
```

## Axiom Relationships

```python
# Mathematical axiom hierarchy relationships:

# Primary signature-based classification:
# PositiveDefinite ⊆ Definite ⊆ Nondegenerate ⊆ SymmetricBilinearModules
# NegativeDefinite ⊆ Definite ⊆ Nondegenerate ⊆ SymmetricBilinearModules
# Indefinite ⊆ Nondegenerate ⊆ SymmetricBilinearModules

# Isotropy classification:
# Anisotropic ⊆ Nondegenerate ⊆ SymmetricBilinearModules
# Isotropic = Complement of Anisotropic

# Integrality hierarchy:
# Unimodular ⊆ Integral ⊆ SymmetricBilinearModules
# EvenIntegral ⊆ Integral ⊆ SymmetricBilinearModules

# Key relationships:
# Definite ⟺ Anisotropic (for non-degenerate forms)
# PositiveDefinite ∩ NegativeDefinite = ∅
# PositiveDefinite ∪ NegativeDefinite ∪ Indefinite = Nondegenerate
# EvenIntegral ∩ Unimodular gives important lattice classes

# Dimension-dependent properties:
# Dimension 1: Always definite (positive or negative)
# Dimension 2: Can be definite, indefinite, or degenerate  
# High dimensions: Generic forms are indefinite (over Q)

def _test_axiom_relationships():
    """Verify mathematical relationships between axioms."""
    # Test suite would verify all the above relationships
    pass

# Integration with other categories:
def orthogonal_group_axioms():
    """
    Different axioms give different orthogonal groups:
    - PositiveDefinite → O(n) (compact)
    - Indefinite with signature (p,q) → O(p,q) (non-compact)
    - Unimodular → Arithmetic subgroups
    - EvenIntegral → Connections to modular forms
    """
    pass
```

This axiom system provides mathematically principled specialization of symmetric bilinear modules based on signature, definiteness, isotropy, and integrality properties, enabling efficient specialized algorithms and maintaining connections to number theory, geometry, and lattice theory.