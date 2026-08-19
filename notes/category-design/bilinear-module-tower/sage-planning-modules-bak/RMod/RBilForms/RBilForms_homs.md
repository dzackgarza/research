<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RBilForms/RBilForms_homs.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: BilinearModule Morphisms

Morphisms in the category of bilinear modules: Hom(L₁, L₂).

**Convention**: Hom(L₁, L₂) means form-preserving morphisms by default in bilinear module context.

## Mathematical Test Assertions

```python
# Mathematical assertion: Form-preserving morphisms preserve A2 root system structure
# sage: R = RootSystem(['A', 2])
# sage: L = R.root_lattice()
# sage: alpha1, alpha2 = L.simple_roots()
# sage: # Test standard reflection preserves form structure
# sage: s1 = L.weyl_group().simple_reflection(1)
# sage: assert alpha1.scalar(alpha1) == s1(alpha1).scalar(s1(alpha1))  # Norm preservation
# sage: assert alpha1.scalar(alpha2) == s1(alpha1).scalar(s1(alpha2))  # Cross-term preservation

# Mathematical assertion: Embedding morphisms have trivial kernel in bilinear category
# sage: R = RootSystem(['B', 3])
# sage: L = R.root_lattice()
# sage: sublattice = L.submodule([L.simple_root(1), L.simple_root(2)])
# sage: emb = sublattice.natural_embedding()
# sage: assert emb.kernel().rank() == 0  # Embeddings are injective
# sage: assert emb.is_injective()
# sage: # Verify form preservation on random sublattice elements
# sage: v1 = sublattice.simple_root(1) + 2*sublattice.simple_root(2)
# sage: v2 = 3*sublattice.simple_root(1) - sublattice.simple_root(2)
# sage: assert v1.scalar(v2) == emb(v1).scalar(emb(v2))  # Form preservation

# Mathematical assertion: Adjoint morphisms satisfy b(v, f*(w)) = b(f(v), w) property
# sage: R = RootSystem(['D', 4])
# sage: L = R.root_lattice()
# sage: # Construct endomorphism via Weyl group element
# sage: w = L.weyl_group().longest_element()
# sage: f = L.module_morphism(w.action_on_root_lattice())
# sage: f_adj = f.adjoint()
# sage: # Test adjoint property on simple roots
# sage: alpha1, alpha2 = L.simple_root(1), L.simple_root(2)
# sage: assert alpha1.scalar(f_adj(alpha2)) == f(alpha1).scalar(alpha2)  # Adjoint property
# sage: # Test on arbitrary elements
# sage: v = alpha1 + 2*alpha2
# sage: w = 3*alpha1 - alpha2
# sage: assert v.scalar(f_adj(w)) == f(v).scalar(w)  # General adjoint relation

# Mathematical assertion: Composition preserves isometry property (Mac Lane categorical)
# sage: R = RootSystem(['E', 6])
# sage: L = R.root_lattice()
# sage: W = L.weyl_group()
# sage: s1, s2 = W.simple_reflection(1), W.simple_reflection(2)
# sage: # Compose two reflections to get rotation
# sage: f1 = L.module_morphism(s1.action_on_root_lattice())
# sage: f2 = L.module_morphism(s2.action_on_root_lattice())
# sage: comp = f2.compose(f1)
# sage: assert f1.is_isometry() and f2.is_isometry()  # Components are isometries
# sage: assert comp.is_isometry()  # Composition preserves isometry
# sage: # Verify associativity of composition
# sage: s3 = W.simple_reflection(3)
# sage: f3 = L.module_morphism(s3.action_on_root_lattice())
# sage: assert (f3.compose(f2)).compose(f1) == f3.compose(f2.compose(f1))  # Associativity

# Mathematical assertion: Primitive embeddings have torsion-free cokernels
# sage: # Use standard Z-lattice with bilinear form
# sage: L = IntegralLattice("A2")  # A2 root lattice as integral lattice
# sage: sublat = L.sublattice([L.basis()[0]])  # 1D sublattice
# sage: emb = sublat.primitive_embedding_into(L)
# sage: coker = emb.cokernel()
# sage: assert coker.is_torsion_free()  # Primitive embeddings have torsion-free cokernel
# sage: # Verify cokernel rank
# sage: assert coker.rank() == L.rank() - sublat.rank()  # Correct rank formula
# sage: # Test non-primitive embedding has torsion
# sage: scaled_emb = sublat.embedding_into(L, scale=2)
# sage: assert not scaled_emb.cokernel().is_torsion_free()  # Non-primitive has torsion

# Mathematical assertion: Discriminant preservation for isometric embeddings  
# sage: R = RootSystem(['G', 2])
# sage: L = R.root_lattice()
# sage: sublat = L.submodule([L.simple_root(1)])  # 1D submodule
# sage: emb = sublat.isometric_embedding_into(L)
# sage: # Isometric embeddings preserve discriminant up to codimension
# sage: assert abs(sublat.discriminant()) * abs(emb.orthogonal_complement().discriminant()) == abs(L.discriminant())
# sage: # Verify form preservation preserves discriminant relationships
# sage: assert emb.is_isometry()  # Must be isometry
# sage: assert emb.discriminant_multiplier() == 1  # Isometries preserve discriminant

# Mathematical assertion: Kernel-cokernel exact sequence in abelian category
# sage: R = RootSystem(['F', 4])
# sage: L = R.root_lattice()
# sage: target = L.submodule([L.simple_root(1), L.simple_root(2)])
# sage: proj = L.projection_onto(target)  # Canonical projection
# sage: # Test exactness: im(kernel_inclusion) = ker(original_morphism)
# sage: ker = proj.kernel()
# sage: assert ker.intersection(target).rank() == 0  # Kernel disjoint from image
# sage: # Test coimage-image isomorphism (abelian category property)
# sage: coim = proj.coimage()
# sage: im = proj.image()
# sage: assert coim.is_isomorphic_to(im)  # Fundamental abelian category property
# sage: # Verify canonical factorization exists
# sage: epic, iso, monic = proj.canonical_factorization()
# sage: assert epic.is_surjective() and monic.is_injective() and iso.is_isomorphism()
```

## Hierarchy of Morphism Spaces

We have a natural hierarchy of inclusions:

```
PrimEmb(L₁, L₂) ⊆ Emb(L₁, L₂) ⊆ Hom(L₁, L₂) ⊆ Hom_R(L₁, L₂)
```

- **Hom_R(L₁, L₂)**: All R-module morphisms (ignore bilinear forms)
- **Hom(L₁, L₂)**: Form-preserving R-module morphisms (default in BilR-Mod)  
  `{φ ∈ Hom_R(L₁, L₂) : b₂(φ(v), φ(w)) = b₁(v, w) for all v, w}`
- **Emb(L₁, L₂)**: Embeddings = injective form-preserving morphisms  
  `{φ ∈ Hom(L₁, L₂) : φ is injective}`
- **PrimEmb(L₁, L₂)**: Primitive embeddings = embeddings with torsion-free cokernel  
  `{φ ∈ Emb(L₁, L₂) : coker(φ) is torsion-free}`

**Key insight**: In BilR-Mod, all embeddings are automatically isometric since all morphisms preserve forms.

## Set Membership Tests

```python
def is_isometry(self):
    r"""
    Test membership in Hom(L₁, L₂) (form-preserving morphisms).
    
    This tests if φ ∈ Hom_R(L₁, L₂) also preserves bilinear forms:
    b₂(φ(v), φ(w)) = b₁(v, w) for all v, w ∈ L₁
    
    OUTPUT:
    True if φ ∈ Hom(L₁, L₂), False otherwise
    
    EXAMPLES::
    
        sage: # Standard orthonormal lattice Z^2
        sage: L.<e1, e2> = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: 
        sage: # Form-preserving rotation: e1 ↦ e2, e2 ↦ -e1
        sage: phi = L.hom(L, {e1: e2, e2: -e1})
        sage: assert phi.is_isometry()
        
        sage: # Non-form-preserving scaling: e1 ↦ 2*e1, e2 ↦ 2*e2
        sage: psi = L.hom_R(L, {e1: 2*e1, e2: 2*e2})
        sage: # Show form is not preserved: scaling by 2 multiplies pairings by 4
        sage: assert e1 * e1 != psi(e1) * psi(e1)  # 1 ≠ 4
        sage: assert e2 * e2 != psi(e2) * psi(e2)  # 1 ≠ 4
        sage: test_vec = e1 + e2  # Use mixed vector
        sage: assert test_vec * test_vec != psi(test_vec) * psi(test_vec)  # 2 ≠ 8
        
        sage: # Set membership testing between different lattices
        sage: L1.<u, v> = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: L2.<x, y> = BilinearModule(matrix(ZZ, [[1, 0], [0, -1]]))
        sage: 
        sage: Hom_space = L1.hom(L2)
        sage: # Form-preserving morphism: u ↦ x+y, v ↦ x-y
        sage: good_morphism = L1.hom(L2, {u: x+y, v: x-y})
        sage: assert good_morphism in Hom_space  # Tests form preservation
        sage: assert good_morphism.is_isometry()  # Equivalent test
        
        sage: # Non-form-preserving morphism not in Hom space
        sage: bad_morphism = L1.hom_R(L2, {u: 2*x, v: y})
        sage: assert bad_morphism not in Hom_space
        sage: # Show form is not preserved by finding concrete counterexample
        sage: assert u * u != bad_morphism(u) * bad_morphism(u)  # 2 ≠ 4 
        sage: assert u * v != bad_morphism(u) * bad_morphism(v)  # 1 ≠ 0
        sage: assert u * u == 2 and bad_morphism(u) * bad_morphism(u) == 4
        sage: assert u * v == 1 and bad_morphism(u) * bad_morphism(v) == 0
        
        sage: # Alternative: construct maps through the homset
        sage: HomSet = L1.Hom(L2)  # Abstract homset
        sage: # Create morphism using homset's element constructor
        sage: morphism1 = HomSet({u: x+y, v: x-y})
        sage: assert morphism1 == good_morphism
        sage: assert morphism1.is_isometry()
        
        sage: # Try creating non-form-preserving map (should fail)
        sage: try:
        ....:     invalid_map = HomSet({u: 2*x, v: y})
        ....: except ValueError as e:
        ....:     print(f"Error: {e}")
        Error: Map {u: 2*x, v: y} does not preserve bilinear forms
        
        sage: # Mathematical verification: form preservation
        sage: # For any v, w in L1: ⟨v, w⟩_L1 = ⟨φ(v), φ(w)⟩_L2
        sage: v1, v2 = u + v, 2*u - v  # Random elements of L1
        sage: assert v1 * v2 == good_morphism(v1) * good_morphism(v2)  # Form preservation
        
        sage: # Check on basis elements too
        sage: assert u * v == good_morphism(u) * good_morphism(v)  # ⟨u,v⟩ = ⟨φ(u),φ(v)⟩
        sage: assert u * u == good_morphism(u) * good_morphism(u)  # ⟨u,u⟩ = ⟨φ(u),φ(u)⟩  
        sage: assert v * v == good_morphism(v) * good_morphism(v)  # ⟨v,v⟩ = ⟨φ(v),φ(v)⟩
    """

def is_embedding(self):
    r"""
    Test membership in Emb(L₁, L₂) ⊆ Hom(L₁, L₂).
    
    This tests: φ ∈ Hom(L₁, L₂) AND φ is injective
    
    Note: In BilR-Mod, all embeddings are automatically isometric.
    
    OUTPUT:
    True if φ ∈ Emb(L₁, L₂), False otherwise
    
    EXAMPLES::
    
        sage: # 3D lattice 
        sage: L.<a, b, c> = BilinearModule(matrix(ZZ, [[2, 1, 0],
        ....:                                          [1, 3, 1], 
        ....:                                          [0, 1, 2]]))
        sage: 
        sage: # Sublattice S generated by first two generators
        sage: S = L.submodule(generators=[a, b])
        sage: inc = S.inclusion_into(L)  # Natural inclusion a ↦ a, b ↦ b
        sage: assert inc.is_embedding()
        sage: assert inc.is_injective()
        sage: assert inc.is_isometry()
        
        sage: # Set membership testing
        sage: Emb_space = S.embeddings(L)
        sage: assert inc in Emb_space  # Tests injectivity + form preservation
        sage: assert inc.is_embedding()  # Equivalent test
        
        sage: # Alternative: construct embeddings through the embedding space
        sage: EmbeddingSet = S.Embeddings(L)  # Abstract embedding space
        sage: # Create embedding using embedding space's element constructor
        sage: emb1 = EmbeddingSet({a: a, b: b})  # Natural inclusion
        sage: assert emb1 == inc
        sage: assert emb1.is_embedding()
        
        sage: # Try creating non-injective map in embedding space (should fail)
        sage: try:
        ....:     bad_emb = EmbeddingSet({a: a+b, b: a+b})  # Not injective
        ....: except ValueError as e:
        ....:     print(f"Error: {e}")
        Error: Map {a: a+b, b: a+b} is not injective
        
        sage: # Mathematical verification: kernel is trivial
        sage: assert inc.kernel() == S.submodule([])  # ker(φ) = {0} for embeddings
        sage: assert inc.kernel().rank() == 0  # Rank is 0 (but could have torsion)
        
        sage: # Verify injectivity on random elements
        sage: test_elem = 3*a - 2*b  # Random element of S
        sage: assert inc(test_elem) != 0*a  # Only zero maps to zero
        sage: assert inc(0*a) == 0*a  # Zero maps to zero
        
        sage: # Form preservation for embeddings
        sage: elem1, elem2 = a + b, 2*a - b  # Random elements of S
        sage: assert elem1 * elem2 == inc(elem1) * inc(elem2)  # ⟨v,w⟩_S = ⟨φ(v),φ(w)⟩_L
        
        sage: # Form-preserving but not injective projection
        sage: L2.<x, y> = BilinearModule(matrix(ZZ, [[2, 1], [1, 3]]))
        sage: 
        sage: # Projection: a ↦ x, b ↦ y, c ↦ 0 (rank-reducing)
        sage: proj = L.hom(L2, {a: x, b: y, c: 0*x})
        sage: assert proj not in Emb_space
        sage: assert not proj.is_embedding()
        sage: assert proj.is_isometry()  # Still form-preserving
        sage: # Verify form preservation on a few elements
        sage: assert a * b == proj(a) * proj(b)  # 1 = 1
        sage: assert a * a == proj(a) * proj(a)  # 2 = 2
    """

def is_primitive_embedding(self):
    r"""
    Test membership in PrimEmb(L₁, L₂) ⊆ Emb(L₁, L₂).
    
    A primitive embedding satisfies:
    φ ∈ Emb(L₁, L₂) AND coker(φ) is torsion-free
    
    This is the strongest condition: L₂/φ(L₁) has no torsion.
    
    OUTPUT:
    True if φ ∈ PrimEmb(L₁, L₂), False otherwise
    
    EXAMPLES::
    
        sage: # Hyperbolic plane
        sage: H.<u, v> = BilinearModule(matrix(ZZ, [[0, 1], [1, 0]]))
        sage: 
        sage: # Target 3D lattice: hyperbolic plane ⊥ ⟨w⟩
        sage: L.<e, f, w> = BilinearModule(matrix(ZZ, [[0, 1, 0],
        ....:                                          [1, 0, 0], 
        ....:                                          [0, 0, 1]]))
        sage: 
        sage: # Primitive embedding: u ↦ e, v ↦ f (torsion-free cokernel)
        sage: phi = H.primitive_embedding_into(L, {u: e, v: f})
        sage: assert phi.is_primitive_embedding()
        
        sage: # Non-primitive embedding: scale by 2
        sage: # u ↦ 2*e, v ↦ 2*f (cokernel has 2-torsion)
        sage: psi = H.embedding_into(L, {u: 2*e, v: 2*f})
        sage: assert not psi.is_primitive_embedding()
        sage: assert psi.cokernel().has_torsion()
        
        sage: # Set membership testing
        sage: PrimEmb_space = H.primitive_embeddings(L)
        sage: assert phi in PrimEmb_space  # Tests torsion-free cokernel
        sage: assert phi.is_primitive_embedding()  # Equivalent test
        
        sage: # Alternative: construct through primitive embedding space
        sage: PrimEmbSet = H.PrimitiveEmbeddings(L)  # Abstract primitive embedding space
        sage: # Create primitive embedding using element constructor
        sage: prim_emb1 = PrimEmbSet({u: e, v: f})  # Standard inclusion
        sage: assert prim_emb1 == phi
        sage: assert prim_emb1.is_primitive_embedding()
        
        sage: # Try creating scaled embedding (should fail for primitive)
        sage: try:
        ....:     scaled_emb = PrimEmbSet({u: 2*e, v: 2*f})  # Cokernel has torsion
        ....: except ValueError as e:
        ....:     print(f"Error: {e}")
        Error: Map {u: 2*e, v: 2*f} produces torsion in cokernel
        
        sage: # But the scaled embedding works in regular embedding space
        sage: EmbSet = H.Embeddings(L)
        sage: scaled_emb = EmbSet({u: 2*e, v: 2*f})
        sage: assert scaled_emb.is_embedding()
        sage: assert not scaled_emb.is_primitive_embedding()
        
        sage: # Mathematical verification: primitive embeddings have torsion-free cokernel
        sage: assert phi.cokernel().is_torsion_free()  # coker(φ) is torsion-free
        sage: assert phi.cokernel().rank() == 1  # Rank of cokernel
        sage: assert phi.cokernel() == L.quotient(phi.image())  # coker(φ) = L/im(φ)
        
        sage: # Non-primitive embedding has torsion in cokernel
        sage: assert not psi.cokernel().is_torsion_free()  # coker(ψ) has torsion
        sage: assert not psi.cokernel().torsion_submodule().is_zero()  # Has non-trivial torsion
        
        sage: # Verify the 2-torsion specifically
        sage: # coker(ψ) ≅ ⟨w⟩ ⊕ Z/2Z where the Z/2Z comes from scaling
        sage: assert psi.cokernel().torsion_submodule().exponent() == 2
        
        sage: # Form preservation still holds for primitive embeddings
        sage: test_u, test_v = u + v, 2*u - v  # Random elements of H
        sage: assert test_u * test_v == phi(test_u) * phi(test_v)  # ⟨·,·⟩_H = ⟨φ(·),φ(·)⟩_L
        
        sage: # Kernel is still trivial (it's an embedding)
        sage: assert phi.kernel().rank() == 0
        
        sage: # Embedding with torsion in cokernel
        sage: assert psi not in PrimEmb_space
        sage: assert not psi.is_primitive_embedding()
        
        sage: # But still an embedding
        sage: Emb_space = H.embeddings(L)
        sage: assert psi in Emb_space
        sage: assert psi.is_embedding()
    """


def scaling_factor(self):
    r"""
    Return the scaling factor if this is a similarity.
    
    A similarity satisfies: b₂(φ(v), φ(w)) = λ · b₁(v, w) for some λ ∈ R.
    
    OUTPUT:
    The scaling factor λ if the morphism is a similarity, 
    None if it's not a similarity
    
    EXAMPLES::
    
        sage: L = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: scaling = matrix(ZZ, [[3, 0], [0, 3]])
        sage: phi = L.morphism_to(L, scaling)
        sage: phi.scaling_factor()
        9
        
        sage: # Form-preserving has scaling factor 1
        sage: refl = matrix(ZZ, [[-1, 0], [0, 1]])
        sage: psi = L.morphism_to(L, refl)
        sage: psi.scaling_factor()
        1
    """
```

## Abelian Category Structure

```python
def kernel(self):
    r"""
    Return the kernel as a bilinear submodule of the domain.
    
    For φ: (L₁, b₁) → (L₂, b₂), ker(φ) inherits the form by restriction.
    
    OUTPUT:
    Kernel as a bilinear module with restricted form
    
    EXAMPLES::
    
        sage: L1.<u, v, w> = BilinearModule(matrix(ZZ, [[2,1,0],[1,3,0],[0,0,1]]))
        sage: L2.<x, y> = BilinearModule(matrix(ZZ, [[1,0],[0,-1]]))
        sage: phi = L1.hom(L2, {u: x+y, v: x-y, w: 0*x})
        
        sage: K = phi.kernel()
        sage: K.rank()
        1
        sage: K.generators()
        [w]
        sage: K.gram_matrix()  # Form restricted from L1
        [1]
        
        sage: # Kernel is always a bilinear submodule
        sage: assert K.is_submodule_of(L1)
        sage: assert phi(K.0) == 0*x
    """

def cokernel(self):
    r"""
    Return the cokernel L₂/im(φ) with quotient bilinear form.
    
    The form descends to the quotient iff im(φ) is isotropic in L₂.
    For form-preserving maps from non-degenerate L₁, this is automatic.
    
    OUTPUT:
    Cokernel as a bilinear quotient module
    
    EXAMPLES::
    
        sage: # Scaling map - cokernel is torsion
        sage: L.<e, f> = BilinearModule(matrix(ZZ, [[0,1],[1,0]]))
        sage: phi = L.hom(L, {e: 2*e, f: 2*f})
        
        sage: C = phi.cokernel()
        sage: C.rank()
        0
        sage: C.is_torsion()  # Z/2Z ⊕ Z/2Z
        True
        
        sage: # Form descends because im(φ) = 2L is isotropic mod 2
        sage: # The quotient form is well-defined
    """

def image(self):
    r"""
    Return the image as a bilinear submodule of the codomain.
    
    im(φ) ⊆ L₂ inherits the form by restriction.
    
    OUTPUT:
    Image as a bilinear submodule
    
    EXAMPLES::
    
        sage: L1.<u, v> = BilinearModule(matrix(ZZ, [[1,0],[0,1]]))
        sage: L2.<x, y, z> = BilinearModule(matrix(ZZ, [[2,0,0],[0,2,0],[0,0,2]]))
        sage: phi = L1.hom(L2, {u: x+y, v: x-y})
        
        sage: Im = phi.image()
        sage: Im.rank()
        2
        sage: Im.gram_matrix()  # Restricted from L2
        [4 0]
        [0 4]
        
        sage: # For isometries, image has same form as domain
        sage: assert phi.is_isometry()
    """

def coimage(self):
    r"""
    Return the coimage L₁/ker(φ) with quotient form.
    
    Always well-defined since ker(φ) is isotropic for form-preserving maps.
    In abelian categories: coimage ≅ image (via induced isomorphism).
    
    OUTPUT:
    Coimage as a bilinear quotient module
    
    EXAMPLES::
    
        sage: L1.<u, v, w> = BilinearModule(matrix(ZZ, [[2,0,0],[0,2,0],[0,0,0]]))
        sage: L2.<x, y> = BilinearModule(matrix(ZZ, [[1,0],[0,1]]))
        sage: phi = L1.hom(L2, {u: x, v: y, w: 0})
        
        sage: CoIm = phi.coimage()
        sage: CoIm.rank()
        2
        sage: # Coimage ≅ image via factorization
        sage: Im = phi.image()
        sage: assert CoIm.is_isomorphic_to(Im)
    """

def factor_through_image(self):
    r"""
    Factor morphism as L₁ → coimage ≅ image → L₂.
    
    This is the canonical factorization in abelian categories.
    
    OUTPUT:
    Triple (epi, iso, mono) where φ = mono ∘ iso ∘ epi
    
    EXAMPLES::
    
        sage: L1 = BilinearModule(matrix(ZZ, [[2,0],[0,0]]))
        sage: L2 = BilinearModule(matrix(ZZ, [[1]]))
        sage: phi = L1.hom(L2, {L1.0: L2.0, L1.1: 0})
        
        sage: epi, iso, mono = phi.factor_through_image()
        sage: # phi = mono ∘ iso ∘ epi
        sage: assert phi == mono.compose(iso.compose(epi))
        sage: assert epi.is_surjective()
        sage: assert iso.is_isomorphism()
        sage: assert mono.is_injective()
    """
```

## Orthogonal Complements

```python
def orthogonal_complement_in_target(self):
    r"""
    Return the orthogonal complement of the image in the target module.
    
    For an embedding φ: L₁ → L₂, returns φ(L₁)^⊥ ⊆ L₂.
    
    OUTPUT:
    Submodule of the target orthogonal to the image
    
    EXAMPLES::
    
        sage: # 2D subspace in 3D
        sage: L2 = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: L3 = BilinearModule(matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        sage: phi = L2.standard_embedding_into(L3)
        sage: orth_comp = phi.orthogonal_complement_in_target()
        sage: orth_comp.dimension()
        1
        sage: orth_comp.basis()
        [(0, 0, 1)]
    """
```

## Composition and Group Structure

```python
def compose(self, other):
    r"""
    Compose this morphism with another.
    
    For φ: L₁ → L₂ and ψ: L₂ → L₃, returns ψ ∘ φ: L₁ → L₃.
    
    INPUT:
    - other: Morphism whose domain is this morphism's codomain
    
    OUTPUT:
    Composed morphism
    
    EXAMPLES::
    
        sage: L1 = BilinearModule(matrix(ZZ, [[1]]))
        sage: L2 = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: L3 = BilinearModule(matrix(ZZ, [[2, 1], [1, 2]]))
        
        sage: phi = L1.embedding_into(L2)
        sage: psi = L2.embedding_into(L3)
        sage: composed = psi.compose(phi)
        sage: composed.domain() == L1
        True
        sage: composed.codomain() == L3
        True
    """

def inverse(self):
    r"""
    Return the inverse morphism (if this is an isometry).
    
    OUTPUT:
    Inverse morphism, or raises error if not invertible
    
    EXAMPLES::
    
        sage: L = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: refl = matrix(ZZ, [[-1, 0], [0, 1]])
        sage: phi = L.morphism_to(L, refl)
        sage: phi_inv = phi.inverse()
        sage: phi.compose(phi_inv).is_identity()
        True
    """

def orthogonal_group_element(self):
    r"""
    View this isometry as an element of the orthogonal group.
    
    For isometries φ: L → L, returns the corresponding element in O(L).
    
    OUTPUT:
    Element of the orthogonal group O(L)
    """

def adjoint(self):
    r"""
    Return the adjoint morphism f*: L₂ → L₁ of this morphism f: L₁ → L₂.
    
    The adjoint satisfies: b₁(v, f*(w)) = b₂(f(v), w) for all v ∈ L₁, w ∈ L₂.
    
    OUTPUT:
    The adjoint morphism f* in Hom_BilRMod(L₂, L₁)
    
    EXAMPLES::
    
        sage: # Endomorphism case
        sage: L = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: f = L.endomorphism(matrix(ZZ, [[2, 1], [0, 3]]))
        sage: f_adj = f.adjoint()
        sage: f_adj.matrix()
        [2 0]
        [1 3]
        
        sage: # For standard inner product, adjoint is transpose
        sage: f_adj.matrix() == f.matrix().T
        True
        
        sage: # Verify adjoint property
        sage: v = L([1, 0])
        sage: w = L([0, 1])
        sage: L.bilinear_form(v, f_adj(w)) == L.bilinear_form(f(v), w)
        True
        
        sage: # General bilinear form
        sage: M = BilinearModule(matrix(ZZ, [[1, 2], [0, 1]]))
        sage: g = M.endomorphism(matrix(ZZ, [[1, 1], [1, 0]]))
        sage: g_adj = g.adjoint()
        
        sage: # Adjoint depends on the bilinear form
        sage: g_adj.matrix() != g.matrix().T
        True
        
    NOTE:
    This requires the bilinear forms to be non-degenerate for the 
    adjoint to be uniquely defined.
    """
```

## Discriminant and Invariants

```python
def discriminant_multiplier(self):
    r"""
    Return how this morphism scales the discriminant.
    
    For φ: L₁ → L₂, if both are non-degenerate, computes:
    disc(L₂) / disc(φ(L₁))
    
    OUTPUT:
    Ratio of discriminants
    
    EXAMPLES::
    
        sage: L = BilinearModule(matrix(ZZ, [[1, 0], [0, 1]]))
        sage: scaling = matrix(ZZ, [[2, 0], [0, 2]])
        sage: phi = L.morphism_to(L, scaling)
        sage: phi.discriminant_multiplier()
        4
        
        sage: # Isometry preserves discriminant
        sage: refl = matrix(ZZ, [[-1, 0], [0, 1]])
        sage: psi = L.morphism_to(L, refl)
        sage: psi.discriminant_multiplier()
        1
    """

def signature_change(self):
    r"""
    Return how this morphism changes the signature.
    
    For morphisms between forms over ordered fields.
    
    OUTPUT:
    Tuple describing signature change
    """

def witt_index_change(self):
    r"""
    Return how this morphism changes the Witt index.
    
    OUTPUT:
    Change in Witt index from domain to image
    """
```

## Special Morphism Constructions

```python
def restrict_to_submodule(self, submodule):
    r"""
    Restrict this morphism to a submodule of the domain.
    
    INPUT:
    - submodule: Submodule of the domain
    
    OUTPUT:
    Restricted morphism with the given submodule as domain
    """

def extend_by_orthogonal_sum(self, other_morphism):
    r"""
    Extend by orthogonal direct sum with another morphism.
    
    For φ₁: L₁ → M₁ and φ₂: L₂ → M₂, returns φ₁ ⊥ φ₂: L₁ ⊥ L₂ → M₁ ⊥ M₂.
    
    INPUT:
    - other_morphism: Morphism to combine orthogonally
    
    OUTPUT:
    Direct sum morphism
    """

def tensor_with(self, other_morphism):
    r"""
    Tensor product with another morphism.
    
    For φ₁: L₁ → M₁ and φ₂: L₂ → M₂, returns φ₁ ⊗ φ₂: L₁ ⊗ L₂ → M₁ ⊗ M₂.
    
    INPUT:
    - other_morphism: Morphism to tensor with
    
    OUTPUT:
    Tensor product morphism
    """
```

## Hierarchy Constructors

```python
@classmethod
def hom_r(cls, L1, L2):
    r"""
    Return the full R-module morphism space Hom_R(L₁, L₂).
    
    This includes all R-module morphisms, ignoring bilinear form structure.
    
    OUTPUT:
    The R-module Hom_R(L₁, L₂)
    """

@classmethod  
def hom(cls, L1, L2):
    r"""
    Return Hom(L₁, L₂) ⊆ Hom_R(L₁, L₂) (form-preserving morphisms).
    
    This is the subset of form-preserving R-module morphisms:
    {φ ∈ Hom_R(L₁, L₂) : b₂(φ(v), φ(w)) = b₁(v, w) for all v, w ∈ L₁}
    
    Note: This is the default Hom in BilR-Mod category.
    
    OUTPUT:
    Subspace of form-preserving morphisms
    """

@classmethod
def embeddings(cls, L1, L2):
    r"""
    Return Emb(L₁, L₂) ⊆ Hom(L₁, L₂).
    
    This is the subset of injective form-preserving morphisms:
    {φ ∈ Hom(L₁, L₂) : φ is injective}
    
    In BilR-Mod, these are automatically isometric embeddings.
    
    OUTPUT:
    Subspace of embeddings from L₁ to L₂
    """

@classmethod
def primitive_embeddings(cls, L1, L2):
    r"""
    Return PrimEmb(L₁, L₂) ⊆ Emb(L₁, L₂).
    
    This is the subset of primitive embeddings:
    {φ ∈ Emb(L₁, L₂) : coker(φ) is torsion-free}
    
    OUTPUT:
    Subspace of primitive embeddings from L₁ to L₂
    """

@classmethod
def isometry_group(cls, L):
    r"""
    Return the orthogonal group O(L) = Hom(L, L).
    
    Since Hom(L, L) consists of bijective form-preserving endomorphisms,
    the orthogonal group is exactly the full Hom space for isomorphic modules.
    
    OUTPUT:
    The orthogonal group O(L) as a group object
    """
```

This interface captures the rich structure of morphisms between bilinear modules, including isometries, embeddings, primitive embeddings, and their relationships to classical invariants like discriminants and Witt indices.
