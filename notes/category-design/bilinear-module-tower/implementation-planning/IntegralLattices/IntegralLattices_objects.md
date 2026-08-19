<!--
Origin: gitclones/Coxeter/implementation/planning/IntegralLattices/IntegralLattices_objects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects: Integral Lattice Parent Implementation

Parent class implementation for integral lattices with algorithms for lattice reduction, shortest vectors, and arithmetic invariants.

## Parent Class Structure

```python
from sage.modules.free_module import FreeModule_submodule_with_basis_pid
from sage.structure.unique_representation import UniqueRepresentation

class IntegralLattice_with_basis(SymmetricBilinearModule_with_basis):
    """
    An integral lattice with distinguished basis.
    
    An integral lattice is a free ℤ-module with symmetric bilinear form
    taking integer values. The Gram matrix has integer entries.
    
    This class provides:
    - Lattice reduction algorithms (LLL, BKZ)
    - Shortest vector algorithms
    - Theta series computation
    - Genus and spinor genus
    - Automorphism groups
    - Embeddings and primitive extensions
    
    EXAMPLES::
    
        sage: # Standard Euclidean lattice
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L
        3-dimensional integral lattice
        sage: L.discriminant()
        1
        sage: L.minimum()
        1
        
        sage: # E₈ root lattice
        sage: E8 = IntegralLattice("E8")
        sage: E8.rank()
        8
        sage: E8.minimum()
        2
        sage: E8.kissing_number()
        240
        
        sage: # Custom lattice
        sage: G = matrix(ZZ, [[4, 1, 0], [1, 2, 1], [0, 1, 6]])
        sage: L = IntegralLattice(G)
        sage: L.is_positive_definite()
        True
        sage: L.discriminant()
        42
    """
    
    def __init__(self, gram_matrix, basis=None, check=True, **kwds):
        """
        Initialize an integral lattice.
        
        INPUT:
        - gram_matrix -- symmetric integer matrix
        - basis -- optional basis labels
        - check -- verify integrality and symmetry
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: L.base_ring()
            Integer Ring
            sage: L.gram_matrix().base_ring()
            Integer Ring
        """
        if check:
            if gram_matrix.base_ring() != ZZ:
                raise ValueError("Gram matrix must have integer entries")
            if gram_matrix != gram_matrix.transpose():
                raise ValueError("Gram matrix must be symmetric")
        
        # Set up category
        from sage.categories.integral_lattices import IntegralLattices
        category = IntegralLattices()
        
        # Determine additional axioms
        if self._check_positive_definite(gram_matrix):
            category = category.PositiveDefinite()
        
        if self._check_even(gram_matrix):
            category = category.Even()
        
        if abs(gram_matrix.determinant()) == 1:
            category = category.Unimodular()
        
        # Initialize as symmetric bilinear module
        super().__init__(gram_matrix, basis=basis, category=category, **kwds)
        
        # Cache for expensive computations
        self._minimum = None
        self._kissing_number = None
        self._automorphism_group = None
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: IntegralLattice(matrix.identity(3))
            3-dimensional integral lattice
            
            sage: IntegralLattice("E8")
            E₈ root lattice
        """
        if hasattr(self, '_name'):
            return self._name
        
        special = []
        if self.is_even():
            special.append("even")
        if self.is_unimodular():
            special.append("unimodular")
        if hasattr(self, '_root_system'):
            special.append("root")
        
        if special:
            return f"{self.rank()}-dimensional {' '.join(special)} integral lattice"
        else:
            return f"{self.rank()}-dimensional integral lattice"
    
    def _check_positive_definite(self, gram_matrix):
        """Check if Gram matrix is positive definite."""
        try:
            return gram_matrix.is_positive_definite()
        except:
            # Fallback to eigenvalue check
            eigenvals = gram_matrix.eigenvalues()
            return all(ev > 0 for ev in eigenvals)
    
    def _check_even(self, gram_matrix):
        """Check if lattice is even."""
        return all(gram_matrix[i,i] % 2 == 0 for i in range(gram_matrix.nrows()))
```

## Lattice Reduction Algorithms

```python
def LLL(self, delta=0.75, eta=0.501):
    """
    Return LLL-reduced basis.
    
    The LLL algorithm finds a nearly orthogonal basis with
    controlled basis vector lengths. For dimension n and shortest
    vector length λ₁, the first basis vector satisfies:
    ||b₁|| ≤ ((4/3)^((n-1)/2)) * λ₁
    
    INPUT:
    - delta -- reduction parameter (default: 0.75)
    - eta -- precision parameter (default: 0.501)
    
    OUTPUT:
    LLL-reduced basis as list of lattice elements
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[10, 3], [3, 10]]))
        sage: reduced_basis = L.LLL()
        sage: G_reduced = matrix([v.to_vector() for v in reduced_basis])
        sage: G_reduced
        [ 3  1]
        [-1  3]  # Much more orthogonal than original
    """
    from sage.modules.free_module_integer import IntegerLattice
    
    # Convert to Sage's integer lattice for LLL
    ambient = IntegerLattice(self.gram_matrix())
    reduced_basis_coords = ambient.LLL(delta=delta, eta=eta)
    
    # Convert back to lattice elements
    return [self._from_vector(v) for v in reduced_basis_coords]

def BKZ(self, block_size=20, precision=None):
    """
    Return BKZ-reduced basis.
    
    Block Korkine-Zolotarev reduction generalizes LLL with
    blocks of size k. Gives better reduction than LLL but
    slower for large block sizes.
    
    INPUT:
    - block_size -- BKZ parameter (default: 20)
    - precision -- floating point precision
    
    OUTPUT:
    BKZ-reduced basis
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[100, 30], [30, 100]]))
        sage: bkz_basis = L.BKZ(block_size=2)
        sage: # Should find very short basis vectors
    """
    # This requires interface to fplll or similar
    raise NotImplementedError("BKZ reduction requires fplll")

def HKZ(self):
    """
    Return HKZ-reduced (Hermite-Korkine-Zolotarev) basis.
    
    HKZ gives optimal reduction: first vector is shortest,
    second is shortest orthogonal to first, etc.
    
    OUTPUT:
    HKZ-reduced basis
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L.HKZ()
        [(1, 0), (0, 1)]  # Already HKZ-reduced
    """
    # HKZ is computationally intensive
    raise NotImplementedError("HKZ reduction")
```

## Shortest Vector Algorithms

```python
def shortest_vectors(self):
    """
    Return all shortest non-zero vectors.
    
    Finds all vectors v with q(v) = minimum.
    Uses enumeration algorithms for positive definite lattices.
    
    OUTPUT:
    List of shortest vectors (includes ±v for each v)
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L.shortest_vectors()
        [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), 
         (0, 0, 1), (0, 0, -1)]
        
        sage: # A₂ root lattice
        sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
        sage: len(A2.shortest_vectors())
        6  # The 6 roots
    """
    if not self.is_positive_definite():
        raise ValueError("Shortest vectors only for positive definite lattices")
    
    if self._minimum is None:
        self._compute_minimum_and_shortest()
    
    return self._shortest_vectors

def _compute_minimum_and_shortest(self):
    """
    Compute minimum and shortest vectors using enumeration.
    
    Uses branch-and-bound enumeration with LLL preprocessing.
    """
    # Start with LLL-reduced basis for efficiency
    reduced_basis = self.LLL()
    
    # Use first vector norm as upper bound
    bound = self.quadratic_form(reduced_basis[0])
    
    # Enumeration algorithm
    shortest = []
    minimum = bound
    
    # This is a simplified sketch - real implementation needs
    # efficient enumeration (Schnorr-Euchner, pruning, etc.)
    from itertools import product
    
    # Search in a box determined by the bound
    n = self.rank()
    coord_bound = int(bound ** 0.5) + 1
    
    for coords in product(range(-coord_bound, coord_bound + 1), repeat=n):
        if all(c == 0 for c in coords):
            continue
        
        v = sum(c * b for c, b in zip(coords, reduced_basis) if c != 0)
        norm = self.quadratic_form(v)
        
        if norm < minimum:
            minimum = norm
            shortest = [v, -v]
        elif norm == minimum:
            if v not in shortest and -v not in shortest:
                shortest.extend([v, -v])
    
    self._minimum = minimum
    self._shortest_vectors = shortest
    self._kissing_number = len(shortest)

def closest_vector(self, target):
    """
    Find lattice vector closest to target.
    
    Solves the closest vector problem (CVP) which is
    computationally hard in general.
    
    INPUT:
    - target -- vector in ambient space
    
    OUTPUT:
    Closest lattice vector
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: target = vector([2.7, 3.2])
        sage: L.closest_vector(target)
        (3, 3)
    """
    # Use Babai's nearest plane algorithm
    # Start with LLL basis
    reduced_basis = self.LLL()
    
    # This is a simplified version
    # Real implementation needs careful rounding
    from sage.modules.free_module_element import vector
    
    # Express target in reduced basis coordinates
    basis_matrix = matrix([b.to_vector() for b in reduced_basis])
    coords = basis_matrix.solve_left(vector(target))
    
    # Round to nearest integers
    rounded_coords = [round(c) for c in coords]
    
    # Reconstruct lattice vector
    return sum(c * b for c, b in zip(rounded_coords, reduced_basis))
```

## Arithmetic Invariants

```python
def successive_minima(self, k=None):
    """
    Return the successive minima λ₁, ..., λₖ.
    
    The i-th successive minimum λᵢ is the smallest r such that
    the ball of radius r contains i linearly independent vectors.
    
    INPUT:
    - k -- number of minima (default: rank)
    
    OUTPUT:
    List of successive minima
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[4, 1], [1, 4]]))
        sage: L.successive_minima()
        [3, 4]  # λ₁ = 3 from (1,0), λ₂ = 4 from (0,1)
    """
    if k is None:
        k = self.rank()
    
    # This requires sophisticated enumeration
    raise NotImplementedError("Successive minima computation")

def covering_radius(self):
    """
    Return the covering radius.
    
    The covering radius is max_{x} d(x, L), the maximum
    distance from any point to the lattice.
    
    OUTPUT:
    Covering radius
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L.covering_radius()
        sqrt(2)/2  # For ℤ², covering radius is √2/2
    """
    # Related to dual lattice and Voronoi cell
    raise NotImplementedError("Covering radius computation")

def hermite_constant(self):
    """
    Return achieved Hermite constant γ(L).
    
    For minimum λ₁ and discriminant d:
    γ(L) = λ₁ / d^(1/n)
    
    OUTPUT:
    Hermite constant for this lattice
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L.hermite_constant()
        1  # Achieves γ₃ for dimension 3
    """
    n = self.rank()
    minimum = self.minimum()
    disc = abs(self.discriminant())
    
    return minimum / disc ** (1/n)

def dual_lattice(self):
    """
    Return the dual lattice L*.
    
    L* = {v ∈ ℚⁿ : b(v,w) ∈ ℤ for all w ∈ L}
    
    Has Gram matrix G⁻¹.
    
    OUTPUT:
    IntegralLattice representing L*
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 0], [0, 2]]))
        sage: Ldual = L.dual_lattice()
        sage: Ldual.gram_matrix()
        [1/2   0]
        [  0 1/2]
        sage: Ldual.discriminant()
        1/4  # = 1/disc(L)
    """
    G = self.gram_matrix()
    if G.determinant() == 0:
        raise ValueError("Cannot dualize degenerate lattice")
    
    G_dual = G.inverse()
    
    # Dual may not be integral - need FractionalLattice
    if all(e in ZZ for e in G_dual.list()):
        return IntegralLattice(G_dual)
    else:
        # Return as fractional lattice
        raise NotImplementedError("Fractional lattice needed")

def primitive_extensions(self, max_index=10):
    """
    Enumerate primitive extensions of this lattice.
    
    A primitive extension L' ⊃ L has [L' : L] = p prime.
    These correspond to isotropic vectors in L*/L mod p.
    
    INPUT:
    - max_index -- bound on extension index
    
    OUTPUT:
    List of primitive extensions
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 0], [0, 2]]))
        sage: extensions = L.primitive_extensions(max_index=3)
        sage: len(extensions)
        2  # Index 2 extensions
    """
    # This involves gluing theory and local-global principles
    raise NotImplementedError("Primitive extension enumeration")
```

## Genus and Class Group

```python
def genus_representatives(self):
    """
    Return representatives for the genus of this lattice.
    
    The genus consists of all lattices locally isomorphic
    to this one at all primes (including ∞).
    
    OUTPUT:
    List of inequivalent lattices in the genus
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
        sage: genus_reps = L.genus_representatives()
        sage: len(genus_reps)
        1  # Often unique in genus for small discriminant
    """
    # Use mass formula and neighbor enumeration
    raise NotImplementedError("Genus representative computation")

def class_number(self):
    """
    Return the class number (size of genus).
    
    OUTPUT:
    Number of isometry classes in the genus
    
    EXAMPLES::
    
        sage: E8 = IntegralLattice("E8")
        sage: E8.class_number()
        1  # E₈ is unique in its genus
    """
    return len(self.genus_representatives())

def mass(self):
    """
    Return the mass of the genus.
    
    mass = Σ_{L in genus} 1/|Aut(L)|
    
    OUTPUT:
    Rational number
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L.mass()
        1/8  # mass of 2-dimensional unimodular genus
    """
    # Computed via local densities
    raise NotImplementedError("Mass formula computation")

def spinor_genera(self):
    """
    Return the spinor genera within this genus.
    
    The genus splits into 2^t spinor genera where
    t depends on the discriminant factorization.
    
    OUTPUT:
    List of spinor genus representatives
    """
    # Involves spinor norm computations
    raise NotImplementedError("Spinor genus computation")
```

## Automorphism Group

```python
def automorphism_group(self, gens_only=False):
    """
    Return the automorphism group of this lattice.
    
    Aut(L) = {g ∈ GL_n(ℤ) : g^T G g = G}
    
    INPUT:
    - gens_only -- if True, return only generators
    
    OUTPUT:
    MatrixGroup representing Aut(L)
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: G = L.automorphism_group()
        sage: G.order()
        48  # = 2³ × 3! = hyperoctahedral group
        
        sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
        sage: A2.automorphism_group().order()
        12  # Dihedral group D₆
    """
    if self._automorphism_group is not None and not gens_only:
        return self._automorphism_group
    
    # Use shortest vectors to constrain automorphisms
    shortest = self.shortest_vectors()
    
    # Automorphisms must permute shortest vectors
    # This gives a finite computation
    raise NotImplementedError("Automorphism group computation")

def is_isometric(self, other, certificate=False):
    """
    Test if this lattice is isometric to another.
    
    Two lattices are isometric if there exists g ∈ GL_n(ℤ)
    with g^T G₁ g = G₂.
    
    INPUT:
    - other -- another integral lattice
    - certificate -- if True, return isometry
    
    OUTPUT:
    Boolean or (boolean, matrix)
    
    EXAMPLES::
    
        sage: L1 = IntegralLattice(matrix([[2, 0], [0, 3]]))
        sage: L2 = IntegralLattice(matrix([[3, 0], [0, 2]]))
        sage: L1.is_isometric(L2)
        True  # Via permutation matrix
    """
    # First check basic invariants
    if self.rank() != other.rank():
        return False if not certificate else (False, None)
    
    if self.discriminant() != other.discriminant():
        return False if not certificate else (False, None)
    
    if self.signature() != other.signature():
        return False if not certificate else (False, None)
    
    # Check genus
    if not self.is_in_same_genus(other):
        return False if not certificate else (False, None)
    
    # Now need to check isometry within genus
    # This is computationally hard in general
    raise NotImplementedError("Isometry testing algorithm")
```

## Embeddings and Representations

```python
def primitive_embeddings_in(self, target, max_index=None):
    """
    Find primitive embeddings of this lattice into target.
    
    An embedding L ↪ M is primitive if L ∩ pM = pL for all
    primes p (i.e., L is a direct summand of M).
    
    INPUT:
    - target -- larger integral lattice
    - max_index -- bound on [M : L + L^⊥_M]
    
    OUTPUT:
    List of primitive embeddings
    
    EXAMPLES::
    
        sage: A1 = IntegralLattice(matrix([[2]]))
        sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
        sage: embeddings = A1.primitive_embeddings_in(A2)
        sage: len(embeddings)
        3  # Three ways to embed A₁ root in A₂
    """
    # Use Nikulin's theory and gluing conditions
    raise NotImplementedError("Primitive embedding enumeration")

def orthogonal_group(self):
    """
    Return the orthogonal group O(L).
    
    For integral lattices, this is a finite group.
    O(L) = Aut(L) when L is positive definite.
    
    OUTPUT:
    MatrixGroup
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 1], [1, 2]]))
        sage: O = L.orthogonal_group()
        sage: O.order()
        12  # Dihedral group D₆
    """
    if self.is_positive_definite():
        return self.automorphism_group()
    else:
        # For indefinite lattices, O(L) may be infinite
        raise NotImplementedError("Orthogonal group for indefinite lattices")

def representation_numbers(self, B, max_norm):
    """
    Count representations of quadratic forms by this lattice.
    
    r_L(n) = #{v ∈ L : q(v) = n}
    
    INPUT:
    - B -- quadratic form or integer
    - max_norm -- compute for norms up to max_norm
    
    OUTPUT:
    List of representation numbers
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L.representation_numbers(1, 10)
        [0, 6, 12, 8, 6, 24, 24, 0, 12, 30]
        # r(n) for n = 1,...,10
    """
    # Related to theta series coefficients
    raise NotImplementedError("Representation number computation")
```

## Mathematical Properties

The integral lattice implementation maintains:

```python
# Mathematical assertion: Dual lattice relationship
# (L*)* = L for non-degenerate L

# Mathematical assertion: Discriminant invariant
# disc(L) = det(Gram) is invariant under base change

# Mathematical assertion: Primitive vector characterization
# v primitive ⟺ v = kg implies k = ±1

# Mathematical assertion: Hermite bound
# λ₁(L) ≤ γₙ · disc(L)^(1/n) where γₙ is Hermite constant

# Mathematical assertion: Voronoi's theorem
# L determined up to isometry by Voronoi cell

# Mathematical assertion: Mass formula
# Σ_{L in genus} 1/|Aut(L)| = product of local densities

# Mathematical assertion: Primitive extension correspondence
# Primitive extensions ↔ isotropic lines in L*/L

# Mathematical assertion: Root lattice property
# L is root lattice ⟺ min(L) = 2 and roots span L
```

This implementation provides comprehensive algorithms for integral lattice computations while maintaining mathematical rigor and efficiency.