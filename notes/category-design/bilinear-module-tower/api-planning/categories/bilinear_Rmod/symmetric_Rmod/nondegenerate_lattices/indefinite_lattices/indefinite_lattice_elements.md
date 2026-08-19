<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/indefinite_lattices/indefinite_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: IndefiniteLattices

Elements of indefinite lattices. Inherits from Lattices elements.

## Cone Structure

```python
def positive_cone_projection(self):
    r"""
    Project this element onto the positive cone.
    
    For indefinite lattices with signature (p,q), the positive cone
    is the set of vectors with positive norm.
    """

def negative_cone_projection(self):
    r"""
    Project this element onto the negative cone.
    
    The set of vectors with negative norm.
    """

def is_lightlike(self):
    r"""Test if this element has zero norm (lies on light cone)."""

def is_timelike(self):
    r"""Test if this element has positive norm."""
    
def is_spacelike(self):
    r"""Test if this element has negative norm."""
```

## Lorentzian Operations

```python
def causal_class(self):
    r"""
    Return the causal class of this element.
    
    OUTPUT:
    'timelike', 'spacelike', 'lightlike', or 'zero'
    """

def lorentz_boost(self, direction):
    r"""
    Apply a Lorentz boost in the given direction.
    
    Only meaningful for Lorentzian signature lattices.
    """
```