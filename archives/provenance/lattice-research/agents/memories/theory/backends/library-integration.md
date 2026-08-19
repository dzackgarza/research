# Library Integration Opportunities

**Purpose:** Map goal_expansion.md tasks to existing libraries (Oscar.jl, GAP, Indefinite.jl, buildings.sage) that already implement required functionality. **Do not reinvent.**

---

## ⚠️ MANDATORY: Use Existing Tools

**DO NOT:**
- Write ad-hoc lattice embedding code
- Implement Nikulin theory from scratch
- Write custom orbit enumeration for finite groups
- Implement Vinberg's algorithm manually
- Construct involutions via raw matrix equations
- Enumerate isotropic planes by brute force

**DO:**
- Check [EasyBuild's supported software list](https://docs.easybuild.io/version-specific/supported-software/) before any nontrivial computation
- Use `primitive_embeddings` from Oscar.jl (already implements Nikulin theory)
- Use `Orbit`/`Stabilizer` from GAP (optimized for finite group actions)
- Use `building()` from buildings.sage (designed for isotropic plane orbits)
- Use `vinberg_algorithm` from Oscar.jl (proven implementation)
- Use `equivariant_primitive_extensions` from Oscar.jl (handles isometry-preserving extensions)
- Use `image_centralizer_in_Oq` from Oscar.jl (discriminant group lifting)

**Reference documentation:**
- **Oscar.jl lattices:** `theory/backends/oscar-lattices`
- **GAP orbits:** `theory/backends/gap-orbits`
- **Indefinite.jl:** `theory/backends/indefinite-jl`
- **buildings.sage:** `theory/backends/buildings`

**Before starting ANY computation task:**
1. Check [EasyBuild's supported software list](https://docs.easybuild.io/version-specific/supported-software/) for existing packaged implementations
2. Read the relevant documentation above
3. Identify the existing function that does what you need
4. Use that function with correct syntax
5. Only if NO existing function exists, then consider custom implementation

---

## G1.2: Gram Matrices and Invariants (T-0001)

**Current risk:** Low (but building from scratch)

**Use Oscar.jl instead:**

**Doc:** `theory/backends/oscar-lattices` → Creation, Invariants, Discriminant groups

```julia
using Oscar, Hecke

# S_Co ≅ <2> ⊕ <-2>^10
S_Co = direct_sum(integer_lattice(gram = matrix(ZZ, [2])), 
                  root_lattice(:A, 1)^10)[1]  # or scale root_lattice(:A,1) by -2

# T_Co from coble_geometry_foundation
T_Co = ...  # whatever the actual construction is

# Invariants (no definiteness required)
rank(T_Co)
det(T_Co)
signature_tuple(T_Co)
discriminant_group(T_Co)
genus(T_Co)
is_even(T_Co)
is_primary(T_Co, 2)
```

**Functions:** `integer_lattice`, `root_lattice`, `direct_sum`, `discriminant_group`, `genus`, `signature_tuple`, `is_primary`, `is_elementary`

---

## G1.3: Primitive Embedding Matrices (T-0003)

**Current risk:** Medium ("requires Nikulin embedding theory implementation")

**Use Oscar.jl instead - already implements Nikulin theory:**

**Doc:** `theory/backends/oscar-lattices` → Primitive embeddings and extensions

```julia
using Oscar, Hecke

# T_Co → T_En → T_dP → Λ_K3
# L must be unique in its genus (K3 lattice is!)

# Embed T_Co into K3 lattice
exists, embeddings = primitive_embeddings(k3_lattice(), T_Co)
# Returns: [(L', T_Co', T_Co'^⊥)]

# Get explicit embedding matrix
L_prime, T_Co_prime, N_prime = embeddings[1]
# The embedding is given by the change of basis from T_Co to T_Co_prime

# With classification control
exists, embeddings = primitive_embeddings(k3_lattice(), T_Co;
                                         classification = :sub)  # up to O(T_Co) × O(q)
```

**Functions:** `primitive_embeddings`, `k3_lattice`

**Risk reduction:** Medium → Low (library handles Nikulin conditions)

---

## G2.1: Orbit Enumeration in A_T (T-0004)

**Current risk:** Low ("finite group computation")

**Use GAP instead:**

**Doc:** `theory/backends/gap-orbits` → Orbit, Stabilizer, OrbitsDomain

```gap
# A_T = (Z/2Z)^11 with discriminant form q_T
# O(q_T) acts on isotropic vectors

# Create finite group O(q_T) from generators
G := Group(generators_of_O_qT);

# Isotropic vectors in A_T
iso_vecs := Filtered(Elements((GF(2)^11)), v -> qT(v) = 0);

# Orbits under O(q_T)
orbits := Orbits(G, iso_vecs, OnRight);

# Orbit representatives and sizes
for orb in orbits do
  Print("Representative: ", orb[1], "\n");
  Print("Size: ", Length(orb), "\n");
od;

# Or with Stabilizer
for rep in List(orbits, o -> o[1]) do
  stab := Stabilizer(G, rep, OnRight);
  Print("Stab size: ", Size(stab), "\n");
od;
```

**Functions:** `Orbit`, `Orbits`, `Stabilizer`, `OnRight`

**Risk reduction:** Low → Very Low (GAP optimized for finite group actions)

---

## G2.2: Orbit Lifting to T_Co (T-0007)

**Current risk:** Medium ("requires Sterk's technique implementation")

**Use Oscar.jl instead:**

**Doc:** `theory/backends/oscar-lattices` → Lattices with isometry, Discriminant groups

```julia
using Oscar, Hecke

# Image of centralizer in O(D_L) - CRITICAL for lifting
G_image, phi = image_centralizer_in_Oq(T_Co_with_isometry)
# G_image = image of O(T_Co, f) in O(D_T_Co, D_f)

# Discriminant representation
pi = discriminant_representation(T_Co, G)
# π: G → O(D_T_Co) orthogonal representation

# Use this to lift orbits from A_T to T_Co
# (the image G_image tells you which discriminant isometries lift)
```

**Functions:** `image_centralizer_in_Oq`, `discriminant_representation`, `integer_lattice_with_isometry`

**Risk reduction:** Medium → Low (library handles lifting via discriminant group)

---

## G3.1: Γ_Co Generators (T-0008)

**Current risk:** High ("infinite group computation")

**Use Oscar.jl instead:**

**Doc:** `theory/backends/oscar-lattices` → Lattices with isometry, Kernel sublattices

```julia
using Oscar, Hecke

# Γ_Co = Stab_O(T_En)(h_Co) ∩ Z_O(T_En)(θ)

# Create lattice with isometry
T_En_f = integer_lattice_with_isometry(T_En, θ)

# Invariant lattice under θ
T_En_inv = invariant_lattice(T_En_f)  # = T_Co if θ is the right involution

# Coinvariant lattice
T_En_coinv = coinvariant_lattice(T_En_f)

# Image of centralizer in O(D_L)
G_image, phi = image_centralizer_in_Oq(T_En_f)

# This gives generators for the image of O(T_En, θ) in O(D_T_En)
# Use this to get generators for Γ_Co
```

**Functions:** `integer_lattice_with_isometry`, `invariant_lattice`, `coinvariant_lattice`, `image_centralizer_in_Oq`

**Risk reduction:** High → Medium (library handles isometry centralizers)

---

## G3.2: Isotropic Plane Orbits (T-0009)

**Current risk:** High ("requires plane orbit enumeration")

**Use buildings.sage instead - THIS IS EXACTLY WHAT IT COMPUTES:**

**Doc:** `theory/backends/buildings` → Main classes, building()

```python
load("src/external/buildings.sage")

# For lattice of signature (2,n), compute Tits' building
# This gives orbits of isotropic lines AND planes

H = SubGp_A2t()  # or appropriate subgroup for your lattice
lines, planes, incid = H.building()

# lines = orbit reps of isotropic lines
# planes = orbit reps of isotropic planes
# incid = incidence relations

# For each plane orbit, compute J^⊥/J
for plane_idx, plane_rep in enumerate(planes):
    # plane_rep is a matrix whose rows span the isotropic plane J
    # Compute J^⊥/J ≅ A_1^⊕7 verification here
    pass
```

**Functions:** `SubGp_A2t`, `SubGp_UU2A2t`, `SubGp_UUmA2t`, `building()`, `incid_rels()`

**Risk reduction:** High → Low (buildings.sage is designed for exactly this)

---

## G4.1: Coxeter Parabolics (T-0005)

**Current risk:** Medium ("combinatorial search")

**Use Oscar.jl Vinberg algorithm instead:**

**Doc:** `theory/backends/oscar-lattices` → Vinberg's algorithm

```julia
using Oscar

# For hyperbolic lattice (signature (1,n)), compute fundamental chamber
Q = gram_matrix(S_Co)  # or appropriate Gram matrix
v0 = matrix(ZZ, [1, 0, 0, ...])  # control vector with v0² > 0

roots = vinberg_algorithm(Q, upper_bound;
                         v0 = v0,
                         root_lengths = [-2])  # for -2-roots

# roots = simple roots of fundamental chamber
# These generate the Weyl group

# Maximal parabolic subdiagrams correspond to subsets of simple roots
# Search subdiagrams of the Dynkin diagram defined by roots
```

**Functions:** `vinberg_algorithm`

**Risk reduction:** Medium → Low (Vinberg's algorithm is implemented)

---

## G5.1: θ Construction (T-0006)

**Current risk:** Medium ("requires involution construction")

**Use Oscar.jl instead:**

**Doc:** `theory/backends/oscar-lattices` → Primitive embeddings and extensions, Equivariant primitive extensions

```julia
using Oscar, Hecke

# Construct Λ_K3 with involution θ such that:
# Λ_K3^θ ≅ T_Co, Λ_K3^-θ ≅ S_Co

# Method 1: From discriminant forms
# Use primitive_extensions with isometries
T_Co_f = integer_lattice_with_isometry(T_Co, id)  # θ acts as +1 on T_Co
S_Co_f = integer_lattice_with_isometry(S_Co, -id)  # θ acts as -1 on S_Co

exists, extensions = equivariant_primitive_extensions(T_Co_f, S_Co_f)
# Returns: [(Λ_K3_f, T_Co_f', S_Co_f')] where θ preserves both

# Method 2: From genus
# If you know the genus of Λ_K3 with θ
exists, extensions = primitive_extensions(T_Co, S_Co;
                                         form_over = [k3_discriminant_form])
```

**Functions:** `equivariant_primitive_extensions`, `integer_lattice_with_isometry`, `primitive_extensions`

**Risk reduction:** Medium → Low (library handles equivariant extensions)

---

## G6.1: Surgery Vector Mapping (T-0010)

**Current risk:** High ("depends on external AEGS23 construction")

**Use Oscar.jl instead:**

**Doc:** `theory/backends/oscar-lattices` → Primitive embeddings and extensions, Admissible equivariant extensions

```julia
using Oscar, Hecke

# Map h_Co to surgery vector ℓ via equivariant extensions
# This requires admissible equivariant primitive extensions

# For p-admissible triples ((A,f_A), (B,f_B), (C,f_C))
extensions = admissible_equivariant_primitive_extensions(Af, Bf, Cf, p, q)
# Returns reps of G_B \ S / G_A

# Use this to find the correct surgery vector ℓ
# such that type(D, f_D^q) = type(C, f_C)
```

**Functions:** `admissible_equivariant_primitive_extensions`, `equivariant_primitive_extensions`

**Risk reduction:** High → Medium (library handles admissible extensions, but AEGS23 criterion still needs formalization)

---

## Summary Table

| Task | Current Risk | Library | Doc | Functions | New Risk |
|------|-------------|---------|-----|-----------|----------|
| G1.2 (T-0001) | Low | Oscar.jl | `oscar_lattices.md` → Creation, Invariants | `integer_lattice`, `genus`, `discriminant_group` | Very Low |
| G1.3 (T-0003) | Medium | Oscar.jl | `oscar_lattices.md` → Primitive embeddings | `primitive_embeddings` | Low |
| G2.1 (T-0004) | Low | GAP | `gap_orbits.md` → Orbit, Stabilizer | `Orbit`, `Orbits`, `Stabilizer` | Very Low |
| G2.2 (T-0007) | Medium | Oscar.jl | `oscar_lattices.md` → Lattices with isometry | `image_centralizer_in_Oq` | Low |
| G3.1 (T-0008) | High | Oscar.jl | `oscar_lattices.md` → Kernel sublattices | `invariant_lattice`, `coinvariant_lattice` | Medium |
| G3.2 (T-0009) | High | buildings.sage | `buildings.md` → Main classes | `building()`, `incid_rels()` | Low |
| G4.1 (T-0005) | Medium | Oscar.jl | `oscar_lattices.md` → Vinberg | `vinberg_algorithm` | Low |
| G5.1 (T-0006) | Medium | Oscar.jl | `oscar_lattices.md` → Equivariant extensions | `equivariant_primitive_extensions` | Low |
| G6.1 (T-0010) | High | Oscar.jl | `oscar_lattices.md` → Admissible extensions | `admissible_equivariant_primitive_extensions` | Medium |

---

## Critical Path

**Highest priority library integrations:**

1. **buildings.sage for G3.2** - This is THE tool for isotropic plane orbits. Risk: High → Low
   - **Doc:** `theory/backends/buildings`
   - **Function:** `building()`, `incid_rels()`

2. **Oscar.jl `primitive_embeddings` for G1.3** - Nikulin theory already implemented. Risk: Medium → Low
   - **Doc:** `theory/backends/oscar-lattices` → Primitive embeddings
   - **Function:** `primitive_embeddings`

3. **Oscar.jl `equivariant_primitive_extensions` for G5.1, G6.1** - Handles isometry-preserving extensions. Risk: High/Medium → Low/Medium
   - **Doc:** `theory/backends/oscar-lattices` → Equivariant/Admissible extensions
   - **Functions:** `equivariant_primitive_extensions`, `admissible_equivariant_primitive_extensions`

4. **GAP for G2.1** - Finite group orbit enumeration. Risk: Low → Very Low
   - **Doc:** `theory/backends/gap-orbits`
   - **Functions:** `Orbit`, `Orbits`, `Stabilizer`

5. **Oscar.jl `image_centralizer_in_Oq` for G2.2, G3.1** - Discriminant group lifting. Risk: Medium/High → Low/Medium
   - **Doc:** `theory/backends/oscar-lattices` → Lattices with isometry
   - **Function:** `image_centralizer_in_Oq`

**Do NOT implement from scratch:**
- Nikulin embedding theory (Oscar.jl has it)
- Tits' building computation (buildings.sage has it)
- Finite group orbit enumeration (GAP has it)
- Vinberg's algorithm (Oscar.jl has it)
- Equivariant primitive extensions (Oscar.jl has it)

**Before ANY computation:**
1. Read relevant doc in `/home/dzack/research/theory/`
2. Find existing function
3. Use it with correct syntax
4. Only then consider custom implementation if NO existing function exists
