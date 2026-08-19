<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/positive_definite_lattices/positive_definite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: PositiveDefiniteLattices

Positive definite lattices inherit all methods from `DefiniteLattices` and add:

## Sphere Packing Methods

```python
def density(self):
    r"""
    Return the packing density of the lattice.
    
    This is the fraction of space covered by non-overlapping spheres
    centered at lattice points.
    """

def center_density(self):
    r"""
    Return the center density (packing density times volume).
    
    This is a normalized measure of packing efficiency.
    """

def hermite_constant(self):
    r"""
    Return the Hermite constant γ(L) of the lattice.
    
    This is the square of the minimal norm divided by the 
    determinant to the power 2/n.
    """

def contact_polytope(self):
    r"""
    Return the contact polytope of the lattice.
    
    This is the convex hull of the minimal vectors.
    """
```

## LLL and Reduction

```python
def LLL(self):
    r"""
    Return an LLL-reduced basis for the lattice.
    
    Uses the Lenstra-Lenstra-Lovász lattice basis reduction algorithm.
    """

def BKZ(self, block_size):
    r"""
    Return a BKZ-reduced basis for the lattice.
    
    Uses block Korkine-Zolotarev reduction with given block size.
    
    INPUT:
    - block_size: Size of blocks for BKZ algorithm
    """

def HKZ(self):
    r"""
    Return a Hermite-Korkine-Zolotarev reduced basis.
    
    This is the strongest notion of reduction but computationally expensive.
    """
```

## Geometric Properties

```python
def inradius(self):
    r"""
    Return the inradius of the Voronoi cell.
    
    This equals the packing radius.
    """

def circumradius(self):
    r"""
    Return the circumradius of the Voronoi cell.
    
    This equals the covering radius.
    """

def normalized_volume(self):
    r"""
    Return the normalized volume of the fundamental domain.
    
    This is det(L)^(1/2) / V_n where V_n is the volume of 
    the unit ball in dimension n.
    """
```

## Optimization Methods

```python
def shortest_vector_problem(self, target=None):
    r"""
    Solve the shortest vector problem (SVP).
    
    Find the shortest nonzero vector, or the closest vector to a target.
    
    INPUT:
    - target: Target vector (if None, find shortest nonzero vector)
    
    OUTPUT:
    Shortest/closest lattice vector
    """

def closest_vector_problem(self, target):
    r"""
    Solve the closest vector problem (CVP).
    
    Find the lattice vector closest to the given target.
    
    INPUT:
    - target: Target point in ambient space
    
    OUTPUT:
    Closest lattice vector
    """
```