<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/indefinite_lattices/hyperbolic_lattices/hyperbolic_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: HyperbolicLattices

Elements of hyperbolic lattices (Lorentzian signature). Inherits from IndefiniteLattices elements.

## Hyperbolic Geometry

```python
def hyperbolic_distance_to(self, other):
    r"""
    Compute hyperbolic distance to another element.
    
    Only defined for timelike vectors in Lorentzian signature.
    """

def hyperbolic_angle_with(self, other):
    r"""
    Compute hyperbolic angle between two timelike vectors.
    """

def is_future_pointing(self):
    r"""Test if this timelike vector points to the future."""
    
def is_past_pointing(self):
    r"""Test if this timelike vector points to the past."""
```

## Vinberg Theory

```python
def reflection_hyperplane(self):
    r"""
    Return the reflection hyperplane for this root.
    
    In hyperbolic space, this corresponds to a geodesic hyperplane.
    """

def fundamental_domain_chamber(self):
    r"""
    Determine which fundamental domain chamber contains this vector.
    
    Used in Vinberg's algorithm for hyperbolic reflection groups.
    """

def vinberg_distance(self):
    r"""
    Compute distance from this vector to the fundamental domain boundary.
    """
```