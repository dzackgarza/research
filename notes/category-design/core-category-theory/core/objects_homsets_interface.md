<!--
Origin: gitclones/Coxeter/implementation/planning/core/objects_homsets_interface.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects and Hom-sets Interface for Categories

This document implements the fundamental interface for objects and hom-sets in categories, incorporating lessons from Coq-HoTT and addressing the gaps identified in our mathematical audit.

---

## Core Design Principles

1. **Explicit objects collection**: Categories must provide access to their objects
2. **Hom-sets as Parents**: Each Hom(X,Y) is a SageMath Parent with its morphisms as elements
3. **Cached composition**: Composition can be cached for efficiency
4. **Clean notation**: Support standard mathematical notation f∘g or g;f

---

## Implementation

### **1. Enhanced Category Base Class**

```python
class Category(Parent):
    """
    Enhanced base class for categories with explicit objects and hom-sets.
    
    A category C consists of:
    - A collection of objects (accessible via C.objects())
    - For each pair (X,Y) of objects, a hom-set Hom(X,Y)
    - Composition of morphisms
    - Identity morphisms
    
    EXAMPLES::
    
        sage: C = SomeConcreteCategory()
        sage: C.objects()  # May be a list, Family, or DisjointUnionEnumeratedSets
        [Object1, Object2, ...]
        
        sage: X, Y = C.an_object(), C.an_object()
        sage: C.hom(X, Y)
        Set of Morphisms from X to Y in SomeConcreteCategory
        
        sage: f = C.hom(X, Y).an_element()
        sage: g = C.hom(Y, Z).an_element()
        sage: h = g * f  # Composition
        sage: h.parent() is C.hom(X, Z)
        True
    """
    
    @abstract_method
    def objects(self):
        """
        Return the collection of objects in this category.
        
        OUTPUT:
        An iterable of objects. Common return types:
        - list or tuple for finite categories
        - Family for indexed collections
        - DisjointUnionEnumeratedSets for infinite collections
        - generator for computed-on-demand objects
        
        EXAMPLES::
        
            sage: FiniteSets().objects()
            DisjointUnionEnumeratedSets(Family(Non negative integers, <lambda>))
            
            sage: Sets().objects()
            NotImplementedError: Sets has too many objects to enumerate
        """
        raise NotImplementedError(f"{self} must implement objects()")
    
    def hom(self, X, Y):
        """
        Return the hom-set Hom(X, Y).
        
        INPUT:
        - X: an object of this category
        - Y: an object of this category
        
        OUTPUT:
        The set of morphisms from X to Y as a Parent
        
        EXAMPLES::
        
            sage: C = Sets()
            sage: X = Set([1,2,3])
            sage: Y = Set(['a','b'])
            sage: H = C.hom(X, Y)
            sage: H
            Set of Morphisms from {1, 2, 3} to {'a', 'b'} in Category of sets
            sage: H.cardinality()
            8  # 2^3 functions
        """
        return Hom(X, Y, category=self)
    
    def hom_set(self, X, Y):
        """
        Alias for hom() for compatibility.
        """
        return self.hom(X, Y)
    
    def _Hom_(self, X, Y, category=None):
        """
        Internal method for creating hom-sets.
        
        Override this to customize hom-set construction.
        """
        if category is not self:
            raise ValueError(f"Hom-sets must be in the same category")
        
        # Default to generic hom-set
        from sage.categories.homset import Hom
        return Hom(X, Y, category=self)
    
    def compose(self, g, f):
        """
        Compose morphisms g ∘ f.
        
        INPUT:
        - g: morphism Y → Z
        - f: morphism X → Y
        
        OUTPUT:
        The composite morphism g ∘ f: X → Z
        
        NOTE:
        We use the standard mathematical convention where
        (g ∘ f)(x) = g(f(x)), so g comes first in the notation
        but acts second.
        """
        if f.codomain() != g.domain():
            raise TypeError(f"Cannot compose {g}: {g.domain()} → {g.codomain()} "
                           f"with {f}: {f.domain()} → {f.codomain()}")
        
        # Most morphisms support * for composition
        return g * f
    
    def identity(self, X):
        """
        Return the identity morphism on object X.
        
        EXAMPLES::
        
            sage: C = Sets()
            sage: X = Set([1,2,3])
            sage: id_X = C.identity(X)
            sage: id_X
            Identity morphism of {1, 2, 3}
            sage: id_X(2)
            2
        """
        return self.hom(X, X).identity()
    
    def has_object(self, X):
        """
        Test if X is an object of this category.
        
        Default implementation tests if X is in objects().
        Override for infinite categories.
        """
        try:
            return X in self.objects()
        except NotImplementedError:
            # For categories that can't enumerate objects,
            # try to construct hom(X, X) as a proxy test
            try:
                self.hom(X, X)
                return True
            except (TypeError, ValueError):
                return False
    
    @cached_method
    def an_object(self):
        """
        Return an object of this category.
        
        Useful for doctests and examples.
        """
        try:
            for obj in self.objects():
                return obj
        except NotImplementedError:
            raise NotImplementedError(f"{self} cannot provide example objects")
    
    def random_object(self):
        """
        Return a random object of this category.
        
        Override in concrete categories for better distributions.
        """
        return self.an_object()
    
    def is_full_subcategory_of(self, other):
        """
        Test if this is a full subcategory of other.
        
        A full subcategory has all morphisms between its objects.
        """
        if not self.is_subcategory_of(other):
            return False
        
        # Check that all morphisms are included
        try:
            for X in self.objects():
                for Y in self.objects():
                    if self.hom(X, Y) != other.hom(X, Y):
                        return False
            return True
        except NotImplementedError:
            raise NotImplementedError("Cannot verify full subcategory property")
```

### **2. Enhanced Homset Class**

```python
class CategoryHomset(Parent):
    """
    The set of morphisms between two objects in a category.
    
    EXAMPLES::
    
        sage: C = Sets()
        sage: X = Set([1,2])
        sage: Y = Set(['a','b','c'])
        sage: H = C.hom(X, Y)
        sage: H
        Set of Morphisms from {1, 2} to {'a', 'b', 'c'} in Category of sets
        
        sage: # Morphisms are elements of the hom-set
        sage: f = H(lambda x: 'a' if x == 1 else 'b')
        sage: f in H
        True
        
        sage: # Composition via multiplication
        sage: Z = Set([True, False])
        sage: g = C.hom(Y, Z)(lambda y: True if y == 'a' else False)
        sage: h = g * f  # g ∘ f
        sage: h(1)
        True
    """
    
    def __init__(self, X, Y, category=None, base=None, check=True):
        """
        Initialize a hom-set.
        
        INPUT:
        - X: source object (domain)
        - Y: target object (codomain)
        - category: the ambient category
        - base: base ring (for module categories)
        - check: whether to verify objects are in category
        """
        self._domain = X
        self._codomain = Y
        self._category = category or X.category()
        
        if check:
            if not self._category.has_object(X):
                raise ValueError(f"{X} is not an object of {self._category}")
            if not self._category.has_object(Y):
                raise ValueError(f"{Y} is not an object of {self._category}")
        
        # Determine category of hom-set itself
        # (usually Sets(), but might be Modules(R) for enriched categories)
        if base is not None:
            from sage.categories.modules import Modules
            homset_category = Modules(base)
        else:
            from sage.categories.sets_cat import Sets
            homset_category = Sets()
        
        Parent.__init__(self, base=base, category=homset_category)
    
    def _repr_(self):
        return f"Set of Morphisms from {self._domain} to {self._codomain} in {self._category}"
    
    def domain(self):
        """Return the domain (source) object."""
        return self._domain
    
    def codomain(self):
        """Return the codomain (target) object."""
        return self._codomain
    
    def source(self):
        """Alias for domain()."""
        return self._domain
        
    def target(self):
        """Alias for codomain()."""
        return self._codomain
    
    def identity(self):
        """
        Return the identity morphism if domain == codomain.
        
        EXAMPLES::
        
            sage: C = Sets()
            sage: X = Set([1,2,3])
            sage: H = C.hom(X, X)
            sage: id = H.identity()
            sage: id(2)
            2
            sage: f = H.an_element()
            sage: f * id == f == id * f
            True
        """
        if self._domain != self._codomain:
            raise ValueError("Identity morphism only exists for End(X)")
        
        # Most concrete categories override this
        return self.element_class(self, is_identity=True)
    
    def zero(self):
        """
        Return the zero morphism if it exists.
        
        Only available in categories with zero morphisms.
        """
        if not hasattr(self._category, 'zero_morphism'):
            raise ValueError(f"{self._category} does not have zero morphisms")
        
        return self._category.zero_morphism(self._domain, self._codomain)
    
    @cached_method
    def endomorphism_ring(self):
        """
        If this is End(X), return the endomorphism ring structure.
        
        EXAMPLES::
        
            sage: C = VectorSpaces(QQ)
            sage: V = QQ^3
            sage: End_V = C.hom(V, V)
            sage: End_V.endomorphism_ring()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
        """
        if self._domain != self._codomain:
            raise ValueError("Endomorphism ring only exists for End(X)")
        
        # Return self with ring structure
        # Concrete categories should override for efficiency
        return self
    
    def __call__(self, *args, **kwargs):
        """
        Construct a morphism in this hom-set.
        
        EXAMPLES::
        
            sage: C = Sets()
            sage: X = Set([1,2])
            sage: Y = Set(['a','b'])
            sage: H = C.hom(X, Y)
            sage: f = H(lambda x: 'a' if x == 1 else 'b')
            sage: f(1)
            'a'
        """
        # Dispatch to element constructor
        return self.element_class(self, *args, **kwargs)
```

### **3. Composition Infrastructure**

```python
class CategoryWithCompositionCache(Category):
    """
    Mixin for categories that cache composition of morphisms.
    
    Useful for categories where composition is expensive to compute.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._composition_cache = {}
    
    def compose(self, g, f, cache=True):
        """
        Compose g ∘ f with optional caching.
        """
        if not cache:
            return super().compose(g, f)
        
        # Cache key is (g, f) pair
        key = (g, f)
        if key in self._composition_cache:
            return self._composition_cache[key]
        
        # Compute composition
        result = super().compose(g, f)
        
        # Cache if morphisms are immutable
        if hasattr(g, '__hash__') and hasattr(f, '__hash__'):
            try:
                hash(g)
                hash(f) 
                self._composition_cache[key] = result
            except TypeError:
                pass  # Not hashable, don't cache
        
        return result
    
    def clear_composition_cache(self):
        """Clear the composition cache."""
        self._composition_cache.clear()
```

### **4. Examples of Concrete Implementation**

```python
class FiniteEnumeratedSetsExample(Category):
    """
    Example: The category of finite enumerated sets.
    
    Demonstrates how to implement objects() and hom().
    """
    
    def objects(self):
        """
        Return finite enumerated sets.
        
        We can't return ALL of them, so we return a DisjointUnionEnumeratedSets
        that can generate them on demand.
        """
        from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
        from sage.sets.family import Family
        from sage.sets.non_negative_integers import NonNegativeIntegers
        
        # Family of all sets of size n
        def sets_of_size_n(n):
            # This is a generator of all sets of size n
            # In practice, we'd enumerate these more carefully
            if n == 0:
                yield Set([])
            elif n == 1:
                # All singletons - infinitely many!
                # Just return some examples
                for i in range(10):
                    yield Set([i])
            # etc.
        
        return DisjointUnionEnumeratedSets(
            Family(NonNegativeIntegers(), sets_of_size_n)
        )
    
    def _Hom_(self, X, Y, category=None):
        """
        Hom-set for finite enumerated sets.
        """
        # Use specialized FiniteEnumeratedSetHomset
        return FiniteEnumeratedSetHomset(X, Y, category=self)
    
    def has_object(self, X):
        """
        Check if X is a finite enumerated set.
        """
        from sage.sets.set import Set_object_enumerated
        return isinstance(X, Set_object_enumerated) and X.is_finite()

class FiniteEnumeratedSetHomset(CategoryHomset):
    """
    Hom-sets in FiniteEnumeratedSets are finite sets of functions.
    """
    
    def cardinality(self):
        """
        Number of functions from X to Y is |Y|^|X|.
        """
        return self._codomain.cardinality() ** self._domain.cardinality()
    
    def __iter__(self):
        """
        Iterate over all functions X → Y.
        """
        from itertools import product
        
        # Each function is determined by where it sends each element
        for image_tuple in product(self._codomain, repeat=self._domain.cardinality()):
            # Create the function
            images = dict(zip(self._domain, image_tuple))
            yield self(images)
    
    def identity(self):
        """
        The identity function.
        """
        return self(lambda x: x)
```

---

## Integration with Existing Infrastructure

### **1. Backward Compatibility**
- Existing categories that don't implement objects() continue to work
- Default implementations fall back gracefully
- Hom() function continues to work as before

### **2. Category Axioms**
```python
class CategoryWithObjects(CategoryAxiom):
    """
    Axiom: Category can enumerate its objects.
    """
    def has_object_enumeration(self):
        try:
            iter(self.objects())
            return True
        except NotImplementedError:
            return False

class CategoryWithHomSets(CategoryAxiom):
    """
    Axiom: Category provides explicit hom-sets.
    """
    def has_explicit_homsets(self):
        try:
            X = self.an_object()
            H = self.hom(X, X)
            return isinstance(H, Parent)
        except NotImplementedError:
            return False
```

### **3. Diagram Category Integration**
With explicit objects and hom-sets, our diagram categories become more natural:

```python
def product_diagram(objects, category):
    """
    Create diagram for product using explicit objects.
    """
    n = len(objects)
    
    # Verify all objects are in the category
    for obj in objects:
        if not category.has_object(obj):
            raise ValueError(f"{obj} is not in {category}")
    
    # Create discrete diagram
    index = discrete_category(range(n))
    return Diagram(index, category, dict(enumerate(objects)))
```

---

## Benefits of This Design

1. **Mathematical Clarity**: Objects and morphisms are first-class citizens
2. **Better Error Messages**: Can check if objects are actually in the category
3. **Efficient Iteration**: Categories can optimize object enumeration
4. **Clean Notation**: Standard mathematical notation works naturally
5. **Caching Support**: Composition can be cached when beneficial
6. **Extensibility**: Easy to add new features like enriched hom-sets

This completes the fundamental objects and hom-sets interface, providing the foundation needed for proper limit/colimit implementations!