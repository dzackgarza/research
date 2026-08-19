# Nemo/Hecke Lattice Methods Reference
## Comprehensive Julia lattice stack reference (indefinite-aware)

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite setting |
| `[ND]` | Non-degenerate bilinear form required |
| `[INDEF]` | Works in indefinite signatures |
| `[DEG]` | Works with degenerate data |
| `[ZZMOD]` | Matrix/module-level integer lattice operations |
| `[NT]` | Number-theoretic lattice/form workflows |
| `[RED]` | Basis reduction |
| `[FLINT]` | Backed by FLINT |
| `[GAP]` | Uses GAP-backed routines |

---

## 1. Scope

This file documents the lattice-relevant surfaces of:

- `Hecke.jl` (high-level arithmetic lattices, genera, isometries, discriminant forms)
- `Nemo.jl` (matrix-level integer lattice primitives)

For cross-package Julia context (Oscar, Indefinite.jl, LLLplus, etc.), see `julia_lattice_methods_reference.md`.

---

## 2. Hecke.jl (Lattice-Level)

### 2.1 Core types

| Type | Description | Tags |
|------|-------------|------|
| `ZZLat` | Integral quadratic lattice over Z | `[ND, NT]` |
| `QuadLat` | Quadratic lattice over Q or number field | `[ND, NT]` |
| `HermLat` | Hermitian lattice over quadratic extension | `[ND, NT]` |
| `ZZGenus` | Global genus symbol for integer lattices | `[NT]` |
| `ZZLocalGenus` | Local genus symbol at prime `p` | `[NT]` |
| `TorQuadModule` | Finite quadratic module (`L^vee/L`) | `[NT]` |
| `QuadSpace` | Quadratic space over a field | `[NT]` |
| `HermSpace` | Hermitian space over extension field | `[NT]` |
| `ZZLatWithIsom` | Integer lattice with finite-order isometry | `[NT]` |
| `QuadSpaceWithIsom` | Quadratic space with isometry | `[NT]` |

### 2.2 Space construction and invariants

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space(K, n)` / `quadratic_space(K, G)` | Build quadratic space from dimension or Gram matrix | `[NT]` |
| `hermitian_space(E, n)` / `hermitian_space(E, G)` | Build hermitian space | `[NT]` |
| `gram_matrix(V)` / `gram_matrix(V, M)` | Gram matrix (optionally on subspace) | `[NT]` |
| `signature_tuple(V)` | Signature `(p, n)` | `[INDEF, NT]` |
| `det(V)` / `discriminant(V)` | Determinant/discriminant | `[NT]` |
| `is_regular(V)` | Non-degeneracy test | `[ND, NT]` |
| `is_isometric(V, W)` / `is_isometric(V, W, p)` | Global/local isometry tests | `[NT]` |
| `is_isotropic(V, p)` | Local isotropy test | `[INDEF, NT]` |
| `orthogonal_complement(V, M)` | Orthogonal complement | `[NT]` |
| `orthogonal_projection(V, M)` | Orthogonal projection | `[NT]` |

### 2.3 Lattice construction

| Method | Description | Tags |
|--------|-------------|------|
| `integer_lattice(; gram=G)` | Integer lattice from Gram matrix | `[NT]` |
| `integer_lattice(B; gram=G)` | Integer lattice from basis + optional Gram | `[NT]` |
| `lattice(V, B)` | Lattice in ambient quadratic space `V` | `[NT]` |
| `quadratic_lattice(K, gens; gram=M)` | Lattice from generators and Gram data | `[INDEF, NT]` |
| `hermitian_lattice(E, gens; gram=M)` | Hermitian lattice from generators | `[NT]` |
| `root_lattice(:A/:D/:E/:I, n)` | Root lattice constructors | `[PD, NT]` |
| `hyperbolic_plane_lattice(n)` | Hyperbolic plane lattice | `[INDEF, NT]` |
| `k3_lattice()` | K3 lattice constructor | `[INDEF, NT]` |
| `mukai_lattice()` | Mukai lattice constructor | `[INDEF, NT]` |
| `hyperkaehler_lattice(:K3, n=3)` | Hyperkahler intersection-form lattice | `[INDEF, NT]` |
| `rescale(L, r)` | Rescaled lattice | `[NT]` |

### 2.4 Intrinsic data and predicates

| Method | Description | Tags |
|--------|-------------|------|
| `gram_matrix(L)` / `basis_matrix(L)` | Core matrix data | `[NT]` |
| `ambient_space(L)` / `rational_span(L)` | Ambient/rational span | `[NT]` |
| `rank(L)` / `degree(L)` | Rank/ambient degree | `[NT]` |
| `signature_tuple(L)` | Signature triple `(n_positive, n_zero, n_negative)` | `[INDEF, NT]` |
| `det(L)` / `discriminant(L)` | Determinant/discriminant | `[NT]` |
| `scale(L)` / `norm(L)` | Scale and norm ideals | `[NT]` |
| `is_even(L)` / `is_integral(L)` / `is_unimodular(L)` | Arithmetic predicates | `[NT]` |
| `is_positive_definite(L)` / `is_negative_definite(L)` / `is_definite(L)` | Definiteness predicates | `[NT]` |
| `is_primary(L, p)` / `is_elementary(L, p)` | Discriminant-group structure predicates | `[NT]` |

### 2.5 Reduction and vector algorithms

| Method | Description | Tags |
|--------|-------------|------|
| `lll(L::ZZLat; same_ambient::Bool=true, redo::Bool=false, ctx::LLLContext=...)` | LLL reduction; `redo=true` forces recomputation; Lovász parameters via `ctx` | `[RED, FLINT, INDEF]` |
| `short_vectors(L::ZZLat, [lb=0,] ub, [elem_type=ZZRingElem]; check::Bool=true)` | Enumerate bounded-norm vectors; returns `Vector{Tuple{Vector{elem_type}, QQFieldElem}}` | `[PD, NT]` |
| `short_vectors_iterator(L, lb, ub)` | Lazy bounded-norm iterator | `[PD, NT]` |
| `shortest_vectors(L::ZZLat, [elem_type=ZZRingElem]; check::Bool=true)` | Shortest vectors + norm | `[PD, NT]` |
| `minimum(L)` / `kissing_number(L)` | Shortest norm / kissing number | `[PD, NT]` |
| `close_vectors(L::ZZLat, v::Vector, [lb,] ub; check::Bool=false)` | Bounded close-vector enumeration; **`check` defaults to `false`**; returns `Vector{Tuple{Vector{Int}, QQFieldElem}}` | `[PD, NT]` |
| `vectors_of_square_and_divisibility(L, n, d)` | Arithmetic vector constraints | `[PD, NT]` |
| `short_vectors_affine(S, v, a, d)` | Affine constrained vector search | `[INDEF, NT]` |

Indefinite caveats:

- `lll` can run on indefinite lattices, but "shortness" is relative to a majorant.
- `short_vectors`/`shortest_vectors` are positive-definite workflows.
- For indefinite reflection workflows use `short_vectors_affine` and Vinberg methods.

### 2.6 Genus and classification

| Method | Description | Tags |
|--------|-------------|------|
| `genus(L::ZZLat)` / `genus(A::MatElem)` | Global genus from lattice or Gram | `[INDEF, NT]` |
| `genus(L, p)` | Local genus at prime `p` | `[NT]` |
| `integer_genera(sig_pair::Vector{Int}, det::RationalUnion; min_scale=min(1,abs(det)), max_scale=max(1,abs(det)), even::Bool=false)` | Enumerate genera by signature and determinant; `even=false` (default) allows both even and odd lattices; `min_scale`/`max_scale` bound Jordan-block scales; upstream docs do not expose a `rank` keyword argument | `[NT]` |
| `representative(gen)` / `representatives(gen)` | Class representatives in genus | `[NT]` |
| `mass(gen)` | Genus mass | `[NT]` |
| `primes(gen)` / `local_symbol(gen, p)` | Local symbol access | `[NT]` |
| `quadratic_space(gen)` / `rational_representative(gen)` | Rational representatives | `[NT]` |
| `represents(G1, G2)` | Representation relation between genera | `[NT]` |
| `discriminant_group(L)` | `L^vee/L` as finite quadratic module | `[NT]` |
| `genus_representatives(L)` | Representatives of genus of `L` | `[NT]` |

### 2.7 Automorphisms and isometry

| Method | Description | Tags |
|--------|-------------|------|
| `automorphism_group_generators(L::AbstractLat; ambient_representation::Bool=true, depth::Int=-1, bacher_depth::Int=0)` | Generators for `Aut(L)`; upstream requires `is_definite(L)` (positive or negative definite); `ambient_representation=true` returns matrices in ambient-space coordinates | `[DEFINITE, GAP, NT]` |
| `automorphism_group_order(L::AbstractLat; depth::Int=-1, bacher_depth::Int=0)` | Order of automorphism group; upstream requires `is_definite(L)` (positive or negative definite) | `[DEFINITE, NT]` |
| `is_isometric(L1, L2)` | Isometry test; upstream requires `is_definite(L1)` and `is_definite(L2)` (positive or negative definite); uses LLL to rescale ND to PD before comparison | `[DEFINITE, NT]` |
| `is_isometric_with_isometry(L1, L2)` | Isometry test returning `(isometric::Bool, f)`; upstream requires `is_definite(L1)` and `is_definite(L2)`; docs specify `(false, zero_matrix(QQ, 0, 0))` on failure and expose kwargs `depth=3`, `bacher_depth=5`, `ambient_representation=true` | `[DEFINITE, NT]` |
| `is_locally_isometric(L1, L2, p)` | Local p-adic isometry test | `[NT]` |
| `is_rationally_isometric(L1, L2)` | Rational isometry test | `[INDEF, NT]` |
| `hasse_invariant(L, p)` / `witt_invariant(L, p)` | Local invariants | `[NT]` |

Definite note: `automorphism_group_generators` and `automorphism_group_order` support both positive and negative definite lattices; the upstream requirement is `is_definite(L)`, not `is_positive_definite(L)`.
Indefinite note: full automorphism groups are often infinite; practical workflows rely on local/rational tests, genus/discriminant forms, and Vinberg/reflection tools.

### 2.8 Module operations, embeddings, overlattices

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(L1, L2)` / `direct_product` / `biproduct` | Categorical lattice operations | `[NT]` |
| `intersect(L1, L2)` / `+(L1, L2)` / `*(n, L)` | Basic module operations | `[NT]` |
| `lattice_in_same_ambient_space(L, B)` | Sublattice in same ambient space | `[NT]` |
| `orthogonal_submodule(L, S)` | Orthogonal complement submodule | `[NT]` |
| `dual(L)` | Dual lattice | `[NT]` |
| `is_sublattice(L, S)` / `is_primitive(L, S)` | Inclusion/primitive tests | `[NT]` |
| `primitive_closure(L, S)` / `divisibility(L, v)` | Primitive closure/divisibility | `[NT]` |
| `glue_map(...)` / `overlattice(glue_map)` | Overlattice construction via gluing | `[NT]` |
| `primitive_extension(...)` | Nikulin-style primitive extension | `[NT]` |
| `local_modification(M, L, p)` | Local modification; current docs assume `M` is `Z_p`-maximal and `L` is isomorphic to `M` over `Q_p` | `[NT]` |
| `maximal_integral_lattice(L)` / `is_maximal_integral(L)` | Maximal-integral workflows | `[NT]` |
| `embed(L, gen)` / `embed_in_unimodular(L, ...)` | Embedding algorithms; current docs note `embed_in_unimodular` is presently implemented only for even lattices | `[NT]` |
| `kernel_lattice(L, f)` / `invariant_lattice(L, G)` / `coinvariant_lattice(L, G)` | Endomorphism/group-action derived sublattices | `[NT]` |

### 2.9 Vinberg algorithm (indefinite core)

| Method | Description | Tags |
|--------|-------------|------|
| `vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)` | Fundamental roots from Gram matrix | `[INDEF, NT]` |
| `vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)` | Fundamental roots from lattice object | `[INDEF, NT]` |
| `short_vectors_affine(S, v, a, d)` | Affine constrained vectors used by Vinberg | `[INDEF, NT]` |

This targets hyperbolic signatures `(1, n)` and reflection-group chamber computation.

### 2.10 Discriminant finite quadratic modules (`TorQuadModule`)

| Method | Description | Tags |
|--------|-------------|------|
| `torsion_quadratic_module(M, N)` / `torsion_quadratic_module(q::QQMatrix)` | Build finite quadratic module | `[NT]` |
| `abelian_group(T)` / `cover(T)` / `relations(T)` | Structural accessors | `[NT]` |
| `gram_matrix_bilinear(T)` / `gram_matrix_quadratic(T)` | Bilinear/quadratic Gram data | `[NT]` |
| `inner_product(a, b)` / `quadratic_product(a)` | Form evaluation | `[NT]` |
| `lift(a)` / `representative(a)` | Lift to cover lattice | `[NT]` |
| `orthogonal_submodule(T, S)` | Orthogonal complement in module | `[NT]` |
| `is_isometric_with_isometry(T, U)` | Isometry test returning `(Bool, map)` (or `(false, 0)` if no isometry). Upstream requires either equal quadratic-form moduli (or prior rescaling) and semiregular decomposition checks on `T ⊕ U` and `T ⊕ U^{-1}` | `[NT]` |
| `is_anti_isometric_with_anti_isometry(T, U)` | Anti-isometry test returning `(Bool, anti_map)` (or `(false, 0)` if absent). Upstream documents the same modulus-matching/rescale precondition and semiregular decomposition checks | `[NT]` |
| `normal_form(T; partial=false)` / `snf(T)` | Normal forms | `[NT]` |
| `brown_invariant(T)` / `genus(T, sig_pair)` / `is_genus(T, sig_pair)` | Genus-level invariants and feasibility | `[NT]` |
| `submodules(T::TorQuadModule; order::Int, index::Int, subtype::Vector{Int}, quotype::Vector{Int})` | Iterator over submodules of `T`; keyword filters: `order` (by cardinality), `index` (by index in `T`), `subtype` (by abelian-group invariants of the submodule), `quotype` (by abelian-group invariants of the quotient) | `[NT]` |
| `stable_submodules(T::TorQuadModule, act::Vector{TorQuadModuleMap}; quotype::Vector{Int})` | Iterator over submodules of `T` stable under the endomorphisms in `act`; keyword `quotype` filters by quotient abelian-group invariants | `[NT]` |

### 2.11 Lattices/spaces with isometry

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space_with_isometry(...)` | Construct `QuadSpaceWithIsom` | `[NT]` |
| `integer_lattice_with_isometry(...)` | Construct `ZZLatWithIsom` | `[NT]` |
| `isometry(Lf)` / `ambient_isometry(Lf)` | Isometry accessors | `[NT]` |
| `order_of_isometry(Lf)` | Order of lattice isometry `f`; upstream frames this as a divisor of the ambient isometry order and supports both finite- and infinite-order isometries | `[NT]` |
| `characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)` | Isometry polynomials | `[NT]` |
| `rank(Lf)` / `degree(Lf)` / `gram_matrix(Lf)` / `det(Lf)` / `discriminant(Lf)` / `signature_tuple(Lf)` / `scale(Lf)` / `norm(Lf)` / `genus(Lf)` / `rational_span(Lf)` | Direct attribute-forwarding methods for `ZZLatWithIsom`; contracts are inherited from the underlying lattice invariants | `[NT]` |
| `minimum(Lf)` | Minimum norm of nonzero vectors in the underlying lattice; requires `L` positive-definite (contracts inherited from `minimum(L)`). Source: OSCAR/Hecke lattices-with-isometry manual; local provenance `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom_online_provenance_2026-02-17.md` | `[PD, NT]` |
| `is_even(Lf)` / `is_integral(Lf)` / `is_unimodular(Lf)` / `is_primary(Lf, p)` / `is_primary_with_prime(Lf)` / `is_elementary(Lf, p)` / `is_elementary_with_prime(Lf)` / `is_positive_definite(Lf)` / `is_negative_definite(Lf)` / `is_definite(Lf)` | Arithmetic/discriminant-structure/definiteness predicates forwarded from the underlying lattice | `[NT]` |
| `invariant_lattice(Lf)` / `coinvariant_lattice(Lf)` | Fixed sublattice and its orthogonal complement, both primitive in `L` | `[NT]` |
| `kernel_lattice(Lf::ZZLatWithIsom, p::Union{ZZPolyRingElem, QQPolyRingElem})` | Kernel of polynomial `p(f)` as a primitive sublattice with induced isometry action | `[NT]` |
| `kernel_lattice(Lf::ZZLatWithIsom, l::Integer)` | Kernel of `f^l - 1` as a primitive sublattice with induced isometry action | `[NT]` |
| `discriminant_group(Lf)` / `discriminant_representation(L, G)` | Induced discriminant action; `image_centralizer_in_Oq(Lf)` computes $G_{L,f}$ and requires $L$ even for the general Miranda-Morrison case (simple cases: definite, ±identity, Euler-totient-rank bypass this restriction) | `[NT]` |
| `enumerate_classes_of_lattices_with_isometry(...)` | Isometry-equivariant class enumeration | `[NT]` |

### 2.12 Hermitian-specific surfaces

| Method | Description | Tags |
|--------|-------------|------|
| `jordan_decomposition(L, p)` | Local Jordan decomposition | `[NT]` |
| `is_isotropic(L, p)` / `is_modular(L)` / `is_modular(L, p)` | Local/global predicates | `[NT]` |
| `volume(L)` | Volume ideal | `[NT]` |
| `genus(L::HermLat)` / `genus(L::HermLat, p)` | Global/local hermitian genus | `[NT]` |
| `hermitian_genera(E::NumField, rank::Int, signatures::Vector{Tuple{Int, Int}}, determinant::Vector{QQFieldElem}; min_scale::Int=(determinant[1] != 0 ? 0 : -3), max_scale::Int=(determinant[1] != 0 ? 0 : 3), kwargs...)` | Enumerate hermitian genera; upstream requires `E` imaginary quadratic, `rank > 0`, and same-sign determinants (positive for even rank, negative for odd rank) | `[NT]` |
| `hermitian_local_genera(E::NumField, p::AbsNumFieldOrderIdeal, rank::Int, determinant::QQFieldElem, min_scale::Int, max_scale::Int)` | Enumerate local hermitian genera for ideal `p` in explicit scale window `[min_scale, max_scale]` | `[NT]` |
| `mass(L)` | Hermitian genus mass | `[NT]` |

### 2.13 Torsion quadratic modules with isometry (`TorQuadModuleWithIsom`)

| Method | Description | Tags |
|--------|-------------|------|
| `TorQuadModuleWithIsom` | Pair `(T, f)` of finite quadratic module and isometry | `[NT]` |
| `underlying_module(Tf)` / `torsion_quadratic_module(Tf)` | Access underlying finite quadratic module | `[NT]` |
| `isometry(Tf)` / `order_of_isometry(Tf)` | Access fixed isometry and its (cached) finite order | `[NT]` |
| `torsion_quadratic_module_with_isometry(T::TorQuadModule, [f::U]; check::Bool=true)` | Constructor from module and optional isometry `f`; upstream stable docs document `U` as any of `AutomorphismGroupElem{TorQuadModule}`, `TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, or `MatGroupElem{QQFieldElem, QQMatrix}`; omitting `f` uses identity; `check=true` validates compatibility | `[NT]` |
| `torsion_quadratic_module_with_isometry(q::QQMatrix, [f::ZZMatrix]; check::Bool=true)` | Constructor from rational quadratic-form matrix and optional integer action matrix; omitting `f` uses identity; `check=true` validates constraints | `[NT]` |
| `sub(Tf::TorQuadModuleWithIsom, gene::Vector{TorQuadModuleElem})` | Stable submodule from generators; returns `(TorQuadModuleWithIsom, TorQuadModuleMap)` | `[NT]` |
| `primary_part(Tf::TorQuadModuleWithIsom, m::IntegerUnion)` | Primary part with induced isometry; returns `(TorQuadModuleWithIsom, TorQuadModuleMap)` | `[NT]` |
| `orthogonal_submodule(Tf::TorQuadModuleWithIsom, S::TorQuadModule; check::Bool=true)` | Orthogonal complement with induced action; returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`; upstream requires `S` stable under isometry (`check=true` enforces this) | `[NT]` |
| `submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])` | Enumerate isometry-stable submodules of a torsion quadratic module with fixed isometry; current OSCAR docs expose `quotype` filtering with accepted selector values `0,1,2,3` | `[NT]` |
| `automorphism_group_with_inclusion(Tf::TorQuadModuleWithIsom)` | Automorphism group of the pair commuting with fixed isometry; returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)` | `[NT]` |
| `automorphism_group(Tf::TorQuadModuleWithMap)` | Automorphism group of the pair; upstream typesets `TorQuadModuleWithMap` at this location (page context: `TorQuadModuleWithIsom`) — known typesetting inconsistency | `[NT]` |
| `is_isomorphic_with_map(Tf::TorQuadModuleWithIsom, Sg::TorQuadModuleWithIsom)` / `is_anti_isomorphic_with_map(Tf::TorQuadModuleWithIsom, Sg::TorQuadModuleWithIsom)` | Isomorphism/anti-isomorphism tests; return `(Bool, TorQuadModuleMap)` — `(true, map)` on success, `(false, 0)` on failure | `[NT]` |

Source note: reconciled against `docs/julia/oscar_jl/number_theory/quad_form_and_isom/torquadmodwithisom.md` and OSCAR upstream docs at `https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/` (accessed 2026-02-17), with tuple-return, `submodules` keyword-contract, and constructor type-union addenda cross-checked on 2026-02-18 in `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`.
- Pass-24 addendum (2026-02-18): added `submodules`/`stable_submodules` typed signatures to §2.10 (TorQuadModule) and updated `torsion_quadratic_module_with_isometry` constructor type union in §2.13 to include `AutomorphismGroupElem{TorQuadModule}`, per OSCAR stable upstream docs.
- Pass-26 addendum (2026-02-18): added typed signatures and tuple return shapes for `sub`, `primary_part`, `orthogonal_submodule` (`(TorQuadModuleWithIsom, TorQuadModuleMap)`); `automorphism_group_with_inclusion` return type `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`; typed `is_isomorphic_with_map` / `is_anti_isomorphic_with_map` with confirmed return types. Source: OSCAR stable upstream `torquadmodwithisom` page (2026-02-18).

---

## 3. Nemo.jl (Matrix-Level Lattice Primitives)

Nemo provides integer matrix algorithms that underpin many Hecke lattice computations.

### 3.1 Reduction and normal forms

| Method | Description | Tags |
|--------|-------------|------|
| `lll(B::ZZMatrix, ctx::LLLContext)` | LLL reduction with context parameters | `[RED, FLINT, ZZMOD]` |
| `lll_with_transform(B)` | Returns reduced basis and transform matrix | `[RED, FLINT, ZZMOD]` |
| `lll_gram(G)` / `lll_gram_with_transform(G)` | Gram-based LLL variants | `[RED, FLINT, PD]` |
| `hnf(X)` / `hnf_with_transform(X)` | Hermite normal form and transform | `[DEG, ZZMOD]` |
| `snf(X)` / `snf_with_transform(X)` | Smith normal form and transforms | `[DEG, ZZMOD]` |

### 3.2 Practical notes

- `hnf`/`snf` are algebraic and signature-agnostic.
- `lll_gram` is meaningful for positive-definite (or semidefinite) Gram workflows.
- Hecke uses Nemo `ZZMatrix`/`QQMatrix` as the underlying matrix layer.

---

## 4. Indefinite-First Workflow Map

For your stated use case (indefinite lattices):

1. Build lattice/space (`integer_lattice`, `quadratic_lattice`, `hyperbolic_plane_lattice`, K3/Mukai constructors).
2. Use invariants and classification (`signature_tuple`, `genus`, local symbols, `discriminant_group`).
3. Use rational/local isometry tests (`is_rationally_isometric`, `is_locally_isometric`).
4. For reflection-group geometry use `vinberg_algorithm` + `short_vectors_affine`.
5. Use `ZZLatWithIsom` when finite-order isometries are central to classification.

---

## 5. Sources

- Oscar/Hecke docs root: https://docs.oscar-system.org/stable/Hecke/
- Oscar/Hecke integer lattices manual: https://docs.oscar-system.org/stable/Hecke/manual/lattices/integrelattices/ (accessed 2026-02-17)
- Oscar/Hecke integer genera manual: https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genera/ (accessed 2026-02-18)
- Oscar/Hecke hermitian genera manual: https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genusherm/ (accessed 2026-02-18)
- Oscar/Hecke lattices-with-isometry manual: https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/ (accessed 2026-02-17)
- Oscar/Hecke torsion-quadratic-modules-with-isometry manual: https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/ (accessed 2026-02-17)
- In-repo localized provenance for `ZZLatWithIsom` attribute-forwarding survey: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom_online_provenance_2026-02-17.md`
- Vinberg docs (Oscar legacy path): https://docs.oscar-system.org/v1.2/NumberTheory/vinberg/
- Existing in-repo canonical detail: `julia_lattice_methods_reference.md`
