<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/degenerate_lattices/degenerate_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: DegenerateLattices(R)

Degenerate lattices (with nontrivial radical) have a specialized interface.

**IMPORTANT**: DegenerateLattices inherit ALL methods from:
- FreeModules(R): rank(), basis(), generators(), dual(), tensor(), direct_sum()
- FreeBilinearModules(R): bilinear_form(), gram_matrix(), discriminant(), dual(), left_dual(), right_dual(), orthogonal_group(), left_radical(), right_radical(), radical(), nondegenerate_quotient()
- SymmetricBilinearModules(R): signature(), is_definite(), optimized right_radical(), etc.

The methods below are ADDITIONAL to those inherited methods.

**NOTE**: By definition, objects in DegenerateLattices have rad(L) ≠ {0},
so discriminant() always returns 0, and the signature has r > 0.

## Radical-Specific Methods

```python
def radical_rank(self):
    r"""
    Return the rank of the radical.
    
    This is the r component of signature (p,q,r).
    """

## NOTE: quotient_by_radical() is inherited from SymmetricBilinearModules(R)
# The specific implementation for DegenerateLattices returns (Q, π) tuple
# where Q is nondegenerate and π is the quotient map

def radical_complement(self):
    r"""
    Return a complement to the radical (not unique).
    
    This is a sublattice M such that L = M ⊕ rad(L) as R-modules
    (but not necessarily as an orthogonal direct sum).
    """
```

## Orthogonal Decomposition

```python
def orthogonal_to_radical(self):
    r"""
    Return rad(L)^⊥, the orthogonal complement of the radical.
    
    Note: For degenerate forms, rad(L) ⊆ rad(L)^⊥, so this
    contains the radical as a sublattice.
    """

def is_split_degenerate(self):
    r"""
    Test if L = M ⊕ rad(L) as an orthogonal direct sum.
    
    True if there exists a nondegenerate sublattice M such that
    L = M ⊕ rad(L) and M ⊥ rad(L).
    """
```

## Classification

```python
def is_parabolic(self):
    r"""
    Test if this is a parabolic lattice.
    
    True if radical has rank 1 and the form on rad(L)^⊥/rad(L)
    is negative definite.
    """

def signature_on_quotient(self):
    r"""
    Return the signature of the induced form on L/rad(L).
    
    This determines the type of degeneracy.
    """
```

## Degenerate-Specific Invariants

```python
def discriminant_group(self):
    r"""
    For degenerate lattices, L*/L is not a finite group.
    
    Raises NotImplementedError. Use quotient_by_radical() and
    compute the discriminant group of the nondegenerate quotient.
    """
    raise NotImplementedError("Discriminant group is infinite for degenerate lattices")
```

## NOTE: dual() and orthogonal_group() are inherited from SymmetricBilinearModules(R)
# For degenerate lattices:
# - dual() returns (L*, ι) where ker(ι) = rad(L)
# - orthogonal_group() preserves the radical

## Degenerate-Specific Group Actions

```python
def stabilizer_of_radical(self):
    r"""
    Return the subgroup of O(L) that fixes rad(L) pointwise.
    
    This is often the relevant group for degenerate lattices,
    as it acts faithfully on the nondegenerate quotient L/rad(L).
    """
```

## Mathematical Test Assertions

```python
# Mathematical assertion: Affine root lattices are degenerate with null root in radical
# Reference: Kac "Infinite Dimensional Lie Algebras" Chapter 6
# sage: R = RootSystem(['A', 2, 1])  # Affine A2
# sage: L = R.root_lattice()
# sage: delta = L.null_root()  # The null root
# sage: G = L.bilinear_form()
# sage: G(delta, delta)
# 0  # Null root has zero norm (degenerate direction)

# Mathematical assertion: Null root spans the radical in affine types
# Reference: Bourbaki "Lie Groups and Lie Algebras" Ch 4-6
# sage: simple_roots = L.simple_roots()
# sage: all(G(delta, alpha) == 0 for alpha in simple_roots)
# True  # Delta orthogonal to all simple roots

# Mathematical assertion: Extended weight lattice quotient by radical is nondegenerate
# Reference: Kumar "Kac-Moody Groups" Section 1.3
# sage: W = R.weight_lattice(extended=True)
# sage: delta_w = W.null_root()
# sage: span_delta = W.submodule([delta_w])
# sage: quotient_rank = W.rank() - span_delta.rank()
# sage: quotient_rank
# 3  # A2 affine: 4D extended lattice minus 1D radical = 3D nondegenerate

# Mathematical assertion: Parabolic lattices have exactly one zero eigenvalue
# Reference: Conway & Sloane "Sphere Packings" Chapter 4
# sage: from sage.quadratic_forms.quadratic_form import QuadraticForm
# sage: # Example: Degenerate form from affine A1 (rank 1 radical)
# sage: matrix_A1_affine = matrix(QQ, [[2, -2], [-2, 2]])
# sage: Q = QuadraticForm(matrix_A1_affine)
# sage: eigenvals = matrix_A1_affine.eigenvalues()
# sage: sum(1 for ev in eigenvals if ev == 0)
# 1  # Exactly one zero eigenvalue (parabolic type)

# Mathematical assertion: Radical vectors are isotropic for symmetric forms
# Reference: Serre "A Course in Arithmetic" Chapter VII
# sage: # Using degenerate quadratic form example
# sage: isotropic_vector = vector(QQ, [1, 1])  # In radical of A1 affine
# sage: Q(isotropic_vector)
# 0  # Vector in radical has zero quadratic form value

# Mathematical assertion: Determinant zero for all degenerate lattices
# Reference: Milnor & Husemoller "Symmetric Bilinear Forms" Chapter I
# sage: matrix_A1_affine.determinant()
# 0  # Singular matrix (degenerate bilinear form)

# Mathematical assertion: Orthogonal complement contains radical for degenerate forms
# Reference: Jacobson "Basic Algebra II" Chapter 6
# sage: # For symmetric degenerate form, radical ⊆ radical^⊥
# sage: rad_vector = vector(QQ, [1, 1])
# sage: all(matrix_A1_affine * rad_vector == 0)
# True  # Radical vector orthogonal to all vectors (including itself)

# Mathematical assertion: Signature has positive zero-eigenvalue count for degenerate forms
# Reference: Sylvester's Law of Inertia
# sage: pos_eigs = sum(1 for ev in eigenvals if ev > 0)
# sage: neg_eigs = sum(1 for ev in eigenvals if ev < 0)  
# sage: zero_eigs = sum(1 for ev in eigenvals if ev == 0)
# sage: (pos_eigs, neg_eigs, zero_eigs)
# (0, 1, 1)  # Signature (0,1,1) for A1 affine type
```