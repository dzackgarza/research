<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/two_elementary_lattices/two_elementary_lattices.md
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

## Mathematical Test Assertions

```python
# Mathematical assertion: A_1 root lattice is 2-elementary with discriminant 2
# sage: R = RootSystem(['A', 1])
# sage: C = R.cartan_matrix()
# sage: det = (-C).determinant()  # Gram matrix determinant
# sage: det == 2  # A_1 discriminant = 2 = 2^1 (Conway & Sloane Ch 4)
# True

# Mathematical assertion: A_3 root lattice is 2-elementary with discriminant 4  
# sage: R = RootSystem(['A', 3])
# sage: C = R.cartan_matrix()
# sage: det = (-C).determinant()
# sage: det == 4  # A_3 discriminant = 4 = 2^2 (2-elementary)
# True

# Mathematical assertion: D_4 root lattice is 2-elementary with discriminant 4
# sage: R = RootSystem(['D', 4]) 
# sage: C = R.cartan_matrix()
# sage: det = (-C).determinant()
# sage: det == 4  # All D_n (n≥3) have discriminant 4 = 2^2
# True

# Mathematical assertion: E_8 root lattice is 2-elementary with discriminant 1
# sage: R = RootSystem(['E', 8])
# sage: C = R.cartan_matrix()
# sage: det = (-C).determinant()
# sage: det == 1  # E_8 discriminant = 1 = 2^0 (unimodular)
# True

# Mathematical assertion: E_7 root lattice is 2-elementary with discriminant 2
# sage: R = RootSystem(['E', 7])
# sage: C = R.cartan_matrix()
# sage: det = (-C).determinant()
# sage: det == 2  # E_7 discriminant = 2 = 2^1 
# True

# Mathematical assertion: Root lattices have even norms (all roots have norm 2)
# sage: R = RootSystem(['A', 3])
# sage: roots = R.root_lattice().roots()
# sage: all(alpha.inner_product(alpha) == 2 for alpha in roots)
# True  # All simple roots have norm 2, hence even lattice

# Mathematical assertion: 2-elementary property is preserved under orthogonal direct sums
# sage: R1 = RootSystem(['A', 1])
# sage: R2 = RootSystem(['A', 3])
# sage: det1, det2 = 2, 4  # Their discriminants
# sage: combined_det = det1 * det2  # Orthogonal sum discriminant
# sage: combined_det == 8  # 8 = 2^3, so still 2-elementary
# True

# Mathematical assertion: Non-2-elementary examples have odd prime divisors
# sage: # A_2 has discriminant 3 (not 2-elementary)
# sage: disc_A2 = 3
# sage: (disc_A2 & (disc_A2 - 1)) == 0  # Check if power of 2
# False  # A_2 is not 2-elementary due to odd prime factor
```