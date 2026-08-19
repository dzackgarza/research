<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/degenerate_lattices/degenerate_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: DegenerateLattices(R)

Degenerate lattices (with nontrivial radical) have a specialized interface.

**IMPORTANT**: DegenerateLattices inherit ALL methods from:
- FreeModules(R): rank(), basis(), generators(), dual(), tensor(), direct_sum()
- FreeBilinearModules(R): bilinear_form(), gram_matrix(), discriminant(), dual(), left_dual(), right_dual(), orthogonal_group(), left_radical(), right_radical(), radical(), nondegenerate_quotient()
- SymmetricBilinearModules(R): signature(), is_definite(), optimized right_radical(), etc.

The methods below are ADDITIONAL to those inherited methods.

**NOTE**: By definition, objects in DegenerateLattices have rad(L) ≠ {0},
so discriminant() always returns 0, and the signature has r > 0.

## Radical-Specific Methods

```python
def radical_rank(self):
    r"""
    Return the rank of the radical.
    
    This is the r component of signature (p,q,r).
    """

## NOTE: quotient_by_radical() is inherited from SymmetricBilinearModules(R)
# The specific implementation for DegenerateLattices returns (Q, π) tuple
# where Q is nondegenerate and π is the quotient map

def radical_complement(self):
    r"""
    Return a complement to the radical (not unique).
    
    This is a sublattice M such that L = M ⊕ rad(L) as R-modules
    (but not necessarily as an orthogonal direct sum).
    """
```

## Orthogonal Decomposition

```python
def orthogonal_to_radical(self):
    r"""
    Return rad(L)^⊥, the orthogonal complement of the radical.
    
    Note: For degenerate forms, rad(L) ⊆ rad(L)^⊥, so this
    contains the radical as a sublattice.
    """

def is_split_degenerate(self):
    r"""
    Test if L = M ⊕ rad(L) as an orthogonal direct sum.
    
    True if there exists a nondegenerate sublattice M such that
    L = M ⊕ rad(L) and M ⊥ rad(L).
    """
```

## Classification

```python
def is_parabolic(self):
    r"""
    Test if this is a parabolic lattice.
    
    True if radical has rank 1 and the form on rad(L)^⊥/rad(L)
    is negative definite.
    """

def signature_on_quotient(self):
    r"""
    Return the signature of the induced form on L/rad(L).
    
    This determines the type of degeneracy.
    """
```

## Degenerate-Specific Invariants

```python
def discriminant_group(self):
    r"""
    For degenerate lattices, L*/L is not a finite group.
    
    Raises NotImplementedError. Use quotient_by_radical() and
    compute the discriminant group of the nondegenerate quotient.
    """
    raise NotImplementedError("Discriminant group is infinite for degenerate lattices")
```

## NOTE: dual() and orthogonal_group() are inherited from SymmetricBilinearModules(R)
# For degenerate lattices:
# - dual() returns (L*, ι) where ker(ι) = rad(L)
# - orthogonal_group() preserves the radical

## Degenerate-Specific Group Actions

```python
def stabilizer_of_radical(self):
    r"""
    Return the subgroup of O(L) that fixes rad(L) pointwise.
    
    This is often the relevant group for degenerate lattices,
    as it acts faithfully on the nondegenerate quotient L/rad(L).
    """
```