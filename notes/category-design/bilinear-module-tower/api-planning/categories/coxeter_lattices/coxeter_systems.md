<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/coxeter_lattices/coxeter_systems.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: CoxeterSystems

The category of Coxeter systems with proper geometric morphisms.

## Category Definition

**Objects**: Pairs (Φ, ι) where:
- **Φ = {α₁, α₂, ..., αₙ}** is a simple root system satisfying root system axioms
- **ι: ⟨Φ⟩_R ↪ L** is a primitive embedding into some ambient lattice L

**Morphisms**: φ: (Φ₁, ι₁) → (Φ₂, ι₂) consists of:
- **Root system map** f: Φ₁ → Φ₂ (preserving simple root structure)
- **Lattice homomorphism** g: L₁ → L₂
- **Commutative diagram**: g ∘ ι₁ = ι₂ ∘ ⟨f⟩

```
⟨Φ₁⟩_R --⟨f⟩--> ⟨Φ₂⟩_R
    |                |
    ι₁               ι₂
    |                |
    v                v
    L₁ ------g-----> L₂
```

## Core Operations

### Construction

```python
def CoxeterSystem(simple_roots, ambient_lattice):
    r"""
    Construct a Coxeter system from simple roots in an ambient lattice.
    
    INPUT:
    - ``simple_roots`` -- List of vectors [α₁, α₂, ..., αₙ] in ambient_lattice
    - ``ambient_lattice`` -- Lattice L containing the simple roots
    
    OUTPUT: CoxeterSystem object (Φ, ι) where ι: ⟨Φ⟩_R ↪ L
    
    The simple roots must satisfy root system axioms:
    - Each αᵢ spans a 1-dimensional radical of its reflection hyperplane
    - Reflections sᵢ(αⱼ) - αⱼ ∈ R₊·αᵢ for i ≠ j
    - No proper subset generates the same root system
    """

@classmethod
def from_cartan_type(cls, cartan_type, ambient_lattice=None):
    r"""
    Construct canonical Coxeter system from Cartan type.
    
    INPUT:
    - ``cartan_type`` -- Cartan type like 'A3', ['B', 4], etc.
    - ``ambient_lattice`` -- Optional ambient lattice (default: canonical)
    
    Uses standard realizations (weight lattice, root lattice, etc.)
    """

@classmethod  
def from_coxeter_matrix(cls, coxeter_matrix, ambient_lattice=None):
    r"""
    Construct Coxeter system from Coxeter matrix.
    
    INPUT:
    - ``coxeter_matrix`` -- Matrix M where M[i,j] = order(sᵢsⱼ)
    - ``ambient_lattice`` -- Optional ambient lattice
    
    Constructs simple roots with prescribed reflection orders.
    """
```

### Morphism Operations

```python
def Hom(self, other):
    r"""
    Return the set of morphisms from this Coxeter system to another.
    
    OUTPUT: Set of morphisms (f, g) where f: Φ₁ → Φ₂ and g: L₁ → L₂
    """

def is_isomorphic_to(self, other):
    r"""
    Test if two Coxeter systems are isomorphic.
    
    Two systems (Φ₁, ι₁) and (Φ₂, ι₂) are isomorphic if there exists
    a bijective morphism between them.
    """

def automorphism_group(self):
    r"""
    Return the automorphism group of this Coxeter system.
    
    OUTPUT: Group of automorphisms preserving both root structure
    and lattice embedding.
    """

def canonical_form(self):
    r"""
    Return canonical representative for the isomorphism class.
    
    Used for efficient isomorphism testing and classification.
    """
```

## Properties and Queries

### Basic Properties

```python
def rank(self):
    r"""Return the rank (number of simple roots)."""

def simple_roots(self):
    r"""Return the simple root system Φ."""

def ambient_lattice(self):
    r"""Return the ambient lattice L."""

def root_lattice(self):
    r"""Return the root lattice ⟨Φ⟩_R."""

def embedding(self):
    r"""Return the primitive embedding ι: ⟨Φ⟩_R ↪ L."""

def embedding_index(self):
    r"""Return [L : ⟨Φ⟩_R], the index of the root lattice in ambient lattice."""
```

### Classification

```python
def cartan_type(self):
    r"""
    Return the Cartan type if crystallographic, None otherwise.
    
    OUTPUT: Cartan type like 'A3', ['B', 4], or None for non-crystallographic
    """

def is_crystallographic(self):
    r"""
    Test if all root lengths are rational multiples of each other.
    
    Crystallographic Coxeter systems correspond to semisimple Lie algebras.
    """

def is_finite(self):
    r"""Test if the Weyl group is finite (elliptic type)."""

def is_affine(self):
    r"""Test if extends finite type by one node (parabolic type)."""

def is_hyperbolic(self):
    r"""Test if has infinite volume fundamental domain."""

def signature(self):
    r"""
    Return signature (p,q,r) of the bilinear form on ⟨Φ⟩_ℝ.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # Finite types have signature (0, n, 0) - negative definite
    sage: A3 = CoxeterSystem.from_cartan_type(['A', 3])
    sage: A3.signature()  # Should be (0, 3, 0)
    (0, 3, 0)
    
    sage: E8 = CoxeterSystem.from_cartan_type(['E', 8])
    sage: E8.signature()  # Should be (0, 8, 0)
    (0, 8, 0)
    
    sage: # Affine types have signature (0, n, 1) - parabolic
    sage: A3_aff = CoxeterSystem.from_cartan_type(['A', 3, 1])
    sage: A3_aff.signature()  # Should be (0, 3, 1)
    (0, 3, 1)
    
    sage: E8_aff = CoxeterSystem.from_cartan_type(['E', 8, 1])
    sage: E8_aff.signature()  # Should be (0, 8, 1)  
    (0, 8, 1)
    
    sage: # Hyperbolic types have signature (1, n-1, 0) - Lorentzian
    sage: # H₃ hyperbolic 3-space (rank 3)
    sage: H3_gram = matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
    sage: H3 = CoxeterSystem.from_gram_matrix(H3_gram)
    sage: H3.signature()  # Should be (1, 2, 0)
    (1, 2, 0)
    
    sage: # Hyperbolic plane H₁,₁ (rank 2)
    sage: H11_gram = matrix([[-1, 0], [0, 1]])
    sage: H11 = CoxeterSystem.from_gram_matrix(H11_gram)
    sage: H11.signature()  # Should be (1, 1, 0)
    (1, 1, 0)
    
    sage: # Classification via signature
    sage: def classify_by_signature(system):
    ...     p, q, r = system.signature()
    ...     if r > 0:
    ...         return "parabolic" if r == 1 else "indefinite"
    ...     elif p == 0:
    ...         return "finite"
    ...     elif p == 1:
    ...         return "hyperbolic"
    ...     else:
    ...         return "general_indefinite"
    sage: classify_by_signature(A3)  # Should be "finite"
    "finite"
    sage: classify_by_signature(A3_aff)  # Should be "parabolic"
    "parabolic"  
    sage: classify_by_signature(H3)  # Should be "hyperbolic"
    "hyperbolic"
    """
```

## Derived Structure

All structure below is computed and cached from the basic data (Φ, ι):

### Algebraic Structure

```python
def coxeter_matrix(self):
    r"""
    Return Coxeter matrix M where M[i,j] = order(sᵢsⱼ).
    
    Computed from inner products: M[i,j] = 2π/arccos(2⟨αᵢ,αⱼ⟩/(|αᵢ||αⱼ|))
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₃ Coxeter matrix (adjacent reflections have order 3)
    sage: A3 = CoxeterSystem.from_cartan_type(['A', 3])
    sage: M = A3.coxeter_matrix()
    sage: M  # Should be [[1, 3, 2], [3, 1, 3], [2, 3, 1]]
    [[1, 3, 2], [3, 1, 3], [2, 3, 1]]
    sage: M[0,1] == M[1,2] == 3  # Adjacent pairs
    True
    sage: M[0,2] == 2  # Non-adjacent (commute)
    True
    
    sage: # B₃ Coxeter matrix (double bond gives order 4)
    sage: B3 = CoxeterSystem.from_cartan_type(['B', 3])
    sage: M = B3.coxeter_matrix()
    sage: M[1,2]  # Should be 4 (double bond)
    4
    sage: M[0,1]  # Should be 3 (single bond)  
    3
    sage: M[0,2]  # Should be 2 (no bond = commute)
    2
    
    sage: # G₂ Coxeter matrix (triple bond gives order 6)
    sage: G2 = CoxeterSystem.from_cartan_type(['G', 2])
    sage: M = G2.coxeter_matrix()
    sage: M[0,1]  # Should be 6 (triple bond)
    6
    
    sage: # Hyperbolic example with infinite order
    sage: # Custom hyperbolic Coxeter system
    sage: hyp_gram = matrix([[-2, 1, 1], [1, -2, 0], [1, 0, -2]])
    sage: hyp = CoxeterSystem.from_gram_matrix(hyp_gram)  
    sage: M = hyp.coxeter_matrix()
    sage: M[0,2]  # Should be ∞ (hyperbolic reflection pair)
    oo
    
    sage: # I₂(5) dihedral group (pentagonal symmetry)
    sage: I2_5_gram = matrix([[-2, 1], [1, -2]]) * cos(pi/5)  # 72° angle
    sage: I2_5 = CoxeterSystem.from_gram_matrix(I2_5_gram)
    sage: M = I2_5.coxeter_matrix()
    sage: M[0,1]  # Should be 5
    5
    """

def gram_matrix(self):
    r"""
    Return Gram matrix G where G[i,j] = ⟨αᵢ,αⱼ⟩.
    
    This is the fundamental data encoding all geometric information.
    
    MATHEMATICAL EXAMPLES (should be computable):
    
    sage: # A₂ Gram matrix (our negative definite convention)
    sage: A2 = CoxeterSystem.from_cartan_type(['A', 2])
    sage: A2.gram_matrix()  # Should be [[-2, 1], [1, -2]]
    [[-2, 1], [1, -2]]
    
    sage: # G₂ Gram matrix (multiple root lengths)  
    sage: G2 = CoxeterSystem.from_cartan_type(['G', 2])
    sage: G = G2.gram_matrix()
    sage: G[0,0] / G[1,1]  # Ratio should be 3 (long/short = √3)
    3
    
    sage: # B₃ Gram matrix
    sage: B3 = CoxeterSystem.from_cartan_type(['B', 3])
    sage: G = B3.gram_matrix()
    sage: G  # Should have 120° angles except for last root
    [[-2, 1, 0], [1, -2, 1], [0, 1, -1]]
    
    sage: # Hyperbolic example H₃
    sage: H3_matrix = matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
    sage: H3 = CoxeterSystem.from_gram_matrix(H3_matrix)
    sage: H3.signature()  # Should be (1, 2, 0) - hyperbolic
    (1, 2, 0)
    
    sage: # Affine A₂ Gram matrix (parabolic)
    sage: A2_aff = CoxeterSystem.from_cartan_type(['A', 2, 1])
    sage: G = A2_aff.gram_matrix()
    sage: G.determinant()  # Should be 0 (parabolic = one null eigenvalue)
    0
    sage: G.rank()  # Should be 2 (affine = rank n-1 radical)
    2
    """

def schlaefli_matrix(self):
    r"""
    Return Schläfli matrix encoding dihedral angles between hyperplanes.
    """

def weyl_group(self):
    r"""
    Return the Weyl group W ⊆ O(L) generated by simple reflections.
    
    W = ⟨sα : α ∈ Φ⟩ where sα(x) = x - 2⟨x,α⟩/⟨α,α⟩ α
    """

def root_system(self):
    r"""
    Return the full root system R = W·Φ (orbit of Φ under W).
    """
```

### Geometric Structure

```python
def hyperplane_arrangement(self):
    r"""
    Return hyperplane arrangement H = {α^⊥ : α ∈ R}.
    
    Collection of reflection hyperplanes partitioning the ambient space.
    """

def fundamental_polytope(self):
    r"""
    Return fundamental domain P of W acting on ⟨Φ⟩_ℝ.
    
    The fundamental region bounded by simple root hyperplanes.
    """

def chamber_complex(self):
    r"""
    Return the chamber complex - subdivision of space by hyperplanes.
    """

def alcove_complex(self):
    r"""
    Return alcove complex (for affine types).
    
    Fundamental domains for affine Weyl group action.
    """
```

### Combinatorial Structure

```python
def coxeter_diagram(self):
    r"""
    Return Coxeter diagram as a graph.
    
    Vertices are simple roots, edges encode non-trivial orders.
    """

def dynkin_diagram(self):
    r"""
    Return Dynkin diagram (for crystallographic types).
    
    Encodes relative root lengths via edge multiplicities.
    """
```

## Examples

### Standard Constructions

```python
# Type A₃ in standard realization
A3 = CoxeterSystem.from_cartan_type('A3')
A3.ambient_lattice()    # Standard weight lattice
A3.embedding_index()   # [P : Q] where P = weight lattice, Q = root lattice

# Type A₃ in root lattice realization  
A3_root = CoxeterSystem.from_cartan_type('A3', ambient_lattice='root')
A3_root.embedding_index()  # 1 (root lattice embeds in itself)

# Custom embedding
L = IntegralLattice(some_gram_matrix)  
roots = [L([1,-1,0]), L([0,1,-1])]  # Simple roots for A₂ ⊆ A₃
A2_in_L = CoxeterSystem(roots, L)
```

### Morphism Examples

```python
# Inclusion A₂ ↪ A₃
A2 = CoxeterSystem.from_cartan_type('A2')
A3 = CoxeterSystem.from_cartan_type('A3')
inclusions = Hom(A2, A3)  # Multiple ways to embed A₂ in A₃

# Automorphisms of D₄ (exceptional case)
D4 = CoxeterSystem.from_cartan_type('D4')  
D4.automorphism_group()  # S₃ acting on the three equivalent nodes

# Base change morphisms
A2_weight = CoxeterSystem.from_cartan_type('A2', ambient_lattice='weight')
A2_root = CoxeterSystem.from_cartan_type('A2', ambient_lattice='root')
base_change = Hom(A2_root, A2_weight)  # Canonical inclusion
```

## Implementation Notes

### Efficiency Considerations

- **Lazy evaluation**: Derived structure computed only when needed
- **Caching**: Expensive computations cached after first access
- **Canonical forms**: Isomorphism testing via canonical representatives
- **Gram matrix primary**: All computations derive from Gram matrix of simple roots

### Morphism Computation

- **Root system maps**: Determined by simple root images (combinatorial)
- **Lattice maps**: Linear algebra over the ambient lattices  
- **Compatibility**: Verify commutative diagram condition
- **Classification**: Enumerate via root system automorphisms and lattice embeddings

This category provides the geometric foundation for all Coxeter theory in the lattice component.