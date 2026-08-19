<!--
Origin: gitclones/Coxeter/implementation/planning/examples/category_decorators.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Category Method Decorators

Clean decorator-based approach to mark abstract vs derived methods.

---

## The Decorators

```python
def abstract_method(func):
    """
    Mark a method as abstract - must be implemented by concrete categories.
    
    Adds metadata and provides clear error messages.
    """
    func._category_method_type = 'abstract'
    func._original_doc = func.__doc__
    
    def wrapper(self, *args, **kwargs):
        category_name = getattr(self.category(), '_name', str(self.category()))
        raise NotImplementedError(
            f"Abstract method {func.__name__} must be implemented by "
            f"concrete category {category_name}"
        )
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = f"**ABSTRACT**: {func._original_doc or ''}"
    wrapper._category_method_type = 'abstract'
    return wrapper

def derived_method(depends_on=None):
    """
    Mark a method as derived - implemented using abstract methods.
    
    Args:
        depends_on: List of abstract methods this depends on
    """
    def decorator(func):
        func._category_method_type = 'derived'
        func._depends_on = depends_on or []
        func._original_doc = func.__doc__
        
        # Update docstring
        deps_str = ', '.join(func._depends_on) if func._depends_on else 'abstract methods'
        func.__doc__ = f"**DERIVED** (uses {deps_str}): {func._original_doc or ''}"
        
        return func
    return decorator

def concrete_method(implements=None):
    """
    Mark a method as concrete - specific implementation for this category.
    
    Args:
        implements: Name of abstract method this implements
    """
    def decorator(func):
        func._category_method_type = 'concrete'
        func._implements = implements
        func._original_doc = func.__doc__
        
        impl_str = f" (implements {implements})" if implements else ""
        func.__doc__ = f"**CONCRETE{impl_str}**: {func._original_doc or ''}"
        
        return func
    return decorator
```

---

## Usage in Abelian Categories

```python
class AbelianCategories(Category):
    class HomsetMethods:
        @abstract_method
        def kernel(self):
            """
            Return the kernel of this morphism.
            
            For morphism f: A → B, the kernel is the object ker(f) together
            with the kernel morphism k: ker(f) → A such that f ∘ k = 0
            and ker(f) is universal with this property.
            """
            pass  # Implementation provided by decorator
        
        @abstract_method  
        def cokernel(self):
            """
            Return the cokernel of this morphism.
            
            For morphism f: A → B, the cokernel is the object coker(f) together  
            with the cokernel morphism c: B → coker(f) such that c ∘ f = 0
            and coker(f) is universal with this property.
            """
            pass
        
        @derived_method(depends_on=['kernel'])
        def is_monomorphism(self):
            """
            Test if this morphism is a monomorphism (injective).
            
            In abelian categories, f is mono iff ker(f) = 0.
            """
            ker_obj, _ = self.kernel()
            return ker_obj.is_zero_object()
        
        @derived_method(depends_on=['cokernel'])
        def is_epimorphism(self):
            """
            Test if this morphism is an epimorphism (surjective).
            
            In abelian categories, f is epi iff coker(f) = 0.
            """
            coker_obj, _ = self.cokernel()
            return coker_obj.is_zero_object()
        
        @derived_method(depends_on=['is_monomorphism', 'is_epimorphism'])
        def is_isomorphism(self):
            """
            Test if this morphism is an isomorphism.
            
            In abelian categories, f is iso iff it's both mono and epi.
            """
            return self.is_monomorphism() and self.is_epimorphism()
        
        @derived_method(depends_on=['kernel', 'cokernel'])
        def image(self):
            """
            Return the image of this morphism.
            
            Standard construction: im(f) = ker(coker(f)) = coker(ker(f)).
            """
            # Implementation using kernel() and cokernel()
            ker_obj, ker_mor = self.kernel()
            coker_obj, coker_mor = self.cokernel()
            
            try:
                quotient_obj, quotient_mor = ker_mor.cokernel()
                mono_part = self._induced_map_to_codomain(quotient_mor)
                return quotient_obj, quotient_mor, mono_part
            except NotImplementedError:
                image_obj, image_mor = coker_mor.kernel()
                epi_part = self._induced_map_from_domain(image_mor)
                return image_obj, epi_part, image_mor
```

---

## Usage in Concrete Categories

```python
class Modules(AbelianCategories.subcategory()):
    class HomsetMethods(AbelianCategories.HomsetMethods):
        @concrete_method(implements='kernel')
        def kernel(self):
            """
            Kernel as submodule of domain.
            
            Uses matrix representation to compute right kernel.
            """
            if hasattr(self, 'matrix'):
                ker_matrix = self.matrix().right_kernel()
                return self.domain().submodule(ker_matrix.basis())
            else:
                raise NotImplementedError("Must implement for non-matrix morphisms")
        
        @concrete_method(implements='cokernel')
        def cokernel(self):
            """
            Cokernel as quotient of codomain.
            
            Uses matrix representation to compute quotient by image.
            """
            if hasattr(self, 'matrix'):
                im_matrix = self.matrix().column_space()
                coker_gens = self.codomain().basis() - im_matrix.basis()
                coker_submod = self.codomain().submodule(coker_gens)
                return self.codomain().quotient(coker_submod)
            else:
                raise NotImplementedError("Must implement for non-matrix morphisms")
        
        # All derived methods (is_monomorphism, is_isomorphism, etc.) 
        # are automatically inherited!
```

---

## Benefits

### 1. **Clear Method Classification**
```python
# Check what type of method it is
>>> f.kernel._category_method_type
'abstract'
>>> f.is_monomorphism._category_method_type  
'derived'
>>> f.kernel._depends_on  # For derived methods
['kernel']
```

### 2. **Dependency Tracking**
```python
def check_category_completeness(category):
    """Check if all abstract methods are implemented."""
    missing = []
    for method_name in dir(category):
        method = getattr(category, method_name)
        if getattr(method, '_category_method_type', None) == 'abstract':
            if method.__name__ not in implemented_methods:
                missing.append(method_name)
    return missing
```

### 3. **Automatic Documentation**
The decorators automatically update docstrings with clear markers.

### 4. **Better Error Messages**
```python
>>> f.kernel()  # In abstract category
NotImplementedError: Abstract method kernel must be implemented by 
concrete category Category of modules over Integer Ring
```

### 5. **IDE Support**
IDEs can use the metadata to provide better autocomplete and warnings.

---

## Advanced Features

### Method Validation
```python
@derived_method(depends_on=['kernel', 'cokernel'])
def image(self):
    # Check dependencies are available
    for dep in image._depends_on:
        if not hasattr(self, dep):
            raise AttributeError(f"Derived method image requires {dep}")
    # ... implementation
```

### Category Introspection
```python
def get_abstract_methods(category):
    """Get all abstract methods that need implementation."""
    methods = []
    for name in dir(category):
        method = getattr(category, name)
        if getattr(method, '_category_method_type', None) == 'abstract':
            methods.append(name)
    return methods

def get_derived_methods(category):
    """Get all methods implemented by the abstract category."""
    methods = []
    for name in dir(category):
        method = getattr(category, name)
        if getattr(method, '_category_method_type', None) == 'derived':
            methods.append((name, method._depends_on))
    return methods
```

### Documentation Generation
```python
def generate_category_docs(category):
    """Auto-generate documentation showing method inheritance."""
    abstract = get_abstract_methods(category)
    derived = get_derived_methods(category)
    
    print("Abstract Methods (must implement):")
    for method in abstract:
        print(f"  - {method}")
    
    print("\nDerived Methods (automatically available):")
    for method, deps in derived:
        print(f"  - {method} (uses: {', '.join(deps)})")
```

This gives us clean separation with zero boilerplate!