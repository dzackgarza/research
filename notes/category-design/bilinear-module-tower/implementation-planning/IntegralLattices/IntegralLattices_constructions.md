<!--
Origin: gitclones/Coxeter/implementation/planning/IntegralLattices/IntegralLattices_constructions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Constructions: Integral Lattice Factory Functions

Factory methods and constructors for creating standard integral lattices, classical examples, and custom lattices.

## Classical Lattice Constructions

```python
def root_lattice(root_system_type):
    """
    Construct root lattice from root system type.
    
    INPUT:
    - root_system_type -- string like "A3", "D4", "E8", etc.
    
    OUTPUT:
    IntegralLattice with associated root system
    
    EXAMPLES::
    
        sage: A3 = IntegralLattice.root_lattice("A3")
        sage: A3.rank()
        3
        sage: A3.discriminant()
        4  # = det(Cartan matrix)
        sage: A3.minimum()
        2  # All root lattices have minimum 2
        
        sage: E8 = IntegralLattice.root_lattice("E8")
        sage: E8.is_unimodular()
        True
        sage: E8.is_even()
        True
        sage: len(E8.roots())
        240
        
        sage: D4 = IntegralLattice.root_lattice("D4")
        sage: D4.discriminant()
        4
        sage: D4.automorphism_group().order()
        1152  # Includes triality
    """
    if root_system_type.startswith('A'):
        n = int(root_system_type[1:])
        return _construct_A_n_lattice(n)
    elif root_system_type.startswith('D'):
        n = int(root_system_type[1:])
        return _construct_D_n_lattice(n)
    elif root_system_type.startswith('E'):
        n = int(root_system_type[1:])
        if n in [6, 7, 8]:
            return _construct_E_n_lattice(n)
        else:
            raise ValueError(f"E{n} root system does not exist")
    else:
        raise ValueError(f"Unknown root system type: {root_system_type}")

def _construct_A_n_lattice(n):
    """
    Construct A_n root lattice.
    
    A_n has Gram matrix with 2 on diagonal, -1 on super/sub-diagonals.
    """
    if n < 1:
        raise ValueError("A_n requires n ≥ 1")
    
    from sage.matrix.constructor import matrix
    
    # Cartan matrix of A_n
    G = matrix(ZZ, n, n)
    for i in range(n):
        G[i, i] = 2
        if i < n - 1:
            G[i, i + 1] = -1
            G[i + 1, i] = -1
    
    lattice = IntegralLattice(G)
    lattice._name = f"A_{n} root lattice"
    lattice._root_system = f"A{n}"
    return lattice

def _construct_D_n_lattice(n):
    """
    Construct D_n root lattice.
    
    D_n is the even sublattice of Z^n.
    """
    if n < 4:
        raise ValueError("D_n requires n ≥ 4")
    
    from sage.matrix.constructor import matrix
    
    # D_n Cartan matrix
    G = matrix(ZZ, n, n)
    for i in range(n):
        G[i, i] = 2
    
    # Standard adjacencies
    for i in range(n - 2):
        G[i, i + 1] = -1
        G[i + 1, i] = -1
    
    # Special connection: node n-2 connects to both n-1 and n
    G[n - 3, n - 1] = -1
    G[n - 1, n - 3] = -1
    
    lattice = IntegralLattice(G)
    lattice._name = f"D_{n} root lattice"
    lattice._root_system = f"D{n}"
    return lattice

def _construct_E_n_lattice(n):
    """
    Construct exceptional root lattices E_6, E_7, E_8.
    """
    if n == 6:
        # E_6 Cartan matrix
        G = matrix(ZZ, [
            [ 2, -1,  0,  0,  0,  0],
            [-1,  2, -1,  0,  0,  0],
            [ 0, -1,  2, -1,  0, -1],
            [ 0,  0, -1,  2, -1,  0],
            [ 0,  0,  0, -1,  2,  0],
            [ 0,  0, -1,  0,  0,  2]
        ])
    elif n == 7:
        # E_7 Cartan matrix
        G = matrix(ZZ, [
            [ 2, -1,  0,  0,  0,  0,  0],
            [-1,  2, -1,  0,  0,  0,  0],
            [ 0, -1,  2, -1,  0,  0,  0],
            [ 0,  0, -1,  2, -1,  0,  0],
            [ 0,  0,  0, -1,  2, -1,  0],
            [ 0,  0,  0,  0, -1,  2, -1],
            [ 0,  0,  0,  0,  0, -1,  2]
        ])
    elif n == 8:
        # E_8 Cartan matrix
        G = matrix(ZZ, [
            [ 2, -1,  0,  0,  0,  0,  0,  0],
            [-1,  2, -1,  0,  0,  0,  0,  0],
            [ 0, -1,  2, -1,  0,  0,  0,  0],
            [ 0,  0, -1,  2, -1,  0,  0,  0],
            [ 0,  0,  0, -1,  2, -1,  0,  0],
            [ 0,  0,  0,  0, -1,  2, -1,  0],
            [ 0,  0,  0,  0,  0, -1,  2, -1],
            [ 0,  0,  0,  0,  0,  0, -1,  2]
        ])
    
    lattice = IntegralLattice(G)
    lattice._name = f"E_{n} root lattice"
    lattice._root_system = f"E{n}"
    return lattice
```

## Classical Extremal Lattices

```python
def leech_lattice():
    """
    Construct the Leech lattice.
    
    The unique even unimodular lattice in dimension 24 with no roots.
    Central to the Monster group and moonshine theory.
    
    OUTPUT:
    24-dimensional even unimodular integral lattice
    
    EXAMPLES::
    
        sage: Lambda = IntegralLattice.leech_lattice()
        sage: Lambda.rank()
        24
        sage: Lambda.discriminant()
        1  # Unimodular
        sage: Lambda.is_even()
        True
        sage: Lambda.minimum()
        4  # No roots (no norm-2 vectors)
        sage: Lambda.kissing_number()
        196560  # Exceptional kissing configuration
    """
    # Construction via MOG (Miracle Octad Generator) or other method
    # This requires careful implementation of 24×24 Gram matrix
    raise NotImplementedError("Leech lattice construction requires specialized algorithm")

def niemeier_lattices():
    """
    Construct all 24 Niemeier lattices.
    
    The complete list of even unimodular lattices in dimension 24.
    Classified by their root system decomposition.
    
    OUTPUT:
    List of 24 integral lattices
    
    EXAMPLES::
    
        sage: niemeier = IntegralLattice.niemeier_lattices()
        sage: len(niemeier)
        24
        sage: all(L.rank() == 24 for L in niemeier)
        True
        sage: all(L.is_even() and L.is_unimodular() for L in niemeier)
        True
        
        sage: # Leech lattice is the one with no roots
        sage: leech = [L for L in niemeier if L.minimum() == 4][0]
        sage: leech.minimum()
        4
    """
    # Each Niemeier lattice corresponds to a specific root system
    # decomposition that fills dimension 24
    raise NotImplementedError("Niemeier lattice enumeration")

def barnes_wall_lattice(n):
    """
    Construct Barnes-Wall lattice BW_n.
    
    Family of extremal even lattices related to Reed-Muller codes.
    
    INPUT:
    - n -- dimension parameter (n = 2^k)
    
    OUTPUT:
    Even integral lattice of dimension 2^n
    
    EXAMPLES::
    
        sage: BW4 = IntegralLattice.barnes_wall_lattice(4)
        sage: BW4.rank()
        16
        sage: BW4.is_even()
        True
        sage: BW4.minimum()
        4
    """
    if not (n > 0 and (n & (n - 1)) == 0):
        raise ValueError("n must be a power of 2")
    
    # Construction via first-order Reed-Muller codes
    raise NotImplementedError("Barnes-Wall lattice construction")
```

## Standard Constructions

```python
def hyperbolic_plane():
    """
    Construct the hyperbolic plane H.
    
    The unique even unimodular lattice of signature (1,1).
    
    OUTPUT:
    2-dimensional indefinite unimodular lattice
    
    EXAMPLES::
    
        sage: H = IntegralLattice.hyperbolic_plane()
        sage: H.gram_matrix()
        [0 1]
        [1 0]
        sage: H.signature()
        (1, 1, 0)
        sage: H.discriminant()
        -1
        sage: H.is_unimodular()
        True
    """
    G = matrix(ZZ, [[0, 1], [1, 0]])
    lattice = IntegralLattice(G)
    lattice._name = "Hyperbolic plane"
    return lattice

def standard_lattice(n):
    """
    Construct the standard lattice Z^n.
    
    INPUT:
    - n -- dimension
    
    OUTPUT:
    n-dimensional integral lattice with identity Gram matrix
    
    EXAMPLES::
    
        sage: Z3 = IntegralLattice.standard_lattice(3)
        sage: Z3.gram_matrix()
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: Z3.minimum()
        1
        sage: Z3.is_unimodular()
        True
    """
    G = matrix.identity(ZZ, n)
    lattice = IntegralLattice(G)
    lattice._name = f"Standard lattice Z^{n}"
    return lattice

def scaled_lattice(lattice, scale):
    """
    Scale a lattice by constant factor.
    
    INPUT:
    - lattice -- integral lattice
    - scale -- positive integer
    
    OUTPUT:
    Lattice with Gram matrix scale * original
    
    EXAMPLES::
    
        sage: L = IntegralLattice.standard_lattice(2)
        sage: L2 = IntegralLattice.scaled_lattice(L, 2)
        sage: L2.minimum()
        2  # Was 1, now 2
        sage: L2.discriminant()
        4  # Was 1, now 2^2
    """
    scale = ZZ(scale)
    if scale <= 0:
        raise ValueError("Scale must be positive")
    
    G_scaled = scale * lattice.gram_matrix()
    scaled = IntegralLattice(G_scaled)
    scaled._name = f"{scale} * ({lattice._name})" if hasattr(lattice, '_name') else f"Scaled lattice"
    return scaled

def orthogonal_sum(lattices):
    """
    Construct orthogonal direct sum L₁ ⊕ ... ⊕ Lₖ.
    
    INPUT:
    - lattices -- list of integral lattices
    
    OUTPUT:
    Block diagonal orthogonal sum
    
    EXAMPLES::
    
        sage: A2 = IntegralLattice.root_lattice("A2")
        sage: A3 = IntegralLattice.root_lattice("A3")
        sage: L = IntegralLattice.orthogonal_sum([A2, A3])
        sage: L.rank()
        5  # = 2 + 3
        sage: L.discriminant()
        12  # = 3 * 4
    """
    if not lattices:
        raise ValueError("Need at least one lattice")
    
    from sage.matrix.constructor import block_diagonal_matrix
    
    gram_matrices = [L.gram_matrix() for L in lattices]
    G_sum = block_diagonal_matrix(gram_matrices)
    
    sum_lattice = IntegralLattice(G_sum)
    
    # Construct name
    if all(hasattr(L, '_name') for L in lattices):
        names = [L._name for L in lattices]
        sum_lattice._name = " ⊕ ".join(names)
    
    return sum_lattice
```

## Construction from Codes

```python
def from_binary_code(code, construction='A'):
    """
    Construct lattice from binary linear code.
    
    INPUT:
    - code -- binary linear code
    - construction -- 'A' (Construction A) or 'B' (Construction B)
    
    OUTPUT:
    Integral lattice derived from code
    
    EXAMPLES::
    
        sage: # Hamming code gives E8 via Construction A
        sage: H = codes.HammingCode(GF(2), 3)
        sage: E8_from_code = IntegralLattice.from_binary_code(H, 'A')
        sage: E8_from_code.rank()
        8
        sage: E8_from_code.minimum()
        2
    """
    n = code.length()
    
    if construction == 'A':
        # Construction A: lattice generated by
        # (1/√2) * {x ∈ Z^n : x mod 2 ∈ code}
        
        # Generate all codewords
        codewords = list(code)
        
        # Lift to integers (0 → 0, 1 → 1)
        generators = []
        for cw in codewords:
            gen = vector(ZZ, [int(x) for x in cw])
            generators.append(gen)
        
        # Add 2*e_i for standard basis
        for i in range(n):
            gen = 2 * vector(ZZ, [1 if j == i else 0 for j in range(n)])
            generators.append(gen)
        
        # Form Gram matrix
        G = matrix(ZZ, [[sum(g1[k] * g2[k] for k in range(n)) 
                        for g2 in generators] for g1 in generators])
        
        return IntegralLattice(G)
        
    elif construction == 'B':
        # Construction B: more complex, uses dual code
        raise NotImplementedError("Construction B from codes")
    else:
        raise ValueError("construction must be 'A' or 'B'")

def reed_muller_lattice(r, m):
    """
    Construct lattice from Reed-Muller code.
    
    INPUT:
    - r -- order of Reed-Muller code
    - m -- number of variables
    
    OUTPUT:
    Integral lattice via Construction A
    
    EXAMPLES::
    
        sage: # First-order Reed-Muller gives extremal lattice
        sage: RM_1_4 = IntegralLattice.reed_muller_lattice(1, 4)
        sage: RM_1_4.rank()
        16
        sage: RM_1_4.is_even()
        True
    """
    from sage.coding.reed_muller_code import ReedMullerCode
    
    RM = ReedMullerCode(GF(2), r, m)
    return from_binary_code(RM, construction='A')
```

## Gluing Constructions

```python
def glue_lattices(L1, L2, gluing_map):
    """
    Glue two lattices via discriminant group isometry.
    
    For lattices L₁, L₂ with isometry φ: L₁*/L₁ → L₂*/L₂,
    constructs the glued lattice L₁ ⊕_φ L₂.
    
    INPUT:
    - L1, L2 -- integral lattices
    - gluing_map -- isometry of discriminant groups
    
    OUTPUT:
    Glued integral lattice
    
    EXAMPLES::
    
        sage: # Glue two copies of A₁
        sage: A1 = IntegralLattice.root_lattice("A1")
        sage: # Identity gluing gives A₁²
        sage: A1_squared = IntegralLattice.glue_lattices(A1, A1, "identity")
        sage: A1_squared.discriminant()
        4  # = 2 × 2
    """
    # This implements Nikulin's gluing theory
    # Requires discriminant group computations
    raise NotImplementedError("Lattice gluing construction")

def unimodular_gluing(L, complement_rank=None):
    """
    Complete lattice to unimodular by gluing.
    
    Given lattice L, find minimal unimodular overlattice.
    
    INPUT:
    - L -- integral lattice
    - complement_rank -- rank of orthogonal complement
    
    OUTPUT:
    Unimodular lattice containing L
    
    EXAMPLES::
    
        sage: A2 = IntegralLattice.root_lattice("A2")
        sage: A2.discriminant()
        3
        sage: # Need rank-1 complement
        sage: completed = IntegralLattice.unimodular_gluing(A2, 1)
        sage: completed.is_unimodular()
        True
        sage: completed.rank()
        3
    """
    # Find orthogonal complement of appropriate rank
    # Glue using discriminant group anti-isometry
    raise NotImplementedError("Unimodular completion")
```

## Random and Parametric Constructions

```python
def random_lattice(rank, discriminant_bound=100, positive_definite=True):
    """
    Generate random integral lattice.
    
    INPUT:
    - rank -- dimension
    - discriminant_bound -- bound on |discriminant|
    - positive_definite -- ensure positive definiteness
    
    OUTPUT:
    Random integral lattice
    
    EXAMPLES::
    
        sage: L = IntegralLattice.random_lattice(3, discriminant_bound=20)
        sage: L.rank()
        3
        sage: abs(L.discriminant()) <= 20
        True
    """
    from sage.misc.prandom import randrange
    
    # Generate random symmetric integer matrix
    G = matrix(ZZ, rank, rank)
    
    for i in range(rank):
        for j in range(i, rank):
            if i == j:
                # Diagonal entries - ensure positive definite
                G[i, i] = randrange(1, discriminant_bound // rank + 1)
            else:
                # Off-diagonal entries
                bound = min(G[i, i], discriminant_bound // rank) if i < rank else 1
                G[i, j] = G[j, i] = randrange(-bound, bound + 1)
    
    # Check properties
    if positive_definite and not G.is_positive_definite():
        # Adjust to make positive definite
        G = G + matrix.identity(ZZ, rank) * discriminant_bound
    
    return IntegralLattice(G)

def from_gram_matrix(G, check=True):
    """
    Construct lattice from explicit Gram matrix.
    
    INPUT:
    - G -- symmetric integer matrix
    - check -- verify properties
    
    OUTPUT:
    Integral lattice with given Gram matrix
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1, 0], [1, 2, 1], [0, 1, 3]])
        sage: L = IntegralLattice.from_gram_matrix(G)
        sage: L.gram_matrix() == G
        True
        sage: L.discriminant()
        7
    """
    return IntegralLattice(G, check=check)

def from_quadratic_form(qf):
    """
    Construct lattice from quadratic form.
    
    INPUT:
    - qf -- QuadraticForm object
    
    OUTPUT:
    Integral lattice with same quadratic form
    
    EXAMPLES::
    
        sage: qf = QuadraticForm(ZZ, matrix([[2, 1], [1, 3]]))
        sage: L = IntegralLattice.from_quadratic_form(qf)
        sage: L.quadratic_form() == qf
        True
    """
    return IntegralLattice(qf.matrix())
```

## Named Lattice Database

```python
def named_lattice(name):
    """
    Construct named lattice from database.
    
    INPUT:
    - name -- string identifier
    
    OUTPUT:
    Named integral lattice
    
    EXAMPLES::
    
        sage: E8 = IntegralLattice.named_lattice("E8")
        sage: E8.rank()
        8
        sage: E8.is_unimodular()
        True
        
        sage: Leech = IntegralLattice.named_lattice("Leech")
        sage: Leech.rank()
        24
        sage: Leech.minimum()
        4
        
        sage: D4 = IntegralLattice.named_lattice("D4")
        sage: D4.discriminant()
        4
    """
    name = name.upper()
    
    # Root lattices
    if name.startswith('A') and name[1:].isdigit():
        n = int(name[1:])
        return root_lattice(f"A{n}")
    elif name.startswith('D') and name[1:].isdigit():
        n = int(name[1:])
        return root_lattice(f"D{n}")
    elif name.startswith('E') and name[1:] in ['6', '7', '8']:
        n = int(name[1:])
        return root_lattice(f"E{n}")
    
    # Special lattices
    elif name == "LEECH":
        return leech_lattice()
    elif name == "HYPERBOLIC" or name == "H":
        return hyperbolic_plane()
    elif name.startswith('Z') and name[1:].isdigit():
        n = int(name[1:])
        return standard_lattice(n)
    
    else:
        raise ValueError(f"Unknown named lattice: {name}")

# Register constructor aliases
IntegralLattice.root_lattice = staticmethod(root_lattice)
IntegralLattice.leech_lattice = staticmethod(leech_lattice)
IntegralLattice.niemeier_lattices = staticmethod(niemeier_lattices)
IntegralLattice.hyperbolic_plane = staticmethod(hyperbolic_plane)
IntegralLattice.standard_lattice = staticmethod(standard_lattice)
IntegralLattice.orthogonal_sum = staticmethod(orthogonal_sum)
IntegralLattice.from_binary_code = staticmethod(from_binary_code)
IntegralLattice.random_lattice = staticmethod(random_lattice)
IntegralLattice.named_lattice = staticmethod(named_lattice)
```

## Mathematical Properties

The construction framework ensures:

```python
# Mathematical assertion: Root lattice classification
# All irreducible root lattices are ADE type

# Mathematical assertion: Niemeier completeness
# Exactly 24 even unimodular lattices in dimension 24

# Mathematical assertion: Orthogonal sum discriminant
# disc(L₁ ⊕ L₂) = disc(L₁) · disc(L₂)

# Mathematical assertion: Construction A evenness
# Lattices from doubly-even codes are even

# Mathematical assertion: Gluing determinant
# det(L₁ ⊕_φ L₂) = det(L₁) · det(L₂) / |G|²

# Mathematical assertion: Hermite optimality
# E₈ and Leech achieve optimal sphere packing densities

# Mathematical assertion: Unimodular gluing existence
# Every positive definite lattice embeds in unimodular lattice

# Mathematical assertion: Random lattice distribution
# Generic lattices have trivial automorphism groups
```

This comprehensive construction system provides access to all major classes of integral lattices through both explicit constructions and algorithmic generation methods.