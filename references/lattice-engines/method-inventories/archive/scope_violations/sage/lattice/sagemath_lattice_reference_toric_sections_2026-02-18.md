# Archived Sage Reference Sections (Out of Active Scope)

Archived from `docs/sage/lattice/sagemath_lattice_reference.md` on 2026-02-18.

These sections are toric/fan/polytope surfaces and are out of active bilinear-form lattice scope for this project.

## Object Model excerpt (archived)

```text
# ToricLattice(n) — form-free fan lattice for toric geometry; N×M pairing available
#   but NO inner product on N itself; Fan/Cone accept any free ZZ-module as lattice=
#   but silently ignore inner_product_matrix() if present — see §18
# Out-of-scope *Lattice* names with no bridge:
# LatticePolytope, LatticePolytope_PPL — see §18.6
```

## §12 table row (archived)

| Class | Non-degenerate | Integer-valued b | Positive definite | Symmetric |
|-------|:-:|:-:|:-:|:-:|
| `ToricLattice` (on N itself) | N/A — N has no self-pairing | N/A | N/A | N/A — `Fan`/`Cone` accept any free ℤ-module as `lattice=` but ignore its inner product; see §18 |

## §13 gotchas bullets (archived)

- **`LatticePolytope`, `Lattice` (poset) have no bilinear form and no bridge.** They carry the word "lattice" but `gram_matrix()` or `inner_product_matrix()` on them will raise `AttributeError`. See §18.6.
- **`ToricLattice` is a form-free fan lattice; the metric must be carried separately.** `Fan`, `Cone`, and `LatticePolytope` accept any free ℤ-module as their `lattice=` parameter. If you pass an `IntegralLattice`, basic fan construction works but `cone.dual()` raises `AttributeError` (no `dual()` method on `IntegralLattice`) and all methods that should use the inner product silently ignore `inner_product_matrix()`, treating the Gram matrix as the identity instead. The correct workflow is to use `ToricLattice` for the toric machinery and carry the Gram matrix as an external object. See §18 for the full picture and workaround patterns.

## §18 archived section

### 18. Lattices as the A Priori Object for Toric Geometry — and the Missing Integration

### 18.1 The correct mathematical picture

A toric variety is defined by a fan Σ in a **free ℤ-module N of rank n** — the fan lattice. The choice of N is the first datum; the fan is secondary structure built on top of it. Concretely: choosing a ℤ-basis b₁, …, bₙ of N gives a module isomorphism φ: N ≅ ℤⁿ, and each primitive ray generator (or polytope vertex) is specified by its integer coordinates in that basis. The combinatorial data of the fan — which rays span which cones — lives entirely in those coordinate vectors.

**N may carry a bilinear form or may not.** This is orthogonal to the combinatorial structure of the fan:

- If N is a plain free ℤ-module with no form (e.g. `ToricLattice` or `FreeModule(ZZ, n)`), the fan is purely combinatorial: you get the toric variety's topology, its Cox ring, its intersection cohomology ring as an abstract ring, etc.
- If N carries a bilinear form Q (e.g. N is an `IntegralLattice` with Gram matrix G), then Q assigns inner products ⟨rᵢ, rⱼ⟩ = rᵢᵀ G rⱼ to ray generators. This has geometric content: it determines the norms and angles between rays as vectors in the ambient space, feeds into metric properties of the discriminant group N*/N, and in certain constructions (e.g. K3 lattice polarizations, lattice-polarized toric compactifications, string-theory applications) is the primary structure of interest.
- **The bilinear form does not need to be positive definite.** An indefinite lattice — the intersection form on H²(S,ℤ) of a surface, or a Lorentzian lattice — can equally well serve as the fan lattice. The fan data is still well-defined; Q provides additional structure.

The dependency therefore runs: **lattice first, fan second.** The lattice (with whatever form it carries, or none) is the a priori object. You choose a basis, express rays in coordinates, and build the fan. `ToricLattice` is a specific Sage implementation of a form-free fan lattice — one particular option — not the definition of what a fan lattice is.

### 18.2 What `ToricLattice` is and is not

`ToricLattice(n)` (module `sage.geometry.toric_lattice`) is a free ℤ-module of rank n that adds two things plain `FreeModule(ZZ, n)` does not have:

1. **Named N/M duality.** `N.dual()` returns a distinct type M with a canonical ℤ-valued pairing `n * m = Σ nᵢmᵢ`. Sage's `Cone.dual()`, `fan.normal_fan()`, and all toric duality computations depend on this.
2. **Type-checked arithmetic.** Elements of N and M are distinct types; `n + m` raises `TypeError`. This prevents accidentally mixing the fan and character lattices.

`ToricLattice_ambient` inherits from `FreeModule_ambient_pid` — it is a `FreeModule` over ℤ with all standard module operations (`submodule()`, `quotient()`, `hom()`, `direct_sum()`, `saturation()`, etc.). What it does not have is any bilinear form: `n * n` on two elements of the same lattice is a `TypeError` by design.

| Method | Description |
|--------|-------------|
| `N.dual()` | Returns the dual lattice M; `M.dual() is N` |
| `n * m` (n ∈ N, m ∈ M) | Canonical ℤ-pairing Σ nᵢmᵢ |
| `N.submodule(gens)` | ℤ-submodule; returns `ToricLattice_sublattice` |
| `N.submodule_with_basis(gens)` | Submodule with specified (not echelon) basis |
| `N.quotient(sub)` / `N/sub` | Quotient as `ToricLattice_quotient` |
| `Ns.dual()` | Dual of sublattice = quotient of M |
| `N.direct_sum(L)` | Direct sum; returns toric lattice if L is toric, else plain FreeModule |
| `N.hom(matrix, codomain)` | Free module morphism |
| `N.saturation()` | Saturation of sublattice |

`ToricLattice` is not a bilinear-form lattice. It is a convenience wrapper that gives Sage's toric machinery typed N/M duality. It has no `gram_matrix()`, no `inner_product_matrix()`, no `shortest_vector()`, no `discriminant()` in the quadratic-form sense.

### 18.3 What Sage's toric machinery actually accepts

`Fan`, `Cone`, and `LatticePolytope` accept a `lattice=` parameter documented as "ToricLattice, ℤⁿ, or any other object that behaves like these." In practice, "behaves like" means: base ring ℤ, supports element construction from tuples, elements support ℤ-linear arithmetic, has `rank()`. Both `IntegralLattice` and `FreeQuadraticModule` satisfy these requirements.

**What works when you pass an `IntegralLattice` as the fan lattice:**

```python
G = matrix(ZZ, [[2, 1], [1, 2]])    # e.g. A2 root lattice
L = IntegralLattice(G)

# Express primitive ray generators as integer coordinate vectors in the chosen basis
rays = [L([1, 0]), L([0, 1]), L([-1, -1])]
fan = Fan(cones=[(0,1), (1,2), (2,0)], rays=rays, lattice=L)
# Works: Fan is constructed, fan.rays() returns elements of L
```

**What fails immediately:**

```python
fan.dual_cone()    # or cone.dual()
# AttributeError: 'IntegralLattice_with_category' object has no attribute 'dual'
# cone.dual() calls L.dual() — IntegralLattice has no dual() method
```

`fan.normal_fan()`, `LatticePolytope.normal_fan()`, `cone.facet_normals()` returning dual-lattice elements, and `ToricVariety(fan)` all fail for the same reason. The entire dual/normal-fan apparatus requires `L.dual()`.

**What is silently wrong when a form is present:**

Even when fan construction succeeds, **none of the toric methods use `L.inner_product_matrix()`**. `cone.Hilbert_basis()`, `cone.lattice_points()`, `cone.dual()` (when it works), ray normalization — all operate on bare integer coordinates and implicitly treat the Gram matrix as the identity. If G is not the identity matrix, any computation involving lengths, angles, or duality in the metric sense returns the wrong answer with no error or warning.

This is the core architectural gap: **`Fan` and `Cone` carry a lattice parameter but treat it as pure combinatorial data. The form, if present, is inert.**

### 18.4 What a correct integration would require

For a bilinear-form lattice L to function as a first-class fan lattice in Sage, the toric machinery would need:

1. **`L.dual()` returning L^∨** — the dual lattice equipped with the dual form G^{-1}, with the canonical evaluation pairing L × L^∨ → ℤ. For a unimodular lattice this is an isomorphism L ≅ L^∨; for non-unimodular lattices it is distinct.
2. **Metric-aware `cone.Hilbert_basis()` and `cone.lattice_points()`** — these currently iterate over integer points using bare ℤⁿ structure and are form-independent. For a non-standard G they return results that are correct combinatorially but geometrically meaningless without knowing G.
3. **`fan.discriminant_group()` using G** — the discriminant group L^∨/L has invariants (discriminant form, genus symbol) derived from G. Currently these are not computed from the fan lattice.
4. **`cone.dual()` using the metric dual** — the metric dual of a cone C is {y ∈ L^∨_ℝ : ⟨x,y⟩_G ≥ 0 for all x ∈ C}, which differs from the combinatorial dual when G ≠ I.

None of these are currently implemented.

### 18.5 How to work with metric lattices and fans today

The practical pattern is: use `ToricLattice` for all toric machinery, carry the Gram matrix separately, and apply it manually when metric data is needed.

```python
# Lattice of interest: A2 root lattice with Gram matrix G
G = matrix(ZZ, [[2, 1], [1, 2]])
L = IntegralLattice(G)

# Choose a basis: standard basis of ZZ^2 = the simple roots of A2
# Ray generators in these coordinates:
ray_coords = [(1, 0), (0, 1), (-1, -1)]   # simple roots and their negated sum

# Build the fan in a ToricLattice (required for full toric functionality)
N = ToricLattice(2)
fan = Fan(cones=[(0,1), (1,2), (2,0)], rays=[N(r) for r in ray_coords])

# Apply metric data explicitly when needed
B = matrix(ZZ, ray_coords)                 # rows = ray generators
gram_of_rays = B * G * B.T                 # ⟨rᵢ, rⱼ⟩_G  — metric Gram matrix of rays
norms_squared = [G[0,0]*r[0]^2 + 2*G[0,1]*r[0]*r[1] + G[1,1]*r[1]^2
                 for r in ray_coords]      # or: (B * G * B.T).diagonal()

# Discriminant group of L (from L, not from fan):
L.discriminant_group()                     # works — uses G directly on IntegralLattice
L.gram_matrix().det()                      # discriminant |det G|

# LLL-reduce the row basis in Euclidean embedding space:
from sage.modules.free_module_integer import IntegerLattice
L_rows = IntegerLattice(B)
L_rows.LLL()

# If you need reduction of the row-lattice Gram matrix under G, use Gram-level LLL:
U = (B * G * B.T).LLL_gram()
G_red = U.transpose() * (B * G * B.T) * U
```

**For the dual fan / character lattice:** The combinatorial dual fan requires only `N.dual()` = M, which `ToricLattice` provides. If you need the metric dual — the lattice M carrying the dual form G^{-1} — you must construct it separately:

```python
# Character lattice M with dual form G^{-1}
G_dual = G.inverse().change_ring(QQ)        # dual form; may be rational
# If G is unimodular (det = ±1), G_dual is integral:
if G.det().abs() == 1:
    L_dual = IntegralLattice(G_dual.change_ring(ZZ))

# Pairing between L and L_dual at the level of coordinate vectors:
# ⟨b, b*⟩ = b^T · (G · G^{-1}) · b* = b^T · b*  (i.e., the standard dot product
# in coordinates when using the dual basis for L_dual)
# This matches what ToricLattice's n * m computes.
```

### 18.6 Other `*Lattice*` classes with no toric relevance

| Class | Module | What it is |
|-------|--------|------------|
| `LatticePolytope` | `sage.geometry.lattice_polytope` | Convex polytope with integer vertices; PALP interface; no bilinear form; no free-module structure |
| `LatticePolytope_PPL` | `sage.geometry.polyhedron.ppl_lattice_polytope` | PPL-backed variant; same |
| `Lattice` (poset) | `sage.combinat.posets.lattices` | Finite meet-semilattice in the order-theoretic sense; entirely unrelated |
| `gen_lattice(lattice=True)` | `sage.crypto.lattice` | Returns `IntegerLattice` (Euclidean form) when `lattice=True`; otherwise a bare matrix |

These carry the word "lattice" but have no structural relationship to fan lattices or bilinear-form lattices and no role in the discussion above.
