<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RBilForms/RBilForms_objects.md
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
    
    Natural notation: We would prefer ⟨v, w⟩ but this requires preprocessing.
    Alternative keyboard-friendly notation: <v, w> could be implemented via
    operator overloading or preprocessor extensions.
    
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
        
        # PROPOSED NATURAL NOTATION (not yet implemented):
        # sage: <v, w>  # Should evaluate bilinear form
        # 1
        # sage: ⟨v, w⟩  # Unicode inner product notation
        # 1
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

## Mathematical Test Assertions

The following assertions verify the mathematical properties of bilinear form operations using SageMath's canonical constructions:

### Assertion 1: Bilinearity Property
```python
# Mathematical assertion: Bilinear forms must satisfy linearity in both arguments
# Reference: Jacobson "Basic Algebra" Vol I, multilinear functions definition
# sage: M = matrix(ZZ, [[2, 1], [1, 3]])  # Symmetric positive definite form
# sage: v1, v2, v3 = vector([1, 0]), vector([0, 1]), vector([1, 1])
# sage: a, b = 2, 3
# sage: def bilinear_eval(M, x, y): return x * M * y
# sage: left_linear = bilinear_eval(M, a*v1 + b*v2, v3)
# sage: sum_evals = a * bilinear_eval(M, v1, v3) + b * bilinear_eval(M, v2, v3)
# sage: left_linear == sum_evals
# True
# sage: right_linear = bilinear_eval(M, v3, a*v1 + b*v2)
# sage: sum_evals_right = a * bilinear_eval(M, v3, v1) + b * bilinear_eval(M, v3, v2)
# sage: right_linear == sum_evals_right
# True
```

### Assertion 2: Symmetric-Skew Decomposition (Serre)
```python
# Mathematical assertion: Every bilinear form decomposes uniquely into symmetric and skew parts
# Reference: Serre "Linear Representations", symmetric and alternating squares
# sage: M_nonsym = matrix(ZZ, [[1, 2], [3, 4]])
# sage: M_sym = (M_nonsym + M_nonsym.transpose()) / 2
# sage: M_skew = (M_nonsym - M_nonsym.transpose()) / 2
# sage: M_sym + M_skew == M_nonsym  # Reconstruction
# True
# sage: M_sym.is_symmetric()  # Symmetric part is symmetric
# True
# sage: M_skew == -M_skew.transpose()  # Skew part is skew-symmetric
# True
# sage: # For symmetric forms, skew part is zero
# sage: M_already_sym = matrix(ZZ, [[2, 1], [1, 3]])
# sage: skew_of_sym = (M_already_sym - M_already_sym.transpose()) / 2
# sage: skew_of_sym.is_zero()
# True
```

### Assertion 3: Pullback Form Evaluation
```python
# Mathematical assertion: Pullback forms preserve evaluation under morphisms
# Reference: Jacobson "Basic Algebra" Vol II, morphisms and universal properties
# sage: M_orig = matrix(ZZ, [[2, 1], [1, 3]])  # Original bilinear form
# sage: f = matrix(ZZ, [[1], [1]])  # Morphism Z -> Z^2: x ↦ (x,x)
# sage: M_pullback = f.transpose() * M_orig * f  # Pullback form
# sage: # Direct evaluation on original space
# sage: v_orig = vector([1, 1])
# sage: direct_eval = v_orig * M_orig * v_orig
# sage: # Evaluation via pullback
# sage: pullback_eval = M_pullback[0, 0]  # 1×1 matrix entry
# sage: direct_eval == pullback_eval
# True
# sage: direct_eval  # Should be 2·1·1 + 1·1·1 + 1·1·1 + 3·1·1 = 7
# 7
```

### Assertion 4: Tensor Product Signature Preservation
```python
# Mathematical assertion: Tensor products preserve certain signature properties
# Reference: Jacobson "Basic Algebra", tensor products of bilinear forms
# sage: def matrix_signature(M):
# ....:     eigenvals = M.eigenvalues()
# ....:     pos = sum(1 for ev in eigenvals if ev > 0)
# ....:     neg = sum(1 for ev in eigenvals if ev < 0)
# ....:     zero = sum(1 for ev in eigenvals if ev == 0)
# ....:     return (pos, neg, zero)
# sage: M1 = matrix(ZZ, [[1, 0], [0, -1]])  # Hyperbolic form (1,1,0)
# sage: M2 = matrix(ZZ, [[2]])  # Positive definite (1,0,0)
# sage: M_tensor = M1.tensor_product(M2)
# sage: sig1, sig2, sig_tensor = matrix_signature(M1), matrix_signature(M2), matrix_signature(M_tensor)
# sage: sig1, sig2, sig_tensor
# ((1, 1, 0), (1, 0, 0), (1, 1, 0))
# sage: # Signature relationship: rank and determinant sign preserve structure
# sage: M_tensor.rank() == M1.rank() * M2.rank()
# True
```

### Assertion 5: Orthogonality Relations for Symmetric Forms
```python
# Mathematical assertion: Symmetric forms have well-defined orthogonal complements
# Reference: Conventions - orthogonality behavior section
# sage: M_sym = matrix(ZZ, [[2, 1], [1, 3]])  # Symmetric form
# sage: v1, v2 = vector([1, 0]), vector([0, 1])
# sage: # Symmetry: B(v1, v2) = B(v2, v1)
# sage: eval_12 = v1 * M_sym * v2
# sage: eval_21 = v2 * M_sym * v1
# sage: eval_12 == eval_21
# True
# sage: eval_12  # Should be 1
# 1
# sage: # For symmetric forms, if B(v,w) = 0 then B(w,v) = 0
# sage: # Find orthogonal vector to v1 = (1,0)
# sage: v_ortho = vector([-1, 2])  # Chosen so (1,0)·M·(-1,2) = 0
# sage: orthogonal_check = v1 * M_sym * v_ortho
# sage: orthogonal_check == 0
# True
```

### Assertion 6: Root System Cartan Matrix Properties
```python
# Mathematical assertion: Root systems provide canonical symmetric bilinear forms
# Reference: Conventions - Cartan matrices vs Gram matrices distinction
# sage: R = RootSystem(['A', 2])  # A2 root system (triangular lattice)
# sage: C = R.cartan_matrix()  # Cartan matrix (reflection encoding)
# sage: C
# [ 2 -1]
# [-1  2]
# sage: C.is_symmetric()  # A-series Cartan matrices are symmetric
# True
# sage: # Cartan matrix is positive definite for finite root systems
# sage: eigenvals = C.eigenvalues()
# sage: all(ev > 0 for ev in eigenvals)
# True
# sage: eigenvals  # Should be [1, 3] for A2
# [3, 1]
# sage: # A2 has finite Weyl group (dihedral D_6)
# sage: W = R.root_system.weyl_group()
# sage: W.cardinality()
# 6
```

### Assertion 7: Non-Degenerate Form Properties
```python
# Mathematical assertion: Non-degenerate forms have invertible Gram matrices
# Reference: Conventions - non-degeneracy definition
# sage: M_nondegenerate = matrix(ZZ, [[2, 1], [1, 3]])
# sage: det_nonzero = M_nondegenerate.determinant() != 0
# sage: det_nonzero  # Should be True for non-degenerate forms
# True
# sage: M_nondegenerate.determinant()  # Should be 2·3 - 1·1 = 5
# 5
# sage: # Degenerate form has zero determinant
# sage: M_degenerate = matrix(ZZ, [[1, 2], [2, 4]])  # Rank 1 matrix
# sage: M_degenerate.determinant() == 0
# True
# sage: M_degenerate.rank()  # Should be 1
# 1
```

### Assertion 8: Indefinite Form Existence
```python
# Mathematical assertion: Indefinite forms can be constructed with mixed signature
# Reference: Mathematical Foundations - indefinite quadratic forms theory
# sage: # Construct hyperbolic form (signature (1,1,0))
# sage: M_hyperbolic = matrix(ZZ, [[1, 0], [0, -1]])
# sage: sig = matrix_signature(M_hyperbolic)
# sage: sig == (1, 1, 0)  # One positive, one negative eigenvalue
# True
# sage: # Standard hyperbolic form: x^2 - y^2
# sage: v_pos = vector([1, 0])  # Positive direction
# sage: v_neg = vector([0, 1])  # Negative direction
# sage: pos_eval = v_pos * M_hyperbolic * v_pos
# sage: neg_eval = v_neg * M_hyperbolic * v_neg
# sage: pos_eval > 0 and neg_eval < 0
# True
# sage: pos_eval, neg_eval
# (1, -1)
```

---

## Natural Inner Product Notation: `<v, w>`

The most natural mathematical notation for evaluating bilinear forms is the inner product notation `⟨v, w⟩` or `<v, w>`. This section explores implementation strategies for this intuitive syntax.

### Current SageMath Limitation

```sage
# Current verbose syntax:
sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
sage: v = vector([1, 0])
sage: w = vector([0, 1])
sage: b.evaluate(v, w)  # Clunky method call
1

# What mathematicians actually write:
# ⟨v, w⟩ = 1  (not supported)
# <v, w> = 1  (not supported)
```

### Proposed Implementation Strategies

#### Strategy 1: Context-Aware Angle Bracket Overloading

```python
class BilinearModule(FreeModule):
    """Module with natural inner product notation."""
    
    def __init__(self, base_ring, rank, bilinear_form=None):
        super().__init__(base_ring, rank)
        self._bilinear_form = bilinear_form or self._default_form()
    
    def _default_form(self):
        """Default to standard Euclidean inner product."""
        from sage.matrix.constructor import identity_matrix
        return BilinearForm(identity_matrix(self.base_ring(), self.rank()))
    
    class Element(FreeModuleElement):
        """Vector with inner product operations."""
        
        def __lt__(self, other):
            """
            Override < for inner product: <v, w> via v < w (EXPERIMENTAL).
            
            WARNING: This conflicts with vector ordering, so it's not recommended.
            Better to use preprocessing approach below.
            """
            if hasattr(self.parent(), '_in_inner_product_context'):
                return self.parent()._bilinear_form.evaluate(self, other)
            else:
                return super().__lt__(other)  # Normal vector comparison

# Better approach: Preprocessing
class InnerProductPreprocessor:
    """Preprocess <v, w> notation into form.evaluate(v, w)."""
    
    @staticmethod
    def preprocess_inner_product(code_string):
        """
        Convert <v, w> notation to proper evaluation calls.
        
        EXAMPLES::
        
            sage: code = "result = <v, w> + 2*<u, v>"
            sage: processed = InnerProductPreprocessor.preprocess_inner_product(code)
            sage: print(processed)
            result = _default_form.evaluate(v, w) + 2*_default_form.evaluate(u, v)
        """
        import re
        
        # Pattern: <variable, variable> 
        pattern = r'<\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*>'
        replacement = r'_default_form.evaluate(\1, \2)'
        
        return re.sub(pattern, replacement, code_string)
    
    @staticmethod
    def install_preprocessor():
        """Install the preprocessor in SageMath's input pipeline."""
        # This would integrate with SageMath's preparser
        pass
```

#### Strategy 2: Unicode Angle Bracket Support

```python
class UnicodeInnerProduct:
    """Support for Unicode ⟨v, w⟩ notation via special parsing."""
    
    @staticmethod
    def parse_unicode_brackets(code_string):
        """
        Convert ⟨v, w⟩ to proper evaluation.
        
        EXAMPLES::
        
            sage: code = "norm_squared = ⟨v, v⟩"
            sage: processed = UnicodeInnerProduct.parse_unicode_brackets(code)
            sage: print(processed)
            norm_squared = _default_form.evaluate(v, v)
        """
        import re
        
        # Unicode left/right angle brackets: ⟨ (U+27E8) and ⟩ (U+27E9)
        pattern = r'⟨\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*⟩'
        replacement = r'_default_form.evaluate(\1, \2)'
        
        return re.sub(pattern, replacement, code_string)
```

#### Strategy 3: Function-Call Alternative with Natural Names

```python
# Compromise: Use function calls but with natural names
def inner(v, w, form=None):
    """
    Natural inner product function: inner(v, w).
    
    This provides a keyboard-friendly alternative to <v, w>.
    
    INPUT:
    - v, w: Vectors in the module
    - form: Bilinear form to use (defaults to Euclidean)
    
    OUTPUT:
    Inner product value
    
    EXAMPLES::
    
        sage: v = vector([1, 2])
        sage: w = vector([3, 4])
        sage: inner(v, w)  # Euclidean inner product
        11
        
        sage: # Custom form
        sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: inner(v, w, form=b)
        19
    """
    if form is None:
        # Default Euclidean inner product
        return v.dot_product(w)
    else:
        return form.evaluate(v, w)

# Even shorter aliases
def ⟨(v, w, form=None): return inner(v, w, form)  # Unicode function name!
def dot(v, w, form=None): return inner(v, w, form)  # Traditional name
```

### Usage Examples with Natural Notation

```sage
# Current SageMath (verbose):
sage: b = BilinearForm(matrix(ZZ, [[2, 1], [1, 3]]))
sage: v = vector([1, 0])
sage: w = vector([0, 1])
sage: result = b.evaluate(v, w)

# Proposed natural notation (after preprocessing):
sage: result = <v, w>  # Automatically uses default form
1

sage: result = ⟨v, w⟩  # Unicode version
1

# For custom forms:
sage: with BilinearForm(matrix(ZZ, [[2, 1], [1, 3]])) as b:
....:     result = <v, w>  # Uses custom form b
1

# Function-based alternative (works immediately):
sage: result = inner(v, w)  # Euclidean
11
sage: result = inner(v, w, form=b)  # Custom form
1
```

### Implementation Benefits

#### 1. **Mathematical Naturalness**
- `<v, w>` matches handwritten mathematics exactly
- Much clearer than `b.evaluate(v, w)`
- Supports complex expressions: `<v, w> + 2*<u, v> - <v, v>`

#### 2. **Backwards Compatibility**
- Original `.evaluate()` method still works
- Can be implemented via preprocessing without breaking existing code
- Graceful fallback for edge cases

#### 3. **Context Awareness**
- Different forms can be active in different contexts
- Natural integration with symmetric/skew forms
- Supports both Euclidean and general bilinear forms

#### 4. **Multiple Implementation Paths**
- **Immediate**: Function-based `inner(v, w)` 
- **Short-term**: Preprocessing `<v, w>`
- **Long-term**: Unicode support `⟨v, w⟩`

### Mathematical Applications

```sage
# Gram-Schmidt orthogonalization with natural notation:
sage: def gram_schmidt(vectors, form=None):
....:     orthogonal = []
....:     for v in vectors:
....:         for u in orthogonal:
....:             proj_coeff = <v, u> / <u, u>  # Natural!
....:             v = v - proj_coeff * u
....:         orthogonal.append(v)
....:     return orthogonal

# Bilinear form properties:
sage: def is_positive_definite(form, test_vectors):
....:     return all(<v, v> > 0 for v in test_vectors)

# Symmetric vs skew-symmetric testing:
sage: def verify_symmetry(form, v, w):
....:     return <v, w> == <w, v>  # Should be True for symmetric forms

# Orthogonality testing:
sage: def are_orthogonal(v, w, form=None):
....:     return <v, w> == 0
```

This natural notation would dramatically improve the mathematical experience in SageMath, making bilinear form computations as intuitive as handwritten mathematics!
