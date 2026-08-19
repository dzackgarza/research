<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/bilinear_RMod.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: FreeBilinearModules(R)

Free R-modules equipped with a bilinear form b: L ⊗_R L → R. Inherits from FreeModules(R).

## Bilinear Form

```python
def bilinear_form(self):
    r"""Return the bilinear form b: L ⊗_R L → R on the module."""
    
def bilinear_form(self, v, w):
    r"""
    Compute the bilinear form of two module elements.
    
    INPUT:
    - v, w: Elements of the R-module
    
    OUTPUT:
    Value of the bilinear form b(v,w) ∈ R
    """

def is_symmetric(self):
    r"""Test if the bilinear form is symmetric."""
    
def is_skew_symmetric(self):
    r"""Test if the bilinear form is skew-symmetric."""
```

## Associated Matrices and Invariants

```python
def gram_matrix(self, basis=None):
    r"""
    Return the Gram matrix of the bilinear form.
    
    INPUT:
    - basis: Optional R-module basis (uses standard basis if not provided)
    
    OUTPUT:
    Matrix G over R where G[i,j] = b(basis[i], basis[j])
    """

def discriminant(self):
    r"""
    Return the discriminant (determinant of the Gram matrix).
    
    This is well-defined up to squares in R.
    Under basis change P, det(G') = det(P)² det(G), so
    the discriminant modulo squares is a basis-invariant.
    
    Zero if and only if the form is degenerate.
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: M.discriminant()
        5
        sage: M.is_definite()  # positive discriminant
        True
        
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: H.discriminant()
        -1
        sage: H.is_indefinite()
        True
    """
```

## Enhanced Fundamental Constructions

```python
def dual(self):
    r"""
    Return the dual M* = (Hom(M,R), ι: M → Hom(M,R)) in BilinearModules.
    
    The canonical morphism ι is defined by ι(v)(w) = b(v,w).
    This is the dual object in the category of bilinear modules.
    
    For non-symmetric forms, use left_dual() or right_dual() to be explicit.
    
    OUTPUT:
    BilinearModule structure on Hom_R(M, R) with canonical morphism.
    """

def left_dual(self):
    r"""
    Return the left dual with canonical map ι_L(v)(w) = b(v,w).
    
    This is the standard "row" interpretation of the bilinear form.
    """

def right_dual(self):
    r"""
    Return the right dual with canonical map ι_R(v)(w) = b(w,v).
    
    This is the "column" interpretation of the bilinear form.
    For symmetric forms: right_dual() = left_dual().
    """

def tensor(self, other):
    r"""
    Return the tensor product (M₁ ⊗_R M₂, b₁ ⊗ b₂) of bilinear R-modules.
    
    The form on M₁ ⊗_R M₂ is given by:
    b₁ ⊗ b₂((v₁ ⊗ w₁), (v₂ ⊗ w₂)) = b₁(v₁, v₂) · b₂(w₁, w₂)
    
    INPUT:
    - other: Another bilinear R-module
    
    OUTPUT:
    The tensor product as a bilinear R-module.
    """

def direct_sum(self, other):
    r"""
    Return the direct sum (M₁ ⊕ M₂, b₁ ⊕ b₂) of bilinear R-modules.
    
    The form on M₁ ⊕ M₂ is given by:
    b₁ ⊕ b₂((v₁, w₁), (v₂, w₂)) = b₁(v₁, v₂) + b₂(w₁, w₂)
    
    INPUT:
    - other: Another bilinear R-module
    
    OUTPUT:
    The direct sum as a bilinear R-module.
    """
```

## Bilinear Form Structure

```python
def orthogonal_group(self):
    r"""
    Return the orthogonal group O(M) of form-preserving R-automorphisms.
    
    O(M) = {φ ∈ Aut_R(M) : b(φ(v), φ(w)) = b(v, w) for all v, w ∈ M}
    
    This is the subgroup of the R-automorphism group that preserves the bilinear form.
    """

def left_radical(self):
    r"""
    Return the left radical of the bilinear form.
    
    rad_L(M) = {v ∈ M : b(v, w) = 0 for all w ∈ M}
    
    This is the left kernel of the bilinear form.
    """

def right_radical(self):
    r"""
    Return the right radical of the bilinear form.
    
    rad_R(M) = {w ∈ M : b(v, w) = 0 for all v ∈ M}
    
    This is the right kernel of the bilinear form.
    For non-symmetric forms, this may differ from the left radical.
    """

def radical(self):
    r"""
    Return the radical of the bilinear form (left radical by convention).
    
    By mathematical convention, when 'radical' is used without qualification,
    it refers to the left radical: {v ∈ M : b(v, w) = 0 for all w ∈ M}.
    
    For symmetric forms, left and right radicals are identical.
    """
    return self.left_radical()

def nondegenerate_quotient(self):
    r"""
    Return the nondegenerate quotient M/rad(M).
    
    This is the standard construction in bilinear form theory to obtain
    the associated nondegenerate module from any bilinear module.
    The quotient inherits a well-defined nondegenerate bilinear form.
    
    This is the first step in structure theory (e.g., Witt decomposition).
    
    EXAMPLES::
    
        sage: # Degenerate form
        sage: M = BilinearModule(matrix(ZZ, [[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
        sage: M.discriminant()
        0
        sage: Q = M.nondegenerate_quotient()
        sage: Q.discriminant() != 0
        True
        sage: Q.rank()
        2
    
    OUTPUT:
    The nondegenerate quotient as a BilinearModule.
    """

## Additional Standard Operations

```python
def are_orthogonal(self, v, w):
    r"""
    Check if two vectors are orthogonal under the bilinear form.
    
    INPUT:
    - v, w: Elements of the R-module
    
    OUTPUT:
    True if b(v, w) = 0, False otherwise
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: v = M([1, 0])
        sage: w = M([0, 1])
        sage: M.are_orthogonal(v, w)
        False
        sage: M.bilinear_form(v, w)
        1
    """

def left_orthogonal_complement(self, W):
    r"""
    Return the left orthogonal complement of submodule W.
    
    W^⊥_L = {v ∈ M : b(v, w) = 0 for all w ∈ W}
    
    INPUT:
    - W: Submodule of this bilinear module
    
    OUTPUT:
    The left orthogonal complement as a submodule
    
    For symmetric forms, left and right orthogonal complements coincide.
    """

def right_orthogonal_complement(self, W):
    r"""
    Return the right orthogonal complement of submodule W.
    
    W^⊥_R = {v ∈ M : b(w, v) = 0 for all w ∈ W}
    
    INPUT:
    - W: Submodule of this bilinear module
    
    OUTPUT:
    The right orthogonal complement as a submodule
    
    For non-symmetric forms, this may differ from left_orthogonal_complement.
    """
```

## Form Classification and Invariants

```python
def rank(self):
    r"""
    Return the rank of the bilinear form.
    
    This is the rank of the Gram matrix, which equals the 
    dimension minus the dimension of the radical.
    
    OUTPUT:
    Integer rank of the bilinear form
    
    EXAMPLES::
    
        sage: # Nondegenerate form
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: M.rank()
        2
        sage: M.dimension()
        2
        
        sage: # Degenerate form
        sage: N = BilinearModule(matrix(ZZ, [[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
        sage: N.rank()
        2
        sage: N.dimension()
        3
    """

def is_nondegenerate(self):
    r"""
    Test if the bilinear form is nondegenerate.
    
    Equivalent to checking if radical() == {0}.
    
    OUTPUT:
    True if the form is nondegenerate, False otherwise
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: M.is_nondegenerate()
        True
        sage: M.discriminant()
        5
        
        sage: N = BilinearModule(matrix(ZZ, [[1, 0], [0, 0]]))
        sage: N.is_nondegenerate()
        False
        sage: N.discriminant()
        0
    """

def is_alternating(self):
    r"""
    Test if the bilinear form is alternating.
    
    A form is alternating if b(v, v) = 0 for all v ∈ M.
    This implies the form is skew-symmetric.
    
    OUTPUT:
    True if the form is alternating, False otherwise
    
    EXAMPLES::
    
        sage: # Alternating form (symplectic)
        sage: M = BilinearModule(matrix(ZZ, [[0, 1], [-1, 0]]))
        sage: M.is_alternating()
        True
        sage: M.is_skew_symmetric()
        True
        
        sage: # Skew-symmetric but not alternating (characteristic 2)
        sage: N = BilinearModule(matrix(GF(2), [[0, 1], [1, 1]]))
        sage: N.is_skew_symmetric()
        True
        sage: N.is_alternating()
        False
    """

def is_anisotropic(self):
    r"""
    Test if the form has no non-zero isotropic vectors.
    
    A form is anisotropic if there are no non-zero v with b(v, v) = 0.
    Equivalently, the Witt index is 0.
    
    OUTPUT:
    True if the form is anisotropic, False otherwise
    
    EXAMPLES::
    
        sage: # Positive definite form (anisotropic)
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 2]]))
        sage: M.is_anisotropic()
        True
        sage: M.witt_index()
        0
        
        sage: # Hyperbolic form (isotropic)
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: H.is_anisotropic()
        False
        sage: H.witt_index()
        1
    """

def witt_index(self):
    r"""
    Return the Witt index of the bilinear form.
    
    The Witt index is the dimension of the maximal totally isotropic submodule.
    This is a fundamental invariant of non-degenerate bilinear forms.
    
    OUTPUT:
    Non-negative integer Witt index
    
    EXAMPLES::
    
        sage: # Anisotropic form
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 2]]))
        sage: M.witt_index()
        0
        
        sage: # Hyperbolic plane
        sage: H = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: H.witt_index()
        1
        
        sage: # Symplectic form
        sage: S = BilinearModule(matrix(ZZ, [[0, 1, 0, 0], [-1, 0, 0, 0], 
        ....:                              [0, 0, 0, 1], [0, 0, -1, 0]]))
        sage: S.witt_index()
        2
        sage: S.dimension() // 2
        2
    """

def witt_decomposition(self):
    r"""
    Return the Witt decomposition of the form.
    
    Every non-degenerate bilinear form decomposes as:
    M ≅ M_anisotropic ⊥ (hyperbolic planes)
    
    OUTPUT:
    Tuple (anisotropic_part, hyperbolic_part) where the hyperbolic
    part is a direct sum of hyperbolic planes
    
    EXAMPLES::
    
        sage: # Form with both anisotropic and hyperbolic parts
        sage: M = BilinearModule(matrix(ZZ, [[1, 0, 0], [0, 0, 1], [0, 1, 0]]))
        sage: anis, hyp = M.witt_decomposition()
        sage: anis.is_anisotropic()
        True
        sage: hyp.witt_index()
        1
    """
```

## Submodule Operations

```python
def submodule(self, basis_vectors):
    r"""
    Create a submodule with the inherited bilinear form.
    
    INPUT:
    - basis_vectors: List of vectors that span the submodule
    
    OUTPUT:
    Submodule with restriction of the bilinear form
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1, 0], [1, 3, 1], [0, 1, 2]]))
        sage: v1 = M([1, 0, 0])
        sage: v2 = M([0, 1, 0])
        sage: S = M.submodule([v1, v2])
        sage: S.gram_matrix()
        [2 1]
        [1 3]
    """

def restrict_form_to_submodule(self, S):
    r"""
    Restrict the bilinear form to a submodule.
    
    For S ⊆ L, returns b|_{S×S}: S × S → R.
    
    INPUT:
    - S: Submodule of this bilinear module
    
    OUTPUT:
    The restricted bilinear form on S
    
    EXAMPLES::
    
        sage: L = BilinearModule(matrix(ZZ, [[2, 1, 0], [1, 3, 1], [0, 1, 2]]))
        sage: S = L.submodule([L([1, 0, 0]), L([0, 1, 0])])
        sage: b_S = L.restrict_form_to_submodule(S)
        sage: b_S.matrix()
        [2 1]
        [1 3]
    """

def quotient_by_submodule(self, S):
    r"""
    Return the quotient module L/S with induced bilinear form.
    
    The form on L/S is defined by b̄([v], [w]) = b(v, w).
    This is well-defined iff S ⊆ S^⊥ (S is isotropic).
    
    INPUT:
    - S: Submodule to quotient by
    
    OUTPUT:
    Quotient bilinear module L/S
    
    EXAMPLES::
    
        sage: # Quotient by isotropic submodule
        sage: L = BilinearModule(matrix(ZZ, [[0, 1, 0], [1, 0, 0], [0, 0, 2]]))
        sage: v = L([1, 1, 0])  # Isotropic: v*v = 0
        sage: S = L.submodule([v])
        sage: assert S.is_isotropic()
        sage: Q = L.quotient_by_submodule(S)
        sage: Q.rank()
        2
        
        sage: # Non-isotropic submodule - form may not descend
        sage: w = L([0, 0, 1])  # Not isotropic: w*w = 2
        sage: T = L.submodule([w])
        sage: try:
        ....:     L.quotient_by_submodule(T)
        ....: except ValueError as e:
        ....:     print("Form does not descend to quotient")
    """

def is_isotropic_submodule(self, S):
    r"""
    Test if a submodule is isotropic (contained in its orthogonal complement).
    
    S is isotropic iff S ⊆ S^⊥, equivalently b(s₁, s₂) = 0 for all s₁, s₂ ∈ S.
    
    INPUT:
    - S: Submodule to test
    
    OUTPUT:
    True if S is isotropic, False otherwise
    
    EXAMPLES::
    
        sage: L = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: # Diagonal subspace is isotropic
        sage: S = L.submodule([L([1, 1])])
        sage: L.is_isotropic_submodule(S)
        True
        sage: # Anti-diagonal is not
        sage: T = L.submodule([L([1, -1])])
        sage: L.is_isotropic_submodule(T)
        False
    """
```

## Basis Transformations

```python
def change_basis(self, P):
    r"""
    Transform to a new basis with transformation matrix P.
    
    For bilinear forms, this conjugates the Gram matrix: G' = P^T G P
    
    INPUT:
    - P: Invertible matrix representing the basis change
    
    OUTPUT:
    New bilinear module with transformed basis
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: P = matrix(ZZ, [[1, 1], [0, 1]])
        sage: M_new = M.change_basis(P)
        sage: M_new.gram_matrix()
        [2 3]
        [3 5]
        sage: P.T * M.gram_matrix() * P
        [2 3]
        [3 5]
    """
```

## Symmetric Monoidal Category Structure

```python
class BilinearModulesCategory(Category):
    r"""
    The category of bilinear modules over a ring R.
    
    This is a symmetric monoidal category via the fibration:
    BilinearModules → R-Modules × BilinearForms
    
    The tensor product of (L₁, b₁) and (L₂, b₂) is:
    (L₁ ⊗_R L₂, b₁ ⊗ b₂)
    
    where the module tensor is over R and the form tensor is the induced form.
    
    EXAMPLES::
    
        sage: BilMod = BilinearModulesCategory(ZZ)
        sage: BilMod in SymmetricMonoidalCategories()
        True
        
        sage: # Hyperbolic plane and positive definite form
        sage: H.<e, f> = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: P.<u> = BilinearModule(matrix(ZZ, [[2]]))
        
        sage: # Tensor product: (H ⊗ P, b_H ⊗ b_P)
        sage: T = H.tensor_product(P)
        sage: T.dimension()
        2
        sage: # Basis: e⊗u, f⊗u
        sage: # Form: hyperbolic scaled by 2
        sage: T.gram_matrix()
        [0 2]
        [2 0]
        
        sage: # Unit object: (R, scalar multiplication)
        sage: I = BilMod.tensor_unit()
        sage: I.dimension()
        1
        sage: I.gram_matrix()
        [1]
    """
    
    def __init__(self, base_ring):
        """Initialize the category of bilinear modules over base_ring."""
        self._base_ring = base_ring
        Category.__init__(self)
    
    def super_categories(self):
        """
        Return the super categories.
        
        Bilinear modules form a symmetric monoidal category.
        """
        from sage.categories.symmetric_monoidal_categories import SymmetricMonoidalCategories
        from sage.categories.modules import Modules
        return [SymmetricMonoidalCategories(), Modules(self._base_ring)]
    
    def base_ring(self):
        """Return the base ring."""
        return self._base_ring
    
    class ParentMethods:
        """
        Methods for bilinear modules as objects in a symmetric monoidal category.
        """
        
        def tensor_product(self, *others):
            r"""
            Return the tensor product of bilinear modules.
            
            For bilinear modules (L₁, b₁) and (L₂, b₂), returns:
            (L₁ ⊗_R L₂, b₁ ⊗ b₂)
            
            The module structure is the usual tensor product over R.
            The bilinear form is given by:
            b((v₁⊗w₁), (v₂⊗w₂)) = b₁(v₁,v₂) · b₂(w₁,w₂)
            
            EXAMPLES::
            
                sage: # Standard basis forms
                sage: L1.<e1, e2> = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
                sage: L2.<f> = BilinearModule(matrix(ZZ, [[3]]))
                
                sage: # Tensor product
                sage: T = L1.tensor_product(L2)
                sage: T.dimension()
                2
                sage: # Basis: e1⊗f, e2⊗f
                sage: T.gram_matrix()
                [3 0]
                [0 3]
                
                sage: # Non-symmetric example
                sage: M.<u, v> = BilinearModule(matrix(ZZ, [[1, 2], [3, 4]]))
                sage: N.<w> = BilinearModule(matrix(ZZ, [[-1]]))
                sage: MN = M.tensor_product(N)
                sage: MN.gram_matrix()
                [-1 -2]
                [-3 -4]
            """
            if hasattr(self, 'tensor'):
                # Use existing tensor method from the module interface
                if len(others) == 1:
                    return self.tensor(others[0])
                else:
                    result = self
                    for other in others:
                        result = result.tensor(other)
                    return result
            else:
                raise NotImplementedError("tensor_product requires tensor method")
        
        def tensor_unit(self):
            r"""
            Return the unit object for tensor products.
            
            The unit is (R, b) where R is the base ring as a rank-1 free module
            and b is the standard multiplication form: b(r,s) = r·s.
            
            OUTPUT:
            The unit bilinear module
            
            EXAMPLES::
            
                sage: BilMod = BilinearModulesCategory(ZZ)
                sage: I = BilMod.tensor_unit()
                sage: I.dimension()
                1
                sage: I.gram_matrix()
                [1]
                
                sage: # Unit property: I ⊗ L ≅ L
                sage: L = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I_tensor_L = I.tensor_product(L)
                sage: I_tensor_L.is_isomorphic_to(L)
                True
            """
            from sage.matrix.constructor import matrix
            return BilinearModule(matrix(self.base_ring(), [[1]]))
        
        def associator(self, B, C):
            r"""
            Return the associator isomorphism (A⊗B)⊗C ≅ A⊗(B⊗C).
            
            This is the module isomorphism that preserves bilinear forms.
            The underlying module associator is the standard one for R-modules.
            
            INPUT:
            - ``B``, ``C`` -- other bilinear modules
            
            OUTPUT:
            Associator isomorphism in BilR-Mod
            
            EXAMPLES::
            
                sage: A.<a> = BilinearModule(matrix(ZZ, [[1]]))
                sage: B.<b> = BilinearModule(matrix(ZZ, [[2]]))
                sage: C.<c> = BilinearModule(matrix(ZZ, [[3]]))
                
                sage: # Two ways to tensor three modules
                sage: AB_C = (A.tensor_product(B)).tensor_product(C)
                sage: A_BC = A.tensor_product(B.tensor_product(C))
                
                sage: # Associator provides the isomorphism
                sage: alpha = A.associator(B, C)
                sage: assert alpha.domain() == AB_C
                sage: assert alpha.codomain() == A_BC
                sage: assert alpha.is_isometry()  # Preserves forms
                sage: assert alpha.is_isomorphism()
                
                sage: # Map basis elements
                sage: # (a⊗b)⊗c ↦ a⊗(b⊗c)
                sage: alpha((a.tensor(b)).tensor(c)) == a.tensor(b.tensor(c))
                True
            """
            AB = self.tensor_product(B)
            BC = B.tensor_product(C)
            AB_C = AB.tensor_product(C)
            A_BC = self.tensor_product(BC)
            
            # The standard module associator preserves the tensor product form
            return BilinearModuleAssociator(AB_C, A_BC)
        
        def left_unitor(self):
            r"""
            Return the left unitor isomorphism I⊗A ≅ A.
            
            OUTPUT:
            Left unitor isomorphism in BilR-Mod
            
            EXAMPLES::
            
                sage: L.<e1, e2> = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I = L.parent().tensor_unit()
                
                sage: lambda_L = L.left_unitor()
                sage: assert lambda_L.domain() == I.tensor_product(L)
                sage: assert lambda_L.codomain() == L
                sage: assert lambda_L.is_isometry()
                
                sage: # Maps basis: 1⊗e_i ↦ e_i
                sage: one = I.basis()[0]
                sage: lambda_L(one.tensor(e1)) == e1
                True
                sage: lambda_L(one.tensor(e2)) == e2
                True
            """
            I = self.parent().tensor_unit()
            I_self = I.tensor_product(self)
            return BilinearModuleLeftUnitor(I_self, self)
        
        def right_unitor(self):
            r"""
            Return the right unitor isomorphism A⊗I ≅ A.
            
            OUTPUT:
            Right unitor isomorphism in BilR-Mod
            
            EXAMPLES::
            
                sage: L.<e1, e2> = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
                sage: I = L.parent().tensor_unit()
                
                sage: rho_L = L.right_unitor()
                sage: assert rho_L.domain() == L.tensor_product(I)
                sage: assert rho_L.codomain() == L
                sage: assert rho_L.is_isometry()
                
                sage: # Maps basis: e_i⊗1 ↦ e_i
                sage: one = I.basis()[0]
                sage: rho_L(e1.tensor(one)) == e1
                True
                sage: rho_L(e2.tensor(one)) == e2
                True
            """
            I = self.parent().tensor_unit()
            self_I = self.tensor_product(I)
            return BilinearModuleRightUnitor(self_I, self)
        
        def braiding(self, B):
            r"""
            Return the braiding isomorphism A⊗B ≅ B⊗A.
            
            This swaps tensor factors while preserving the bilinear form.
            
            INPUT:
            - ``B`` -- another bilinear module
            
            OUTPUT:
            Braiding isomorphism in BilR-Mod
            
            EXAMPLES::
            
                sage: L1.<e1, e2> = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))
                sage: L2.<f> = BilinearModule(matrix(ZZ, [[2]]))
                
                sage: beta = L1.braiding(L2)
                sage: assert beta.domain() == L1.tensor_product(L2)
                sage: assert beta.codomain() == L2.tensor_product(L1)
                sage: assert beta.is_isometry()
                
                sage: # Maps basis: e_i⊗f ↦ f⊗e_i
                sage: beta(e1.tensor(f)) == f.tensor(e1)
                True
                sage: beta(e2.tensor(f)) == f.tensor(e2)
                True
                
                sage: # Verify symmetry: β_{B,A} ∘ β_{A,B} = id
                sage: beta_inv = L2.braiding(L1)
                sage: composition = beta.compose(beta_inv)
                sage: composition.is_identity()
                True
            """
            A_tensor_B = self.tensor_product(B)
            B_tensor_A = B.tensor_product(self)
            return BilinearModuleBraiding(A_tensor_B, B_tensor_A)

    class MorphismMethods:
        """
        Tensor products of morphisms in the symmetric monoidal category.
        """
        
        def tensor_with(self, other):
            r"""
            Return the tensor product of morphisms.
            
            For φ: L₁ → L₂ and ψ: M₁ → M₂, returns φ ⊗ ψ: L₁⊗M₁ → L₂⊗M₂.
            
            INPUT:
            - ``other`` -- another morphism in BilR-Mod
            
            OUTPUT:
            Tensor product morphism
            
            EXAMPLES::
            
                sage: L1 = BilinearModule(matrix(ZZ, [[1]]))
                sage: L2 = BilinearModule(matrix(ZZ, [[2]]))
                sage: M1 = BilinearModule(matrix(ZZ, [[3]]))
                sage: M2 = BilinearModule(matrix(ZZ, [[4]]))
                
                sage: phi = L1.hom(L2, {L1.0: 2*L2.0})  # Scaling by 2
                sage: psi = M1.hom(M2, {M1.0: M2.0})    # Identity
                
                sage: tensor_morph = phi.tensor_with(psi)
                sage: assert tensor_morph.domain() == L1.tensor_product(M1)
                sage: assert tensor_morph.codomain() == L2.tensor_product(M2)
                sage: assert tensor_morph.is_isometry()  # If both preserve forms
            """
            # Implementation would tensor the underlying module morphisms
            raise NotImplementedError("tensor_with for morphisms")
```