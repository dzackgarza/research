<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/nondegenerate_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Base Interface: All Lattices(R)

All lattices (nondegenerate R-modules with bilinear forms) share this base interface.
Our primary focus is **integer lattices** (R = ℤ), with generalizations to other Dedekind domains R.

**IMPORTANT**: Lattices inherit ALL methods from:
- FreeModules(R): rank(), basis(), generators(), dual(), tensor(), direct_sum()
- FreeBilinearModules(R): bilinear_form(), gram_matrix(), discriminant(), dual(), left_dual(), right_dual(), orthogonal_group(), left_radical(), right_radical(), radical(), nondegenerate_quotient()
- SymmetricBilinearModules(R): signature(), is_definite(), is_positive_definite(), optimized right_radical(), etc.

The methods below are ADDITIONAL to those inherited methods.

## Convenience Methods

```python
def gram(self):
    r"""
    Return the Gram matrix of the lattice.
    
    This is a convenience method equivalent to gram_matrix() with
    the standard R-module basis. Inherited from FreeBilinearModules(R).
    """
```

## Lattice-Specific Classification

```python
def is_hyperbolic(self):  
    r"""
    Test if the lattice is hyperbolic (Lorentzian signature).
    
    This is a convenience method equivalent to:
    signature() == (1, n-1, 0) where n = rank_R(L).
    
    NOTE: Only meaningful when R embeds in ℝ.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # Hyperbolic plane H₁,₁
    sage: H11 = IntegralLattice(matrix([[-1, 0], [0, 1]]))
    sage: H11.is_hyperbolic()  # Should be True
    True
    sage: H11.signature()  # Should be (1, 1, 0)
    (1, 1, 0)
    
    sage: # A₂ root lattice (elliptic)
    sage: A2 = IntegralLattice(matrix([[-2, 1], [1, -2]]))
    sage: A2.is_hyperbolic()  # Should be False
    False
    sage: A2.signature()  # Should be (0, 2, 0)
    (0, 2, 0)
    
    sage: # Extended A₂ affine diagram (parabolic)
    sage: A2_tilde = IntegralLattice(matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]]))
    sage: A2_tilde.is_hyperbolic()  # Should be False  
    False
    sage: A2_tilde.signature()  # Should be (0, 2, 1) - parabolic
    (0, 2, 1)
    
    sage: # Hyperbolic 3-space H₁,₂
    sage: H12 = IntegralLattice(matrix([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    sage: H12.is_hyperbolic()  # Should be True
    True
    sage: H12.signature()  # Should be (1, 2, 0)
    (1, 2, 0)
    """

def is_parabolic(self):
    r"""
    Test if would be parabolic (if it were degenerate).
    
    Always False for nondegenerate lattices. Provided for interface consistency.
    """  
    return False
```

## Isometry and Automorphisms

```python  
def is_isometric(self, other):
    r"""
    Test if this lattice is isometric to another lattice.
    
    Two lattices L₁ and L₂ are isometric if there exists a
    bijective linear map φ: L₁ → L₂ preserving the bilinear form.
    
    INPUT:
    - other: Another lattice
    
    OUTPUT:
    Boolean indicating if an isometry exists.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # All A₂ root lattices are isometric
    sage: A2_standard = IntegralLattice(matrix([[-2, 1], [1, -2]]))
    sage: A2_scaled = IntegralLattice(matrix([[-6, 3], [3, -6]]))  # Scale by 3
    sage: A2_standard.is_isometric(A2_scaled)  # Should be False (different scale)
    False
    
    sage: # A₂ and hexagonal lattice are isometric  
    sage: A2 = IntegralLattice(matrix([[-2, 1], [1, -2]]))
    sage: hex_lattice = IntegralLattice(matrix([[-2, -1], [-1, -2]]))
    sage: A2.is_isometric(hex_lattice)  # Should be True
    True
    
    sage: # D₄ and F₄ root lattices have same signature but not isometric
    sage: D4_gram = RootSystem(['D', 4]).root_lattice().gram_matrix()
    sage: D4 = IntegralLattice(D4_gram)
    sage: F4_gram = RootSystem(['F', 4]).root_lattice().gram_matrix()  
    sage: F4 = IntegralLattice(F4_gram)
    sage: D4.signature() == F4.signature()  # Same signature
    True
    sage: D4.is_isometric(F4)  # Should be False (different discriminants)
    False
    
    sage: # Hyperbolic planes with same signature
    sage: H1 = IntegralLattice(matrix([[-1, 0], [0, 1]]))
    sage: H2 = IntegralLattice(matrix([[-2, 3], [3, -2]]))
    sage: H1.signature() == H2.signature()  # Both (1,1,0)
    True  
    sage: H1.is_isometric(H2)  # Should be False (different discriminants)
    False
    """

def automorphism_group(self):
    r"""
    Return the automorphism group of the lattice.
    
    This is the group of isometries from the lattice to itself.
    """
```

**NOTE**: By definition, objects in Lattices(R) category have radical = {0},
so is_degenerate() always returns False and radical() always returns {0}.
These are inherited from SymmetricBilinearModules(R).

## Structure Tests

```python
def admits_coxeter_system(self):
    r"""
    Test if this lattice admits a Coxeter system embedding.
    
    Returns True if there exists a primitive embedding ι: ⟨Φ⟩_R ↪ L 
    for some simple root system Φ.
    """

def is_p_elementary(self):
    r"""Test if the lattice is p-elementary for some prime p."""

def is_2_elementary(self):
    r"""Test if the lattice is 2-elementary."""
```

## Sublattice Operations

```python
def sublattice(self, generators):
    r"""
    Return the sublattice spanned by given generators.
    
    The returned sublattice will include SublatticeMixin for embedding functionality.
    """

def sublattice_poset(self):
    r"""Return the poset of all sublattices ordered by inclusion."""
    
def root_system_poset(self):
    r"""Return the sub-poset of subsets which form root systems."""

def span(self, sublattices):
    r"""
    Return the span of a collection of sublattices and/or elements.
    
    Every element v ∈ L is treated as the rank-1 sublattice Rv with its natural
    embedding. For sublattices L₁, ..., Lₙ with embeddings jᵢ: Lᵢ → L, the span 
    is the smallest sublattice containing all jᵢ(Lᵢ).
    
    INPUT:
    - sublattices: A list of sublattices and/or elements of this lattice
    
    OUTPUT:
    The sublattice spanned by the images of all inputs.
    
    EXAMPLES:
    - span([v, w]) for elements v, w ∈ L
    - span([L1, L2]) for sublattices L1, L2
    - span([v, L1, w]) mixing elements and sublattices
    """
```

## Lattice-Specific Operations

```python
def base_change(self, target_ring):
    r"""
    Return the base change L ⊗_R S to any R-algebra S.
    
    INPUT:
    - target_ring: A ring S that is an R-algebra 
    
    OUTPUT:
    The lattice with coefficients extended to S.
    """

def twist(self, scalar):
    r"""
    Return the twisted lattice with quadratic form multiplied by scalar ∈ R.
    
    INPUT:
    - scalar: An element of the base ring R
    """
```

## Lattice-Specific Duality

```python
def stable_orthogonal_group(self):
    r"""
    Return the stable orthogonal group O*(L).
    
    This is the group of isometries of L ⊗_R F that preserve L up to scaling,
    where F is the field of fractions of R.
    
    OUTPUT:
    The stable orthogonal group O*(L).
    """
    
def dual_embedding(self):
    r"""
    Return the canonical embedding ι: L → L*.
    
    For v ∈ L, ι(v) is the R-linear functional w ↦ b(v, w).
    
    OUTPUT:
    The embedding morphism L → L* = Hom_R(L, R).
    """

def metric_dual(self):
    r"""
    Return the metric dual L# = {v ∈ L ⊗ ℚ : b(v, L) ⊆ ℤ} (for integer lattices).
    
    For lattices over general Dedekind domains R, returns {v ∈ L ⊗_R F : b(v, L) ⊆ R}
    where F is the field of fractions of R.
    
    OUTPUT:
    The metric dual lattice L# as an R-module.
    """

def discriminant_group(self):
    r"""
    Return the discriminant group L#/L (finite abelian group for integer lattices).
    
    For general Dedekind domains R, this is a finite torsion R-module.
    
    OUTPUT:
    The discriminant group L#/L.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₂ root lattice discriminant group
    sage: A2 = IntegralLattice(matrix([[-2, 1], [1, -2]]))
    sage: A_L = A2.discriminant_group()
    sage: A_L.order()  # Should be 3
    3
    sage: A_L.structure()  # Should be (ℤ/3ℤ)
    [3]
    
    sage: # E₈ root lattice discriminant group  
    sage: E8_gram = RootSystem(['E', 8]).root_lattice().gram_matrix()
    sage: E8 = IntegralLattice(E8_gram)
    sage: A_E8 = E8.discriminant_group()
    sage: A_E8.order()  # Should be 1 (unimodular)
    1
    
    sage: # Hyperbolic plane H₁,₁ discriminant
    sage: H = IntegralLattice(matrix([[-2, 3], [3, -2]]))
    sage: A_H = H.discriminant_group() 
    sage: A_H.order()  # Should be |det| = |4-9| = 5
    5
    
    sage: # D₄ root lattice discriminant group
    sage: D4_gram = RootSystem(['D', 4]).root_lattice().gram_matrix() 
    sage: D4 = IntegralLattice(D4_gram)
    sage: A_D4 = D4.discriminant_group()
    sage: A_D4.order()  # Should be 4
    4
    sage: A_D4.structure()  # Should be (ℤ/2ℤ)²
    [2, 2]
    """

def discriminant_form(self):
    r"""
    Return the discriminant quadratic form (A_L, q_L) where q_L: A_L → ℚ/ℤ (for integer lattices).
    
    For general rings R, q_L: A_L → F/R where F is the field of fractions.
    
    OUTPUT:
    The discriminant quadratic form (A_L, q_L) where A_L = L#/L is the 
    discriminant group and q_L is the canonical quadratic form.
    """
```

## Miscellaneous

```python
def projectivization(self):
    r"""Return the projectivization P(L) of the lattice."""
```