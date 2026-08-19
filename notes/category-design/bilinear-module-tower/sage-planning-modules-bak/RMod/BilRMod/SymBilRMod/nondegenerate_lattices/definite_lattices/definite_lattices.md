<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/nondegenerate_lattices/definite_lattices/definite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: DefiniteLattices

Definite lattices inherit all methods from `Lattices` and add:

**INHERITANCE**: DefiniteLattices inherit is_definite() from SymmetricBilinearModules,
which returns True for all objects in this category.

## Mathematical Test Assertions

```python
# Mathematical assertion: All eigenvalues have same sign for definite lattices
# sage: R = RootSystem(['E', 6])
# sage: C = R.cartan_matrix()
# sage: G = -C  # Gram matrix for simply-laced types
# sage: eigs = G.eigenvalues()
# sage: all(e < 0 for e in eigs) or all(e > 0 for e in eigs)
# True  # E6 is negative definite under our convention (Humphreys, Reflection Groups)

# Mathematical assertion: No isotropic vectors except zero in definite lattices
# sage: R = RootSystem(['D', 8])
# sage: L = R.root_lattice()
# sage: # For definite lattices, if ⟨v,v⟩ = 0 then v = 0
# sage: # This is equivalent to having no zero eigenvalues
# sage: G = -R.cartan_matrix()
# sage: 0 not in G.eigenvalues()
# True  # No null vectors in definite lattices (Conway & Sloane, Ch. 1)

# Mathematical assertion: Finite automorphism groups for definite lattices
# sage: R = RootSystem(['E', 8])
# sage: W = R.root_system().weyl_group()
# sage: W.order() < infinity
# True  # E8 has finite Weyl group |W(E8)| = 696,729,600 (Conway & Sloane, Ch. 4)

# Mathematical assertion: Minimal vectors exist in definite lattices
# sage: R = RootSystem(['A', 5])
# sage: L = R.root_lattice()
# sage: roots = L.roots()
# sage: len(roots) > 0 and len(roots) < infinity
# True  # A5 has exactly 30 roots, all of minimal length (Bourbaki, Ch. VI)

# Mathematical assertion: Our convention - finite types have negative definite Gram matrices
# sage: for typ in [['A', 3], ['D', 5], ['E', 7]]:
# ...     R = RootSystem(typ)
# ...     G = -R.cartan_matrix()
# ...     if not all(e < 0 for e in G.eigenvalues()):
# ...         print(f"Failed for {typ}")
# # (No output - all finite types are negative definite under our convention)

# Mathematical assertion: Positive definite lattices have "opposite" Gram matrices
# sage: R = RootSystem(['F', 4])
# sage: G_neg = -R.cartan_matrix()  # Our convention: negative definite
# sage: G_pos = -G_neg  # Standard positive definite convention
# sage: all(e > 0 for e in G_pos.eigenvalues())
# True  # Negating our Gram matrix gives positive definite form

# Mathematical assertion: Unimodular definite lattices have determinant ±1
# sage: R = RootSystem(['E', 8])
# sage: G = -R.cartan_matrix()
# sage: abs(G.determinant()) == 1
# True  # E8 is the unique even unimodular lattice in dimension 8 (Milnor & Husemoller)

# Mathematical assertion: Definite lattices have well-ordered successive minima
# sage: R = RootSystem(['D', 4])
# sage: L = R.root_lattice()
# sage: # For definite lattices, successive minima satisfy λ₁ ≤ λ₂ ≤ ... ≤ λₙ
# sage: # This follows from the geometry of ellipsoids in Euclidean space
# sage: G = -R.cartan_matrix()
# sage: G.is_negative_definite()  # Uses Sylvester's criterion
# True  # Successive minima exist and are well-ordered (Cassels, Geometry of Numbers)
```

## Definite-Specific Properties

def shortest_vectors(self):
    r"""
    Return the shortest nonzero vectors in the lattice.
    
    For definite lattices, there is a finite set of vectors achieving
    the minimum nonzero norm.
    
    OUTPUT:
    List of vectors v with minimal |⟨v,v⟩| > 0
    """

def minimal_norm(self):
    r"""
    Return the minimal nonzero norm in the lattice.
    
    OUTPUT:
    The minimum value of |⟨v,v⟩| for nonzero v ∈ L
    """

def covering_radius(self):
    r"""
    Return the covering radius of the lattice.
    
    This is the maximum distance from any point in the ambient space
    to the nearest lattice point.
    """

def packing_radius(self):
    r"""
    Return the packing radius of the lattice.
    
    This is half the minimal distance between distinct lattice points.
    """

def theta_series(self, prec):
    r"""
    Return the theta series of the lattice.
    
    For a definite lattice, this is the generating function:
    θ_L(q) = Σ_{v∈L} q^{⟨v,v⟩}
    
    INPUT:
    - prec: Precision (number of terms)
    
    OUTPUT:
    Power series in q
    """

def kissing_number(self):
    r"""
    Return the kissing number (coordination number) of the lattice.
    
    This is the number of minimal nonzero vectors.
    """

def successive_minima(self, n=None):
    r"""
    Return the successive minima of the lattice.
    
    The i-th successive minimum λ_i is the smallest radius such that
    the ball of radius λ_i contains i linearly independent lattice vectors.
    
    INPUT:
    - n: Number of successive minima to compute (default: rank of lattice)
    
    OUTPUT:
    List [λ_1, λ_2, ..., λ_n] of successive minima
    """

def voronoi_cell(self):
    r"""
    Return the Voronoi cell (fundamental domain) of the lattice.
    
    This is the set of points closer to the origin than to any other
    lattice point.
    """

```

**NOTE**: For definite lattices, automorphism_group() equals orthogonal_group(),
both inherited from Lattices.

## Enumeration Methods

```python
def enumerate_upto_norm(self, bound):
    r"""
    Enumerate all lattice vectors v with |⟨v,v⟩| ≤ bound.
    
    INPUT:
    - bound: Upper bound on the absolute norm
    
    OUTPUT:
    Iterator over lattice vectors
    """

def count_upto_norm(self, bound):
    r"""
    Count lattice vectors v with |⟨v,v⟩| ≤ bound.
    
    INPUT:
    - bound: Upper bound on the absolute norm
    
    OUTPUT:
    Integer count
    """
```

## Reduction Methods

```python
def is_reduced(self):
    r"""
    Test if the lattice basis is reduced.
    
    The notion of reduction depends on the sign:
    - Positive definite: LLL or Minkowski reduced
    - Negative definite: Analogous reduction
    """

def reduce(self):
    r"""
    Return a reduced basis for the lattice.
    
    Applies appropriate reduction algorithm based on definiteness.
    """
```