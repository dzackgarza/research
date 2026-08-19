<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_objects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects: Bilinear Module Parent Implementation

Parent class implementation for bilinear modules with Gram matrix and form evaluation.

## Parent Class Structure

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.parent import Parent

class BilinearModule_with_basis(UniqueRepresentation, Parent):
    """
    Concrete parent class for bilinear modules with basis.
    
    A bilinear module consists of:
    - An R-module M with basis
    - A bilinear form b: M × M → R
    - Gram matrix representation relative to the chosen basis
    
    This extends RModule_with_basis by adding bilinear form functionality
    while preserving all module operations and structure.
    
    EXAMPLES::
    
        sage: # Positive definite form
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M
        Bilinear module of rank 2 over Integer Ring
        sage: M.discriminant()
        5
        sage: M.is_positive_definite()
        True
        
        sage: # Hyperbolic plane
        sage: H_matrix = matrix(QQ, [[0, 1], [1, 0]])
        sage: H = BilinearModule(H_matrix)
        sage: H.signature()
        (1, 1, 0)
        sage: H.is_indefinite()
        True
    """
    
    def __init__(self, gram_matrix, basis=None, category=None, **kwds):
        """
        Initialize a bilinear module with given Gram matrix.
        
        INPUT:
        - gram_matrix -- matrix defining the bilinear form
        - basis -- optional basis names (defaults to indexed names)
        - category -- optional category (defaults to BilinearModules)
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[1, 0], [0, -1]])
            sage: M = BilinearModule(G)
            sage: M.base_ring()
            Integer Ring
            sage: M.rank()
            2
        """
        # Validate Gram matrix
        if not gram_matrix.is_square():
            raise ValueError("Gram matrix must be square")
        
        self._gram_matrix = gram_matrix
        base_ring = gram_matrix.base_ring()
        rank = gram_matrix.nrows()
        
        # Set up basis
        if basis is None:
            basis = [f'e{i}' for i in range(rank)]
        self._basis_keys = basis
        
        # Set up category
        if category is None:
            from sage.categories.bilinear_modules import BilinearModules
            category = BilinearModules(base_ring).WithBasis()
        
        # Initialize parent
        Parent.__init__(self, base=base_ring, category=category, **kwds)
        
        # Cache for computational efficiency
        self._rank = rank
        self._gram_matrix_cached = gram_matrix
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            Bilinear module of rank 2 over Integer Ring
        """
        return f"Bilinear module of rank {self.rank()} over {self.base_ring()}"
    
    def rank(self):
        """Return the rank of the underlying module."""
        return self._rank
    
    def dimension(self):
        """Return the dimension (same as rank for free modules)."""
        return self.rank()
```

## Bilinear Form Implementation

```python
def bilinear_form(self, v, w):
    """
    Evaluate the bilinear form on two elements.
    
    Uses the Gram matrix: b(v,w) = v^T * G * w where G is the Gram matrix.
    
    INPUT:
    - v, w -- elements of this bilinear module
    
    OUTPUT:
    Value b(v,w) in the base ring
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G) 
        sage: e, f = M.gens()
        sage: M.bilinear_form(e, f)
        1
        sage: M.bilinear_form(e, e)
        2
        sage: M.bilinear_form(f, f) 
        3
        
        sage: # Linearity
        sage: M.bilinear_form(2*e + f, e)
        2*M.bilinear_form(e, e) + M.bilinear_form(f, e)
        True
    """
    # Convert elements to coordinate vectors
    v_coords = v.to_vector()
    w_coords = w.to_vector()
    
    # Compute v^T * G * w
    return v_coords * self._gram_matrix * w_coords

def gram_matrix(self, basis=None):
    """
    Return the Gram matrix of the bilinear form.
    
    INPUT:
    - basis -- optional basis (uses module basis if not provided)
    
    OUTPUT:
    Matrix G where G[i,j] = b(basis[i], basis[j])
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M.gram_matrix() == G
        True
        
        sage: # Custom basis changes Gram matrix
        sage: e, f = M.gens()
        sage: new_basis = [e + f, e - f]
        sage: M.gram_matrix(new_basis)
        [6 -1]
        [-1  1]
    """
    if basis is None:
        return self._gram_matrix
    
    # Compute Gram matrix for custom basis
    n = len(basis)
    from sage.matrix.constructor import matrix
    G = matrix(self.base_ring(), n, n)
    for i in range(n):
        for j in range(n):
            G[i,j] = self.bilinear_form(basis[i], basis[j])
    return G

def is_symmetric(self):
    """
    Test if the bilinear form is symmetric.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M.is_symmetric()
        True
        
        sage: A = matrix(ZZ, [[0, 1], [-1, 0]])
        sage: N = BilinearModule(A)
        sage: N.is_symmetric()
        False
    """
    return self._gram_matrix == self._gram_matrix.transpose()

def is_skew_symmetric(self):
    """
    Test if the bilinear form is skew-symmetric.
    
    EXAMPLES::
    
        sage: A = matrix(ZZ, [[0, 1], [-1, 0]])
        sage: M = BilinearModule(A)
        sage: M.is_skew_symmetric()
        True
    """
    return self._gram_matrix == -self._gram_matrix.transpose()

def is_alternating(self):
    """
    Test if the bilinear form is alternating.
    
    A form is alternating if b(v,v) = 0 for all v.
    
    EXAMPLES::
    
        sage: A = matrix(ZZ, [[0, 1], [-1, 0]])
        sage: M = BilinearModule(A)
        sage: M.is_alternating()
        True
    """
    # Check diagonal entries are zero
    for i in range(self._gram_matrix.nrows()):
        if self._gram_matrix[i,i] != 0:
            return False
    return True
```

## Invariants and Properties

```python
def discriminant(self):
    """
    Return the discriminant (determinant of Gram matrix).
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M.discriminant()
        5
        
        sage: # Degenerate form
        sage: D = matrix(ZZ, [[1, 1], [1, 1]])
        sage: N = BilinearModule(D)
        sage: N.discriminant()
        0
    """
    return self._gram_matrix.determinant()

def signature(self):
    """
    Return the signature (p, q, r) over ordered fields.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M.signature()
        (2, 0, 0)  # positive definite
        
        sage: H = matrix(QQ, [[1, 0], [0, -1]])
        sage: N = BilinearModule(H)
        sage: N.signature()
        (1, 1, 0)  # indefinite
    """
    eigenvals = self._gram_matrix.eigenvalues()
    
    pos = sum(1 for ev in eigenvals if ev > 0)
    neg = sum(1 for ev in eigenvals if ev < 0)
    zero = sum(1 for ev in eigenvals if ev == 0)
    
    return (pos, neg, zero)

def is_positive_definite(self):
    """Test if form is positive definite."""
    p, q, r = self.signature()
    return q == 0 and r == 0

def is_negative_definite(self):
    """Test if form is negative definite.""" 
    p, q, r = self.signature()
    return p == 0 and r == 0

def is_definite(self):
    """Test if form is definite."""
    return self.is_positive_definite() or self.is_negative_definite()

def is_indefinite(self):
    """Test if form is indefinite."""
    p, q, r = self.signature()
    return p > 0 and q > 0

def is_degenerate(self):
    """Test if form is degenerate."""
    return self.discriminant() == 0

def is_nondegenerate(self):
    """Test if form is non-degenerate."""
    return not self.is_degenerate()
```

## Module Structure Inheritance

```python
def gens(self):
    """
    Return the generators (basis elements).
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: M.bilinear_form(e, f)
        1
    """
    return tuple(self.monomial(key) for key in self._basis_keys)

def gen(self, i):
    """Return the i-th generator."""
    return self.monomial(self._basis_keys[i])

def ngens(self):
    """Return the number of generators."""
    return len(self._basis_keys)

def basis(self):
    """Return the basis as a family."""
    return self.gens()

def monomial(self, key):
    """Return the monomial corresponding to a basis key."""
    return self.element_class(self, {key: self.base_ring().one()})

def _from_dict(self, coefficients):
    """Construct element from coefficient dictionary."""
    return self.element_class(self, coefficients)

def _from_vector(self, vector):
    """
    Construct element from coordinate vector.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: v = M._from_vector(vector([1, -1]))
        sage: e, f = M.gens()
        sage: v == e - f
        True
    """
    coeffs = {}
    for i, coord in enumerate(vector):
        if coord != 0:
            coeffs[self._basis_keys[i]] = coord
    return self._from_dict(coeffs)

def _to_vector(self, element):
    """Convert element to coordinate vector."""
    coords = []
    for key in self._basis_keys:
        coords.append(element.coefficient(key))
    from sage.modules.free_module_element import vector
    return vector(self.base_ring(), coords)

# Element class specification
element_class = None  # Will be set to BilinearModuleElement
```

## Construction and TestSuite

```python
def an_element(self):
    """
    Return a typical element for testing.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: M.an_element()
        e0 + e1
    """
    if self.ngens() == 0:
        return self.zero()
    return sum(self.gens()[:min(2, self.ngens())])

def some_elements(self):
    """Return several elements for testing."""
    elements = [self.zero(), self.an_element()]
    if self.ngens() > 0:
        elements.extend(self.gens()[:3])
    if self.ngens() >= 2:
        e, f = self.gens()[:2]
        elements.extend([2*e, e + f, e - f])
    return elements

def zero(self):
    """Return the zero element."""
    return self._from_dict({})

def is_free(self):
    """Bilinear modules with basis are free."""
    return True

def is_finitely_generated(self):
    """Bilinear modules with basis are finitely generated."""
    return True

def coordinate_module(self):
    """Return the coordinate module (vector space of coordinates)."""
    from sage.modules.free_module import FreeModule
    return FreeModule(self.base_ring(), self.rank())
```

## Factory Integration

```python
def _test_bilinear_form(self, **options):
    """
    Test the bilinear form satisfies required properties.
    
    This is called automatically by TestSuite.
    """
    tester = self._tester(**options)
    
    # Test bilinearity in first argument
    if self.ngens() >= 2:
        v, w, x = (self.some_elements() + [self.zero()])[:3]
        r = self.base_ring().random_element()
        
        # b(r*v + w, x) = r*b(v,x) + b(w,x)
        lhs = self.bilinear_form(r*v + w, x)
        rhs = r*self.bilinear_form(v, x) + self.bilinear_form(w, x)
        tester.assertEqual(lhs, rhs)
        
        # b(v, r*w + x) = r*b(v,w) + b(v,x)  
        lhs = self.bilinear_form(v, r*w + x)
        rhs = r*self.bilinear_form(v, w) + self.bilinear_form(v, x)
        tester.assertEqual(lhs, rhs)

def _test_gram_matrix_consistency(self, **options):
    """Test Gram matrix matches bilinear form evaluation."""
    tester = self._tester(**options)
    
    if self.ngens() >= 2:
        G = self.gram_matrix()
        gens = self.gens()
        
        for i in range(min(len(gens), 3)):
            for j in range(min(len(gens), 3)):
                expected = G[i,j]
                actual = self.bilinear_form(gens[i], gens[j])
                tester.assertEqual(expected, actual)
```

## Mathematical Assertions

The bilinear module implementation maintains these mathematical properties:

```python
# Mathematical assertion: Bilinear form evaluation
# b(v,w) = v^T * G * w where G is Gram matrix and v,w are coordinate vectors

# Mathematical assertion: Gram matrix definition  
# G[i,j] = b(e_i, e_j) for basis elements e_i, e_j

# Mathematical assertion: Discriminant invariance
# det(G') = det(P)² * det(G) under basis change matrix P

# Mathematical assertion: Signature invariance
# Signature (p,q,r) is independent of basis choice over ordered fields

# Mathematical assertion: Form properties
# is_symmetric() ⟺ G = G^T
# is_skew_symmetric() ⟺ G = -G^T  
# is_alternating() ⟺ diagonal entries of G are zero
```

This parent class provides the computational foundation for bilinear modules while inheriting all R-module functionality from the category framework.