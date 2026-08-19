<!--
Origin: gitclones/Coxeter/implementation/planning/BilRMod/structures/tensor_product_structure.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Structure: Tensor Product for Bilinear Modules

Tensor product monoidal structure for bilinear modules with bilinear form compatibility.

## Tensor Product Definition

```python
def tensor_product_bilinear(M1, M2):
    """
    Tensor product of bilinear modules.
    
    For bilinear modules (M₁, b₁) and (M₂, b₂), the tensor product
    (M₁ ⊗ M₂, b₁ ⊗ b₂) has bilinear form:
    
    (b₁ ⊗ b₂)(v₁ ⊗ w₁, v₂ ⊗ w₂) = b₁(v₁, v₂) · b₂(w₁, w₂)
    
    The Gram matrix is the Kronecker product: G₁ ⊗ G₂.
    
    INPUT:
    - M1, M2 -- bilinear modules over the same base ring
    
    OUTPUT:
    BilinearModule representing M₁ ⊗ M₂
    
    EXAMPLES::
    
        sage: # Tensor product of positive definite forms
        sage: G1 = matrix(QQ, [[2]])
        sage: G2 = matrix(QQ, [[3]])
        sage: M1 = BilinearModule(G1)
        sage: M2 = BilinearModule(G2)
        sage: M = tensor_product_bilinear(M1, M2)
        sage: M.gram_matrix()
        [6]
        sage: M.is_positive_definite()
        True
        
        sage: # Higher dimensional example
        sage: G1 = matrix(QQ, [[1, 0], [0, -1]])  # Hyperbolic
        sage: G2 = matrix(QQ, [[2]])              # Positive
        sage: M1 = BilinearModule(G1)
        sage: M2 = BilinearModule(G2)
        sage: M = tensor_product_bilinear(M1, M2)
        sage: M.gram_matrix()
        [2  0]
        [0 -2]
        sage: M.signature()
        (1, 1, 0)  # Still hyperbolic
    """
    if M1.base_ring() != M2.base_ring():
        raise ValueError("Base rings must match for tensor product")
    
    # Compute Kronecker product of Gram matrices
    G1 = M1.gram_matrix()
    G2 = M2.gram_matrix()
    G_tensor = G1.kronecker_product(G2)
    
    # Create basis names for tensor product
    basis_names = []
    for b1 in M1._basis_keys:
        for b2 in M2._basis_keys:
            basis_names.append(f"{b1}⊗{b2}")
    
    return BilinearModule(G_tensor, basis=basis_names)
```

## Monoidal Category Structure

```python
class BilinearTensorProduct:
    """
    Tensor product functor for bilinear modules.
    
    This makes BilinearModules(R) into a monoidal category with:
    - Tensor product: ⊗
    - Unit object: R with trivial bilinear form
    - Associativity and unit constraints
    """
    
    @staticmethod
    def unit_object(base_ring):
        """
        Unit object for tensor product monoidal structure.
        
        This is the base ring R viewed as a rank-1 bilinear module
        with Gram matrix [1].
        
        EXAMPLES::
        
            sage: I = BilinearTensorProduct.unit_object(QQ)
            sage: I.rank()
            1
            sage: I.gram_matrix()
            [1]
        """
        from sage.matrix.constructor import matrix
        unit_gram = matrix(base_ring, [[1]])
        return BilinearModule(unit_gram, basis=['1'])
    
    @staticmethod
    def associator(M1, M2, M3):
        """
        Associativity isomorphism: (M₁ ⊗ M₂) ⊗ M₃ ≅ M₁ ⊗ (M₂ ⊗ M₃).
        
        This is a natural isomorphism of bilinear modules.
        """
        # Left association: (M1 ⊗ M2) ⊗ M3
        left = tensor_product_bilinear(tensor_product_bilinear(M1, M2), M3)
        
        # Right association: M1 ⊗ (M2 ⊗ M3)
        right = tensor_product_bilinear(M1, tensor_product_bilinear(M2, M3))
        
        # The isomorphism is given by rearranging tensor factors
        # Implementation would construct explicit isomorphism
        return BilinearModuleIsomorphism(left, right, 
                                       associativity_isomorphism=True)
    
    @staticmethod
    def left_unitor(M):
        """
        Left unit isomorphism: I ⊗ M ≅ M.
        """
        base_ring = M.base_ring()
        I = BilinearTensorProduct.unit_object(base_ring)
        I_tensor_M = tensor_product_bilinear(I, M)
        
        # Natural isomorphism dropping the unit factor
        return BilinearModuleIsomorphism(I_tensor_M, M, unit_isomorphism=True)
    
    @staticmethod
    def right_unitor(M):
        """
        Right unit isomorphism: M ⊗ I ≅ M.
        """
        base_ring = M.base_ring()
        I = BilinearTensorProduct.unit_object(base_ring)
        M_tensor_I = tensor_product_bilinear(M, I)
        
        return BilinearModuleIsomorphism(M_tensor_I, M, unit_isomorphism=True)
```

## Properties of Tensor Products

```python
def tensor_product_properties(M1, M2):
    """
    Analyze properties of tensor product bilinear form.
    
    The tensor product interacts with form properties in specific ways:
    - Signatures multiply: sig(M₁ ⊗ M₂) = sig(M₁) × sig(M₂)
    - Discriminants multiply: disc(M₁ ⊗ M₂) = disc(M₁)^r₂ · disc(M₂)^r₁
    - Definiteness: both positive ⇒ tensor positive
    - Symmetry: both symmetric ⇒ tensor symmetric
    
    INPUT:
    - M1, M2 -- bilinear modules
    
    OUTPUT:
    Dictionary of tensor product properties
    """
    M = tensor_product_bilinear(M1, M2)
    
    properties = {}
    
    # Signature computation
    if hasattr(M1, 'signature') and hasattr(M2, 'signature'):
        sig1 = M1.signature()
        sig2 = M2.signature()
        # (p₁,q₁,r₁) × (p₂,q₂,r₂) gives:
        expected_sig = (
            sig1[0] * sig2[0] + sig1[1] * sig2[1],  # + eigenvalues  
            sig1[0] * sig2[1] + sig1[1] * sig2[0],  # - eigenvalues
            sig1[0] * sig2[2] + sig1[1] * sig2[2] + sig1[2] * (sig2[0] + sig2[1] + sig2[2])
        )
        actual_sig = M.signature()
        properties['signature_formula'] = (expected_sig == actual_sig)
    
    # Discriminant formula
    disc1 = M1.discriminant()
    disc2 = M2.discriminant()
    expected_disc = disc1 ** M2.rank() * disc2 ** M1.rank()
    actual_disc = M.discriminant()
    properties['discriminant_formula'] = (expected_disc == actual_disc)
    
    # Symmetry preservation
    if M1.is_symmetric() and M2.is_symmetric():
        properties['symmetry_preserved'] = M.is_symmetric()
    
    # Definiteness
    if M1.is_positive_definite() and M2.is_positive_definite():
        properties['definiteness_preserved'] = M.is_positive_definite()
    
    return properties

def tensor_power(M, n):
    """
    n-fold tensor product M^⊗n.
    
    INPUT:
    - M -- bilinear module
    - n -- positive integer
    
    OUTPUT:
    BilinearModule representing M ⊗ M ⊗ ... ⊗ M (n factors)
    
    EXAMPLES::
    
        sage: # Square of hyperbolic plane
        sage: H = HyperbolicPlane()
        sage: H2 = tensor_power(H, 2)
        sage: H2.signature()
        (2, 2, 0)  # Two hyperbolic planes
        
        sage: # Cube of positive definite form
        sage: G = matrix(QQ, [[2]])
        sage: M = BilinearModule(G)
        sage: M3 = tensor_power(M, 3)
        sage: M3.discriminant()
        8  # 2^3
    """
    if n == 0:
        return BilinearTensorProduct.unit_object(M.base_ring())
    elif n == 1:
        return M
    else:
        result = M
        for i in range(n - 1):
            result = tensor_product_bilinear(result, M)
        return result
```

## External Tensor Products

```python
def external_tensor_product(M1, M2):
    """
    External tensor product (different from internal tensor product).
    
    For modules over different rings R₁, R₂, the external tensor
    product is over R₁ ⊗ R₂.
    
    This is more general than the internal tensor product for
    modules over the same ring.
    """
    # Would require implementation of ring tensor products
    raise NotImplementedError("External tensor products")

def tensor_product_with_ring_extension(M, field_extension):
    """
    Tensor with field extension: M ⊗_R K for ring extension R ⊆ K.
    
    This extends scalars while preserving bilinear form structure.
    
    INPUT:
    - M -- bilinear module over R
    - field_extension -- field K containing R
    
    OUTPUT:
    BilinearModule over K
    
    EXAMPLES::
    
        sage: # Extend rational form to reals
        sage: G = matrix(QQ, [[1, 0], [0, -1]])
        sage: M = BilinearModule(G)
        sage: # M_R = tensor_product_with_ring_extension(M, RR)
        sage: # M_R.base_ring() == RR
    """
    # Change base ring of Gram matrix
    extended_gram = field_extension(M.gram_matrix())
    return BilinearModule(extended_gram, base_ring=field_extension)
```

## Compatibility with Other Structures

```python
def tensor_product_compatibility():
    """
    Tensor products interact well with other bilinear module structures:
    
    1. Direct sum: (M₁ ⊕ M₂) ⊗ N ≅ (M₁ ⊗ N) ⊕ (M₂ ⊗ N)
    2. Duality: (M₁ ⊗ M₂)* ≅ M₁* ⊗ M₂*
    3. Quotients: (M/N) ⊗ P ≅ (M ⊗ P)/(N ⊗ P) when N ⊗ P is well-defined
    4. Orthogonal complements: (N⊥)^⊗k ⊆ (N^⊗k)⊥
    """
    pass

def braiding_isomorphism(M1, M2):
    """
    Braiding isomorphism: M₁ ⊗ M₂ ≅ M₂ ⊗ M₁.
    
    For symmetric bilinear forms, this is always an isometry.
    For skew-symmetric forms, may introduce sign changes.
    
    INPUT:
    - M1, M2 -- bilinear modules
    
    OUTPUT:
    BilinearModuleIsomorphism representing the braiding
    """
    # The braiding permutes tensor factors
    # For bilinear forms: b₁ ⊗ b₂ ↦ b₂ ⊗ b₁
    
    left = tensor_product_bilinear(M1, M2)
    right = tensor_product_bilinear(M2, M1)
    
    # Construct permutation matrix for basis elements
    # Implementation would create explicit permutation
    return BilinearModuleIsomorphism(left, right, braiding=True)

def symmetrizer(M, n):
    """
    Symmetrizer operator on n-fold tensor product.
    
    Projects M^⊗n onto symmetric tensors Sym^n(M).
    
    INPUT:
    - M -- bilinear module
    - n -- tensor power
    
    OUTPUT:
    Projection operator
    """
    M_tensor_n = tensor_power(M, n)
    
    # Symmetrizer is (1/n!) * Σ_{σ ∈ Sₙ} σ
    # where σ acts by permuting tensor factors
    
    from sage.combinat.permutation import Permutations
    from fractions import Fraction
    
    # This would sum over all permutations
    # Implementation requires permutation action on tensor products
    raise NotImplementedError("Symmetrizer operator")

def alternator(M, n):
    """
    Alternator operator on n-fold tensor product.
    
    Projects M^⊗n onto alternating tensors ∧^n(M).
    """
    # Alternator is (1/n!) * Σ_{σ ∈ Sₙ} sgn(σ) σ
    raise NotImplementedError("Alternator operator")
```

## Mathematical Properties

The tensor product structure satisfies these mathematical properties:

```python
# Mathematical assertion: Tensor product bilinear form
# (b₁ ⊗ b₂)(v₁ ⊗ w₁, v₂ ⊗ w₂) = b₁(v₁, v₂) · b₂(w₁, w₂)

# Mathematical assertion: Gram matrix formula
# If G₁, G₂ are Gram matrices, then G₁ ⊗ G₂ is Gram matrix of tensor product

# Mathematical assertion: Signature multiplicativity
# sig(M₁ ⊗ M₂) follows specific formula based on sig(M₁), sig(M₂)

# Mathematical assertion: Discriminant formula
# disc(M₁ ⊗ M₂) = disc(M₁)^(rank M₂) · disc(M₂)^(rank M₁)

# Mathematical assertion: Monoidal category axioms
# Tensor product is associative, unital, with natural isomorphisms

# Mathematical assertion: Braiding compatibility
# For symmetric forms, braiding is always an isometry

# Mathematical assertion: Distributivity over direct sum
# (M₁ ⊕ M₂) ⊗ N ≅ (M₁ ⊗ N) ⊕ (M₂ ⊗ N)

# Mathematical assertion: Functoriality
# Tensor product preserves isomorphisms and exact sequences
```

This tensor product structure provides the monoidal category foundation for bilinear modules while preserving all bilinear form properties and enabling multilinear algebra constructions.