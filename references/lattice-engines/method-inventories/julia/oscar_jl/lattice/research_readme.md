# Julia Lattice Methods Reference
## Lattice = free ℤ-module with symmetric bilinear form

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Requires or only meaningful for **positive definite** forms |
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[INDEF]` | Works correctly for **indefinite** signatures |
| `[DEFINITE]` | Requires **definite** form (positive-definite or negative-definite); indefinite forms raise error or return invalid results |
| `[DEG]` | Works with **degenerate** forms |
| `[EUCLID]` | Uses ambient Euclidean norm I_n; bilinear form not independently specified |
| `[GAP]` | Delegates to **GAP** |
| `[FLINT]` | Delegates to **FLINT** (via Nemo) |

---

## 1. Indefinite.jl

`[INDEF]` — Integral indefinite quadratic forms. Isometry classification and orbit enumeration under $GL(n,\mathbb{Z})$. ~90% GAP code. Not a registered package (install via GitHub URL).

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `INDEF_FORM_TestEquivalence(Q1, Q2)` | Test $GL(n,\mathbb{Z})$-equivalence of two indefinite forms; returns explicit unimodular transformation if equivalent | `[INDEF, GAP]` |
| `INDEF_FORM_AutomorphismGroup(Q)` | Finite generating set for $\text{Aut}(L)$ of an indefinite form ($O(L)$ often infinite) | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbitRepresentative(Q, C)` | Representatives (mod Aut) of integer solutions to $Q[v]=C$; $C=0$ gives primitive isotropic vectors | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)` | Orbit reps of $k$-dim totally isotropic subspaces, $k \le \min(p,q)$ | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)` | Orbit reps of isotropic flags of length $k$ | `[INDEF, GAP]` |

### Definiteness

- Assumes mixed signature (at least one positive and one negative direction)
- Not optimized for PD lattices; use Hecke/Oscar instead
- PD automorphism groups are finite and have no nonzero isotropic vectors — qualitatively different
- Algorithms exploit structure of indefinite forms: reduction to computations on finite quadratic modules, subgroup algorithms in GAP
- For PD lattices, traditional invariants (genus, theta series) and neighbor methods suffice; Indefinite.jl tackles the harder indefinite regime

### References

- Dutour Sikirić et al.; applied to K3 surface lattices and Enriques surfaces moduli
- Sengun–Sikiric (automorphism groups of lattices)

---

## 2. Hecke.jl (via Oscar)

Comprehensive number theory package (part of OSCAR). Builds on Nemo/FLINT and GAP. Handles PD, ND, and indefinite lattices, plus hermitian lattices over number fields.

### 2.1 Types

| Type | Description | Tags |
|------|-------------|------|
| `ZZLat` | Integral quadratic lattice over ℤ | `[INT, ND]` |
| `QuadLat` | Quadratic lattice over ℚ or number field | `[ND]` |
| `HermLat` | Hermitian lattice over quadratic extension | `[ND]` |
| `ZZGenus` | Genus symbol of an integer lattice | |
| `ZZLocalGenus` | Local genus symbol at a prime $p$ | |
| `TorQuadModule` | Torsion quadratic module (finite quadratic form on $L^\vee/L$) | |
| `QuadSpace` | Quadratic space over a field | |
| `HermSpace` | Hermitian space over a quadratic extension | |
| `ZZLatWithIsom` | Integer lattice paired with a finite-order isometry | |
| `QuadSpaceWithIsom` | Quadratic space paired with an isometry | |

### 2.2 Quadratic and hermitian spaces

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `quadratic_space(K, n)` / `quadratic_space(K, G)` | `K`: `Field`, `n`: `Int` / `G`: `Matrix` | `QuadSpace` | Quadratic space from dimension or Gram matrix | |
| `hermitian_space(E, n)` / `hermitian_space(E, G)` | `E`: `Field`, `n`: `Int` / `G`: `Matrix` | `HermSpace` | Hermitian space from dimension or Gram matrix | |
| `rank(V)` / `dim(V)` | `V`: `QuadSpace` | `Int` | Rank / dimension | |
| `gram_matrix(V)` / `gram_matrix(V, M)` | `V`: `QuadSpace`, `M`: `Matrix` (optional) | `Matrix` | Gram matrix (optionally on subspace $M$) | |
| `det(V)` / `discriminant(V)` | `V`: `QuadSpace` | `FieldElem` | Determinant / discriminant | |
| `diagonal(V)` | `V`: `QuadSpace` | `Vector{FieldElem}` | Diagonal entries after diagonalization | |
| `diagonal_with_transform(V)` | `V`: `QuadSpace` | `Tuple{Vector{FieldElem}, Matrix}` | Diagonal + transformation matrix | |
| `orthogonal_basis(V)` | `V`: `QuadSpace` | `Matrix` | Orthogonal basis | |
| `signature_tuple(V)` | `V`: `QuadSpace` | `Tuple{Int, Int, Int}` | $(n_+, n_0, n_-)$ | `[INDEF ok]` |
| `is_regular(V)` | `V`: `QuadSpace` | `Bool` | Non-degeneracy | |
| `is_quadratic(V)` / `is_hermitian(V)` | `V`: `AbstractSpace` | `Bool` | Type check | |
| `is_positive_definite(V)` / `is_negative_definite(V)` / `is_definite(V)` | `V`: `QuadSpace` | `Bool` | Definiteness | |
| `hasse_invariant(V, p)` / `witt_invariant(V, p)` | `V`: `QuadSpace`, `p`: `Int` | `Int` | Local invariants; value in $\{+1, -1\}$ | |
| `invariants(V)` | `V`: `QuadSpace` | `Tuple` | All rational invariants (dim, det, signatures, Hasse) | |
| `is_isometric(V, W)` / `is_isometric(V, W, p)` | `V`: `QuadSpace`, `W`: `QuadSpace`, `p`: `Int` (local form only) | `Bool` | Global / local isometry test | |
| `is_locally_represented_by(U, V, p)` | `U`: `QuadSpace`, `V`: `QuadSpace`, `p`: `Int` | `Bool` | Whether $U$ is locally represented by $V$ | |
| `is_represented_by(U, V)` | `U`: `QuadSpace`, `V`: `QuadSpace` | `Bool` | Whether $U$ is globally represented by $V$ | |
| `inner_product(V, v, w)` | `V`: `QuadSpace`, `v`: `Vector`, `w`: `Vector` | `FieldElem` | Evaluate bilinear form $b(v,w)$ | |
| `orthogonal_complement(V, M)` | `V`: `QuadSpace`, `M`: `Matrix` | `QuadSpace` | Orthogonal complement of subspace $M$ | |
| `orthogonal_projection(V, M)` | `V`: `QuadSpace`, `M`: `Matrix` | `Matrix` | Projection matrix onto subspace $M$ | |
| `is_isotropic(V, p)` | `V`: `QuadSpace`, `p`: `Int` | `Bool` | Local isotropy test | |
| `is_locally_hyperbolic(V, p)` | `V`: `HermSpace`, `p`: `Int` | `Bool` | Whether $V_p$ is hyperbolic (hermitian spaces) | |
| `restrict_scalars(V, K, α)` | `V`: `HermSpace`, `K`: `Field`, `α`: `FieldElem` | `QuadSpace` | Restriction of scalars | |
| `direct_sum(V, W)` / `direct_product` / `biproduct` | `V`: `QuadSpace`, `W`: `QuadSpace` | `Tuple{QuadSpace, ...}` | Categorical constructions returning space plus injection/projection maps | |

### 2.3 Construction

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `integer_lattice(; gram=G)` | `gram`: `Matrix` (keyword) | `ZZLat` | Integer lattice from Gram matrix | |
| `integer_lattice(B; gram=G)` | `B`: `Matrix`, `gram`: `Matrix` (optional keyword) | `ZZLat` | Integer lattice from basis matrix $B$ and optional Gram | |
| `lattice(V, B)` | `V`: `QuadSpace`, `B`: `Matrix` | `ZZLat` | Lattice in quadratic space $V$ with basis matrix $B$ | |
| `quadratic_lattice(K, gens; gram=M)` | `K`: `Field`, `gens`: `Vector`, `gram`: `Matrix` (keyword) | `QuadLat` | Lattice from generators + Gram matrix; `K=QQ` → `ZZLat` | `[INDEF ok]` |
| `hermitian_lattice(E, gens; gram=M)` | `E`: `Field`, `gens`: `Vector`, `gram`: `Matrix` (keyword) | `HermLat` | Hermitian lattice over quadratic extension E | |
| `root_lattice(:A, n)` / `(:D, n)` / `(:E, n)` / `(:I, n)` | `Symbol`, `n`: `Int` | `ZZLat` | Named root lattice | `[PD]` |
| `hyperbolic_plane_lattice(n)` | `n`: `Int` | `ZZLat` | Hyperbolic plane $U$ scaled by $n$ | `[INDEF]` |
| `leech_lattice()` | — | `ZZLat` | Rank-24 Leech lattice | `[PD]` |
| `k3_lattice()` | — | `ZZLat` | K3 surface lattice $U^3 \oplus E_8(-1)^2$ | `[INDEF]` |
| `mukai_lattice()` | — | `ZZLat` | Rank-24 Mukai lattice (K3 theory); optional extended form | `[INDEF]` |
| `hyperkaehler_lattice(:K3, n=3)` | `Symbol`, `n`: `Int` (optional) | `ZZLat` | Hyperkähler intersection form (sig $(3,19)$ or similar) | `[INDEF]` |
| `rescale(L, r)` | `L`: `ZZLat`, `r`: `RingElement` | `ZZLat` | New lattice with Gram $r \cdot G$; use `rescale(L, -1)` to flip sign of ND lattice | |

### 2.4 Intrinsic data

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `gram_matrix(L)` | `L`: `ZZLat` | `Matrix{QQFieldElem}` | Gram matrix | |
| `basis_matrix(L)` | `L`: `ZZLat` | `Matrix{QQFieldElem}` | Basis matrix | |
| `ambient_space(L)` | `L`: `ZZLat` | `QuadSpace` | Ambient quadratic space | |
| `rational_span(L)` | `L`: `ZZLat` | `QuadSpace` | Rational span as quadratic space | |
| `rank(L)` | `L`: `ZZLat` | `Int` | Rank | |
| `degree(L)` | `L`: `ZZLat` | `Int` | Degree (ambient dimension) | |
| `signature_tuple(L)` | `L`: `ZZLat` | `Tuple{Int, Int, Int}` | $(n_{+}, n_{0}, n_{-})$ (positive, zero, negative counts) | `[INDEF ok]` |
| `det(L)` | `L`: `ZZLat` | `QQFieldElem` | Determinant of Gram | |
| `discriminant(L)` | `L`: `ZZLat` | `ZZRingElem` | Discriminant | |
| `scale(L)` | `L`: `ZZLat` | `ZZIdeal` | Scale ideal (generated by $b(x,y)$ for all $x,y \in L$) | |
| `norm(L)` | `L`: `ZZLat` | `ZZIdeal` | Norm ideal (generated by $q(x)$ for all $x \in L$) | |
| `is_positive_definite(L)` | `L`: `ZZLat` | `Bool` | All eigenvalues > 0 | `[PD]` |
| `is_negative_definite(L)` | `L`: `ZZLat` | `Bool` | All eigenvalues < 0 | |
| `is_definite(L)` | `L`: `ZZLat` | `Bool` | Positive or negative definite (not indefinite or degenerate) | |
| `is_even(L)` | `L`: `ZZLat` | `Bool` | All $(x,x) \in 2\mathbb{Z}$ | |
| `is_integral(L)` | `L`: `ZZLat` | `Bool` | All $b(x,y) \in \mathbb{Z}$ | |
| `is_unimodular(L)` | `L`: `ZZLat` | `Bool` | $|\det G| = 1$ | |
| `is_primary(L, p)` | `L`: `ZZLat`, `p`: `Int` | `Bool` | $L^\vee/L$ is a $p$-group | |
| `is_primary_with_prime(L)` | `L`: `ZZLat` | `Tuple{Bool, Int}` | Returns `(true, p)` if primary | |
| `is_elementary(L, p)` | `L`: `ZZLat`, `p`: `Int` | `Bool` | $L^\vee/L \cong (\mathbb{Z}/p)^k$ | |
| `is_elementary_with_prime(L)` | `L`: `ZZLat` | `Tuple{Bool, Int}` | Returns `(true, p)` if elementary | |

### 2.5 Reduction

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `lll(L; same_ambient=true, redo=false, ctx=...)` | `L`: `ZZLat`, `same_ambient`: `Bool`, `redo`: `Bool`, `ctx`: `LLLContext` | `ZZLat` | LLL-reduced basis; `redo=true` forces recomputation even if cached; `ctx` specifies Lovász parameters | `[INDEF ok, FLINT]` |

- PD: specify Lovász parameters via `LLLContext(δ, η)` passed as `ctx`
- INDEF: runs but "shorter" is w.r.t. a majorant, not the indefinite form itself

### 2.6 Vector enumeration

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `short_vectors(L, [lb=0,] ub, [elem_type=ZZRingElem]; check=true)` | `L`: `ZZLat`, `lb`: `Integer` (optional, default 0), `ub`: `Integer`, `elem_type`: type (optional, default `ZZRingElem`), `check`: `Bool` (keyword, default `true`) | `Vector{Tuple{Vector{elem_type}, QQFieldElem}}` | Nonzero vectors with $lb \le \|v\|^2 \le ub$ (up to sign); requires `L` definite; `check=true` validates definiteness before enumeration | `[PD]` |
| `short_vectors_iterator(L, lb, ub)` | `L`: `ZZLat`, `lb`: `Integer`, `ub`: `Integer` | Iterator | Lazy iterator version of `short_vectors` | `[PD]` |
| `shortest_vectors(L, [elem_type=ZZRingElem]; check=true)` | `L`: `ZZLat`, `elem_type`: type (optional, default `ZZRingElem`), `check`: `Bool` (keyword, default `true`) | `Vector{Tuple{Vector{elem_type}, QQFieldElem}}` | Shortest vectors and their squared norm; requires `L` definite | `[PD]` |
| `close_vectors(L::ZZLat, v::Vector, [lb,] ub; check::Bool=false)` | `L`: `ZZLat`, `v`: `Vector`, `lb`: `Integer` (optional), `ub`: `Integer`, `check`: `Bool` | `Vector{Tuple{Vector{Int}, QQFieldElem}}` | Returns lattice points $x$ with $b(v-x, v-x) \le ub$; Fincke–Pohst enumeration; **`check` defaults to `false`** (not `true`) | `[PD]` |
| `short_vectors_affine(S, v, α, d)` | `S`: `ZZLat`, `v`: `Vector`, `α`: `RingElement`, `d`: `RingElement` | `Vector` | Vectors $x \in S$ with $x^2 = d$ and $x \cdot v = \alpha$ (Vinberg) | `[INDEF]` |
| `vectors_of_square_and_divisibility(L, n, d)` | `L`: `ZZLat`, `n`: `Integer`, `d`: `Integer` | `Vector{Vector{Int}}` | Vectors $v$ with $v^2 = n$ and divisibility $d$ in $L$ | `[PD]` |
| `enumerate_quadratic_triples(L, ...)` | `L`: `ZZLat`, `...` | `Vector` | Enumerate quadratic solutions in lattice | `[PD]` |
| `minimum(L)` | `L`: `ZZLat` | `ZZRingElem` | Squared length of shortest nonzero vector | `[PD]` |
| `kissing_number(L)` | `L`: `ZZLat` | `Int` | Number of shortest vectors | `[PD]` |

- ND lattices: use `rescale(L, -1)` then enumerate (no scalar rescaling makes INDEF → PD)
- INDEF: `short_vectors` / `shortest_vectors` refuse; use `short_vectors_affine` or genus methods
- `close_vectors` with `check=false` runs on INDEF but result is ill-posed (distances can be negative/zero)

### 2.7 Genus and classification

#### ZZGenus methods

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `genus(L::ZZLat)` | `L`: `ZZLat` | `ZZGenus` | Genus symbol (local invariants at all primes) | `[INDEF ok]` |
| `genus(A::MatElem)` | `A`: `MatElem` | `ZZGenus` | Genus from Gram matrix | `[INDEF ok]` |
| `genus(L, p)` | `L`: `ZZLat`, `p`: `Int` | `ZZLocalGenus` | Local genus at prime $p$ | |
| `integer_genera(sig_pair::Vector{Int}, det::RationalUnion; min_scale=min(1,abs(det)), max_scale=max(1,abs(det)), even::Bool=false)` | `sig_pair`: `Vector{Int}` (also accepts `Tuple{Int,Int}`), `det`: `RationalUnion`, `min_scale`: `RationalUnion` (keyword), `max_scale`: `RationalUnion` (keyword), `even`: `Bool` (keyword, default **`false`**) | `Vector{ZZGenus}` | Enumerate all genera with given signature and determinant; `even=false` allows both even and odd lattices (default); `min_scale`/`max_scale` bound Jordan-block scales | |
| `direct_sum(G1::ZZGenus, G2::ZZGenus)` | `G1`: `ZZGenus`, `G2`: `ZZGenus` | `ZZGenus` | Genus of the orthogonal direct sum | |
| `representative(gen)` | `gen`: `ZZGenus` | `ZZLat` | Concrete lattice for a genus class | |
| `representatives(gen)` | `gen`: `ZZGenus` | `Vector{ZZLat}` | All classes in genus | |
| `mass(gen)` | `gen`: `ZZGenus` | `QQFieldElem` | Mass of the genus | |
| `dim(gen)` / `rank(gen)` | `gen`: `ZZGenus` | `Int` | Dimension / rank of genus | |
| `signature(gen)` | `gen`: `ZZGenus` | `Tuple{Int, Int}` | Signature pair | |
| `det(gen)` | `gen`: `ZZGenus` | `ZZRingElem` | Determinant | |
| `iseven(gen)` | `gen`: `ZZGenus` | `Bool` | Evenness | |
| `is_definite(gen)` | `gen`: `ZZGenus` | `Bool` | Definiteness | |
| `level(gen)` | `gen`: `ZZGenus` | `ZZRingElem` | Level | |
| `scale(gen)` / `norm(gen)` | `gen`: `ZZGenus` | `ZZIdeal` | Scale / norm of genus | |
| `primes(gen)` | `gen`: `ZZGenus` | `Vector{Int}` | List of primes appearing in local symbols | |
| `is_integral(gen)` | `gen`: `ZZGenus` | `Bool` | Integrality | |
| `local_symbol(gen, p)` | `gen`: `ZZGenus`, `p`: `Int` | `ZZLocalGenus` | Retrieve local genus at prime $p$ | |
| `quadratic_space(gen)` | `gen`: `ZZGenus` | `QuadSpace` | Quadratic space representing the genus | |
| `rational_representative(gen)` | `gen`: `ZZGenus` | `QuadSpace` | Rational form | |
| `rescale(gen, a)` | `gen`: `ZZGenus`, `a`: `RingElement` | `ZZGenus` | Rescaled genus | |
| `represents(G1, G2)` | `G1`: `ZZGenus`, `G2`: `ZZGenus` | `Bool` | Whether genus $G_1$ represents $G_2$ | |

#### ZZLocalGenus methods

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `prime(S)` | `S`: `ZZLocalGenus` | `Int` | Underlying prime | |
| `iseven(S)` | `S`: `ZZLocalGenus` | `Bool` | Evenness at $p$ | |
| `symbol(S, scale)` | `S`: `ZZLocalGenus`, `scale`: `Int` | `ZZLocalGenusSymbol` | Jordan block invariants | |
| `hasse_invariant(S)` | `S`: `ZZLocalGenus` | `Int` | Hasse invariant | |
| `det(S)` | `S`: `ZZLocalGenus` | `ZZRingElem` | Determinant | |
| `dim(S)` / `rank(S)` | `S`: `ZZLocalGenus` | `Int` | Dimension / rank | |
| `excess(S)` | `S`: `ZZLocalGenus` | `Int` | $p$-excess | |
| `signature(S)` | `S`: `ZZLocalGenus` | `Tuple{Int, Int}` | $p$-signature | |
| `oddity(S)` | `S`: `ZZLocalGenus` | `Int` | 2-adic oddity | |
| `scale(S)` / `norm(S)` / `level(S)` | `S`: `ZZLocalGenus` | `ZZIdeal` | Scale / norm / level | |
| `representative(S)` | `S`: `ZZLocalGenus` | `ZZLat` | Representative lattice | |
| `gram_matrix(S)` | `S`: `ZZLocalGenus` | `QQMatrix` | Gram matrix | |
| `rescale(S, a)` | `S`: `ZZLocalGenus`, `a`: `RingElement` | `ZZLocalGenus` | Rescaled local genus | |
| `direct_sum(S1, S2)` | `S1`: `ZZLocalGenus`, `S2`: `ZZLocalGenus` | `ZZLocalGenus` | Local genus direct sum | |
| `represents(S1, S2)` | `S1`: `ZZLocalGenus`, `S2`: `ZZLocalGenus` | `Bool` | Local representation check | |

#### Discriminant group and classification

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `discriminant_group(L)` | `L`: `ZZLat` | `TorQuadModule` | $L^\vee / L$ as torsion quadratic module | |
| `genus_representatives(L)` | `L`: `ZZLat` | `Vector{ZZLat}` | All isometry class representatives in the genus of $L$ | |
| `Hecke.quadratic_lattice_database()` | — | `LatticeDatabase` | DB of lattices rank ≥ 3 with class number 1 or 2 | `[PD]` |

- Genus relies on local theory (Jordan decomposition, local densities) via MAGMA/GAP
- INDEF genus: can compute discriminant forms and genera even for indefinite lattices
- Handles even unimodular indefinite forms $II_{p,q}$
- Two even INDEF lattices of the same genus are often isometric (Hasse–Minkowski); genus invariants may suffice for equivalence

### 2.8 Automorphism and isometry

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `automorphism_group_generators(L; ambient_representation=true, depth=-1, bacher_depth=0)` | `L`: `AbstractLat`, `ambient_representation`: `Bool`, `depth`: `Int`, `bacher_depth`: `Int` | `Vector{QQMatrix}` | Generators of `Aut(L)`; upstream requires `is_definite(L)` (positive or negative definite); `ambient_representation=true` returns matrices in ambient-space coordinates; `ambient_representation=false` returns `ZZMatrix` in lattice-basis coordinates | `[DEFINITE, GAP]` |
| `automorphism_group_order(L; depth=-1, bacher_depth=0)` | `L`: `AbstractLat`, `depth`: `Int`, `bacher_depth`: `Int` | `ZZRingElem` | Order of `Aut(L)`; upstream requires `is_definite(L)` (positive or negative definite) | `[DEFINITE]` |
| `is_isometric(L1, L2)` | `L1`: `AbstractLat`, `L2`: `AbstractLat` | `Bool` | Isometry test; upstream requires `is_definite(L1)` and `is_definite(L2)` (positive or negative definite); uses LLL to rescale ND to PD before comparison | `[DEFINITE]` |
| `is_isometric_with_isometry(L1, L2; depth=3, bacher_depth=5, ambient_representation=true)` | `L1`: `AbstractLat`, `L2`: `AbstractLat`, `depth`: `Int`, `bacher_depth`: `Int`, `ambient_representation`: `Bool` | `Tuple{Bool, QQMatrix}` | Returns `(true, f)` when isometry exists, `(false, zero_matrix(QQ, 0, 0))` otherwise; upstream requires `is_definite(L1)` and `is_definite(L2)` | `[DEFINITE]` |
| `is_locally_isometric(L1, L2, p)` | `L1`: `AbstractLat`, `L2`: `AbstractLat`, `p`: `Int` | `Bool` | $p$-adic isometry test | |
| `is_rationally_isometric(L1, L2)` | `L1`: `AbstractLat`, `L2`: `AbstractLat` | `Bool` | Rational (ℚ) isometry test | `[INDEF ok]` |
| `hasse_invariant(L, p)` | `L`: `ZZLat`, `p`: `Int` | `Int` | Hasse invariant at prime $p$; value in $\{+1, -1\}$ | |
| `witt_invariant(L, p)` | `L`: `ZZLat`, `p`: `Int` | `Int` | Witt invariant at prime $p$; value in $\{+1, -1\}$ | |

- DEFINITE (PD or ND): `automorphism_group_generators` / `automorphism_group_order` support both positive and negative definite lattices; finite groups computed via shortest vectors + symmetries (e.g. $E_8$ Weyl group); negative definite lattices may be passed directly (no need to rescale by $-1$ first)
- Oscar also exposes "Lattices with isometry" and "Groups of automorphisms" sections
- INDEF: Aut(L) infinite; use Indefinite.jl or Vinberg's algorithm for reflection subgroups
- Rational/local isometry tests work for all signatures and are key ingredients in genus theory

### 2.9 Module operations and embeddings

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `direct_sum(L1, L2)` | `L1`: `ZZLat`, `L2`: `ZZLat` | `Tuple{ZZLat, AbstractSpaceMor, AbstractSpaceMor}` | Orthogonal direct sum; returns $(L, i_1, i_2)$ with injection maps | |
| `direct_product(L1, L2)` | `L1`: `ZZLat`, `L2`: `ZZLat` | `Tuple{ZZLat, AbstractSpaceMor, AbstractSpaceMor}` | Direct product; returns $(L, p_1, p_2)$ with projection maps | |
| `biproduct(L1, L2)` | `L1`: `ZZLat`, `L2`: `ZZLat` | `Tuple{ZZLat, AbstractSpaceMor, AbstractSpaceMor, AbstractSpaceMor, AbstractSpaceMor}` | Biproduct; returns $(L, i_1, i_2, p_1, p_2)$ | |
| `intersect(L1, L2)` | `L1`: `ZZLat`, `L2`: `ZZLat` | `ZZLat` | Intersection in common ambient space | |
| `+(L1, L2)` | `L1`: `ZZLat`, `L2`: `ZZLat` | `ZZLat` | Sum of lattices in common ambient | |
| `*(n, L)` | `n`: `Integer`, `L`: `ZZLat` | `ZZLat` | Scalar multiple of lattice | |
| `lattice_in_same_ambient_space(L, B)` | `L`: `ZZLat`, `B`: `Matrix` | `ZZLat` | Sublattice with basis B in ambient of L | |
| `orthogonal_submodule(L, S)` | `L`: `ZZLat`, `S`: `ZZLat` | `ZZLat` | Orthogonal complement of S in L | |
| `dual(L)` | `L`: `ZZLat` | `ZZLat` | Dual lattice $L^\vee$ | |
| `is_sublattice(L, S)` | `L`: `ZZLat`, `S`: `ZZLat` | `Bool` | Whether $S \subseteq L$ | |
| `is_sublattice_with_relations(L, S)` | `L`: `ZZLat`, `S`: `ZZLat` | `Tuple{Bool, QQMatrix}` | Sublattice test + inclusion relation matrix | |
| `is_primitive(L, S)` | `L`: `ZZLat`, `S`: `ZZLat` | `Bool` | Whether S is primitive in L ($L/S$ torsion-free) | |
| `primitive_closure(L, S)` | `L`: `ZZLat`, `S`: `ZZLat` | `ZZLat` | Smallest primitive sublattice of $L$ containing $S$ | |
| `divisibility(L, v)` | `L`: `ZZLat`, `v`: `Vector` | `ZZRingElem` | Divisibility of vector $v$ in $L$ | |
| `in(v, L)` | `v`: `Vector`, `L`: `ZZLat` | `Bool` | Vector membership test | |
| `irreducible_components(L)` | `L`: `ZZLat` | `Vector{ZZLat}` | Decompose into orthogonally irreducible components | |

#### Overlattices and embeddings

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `glue_map(L, S, gen_imgs)` | `L`: `ZZLat`, `S`: `ZZLat`, `gen_imgs`: `Vector` | `TorQuadModuleMap` | Construct glue map for primitive extension | |
| `overlattice(glue_map)` | `glue_map`: `TorQuadModuleMap` | `ZZLat` | Build overlattice from a glue map | |
| `primitive_extension(L1, L2, glue_map)` | `L1`: `ZZLat`, `L2`: `ZZLat`, `glue_map`: `TorQuadModuleMap` | `ZZLat` | Nikulin gluing: lattice from isometric discriminant subquotients | |
| `local_modification(M, L, p)` | `M`: `ZZLat`, `L`: `ZZLat`, `p`: `Int` | `ZZLat` | Local modification at prime $p$; docs assume `M` is $\mathbf{Z}_p$-maximal and `L` is isomorphic to `M` over $\mathbf{Q}_p$ | |
| `maximal_integral_lattice(L)` | `L`: `ZZLat` | `ZZLat` | Maximal integral overlattice | |
| `is_maximal_integral(L)` | `L`: `ZZLat` | `Bool` | Whether $L$ is already maximal integral | |
| `is_maximal(L)` | `L`: `ZZLat` | `Bool` | Whether $L$ is maximal | |
| `embed(L, gen)` | `L`: `ZZLat`, `gen`: `ZZGenus` | `ZZLat` | Embed lattice into a genus | |
| `embed_in_unimodular(L, ...)` | `L`: `ZZLat` | `ZZLat` | Embed into a unimodular lattice; current Hecke docs note this presently works only for even lattices | |

#### Endomorphism-based sublattices

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `kernel_lattice(L, f)` | `L`: `ZZLat`, `f`: `QQMatrix` | `ZZLat` | Kernel of endomorphism $f$ on $L$ | |
| `invariant_lattice(L, G)` | `L`: `ZZLat`, `G`: `MatGroup` | `ZZLat` | Fixed-point sublattice $L^G$ under finite group action | |
| `coinvariant_lattice(L, G)` | `L`: `ZZLat`, `G`: `MatGroup` | `ZZLat` | Orthogonal complement of $L^G$ in $L$ for finite group action | |
| `invariant_coinvariant_pair(L, f)` | `L`: `ZZLat`, `f`: `Union{QQMatrix, Vector{QQMatrix}, MatGroup}` | `Tuple{ZZLat, ZZLat}` | Compute invariant/coinvariant pair simultaneously from a single isometry, a list of matrices, or a matrix group action | |

#### Root lattice recognition

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `root_lattice_recognition(L)` | `L`: `ZZLat` | `Tuple{Vector{Pair{Symbol, Int}}, ZZLat}` | Identify ADE type of root sublattice; returns type list and root sublattice | `[PD]` |
| `root_lattice_recognition_fundamental(L)` | `L`: `ZZLat` | `Tuple{Vector{Pair{Symbol, Int}}, ZZLat}` | Find fundamental root system; returns ADE type list and root sublattice | `[PD]` |
| `ADE_type(L)` | `L`: `ZZLat` | `Pair{Symbol, Int}` | Determine root lattice type (e.g. `:A => 2`) | `[PD]` |
| `coxeter_number(L)` | `L`: `ZZLat` | `Int` | Coxeter number | `[PD]` |
| `highest_root(L)` | `L`: `ZZLat` | `ZZMatrix` | Highest root coordinates | `[PD]` |

### 2.10 Vinberg's algorithm

`[INDEF]` — For hyperbolic lattices (signature $(1,n)$). Enumerates simple roots defining the Weyl chamber of the reflection group.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `vinberg_algorithm(Q, ub; v0, root_lengths, direction_vector)` | `Q`: `ZZMatrix`, `ub`: `Integer`, `v0`: `Vector` (keyword), `root_lengths`: `Vector` (keyword), `direction_vector`: `Vector` (keyword) | `Vector{ZZMatrix}` | Fundamental roots of hyperbolic reflection lattice from Gram matrix | `[INDEF]` |
| `vinberg_algorithm(S, ub; v0, root_lengths, direction_vector)` | `S`: `ZZLat`, `ub`: `Integer`, `v0`: `Vector` (keyword), `root_lengths`: `Vector` (keyword), `direction_vector`: `Vector` (keyword) | `Vector{ZZMatrix}` | Same, from `ZZLat` of signature $(1,0,n)$ | `[INDEF]` |
| `short_vectors_affine(S, v, α, d)` | `S`: `ZZLat`, `v`: `Vector`, `α`: `RingElement`, `d`: `RingElement` | `Vector` | Vectors $x$ with $x^2 = d$, $x \cdot v = \alpha$ (used internally by Vinberg) | `[INDEF]` |

Computes Coxeter diagram of reflecting hyperplanes. Applicable to even hyperbolic lattices ($U \oplus E_8(-1)$, etc.). Implementation follows Algorithm 2.2 of Jingyu Shi 2015.

### 2.11 Discriminant groups (`TorQuadModule`)

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `torsion_quadratic_module(M, N)` | `M`: `ZZLat`, `N`: `ZZLat` | `TorQuadModule` | Torsion quadratic module $M/N$ | |
| `torsion_quadratic_module(q::QQMatrix)` | `q`: `QQMatrix` | `TorQuadModule` | From rational Gram matrix | |
| `discriminant_group(L)` | `L`: `ZZLat` | `TorQuadModule` | $L^\vee / L$ as torsion quadratic module | |
| `abelian_group(T)` | `T`: `TorQuadModule` | `FinGenAbGroup` | Underlying abelian group | |
| `cover(T)` | `T`: `TorQuadModule` | `ZZLat` | Cover lattice | |
| `relations(T)` | `T`: `TorQuadModule` | `ZZLat` | Relation lattice | |
| `gram_matrix_bilinear(T)` | `T`: `TorQuadModule` | `QQMatrix` | Bilinear Gram matrix over $\mathbb{Q}/\mathbb{Z}$ | |
| `gram_matrix_quadratic(T)` | `T`: `TorQuadModule` | `QQMatrix` | Quadratic Gram matrix over $\mathbb{Q}/2\mathbb{Z}$ | |
| `value_module(T)` | `T`: `TorQuadModule` | `FinGenAbGroup` | Value module of bilinear form | |
| `value_module_quadratic_form(T)` | `T`: `TorQuadModule` | `FinGenAbGroup` | Value module of quadratic form | |
| `modulus_bilinear_form(T)` | `T`: `TorQuadModule` | `QQFieldElem` | Modulus of bilinear form | |
| `modulus_quadratic_form(T)` | `T`: `TorQuadModule` | `QQFieldElem` | Modulus of quadratic form | |
| `quadratic_product(a)` | `a`: `TorQuadModuleElem` | `QQFieldElem` | $q(a)$ for element $a \in T$ | |
| `inner_product(a, b)` | `a`: `TorQuadModuleElem`, `b`: `TorQuadModuleElem` | `QQFieldElem` | $b(a,b)$ for elements $a,b \in T$ | |
| `lift(a)` | `a`: `TorQuadModuleElem` | `Vector{QQFieldElem}` | Lift element to cover lattice | |
| `representative(a)` | `a`: `TorQuadModuleElem` | `Vector{QQFieldElem}` | Representative of element | |
| `orthogonal_submodule(T, S)` | `T`: `TorQuadModule`, `S`: `TorQuadModule` | `TorQuadModule` | Orthogonal complement of submodule $S$ in $T$ | |
| `is_isometric_with_isometry(T, U)` | `T`: `TorQuadModule`, `U`: `TorQuadModule` | `Tuple{Bool, TorQuadModuleMap}` | Isometry test returning `(Bool, map)` (or `(false, 0)` if no isometry). Upstream states the contract assumes either equal quadratic-form moduli or prior rescaling to match | |
| `is_anti_isometric_with_anti_isometry(T, U)` | `T`: `TorQuadModule`, `U`: `TorQuadModule` | `Tuple{Bool, TorQuadModuleMap}` | Anti-isometry test returning `(Bool, anti_map)` (or `(false, 0)` if absent) | |
| `is_degenerate(T)` | `T`: `TorQuadModule` | `Bool` | Degeneracy test | |
| `is_semi_regular(T)` | `T`: `TorQuadModule` | `Bool` | Semi-regularity test | |
| `radical_bilinear(T)` | `T`: `TorQuadModule` | `TorQuadModule` | Radical of bilinear form | |
| `radical_quadratic(T)` | `T`: `TorQuadModule` | `TorQuadModule` | Radical of quadratic form | |
| `normal_form(T; partial=false)` | `T`: `TorQuadModule`, `partial`: `Bool` | `TorQuadModule` | Normal form of torsion quadratic module | |
| `brown_invariant(T)` | `T`: `TorQuadModule` | `Int` | Brown invariant (mod 8) | |
| `snf(T)` | `T`: `TorQuadModule` | `TorQuadModule` | Smith normal form | |
| `is_snf(T)` | `T`: `TorQuadModule` | `Bool` | Smith normal form test | |
| `rescale(T, k)` | `T`: `TorQuadModule`, `k`: `RingElement` | `TorQuadModule` | Rescaled module | |
| `genus(T, sig_pair)` | `T`: `TorQuadModule`, `sig_pair`: `Tuple{Int, Int}` | `ZZGenus` | Genus from discriminant form + signature | |
| `is_genus(T, sig_pair)` | `T`: `TorQuadModule`, `sig_pair`: `Tuple{Int, Int}` | `Bool` | Check if a genus with this discriminant form exists | |
| `direct_sum(T1, T2)` | `T1`: `TorQuadModule`, `T2`: `TorQuadModule` | `TorQuadModule` | Direct sum | |
| `direct_product(T1, T2)` | `T1`: `TorQuadModule`, `T2`: `TorQuadModule` | `TorQuadModule` | Direct product | |
| `biproduct(T1, T2)` | `T1`: `TorQuadModule`, `T2`: `TorQuadModule` | `TorQuadModule` | Biproduct | |
| `submodules(T::TorQuadModule; ...)` | `T`: `TorQuadModule`, `order`: `Int` (keyword), `index`: `Int` (keyword), `subtype`: `Vector{Int}` (keyword), `quotype`: `Vector{Int}` (keyword) | Iterator | Iterator over submodules of `T` with keyword filters | |
| `stable_submodules(T::TorQuadModule, act::Vector{TorQuadModuleMap}; ...)` | `T`: `TorQuadModule`, `act`: `Vector{TorQuadModuleMap}`, `quotype`: `Vector{Int}` (keyword) | Iterator | Iterator over submodules stable under endomorphisms | |

### 2.12 Hermitian lattices (`HermLat` / `QuadLat`)

Methods shared with `ZZLat` (construction, rank, det, etc.) are listed in §2.2–2.8. Additional methods specific to lattices over number fields:

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `base_field(L)` / `base_ring(L)` | `L`: `AbstractLat` | `Field` / `Ring` | Base field $K$ / ring of integers $\mathcal{O}_K$ | |
| `fixed_field(L)` / `fixed_ring(L)` | `L`: `HermLat` | `Field` / `Ring` | Fixed field under involution / its ring of integers | |
| `involution(L)` | `L`: `HermLat` | `Map` | Involution of the hermitian form | |
| `pseudo_matrix(L)` / `pseudo_basis(L)` | `L`: `AbstractLat` | `PMat` / `Vector{Tuple{Ideal, Vector}}` | Pseudo-matrix / pseudo-basis (fractional ideals + vectors) | |
| `coefficient_ideals(L)` | `L`: `AbstractLat` | `Vector{Ideal}` | Coefficient ideals of pseudo-basis | |
| `absolute_basis(L)` / `absolute_basis_matrix(L)` | `L`: `AbstractLat` | `Vector` / `Matrix` | Absolute $\mathbb{Z}$-basis / basis matrix | |
| `generators(L)` / `gram_matrix_of_generators(L)` | `L`: `AbstractLat` | `Vector` / `Matrix` | Generators and their Gram matrix | |
| `local_basis_matrix(L, p)` | `L`: `AbstractLat`, `p`: `Ideal` | `Matrix` | Basis matrix of local completion $L_p$ | |
| `jordan_decomposition(L, p)` | `L`: `AbstractLat`, `p`: `Ideal` | `Tuple` | Jordan decomposition at prime $p$ | |
| `is_isotropic(L, p)` | `L`: `AbstractLat`, `p`: `Ideal` | `Bool` | Whether $L_p$ is isotropic | |
| `is_modular(L)` / `is_modular(L, p)` | `L`: `AbstractLat`, `p`: `Ideal` (local form) | `Bool` | Modular lattice test (global / local) | |
| `can_scale_totally_positive(L)` | `L`: `HermLat` | `Bool` | Whether the form can be rescaled to totally positive | |
| `volume(L)` | `L`: `AbstractLat` | `Ideal` | Volume ideal | |
| `is_maximal_integral(L)` / `is_maximal(L)` | `L`: `AbstractLat` | `Bool` | Maximality tests | |
| `maximal_integral_lattice(L)` | `L`: `AbstractLat` | `AbstractLat` | Maximal integral overlattice | |

### 2.13 Quadratic spaces with isometry (`QuadSpaceWithIsom`)

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `quadratic_space_with_isometry(V, f; check)` | `V`: `QuadSpace`, `f`: `QQMatrix`, `check`: `Bool` | `QuadSpaceWithIsom` | Pair space $V$ with isometry matrix $f$ (pass `check` explicitly; upstream docs currently show conflicting default wording) | |
| `quadratic_space_with_isometry(V; neg=false)` | `V`: `QuadSpace`, `neg`: `Bool` | `QuadSpaceWithIsom` | Pair with identity (or negation if `neg=true`) | |
| `space(Vf)` | `Vf`: `QuadSpaceWithIsom` | `QuadSpace` | Underlying quadratic space | |
| `isometry(Vf)` | `Vf`: `QuadSpaceWithIsom` | `QQMatrix` | Isometry matrix | |
| `order_of_isometry(Vf)` | `Vf`: `QuadSpaceWithIsom` | `Union{Int, PosInf}` | Order of isometry; `PosInf` for infinite-order; `-1` for rank-0 case | |
| `rank(Vf)` / `dim(Vf)` | `Vf`: `QuadSpaceWithIsom` | `Int` | Rank / dimension of underlying space | |
| `gram_matrix(Vf)` | `Vf`: `QuadSpaceWithIsom` | `QQMatrix` | Gram matrix of underlying space | |
| `det(Vf)` / `discriminant(Vf)` | `Vf`: `QuadSpaceWithIsom` | `QQFieldElem` | Determinant / discriminant of underlying space | |
| `diagonal(Vf)` | `Vf`: `QuadSpaceWithIsom` | `Vector{QQFieldElem}` | Diagonal entries of underlying space | |
| `signature_tuple(Vf)` | `Vf`: `QuadSpaceWithIsom` | `Tuple{Int, Int, Int}` | Signature triple $(n_+, n_0, n_-)$ of underlying space | |
| `is_definite(Vf)` / `is_positive_definite(Vf)` / `is_negative_definite(Vf)` | `Vf`: `QuadSpaceWithIsom` | `Bool` | Definiteness of underlying space | |
| `characteristic_polynomial(Vf)` / `minimal_polynomial(Vf)` | `Vf`: `QuadSpaceWithIsom` | `QQPolyRingElem` | Characteristic / minimal polynomial of isometry | |
| `^(Vf, n)` | `Vf`: `QuadSpaceWithIsom`, `n`: `Int` | `QuadSpaceWithIsom` | Raise isometry to power $n$ | |
| `direct_sum(Vf...)` | `Vf`: `Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}` | `Tuple{QuadSpaceWithIsom, ...}` | Equivariant direct sum; binary form returns `(Vf, emb1, emb2)`; varargs and vector input accepted | |
| `rescale(Vf, a)` | `Vf`: `QuadSpaceWithIsom`, `a`: `RationalUnion` | `QuadSpaceWithIsom` | Rescale underlying space preserving isometry | |
| `rational_spinor_norm(Vf; b=-1)` | `Vf`: `QuadSpaceWithIsom`, `b`: `Int` | `QQFieldElem` | Rational spinor norm of isometry w.r.t. form `b·Φ`; default `b=-1` | |

### 2.14 Lattices with isometry (`ZZLatWithIsom`)

Pairs an integer lattice with a finite- or infinite-order isometry. Used for equivariant classification and K3/hyperkähler applications.

#### Construction

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `integer_lattice_with_isometry(L, f; check, ambient_representation)` | `L`: `ZZLat`, `f`: `QQMatrix`, `check`: `Bool`, `ambient_representation`: `Bool` | `ZZLatWithIsom` | Pair lattice $L$ with isometry matrix $f$; `ambient_representation` selects whether `f` is interpreted in the ambient-space basis (`true`) or in the fixed basis of `L` (`false`) | |
| `integer_lattice_with_isometry(L; neg=false)` | `L`: `ZZLat`, `neg`: `Bool` | `ZZLatWithIsom` | Pair with identity (or negation if `neg=true`) | |
| `lattice(Vf::QuadSpaceWithIsom)` | `Vf`: `QuadSpaceWithIsom` | `ZZLatWithIsom` | Extract lattice from space-with-isometry | |
| `lattice(Vf::QuadSpaceWithIsom, B)` | `Vf`: `QuadSpaceWithIsom`, `B`: `Matrix` | `ZZLatWithIsom` | Construct an integral lattice in ambient `Vf` from basis/generator matrix `B`; induced isometry is defined when the lattice is stable under ambient action | |
| `lattice_in_same_ambient_space(Lf, B)` | `Lf`: `ZZLatWithIsom`, `B`: `Matrix` | `ZZLatWithIsom` | Sublattice preserving ambient isometry | |

#### Accessors

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `isometry(Lf)` | `Lf`: `ZZLatWithIsom` | `QQMatrix` | Isometry matrix | |
| `ambient_isometry(Lf)` | `Lf`: `ZZLatWithIsom` | `QQMatrix` | Isometry on ambient space | |
| `ambient_space(Lf)` | `Lf`: `ZZLatWithIsom` | `QuadSpaceWithIsom` | Ambient quadratic space carrying the isometry | |
| `lattice(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZLat` | Underlying `ZZLat` | |
| `basis_matrix(Lf)` | `Lf`: `ZZLatWithIsom` | `QQMatrix` | Basis matrix of underlying lattice | |
| `order_of_isometry(Lf)` | `Lf`: `ZZLatWithIsom` | `Union{Int, PosInf}` | Order of lattice isometry `f`; upstream defines it as a divisor of the ambient isometry order and documents support for both finite- and infinite-order isometries | |
| `characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)` | `Lf`: `ZZLatWithIsom` | `QQPolyRingElem` | Polynomials of the isometry | |

#### Attributes

Upstream docs explicitly expose many `ZZLat` attributes on `ZZLatWithIsom`; these methods report invariants of the underlying lattice `L` in the pair `(L, f)` unless stated otherwise.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `rank(Lf)` / `degree(Lf)` | `Lf`: `ZZLatWithIsom` | `Int` | Rank and ambient degree inherited from the underlying lattice | |
| `gram_matrix(Lf)` / `det(Lf)` / `discriminant(Lf)` | `Lf`: `ZZLatWithIsom` | `QQMatrix` / `QQFieldElem` / `ZZRingElem` | Gram/determinant/discriminant invariants forwarded from `L` | |
| `signature_tuple(Lf)` | `Lf`: `ZZLatWithIsom` | `Tuple{Int, Int, Int}` | Lattice signature tuple `(n_{+}, n_{0}, n_{-})`; distinct from eigenspace signatures returned by `signatures(Lf)` | `[INDEF]` |
| `rational_span(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `QuadSpaceWithIsom` | Returns `QuadSpaceWithIsom` — the rational span of the underlying lattice, carrying the induced isometry | `[INDEF]` |
| `genus(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZGenus` | Genus of the underlying lattice `L` | `[INDEF]` |
| `minimum(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZRingElem` | Minimum of the underlying lattice; same positive-definite precondition as `minimum(L)` | `[PD]` |
| `scale(Lf)` / `norm(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZIdeal` | Scale and norm ideals forwarded from `L` | |
| `is_even(Lf)` / `is_integral(Lf)` / `is_unimodular(Lf)` | `Lf`: `ZZLatWithIsom` | `Bool` | Arithmetic predicates of the underlying lattice | |
| `is_primary(Lf, p)` / `is_primary_with_prime(Lf)` | `Lf`: `ZZLatWithIsom`, `p`: `Int` (first form only) | `Bool` / `Tuple{Bool, Int}` | `p`-primary discriminant-group predicates forwarded from `L` | |
| `is_elementary(Lf, p)` / `is_elementary_with_prime(Lf)` | `Lf`: `ZZLatWithIsom`, `p`: `Int` (first form only) | `Bool` / `Tuple{Bool, Int}` | Elementary discriminant-group predicates forwarded from `L` | |
| `is_positive_definite(Lf)` / `is_negative_definite(Lf)` / `is_definite(Lf)` | `Lf`: `ZZLatWithIsom` | `Bool` | Definiteness predicates inherited from `L` | |

#### Type classification

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `type(Lf)` | `Lf`: `ZZLatWithIsom` | `Dict` | Type of lattice-with-isometry (dictionary of invariants) | |
| `is_of_type(Lf, t)` | `Lf`: `ZZLatWithIsom`, `t`: `Dict` | `Bool` | Test against a type | |
| `is_of_same_type(Lf, Mg)` | `Lf`: `ZZLatWithIsom`, `Mg`: `ZZLatWithIsom` | `Bool` | Whether two lattices-with-isometry share the same type | |
| `is_of_hermitian_type(Lf)` | `Lf`: `ZZLatWithIsom` | `Bool` | Whether the isometry gives a hermitian structure | |
| `hermitian_structure(Lf)` | `Lf`: `ZZLatWithIsom` | `HermLat` | Extract hermitian lattice from hermitian-type isometry | |
| `trace_lattice_with_isometry(H)` | `H`: `HermLat` | `ZZLatWithIsom` | Recover `ZZLatWithIsom` from hermitian lattice via trace form | |
| `trace_lattice_with_isometry(H, res)` | `H`: `HermLat`, `res`: embedding | `ZZLatWithIsom` | Recover `ZZLatWithIsom` from hermitian lattice with an explicit residue-field embedding choice used in trace-equivalence setup | |
| `is_hermitian(t::Dict)` | `t`: `Dict` | `Bool` | Whether a type dictionary corresponds to hermitian type | |

#### Operations

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `^(Lf, n)` | `Lf`: `ZZLatWithIsom`, `n`: `Int` | `ZZLatWithIsom` | Raise isometry to power $n$ | |
| `direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)` | `Lf`: `ZZLatWithIsom` (varargs or `Vector`) | `Tuple{ZZLatWithIsom, ...}` | Equivariant direct sum of lattices with isometry; current upstream signatures accept varargs and vector input, with binary form returning `(Lf, emb1, emb2)` | |
| `dual(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZLatWithIsom` | Dual with induced isometry | |
| `lll(Lf)` | `Lf`: `ZZLatWithIsom` | `ZZLatWithIsom` | LLL with isometry carried along | |
| `rescale(Lf, a)` | `Lf`: `ZZLatWithIsom`, `a`: `RingElement` | `ZZLatWithIsom` | Rescale with isometry preserved | |
| `orthogonal_submodule(Lf, B)` | `Lf`: `ZZLatWithIsom`, `B`: `QQMatrix` | `ZZLatWithIsom` | Orthogonal complement with induced isometry | |

#### Kernel sublattices

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `kernel_lattice(Lf::ZZLatWithIsom, p::Union{ZZPolyRingElem, QQPolyRingElem})` | `Lf`: `ZZLatWithIsom`, `p`: `Union{ZZPolyRingElem, QQPolyRingElem}` | `ZZLatWithIsom` | Kernel of polynomial $p$ applied to the isometry $f$, as a sublattice with induced action; primitive in $L$ | |
| `kernel_lattice(Lf::ZZLatWithIsom, l::Integer)` | `Lf`: `ZZLatWithIsom`, `l`: `Integer` | `ZZLatWithIsom` | Kernel of $f^l - 1$ as a sublattice with induced action; primitive in $L$ | |
| `invariant_lattice(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `ZZLatWithIsom` | Fixed sublattice $L^f$ with induced isometry | |
| `coinvariant_lattice(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `ZZLatWithIsom` | Orthogonal complement of $L^f$ with induced isometry | |
| `invariant_coinvariant_pair(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `Tuple{ZZLatWithIsom, ZZLatWithIsom}` | Invariant and coinvariant sublattices simultaneously | |

#### Discriminant groups

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `discriminant_group(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `Tuple{TorQuadModule, AutomorphismGroupElem}` | Discriminant module plus the element of `O(D_L)` induced by `f` | |
| `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom; ambient_representation::Bool=true)` | `Lf`: `ZZLatWithIsom`, `ambient_representation`: `Bool` | `TorQuadModuleWithIsom` | Wraps the discriminant module with induced isometry action; `ambient_representation` selects basis for representing the action | |
| `image_centralizer_in_Oq(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `Tuple{AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism}` | Image $G_{L,f}$ of the centralizer map $O(L,f) \to O(D_L, D_f)$; computable directly for definite lattices, ±identity isometries, and Euler-totient-rank cases; general case uses hermitian Miranda-Morrison theory, which **requires $L$ even** (local snapshot `latwithisom.md`) | |
| `image_in_Oq(Lf)` | `Lf`: `ZZLatWithIsom` | `Tuple{AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism}` | Image of $\pi:O(L)\to O(D_L)$ (Miranda-Morrison setting; documented for both definite and indefinite lattices; distinct from `image_centralizer_in_Oq`) | |
| `discriminant_representation(L::ZZLat, G::MatGroup; ambient_representation::Bool=true, full::Bool=true, check::Bool=true)` | `L`: `ZZLat`, `G`: `MatGroup`, `ambient_representation`: `Bool`, `full`: `Bool`, `check`: `Bool` | `GAPGroupHomomorphism` | Action of matrix group `G` on the discriminant group; `ambient_representation` selects coordinate system; `full` controls whether full discriminant group representation is computed; `check=true` validates input | |

#### Spinor norm

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `signatures(Lf::ZZLatWithIsom)` | `Lf`: `ZZLatWithIsom` | `Dict{Int, Tuple{Int, Int}}` | Signatures of the hermitian-type eigenspace decomposition; upstream constrains this to hermitian-type lattices with isometry whose minimal polynomial is irreducible and cyclotomic | |
| `rational_spinor_norm(Lf::ZZLatWithIsom; b::Int=-1)` | `Lf`: `ZZLatWithIsom`, `b`: `Int` | `QQFieldElem` | Rational spinor norm of the isometry with respect to the form `b·Φ`; default `b=-1` | |

#### Enumeration

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `enumerate_classes_of_lattices_with_isometry(::Union{ZZGenus, ZZLat}, ::Int)` | `Union{ZZGenus, ZZLat}`, `Int` | `Vector{ZZLatWithIsom}` | Enumerate isomorphism-class representatives for even lattices with finite-order isometry in a fixed genus/lattice context | |
| `representatives_of_hermitian_type(::Union{ZZLat, ZZGenus}, ::Union{ZZPolyRingElem, QQPolyRingElem}, ::Int)` | `Union{ZZLat, ZZGenus}`, `Union{ZZPolyRingElem, QQPolyRingElem}`, `Int` | `Vector{ZZLatWithIsom}` | Hermitian-type representatives for irreducible reciprocal polynomial input | |
| `representatives_of_hermitian_type(::Union{ZZGenus, ZZLat}, ::Int, ::Int)` | `Union{ZZGenus, ZZLat}`, `Int`, `Int` | `Vector{ZZLatWithIsom}` | Cyclotomic finite-order shortcut for hermitian-type representatives | |
| `admissible_triples(::ZZGenus, ::Int)` | `ZZGenus`, `Int` | `Vector{Tuple{ZZGenus, ZZGenus, ZZGenus}}` | Tuples of genera satisfying $p$-admissibility constraints | |
| `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)` | `ZZGenus`, `ZZGenus`, `ZZGenus`, `Int` | `Bool` | Validate $p$-admissibility for a genus triple | |
| `splitting(::ZZLatWithIsom, ::Int, ::Int)` | `ZZLatWithIsom`, `Int`, `Int` | `Vector{ZZLatWithIsom}` | Generic splitting routine in the finite-order enumeration machinery | |
| `splitting_of_hermitian_type(::ZZLatWithIsom, ::Int, ::Int)` | `ZZLatWithIsom`, `Int`, `Int` | `Vector{ZZLatWithIsom}` | Split hermitian-type lattice-with-isometry into hermitian sublattices | |
| `splitting_of_prime_power(::ZZLatWithIsom, ::Int, ::Int)` | `ZZLatWithIsom`, `Int`, `Int` | `Vector{ZZLatWithIsom}` | Split lattice-with-isometry at a prime-power stage | |
| `splitting_of_pure_mixed_prime_power(::ZZLatWithIsom, ::Int)` | `ZZLatWithIsom`, `Int` | `Vector{ZZLatWithIsom}` | Split pure/mixed part at fixed prime | |
| `splitting_of_mixed_prime_power(::ZZLatWithIsom, ::Int, ::Int)` | `ZZLatWithIsom`, `Int`, `Int` | `Vector{ZZLatWithIsom}` | Split mixed part at prime-power stage | |

### 2.15 Primitive embeddings

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `primitive_embeddings(L, M)` | `L`: `ZZLat`, `M`: `ZZLat` | `Vector` | Primitive embeddings of $M$ into $L$; returns isomorphism-class representatives (requires `L` unique in its genus) | |
| `primitive_embeddings(G, M)` | `G`: `ZZGenus`, `M`: `ZZLat` | `Vector` | Primitive embeddings into lattices of genus $G$ | |
| `primitive_embeddings(q, sig, M)` | `q`: `TorQuadModule`, `sig`: `Tuple{Int, Int}`, `M`: `ZZLat` | `Vector` | Primitive embeddings via discriminant form + signature | |
| `primitive_extensions(M, N)` | `M`: `ZZLat`, `N`: `ZZLat` | `Vector{ZZLat}` | Isomorphism classes of primitive extensions of $M \oplus N$ | |
| `equivariant_primitive_extensions(Mf, Nf; glue_only=false)` | `Mf`: `ZZLatWithIsom`, `Nf`: `ZZLatWithIsom`, `glue_only`: `Bool` | `Vector{ZZLatWithIsom}` | Equivariant primitive extensions (with isometries) | |
| `admissible_equivariant_primitive_extensions(Mf, Nf, gen, poly, p)` | `Mf`: `ZZLatWithIsom`, `Nf`: `ZZLatWithIsom`, `gen`: `ZZGenus`, `poly`: `Union{ZZPolyRingElem, QQPolyRingElem}`, `p`: `Int` | `Vector{ZZLatWithIsom}` | Admissible equivariant extensions satisfying type conditions for a target genus | |

### 2.16 Hermitian genera

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `genus(L)` | `L`: `HermLat` | `HermGenus` | Global genus of hermitian lattice | |
| `genus(L, p)` | `L`: `HermLat`, `p`: `AbsNumFieldOrderIdeal` | `HermLocalGenus` | Local genus at prime $p$ | |
| `hermitian_genera(E, rank, signatures, determinant; min_scale, max_scale, ...)` | `E`: `NumField`, `rank`: `Int`, `signatures`: `Vector{Tuple{Int, Int}}`, `determinant`: `Vector{QQFieldElem}`, `min_scale`: `Int`, `max_scale`: `Int` | `Vector{HermGenus}` | Enumerate hermitian genera; upstream requires `E` imaginary quadratic, `rank > 0`, and all determinants same sign (positive if `rank` even, negative if `rank` odd) | |
| `hermitian_local_genera(E, p, rank, determinant, min_scale, max_scale)` | `E`: `NumField`, `p`: `AbsNumFieldOrderIdeal`, `rank`: `Int`, `determinant`: `QQFieldElem`, `min_scale`: `Int`, `max_scale`: `Int` | `Vector{HermLocalGenus}` | Enumerate local hermitian genera at ideal `p` within scale window `[min_scale, max_scale]` | |
| `representative(G)` / `representatives(G)` | `G`: `HermGenus` | `HermLat` / `Vector{HermLat}` | Single representative / all representatives of genus class | |
| `genus_representatives(L)` | `L`: `HermLat` | `Vector{HermLat}` | All representatives in genus of $L$ | |
| `mass(L)` | `L`: `HermLat` | `QQFieldElem` | Mass of hermitian lattice | |
| `rank(G)` / `is_integral(G)` | `G`: `HermGenus` | `Int` / `Bool` | Genus rank / integrality test | |
| `primes(G)` | `G`: `HermGenus` | `Vector{AbsNumFieldOrderIdeal}` | Primes where genus is non-trivial | |
| `signatures(G)` | `G`: `HermGenus` | `Dict` | Signatures of genus | |
| `scale(G)` / `norm(G)` | `G`: `HermGenus` | `Ideal` | Scale / norm ideal | |
| `local_symbols(G)` | `G`: `HermGenus` | `Vector{HermLocalGenus}` | Local symbol data | |
| `direct_sum(G1, G2)` / `rescale(G, a)` | `G1`: `HermGenus`, `G2`: `HermGenus` / `a`: `FieldElem` | `HermGenus` | Operations on genera | |
| `is_ramified(g)` / `is_split(g)` / `is_inert(g)` / `is_dyadic(g)` | `g`: `HermLocalGenus` | `Bool` | Local genus splitting behavior | |

### 2.17 Isometry group actions on lattices

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `is_isometry(V, f)` | `V`: `Hecke.QuadSpace` or `ZZLat`, `f`: `QQMatrix` | `Bool` | Matrix-level isometry check for quadratic spaces / integer lattices | |
| `is_isometry_list(V, fs)` | `V`: `Hecke.QuadSpace` or `ZZLat`, `fs`: `Vector{QQMatrix}` | `Bool` | Batch isometry check for matrix list (upstream docs note not exported) | |
| `is_isometry_group(V, G)` | `V`: `Hecke.QuadSpace` or `ZZLat`, `G`: `MatGroup` | `Bool` | Group-level isometry check (upstream docs note not exported) | |
| `is_stable_isometry(Lf)` | `Lf`: `ZZLatWithIsom` | `Bool` | Fixed isometry acts trivially on discriminant group | |
| `is_special_isometry(Lf)` | `Lf`: `ZZLatWithIsom` | `Bool` | Fixed isometry has determinant $+1$ | |
| `special_orthogonal_group(L)` | `L`: `ZZLat` | `MatGroup` | Special orthogonal group $SO(L)$ | |
| `special_subgroup(L, G)` | `L`: `ZZLat`, `G`: `MatGroup` | `MatGroup` | Special subgroup of a finite isometry group | |
| `stable_orthogonal_group(L)` | `L`: `ZZLat` | `MatGroup` | Stable orthogonal group $O^{\#}(L)$ | |
| `stable_subgroup(L, G)` | `L`: `ZZLat`, `G`: `MatGroup` | `MatGroup` | Stable subgroup of a finite isometry group | |
| `stabilizer_discriminant_subgroup(L, G, H; pointwise=false, ambient_representation=true, check=true)` | `L`: `ZZLat`, `G`: `MatGroup`, `H`: `TorQuadModule`, `pointwise`: `Bool`, `ambient_representation`: `Bool`, `check`: `Bool` | `Tuple{MatGroup, GAPGroupHomomorphism}` | Largest subgroup of `G` preserving discriminant-group submodule `H` | |
| `stabilizer_in_orthogonal_group(L, B; stable=false, special=false, check=true, ...)` | `L`: `ZZLat`, `B`: `QQMatrix`, `stable`: `Bool`, `special`: `Bool`, `check`: `Bool` | `MatGroup` | Joint stabilizer in `O(L)` of rows of `B`; upstream requires largest saturated orthogonal submodule of `L` orthogonal to `B` to be definite or rank 2 | |
| `pointwise_stabilizer_in_orthogonal_group(L, S; ...)` | `L`: `ZZLat`, `S`: `ZZLat` | `MatGroup` | Pointwise stabilizer of sublattice `S`; upstream requires same definite/rank-2 condition on orthogonal submodule | |
| `setwise_stabilizer_in_orthogonal_group(L, S; stable=false, special=false, check=true, ...)` | `L`: `ZZLat`, `S`: `Union{QQMatrix, ZZLat}`, `stable`: `Bool`, `special`: `Bool`, `check`: `Bool` | `MatGroup` | Setwise stabilizer of `S`; upstream requires `S` and `S^\perp` definite or rank 2 | |
| `pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(L, S; check=true, ...)` | `L`: `ZZLat`, `S`: `Union{QQMatrix, ZZLat}`, `check`: `Bool` | `MatGroup` | Pointwise stabilizer of `S^\perp`; upstream requires `S` definite or rank 2 | |
| `stabilizer_in_diagonal_action(L, K, N, OK, ON; check=true)` | `L`: `ZZLat`, `K`: `ZZLat`, `N`: `ZZLat`, `OK`: `MatGroup`, `ON`: `MatGroup`, `check`: `Bool` | `Vector{QQMatrix}` | Generators for setwise stabilizer of primitive extension `K ⊕ N ⊆ L` | |
| `maximal_extension(L, K, G)` | `L`: `ZZLat`, `K`: `ZZLat`, `G`: `MatGroup` | `MatGroup` | Maximal extension in the group-action framework | |
| `saturation(L, G, H)` | `L`: `ZZLat`, `G`: `MatGroup`, `H`: `MatGroup` | `MatGroup` | Saturation of subgroup $H \le G$; requires finite `G` | |
| `saturation(L, G)` | `L`: `ZZLat`, `G`: `MatGroup` | `MatGroup` | Saturation inside $O(L)$; upstream requires coinvariant lattice definite or rank 2 | |
| `is_saturated_with_saturation(...)` | Varies | `Tuple{Bool, MatGroup}` | Saturation predicate plus witness; upstream requires coinvariant lattice definite | |
| `extend_to_ambient_space(L, F; check=false)` | `L`: `ZZLat`, `F`: `Union{QQMatrix, Vector{QQMatrix}, MatGroup}`, `check`: `Bool` | Same type as `F` | Convert isometries from lattice-basis to ambient-space coordinates | |
| `restrict_to_lattice(L, F; check=false)` | `L`: `ZZLat`, `F`: `Union{QQMatrix, Vector{QQMatrix}, MatGroup}`, `check`: `Bool` | Same type as `F` | Convert ambient-space isometries preserving `L` to lattice-basis coordinates | |

- Constraint caveat: stabilizer-family methods carry explicit geometric preconditions in upstream docs (definite/rank-2 requirements on relevant orthogonal sublattices); these constraints are part of the method contracts.
- Representation caveat: upstream text frames `extend_to_ambient_space` / `restrict_to_lattice` as basis-representation conversion for collections of isometries, with `restrict_to_lattice` also usable for ambient-space isometries preserving `L`.

### 2.18 Torsion quadratic modules with isometry (`TorQuadModuleWithIsom`)

Finite quadratic module workflows with a distinguished isometry action. This is the discriminant-form analogue of lattice-with-isometry surfaces and is central for equivariant gluing/classification contracts.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `torsion_quadratic_module_with_isometry(T, [f]; check=true)` | `T`: `TorQuadModule`, `f`: `Union{AutomorphismGroupElem{TorQuadModule}, TorQuadModuleMap, FinGenAbGroupHom, ZZMatrix, MatGroupElem{QQFieldElem, QQMatrix}}` (optional), `check`: `Bool` | `TorQuadModuleWithIsom` | Constructor from `TorQuadModule` and optional isometry; omitting `f` uses identity; `check=true` validates compatibility | `[NT]` |
| `torsion_quadratic_module_with_isometry(q, [f]; check=true)` | `q`: `QQMatrix`, `f`: `ZZMatrix` (optional), `check`: `Bool` | `TorQuadModuleWithIsom` | Constructor from quadratic-form matrix and optional integer action matrix | `[NT]` |
| `underlying_module(Tf)` / `torsion_quadratic_module(Tf)` | `Tf`: `TorQuadModuleWithIsom` | `TorQuadModule` | Access underlying finite quadratic module | `[NT]` |
| `isometry(Tf)` | `Tf`: `TorQuadModuleWithIsom` | `AutomorphismGroupElem{TorQuadModule}` | Access isometry of the pair | `[NT]` |
| `order_of_isometry(Tf)` | `Tf`: `TorQuadModuleWithIsom` | `Int` | Order of isometry (finite; computed lazily and cached) | `[NT]` |
| `sub(Tf, gene)` | `Tf`: `TorQuadModuleWithIsom`, `gene`: `Vector{TorQuadModuleElem}` | `Tuple{TorQuadModuleWithIsom, TorQuadModuleMap}` | Construct isometry-stable submodule from generators | `[NT]` |
| `primary_part(Tf, m)` | `Tf`: `TorQuadModuleWithIsom`, `m`: `IntegerUnion` | `Tuple{TorQuadModuleWithIsom, TorQuadModuleMap}` | Primary part with induced isometry action | `[NT]` |
| `orthogonal_submodule(Tf, S; check=true)` | `Tf`: `TorQuadModuleWithIsom`, `S`: `TorQuadModule`, `check`: `Bool` | `Tuple{TorQuadModuleWithIsom, TorQuadModuleMap}` | Orthogonal complement with induced action; upstream requires `S` stable under isometry (enforced when `check=true`) | `[NT]` |
| `submodules(Tf; quotype=Int[])` | `Tf`: `TorQuadModuleWithIsom`, `quotype`: `Vector{Int}` | Iterator | Enumerate isometry-stable submodules; upstream restricts `quotype` entries to `{0,1,2,3}` | `[NT]` |
| `automorphism_group_with_inclusion(Tf)` | `Tf`: `TorQuadModuleWithIsom` | `Tuple{AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism}` | Automorphism group of the pair commuting with fixed isometry | `[NT]` |
| `automorphism_group(Tf)` | `Tf`: `TorQuadModuleWithIsom` | `AutomorphismGroup{TorQuadModule}` | Automorphism group of the pair `(T, f)` (upstream typesets arg as `TorQuadModuleWithMap` — documentation typesetting inconsistency) | `[NT]` |
| `is_isomorphic_with_map(Tf, Sg)` | `Tf`: `TorQuadModuleWithIsom`, `Sg`: `TorQuadModuleWithIsom` | `Tuple{Bool, TorQuadModuleMap}` | Isomorphism test; returns `(true, map)` on success, `(false, 0)` on failure | `[NT]` |
| `is_anti_isomorphic_with_map(Tf, Sg)` | `Tf`: `TorQuadModuleWithIsom`, `Sg`: `TorQuadModuleWithIsom` | `Tuple{Bool, TorQuadModuleMap}` | Anti-isomorphism test; returns `(true, anti_map)` on success, `(false, 0)` on failure | `[NT]` |

Source note: contracts in §2.7/§2.11/§2.13/§2.14/§2.16/§2.17/§2.18 were reconciled against local snapshots under `docs/julia/oscar_jl/number_theory/quad_form_and_isom/` plus OSCAR stable/dev `QuadFormAndIsom` pages (including `spacewithisom`, `latwithisom`, `fingrpact`, `torquadmodwithisom`, and current index surfacing for collections/enumeration) and Hecke manual pages for genera (`quad_forms/genera`, `quad_forms/genusherm`) accessed 2026-02-17/2026-02-18. See provenance note `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`.
- Pass-24 addendum (2026-02-18): `TorQuadModule.submodules` and `stable_submodules` typed signatures updated in §2.11 from OSCAR upstream Hecke discriminant-group docs; `torsion_quadratic_module_with_isometry` type union in §2.18 updated to include `AutomorphismGroupElem{TorQuadModule}` per OSCAR stable upstream constructor docs.

### References

- Oscar manual and Hecke GitHub documentation
- Hofmann & Fieker (2025)
- Nebe–Pless–Sloane (lattices), Conway–Sloane (theta series, classification)
- Kirschmer–Voight (forms over number fields)
- GAP Quadratic Forms package

### Definiteness summary

| Regime | Available methods |
|--------|------------------|
| **PD** | All: LLL, SVP/CVP, kissing number, genus, automorphisms, root recognition, theta series ingredients |
| **ND** | Use `rescale(L, -1)` to reduce to PD |
| **INDEF** | `lll` (runs, limited meaning); genus/discriminant forms; rational/local isometry; Vinberg's algorithm (sig $(1,n)$); discriminant group operations; no SVP/CVP |

---

## 3. Oscar.jl

Metapackage combining Nemo, Hecke, Polymake, Singular, GAP. Does not add distinct lattice algorithms — provides unified interface to Hecke's methods.

### Integration points

| Capability | Notes |
|------------|-------|
| `Oscar.ZZLat` | High-level type wrapping Hecke's `ZZLat` |
| `Oscar.to_oscar(obj)` | Emit reproducible Julia code to reconstruct `obj` (useful for `ZZLatWithIsom` examples and bug reports) |
| Lattice databases | Markus Kirschmer's databases accessible directly |
| `lll`, `short_vectors`, `close_vectors` | Dispatch to Hecke/Nemo |
| Discriminant groups | Finite quadratic module type; computes isometries of discriminant form (Nikulin theory) |
| `rescale(L, r)` | Documented with warnings about INDEF limitations |
| Intersection forms | Verify primitive embeddings for Néron–Severi / K3 lattices (Nikulin theory) |
| Polyhedral integration | Use lattice in polyhedral context via Polymake; compute Aut(L) as abstract group |

Same definiteness constraints as Hecke. Oscar v1.6 includes Hecke v0.39.

### References

- Oscar manual, Quadratic Forms section
- OSCAR homepage and reference paper (2023)
- `using Oscar` provides unified namespace for Nemo LLL + Hecke genus functions

---

## 4. Nemo.jl

Computer algebra over ℤ, ℚ, ℤ/n. Built on FLINT/Antic. Lattice = `ZZMatrix` (`fmpz_mat` — FLINT integer matrix) whose rows (or columns) form a basis in $\mathbb{Z}^n$. Provides matrix-level reduction, not high-level lattice classification.

### 4.1 LLL reduction

| Function | Description | Tags |
|----------|-------------|------|
| `lll(B::ZZMatrix, ctx::LLLContext)` | LLL-reduced basis; default δ=0.99, η=0.51 | `[PD, FLINT]` |
| `lll_with_transform(B)` | Returns $(L, T)$ with $L = T \cdot B$ | `[PD, FLINT]` |
| `lll_gram(G)` | LLL on Gram matrix $G = B B^T$; requires symmetric PSD | `[PD, FLINT]` |
| `lll_gram_with_transform(G)` | Gram-based LLL + transformation | `[PD, FLINT]` |

- `lll(B)` without explicit Gram uses standard Euclidean dot product
- Gram-based variant requires symmetric, non-singular (or semi-definite) G
- INDEF Gram: algorithm executes but "reduced" is meaningless — LLL criteria assume PD; supply a PD Gram majorant instead (as in BKZ contexts)

### 4.2 Hermite Normal Form

| Function | Description | Tags |
|----------|-------------|------|
| `hnf(X)` / `AbstractAlgebra.hnf(X)` | Hermite normal form (triangular, divisibility) | `[DEG, INDEF ok]` |
| `hnf_with_transform(X)` | Returns $(H, U)$ with $H = U \cdot X$ | `[DEG, INDEF ok]` |

No definiteness assumptions. Purely algebraic. Canonical representative of lattice basis. Used in ideal arithmetic and linear Diophantine equations. Fast modular HNF via FLINT. Does not prefer short vectors.

### 4.3 Smith Normal Form

| Function | Description | Tags |
|----------|-------------|------|
| `snf(X)` / `AbstractAlgebra.snf(X)` | Smith normal form; diagonal $D = UXV$ with invariant factors | `[DEG, INDEF ok]` |
| `snf_with_transform(X)` | Returns $(D, U, V)$ | `[DEG, INDEF ok]` |

Reveals $\mathbb{Z}^n / L \cong \mathbb{Z}/d_1 \times \cdots \times \mathbb{Z}/d_n$. Discriminant = $\prod d_i$ (up to sign). No definiteness assumptions.

### 4.4 Other

| Function | Description | Tags |
|----------|-------------|------|
| Echelon form | Via FLINT | `[DEG]` |
| Saturation | No high-level `saturate` function; achieve via HNF/SNF (invariant factors reveal if sublattice has index > 1 in rational span) | `[DEG]` |

### Interaction with Hecke

Nemo `ZZMatrix` / `QQMatrix` are the underlying matrix types in Hecke/Oscar lattice objects. One can extract basis/Gram and apply Nemo functions directly.

### References

- Fieker et al., ISSAC 2017
- FLINT documentation (floating-point LLL, Gram-Schmidt)
- Cohen, *A Course in Computational Algebraic Number Theory* (HNF/SNF)
- Nguyen–Vallée, *The LLL Algorithm*

---

## 5. LLLplus.jl

`[PD, EUCLID]` — Experimental lattice reduction toolkit by Christian Peel. Pure Julia. Not registered. Pedagogical / prototyping focus. Applications: cryptography, communications, integer programming.

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `lll(B)` | LLL reduction | `[PD, EUCLID]` |
| `seysen(B)` | Seysen's reduction (minimizes pairwise dot products; more orthogonal than LLL) | `[PD, EUCLID]` |
| `hkz(B)` | Hermite-Korkine-Zolotarev reduction (exact SVP in projected lattices; exponential cost) | `[PD, EUCLID]` |
| `brun(B)` | Brun's algorithm (integer relations / Diophantine approximation; precursor to PSLQ) | `[PD, EUCLID]` |
| `cvp(Q, R, y)` | Closest vector problem via sphere decoder (QR factorization input) | `[PD, EUCLID]` |

### Utility functions

| Function | Description |
|----------|-------------|
| `subsetsum(...)` | Subset sum via lattice formulation |
| `integerfeasibility(...)` | Integer linear feasibility |
| `rationalapprox(...)` | Rational approximation via short vectors |
| BBP π digits | Spigot algorithm demo |

### Definiteness

All algorithms assume Euclidean norm. Input is a real matrix (accepts `randn` floating-point); form is the standard inner product or implicit via QR. INDEF forms not supported. Brun's algorithm internally constructs a PD lattice in extended dimension. For serious/large-scale use, consider fplll (C++) or Nemo.

### References

- Wübben et al. (lattice reduction in communications)
- Bremner, *Lattice Basis Reduction*
- Simons Institute Lattice Algorithms workshop (2020)
- Chris Peel, JuliaCon 2021: "Lattice Reduction using LLLplus.jl"

---

## 6. LatticeAlgorithms.jl (Amazon Science)

`[PD, EUCLID]` — Lattice algorithms for GKP quantum error-correcting codes. Accompanied PRX Quantum 4, 040334 (2023).

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `lll(M)` | LLL reduction on basis matrix input | `[PD, EUCLID]` |
| `islllreduced(B)` | Predicate for LLL-reduced basis conditions | `[PD, EUCLID]` |
| `kz(M)` | KZ (HKZ-style) reduction routine | `[PD, EUCLID]` |
| `closest_point(x, M)` | CVP-style closest-lattice-point solver | `[PD, EUCLID]` |
| `closest_point_Dn(x)` | Specialized closest-point routine for $D_n$ | `[PD, EUCLID]` |
| `Dn(n)` | Constructor/helper for the $D_n$ root lattice family | `[PD, EUCLID]` |
| `distance(M)` / `distances(M)` | Lattice-distance helper routines used by decoding workflows | `[PD, EUCLID]` |

Higher-level capabilities documented in the package context:

- SVP/CVP and MLD workflows in multimode GKP decoding.
- Predefined lattice families used in decoder benchmarks.

### Definiteness

All algorithms require PD (Euclidean distance minimization). GKP symplectic form is INDEF but the decoding problem reduces to CVP in a PD lattice of errors.

### References

- "Closest Lattice Point Decoding for Multimode GKP Codes", PRX Quantum 4, 040334 (2023)
- Subsequent arXiv papers on tensor-network / matching decoders with lattice methods
- Search algorithm reference: Chalmers University publication (lattice point enumeration)
- Algorithms efficient in moderate dimensions ($n \sim 8$–$10$ for multimode GKP)
- Repository: `https://github.com/QuantumSavory/LatticeAlgorithms.jl`
- Research repository hub: `https://github.com/amazon-science/lattice-algorithms`

---

## 7. Minor Packages

### 7.1 LatticeBasisReduction.jl

`[PD, EUCLID]` — Minimal Julia package for LLL basis reduction.

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `lll(B::AbstractMatrix{<:Integer}; delta=0.99, eta=0.51)` | LLL reduction on an integer basis matrix. | `[PD, EUCLID]` |
| `lll!(B::Matrix{BigFloat}; delta=0.99, eta=0.51)` | In-place LLL reduction on a `BigFloat` matrix. | `[PD, EUCLID]` |
| `islllreduced(B::AbstractMatrix{BigFloat}; delta=0.99, eta=0.51)` | Predicate for LLL-reducedness conditions. | `[PD, EUCLID]` |

Caveats:

- The package exports `lll`; `lll!` and `islllreduced` are documented API surfaces but non-exported.
- Implementation is Euclidean/Gram-Schmidt based and does not provide indefinite-form classification methods.

### 7.2 MinkowskiReduction.jl

`[PD, EUCLID]` — Minkowski reduction for integer lattice bases.

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `minkReduce(B::AbstractMatrix{<:Integer}; stable=true)` | Returns a Minkowski-reduced basis. | `[PD, EUCLID]` |
| `deviousMat(n::Int64, m::Int64)` | Generator for difficult benchmark-style integer bases. | `[PD, EUCLID]` |

Caveats:

- Package scope is low-dimensional Euclidean reduction; no indefinite-form or genus/isometry classification APIs are documented.
- Upstream notes implementation tested only up to rank `n <= 7`.

### References

- `https://github.com/MGBoom/LatticeBasisReduction.jl`
- `https://mgboom.github.io/LatticeBasisReduction.jl/stable/API/`
- `https://github.com/MGBoom/LatticeBasisReduction.jl/blob/master/src/LatticeBasisReduction.jl`
- `https://github.com/glwhart/MinkowskiReduction.jl`
- `https://github.com/glwhart/MinkowskiReduction.jl/blob/master/src/MinkowskiReduction.jl`
- `https://github.com/glwhart/MinkowskiReduction.jl/blob/master/README.md`

---

## 8. Other Considerations

### Theta series

No Julia package automates theta series computation. Use `short_vectors(L, 0, N)` in Hecke to count vectors by norm and assemble $\Theta_L(q) = \sum_{v \in L} q^{|v|^2}$ manually. No `theta_series(L, precision)` function yet. No package for Eisenstein series or Siegel theta constants; use PARI/GP via Nemo for deeper analysis. `[PD]`

### GAP packages (via GAP.jl / Oscar)

`OrthogonalForms`, `AutomorphismGroups`, etc. Not Julia packages per se. Complement Oscar for exact isometry tests via Hasse invariants.

### Performance notes

| Package | Backend | Speed |
|---------|---------|-------|
| Nemo.jl | FLINT (C) | Fast (LLL, HNF) |
| Hecke.jl | Nemo + GAP + optional PARI/MAGMA (genus computations) | Moderate–fast |
| Indefinite.jl | GAP | Moderate |
| LLLplus.jl | Pure Julia | Moderate; use fplll for large-scale |
| LatticeAlgorithms.jl | Pure Julia | Moderate (designed for dim ~8–10) |

---

## 9. Definiteness Constraints Summary

### Positive-definite

All reduction (LLL, BKZ, HKZ, Seysen), enumeration (SVP, CVP, `short_vectors`), and packing invariants (`kissing_number`, theta series) apply. Algorithms treat the lattice as a metric space.

### Indefinite

No SVP/CVP (infinitely many vectors in any bounded norm range due to null directions). Use:
- Genus symbols and discriminant forms for classification
- Orbits of isotropic vectors (Indefinite.jl)
- Vinberg's algorithm for sig $(1,n)$ reflection groups
- Functions enforce via `check::Bool=true`; throws if form is not definite

### Semi-definite / degenerate

Most functions demand non-degenerate forms ("nondegenerate $\mathbb{Z}$-lattice"). Preprocess by quotienting out the null space. HNF/SNF (Nemo) handle rank-deficient matrices. Hecke/Oscar error out and guide toward `rescale`, `scale(L)`, or orthogonal complement to remove null directions. Nemo/LLLplus simply assume away degenerate cases or rely on generic linear algebra for rank deficiency.

---

## Sources

- Indefinite.jl README (Dutour Sikirić et al.)
- Oscar/Hecke stable manual (lattices): https://docs.oscar-system.org/stable/Hecke/manual/lattices/integrelattices/ (accessed 2026-02-17)
- Oscar/Hecke stable manual (lattices with isometry): https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/ (accessed 2026-02-17)
- In-repo localized provenance for `ZZLatWithIsom` attribute-forwarding survey: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom_online_provenance_2026-02-17.md`
- Nemo.jl documentation — LLL, HNF
- LLLplus.jl README
- LatticeAlgorithms.jl README (Amazon Science)
