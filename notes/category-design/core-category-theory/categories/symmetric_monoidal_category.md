<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/symmetric_monoidal_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Abstract Symmetric Monoidal Categories

Base class defining the axiomatic structure of symmetric monoidal categories.

## Definition

```python
class SymmetricMonoidalCategory:
    """
    Abstract base class for symmetric monoidal categories.
    
    Axiomatic Data:
    - tensor_product: bifunctor ⊗: C × C → C
    - unit_object: object 1 in C
    - associator: α: (A ⊗ B) ⊗ C ≃ A ⊗ (B ⊗ C)
    - left_unitor: λ: 1 ⊗ A ≃ A
    - right_unitor: ρ: A ⊗ 1 ≃ A
    - braiding: β: A ⊗ B ≃ B ⊗ A
    
    Must satisfy coherence axioms (pentagon, triangle, hexagon).
    """
    
    def tensor_product(self, obj1, obj2):
        """Abstract tensor product obj1 ⊗ obj2."""
        raise NotImplementedError
    
    def unit_object(self):
        """Abstract unit object 1."""
        raise NotImplementedError
    
    def associator(self, obj1, obj2, obj3):
        """α: (A ⊗ B) ⊗ C ≃ A ⊗ (B ⊗ C)."""
        raise NotImplementedError
    
    def left_unitor(self, obj):
        """λ: 1 ⊗ A ≃ A."""
        raise NotImplementedError
    
    def right_unitor(self, obj):
        """ρ: A ⊗ 1 ≃ A."""
        raise NotImplementedError
    
    def braiding(self, obj1, obj2):
        """β: A ⊗ B ≃ B ⊗ A."""
        raise NotImplementedError
    
    def pentagon_axiom(self):
        """
        Pentagon axiom for associator coherence.
        
        The diagram:
        ((A⊗B)⊗C)⊗D → (A⊗B)⊗(C⊗D) → A⊗(B⊗(C⊗D))
               ↓                            ↑
        (A⊗(B⊗C))⊗D ──────→ A⊗((B⊗C)⊗D)
        
        must commute.
        """
        raise NotImplementedError
    
    def triangle_axiom(self):
        """
        Triangle axiom relating associator and unitors.
        
        The diagram:
        (A⊗1)⊗B → A⊗(1⊗B)
            ↓         ↓
            A⊗B ──→ A⊗B
        
        must commute.
        """
        raise NotImplementedError
    
    def hexagon_axiom(self):
        """
        Hexagon axiom for braiding and associator coherence.
        
        Two hexagonal diagrams relating braiding with associativity
        must commute.
        """
        raise NotImplementedError
```

## Coherence Conditions

A symmetric monoidal category must satisfy:

1. **Pentagon axiom**: Associator coherence
2. **Triangle axiom**: Unitor-associator coherence  
3. **Hexagon axioms**: Braiding-associator coherence
4. **Symmetry**: β ∘ β = id (braiding is self-inverse)

## Examples

Implementations include:
- BilR-Mod with tensor product over R
- Sp(BilR-Mod) with smash product
- Chain complexes with tensor product
- Spectra with smash product