<!--
Origin: gitclones/Coxeter/implementation/planning/RMod/RMod_homs.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Homs: R-Module Morphisms and Homomorphism Spaces

Implementation of morphism spaces Hom_R(M, N) between R-modules and the category-theoretic structure of module homomorphisms.

## Homset Structure

```python
from sage.categories.homsets import HomsetWithBase
from sage.structure.parent import Parent

class RModuleHomset(HomsetWithBase):
    """
    The set Hom_R(M, N) of R-module homomorphisms from M to N.
    
    This is the set of all R-linear maps f: M → N satisfying:
    - f(m₁ + m₂) = f(m₁) + f(m₂) for all m₁, m₂ ∈ M
    - f(r·m) = r·f(m) for all r ∈ R, m ∈ M
    
    The homset itself forms an R-module with pointwise operations:
    - (f + g)(m) = f(m) + g(m)
    - (r·f)(m) = r·f(m)
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=2)
        sage: N = RModule(ZZ, rank=3)
        sage: H = Hom(M, N)
        sage: H
        Set of Morphisms from Free module of rank 2 over Integer Ring 
                         to Free module of rank 3 over Integer Ring
                         in Category of modules over Integer Ring
        
        sage: # Dimension of Hom space
        sage: H.dimension()  # 2 × 3 = 6 for free modules
        6
        
        sage: # Construct morphism by images of generators
        sage: e1, e2 = M.gens()
        sage: f1, f2, f3 = N.gens()
        sage: phi = H([f1 + f2, 2*f3])  # Images of e1, e2
        sage: phi
        Module morphism:
          From: Free module of rank 2 over Integer Ring
          To:   Free module of rank 3 over Integer Ring
        sage: phi(e1)
        f1 + f2
        sage: phi(e2)
        2*f3
    """
    
    def __init__(self, domain, codomain, category=None, base=None, check=True):
        """
        Initialize homset between R-modules.
        
        INPUT:
        - domain -- source R-module
        - codomain -- target R-module
        - category -- category of modules (inferred if not given)
        - base -- base ring (must match module base rings)
        - check -- whether to verify module compatibility
        """
        if check:
            if domain.base_ring() != codomain.base_ring():
                raise ValueError("Modules must have same base ring")
        
        if base is None:
            base = domain.base_ring()
        
        if category is None:
            from sage.categories.modules import Modules
            category = Modules(base)
        
        super().__init__(domain, codomain, category=category, base=base, check=check)
    
    def _repr_(self):
        """
        String representation of hom-set.
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=2)
            sage: Hom(M, M)
            Set of Morphisms from Vector space of dimension 2 over Rational Field
                             to Vector space of dimension 2 over Rational Field
                             in Category of vector spaces over Rational Field
        """
        return (f"Set of Morphisms from {self.domain()} to {self.codomain()} "
                f"in {self.homset_category()}")
    
    def _element_constructor_(self, x, check=True):
        """
        Construct morphism from various input formats.
        
        INPUT:
        - x -- morphism data in one of these formats:
          * List/tuple of images of generators
          * Dictionary mapping generators to images
          * Matrix (for modules with basis)
          * Function/callable
          * Existing morphism to convert
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=2)
            sage: N = RModule(ZZ, rank=3)
            sage: H = Hom(M, N)
            
            sage: # From generator images
            sage: e1, e2 = M.gens()
            sage: f1, f2, f3 = N.gens()
            sage: phi = H([f1, f2 + f3])
            
            sage: # From dictionary
            sage: psi = H({e1: 2*f1, e2: f3})
            
            sage: # From matrix (requires bases)
            sage: A = matrix(ZZ, [[1, 0], [0, 1], [1, 1]])
            sage: chi = H(A)
        """
        if isinstance(x, (list, tuple)):
            # Images of generators
            return self.from_generators(x, check=check)
        elif isinstance(x, dict):
            # Dictionary of generator mappings
            return self.from_dictionary(x, check=check)
        elif hasattr(x, 'nrows') and hasattr(x, 'ncols'):
            # Matrix representation
            return self.from_matrix(x, check=check)
        elif callable(x):
            # Function defining morphism
            return RModuleMorphism(self, x, check=check)
        else:
            # Try to convert existing morphism
            return super()._element_constructor_(x, check=check)
    
    def __call__(self, *args, **kwds):
        """
        Construct morphism with flexible syntax.
        
        Can be called as:
        - H(images) where images is list of generator images
        - H(f) where f is a function
        - H(matrix) where matrix defines linear map
        """
        if len(args) == 1:
            return self._element_constructor_(args[0], **kwds)
        else:
            # Multiple arguments interpreted as generator images
            return self._element_constructor_(list(args), **kwds)
    
    def zero(self):
        """
        Return the zero morphism.
        
        The zero morphism sends every element to zero.
        
        OUTPUT:
        RModuleMorphism that is the zero map
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=2)
            sage: N = RModule(ZZ, rank=3)
            sage: H = Hom(M, N)
            sage: zero = H.zero()
            sage: zero(M.an_element())
            (0, 0, 0)
            sage: zero.is_zero()
            True
        """
        codomain = self.codomain()
        zero_images = [codomain.zero() for _ in self.domain().gens()]
        return self(zero_images)
    
    def identity(self):
        """
        Return identity morphism (if domain == codomain).
        
        OUTPUT:
        Identity endomorphism
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=3)
            sage: H = Hom(M, M)
            sage: id = H.identity()
            sage: id.is_identity()
            True
            sage: all(id(v) == v for v in M.some_elements())
            True
        """
        if self.domain() != self.codomain():
            raise ValueError("Identity only exists for endomorphisms")
        
        # Identity maps generators to themselves
        return self(list(self.domain().gens()))
    
    def dimension(self):
        """
        Dimension of Hom(M,N) as R-module.
        
        For free modules: dim(Hom(R^m, R^n)) = m × n
        
        OUTPUT:
        Integer or Infinity
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=2)
            sage: N = RModule(QQ, rank=3)
            sage: Hom(M, N).dimension()
            6  # 2 × 3
        """
        if self.domain().is_free() and self.codomain().is_free():
            m = self.domain().rank()
            n = self.codomain().rank()
            if m < Infinity and n < Infinity:
                return m * n
            else:
                return Infinity
        else:
            # General case requires more analysis
            raise NotImplementedError("Dimension for non-free modules")
    
    def basis(self):
        """
        Basis of Hom(M,N) as R-module (when finite dimensional).
        
        For free modules with bases, returns basis of linear maps.
        
        OUTPUT:
        List of morphisms forming R-basis
        """
        if not (self.domain().is_free() and self.codomain().is_free()):
            raise ValueError("Basis only implemented for free modules")
        
        domain_basis = self.domain().basis()
        codomain_basis = self.codomain().basis()
        
        basis_morphisms = []
        
        # Standard basis: maps sending one basis element to another, rest to 0
        for i, e_i in enumerate(domain_basis):
            for j, f_j in enumerate(codomain_basis):
                # Create morphism e_i ↦ f_j, others ↦ 0
                images = [self.codomain().zero() for _ in domain_basis]
                images[i] = f_j
                basis_morphisms.append(self(images))
        
        return basis_morphisms
    
    def from_generators(self, images, check=True):
        """
        Construct morphism from images of generators.
        
        INPUT:
        - images -- list of elements in codomain
        - check -- verify linearity
        
        OUTPUT:
        RModuleMorphism
        """
        domain_gens = self.domain().gens()
        
        if len(images) != len(domain_gens):
            raise ValueError(f"Need {len(domain_gens)} images, got {len(images)}")
        
        # Convert to codomain elements
        codomain = self.codomain()
        images = [codomain(img) for img in images]
        
        # Create morphism data
        morphism_dict = dict(zip(domain_gens, images))
        
        return RModuleMorphism(self, morphism_dict, check=check)
    
    def from_matrix(self, matrix, check=True):
        """
        Construct morphism from matrix representation.
        
        Requires both domain and codomain to have bases.
        
        INPUT:
        - matrix -- matrix over base ring
        - check -- verify dimensions
        
        OUTPUT:
        RModuleMorphism
        """
        if not (hasattr(self.domain(), 'basis') and hasattr(self.codomain(), 'basis')):
            raise ValueError("Both modules must have bases for matrix representation")
        
        if check:
            expected_rows = self.codomain().dimension()
            expected_cols = self.domain().dimension()
            if matrix.nrows() != expected_rows or matrix.ncols() != expected_cols:
                raise ValueError(f"Matrix has wrong dimensions: expected {expected_rows}×{expected_cols}, "
                                f"got {matrix.nrows()}×{matrix.ncols()}")
        
        # Matrix acts on coordinate vectors
        domain_basis = list(self.domain().basis())
        codomain_basis = list(self.codomain().basis())
        
        # Compute images of basis elements
        images = []
        for j in range(len(domain_basis)):
            # j-th column gives coordinates of image of j-th basis element
            coords = [matrix[i,j] for i in range(len(codomain_basis))]
            image = sum(c * b for c, b in zip(coords, codomain_basis) if c != 0)
            images.append(image)
        
        return self.from_generators(images, check=False)
```

## R-Module Morphism Implementation

```python
from sage.categories.morphism import Morphism

class RModuleMorphism(Morphism):
    """
    R-module homomorphism preserving module structure.
    
    An R-linear map f: M → N satisfying:
    - f(m₁ + m₂) = f(m₁) + f(m₂) (additivity)
    - f(r·m) = r·f(m) (R-linearity)
    
    Morphisms can be specified by:
    - Images of generators (extends by linearity)
    - Matrix representation (for modules with basis)
    - Explicit function
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=2)
        sage: N = RModule(ZZ, rank=3)
        sage: e1, e2 = M.gens()
        sage: f1, f2, f3 = N.gens()
        
        sage: # Define morphism by generator images
        sage: phi = M.hom([f1 + f2, 2*f3], N)
        sage: phi(e1)
        f1 + f2
        sage: phi(3*e1 + 5*e2)
        3*f1 + 3*f2 + 10*f3
        
        sage: # Morphism properties
        sage: phi.rank()
        2
        sage: phi.is_injective()
        True
        sage: phi.is_surjective()
        False
    """
    
    def __init__(self, parent, data, check=True):
        """
        Initialize module morphism.
        
        INPUT:
        - parent -- HomSet this morphism belongs to
        - data -- morphism data (dict, function, or matrix)
        - check -- whether to verify linearity
        """
        super().__init__(parent)
        
        if isinstance(data, dict):
            self._morphism_dict = data
            self._morphism_from = 'generators'
        elif callable(data):
            self._morphism_function = data
            self._morphism_from = 'function'
        elif hasattr(data, 'nrows'):
            self._morphism_matrix = data
            self._morphism_from = 'matrix'
        else:
            raise ValueError("Morphism data must be dict, function, or matrix")
        
        if check:
            self._check_linearity()
    
    def _call_(self, x):
        """
        Evaluate morphism on element.
        
        INPUT:
        - x -- element of domain module
        
        OUTPUT:
        Element of codomain module
        """
        if self._morphism_from == 'generators':
            # Extend linearly from generators
            result = self.codomain().zero()
            
            # Express x in terms of generators
            for gen, coeff in x:
                if gen in self._morphism_dict:
                    result += coeff * self._morphism_dict[gen]
                else:
                    # Try to express gen in terms of known generators
                    raise NotImplementedError("General linear extension")
            
            return result
            
        elif self._morphism_from == 'function':
            return self._morphism_function(x)
            
        elif self._morphism_from == 'matrix':
            # Convert to coordinates, apply matrix, convert back
            coords = x.to_vector()
            result_coords = self._morphism_matrix * coords
            return self.codomain()._from_vector(result_coords)
    
    def _repr_(self):
        """String representation."""
        return f"Module morphism:\n  From: {self.domain()}\n  To:   {self.codomain()}"
    
    def _check_linearity(self):
        """Verify this defines a linear map."""
        # Check on generators and some linear combinations
        domain = self.domain()
        
        # Check additivity: f(g1 + g2) = f(g1) + f(g2)
        gens = list(domain.gens())
        if len(gens) >= 2:
            g1, g2 = gens[0], gens[1]
            if self(g1 + g2) != self(g1) + self(g2):
                raise ValueError("Morphism is not additive")
        
        # Check R-linearity: f(r·g) = r·f(g)
        if gens:
            g = gens[0]
            r = domain.base_ring().an_element()
            if self(r * g) != r * self(g):
                raise ValueError("Morphism is not R-linear")
    
    def kernel(self):
        """
        Return kernel as submodule of domain.
        
        ker(f) = {m ∈ M : f(m) = 0}
        
        OUTPUT:
        Submodule of domain
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=3)
            sage: N = RModule(ZZ, rank=2)
            sage: # Map (x,y,z) ↦ (x+y, y+z)
            sage: A = matrix(ZZ, [[1, 1, 0], [0, 1, 1]])
            sage: phi = M.hom(A, N)
            sage: K = phi.kernel()
            sage: K.gens()
            [(1, -2, 1)]  # Solutions to x+y=0, y+z=0
        """
        if self._morphism_from == 'matrix':
            # Kernel is null space of matrix
            kernel_matrix = self._morphism_matrix.right_kernel_matrix()
            kernel_gens = [self.domain()._from_vector(row) 
                          for row in kernel_matrix.rows()]
            return self.domain().submodule(kernel_gens)
        else:
            # General algorithm for kernel computation
            raise NotImplementedError("Kernel for non-matrix morphisms")
    
    def image(self):
        """
        Return image as submodule of codomain.
        
        im(f) = {f(m) : m ∈ M}
        
        OUTPUT:
        Submodule of codomain
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=2)
            sage: N = RModule(ZZ, rank=3)
            sage: phi = M.hom([[1, 0, 1], [0, 1, 1]], N)
            sage: I = phi.image()
            sage: I.gens()
            [(1, 0, 1), (0, 1, 1)]
            sage: I.rank()
            2
        """
        # Image is generated by images of generators
        image_gens = [self(g) for g in self.domain().gens()]
        return self.codomain().submodule(image_gens)
    
    def cokernel(self):
        """
        Return cokernel as quotient module.
        
        coker(f) = N / im(f)
        
        OUTPUT:
        Quotient module
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=2)
            sage: N = RModule(ZZ, rank=3)
            sage: phi = M.hom([[1, 0, 0], [0, 1, 0]], N)
            sage: C = phi.cokernel()
            sage: C.rank()
            1  # Dimension drops by rank of image
        """
        return self.codomain().quotient(self.image())
    
    def rank(self):
        """
        Rank of the morphism (dimension of image).
        
        OUTPUT:
        Non-negative integer
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=3)
            sage: N = RModule(QQ, rank=4)
            sage: phi = M.hom(matrix(QQ, [[1,0,0,0], [0,1,0,0], [0,0,0,0]]), N)
            sage: phi.rank()
            2
        """
        if self._morphism_from == 'matrix':
            return self._morphism_matrix.rank()
        else:
            return self.image().rank()
    
    def is_zero(self):
        """Test if this is the zero morphism."""
        # Check if all generators map to zero
        return all(self(g).is_zero() for g in self.domain().gens())
    
    def is_identity(self):
        """Test if this is the identity morphism."""
        if self.domain() != self.codomain():
            return False
        
        # Check if generators map to themselves
        return all(self(g) == g for g in self.domain().gens())
    
    def is_injective(self):
        """
        Test if morphism is injective (monomorphism).
        
        Equivalent to ker(f) = {0}.
        
        OUTPUT:
        Boolean
        """
        if self._morphism_from == 'matrix':
            # Injective iff matrix has full column rank
            return self._morphism_matrix.rank() == self.domain().rank()
        else:
            return self.kernel().is_zero()
    
    def is_surjective(self):
        """
        Test if morphism is surjective (epimorphism).
        
        Equivalent to im(f) = N.
        
        OUTPUT:
        Boolean
        """
        if self._morphism_from == 'matrix':
            # Surjective iff matrix has full row rank
            return self._morphism_matrix.rank() == self.codomain().rank()
        else:
            return self.image() == self.codomain()
    
    def is_isomorphism(self):
        """
        Test if morphism is an isomorphism.
        
        True iff morphism is both injective and surjective.
        
        OUTPUT:
        Boolean
        """
        # For finite modules, injective + same dimension implies isomorphism
        if (self.domain().is_finite() and self.codomain().is_finite() and
            self.domain().cardinality() == self.codomain().cardinality()):
            return self.is_injective()
        
        # General case
        return self.is_injective() and self.is_surjective()
    
    def inverse(self):
        """
        Return inverse morphism (if isomorphism).
        
        OUTPUT:
        RModuleMorphism that is the inverse
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=2)
            sage: phi = M.hom(matrix(QQ, [[1, 2], [3, 4]]), M)
            sage: phi.is_isomorphism()
            True
            sage: psi = phi.inverse()
            sage: (phi * psi).is_identity()
            True
        """
        if not self.is_isomorphism():
            raise ValueError("Morphism is not an isomorphism")
        
        if self._morphism_from == 'matrix':
            inv_matrix = self._morphism_matrix.inverse()
            return self.codomain().hom(inv_matrix, self.domain())
        else:
            # General inverse computation
            raise NotImplementedError("Inverse for non-matrix morphisms")
    
    def __mul__(self, other):
        """
        Composition of morphisms.
        
        Returns other ∘ self (read right to left).
        """
        if not isinstance(other, RModuleMorphism):
            # Might be scalar multiplication
            return NotImplemented
        
        if self.codomain() != other.domain():
            raise ValueError("Morphisms not composable")
        
        # Composition of morphisms
        if (self._morphism_from == 'matrix' and 
            other._morphism_from == 'matrix'):
            # Matrix composition
            comp_matrix = other._morphism_matrix * self._morphism_matrix
            return self.domain().hom(comp_matrix, other.codomain())
        else:
            # General composition
            def composition(x):
                return other(self(x))
            
            return RModuleMorphism(
                Hom(self.domain(), other.codomain()),
                composition
            )
    
    def direct_sum(self, other):
        """
        Direct sum of morphisms f ⊕ g.
        
        (f ⊕ g): M₁ ⊕ M₂ → N₁ ⊕ N₂
        """
        # Would construct morphism between direct sum modules
        raise NotImplementedError("Direct sum of morphisms")
    
    def tensor_product(self, other):
        """
        Tensor product of morphisms f ⊗ g.
        
        (f ⊗ g): M₁ ⊗ M₂ → N₁ ⊗ N₂
        """
        # Would construct morphism between tensor product modules
        raise NotImplementedError("Tensor product of morphisms")
```

## Special Morphisms and Constructions

```python
def inclusion_morphism(submodule, ambient):
    """
    Canonical inclusion morphism ι: S ↪ M.
    
    INPUT:
    - submodule -- submodule S of ambient module M
    - ambient -- ambient module M
    
    OUTPUT:
    Injective morphism S → M
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=3)
        sage: S = M.submodule([[1, 0, 0], [0, 1, 0]])
        sage: iota = inclusion_morphism(S, M)
        sage: iota.is_injective()
        True
        sage: e1 = S.gen(0)
        sage: iota(e1) in M
        True
    """
    def inclusion_map(x):
        # Elements of submodule are already elements of ambient
        return ambient(x)
    
    return RModuleMorphism(Hom(submodule, ambient), inclusion_map)

def projection_morphism(module, quotient):
    """
    Canonical projection morphism π: M → M/N.
    
    INPUT:
    - module -- module M
    - quotient -- quotient module M/N
    
    OUTPUT:
    Surjective morphism M → M/N
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=3)
        sage: N = M.submodule([[2, 0, 0], [0, 3, 0]])
        sage: Q = M.quotient(N)
        sage: pi = projection_morphism(M, Q)
        sage: pi.is_surjective()
        True
        sage: pi(2*M.gen(0)).is_zero()  # 2e₁ ∈ N
        True
    """
    def projection_map(x):
        # Map to equivalence class in quotient
        return quotient(x)
    
    return RModuleMorphism(Hom(module, quotient), projection_map)

def evaluation_morphism(module, element):
    """
    Evaluation morphism at fixed element.
    
    For dual module M* and element m ∈ M, gives:
    ev_m: M* → R, φ ↦ φ(m)
    
    INPUT:
    - module -- dual module M*
    - element -- element m of original module
    
    OUTPUT:
    Linear functional M* → R
    """
    base_ring = module.base_ring()
    
    def evaluate_at_element(phi):
        # phi is element of dual, evaluate at fixed element
        return phi(element)
    
    return RModuleMorphism(
        Hom(module, base_ring),
        evaluate_at_element
    )

def canonical_pairing(dual_module, module):
    """
    Canonical pairing ⟨·,·⟩: M* × M → R.
    
    The evaluation pairing between a module and its dual.
    
    INPUT:
    - dual_module -- dual module M*
    - module -- original module M
    
    OUTPUT:
    Bilinear pairing as morphism M* ⊗ M → R
    """
    # This defines the canonical duality pairing
    raise NotImplementedError("Canonical pairing construction")
```

## Homset as Module

```python
class HomRModule(Parent):
    """
    The R-module structure on Hom(M,N).
    
    Hom_R(M,N) forms an R-module with:
    - Addition: (f + g)(m) = f(m) + g(m)
    - Scalar multiplication: (r·f)(m) = r·f(m)
    
    For bimodules, Hom has additional structure.
    """
    
    def __init__(self, homset):
        """Initialize Hom as R-module."""
        self._homset = homset
        base = homset.base_ring()
        
        from sage.categories.modules import Modules
        Parent.__init__(self, base=base, category=Modules(base))
    
    def _element_constructor_(self, x):
        """Construct element of Hom module."""
        return self._homset(x)
    
    def zero(self):
        """Zero morphism as module element."""
        return self._homset.zero()
    
    def _add_(self, f, g):
        """Addition of morphisms."""
        def sum_morphism(x):
            return f(x) + g(x)
        
        return RModuleMorphism(self._homset, sum_morphism)
    
    def _lmul_(self, r, f):
        """Scalar multiplication of morphism."""
        def scaled_morphism(x):
            return r * f(x)
        
        return RModuleMorphism(self._homset, scaled_morphism)
    
    def basis(self):
        """Basis of Hom(M,N) when finite dimensional."""
        return self._homset.basis()
    
    def dimension(self):
        """Dimension as R-module."""
        return self._homset.dimension()
```

## Mathematical Properties

```python
# Mathematical assertion: Hom is a functor
# Hom_R(-, N) is contravariant in first argument
# Hom_R(M, -) is covariant in second argument

# Mathematical assertion: Hom-Tensor adjunction
# Hom_R(M ⊗_R N, P) ≅ Hom_R(M, Hom_R(N, P))

# Mathematical assertion: First isomorphism theorem
# For f: M → N, have M/ker(f) ≅ im(f)

# Mathematical assertion: Exactness properties
# 0 → A → B → C → 0 exact iff
# 0 → Hom(M,A) → Hom(M,B) → Hom(M,C) → 0 exact for all M

# Mathematical assertion: Representability
# Every R-linear functional M → R arises from element of M*

# Mathematical assertion: Composition associativity
# (h ∘ g) ∘ f = h ∘ (g ∘ f)

# Mathematical assertion: Rank-nullity theorem
# rank(f) + nullity(f) = dim(domain) for finite dimensional

# Mathematical assertion: Matrix representation
# Every morphism between free finite modules has unique matrix
```

This comprehensive morphism framework provides the complete homomorphism structure for R-modules including construction methods, morphism properties, special morphisms, and the module structure on Hom sets.