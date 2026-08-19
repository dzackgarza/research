<!--
Origin: gitclones/Coxeter/implementation/planning/SymmetricBilRMod/SymmetricBilRMod_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Elements: Symmetric Bilinear Module Element Implementation

Element class for symmetric bilinear modules with quadratic form evaluation and geometric operations.

## Element Class Structure

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class SymmetricBilinearModuleElement(BilinearModuleElement):
    """
    Element of a symmetric bilinear module with quadratic form operations.
    
    This extends BilinearModuleElement with symmetric form functionality:
    - Quadratic form evaluation: q(v) = b(v,v)
    - Norm and length computations for definite forms
    - Angle computations for positive definite forms
    - Isotropic vector detection
    - Orthogonal projection operations
    
    Inherits all bilinear form operations while adding quadratic
    form specific functionality unique to symmetric forms.
    
    EXAMPLES::
    
        sage: G = matrix(ZZ, [[2, 1], [1, 3]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 2*e + f
        sage: w = e - f
        
        sage: # Quadratic form evaluation
        sage: v.quadratic_form()
        15
        sage: w.quadratic_form()
        2
        
        sage: # Symmetry verification
        sage: v.bilinear_form(w) == w.bilinear_form(v)
        True
        
        sage: # For positive definite forms
        sage: v.norm_squared()  # Same as quadratic form
        15
        sage: v.norm()  # Square root for positive definite
        sqrt(15)
    """
    
    def quadratic_form(self):
        """
        Evaluate the quadratic form: q(v) = b(v,v).
        
        For symmetric bilinear forms, this is the fundamental
        invariant of each vector.
        
        OUTPUT:
        Value q(v) in the base ring
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[2, 1], [1, 3]])
            sage: M = SymmetricBilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 3*e + 2*f
            sage: v.quadratic_form()
            34  # 3²·2 + 2·3·2·1 + 2²·3 = 18 + 12 + 12 = 42? Let me recalculate
            # q(3e + 2f) = (3e + 2f)^T G (3e + 2f)
            # = [3, 2] [[2,1],[1,3]] [3, 2]^T
            # = [3, 2] [6+2, 3+6] = [3, 2] [8, 9] = 24 + 18 = 42
            42
            
            sage: # For basis elements
            sage: e.quadratic_form()
            2
            sage: f.quadratic_form()
            3
        """
        return self.parent().quadratic_form(self)
    
    def norm_squared(self):
        """
        Return squared norm (alias for quadratic_form).
        
        For positive definite forms, this gives squared Euclidean norm.
        For indefinite forms, this can be negative.
        
        EXAMPLES::
        
            sage: # Positive definite case
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: M = SymmetricBilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 3*e + 4*f
            sage: v.norm_squared()
            25
            
            sage: # Indefinite case (can be negative)
            sage: H = matrix(QQ, [[1, 0], [0, -1]])
            sage: N = SymmetricBilinearModule(H)
            sage: x, y = N.gens()
            sage: w = x + 2*y
            sage: w.norm_squared()
            -3  # 1 - 4 = -3
        """
        return self.quadratic_form()
    
    def norm(self):
        """
        Return norm (square root of quadratic form).
        
        Only well-defined for positive definite forms over ordered fields.
        For indefinite forms, may return complex numbers or raise errors.
        
        EXAMPLES::
        
            sage: # Standard inner product
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: M = SymmetricBilinearModule(G)
            sage: e, f = M.gens()
            sage: v = 3*e + 4*f
            sage: v.norm()
            5
            sage: v.norm()^2 == v.norm_squared()
            True
            
            sage: # Zero vector
            sage: M.zero().norm()
            0
        """
        norm_sq = self.norm_squared()
        
        if norm_sq < 0:
            if self.parent().is_positive_definite():
                raise ValueError("Negative norm squared in positive definite form")
            else:
                # Could return complex norm or raise error
                from sage.functions.other import sqrt
                return sqrt(abs(norm_sq)) * I
        
        from sage.functions.other import sqrt
        return sqrt(norm_sq)
    
    def is_isotropic(self):
        """
        Test if this is an isotropic vector.
        
        A vector is isotropic if its quadratic form evaluation is zero:
        q(v) = 0. These vectors lie on the "light cone" of the form.
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: # Hyperbolic plane
            sage: H = matrix(QQ, [[0, 1], [1, 0]])
            sage: M = SymmetricBilinearModule(H)
            sage: e, f = M.gens()
            sage: (e + f).is_isotropic()
            True
            sage: (e - f).is_isotropic()
            True
            sage: e.is_isotropic()
            True  # Basis vectors are isotropic
            
            sage: # Positive definite form
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: N = SymmetricBilinearModule(G)
            sage: x, y = N.gens()
            sage: x.is_isotropic()
            False  # No non-zero isotropic vectors
            sage: N.zero().is_isotropic()
            True  # Zero is always isotropic
        """
        return self.quadratic_form() == 0
    
    def is_positive(self):
        """Test if q(v) > 0."""
        return self.quadratic_form() > 0
    
    def is_negative(self):
        """Test if q(v) < 0."""
        return self.quadratic_form() < 0
    
    def sign(self):
        """
        Return the sign of the quadratic form.
        
        OUTPUT:
        +1 if q(v) > 0, -1 if q(v) < 0, 0 if q(v) = 0
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[1, 0], [0, -1]])
            sage: M = SymmetricBilinearModule(G)
            sage: e, f = M.gens()
            sage: e.sign()
            1
            sage: f.sign()
            -1
            sage: (e + f).sign()
            0  # Isotropic vector
        """
        q = self.quadratic_form()
        if q > 0:
            return 1
        elif q < 0:
            return -1
        else:
            return 0
```

## Geometric Operations

```python
def distance_to(self, other):
    """
    Euclidean distance to another element.
    
    Only meaningful for positive definite forms.
    
    INPUT:
    - other -- another element of the same module
    
    OUTPUT:
    Distance ||self - other||
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: w = 0*e + 3*f
        sage: v.distance_to(w)
        sqrt(10)  # ||(3,4) - (0,3)|| = ||(3,1)|| = sqrt(9+1) = sqrt(10)
    """
    if not self.parent().is_positive_definite():
        raise ValueError("Distance only defined for positive definite forms")
    
    return (self - other).norm()

def angle_with(self, other):
    """
    Angle between vectors (in radians).
    
    Uses the formula: cos(θ) = b(v,w) / (||v|| ||w||)
    Only defined for positive definite forms.
    
    INPUT:
    - other -- another non-zero element
    
    OUTPUT:
    Angle in radians (0 to π)
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: e.angle_with(f)
        pi/2  # Orthogonal vectors
        
        sage: v = e + f
        sage: v.angle_with(e)
        pi/4  # 45 degrees
    """
    if not self.parent().is_positive_definite():
        raise ValueError("Angle only defined for positive definite forms")
    
    if self.is_zero() or other.is_zero():
        raise ValueError("Cannot compute angle with zero vector")
    
    # Compute cosine of angle
    inner_product = self.bilinear_form(other)
    norm_product = self.norm() * other.norm()
    
    cos_angle = inner_product / norm_product
    
    # Handle numerical precision issues
    if cos_angle > 1:
        cos_angle = 1
    elif cos_angle < -1:
        cos_angle = -1
    
    from sage.functions.trig import arccos
    return arccos(cos_angle)

def is_unit_vector(self):
    """
    Test if this is a unit vector (norm = 1).
    
    Only meaningful for positive definite forms.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: e.is_unit_vector()
        True
        sage: (2*e).is_unit_vector()
        False
        sage: (e + f).normalize().is_unit_vector()
        True
    """
    if not self.parent().is_positive_definite():
        raise ValueError("Unit vectors only defined for positive definite forms")
    
    return self.norm_squared() == 1

def normalize(self):
    """
    Return normalized version of this vector.
    
    Only works for non-isotropic vectors in positive definite forms.
    
    OUTPUT:
    Unit vector in same direction
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: u = v.normalize()
        sage: u.is_unit_vector()
        True
        sage: u.norm()
        1
    """
    if not self.parent().is_positive_definite():
        raise ValueError("Normalization only defined for positive definite forms")
    
    norm = self.norm()
    if norm == 0:
        raise ValueError("Cannot normalize zero vector")
    
    return self / norm

def unit_vector(self):
    """Alias for normalize()."""
    return self.normalize()
```

## Orthogonal Projections and Reflections

```python
def orthogonal_projection_onto(self, other):
    """
    Compute orthogonal projection of self onto other.
    
    proj_other(self) = b(self,other)/b(other,other) * other
    
    INPUT:
    - other -- non-isotropic element to project onto
    
    OUTPUT:
    Element representing the projection
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: proj_e = v.orthogonal_projection_onto(e)
        sage: proj_e
        3*e
        
        sage: # Verify projection property
        sage: (v - proj_e).is_orthogonal_to(e)
        True
    """
    if other.is_isotropic():
        raise ValueError("Cannot project onto isotropic vector")
    
    other_norm_sq = other.norm_squared()
    if other_norm_sq == 0:
        raise ValueError("Cannot project onto zero vector")
    
    coeff = self.bilinear_form(other) / other_norm_sq
    return coeff * other

def orthogonal_component_to(self, other):
    """
    Return component orthogonal to other.
    
    This is self minus its projection onto other.
    
    INPUT:
    - other -- element to be orthogonal to
    
    OUTPUT:
    Element orthogonal to other
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: perp = v.orthogonal_component_to(e)
        sage: perp
        4*f
        sage: perp.is_orthogonal_to(e)
        True
    """
    if other.is_isotropic():
        # For isotropic vectors, cannot use standard projection formula
        raise ValueError("Orthogonal component to isotropic vector not well-defined")
    
    projection = self.orthogonal_projection_onto(other)
    return self - projection

def reflect_across_hyperplane(self, normal):
    """
    Reflect this vector across hyperplane perpendicular to normal.
    
    For hyperplane H_n = {v : b(v,n) = 0}, the reflection is:
    ref_n(v) = v - 2 * b(v,n)/b(n,n) * n
    
    INPUT:
    - normal -- normal vector to hyperplane (non-isotropic)
    
    OUTPUT:
    Reflected vector
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: # Reflect across line perpendicular to e (i.e., across y-axis)
        sage: reflected = v.reflect_across_hyperplane(e)
        sage: reflected
        -3*e + 4*f
    """
    if normal.is_isotropic():
        raise ValueError("Cannot reflect across hyperplane with isotropic normal")
    
    normal_norm_sq = normal.norm_squared()
    if normal_norm_sq == 0:
        raise ValueError("Normal vector cannot be zero")
    
    # Reflection formula: v - 2 * proj_n(v)
    proj_coeff = self.bilinear_form(normal) / normal_norm_sq
    return self - 2 * proj_coeff * normal

def householder_reflection(self):
    """
    Householder reflection that maps this vector to its norm times e₁.
    
    For non-zero vector v, constructs reflection H such that
    H(v) = ||v|| * e₁ where e₁ is first basis vector.
    
    OUTPUT:
    Dictionary with reflection data
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: refl_data = v.householder_reflection()
        sage: # refl_data contains reflection vector and matrix
    """
    if self.is_zero():
        raise ValueError("Cannot construct Householder reflection for zero vector")
    
    # Standard Householder algorithm
    norm_v = self.norm()
    e1 = self.parent().gen(0)  # First basis vector
    
    # Choose sign to avoid cancellation
    if self.coefficient(0) >= 0:
        w = self + norm_v * e1
    else:
        w = self - norm_v * e1
    
    w_normalized = w.normalize() if not w.is_zero() else w
    
    return {
        'reflection_vector': w_normalized,
        'target': norm_v * e1,
        'norm': norm_v
    }
```

## Inner Product Space Operations

```python
def gram_schmidt_coefficient(self, orthogonal_basis):
    """
    Compute Gram-Schmidt coefficients relative to orthogonal basis.
    
    Expresses self = Σ cᵢ bᵢ where {bᵢ} is orthogonal basis.
    
    INPUT:
    - orthogonal_basis -- list of mutually orthogonal elements
    
    OUTPUT:
    List of coefficients
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: coeffs = v.gram_schmidt_coefficient([e, f])
        sage: coeffs
        [3, 4]
    """
    coefficients = []
    
    for basis_vector in orthogonal_basis:
        if basis_vector.is_isotropic():
            # Skip isotropic vectors in Gram-Schmidt
            coefficients.append(0)
        else:
            coeff = self.bilinear_form(basis_vector) / basis_vector.norm_squared()
            coefficients.append(coeff)
    
    return coefficients

def inner_product(self, other):
    """
    Alias for bilinear_form (emphasizes positive definite case).
    
    INPUT:
    - other -- another element
    
    OUTPUT:
    Inner product ⟨self, other⟩
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: w = 2*e - f
        sage: v.inner_product(w)
        2  # 3*2 + 4*(-1) = 6 - 4 = 2
    """
    return self.bilinear_form(other)

def dot_product(self, other):
    """Alias for inner_product."""
    return self.inner_product(other)

def __mul__(self, other):
    """
    Overload * for inner product (when both are vectors).
    
    This is contextual - may conflict with scalar multiplication.
    Use inner_product() for clarity.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: w = 2*e - f
        sage: v * w  # Inner product
        2
        sage: 3 * v  # Scalar multiplication
        9*e + 12*f
    """
    if hasattr(other, 'parent') and other.parent() == self.parent():
        return self.inner_product(other)
    else:
        # Delegate to scalar multiplication
        return super().__rmul__(other)
```

## Arithmetic Extensions

```python
def __pow__(self, n):
    """
    Power operation for quadratic forms.
    
    v^n could mean various things:
    - v^2 = q(v) (quadratic form evaluation)
    - v^n = v * v * ... * v (not well-defined for vectors)
    
    We implement v^2 as quadratic form evaluation.
    
    EXAMPLES::
    
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = SymmetricBilinearModule(G)
        sage: e, f = M.gens()
        sage: v = 3*e + 4*f
        sage: v^2
        25  # Same as v.quadratic_form()
    """
    if n == 2:
        return self.quadratic_form()
    elif n == 0:
        return self.parent().base_ring().one()
    elif n == 1:
        return self
    else:
        raise ValueError(f"Power {n} not defined for vectors")

def conjugate(self):
    """
    Complex conjugate (for forms over C).
    
    For real forms, this is the identity.
    For complex forms, conjugates coefficients.
    """
    base_ring = self.parent().base_ring()
    
    if hasattr(base_ring, 'conjugate'):
        # Complex or other field with conjugation
        conjugated_coeffs = {}
        for key, coeff in self:
            conjugated_coeffs[key] = coeff.conjugate()
        return self.parent()._from_dict(conjugated_coeffs)
    else:
        # Real field - no change
        return self

def real_part(self):
    """Real part (for complex vector spaces)."""
    if hasattr(self.parent().base_ring(), 'real_field'):
        real_coeffs = {}
        for key, coeff in self:
            real_coeffs[key] = coeff.real()
        return self.parent()._from_dict(real_coeffs)
    else:
        return self

def imaginary_part(self):
    """Imaginary part (for complex vector spaces)."""
    if hasattr(self.parent().base_ring(), 'real_field'):
        imag_coeffs = {}
        for key, coeff in self:
            imag_coeffs[key] = coeff.imag()
        return self.parent()._from_dict(imag_coeffs)
    else:
        return self.parent().zero()
```

## Category Method Integration

```python
# From SymmetricBilinearModules.ElementMethods:
def quadratic_form(self):
    """Quadratic form evaluation q(v) = b(v,v)."""
    pass

def is_isotropic(self):
    """Test if q(v) = 0."""
    pass

def norm_squared(self):
    """Squared norm for definite forms."""
    pass

# From PositiveDefinite axiom:
def norm(self):
    """Euclidean norm for positive definite forms."""
    pass

def normalize(self):
    """Unit vector in same direction."""
    pass

def angle_with(self, other):
    """Angle between vectors."""
    pass

# From Indefinite axiom:
def is_positive(self):
    """Test if q(v) > 0."""
    pass

def is_negative(self):
    """Test if q(v) < 0."""
    pass

def sign(self):
    """Sign of quadratic form."""
    pass
```

## Usage Examples

```python
# Create symmetric bilinear module and elements
sage: G = matrix(QQ, [[2, -1], [-1, 3]])
sage: M = SymmetricBilinearModule(G)
sage: e, f = M.gens()
sage: v = 2*e + f
sage: w = e - 2*f

# Quadratic forms
sage: v.quadratic_form()
9
sage: w.quadratic_form()
8

# Symmetry verification
sage: v.bilinear_form(w) == w.bilinear_form(v)
True

# Geometric operations (for positive definite forms)
sage: H = matrix(QQ, [[1, 0], [0, 1]])
sage: N = SymmetricBilinearModule(H)
sage: x, y = N.gens()
sage: u = 3*x + 4*y
sage: u.norm()
5
sage: u.normalize().is_unit_vector()
True

# Projections
sage: proj = u.orthogonal_projection_onto(x)
sage: proj
3*x
sage: (u - proj).is_orthogonal_to(x)
True

# Isotropic vectors (indefinite forms)
sage: L = matrix(QQ, [[1, 0], [0, -1]])
sage: P = SymmetricBilinearModule(L)
sage: a, b = P.gens()
sage: isotropic = a + b
sage: isotropic.is_isotropic()
True
sage: isotropic.quadratic_form()
0

# Reflections
sage: reflected = u.reflect_across_hyperplane(x)
sage: reflected
-3*x + 4*y
```

## Mathematical Properties

Elements maintain these mathematical properties specific to symmetric forms:

```python
# Mathematical assertion: Quadratic form
# q(v) = b(v,v) for all v

# Mathematical assertion: Polarization identity
# b(v,w) = (q(v+w) - q(v) - q(w))/2

# Mathematical assertion: Homogeneity
# q(rv) = r² q(v) for all r ∈ R

# Mathematical assertion: Parallelogram law (positive definite)
# ||v + w||² + ||v - w||² = 2(||v||² + ||w||²)

# Mathematical assertion: Cauchy-Schwarz inequality (positive definite)
# |b(v,w)| ≤ ||v|| ||w||

# Mathematical assertion: Triangle inequality (positive definite)
# ||v + w|| ≤ ||v|| + ||w||

# Mathematical assertion: Isotropic characterization
# v is isotropic ⟺ q(v) = 0

# Mathematical assertion: Orthogonal projection property
# proj_u(v) minimizes ||v - w|| over all w ∈ span(u)
```

This element class provides natural quadratic form operations while maintaining full compatibility with the symmetric bilinear module structure and category framework.