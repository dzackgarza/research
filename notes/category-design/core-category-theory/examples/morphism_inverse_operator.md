<!--
Origin: gitclones/Coxeter/implementation/planning/examples/morphism_inverse_operator.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Overriding the ^(-1) Operator for Morphisms

A design exploration for making `f^(-1)(y)` mean "choose a preimage of y under f" instead of the current `f.lift(y)`.

## Current SageMath Behavior

```python
# Current way to get preimages
sage: V = QQ^3
sage: W = QQ^2  
sage: f = V.hom([[1, 2], [3, 4], [5, 6]])
sage: y = W([7, 8])

# Get a preimage (if it exists)
sage: x = f.lift(y)  # Current method
sage: f(x) == y
True

# But this would be much more natural:
sage: x = f^(-1)(y)  # Proposed syntax
sage: f(x) == y
True
```

## Design Challenges

### 1. The `^` Operator in SageMath

Currently `f^n` means:
- `f^1 = f` (identity)
- `f^2 = f * f` (composition)  
- `f^(-1)` = inverse morphism (when f is invertible)

So we need to be careful about backwards compatibility.

### 2. Mathematical Clarity

We want to distinguish:
- `f^(-1)`: The inverse morphism (when f is bijective)
- `f^(-1)(y)`: A preimage of y (when y ∈ im(f))

## Proposed Implementation

```python
class RModuleMorphism(ModuleMorphism):
    """
    Enhanced morphisms with natural preimage syntax.
    """
    
    def __pow__(self, n):
        """
        Override the ^ operator to handle various cases.
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: f = V.hom([[1, 0], [0, 1], [0, 0]])  # V → QQ^2
            
            # Positive powers = composition
            sage: f^2  # f ∘ f (when domain = codomain)
            TypeError: Cannot compose f: QQ^3 → QQ^2 with itself
            
            # f^1 is identity
            sage: f^1 == f
            True
            
            # f^0 should be identity on domain (when f is endomorphism)
            sage: g = V.hom([[1, 0, 0], [0, 2, 0], [0, 0, 3]])  # V → V
            sage: g^0 == V.identity()
            True
            
            # f^(-1) for invertible morphisms
            sage: h = V.hom([[2, 0, 0], [0, 3, 0], [0, 0, 1]])  # Invertible
            sage: h^(-1) * h == V.identity()
            True
            
            # f^(-1) for non-invertible morphisms returns PreimageOperator
            sage: f^(-1)
            Preimage operator of Linear transformation: QQ^3 → QQ^2
        """
        if n == 1:
            return self
        elif n == 0:
            if self.domain() != self.codomain():
                raise TypeError("f^0 only defined for endomorphisms")
            return self.domain().identity()
        elif n > 1:
            if self.domain() != self.codomain():
                raise TypeError(f"Cannot compose f: {self.domain()} → {self.codomain()} with itself")
            result = self
            for _ in range(n - 1):
                result = result * self
            return result
        elif n == -1:
            # Key innovation: return PreimageOperator for non-invertible morphisms
            if self.is_isomorphism():
                return self.inverse()
            else:
                return PreimageOperator(self)
        else:  # n < -1
            if not self.is_isomorphism():
                raise TypeError("Negative powers only defined for invertible morphisms")
            inv = self.inverse()
            return inv^(-n)
    
    def lift(self, y):
        """
        DEPRECATED: Use f^(-1)(y) instead.
        
        This method is kept for backwards compatibility.
        """
        import warnings
        warnings.warn("Use f^(-1)(y) instead of f.lift(y)", DeprecationWarning)
        return (self^(-1))(y)


class PreimageOperator:
    """
    Represents the preimage operation f^(-1): im(f) → domain(f).
    
    This is NOT a morphism - it's a partial function that only
    works on elements in the image of f.
    
    EXAMPLES::
    
        sage: V = QQ^3
        sage: W = QQ^2
        sage: f = V.hom([[1, 2], [3, 4], [5, 6]])
        sage: finv = f^(-1)
        sage: finv
        Preimage operator of Linear transformation: QQ^3 → QQ^2
        
        sage: # Use it to find preimages
        sage: y = W([7, 8])
        sage: x = finv(y)  # This is f^(-1)(y)
        sage: f(x) == y
        True
        
        sage: # Error for elements not in image
        sage: z = W([1, 0])  # Might not be in image
        sage: finv(z)
        ValueError: Element (1, 0) is not in the image of f
    """
    
    def __init__(self, morphism):
        """
        Initialize the preimage operator.
        
        INPUT:
        - morphism -- the morphism f: A → B
        """
        self._morphism = morphism
        self._domain = morphism.codomain()  # Domain of f^(-1)
        self._codomain = morphism.domain()  # Codomain of f^(-1)
    
    def __call__(self, y):
        """
        Find a preimage of y under the original morphism.
        
        INPUT:
        - y -- element of the codomain of the original morphism
        
        OUTPUT:
        - x -- element of the domain such that f(x) = y
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: W = QQ^2
            sage: f = V.hom([[1, 0], [0, 1], [1, 1]])
            sage: finv = f^(-1)
            
            # Find preimage
            sage: y = W([2, 3])
            sage: x = finv(y)
            sage: f(x) == y
            True
            
            # Multiple preimages - returns one arbitrarily
            sage: # ker(f) = span{(1, 0, -1)}, so f^(-1)(y) + ker(f) are all preimages
            
            sage: # Error for y not in image
            sage: try:
            ...     finv(W([1, 2]))  # This might not be in image
            ... except ValueError as e:
            ...     print(e)
            Element (1, 2) is not in the image
        """
        # Check if y is in the image
        if not self._in_image(y):
            raise ValueError(f"Element {y} is not in the image of {self._morphism}")
        
        # Find a preimage using the morphism's built-in lift method
        return self._morphism.lift(y)
    
    def _in_image(self, y):
        """
        Check if y is in the image of the morphism.
        
        This could be implemented efficiently for specific morphism types.
        """
        try:
            self._morphism.lift(y)
            return True
        except (ValueError, TypeError):
            return False
    
    def __repr__(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: f = V.hom([[1, 2], [3, 4], [5, 6]])
            sage: f^(-1)
            Preimage operator of Linear transformation: QQ^3 → QQ^2
        """
        return f"Preimage operator of {self._morphism}"
    
    def domain(self):
        """
        Return the domain of the preimage operator.
        
        This is the image of the original morphism.
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: f = V.hom([[1, 0], [0, 1], [0, 0]])
            sage: finv = f^(-1)
            sage: finv.domain()
            Vector space of dimension 2 over Rational Field  # im(f) ≅ QQ^2
        """
        return self._morphism.image()
    
    def codomain(self):
        """
        Return the codomain of the preimage operator.
        
        This is the domain of the original morphism.
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: f = V.hom([[1, 0], [0, 1], [0, 0]])
            sage: finv = f^(-1)
            sage: finv.codomain()
            Vector space of dimension 3 over Rational Field
        """
        return self._codomain
    
    def kernel(self):
        """
        Return the kernel of the preimage operator.
        
        This is always trivial since f^(-1) is well-defined on im(f).
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: f = V.hom([[1, 0], [0, 1], [0, 0]])
            sage: finv = f^(-1)
            sage: finv.kernel()
            Trivial subspace of Vector space of dimension 2
        """
        return self.domain().subspace([])
    
    def is_injective(self):
        """
        Test if the preimage operator is injective.
        
        This is true iff the original morphism is surjective.
        
        EXAMPLES::
        
            sage: # Surjective morphism
            sage: V = QQ^3
            sage: W = QQ^2
            sage: f = V.hom([[1, 0], [0, 1], [1, 1]])  # Surjective
            sage: finv = f^(-1)
            sage: finv.is_injective()
            True
            
            sage: # Non-surjective morphism  
            sage: g = V.hom([[1, 0], [2, 0], [3, 0]])  # Not surjective
            sage: ginv = g^(-1)
            sage: ginv.is_injective()
            False  # Multiple preimages exist
        """
        return self._morphism.is_surjective()
    
    def fiber(self, y):
        """
        Return all preimages of y (the fiber over y).
        
        INPUT:
        - y -- element in the image of the original morphism
        
        OUTPUT:
        - Affine subspace x₀ + ker(f) where f(x₀) = y
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: W = QQ^2  
            sage: f = V.hom([[1, 0], [0, 1], [1, 1]])
            sage: finv = f^(-1)
            
            sage: y = W([2, 3])
            sage: fiber = finv.fiber(y)
            sage: fiber
            Affine subspace of QQ^3: (2, 3, 0) + Span{(-1, 0, 1)}
            
            sage: # All elements of fiber map to y
            sage: all(f(x) == y for x in fiber.some_elements())
            True
        """
        if not self._in_image(y):
            raise ValueError(f"Element {y} is not in the image")
        
        # Get one preimage
        x0 = self(y)
        
        # The fiber is x0 + ker(f)
        kernel = self._morphism.kernel()
        return kernel.translation(x0)


## Usage Examples

```python
# Example 1: Linear transformation
sage: V = QQ^3
sage: W = QQ^2
sage: f = V.hom([[1, 2], [3, 4], [5, 6]])

# Old way
sage: y = W([7, 8])  
sage: x = f.lift(y)
sage: f(x) == y
True

# New way - much more natural!
sage: x = f^(-1)(y)
sage: f(x) == y  
True

# Example 2: Quotient maps
sage: V = QQ^3
sage: S = V.subspace([(1, 1, 0)])
sage: pi = V.quotient_map(S)  # V → V/S

sage: y_bar = pi(V([2, 3, 1]))  # Element of quotient
sage: x = pi^(-1)(y_bar)       # Lift back to V
sage: pi(x) == y_bar
True

# Example 3: Error handling
sage: f = V.hom([[1, 0], [0, 0], [0, 0]])  # Not surjective
sage: try:
...     f^(-1)(W([0, 1]))  # (0,1) not in image
... except ValueError as e:
...     print(f"Expected error: {e}")
Expected error: Element (0, 1) is not in the image of f

# Example 4: Invertible morphisms work as before
sage: g = V.hom([[2, 0, 0], [0, 3, 0], [0, 0, 1]])  # Invertible
sage: g^(-1)  # Returns actual inverse morphism
Linear transformation: QQ^3 → QQ^3
sage: (g^(-1) * g).is_identity()
True
```

## Benefits

### 1. **Natural Notation**
- `f^(-1)(y)` is standard mathematical notation
- Much clearer than `f.lift(y)`
- Matches what students expect

### 2. **Backwards Compatibility**  
- `f^(-1)` still returns inverse for invertible morphisms
- `f.lift()` still works (with deprecation warning)
- Existing code continues to function

### 3. **Error Handling**
- Clear error messages when y ∉ im(f)
- Distinguishes between "not invertible" and "element not in image"

### 4. **Rich Structure**
- PreimageOperator has domain, codomain, kernel methods
- Can compute fibers (all preimages of an element)
- Supports advanced linear algebra operations

## Potential Issues

### 1. **Performance**
- Checking if y ∈ im(f) might be expensive
- Could cache image for repeated queries

### 2. **Ambiguity**
- For non-injective f, which preimage to return?
- Current design: return arbitrary preimage (same as lift)

### 3. **Type Confusion**
- f^(-1) returns different types (morphism vs PreimageOperator)
- Need good documentation and error messages

## Implementation Strategy

1. **Start with linear transformations** (most common case)
2. **Add support for other morphism types** gradually
3. **Extensive testing** for edge cases
4. **Good documentation** with clear examples
5. **Deprecation path** for old `lift()` method

This would make SageMath much more intuitive for students and researchers! The notation `f^(-1)(y)` is exactly what mathematicians write on paper.