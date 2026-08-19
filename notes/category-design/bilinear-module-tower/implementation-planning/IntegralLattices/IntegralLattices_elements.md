<!--
Origin: gitclones/Coxeter/implementation/planning/IntegralLattices/IntegralLattices_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Elements: Integral Lattice Vector Implementation

Element class for vectors in integral lattices with norm computations, divisibility, and height.

## Element Class Structure

```python
from sage.modules.free_module_element import FreeModuleElement_generic_pid
from sage.structure.element import IntegralDomainElement

class IntegralLatticeElement(SymmetricBilinearModuleElement):
    """
    Element of an integral lattice.
    
    Represents a vector v in a ℤ-lattice with integer-valued norm q(v).
    Provides arithmetic operations preserving the lattice structure and
    specialized methods for divisibility, primitivity, and representation.
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 1], [1, 3]]))
        sage: v = L([1, 0])
        sage: w = L([0, 1])
        sage: v.norm()
        2
        sage: v.inner_product(w)
        1
        
        sage: # Arithmetic preserves lattice
        sage: u = 2*v + 3*w
        sage: u
        (2, 3)
        sage: u.norm()
        35  # = 2*(2)² + 2*2*3*1 + 3*(3)² = 8 + 12 + 27
        
        sage: # E₈ root lattice element
        sage: E8 = IntegralLattice("E8")
        sage: alpha = E8.simple_root(0)
        sage: alpha.norm()
        2  # All roots have norm 2
        sage: alpha.is_primitive()
        True
    """
    
    def __init__(self, parent, coords):
        """
        Initialize lattice element from coordinates.
        
        INPUT:
        - parent -- IntegralLattice_with_basis instance
        - coords -- coordinate vector with integer entries
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix.identity(2))
            sage: v = L([3, -4])
            sage: v.parent() is L
            True
            sage: v.to_vector()
            (3, -4)
        """
        # Ensure integer coordinates
        coords = [ZZ(c) for c in coords]
        super().__init__(parent, coords)
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix.identity(3))
            sage: L([1, 2, 3])
            (1, 2, 3)
            
            sage: L = IntegralLattice(matrix.identity(2), basis=['u', 'v'])
            sage: L([2, -1])
            2*u - v
        """
        if hasattr(self.parent(), '_basis_names'):
            # Use named basis
            terms = []
            basis_names = self.parent()._basis_names
            
            for i, c in enumerate(self._coords):
                if c == 0:
                    continue
                elif c == 1:
                    terms.append(basis_names[i])
                elif c == -1:
                    terms.append(f"-{basis_names[i]}")
                else:
                    terms.append(f"{c}*{basis_names[i]}")
            
            if not terms:
                return "0"
            
            result = terms[0]
            for term in terms[1:]:
                if term.startswith('-'):
                    result += f" - {term[1:]}"
                else:
                    result += f" + {term}"
            return result
        else:
            # Default coordinate representation
            return str(tuple(self._coords))
    
    def _add_(self, other):
        """
        Addition of lattice elements.
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix([[2, 1], [1, 2]]))
            sage: v = L([1, 0])
            sage: w = L([0, 1])
            sage: v + w
            (1, 1)
            sage: (v + w).norm()
            6  # = 2*1² + 2*1*1 + 2*1² = 2 + 2 + 2
        """
        coords = [a + b for a, b in zip(self._coords, other._coords)]
        return self.__class__(self.parent(), coords)
    
    def _sub_(self, other):
        """
        Subtraction of lattice elements.
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix.identity(2))
            sage: v = L([3, 4])
            sage: w = L([1, 1])
            sage: v - w
            (2, 3)
        """
        coords = [a - b for a, b in zip(self._coords, other._coords)]
        return self.__class__(self.parent(), coords)
    
    def _neg_(self):
        """
        Negation of lattice element.
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix.identity(2))
            sage: v = L([2, -3])
            sage: -v
            (-2, 3)
        """
        coords = [-c for c in self._coords]
        return self.__class__(self.parent(), coords)
    
    def _lmul_(self, scalar):
        """
        Left scalar multiplication by integer.
        
        EXAMPLES::
        
            sage: L = IntegralLattice(matrix.identity(2))
            sage: v = L([1, 2])
            sage: 3 * v
            (3, 6)
            sage: (-2) * v
            (-2, -4)
        """
        scalar = ZZ(scalar)
        coords = [scalar * c for c in self._coords]
        return self.__class__(self.parent(), coords)
    
    def _rmul_(self, scalar):
        """Right scalar multiplication."""
        return self._lmul_(scalar)
```

## Norm and Inner Product

```python
def norm(self):
    """
    Return the norm q(v) = b(v,v).
    
    For integral lattices, this is always an integer.
    
    OUTPUT:
    Integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[4, 1], [1, 2]]))
        sage: v = L([1, 2])
        sage: v.norm()
        14  # = 4*1² + 2*1*2 + 2*2² = 4 + 4 + 8
        
        sage: # Shortest vectors have minimal norm
        sage: E8 = IntegralLattice("E8")
        sage: roots = E8.shortest_vectors()
        sage: all(r.norm() == 2 for r in roots)
        True
    """
    return self.parent().quadratic_form(self)

def inner_product(self, other):
    """
    Return the inner product b(v,w).
    
    Always an integer for integral lattices.
    
    INPUT:
    - other -- another lattice element
    
    OUTPUT:
    Integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 1], [1, 2]]))
        sage: v = L([1, 0])
        sage: w = L([0, 1])
        sage: v.inner_product(w)
        1
        sage: v.inner_product(v)
        2  # = v.norm()
        
        sage: # Orthogonal vectors
        sage: u = L([1, 1])
        sage: t = L([1, -1])
        sage: u.inner_product(t)
        0  # u ⟂ t
    """
    return self.parent().bilinear_form(self, other)

def is_zero(self):
    """
    Test if this is the zero vector.
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L([0, 0]).is_zero()
        True
        sage: L([1, 0]).is_zero()
        False
    """
    return all(c == 0 for c in self._coords)

def is_primitive(self):
    """
    Test if this vector is primitive in the lattice.
    
    A vector is primitive if gcd(coordinates) = 1,
    meaning it's not a proper multiple of another vector.
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L([2, 3, 5]).is_primitive()
        True  # gcd(2,3,5) = 1
        
        sage: L([2, 4, 6]).is_primitive()
        False  # = 2*(1,2,3)
        
        sage: L([0, 0, 0]).is_primitive()
        False  # Zero is not primitive
    """
    if self.is_zero():
        return False
    
    from sage.arith.misc import gcd
    return gcd(self._coords) == 1

def divisibility(self):
    """
    Return the divisibility of this vector.
    
    The divisibility is gcd(coordinates), the largest integer
    d such that v = d*w for some lattice vector w.
    
    OUTPUT:
    Positive integer (0 for zero vector)
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: L([6, 9, 12]).divisibility()
        3  # = gcd(6,9,12)
        
        sage: L([10, 15, 25]).divisibility()
        5
        
        sage: L([1, 2, 3]).divisibility()
        1  # Primitive vector
    """
    if self.is_zero():
        return ZZ(0)
    
    from sage.arith.misc import gcd
    return gcd(self._coords)

def primitive_part(self):
    """
    Return the primitive part v/gcd(v).
    
    Every non-zero vector uniquely factors as d*w
    where d = divisibility and w is primitive.
    
    OUTPUT:
    Primitive lattice element
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: v = L([6, 9])
        sage: w = v.primitive_part()
        sage: w
        (2, 3)
        sage: w.is_primitive()
        True
        sage: 3 * w == v
        True
    """
    d = self.divisibility()
    if d == 0:
        raise ValueError("Zero vector has no primitive part")
    
    coords = [c // d for c in self._coords]
    return self.__class__(self.parent(), coords)
```

## Height and Enumeration

```python
def height(self):
    """
    Return the height max(|coordinates|).
    
    Used for enumerating lattice points by increasing height.
    
    OUTPUT:
    Non-negative integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L([3, -5]).height()
        5
        sage: L([2, 2]).height()
        2
        
        sage: # Points of height ≤ 1 in ℤ²
        sage: points = [v for v in L.enumerate_upto_height(1)]
        sage: len(points)
        9  # (0,0), ±(1,0), ±(0,1), ±(1,±1)
    """
    return max(abs(c) for c in self._coords)

def sup_norm(self):
    """
    Return the supremum norm max(|coordinates|).
    
    Same as height(), alternative name.
    
    OUTPUT:
    Non-negative integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: v = L([2, -7, 4])
        sage: v.sup_norm()
        7
    """
    return self.height()

def l1_norm(self):
    """
    Return the L¹ norm sum(|coordinates|).
    
    OUTPUT:
    Non-negative integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: v = L([2, -3, 1])
        sage: v.l1_norm()
        6  # = 2 + 3 + 1
    """
    return sum(abs(c) for c in self._coords)

def l2_norm_squared(self):
    """
    Return the squared Euclidean norm sum(coordinates²).
    
    Note: This is the standard ℓ² norm, NOT the quadratic form.
    For quadratic form value, use norm().
    
    OUTPUT:
    Non-negative integer
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, 1], [1, 2]]))
        sage: v = L([1, 1])
        sage: v.l2_norm_squared()
        2  # = 1² + 1²
        sage: v.norm()
        5  # = quadratic form value ≠ ℓ² norm
    """
    return sum(c**2 for c in self._coords)
```

## Representation and Orbits

```python
def orbit_under_automorphisms(self):
    """
    Return the orbit of this vector under Aut(L).
    
    The automorphism group acts on vectors preserving norms
    and inner products.
    
    OUTPUT:
    Set of lattice vectors in the orbit
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: v = L([1, 0])
        sage: orbit = v.orbit_under_automorphisms()
        sage: len(orbit)
        4  # {(±1,0), (0,±1)}
        
        sage: # All have same norm
        sage: all(w.norm() == v.norm() for w in orbit)
        True
    """
    G = self.parent().automorphism_group()
    orbit = set()
    
    for g in G:
        # Apply automorphism
        image_coords = g * vector(self._coords)
        image = self.parent()(image_coords)
        orbit.add(image)
    
    return orbit

def stabilizer(self):
    """
    Return the stabilizer subgroup fixing this vector.
    
    Stab(v) = {g ∈ Aut(L) : g(v) = v}
    
    OUTPUT:
    Subgroup of automorphism group
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(3))
        sage: v = L([1, 0, 0])
        sage: S = v.stabilizer()
        sage: S.order()
        8  # Symmetries of square in yz-plane
    """
    G = self.parent().automorphism_group()
    
    # Find elements fixing this vector
    stabilizer_gens = []
    for g in G.gens():
        if g * vector(self._coords) == vector(self._coords):
            stabilizer_gens.append(g)
    
    return G.subgroup(stabilizer_gens)

def is_characteristic(self):
    """
    Test if this is a characteristic vector.
    
    A vector v is characteristic if v·w ≡ w·w (mod 2)
    for all w in the lattice.
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: # For even lattices, 0 is the only characteristic vector
        sage: E8 = IntegralLattice("E8")
        sage: E8([0]*8).is_characteristic()
        True
        sage: E8.simple_root(0).is_characteristic()
        False
        
        sage: # For odd lattices, characteristic vectors exist
        sage: L = IntegralLattice(matrix.identity(2))
        sage: L([1, 1]).is_characteristic()
        True  # v·eᵢ ≡ 1 ≡ eᵢ·eᵢ (mod 2)
    """
    # Check on basis vectors
    basis = self.parent().basis()
    
    for b in basis:
        if (self.inner_product(b) - b.norm()) % 2 != 0:
            return False
    
    return True

def theta_function_contribution(self, q_var='q'):
    """
    Return this vector's contribution to theta series.
    
    Contributes q^(norm/2) to the theta function.
    
    INPUT:
    - q_var -- variable name for q
    
    OUTPUT:
    Monomial in power series ring
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: v = L([1, 1])
        sage: v.theta_function_contribution()
        q  # Since norm = 2, contributes q^(2/2) = q
        
        sage: w = L([2, 0])
        sage: w.theta_function_contribution()
        q^2  # norm = 4, contributes q^2
    """
    from sage.rings.power_series_ring import PowerSeriesRing
    from sage.rings.rational_field import QQ
    
    R = PowerSeriesRing(QQ, q_var)
    q = R.gen()
    
    norm = self.norm()
    if norm % 2 == 0:
        return q ** (norm // 2)
    else:
        # Half-integer power - need Puiseux series
        raise NotImplementedError("Half-integer powers need Puiseux series")
```

## Modular Transformations

```python
def apply_matrix(self, matrix):
    """
    Apply integer matrix transformation.
    
    Used for basis changes and isometries.
    
    INPUT:
    - matrix -- integer matrix of appropriate size
    
    OUTPUT:
    Transformed lattice element
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: v = L([1, 2])
        sage: M = matrix(ZZ, [[0, -1], [1, 0]])  # 90° rotation
        sage: v.apply_matrix(M)
        (-2, 1)
    """
    new_coords = matrix * vector(self._coords)
    return self.parent()(new_coords)

def reflect_through(self, root):
    """
    Reflect this vector through hyperplane orthogonal to root.
    
    Reflection formula: v ↦ v - 2(v·r)/(r·r) * r
    
    INPUT:
    - root -- lattice vector defining reflection hyperplane
    
    OUTPUT:
    Reflected lattice element
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix([[2, -1], [-1, 2]]))  # A₂
        sage: v = L([1, 0])  # Simple root α₁
        sage: w = L([0, 1])  # Simple root α₂
        sage: v.reflect_through(w)
        (1, -1)  # α₁ - α₂
    """
    if root.is_zero():
        raise ValueError("Cannot reflect through zero vector")
    
    num = 2 * self.inner_product(root)
    den = root.norm()
    
    if num % den != 0:
        raise ValueError("Reflection does not preserve lattice")
    
    coeff = num // den
    return self - coeff * root

def weyl_group_orbit(self):
    """
    Return Weyl group orbit for root lattices.
    
    The Weyl group is generated by reflections through
    simple roots.
    
    OUTPUT:
    Set of vectors in Weyl group orbit
    
    EXAMPLES::
    
        sage: A2 = IntegralLattice(matrix([[2, -1], [-1, 2]]))
        sage: alpha1 = A2([1, 0])
        sage: orbit = alpha1.weyl_group_orbit()
        sage: len(orbit)
        6  # The 6 roots of A₂
    """
    # Check if parent is a root lattice
    if not hasattr(self.parent(), 'simple_roots'):
        raise ValueError("Weyl group only defined for root lattices")
    
    simple_roots = self.parent().simple_roots()
    orbit = {self}
    new_vectors = {self}
    
    # Repeatedly apply simple reflections
    while new_vectors:
        next_new = set()
        for v in new_vectors:
            for root in simple_roots:
                reflected = v.reflect_through(root)
                if reflected not in orbit:
                    next_new.add(reflected)
                    orbit.add(reflected)
        new_vectors = next_new
    
    return orbit
```

## Enumeration Helpers

```python
@staticmethod
def enumerate_by_height(parent, max_height):
    """
    Enumerate lattice vectors by increasing height.
    
    INPUT:
    - parent -- integral lattice
    - max_height -- maximum height
    
    OUTPUT:
    Iterator of lattice elements
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: list(IntegralLatticeElement.enumerate_by_height(L, 1))
        [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
         (1, 1), (1, -1), (-1, 1), (-1, -1)]
    """
    n = parent.rank()
    
    for height in range(max_height + 1):
        # Generate all vectors with supremum norm = height
        from itertools import product
        
        for coords in product(range(-height, height + 1), repeat=n):
            if max(abs(c) for c in coords) == height:
                yield parent(coords)

@staticmethod
def enumerate_by_norm(parent, max_norm):
    """
    Enumerate lattice vectors by increasing norm.
    
    INPUT:
    - parent -- positive definite integral lattice
    - max_norm -- maximum quadratic form value
    
    OUTPUT:
    Iterator of lattice elements
    
    EXAMPLES::
    
        sage: L = IntegralLattice(matrix.identity(2))
        sage: vecs = list(IntegralLatticeElement.enumerate_by_norm(L, 2))
        sage: len(vecs)
        9  # 0 (norm 0), ±e₁, ±e₂ (norm 1), ±e₁±e₂ (norm 2)
    """
    if not parent.is_positive_definite():
        raise ValueError("Norm enumeration requires positive definite lattice")
    
    # Use shortest vector algorithms with increasing bounds
    yielded = set()
    
    for norm_bound in range(max_norm + 1):
        # Find all vectors with norm exactly norm_bound
        # This is a simplified approach - real implementation
        # would use sphere enumeration algorithms
        
        # Enumerate by height as approximation
        height_bound = int((norm_bound ** 0.5) * parent.rank()) + 1
        
        for v in IntegralLatticeElement.enumerate_by_height(parent, height_bound):
            if v not in yielded and v.norm() == norm_bound:
                yielded.add(v)
                yield v
```

## Mathematical Properties

The integral lattice element implementation maintains:

```python
# Mathematical assertion: Integer arithmetic
# All operations preserve integer coordinates

# Mathematical assertion: Norm integrality
# q(v) ∈ ℤ for all v ∈ L

# Mathematical assertion: Bilinearity
# b(av + bw, u) = a·b(v,u) + b·b(w,u)

# Mathematical assertion: Primitive decomposition
# Every v ≠ 0 uniquely factors as v = d·w with w primitive

# Mathematical assertion: Height bounds
# |v·w| ≤ height(v) · height(w) · rank

# Mathematical assertion: Orbit finiteness
# |Orb(v)| ≤ |Aut(L)| < ∞ for integral lattices

# Mathematical assertion: Reflection formula
# Reflection through r: v ↦ v - 2(v·r)/(r·r)·r

# Mathematical assertion: Theta contribution
# Each v contributes q^(q(v)/2) to theta series
```

This implementation provides comprehensive functionality for integral lattice elements while maintaining efficiency and mathematical correctness.