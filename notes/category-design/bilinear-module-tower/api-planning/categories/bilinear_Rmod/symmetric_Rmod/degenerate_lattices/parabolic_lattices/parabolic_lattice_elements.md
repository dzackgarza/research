<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/degenerate_lattices/parabolic_lattices/parabolic_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: ParabolicLattices

Elements of parabolic lattices (1-dimensional radical). Inherits from DegenerateLattices elements.

## Parabolic Structure

```python
def level(self):
    r"""
    Return the level of this element.
    
    In affine root systems, this is the coefficient of the affine root.
    """

def height_function_value(self):
    r"""
    Compute the value of the height function at this element.
    
    The height function measures distance from the hyperplane at infinity.
    """

def is_real_root(self):
    r"""Test if this is a real root in the affine root system."""
    
def is_imaginary_root(self):
    r"""Test if this is an imaginary root (multiple of null root)."""
```

## Affine Geometry

```python
def affine_hyperplane_distance(self):
    r"""
    Compute distance to the affine hyperplane.
    
    In parabolic lattices, there's a distinguished hyperplane.
    """

def cusp_projection(self):
    r"""
    Project this element to the cusp at infinity.
    
    Related to the parabolic structure.
    """
```

## Affine Root Systems

```python
def null_root_coefficient(self):
    r"""
    Return the coefficient of the null root δ.
    
    Every element can be written as sum of finite roots plus multiple of δ.
    """

def finite_part(self):
    r"""
    Return the finite root system component.
    
    Projection to the quotient by the radical.
    """

def affine_weyl_orbit(self):
    r"""Return the affine Weyl group orbit of this element."""
```