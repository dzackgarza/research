# buildings: Tits' buildings for O(2,n) subgroups

**Source:** https://github.com/m-dawes/buildings

**Local:** `/home/dzack/research/src/external/buildings.sage`

**Author:** Matthew Dawes (same as Indefinite.jl and arXiv:2205.10601)

**What it computes:** Tits' buildings for subgroups of O(2,n) — orbits of totally isotropic lines and planes in L ⊗ ℚ, plus incidence relations between them.

---

## Usage

```python
load("src/external/buildings.sage")

H = SubGp_A2t()
H.building()
```

### SubGp_A2t — Õ⁺(2U + A₂)

```python
load("src/external/buildings.sage")

H = SubGp_A2t()
H.building()
```

**Returns:** `[lines, planes, incid]`
- `lines` — list of orbits of totally isotropic lines
- `planes` — list of orbits of totally isotropic planes  
- `incid` — list of `(i,j)` pairs where plane `i` is incident to line `j`

**Attributes set by `H.building()`:**
- `H.lines` — orbit representatives for isotropic lines
- `H.planes` — orbit representatives for isotropic planes

**Note:** Calculations may take "several minutes to several hours" depending on the group.

---

### SubGp_GK — Õ⁺(2U + ⟨-6⟩ + ⟨-2⟩)

```python
H = SubGp_GK()
H.building()
```

---

### SubGp_UU2A2t — Õ⁺(U + U(2) + A₂)

```python
H = SubGp_UU2A2t()
H.building()
```

---

### SubGp_UUmA2t — Õ⁺(U + U(m) + A₂)

```python
H = SubGp_UUmA2t(m, N)  # m, N positive integers
H.building()
```

**Parameters:**
- `m` — scaling factor for second hyperbolic plane
- `N` — level for principal congruence subgroup Γ(N)

---

### SubGp_U2U2A2t — Õ⁺(U(2) + U(2) + A₂)

```python
H = SubGp_U2U2A2t()
H.building()
```

---

## Key methods (all SubGp classes)

```python
# Compute building (orbits + incidence)
H.building()  # Returns [lines, planes, incid]

# Get isotropic line orbit representatives
H.identify_bc_e()  # Returns [g_i] such that [g_i·e] are inequivalent lines

# Get isotropic plane orbit representatives  
H.identify_bc_E()  # Returns [g_i] such that [g_i·E] are inequivalent planes

# Get incidence relations
H.incid_rels()  # Returns [(i,j), ...] pairs

# Test if plane E contains vector equivalent to g·e under SubGp
H.line_plane_incid(e1, e2, gk, u)
```

---

## BigGp class — O⁺(2U + A₂)

**Base group containing all SubGp classes above.**

```python
G = BigGp()

# Inner product in 2U+A₂
val = G.ip(x, y)  # Returns (x^T · gm · y)[0,0]

# Eichler transvection t(e,a) for isotropic e and a ∈ e^⊥/e
T = G.make_eichler(e, a)

# Reflection in reflective vector a
R = G.make_reflection(a)

# Embed SL(2,Z) into 6×6 via left/right action
A_left = G.SL_emb_left(A)   # A is 2×2
B_right = G.SL_emb_right(B) # B is 2×2

# Generators for O(2U+A₂) (22 total)
gens = G.make_gens()

# Generators for stabilizers
gens_stab_E = G.make_gens_stab_E()  # Stab(E) for isotropic plane E
gens_stab_e = G.make_gens_stab_e()  # Stab(e) for isotropic line e
```

**Gram matrix of 2U+A₂:**
```
gm = [[0,1,0,0,0,0], [1,0,0,0,0,0], [0,0,0,1,0,0], 
      [0,0,1,0,0,0], [0,0,0,0,-2,-1], [0,0,0,0,-1,-2]]
```

---

## Ell class — Principal congruence subgroup Γ(N) ⊂ SL(2,ℤ)

```python
Gamma = Ell(N)

# Test if matrix x ∈ SL(2,ℤ) belongs to Γ(N)
Gamma.in_gamma_N(x)  # True if x[0,1], x[1,0] ≡ 0 (mod N) and x[0,0], x[1,1] ≡ 1 (mod N)

# Test if x·Γ(N) ∈ gens·Γ(N)
Gamma.in_gens(x, gens)

# Expected index [SL(2,ℤ) : Γ(N)]
size = Gamma.expected_size()  # = N³ · ∏_{p|N}(1-1/p²)

# Get coset representatives
cosets = Gamma.make_gamma_N()
```

---

## Helper functions (SubGp classes)

```python
# Test membership in subgroup
H.in_gp(x)  # True if x ∈ SubGp

# Coset membership tests
H.in_right_cosets(x, cosets)  # True if SubGp·x ∈ SubGp·cosets
H.in_left_cosets(x, cosets)   # True if x·SubGp ∈ cosets·SubGp

# Compute coset representatives
H.make_right_cosets()  # For SubGp\BigGp
H.make_left_cosets()   # For BigGp/SubGp

# Stabilizer cosets (conjugated)
H.make_right_cosets_stab_e_cong(g)
H.make_left_cosets_stab_e_cong(g)
H.make_right_cosets_stab_E_cong(g)
H.make_left_cosets_stab_E_cong(g)

# Gritsenko-Hulek-Sankaran criterion: find g with gx=y for primitive isotropic x,y
g = H.eichler_equiv(x, y)

# SL(2,ℤ)/Γ(N) representatives for primitive isotropic vectors in plane E
reps = H.iso_classes_in_E(e1, e2)

# Reduce vector to L₁ subspace
x_red = H.red_L1(x)

# Coprime combination coefficients
coeffs = H.coprime_comb(x)
```

---

## Lattice signatures

All classes work with **indefinite lattices of signature (2,n)**:

| Class | Lattice | Signature |
|-------|---------|-----------|
| `SubGp_A2t` | 2U + A₂ | (2, 4) |
| `SubGp_GK` | 2U + ⟨-6⟩ + ⟨-2⟩ | (2, 4) |
| `SubGp_UU2A2t` | U + U(2) + A₂ | (2, 4) |
| `SubGp_UUmA2t(m,N)` | U + U(m) + A₂ | (2, 4) |
| `SubGp_U2U2A2t` | U(2) + U(2) + A₂ | (2, 4) |
| `BigGp` | 2U + A₂ | (2, 4) |

---

## Application: Baily-Borel compactification boundary

The building data computes the boundary configuration of orthogonal modular varieties:

```python
H = SubGp_A2t()
lines, planes, incid = H.building()

# Boundary components:
# - One modular curve C_Π for each plane orbit in `planes`
# - One cusp Q_ℓ for each line orbit in `lines`
# - Incidence: Q_ℓ ⊂ closure(C_Π) iff (plane_idx, line_idx) in `incid`
```

**Reference:** Theorem 1.5 in Dawes, "Orbits in Lattices" (arXiv:2205.10601)
