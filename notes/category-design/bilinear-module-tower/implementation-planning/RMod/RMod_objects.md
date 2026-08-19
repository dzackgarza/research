<!--
Origin: gitclones/Coxeter/implementation/planning/RMod/RMod_objects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects: R-Module Parent Implementation

Parent class implementation for R-modules with computational methods.

## Parent Class Structure

```python
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.indexed_generators import IndexedGenerators

class RModule_with_basis(UniqueRepresentation, Parent, IndexedGenerators):
    """
    Concrete parent class for R-modules with symbolic basis.
    
    This is the main parent class for R-modules. It provides:
    - Symbolic basis with natural notation
    - Efficient conversion to numerical representations
    - Integration with the category framework
    - Natural operations (+, *, @, /) for split Grothendieck ring
    
    INPUT:
    - base_ring -- the base ring R
    - basis -- list of basis element names (optional)
    - category -- the category (defaults to RModules(base_ring).WithBasis())
    - prefix -- prefix for basis elements
    - **kwds -- additional options for IndexedGenerators
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
        sage: M
        Free module over Integer Ring with basis {a, b, c}
        
        sage: M.an_element()
        2*a + 3*b + c
        
        sage: M in RModules(ZZ).WithBasis()
        True
    """
    
    def __init__(self, base_ring, basis=None, category=None, prefix=None, **kwds):
        """
        Initialize an R-module with symbolic basis.
        
        TESTS::
        
            sage: M = RModule_with_basis(QQ, basis=['x', 'y'])
            sage: TestSuite(M).run()
        """
        # Set up category
        if category is None:
            from sage.categories.rmodules import RModules
            category = RModules(base_ring).WithBasis()
            # If basis is finite, add FinitelyGenerated
            if basis is not None and len(basis) < float('inf'):
                category = category & RModules(base_ring).FinitelyGenerated()
        
        # Initialize parent
        Parent.__init__(self, base=base_ring, category=category)
        
        # Set up basis
        if basis is not None:
            self._basis_keys = basis
        else:
            # Will be set by _first_ngens for generator assignment
            self._basis_keys = None
            
        # Initialize generators
        if self._basis_keys is not None:
            IndexedGenerators.__init__(self, self._basis_keys, prefix=prefix, **kwds)
    
    def _element_constructor_(self, x=None):
        """
        Construct a module element.
        
        Handles various input formats:
        - Lists/tuples of coordinates
        - Vectors over any ring (converts to base ring)
        - Existing module elements
        - Zero for zero element
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(QQ, basis=['a', 'b', 'c'])
            sage: M(0)
            0
            sage: M([1, 0, -1])  # From coordinate list
            a - c
            sage: M({'a': 2, 'c': 3})  # From coefficient dict
            2*a + 3*c
        """
        from sage.modules.rmodule_element import RModuleElement
        
        if x is None or x == 0:
            return self.zero()
            
        if isinstance(x, RModuleElement) and x.parent() is self:
            return x
            
        # Handle coordinate lists/tuples
        if isinstance(x, (list, tuple)):
            R = self.base_ring()
            try:
                # Convert each entry to base ring
                coeffs = {i: R(c) for i, c in enumerate(x) if c != 0}
                return self._from_dict(coeffs)
            except (TypeError, ValueError) as err:
                raise TypeError(f"Cannot convert coordinates to {R}: {err}")
        
        # Handle coefficient dictionaries
        if isinstance(x, dict):
            return self._from_dict(x)
            
        # Handle vectors (from any ring)
        if hasattr(x, 'parent') and hasattr(x.parent(), 'is_vector_space'):
            R = self.base_ring()
            try:
                coeffs = {i: R(c) for i, c in enumerate(x) if c != 0}
                return self._from_dict(coeffs)
            except (TypeError, ValueError) as err:
                raise TypeError(f"Cannot convert vector entries to {R}: {err}")
        
        # Default element construction for other types
        return super()._element_constructor_(x)
    
    def basis(self):
        """
        Return the basis of this module.
        
        EXAMPLES::
        
            sage: M = RModule_with_basis(ZZ, basis=['x', 'y', 'z'])
            sage: list(M.basis())
            [x, y, z]
        """
        from sage.sets.family import Family
        return Family(self._basis_keys, self.monomial)
    
    def _first_ngens(self, n):
        """
        Used by the preparser for generator assignment.
        
        EXAMPLES::
        
            sage: M.<x,y,z> = RMod(ZZ)  # Calls this method
            sage: M._first_ngens(3)
            (x, y, z)
        """
        if self._basis_keys is None:
            # Set up basis from generator assignment
            self._basis_keys = [f'e{i}' for i in range(n)]
            IndexedGenerators.__init__(self, self._basis_keys)
            
        return self.gens()[:n]
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
            Free module over Integer Ring with basis {a, b, c}
        """
        if self._basis_keys:
            basis_str = ', '.join(map(str, self._basis_keys))
            return f"Free module over {self.base_ring()} with basis {{{basis_str}}}"
        else:
            return f"Free module over {self.base_ring()}"
```

## Computational Methods

```python
def rank(self):
    """
    Return the rank of this free module.
    
    For modules with basis, this is the cardinality of the basis.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
        sage: M.rank()
        3
        
        sage: # Empty basis gives rank 0
        sage: Z = RModule_with_basis(QQ, basis=[])
        sage: Z.rank()
        0
    """
    if self._basis_keys is None:
        raise NotImplementedError("Rank not defined for modules without basis")
    return len(self._basis_keys)

def dimension(self):
    """
    Alias for rank().
    
    In the context of free modules, dimension = rank.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['x', 'y'])
        sage: M.dimension()
        2
        sage: M.rank() == M.dimension()
        True
    """
    return self.rank()

def is_free(self):
    """
    Test if this module is free.
    
    Modules with basis are always free by definition.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b'])
        sage: M.is_free()
        True
    """
    return True  # WithBasis implies Free

def is_finitely_generated(self):
    """
    Test if this module is finitely generated.
    
    For modules with basis, this depends on whether the basis is finite.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['x', 'y', 'z'])
        sage: M.is_finitely_generated()
        True
        
        sage: # Infinite basis would give False (when implemented)
        sage: # M_inf = RModule_with_basis(ZZ, basis=Naturals())
        sage: # M_inf.is_finitely_generated()
        sage: # False
    """
    if self._basis_keys is None:
        return None  # Unknown
    return len(self._basis_keys) < float('inf')

def zero(self):
    """
    Return the zero element of this module.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['e', 'f'])
        sage: M.zero()
        0
        sage: M.zero().is_zero()
        True
    """
    return self._from_dict({})

def an_element(self):
    """
    Return a typical element of this module.
    
    Used by TestSuite and for general examples.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['a', 'b', 'c'])
        sage: M.an_element()
        2*a + 3*b + c
    """
    if not self._basis_keys:
        return self.zero()
    
    # Create element with coefficients 2, 3, 1, 0, 0, ...
    coeffs = {}
    for i, key in enumerate(self._basis_keys[:3]):  # At most 3 terms
        if i == 0:
            coeffs[key] = self.base_ring()(2)
        elif i == 1:
            coeffs[key] = self.base_ring()(3)
        elif i == 2:
            coeffs[key] = self.base_ring()(1)
    
    return self._from_dict(coeffs)

def some_elements(self):
    """
    Return several elements for testing.
    
    Used by TestSuite.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['x', 'y'])
        sage: elts = M.some_elements()
        sage: len(elts) >= 3
        True
        sage: M.zero() in elts
        True
    """
    elements = [self.zero()]
    
    if self._basis_keys:
        # Add basis elements
        elements.extend(self.gens()[:min(3, len(self._basis_keys))])
        
        # Add an_element
        elements.append(self.an_element())
        
        # Add some combinations
        if len(self._basis_keys) >= 2:
            g = list(self.gens())
            elements.append(g[0] + g[1])
            elements.append(g[0] - g[1])
    
    return elements
```

## Module Operations

```python
def direct_sum(self, *others):
    """Direct sum M ⊕ N (biproduct in abelian category)."""
    pass

def tensor_product(self, *others):
    """Tensor product M ⊗ N."""
    pass

def cartesian_product(self, *others):
    """Cartesian product M × N."""
    pass

def dual(self):
    """Dual module Hom(M, R)."""
    pass
```

## Coordinate Conversion

```python
def _from_dict(self, coeffs):
    """
    Internal: Create element from coefficient dictionary.
    
    INPUT:
    - coeffs -- dictionary mapping basis keys to coefficients
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
        sage: # Internal method:
        sage: M._from_dict({'a': 2, 'c': -1})
        2*a - c
    """
    from sage.modules.rmodule_element import RModuleElement
    return RModuleElement(self, coeffs)

def _from_vector(self, vec):
    """
    Internal: Create element from coordinate vector.
    
    This is an internal method - users should use M([...]) syntax.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b'])
        sage: from sage.modules.free_module import vector
        sage: # Internal use only:
        sage: M._from_vector(vector(ZZ, [3, -1]))
        3*a - b
    """
    if self._basis_keys is None:
        raise NotImplementedError("Cannot convert vector without basis")
    
    # Convert to coefficient dictionary
    coeffs = {}
    for i, coeff in enumerate(vec):
        if i >= len(self._basis_keys):
            break
        if coeff != 0:
            coeffs[self._basis_keys[i]] = coeff
    
    return self._from_dict(coeffs)

def _to_vector(self, element):
    """
    Internal: Convert element to coordinate vector.
    
    This is an internal method - users should use element.to_vector().
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['x', 'y'])
        sage: x, y = M.gens()
        sage: v = 2*x - 3*y
        sage: # Internal use only:
        sage: M._to_vector(v)
        (2, -3)
    """
    if self._basis_keys is None:
        raise NotImplementedError("Cannot convert to vector without basis")
    
    # Extract coordinates in basis order
    from sage.modules.free_module import FreeModule
    V = FreeModule(self.base_ring(), len(self._basis_keys))
    coords = []
    
    for key in self._basis_keys:
        coeff = element.coefficient(key) if hasattr(element, 'coefficient') else 0
        coords.append(coeff)
    
    return V(coords)

def coordinate_module(self):
    """
    Return the coordinate module (isomorphic FreeModule).
    
    This is the "numerical" version of this module - a standard
    FreeModule over the base ring with the same rank.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['a', 'b'])
        sage: F = M.coordinate_module()
        sage: F
        Vector space of dimension 2 over Rational Field
        sage: F.rank() == M.rank()
        True
        
        sage: # Can convert back and forth
        sage: a, b = M.gens()
        sage: v = 2*a - 3*b
        sage: coords = M._to_vector(v)
        sage: coords
        (2, -3)
        sage: coords in F
        True
        sage: M._from_vector(coords) == v
        True
    """
    if self._basis_keys is None:
        raise NotImplementedError("Coordinate module not defined without basis")
    
    from sage.modules.free_module import FreeModule
    return FreeModule(self.base_ring(), len(self._basis_keys))

def gens(self):
    """
    Return the generators (basis elements) of this module.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['e', 'f', 'g'])
        sage: M.gens()
        (e, f, g)
        sage: list(M.gens()) == list(M.basis())
        True
    """
    if self._basis_keys is None:
        return ()
    
    return tuple(self.monomial(key) for key in self._basis_keys)

def ngens(self):
    """
    Return the number of generators.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(QQ, basis=['x', 'y', 'z'])
        sage: M.ngens()
        3
        sage: M.ngens() == M.rank()
        True
    """
    return len(self._basis_keys) if self._basis_keys is not None else 0

def gen(self, i):
    """
    Return the i-th generator.
    
    EXAMPLES::
    
        sage: M = RModule_with_basis(ZZ, basis=['a', 'b', 'c'])
        sage: M.gen(0)
        a
        sage: M.gen(1)  
        b
        sage: M.gen(2)
        c
    """
    if self._basis_keys is None or i >= len(self._basis_keys):
        raise IndexError(f"Generator index {i} out of range")
    
    return self.monomial(self._basis_keys[i])
```

## Natural Operations (Split Grothendieck Ring)

```python
def __add__(self, other):
    """M + N syntax for direct sum M ⊕ N."""
    return self.direct_sum(other)

def __mul__(self, other):
    """M * N syntax for cartesian product M × N."""
    return self.cartesian_product(other)

def __matmul__(self, other):
    """M @ N syntax for tensor product M ⊗ N."""
    return self.tensor_product(other)

def __truediv__(self, submodule):
    """M / N syntax for quotient M/N."""
    return self.quotient(submodule)
```