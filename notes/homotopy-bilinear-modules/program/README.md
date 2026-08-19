<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/connections/homotopy_theory/README.md`
>
> **Preamble status.** Program overview. The preamble owns the category of modules with a form (`categories/modules/framed/formed/form_modules.sage`) and the hyperbolic plane as a catalogue specimen (`Lattices.U`, `catalogue.sage`). It owns no chain complexes, no simplicial objects, no spectra, and no stable category; nothing in this document has an implemented counterpart.
>
> **Recorded error.** This overview states the suspension as the orthogonal sum with a hyperbolic plane on each side, while `suspension/suspension_functor.md` states it as one hyperbolic plane; see the note on that file.

---

# Homotopy Theory for Bilinear Modules

This directory contains the modern homotopy-theoretic approach to bilinear modules using ∞-categories and spectra.

## Overview

Instead of classical homological algebra from the 1960s, we use the modern framework of stable ∞-categories. The key insight is that the derived category D(BilR-Mod) is better understood as the homotopy category of a stable ∞-category.

## Directory Structure

```
homotopy_theory/
├── README.md                          # This file
├── suspension/
│   └── suspension_functor.md          # Suspension functor Σ: BilR-Mod → BilR-Mod
├── infinity_categories/
│   └── bilinear_infinity_category.md  # The ∞-category BilR-Mod^∞
└── spectra/
    └── bilinear_module_spectra.md     # Stable ∞-category Sp(BilR-Mod)
```

## Key Concepts

### 1. Suspension Functor
The suspension functor Σ adds hyperbolic planes:
```
ΣM = H ⊕ M ⊕ H
```
where H is the hyperbolic plane. This is functorial and leads to the stabilization.

### 2. ∞-Category Structure
BilR-Mod^∞ enhances the ordinary category with:
- Higher morphisms (homotopies between morphisms)
- Homotopy coherent limits and colimits
- Derived tensor products and internal homs

### 3. Stable ∞-Category of Spectra
Sp(BilR-Mod) is the stabilization - the ∞-categorical colimit of:
```
BilR-Mod --Σ--> BilR-Mod --Σ--> BilR-Mod --Σ--> ...
```

Objects are sequences {E_n} with structure maps ΣE_n → E_{n+1}.

## Why This Approach?

1. **Conceptual Clarity**: Spectra naturally encode all derived phenomena
2. **Computational Power**: Modern tools from stable homotopy theory apply
3. **Generality**: Works for any ring R, not just nice ones
4. **Connections**: Links to K-theory, L-theory, and motivic homotopy theory

## Classical Recovery

The classical constructions are recovered as:
- Ext groups: π_* of mapping spectra
- Tor groups: π_* of smash products  
- Resolutions: Cofibrant replacements in model structure
- Spectral sequences: From filtered spectra

## Implementation Notes

This is primarily a theoretical framework. Actual computations would use:
- Model category of chain complexes for concrete calculations
- Spectral sequence machinery for homotopy groups
- The equivalence D(BilR-Mod) ≃ Ho(Sp(BilR-Mod))