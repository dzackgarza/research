<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: BilinearModules(R)

The category of R-modules equipped with bilinear forms, inheriting from RModules(R).

## Category Definition

```python
from sage.categories.category_with_axiom import CategoryWithAxiom

class BilinearModules(CategoryWithAxiom):
    """
    The category of R-modules equipped with bilinear forms.
    
    This category extends RModules(R) by adding a bilinear form
    b: M ⊗_R M → R to each module. The bilinear form must satisfy:
    - Linearity in each argument
    - R-multilinearity: b(rx, y) = r·b(x,y) = b(x, ry)
    
    Objects in this category include:
    - Symmetric bilinear modules (b(x,y) = b(y,x))  
    - Skew-symmetric bilinear modules (b(x,y) = -b(y,x))
    - General bilinear modules (no symmetry constraint)
    - Lattices (integral bilinear forms)
    - Quadratic forms (via polarization: q(x) = b(x,x))
    
    The category provides:
    - All RModules functionality (natural operations +, *, @, /)
    - Bilinear form evaluation and properties
    - Gram matrix computations
    - Discriminant and signature invariants
    - Orthogonality and radical computations
    - Specialized constructions (dual, tensor, direct sum)
    
    EXAMPLES::
    
        sage: C = BilinearModules(ZZ)
        sage: C
        Category of bilinear modules over Integer Ring
        sage: C.super_categories()
        [Category of R-modules over Integer Ring]
        
        sage: # Hyperbolic plane
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: H in C
        True
        sage: H.discriminant()
        -1
        sage: H.is_indefinite()
        True
    """
    
    def super_categories(self):
        """
        BilinearModules inherits all structure from RModules.
        
        This ensures we get:
        - Abelian category structure (exact sequences, kernels, cokernels)
        - Natural operations (+, *, @, /) for split Grothendieck ring
        - Module homomorphism universal properties
        - Tensor-hom adjunction
        - Optional symmetric monoidal structures
        
        EXAMPLES::
        
            sage: BilinearModules(QQ).super_categories()
            [Category of R-modules over Rational Field]
        """
        return [RModules(self.base_ring())]
    
    def _repr_(self):
        """
        String representation of the category.
        
        EXAMPLES::
        
            sage: BilinearModules(ZZ)
            Category of bilinear modules over Integer Ring
        """
        return f"Category of bilinear modules over {self.base_ring()}"
    
    def WithBasis(self):
        """
        Return the subcategory of bilinear modules with basis.
        
        For bilinear modules with basis, we can:
        - Compute Gram matrices
        - Convert between coordinate and symbolic representations
        - Perform efficient orthogonality computations
        - Apply basis change transformations
        
        EXAMPLES::
        
            sage: C = BilinearModules(ZZ).WithBasis()
            sage: C
            Category of bilinear modules with basis over Integer Ring
        """
        return BilinearModulesWithBasis(self.base_ring())
```

## Bilinear Form Interface

```python
class ParentMethods:
    """
    Methods available on bilinear module parent objects.
    
    These methods extend RModules.ParentMethods with bilinear form
    functionality while preserving all inherited operations.
    """
    
    def bilinear_form(self, v, w):
        """
        Evaluate the bilinear form on two elements.
        
        INPUT:
        - v, w -- elements of this bilinear module
        
        OUTPUT:
        Value b(v,w) in the base ring
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: e, f = M.gens()
            sage: M.bilinear_form(e, f)
            1
            sage: M.bilinear_form(e, e)
            2
            sage: M.bilinear_form(f, f)
            3
        """
        raise NotImplementedError("Subclasses must implement bilinear_form")
    
    def is_symmetric(self):
        """
        Test if the bilinear form is symmetric.
        
        A bilinear form is symmetric if b(v,w) = b(w,v) for all v,w.
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.is_symmetric()
            True
            
            sage: H = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))  
            sage: H.is_symmetric()
            False
            sage: H.is_skew_symmetric()
            True
        """
        raise NotImplementedError("Subclasses must implement is_symmetric")
    
    def is_skew_symmetric(self):
        """
        Test if the bilinear form is skew-symmetric.
        
        A bilinear form is skew-symmetric if b(v,w) = -b(w,v) for all v,w.
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: H = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))
            sage: H.is_skew_symmetric()
            True
            
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.is_skew_symmetric()
            False
        """
        raise NotImplementedError("Subclasses must implement is_skew_symmetric")
    
    def is_alternating(self):
        """
        Test if the bilinear form is alternating.
        
        A bilinear form is alternating if b(v,v) = 0 for all v.
        Over rings where 2 is invertible, alternating ⟺ skew-symmetric.
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: H = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))
            sage: H.is_alternating()
            True
            
            sage: # Over Z/2Z, different from skew-symmetric
            sage: R = GF(2)
            sage: M = BilinearModule(matrix(R, [[0, 1], [1, 0]]))
            sage: M.is_skew_symmetric()
            True
            sage: M.is_alternating()  
            False  # b(e,e) = 0 but b(f,f) = 0, so alternating
        """
        # Default implementation: check b(v,v) = 0 for basis elements
        if hasattr(self, 'gens'):
            for v in self.gens():
                if self.bilinear_form(v, v) != 0:
                    return False
            return True
        raise NotImplementedError("Cannot test alternating without basis")
    
    def radical(self):
        """
        Return the radical (left kernel) of the bilinear form.
        
        The radical is Rad(M) = {v ∈ M : b(v,w) = 0 for all w ∈ M}.
        The form is non-degenerate iff the radical is zero.
        
        OUTPUT:
        Submodule of this module
        
        EXAMPLES::
        
            sage: # Non-degenerate form
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.radical().dimension()
            0
            
            sage: # Degenerate form
            sage: D = BilinearModule(matrix(ZZ, [[1, 1], [1, 1]]))
            sage: D.radical().dimension()
            1
        """
        raise NotImplementedError("Subclasses must implement radical")
    
    def is_degenerate(self):
        """
        Test if the bilinear form is degenerate.
        
        A form is degenerate if its radical is non-trivial.
        Equivalently, if the discriminant is zero.
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.is_degenerate()
            False
            
            sage: D = BilinearModule(matrix(ZZ, [[1, 1], [1, 1]]))
            sage: D.is_degenerate()
            True
        """
        return self.radical().dimension() > 0
    
    def is_nondegenerate(self):
        """
        Test if the bilinear form is non-degenerate.
        
        A form is non-degenerate if its radical is trivial.
        
        OUTPUT:
        Boolean
        """
        return not self.is_degenerate()
```

## Matrix and Invariant Interface

```python
class WithBasisMethods:
    """
    Additional methods for bilinear modules with basis.
    
    Only available when the module has a distinguished basis,
    allowing coordinate-based computations.
    """
    
    def gram_matrix(self, basis=None):
        """
        Return the Gram matrix of the bilinear form.
        
        INPUT:
        - basis -- optional basis (uses module basis if not provided)
        
        OUTPUT:
        Matrix G where G[i,j] = b(basis[i], basis[j])
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.gram_matrix()
            [2 1]
            [1 3]
            
            sage: # Custom basis  
            sage: e, f = M.gens()
            sage: M.gram_matrix([e + f, e - f])
            [6 -1]
            [-1 1]
        """
        if basis is None:
            # Use internal Gram matrix if available
            if hasattr(self, '_gram_matrix'):
                return self._gram_matrix
            basis = self.gens()
        
        # Compute Gram matrix from bilinear form
        n = len(basis)
        from sage.matrix.constructor import matrix
        G = matrix(self.base_ring(), n, n)
        for i in range(n):
            for j in range(n):
                G[i,j] = self.bilinear_form(basis[i], basis[j])
        return G
    
    def discriminant(self):
        """
        Return the discriminant (determinant of Gram matrix).
        
        This is well-defined up to squares in the base ring.
        Zero iff the form is degenerate.
        
        OUTPUT:
        Element of base ring
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.discriminant()
            5
            
            sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
            sage: H.discriminant()
            -1
        """
        return self.gram_matrix().determinant()
    
    def signature(self):
        """
        Return the signature (p, q, r) of the bilinear form.
        
        Where p = # positive eigenvalues, q = # negative eigenvalues,
        r = # zero eigenvalues (dimension of radical).
        
        Only defined over ordered fields (QQ, RR, etc.).
        
        OUTPUT:
        Triple (p, q, r) of integers with p + q + r = rank
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(QQ, [[2, 1], [1, 3]]))
            sage: M.signature()
            (2, 0, 0)  # positive definite
            
            sage: H = BilinearModule(matrix(QQ, [[1, 0], [0, -1]]))
            sage: H.signature()
            (1, 1, 0)  # indefinite (hyperbolic)
        """
        G = self.gram_matrix()
        eigenvals = G.eigenvalues()
        
        pos = sum(1 for ev in eigenvals if ev > 0)
        neg = sum(1 for ev in eigenvals if ev < 0)  
        zero = sum(1 for ev in eigenvals if ev == 0)
        
        return (pos, neg, zero)
    
    def is_positive_definite(self):
        """Test if form is positive definite (all eigenvalues > 0)."""
        p, q, r = self.signature()
        return q == 0 and r == 0
    
    def is_negative_definite(self):
        """Test if form is negative definite (all eigenvalues < 0)."""
        p, q, r = self.signature()
        return p == 0 and r == 0
    
    def is_definite(self):
        """Test if form is definite (positive or negative definite)."""
        return self.is_positive_definite() or self.is_negative_definite()
    
    def is_indefinite(self):
        """Test if form is indefinite (has both positive and negative eigenvalues)."""
        p, q, r = self.signature()
        return p > 0 and q > 0
```

## Enhanced Operations

```python
def orthogonal_complement(self, submodule):
    """
    Return the orthogonal complement of a submodule.
    
    For submodule N ⊆ M, returns N⊥ = {v ∈ M : b(v,w) = 0 for all w ∈ N}.
    
    INPUT:
    - submodule -- submodule of this bilinear module
    
    OUTPUT:
    Submodule representing the orthogonal complement
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: e, f = M.gens()
        sage: N = M.submodule([e])
        sage: N_perp = M.orthogonal_complement(N)
        sage: N_perp.dimension()
        0  # Non-degenerate form, so dim(N) + dim(N⊥) = dim(M)
    """
    raise NotImplementedError("Subclasses must implement orthogonal_complement")

def direct_sum_bilinear(self, other):
    """
    Direct sum of bilinear modules with orthogonal bilinear form.
    
    For (M₁, b₁) and (M₂, b₂), returns (M₁ ⊕ M₂, b₁ ⊕ b₂) where:
    (b₁ ⊕ b₂)((v₁, v₂), (w₁, w₂)) = b₁(v₁, w₁) + b₂(v₂, w₂)
    
    This is different from the module direct sum M₁ + M₂ (which uses
    the same underlying module but may have different bilinear form).
    
    INPUT:  
    - other -- another bilinear module over the same ring
    
    OUTPUT:
    BilinearModule representing the orthogonal direct sum
    
    EXAMPLES::
    
        sage: M1 = BilinearModule(matrix(ZZ, [[2]]))  # rank 1, positive
        sage: M2 = BilinearModule(matrix(ZZ, [[-3]]))  # rank 1, negative  
        sage: M = M1.direct_sum_bilinear(M2)
        sage: M.signature()
        (1, 1, 0)  # indefinite
        sage: M.gram_matrix()
        [2  0]
        [0 -3]
    """
    raise NotImplementedError("Subclasses must implement direct_sum_bilinear")

def tensor_product_bilinear(self, other):
    """
    Tensor product of bilinear modules.
    
    For (M₁, b₁) and (M₂, b₂), returns (M₁ ⊗ M₂, b₁ ⊗ b₂) where:
    (b₁ ⊗ b₂)(v₁ ⊗ w₁, v₂ ⊗ w₂) = b₁(v₁, v₂) · b₂(w₁, w₂)
    
    INPUT:
    - other -- another bilinear module over the same ring
    
    OUTPUT:
    BilinearModule representing the tensor product
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))  # hyperbolic
        sage: N = BilinearModule(matrix(ZZ, [[2]]))  # positive definite
        sage: P = M.tensor_product_bilinear(N) 
        sage: P.signature()
        (1, 1, 0)  # Still hyperbolic
    """
    raise NotImplementedError("Subclasses must implement tensor_product_bilinear")
```

## Mathematical Correctness Tests

The bilinear form interface must satisfy fundamental mathematical properties:

```python
# Mathematical assertion: Bilinearity
# For all r ∈ R, v, w, x ∈ M:
# b(rv + w, x) = r·b(v,x) + b(w,x)  
# b(v, rw + x) = r·b(v,w) + b(v,x)

# Mathematical assertion: Gram matrix symmetry
# G = gram_matrix() satisfies G[i,j] = b(e_i, e_j)
# If is_symmetric(): G = G.transpose()  
# If is_skew_symmetric(): G = -G.transpose()

# Mathematical assertion: Discriminant invariance  
# Under basis change P: det(G') = det(P)² · det(G)
# So discriminant is well-defined modulo squares

# Mathematical assertion: Orthogonal complement dimension
# For non-degenerate forms: dim(N) + dim(N⊥) = dim(M)
# For degenerate forms: dim(M) ≤ dim(N) + dim(N⊥)

# Mathematical assertion: Radical characterization
# v ∈ Rad(M) ⟺ b(v,w) = 0 for all w ∈ M
# dim(Rad(M)) = nullity of Gram matrix
# M is non-degenerate ⟺ Rad(M) = {0}
```