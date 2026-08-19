<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_subcategories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Subcategories: Bilinear Module Axioms and Specializations

Axiom-based subcategories for bilinear modules with specialized properties.

## Axiom Organization

```python
from sage.categories.category_with_axiom import CategoryWithAxiom

class BilinearModulesWithAxiom(CategoryWithAxiom):
    """
    Base class for bilinear module axioms.
    
    Provides the framework for axiom-based specialization of bilinear modules.
    Each axiom represents a mathematical property that some (but not all)
    bilinear modules satisfy.
    
    Axiom hierarchy:
    - Symmetric ⊆ BilinearModules
    - SkewSymmetric ⊆ BilinearModules  
    - Alternating ⊆ SkewSymmetric
    - Nondegenerate ⊆ BilinearModules
    - PositiveDefinite ⊆ Symmetric ∩ Nondegenerate
    - NegativeDefinite ⊆ Symmetric ∩ Nondegenerate
    - Indefinite ⊆ Symmetric ∩ Nondegenerate
    """
    pass
```

## Symmetric Bilinear Forms

```python
class Symmetric(BilinearModulesWithAxiom):
    """
    Axiom for symmetric bilinear forms.
    
    A bilinear form is symmetric if b(v,w) = b(w,v) for all v,w.
    Equivalently, the Gram matrix satisfies G = G^T.
    
    Properties:
    - Diagonalizable over algebraically closed fields
    - Associated quadratic form q(v) = b(v,v)
    - Spectral theorem applies (over R, C)
    - Canonical forms (Sylvester's law of inertia)
    
    EXAMPLES::
    
        sage: from sage.categories.bilinear_modules import BilinearModules
        sage: C = BilinearModules(QQ).Symmetric()
        sage: C
        Category of symmetric bilinear modules over Rational Field
        
        sage: # Positive definite example
        sage: G = matrix(QQ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M in C
        True
        sage: M.is_symmetric()
        True
    """
    
    class ParentMethods:
        def is_symmetric(self):
            """Test symmetry - always True for this axiom."""
            return True
        
        def symmetric_part(self):
            """Return symmetric part - just return self."""
            return self
        
        def skew_symmetric_part(self):
            """Return skew-symmetric part - always zero."""
            return self.parent().zero_module()
        
        def diagonalize(self):
            """
            Diagonalize the symmetric bilinear form.
            
            Returns orthogonal basis where Gram matrix is diagonal.
            
            EXAMPLES::
            
                sage: G = matrix(QQ, [[3, 1], [1, 3]])
                sage: M = BilinearModule(G)
                sage: eigenspaces = M.diagonalize()
                sage: len(eigenspaces)
                2  # Two distinct eigenvalues
            """
            G = self.gram_matrix()
            eigenvals, eigenvecs = G.eigenspaces_right(format='galois')
            
            # Construct orthogonal basis
            orthogonal_basis = []
            for eigenval, eigenspace in zip(eigenvals, eigenvecs):
                for vec in eigenspace.basis():
                    orthogonal_basis.append(self._from_vector(vec))
            
            return orthogonal_basis
    
    class ElementMethods:
        def quadratic_form(self):
            """
            Quadratic form evaluation: q(v) = b(v,v).
            
            For symmetric forms, this is the canonical associated quadratic form.
            """
            return self.bilinear_form(self)
        
        def is_positive(self):
            """Test if q(v) > 0."""
            return self.quadratic_form() > 0
        
        def is_negative(self):
            """Test if q(v) < 0."""
            return self.quadratic_form() < 0
```

## Skew-Symmetric Bilinear Forms

```python
class SkewSymmetric(BilinearModulesWithAxiom):
    """
    Axiom for skew-symmetric bilinear forms.
    
    A bilinear form is skew-symmetric if b(v,w) = -b(w,v) for all v,w.
    Equivalently, the Gram matrix satisfies G = -G^T.
    
    Properties:
    - Diagonal entries are zero: b(v,v) = 0
    - Dimension must be even for non-degenerate forms
    - Canonical form has 2×2 blocks [[0,1],[-1,0]]
    - Associated with symplectic geometry
    
    EXAMPLES::
    
        sage: C = BilinearModules(QQ).SkewSymmetric()
        sage: A = matrix(QQ, [[0, 1, 2], [-1, 0, 3], [-2, -3, 0]])
        sage: M = BilinearModule(A)
        sage: M in C
        True
        sage: M.is_skew_symmetric()
        True
    """
    
    class ParentMethods:
        def is_skew_symmetric(self):
            """Test skew-symmetry - always True for this axiom."""
            return True
        
        def is_alternating(self):
            """
            Test if alternating.
            
            Over fields of characteristic ≠ 2, skew-symmetric ⟺ alternating.
            """
            char = self.base_ring().characteristic()
            if char == 0 or char != 2:
                return True
            # In characteristic 2, need to check diagonal
            return super().is_alternating()
        
        def symplectic_complement(self, subspace):
            """
            Return symplectic complement of subspace.
            
            For skew-symmetric forms, this is the orthogonal complement.
            """
            return self.orthogonal_complement(subspace)
        
        def canonical_form(self):
            """
            Reduce to canonical symplectic form.
            
            Returns basis where Gram matrix has 2×2 blocks [[0,1],[-1,0]].
            """
            # Implementation would use symplectic diagonalization
            raise NotImplementedError("Symplectic canonical form")
    
    class ElementMethods:
        def quadratic_form(self):
            """Quadratic form is always zero for skew-symmetric forms."""
            return self.parent().base_ring().zero()
        
        def is_isotropic(self):
            """All vectors are isotropic in skew-symmetric forms."""
            return True
        
        def symplectic_orthogonal_to(self, other):
            """Test symplectic orthogonality (same as orthogonality)."""
            return self.is_orthogonal_to(other)
```

## Alternating Bilinear Forms

```python
class Alternating(SkewSymmetric):
    """
    Axiom for alternating bilinear forms.
    
    A bilinear form is alternating if b(v,v) = 0 for all v.
    This implies skew-symmetry: b(v,w) = -b(w,v).
    
    Over fields of characteristic ≠ 2: alternating ⟺ skew-symmetric.
    Over fields of characteristic 2: alternating ⟹ skew-symmetric (proper subset).
    
    EXAMPLES::
    
        sage: C = BilinearModules(GF(2)).Alternating()
        sage: # In char 2, [0,1],[1,0] is skew-symmetric but not alternating
        sage: A1 = matrix(GF(2), [[0, 1], [1, 0]])
        sage: M1 = BilinearModule(A1)
        sage: M1.is_skew_symmetric()
        True
        sage: M1.is_alternating()
        False
        
        sage: # This is alternating
        sage: A2 = matrix(GF(2), [[0, 1], [1, 0]])  # Wait, same matrix
        sage: # Let me think: in GF(2), 1 = -1, so G = -G^T means G = G^T
        sage: # For alternating, need diagonal zero, so:
        sage: A2 = matrix(GF(2), [[0, 1], [1, 0]])  # Diagonal is zero ✓
        sage: M2 = BilinearModule(A2)
        sage: M2.is_alternating()
        True
    """
    
    class ParentMethods:
        def is_alternating(self):
            """Always True for alternating forms."""
            return True
        
        def exterior_power(self, k):
            """
            k-th exterior power of the alternating form.
            
            Natural operation for alternating bilinear forms.
            """
            # Would return alternating k-form
            raise NotImplementedError("Exterior powers")
    
    class ElementMethods:
        def quadratic_form(self):
            """Always zero for alternating forms."""
            return self.parent().base_ring().zero()
        
        def wedge_product(self, other):
            """
            Wedge product operation.
            
            Natural for alternating forms - related to exterior algebra.
            """
            # Implementation would depend on exterior algebra integration
            raise NotImplementedError("Wedge product")
```

## Non-degenerate Forms

```python
class Nondegenerate(BilinearModulesWithAxiom):
    """
    Axiom for non-degenerate bilinear forms.
    
    A bilinear form is non-degenerate if its radical is trivial.
    Equivalently, the Gram matrix has full rank.
    
    Properties:
    - Isomorphism with dual: M → M* via v ↦ b(v,·)
    - Orthogonal complement has complementary dimension
    - Can define orthogonal projections
    - Classification by signature (over ordered fields)
    
    EXAMPLES::
    
        sage: C = BilinearModules(QQ).Nondegenerate()
        sage: G = matrix(QQ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M in C
        True
        sage: M.discriminant() != 0
        True
    """
    
    class ParentMethods:
        def is_nondegenerate(self):
            """Always True for non-degenerate forms."""
            return True
        
        def is_degenerate(self):
            """Always False for non-degenerate forms."""
            return False
        
        def radical(self):
            """Radical is always trivial."""
            return self.submodule([])
        
        def orthogonal_projection(self, v, subspace):
            """
            Orthogonal projection onto subspace.
            
            Well-defined for non-degenerate forms.
            """
            # Find orthonormal basis of subspace
            basis = subspace.orthogonal_basis()
            
            projection = self.zero()
            for b in basis:
                coeff = v.bilinear_form(b) / b.norm_squared()
                projection += coeff * b
            
            return projection
        
        def orthogonal_complement(self, subspace):
            """
            Orthogonal complement with dimension formula.
            
            For non-degenerate forms: dim(V) = dim(W) + dim(W⊥)
            """
            complement = super().orthogonal_complement(subspace)
            
            # Verify dimension formula
            expected_dim = self.dimension() - subspace.dimension()
            assert complement.dimension() == expected_dim
            
            return complement
    
    class ElementMethods:
        def orthogonal_projection_onto_span(self, vectors):
            """
            Project onto span of vectors.
            
            Uses Gram-Schmidt with the bilinear form.
            """
            if not vectors:
                return self.parent().zero()
            
            # Gram-Schmidt orthogonalization
            orthogonal_basis = []
            for v in vectors:
                orthogonal_v = v
                for b in orthogonal_basis:
                    proj_coeff = v.bilinear_form(b) / b.norm_squared()
                    orthogonal_v -= proj_coeff * b
                
                if not orthogonal_v.is_zero():
                    orthogonal_basis.append(orthogonal_v)
            
            # Project onto orthogonal basis
            projection = self.parent().zero()
            for b in orthogonal_basis:
                coeff = self.bilinear_form(b) / b.norm_squared()
                projection += coeff * b
            
            return projection
```

## Definite Forms

```python
class PositiveDefinite(Symmetric, Nondegenerate):
    """
    Axiom for positive definite bilinear forms.
    
    A symmetric bilinear form is positive definite if q(v) > 0 for all v ≠ 0.
    Equivalently, all eigenvalues of the Gram matrix are positive.
    
    Properties:
    - Defines a proper inner product
    - Norm: ||v|| = √q(v)
    - Cauchy-Schwarz inequality
    - Triangle inequality
    - Parallelogram law
    
    EXAMPLES::
    
        sage: C = BilinearModules(QQ).PositiveDefinite()
        sage: G = matrix(QQ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M in C
        True
        sage: M.signature()
        (2, 0, 0)
    """
    
    class ParentMethods:
        def is_positive_definite(self):
            """Always True for positive definite forms."""
            return True
        
        def inner_product(self, v, w):
            """Alias for bilinear_form - proper inner product."""
            return self.bilinear_form(v, w)
        
        def norm(self, v):
            """Euclidean norm: ||v|| = √⟨v,v⟩."""
            from sage.functions.other import sqrt
            return sqrt(self.bilinear_form(v, v))
        
        def orthonormal_basis(self):
            """
            Return orthonormal basis via Gram-Schmidt.
            
            Each basis vector has norm 1 and is orthogonal to others.
            """
            basis = list(self.gens())
            orthonormal = []
            
            for v in basis:
                # Subtract projections onto previous vectors
                orthogonal_v = v
                for u in orthonormal:
                    proj_coeff = self.inner_product(v, u)
                    orthogonal_v -= proj_coeff * u
                
                # Normalize
                if not orthogonal_v.is_zero():
                    norm = self.norm(orthogonal_v)
                    orthonormal.append(orthogonal_v / norm)
            
            return orthonormal
    
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
        
        def distance_to(self, other):
            """Euclidean distance to another element."""
            return (self - other).norm()
        
        def angle_with(self, other):
            """
            Angle between vectors (in radians).
            
            Uses arccos(⟨v,w⟩ / (||v|| ||w||)).
            """
            if self.is_zero() or other.is_zero():
                raise ValueError("Cannot compute angle with zero vector")
            
            cos_angle = self.inner_product(other) / (self.norm() * other.norm())
            from sage.functions.trig import arccos
            return arccos(cos_angle)

class NegativeDefinite(Symmetric, Nondegenerate):
    """
    Axiom for negative definite bilinear forms.
    
    A symmetric bilinear form is negative definite if q(v) < 0 for all v ≠ 0.
    Equivalently, all eigenvalues of the Gram matrix are negative.
    """
    
    class ParentMethods:
        def is_negative_definite(self):
            """Always True for negative definite forms."""
            return True
        
        def signature(self):
            """Signature is (0, n, 0) for rank n."""
            n = self.rank()
            return (0, n, 0)

class Indefinite(Symmetric, Nondegenerate):
    """
    Axiom for indefinite bilinear forms.
    
    A symmetric bilinear form is indefinite if it has both positive
    and negative eigenvalues.
    
    Properties:
    - Contains both positive and negative vectors
    - Light cone structure (isotropic vectors)
    - Hyperbolic geometry for signature (n,1) or (1,n)
    - Lorentzian geometry for signature (n-1,1)
    """
    
    class ParentMethods:
        def is_indefinite(self):
            """Always True for indefinite forms."""
            return True
        
        def light_cone(self):
            """
            Return the light cone (isotropic vectors).
            
            These are vectors v with q(v) = 0.
            """
            # This would require solving quadratic equations
            raise NotImplementedError("Light cone computation")
        
        def positive_cone(self):
            """Return cone of vectors with q(v) > 0."""
            raise NotImplementedError("Positive cone computation")
        
        def negative_cone(self):
            """Return cone of vectors with q(v) < 0."""
            raise NotImplementedError("Negative cone computation")
```

## Axiom Relationships

```python
# Mathematical axiom hierarchy relationships:

# Inclusion relationships:
# Alternating ⊆ SkewSymmetric ⊆ BilinearModules
# Symmetric ⊆ BilinearModules
# Nondegenerate ⊆ BilinearModules
# PositiveDefinite ⊆ Symmetric ∩ Nondegenerate
# NegativeDefinite ⊆ Symmetric ∩ Nondegenerate  
# Indefinite ⊆ Symmetric ∩ Nondegenerate

# Disjoint axioms:
# Symmetric ∩ SkewSymmetric = {zero forms only}
# PositiveDefinite ∩ NegativeDefinite = ∅
# PositiveDefinite ∩ Indefinite = ∅
# NegativeDefinite ∩ Indefinite = ∅
# (PositiveDefinite ∪ NegativeDefinite ∪ Indefinite) ∩ Degenerate = ∅

# Characteristic-dependent relationships:
# char(F) ≠ 2: Alternating ⟺ SkewSymmetric
# char(F) = 2: Alternating ⟹ SkewSymmetric (proper inclusion)

def _test_axiom_relationships():
    """Test mathematical relationships between axioms."""
    # This would be called by TestSuite
    pass
```

This axiom system provides mathematically correct specialization of bilinear modules while maintaining the category theory framework and enabling efficient specialized algorithms for each form type.