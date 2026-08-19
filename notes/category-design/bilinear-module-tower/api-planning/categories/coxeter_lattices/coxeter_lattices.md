<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/coxeter_lattices/coxeter_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: CoxeterLattices

The category of lattices equipped with Coxeter system structure.

## Category Definition

**Objects**: Pairs (L, C) where:
- **L** is a lattice (nondegenerate integral lattice)
- **C = (Φ, ι)** is a Coxeter system with primitive embedding ι: ⟨Φ⟩_R ↪ L

**Morphisms**: ψ: (L₁, C₁) → (L₂, C₂) consists of:
- **Lattice homomorphism** h: L₁ → L₂ 
- **Coxeter system morphism** φ: C₁ → C₂
- **Compatibility**: The lattice map h extends the lattice component of φ

This combines the rich structure of both categories: signature-based lattice classification with geometric Coxeter embeddings.

## Construction

### Primary Constructors

```python
def CoxeterLattice(lattice, coxeter_system):
    r"""
    Construct a Coxeter lattice from a lattice and compatible Coxeter system.
    
    INPUT:
    - ``lattice`` -- Lattice L
    - ``coxeter_system`` -- CoxeterSystem C = (Φ, ι) with ι: ⟨Φ⟩_R ↪ L
    
    OUTPUT: CoxeterLattice object (L, C)
    
    PRECONDITION: The Coxeter system must embed into the given lattice.
    """

@classmethod
def from_cartan_type(cls, cartan_type, ambient_lattice=None):
    r"""
    Construct canonical Coxeter lattice from Cartan type.
    
    INPUT:
    - ``cartan_type`` -- Cartan type like 'A3', ['B', 4], etc.
    - ``ambient_lattice`` -- Optional choice ('weight', 'root', 'ambient')
    
    Uses standard realizations and automatically detects signature.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₃ in root lattice
    sage: A3 = CoxeterLattice.from_cartan_type(['A', 3], ambient_lattice='root')
    sage: A3.rank()  # Should be 3
    3
    sage: A3.weyl_group().order()  # Should be 24 = 4!
    24
    sage: A3.is_finite_type()  # Should be True
    True
    sage: A3.signature()  # Should be (0, 3, 0) - negative definite
    (0, 3, 0)
    
    sage: # E₈ exceptional type
    sage: E8 = CoxeterLattice.from_cartan_type(['E', 8])
    sage: E8.rank()  # Should be 8
    8
    sage: E8.weyl_group().order()  # Should be 696729600
    696729600
    sage: E8.root_system().cardinality()  # Should be 240 roots
    240
    
    sage: # Affine A₂ (parabolic type)
    sage: A2_aff = CoxeterLattice.from_cartan_type(['A', 2, 1])
    sage: A2_aff.is_affine_type()  # Should be True
    True
    sage: A2_aff.signature()  # Should be (0, 2, 1) - parabolic
    (0, 2, 1)
    sage: A2_aff.finite_part().cartan_type()  # Should be A₂
    ['A', 2]
    
    sage: # B₃ (multiple root lengths)
    sage: B3 = CoxeterLattice.from_cartan_type(['B', 3])
    sage: B3.has_multiple_root_lengths()  # Should be True
    True
    sage: B3.is_simply_laced()  # Should be False
    False
    """

@classmethod
def from_simple_roots(cls, simple_roots, ambient_lattice=None):
    r"""
    Construct from simple roots, auto-detecting ambient lattice.
    
    INPUT:
    - ``simple_roots`` -- List of vectors defining simple root system
    - ``ambient_lattice`` -- Optional ambient lattice (default: span of roots)
    """

@classmethod
def from_gram_matrix(cls, gram_matrix):
    r"""
    Construct from Gram matrix of simple roots.
    
    Creates both the lattice ⟨Φ⟩_R and the Coxeter system from the matrix.
    """
```

### Specialized Constructors

```python
@classmethod
def elliptic_from_cartan_type(cls, cartan_type):
    r"""Construct elliptic Coxeter lattice (finite Weyl group)."""

@classmethod  
def parabolic_from_cartan_type(cls, cartan_type):
    r"""Construct parabolic Coxeter lattice (affine Weyl group)."""

@classmethod
def hyperbolic_from_cartan_type(cls, cartan_type):
    r"""Construct hyperbolic Coxeter lattice (infinite volume)."""
```

## Core Operations

### Lattice Structure Access

```python
def lattice(self):
    r"""Return the underlying lattice L."""

def coxeter_system(self):
    r"""Return the Coxeter system C = (Φ, ι)."""

def simple_roots(self):
    r"""Return simple roots Φ as vectors in L."""

def root_lattice(self):
    r"""Return the root lattice ⟨Φ⟩_R."""

def embedding(self):
    r"""Return the primitive embedding ι: ⟨Φ⟩_R ↪ L."""

def embedding_index(self):
    r"""
    Return [L : ⟨Φ⟩_R], the embedding index.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₂ root lattice vs weight lattice embedding
    sage: A2_root = CoxeterLattice.from_cartan_type(['A', 2], ambient_lattice='root')
    sage: A2_root.embedding_index()  # Should be 1 (root lattice = root lattice)
    1
    
    sage: A2_weight = CoxeterLattice.from_cartan_type(['A', 2], ambient_lattice='weight')  
    sage: A2_weight.embedding_index()  # Should be 3 = |P/Q| for A₂
    3
    
    sage: # D₄ root vs weight lattice
    sage: D4_root = CoxeterLattice.from_cartan_type(['D', 4], ambient_lattice='root')
    sage: D4_root.embedding_index()  # Should be 1
    1
    
    sage: D4_weight = CoxeterLattice.from_cartan_type(['D', 4], ambient_lattice='weight')
    sage: D4_weight.embedding_index()  # Should be 4 for D₄
    4
    
    sage: # E₈ is self-dual: root lattice = weight lattice
    sage: E8 = CoxeterLattice.from_cartan_type(['E', 8])
    sage: E8.embedding_index()  # Should be 1 (unimodular)
    1
    """
```

### Inherited Lattice Operations

All standard lattice operations are available via inheritance:

```python
def gram_matrix(self):
    r"""Return Gram matrix of the ambient lattice L."""

def signature(self):
    r"""Return signature (p,q,r) of L."""

def is_elliptic(self):
    r"""Test if L has elliptic signature (inherited from Lattices)."""

def dual_lattice(self):
    r"""Return dual lattice L^*."""

def is_elliptic(self):
    r"""Test if L has elliptic signature."""

def is_parabolic(self):
    r"""Test if L has parabolic signature."""

def is_hyperbolic(self):
    r"""Test if L has hyperbolic signature."""
```

### Coxeter-Specific Operations

```python
def weyl_group(self):
    r"""
    Return Weyl group W ⊆ O(L) generated by simple reflections.
    
    This is the subgroup of O(L) preserving the lattice L.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # Classical series orders
    sage: A4 = CoxeterLattice.from_cartan_type(['A', 4])
    sage: A4.weyl_group().order()  # Should be 5! = 120
    120
    
    sage: B3 = CoxeterLattice.from_cartan_type(['B', 3])
    sage: B3.weyl_group().order()  # Should be 2³ · 3! = 48
    48
    
    sage: # Exceptional groups
    sage: G2 = CoxeterLattice.from_cartan_type(['G', 2])
    sage: G2.weyl_group().order()  # Should be 12
    12
    
    sage: F4 = CoxeterLattice.from_cartan_type(['F', 4])
    sage: F4.weyl_group().order()  # Should be 1152
    1152
    
    sage: E6 = CoxeterLattice.from_cartan_type(['E', 6])
    sage: E6.weyl_group().order()  # Should be 51840
    51840
    
    sage: E7 = CoxeterLattice.from_cartan_type(['E', 7])
    sage: E7.weyl_group().order()  # Should be 2903040
    2903040
    
    sage: # Weyl group structure for D₄ (has triality)
    sage: D4 = CoxeterLattice.from_cartan_type(['D', 4])
    sage: W = D4.weyl_group()
    sage: W.order()  # Should be 192 = 2³ · 4!
    192
    sage: W.simple_reflections()  # Should have 4 generators
    [s₁, s₂, s₃, s₄]
    """

def root_system(self):
    r"""
    Return full root system R ⊆ L as W-orbit of simple roots.
    """

def positive_roots(self):
    r"""Return positive roots with respect to simple system Φ."""

def fundamental_weights(self):
    r"""Return fundamental weights (for crystallographic types)."""

def weight_lattice(self):
    r"""Return weight lattice (dual to coroot lattice)."""

def coroot_lattice(self):
    r"""Return coroot lattice spanned by coroots."""
```

## Geometric Structure

### Reflection Operations

```python
def simple_reflections(self):
    r"""
    Return simple reflections as elements of O(L).
    
    OUTPUT: List of reflections [s₁, s₂, ..., sₙ] where sᵢ ∈ O(L)
    """

def reflection(self, root):
    r"""
    Return reflection in a given root.
    
    INPUT:
    - ``root`` -- Vector in L (typically in the root system R)
    
    OUTPUT: Reflection s_root ∈ O(L)
    
    For roots in R, this preserves the lattice L.
    For general vectors, this may only preserve L ⊗ ℚ.
    """

def act_by_weyl_element(self, vector, weyl_element):
    r"""Apply Weyl group element to vector in L."""
```

### Fundamental Domains

```python
def fundamental_polytope(self):
    r"""
    Return fundamental domain of W acting on L ⊗ ℝ.
    
    This is the convex hull of the fundamental alcove.
    """

def fundamental_alcove(self):
    r"""
    Return fundamental alcove (for affine types).
    
    The fundamental domain for affine Weyl group action.
    """

def chamber_complex(self):
    r"""
    Return chamber complex in L ⊗ ℝ.
    
    Subdivision by hyperplanes of roots.
    """
```

### Hyperplane Arrangements

```python
def hyperplane_arrangement(self):
    r"""
    Return arrangement of root hyperplanes in L ⊗ ℝ.
    
    Collection H = {α^⊥ : α ∈ R} where α^⊥ = {x ∈ L⊗ℝ : ⟨x,α⟩ = 0}
    """

def reflecting_hyperplanes(self):
    r"""Return hyperplanes of simple roots."""

def dominant_cone(self):
    r"""
    Return dominant Weyl chamber.
    
    {x ∈ L⊗ℝ : ⟨x,αᵢ⟩ ≥ 0 for all simple roots αᵢ}
    """
```

## Classification and Properties

### Type Detection

```python
def cartan_type(self):
    r"""
    Return Cartan type if crystallographic.
    
    OUTPUT: Cartan type or None for non-crystallographic systems
    """

def is_crystallographic(self):
    r"""Test if corresponds to semisimple Lie algebra."""

def is_simply_laced(self):
    r"""Test if all roots have same length (A,D,E types)."""

def has_multiple_root_lengths(self):
    r"""Test if has multiple root lengths (B,C,F,G types)."""
```

### Finite/Infinite Classification

```python
def is_finite_type(self):
    r"""Test if Weyl group is finite (elliptic lattice)."""

def is_affine_type(self):
    r"""Test if extends finite type (parabolic lattice)."""

def is_hyperbolic_type(self):
    r"""Test if has infinite volume fundamental domain."""

def finite_part(self):
    r"""
    Return finite part (for affine types).
    
    The finite Coxeter lattice obtained by removing affine node.
    """
```

## Parabolic Subgroups and Sublattices

### Standard Parabolics

```python
def parabolic_subgroup(self, subset):
    r"""
    Return parabolic subgroup generated by subset of simple reflections.
    
    INPUT:
    - ``subset`` -- Subset I ⊆ {1,2,...,n} of simple root indices
    
    OUTPUT: Subgroup W_I = ⟨sᵢ : i ∈ I⟩
    """

def parabolic_sublattice(self, subset):
    r"""
    Return sublattice corresponding to parabolic subgroup.
    
    The sublattice spanned by simple roots in the subset.
    """

def maximal_parabolics(self):
    r"""
    Return all maximal parabolic subgroups.
    
    These correspond to removing one simple root.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₃ has 3 maximal parabolics
    sage: A3 = CoxeterLattice.from_cartan_type(['A', 3])
    sage: parabolics = A3.maximal_parabolics()
    sage: len(parabolics)  # Should be 3
    3
    sage: [P.cartan_type() for P in parabolics]  # Should be [A₂, A₁⊕A₁, A₂]
    [['A', 2], ['A', 1, 'A', 1], ['A', 2]]
    
    sage: # D₄ has 4 maximal parabolics
    sage: D4 = CoxeterLattice.from_cartan_type(['D', 4])
    sage: parabolics = D4.maximal_parabolics()
    sage: len(parabolics)  # Should be 4
    4
    sage: types = [P.cartan_type() for P in parabolics]
    sage: types  # Should include A₃ and three A₁⊕A₁⊕A₁
    [['A', 3], ['A', 1, 'A', 1, 'A', 1], ['A', 1, 'A', 1, 'A', 1], ['A', 1, 'A', 1, 'A', 1]]
    
    sage: # E₈ has 8 maximal parabolics 
    sage: E8 = CoxeterLattice.from_cartan_type(['E', 8])
    sage: parabolics = E8.maximal_parabolics()
    sage: len(parabolics)  # Should be 8
    8
    sage: # One should be E₇, others involve A and D factors
    sage: E7_parabolic = [P for P in parabolics if P.cartan_type() == ['E', 7]]
    sage: len(E7_parabolic)  # Should be 1
    1
    
    sage: # Affine types have no proper maximal parabolics
    sage: A2_aff = CoxeterLattice.from_cartan_type(['A', 2, 1])
    sage: parabolics = A2_aff.maximal_parabolics()
    sage: len(parabolics)  # Should be 0 (all are finite type)
    0
    """
```

### Levi Decomposition

```python
def levi_factor(self, subset):
    r"""Return Levi factor of parabolic subgroup."""

def unipotent_radical(self, subset):
    r"""Return unipotent radical of parabolic subgroup."""
```

## Representation Theory

### Weight Spaces

```python
def weight_space_decomposition(self):
    r"""
    Decompose ambient lattice into weight spaces.
    
    For representations of the corresponding Lie algebra.
    """

def highest_weight_vectors(self):
    r"""Return highest weight vectors in various representations."""

def fundamental_representations(self):
    r"""Return fundamental representations (for crystallographic types)."""
```

### Characters

```python
def weyl_character_formula(self, highest_weight):
    r"""
    Compute character via Weyl character formula.
    
    INPUT:
    - ``highest_weight`` -- Dominant weight
    
    OUTPUT: Character of irreducible representation
    """

def multiplicity(self, weight, highest_weight):
    r"""Compute weight multiplicity in irreducible representation."""
```

## Examples

### Standard Types

```python
# Elliptic types (finite Weyl groups)
A3 = CoxeterLattice.from_cartan_type('A3')
A3.is_finite_type()        # True
A3.weyl_group().order()    # 24

# Parabolic types (affine Weyl groups)  
A3_tilde = CoxeterLattice.from_cartan_type(['A', 3, 1])
A3_tilde.is_affine_type()  # True
A3_tilde.finite_part()     # Returns A3

# Hyperbolic types
H3 = CoxeterLattice.from_coxeter_matrix([[1,3,2],[3,1,5],[2,5,1]])
H3.is_hyperbolic_type()    # True
```

### Custom Constructions

```python
# A₂ embedded in larger lattice
gram = matrix([[-2,1,0],[1,-2,1],[0,1,-2]])  # A₃ Gram matrix
L = IntegralLattice(gram)
simple_roots = [L.basis()[0], L.basis()[1]]  # First two roots
A2_in_A3 = CoxeterLattice.from_simple_roots(simple_roots, L)
A2_in_A3.embedding_index()  # > 1
```

### Morphisms and Relationships

```python
# Inclusion morphisms
A2 = CoxeterLattice.from_cartan_type('A2')
A3 = CoxeterLattice.from_cartan_type('A3')
inclusions = Hom(A2, A3)

# Base change
A2_weight = CoxeterLattice.from_cartan_type('A2', ambient_lattice='weight')
A2_root = CoxeterLattice.from_cartan_type('A2', ambient_lattice='root')
base_change = Hom(A2_root, A2_weight)
```

## Integration with SageMath Categories

This category integrates seamlessly with SageMath's automatic joining:

```python
# Automatic signature detection and joining
CoxeterLattices() & Lattices().Elliptic()     # Elliptic Coxeter lattices
CoxeterLattices() & Lattices().Hyperbolic()   # Hyperbolic Coxeter lattices
CoxeterLattices() & DegenerateLattices().Parabolic()  # Parabolic Coxeter lattices
```

Operations are inherited from both parent categories and composed automatically via SageMath's ParentMethods and ElementMethods framework.