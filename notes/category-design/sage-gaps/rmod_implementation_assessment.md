<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/misc/RMOD_IMPLEMENTATION_ASSESSMENT.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is an ALGORITHM/REQUIREMENT SURVEY written against SageMath as it
stood in the source tree. Rows now owned by the preamble, and errors the
audit recorded, are listed in the README.md of this directory.
-->

# RMod Category Implementation Assessment

## Executive Summary

Creating a new RMod category that combines symbolic-first computation with numerical efficiency is **highly viable**. SageMath provides excellent infrastructure we can reuse:

1. **AbelianCategory** exists as a minimal base class
2. **TensorProductsCategory** provides monoidal structure (no explicit SymmetricMonoidalCategory needed)
3. Both **FreeModule_generic** and **CombinatorialFreeModule** have clean, reusable code
4. The category framework supports all necessary mathematical structures

## Key Findings

### 1. Category Infrastructure

#### AbelianCategory (EXISTS)
```python
# From sage/categories/category_types.py
class AbelianCategory(Category):
    def is_abelian(self):
        return True
```
- Minimal implementation - perfect for extension
- Used by `CommutativeAdditiveGroups` and similar categories

#### SymmetricMonoidalCategory (NOT EXPLICIT)
- Not a separate class in SageMath
- Instead, implemented via `TensorProductsCategory` and `TensorProductFunctor`
- Found in: `sage/categories/tensor.py`
- Categories with tensor products automatically get monoidal structure

#### Modules Category Structure
```python
class Modules(Category_module):
    # Full support for:
    # - Tensor products
    # - Dual objects
    # - Cartesian products
    # - Homomorphisms
    # - Base change functors
```

### 2. Implementation Strategies

#### FreeModule_generic Strengths
- Clean numerical implementation
- Efficient vector operations
- Good for coordinate-based computations
- Inherits from `Module_free_ambient`
- ~2000 lines of reusable code

#### CombinatorialFreeModule Strengths
- Natural algebraic notation: `2*e + 3*f`
- Symbolic basis handling via `IndexedGenerators`
- Built-in support for graded structures
- Category framework integration
- ~3000 lines, but modular design

### 3. Code Reuse Opportunities

#### From FreeModule_generic
```python
# Key methods we can adapt:
- coordinate_vector() / to_vector()
- gram_schmidt() 
- matrix representations
- submodule generation
- linear algebra operations
```

#### From CombinatorialFreeModule
```python
# Key infrastructure to reuse:
- IndexedGenerators mixin for basis notation
- _repr_ methods for pretty printing
- monomial/term infrastructure
- category integration patterns
```

## Proposed RMod Implementation

### Core Design

```python
from sage.categories.category import Category
from sage.categories.category_types import AbelianCategory, Category_over_base_ring
from sage.categories.tensor import TensorProductsCategory
from sage.structure.parent import Parent
from sage.structure.indexed_generators import IndexedGenerators

class RModCategory(AbelianCategory, Category_over_base_ring):
    """
    Category of R-modules with emphasis on symbolic computation.
    
    Combines:
    - Symbolic basis notation from CombinatorialFreeModule
    - Efficient numerics from FreeModule_generic
    - Proper categorical structure (abelian + monoidal)
    """
    
    def super_categories(self):
        from sage.categories.modules import Modules
        return [Modules(self.base_ring())]
    
    class ParentMethods:
        # Inherit key methods from both implementations
        pass
    
    class ElementMethods:
        # Symbolic operations with conversion to numerical
        pass
    
    class TensorProducts(TensorProductsCategory):
        # Symmetric monoidal structure
        pass

class RMod(Parent, IndexedGenerators):
    """
    An R-module with symbolic-first computation.
    
    Features:
    - Natural notation: M.<e,f,g> = RMod(QQ, ['e','f','g'])
    - Efficient conversion to numerical vectors
    - Full categorical structure
    """
    
    def __init__(self, base_ring, basis_keys, **kwds):
        # Combine best initialization from both
        Parent.__init__(self, category=RModCategory(base_ring))
        IndexedGenerators.__init__(self, basis_keys, **kwds)
        
    def _element_constructor_(self, x):
        # Smart constructor handling both symbolic and numeric input
        pass
        
    def to_vector(self, element):
        # Efficient conversion to FreeModule vectors
        pass
        
    def from_vector(self, vec):
        # Convert back from numerical representation
        pass
```

### Key Implementation Points

1. **Symbolic First**: Default representation uses basis symbols
2. **Efficient Conversion**: Easy `to_vector()` for numerical computation
3. **Category Integration**: Proper abelian and monoidal structure
4. **Code Reuse**: Copy tested implementations from both sources
5. **Clean API**: Best of both worlds without the baggage

## Specific Code to Reuse

### From CombinatorialFreeModule
- `IndexedGenerators.__init__` (lines 200-250) - basis setup
- `_repr_term` and `_repr_` methods - pretty printing
- `monomial()` and `term()` - element construction
- Category registration patterns

### From FreeModule_generic  
- Vector space algorithms (gram_schmidt, etc.)
- Submodule generation code
- Matrix representation methods
- Numerical linear algebra interfaces

### From Categories Framework
- `TensorProductFunctor` - monoidal structure
- `DualObjectsCategory` - dual modules
- `HomsetsCategory` - morphism spaces
- `CartesianProductsCategory` - direct sums

## Implementation Timeline

1. **Phase 1**: Core RMod category and parent class (~200 lines)
2. **Phase 2**: Element class with symbolic operations (~150 lines)
3. **Phase 3**: Conversion methods to/from numerical (~100 lines)
4. **Phase 4**: Tensor products and categorical operations (~150 lines)
5. **Phase 5**: Integration with bilinear forms (~100 lines)

Total: ~700 lines of new code, heavily leveraging existing implementations.

## Advantages Over Existing Solutions

1. **Cleaner than inheriting CombinatorialFreeModule**: No monomial baggage
2. **More flexible than FreeModule_generic**: Symbolic computation support
3. **Better for indefinite lattices**: Custom optimizations possible
4. **Maintainable**: Clear separation of concerns
5. **Extensible**: Easy to add specialized methods

## Risks and Mitigations

1. **Risk**: Missing some category integration
   - **Mitigation**: Careful study of both implementations
   
2. **Risk**: Performance overhead in conversions
   - **Mitigation**: Lazy conversion, caching strategies
   
3. **Risk**: Compatibility with existing SageMath code
   - **Mitigation**: Implement standard interfaces, coercion

## Conclusion

Creating a new RMod category is not only viable but recommended. We can:
- Reuse significant code from both implementations
- Create a cleaner, more focused design
- Optimize specifically for indefinite lattice computations
- Maintain full mathematical rigor and categorical structure

The SageMath infrastructure provides all necessary building blocks. We just need to assemble them in a way that serves our specific needs without inheriting unnecessary complexity.