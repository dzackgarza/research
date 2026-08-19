<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/implementation-notes/homotopy-theory/ring-spectra/ring_spectrum_objects.md`
>
> **Preamble status.** Absent.

---

# Ring Spectrum Objects in Sp(BilR-Mod)

Objects in the category of ring spectra - spectra equipped with multiplication and unit structures.

## Definition of Ring Spectrum Objects

A **ring spectrum object** R in Sp(BilR-Mod) consists of:
1. **Underlying spectrum**: R as object in Sp(BilR-Mod)
2. **Multiplication**: μ: R ∧ R → R (associative up to homotopy)
3. **Unit**: η: S → R (from sphere spectrum S)
4. **Coherence**: Higher homotopies making diagrams commute

## Fundamental Ring Spectrum Objects

### Sphere Spectrum
```python
class SphereSpectrum:
    """
    The sphere spectrum S = Σ^∞S^0 as initial ring spectrum.
    
    Properties:
    - Initial object in ring spectra: unique map S → R for any ring spectrum R
    - π_*(S) = stable homotopy groups of spheres
    - Unit for smash product: S ∧ R ≃ R
    """
    
    def __init__(self):
        pass
    
    def homotopy_groups(self):
        """π_*(S) = stable homotopy groups of spheres."""
        pass
    
    def universal_ring_map(self, target_ring):
        """Unique ring map S → R for any ring spectrum R."""
        pass
```

### Eilenberg-MacLane Ring Spectra
```python
class EilenbergMacLaneRingSpectrum:
    """
    The Eilenberg-MacLane ring spectrum HR for a ring R.
    
    Properties:
    - π_0(HR) = R, π_i(HR) = 0 for i ≠ 0
    - E_∞ when R is commutative
    - Represents ordinary cohomology with coefficients in R
    """
    
    def __init__(self, coefficient_ring):
        pass
    
    def steenrod_operations(self):
        """Power operations when R = Z/p."""
        pass
    
    def cohomology_theory(self):
        """The associated cohomology theory X ↦ [X, HR]."""
        pass
```

### Group Ring Spectra
```python
class GroupRingSpectrum:
    """
    Group ring spectrum S[G] for finite group G.
    
    Construction:
    - S[G] = ⋁_{g∈G} S (wedge sum over group elements)
    - Multiplication from group multiplication
    - Unit sends 1 to identity element
    """
    
    def __init__(self, finite_group):
        pass
    
    def representation_ring(self):
        """The representation ring R(G) from G-spectra."""
        pass
    
    def transfer_maps(self, subgroup):
        """Transfer maps from subgroup H ⊆ G."""
        pass
```

## Specialized Ring Spectrum Objects

### Topological Hochschild Homology Spectra
```python
class TopologicalHochschildHomologySpectrum:
    """
    THH(R) = topological Hochschild homology of ring spectrum R.
    
    Definition:
    - THH(R) = R ⊗_{R⊗R^op} R in the ∞-category of R-bimodules
    - Has natural S¹-action from cyclic structure
    - Starting point for trace methods in K-theory
    """
    
    def __init__(self, ring_spectrum):
        pass
    
    def circle_action(self):
        """The natural S¹-action on THH(R)."""
        pass
    
    def dennis_trace_map(self):
        """The trace map K(R) → THH(R)."""
        pass
    
    def topological_cyclic_homology(self):
        """TC(R) from THH(R) with circle action."""
        pass
```

### K-Theory Ring Spectra
```python
class AlgebraicKTheoryRingSpectrum:
    """
    The algebraic K-theory spectrum K(R) of ring spectrum R.
    
    Definition:
    - K(R) = K(R-Mod^perf) for perfect R-modules
    - Ring structure from tensor product of modules
    - Universal among stable ring theories on R-modules
    """
    
    def __init__(self, ring_spectrum):
        pass
    
    def k_groups(self, degree):
        """K_degree(R) = π_degree(K(R))."""
        pass
    
    def trace_to_thh(self):
        """The Dennis trace K(R) → THH(R)."""
        pass
```

## Computational Ring Spectrum Objects

### Matrix Ring Spectra
```python
class MatrixRingSpectrum:
    """
    Matrix ring spectrum M_n(R) over ring spectrum R.
    
    Definition:
    - M_n(R) = End(R^n) in R-modules
    - Morita equivalent to R
    - Represents n×n matrices over R
    """
    
    def __init__(self, base_ring, matrix_size):
        pass
    
    def morita_equivalence(self):
        """The Morita equivalence with base ring."""
        pass
    
    def k_theory_comparison(self):
        """Isomorphism K(M_n(R)) ≃ K(R)."""
        pass
```

### Completion and Localization Objects
```python
class LocalizedRingSpectrum:
    """
    Localization R[S⁻¹] of ring spectrum R.
    
    Construction:
    - Formal inversion of multiplicative set S ⊆ π_*(R)
    - Universal ring map R → R[S⁻¹] inverting S
    - Changes structural properties dramatically
    """
    
    def __init__(self, base_ring, multiplicative_set):
        pass
    
    def localization_map(self):
        """Universal map R → R[S⁻¹]."""
        pass
```