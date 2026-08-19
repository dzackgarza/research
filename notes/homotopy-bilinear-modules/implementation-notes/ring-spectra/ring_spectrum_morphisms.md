<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/implementation-notes/homotopy-theory/ring-spectra/ring_spectrum_morphisms.md`
>
> **Preamble status.** Absent. Base change along a ring morphism is owned as a functor with its adjunction (`categories/functors/base_change_adjunction.sage`, `algebra_base_change.sage`); the ring-spectrum layer above it is absent.

---

# Ring Spectrum Morphisms in Sp(BilR-Mod)

Morphisms in the category of ring spectra - maps that preserve ring structure.

## Definition of Ring Spectrum Morphisms

A **ring spectrum morphism** f: R → S consists of:
1. **Underlying map**: f: R → S as morphism in Sp(BilR-Mod)
2. **Multiplicativity**: f ∘ μ_R = μ_S ∘ (f ∧ f)
3. **Unit preservation**: f ∘ η_R = η_S
4. **Coherence**: Preservation of higher multiplicative structure

## Basic Ring Morphism Types

### Ring Homomorphisms
```python
class RingSpectrumHomomorphism:
    """
    A ring map f: R → S between ring spectra.
    
    Properties:
    - Preserves multiplication: f(xy) = f(x)f(y)
    - Preserves unit: f(1) = 1
    - Induces functor f*: R-Mod → S-Mod
    """
    
    def __init__(self, source_ring, target_ring, underlying_map):
        pass
    
    def induced_module_functor(self):
        """The functor f*: R-Mod → S-Mod."""
        pass
    
    def is_faithfully_flat(self):
        """Check if map is faithfully flat for descent."""
        pass
    
    def change_of_rings_isomorphism(self):
        """S ⊗_R M ≅ f*(M) for R-modules M."""
        pass
```

### Localizations
```python
class LocalizationMap:
    """
    Localization map R → R[S⁻¹] inverting multiplicative set S.
    
    Structure:
    - Universal among ring maps R → T that invert S
    - Changes arithmetic properties significantly
    - Often simplifies computations
    """
    
    def __init__(self, base_ring, multiplicative_set):
        pass
    
    def universal_property(self, test_ring, test_map):
        """Unique factorization through localization."""
        pass
    
    def fiber_sequence(self):
        """Fiber sequence computing what's lost in localization."""
        pass
```

### Completion Maps
```python
class CompletionMap:
    """
    Completion map R → R^∧_I at ideal I.
    
    Structure:
    - R^∧_I = lim R/I^n (inverse limit)
    - Universal for continuous maps to I-adically complete rings
    - Changes topology but preserves much algebra
    """
    
    def __init__(self, base_ring, ideal):
        pass
    
    def completion_tower(self):
        """Tower ... → R/I³ → R/I² → R/I."""
        pass
    
    def hensel_lifting(self):
        """Hensel's lemma for solutions modulo I^n."""
        pass
```

## Structural Ring Morphisms

### Inclusions and Extensions
```python
class InclusionMap:
    """
    Inclusion R → S as sub-ring spectrum.
    
    Types:
    - Direct summand inclusions
    - Subring inclusions (Z ⊆ Q)
    - Extension field inclusions
    """
    
    def __init__(self, subring, parent_ring):
        pass
    
    def extension_functor(self):
        """(-) ⊗_R S: R-Mod → S-Mod."""
        pass
    
    def restriction_functor(self):
        """Forget S-action: S-Mod → R-Mod."""
        pass
    
    def norm_map(self):
        """Norm map in the opposite direction S → R."""
        pass
```

### Quotient Maps
```python
class QuotientMap:
    """
    Quotient map R → R/I for ideal I.
    
    Structure:
    - Kernel is the ideal spectrum HI
    - Cofiber sequence: HI → R → R/I
    - Universal for maps killing I
    """
    
    def __init__(self, base_ring, ideal_spectrum):
        pass
    
    def kernel_ideal(self):
        """The ideal I as spectrum HI."""
        pass
    
    def cofiber_sequence(self):
        """HI → R → R/I cofiber sequence."""
        pass
```

## Functorial Morphisms

### Base Change Maps
```python
class BaseChangeMap:
    """
    Base change map R → S inducing change of coefficients.
    
    Construction:
    - Given ring map φ: R → S
    - For R-algebra A, get S-algebra S ⊗_R A
    - Functorial in both variables
    """
    
    def __init__(self, base_map, algebra):
        pass
    
    def tensor_product_formula(self):
        """S ⊗_R A construction."""
        pass
    
    def descent_data(self):
        """Descent data for faithfully flat base change."""
        pass
```

### Transfer Maps
```python
class TransferMap:
    """
    Transfer map S → R for inclusion R → S.
    
    Construction:
    - Dual to extension: trace or norm-like operation
    - Exists when S is finite flat over R
    - Right adjoint to extension in some sense
    """
    
    def __init__(self, large_ring, small_ring):
        pass
    
    def degree_formula(self):
        """tr ∘ ext = multiplication by [S:R]."""
        pass
    
    def adams_operations_compatibility(self):
        """Compatibility with Adams operations."""
        pass
```

## Derived and Homotopical Morphisms

### K-Theory Maps
```python
class KTheoryInducedMap:
    """
    K-theory map K(R) → K(S) induced by ring map R → S.
    
    Construction:
    - Apply K-theory functor to ring map
    - Preserves K-theory ring structure
    - Encodes change of coefficients in K-theory
    """
    
    def __init__(self, ring_map):
        pass
    
    def on_k_groups(self, degree):
        """Induced map K_degree(R) → K_degree(S)."""
        pass
    
    def multiplicative_structure(self):
        """Preservation of K-theory ring structure."""
        pass
```

### THH Maps
```python
class THHInducedMap:
    """
    THH map THH(R) → THH(S) induced by ring map R → S.
    
    Construction:
    - THH is functorial for ring maps
    - Preserves E_∞ structure and S¹-actions
    - Starting point for trace method computations
    """
    
    def __init__(self, ring_map):
        pass
    
    def circle_action_compatibility(self):
        """Preservation of S¹-action on THH."""
        pass
    
    def dennis_trace_naturality(self):
        """Naturality of Dennis trace K → THH."""
        pass
```