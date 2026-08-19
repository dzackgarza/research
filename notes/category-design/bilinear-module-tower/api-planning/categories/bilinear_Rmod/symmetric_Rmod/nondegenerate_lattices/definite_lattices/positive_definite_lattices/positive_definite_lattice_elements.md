<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/positive_definite_lattices/positive_definite_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: PositiveDefiniteLattices

Elements of positive definite lattices. Inherits from DefiniteLattices elements.

## Euclidean Properties

```python
def euclidean_norm(self):
    r"""
    Return the Euclidean norm of this element.
    
    For positive definite lattices: ||v|| = sqrt(⟨v,v⟩).
    """

def euclidean_distance_to(self, other):
    r"""
    Compute Euclidean distance to another element.
    
    Distance = ||v - w|| in the Euclidean metric.
    """

def angle_with(self, other):
    r"""
    Compute the angle between this element and another.
    
    Returns angle in [0, π] using the Euclidean inner product.
    """
```

## Lattice Reduction

```python
def lll_reduced(self):
    r"""
    Return the LLL-reduced representative of this element.
    
    Uses the Lenstra-Lenstra-Lovász algorithm.
    """

def is_lll_reduced(self):
    r"""Test if this element is LLL-reduced."""

def shortest_equivalent(self):
    r"""
    Find the shortest vector equivalent to this one.
    
    Uses lattice reduction techniques.
    """
```

## Sphere Packing

```python
def packing_density_contribution(self):
    r"""
    Compute this vector's contribution to packing density.
    """

def kissing_number_neighbors(self):
    r"""
    Find all vectors at minimal distance from this one.
    
    Related to the kissing number problem.
    """
```