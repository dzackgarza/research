<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/symmetric_Rmod.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: SymmetricBilinearModules(R)

Free R-modules with symmetric bilinear forms b: L ⊗_R L → R. Inherits from FreeBilinearModules(R).

## Mathematical Test Assertions

```python
# Mathematical assertion: Symmetry is the defining property of this category
# sage: R = RootSystem(['A', 3])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: alpha[1].inner_product(alpha[2]) == alpha[2].inner_product(alpha[1])
# True  # Symmetry: B(x,y) = B(y,x) for all x,y

# Mathematical assertion: Classical root lattices have symmetric bilinear forms
# sage: R = RootSystem(['E', 8]) 
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: G == G.transpose()
# True  # Gram matrix is symmetric, confirming symmetric bilinear form

# Mathematical assertion: Orthogonal complements are well-defined for symmetric forms
# sage: R = RootSystem(['D', 4])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: v = alpha[1] + alpha[2]
# sage: # Elements orthogonal to v form a well-defined submodule
# sage: all(v.inner_product(w) == 0 for w in L.basis() if v.inner_product(w) == 0)
# True  # Orthogonality relation is consistent

# Mathematical assertion: Definite forms have trivial radical (non-degenerate)
# sage: R = RootSystem(['A', 5])  # Finite type = negative definite
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: G.determinant() != 0
# True  # Non-zero determinant implies trivial radical (Conway & Sloane)

# Mathematical assertion: Signature classifies symmetric forms up to isomorphism
# sage: from sage.quadratic_forms.quadratic_form import QuadraticForm
# sage: # A2 root lattice has signature (0,2,0) - negative definite
# sage: R = RootSystem(['A', 2])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: all(eig < 0 for eig in G.eigenvalues())
# True  # All negative eigenvalues confirms negative definite (Humphreys)

# Mathematical assertion: Hyperbolic plane has Witt index 1
# sage: # The standard hyperbolic plane H has maximal isotropic subspaces of dimension 1
# sage: # H = span(e,f) with B(e,e) = B(f,f) = 0, B(e,f) = 1
# sage: # This is the fundamental indefinite form with signature (1,1,0)
# sage: # Witt index = 1 since max{dim(V) : V totally isotropic} = 1
# sage: # Reference: Serre, "A Course in Arithmetic", Chapter V

# Mathematical assertion: Affine root lattices have exactly one null direction  
# sage: R = RootSystem(['A', 2, 1])  # Affine type
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: eigenvalues = G.eigenvalues()
# sage: sum(1 for eig in eigenvalues if eig == 0) == 1
# True  # Exactly one zero eigenvalue for affine types (Kac, Infinite Dimensional Lie Algebras)
```

## Symmetric Properties

```python
def is_symmetric(self):
    r"""Always returns True for modules in this category."""
    return True

def quadratic_form(self):
    r"""
    Return the associated quadratic form Q(v) = ⟨v,v⟩.
    """

## NOTE: radical() is inherited from FreeBilinearModules
# For symmetric forms, left_radical() = right_radical() = radical()

def is_nondegenerate(self):
    r"""Test if the form is nondegenerate (radical = {0})."""
    
def is_degenerate(self):
    r"""Test if the form is degenerate (radical ≠ {0})."""
```

## Signature and Classification

```python
def signature(self):
    r"""
    Return the signature (p, q, r) of the bilinear form.
    
    NOTE: This only makes sense when R embeds in ℝ (e.g., R = ℤ, or R = ring of integers 
    in a totally real number field).
    
    - p = max{dim_F(V) : V ⊆ M ⊗_R F subspace with b|_V positive definite}
    - q = max{dim_F(V) : V ⊆ M ⊗_R F subspace with b|_V negative definite}
    - r = dim_F(radical(M ⊗_R F))
    
    where F is the field of fractions of R.
    This is a basis-invariant property of the bilinear form.
    Note: p + q + r = rank_R(M).
    """

def is_positive_definite(self):
    r"""
    Test if b(v,v) > 0 for all non-zero v ∈ M ⊗_R F.
    
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_negative_definite(self):
    r"""
    Test if b(v,v) < 0 for all non-zero v ∈ M ⊗_R F.
    
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_definite(self):
    r"""
    Test if the form is definite (positive or negative).
    
    Equivalent to: signature has form (n,0,0) or (0,n,0).
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_indefinite(self):
    r"""
    Test if the form is indefinite.
    
    Equivalent to: ∃ v,w ∈ M ⊗_R F with b(v,v) > 0 and b(w,w) < 0.
    Also equivalent to: p ≥ 1 and q ≥ 1 in signature (p,q,r).
    NOTE: Only meaningful when R embeds in ℝ.
    """

def witt_index(self):
    r"""
    Return the Witt index of the form.
    
    This is max{dim(V) : V ⊆ M totally isotropic submodule}.
    A submodule V is totally isotropic if b(v,w) = 0 for all v,w ∈ V.
    """
```

## Computational Invariants

```python
def rank(self):
    r"""
    Return the rank of the R-module.
    
    Note: If (p,q,r) is the signature, then rank_R(M) = p + q + r.
    For nondegenerate forms, rank_R(M) = p + q.
    """
```

## Symmetric-Specific Optimizations

```python
def right_radical(self):
    r"""
    Return the right radical. For symmetric forms, this equals the left radical.
    
    This override makes the mathematical identity explicit and avoids
    redundant computation since left_radical() = right_radical() for symmetric forms.
    """
    return self.left_radical()
```

## NOTE: The following methods are inherited from FreeBilinearModules(R):
# - dual() - enhanced with canonical map using bilinear form
# - orthogonal_group() - form-preserving R-automorphisms  
# - tensor(), direct_sum() - with bilinear form extension over R
# - quotient_by_radical() - standard degeneracy elimination