<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/bilinear_module_morphisms.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# BilinearModuleMorphism Framework

## Core Design: Extending Sage's Morphism Infrastructure

This framework extends SageMath's existing Hom/Morphism system with bilinear form awareness, following Sage's category-theoretic patterns while adding specialized functionality for integral lattices and root systems.

## 1. BilinearModuleMorphism Class

```python
class BilinearModuleMorphism(ModuleMorphism):
    """Morphism between modules equipped with bilinear forms.
    
    Extends Sage's ModuleMorphism with form preservation checks
    and primitive embedding detection for integral lattices.
    """
    
    def is_form_preserving(self):
        """Check if φ(v)·φ(w) = v·w for all v,w in domain."""
        
    def is_primitive_embedding(self):
        """Check if inclusion has no common factors (coprime image)."""
        
    def form_defect(self, v, w):
        """Compute φ(v)·φ(w) - v·w to measure form preservation failure."""
        
    def induced_gram_morphism(self):
        """Return morphism φ*: Gram(codomain) → Gram(domain)."""
```

## 2. BilinearModules Category Integration

```python
class BilinearModules(Category_over_base_ring):
    """Category of modules with bilinear forms."""
    
    class ParentMethods:
        def hom(self, codomain, im_gens, check=True):
            """Override to return BilinearModuleMorphism instances."""
            
        def primitive_embedding(self, ambient_module, element):
            """Create ⟨element⟩ ↪ ambient_module morphism."""
            
        def element_inclusion(self, element):
            """Create element → parent inclusion morphism."""
            
    class ElementMethods:
        def inclusion_morphism(self):
            """Return this element's inclusion: self → parent."""
            
        def primitive_sublattice_embedding(self):
            """Return ⟨self⟩_ℤ ↪ parent morphism."""
```

## 3. Element-Morphism Tracking System

```python
class BilinearModuleElement(ModuleElement):
    """Element that tracks its inclusion morphisms."""
    
    def __init__(self, parent, coords, **kwargs):
        super().__init__(parent, coords)
        self._inclusion_cache = {}
        
    @cached_method
    def as_inclusion(self):
        """Return inclusion morphism {self} → parent."""
        
    @cached_method 
    def primitive_embedding(self):
        """Return ⟨self⟩_ℤ ↪ parent embedding."""
        
    def compose_inclusions(self, target_module):
        """Chain: {self} → ⟨self⟩ → parent → target."""
```

## 4. Mathematical Examples

```python
# Root system example: α ∈ Φ carries both morphisms
R = RootSystem(['A', 3])
L = R.root_lattice()  # Bilinear module
alpha = L.simple_root(1)

# Element inclusion: α → L  
inc_element = alpha.as_inclusion()

# Primitive embedding: ⟨α⟩_ℤ ↪ L
emb_sublattice = alpha.primitive_embedding()

# Composition chain
target = R.weight_lattice()
composition = alpha.compose_inclusions(target)

# Form preservation check
assert inc_element.is_form_preserving()
assert emb_sublattice.is_primitive_embedding()
```

## 5. Integration with Sage Infrastructure

Leverages existing Sage patterns:
- **HomSet framework**: Creates `BilinearModuleHomset` automatically
- **Category coercion**: Bilinear modules inherit `.hom()` method  
- **Caching system**: Uses `@cached_method` for expensive computations
- **Composition**: Standard `*` operator for morphism composition
- **Kernel/Image**: Inherits `.kernel()`, `.image()` from parent class

This design extends rather than replaces Sage's morphism infrastructure, ensuring compatibility while adding the specialized bilinear form functionality needed for Coxeter system analysis.