<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/implementation-notes/homotopy-theory/stable-category/sp_bilr_mod_morphisms.md`
>
> **Preamble status.** Absent. Morphisms of formed modules are owned (`FormMorphism`, `FormHomset` in `form_modules.sage`; isometries in `integrallattice/lattice_isometries.sage`).
>
> **Recorded error.** Condition 3 of the definition of a stable map, that the map becomes an equivalence after enough suspensions, defines a stable *equivalence*. Morphisms of a stable category are arbitrary maps and need never become equivalences; the zero map is one.

---

# Morphisms in Sp(BilR-Mod): Stable Maps Between Spectra

Morphisms in the stable ∞-category Sp(BilR-Mod) are stable maps between bilinear module spectra.

## Definition of Morphisms

A **stable map** f: E → F between bilinear module spectra consists of:
1. Compatible maps f_n: E_n → F_n for each level n
2. Compatibility with structure maps: σ_F ∘ Σf_n = f_{n+1} ∘ σ_E
3. Stability: f becomes an equivalence after enough suspensions

## Basic Morphism Types

### Level Maps
```python
class LevelMap:
    """
    A map f: E → F induced by maps at each level.
    
    Structure:
    - f_n: E_n → F_n for each level n
    - Compatibility with suspension structure
    - Represents "unstable" phenomena that become stable
    """
    
    def __init__(self, level_maps, source_spectrum, target_spectrum):
        pass
    
    def level_map(self, n):
        """Return the map E_n → F_n at level n."""
        pass
    
    def is_stable_equivalence(self):
        """Check if map becomes equivalence after enough suspensions."""
        pass
```

### Suspension Maps
```python
class SuspensionMap:
    """
    The suspension map Σ: E → ΣE in the stable category.
    
    Properties:
    - Equivalence in Sp(BilR-Mod) (not in unstable category)
    - Canonical inverse given by desuspension
    - Generator of the stable equivalences
    """
    
    def __init__(self, spectrum):
        pass
    
    def inverse(self):
        """The desuspension map ΣE → E (exists in stable category)."""
        pass
```

### Structure Maps
```python
class StructureMap:
    """
    Structure maps σ_n: ΣE_n → E_{n+1} defining the spectrum.
    
    Properties:
    - Part of the datum of a spectrum
    - Encode how suspension interacts with the spectrum structure
    - Must satisfy coherence conditions
    """
    
    def __init__(self, source_level, target_level):
        pass
    
    def coherence_check(self):
        """Verify structure map satisfies spectrum axioms."""
        pass
```

## Derived and Stable Phenomena

### Mapping Spectra
```python
class MappingSpectrum:
    """
    The mapping spectrum Map(E,F) = internal hom in Sp(BilR-Mod).
    
    Structure:
    - Map(E,F)_n = holim_k MapBilR-Mod(E_k, F_{n+k})
    - Represents "derived" hom from E to F
    - π_*(Map(E,F)) gives stable homotopy classes
    
    Universal property:
    - Map(E ∧ F, G) ≅ Map(E, Map(F,G))
    """
    
    def __init__(self, source, target):
        pass
    
    def homotopy_classes(self, degree):
        """Compute π_degree(Map(E,F)) = stable maps up to homotopy."""
        pass
    
    def evaluation_map(self):
        """The evaluation Map(E,F) ∧ E → F."""
        pass
```

### Stable Homotopy Classes
```python
class StableHomotopyClass:
    """
    Stable homotopy classes [E,F] = morphisms in Ho(Sp(BilR-Mod)).
    
    Definition:
    - [E,F] = colim_n [Σ^n E, Σ^n F]
    - Stabilization of unstable homotopy classes
    - What we compute in practice
    """
    
    def __init__(self, source, target, representing_map):
        pass
    
    def compose(self, other):
        """Composition of stable homotopy classes."""
        pass
    
    def suspension(self):
        """Image under suspension Σ: [E,F] → [ΣE,ΣF]."""
        pass
```