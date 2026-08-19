<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/two_elementary_lattices/two_elementary_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: TwoElementaryLattices

Elements of 2-elementary lattices. Inherits from Lattices elements via Category.join().

## 2-Elementary Properties

```python
def discriminant_group_order(self):
    r"""
    Return the order of this element's image in the discriminant group.
    
    For 2-elementary lattices, all elements have order 1 or 2 in A_L = L*/L.
    """

def is_even(self):
    r"""
    Test if this element has even norm.
    
    In 2-elementary lattices, this determines discriminant group behavior.
    """

def mod_2_class(self):
    r"""
    Return the class of this element modulo 2L.
    
    OUTPUT:
    Element of L/2L ≅ (Z/2Z)^rank.
    """
```

## 2-Elementary Structure

```python
def companion_vector(self):
    r"""
    Return a vector v' such that ⟨v, v'⟩ ≡ 1 (mod 2).
    
    Such vectors exist due to the 2-elementary property.
    """

def orthogonal_mod_2(self):
    r"""
    Return vectors orthogonal to this one modulo 2.
    
    The set {w ∈ L : ⟨v, w⟩ ≡ 0 (mod 2)}.
    """
```