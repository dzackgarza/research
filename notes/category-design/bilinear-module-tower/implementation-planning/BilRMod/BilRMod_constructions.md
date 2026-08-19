<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_constructions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Constructions: Bilinear Module Factory Functions

Factory functions and standard constructions for bilinear modules.

## Primary Constructor

```python
def BilinearModule(gram_matrix, base_ring=None, basis=None, category=None, **kwds):
    """
    Construct a bilinear module from a Gram matrix.
    
    This is the primary factory function for creating bilinear modules.
    It provides pattern matching and intelligent defaults for various
    input formats.
    
    INPUT:
    - gram_matrix -- square matrix defining the bilinear form
    - base_ring -- base ring (inferred from matrix if not given)
    - basis -- basis element names (defaults to indexed names)
    - category -- category (defaults to appropriate BilinearModules category)
    
    OUTPUT:
    BilinearModule_with_basis object
    
    EXAMPLES::
    
        sage: # From integer matrix
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M
        Bilinear module of rank 2 over Integer Ring
        sage: M.discriminant()
        5
        
        sage: # With custom basis names
        sage: M = BilinearModule(G, basis=['x', 'y'])
        sage: x, y = M.gens()
        sage: M.bilinear_form(x, y)
        1
        
        sage: # Positive definite over rationals
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: M.is_positive_definite()
        True
    """
    # Validate input
    if not hasattr(gram_matrix, 'is_square') or not gram_matrix.is_square():
        raise ValueError("Gram matrix must be square")
    
    # Infer base ring
    if base_ring is None:
        base_ring = gram_matrix.base_ring()
    
    # Determine appropriate category based on form properties
    if category is None:
        category = _infer_bilinear_category(gram_matrix, base_ring)
    
    # Create the bilinear module
    return BilinearModule_with_basis(
        gram_matrix=gram_matrix,
        basis=basis,
        category=category,
        **kwds
    )

def _infer_bilinear_category(gram_matrix, base_ring):
    """
    Infer the most specific category for a bilinear form.
    
    Analyzes the Gram matrix properties to determine axioms.
    """
    from sage.categories.bilinear_modules import BilinearModules
    
    # Start with base category
    category = BilinearModules(base_ring).WithBasis()
    
    # Check for special properties
    G = gram_matrix
    
    # Symmetry properties
    if G == G.transpose():
        category = category.Symmetric()
        
        # Definiteness (only for symmetric forms over ordered fields)
        if hasattr(base_ring, 'is_ordered') and base_ring.is_ordered():
            eigenvals = G.eigenvalues()
            if all(ev > 0 for ev in eigenvals):
                category = category.PositiveDefinite()
            elif all(ev < 0 for ev in eigenvals):
                category = category.NegativeDefinite()
            elif any(ev > 0 for ev in eigenvals) and any(ev < 0 for ev in eigenvals):
                category = category.Indefinite()
    
    elif G == -G.transpose():
        category = category.SkewSymmetric()
        
        # Check for alternating property
        if all(G[i,i] == 0 for i in range(G.nrows())):
            category = category.Alternating()
    
    # Non-degeneracy
    if G.determinant() != 0:
        category = category.Nondegenerate()
    
    return category
```

## Standard Constructions

```python
def HyperbolicPlane(base_ring=ZZ):
    """
    Construct the hyperbolic plane.
    
    The hyperbolic plane is the rank-2 bilinear module with Gram matrix
    [[0, 1], [1, 0]]. It has signature (1, 1, 0) and is the fundamental
    indefinite bilinear form.
    
    INPUT:
    - base_ring -- base ring (default: ZZ)
    
    OUTPUT:
    BilinearModule representing the hyperbolic plane
    
    EXAMPLES::
    
        sage: H = HyperbolicPlane(QQ)
        sage: H.signature()
        (1, 1, 0)
        sage: H.discriminant()
        -1
        sage: H.is_indefinite()
        True
        
        sage: # Standard basis elements
        sage: e, f = H.gens()
        sage: H.bilinear_form(e, e)
        0
        sage: H.bilinear_form(f, f)
        0
        sage: H.bilinear_form(e, f)
        1
    """
    from sage.matrix.constructor import matrix
    G = matrix(base_ring, [[0, 1], [1, 0]])
    return BilinearModule(G, basis=['e', 'f'])

def StandardInnerProduct(n, base_ring=QQ):
    """
    Construct standard Euclidean inner product space.
    
    This is the positive definite bilinear form with Gram matrix
    equal to the identity matrix.
    
    INPUT:
    - n -- dimension
    - base_ring -- base ring (default: QQ)
    
    OUTPUT:
    BilinearModule representing Euclidean n-space
    
    EXAMPLES::
    
        sage: E3 = StandardInnerProduct(3)
        sage: E3.is_positive_definite()
        True
        sage: E3.signature()
        (3, 0, 0)
        
        sage: # Orthonormal basis
        sage: e1, e2, e3 = E3.gens()
        sage: E3.bilinear_form(e1, e2)
        0
        sage: E3.bilinear_form(e1, e1)
        1
    """
    from sage.matrix.constructor import identity_matrix
    G = identity_matrix(base_ring, n)
    basis = [f'e{i+1}' for i in range(n)]
    return BilinearModule(G, basis=basis)

def MinkowskiSpace(n, base_ring=QQ):
    """
    Construct Minkowski spacetime.
    
    Signature (n-1, 1, 0) with Gram matrix diag(1, 1, ..., 1, -1).
    Used in special relativity for n=4.
    
    INPUT:
    - n -- dimension (spacetime dimension)
    - base_ring -- base ring (default: QQ)
    
    OUTPUT:
    BilinearModule representing Minkowski space
    
    EXAMPLES::
    
        sage: # 4D Minkowski spacetime
        sage: M4 = MinkowskiSpace(4)
        sage: M4.signature()
        (3, 1, 0)
        sage: M4.is_indefinite()
        True
        
        sage: # Light cone vectors
        sage: t, x, y, z = M4.gens()
        sage: light_like = t + x  # Light ray
        sage: light_like.is_isotropic()
        True
    """
    from sage.matrix.constructor import diagonal_matrix
    diagonal_entries = [1] * (n-1) + [-1]
    G = diagonal_matrix(base_ring, diagonal_entries)
    basis = ['t'] + [f'x{i}' for i in range(1, n)]
    return BilinearModule(G, basis=basis)

def SymplecticForm(n, base_ring=QQ):
    """
    Construct standard symplectic form.
    
    Creates the canonical skew-symmetric bilinear form on R^(2n)
    with Gram matrix consisting of 2×2 blocks [[0,1],[-1,0]].
    
    INPUT:
    - n -- half the dimension (dimension is 2n)
    - base_ring -- base ring (default: QQ)
    
    OUTPUT:
    BilinearModule representing symplectic 2n-space
    
    EXAMPLES::
    
        sage: # Symplectic 4-space
        sage: S = SymplecticForm(2)
        sage: S.dimension()
        4
        sage: S.is_skew_symmetric()
        True
        sage: S.discriminant()
        1
        
        sage: # Symplectic basis
        sage: p1, q1, p2, q2 = S.gens()
        sage: S.bilinear_form(p1, q1)
        1
        sage: S.bilinear_form(p1, p2)
        0
    """
    from sage.matrix.constructor import block_diagonal_matrix, matrix
    
    # 2×2 symplectic block
    J = matrix(base_ring, [[0, 1], [-1, 0]])
    
    # Create block diagonal matrix with n copies of J
    G = block_diagonal_matrix([J] * n)
    
    # Create basis names
    basis = []
    for i in range(n):
        basis.extend([f'p{i+1}', f'q{i+1}'])
    
    return BilinearModule(G, basis=basis)

def DiagonalBilinearForm(diagonal_entries, base_ring=None):
    """
    Construct diagonal bilinear form.
    
    Creates bilinear form with diagonal Gram matrix.
    
    INPUT:
    - diagonal_entries -- list of diagonal values
    - base_ring -- base ring (inferred if not given)
    
    OUTPUT:
    BilinearModule with diagonal form
    
    EXAMPLES::
    
        sage: # Mixed signature form
        sage: B = DiagonalBilinearForm([1, -1, 2, -3])
        sage: B.signature()
        (2, 2, 0)
        sage: B.is_indefinite()
        True
        
        sage: # Degenerate form
        sage: D = DiagonalBilinearForm([1, 0, -1])
        sage: D.is_degenerate()
        True
        sage: D.signature()
        (1, 1, 1)
    """
    from sage.matrix.constructor import diagonal_matrix
    
    if base_ring is None:
        # Infer base ring from entries
        from sage.structure.sequence import Sequence
        base_ring = Sequence(diagonal_entries).universe()
    
    G = diagonal_matrix(base_ring, diagonal_entries)
    n = len(diagonal_entries)
    basis = [f'e{i+1}' for i in range(n)]
    
    return BilinearModule(G, basis=basis)
```

## Lattice Constructions

```python
def IntegerLattice(gram_matrix):
    """
    Construct integer lattice with given Gram matrix.
    
    This is a bilinear module over ZZ, representing a lattice
    in Euclidean space with the given inner product.
    
    INPUT:
    - gram_matrix -- symmetric positive definite integer matrix
    
    OUTPUT:
    BilinearModule over ZZ
    
    EXAMPLES::
    
        sage: # Root lattice A₂
        sage: G = matrix(ZZ, [[2, -1], [-1, 2]])
        sage: A2 = IntegerLattice(G)
        sage: A2.discriminant()
        3
        sage: A2.is_positive_definite()
        True
    """
    if gram_matrix.base_ring() != ZZ:
        gram_matrix = gram_matrix.change_ring(ZZ)
    
    return BilinearModule(gram_matrix, base_ring=ZZ)

def RootLattice(cartan_type):
    """
    Construct root lattice for given Cartan type.
    
    INPUT:
    - cartan_type -- Cartan type (e.g., 'A3', 'D4', 'E8')
    
    OUTPUT:
    BilinearModule representing the root lattice
    
    EXAMPLES::
    
        sage: # A₃ root lattice
        sage: A3 = RootLattice('A3')
        sage: A3.rank()
        3
        sage: A3.discriminant()
        4
    """
    from sage.combinat.root_system.cartan_type import CartanType
    from sage.combinat.root_system.root_system import RootSystem
    
    ct = CartanType(cartan_type)
    root_system = RootSystem(ct)
    
    # Get Cartan matrix (this is the Gram matrix for simple roots)
    cartan_matrix = root_system.cartan_matrix()
    
    return IntegerLattice(cartan_matrix)

def WeightLattice(cartan_type):
    """
    Construct weight lattice for given Cartan type.
    
    The weight lattice is dual to the root lattice.
    
    INPUT:
    - cartan_type -- Cartan type
    
    OUTPUT:
    BilinearModule representing the weight lattice
    """
    from sage.combinat.root_system.cartan_type import CartanType
    from sage.combinat.root_system.root_system import RootSystem
    
    ct = CartanType(cartan_type)
    root_system = RootSystem(ct)
    
    # Weight lattice has Gram matrix as inverse of Cartan matrix
    cartan_matrix = root_system.cartan_matrix()
    weight_gram = cartan_matrix.inverse()
    
    return BilinearModule(weight_gram, base_ring=QQ)
```

## Random and Special Constructions

```python
def RandomBilinearModule(n, base_ring=QQ, form_type='general', **kwds):
    """
    Construct random bilinear module for testing.
    
    INPUT:
    - n -- dimension
    - base_ring -- base ring
    - form_type -- 'symmetric', 'skew_symmetric', 'general'
    
    OUTPUT:
    Random BilinearModule
    
    EXAMPLES::
    
        sage: # Random symmetric form
        sage: M = RandomBilinearModule(3, form_type='symmetric')
        sage: M.is_symmetric()
        True
        sage: M.rank()
        3
    """
    from sage.matrix.constructor import random_matrix
    
    if form_type == 'symmetric':
        # Generate random symmetric matrix
        A = random_matrix(base_ring, n, n, **kwds)
        G = A + A.transpose()
    elif form_type == 'skew_symmetric':
        # Generate random skew-symmetric matrix
        A = random_matrix(base_ring, n, n, **kwds)
        G = A - A.transpose()
    else:  # general
        G = random_matrix(base_ring, n, n, **kwds)
    
    return BilinearModule(G)

def ZeroBilinearModule(n, base_ring=ZZ):
    """
    Construct zero bilinear form.
    
    INPUT:
    - n -- dimension
    - base_ring -- base ring
    
    OUTPUT:
    BilinearModule with zero Gram matrix
    
    EXAMPLES::
    
        sage: Z = ZeroBilinearModule(3)
        sage: Z.is_degenerate()
        True
        sage: Z.radical().dimension()
        3
    """
    from sage.matrix.constructor import zero_matrix
    G = zero_matrix(base_ring, n)
    return BilinearModule(G)

def HyperbolicSpace(signature, base_ring=QQ):
    """
    Construct hyperbolic space with given signature.
    
    Creates indefinite form that's a sum of hyperbolic planes
    plus additional positive/negative definite parts.
    
    INPUT:
    - signature -- tuple (p, q, r) for signature
    - base_ring -- base ring
    
    OUTPUT:
    BilinearModule with specified signature
    
    EXAMPLES::
    
        sage: # Signature (2,2,0) - two hyperbolic planes
        sage: H = HyperbolicSpace((2, 2, 0))
        sage: H.signature()
        (2, 2, 0)
        sage: H.rank()
        4
    """
    p, q, r = signature
    total_dim = p + q + r
    
    # Construct diagonal matrix with appropriate signature
    diagonal = [1] * p + [-1] * q + [0] * r
    
    from sage.matrix.constructor import diagonal_matrix
    G = diagonal_matrix(base_ring, diagonal)
    
    return BilinearModule(G, basis=[f'e{i+1}' for i in range(total_dim)])
```

## Factory Integration

```python
class BilinearModuleCategoryFactory:
    """
    Factory for constructing bilinear modules with category inference.
    
    Provides intelligent construction based on mathematical properties
    and integrates with the SageMath category framework.
    """
    
    @staticmethod
    def from_gram_matrix(gram_matrix, **kwds):
        """Primary construction method."""
        return BilinearModule(gram_matrix, **kwds)
    
    @staticmethod  
    def from_quadratic_form(quadratic_matrix, **kwds):
        """
        Construct from quadratic form matrix.
        
        The quadratic form Q(x) = x^T * A * x gives rise to
        bilinear form B(x,y) = (Q(x+y) - Q(x) - Q(y))/2.
        For characteristic ≠ 2, this is B(x,y) = x^T * (A + A^T) * y / 2.
        """
        base_ring = quadratic_matrix.base_ring()
        
        if base_ring.characteristic() == 2:
            # In characteristic 2, different relationship
            gram_matrix = quadratic_matrix
        else:
            # Standard case: symmetrize
            gram_matrix = (quadratic_matrix + quadratic_matrix.transpose()) / 2
        
        return BilinearModule(gram_matrix, **kwds)
    
    @staticmethod
    def from_basis_and_form(basis_elements, form_function, **kwds):
        """
        Construct from basis elements and bilinear form function.
        
        INPUT:
        - basis_elements -- list of symbolic basis elements
        - form_function -- function b(v, w) defining bilinear form
        """
        n = len(basis_elements)
        base_ring = kwds.get('base_ring', QQ)
        
        # Compute Gram matrix
        from sage.matrix.constructor import matrix
        G = matrix(base_ring, n, n)
        for i in range(n):
            for j in range(n):
                G[i,j] = form_function(basis_elements[i], basis_elements[j])
        
        basis_names = [str(b) for b in basis_elements]
        return BilinearModule(G, basis=basis_names, **kwds)

# Convenient module-level factory function
def BilRMod(*args, **kwds):
    """
    Convenient constructor for bilinear modules.
    
    Supports multiple input formats with intelligent pattern matching.
    
    EXAMPLES::
    
        sage: # From Gram matrix
        sage: M = BilRMod([[2, 1], [1, 3]])
        sage: M.discriminant()
        5
        
        sage: # Standard constructions
        sage: H = BilRMod('hyperbolic_plane')
        sage: E = BilRMod('euclidean', 3)
        sage: S = BilRMod('symplectic', 2)
    """
    if len(args) == 1:
        arg = args[0]
        
        # String patterns for standard constructions
        if arg == 'hyperbolic_plane':
            return HyperbolicPlane(**kwds)
        elif isinstance(arg, str) and arg.startswith('euclidean'):
            # Handle 'euclidean_n' pattern
            n = kwds.get('dimension', 3)
            return StandardInnerProduct(n, **kwds)
        elif isinstance(arg, str) and arg.startswith('symplectic'):
            n = kwds.get('half_dimension', 1)
            return SymplecticForm(n, **kwds)
        else:
            # Assume it's a matrix
            return BilinearModule(arg, **kwds)
    
    elif len(args) == 2 and isinstance(args[0], str):
        # Pattern: BilRMod('type', parameter)
        form_type, param = args
        
        if form_type == 'euclidean':
            return StandardInnerProduct(param, **kwds)
        elif form_type == 'minkowski':
            return MinkowskiSpace(param, **kwds)
        elif form_type == 'symplectic':
            return SymplecticForm(param, **kwds)
        elif form_type == 'diagonal':
            return DiagonalBilinearForm(param, **kwds)
        elif form_type == 'signature':
            return HyperbolicSpace(param, **kwds)
    
    # Default: assume first argument is Gram matrix
    return BilinearModule(args[0], **kwds)
```

## Integration with Parent Framework

```python
# Register with SageMath's parent framework
BilinearModule._make_named_class('BilinearModule_with_basis', 'bilinear module')

# Category registration
from sage.categories.bilinear_modules import BilinearModules
BilinearModules.ParentMethods.Element = BilinearModuleElement

# Enable natural syntax
def _sympify_bilinear_module(arg, parent):
    """Enable symbolic integration."""
    if hasattr(arg, 'gram_matrix'):
        return BilinearModule(arg.gram_matrix())
    return None

# Test suite integration
def _test_bilinear_constructions():
    """Test standard constructions work correctly."""
    # Test hyperbolic plane
    H = HyperbolicPlane()
    assert H.signature() == (1, 1, 0)
    assert H.discriminant() == -1
    
    # Test Euclidean space
    E = StandardInnerProduct(3)
    assert E.is_positive_definite()
    assert E.signature() == (3, 0, 0)
    
    # Test symplectic form
    S = SymplecticForm(2)
    assert S.is_skew_symmetric()
    assert S.dimension() == 4
    
    print("All construction tests passed")
```

This construction framework provides mathematically principled factory functions while maintaining integration with SageMath's category system and enabling natural mathematical syntax for creating bilinear modules.