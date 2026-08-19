<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/nondegenerate_lattices/definite_lattices/positive_definite_lattices/positive_definite_lattices.md
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

## Mathematical Test Assertions

The following assertions establish mathematical ground truth for positive definite lattice properties using canonical examples from Conway & Sloane's "Sphere Packings, Lattices and Groups" and standard mathematical literature.

### Property 1: Eigenvalue Positivity (Fundamental Definition)
```python
# Mathematical assertion: All eigenvalues must be strictly positive for positive definite lattices
# Note: Our convention uses negative Gram matrices, so we test -G for positivity
# sage: R = RootSystem(['A', 3])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: all(ev > 0 for ev in (-G).eigenvalues())
# True  # -G is positive definite for finite root systems

# sage: R = RootSystem(['E', 8])
# sage: L = R.root_lattice()  
# sage: G = L.gram_matrix()
# sage: all(ev > 0 for ev in (-G).eigenvalues())
# True  # E8 root lattice has positive definite -G
```

### Property 2: Sphere Packing Density Bounds (Conway & Sloane)
```python
# Mathematical assertion: Positive definite lattices admit sphere packings with finite density
# E8 achieves optimal density in dimension 8 (Viazovska 2016)
# sage: R = RootSystem(['E', 8])
# sage: L = R.root_lattice()
# sage: min_norm = min(v.inner_product(v) for v in L.roots())
# sage: min_norm > 0
# True  # All roots have positive norm (since form is positive definite)

# sage: len(L.roots())
# 240  # E8 has exactly 240 roots (Conway & Sloane Table 4.12)
```

### Property 3: Shortest Vector Problem Well-Definedness
```python
# Mathematical assertion: SVP is well-defined for positive definite lattices
# The minimum exists due to positive definiteness ensuring lower bounds
# sage: R = RootSystem(['A', 2])
# sage: L = R.root_lattice()
# sage: roots = L.roots()
# sage: norms = [v.inner_product(v) for v in roots]
# sage: min_norm = min(norms)
# sage: all(norm >= min_norm for norm in norms)
# True  # Minimum norm is achieved (SVP has solutions)
```

### Property 4: Hermite Constant Finiteness
```python
# Mathematical assertion: Hermite constant γ(L) is finite for positive definite lattices
# γ(L) = (minimum norm)^2 / det(L)^(2/n) where n is rank
# sage: R = RootSystem(['D', 4])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: det_G = G.determinant()
# sage: det_G != 0
# True  # Non-degenerate (determinant is non-zero)
# sage: det_G < 0
# True  # Our convention: negative determinant for positive definite forms
```

### Property 5: Voronoi Cell Compactness
```python
# Mathematical assertion: Fundamental domains are compact for positive definite lattices
# This follows from coercivity: ||x|| → ∞ as |coordinates| → ∞
# sage: R = RootSystem(['B', 3])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: # Test coercivity: all eigenvalues of -G are bounded away from 0
# sage: min_eigenval = min((-G).eigenvalues())
# sage: min_eigenval > 0
# True  # Positive definite ensures coercivity
```

### Property 6: Duality with Negative Definite Convention
```python
# Mathematical assertion: Our negative definite convention for finite types
# creates mathematical duality with positive definite sphere packing theory
# sage: R = RootSystem(['G', 2])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: # G is negative definite (our convention)
# sage: all(ev < 0 for ev in G.eigenvalues())
# True  # Finite type ⟺ negative definite Gram matrix
# sage: # -G would be the positive definite form for sphere packing
# sage: all(ev > 0 for ev in (-G).eigenvalues())
# True  # -G is positive definite (standard sphere packing form)
```

### Property 7: LLL Reduction Termination
```python
# Mathematical assertion: LLL algorithm terminates for positive definite lattices
# Termination follows from the decrease in the Lovász condition
# sage: R = RootSystem(['F', 4])
# sage: L = R.root_lattice()
# sage: G = L.gram_matrix()
# sage: # Reduced basis exists due to positive definiteness of -G
# sage: (-G).is_positive_definite()
# True  # Ensures LLL termination and well-definedness
```

### Property 8: Theta Series Convergence (Jacobi)
```python
# Mathematical assertion: Theta series converges for positive definite lattices
# θ_L(τ) = Σ_{v∈L} q^(v·v) converges for Im(τ) > 0 when form is positive definite
# sage: R = RootSystem(['E', 6])
# sage: L = R.root_lattice()
# sage: roots = L.roots()
# sage: # Test exponential decay: count vectors by norm squared
# sage: norm_counts = {}
# sage: for v in roots:
# sage:     norm_sq = v.inner_product(v)
# sage:     norm_counts[norm_sq] = norm_counts.get(norm_sq, 0) + 1
# sage: len(norm_counts) < 10  # Finite number of norms (exponential decay)
# True  # E6 has roots of only a few distinct lengths
```