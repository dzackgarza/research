# Oscar.jl: Integer lattices

**Documentation:** https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/

---

## Creation

```julia
using Oscar, Hecke

# From Gram matrix
L = integer_lattice(gram = matrix(ZZ, [2 -1; -1 2]))

# Root lattices
A3 = root_lattice(:A, 3)
D4 = root_lattice(:D, 4)
E8 = root_lattice(:E, 8)

# Negative definite root lattices
D4_neg = root_lattice(:D, 4, -1)

# Hyperbolic plane (signature (1,1))
U = hyperbolic_plane_lattice()

# K3 lattice (signature (3,19))
L_K3 = k3_lattice()
```

---

## Invariants

```julia
rank(L)              # Int
det(L)               # QQFieldElem
scale(L)             # QQFieldElem
level(L)             # QQFieldElem
norm(L)              # QQFieldElem
iseven(L)            # Bool
is_integral(L)       # Bool

signature_tuple(L)   # (n₊, n₀, n₋)
is_positive_definite(L)  # Bool
is_negative_definite(L)  # Bool
is_definite(L)           # Bool

is_primary(L, p)           # Bool
is_primary_with_prime(L)   # (Bool, p)
is_elementary(L, p)        # Bool
is_elementary_with_prime(L)  # (Bool, p)
```

---

## Genus (no definiteness required)

**Documentation:** https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/Zgenera/

```julia
G = genus(L)
G = genus(gram_matrix(L))

# Invariants
dim(G)
rank(G)
signature(G)       # p - n
det(G)
iseven(G)
is_definite(G)
level(G)
scale(G)
norm(G)
is_integral(G)
primes(G)          # Vector of primes (always includes 2)

# Local genus at prime p
S = genus(L, 2)
prime(S)
iseven(S)
symbol(S, scale)
hasse_invariant(S)
det(S)
dim(S)
excess(S)          # p-excess (oddity when p=2)
signature(S)
oddity(S)

# Canonical symbol
canonical_symbol(G)
canonical_symbol(S)

# Class number (use to prove isometry claims abstractly)
h = class_number(G)
# Example: class_number(genus(root_lattice(:E, 8))) returns 1

# ⚠️ REQUIRES DEFINITE
m = mass(G)

# Representatives
reps = representatives(G)
L_rep = representative(G)
V = rational_representative(G)

represents(G1, G2)
G_scaled = rescale(G, 2)
```

---

## Isometry ⚠️ DEFINITE REQUIRED

```julia
# ⚠️ REQUIRES DEFINITE LATTICE
gens = automorphism_group_generators(L)
order = automorphism_group_order(L)
iso = is_isometric(L, M)

# For indefinite lattices, use Indefinite.jl instead
```

---

## Local isometry (no definiteness required)

```julia
is_locally_isometric(L, M, p)  # Bool: L ⊗ ℤₚ ≅ M ⊗ ℤₚ
```

---

## Root lattice recognition ⚠️ DEFINITE REQUIRED

```julia
# ⚠️ REQUIRES DEFINITE AND INTEGRAL
ADE_types, sublattices = root_lattice_recognition(L)

root_subl, ADE_types, sublattices = root_lattice_recognition_fundamental(L)

# ADE type from Gram matrix
ADE_type(gram_matrix(A3))  # (:A, 3)

# Combinatorial data
coxeter_number(:A, 3)
highest_root(:E, 6)
```

---

## Module operations

```julia
L == M
is_sublattice(L, M)
is_sublattice_with_relations(L, M)  # (Bool, transformation matrix)

L + M
intersect(L, M)
a * L

v in L

primitive_closure(M, N)
is_primitive(M, N)
is_primitive(L, v)
divisibility(L, v)
```

---

## Orthogonal submodule

```julia
S_perp = orthogonal_submodule(L, S)

# ⚠️ REQUIRES DEFINITE
components = irreducible_components(L)
```

---

## Dual and overlattices

```julia
L_dual = dual(L)

γ, ι_S, ι_R = glue_map(L, S, R)
L_new = overlattice(γ)
L_ext, incl_S, incl_R = primitive_extension(γ)

M_prime = local_modification(M, L, p)
M = maximal_integral_lattice(L)
```

---

## Invariant/coinvariant lattices

```julia
G = [g1, g2]  # Vector of matrices

L_fixed = invariant_lattice(L, G)
L_coinv = coinvariant_lattice(L, G)
ker = kernel_lattice(L, f)
```

---

## Embedding

```julia
success, embedding = embed(S, G; primitive = true)

# ⚠️ REQUIRES EVEN LATTICE
success, L_target, S_embed, ι_S, ι_R = embed_in_unimodular(S, pos, neg; primitive = true, even = true)
```

---

## Short vectors ⚠️ DEFINITE REQUIRED

```julia
# ⚠️ REQUIRES DEFINITE
min_norm, vectors, count = shortest_vectors(L)
vectors = short_vectors(L, lb, ub)
M, L_orig, gens = shortest_vectors_sublattice(L)

# For indefinite isotropic vectors, use Indefinite.jl
```

---

## Vectors with given square and divisibility

```julia
# ⚠️ REQUIRES S DEFINITE
vectors = vectors_of_square_and_divisibility(L, S, n, d)
```

---

## Affine short vectors ⚠️ HYPERBOLIC OR NEGATIVE DEFINITE

```julia
# ⚠️ REQUIRES HYPERBOLIC OR NEGATIVE DEFINITE
vecs = short_vectors_affine(S, v, α, d)
vecs = short_vectors_affine(gram, v, α, d)

# ⚠️ REQUIRES POSITIVE DEFINITE Q
solutions = enumerate_quadratic_triples(Q, b, c)
```

---

## Close vectors

```julia
close = close_vectors(L, v, lb, ub)
# ⚠️ Checks positive definite by default; use check=false for indefinite
```

---

## LLL (works for indefinite)

```julia
L_red = lll(L; same_ambient = true, redo = false)
ctx = LLLContext(0.99, 0.51, :gram)
L_red = lll(L; ctx = ctx)
```

---

## Discriminant groups (no definiteness required)

**Documentation:** https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/discriminant_group/

```julia
# Creation
D = discriminant_group(L)
T = torsion_quadratic_module(QQ[1//6;])
T = torsion_quadratic_module(M, N)

# Invariants
abelian_group(D)
cover(D)
relations(D)
value_module(D)
value_module_quadratic_form(D)
gram_matrix_bilinear(D)
gram_matrix_quadratic(D)
modulus_bilinear_form(D)
modulus_quadratic_form(D)

# Element operations
gens_D = gens(D)
a = gens_D[1]
q_a = quadratic_product(a)
b_ab = inner_product(a, b)
v = lift(a)
v = representative(a)

# Isometry testing (no definiteness required)
is_iso, phi = is_isometric_with_isometry(D1, D2)
is_anti_iso, psi = is_anti_isometric_with_anti_isometry(D1, D2)

# Submodules (enumerate isotropic subgroups, etc.)
for S in submodules(D)
for S in submodules(D; order = 4)
for S in submodules(D; index = 2)
G = [g1, g2]  # Vector of TorQuadModuleMap
for S in stable_submodules(D, G)
S_perp = orthogonal_submodule(D, S)

# Smith normal form (canonical reps of isometry classes)
D_snf, iso_map = snf(D)
is_snf(D)

# Radicals
is_degenerate(D)
is_semi_regular(D)
rad_bilin, incl = radical_bilinear(D)
rad_quad, incl = radical_quadratic(D)
D_norm, proj = normal_form(D)

# Brown invariant
br = brown_invariant(D)

# Construct genus from discriminant form
exists = is_genus(D, sig; parity = 2)
G = genus(D, sig; parity = 2)

# Categorical
D_sum, injections = direct_sum(D1, D2, D3)
D_prod, projections = direct_product(D1, D2)
D_bi, inj, proj = biproduct(D1, D2)
D_scaled = rescale(D, 2)
```

---

## Vinberg's algorithm (signature (1,n))

**Documentation:** https://docs.oscar-system.org/stable/NumberTheory/vinberg/

```julia
# Matrix interface
Q = matrix(ZZ, [1 0 0; 0 -1 0; 0 0 -1])
v0 = matrix(ZZ, [1 0 0])
roots = vinberg_algorithm(Q, upper_bound;
                         v0 = v0,
                         root_lengths = [-2],
                         direction_vector = matrix(ZZ, [0 1 0]))

# Lattice interface
S = integer_lattice(gram = Q)
divisibilities = Dict(-2 => 1)
roots = vinberg_algorithm(S, upper_bound;
                         v0 = v0,
                         root_lengths = [-2],
                         direction_vector = matrix(ZZ, [0 1 0]),
                         divisibilities = divisibilities)
```

---

## Lattices with isometry

**Documentation:** https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/latwithisom/

```julia
# Create lattice with isometry
L = root_lattice(:A, 5)
f = matrix(QQ, 5, 5, [1 1 1 1 1; 0 -1 -1 -1 -1; 0 1 0 0 0; 0 0 1 0 0; 0 0 0 1 0])
Lf = integer_lattice_with_isometry(L, f)

# Or with -I as isometry
Lf = integer_lattice_with_isometry(L; neg = true)

# Accessors
lattice(Lf)              # Underlying lattice
isometry(Lf)             # Isometry matrix f
ambient_isometry(Lf)     # Isometry of ambient space
ambient_space(Lf)        # (V, f) pair
order_of_isometry(Lf)    # Order of f

# Invariants
rank(Lf)
det(Lf)
signature_tuple(Lf)
genus(Lf)
characteristic_polynomial(Lf)
minimal_polynomial(Lf)
type(Lf)                 # Dict of k-types (H_k, A_k)

# Kernel sublattices
Lf_inv = invariant_lattice(Lf)           # L^f (fixed lattice)
Lf_coinv = coinvariant_lattice(Lf)       # Orthogonal complement of L^f
Lf_ker = kernel_lattice(Lf, x - 1)       # ker(f - 1)
Lf_ker = kernel_lattice(Lf, 5)           # ker(Φ₅(f))

# Both at once
Lf_inv, Lf_coinv = invariant_coinvariant_pair(Lf)

# Discriminant group with isometry
DL, Df = discriminant_group(Lf)
Df_iso = discriminant_group(TorQuadModuleWithIsom, Lf)

# ⚠️ CRITICAL: Image of centralizer in O(D_L)
G, phi = image_centralizer_in_Oq(Lf)
# G = image of O(L, f) in O(D_L, D_f)
order(G)

# Discriminant representation
pi = discriminant_representation(L, G)
# π: G → O(D_L) orthogonal representation on discriminant

# Hermitian structure (if f has irreducible minimal polynomial)
H = hermitian_structure(Lf_coinv)

# Signatures of eigenspaces
sigs = signatures(Lf)

# Spinor norm
sp = rational_spinor_norm(Lf)

# Operations
Lf_dual = dual(Lf)
Lf_rescaled = rescale(Lf, 1//2)
Lf_lll = lll(Lf)
Lf_pow = Lf^3                    # (L, f³)
Lf_sum, emb, proj = direct_sum(Lf1, Lf2)

# Orthogonal submodule with isometry
B = matrix(QQ, 3, 5, [1 0 0 0 0; 0 0 1 0 1; 0 0 0 1 0])
S = orthogonal_submodule(Lf, B)

# Lattice in same ambient space
I = lattice_in_same_ambient_space(Lf, B)
```

---

## Primitive embeddings and extensions

**Documentation:** https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/primembed/

```julia
# ⚠️ CRITICAL: Primitive embeddings of M into L
# L must be unique in its genus
exists, embeddings = primitive_embeddings(L, M)
# Returns: [(L', M', N')] where L' ≅ L, M' ⊆ L' ≅ M, N' = M'^⊥

# From genus instead of lattice
exists, embeddings = primitive_embeddings(G, M)
# G is genus, M embeds into some L ∈ G

# From discriminant form + signature
exists, embeddings = primitive_embeddings(q, sign, M)
# q = discriminant form, sign = (n₊, n₋)

# Classification levels:
# :none  - just test existence
# :first - return one embedding
# :sub   - classify up to O(M) and O(q)
# :emb   - classify up to O(q) only

# ⚠️ CRITICAL: Primitive extensions (overlattices)
# Find L containing M ⊕ N as primitive sublattices
exists, extensions = primitive_extensions(M, N)
# Returns: [(L, M', N')] where M' ≅ M, N' ≅ N, M' ⊕ N' ⊆ L primitive

# With constraints
exists, extensions = primitive_extensions(M, N;
                                         glue_order = [2, 4],      # [L : M⊕N]
                                         form_over = [target_q],   # desired D(L)
                                         even = true,              # force even lattices
                                         classification = :subsub) # up to O(M)×O(N)

# Classification levels:
# :subsub  - up to O(M) × O(N)
# :subemb  - up to O(M) only
# :embsub  - up to O(N) only
# :embemb  - no quotient (finest)

# ⚠️ CRITICAL: Equivariant primitive extensions (with isometries)
# Find (L, f_L) containing (M, f_M) ⊕ (N, f_N) as primitive sublattices
exists, extensions = equivariant_primitive_extensions(Mf, Nf)
# Returns: [(Lf, Mf', Nf')] where f_L preserves M' and N'

# With isometries on inputs
Mf = integer_lattice_with_isometry(M, fM)
Nf = integer_lattice_with_isometry(N, fN)
exists, extensions = equivariant_primitive_extensions(Mf, Nf;
                                                      glue_order = [2],
                                                      form_over = [target_q],
                                                      even = true,
                                                      classification = :subsub,
                                                      compute_bar_Gf = true,           # compute image of O(L,f) → O(D_L,D_f)
                                                      first_fitting_isometry = false)  # extend conjugacy class reps

# ⚠️ CRITICAL: Admissible equivariant extensions (double coset reps)
# For p-admissible triples ((A,f_A), (B,f_B), (C,f_C))
# Returns reps of G_B \ S / G_A
extensions = admissible_equivariant_primitive_extensions(Af, Bf, Cf, p, q)
# p, q are primes (default q = p)
# Requires: type(D, f_D^q) = type(C, f_C)
```
