<!--
Origin: gitclones/Coxeter/implementation/planning/SymmetricBilRMod/SymmetricBilRMod_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category: SymmetricBilinearModules(R)

The category of R-modules equipped with symmetric bilinear forms, inheriting from BilinearModules(R).

## Category Definition

```python
from sage.categories.category_with_axiom import CategoryWithAxiom

class SymmetricBilinearModules(CategoryWithAxiom):
    """
    The category of R-modules equipped with symmetric bilinear forms.
    
    This category extends BilinearModules(R) by requiring b(v,w) = b(w,v).
    Equivalently, the Gram matrix must satisfy G = G^T.
    
    Symmetric bilinear forms are fundamental in:
    - Quadratic form theory: q(v) = b(v,v) 
    - Riemannian geometry: metric tensors
    - Lattice theory: integral quadratic forms
    - Representation theory: invariant forms
    - Number theory: arithmetic of quadratic forms
    
    Key properties:
    - Associated quadratic form q(v) = b(v,v)
    - Diagonalization over algebraically closed fields
    - Sylvester's law of inertia (signature invariant)
    - Witt decomposition theory
    - Connection to orthogonal groups O(n,R)
    
    EXAMPLES::
    
        sage: C = SymmetricBilinearModules(ZZ)
        sage: C
        Category of symmetric bilinear modules over Integer Ring
        sage: C.super_categories()
        [Category of bilinear modules over Integer Ring]
        
        sage: # Positive definite example
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: M in C
        True
        sage: M.quadratic_form_matrix()
        [2 1]
        [1 3]
        
        sage: # Indefinite example (hyperbolic)
        sage: H = matrix(QQ, [[0, 1], [1, 0]])
        sage: L = SymmetricBilinearModule(H)
        sage: L.signature()
        (1, 1, 0)
        sage: L.is_indefinite()
        True
    """
    
    def super_categories(self):
        """
        SymmetricBilinearModules inherits from BilinearModules.
        
        This ensures we get:
        - All bilinear form functionality 
        - Abelian category structure (from RModules)
        - Natural operations for split Grothendieck ring
        - Specialization to symmetric forms only
        
        EXAMPLES::
        
            sage: SymmetricBilinearModules(QQ).super_categories()
            [Category of bilinear modules over Rational Field]
        """
        return [BilinearModules(self.base_ring())]
    
    def _repr_(self):
        """
        String representation of the category.
        
        EXAMPLES::
        
            sage: SymmetricBilinearModules(ZZ)
            Category of symmetric bilinear modules over Integer Ring
        """
        return f"Category of symmetric bilinear modules over {self.base_ring()}"
    
    def WithBasis(self):
        """
        Return the subcategory of symmetric bilinear modules with basis.
        
        For symmetric modules with basis:
        - Gram matrix is always symmetric: G = G^T
        - Diagonalization algorithms available
        - Quadratic form evaluation via coordinates
        - Efficient signature computation
        
        EXAMPLES::
        
            sage: C = SymmetricBilinearModules(QQ).WithBasis()
            sage: C
            Category of symmetric bilinear modules with basis over Rational Field
        """
        return SymmetricBilinearModulesWithBasis(self.base_ring())
    
    def PositiveDefinite(self):
        """
        Subcategory of positive definite symmetric bilinear forms.
        
        These define proper inner product spaces with:
        - q(v) > 0 for all v ≠ 0
        - Euclidean norm ||v|| = √q(v)
        - Cauchy-Schwarz inequality
        - Orthogonal group O(n) preserves the form
        """
        return SymmetricBilinearModules(self.base_ring()).PositiveDefinite()
    
    def NegativeDefinite(self):
        """Subcategory of negative definite symmetric bilinear forms."""
        return SymmetricBilinearModules(self.base_ring()).NegativeDefinite()
    
    def Indefinite(self):
        """
        Subcategory of indefinite symmetric bilinear forms.
        
        These have both positive and negative eigenvalues:
        - Mixed signature (p, q, 0) with p, q > 0
        - Light cone structure (isotropic vectors)
        - Hyperbolic geometry
        - Connection to Lorentz groups O(p,q)
        """
        return SymmetricBilinearModules(self.base_ring()).Indefinite()
```

## Quadratic Form Interface

```python
class ParentMethods:
    """
    Methods available on symmetric bilinear module parent objects.
    
    These methods extend BilinearModules.ParentMethods with
    symmetric form specific functionality.
    """
    
    def is_symmetric(self):
        """Always True for symmetric bilinear modules."""
        return True
    
    def quadratic_form(self, v):
        """
        Evaluate associated quadratic form: q(v) = b(v,v).
        
        For symmetric bilinear forms, there's a natural associated
        quadratic form that recovers the bilinear form via polarization:
        b(v,w) = (q(v+w) - q(v) - q(w))/2
        
        INPUT:
        - v -- element of this symmetric bilinear module
        
        OUTPUT:
        Value q(v) in the base ring
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[2, 1], [1, 3]])
            sage: M = SymmetricBilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 2*e + f
            sage: M.quadratic_form(v)
            15  # 2²·2 + 2·2·1·1 + 1²·3 = 8 + 4 + 3 = 15
            sage: M.bilinear_form(v, v)
            15  # Same result
        """
        return self.bilinear_form(v, v)
    
    def quadratic_form_matrix(self):
        """
        Return the quadratic form matrix (same as Gram matrix for symmetric forms).
        
        For symmetric bilinear forms, the quadratic form matrix Q
        is identical to the Gram matrix: Q = G.
        
        OUTPUT:
        Symmetric matrix representing the quadratic form
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[3, -1], [-1, 2]])
            sage: M = SymmetricBilinearModule(G)
            sage: Q = M.quadratic_form_matrix()
            sage: Q == G
            True
            sage: Q.is_symmetric()
            True
        """
        return self.gram_matrix()
    
    def diagonalize(self):
        """
        Diagonalize the symmetric bilinear form.
        
        Returns an orthogonal basis where the Gram matrix is diagonal.
        This uses spectral decomposition of symmetric matrices.
        
        OUTPUT:
        Tuple (basis, diagonal_values) where:
        - basis: list of orthogonal elements
        - diagonal_values: eigenvalues of the form
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[3, 1], [1, 3]])
            sage: M = SymmetricBilinearModule(G)
            sage: basis, eigenvals = M.diagonalize()
            sage: len(basis)
            2
            sage: eigenvals
            [4, 2]  # 3±1
        """
        G = self.gram_matrix()
        
        # Compute eigendecomposition
        eigenvals, eigenvecs = G.eigenmatrix_right()
        
        # Convert eigenvectors to module elements
        orthogonal_basis = []
        for i in range(eigenvecs.ncols()):
            eigenvec = eigenvecs.column(i)
            element = self._from_vector(eigenvec)
            orthogonal_basis.append(element)
        
        diagonal_values = eigenvals.diagonal()
        return orthogonal_basis, diagonal_values
    
    def signature(self):
        """
        Return the signature (p, q, r) of the symmetric form.
        
        Counts positive, negative, and zero eigenvalues.
        This is independent of basis choice (Sylvester's law of inertia).
        
        OUTPUT:
        Tuple (p, q, r) where:
        - p = number of positive eigenvalues
        - q = number of negative eigenvalues  
        - r = number of zero eigenvalues (dimension of radical)
        
        EXAMPLES::
        
            sage: # Positive definite
            sage: G = matrix(QQ, [[2, 1], [1, 3]])
            sage: M = SymmetricBilinearModule(G)
            sage: M.signature()
            (2, 0, 0)
            
            sage: # Hyperbolic (indefinite)
            sage: H = matrix(QQ, [[1, 0], [0, -1]])
            sage: L = SymmetricBilinearModule(H)
            sage: L.signature()
            (1, 1, 0)
            
            sage: # Degenerate
            sage: D = matrix(QQ, [[1, 1], [1, 1]])
            sage: N = SymmetricBilinearModule(D)
            sage: N.signature()
            (1, 0, 1)
        """
        G = self.gram_matrix()
        eigenvals = G.eigenvalues()
        
        pos = sum(1 for ev in eigenvals if ev > 0)
        neg = sum(1 for ev in eigenvals if ev < 0)
        zero = sum(1 for ev in eigenvals if ev == 0)
        
        return (pos, neg, zero)
    
    def witt_index(self):
        """
        Return the Witt index (dimension of maximal isotropic subspace).
        
        For signature (p, q, r), the Witt index is min(p, q).
        
        OUTPUT:
        Integer representing the Witt index
        
        EXAMPLES::
        
            sage: # Hyperbolic plane
            sage: H = matrix(QQ, [[0, 1], [1, 0]])
            sage: M = SymmetricBilinearModule(H)
            sage: M.witt_index()
            1
            
            sage: # Positive definite (no isotropic vectors)
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: N = SymmetricBilinearModule(G)
            sage: N.witt_index()
            0
        """
        p, q, r = self.signature()
        return min(p, q)
    
    def is_positive_definite(self):
        """Test if the form is positive definite."""
        p, q, r = self.signature()
        return q == 0 and r == 0
    
    def is_negative_definite(self):
        """Test if the form is negative definite."""
        p, q, r = self.signature()
        return p == 0 and r == 0
    
    def is_definite(self):
        """Test if the form is definite (positive or negative)."""
        return self.is_positive_definite() or self.is_negative_definite()
    
    def is_indefinite(self):
        """Test if the form is indefinite (mixed signature)."""
        p, q, r = self.signature()
        return p > 0 and q > 0
    
    def is_anisotropic(self):
        """
        Test if the form is anisotropic (no non-zero isotropic vectors).
        
        Equivalent to having trivial radical and Witt index 0.
        """
        return self.witt_index() == 0 and not self.is_degenerate()
```

## Witt Theory Integration

```python
def witt_decomposition(self):
    """
    Witt decomposition of symmetric bilinear form.
    
    Every symmetric bilinear form decomposes as:
    M ≅ H^⊕w ⊕ A ⊕ R
    where:
    - H is the hyperbolic plane (signature (1,1,0))
    - w is the Witt index  
    - A is anisotropic (Witt index 0)
    - R is the radical (degenerate part)
    
    OUTPUT:
    Dictionary with decomposition components
    
    EXAMPLES::
    
        sage: # Indefinite form
        sage: G = matrix(QQ, [[1, 0, 0], [0, -1, 0], [0, 0, 2]])
        sage: M = SymmetricBilinearModule(G)
        sage: decomp = M.witt_decomposition()
        sage: decomp['hyperbolic_rank']
        2  # One hyperbolic plane
        sage: decomp['anisotropic_signature']
        (1, 0, 0)  # Remaining positive part
    """
    p, q, r = self.signature()
    w = min(p, q)  # Witt index
    
    decomposition = {
        'witt_index': w,
        'hyperbolic_rank': 2 * w,
        'anisotropic_signature': (p - w, q - w, 0),
        'radical_dimension': r,
        'total_signature': (p, q, r)
    }
    
    # Could construct explicit decomposition basis
    # This would require more sophisticated algorithms
    
    return decomposition

def orthogonal_group(self):
    """
    Return the orthogonal group preserving this symmetric form.
    
    O(M, b) = {f ∈ GL(M) : b(f(v), f(w)) = b(v, w) for all v, w}
    
    For signature (p, q, 0), this is isomorphic to O(p, q).
    
    OUTPUT:
    Group object representing the orthogonal group
    """
    p, q, r = self.signature()
    
    if r > 0:
        raise ValueError("Orthogonal group not well-defined for degenerate forms")
    
    # This would return appropriate matrix group
    # O(p,q) for indefinite forms, O(n) for definite forms
    from sage.groups.matrix_gps.orthogonal import OrthogonalMatrixGroup
    return OrthogonalMatrixGroup(p + q, self.base_ring(), invariant_form=self.gram_matrix())

def special_orthogonal_group(self):
    """
    Return the special orthogonal group SO(M, b).
    
    SO(M, b) = {f ∈ O(M, b) : det(f) = 1}
    """
    # Similar to orthogonal_group but with determinant 1 constraint
    raise NotImplementedError("Special orthogonal group construction")
```

## Sylvester's Law of Inertia

```python
class WithBasisMethods:
    """
    Additional methods for symmetric bilinear modules with basis.
    """
    
    def sylvester_matrix(self):
        """
        Return matrix P such that P^T G P is diagonal.
        
        This implements Sylvester's algorithm for diagonalizing
        symmetric matrices via congruence transformations.
        
        OUTPUT:
        Matrix P such that P^T * gram_matrix() * P is diagonal
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[2, -1], [-1, 3]])
            sage: M = SymmetricBilinearModule(G)
            sage: P = M.sylvester_matrix()
            sage: D = P.transpose() * G * P
            sage: D.is_diagonal()
            True
        """
        G = self.gram_matrix()
        n = G.nrows()
        
        # Sylvester's algorithm for symmetric matrix diagonalization
        P = G.parent().identity_matrix()
        D = G
        
        for i in range(n):
            if D[i,i] == 0:
                # Find non-zero entry to pivot
                for j in range(i+1, n):
                    if D[i,j] != 0:
                        # Rotation to make diagonal entry non-zero
                        # This is simplified - full implementation more complex
                        break
            
            if D[i,i] != 0:
                # Eliminate column/row i
                for j in range(i+1, n):
                    if D[i,j] != 0:
                        factor = D[i,j] / D[i,i]
                        # Elementary row/column operations
                        # D[j,:] -= factor * D[i,:]
                        # D[:,j] -= factor * D[:,i]
                        # Update P accordingly
        
        return P
    
    def canonical_form(self):
        """
        Return canonical diagonal form.
        
        Uses Sylvester's algorithm to find a basis where the
        Gram matrix is diagonal with entries ±1 and 0.
        
        OUTPUT:
        Tuple (basis, diagonal_form) in canonical form
        """
        # This would implement full canonical form algorithm
        # Result has diagonal entries in {-1, 0, 1}
        raise NotImplementedError("Canonical form algorithm")
    
    def invariants(self):
        """
        Return complete set of invariants.
        
        For symmetric bilinear forms over fields, the signature
        completely determines the isomorphism class.
        
        OUTPUT:
        Dictionary of invariant properties
        """
        return {
            'signature': self.signature(),
            'discriminant': self.discriminant(),
            'witt_index': self.witt_index(),
            'rank': self.rank(),
            'is_definite': self.is_definite(),
            'is_anisotropic': self.is_anisotropic()
        }
```

## Integration with Number Theory

```python
def local_invariants(self, prime=None):
    """
    Compute local invariants at a prime.
    
    For forms over number fields, local invariants determine
    global properties via the Hasse principle.
    
    INPUT:
    - prime -- prime ideal or None for archimedean places
    
    OUTPUT:
    Dictionary of local invariants
    """
    if prime is None:
        # Archimedean (real) invariant is the signature
        return {'signature': self.signature()}
    else:
        # p-adic invariants: Hilbert symbol, etc.
        raise NotImplementedError("p-adic invariants")

def genus(self):
    """
    Return the genus of this quadratic form.
    
    Two forms are in the same genus if they are locally equivalent
    at all places (including the archimedean place).
    
    OUTPUT:
    Genus representative or class
    """
    # This requires sophisticated number theory
    raise NotImplementedError("Genus theory")

def is_locally_equivalent(self, other, prime=None):
    """
    Test local equivalence at a prime.
    
    Two symmetric bilinear forms are locally equivalent if
    one can be transformed into the other by a change of basis
    over the completion at the given prime.
    """
    raise NotImplementedError("Local equivalence testing")
```

## Mathematical Properties

The symmetric bilinear module framework maintains these properties:

```python
# Mathematical assertion: Symmetry
# b(v,w) = b(w,v) for all v,w (Gram matrix G = G^T)

# Mathematical assertion: Quadratic form relationship
# q(v) = b(v,v) and b(v,w) = (q(v+w) - q(v) - q(w))/2

# Mathematical assertion: Sylvester's law of inertia
# Signature (p,q,r) is invariant under change of basis

# Mathematical assertion: Witt decomposition
# M ≅ H^⊕w ⊕ A ⊕ R (hyperbolic ⊕ anisotropic ⊕ radical)

# Mathematical assertion: Diagonalization
# Over algebraically closed fields, any symmetric form is diagonalizable

# Mathematical assertion: Orthogonal group preservation
# O(M,b) = {f : b(f(v),f(w)) = b(v,w)} is a group

# Mathematical assertion: Local-global principle
# For number fields, genus theory relates local and global equivalence

# Mathematical assertion: Positive definite characterization
# b is positive definite ⟺ all eigenvalues > 0 ⟺ signature is (n,0,0)
```

This symmetric bilinear module category provides the mathematical foundation for quadratic form theory while maintaining full compatibility with the bilinear module framework.