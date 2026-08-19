<!--
Origin: gitclones/Coxeter/implementation/planning/core/CATEGORY_INHERITANCE_GUIDE.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category Inheritance Guide: Abstract vs Concrete Methods

## The Confusion

In our abelian category framework, methods fall into three categories:

1. **Abstract/Interface methods**: Must be implemented by concrete categories
2. **Derived methods**: Implemented by the abstract category using abstract methods  
3. **Concrete methods**: Specific implementations for particular categories

This document clarifies which is which.

---

## Method Classification

### 🔶 **Abstract Methods** (Must Implement)

These define the **interface** that concrete abelian categories must provide:

```python
# In AbelianCategories.HomsetMethods:

def kernel(self):
    """Abstract: Concrete categories MUST implement this."""
    raise NotImplementedError("Concrete abelian categories must implement kernel()")

def cokernel(self):  
    """Abstract: Concrete categories MUST implement this."""
    raise NotImplementedError("Concrete abelian categories must implement cokernel()")

def _canonical_isomorphism(self, coimage_obj, image_obj):
    """Abstract: How coim(f) ≅ im(f) works in this category."""
    raise NotImplementedError("Concrete categories must implement canonical isomorphism")
```

**Why abstract?** These depend on the specific structure of objects in the category.

### 🟢 **Derived Methods** (Already Implemented)

These are implemented by the abstract category using the abstract methods:

```python
# In AbelianCategories.HomsetMethods:

def is_monomorphism(self):
    """Derived: Uses abstract kernel() method."""
    ker_obj, _ = self.kernel()
    return ker_obj.is_zero_object()

def is_epimorphism(self):
    """Derived: Uses abstract cokernel() method."""
    coker_obj, _ = self.cokernel()
    return coker_obj.is_zero_object()

def is_isomorphism(self):
    """Derived: Uses derived mono + epi tests."""
    return self.is_monomorphism() and self.is_epimorphism()

def image(self):
    """Derived: Uses abstract kernel() and cokernel()."""
    # Method 1: Image as cokernel of kernel  
    ker_obj, ker_mor = self.kernel()
    # ... uses ker_mor.cokernel()

def coimage(self):
    """Derived: Uses abstract kernel()."""
    ker_obj, ker_mor = self.kernel()
    return ker_mor.cokernel()  # A/ker(f)

def canonical_factorization(self):
    """Derived: Uses derived image() and coimage()."""
    coim_obj, epi_part = self.coimage()         
    im_obj, _, mono_part = self.image()         
    iso_part = self._canonical_isomorphism(coim_obj, im_obj)
    return epi_part, iso_part, mono_part
```

**Why derived?** These follow from universal properties that work the same in all abelian categories.

### 🔵 **Concrete Methods** (Category-Specific)

These are implemented by specific categories like `Modules(R)`:

```python
# In Modules.HomsetMethods:

def kernel(self):
    """Concrete: Kernel as submodule of domain."""
    if hasattr(self, 'matrix'):
        ker_matrix = self.matrix().right_kernel()
        return self.domain().submodule(ker_matrix.basis())
    else:
        raise NotImplementedError("Must implement for non-matrix morphisms")

def cokernel(self):
    """Concrete: Cokernel as quotient of codomain.""" 
    if hasattr(self, 'matrix'):
        im_matrix = self.matrix().column_space()
        coker_gens = self.codomain().basis() - im_matrix.basis()
        coker_submod = self.codomain().submodule(coker_gens)
        return self.codomain().quotient(coker_submod)  
    else:
        raise NotImplementedError("Must implement for non-matrix morphisms")
```

---

## The Pattern: Interface + Derived + Concrete

```python
# Abstract Category: Defines interface + derived methods
class AbelianCategories(Category):
    class HomsetMethods:
        # ABSTRACT: Must implement
        def kernel(self): raise NotImplementedError()
        def cokernel(self): raise NotImplementedError()
        
        # DERIVED: Already implemented using abstract methods
        def is_monomorphism(self):
            return self.kernel()[0].is_zero_object()
        
        def is_isomorphism(self):
            return self.is_monomorphism() and self.is_epimorphism()

# Concrete Category: Implements interface
class Modules(AbelianCategories.subcategory()):
    class HomsetMethods(AbelianCategories.HomsetMethods):
        # CONCRETE: Specific implementation
        def kernel(self):
            # Matrix-based kernel computation for modules
            return self.domain().submodule(self.matrix().right_kernel().basis())
```

---

## What You Need to Implement

When creating a new abelian category, you only need to implement the **abstract methods**:

### Required for ParentMethods:
- `_zero_object()` - The zero object construction

### Required for HomsetMethods:
- `kernel()` - Kernel object and morphism
- `cokernel()` - Cokernel object and morphism  
- `_canonical_isomorphism()` - How coim(f) ≅ im(f)

### Everything Else is Free!

Once you implement those 3-4 methods, you automatically get:
- `is_monomorphism()`, `is_epimorphism()`, `is_isomorphism()`
- `image()`, `coimage()`, `canonical_factorization()`
- Natural operators: `+`, `==`, `<=`
- Zero object testing and construction

---

## Benefits of This Design

### 1. **Mathematical Correctness**
The derived methods implement universal properties that are identical across all abelian categories.

### 2. **Minimal Implementation Burden**
You only implement the category-specific core operations.

### 3. **Consistency**
All abelian categories behave the same way for isomorphism testing, factorization, etc.

### 4. **Extensibility**
Add new derived methods once, all concrete categories inherit them.

---

## Example: Vector Spaces

```python
class VectorSpaces(AbelianCategories.subcategory()):
    class HomsetMethods(AbelianCategories.HomsetMethods):
        def kernel(self):
            # Linear algebra kernel
            return self.matrix().right_kernel_matrix().row_space()
        
        def cokernel(self):
            # Linear algebra cokernel
            return self.codomain().quotient(self.image()[0])
        
        def _canonical_isomorphism(self, coimage, image):
            # Isomorphism by dimension matching
            return coimage.isomorphism_to(image)
    
    # Now you automatically have:
    # - f.is_monomorphism() (checks if kernel is zero)
    # - f.is_isomorphism() (checks mono + epi)
    # - f.canonical_factorization() (epi-iso-mono factorization)
    # - All natural operators (+, ==, etc.)
```

---

## Documentation Convention

Let's use clear markers in docstrings:

```python
def kernel(self):
    """
    **ABSTRACT**: Concrete abelian categories must implement this.
    
    Return the kernel of this morphism...
    """
    raise NotImplementedError()

def is_monomorphism(self):
    """
    **DERIVED**: Implemented using abstract kernel() method.
    
    Test if this morphism is a monomorphism...
    """
    return self.kernel()[0].is_zero_object()

def kernel(self):  # In Modules category
    """
    **CONCRETE**: Matrix-based kernel computation for R-modules.
    
    Implementation of abstract kernel() for modules...
    """
    return self.domain().submodule(...)
```

This makes it crystal clear what's interface, what's implementation, and what's derived!