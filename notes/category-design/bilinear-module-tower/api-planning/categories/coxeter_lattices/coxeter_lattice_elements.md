<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/coxeter_lattices/coxeter_lattice_elements.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Element Interface: CoxeterLattices

Elements of Coxeter lattices with both general lattice operations and Coxeter-specific structure.

## Inheritance Hierarchy

CoxeterLattice elements inherit from:
- **LatticeElements**: General lattice vector operations  
- **CoxeterStructure**: Root system and Weyl group operations

## General Lattice Operations

All standard lattice element operations are available:

### Bilinear Forms and Norms

```python
def bilinear_form(self, other):
    r"""
    Bilinear form evaluation using the ambient lattice's form.
    
    This respects the lattice structure and signature.
    
    NOTE: Only called "inner product" for positive definite lattices.
    """

def norm_squared(self):
    r"""Return ⟨self, self⟩ using lattice bilinear form."""

def norm(self):
    r"""Return |self| = sqrt(|⟨self, self⟩|) (absolute value for indefinite case)."""

def is_isotropic(self):
    r"""Test if ⟨self, self⟩ = 0 (lies on light cone for indefinite lattices)."""
```

### Reflection Operations

```python
def reflection(self):
    r"""
    Return reflection s_v ∈ O(L_ℚ) in this vector.
    
    Always defined: s_v(x) = x - 2⟨x,v⟩/⟨v,v⟩ v
    
    OUTPUT: Linear transformation of L ⊗ ℚ
    
    NOTE: For roots in the root system, this preserves the lattice L.
    For general vectors, this may only preserve L ⊗ ℚ.
    """

def preserves_lattice(self):
    r"""
    Test if reflection in this vector preserves the ambient lattice.
    
    OUTPUT: True if s_v(L) = L, False if s_v(L) ⊆ L ⊗ ℚ only
    
    This is true precisely when v is in the root system.
    """
```

## Coxeter System Operations

### Root System Membership

```python
def is_root(self):
    r"""Test if this vector is in the root system R."""

def is_simple_root(self):
    r"""Test if this vector is a simple root (in Φ)."""

def is_positive_root(self):
    r"""Test if this is a positive root with respect to simple system."""

def is_negative_root(self):
    r"""Test if this is a negative root."""

def root_height(self):
    r"""
    Return height of this root (if it is a root).
    
    Height = sum of coefficients when expressed as linear combination of simple roots.
    """
```

### Simple Root Decomposition

```python
def simple_root_coordinates(self):
    r"""
    Express this vector in terms of simple roots.
    
    OUTPUT: Coordinates [c₁, c₂, ..., cₙ] such that self = Σ cᵢ αᵢ
    
    Only meaningful if this vector is in the root lattice ⟨Φ⟩_R.
    """

def positive_simple_support(self):
    r"""
    Return simple roots with positive coefficients.
    
    For positive roots, this gives the "support" of the root.
    """

def simple_root_string(self, direction):
    r"""
    Return α-string through this vector in given direction.
    
    INPUT:
    - ``direction`` -- Simple root α
    
    OUTPUT: Maximal sequence [..., α-2β, α-β, α, α+β, α+2β, ...]
    where β is this vector and all elements are roots.
    """
```

### Coroots and Duality

```python
def coroot(self):
    r"""
    Return coroot α^∨ = 2α/⟨α,α⟩.
    
    Only meaningful for roots. The coroot lies in the dual lattice.
    """

def fundamental_weight_coordinates(self):
    r"""
    Express this vector in terms of fundamental weights.
    
    Available only for crystallographic types.
    """

def weight_space_component(self, weight):
    r"""
    Project this vector onto given weight space.
    
    For representation theory applications.
    """
```

## Weyl Group Action

### Individual Reflections

```python
def apply_simple_reflection(self, i):
    r"""
    Apply i-th simple reflection to this vector.
    
    INPUT:
    - ``i`` -- Index of simple root (1-based)
    
    OUTPUT: s_i(self) where s_i is reflection in i-th simple root
    """

def apply_reflection(self, root):
    r"""
    Apply reflection in given root to this vector.
    
    INPUT:
    - ``root`` -- Root vector (must be in root system)
    
    OUTPUT: s_root(self)
    """
```

### Weyl Group Elements

```python
def apply_weyl_element(self, w):
    r"""
    Apply Weyl group element to this vector.
    
    INPUT:
    - ``w`` -- Element of Weyl group
    
    OUTPUT: w(self)
    """

def stabilizer_in_weyl_group(self):
    r"""
    Return subgroup of Weyl group fixing this vector.
    
    OUTPUT: Subgroup {w ∈ W : w(self) = self}
    """

def weyl_orbit(self):
    r"""
    Return Weyl group orbit of this vector.
    
    OUTPUT: Set {w(self) : w ∈ W}
    """
```

### Reduced Words

```python
def reflection_length(self):
    r"""
    Return minimal length of Weyl group element mapping self to dominant chamber.
    
    Only meaningful for roots or weight vectors.
    """

def reduced_word_to_dominant(self):
    r"""
    Return reduced word bringing this vector to dominant chamber.
    
    OUTPUT: Sequence of simple reflection indices
    """
```

## Chamber and Alcove Operations

### Chamber Membership

```python
def chamber(self):
    r"""
    Return chamber containing this vector.
    
    Chambers are connected components of L⊗ℝ minus hyperplane arrangement.
    """

def is_in_dominant_chamber(self):
    r"""
    Test if this vector is in dominant Weyl chamber.
    
    Dominant chamber: {x : ⟨x,αᵢ⟩ ≥ 0 for all simple roots αᵢ}
    """

def make_dominant(self):
    r"""
    Return Weyl group conjugate of this vector in dominant chamber.
    
    OUTPUT: w(self) where w ∈ W and ⟨w(self), αᵢ⟩ ≥ 0 for all i
    """
```

### Alcove Operations (Affine Types)

```python
def alcove(self):
    r"""
    Return alcove containing this vector (for affine types).
    
    Alcoves are fundamental domains for affine Weyl group action.
    """

def level(self):
    r"""
    Return level of this vector (for affine types).
    
    Level = coefficient of affine simple root when expressing in simple roots.
    """

def affine_height(self):
    r"""
    Return affine height (distance from level 0 hyperplane).
    """
```

## Special Root Operations

### Root Lengths and Angles

```python
def root_length_squared(self):
    r"""
    Return squared length ⟨α,α⟩ assuming this is a root.
    
    For multiple root length systems, this distinguishes long/short roots.
    """

def is_long_root(self):
    r"""Test if this is a long root (for multiple root length systems)."""

def is_short_root(self):
    r"""Test if this is a short root."""

def angle_with_simple_root(self, i):
    r"""
    Return angle between this vector and i-th simple root.
    
    Computed via inner products and norms.
    """
```

### Root System Generation

```python
def generate_root_system(self):
    r"""
    Generate root system starting from this vector.
    
    Applies all reflections iteratively until no new roots are found.
    Only meaningful if this vector generates the same root system.
    """

def positive_closure(self):
    r"""
    Return positive span R₊⟨self⟩ ∩ root system.
    
    All positive integer multiples that are roots.
    """
```

## Parabolic Structure

### Parabolic Decomposition

```python
def parabolic_component(self, subset):
    r"""
    Project this vector onto parabolic sublattice.
    
    INPUT:
    - ``subset`` -- Subset of simple root indices
    
    OUTPUT: Component in sublattice spanned by simple roots in subset
    """

def levi_component(self, subset):
    r"""Project onto Levi factor of parabolic subgroup."""

def unipotent_component(self, subset):
    r"""Project onto unipotent radical component."""
```

## Examples

### Basic Operations

```python
# Element in A₃ Coxeter lattice
A3 = CoxeterLattice.from_cartan_type('A3')
alpha1 = A3.simple_root(1)
alpha2 = A3.simple_root(2)

# Inner products
alpha1.inner_product(alpha2)  # -1 (off-diagonal Cartan entry)
alpha1.norm_squared()         # -2 (diagonal Cartan entry)

# Root operations  
alpha1.is_simple_root()       # True
alpha1.is_root()             # True
alpha1.is_positive_root()    # True
```

### Weyl Group Actions

```python
# Apply simple reflections
v = alpha1 + alpha2
v_reflected = v.apply_simple_reflection(1)  # s₁(α₁ + α₂) = -α₁ + α₂

# Weyl orbit
orbit = alpha1.weyl_orbit()  # All roots in Weyl orbit of α₁

# Move to dominant chamber
beta = -alpha1 - alpha2  # Negative root
beta_dominant = beta.make_dominant()  # Some positive root
```

### Root System Analysis

```python
# Positive root
gamma = alpha1 + alpha2  # Root of height 2
gamma.root_height()      # 2
gamma.simple_root_coordinates()  # [1, 1, 0]

# Reflection properties
gamma.reflection()       # Reflection s_γ ∈ O(L)
gamma.preserves_lattice()  # True (γ is a root)

# General vector
v = A3([1, 2, 3])       # Random lattice vector
v.is_root()             # Probably False
v.preserves_lattice()   # Probably False
```

### Affine Operations

```python
# Affine A₃
A3_aff = CoxeterLattice.from_cartan_type(['A', 3, 1])
v = A3_aff.simple_root(0)  # Affine simple root
v.level()               # 1 (coefficient of affine root)
v.affine_height()       # Distance from level 0

# Alcove membership
x = A3_aff([1, 0, 0, -1])
x.alcove()              # Which alcove contains x
```

This provides the complete interface for vectors in Coxeter lattices, combining general lattice operations with rich Coxeter-specific structure.