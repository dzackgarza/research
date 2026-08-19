<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/symmetric_Rmod.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: SymmetricBilinearModules(R)

Free R-modules with symmetric bilinear forms b: L ⊗_R L → R. Inherits from FreeBilinearModules(R).

## Symmetric Properties

```python
def is_symmetric(self):
    r"""Always returns True for modules in this category."""
    return True

def quadratic_form(self):
    r"""
    Return the associated quadratic form Q(v) = ⟨v,v⟩.
    """

## NOTE: radical() is inherited from FreeBilinearModules
# For symmetric forms, left_radical() = right_radical() = radical()

def is_nondegenerate(self):
    r"""Test if the form is nondegenerate (radical = {0})."""
    
def is_degenerate(self):
    r"""Test if the form is degenerate (radical ≠ {0})."""
```

## Signature and Classification

```python
def signature(self):
    r"""
    Return the signature (p, q, r) of the bilinear form.
    
    NOTE: This only makes sense when R embeds in ℝ (e.g., R = ℤ, or R = ring of integers 
    in a totally real number field).
    
    - p = max{dim_F(V) : V ⊆ M ⊗_R F subspace with b|_V positive definite}
    - q = max{dim_F(V) : V ⊆ M ⊗_R F subspace with b|_V negative definite}
    - r = dim_F(radical(M ⊗_R F))
    
    where F is the field of fractions of R.
    This is a basis-invariant property of the bilinear form.
    Note: p + q + r = rank_R(M).
    """

def is_positive_definite(self):
    r"""
    Test if b(v,v) > 0 for all non-zero v ∈ M ⊗_R F.
    
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_negative_definite(self):
    r"""
    Test if b(v,v) < 0 for all non-zero v ∈ M ⊗_R F.
    
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_definite(self):
    r"""
    Test if the form is definite (positive or negative).
    
    Equivalent to: signature has form (n,0,0) or (0,n,0).
    NOTE: Only meaningful when R embeds in ℝ.
    """

def is_indefinite(self):
    r"""
    Test if the form is indefinite.
    
    Equivalent to: ∃ v,w ∈ M ⊗_R F with b(v,v) > 0 and b(w,w) < 0.
    Also equivalent to: p ≥ 1 and q ≥ 1 in signature (p,q,r).
    NOTE: Only meaningful when R embeds in ℝ.
    """

def witt_index(self):
    r"""
    Return the Witt index of the form.
    
    This is max{dim(V) : V ⊆ M totally isotropic submodule}.
    A submodule V is totally isotropic if b(v,w) = 0 for all v,w ∈ V.
    """
```

## Computational Invariants

```python
def rank(self):
    r"""
    Return the rank of the R-module.
    
    Note: If (p,q,r) is the signature, then rank_R(M) = p + q + r.
    For nondegenerate forms, rank_R(M) = p + q.
    """
```

## Symmetric-Specific Optimizations

```python
def right_radical(self):
    r"""
    Return the right radical. For symmetric forms, this equals the left radical.
    
    This override makes the mathematical identity explicit and avoids
    redundant computation since left_radical() = right_radical() for symmetric forms.
    """
    return self.left_radical()
```

## NOTE: The following methods are inherited from FreeBilinearModules(R):
# - dual() - enhanced with canonical map using bilinear form
# - orthogonal_group() - form-preserving R-automorphisms  
# - tensor(), direct_sum() - with bilinear form extension over R
# - quotient_by_radical() - standard degeneracy elimination