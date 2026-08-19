<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/definite_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: DefiniteLattices  

Elements of definite lattices. Inherits from Lattices elements.

## Definite Properties

```python
def norm(self):
    r"""
    Return the norm of this element.
    
    For definite lattices, sqrt(|⟨v,v⟩|) is always real and well-defined.
    """

def distance_to(self, other):
    r"""
    Return the distance between this element and another.
    
    Uses the lattice's inner product to define distance.
    """
```

## Minimal Vectors

```python
def is_minimal_vector(self):
    r"""
    Test if this is a shortest nonzero vector in the lattice.
    
    For definite lattices, there are finitely many minimal vectors.
    """

def minimal_norm(self):
    r"""
    Return the minimal nonzero norm in the lattice.
    
    This is min{|⟨v,v⟩| : v ∈ L, v ≠ 0}.
    """
```

## Reduction Theory

```python
def reduced_representative(self):
    r"""
    Return a reduced representative in the same coset.
    
    Uses lattice reduction algorithms appropriate for the signature.
    """

def is_reduced(self):
    r"""Test if this element is in reduced form."""
```