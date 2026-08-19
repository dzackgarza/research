<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/implementation-notes/homotopy-theory/ring-spectra/ring_spectra_category.md`
>
> **Preamble status.** Absent. The preamble owns algebras over a ring (`categories/algebras/`) and the centre functor (`categories/functors/ring_centers.sage`), which are the unstable shadows of these objects.

---

# Category: Ring Spectra in Sp(BilR-Mod)

The category of ring objects in the stable ∞-category of bilinear module spectra.

## Mathematical Definition

A **ring spectrum** in Sp(BilR-Mod) is a spectrum R equipped with:
1. **Multiplication**: μ: R ∧ R → R (associative up to coherent homotopy)
2. **Unit**: η: S → R (where S is the sphere spectrum)
3. **Coherence data**: Higher homotopies making this an A_∞ or E_∞ ring object

## Category Structure

### Objects
Ring spectra R with multiplication and unit structure.

### Morphisms  
Ring maps f: R → S that preserve multiplication and unit:
- f ∘ μ_R = μ_S ∘ (f ∧ f)
- f ∘ η_R = η_S

### Composition
Standard composition of spectrum maps, compatible with ring structure.

## Ring Spectrum Types

### E_∞ Ring Spectra
```python
class EInfinityRingSpectrum:
    """
    E_∞ ring spectrum - commutative ring object in Sp(BilR-Mod).
    
    Structure:
    - Multiplication is commutative up to all higher homotopies
    - Action of symmetric groups on tensor powers
    - Admits theories of modules, algebras, etc.
    """
    
    def __init__(self, underlying_spectrum, multiplication, unit, coherence):
        pass
    
    def power_operations(self):
        """The power operations P^i in cohomology."""
        pass
    
    def formal_group_law(self):
        """The associated formal group law over π_*(R)."""
        pass
```

### A_∞ Ring Spectra
```python
class AInfinityRingSpectrum:
    """
    A_∞ ring spectrum - associative ring object in Sp(BilR-Mod).
    
    Structure:
    - Multiplication associative up to coherent homotopy
    - No commutativity required
    - Still admits module categories
    """
    
    def __init__(self, underlying_spectrum, multiplication, unit):
        pass
    
    def hochschild_homology(self):
        """THH(R) = R ⊗_{R^e} R."""
        pass
    
    def derived_center(self):
        """The derived center as an E_∞ ring."""
        pass
```

### Matrix Ring Spectra
```python
class MatrixRingSpectrum:
    """
    Matrix ring spectra M_n(R) over a ring spectrum R.
    
    Structure:
    - M_n(R) = End(R^n) as ring spectrum
    - Morita equivalent to R for finite n
    - Generalizes matrix rings to stable setting
    """
    
    def __init__(self, base_ring, matrix_size):
        pass
    
    def morita_equivalence(self):
        """The Morita equivalence with base ring."""
        pass
```

## Module Categories

### Module Spectra
```python
class ModuleSpectrumCategory:
    """
    The ∞-category R-Mod of module spectra over ring spectrum R.
    
    Objects: Spectra M with action R ∧ M → M
    Morphisms: R-linear maps between modules
    
    Structure:
    - Symmetric monoidal via ⊗_R
    - Complete and cocomplete
    - Stable ∞-category
    """
    
    def __init__(self, ring_spectrum):
        pass
    
    def tensor_product(self, module1, module2):
        """M ⊗_R N over the ring spectrum R."""
        pass
    
    def internal_hom(self, module1, module2):
        """Hom_R(M,N) in R-modules."""
        pass
```

### Algebraic K-Theory of Ring Spectra
```python
class RingSpectrumKTheory:
    """
    K-theory K(R) of a ring spectrum R.
    
    Definition:
    - K(R) = K(R-Mod^perf) for perfect R-modules
    - Represents algebraic K-theory in stable setting
    - Generalizes classical K-theory of rings
    """
    
    def __init__(self, ring_spectrum):
        pass
    
    def k_groups(self, degree):
        """Compute K_degree(R)."""
        pass
    
    def trace_map_to_thh(self):
        """The Dennis trace K(R) → THH(R)."""
        pass
```