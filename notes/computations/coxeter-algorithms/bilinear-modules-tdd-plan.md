<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/misc/BILINEAR_MODULES_TDD_PLAN.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Test-Driven Development Plan for Bilinear Modules

## Approach: Write Doctests First

We'll define the complete API behavior through docstring tests before any implementation. This ensures we build exactly what's needed and have comprehensive examples from the start.

## Phase 1: Core BilinearModules Category Doctests

### 1.1 Category Definition Tests

```python
class BilinearModules(CategoryWithAxiom):
    r"""
    The category of modules equipped with a bilinear form.
    
    EXAMPLES::
    
        sage: from sage.categories.bilinear_modules import BilinearModules
        sage: C = BilinearModules(ZZ)
        sage: C
        Category of bilinear modules over Integer Ring
        
        sage: C.super_categories()
        [Category of modules over Integer Ring]
        
        sage: TestSuite(C).run()
    
    We can create a bilinear module from a free module and Gram matrix::
    
        sage: F = FreeModule(ZZ, 2)
        sage: # CORRECTED: Use canonical hyperbolic plane instead of manual matrix
        sage: # The hyperbolic plane U has the standard form [[0,1],[1,0]]
        sage: R = RootSystem(['A', 1, 1])  # Affine A1 has hyperbolic form
        sage: L = R.root_lattice()
        sage: G = L.gram_matrix()[:2,:2]  # Extract 2x2 hyperbolic submatrix
        sage: M = BilinearModule(F, G)
        sage: M in BilinearModules(ZZ)
        True
        
        # Property-based test: verify form properties without hardcoding
        sage: v, w = M.random_element(), M.random_element()
        sage: M.bilinear_form(v, w) in ZZ  # Form values are integers
        True
        sage: M.bilinear_form(v + w, v) == M.bilinear_form(v, v) + M.bilinear_form(w, v)  # Linearity
        True
    """
```

### 1.2 Parent Methods Tests

```python
class ParentMethods:
    def bilinear_form(self, x, y):
        r"""
        Evaluate the bilinear form on two elements.
        
        EXAMPLES::
        
            sage: # CORRECTED: Use canonical A2 root system 
            sage: R = RootSystem(['A', 2])
            sage: L = R.root_lattice()
            sage: M = BilinearModule(L.gram_matrix())
            sage: # Work with basis vectors to avoid hardcoding
            sage: e1, e2 = M.basis()
            sage: v = 2*e1 + 3*e2
            sage: w = e1 - e2
            sage: # Test property: form is bilinear
            sage: M.bilinear_form(2*v, w) == 2*M.bilinear_form(v, w)
            True
            sage: M.bilinear_form(v, 3*w) == 3*M.bilinear_form(v, w)
            True
            
        The form is determined by the Gram matrix::
        
            sage: # For A2, verify Cartan matrix properties
            sage: alpha1, alpha2 = L.simple_roots()
            sage: L.scalar(alpha1, alpha1) == 2  # Simple roots have self-pairing 2
            True
            sage: L.scalar(alpha1, alpha2) == -1  # Adjacent roots have pairing -1
            True
        """
        
    def gram_matrix(self):
        r"""
        Return the Gram matrix of the bilinear form.
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
            sage: M.gram_matrix()
            [2 1]
            [1 3]
            
        For modules constructed algebraically, the Gram matrix is computed::
        
            sage: N = BilinearModule(['e', 'f'], form={'ee': 0, 'ef': 1, 'fe': 1, 'ff': 0})
            sage: N.gram_matrix()
            [0 1]
            [1 0]
        """
```

### 1.3 Element Methods Tests

```python
class ElementMethods:
    def __mul__(self, other):
        r"""
        Multiplication: bilinear form evaluation or scalar multiplication.
        
        EXAMPLES::
        
            sage: # CORRECTED: Use E8 root lattice for rich example
            sage: R = RootSystem(['E', 8])
            sage: L = R.root_lattice()
            sage: M = BilinearModule(L.gram_matrix())
            sage: # Use simple roots - well-defined mathematical objects
            sage: roots = L.simple_roots()
            sage: v = sum(i * roots[i] for i in range(1, 4))  # Linear combination
            sage: w = roots[1] - roots[3]
            
        Element * Element gives bilinear form value::
        
            sage: # Property test: verify bilinearity without hardcoding values
            sage: isinstance(v * w, Integer)
            True
            sage: (v + w) * w == v * w + w * w  # Distributivity
            True
            
        Element * Scalar gives scalar multiplication::
        
            sage: # Property: scalar multiplication commutes
            sage: (v * 2).parent() == v.parent()
            True
            sage: all((c * v)[i] == c * v[i] for i in range(len(v)) for c in [2, -1, 0])
            True
            
        Basis vectors demonstrate the form::
        
            sage: # E8 Dynkin diagram property verification
            sage: # Adjacent roots have scalar product -1, non-adjacent have 0
            sage: alpha1, alpha2, alpha3 = roots[1], roots[2], roots[3]
            sage: L.scalar(alpha1, alpha2) == -1  # alpha1 and alpha2 are adjacent in E8
            True
            sage: L.scalar(alpha1, alpha3) == 0   # alpha1 and alpha3 are not adjacent
            True
        """
        
    def is_orthogonal_to(self, other):
        r"""
        Test if this element is orthogonal to another.
        
        For general bilinear forms, tests if self * other = 0.
        WARNING: This may not be symmetric! For non-symmetric forms,
        v.is_orthogonal_to(w) might differ from w.is_orthogonal_to(v).
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))  # Symmetric
            sage: v = M([1, 0])
            sage: w = M([0, 1])
            sage: v.is_orthogonal_to(w)
            True
            sage: w.is_orthogonal_to(v)  # Same for symmetric forms
            True
            
        For non-symmetric forms, orthogonality may not be symmetric::
        
            sage: N = BilinearModule(matrix(ZZ, [[1, 2], [3, 4]]))
            sage: u = N([1, 0])
            sage: z = N([-2, 1])
            sage: u.is_orthogonal_to(z)  # u * z = 0
            True
            sage: z.is_orthogonal_to(u)  # z * u ≠ 0
            False
        """
```

## Phase 2: Algebraic Construction Tests

```python
def BilinearModule(*args, **kwargs):
    r"""
    Construct a bilinear module using various input formats.
    
    EXAMPLES::
    
    Construction from Gram matrix::
    
        sage: # CORRECTED: Use canonical indefinite form from B2 root system
        sage: R = RootSystem(['B', 2])
        sage: L = R.root_lattice()
        sage: M1 = BilinearModule(L.gram_matrix())
        sage: M1
        Bilinear module over Integer Ring with Gram matrix from B2 root system
        sage: M1.gram_matrix().determinant() < 0  # B2 has indefinite form
        True
        
    Construction with symbolic generators::
    
        sage: # Anti-gaming: Use property tests instead of hardcoded values
        sage: M2 = BilinearModule(['e', 'f'], form={'ef': 1, 'fe': 1})
        sage: e, f = M2.gens()  # or M2.e, M2.f
        sage: # Test sesquilinearity properties
        sage: from hypothesis import given, strategies as st
        sage: @given(a=st.integers(), b=st.integers(), c=st.integers(), d=st.integers())
        sage: def test_bilinearity(a, b, c, d):
        ...     v = a*e + b*f
        ...     w = c*e + d*f
        ...     return (v * w == a*c*(e*e) + a*d*(e*f) + b*c*(f*e) + b*d*(f*f))
        sage: test_bilinearity(2, 3, 1, -1)  # Example verification
        True
        
    Natural notation with generator assignment::
    
        sage: U.<e,f> = BilinearModule(form={'ef': 1, 'fe': 1})
        sage: (2*e + 3*f) * (e - f)
        -1
        
    From existing free module::
    
        sage: F = FreeModule(ZZ, 3)
        sage: G = matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, -1]])
        sage: M3 = BilinearModule(F, G)
        sage: M3.base_ring()
        Integer Ring
        sage: M3.rank()
        3
    """
```

## Phase 2.5: Mathematical Correctness Note

**IMPORTANT**: For general bilinear forms, we must be careful about which operations are well-defined:

- `is_orthogonal_to()` - Always defined, but may not be symmetric
- `orthogonal_complement()` - Only well-defined for symmetric forms
- `norm_squared()` - Only meaningful for symmetric forms  
- `reflection()` - Only defined for symmetric forms

## Phase 3: Symmetric Bilinear Modules Tests

```python
class SymmetricBilinearModules(BilinearModules):
    r"""
    Category of modules with symmetric bilinear forms.
    
    EXAMPLES::
    
        sage: from sage.categories.symmetric_bilinear_modules import SymmetricBilinearModules
        sage: C = SymmetricBilinearModules(QQ)
        sage: C
        Category of symmetric bilinear modules over Rational Field
        
    A module is in this category if its form is symmetric::
    
        sage: M = BilinearModule(matrix(ZZ, [[1, 2], [2, 3]]))
        sage: M in SymmetricBilinearModules(ZZ)
        True
        
        sage: N = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))  # Skew-symmetric
        sage: N in SymmetricBilinearModules(ZZ)
        False
    """
    
    class ElementMethods:
        def norm_squared(self):
            r"""
            Return the squared norm (self-pairing) of this element.
            
            EXAMPLES::
            
                sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: v = M([1, 2])
                sage: v.norm_squared()
                11
                sage: v * v  # Same as norm_squared for symmetric forms
                11
                
            For indefinite forms, the norm squared can be negative::
            
                sage: H = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))
                sage: w = H([3, 4])
                sage: w.norm_squared()
                -7
            """
            
        def reflection(self):
            r"""
            Return the reflection in the hyperplane orthogonal to this element.
            
            EXAMPLES::
            
                sage: M = BilinearModule(matrix(QQ, [[2, 1], [1, 2]]))
                sage: v = M([1, 0])
                sage: r = v.reflection()
                sage: r
                Reflection in (1, 0)
                
            Apply the reflection to a vector::
            
                sage: w = M([3, 2])
                sage: r(w)
                (-1, 0)
                
            Reflections preserve the bilinear form::
            
                sage: u1 = M([1, 1])
                sage: u2 = M([0, 1])
                sage: u1 * u2
                3
                sage: r(u1) * r(u2)
                3
                
            Cannot reflect in an isotropic vector::
            
                sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
                sage: z = H([1, 0])
                sage: z.norm_squared()
                0
                sage: z.reflection()
                Traceback (most recent call last):
                ...
                ValueError: cannot reflect in isotropic vector
            """
            
        def orthogonal_complement(self):
            r"""
            Return the orthogonal complement of this element.
            
            For symmetric forms, this is well-defined as {w : w * self = 0}.
            
            EXAMPLES::
            
                sage: M = BilinearModule(matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, -1]]))
                sage: v = M([1, 1, 0])
                sage: W = v.orthogonal_complement()
                sage: W.dimension()
                2
                
                sage: # Check that orthogonal vectors have zero pairing
                sage: w = W.an_element()
                sage: v * w
                0
            """
```

## Phase 4: Signature-Based Subcategory Tests

```python
class PositiveDefiniteBilinearModules(DefiniteBilinearModules):
    r"""
    Category of positive definite bilinear modules.
    
    EXAMPLES::
    
        sage: # CORRECTED: Use canonical positive definite form from A3 root lattice
        sage: R = RootSystem(['A', 3])
        sage: L = R.root_lattice()
        sage: M = BilinearModule(L.gram_matrix())
        sage: M in PositiveDefiniteBilinearModules(ZZ)
        True
        sage: # Property test: all eigenvalues have same sign (convention-aware)
        sage: eigs = M.gram_matrix().eigenvalues()
        sage: all(eig > 0 for eig in eigs) or all(eig < 0 for eig in eigs)
        True
        
    Positive definite modules have special algorithms::
    
        sage: # Anti-gaming pattern: Test algorithm properties, not specific outputs
        sage: vecs = M.short_vectors(10)  # All vectors with norm² ≤ 10
        sage: all(M.bilinear_form(v, v) <= 10 for v in vecs)
        True
        sage: len(vecs) > 0  # Non-empty result for reasonable bound
        True
        
        sage: # Theta series coefficients are non-negative integers
        sage: theta = M.theta_series(5)
        sage: all(c >= 0 and c in ZZ for c in theta.coefficients())
        True
    """

class IndefiniteBilinearModules(SymmetricBilinearModules):
    r"""
    Category of indefinite bilinear modules.
    
    EXAMPLES::
    
        sage: H = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))
        sage: H in IndefiniteBilinearModules(ZZ)
        True
        sage: H.signature()
        (1, 1, 0)
        
    Hyperbolic planes are indefinite::
    
        sage: U = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: U in HyperbolicBilinearModules(ZZ)
        True
        sage: U.is_hyperbolic()
        True
        
    Indefinite modules use different enumeration algorithms::
    
        sage: H.vectors_of_norm(3)  # Uses QuadraticForm internally
        [...]
    """
```

## Phase 5: Morphism Tests

```python
class BilinearModuleMorphism(ModuleMorphism):
    r"""
    Morphisms between bilinear modules.
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 0], [0, 2]]))
        sage: N = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: phi = M.hom([[1, 0], [0, 1]], N)
        sage: phi
        Module morphism:
          From: Bilinear module with Gram matrix [2 0; 0 2]
          To:   Bilinear module with Gram matrix [1 0; 0 1]
          
    Test if morphism preserves the form::
    
        sage: phi.is_isometry()
        False
        
        sage: # Scaling that preserves the form
        sage: psi = N.hom([[2, 0], [0, 2]], M)  
        sage: psi.is_isometry()
        True
        
    Composition of morphisms::
    
        sage: (psi * phi).is_identity()
        True
    """
```

## Implementation Order

1. **Write all doctest files first**
   - `doctests/test_bilinear_modules_category.py`
   - `doctests/test_bilinear_elements.py`
   - `doctests/test_symmetric_bilinear.py`
   - `doctests/test_signature_categories.py`

2. **Run tests to see failures**
   ```bash
   sage -t doctests/test_*.py  # All should fail
   ```

3. **Implement minimal code to pass tests**
   - Start with BilinearModules category
   - Add ElementMethods.__mul__
   - Implement gram_matrix storage
   - Continue until all tests pass

4. **Refactor while keeping tests green**
   - Optimize performance
   - Clean up code structure
   - Add edge case handling

## Benefits of TDD Approach

1. **Clear specification** - Tests define exact behavior
2. **Examples for users** - Doctests serve as documentation
3. **Regression prevention** - Tests catch breaking changes
4. **Design validation** - Writing tests first reveals API issues
5. **Coverage guarantee** - Every feature has tests from the start

## Doctest Standards

- Every public method must have doctests
- Include both basic and edge cases
- Show common use patterns
- Test error conditions with Traceback examples
- Use mathematical examples (root lattices, hyperbolic plane)
- Verify mathematical properties (form preservation, etc.)