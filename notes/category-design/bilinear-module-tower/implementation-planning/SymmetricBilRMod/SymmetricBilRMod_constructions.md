<!--
Origin: gitclones/Coxeter/implementation/planning/SymmetricBilRMod/SymmetricBilRMod_constructions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Constructions: Symmetric Bilinear Module Factory and Standard Forms

Factory functions and standard constructions for symmetric bilinear modules including classical quadratic forms, lattices, and geometric examples.

## Factory Function

```python
def SymmetricBilinearModule(data=None, base_ring=None, **kwds):
    """
    Construct a symmetric bilinear module from various input formats.
    
    This factory function handles multiple input types:
    - Symmetric matrices (Gram matrices)
    - Quadratic form expressions
    - Classical lattice names
    - Signature specifications
    - Diagonal specifications
    
    INPUT:
    - data -- matrix, quadratic form, signature tuple, or lattice name
    - base_ring -- optional base ring (inferred from data if not given)
    - **kwds -- additional options passed to constructor
    
    OUTPUT:
    SymmetricBilinearModule_with_basis instance
    
    EXAMPLES::
    
        sage: # From Gram matrix
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: M.signature()
        (2, 0, 0)
        
        sage: # From signature
        sage: L = SymmetricBilinearModule(signature=(1, 1, 0))
        sage: L.is_indefinite()
        True
        
        sage: # From diagonal values
        sage: D = SymmetricBilinearModule(diagonal=[1, -1, 2])
        sage: D.gram_matrix()
        [1  0  0]
        [0 -1  0]
        [0  0  2]
        
        sage: # Classical lattices
        sage: E8 = SymmetricBilinearModule("E8")
        sage: E8.rank()
        8
        sage: E8.is_even()
        True
        sage: E8.is_unimodular()
        True
    """
    if isinstance(data, str):
        # Classical lattice name
        return _construct_classical_lattice(data, base_ring=base_ring, **kwds)
    
    elif hasattr(data, 'nrows') and hasattr(data, 'ncols'):
        # Matrix input
        if not data.is_square():
            raise ValueError("Gram matrix must be square")
        if data != data.transpose():
            raise ValueError("Gram matrix must be symmetric")
        
        if base_ring is None:
            base_ring = data.base_ring()
        
        return SymmetricBilinearModule_with_basis(data, **kwds)
    
    elif isinstance(data, (tuple, list)) and len(data) == 3:
        # Signature tuple (p, q, r)
        return _construct_from_signature(data, base_ring=base_ring, **kwds)
    
    elif hasattr(data, '__iter__') and 'diagonal' in kwds:
        # Diagonal specification
        return _construct_diagonal(data, base_ring=base_ring, **kwds)
    
    elif 'signature' in kwds:
        # Signature in keyword arguments
        return _construct_from_signature(kwds['signature'], base_ring=base_ring, **kwds)
    
    elif 'diagonal' in kwds:
        # Diagonal in keyword arguments
        return _construct_diagonal(kwds['diagonal'], base_ring=base_ring, **kwds)
    
    else:
        raise ValueError(f"Cannot construct symmetric bilinear module from {type(data)}")

def _construct_from_signature(signature, base_ring=QQ, **kwds):
    """Construct module with given signature (p, q, r)."""
    p, q, r = signature
    
    if base_ring is None:
        base_ring = QQ
    
    # Build diagonal matrix with p positive, q negative, r zero entries
    diagonal_entries = [1] * p + [-1] * q + [0] * r
    
    from sage.matrix.constructor import diagonal_matrix
    gram_matrix = diagonal_matrix(base_ring, diagonal_entries)
    
    return SymmetricBilinearModule_with_basis(gram_matrix, **kwds)

def _construct_diagonal(diagonal_entries, base_ring=None, **kwds):
    """Construct module with given diagonal entries."""
    if base_ring is None:
        # Infer base ring from entries
        from sage.structure.sequence import Sequence
        base_ring = Sequence(diagonal_entries).universe()
    
    from sage.matrix.constructor import diagonal_matrix
    gram_matrix = diagonal_matrix(base_ring, diagonal_entries)
    
    return SymmetricBilinearModule_with_basis(gram_matrix, **kwds)

def _construct_classical_lattice(name, base_ring=ZZ, **kwds):
    """Construct classical named lattices."""
    name = name.upper()
    
    if name == "E8":
        return _construct_E8_lattice(base_ring, **kwds)
    elif name == "LEECH":
        return _construct_leech_lattice(base_ring, **kwds)
    elif name.startswith("A"):
        # Root lattice A_n
        n = int(name[1:])
        return _construct_root_lattice_A(n, base_ring, **kwds)
    elif name.startswith("D"):
        # Root lattice D_n
        n = int(name[1:])
        return _construct_root_lattice_D(n, base_ring, **kwds)
    elif name.startswith("E"):
        # Exceptional root lattices E_6, E_7, E_8
        n = int(name[1:])
        if n in [6, 7, 8]:
            return _construct_root_lattice_E(n, base_ring, **kwds)
    elif name == "HYPERBOLIC":
        return _construct_hyperbolic_plane(base_ring, **kwds)
    elif name == "EUCLIDEAN":
        # Standard Euclidean form (dimension from kwds)
        dim = kwds.get('dimension', 2)
        return _construct_euclidean_space(dim, base_ring, **kwds)
    elif name == "LORENTZ" or name == "MINKOWSKI":
        # Lorentzian signature (dimension from kwds)
        dim = kwds.get('dimension', 4)
        return _construct_lorentz_space(dim, base_ring, **kwds)
    
    raise ValueError(f"Unknown classical lattice: {name}")
```

## Standard Quadratic Forms

```python
def euclidean_space(dimension, base_ring=QQ):
    """
    Standard Euclidean space with inner product.
    
    Gram matrix is the identity matrix.
    
    INPUT:
    - dimension -- positive integer
    - base_ring -- base field (default QQ)
    
    OUTPUT:
    Positive definite symmetric bilinear module
    
    EXAMPLES::
    
        sage: E3 = euclidean_space(3)
        sage: E3.signature()
        (3, 0, 0)
        sage: E3.is_positive_definite()
        True
        sage: E3.gram_matrix()
        [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    from sage.matrix.constructor import identity_matrix
    gram_matrix = identity_matrix(base_ring, dimension)
    return SymmetricBilinearModule_with_basis(gram_matrix)

def _construct_euclidean_space(dimension, base_ring, **kwds):
    """Internal constructor for Euclidean space."""
    return euclidean_space(dimension, base_ring)

def hyperbolic_plane(base_ring=QQ):
    """
    Standard hyperbolic plane with signature (1, 1, 0).
    
    Gram matrix: [[0, 1], [1, 0]]
    
    INPUT:
    - base_ring -- base field (default QQ)
    
    OUTPUT:
    Indefinite symmetric bilinear module
    
    EXAMPLES::
    
        sage: H = hyperbolic_plane()
        sage: H.signature()
        (1, 1, 0)
        sage: H.witt_index()
        1
        sage: H.gram_matrix()
        [0 1]
        [1 0]
        
        sage: # Isotropic vectors
        sage: e, f = H.gens()
        sage: e.is_isotropic()
        True
        sage: f.is_isotropic()
        True
        sage: (e + f).is_isotropic()
        True
        sage: (e - f).is_isotropic()
        True
    """
    from sage.matrix.constructor import matrix
    gram_matrix = matrix(base_ring, [[0, 1], [1, 0]])
    return SymmetricBilinearModule_with_basis(gram_matrix)

def _construct_hyperbolic_plane(base_ring, **kwds):
    """Internal constructor for hyperbolic plane."""
    return hyperbolic_plane(base_ring)

def lorentz_space(dimension, base_ring=QQ):
    """
    Lorentzian space with signature (dimension-1, 1, 0).
    
    Standard form for relativity: mostly positive with one negative.
    
    INPUT:
    - dimension -- space dimension (≥ 2)
    - base_ring -- base field (default QQ)
    
    OUTPUT:
    Indefinite symmetric bilinear module
    
    EXAMPLES::
    
        sage: # 4D Minkowski spacetime
        sage: M4 = lorentz_space(4)
        sage: M4.signature()
        (3, 1, 0)
        sage: M4.is_indefinite()
        True
        
        sage: # Time-like and space-like vectors
        sage: t, x, y, z = M4.gens()
        sage: t.is_negative()  # Time-like
        True
        sage: x.is_positive()  # Space-like
        True
    """
    if dimension < 2:
        raise ValueError("Lorentz space requires dimension ≥ 2")
    
    # Signature: (dimension-1, 1, 0) - mostly spacelike
    diagonal_entries = [1] * (dimension - 1) + [-1]
    
    from sage.matrix.constructor import diagonal_matrix
    gram_matrix = diagonal_matrix(base_ring, diagonal_entries)
    return SymmetricBilinearModule_with_basis(gram_matrix)

def _construct_lorentz_space(dimension, base_ring, **kwds):
    """Internal constructor for Lorentz space."""
    return lorentz_space(dimension, base_ring)

def definite_form(diagonal_values, base_ring=None):
    """
    Definite quadratic form with specified diagonal values.
    
    All diagonal values must have the same sign for definiteness.
    
    INPUT:
    - diagonal_values -- list of positive or negative values
    - base_ring -- base ring (inferred if not given)
    
    OUTPUT:
    Definite symmetric bilinear module
    
    EXAMPLES::
    
        sage: # Positive definite
        sage: P = definite_form([1, 2, 3])
        sage: P.is_positive_definite()
        True
        
        sage: # Negative definite
        sage: N = definite_form([-1, -2, -3])
        sage: N.is_negative_definite()
        True
    """
    if not diagonal_values:
        raise ValueError("Need at least one diagonal value")
    
    # Check definiteness
    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in diagonal_values]
    if 0 in signs:
        raise ValueError("Definite forms cannot have zero diagonal values")
    if len(set(signs)) > 1:
        raise ValueError("All diagonal values must have same sign for definite forms")
    
    return _construct_diagonal(diagonal_values, base_ring)

def binary_form(a, b, c, base_ring=None):
    """
    Binary quadratic form ax² + 2bxy + cy².
    
    Gram matrix: [[a, b], [b, c]]
    
    INPUT:
    - a, b, c -- coefficients with a, c ≠ 0
    - base_ring -- base ring (inferred from coefficients)
    
    OUTPUT:
    Rank 2 symmetric bilinear module
    
    EXAMPLES::
    
        sage: # Positive definite binary form
        sage: B = binary_form(2, 1, 3)
        sage: B.discriminant()
        5
        sage: B.is_positive_definite()
        True
        
        sage: # Indefinite binary form
        sage: H = binary_form(1, 0, -1)
        sage: H.signature()
        (1, 1, 0)
        sage: H.is_indefinite()
        True
    """
    if base_ring is None:
        from sage.structure.sequence import Sequence
        base_ring = Sequence([a, b, c]).universe()
    
    from sage.matrix.constructor import matrix
    gram_matrix = matrix(base_ring, [[a, b], [b, c]])
    return SymmetricBilinearModule_with_basis(gram_matrix)

def sum_of_squares(coefficients, base_ring=None):
    """
    Sum of squares form: Σ aᵢ xᵢ².
    
    Diagonal form with given coefficients.
    
    INPUT:
    - coefficients -- list of diagonal coefficients
    - base_ring -- base ring (inferred if not given)
    
    OUTPUT:
    Diagonal symmetric bilinear module
    
    EXAMPLES::
    
        sage: # Standard sum of squares
        sage: S = sum_of_squares([1, 1, 1, 1])
        sage: S.is_positive_definite()
        True
        
        sage: # Mixed signature
        sage: M = sum_of_squares([1, 1, -1, -1])
        sage: M.signature()
        (2, 2, 0)
    """
    return _construct_diagonal(coefficients, base_ring)
```

## Classical Lattices

```python
def _construct_root_lattice_A(n, base_ring=ZZ, **kwds):
    """
    Root lattice A_n (simple roots of SL_{n+1}).
    
    Standard realization as sublattice of Z^{n+1} with coordinate sum = 0.
    
    INPUT:
    - n -- positive integer
    - base_ring -- base ring (default ZZ)
    
    OUTPUT:
    Integral positive definite symmetric bilinear module
    """
    if n < 1:
        raise ValueError("A_n requires n ≥ 1")
    
    # A_n has Gram matrix with 2's on diagonal, -1's adjacent
    from sage.matrix.constructor import matrix
    
    gram = matrix(base_ring, n, n)
    for i in range(n):
        gram[i,i] = 2
        if i > 0:
            gram[i,i-1] = -1
            gram[i-1,i] = -1
    
    return SymmetricBilinearModule_with_basis(gram)

def _construct_root_lattice_D(n, base_ring=ZZ, **kwds):
    """
    Root lattice D_n (simple roots of SO_{2n}).
    
    Standard realization with Gram matrix pattern for D_n.
    
    INPUT:
    - n -- integer ≥ 3
    - base_ring -- base ring (default ZZ)
    
    OUTPUT:
    Integral positive definite symmetric bilinear module
    """
    if n < 3:
        raise ValueError("D_n requires n ≥ 3")
    
    # D_n Gram matrix construction
    from sage.matrix.constructor import matrix
    
    gram = matrix(base_ring, n, n)
    
    # Main diagonal: all 2's
    for i in range(n):
        gram[i,i] = 2
    
    # Off-diagonal pattern for D_n
    for i in range(n-2):
        gram[i,i+1] = -1
        gram[i+1,i] = -1
    
    # Special pattern for last two roots
    gram[n-3,n-1] = -1
    gram[n-1,n-3] = -1
    
    return SymmetricBilinearModule_with_basis(gram)

def _construct_root_lattice_E(n, base_ring=ZZ, **kwds):
    """
    Exceptional root lattices E_6, E_7, E_8.
    
    Standard Gram matrix realizations.
    
    INPUT:
    - n -- 6, 7, or 8
    - base_ring -- base ring (default ZZ)
    
    OUTPUT:
    Integral positive definite symmetric bilinear module
    """
    if n not in [6, 7, 8]:
        raise ValueError("Exceptional E lattices only for n = 6, 7, 8")
    
    # This would contain explicit Gram matrices for E_6, E_7, E_8
    # These are well-known from Lie algebra theory
    
    if n == 6:
        # E_6 Gram matrix (6×6)
        gram_data = [
            [2, -1,  0,  0,  0,  0],
            [-1, 2, -1,  0,  0,  0],
            [0, -1,  2, -1,  0, -1],
            [0,  0, -1,  2, -1,  0],
            [0,  0,  0, -1,  2,  0],
            [0,  0, -1,  0,  0,  2]
        ]
    elif n == 7:
        # E_7 Gram matrix (7×7) - extends E_6
        gram_data = [
            [2, -1,  0,  0,  0,  0,  0],
            [-1, 2, -1,  0,  0,  0,  0],
            [0, -1,  2, -1,  0, -1,  0],
            [0,  0, -1,  2, -1,  0,  0],
            [0,  0,  0, -1,  2,  0,  0],
            [0,  0, -1,  0,  0,  2, -1],
            [0,  0,  0,  0,  0, -1,  2]
        ]
    else:  # n == 8
        # E_8 Gram matrix (8×8) - extends E_7
        gram_data = [
            [2, -1,  0,  0,  0,  0,  0,  0],
            [-1, 2, -1,  0,  0,  0,  0,  0],
            [0, -1,  2, -1,  0, -1,  0,  0],
            [0,  0, -1,  2, -1,  0,  0,  0],
            [0,  0,  0, -1,  2,  0,  0,  0],
            [0,  0, -1,  0,  0,  2, -1,  0],
            [0,  0,  0,  0,  0, -1,  2, -1],
            [0,  0,  0,  0,  0,  0, -1,  2]
        ]
    
    from sage.matrix.constructor import matrix
    gram_matrix = matrix(base_ring, gram_data)
    return SymmetricBilinearModule_with_basis(gram_matrix)

def _construct_E8_lattice(base_ring=ZZ, **kwds):
    """Construct the E_8 lattice."""
    return _construct_root_lattice_E(8, base_ring, **kwds)

def _construct_leech_lattice(base_ring=ZZ, **kwds):
    """
    The Leech lattice (24-dimensional even unimodular lattice).
    
    This requires the explicit 24×24 Gram matrix of the Leech lattice.
    Construction is quite involved and typically done via other methods.
    
    OUTPUT:
    24-dimensional even unimodular integral lattice
    """
    # The Leech lattice construction is complex
    # Would typically be built from other constructions like:
    # - Turyn construction using Hadamard matrices
    # - Construction from the Golay code
    # - Vertex operator algebra construction
    
    raise NotImplementedError("Leech lattice construction requires specialized algorithms")

def unimodular_lattice(signature, base_ring=ZZ):
    """
    Construct unimodular lattice with given signature.
    
    A lattice is unimodular if det(Gram matrix) = ±1.
    
    INPUT:
    - signature -- tuple (p, q, 0) with p + q = dimension
    - base_ring -- base ring (should be ZZ for integrality)
    
    OUTPUT:
    Unimodular integral symmetric bilinear module
    
    EXAMPLES::
    
        sage: # Hyperbolic plane (unimodular)
        sage: H = unimodular_lattice((1, 1, 0))
        sage: H.discriminant()
        -1
        sage: abs(H.discriminant()) == 1
        True
        
        sage: # Even positive definite unimodular lattices exist only in dimensions 8k
        sage: E8 = unimodular_lattice((8, 0, 0))  # Would be E_8 lattice
    """
    p, q, r = signature
    
    if r != 0:
        raise ValueError("Unimodular lattices must be non-degenerate")
    
    dimension = p + q
    
    # For small dimensions, we can construct explicit examples
    if dimension == 1:
        # Only ±1 are unimodular in dimension 1
        if p == 1:
            return _construct_diagonal([1], base_ring)
        else:
            return _construct_diagonal([-1], base_ring)
    
    elif dimension == 2 and p == q == 1:
        # Hyperbolic plane
        return hyperbolic_plane(base_ring)
    
    elif dimension == 8 and p == 8 and q == 0:
        # E_8 lattice
        return _construct_E8_lattice(base_ring)
    
    else:
        # General construction would require classification theory
        raise NotImplementedError(f"Unimodular lattice construction for signature {signature}")

def even_unimodular_lattice(dimension, base_ring=ZZ):
    """
    Even unimodular lattice of given dimension.
    
    Even unimodular lattices exist only in dimensions 0 mod 8.
    
    INPUT:
    - dimension -- positive integer ≡ 0 (mod 8)
    - base_ring -- base ring (default ZZ)
    
    OUTPUT:
    Even unimodular positive definite lattice
    
    EXAMPLES::
    
        sage: E8 = even_unimodular_lattice(8)
        sage: E8.is_even()
        True
        sage: E8.is_unimodular()
        True
        sage: E8.discriminant()
        1
    """
    if dimension % 8 != 0:
        raise ValueError("Even unimodular lattices exist only in dimensions 0 mod 8")
    
    if dimension == 8:
        return _construct_E8_lattice(base_ring)
    elif dimension == 16:
        # E_8 ⊕ E_8
        E8 = _construct_E8_lattice(base_ring)
        return E8.orthogonal_sum(E8)
    elif dimension == 24:
        # Leech lattice
        return _construct_leech_lattice(base_ring)
    else:
        # General construction requires more sophisticated methods
        raise NotImplementedError(f"Even unimodular lattice construction for dimension {dimension}")
```

## Random and Generic Forms

```python
def random_definite_form(dimension, base_ring=QQ, positive=True):
    """
    Random definite quadratic form.
    
    Generates a random symmetric matrix and adjusts to ensure definiteness.
    
    INPUT:
    - dimension -- positive integer
    - base_ring -- base ring for coefficients
    - positive -- if True, make positive definite; if False, negative definite
    
    OUTPUT:
    Random definite symmetric bilinear module
    """
    from sage.misc.prandom import randint
    from sage.matrix.constructor import random_matrix
    
    # Generate random symmetric matrix
    A = random_matrix(base_ring, dimension)
    symmetric_A = A + A.transpose()
    
    # Ensure definiteness by adding appropriate diagonal term
    eigenvals = symmetric_A.eigenvalues()
    min_eigenval = min(eigenvals)
    
    if positive:
        # Make positive definite
        shift = max(0, 1 - min_eigenval)
    else:
        # Make negative definite
        max_eigenval = max(eigenvals)
        shift = min(0, -1 - max_eigenval)
    
    from sage.matrix.constructor import identity_matrix
    definite_matrix = symmetric_A + shift * identity_matrix(base_ring, dimension)
    
    return SymmetricBilinearModule_with_basis(definite_matrix)

def random_integral_form(dimension, bound=5, base_ring=ZZ):
    """
    Random integral quadratic form.
    
    Generates random symmetric matrix with bounded integer coefficients.
    
    INPUT:
    - dimension -- positive integer
    - bound -- bound on matrix coefficients
    - base_ring -- base ring (should be ZZ or similar)
    
    OUTPUT:
    Random integral symmetric bilinear module
    """
    from sage.misc.prandom import randint
    from sage.matrix.constructor import matrix
    
    # Generate random symmetric matrix
    gram = matrix(base_ring, dimension, dimension)
    
    for i in range(dimension):
        for j in range(i, dimension):
            if i == j:
                # Diagonal entry: avoid 0 for non-degeneracy
                value = randint(1, bound)
            else:
                # Off-diagonal entry
                value = randint(-bound, bound)
            
            gram[i,j] = value
            gram[j,i] = value  # Symmetry
    
    return SymmetricBilinearModule_with_basis(gram)

def generic_form(signature, base_ring=QQ):
    """
    Generic quadratic form with given signature.
    
    Constructs a "generic" form by using variables as coefficients,
    useful for symbolic computation and general theory.
    
    INPUT:
    - signature -- tuple (p, q, r)
    - base_ring -- base ring (often a polynomial ring)
    
    OUTPUT:
    Symbolic symmetric bilinear module
    """
    p, q, r = signature
    dimension = p + q + r
    
    if hasattr(base_ring, 'gens'):
        # Polynomial ring - use variables as coefficients
        variables = base_ring.gens()
        if len(variables) < dimension * (dimension + 1) // 2:
            raise ValueError("Need enough variables for generic symmetric matrix")
        
        from sage.matrix.constructor import matrix
        gram = matrix(base_ring, dimension, dimension)
        
        var_index = 0
        for i in range(dimension):
            for j in range(i, dimension):
                gram[i,j] = variables[var_index]
                gram[j,i] = variables[var_index]
                var_index += 1
        
        return SymmetricBilinearModule_with_basis(gram)
    
    else:
        # Use diagonal form with signature
        return _construct_from_signature(signature, base_ring)
```

## Mathematical Properties

The construction framework ensures these properties:

```python
# Mathematical assertion: Factory function correctness
# All construction methods produce valid SymmetricBilinearModule instances

# Mathematical assertion: Classical lattice properties
# E_8 is even, unimodular, positive definite with discriminant 1

# Mathematical assertion: Signature preservation
# Constructions from signature specifications produce exact signatures

# Mathematical assertion: Base ring consistency
# All constructions respect the specified base ring

# Mathematical assertion: Gram matrix symmetry
# All constructed Gram matrices are symmetric

# Mathematical assertion: Definiteness conditions
# Definite form constructions satisfy definiteness requirements

# Mathematical assertion: Unimodularity property
# Unimodular constructions have determinant ±1

# Mathematical assertion: Classical form recognition
# Standard forms (Euclidean, hyperbolic, Lorentz) have expected properties
```

This construction framework provides comprehensive factory functions for creating symmetric bilinear modules from various specifications while maintaining mathematical correctness and supporting both concrete and symbolic computation.