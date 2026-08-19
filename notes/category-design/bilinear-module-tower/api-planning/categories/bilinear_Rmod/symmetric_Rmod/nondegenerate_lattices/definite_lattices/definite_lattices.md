<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/definite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: DefiniteLattices

Definite lattices inherit all methods from `Lattices` and add:

**INHERITANCE**: DefiniteLattices inherit is_definite() from SymmetricBilinearModules,
which returns True for all objects in this category.

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