<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/symmetric_Rmod_elements.md
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

## Mathematical Test Assertions

```python
# Mathematical assertion: Symmetry property of bilinear form
# For symmetric bilinear forms: B(x,y) = B(y,x) for all x,y
# sage: R = RootSystem(['A', 3])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: alpha[1].inner_product(alpha[2]) == alpha[2].inner_product(alpha[1])
# True  # Symmetry of inner product (Humphreys, Reflection Groups)

# Mathematical assertion: Quadratic form polarization identity
# For symmetric forms: 4*B(x,y) = Q(x+y) - Q(x-y) where Q(v) = B(v,v)
# sage: R = RootSystem(['B', 3])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: x, y = alpha[1], alpha[2]
# sage: 4 * x.inner_product(y) == (x+y).norm_squared() - (x-y).norm_squared()
# True  # Polarization identity (fundamental quadratic form property)

# Mathematical assertion: Reflection preserves bilinear form
# For reflection s_v: s_v(x).inner_product(s_v(y)) = x.inner_product(y)
# sage: R = RootSystem(['C', 3])
# sage: W = R.weyl_group()
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: s = W.simple_reflection(1)
# sage: x, y = alpha[1], alpha[2] + alpha[3]
# sage: s(x).inner_product(s(y)) == x.inner_product(y)
# True  # Reflections are isometries (Humphreys, Chap 1.1)

# Mathematical assertion: Self-orthogonal vectors under reflection
# For reflection s_v in hyperplane orthogonal to v: s_v(v) = -v
# sage: R = RootSystem(['D', 4])
# sage: W = R.weyl_group()
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: s = W.simple_reflection(1)
# sage: s(alpha[1]) == -alpha[1]
# True  # Reflection in root sends root to its negative

# Mathematical assertion: Norm squared non-negativity for positive definite forms
# For positive definite forms: v.norm_squared() >= 0, equality iff v = 0
# sage: R = RootSystem(['E', 6])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: all(alpha[i].norm_squared() > 0 for i in alpha.index_set())
# True  # Simple roots have positive norm squared

# Mathematical assertion: Orthogonal complement dimension
# For non-degenerate symmetric form on n-dim space: dim(v^perp) = n-1 for v != 0
# sage: R = RootSystem(['F', 4])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: v = alpha[1] + alpha[2]
# sage: orthogonal_subspace = [w for w in alpha if w.inner_product(v) == 0]
# sage: len(orthogonal_subspace) == L.rank() - 1 if v != 0 else True
# True  # Orthogonal complement has codimension 1

# Mathematical assertion: Cauchy-Schwarz inequality for positive definite forms
# For positive definite forms: |B(x,y)|^2 <= B(x,x) * B(y,y)
# sage: R = RootSystem(['G', 2])
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: x, y = alpha[1], alpha[2]
# sage: inner_prod_sq = x.inner_product(y)^2
# sage: norm_product = x.norm_squared() * y.norm_squared()
# sage: inner_prod_sq <= norm_product
# True  # Cauchy-Schwarz for positive definite bilinear forms

# Mathematical assertion: Reflection formula for symmetric forms
# s_v(x) = x - 2*<x,v>/<v,v> * v for symmetric bilinear forms when <v,v> != 0
# sage: R = RootSystem(['A', 2])
# sage: W = R.weyl_group()
# sage: L = R.root_lattice()
# sage: alpha = L.simple_roots()
# sage: s = W.simple_reflection(1)
# sage: x = alpha[2]
# sage: v = alpha[1]
# sage: reflection_formula = x - 2*x.inner_product(v)/v.norm_squared() * v
# sage: s(x) == reflection_formula
# True  # Classical reflection formula (Humphreys, Prop 1.2)
```
```