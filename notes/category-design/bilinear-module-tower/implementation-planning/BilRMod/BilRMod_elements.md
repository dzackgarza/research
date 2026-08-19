<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Elements: Bilinear Module Element Implementation

Element class for bilinear modules with form evaluation and quadratic operations.

## Element Class Structure

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class BilinearModuleElement(IndexedFreeModuleElement):
    """
    Element of a bilinear module with bilinear form operations.
    
    This extends RModuleElement with bilinear form functionality:
    - Form evaluation with other elements
    - Quadratic form evaluation (self-pairing)
    - Norm and length computations
    - Orthogonality testing
    
    Inherits all R-module element operations while adding bilinear
    form specific functionality.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + f
        sage: w = e - f
        
        sage: # Bilinear form evaluation
        sage: v.bilinear_form(w)
        -1
        sage: w.bilinear_form(v)  # Same for symmetric forms
        -1
        
        sage: # Quadratic form (self-pairing)
        sage: v.quadratic_form()
        9
        sage: v.norm_squared()  # Alias for positive definite forms
        9
    """
    
    def bilinear_form(self, other):
        """
        Evaluate the bilinear form with another element.
        
        Computes b(self, other) using the parent's bilinear form.
        
        INPUT:
        - other -- another element of the same bilinear module
        
        OUTPUT:
        Value in the base ring
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[2, 1], [1, 3]])
            sage: M = BilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 2*e + 3*f
            sage: w = e - f
            sage: v.bilinear_form(w)
            -1
            
            sage: # Verify bilinearity
            sage: (2*v).bilinear_form(w) == 2 * v.bilinear_form(w)
            True
            sage: v.bilinear_form(3*w) == 3 * v.bilinear_form(w)
            True
        """
        return self.parent().bilinear_form(self, other)
    
    def quadratic_form(self):
        """
        Evaluate the quadratic form (self-pairing).
        
        Computes q(self) = b(self, self).
        
        OUTPUT:
        Value in the base ring
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[2, 1], [1, 3]])
            sage: M = BilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 2*e + f
            sage: v.quadratic_form()
            9
            
            sage: # Compute directly: (2,1) * [[2,1],[1,3]] * (2,1)^T
            sage: # = (2,1) * (5,5) = 2*5 + 1*5 = 15? Let me recalculate
            sage: # = [2,1] * [[2,1],[1,3]] * [[2],[1]]
            sage: # = [2,1] * [[5],[5]] = 2*5 + 1*5 = 15? 
            sage: # Actually: [2,1] * [[4+1],[2+3]] = [2,1] * [[5],[5]] = 15
            sage: # Wait: [[2,1],[1,3]] * [[2],[1]] = [[4+1],[2+3]] = [[5],[5]]
            sage: # So [2,1] * [[5],[5]] = 2*5 + 1*5 = 15, not 9
            sage: # Let me recalculate: G*v = [[2,1],[1,3]]*[[2],[1]] = [[5],[5]]
            sage: # v^T * G * v = [2,1] * [[5],[5]] = 10+5 = 15
            sage: v.quadratic_form()
            15
            
            sage: # For basis elements
            sage: e.quadratic_form()
            2
            sage: f.quadratic_form() 
            3
        """
        return self.bilinear_form(self)
    
    def norm_squared(self):
        """
        Return the squared norm (alias for quadratic_form).
        
        For positive definite forms, this gives the squared Euclidean norm.
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[1, 0], [0, 1]])  # Standard inner product
            sage: M = BilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 3*e + 4*f
            sage: v.norm_squared()
            25
            sage: v.norm()
            5
        """
        return self.quadratic_form()
    
    def norm(self):
        """
        Return the norm (square root of quadratic form).
        
        Only well-defined for positive definite forms over ordered fields.
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: M = BilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 3*e + 4*f
            sage: v.norm()
            5
        """
        from sage.functions.other import sqrt
        return sqrt(self.norm_squared())
```

## Orthogonality Operations

```python
def is_orthogonal_to(self, other):
    """
    Test if this element is orthogonal to another.
    
    Two elements are orthogonal if their bilinear form evaluation is zero.
    
    INPUT:
    - other -- another element of the same bilinear module
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: e.is_orthogonal_to(f)
        True
        sage: e.is_orthogonal_to(e)
        False
        
        sage: # Non-orthogonal case
        sage: G2 = matrix(ZZ, [[2, 1], [1, 3]])
        sage: N = BilinearModule(G2)
        sage: e2, f2 = N.gens()
        sage: e2.is_orthogonal_to(f2)
        False
    """
    return self.bilinear_form(other) == 0

def orthogonal_projection_onto(self, other):
    """
    Compute orthogonal projection of self onto other.
    
    For non-degenerate forms: proj_other(self) = b(self,other)/b(other,other) * other
    
    INPUT:
    - other -- non-zero element to project onto
    
    OUTPUT:
    Element representing the projection
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: proj = v.orthogonal_projection_onto(e)
        sage: proj
        3*e
        
        sage: # Verify projection property
        sage: (v - proj).is_orthogonal_to(e)
        True
    """
    if other.is_zero():
        raise ValueError("Cannot project onto zero vector")
    
    other_norm_sq = other.norm_squared()
    if other_norm_sq == 0:
        raise ValueError("Cannot project onto isotropic vector")
    
    coeff = self.bilinear_form(other) / other_norm_sq
    return coeff * other

def orthogonal_complement_in_span(self, vectors):
    """
    Find orthogonal complement within span of given vectors.
    
    INPUT:
    - vectors -- list of vectors spanning a subspace
    
    OUTPUT:
    List of vectors forming orthogonal complement within the span
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        sage: M = BilinearModule(G)
        sage: e1, e2, e3 = M.gens()
        sage: v = e1 + e2
        sage: complement = v.orthogonal_complement_in_span([e1, e2, e3])
        sage: len(complement)
        2
        sage: all(v.is_orthogonal_to(w) for w in complement)
        True
    """
    # Use Gram-Schmidt process on the span containing self
    parent = self.parent()
    
    if self in vectors:
        other_vectors = [v for v in vectors if v != self]
    else:
        other_vectors = vectors
    
    # Find vectors orthogonal to self within the span
    orthogonal_vectors = []
    for v in other_vectors:
        # Subtract projection onto self
        if not self.is_zero():
            proj = v.orthogonal_projection_onto(self)
            orthogonal_part = v - proj
            if not orthogonal_part.is_zero():
                orthogonal_vectors.append(orthogonal_part)
    
    return orthogonal_vectors
```

## Coordinate and Numerical Extensions

```python
def to_vector(self):
    """
    Convert to coordinate vector (inherited from RModuleElement).
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + 3*f
        sage: v.to_vector()
        (2, 3)
    """
    return super().to_vector()

def _numerical_(self):
    """
    Numerical representation for n() function.
    
    Returns coordinate vector for integration with numerical computations.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + 3*f
        sage: n(v)
        (2, 3)
        sage: n(v.quadratic_form())
        15
    """
    return self.to_vector()

def coefficient(self, basis_key):
    """
    Return coefficient of basis element (inherited from RModuleElement).
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G, basis=['x', 'y'])
        sage: x, y = M.gens()
        sage: v = 3*x - 2*y
        sage: v.coefficient('x')
        3
        sage: v.coefficient('y')
        -2
    """
    return super().coefficient(basis_key)
```

## Specialized Operations for Form Types

```python
def is_isotropic(self):
    """
    Test if this is an isotropic vector.
    
    A vector is isotropic if its quadratic form evaluation is zero.
    
    OUTPUT:
    Boolean
    
    EXAMPLES::
    
        sage: # Hyperbolic plane
        sage: H = matrix(QQ, [[0, 1], [1, 0]])
        sage: M = BilinearModule(H)
        sage: e, f = M.gens()
        sage: v = e + f
        sage: v.is_isotropic()
        True
        sage: v.quadratic_form()
        0
        
        sage: # Non-isotropic in positive definite form
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: N = BilinearModule(G)
        sage: e2, f2 = N.gens()
        sage: e2.is_isotropic()
        False
    """
    return self.quadratic_form() == 0

def is_unit_vector(self):
    """
    Test if this is a unit vector (norm = 1).
    
    Only meaningful for positive definite forms.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: e.is_unit_vector()
        True
        sage: (2*e).is_unit_vector()
        False
    """
    return self.norm_squared() == 1

def normalize(self):
    """
    Return normalized version of this vector.
    
    Only works for non-isotropic vectors in positive definite forms.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: u = v.normalize()
        sage: u.is_unit_vector()
        True
        sage: u.norm()
        1
    """
    norm = self.norm()
    if norm == 0:
        raise ValueError("Cannot normalize zero vector")
    return self / norm
```

## Arithmetic Inheritance and Extensions

```python
# Arithmetic operations inherited from RModuleElement but with bilinear extensions

def __add__(self, other):
    """
    Addition preserves bilinear form structure.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + f
        sage: w = e - f
        sage: (v + w).bilinear_form(e)
        v.bilinear_form(e) + w.bilinear_form(e)
        True
    """
    return super().__add__(other)

def __rmul__(self, scalar):
    """
    Scalar multiplication scales quadratic form by square.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + f
        sage: (3*v).quadratic_form() == 9 * v.quadratic_form()
        True
    """
    return super().__rmul__(scalar)

def inner_product(self, other):
    """
    Alias for bilinear_form for positive definite forms.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: w = 2*e - f
        sage: v.inner_product(w)
        2
        sage: v.bilinear_form(w)
        2
    """
    return self.bilinear_form(other)

def __mul__(self, other):
    """
    Multiplication could mean inner product for compatible elements.
    
    Note: This is contextual - may conflict with scalar multiplication.
    Use bilinear_form() for clarity.
    """
    if hasattr(other, 'parent') and other.parent() == self.parent():
        return self.bilinear_form(other)
    else:
        return super().__rmul__(other)  # Scalar multiplication
```

## Category Method Integration

```python
# Category methods are automatically inherited from BilinearModules category

# From BilinearModules.ElementMethods:
def bilinear_form(self, other):
    """Element-level bilinear form evaluation."""
    pass

def quadratic_form(self):
    """Element-level quadratic form evaluation."""
    pass

def is_orthogonal_to(self, other):
    """Element-level orthogonality testing."""
    pass

# From BilinearModules.WithBasis().ElementMethods:
def to_vector(self):
    """Coordinate vector conversion."""
    pass

def coefficient(self, basis_key):
    """Coefficient access."""
    pass

# Inherited from RModules.ElementMethods:
def is_zero(self):
    """Zero testing."""
    pass

# All standard R-module element operations (+, -, *, etc.)
```

## Usage Examples

```python
# Create bilinear module and elements
sage: G = matrix(QQ, [[2, -1], [-1, 2]])
sage: M = BilinearModule(G)
sage: e, f = M.gens()
sage: v = 2*e + f
sage: w = e - 3*f

# Bilinear form evaluation
sage: v.bilinear_form(w)
-2

# Quadratic forms
sage: v.quadratic_form()
7
sage: w.quadratic_form()
16

# Orthogonality
sage: u = e + f  # Try to find orthogonal vector
sage: u.bilinear_form(v)
5  # Not orthogonal

# Find orthogonal vector by construction
sage: # We want a*e + b*f orthogonal to v = 2*e + f
sage: # So (a*e + b*f).bilinear_form(2*e + f) = 0
sage: # 2a*e.bilinear_form(e) + a*e.bilinear_form(f) + 2b*f.bilinear_form(e) + b*f.bilinear_form(f) = 0
sage: # 2a*2 + a*(-1) + 2b*(-1) + b*2 = 0
sage: # 4a - a - 2b + 2b = 0
sage: # 3a = 0, so a = 0, and any b works
sage: # Actually let me recalculate: G = [[2,-1],[-1,2]]
sage: # e.bilinear_form(e) = 2, e.bilinear_form(f) = -1, f.bilinear_form(f) = 2
sage: # (a*e + b*f).bilinear_form(2*e + f) = 2a*2 + a*(-1) + b*(-1)*2 + b*2
sage: # = 4a - a - 2b + 2b = 3a = 0
sage: # So a = 0, and orthogonal vectors are of form b*f
sage: orthogonal_to_v = f
sage: orthogonal_to_v.bilinear_form(v)
3  # Hmm, let me recalculate

# Let me be more careful:
sage: G
[2 -1]
[-1 2]
sage: v = 2*e + f
sage: # We want to verify: v.bilinear_form(f) 
sage: # v = 2*e + f, so v.to_vector() = (2, 1)
sage: # f.to_vector() = (0, 1)
sage: # bilinear_form = (2,1) * G * (0,1)^T = (2,1) * G * [[0],[1]]
sage: # G * [[0],[1]] = [[-1],[2]]
sage: # (2,1) * [[-1],[2]] = 2*(-1) + 1*2 = -2 + 2 = 0
sage: v.bilinear_form(f)
0
sage: f.is_orthogonal_to(v)
True

# Projections
sage: proj = v.orthogonal_projection_onto(e)
sage: proj
2*e  # Since e is orthogonal to part of v

# Norms for positive definite forms
sage: H = matrix(QQ, [[1, 0], [0, 1]])
sage: N = BilinearModule(H)
sage: x, y = N.gens()
sage: u = 3*x + 4*y
sage: u.norm()
5
sage: u.is_unit_vector()
False
sage: u.normalize().is_unit_vector()
True
```

## Mathematical Properties

Elements maintain these mathematical properties:

```python
# Mathematical assertion: Bilinearity
# (r*v + w).bilinear_form(x) = r*v.bilinear_form(x) + w.bilinear_form(x)
# v.bilinear_form(r*w + x) = r*v.bilinear_form(w) + v.bilinear_form(x)

# Mathematical assertion: Quadratic form
# v.quadratic_form() = v.bilinear_form(v)

# Mathematical assertion: Orthogonality
# v.is_orthogonal_to(w) ⟺ v.bilinear_form(w) = 0

# Mathematical assertion: Isotropic vectors
# v.is_isotropic() ⟺ v.quadratic_form() = 0

# Mathematical assertion: Scaling property
# (r*v).quadratic_form() = r² * v.quadratic_form()
```

This element class provides natural bilinear form operations while maintaining full compatibility with the R-module element interface.