<!--
Origin: gitclones/Coxeter/implementation/planning/RMod/RMod_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Elements: R-Module Element Implementation

Element class implementation for R-modules with symbolic computation and coordinate conversion.

## Element Class Structure

```python
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class RModuleElement(IndexedFreeModuleElement):
    """
    Element of an R-module with symbolic and numerical representations.
    
    This class provides:
    - Symbolic arithmetic with natural notation
    - Coordinate vector conversion
    - Efficient coefficient access
    - Integration with parent module structure
    
    Supports natural arithmetic and efficient conversion between
    symbolic and numerical representations.
    
    EXAMPLES::
    
        sage: M.<e,f> = RMod(ZZ)
        sage: v = 2*e + 3*f
        sage: w = e - f
        sage: v + w
        3*e + 2*f
        sage: 4*v
        8*e + 12*f
        
        sage: # Coordinate conversion
        sage: v.to_vector()
        (2, 3)
        sage: v.coefficient('e')
        2
    """
    
    def to_vector(self):
        """
        Convert this element to a coordinate vector.
        
        Returns a vector over the base ring with coordinates
        relative to the module's basis.
        
        EXAMPLES::
        
            sage: M.<a,b,c> = RMod(QQ)
            sage: v = a + 2*b - 3*c
            sage: v.to_vector()
            (1, 2, -3)
            
            sage: # Type is vector over base ring
            sage: type(v.to_vector())
            <class 'sage.modules.vector_rational_dense.Vector_rational_dense'>
            sage: v.to_vector().parent()
            Vector space of dimension 3 over Rational Field
        """
        return self.parent()._to_vector(self)
    
    def _numerical_(self):
        """
        Numerical representation via n() function.
        
        This allows using n(element) to get coordinate vector.
        
        EXAMPLES::
        
            sage: M.<e,f> = RMod(ZZ)
            sage: n(e)
            (1, 0)
            sage: n(2*e + 3*f)
            (2, 3)
            sage: n(e - f)
            (1, -1)
            
            sage: # The n() function calls _numerical_
            sage: (3*e + 2*f)._numerical_()
            (3, 2)
        """
        return self.to_vector()
```

## Element Properties and Access

```python
def coefficient(self, basis_key):
    """
    Return the coefficient of a basis element.
    
    INPUT:
    - basis_key -- key identifying a basis element
    
    OUTPUT:
    The coefficient of the specified basis element
    
    EXAMPLES::
    
        sage: M.<x,y,z> = RMod(ZZ)
        sage: v = 3*x - 2*y + 5*z
        sage: v.coefficient('y')
        -2
        sage: v.coefficient('x')
        3
        sage: v.coefficient('w')  # Not a basis element
        0
        
        sage: # Can also use basis indices
        sage: M = RModule_with_basis(QQ, basis=['a', 'b', 'c'])
        sage: a, b, c = M.gens()
        sage: v = 2*a - 3*c
        sage: v.coefficient('a')
        2
        sage: v.coefficient('c')
        -3
    """
    # Handle both string keys and indices
    if isinstance(basis_key, (int, Integer)):
        if basis_key < len(self.parent()._basis_keys):
            basis_key = self.parent()._basis_keys[basis_key]
        else:
            return self.parent().base_ring().zero()
    
    return self.get(basis_key, self.parent().base_ring().zero())

def support(self):
    """
    Return the support (non-zero basis elements).
    
    The support is the set of basis elements with non-zero coefficients.
    
    OUTPUT:
    List of basis keys for which this element has non-zero coefficients
    
    EXAMPLES::
    
        sage: M.<a,b,c> = RMod(QQ)
        sage: v = 2*a - 3*c
        sage: v.support()
        ['a', 'c']
        
        sage: # Zero element has empty support
        sage: M.zero().support()
        []
        
        sage: # All basis elements
        sage: w = a + b + c
        sage: w.support()
        ['a', 'b', 'c']
    """
    return [key for key, coeff in self._monomial_coefficients.items() if coeff != 0]

def is_zero(self):
    """
    Check if this is the zero element.
    
    Fundamental operation valid for all R-module elements.
    
    OUTPUT:
    Boolean - True if this element is zero, False otherwise
    
    EXAMPLES::
    
        sage: M.<e,f> = RMod(ZZ)
        sage: (e - e).is_zero()
        True
        sage: e.is_zero()
        False
        sage: M.zero().is_zero()
        True
        
        sage: # Addition preserves zero testing
        sage: (2*e - 2*e + 3*f - 3*f).is_zero()
        True
    """
    return len(self._monomial_coefficients) == 0

def leading_coefficient(self):
    """
    Return the leading coefficient.
    
    Uses the natural ordering on basis elements.
    
    EXAMPLES::
    
        sage: M.<x,y,z> = RMod(QQ)
        sage: v = 3*y - 2*x + z
        sage: v.leading_coefficient()
        -2  # coefficient of first basis element x
    """
    if self.is_zero():
        return self.parent().base_ring().zero()
    
    parent = self.parent()
    if parent._basis_keys:
        # Use basis ordering
        for key in parent._basis_keys:
            if key in self._monomial_coefficients:
                return self._monomial_coefficients[key]
    
    # Fallback to arbitrary ordering
    return next(iter(self._monomial_coefficients.values()))

def leading_term(self):
    """
    Return the leading term (leading coefficient times leading monomial).
    
    EXAMPLES::
    
        sage: M.<a,b,c> = RMod(ZZ)
        sage: v = 3*b - 2*a + 5*c
        sage: v.leading_term()
        -2*a  # first term in basis order
    """
    if self.is_zero():
        return self.parent().zero()
    
    parent = self.parent()
    if parent._basis_keys:
        # Use basis ordering
        for key in parent._basis_keys:
            if key in self._monomial_coefficients:
                coeff = self._monomial_coefficients[key]
                return parent._from_dict({key: coeff})
    
    # Fallback
    key, coeff = next(iter(self._monomial_coefficients.items()))
    return parent._from_dict({key: coeff})
```

## Structure Access

```python
def terms(self):
    """
    Return list of non-zero terms.
    
    Each term is an element of the form coefficient * basis_element.
    
    EXAMPLES::
    
        sage: M.<x,y,z> = RMod(QQ)
        sage: v = 2*x - 3*y + z
        sage: terms = v.terms()
        sage: len(terms)
        3
        sage: 2*x in terms
        True
        sage: -3*y in terms
        True
    """
    parent = self.parent()
    return [parent._from_dict({key: coeff}) 
            for key, coeff in self._monomial_coefficients.items()
            if coeff != 0]

def monomials(self):
    """
    Return list of monomials (basis elements) with non-zero coefficients.
    
    EXAMPLES::
    
        sage: M.<a,b,c> = RMod(ZZ)
        sage: v = 3*a - 2*c
        sage: monomials = v.monomials()
        sage: len(monomials)
        2
        sage: a in monomials
        True
        sage: c in monomials
        True
        sage: b in monomials
        False
    """
    parent = self.parent()
    return [parent.monomial(key) for key in self.support()]

def coefficients(self):
    """
    Return list of non-zero coefficients.
    
    The coefficients are returned in the same order as support().
    
    EXAMPLES::
    
        sage: M.<x,y,z> = RMod(QQ)  
        sage: v = 2*x - 3*z
        sage: v.coefficients()
        [2, -3]
        sage: v.support()
        ['x', 'z']
    """
    return [self._monomial_coefficients[key] for key in self.support()]

def __iter__(self):
    """
    Iterate over (basis_key, coefficient) pairs.
    
    Only includes non-zero coefficients.
    
    EXAMPLES::
    
        sage: M.<a,b,c> = RMod(ZZ)
        sage: v = 2*a - 3*c
        sage: list(v)
        [('a', 2), ('c', -3)]
        
        sage: # Can unpack in loops
        sage: for key, coeff in v:
        ....:     print(f"{key}: {coeff}")
        a: 2
        c: -3
    """
    return ((key, coeff) for key, coeff in self._monomial_coefficients.items() if coeff != 0)

def __bool__(self):
    """
    Boolean conversion - True if non-zero.
    
    EXAMPLES::
    
        sage: M.<e,f> = RMod(ZZ)
        sage: bool(e)
        True
        sage: bool(M.zero())
        False
        sage: bool(2*e - 2*e)
        False
    """
    return not self.is_zero()
```

## Arithmetic Operations

```python
# Arithmetic operations (inherited from IndexedFreeModuleElement but documented)

def __add__(self, other):
    """
    Addition of R-module elements.
    
    Universal for all R-modules - abelian group operation.
    
    EXAMPLES::
    
        sage: M.<x,y> = RMod(ZZ)
        sage: (2*x + 3*y) + (x - 2*y)
        3*x + y
    """
    # Implementation inherited from IndexedFreeModuleElement
    return super().__add__(other)

def __rmul__(self, scalar):
    """
    Scalar multiplication by ring elements.
    
    Universal R-module operation: r * v for r in R, v in module.
    
    EXAMPLES::
    
        sage: M.<a,b> = RMod(ZZ)
        sage: 3 * (2*a - b)
        6*a - 3*b
        
        sage: # Works with base ring elements
        sage: v = a + b
        sage: (-1) * v
        -a - b
    """
    # Implementation inherited from IndexedFreeModuleElement
    return super().__rmul__(scalar)

def __neg__(self):
    """
    Negation of module elements.
    
    EXAMPLES::
    
        sage: M.<x,y> = RMod(QQ)
        sage: v = 2*x - 3*y
        sage: -v
        -2*x + 3*y
    """
    return super().__neg__()

def __sub__(self, other):
    """
    Subtraction of module elements.
    
    EXAMPLES::
    
        sage: M.<a,b> = RMod(ZZ)
        sage: (3*a + 2*b) - (a - b)
        2*a + 3*b
    """
    return super().__sub__(other)
```

## Category Methods Integration

The element class automatically gains methods from the category framework:

```python
# From RModules(R).ElementMethods:
def is_zero(self):
    """Check if this is the zero element."""
    # Fundamental operation valid for all R-module elements
    pass

# From RModules(R).WithBasis().ElementMethods:  
def to_vector(self):
    """Convert to coordinate vector."""
    pass

def coefficient(self, basis_key):
    """Return coefficient of basis element."""
    pass

def support(self):
    """Return support (non-zero basis elements)."""
    pass
```

## Usage Examples

```python
# Basic symbolic computation
sage: M.<e,f,g> = RMod(ZZ)
sage: v = 2*e + 3*f - g
sage: w = e - 2*f + 4*g
sage: v + w
3*e + f + 3*g

# Coordinate conversion
sage: v.to_vector()
(2, 3, -1)
sage: n(v)  # Shorthand via _numerical_
(2, 3, -1)

# Coefficient access
sage: v.coefficient('f')
3
sage: v.coefficient('g')
-1

# Support and structure
sage: v.support()
['e', 'f', 'g']
sage: v.leading_coefficient()
2
sage: v.leading_term()
2*e

# Boolean and iteration
sage: bool(v)
True
sage: bool(M.zero())
False
sage: list(v)
[('e', 2), ('f', 3), ('g', -1)]
```

## Construction and Conversion

```python
# Construction from coordinates
sage: M = RModule_with_basis(QQ, basis=['x', 'y', 'z'])
sage: M([1, 2, -1])
x + 2*y - z

# Construction from coefficient dict
sage: M({'x': 3, 'z': -2})
3*x - 2*z

# Round-trip conversion
sage: v = 2*x - 3*y + z
sage: coords = v.to_vector()
sage: M._from_vector(coords) == v
True

# Numerical function integration
sage: n(v) == coords
True
sage: v == M(n(v))
True
```

## Mathematical Properties

Elements automatically inherit mathematical properties based on their module's category:

- **All R-modules**: Abelian group structure, zero testing
- **Free modules**: Basis representation, rank computations  
- **WithBasis modules**: Coordinate conversion, coefficient access
- **FinitelyGenerated modules**: Finite support properties

This ensures elements behave correctly mathematically while providing computational efficiency through the symbolic/numerical dual representation.