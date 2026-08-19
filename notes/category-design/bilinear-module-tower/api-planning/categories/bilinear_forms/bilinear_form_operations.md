<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_forms/bilinear_form_operations.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: BilinearForm Operations

Operations on bilinear forms b ∈ Hom_R(L ⊗_R L, R).
These are operations on the form itself, not morphisms between bilinear modules.

## Form Decomposition and Analysis

```python
def symmetric_part(self):
    r"""
    Extract the symmetric part of the bilinear form.
    
    Returns the symmetric bilinear form: (b(v,w) + b(w,v))/2
    
    OUTPUT:
    The symmetric part of this bilinear form
    
    EXAMPLES::
    
        sage: # Non-symmetric form
        sage: b = BilinearForm(matrix(ZZ, [[1, 2], [3, 4]]))
        sage: b_sym = b.symmetric_part()
        sage: b_sym.matrix()
        [  1 5/2]
        [5/2   4]
        
        sage: # Verify symmetry
        sage: b_sym.is_symmetric()
        True
        
        sage: # For symmetric forms, returns self
        sage: c = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: c_sym = c.symmetric_part()
        sage: c_sym == c
        True
    """

def skew_symmetric_part(self):
    r"""
    Extract the skew-symmetric part of the bilinear form.
    
    Returns the skew-symmetric bilinear form: (b(v,w) - b(w,v))/2
    
    OUTPUT:
    The skew-symmetric part of this bilinear form
    
    EXAMPLES::
    
        sage: # Non-symmetric form
        sage: b = BilinearForm(matrix(ZZ, [[1, 2], [3, 4]]))
        sage: b_skew = b.skew_symmetric_part()
        sage: b_skew.matrix()
        [ 0 -1/2]
        [1/2   0]
        
        sage: # Verify skew-symmetry
        sage: b_skew.is_skew_symmetric()
        True
        
        sage: # Canonical decomposition
        sage: b_sym = b.symmetric_part()
        sage: b_skew = b.skew_symmetric_part()
        sage: b == b_sym + b_skew
        True
        
        sage: # For symmetric forms, skew part is zero
        sage: c = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: c_skew = c.skew_symmetric_part()
        sage: c_skew.is_zero()
        True
    """

```

## Form Composition and Operations

```python
def fiber_product(self, phi_left, phi_right=None):
    r"""
    Fiber product of bilinear form with morphisms φ_L: N → M and φ_R: P → M.
    
    Returns the bilinear form on N × P given by: (v, w) ↦ b(φ_L(v), φ_R(w)).
    This is the categorical pullback b ∘ (φ_L × φ_R).
    
    INPUT:
    - phi_left: Morphism N → M for left argument
    - phi_right: Morphism P → M for right argument (defaults to phi_left)
    
    OUTPUT:
    Bilinear form on the fiber product of the morphisms
    
    EXAMPLES::
    
        sage: # Original form on Z^2
        sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        
        sage: # Inclusion of submodule spanned by (1,1)
        sage: phi = matrix(ZZ, [[1], [1]])
        sage: b_fiber = b.fiber_product(phi)
        sage: b_fiber.matrix()
        [6]
        
        sage: # Different left and right morphisms
        sage: phi_L = matrix(ZZ, [[1], [0]])  # First coordinate
        sage: phi_R = matrix(ZZ, [[0], [1]])  # Second coordinate  
        sage: b_mixed = b.fiber_product(phi_L, phi_R)
        sage: b_mixed.matrix()
        [1]  # b((1,0), (0,1)) = 1
        
        sage: # Verify: fiber product gives b((1,1), (1,1)) = 6
        sage: v = vector([1, 1])
        sage: b.evaluate(v, v)
        6
    """

def pullback(self, f):
    r"""
    Standard pullback of bilinear form along a single morphism.
    
    For morphism f: N → M, returns bilinear form on N given by: (v, w) ↦ b(f(v), f(w)).
    This is the special case of fiber_product where φ_L = φ_R = f.
    
    INPUT:
    - f: Morphism N → M
    
    OUTPUT:
    Pullback bilinear form on the domain of f
    
    EXAMPLES::
    
        sage: # Original form on Z^2
        sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        
        sage: # Inclusion map (1,1) -> (1,1)
        sage: inc = matrix(ZZ, [[1], [1]])
        sage: b_pulled = b.pullback(inc)
        sage: b_pulled.matrix()
        [6]
        
        sage: # This is equivalent to fiber_product(inc, inc)
        sage: b_fiber = b.fiber_product(inc, inc)
        sage: b_pulled == b_fiber
        True
    """

def tensor(self, other):
    r"""
    Tensor product of bilinear forms.
    
    For bilinear forms b₁: M₁ × M₁ → R and b₂: M₂ × M₂ → R,
    returns b₁ ⊗ b₂: (M₁ ⊗ M₂) × (M₁ ⊗ M₂) → R defined by:
    (b₁ ⊗ b₂)((v₁ ⊗ v₂), (w₁ ⊗ w₂)) = b₁(v₁, w₁) · b₂(v₂, w₂)
    
    INPUT:
    - other: Another bilinear form
    
    OUTPUT:
    Tensor product bilinear form
    
    EXAMPLES::
    
        sage: b1 = BilinearForm(matrix(ZZ, [[1, 0], [0, -1]]))  # Hyperbolic
        sage: b2 = BilinearForm(matrix(ZZ, [[2]]))              # Positive definite
        sage: b_tensor = b1.tensor(b2)
        sage: b_tensor.matrix()
        [2  0]
        [0 -2]
        
        sage: # Signatures multiply
        sage: b1.signature()
        (1, 1, 0)
        sage: b2.signature()
        (1, 0, 0)
        sage: b_tensor.signature()
        (2, 2, 0)
    """
```

## Form Properties and Invariants

```python
def is_zero(self):
    r"""
    Test if this is the zero bilinear form.
    
    OUTPUT:
    True if b(v, w) = 0 for all v, w, False otherwise
    
    EXAMPLES::
    
        sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: zero_form = BilinearForm(matrix(ZZ, [[0, 0], [0, 0]]))
        sage: b.is_zero()
        False
        sage: zero_form.is_zero()
        True
    """

def evaluate(self, v, w):
    r"""
    Evaluate the bilinear form on two vectors.
    
    INPUT:
    - v, w: Vectors in the module
    
    OUTPUT:
    Value b(v, w) in the base ring
    
    EXAMPLES::
    
        sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: v = vector([1, 0])
        sage: w = vector([0, 1])
        sage: b.evaluate(v, w)
        1
        sage: b.evaluate(w, v)
        1
    """

# COMPUTATIONAL HACKS (basis-dependent, not mathematically well-defined)
# Uncomment only when computational access to matrix representation is needed.
# Requires choice of basis - Zorn's lemma guarantees existence over fields,
# but general modules may not have bases.

# def matrix(self, basis=None):
#     r"""
#     HACK: Return matrix representation relative to a chosen basis.
#     
#     WARNING: This is NOT well-defined without specifying a basis!
#     The same bilinear form has different matrix representations
#     under different bases.
#     
#     INPUT:
#     - basis: Basis of the module (required for well-definedness)
#     
#     OUTPUT:
#     Gram matrix relative to the specified basis
#     """

# def trace(self, basis=None):  
#     r"""
#     HACK: Return trace relative to a chosen basis.
#     
#     WARNING: This is NOT well-defined without specifying a basis!
#     Trace depends on the matrix representation.
#     
#     INPUT:
#     - basis: Basis of the module (required for well-definedness)
#     
#     OUTPUT:
#     Trace of the Gram matrix relative to the specified basis
#     """
```

## Morphisms Between Bilinear Forms

```python
def morphism_to(self, other, module_morphism):
    r"""
    Create a morphism of bilinear forms induced by a module morphism.
    
    For bilinear forms b₁: M₁ × M₁ → R and b₂: M₂ × M₂ → R,
    and module morphism φ: M₁ → M₂, creates the form morphism:
    b₁ → b₂ via φ if b₂(φ(v), φ(w)) = b₁(v, w) for all v, w ∈ M₁
    
    This is the morphism in the category of bilinear forms.
    
    INPUT:
    - other: Target bilinear form
    - module_morphism: R-module morphism between underlying modules
    
    OUTPUT:
    Morphism of bilinear forms (if the module morphism preserves forms)
    
    EXAMPLES::
    
        sage: # Standard orthogonal forms
        sage: b1 = BilinearForm(matrix(ZZ, [[1, 0], [0, 1]]))  # On Z²
        sage: b2 = BilinearForm(matrix(ZZ, [[2, 0], [0, 2]]))  # Scaled version
        
        sage: # Scaling morphism φ: (x,y) ↦ (√2·x, √2·y) 
        sage: # Note: This won't preserve forms in general
        sage: scaling = matrix(QQ, [[sqrt(2), 0], [0, sqrt(2)]])
        sage: 
        sage: # This would fail since scaling doesn't preserve forms
        sage: try:
        ....:     form_morph = b1.morphism_to(b2, scaling)
        ....: except ValueError as e:
        ....:     print(f"Error: {e}")
        Error: Module morphism does not induce form morphism
        
        sage: # Identity morphism always works for same forms
        sage: identity = matrix(ZZ, [[1, 0], [0, 1]])
        sage: id_morph = b1.morphism_to(b1, identity)
        sage: id_morph.is_identity()
        True
        
        sage: # Orthogonal transformation preserves forms
        sage: rotation = matrix(ZZ, [[0, -1], [1, 0]])  # 90° rotation
        sage: rot_morph = b1.morphism_to(b1, rotation)
        sage: rot_morph.preserves_form()
        True
    """

def hom_space(self, other):
    r"""
    Return the space of morphisms from this form to another.
    
    This is Hom(b₁, b₂) in the category of bilinear forms.
    Elements are module morphisms φ: M₁ → M₂ such that b₂ ∘ (φ × φ) = b₁.
    
    INPUT:
    - other: Target bilinear form
    
    OUTPUT:
    The hom-space as a module of form morphisms
    
    EXAMPLES::
    
        sage: b1 = BilinearForm(matrix(ZZ, [[1, 0], [0, -1]]))  # Hyperbolic
        sage: b2 = BilinearForm(matrix(ZZ, [[2, 0], [0, -2]]))  # Scaled hyperbolic
        
        sage: # Hom space between isometric forms
        sage: Hom_space = b1.hom_space(b2)
        sage: Hom_space.dimension()
        0  # No form-preserving morphisms between different scales
        
        sage: # Hom space for same form (orthogonal group)
        sage: End_space = b1.hom_space(b1)
        sage: End_space.is_group()
        True  # This is O(1,1) ≅ {±1} × {±1}
    """

def internal_hom(self, other):
    r"""
    Return the internal hom object Hom(b₁, b₂) for tensor-hom adjunction.
    
    This constructs the bilinear form that represents morphisms from 
    this form to other, enabling the adjunction:
    Hom(b₁ ⊗ b₂, b₃) ≅ Hom(b₁, Hom(b₂, b₃))
    
    INPUT:
    - other: Target bilinear form
    
    OUTPUT:
    Internal hom bilinear form
    
    EXAMPLES::
    
        sage: # Simple 1D forms
        sage: b1 = BilinearForm(matrix(ZZ, [[2]]))
        sage: b2 = BilinearForm(matrix(ZZ, [[3]]))
        
        sage: # Internal hom
        sage: hom_form = b1.internal_hom(b2)
        
        sage: # Verify tensor-hom adjunction
        sage: b3 = BilinearForm(matrix(ZZ, [[5]]))
        sage: tensor_form = b1.tensor(b2)
        
        sage: # These spaces should be isomorphic
        sage: Hom1 = tensor_form.hom_space(b3)
        sage: Hom2 = b1.hom_space(hom_form.internal_hom(b3))
        sage: # Implementation would verify: Hom1.dimension() == Hom2.dimension()
    """

def compose(self, other):
    r"""
    Compose morphisms of bilinear forms.
    
    For morphisms f: b₁ → b₂ and g: b₂ → b₃, returns g ∘ f: b₁ → b₃.
    
    INPUT:
    - other: Morphism to compose with
    
    OUTPUT:
    Composed morphism of bilinear forms
    """

def is_isomorphism(self):
    r"""
    Test if this is an isomorphism of bilinear forms.
    
    A form morphism is an isomorphism if the underlying module morphism
    is an isomorphism and preserves the bilinear form.
    
    OUTPUT:
    True if this is an isomorphism in the category of bilinear forms
    """
```

## Symmetric Monoidal Category Structure

```python
class BilinearFormsCategory(Category):
    r"""
    The category of bilinear forms over a ring R.
    
    This is a symmetric monoidal category with:
    - Tensor product of forms: b₁ ⊗ b₂
    - Unit form: scalar multiplication form
    - Natural isomorphisms satisfying coherence conditions
    
    EXAMPLES::
    
        sage: BilForms = BilinearFormsCategory(ZZ)
        sage: BilForms in SymmetricMonoidalCategories()
        True
        
        sage: # Create forms in the category
        sage: b1 = BilinearForm(matrix(ZZ, [[1, 0], [0, -1]]))  # Hyperbolic
        sage: b2 = BilinearForm(matrix(ZZ, [[2]]))              # Positive definite
        
        sage: # Tensor product
        sage: b_tensor = b1.tensor_product(b2)
        sage: b_tensor.matrix()
        [2  0]
        [0 -2]
        
        sage: # Unit object
        sage: I = BilForms.tensor_unit()
        sage: I.matrix()
        [1]
        
        sage: # Verify unitor properties
        sage: lambda_b1 = b1.left_unitor()
        sage: I_tensor_b1 = I.tensor_product(b1)
        sage: assert lambda_b1.domain() == I_tensor_b1
        sage: assert lambda_b1.codomain() == b1
    """
    
    def __init__(self, base_ring):
        """
        Initialize the category of bilinear forms over base_ring.
        
        INPUT:
        - ``base_ring`` -- the base ring R
        """
        self._base_ring = base_ring
        Category.__init__(self)
    
    def super_categories(self):
        """
        Return the super categories.
        
        The category of bilinear forms is a symmetric monoidal category.
        """
        from sage.categories.symmetric_monoidal_categories import SymmetricMonoidalCategories
        return [SymmetricMonoidalCategories()]
    
    def base_ring(self):
        """Return the base ring."""
        return self._base_ring
    
    class ParentMethods:
        """
        Methods available on bilinear forms (the objects of this category).
        """
        
        def tensor_product(self, *others):
            r"""
            Return the tensor product of bilinear forms.
            
            For forms b₁: M₁×M₁ → R and b₂: M₂×M₂ → R, returns
            b₁ ⊗ b₂: (M₁⊗M₂) × (M₁⊗M₂) → R defined by:
            (b₁ ⊗ b₂)((v₁⊗v₂), (w₁⊗w₂)) = b₁(v₁,w₁) · b₂(v₂,w₂)
            
            EXAMPLES::
            
                sage: b1 = BilinearForm(matrix(ZZ, [[1, 0], [0, -1]]))
                sage: b2 = BilinearForm(matrix(ZZ, [[2]]))
                sage: b_tensor = b1.tensor_product(b2)
                sage: b_tensor.matrix()
                [2  0]
                [0 -2]
            """
            if len(others) == 1:
                return self.tensor(others[0])  # Use existing tensor method
            else:
                # Multi-argument tensor product
                result = self
                for other in others:
                    result = result.tensor(other)
                return result
        
        def tensor_unit(self):
            r"""
            Return the unit object for tensor products.
            
            The unit is the 1×1 form with b(1,1) = 1, representing
            the trivial form on the base ring R.
            
            OUTPUT:
            The unit bilinear form
            
            EXAMPLES::
            
                sage: I = BilinearForm.tensor_unit()
                sage: I.matrix()
                [1]
                sage: 
                sage: # Unit property: I ⊗ b ≅ b ≅ b ⊗ I
                sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I_tensor_b = I.tensor_product(b)
                sage: I_tensor_b.is_isomorphic_to(b)
                True
            """
            from sage.matrix.constructor import matrix
            return BilinearForm(matrix(self.base_ring(), [[1]]))
        
        def associator(self, B, C):
            r"""
            Return the associator isomorphism (A⊗B)⊗C ≅ A⊗(B⊗C).
            
            The associator is a natural isomorphism that relates different
            ways of parenthesizing tensor products.
            
            INPUT:
            - ``B``, ``C`` -- other bilinear forms
            
            OUTPUT:
            Associator isomorphism between the two triple tensor products
            
            EXAMPLES::
            
                sage: A = BilinearForm(matrix(ZZ, [[1]]))
                sage: B = BilinearForm(matrix(ZZ, [[2]]))  
                sage: C = BilinearForm(matrix(ZZ, [[3]]))
                
                sage: # Two ways to tensor three forms
                sage: AB_tensor_C = (A.tensor_product(B)).tensor_product(C)
                sage: A_tensor_BC = A.tensor_product(B.tensor_product(C))
                
                sage: # Associator provides the isomorphism
                sage: alpha = A.associator(B, C)
                sage: alpha.domain() == AB_tensor_C
                True
                sage: alpha.codomain() == A_tensor_BC  
                True
                sage: alpha.is_isomorphism()
                True
            """
            AB = self.tensor_product(B)
            BC = B.tensor_product(C)
            return AssociatorIsomorphism(AB.tensor_product(C), self.tensor_product(BC))
        
        def left_unitor(self):
            r"""
            Return the left unitor isomorphism I⊗A ≅ A.
            
            OUTPUT:
            Left unitor natural isomorphism
            
            EXAMPLES::
            
                sage: A = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I = BilinearForm.tensor_unit()
                
                sage: lambda_A = A.left_unitor()
                sage: lambda_A.domain() == I.tensor_product(A)
                True
                sage: lambda_A.codomain() == A
                True
            """
            I = self.tensor_unit()
            return LeftUnitorIsomorphism(I.tensor_product(self), self)
        
        def right_unitor(self):
            r"""
            Return the right unitor isomorphism A⊗I ≅ A.
            
            OUTPUT:
            Right unitor natural isomorphism
            
            EXAMPLES::
            
                sage: A = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I = BilinearForm.tensor_unit()
                
                sage: rho_A = A.right_unitor()  
                sage: rho_A.domain() == A.tensor_product(I)
                True
                sage: rho_A.codomain() == A
                True
            """
            I = self.tensor_unit()
            return RightUnitorIsomorphism(self.tensor_product(I), self)
        
        def braiding(self, B):
            r"""
            Return the braiding isomorphism A⊗B ≅ B⊗A.
            
            The braiding swaps the order of tensor factors and is its own inverse
            in symmetric monoidal categories.
            
            INPUT:
            - ``B`` -- another bilinear form
            
            OUTPUT:
            Braiding isomorphism between A⊗B and B⊗A
            
            EXAMPLES::
            
                sage: A = BilinearForm(matrix(ZZ, [[1, 0], [0, -1]]))
                sage: B = BilinearForm(matrix(ZZ, [[2]]))
                
                sage: beta_AB = A.braiding(B)
                sage: beta_AB.domain() == A.tensor_product(B)
                True
                sage: beta_AB.codomain() == B.tensor_product(A)
                True
                
                sage: # Symmetry: braiding is its own inverse
                sage: beta_BA = B.braiding(A)
                sage: composition = beta_AB.compose(beta_BA)
                sage: composition.is_identity()
                True
            """
            return BraidingIsomorphism(self.tensor_product(B), B.tensor_product(self))
```

This interface captures bilinear forms as objects in a symmetric monoidal category, enabling tensor-hom adjunctions and other advanced categorical constructions.