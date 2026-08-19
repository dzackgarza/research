<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/CoxeterLattice/coxeter_systems.md
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

## Mathematical Test Assertions

The following SageMath assertions establish the mathematical ground truth for Coxeter systems implementation:

```python
# Mathematical assertion: Classification by signature
# Finite Coxeter groups have negative definite Gram matrices (our convention)
# sage: A3 = RootSystem(['A', 3])
# sage: RL = A3.root_lattice()
# sage: simple_roots = RL.simple_roots()
# sage: gram_A3 = matrix([[r1.scalar(r2) for r2 in simple_roots] for r1 in simple_roots])
# sage: eigenvals = gram_A3.eigenvalues()
# sage: all(ev < 0 for ev in eigenvals)  # Negative definite for finite type
# True

# Mathematical assertion: Cartan matrix vs Gram matrix relationship
# For simply-laced types (ADE), Cartan matrix equals -Gram matrix
# sage: A3 = RootSystem(['A', 3])
# sage: cartan_A3 = A3.cartan_matrix()
# sage: RL = A3.root_lattice()
# sage: simple_roots = RL.simple_roots()
# sage: gram_A3 = matrix([[r1.scalar(r2) for r2 in simple_roots] for r1 in simple_roots])
# sage: cartan_A3 == -gram_A3  # True for simply-laced types
# True

# Mathematical assertion: Coxeter matrix computation
# Coxeter matrix entries determine orders of products of simple reflections
# sage: A3 = RootSystem(['A', 3])
# sage: RL = A3.root_lattice()
# sage: simple_roots = RL.simple_roots()
# sage: r1, r2, r3 = list(simple_roots)
# sage: # Adjacent roots have angle 2π/3, giving order 3
# sage: r1.scalar(r2) / (r1.norm() * r2.norm()) == QQ(-1)/2  # cos(2π/3)
# True
# sage: r1.scalar(r3) / (r1.norm() * r3.norm()) == 0  # orthogonal = order 2
# True

# Mathematical assertion: Root system completeness
# Weyl group orbit of simple roots generates all roots
# sage: E8 = RootSystem(['E', 8])
# sage: E8.root_lattice().roots().cardinality()  # E8 has exactly 240 roots
# 240
# sage: len(E8.root_lattice().simple_roots())  # Generated by 8 simple roots
# 8

# Mathematical assertion: Affine type signature properties
# Affine Coxeter groups have exactly one zero eigenvalue (parabolic)
# sage: A2_aff = RootSystem(['A', 2, 1])
# sage: RL_aff = A2_aff.root_lattice()
# sage: simple_roots_aff = RL_aff.simple_roots()
# sage: gram_aff = matrix([[r1.scalar(r2) for r2 in simple_roots_aff] for r1 in simple_roots_aff])
# sage: eigenvals_aff = gram_aff.eigenvalues()
# sage: sum(1 for ev in eigenvals_aff if ev == 0) == 1  # Exactly one zero eigenvalue
# True
# sage: all(ev <= 0 for ev in eigenvals_aff)  # Non-positive (parabolic)
# True

# Mathematical assertion: Non-crystallographic types require field extensions
# H3 (icosahedral) requires golden ratio field extension
# sage: # H3 would need field extension ℚ(√5) for exact representation
# sage: phi = (1 + sqrt(5))/2  # Golden ratio
# sage: phi^2 - phi - 1 == 0  # Defining equation
# True
# sage: # Dihedral angle in regular icosahedron involves φ
# sage: cos_dihedral_h3 = (3*phi - 1)/(2*sqrt(3))  # Known exact value
# sage: cos_dihedral_h3 in QQ(sqrt(5))  # Requires field extension
# True

# Mathematical assertion: Weyl group generation and length function
# Simple reflections generate Weyl group with reduced expressions
# sage: A3 = RootSystem(['A', 3])
# sage: W = A3.root_system().weyl_group()
# sage: s1, s2, s3 = W.simple_reflections()
# sage: longest_element = W.longest_element()
# sage: longest_element.length()  # For A3, longest element has length 6
# 6
# sage: longest_element == s1*s2*s1*s3*s2*s1  # One reduced expression
# True

# Mathematical assertion: Root system crystallographic condition
# Crystallographic types have integral Cartan matrices
# sage: A3 = RootSystem(['A', 3])
# sage: cartan_A3 = A3.cartan_matrix()
# sage: all(c in ZZ for row in cartan_A3 for c in row)  # Integral entries
# True
# sage: G2 = RootSystem(['G', 2])
# sage: cartan_G2 = G2.cartan_matrix()
# sage: cartan_G2[0,1] * cartan_G2[1,0] == 3  # Product constraint for crystallographic
# True
```