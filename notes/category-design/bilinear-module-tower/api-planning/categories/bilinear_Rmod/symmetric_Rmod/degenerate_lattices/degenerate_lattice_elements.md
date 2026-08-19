<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/degenerate_lattices/degenerate_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: DegenerateLattices

Elements of degenerate lattices (with nontrivial radical). Inherits from SymmetricBilinearModules elements.

## Radical Structure

```python
def radical_component(self):
    r"""
    Return the component of this element lying in the radical.
    
    Every element v can be written as v = v_rad + v_nonrad where
    v_rad ∈ rad(L) and v_nonrad ⊥ rad(L).
    """

def nonradical_component(self):
    r"""
    Return the component orthogonal to the radical.
    
    This projects to the quotient L/rad(L) which is nondegenerate.
    """

def is_in_radical(self):
    r"""
    Test if this element lies entirely in the radical.
    
    Returns True if ⟨v, w⟩ = 0 for all w ∈ L.
    """
```

## Degenerate Operations

```python
def quotient_projection(self):
    r"""
    Project this element to the nondegenerate quotient L/rad(L).
    
    OUTPUT:
    Element of the quotient lattice (which is nondegenerate).
    """

def radical_orthogonal_complement(self):
    r"""
    Return the orthogonal complement of this element within the radical.
    
    Only meaningful if this element lies in the radical.
    """
```

## Limited Operations

```python
def pseudo_norm_squared(self):
    r"""
    Return ⟨v, v⟩ even though the form may be degenerate.
    
    Note: This may be zero even for nonzero elements.
    """

# Note: reflection() is NOT available for degenerate lattices
# as reflections require nondegenerate forms
```