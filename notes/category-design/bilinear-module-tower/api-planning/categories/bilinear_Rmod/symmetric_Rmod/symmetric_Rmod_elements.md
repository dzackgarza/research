<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/symmetric_Rmod_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: SymmetricBilinearModules

Elements of modules with symmetric bilinear forms. Inherits from FreeBilinearModules elements.

## Symmetric Form Properties

```python
def norm_squared(self):
    r"""
    Return the squared norm of this element.
    
    For symmetric forms: norm²(v) = ⟨v, v⟩.
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: v = M([1, 2])
        sage: v.norm_squared()
        11
        sage: v * v  # Same as norm_squared for symmetric forms
        11
        
    For indefinite forms, the norm squared can be negative::
    
        sage: H = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))
        sage: w = H([3, 4])
        sage: w.norm_squared()
        -7
    """

def norm(self):
    r"""
    Return the norm of this element (when it makes sense).
    
    For positive definite forms, this is sqrt(⟨v,v⟩).
    For other signatures, may return complex or be undefined.
    """

def quadratic_form_value(self):
    r"""
    Return the value of the associated quadratic form.
    
    Same as norm_squared() but emphasizes quadratic form viewpoint.
    """
```

## Orthogonal Operations

```python
def orthogonal_hyperplane(self):
    r"""
    Return the hyperplane orthogonal to this element.
    
    The hyperplane H_v = {w ∈ M : ⟨w, v⟩ = 0}.
    """

def radical_projection(self):
    r"""
    Project this element onto the radical of the form.
    
    Returns the component of v that lies in rad(M).
    """

def is_in_radical(self):
    r"""Test if this element lies in the radical of the form."""

def reflection(self):
    r"""
    Return the reflection in the hyperplane orthogonal to this element.
    
    The reflection s_v(x) = x - 2⟨x,v⟩/⟨v,v⟩ v is always defined
    for symmetric bilinear forms (when ⟨v,v⟩ ≠ 0).
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(QQ, [[2, 1], [1, 2]]))
        sage: v = M([1, 0])
        sage: r = v.reflection()
        sage: r
        Reflection in (1, 0)
        
    Apply the reflection to a vector::
    
        sage: w = M([3, 2])
        sage: r(w)
        (-1, 0)
        
    Reflections preserve the bilinear form::
    
        sage: u1 = M([1, 1])
        sage: u2 = M([0, 1])
        sage: u1 * u2
        3
        sage: r(u1) * r(u2)
        3
        
    Cannot reflect in an isotropic vector::
    
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: z = H([1, 0])
        sage: z.norm_squared()
        0
        sage: z.reflection()
        Traceback (most recent call last):
        ...
        ValueError: cannot reflect in isotropic vector
    
    OUTPUT: Linear transformation on the ambient module
    
    NOTE: This reflection preserves the bilinear form but may only 
    preserve the lattice structure for special vectors (roots).
    """

def reflection_matrix(self):
    r"""
    Return the matrix representation of the reflection in this vector.
    
    Computed with respect to the ambient module's basis.
    """
```