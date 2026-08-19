<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/bilinear_Rmod_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: FreeBilinearModules(ZZ)

Elements of free modules with bilinear forms. Inherits from FreeModules elements.

## Bilinear Form Operations

```python
def __mul__(self, other):
    r"""
    Multiplication: bilinear form evaluation or scalar multiplication.
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: v = M([2, 3])
        sage: w = M([1, -1])
        
    Element * Element gives bilinear form value::
    
        sage: v * w
        -1
        sage: w * v  # May differ for non-symmetric forms
        -1
        
    Element * Scalar gives scalar multiplication::
    
        sage: v * 2
        (4, 6)
        sage: 3 * v
        (6, 9)
        
    Basis vectors demonstrate the form::
    
        sage: e1, e2 = M.basis()
        sage: e1 * e1
        0
        sage: e1 * e2
        1
        sage: e2 * e1
        1
        sage: e2 * e2
        0
    
    INPUT:
    - other: Another element of the same module or a scalar
    
    OUTPUT:
    The bilinear form value (if other is an element) or scaled element (if scalar).
    """

def evaluate_form(self, other):
    r"""
    Explicit evaluation of the bilinear form.
    
    Same as __mul__ but more explicit for readability.
    """

def is_orthogonal_to(self, other):
    r"""
    Test if this element is orthogonal to another.
    
    For general bilinear forms, tests if self * other = 0.
    WARNING: This may not be symmetric! For non-symmetric forms,
    v.is_orthogonal_to(w) might differ from w.is_orthogonal_to(v).
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))  # Symmetric
        sage: v = M([1, 0])
        sage: w = M([0, 1])
        sage: v.is_orthogonal_to(w)
        True
        sage: w.is_orthogonal_to(v)  # Same for symmetric forms
        True
        
    For non-symmetric forms, orthogonality may not be symmetric::
    
        sage: N = BilinearModule(matrix(ZZ, [[1, 2], [3, 4]]))
        sage: u = N([1, 0])
        sage: z = N([-2, 1])
        sage: u.is_orthogonal_to(z)  # u * z = 0
        True
        sage: z.is_orthogonal_to(u)  # z * u ≠ 0
        False
    
    Returns True if ⟨self, other⟩ = 0.
    """
```

## Form Properties

```python
def orthogonal_complement(self):
    r"""
    Return the orthogonal complement of this element.
    
    The set {w ∈ M : ⟨v, w⟩ = 0}.
    """

def is_isotropic(self):
    r"""
    Test if this element has zero self-pairing: ⟨v,v⟩ = 0.
    
    An element is isotropic if it lies on the "light cone" of the bilinear form.
    
    OUTPUT:
    True if self * self = 0, False otherwise
    
    EXAMPLES::
    
        sage: # Definite form - no isotropic vectors except zero
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 2]]))
        sage: v = M([1, 0])
        sage: v.is_isotropic()
        False
        sage: v * v
        2
        
        sage: # Hyperbolic form - has isotropic vectors
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: u = H([1, 1])
        sage: u.is_isotropic()
        True
        sage: u * u
        0
        sage: w = H([1, 0])
        sage: w.is_isotropic()
        True
        sage: w * w
        0
        
        sage: # Alternating form - all vectors are isotropic to themselves
        sage: A = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))
        sage: z = A([2, 3])
        sage: z.is_isotropic()
        True
        sage: z * z
        0
    """

def represents(self, k):
    r"""
    Test if this element represents the value k.
    
    Check if the quadratic form evaluation equals k: self * self = k.
    
    INPUT:
    - k: Element of the base ring to test
    
    OUTPUT:
    True if self * self = k, False otherwise
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: v = M([1, 0])
        sage: v.represents(2)
        True
        sage: v * v
        2
        sage: v.represents(3)
        False
        
        sage: w = M([0, 1])
        sage: w.represents(3)
        True
        sage: w * w
        3
        
        sage: # Zero vector represents 0
        sage: zero = M([0, 0])
        sage: zero.represents(0)
        True
        sage: zero.represents(1)
        False
    """
```