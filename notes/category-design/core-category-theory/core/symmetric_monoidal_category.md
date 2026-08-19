<!--
Origin: gitclones/Coxeter/implementation/planning/core/symmetric_monoidal_category.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: SymmetricMonoidalCategory

Base class for symmetric monoidal categories, providing tensor products with coherent natural isomorphisms.

## Tensor Structure Methods

```python
def tensor_product(self, *others):
    r"""
    Return the tensor product of objects.
    
    The tensor product ⊗ is a bifunctor C × C → C that provides
    the monoidal structure. For multiple arguments, associates to the left.
    
    INPUT:
    - ``others`` -- objects to tensor with this one
    
    OUTPUT:
    The tensor product object
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 2)
        sage: W = VectorSpace(QQ, 3)
        sage: V_tensor_W = V.tensor_product(W)
        sage: V_tensor_W.dimension()
        6  # dim(V ⊗ W) = dim(V) × dim(W)
        
        sage: # Multiple tensor products
        sage: U = VectorSpace(QQ, 1)
        sage: VWU = V.tensor_product(W, U)
        sage: VWU.dimension()
        6  # (2 × 3) × 1 = 6
        
        sage: # Functoriality: morphisms tensor
        sage: f = V.hom(matrix([[2, 0], [0, 3]]))
        sage: g = W.hom(matrix([[1, 0, 0], [0, 2, 0], [0, 0, 1]]))
        sage: f_tensor_g = f.tensor_product(g)
        sage: f_tensor_g.matrix().nrows()
        6  # 2 × 3 = 6
    """

def tensor_unit(self):
    r"""
    Return the unit object for tensor products.
    
    The unit object I satisfies the left and right unit laws:
    I ⊗ A ≅ A ≅ A ⊗ I for all objects A.
    
    OUTPUT:
    The tensor unit object
    
    EXAMPLES::
    
        sage: from sage.categories.modules import Modules
        sage: Mod_QQ = Modules(QQ)
        sage: I = Mod_QQ.tensor_unit()
        sage: I.dimension()
        1  # QQ as 1-dimensional vector space
        
        sage: # Unit laws
        sage: V = VectorSpace(QQ, 3)
        sage: I_tensor_V = I.tensor_product(V)
        sage: I_tensor_V.dimension()
        3  # I ⊗ V ≅ V
        
        sage: V_tensor_I = V.tensor_product(I)
        sage: V_tensor_I.dimension()
        3  # V ⊗ I ≅ V
    """

## Coherence Isomorphisms

```python
def associator(self, B, C):
    r"""
    Return the associator isomorphism (A⊗B)⊗C → A⊗(B⊗C).
    
    The associator provides canonical reassociation of tensor products,
    making the monoidal structure associative up to isomorphism.
    
    INPUT:
    - ``B``, ``C`` -- other objects in the category
    
    OUTPUT:
    Natural isomorphism α: (self⊗B)⊗C → self⊗(B⊗C)
    
    EXAMPLES::
    
        sage: A = VectorSpace(QQ, 2)
        sage: B = VectorSpace(QQ, 3)
        sage: C = VectorSpace(QQ, 1)
        
        sage: # Different associations have same dimension
        sage: AB_C = (A.tensor_product(B)).tensor_product(C)
        sage: A_BC = A.tensor_product(B.tensor_product(C))
        sage: AB_C.dimension() == A_BC.dimension()
        True
        
        sage: # Associator provides canonical isomorphism
        sage: alpha = A.associator(B, C)
        sage: alpha.is_isomorphism()
        True
        
        sage: # Maps (v ⊗ w) ⊗ u ↦ v ⊗ (w ⊗ u)
        sage: v = A.basis()[0]
        sage: w = B.basis()[0]  
        sage: u = C.basis()[0]
        sage: # alpha((v ⊗ w) ⊗ u) == v ⊗ (w ⊗ u)
    """

def left_unitor(self):
    r"""
    Return the left unitor isomorphism I⊗A → A.
    
    The left unitor identifies tensoring with the unit on the left
    with the object itself, implementing the left unit law.
    
    OUTPUT:
    Natural isomorphism λ: I⊗self → self
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 3)
        sage: lambda_V = V.left_unitor()
        sage: lambda_V.is_isomorphism()
        True
        
        sage: # Check domains and codomains
        sage: I = V.parent().tensor_unit()  # QQ^1
        sage: I_tensor_V = I.tensor_product(V)
        sage: lambda_V.domain() == I_tensor_V
        True
        sage: lambda_V.codomain() == V
        True
        
        sage: # Maps 1 ⊗ v ↦ v
        sage: v = V.basis()[0]
        sage: one = I.basis()[0]
        sage: # lambda_V(one ⊗ v) == v
    """

def right_unitor(self):
    r"""
    Return the right unitor isomorphism A⊗I → A.
    
    The right unitor identifies tensoring with the unit on the right
    with the object itself, implementing the right unit law.
    
    OUTPUT:
    Natural isomorphism ρ: self⊗I → self
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 3)
        sage: rho_V = V.right_unitor()
        sage: rho_V.is_isomorphism()
        True
        
        sage: # Check domains and codomains
        sage: I = V.parent().tensor_unit()  # QQ^1
        sage: V_tensor_I = V.tensor_product(I)
        sage: rho_V.domain() == V_tensor_I
        True
        sage: rho_V.codomain() == V
        True
        
        sage: # Maps v ⊗ 1 ↦ v
        sage: v = V.basis()[0]
        sage: one = I.basis()[0]
        sage: # rho_V(v ⊗ one) == v
    """

def braiding(self, B):
    r"""
    Return the braiding isomorphism A⊗B → B⊗A.
    
    The braiding swaps tensor factors, providing the symmetric
    structure. In a symmetric monoidal category, β_{B,A} ∘ β_{A,B} = id.
    
    INPUT:
    - ``B`` -- another object in the category
    
    OUTPUT:
    Natural isomorphism β: self⊗B → B⊗self
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 2)
        sage: W = VectorSpace(QQ, 3)
        
        sage: beta_VW = V.braiding(W)
        sage: beta_VW.is_isomorphism()
        True
        
        sage: # Check domains and codomains
        sage: VW = V.tensor_product(W)
        sage: WV = W.tensor_product(V)
        sage: beta_VW.domain() == VW
        True
        sage: beta_VW.codomain() == WV
        True
        
        sage: # Symmetry property
        sage: beta_WV = W.braiding(V)
        sage: composition = beta_WV * beta_VW
        sage: composition.is_identity()
        True
        
        sage: # Maps v ⊗ w ↦ w ⊗ v  
        sage: v = V.basis()[0]
        sage: w = W.basis()[0]
        sage: # beta_VW(v ⊗ w) == w ⊗ v
    """
```

## Functoriality Methods

```python
def tensor_product_morphisms(self, other):
    r"""
    Return the tensor product of morphisms.
    
    For morphisms f: A → B and g: C → D, returns f⊗g: A⊗C → B⊗D.
    This implements the bifunctoriality of the tensor product.
    
    INPUT:
    - ``other`` -- another morphism
    
    OUTPUT:
    The tensor product morphism f⊗g
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 2)
        sage: W = VectorSpace(QQ, 3)
        sage: f = V.hom(matrix([[2, 0], [0, 3]]))  # Scaling
        sage: g = W.hom(matrix([[1, 0, 0], [0, 2, 0], [0, 0, 1]]))
        
        sage: h = f.tensor_product(g)
        sage: h.domain() == V.tensor_product(W)
        True
        sage: h.codomain() == V.tensor_product(W)
        True
        
        sage: # Verify functoriality
        sage: # (f⊗g) ∘ (f'⊗g') = (f∘f') ⊗ (g∘g')
        sage: f_prime = V.hom(matrix([[1, 1], [0, 1]]))
        sage: g_prime = W.hom(matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]))
        sage: 
        sage: left_side = (f * f_prime).tensor_product(g * g_prime)
        sage: right_side = f.tensor_product(g) * f_prime.tensor_product(g_prime)
        sage: left_side == right_side
        True
    """

def is_symmetric_monoidal(self):
    r"""
    Test if this category is symmetric monoidal.
    
    Returns True if the category has tensor products with natural
    isomorphisms satisfying the coherence axioms.
    
    OUTPUT:
    Boolean indicating symmetric monoidal structure
    
    EXAMPLES::
    
        sage: from sage.categories.modules import Modules
        sage: Modules(QQ).is_symmetric_monoidal()
        True
        
        sage: from sage.categories.vector_spaces import VectorSpaces  
        sage: VectorSpaces(QQ).is_symmetric_monoidal()
        True
        
        sage: # Bilinear forms category is symmetric monoidal
        sage: # with tensor product of forms
    """
```

## Coherence Verification Methods

```python
def verify_pentagon_axiom(self, B, C, D):
    r"""
    Verify the pentagon axiom for associativity coherence.
    
    Checks that the pentagon diagram commutes for the given objects,
    ensuring that different ways of reassociating 4-fold tensor products
    yield the same result via associators.
    
    INPUT:
    - ``B``, ``C``, ``D`` -- three other objects in the category
    
    OUTPUT:
    Boolean indicating if the pentagon commutes
    
    EXAMPLES::
    
        sage: # For vector spaces, pentagon always commutes
        sage: A = VectorSpace(QQ, 1)
        sage: B = VectorSpace(QQ, 1)
        sage: C = VectorSpace(QQ, 1)
        sage: D = VectorSpace(QQ, 1)
        sage: A.verify_pentagon_axiom(B, C, D)
        True
        
        sage: # Check with different dimensions
        sage: A = VectorSpace(QQ, 2)
        sage: B = VectorSpace(QQ, 3)
        sage: C = VectorSpace(QQ, 1)
        sage: D = VectorSpace(QQ, 2)
        sage: A.verify_pentagon_axiom(B, C, D)
        True
    
    ALGORITHM:
    Computes both paths around the pentagon and verifies they are equal.
    Path 1: ((A⊗B)⊗C)⊗D → (A⊗B)⊗(C⊗D) → A⊗(B⊗(C⊗D))
    Path 2: ((A⊗B)⊗C)⊗D → (A⊗(B⊗C))⊗D → A⊗((B⊗C)⊗D)
    """

def verify_triangle_axiom(self, B):
    r"""
    Verify the triangle axiom for unit coherence.
    
    Checks that associator and unitors are compatible by verifying
    the triangle diagram commutes.
    
    INPUT:
    - ``B`` -- another object in the category
    
    OUTPUT:
    Boolean indicating if the triangle commutes
    
    EXAMPLES::
    
        sage: A = VectorSpace(QQ, 2)
        sage: B = VectorSpace(QQ, 3)
        sage: A.verify_triangle_axiom(B)
        True
        
        sage: # Works for any objects in symmetric monoidal category
        sage: from sage.categories.modules import Modules
        sage: M = Modules(ZZ)
        sage: A = ZZ^2
        sage: B = ZZ^3
        sage: A.verify_triangle_axiom(B)
        True
    
    ALGORITHM:
    Verifies that: (A⊗I)⊗B → A⊗(I⊗B) → A⊗B equals (A⊗I)⊗B → A⊗B
    via right unitor on A tensored with identity on B.
    """

def verify_hexagon_axioms(self, B, C):
    r"""
    Verify the hexagon axioms for braiding coherence.
    
    Checks that braiding is compatible with associator by verifying
    both hexagon diagrams commute.
    
    INPUT:
    - ``B``, ``C`` -- two other objects in the category
    
    OUTPUT:
    Tuple (hex1, hex2) of booleans for both hexagons
    
    EXAMPLES::
    
        sage: A = VectorSpace(QQ, 1)
        sage: B = VectorSpace(QQ, 1) 
        sage: C = VectorSpace(QQ, 1)
        sage: hex1, hex2 = A.verify_hexagon_axioms(B, C)
        sage: hex1 and hex2
        True
        
        sage: # Works with different dimensions
        sage: A = VectorSpace(QQ, 2)
        sage: B = VectorSpace(QQ, 3)
        sage: C = VectorSpace(QQ, 1)
        sage: hex1, hex2 = A.verify_hexagon_axioms(B, C)
        sage: hex1 and hex2
        True
    
    ALGORITHM:    
    Verifies two hexagonal diagrams relating braiding and associator.
    Both paths around each hexagon must yield the same morphism.
    """

def verify_symmetry_constraint(self, B):
    r"""
    Verify the symmetry constraint β_{B,A} ∘ β_{A,B} = id.
    
    Checks that double braiding returns to the identity, distinguishing
    symmetric monoidal from merely braided monoidal categories.
    
    INPUT:
    - ``B`` -- another object in the category
    
    OUTPUT:
    Boolean indicating if symmetry holds
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 2)
        sage: W = VectorSpace(QQ, 3)
        sage: V.verify_symmetry_constraint(W)
        True
        
        sage: # For modules over commutative rings
        sage: M = ZZ^2
        sage: N = ZZ^3
        sage: M.verify_symmetry_constraint(N)
        True
        
        sage: # This distinguishes from braided categories where
        sage: # β_{B,A} ∘ β_{A,B} might equal -id or other element
    
    ALGORITHM:
    Computes β_{B,A} ∘ β_{A,B} and checks if it equals the identity
    morphism on A⊗B.
    """
```

## Internal Hom and Duality

```python
def internal_hom(self, other):
    r"""
    Return the internal hom object [self, other].
    
    In a closed symmetric monoidal category, the internal hom
    represents morphisms as objects, enabling the tensor-hom adjunction.
    
    INPUT:
    - ``other`` -- target object
    
    OUTPUT:
    The internal hom object
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 2)
        sage: W = VectorSpace(QQ, 3)
        sage: Hom_VW = V.internal_hom(W)
        sage: Hom_VW.dimension()
        6  # 2 × 3 = 6 for linear maps V → W
        
        sage: # Tensor-hom adjunction
        sage: U = VectorSpace(QQ, 1)
        sage: # Hom(U⊗V, W) ≅ Hom(U, [V,W])
        sage: UV = U.tensor_product(V)
        sage: hom1 = Hom(UV, W)
        sage: hom2 = Hom(U, V.internal_hom(W))
        sage: hom1.dimension() == hom2.dimension()
        True
    """

def dual(self):
    r"""
    Return the dual object self* = [self, I].
    
    The dual is the internal hom into the unit object,
    representing linear functionals on self.
    
    OUTPUT:
    The dual object
    
    EXAMPLES::
    
        sage: V = VectorSpace(QQ, 3)
        sage: V_dual = V.dual()
        sage: V_dual.dimension()
        3  # For finite-dimensional spaces: dim(V*) = dim(V)
        
        sage: # Double dual isomorphism for finite dimensional spaces
        sage: V_double_dual = V_dual.dual()
        sage: V_double_dual.is_isomorphic(V)
        True
        
        sage: # Evaluation pairing: V* ⊗ V → k
        sage: eval_map = V_dual.tensor_product(V).hom(V.base_ring())
        sage: eval_map.is_surjective()
        True
    """
```

This interface provides the essential methods for working with symmetric monoidal categories, enabling tensor products with coherent natural isomorphisms for multilinear algebra and categorical constructions.
