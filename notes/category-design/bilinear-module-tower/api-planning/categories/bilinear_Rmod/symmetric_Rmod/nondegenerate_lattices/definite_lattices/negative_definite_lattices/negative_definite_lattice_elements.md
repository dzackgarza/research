<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/negative_definite_lattices/negative_definite_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: NegativeDefiniteLattices

Elements of negative definite lattices. Inherits from DefiniteLattices elements.

## Negative Definite Properties

```python
def negative_norm(self):
    r"""
    Return the norm with respect to the negative definite form.
    
    For negative definite lattices: ||v||² = -⟨v,v⟩ > 0.
    """

def negative_distance_to(self, other):
    r"""
    Compute distance using the negative definite metric.
    """
```

## Coxeter Groups

```python
def coxeter_reflection_length(self):
    r"""
    Compute the reflection length in the Weyl group.
    
    The minimal number of simple reflections needed to reach this element.
    """

def alcove_walk_path(self):
    r"""
    Return a path in the alcove complex to this element.
    
    Used in algebraic combinatorics and representation theory.
    """
```

## Algebraic Geometry

```python
def intersection_multiplicity(self, other):
    r"""
    Compute intersection multiplicity with another element.
    
    Relevant for algebraic geometry applications.
    """

def canonical_height(self):
    r"""
    Compute the canonical height of this element.
    
    Used in arithmetic geometry.
    """
```

## Root System Applications

```python
def weight_space_decomposition(self):
    r"""
    Decompose this element in terms of weights.
    
    When the lattice comes from a representation.
    """

def character_value(self):
    r"""
    Compute the character value at this element.
    
    For applications to representation theory.
    """
```