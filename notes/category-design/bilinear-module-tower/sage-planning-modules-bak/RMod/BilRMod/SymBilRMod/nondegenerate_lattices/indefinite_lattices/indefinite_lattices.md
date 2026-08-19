<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/nondegenerate_lattices/indefinite_lattices/indefinite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: IndefiniteLattices

Indefinite lattices inherit all methods from `Lattices` and add:

## Cone Structure

```python
def positive_cone(self):
    r"""
    Return the positive cone {v ∈ L ⊗ R : ⟨v,v⟩ > 0}.
    
    This is an open convex cone in the ambient space.
    """

def negative_cone(self):
    r"""
    Return the negative cone {v ∈ L ⊗ R : ⟨v,v⟩ < 0}.
    
    This is an open convex cone in the ambient space.
    """

def light_cone(self):
    r"""
    Return the light cone (isotropic boundary) {v ∈ L ⊗ R : ⟨v,v⟩ = 0}.
    
    This is the boundary between positive and negative cones.
    """

def future_cone(self):
    r"""
    Return the future cone (closure of positive cone).
    
    This is {v ∈ L ⊗ R : ⟨v,v⟩ ≥ 0}.
    """

def past_cone(self):
    r"""
    Return the past cone (closure of negative cone).
    
    This is {v ∈ L ⊗ R : ⟨v,v⟩ ≤ 0}.
    """
```

## Isotropic Vectors

```python
def isotropic_vectors(self):
    r"""
    Return primitive isotropic vectors (those with ⟨v,v⟩ = 0).
    
    For indefinite lattices, these form the "light rays" on the light cone.
    """

def primitive_isotropic_vectors(self):
    r"""
    Return primitive isotropic vectors up to sign.
    
    These are the primitive lattice points on the light cone.
    """

def has_isotropic_vector(self):
    r"""
    Test if the lattice contains a nonzero isotropic vector.
    
    This is equivalent to the quadratic form representing zero.
    """
```

## Signature Decomposition

```python
def positive_subspace(self):
    r"""
    Return a maximal positive definite subspace.
    
    This is a subspace on which the form is positive definite,
    of dimension equal to the positive index.
    """

def negative_subspace(self):
    r"""
    Return a maximal negative definite subspace.
    
    This is a subspace on which the form is negative definite,
    of dimension equal to the negative index.
    """

def witt_decomposition(self):
    r"""
    Return a Witt decomposition of the lattice.
    
    Decomposes as L = H^k ⊕ L_0 where H is hyperbolic plane
    and L_0 is anisotropic (contains no isotropic vectors).
    """
```

## Lorentzian Geometry

```python
def lorentzian_inner_product(self, v, w):
    r"""
    Compute the Lorentzian inner product of two vectors.
    
    This is just the bilinear form, but emphasizes the geometric interpretation.
    """
    return v * w

def timelike_vectors(self, bound=None):
    r"""
    Return timelike vectors (those with ⟨v,v⟩ > 0).
    
    INPUT:
    - bound: Optional bound on the norm
    
    OUTPUT:
    List or iterator of timelike vectors
    """

def spacelike_vectors(self, bound=None):
    r"""
    Return spacelike vectors (those with ⟨v,v⟩ < 0).
    
    INPUT:
    - bound: Optional bound on |⟨v,v⟩|
    
    OUTPUT:
    List or iterator of spacelike vectors
    """

def lightlike_vectors(self):
    r"""
    Return lightlike (null) vectors (those with ⟨v,v⟩ = 0).
    
    These are the isotropic vectors.
    """
    return self.isotropic_vectors()
```

## Special Methods

```python
def vinberg_algorithm_applicable(self):
    r"""
    Test if Vinberg's algorithm can be applied to this lattice.
    
    Returns False for general indefinite lattices.
    Overridden in HyperbolicLattices to potentially return True.
    """
    return False

def reflection_vectors(self, norm_bound=None):
    r"""
    Return vectors of bounded norm that could define reflections.
    
    For indefinite lattices, we consider vectors v with ⟨v,v⟩ ≠ 0
    that could define reflections in the orthogonal group.
    
    INPUT:
    - norm_bound: Bound on |⟨v,v⟩|
    
    OUTPUT:
    List of potential reflection vectors
    """

## Mathematical Test Assertions

```python
# Mathematical assertion: Indefinite lattices have mixed eigenvalue signs
# sage: from sage.quadratic_forms.quadratic_form import QuadraticForm
# sage: G = matrix(ZZ, [[2, -1, 0], [-1, 2, -1], [0, -1, -2]])
# sage: eigs = G.change_ring(AA).eigenvalues()
# sage: pos = len([e for e in eigs if e > 0]); neg = len([e for e in eigs if e < 0])
# sage: pos > 0 and neg > 0  # Mixed signs define indefinite
# True  # Signature (2,1,0) - indefinite by definition

# Mathematical assertion: Light cone contains isotropic vectors
# sage: H = matrix(ZZ, [[1, 0], [0, -1]])  # Standard Lorentzian Z^{1,1}
# sage: v = vector([3, 3])  # Light-like vector
# sage: v * H * v  # Isotropic vectors have zero norm
# 0  # Light cone defined by {v : <v,v> = 0}

# Mathematical assertion: Hyperbolic plane has signature (1,1,0)
# sage: H = matrix(ZZ, [[0, 1], [1, 0]])  # Standard hyperbolic plane
# sage: sorted(H.eigenvalues())
# [-1, 1]  # One positive, one negative eigenvalue (Vinberg)

# Mathematical assertion: Indefinite lattices contain timelike and spacelike vectors
# sage: G = matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, -2]])  # Signature (2,1,0)
# sage: timelike = vector([1, 0, 0]); spacelike = vector([0, 0, 1])
# sage: timelike * G * timelike > 0 and spacelike * G * spacelike < 0
# True  # Indefinite lattices have vectors of both positive and negative norm

# Mathematical assertion: Witt decomposition for indefinite lattices
# sage: H = matrix(ZZ, [[0, 1], [1, 0]])  # Hyperbolic plane
# sage: L = matrix.block_diagonal([H, matrix([[-2]])])  # H ⊕ <-2>
# sage: sorted(L.eigenvalues())
# [-2, -1, 1]  # Decomposable indefinite lattice (Conway & Sloane)

# Mathematical assertion: Indefinite lattices can have infinite automorphism groups
# sage: import sage.groups.matrix_gps.orthogonal as orth
# sage: G = matrix(QQ, [[1, 0], [0, -1]])  # Lorentzian plane
# sage: # The orthogonal group O(1,1) contains hyperbolic rotations
# sage: # parametrized by cosh(t), sinh(t) - infinite continuous group
# sage: # Unlike definite lattices which have finite automorphism groups

# Mathematical assertion: Meyer's theorem for indefinite lattices
# sage: # By Meyer's theorem: indefinite lattices of rank ≥ 5 
# sage: # represent all integers (universal quadratic forms)
# sage: # This is a fundamental difference from definite lattices
# sage: # Reference: Meyer, "Über die Auflösung der Gleichung ax² + by² + cz² + du² + ev² = f"

# Mathematical assertion: Project convention for indefinite Coxeter groups
# sage: # Our Gram matrix formula: B_ij = 2 * cos(π/M_ij)
# sage: # For indefinite Coxeter groups, the Gram matrix has mixed eigenvalues
# sage: # Example: A Coxeter matrix with both finite and infinite entries
# sage: M = matrix([[1, 3, 2], [3, 1, infinity], [2, infinity, 1]])  # conceptual
# sage: # Would give Gram matrix with cos(π/∞) = -1 entries
# sage: # Leading to indefinite signature (has both positive and negative eigenvalues)
```
```