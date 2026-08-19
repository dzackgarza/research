<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/BilRMod_homs.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Homs: Bilinear Module Morphisms and Homsets

Morphism implementation for bilinear modules preserving bilinear form structure.

## Homset Structure

```python
from sage.categories.homsets import HomsetWithBase

class BilinearModuleHomset(HomsetWithBase):
    """
    Homset of morphisms between bilinear modules.
    
    A morphism f: (M₁, b₁) → (M₂, b₂) between bilinear modules is an
    R-module homomorphism that preserves the bilinear form:
    b₂(f(v), f(w)) = b₁(v, w) for all v, w ∈ M₁.
    
    This is stronger than just being an R-module homomorphism.
    
    Special cases:
    - Isometry: bijective form-preserving map
    - Orthogonal transformation: isometry of same space
    - Symplectic transformation: isometry of skew-symmetric form
    
    EXAMPLES::
    
        sage: G1 = matrix(ZZ, [[2, 1], [1, 3]])
        sage: G2 = matrix(ZZ, [[1, 0], [0, 1]])
        sage: M1 = BilinearModule(G1)
        sage: M2 = BilinearModule(G2)
        sage: H = Hom(M1, M2)
        sage: H
        Set of Morphisms from Bilinear module of rank 2 over Integer Ring 
                             to Bilinear module of rank 2 over Integer Ring 
                             in Category of bilinear modules over Integer Ring
    """
    
    def __init__(self, domain, codomain, category=None, base=None, check=True):
        """
        Initialize homset of bilinear module morphisms.
        
        INPUT:
        - domain -- source bilinear module
        - codomain -- target bilinear module  
        - category -- category of morphisms (default: BilinearModules morphisms)
        """
        if category is None:
            from sage.categories.bilinear_modules import BilinearModules
            category = BilinearModules(domain.base_ring())
        
        HomsetWithBase.__init__(self, domain, codomain, category=category, 
                               base=base, check=check)
    
    def _repr_(self):
        """String representation of the homset."""
        return (f"Set of Morphisms from {self.domain()} to {self.codomain()} "
                f"in Category of bilinear modules over {self.base()}")
    
    def zero(self):
        """Return the zero morphism."""
        return BilinearModuleMorphism(self, lambda v: self.codomain().zero())
    
    def identity(self):
        """
        Return identity morphism (only if domain = codomain).
        
        EXAMPLES::
        
            sage: G = matrix(ZZ, [[2, 1], [1, 3]])
            sage: M = BilinearModule(G)
            sage: H = Hom(M, M)
            sage: id = H.identity()
            sage: e, f = M.gens()
            sage: id(e) == e
            True
        """
        if self.domain() != self.codomain():
            raise ValueError("Identity only defined for endomorphisms")
        
        return BilinearModuleMorphism(self, lambda v: v)
    
    def _element_constructor_(self, f, check=True):
        """
        Construct morphism from function or matrix.
        
        INPUT:
        - f -- function, matrix, or callable defining the morphism
        - check -- whether to verify bilinear form preservation
        """
        if hasattr(f, 'is_matrix') and f.is_matrix():
            return BilinearModuleMorphism(self, matrix=f, check=check)
        else:
            return BilinearModuleMorphism(self, f, check=check)
```

## Morphism Implementation

```python
from sage.categories.morphism import Morphism

class BilinearModuleMorphism(Morphism):
    """
    Morphism between bilinear modules preserving bilinear forms.
    
    A bilinear module morphism f: (M₁, b₁) → (M₂, b₂) satisfies:
    1. f is an R-module homomorphism: f(rv + w) = rf(v) + f(w)
    2. f preserves bilinear forms: b₂(f(v), f(w)) = b₁(v, w)
    
    The second condition is the key difference from ordinary module morphisms.
    
    EXAMPLES::
    
        sage: # Isometry between equivalent forms
        sage: G1 = matrix(QQ, [[2, 1], [1, 3]])
        sage: G2 = matrix(QQ, [[1, 0, 0], [0, 1, 0], [0, 0, 5]])
        sage: M1 = BilinearModule(G1)
        sage: M2 = BilinearModule(G2)
        
        sage: # Define embedding f: M1 → M2
        sage: def f(v):
        ....:     # Map first basis element to (1,0,0), second to (0,1,0)
        ....:     coords = v.to_vector()
        ....:     return M2([coords[0], coords[1], 0])
        sage: phi = BilinearModuleMorphism(Hom(M1, M2), f)
        
        sage: # Verify form preservation (won't work for this example)
        sage: # phi.preserves_bilinear_form()
    """
    
    def __init__(self, homset, f=None, matrix=None, check=True):
        """
        Initialize bilinear module morphism.
        
        INPUT:
        - homset -- homset this morphism belongs to
        - f -- function defining the morphism
        - matrix -- matrix representation (alternative to f)
        - check -- whether to verify form preservation
        """
        Morphism.__init__(self, homset)
        
        if matrix is not None:
            self._matrix = matrix
            # Define function from matrix
            def matrix_action(v):
                coords = v.to_vector()
                new_coords = matrix * coords
                return self.codomain()._from_vector(new_coords)
            self._function = matrix_action
        elif f is not None:
            self._function = f
            self._matrix = None
        else:
            raise ValueError("Must provide either function f or matrix")
        
        if check:
            self._check_form_preservation()
    
    def _call_(self, v):
        """
        Apply morphism to element.
        
        INPUT:
        - v -- element of domain
        
        OUTPUT:
        Element of codomain
        """
        return self._function(v)
    
    def matrix(self):
        """
        Return matrix representation of morphism.
        
        Computed relative to chosen bases of domain and codomain.
        
        EXAMPLES::
        
            sage: G = matrix(QQ, [[1, 0], [0, 1]])
            sage: M = BilinearModule(G)
            sage: H = Hom(M, M)
            sage: id = H.identity()
            sage: id.matrix()
            [1 0]
            [0 1]
        """
        if self._matrix is not None:
            return self._matrix
        
        # Compute matrix from function
        domain_gens = self.domain().gens()
        codomain_basis = self.codomain().gens()
        
        from sage.matrix.constructor import matrix
        cols = []
        for v in domain_gens:
            image = self(v)
            coords = image.to_vector()
            cols.append(coords)
        
        self._matrix = matrix(self.base_ring(), cols).transpose()
        return self._matrix
    
    def _check_form_preservation(self):
        """
        Verify that this morphism preserves bilinear forms.
        
        Tests b₂(f(v), f(w)) = b₁(v, w) for basis elements.
        """
        domain = self.domain()
        codomain = self.codomain()
        
        # Test on basis elements
        domain_gens = domain.gens()
        
        for i, v in enumerate(domain_gens):
            for j, w in enumerate(domain_gens):
                # Compute b₁(v, w)
                original = domain.bilinear_form(v, w)
                
                # Compute b₂(f(v), f(w))
                fv = self(v)
                fw = self(w)
                image = codomain.bilinear_form(fv, fw)
                
                if original != image:
                    raise ValueError(
                        f"Morphism does not preserve bilinear form: "
                        f"b₁({v}, {w}) = {original} but "
                        f"b₂(f({v}), f({w})) = {image}"
                    )
    
    def preserves_bilinear_form(self):
        """
        Test if morphism preserves bilinear forms.
        
        Returns True if b₂(f(v), f(w)) = b₁(v, w) for all v, w.
        """
        try:
            self._check_form_preservation()
            return True
        except ValueError:
            return False
    
    def is_isometry(self):
        """
        Test if morphism is an isometry.
        
        An isometry is a bijective form-preserving morphism.
        """
        return self.is_bijective() and self.preserves_bilinear_form()
    
    def is_orthogonal_transformation(self):
        """
        Test if this is an orthogonal transformation.
        
        Only meaningful for endomorphisms of the same space.
        """
        if self.domain() != self.codomain():
            return False
        
        return self.is_isometry()
```

## Specialized Morphism Types

```python
class OrthogonalTransformation(BilinearModuleMorphism):
    """
    Orthogonal transformation of a bilinear module.
    
    An orthogonal transformation is an isometry f: M → M that preserves
    the bilinear form: b(f(v), f(w)) = b(v, w).
    
    For symmetric bilinear forms, these form the orthogonal group O(M, b).
    
    EXAMPLES::
    
        sage: # Standard orthogonal transformation (rotation)
        sage: G = matrix(QQ, [[1, 0], [0, 1]])
        sage: M = BilinearModule(G)
        sage: # 90-degree rotation matrix
        sage: R = matrix(QQ, [[0, -1], [1, 0]])
        sage: rot = OrthogonalTransformation(Hom(M, M), matrix=R)
        sage: rot.is_orthogonal_transformation()
        True
    """
    
    def __init__(self, homset, f=None, matrix=None):
        """Initialize orthogonal transformation with automatic checking."""
        super().__init__(homset, f=f, matrix=matrix, check=True)
        
        if not self.is_orthogonal_transformation():
            raise ValueError("Morphism is not an orthogonal transformation")
    
    def inverse(self):
        """
        Return inverse orthogonal transformation.
        
        For orthogonal transformations, the inverse exists and is also orthogonal.
        """
        if not hasattr(self, '_inverse'):
            inv_matrix = self.matrix().inverse()
            self._inverse = OrthogonalTransformation(
                self.parent(), matrix=inv_matrix
            )
        return self._inverse
    
    def determinant(self):
        """
        Return determinant (±1 for orthogonal transformations).
        """
        return self.matrix().determinant()
    
    def is_special_orthogonal(self):
        """Test if determinant is +1 (proper rotation)."""
        return self.determinant() == 1
    
    def is_reflection(self):
        """Test if determinant is -1 (reflection)."""
        return self.determinant() == -1

class SymplecticTransformation(BilinearModuleMorphism):
    """
    Symplectic transformation of a skew-symmetric bilinear module.
    
    Preserves skew-symmetric bilinear forms. These form the symplectic group Sp(M, b).
    """
    
    def __init__(self, homset, f=None, matrix=None):
        """Initialize symplectic transformation."""
        super().__init__(homset, f=f, matrix=matrix, check=True)
        
        # Verify domain has skew-symmetric form
        if not self.domain().is_skew_symmetric():
            raise ValueError("Symplectic transformations require skew-symmetric forms")
        
        if not self.is_isometry():
            raise ValueError("Morphism is not a symplectic transformation")
    
    def symplectic_inverse(self):
        """Return symplectic inverse."""
        # For symplectic matrices: (M^T J M = J) ⟹ M^(-1) = -J M^T J
        # where J is the standard symplectic matrix
        raise NotImplementedError("Symplectic inverse computation")

class BilinearModuleIsomorphism(BilinearModuleMorphism):
    """
    Isomorphism between bilinear modules.
    
    A bijective morphism that preserves bilinear forms.
    Establishes equivalence between bilinear modules.
    """
    
    def __init__(self, homset, f=None, matrix=None):
        """Initialize isomorphism with bijectivity checking."""
        super().__init__(homset, f=f, matrix=matrix, check=True)
        
        if not self.is_bijective():
            raise ValueError("Morphism is not bijective")
    
    def inverse(self):
        """Return inverse isomorphism."""
        if not hasattr(self, '_inverse'):
            inv_matrix = self.matrix().inverse()
            inv_homset = Hom(self.codomain(), self.domain())
            self._inverse = BilinearModuleIsomorphism(
                inv_homset, matrix=inv_matrix
            )
        return self._inverse
```

## Homset Methods and Universal Properties

```python
class BilinearModuleHomset(HomsetWithBase):
    # ... (previous methods) ...
    
    def orthogonal_group(self):
        """
        Return the orthogonal group of endomorphisms.
        
        Only for endomorphisms M → M with symmetric bilinear form.
        """
        if self.domain() != self.codomain():
            raise ValueError("Orthogonal group only defined for endomorphisms")
        
        if not self.domain().is_symmetric():
            raise ValueError("Orthogonal group requires symmetric bilinear form")
        
        return OrthogonalGroup(self.domain())
    
    def symplectic_group(self):
        """
        Return the symplectic group of endomorphisms.
        
        Only for endomorphisms M → M with skew-symmetric bilinear form.
        """
        if self.domain() != self.codomain():
            raise ValueError("Symplectic group only defined for endomorphisms")
        
        if not self.domain().is_skew_symmetric():
            raise ValueError("Symplectic group requires skew-symmetric bilinear form")
        
        return SymplecticGroup(self.domain())
    
    def isometry_group(self):
        """
        Return the group of isometries (form-preserving bijections).
        """
        domain = self.domain()
        
        if domain.is_symmetric():
            return self.orthogonal_group()
        elif domain.is_skew_symmetric():
            return self.symplectic_group()
        else:
            # General isometry group
            return IsometryGroup(domain)
    
    def _test_universal_property(self, **options):
        """
        Test universal property of bilinear module morphisms.
        
        Morphisms form a module under pointwise operations.
        """
        tester = self._tester(**options)
        
        # Test zero morphism
        zero = self.zero()
        if self.domain().ngens() > 0:
            v = self.domain().an_element()
            tester.assertEqual(zero(v), self.codomain().zero())
        
        # Test linearity preservation
        if self.domain().ngens() >= 2:
            v, w = self.domain().gens()[:2]
            r = self.base_ring().random_element()
            
            # Any morphism should preserve linearity
            phi = self.an_element() if hasattr(self, 'an_element') else zero
            
            # f(r*v + w) = r*f(v) + f(w)
            lhs = phi(r*v + w)
            rhs = r*phi(v) + phi(w)
            # Note: this test assumes morphisms preserve R-module structure
```

## Kernel and Image Operations

```python
def kernel(self):
    """
    Return kernel of the morphism.
    
    ker(f) = {v ∈ M₁ : f(v) = 0}
    
    For bilinear module morphisms, the kernel inherits a bilinear form
    (the restriction of the domain's form).
    """
    domain = self.domain()
    
    # Find basis vectors that map to zero
    kernel_basis = []
    domain_gens = domain.gens()
    
    # Use matrix representation to find kernel
    M = self.matrix()
    kernel_space = M.kernel()
    
    # Convert kernel vectors back to domain elements
    for v in kernel_space.basis():
        element = domain._from_vector(v)
        kernel_basis.append(element)
    
    # Create submodule with inherited bilinear form
    return domain.submodule(kernel_basis)

def image(self):
    """
    Return image of the morphism.
    
    im(f) = {f(v) : v ∈ M₁}
    
    The image inherits a bilinear form from the codomain.
    """
    codomain = self.codomain()
    
    # Image is spanned by images of basis elements
    image_generators = []
    for v in self.domain().gens():
        image_generators.append(self(v))
    
    return codomain.submodule(image_generators)

def cokernel(self):
    """
    Return cokernel M₂/im(f).
    
    This is the quotient of codomain by image.
    """
    return self.codomain() / self.image()

def is_injective(self):
    """Test if morphism is injective (kernel is trivial)."""
    return self.kernel().dimension() == 0

def is_surjective(self):
    """Test if morphism is surjective (image is full codomain)."""
    return self.image().dimension() == self.codomain().dimension()

def is_bijective(self):
    """Test if morphism is bijective."""
    return self.is_injective() and self.is_surjective()

def rank(self):
    """Return rank of the morphism (dimension of image)."""
    return self.image().dimension()

def nullity(self):
    """Return nullity of the morphism (dimension of kernel)."""
    return self.kernel().dimension()
```

## Factory Functions

```python
def identity_morphism(module):
    """
    Construct identity morphism on a bilinear module.
    
    INPUT:
    - module -- bilinear module
    
    OUTPUT:
    Identity morphism in End(module)
    """
    homset = Hom(module, module)
    return homset.identity()

def zero_morphism(domain, codomain):
    """
    Construct zero morphism between bilinear modules.
    
    INPUT:
    - domain -- source bilinear module
    - codomain -- target bilinear module
    
    OUTPUT:
    Zero morphism in Hom(domain, codomain)
    """
    homset = Hom(domain, codomain)
    return homset.zero()

def orthogonal_reflection(module, hyperplane):
    """
    Construct orthogonal reflection across hyperplane.
    
    INPUT:
    - module -- bilinear module with symmetric form
    - hyperplane -- codimension-1 submodule
    
    OUTPUT:
    Orthogonal transformation reflecting across hyperplane
    """
    if not module.is_symmetric():
        raise ValueError("Reflection requires symmetric bilinear form")
    
    if hyperplane.dimension() != module.dimension() - 1:
        raise ValueError("Hyperplane must have codimension 1")
    
    # Implementation would construct reflection matrix
    raise NotImplementedError("Orthogonal reflection construction")
```

## Mathematical Properties

The bilinear module morphism framework maintains these properties:

```python
# Mathematical assertion: Form preservation
# For morphism f: (M₁, b₁) → (M₂, b₂):
# b₂(f(v), f(w)) = b₁(v, w) for all v, w ∈ M₁

# Mathematical assertion: Linearity preservation  
# f(r*v + w) = r*f(v) + f(w) for all r ∈ R, v, w ∈ M₁

# Mathematical assertion: Kernel structure
# ker(f) inherits bilinear form from domain by restriction

# Mathematical assertion: Image structure
# im(f) inherits bilinear form from codomain by restriction

# Mathematical assertion: Isometry characterization
# f is isometry ⟺ f is bijective and preserves bilinear form

# Mathematical assertion: Orthogonal group properties
# O(M, b) = {f ∈ End(M) : f isometry} forms a group

# Mathematical assertion: Rank-nullity theorem
# For finite-dimensional modules: dim(M₁) = rank(f) + nullity(f)
```

This morphism framework provides the homological algebra foundation for bilinear modules while maintaining form-preservation constraints.