<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/two_elementary_lattices/two_elementary_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: TwoElementaryLattices

2-elementary lattices - lattices whose discriminant group is (Z/2Z)^a. This is an orthogonal category obtained via Category.join([Lattices(), TwoElementaryLattices()]).

These lattices inherit ALL methods from Lattices and add 2-elementary specific functionality.

## 2-Elementary Properties

```python
def is_2_elementary(self):
    r"""Always returns True for this category."""
    return True

def discriminant_group_2_rank(self):
    r"""
    Return the rank of the discriminant group as a (Z/2Z)-vector space.
    
    For 2-elementary lattices: A_L ≅ (Z/2Z)^a for some a.
    """

def is_even(self):
    r"""
    Test if this is an even lattice.
    
    A lattice is even if ⟨v,v⟩ ≡ 0 (mod 2) for all v ∈ L.
    """

def is_odd(self):
    r"""Test if this lattice contains vectors of odd norm."""
```

## Mod 2 Structure

```python
def mod_2_kernel(self):
    r"""
    Return the kernel of the mod 2 reduction map L → L/2L.
    
    This is {v ∈ L : 2v ∈ 2L} = L.
    """

def mod_2_quotient(self):
    r"""
    Return the quotient L/2L as a (Z/2Z)-vector space.
    
    OUTPUT:
    Vector space (Z/2Z)^rank over the field Z/2Z.
    """

def mod_2_inner_product(self):
    r"""
    Return the induced inner product on L/2L.
    
    This is a symmetric bilinear form over Z/2Z.
    """
```

## Spinor Norm

```python
def spinor_norm(self, element):
    r"""
    Compute the spinor norm of an isometry.
    
    For 2-elementary lattices, this takes values in Z/2Z.
    """

def theta_characteristic(self):
    r"""
    Return the theta characteristic of the lattice.
    
    This is a mod 2 invariant of 2-elementary lattices.
    """
```

## Code Theory Connection

```python
def associated_code(self):
    r"""
    Return the binary code associated to this 2-elementary lattice.
    
    There are connections between 2-elementary lattices and binary codes.
    """

def weight_enumerator(self):
    r"""
    Return the weight enumerator polynomial.
    
    Counts vectors by their norm modulo 2.
    """
```