<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/indefinite_lattices/indefinite_lattices.md
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
```