<!--
Origin: gitclones/Coxeter/implementation/planning/SymmetricBilRMod/SymmetricBilRMod_objects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects: Symmetric Bilinear Module Parent Implementation

Parent class implementation for symmetric bilinear modules with quadratic form evaluation and diagonalization.

## Parent Class Structure

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.parent import Parent

class SymmetricBilinearModule_with_basis(BilinearModule_with_basis):
    """
    Concrete parent class for symmetric bilinear modules with basis.
    
    A symmetric bilinear module consists of:
    - An R-module M with basis
    - A symmetric bilinear form b: M × M → R with b(v,w) = b(w,v)
    - Associated quadratic form q(v) = b(v,v)
    - Gram matrix G satisfying G = G^T
    
    This extends BilinearModule_with_basis by enforcing symmetry
    and adding quadratic form functionality.
    
    EXAMPLES::
    
        sage: # Positive definite form
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: M.is_symmetric()
        True
        sage: M.discriminant()
        5
        sage: M.is_positive_definite()
        True
        
        sage: # Indefinite form (Lorentzian signature)
        sage: L = matrix(QQ, [[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        sage: N = SymmetricBilinearModule(L)
        sage: N.signature()
        (2, 1, 0)
        sage: N.is_indefinite()
        True
    """
    
    def __init__(self, gram_matrix, basis=None, category=None, **kwds):
        """
        Initialize a symmetric bilinear module.
        
        INPUT:
        - gram_matrix -- symmetric matrix defining the bilinear form
        - basis -- optional basis names (defaults to indexed names)
        - category -- optional category (defaults to SymmetricBilinearModules)
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[1, 0.5], [0.5, 2]])
            sage: M = SymmetricBilinearModule(G)
            sage: M.base_ring()
            Rational Field
            sage: M.rank()
            2
            sage: M.is_symmetric()
            True
        """
        # Validate symmetry
        if not gram_matrix.is_square():
            raise ValueError("Gram matrix must be square")
        
        if gram_matrix != gram_matrix.transpose():
            raise ValueError("Gram matrix must be symmetric for symmetric bilinear modules")
        
        # Set up category
        if category is None:
            from sage.categories.symmetric_bilinear_modules import SymmetricBilinearModules
            category = SymmetricBilinearModules(gram_matrix.base_ring()).WithBasis()
        
        # Initialize parent bilinear module
        super().__init__(gram_matrix, basis=basis, category=category, **kwds)
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: SymmetricBilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            Symmetric bilinear module of rank 2 over Integer Ring
        """
        return f"Symmetric bilinear module of rank {self.rank()} over {self.base_ring()}"
    
    def is_symmetric(self):
        """Always True for symmetric bilinear modules."""
        return True
    
    def quadratic_form(self, v):
        """
        Evaluate the associated quadratic form: q(v) = b(v,v).
        
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
            15
            sage: M.bilinear_form(v, v)  # Same result
            15
        """
        return self.bilinear_form(v, v)
    
    def quadratic_form_matrix(self):
        """
        Return the quadratic form matrix (same as Gram matrix).
        
        For symmetric bilinear forms, the quadratic form matrix Q
        equals the Gram matrix G.
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[3, -1], [-1, 2]])
            sage: M = SymmetricBilinearModule(G)
            sage: Q = M.quadratic_form_matrix()
            sage: Q == M.gram_matrix()
            True
        """
        return self.gram_matrix()
```

## Signature and Invariants

```python
def signature(self):
    """
    Return the signature (p, q, r) of the symmetric form.
    
    Where p = # positive eigenvalues, q = # negative eigenvalues,
    r = # zero eigenvalues. This is invariant under change of basis
    (Sylvester's law of inertia).
    
    OUTPUT:
    Triple (p, q, r) of non-negative integers with p + q + r = rank
    
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
    
    # Count signs of eigenvalues
    pos = sum(1 for ev in eigenvals if ev > 0)
    neg = sum(1 for ev in eigenvals if ev < 0)
    zero = sum(1 for ev in eigenvals if ev == 0)
    
    return (pos, neg, zero)

def witt_index(self):
    """
    Return the Witt index (dimension of maximal isotropic subspace).
    
    For signature (p, q, r), the Witt index is min(p, q).
    This measures the "amount of indefiniteness" of the form.
    
    OUTPUT:
    Non-negative integer
    
    EXAMPLES::
    
        sage: # Hyperbolic plane has Witt index 1
        sage: H = matrix(QQ, [[0, 1], [1, 0]])
        sage: M = SymmetricBilinearModule(H)
        sage: M.witt_index()
        1
        
        sage: # Positive definite has Witt index 0
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: N = SymmetricBilinearModule(G)
        sage: N.witt_index()
        0
        
        sage: # General indefinite form
        sage: L = matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, -1]])
        sage: P = SymmetricBilinearModule(L)
        sage: P.witt_index()
        1  # min(2, 1)
    """
    p, q, r = self.signature()
    return min(p, q)

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
    """Test if form is indefinite (both positive and negative eigenvalues)."""
    p, q, r = self.signature()
    return p > 0 and q > 0

def is_anisotropic(self):
    """
    Test if form is anisotropic (no non-zero isotropic vectors).
    
    Equivalent to Witt index = 0 and non-degenerate.
    
    EXAMPLES::
    
        sage: # Positive definite is anisotropic
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: M.is_anisotropic()
        True
        
        sage: # Hyperbolic plane is isotropic
        sage: H = matrix(QQ, [[0, 1], [1, 0]])
        sage: L = SymmetricBilinearModule(H)
        sage: L.is_anisotropic()
        False
    """
    return self.witt_index() == 0 and not self.is_degenerate()
```

## Diagonalization and Spectral Theory

```python
def diagonalize(self):
    """
    Diagonalize the symmetric bilinear form.
    
    Returns orthogonal basis where Gram matrix is diagonal.
    Uses spectral decomposition of symmetric matrices.
    
    OUTPUT:
    Tuple (orthogonal_basis, eigenvalues) where:
    - orthogonal_basis: list of mutually orthogonal elements
    - eigenvalues: corresponding eigenvalues
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[5, 3], [3, 5]])
        sage: M = SymmetricBilinearModule(G)
        sage: basis, eigenvals = M.diagonalize()
        sage: len(basis)
        2
        sage: eigenvals
        [8, 2]  # 5 ± 3
        
        sage: # Verify orthogonality
        sage: M.bilinear_form(basis[0], basis[1])
        0
    """
    G = self.gram_matrix()
    
    # Compute eigendecomposition
    eigenvals, eigenvecs = G.eigenmatrix_right()
    
    # Convert eigenvectors to module elements
    orthogonal_basis = []
    diagonal_values = []
    
    for i in range(eigenvecs.ncols()):
        eigenvec = eigenvecs.column(i)
        eigenval = eigenvals[i,i]
        
        # Convert to module element
        element = self._from_vector(eigenvec)
        orthogonal_basis.append(element)
        diagonal_values.append(eigenval)
    
    return orthogonal_basis, diagonal_values

def orthogonal_basis(self):
    """
    Return orthogonal basis via Gram-Schmidt process.
    
    Uses the bilinear form to orthogonalize the standard basis.
    
    OUTPUT:
    List of mutually orthogonal elements
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[2, 1], [1, 2]])
        sage: M = SymmetricBilinearModule(G)
        sage: ortho_basis = M.orthogonal_basis()
        sage: len(ortho_basis)
        2
        sage: M.bilinear_form(ortho_basis[0], ortho_basis[1])
        0
    """
    basis = list(self.gens())
    orthogonal = []
    
    for v in basis:
        # Subtract projections onto previous orthogonal vectors
        orthogonal_v = v
        for u in orthogonal:
            u_norm_sq = self.bilinear_form(u, u)
            if u_norm_sq != 0:
                proj_coeff = self.bilinear_form(v, u) / u_norm_sq
                orthogonal_v = orthogonal_v - proj_coeff * u
        
        if not orthogonal_v.is_zero():
            orthogonal.append(orthogonal_v)
    
    return orthogonal

def orthonormal_basis(self):
    """
    Return orthonormal basis (only for positive definite forms).
    
    Each basis vector has norm 1 and is orthogonal to others.
    
    OUTPUT:
    List of orthonormal elements
    
    EXAMPLES::
    
        sage: # Standard inner product
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: ortho_basis = M.orthonormal_basis()
        sage: all(M.quadratic_form(v) == 1 for v in ortho_basis)
        True
    """
    if not self.is_positive_definite():
        raise ValueError("Orthonormal basis only defined for positive definite forms")
    
    orthogonal = self.orthogonal_basis()
    orthonormal = []
    
    for v in orthogonal:
        norm_sq = self.quadratic_form(v)
        if norm_sq > 0:
            from sage.functions.other import sqrt
            norm = sqrt(norm_sq)
            unit_vector = v / norm
            orthonormal.append(unit_vector)
    
    return orthonormal

def canonical_form(self):
    """
    Return canonical diagonal form with entries ±1, 0.
    
    Uses Sylvester's algorithm to find basis where Gram matrix
    has diagonal entries in {-1, 0, 1}.
    
    OUTPUT:
    Tuple (canonical_basis, canonical_diagonal) where diagonal
    entries are normalized to ±1 or 0
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[4, 0], [0, -9]])
        sage: M = SymmetricBilinearModule(G)
        sage: basis, diagonal = M.canonical_form()
        sage: diagonal
        [1, -1]  # Normalized from [4, -9]
    """
    orthogonal_basis, eigenvals = self.diagonalize()
    
    # Normalize to canonical form
    canonical_basis = []
    canonical_diagonal = []
    
    for i, (v, eigenval) in enumerate(zip(orthogonal_basis, eigenvals)):
        if eigenval > 0:
            # Normalize to 1
            from sage.functions.other import sqrt
            norm_factor = sqrt(eigenval)
            canonical_v = v / norm_factor
            canonical_basis.append(canonical_v)
            canonical_diagonal.append(1)
        elif eigenval < 0:
            # Normalize to -1
            from sage.functions.other import sqrt
            norm_factor = sqrt(-eigenval)
            canonical_v = v / norm_factor
            canonical_basis.append(canonical_v)
            canonical_diagonal.append(-1)
        else:
            # Keep zero eigenvalue
            canonical_basis.append(v)
            canonical_diagonal.append(0)
    
    return canonical_basis, canonical_diagonal
```

## Witt Theory and Decomposition

```python
def witt_decomposition(self):
    """
    Witt decomposition of the symmetric bilinear form.
    
    Every symmetric bilinear form decomposes as:
    M ≅ H^⊕w ⊕ A ⊕ R
    where:
    - H is hyperbolic plane (signature (1,1,0))
    - w is Witt index
    - A is anisotropic part (Witt index 0)
    - R is radical (degenerate part)
    
    OUTPUT:
    Dictionary describing the decomposition
    
    EXAMPLES::
    
        sage: # Mixed signature form
        sage: G = matrix(QQ, [[1, 0, 0, 0], [0, 1, 0, 0], 
        ....:                 [0, 0, -1, 0], [0, 0, 0, -1]])
        sage: M = SymmetricBilinearModule(G)
        sage: decomp = M.witt_decomposition()
        sage: decomp['witt_index']
        2
        sage: decomp['hyperbolic_dimension']
        4  # Two hyperbolic planes
        sage: decomp['anisotropic_signature']
        (0, 0, 0)  # No anisotropic part
    """
    p, q, r = self.signature()
    w = min(p, q)  # Witt index
    
    # Anisotropic part has signature (p-w, q-w, r)
    anisotropic_p = p - w
    anisotropic_q = q - w
    
    decomposition = {
        'signature': (p, q, r),
        'witt_index': w,
        'hyperbolic_dimension': 2 * w,
        'anisotropic_signature': (anisotropic_p, anisotropic_q, 0),
        'radical_dimension': r,
        'is_anisotropic': (w == 0 and r == 0),
        'is_isotropic': (w > 0 or r > 0)
    }
    
    return decomposition

def maximal_isotropic_subspace(self):
    """
    Find a maximal isotropic subspace.
    
    An isotropic subspace V satisfies b(v,w) = 0 for all v,w ∈ V.
    Maximal means it cannot be extended while preserving isotropy.
    
    OUTPUT:
    Submodule representing maximal isotropic subspace
    
    EXAMPLES::
    
        sage: # Hyperbolic plane
        sage: H = matrix(QQ, [[0, 1], [1, 0]])
        sage: M = SymmetricBilinearModule(H)
        sage: iso = M.maximal_isotropic_subspace()
        sage: iso.dimension()
        1  # One-dimensional isotropic subspace
    """
    w = self.witt_index()
    if w == 0:
        # No non-trivial isotropic vectors
        return self.submodule([])
    
    # Find isotropic vectors via diagonalization
    # This is a simplified approach - full algorithm more complex
    basis, eigenvals = self.diagonalize()
    
    isotropic_generators = []
    
    # Look for pairs of opposite eigenvalues to form isotropic combinations
    positive_indices = [i for i, ev in enumerate(eigenvals) if ev > 0]
    negative_indices = [i for i, ev in enumerate(eigenvals) if ev < 0]
    
    for i, pos_idx in enumerate(positive_indices[:w]):
        if i < len(negative_indices):
            neg_idx = negative_indices[i]
            
            # Form isotropic vector: α*e_pos + β*e_neg where α²*λ_pos + β²*λ_neg = 0
            pos_eigenval = eigenvals[pos_idx]
            neg_eigenval = eigenvals[neg_idx]
            
            # Choose α = 1, β = √(λ_pos / |λ_neg|)
            from sage.functions.other import sqrt
            beta = sqrt(pos_eigenval / (-neg_eigenval))
            isotropic_vector = basis[pos_idx] + beta * basis[neg_idx]
            isotropic_generators.append(isotropic_vector)
    
    return self.submodule(isotropic_generators)
```

## Orthogonal Group and Automorphisms

```python
def orthogonal_group(self):
    """
    Return the orthogonal group preserving this form.
    
    O(M, b) = {f ∈ GL(M) : b(f(v), f(w)) = b(v, w) for all v, w}
    
    For signature (p, q, 0), isomorphic to O(p, q).
    
    OUTPUT:
    Matrix group preserving the bilinear form
    
    EXAMPLES::
    
        sage: # Standard Euclidean form
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: O = M.orthogonal_group()
        sage: O
        Orthogonal Group of degree 2 over Rational Field
    """
    p, q, r = self.signature()
    
    if r > 0:
        raise ValueError("Orthogonal group not well-defined for degenerate forms")
    
    from sage.groups.matrix_gps.orthogonal import OrthogonalMatrixGroup
    return OrthogonalMatrixGroup(
        self.rank(), 
        self.base_ring(), 
        invariant_bilinear_form=self.gram_matrix()
    )

def special_orthogonal_group(self):
    """
    Return the special orthogonal group SO(M, b).
    
    SO(M, b) = {f ∈ O(M, b) : det(f) = 1}
    
    OUTPUT:
    Special orthogonal matrix group
    """
    from sage.groups.matrix_gps.orthogonal import SO
    return SO(self.rank(), self.base_ring(), invariant_form=self.gram_matrix())

def reflection_group(self):
    """
    Return the group generated by reflections.
    
    Every orthogonal transformation is a product of reflections
    in hyperplanes (Cartan-Dieudonné theorem).
    
    OUTPUT:
    Group generated by hyperplane reflections
    """
    # This would construct explicit reflection generators
    raise NotImplementedError("Reflection group construction")
```

## Integration with Lattice Theory

```python
def is_integral(self):
    """
    Test if this is an integral quadratic form.
    
    A form is integral if b(v,w) ∈ Z for all v,w in some Z-basis.
    Equivalently, the Gram matrix has integer entries.
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: # Integral form
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: M.is_integral()
        True
        
        sage: # Non-integral form
        sage: H = matrix(QQ, [[1, 1/2], [1/2, 1]])
        sage: N = SymmetricBilinearModule(H)
        sage: N.is_integral()
        False
    """
    G = self.gram_matrix()
    return G.base_ring() == ZZ and all(g in ZZ for g in G.list())

def is_even(self):
    """
    Test if this is an even quadratic form.
    
    A form is even if q(v) ∈ 2Z for all v (diagonal entries are even).
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: # Even form
        sage: G = matrix(ZZ, [[2, 1], [1, 2]])
        sage: M = SymmetricBilinearModule(G)
        sage: M.is_even()
        True
        
        sage: # Odd form  
        sage: H = matrix(ZZ, [[1, 0], [0, 1]])
        sage: N = SymmetricBilinearModule(H)
        sage: N.is_even()
        False
    """
    if not self.is_integral():
        return False
    
    G = self.gram_matrix()
    return all(G[i,i] % 2 == 0 for i in range(G.nrows()))

def dual_lattice(self):
    """
    Return the dual lattice L* = {v ∈ V : b(v, L) ⊆ Z}.
    
    For integral forms, this gives the lattice of vectors with
    integer inner products with the original lattice.
    
    OUTPUT:
    SymmetricBilinearModule representing the dual lattice
    """
    if not self.is_integral():
        raise ValueError("Dual lattice only defined for integral forms")
    
    # Dual lattice has Gram matrix G^(-1)
    G = self.gram_matrix()
    if G.determinant() == 0:
        raise ValueError("Cannot compute dual of degenerate lattice")
    
    dual_gram = G.inverse()
    return SymmetricBilinearModule(dual_gram)

def theta_series(self, precision=10):
    """
    Compute theta series of the quadratic form.
    
    θ(q) = Σ_{v ∈ L} q^{Q(v)} where Q is the quadratic form.
    
    INPUT:
    - precision -- number of terms to compute
    
    OUTPUT:
    Power series representing the theta function
    """
    # This requires implementation of theta function algorithms
    raise NotImplementedError("Theta series computation")
```

## Mathematical Properties

The symmetric bilinear module implementation maintains these properties:

```python
# Mathematical assertion: Symmetry
# G = G^T where G is the Gram matrix

# Mathematical assertion: Quadratic form relationship  
# q(v) = b(v,v) and b(v,w) = (q(v+w) - q(v) - q(w))/2

# Mathematical assertion: Sylvester's law of inertia
# Signature (p,q,r) is invariant under orthogonal change of basis

# Mathematical assertion: Spectral theorem
# Symmetric matrices are diagonalizable with real eigenvalues

# Mathematical assertion: Witt decomposition
# M ≅ H^⊕w ⊕ A ⊕ R (hyperbolic ⊕ anisotropic ⊕ radical)

# Mathematical assertion: Isotropic subspace bound
# Dimension of isotropic subspace ≤ Witt index = min(p,q)

# Mathematical assertion: Orthogonal group properties
# O(p,q) preserves signature and is a Lie group

# Mathematical assertion: Definite form characterization
# Positive definite ⟺ all eigenvalues > 0 ⟺ signature (n,0,0)
```

This symmetric bilinear module parent class provides the computational foundation for quadratic form theory while maintaining full mathematical rigor and integration with the broader category framework.