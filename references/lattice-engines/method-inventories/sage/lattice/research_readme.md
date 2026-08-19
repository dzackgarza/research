# SageMath Lattice Reference
## Lattice = free ℤ-module with symmetric bilinear form

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Requires or only meaningful for **positive definite** forms |
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[INDEF]` | Works correctly for **indefinite** signatures; may note limitations |
| `[DEG]` | Works with **degenerate** forms |
| `[INT]` | Defined over **ℤ** (integer-valued bilinear form) |
| `[RAT]` | Defined over **ℚ** |
| `[FIELD]` | Defined over a **field** (ℚ, ℝ, finite fields, etc.) |
| `[EUCLID]` | Metric is the ambient Euclidean I_n, fixed by the concrete embedding in ℝ^n (as in `IntegerLattice`); bilinear form cannot be independently specified |
| `[PARI]` | Delegates to **PARI/GP** |
| `[FPLLL]` | Delegates to **fplll/fpylll** |
| `[EVEN]` | Requires even lattice (all (x,x) ∈ 2ℤ) |

---

## Object Model Overview

```
FreeModule(ZZ, n, inner_product_matrix=G)      # general free quadratic module
    └── FreeQuadraticModule(R, n, G)            # explicit bilinear form over any commutative ring R
            │  FreeQuadraticModule_generic       # methods: inner_product_matrix, gram_matrix,
            │      _generic_pid                  #          determinant, discriminant, ambient_module
            │          _generic_field            #          span, span_of_basis (field: echelonised)
            └── IntegralLattice(G)              # ND, symmetric, integral (b: L×L→ℤ)
                    (sage.modules.free_quadratic_module_integer_symmetric)

IntegerLattice(B)                              # concrete sublattice of (ZZ^n, I_n); Gram = B·B^T
    (sage.modules.free_module_integer)         # [PD only; form fixed by embedding]

QuadraticForm(R, n, coeffs)                    # the form q itself, not module
    (sage.quadratic_forms.quadratic_form)

TorsionQuadraticModule(V, W)                   # finite ℤ-module A=V/W with bil/quad form
    (sage.modules.torsion_quadratic_module)

BinaryQF(a, b, c)                              # ax²+bxy+cy² over ℤ; special binary methods
TernaryQF(coeffs)                              # ternary form over ℤ

Genus(A)                                       # genus of an integral lattice
LocalGenusSymbol(A, p)                         # local genus at prime p

GroupOfIsometries(deg, R, gens, bil_form)      # isometry group with named preserved form
    (sage.groups.matrix_gps.isometries)        # returned by IntegralLattice.orthogonal_group()

# Root-system realizations — separate combinatorial hierarchy, no gram_matrix()
RootSystem(type).root_lattice()                # ℤ-module; pairing via .scalar(coroot)
RootSystem(type).ambient_space()               # ℚ-module; Euclidean .inner_product(y)
# → bridge: IntegralLattice("E8") wraps Cartan Gram matrix in IntegralLattice

# Number-field ideals ARE free ℤ-modules (rank n), but without stored metric:
# NumberFieldFractionalIdeal.free_module() → bare FreeModule(ZZ, n) — no inner product
# NumberFieldFractionalIdeal.basis() / integral_basis() → ℤ-basis elements
# Bridge: IntegralLattice(matrix(QQ, n, n, lambda i,j: (B[i]*B[j]).trace())) — see §17

# Quaternion algebra ideals DO carry the metric natively:
# QuaternionAlgebra.free_module()      → FreeQuadraticModule (reduced norm form)
# QuaternionFractionalIdeal.gram_matrix() → Gram matrix of reduced norm — see §17.4

```

**Critical distinction:**
- `IntegralLattice` — abstract lattice specified by a Gram matrix. The bilinear form is a primary input, independent of any basis. Supports all signatures.
- `IntegerLattice` — concrete sublattice of (ℤ^n, I_n). The Gram matrix B·Bᵀ is *derived* from the embedding; it cannot be set independently. Restricted to PSD forms. Algorithms operate on basis vectors using the induced Euclidean form and produce new bases spanning the same lattice.
- `QuadraticForm` is a form, not a module; no ambient lattice distinguished
- `RootSystem(type).root_lattice()` — combinatorial ℤ-module with Cartan pairing; no `gram_matrix()` method; use `IntegralLattice("An")` to get an `IntegralLattice` wrapping the same data (see §16)
- `NumberFieldFractionalIdeal` and `Order` — free ℤ-modules of rank n with natively accessible ℤ-bases (`.basis()`, `.integral_basis()`), but their `.free_module()` returns a bare `FreeModule` with no inner product. The trace form `b(x,y) = Tr(xy)` gives the metric, but must be computed separately and wrapped in `IntegralLattice` or `FreeQuadraticModule` for lattice-theory methods. Contrast with `QuaternionAlgebra` ideals, which carry `gram_matrix()` natively (see §17).

---

## 1. Construction Functions

### 1.1 `IntegralLattice(data, basis=None)` `[INT, ND]`
`sage.modules.free_quadratic_module_integer_symmetric`

Constructs a symmetric non-degenerate integral lattice. **Allows indefinite signatures.**

`data` accepts:
| Input | Result |
|-------|--------|
| `Matrix(ZZ/QQ, n, n)` symmetric | Gram matrix as ambient space |
| integer `n` | Rank-n Euclidean lattice (I_n) |
| Cartan type string e.g. `"E8"` | Root lattice by Cartan matrix — **requires `sage.graphs`** |
| Cartan type list e.g. `["A",3]` | Same |
| `"U"` / `"H"` | Hyperbolic plane `[[0,1],[1,0]]` `[INDEF]` |

`basis` — optional matrix/list of vectors; rows span the sublattice in the ambient space.

```python
IntegralLattice(matrix(ZZ, [[2,1],[1,-2]]))        # indefinite, rank 2
IntegralLattice(3)                                  # I_3  [PD]
IntegralLattice("E8")                               # E8 root lattice  [PD]
IntegralLattice("U")                                # hyperbolic plane U  [INDEF]
IntegralLattice(matrix.identity(3), [[1,-1,0],[0,1,-1]])  # A2 from ambient I_3
```

### 1.2 `FreeQuadraticModule(R, n, inner_product_matrix)` `[DEG, INDEF]`
`sage.modules.free_quadratic_module`

General constructor over any commutative ring R. Allows degenerate and indefinite forms. Full functionality only over ℤ and fields. The `inner_product_matrix` need not be symmetric. **See §14 for the full class hierarchy and method list.**

```python
FreeQuadraticModule(ZZ, 2, matrix([[0,1],[1,0]]))  # hyperbolic plane, more general
VectorSpace(QQ, 3, inner_product_matrix=M)         # ambient quadratic space over field
```

### 1.3 `FreeModule(ZZ, n, inner_product_matrix=G)` `[DEG, INDEF]`
Alias route; returns same type as `FreeQuadraticModule` when `inner_product_matrix` is given.

### 1.4 `IntegerLattice(basis, lll_reduce=True)`
`sage.modules.free_module_integer`

Concrete sublattice of the ambient Euclidean space **(ℝ^n, I_n)**. Rows of `basis` are the basis vectors; the bilinear form is the restriction of the standard inner product, so the Gram matrix is **B·Bᵀ** and is always positive semi-definite (positive definite when B has full column rank). The bilinear form is not a free parameter — it is fixed by the embedding. **Indefinite lattices cannot be represented.** All reduction and vector-finding algorithms (LLL, BKZ, SVP, CVP) operate on the basis vectors using this induced form; they produce a new basis U·B spanning the same lattice with Gram matrix U·(B·Bᵀ)·Uᵀ. Designed for cryptographic/algorithmic lattice problems.

```python
from sage.modules.free_module_integer import IntegerLattice
IntegerLattice([[1,0],[0,2]])                      # Gram = [[1,0],[0,4]]
IntegerLattice(matrix(ZZ, 3, 3, range(9)))
```

### 1.5 `QuadraticForm(R, n, coeffs)` `[FIELD, INT]`
`sage.quadratic_forms.quadratic_form`

The form itself. `coeffs` lists the n(n+1)/2 upper-triangle entries row by row.

```python
QuadraticForm(ZZ, 2, [1, 3, 2])          # x^2 + 3xy + 2y^2
QuadraticForm(QQ, 3, range(6))
QuadraticForm.from_polynomial(f)          # from polynomial in ring
DiagonalQuadraticForm(R, [a, b, c, ...]) # diagonal form
```

### 1.6 `TorsionQuadraticModule(V, W, ...)` `[INT]`
`sage.modules.torsion_quadratic_module`

Finite ℤ-module A = V/W with inherited bilinear/quadratic form. W ⊆ V ⊆ V⊗ℚ.

```python
TorsionQuadraticForm(q)    # from rational Gram matrix; bilinear form non-degenerate
TorsionQuadraticModule(V, W)
```

### 1.7 `BinaryQF(a, b=None, c=None)` `[INT, DEG, INDEF]`
Binary form ax²+bxy+cy². Accepts `[a,b,c]` list, or polynomial.

### 1.8 `TernaryQF(coeffs)` `[INT]`
Ternary form over ℤ; coeffs = [a,b,c,r,s,t] for ax²+by²+cz²+ryz+sxz+txy.

### 1.9 Crypto lattice generation
`sage.crypto.gen_lattice(type, n, m, q, seed, lattice=False)`

Generates algorithm-relevant lattice bases embedded in ℤ^m with the standard Euclidean structure. `lattice=True` returns `IntegerLattice`.

| `type` | Description |
|--------|-------------|
| `'random'` | Random q-ary lattice |
| `'modular'` | Modular/q-ary |
| `'ideal'` | Ideal lattice |
| `'cyclotomic'` | Cyclotomic ideal lattice |
| `'ntru'` | NTRU-type |

### 1.10 Random forms
```python
random_quadraticform(R, n)                         # random QuadraticForm over R
random_quadraticform_with_conditions(R, n, [cond]) # e.g. cond = is_positive_definite
random_ternaryqf()
random_ternaryqf_with_conditions([cond])
```

---

## 2. Special Named Lattices
Via `IntegralLattice(name)` — all are `[PD, INT]` unless noted.

### Root lattices (Cartan types via `sage.combinat`)
| Name | Rank | det(G) | Notes |
|------|------|--------|-------|
| `"A1"` | 1 | 2 | — |
| `"An"` | n | n+1 | n ≥ 1 |
| `"Dn"` | n | 4 | n ≥ 3 |
| `"E6"` | 6 | 3 | — |
| `"E7"` | 7 | 2 | — |
| `"E8"` | 8 | 1 | Even, unimodular |
| `"B2"`, `"G2"`, etc. | — | — | Non-simply-laced; Gram matrix from Cartan matrix |

All Cartan types accepted by `CartanMatrix()` work.

### Special lattices
| Construction | Description | Signature |
|--------------|-------------|-----------|
| `IntegralLattice("U")` or `IntegralLattice(matrix(ZZ,2,[0,1,1,0]))` | Hyperbolic plane `[[0,1],[1,0]]` | (1,1) `[INDEF]` |
| `IntegralLattice(n)` | Rank-n Euclidean I_n | (n,0) `[PD]` |
| `IntegralLattice(matrix.diagonal([1]*8))` | I_8 (odd unimodular) | (8,0) `[PD]` |
| `IntegralLattice("E8").direct_sum(IntegralLattice("E8"))` | II_{16,0} | (16,0) `[PD, EVEN]` |
| `IntegralLattice(matrix.diagonal([1,-1]))` | I_{1,1} Lorentzian | (1,1) `[INDEF]` |

**Leech lattice, Niemeier lattices**: No built-in string constructor. Construct from explicit 24×24 Gram matrix, or use `Genus` representative methods.

---

## 3. `IntegralLattice` / `FreeQuadraticModule_integer_symmetric` Methods
`[INT, ND]` unless otherwise noted.

### Intrinsic data
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `gram_matrix()` | — | `Matrix<Integer>` | Gram matrix of current basis: B·M·Bᵀ where B = `basis_matrix()` and M = `inner_product_matrix()` | |
| `inner_product_matrix()` | — | `Matrix<Integer>` | Gram matrix of ambient space | |
| `inner_product(u, v)` | `u, v`: vector elements | `Integer` | Bilinear form value b(u,v) for lattice elements u, v; alias: `b(u, v)` | |
| `basis_matrix()` | — | `Matrix<Integer>` | Rows form current basis | |
| `degree()` | — | `Integer` | Dimension of ambient space | |
| `rank()` | — | `Integer` | Rank of lattice | |
| `is_positive_definite()` | — | `bool` | Positive definite test | `[PD]` |
| `is_negative_definite()` | — | `bool` | Negative definite test | |
| `is_definite()` | — | `bool` | Positive or negative definite | |
| `is_indefinite()` | — | `bool` | Indefinite test | `[INDEF]` |
| `is_even()` | — | `bool` | All (x,x) ∈ 2ℤ | |
| `is_unimodular()` | — | `bool` | \|det(Gram)\| = 1 | |
| `signature_pair()` | — | `tuple<Integer, Integer>` | (p, n) count of ±1 eigenvalues | `[INDEF ok]` |
| `signature()` | — | `Integer` | p − n | `[INDEF ok]` |
| `discriminant()` | — | `Integer` | det(Gram) | |

### Structural operations
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `direct_sum(other)` | `other`: `IntegralLattice` | `IntegralLattice` | Orthogonal direct sum | |
| `sublattice(basis)` | `basis`: `Matrix` or list | `IntegralLattice` | Sublattice spanned by vectors; must be integral | `[INT]` |
| `overlattice(gens)` | `gens`: `Matrix` or list | `IntegralLattice` | Overlattice spanned by L ∪ gens | `[RAT]` |
| `tensor_product(other)` | `other`: `IntegralLattice` | `IntegralLattice` | Tensor product | |
| `dual_lattice()` | — | `FreeQuadraticModule` | L∨ = {x ∈ L⊗ℚ : (x,ℓ) ∈ ℤ ∀ℓ} | |
| `orthogonal_complement(M)` | `M`: submodule or list | `FreeQuadraticModule` | Orthogonal complement of M in L; M is a submodule or list of vectors | |
| `discriminant_group(s=0)` | `s`: `Integer` (optional) | `TorsionQuadraticModule` | L∨/L as TorsionQuadraticModule; s-primary part if s≠0 | |
| `change_basis(M)` | `M`: `Matrix` | `IntegralLattice` | Lattice with new basis matrix M | |
| `maximal_overlattice(p=None)` | `p`: prime (optional) | `IntegralLattice` | Maximal even integral overlattice; if p given, maximise only at p | `[EVEN if p=None or p=2]` |
| `is_primitive(M)` | `M`: submodule or list | `bool` | Whether submodule M is primitive (L/M is torsion-free) | |

### Arithmetic / Vector enumeration
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `lll()` / `LLL()` | — | `IntegralLattice` | Return new LLL-reduced `IntegralLattice`; `lll` is alias for `LLL`; works on indefinite examples in the official docs | |
| `enumerate_short_vectors()` | — | `iterator` | Iterator over all non-zero vectors (mod sign); uses lattice inner product; **does not guarantee non-decreasing norm order** — a vector of larger norm may be yielded before one of smaller norm (Sage 10.3+) | |
| `enumerate_close_vectors(target)` | `target`: vector | `iterator` | Iterator over lattice vectors closest to `target`; **does not guarantee non-decreasing distance order** — the first element yielded is not guaranteed to be the closest (Sage 10.3+) | |
| `short_vectors(n)` | `n`: `Integer` | `list<tuple>` | List of vectors x with (x,x) ≤ n | `[PD, PARI]` |
| `minimum()` / `min()` | — | `Integer` | min{(x,x) : x ∈ L \ {0}}; finite for PD, −∞ otherwise | |
| `maximum()` / `max()` | — | `Integer` | max{(x,x) : x ∈ L \ {0}}; finite for negative definite, +∞ otherwise | |
| `twist(n, discard_basis=False)` | `n`: scalar, `discard_basis`: `bool` (optional) | `IntegralLattice` | New lattice with form scaled by n | `[INDEF ok]` |
| `genus()` | — | `Genus` | `Genus` object of this lattice | `[ND]` |
| `theta_series(prec)` | `prec`: `Integer` | `power series` | Theta series Σ q^{(x,x)/2} | `[PD, PARI]` |
| `quadratic_form()` | — | `QuadraticForm` | `QuadraticForm` from Gram matrix | |

### Symmetry
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `orthogonal_group(gens, is_finite)` | `gens`: `Matrix` list (optional), `is_finite`: `bool` | `MatrixGroup` | Matrix group of isometries of ambient space preserving L; generators computed automatically if `gens=None` | `[DEFINITE — indefinite raises NotImplementedError]` |
| `automorphisms(gens, is_finite)` | `gens`: `Matrix` list (optional), `is_finite`: `bool` | `MatrixGroup` | Alias for `orthogonal_group()` | `[DEFINITE]` |

---

## 4. `IntegerLattice` / `FreeModule_submodule_with_basis_integer` Methods
Concrete sublattice of **(ℝ^n, I_n)**. Gram matrix = B·Bᵀ (always PSD). Bilinear form fixed by embedding; indefinite lattices impossible. All algorithms work with the form induced by the embedding, producing new bases for the same lattice.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `LLL(*args, **kwds)` | `*args, **kwds`: LLL parameters | `Matrix` | LLL basis reduction; **returns new basis matrix** AND updates `self.reduced_basis` in-place; passes all args to `Matrix.LLL()` | `[FPLLL]` |
| `BKZ(*args, **kwds)` | `*args, **kwds`: BKZ parameters (e.g. `block_size=`) | `Matrix` | BKZ basis reduction; returns matrix, updates `self.reduced_basis`; passes args to `Matrix.BKZ()` | `[FPLLL]` |
| `HKZ(*args, **kwds)` | — | `Matrix` | Hermite-Korkine-Zolotarev reduction; equivalent to `BKZ(block_size=self.rank())` | `[FPLLL]` |
| `shortest_vector()` | — | `Vector` | Exact shortest vector (SVP) | `[FPLLL]` |
| `closest_vector(t)` | `t`: `Vector` | `Vector` | Exact closest vector to target t (CVP) | `[FPLLL]` |
| `approximate_closest_vector(t, delta=None, algorithm='embedding', ...)` | `t`: `Vector`, `delta`: `float` (optional), `algorithm`: `str` | `Vector` | Approx CVP; runs LLL if not already δ-reduced; `algorithm`: `'embedding'`, `'nearest_plane'` (Babai), `'rounding_off'` | |
| `babai(target, *args, **kwds)` | `target`: `Vector`, `*args, **kwds`: LLL parameters | `Vector` | Babai nearest-plane approximation to CVP; convenience wrapper around reduction data | `[FPLLL]` |
| `update_reduced_basis(*args, **kwds)` | `*args, **kwds`: LLL parameters | — | Refresh cached reduced basis used by approximate-CVP helpers | `[FPLLL]` |
| `discriminant()` | — | `Integer` | det(B·Bᵀ) | |
| `volume()` | — | `Real` | Covolume of the lattice in the ambient Euclidean space | |
| `reduced_basis` | — | `Matrix` | Property: current basis matrix after last reduction call | |
| `voronoi_cell()` | — | `Polyhedron` | Voronoi cell as a polytope | `[PD]` |
| `voronoi_relevant_vectors()` | — | `list<Vector>` | Vectors defining Voronoi cell facets | `[PD]` |

---

## 5. `QuadraticForm` Methods
`[INT or FIELD]` depending on base ring; base ring explicit in constructor.

### Intrinsic data
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `base_ring()` | — | `Ring` | Ring R | |
| `dim()` | — | `Integer` | Number of variables n | |
| `rank()` | — | `Integer` | Rank of Gram matrix | |
| `matrix()` | — | `Matrix` | **Hessian matrix A** where Q(x) = **(1/2) xᵀ A x**; A[i,i] = 2·Q[i,i], A[i,j] = Q[i,j] for i≠j; = `Hessian_matrix()`; note A = 2·`Gram_matrix()` | |
| `Gram_matrix()` | — | `Matrix` | **Gram matrix G** where Q(x) = **xᵀ G x**; G[i,i] = Q[i,i], G[i,j] = Q[i,j]/2 for i≠j; G = `matrix()`/2 | |
| `Gram_matrix_rational()` | — | `Matrix` | Same as `Gram_matrix()` but over ℚ | `[RAT]` |
| `Hessian_matrix()` | — | `Matrix` | Same as `matrix()` — alias for the Hessian A; Q(x) = (1/2) xᵀ A x | |
| `polynomial()` | — | `Polynomial` | Polynomial representation | |
| `content()` | — | `Integer` | gcd of all coefficients | `[INT]` |
| `coefficients()` | — | `list` | List of all n(n+1)/2 upper-triangle coefficients by reading across rows from main diagonal | |
| `det()` | — | `Integer` or `Rational` | det(**Hessian**) = det(`matrix()`) = det(2·Gram) — **not** det(Gram); use `Gram_det()` for det(G) | |
| `Gram_det()` | — | `Rational` | det(`Gram_matrix()`) = det(G); defined over fraction field | `[RAT]` |
| `discriminant()` | — | `Integer` | det(Gram_matrix) = det(G); same as `Gram_det()` for integer forms | `[INT]` |
| `level()` | — | `Integer` | Smallest N: N·Q^{-1} integral | `[INT]` |
| `scale_by_factor(c)` | `c`: `RingElement` | `QuadraticForm` | Multiply Q by scalar c | |
| `change_ring(R)` | `R`: `Ring` | `QuadraticForm` | Change base ring | |
| `base_change_to(M)` | `M`: `Matrix` | `QuadraticForm` | Q(Mx) | |

### Definiteness
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `compute_definiteness()` | — | `None` | Caches definiteness string "pos_def"/"neg_def"/"indef"/"zero"/"degenerate" | `[ND ok]` |
| `compute_definiteness_string_by_determinants()` | — | `str` | Same as `compute_definiteness()` but via upper-left subdeterminant signs; returns the string directly | |
| `is_positive_definite()` | — | `bool` | All eigenvalues > 0 | `[PD]` |
| `is_negative_definite()` | — | `bool` | All eigenvalues < 0 | |
| `is_definite()` | — | `bool` | Positive or negative definite (not zero, not degenerate, not indefinite) | |
| `is_indefinite()` | — | `bool` | Mixed signs; **degenerate forms are neither definite nor indefinite** | `[INDEF]` |
| `is_degenerate()` | — | `bool` | det = 0 | `[DEG]` |
| `signature()` | — | `Integer` | p − n | |
| `signature_vector()` | — | `tuple` | (p, n, z): positive, negative, zero eigenvalue counts | |

### Equivalence and classification
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `is_globally_equivalent_to(other, return_matrix)` | `other`: `QuadraticForm`, `return_matrix`: `bool` | `bool` or `tuple` | GL_n(ℤ) equivalence | `[INT, PD for reliability, PARI]` |
| `is_locally_equivalent_to(other, p)` | `other`: `QuadraticForm`, `p`: `Integer` | `bool` | Local equivalence at p (p=−1 for ∞) | `[INT, INDEF ok]` |
| `local_normal_form(p)` | `p`: `Integer` | `QuadraticForm` | Jordan decomposition at prime p | `[INT, PARI]` |
| `p_adic_normal_form(p, ...)` | `p`: `Integer`, ... | `QuadraticForm` | p-adic canonical form | `[INT]` |
| `global_normal_form()` | — | `QuadraticForm` | Reduce over ℤ | `[PD, PARI]` |
| `rational_diagonal_form(return_matrix)` | `return_matrix`: `bool` | `QuadraticForm` or `tuple` | Diagonalize over ℚ | `[FIELD]` |
| `is_rationally_isometric(other)` | `other`: `QuadraticForm` | `bool` | ℚ-isometry | `[FIELD]` |
| `genus()` | — | `Genus` | Genus object | `[INT, ND]` |
| `genera(sig_pair, determinant, max_scale=None, even=False)` | `sig_pair`: `tuple[int, int]`, `determinant`: `Integer` (sign ignored), `max_scale`: `Integer` or `None`, `even`: `bool` (default `False`) | `list[GenusSymbol_global_ring]` | All non-empty global genera with given signature pair and determinant `[static]` | `[INT]` |
| `is_in_genus(G)` | `G`: `Genus` | `bool` | Membership in genus G | `[INT]` |

### Local/Global invariants
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `hasse_invariant(p)` | `p`: `Integer` | `int` | Hasse-Minkowski invariant ±1 at p | `[ND, FIELD]` |
| `hasse_invariant__OMeara(p)` | `p`: `Integer` | `int` | O'Meara convention Hasse invariant | `[ND, FIELD]` |
| `hasse_conductor()` | — | `Integer` | Product of all primes p where the Hasse invariant is −1 | `[ND, INT]` |
| `clifford_invariant(p)` | `p`: `Integer` | `int` | Clifford algebra class in Brauer group at prime p (takes a prime argument; even dim: class of Clifford algebra; odd dim: class of even Clifford algebra; see Lam GSM 67 p.117) | `[ND, FIELD]` |
| `clifford_conductor()` | — | `Integer` | Product of primes where `clifford_invariant(p) == -1`; for ternary forms equals the discriminant of the quaternion algebra | `[ND, INT]` |
| `CS_genus_symbol_list(force_recomputation=False)` | `force_recomputation`: `bool` | `list` | List of Conway-Sloane genus symbols at all primes dividing 2·det(Q), in increasing order of prime; each entry is a `GenusSymbol_p_adic_ring` object | `[INT, ND]` |
| `anisotropic_primes()` | — | `list` | Primes (incl. −1 for ∞) where form is anisotropic; requires PARI | `[ND, INT, PARI]` |
| `is_anisotropic(p)` | `p`: `Integer` | `bool` | Anisotropic at p | `[ND, FIELD]` |
| `is_isotropic(p)` | `p`: `Integer` | `bool` | Isotropic at p | `[ND, FIELD]` |

### Representation theory
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `__call__(v)` | `v`: `Vector` | `RingElement` | Evaluate Q(v) | |
| `bilinear_map(v, w)` | `v`: `Vector`, `w`: `Vector` | `RingElement` | Associated bilinear form B(v,w) = (Q(v+w)−Q(v)−Q(w))/2 | |
| `is_locally_represented(m, p)` | `m`: `Integer`, `p`: `Integer` | `bool` | Q(x)≡m solvable over ℤ_p | `[INT]` |
| `is_locally_universal(p)` | `p`: `Integer` | `bool` | Represents all ℤ locally at p | `[INT]` |
| `local_density(p, m)` | `p`: `Integer`, `m`: `Integer` | `Rational` | Local density α_p(Q, m) | `[INT, PD for convergence]` |
| `local_primitive_density(p, m)` | `p`: `Integer`, `m`: `Integer` | `Rational` | Primitive local density | `[INT]` |
| `local_representation_conditions(recompute_flag=False, silent_flag=False)` | `recompute_flag`: `bool`, `silent_flag`: `bool` | `QuadraticFormLocalRepresentationConditions` | Returns a `QuadraticFormLocalRepresentationConditions` object summarizing the local (p-adic) representability of all integers; `recompute_flag=True` forces recomputation of the cache | `[INT]` |
| `is_locally_represented_number(m, recompute_flag=False)` | `m`: `Integer`, `recompute_flag`: `bool` | `bool` | Whether m is locally represented (i.e., by `local_representation_conditions()`) | `[INT]` |
| `is_locally_universal_at_all_primes()` | — | `bool` | Locally represents all of ℤ_p for all finite primes | `[INT]` |
| `is_locally_universal_at_all_places()` | — | `bool` | Locally represents all integers and is positive definite (universal at ∞ too) | `[INT, PD]` |
| `is_globally_represented(m)` | `m`: `Integer` | `bool` | Q(x) = m solvable over ℤ | `[INT]` |
| `solve(m)` | `m`: `RingElement` | `Vector` or `None` | Find x with Q(x) = m | `[RAT, PARI]` |
| `basiclemma(M)` | `M`: `Integer` | `Integer` | Finds an integer represented by Q that is coprime to M; used in local normal form computation | `[INT]` |
| `basiclemmavec(M)` | `M`: `Integer` | `Vector` | Finds a vector v such that Q(v) is coprime to M; companion to `basiclemma` | `[INT]` |
| `short_vector_list_up_to_length(n, up_to_sign)` | `n`: `Integer`, `up_to_sign`: `bool` | `list` | Vectors with Q(x) ≤ n | `[PD, INT, PARI]` |
| `short_primitive_vector_list_up_to_length(n)` | `n`: `Integer` | `list` | Primitive vectors with Q(x) ≤ n | `[PD, INT]` |
| `basis_of_short_vectors(show_lengths=False)` | `show_lengths`: `bool` | `tuple` | Basis for ℤ^n of minimal-length vectors; uses PARI qfminim; returns tuple of vectors (and optionally lengths) | `[PD, INT, PARI]` |
| `vectors_by_length(b)` | `b`: `Integer` | `dict` | Dict grouping vectors by norm 0..b | `[PD, INT]` |
| `minimum(proof)` | `proof`: `bool` | `Integer` | Minimum nonzero value Q(x) | `[PD, INT]` |
| `maximum(b)` | `b`: `Integer` | `Integer` | Maximum Q(x) for x with Q(x)≤b | `[PD, INT]` |
| `count_congruence_solutions(B, n, m, p, k)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer` | `Integer` | Count Q(x)≡m (mod p^k) | `[INT]` |
| `count_congruence_solutions__bad_type(B, n, m, p, k, NZvec, Zvec, p2)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer`, `NZvec`: `list`, `Zvec`: `list`, `p2`: `Integer` | `Integer` | Conway-Sloane local counting helper: bad-type contribution in p-adic density decomposition | `[INT]` |
| `count_congruence_solutions__bad_type_I(B, n, m, p, k, NZvec, Zvec, p2)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer`, `NZvec`: `list`, `Zvec`: `list`, `p2`: `Integer` | `Integer` | Type-I bad-part contribution for local density counts | `[INT]` |
| `count_congruence_solutions__bad_type_II(B, n, m, p, k, NZvec, Zvec, p2)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer`, `NZvec`: `list`, `Zvec`: `list`, `p2`: `Integer` | `Integer` | Type-II bad-part contribution for local density counts | `[INT]` |
| `count_congruence_solutions__good_type(B, n, m, p, k, NZvec, Zvec, p2)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer`, `NZvec`: `list`, `Zvec`: `list`, `p2`: `Integer` | `Integer` | Good-type contribution in local counting decomposition | `[INT]` |
| `count_congruence_solutions__zero_type(B, n, m, p, k, NZvec, Zvec, p2)` | `B`: `Integer`, `n`: `Integer`, `m`: `Integer`, `p`: `Integer`, `k`: `Integer`, `NZvec`: `list`, `Zvec`: `list`, `p2`: `Integer` | `Integer` | Zero-type contribution in local counting decomposition | `[INT]` |

### Automorphisms
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `automorphisms()` | — | `list` | List of automorphism matrices | `[INT, PD, PARI]` |
| `automorphism_group()` | — | `MatrixGroup` | Automorphism group | `[INT, PD, PARI]` |
| `number_of_automorphisms()` | — | `Integer` | \|Aut(Q)\| | `[INT, PD, PARI]` |

### Analytic / modular
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `theta_series(prec)` | `prec`: `Integer` | `PowerSeries` | Formal power series Σ r(n) q^n | `[PD, INT]` |
| `theta_series_degree_2(prec)` | `prec`: `Integer` | `SiegelThetaSeries` | Siegel modular form | `[PD, INT]` |
| `mass(M=None)` | `M`: `QuadraticForm` or `None` | `Rational` | Total mass of genus = Σ 1/\|Aut(Q')\| over genus representatives; uses GHY formula | `[PD?, INT]` |
| `conway_mass()` | — | `Rational` | Conway-Sloane mass formula implementation for integral forms | `[INT, PD]` |
| `conway_standard_mass()` | — | `Rational` | Conway-Sloane standard mass term | `[INT, PD]` |
| `conway_p_mass(p)` | `p`: `Integer` | `Rational` | Conway local p-mass factor | `[INT, PD]` |
| `conway_standard_p_mass(p)` | `p`: `Integer` | `Rational` | Standardized local p-mass contribution in Conway mass formula | `[INT, PD]` |
| `conway_type_factor(p)` | `p`: `Integer` | `Rational` | Type factor in Conway-Sloane local mass expression | `[INT, PD]` |
| `conway_diagonal_factor(p)` | `p`: `Integer` | `Rational` | Diagonal factor in Conway local mass term | `[INT, PD]` |
| `conway_cross_product_doubled_power(p)` | `p`: `Integer` | `Integer` | Cross-product doubled-power exponent term in Conway local mass | `[INT, PD]` |
| `conway_species_list_at_2()` | — | `list` | 2-adic species data used in Conway local mass calculations | `[INT, PD]` |
| `conway_species_list_at_odd_prime(p)` | `p`: `Integer` | `list` | Odd-prime species data used in Conway local mass calculations | `[INT, PD]` |
| `conway_octane_of_this_unimodular_Jordan_block_at_2(block)` | `block`: `list` | `Integer` | Octane invariant for a 2-adic unimodular Jordan block in Conway notation | `[INT, PD]` |
| `GHY_mass__maximal()` | — | `Rational` | Mass via GHY formula for maximal lattices; valid over any number field; returns a rational number | `[PD, INT]` |
| `Kitaoka_mass_at_2()` | — | `Rational` | Local mass factor at p=2 per Kitaoka Thrm 5.6.3; returns a rational > 0; **docstring warns verification needed** | `[INT, PD]` |
| `Watson_mass_at_2()` | — | `Rational` | Local mass factor at p=2 per Watson 1976; requires `sage.symbolic`; returns a rational number | `[INT, PD]` |
| `Pall_mass_density_at_odd_prime(p)` | `p`: `Integer` | `Rational` | Self-representation local density at odd prime p per Pall (1965); p must be an odd prime; returns a rational number | `[INT, PD]` |
| `local_mass_factor(p)` | `p`: `Integer` | `Rational` | Combined local mass factor at prime p | `[INT]` |
| `p_neighbor(p, y)` | `p`: `Integer`, `y`: `Vector` | `QuadraticForm` | p-neighbor lattice (for genus traversal) | `[INT, ND]` |
| `cholesky_decomposition(bit_prec=53)` | `bit_prec`: `Integer` | `tuple` | Upper-triangular real Cholesky of precision bit_prec; Q must be over ℤ, ℚ, or a real field with at least bit_prec precision | `[PD, FIELD]` |

### Arithmetic / module structure
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `direct_sum(other)` | `other`: `QuadraticForm` | `QuadraticForm` | Orthogonal sum | |
| `tensor_product(other)` | `other`: `QuadraticForm` | `QuadraticForm` | Tensor product | |
| `extract_variables(indices)` | `indices`: `list` | `QuadraticForm` | Restriction to subset of variables | |
| `complementary_subform(indices)` | `indices`: `list` | `QuadraticForm` | Orthogonal complement subform (by variable index list) | |
| `complementary_subform_to_vector(v)` | `v`: `Vector` | `QuadraticForm` | Finds the (n-1)-dimensional quadratic form whose variables are orthogonal to the given vector v; extends v to a unimodular matrix for a cleaner split than the C++ version | `[INT]` |
| `adjoint()` | — | `QuadraticForm` | Integral form with matrix = adj(Q.matrix()); = QuadraticForm with Hessian = classical adjoint of self's Hessian | `[INT, ND]` |
| `adjoint_primitive()` | — | `QuadraticForm` | Primitive adjoint: smallest-discriminant integral form whose matrix is a scalar multiple of Q.matrix()⁻¹; formerly and incorrectly called `primitive_adjoint()` | `[INT, ND]` |
| `antiadjoint()` | — | `QuadraticForm` | Integral form P such that P.adjoint() == self; raises `ValueError: not an adjoint` if self is not an adjoint of any integral form | `[INT, ND]` |
| `is_adjoint()` | — | `bool` | True if `self` is the adjoint of some other integral form | `[INT, ND]` |
| `reciprocal_form()` | — | `QuadraticForm` | Q' with Gram = Q.Gram^{-1} (up to scalar) | `[INT, ND]` |
| `add_symmetric(c, i, j, in_place=False)` | `c`: `RingElement`, `i`: `Integer`, `j`: `Integer`, `in_place`: `bool` | `QuadraticForm` | Performs the substitution **x_j → x_j + c·x_i** (equivalently, symmetrically adds c times the j-th row/col to the i-th row/col); used internally by `local_normal_form()`; returns new form unless `in_place=True` | `[RING]` |
| `divide_variable(c, i, in_place=False)` | `c`: `RingElement`, `i`: `Integer`, `in_place`: `bool` | `QuadraticForm` or `None` | Substitute x_i → x_i/c, scaling row/col i by 1/c; requires c⁻¹ to exist in base ring; returns new form or None if `in_place=True` | `[RING]` |
| `elementary_substitution(c, i, j, in_place=False)` | `c`: `RingElement`, `i`: `Integer`, `j`: `Integer`, `in_place`: `bool` | `QuadraticForm` | Performs substitution **x_i → x_i + c·x_j** (opposite direction from `add_symmetric`); returns new form unless `in_place=True`. `add_symmetric` is the lower-level building block used in `local_normal_form()` | `[RING]` |
| `split_local_cover(p=None)` | `p`: `Integer` or `None` | `QuadraticForm` | *(internal)* Find a local cover that splits off a hyperbolic plane at prime p; used internally in genus and representation computations | `[INT, ND]` |

---

## 6. `BinaryQF` Methods
`[INT]`; `[INDEF ok]` unless noted; discriminant D = b²−4ac.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `discriminant()` | — | `Integer` | D = b²−4ac | |
| `determinant()` / `det()` | — | `Rational` | det of Gram matrix = −D/4; returned as rational even when D even | |
| `content()` | — | `Integer` | gcd(a, b, c) | |
| `polynomial()` | — | `Polynomial` | Polynomial representation ax²+bxy+cy² | |
| `is_positive_definite()` / `is_posdef()` | — | `bool` | D < 0, a > 0 | `[PD]` |
| `is_negative_definite()` / `is_negdef()` | — | `bool` | D < 0, a < 0 | |
| `is_indefinite()` / `is_indef()` | — | `bool` | D > 0 | `[INDEF]` |
| `is_singular()` | — | `bool` | D = 0 | `[DEG]` |
| `is_nonsingular()` | — | `bool` | D ≠ 0 | |
| `is_zero()` | — | `bool` | All coefficients zero | |
| `is_primitive()` | — | `bool` | gcd(a, b, c) = 1 | |
| `has_fundamental_discriminant()` | — | `bool` | D is a fundamental discriminant | |
| `is_reduced()` | — | `bool` | Reduced in classical sense (`\|b\| ≤ a ≤ c` for PD; between-roots criterion for INDEF) | `[PD standard; INDEF see docs]` |
| `is_weakly_reduced()` | — | `bool` | \|b\| ≤ a ≤ c | |
| `is_reducible()` | — | `bool` | Whether the indefinite form is reducible (has a square discriminant) | `[INDEF]` |
| `is_equivalent(other, proper=True)` | `other`: `BinaryQF`, `proper`: `bool` (keyword, default `True`) | `bool` | Proper or improper equivalence; `proper=True` for proper, `proper=False` for improper (includes orientation-reversing isometries) | `[PARI]` |
| `reduced_form(transformation=False, algorithm='default')` | `transformation`: `bool` (keyword), `algorithm`: `str` (keyword) | `BinaryQF` or `tuple<BinaryQF, Matrix>` | Equivalent reduced form; `transformation=True` also returns the GL_2(ℤ) matrix M s.t. `self.matrix_action_right(M) == reduced_form`; `algorithm` can be `'pari'` or `'sage'` | `[PARI default]` |
| `reduction_sequence()` | — | `list<BinaryQF>` | Sequence of Gauss reductions | |
| `cycle(proper=False)` | `proper`: `bool` (keyword, default `False`) | `list<BinaryQF>` | For reduced indefinite forms: list of all forms in the cycle (or proper cycle if `proper=True`) | `[INDEF]` |
| `represents(n)` | `n`: `Integer` | `bool` | Q(x,y) = n solvable | |
| `represented_primitively(n)` | `n`: `Integer` | `bool` | Primitively represents n | |
| `solve_integer(n)` | `n`: `Integer` | `tuple<Integer, Integer>` | Find integers (x,y) with Q(x,y) = n, or raise ValueError | `[PARI]` |
| `small_prime_value()` | — | `Integer` | A small prime represented by Q | `[PD]` |
| `class_number()` | — | `Integer` | Class number of discriminant D | `[PD, PARI]` |
| `form_class()` | — | `BinaryQFClassGroupElement` | Element of BQFClassGroup(D) representing the equivalence class of this form | |
| `complex_point()` | — | `Complex` | Fixed point in upper half-plane; root of ax²+bx+c with positive imaginary part | `[PD, PARI]` |
| `matrix_action_left(M)` | `M`: `Matrix<Integer>` (2×2) | `BinaryQF` | New form obtained by left action of matrix M | |
| `matrix_action_right(M)` | `M`: `Matrix<Integer>` (2×2) | `BinaryQF` | New form obtained by right action of matrix M | |
| `static from_polynomial(f)` | `f`: bivariate `Polynomial` | `BinaryQF` | Constructor from bivariate polynomial | |
| `static principal(D)` | `D`: `Integer` (discriminant) | `BinaryQF` | Principal (identity) form of discriminant D | |
| `BinaryQF_reduced_representatives(D, primitive_only, proper)` | `D`: `Integer`, `primitive_only`: `bool`, `proper`: `bool` | `list<BinaryQF>` | All reduced representatives for classes of discriminant D; `primitive_only=True` omits imprimitive forms | |

---

## 7. `TernaryQF` Methods
`[INT]`; form stored as `(a,b,c,r,s,t)` representing ax²+by²+cz²+ryz+sxz+txy.

### Intrinsic data
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `coefficients()` | — | `tuple<Integer>` | Returns the tuple `(a,b,c,r,s,t)` of all six coefficients | |
| `coefficient(n)` | `n`: `Integer` (0-indexed, 0≤n≤5) | `Integer` | Returns the n-th coefficient | |
| `polynomial(names='x,y,z')` | `names`: `str` (keyword) | `Polynomial` | Polynomial ax²+by²+cz²+ryz+sxz+txy in given variable names | |
| `matrix()` | — | `Matrix<Integer>` (3×3) | Hessian matrix: diagonal `2a,2b,2c` and off-diag `t,s,r`; Q(v) = (1/2)v·M·vᵀ | |
| `disc()` | — | `Integer` | Discriminant = det(Hessian)/2 | |
| `content()` | — | `Integer` | gcd(a,b,c,r,s,t) | |
| `is_primitive()` | — | `bool` | content = 1 | |
| `primitive()` | — | `TernaryQF` | Primitive version Q/content | |

### Invariants
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `divisor()` | — | `Integer` | Content of the adjoint form | |
| `omega()` | — | `Integer` | Content of the adjoint of the primitive form; = Q.primitive().adjoint().content() | |
| `delta()` | — | `Integer` | omega() of the adjoint; same as omega() of the reciprocal form | |
| `level()` | — | `Integer` | 4·disc()/divisor() | |
| `adjoint()` | — | `TernaryQF` | Adjoint ternary form; Hessian = 2·classical adjoint of self.matrix() | |
| `reciprocal()` | — | `TernaryQF` | Reciprocal form; multiple of primitive adjoint with same content as self | |

### Definiteness
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `is_positive_definite()` | — | `bool` | All eigenvalues > 0 | `[PD]` |
| `is_negative_definite()` | — | `bool` | All eigenvalues < 0 | |
| `is_definite()` | — | `bool` | Positive or negative definite | |

### Reduction and equivalence
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `is_eisenstein_reduced()` | — | `bool` | True if form satisfies all eight Eisenstein reduction conditions | |
| `reduced_form_eisenstein()` | — | `tuple<TernaryQF, Matrix<Integer>>` | Returns `(Qr, M)` where Qr is the Eisenstein-reduced equivalent form and M is the transformation matrix; Q(M) == Qr | `[PD, PARI]` |
| `is_equivalent(other)` | `other`: `TernaryQF` | `bool` | GL_3(ℤ)-equivalence check | `[PD, PARI]` |

### Automorphisms
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `automorphisms(slow=True)` | `slow`: `bool` (keyword, default `True`) | `list<Matrix<Integer>>` | List of all GL_3(ℤ) automorphism matrices; `slow=True` uses PARI, `slow=False` uses internal algorithm | `[PD, PARI]` |
| `number_of_automorphisms(slow=True)` | `slow`: `bool` (keyword, default `True`) | `Integer` | \|Aut(Q)\| | `[PD, PARI]` |
| `automorphism_spin_norm(A)` | `A`: `Matrix<Integer>` (3×3, automorphism) | `Integer` (±1) | Spinor norm of the automorphism A ∈ GL_3(ℤ); used in spinor genus computations | `[INT, ND]` |
| `automorphism_symmetries(A)` | `A`: `Matrix<Integer>` (automorphism) | `list<Vector>` | For automorphism A: if identity returns []; otherwise returns [v1,v2] such that symmetry(v1)·symmetry(v2) = A | |
| `symmetry(v)` | `v`: `Vector` | `Matrix<Integer>` | Orthogonal reflection in the hyperplane perpendicular to vector v w.r.t. the quadratic form | |

### Representation and genus
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `basic_lemma(p)` | `p`: prime `Integer` | `Integer` | Find a value represented by Q and coprime to prime p | |
| `find_zeros_mod_p(p)` | `p`: prime `Integer` (p ∤ disc(Q)) | `list<Vector>` | All zeros of Q mod prime p | `[PD, PARI for p>2]` |
| `pseudorandom_primitive_zero_mod_p(p)` | `p`: odd prime `Integer` (p ∤ disc(Q)) | `Vector` | A random primitive zero v=(a,b,1) of Q mod odd prime p | `[PD, PARI]` |
| `find_p_neighbor_from_vec(p, v, mat=False)` | `p`: prime `Integer`, `v`: `Vector`, `mat`: `bool` (keyword) | `TernaryQF` or `tuple<TernaryQF, Matrix>` | p-neighbor of Q at vector v (Q(v)≡0 mod p, v non-singular mod p); returns the reduced equivalent, optionally with transformation matrix | `[PD, PARI]` |
| `find_p_neighbors(p, mat=False)` | `p`: prime `Integer`, `mat`: `bool` (keyword) | `list<TernaryQF>` | All p-neighbors (list); uses all zeros mod p from `find_zeros_mod_p` | `[PD, PARI]` |

### Analytic
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `theta_series(prec)` | `prec`: `Integer` | `PowerSeries` | Formal theta series Σ r(n) q^n | `[PD]` |

### Conversion
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `quadratic_form()` | — | `QuadraticForm` | Returns equivalent `QuadraticForm(ZZ, 3, ...)` | |
| `scale_by_factor(c)` | `c`: scalar | `TernaryQF` | Multiply all coefficients by scalar c; returns new TernaryQF | |

---

## 8. `TorsionQuadraticModule` Methods
`[INT]`; bilinear form is ND; quadratic form may be degenerate.

### Underlying data
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `V()` | — | `FreeQuadraticModule` | Ambient free quadratic module V (the numerator) | |
| `W()` | — | `FreeQuadraticModule` | Submodule W (the denominator); T = V/W | |
| `gens()` | — | `tuple` | Generators of T as a ℤ-module; no minimality guarantee | |
| `order()` | — | `Integer` | Group order \|D\| = \|det(V)\|/\|det(W)\|; inherited from the abelian group parent | |
| `invariants()` | — | `tuple<Integer>` | Invariants of the underlying abelian group, e.g. `(2, 6)` for ℤ/2⊕ℤ/6 | |
| `gram_matrix_bilinear()` | — | `Matrix<Rational>` | Gram matrix of the bilinear form w.r.t. `gens()`; entries in ℚ/mℤ where m = (V,W) | |
| `gram_matrix_quadratic()` | — | `Matrix<Rational>` | Gram matrix of the quadratic form w.r.t. `gens()`; off-diag = bilinear, diag = quadratic values | |
| `value_module()` | — | `QmodnZ` | Codomain ℚ/mℤ of the bilinear form, where m = (V,W) | |
| `value_module_qf()` | — | `QmodnZ` | Codomain ℚ/nℤ of the quadratic form; n = 2m or smaller when all (w,w) ∈ 2ℤ | |

### Element methods
Elements `x` of a `TorsionQuadraticModule` carry the induced forms directly:

| Method on element x | Argument Types | Return Type | Description |
|---------------------|----------------|-------------|-------------|
| `x.b(y)` / `x.inner_product(y)` | `y`: element of T | `Rational (mod mℤ)` | Bilinear form value b(x,y) ∈ ℚ/mℤ |
| `x.q()` / `x.quadratic_product()` | — | `Rational (mod nℤ)` | Quadratic form value q(x) ∈ ℚ/nℤ |

### Structural operations
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `direct_sum(other)` | `other`: `TorsionQuadraticModule` | `TorsionQuadraticModule` | Direct orthogonal sum of two TorsionQuadraticModules | |
| `twist(c)` | `c`: `Integer` | `TorsionQuadraticModule` | Rescale both bilinear and quadratic form by integer c; value modules scale accordingly | |
| `submodule(gens)` | `gens`: list of elements | `TorsionQuadraticModule` | Sub-TQM spanned by the given generators | |
| `submodule_with_gens(gens)` | `gens`: list of elements | `TorsionQuadraticModule` | Sub-TQM with an explicitly supplied (possibly redundant) generator list; useful when you need a specific Gram matrix presentation | |
| `orthogonal_submodule_to(S)` | `S`: submodule or element list | `TorsionQuadraticModule` | Sub-TQM of all elements orthogonal to submodule S; satisfies `T.orthogonal_submodule_to(S).V() + S.V() == T.V()` | |
| `quotient(W)` | `W`: submodule | `TorsionQuadraticModule` | Quotient torsion module T/W (inherited from FGP_Module) | |
| `primary_part(s)` | `s`: `Integer` | `TorsionQuadraticModule` | s-primary submodule (elements annihilated by a power of s) | |
| `all_submodules()` | — | `list<TorsionQuadraticModule>` | List of all submodules; exponential in rank — use only for small groups | |

### Classification and genus
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `normal_form(partial=False)` | `partial`: `bool` (keyword, default `False`) | `TorsionQuadraticModule` | Miranda-Morrison canonical normal form; `partial=True` returns a partial (non-unique) normal form that still exposes p-adic invariants | `[ND]` |
| `is_genus(sig, even=True)` | `sig`: `tuple(Integer, Integer)`, `even`: `bool` (keyword, default `True`) | `bool` | Boolean existence test for a lattice with this discriminant form and signature pair `sig=(s_+, s_-)`; `even` is boolean (default `True`), and upstream marks the odd-lattice branch (`even=False`) as incomplete | |
| `genus(sig)` | `sig`: `tuple(Integer, Integer)` | `Genus` | `Genus` object compatible with this discriminant form and signature `sig`; raises `ValueError` if none exists. Upstream examples include odd-lattice genus construction via this method | |
| `brown_invariant()` | — | `IntegerMod(8)` | Brown invariant Br(D,q) ∈ ℤ/8ℤ; requires quadratic form valued in ℚ/2ℤ (even lattice case); additive over direct sums | |

### Symmetry
| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `orthogonal_group(gens=None)` | `gens`: list of generator matrices (optional) | `MatrixGroup` | Isometry group of T preserving both the bilinear and quadratic forms; if `gens` is given (e.g. from `IntegralLattice.orthogonal_group()`), restricts to those generators; used to compute the image of Aut(L) in Aut(discriminant group) | |

---

## 9. `Genus` Methods
`[INT, ND]`; allows `[INDEF]`.

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `Genus(A)` | `A`: `Matrix<Integer>` (symmetric) | `Genus` | *(standalone constructor)* Create genus from symmetric integer Gram matrix A | |
| `LocalGenusSymbol(A, p)` | `A`: `Matrix<Integer>`, `p`: prime `Integer` | `Genus_Symbol_p_adic_ring` | *(standalone constructor)* Local genus symbol at prime p | |
| `signature()` | — | `Integer` | p − n | |
| `signature_pair()` | — | `tuple<Integer, Integer>` | (p, n); aliases: `signature_pair_of_matrix()` | |
| `dimension()` | — | `Integer` | Rank; aliases: `rank()`, `dim()` | |
| `determinant()` | — | `Integer` | det(Gram) of any representative; docs mention "Hessian determinant" but example confirms it equals det(Gram) passed to constructor; aliases: `det()`; **no** `discriminant()` method on `Genus` | |
| `discriminant_form()` | — | `TorsionQuadraticModule` | Discriminant form as `TorsionQuadraticModule` | |
| `direct_sum(other)` | `other`: `Genus` | `Genus` | Genus of direct sum of representatives | |
| `level()` | — | `Integer` | Level = denominator of inverse Gram matrix of a representative | |
| `scale()` | — | `Integer` | Scale ideal = b(L,L) ⊆ ℤ (as integer) | |
| `norm()` | — | `Integer` | Norm = gcd{(x,x) : x ∈ L} (as integer); for even lattice = scale | |
| `is_even()` | — | `bool` | All (x,x) ∈ 2ℤ | |
| `is_unimodular()` | — | `bool` | det(Gram) = ±1 | |
| `local_symbol(p)` | `p`: prime `Integer` | `Genus_Symbol_p_adic_ring` | `Genus_Symbol_p_adic_ring` object at prime p | |
| `local_symbols()` | — | `list<Genus_Symbol_p_adic_ring>` | List of all local genus symbols (at all relevant primes) | |
| `representative()` | — | `Matrix<Integer>` | Integer Gram matrix of a representative lattice; works for `[INDEF]` | |
| `rational_representative()` | — | `Matrix<Rational>` | Rational diagonal Gram matrix of a rational representative | |
| `representatives(backend, algorithm)` | `backend`: `str`, `algorithm`: `str` | `list<IntegralLattice>` | All distinct lattices in genus (finite list); backend options include `'sage'`, `'magma'` | `[PD]` |
| `mass(backend='sage')` | `backend`: `str` (keyword, default `'sage'`) | `Rational` | Mass = Σ 1/\|Aut(L)\| over genus; default backend is pure Sage (no PARI/Magma required) | `[PD]` |
| `spinor_generators(proper)` | `proper`: `bool` | `list<Integer>` | List of primes not dividing det(Gram) at which the spinor genus splits the genus; `proper=True` for proper spinor genera; used in genus traversal algorithms | |
| `is_2_adic_genus(quintuple_list)` | `quintuple_list`: list | `bool` | Validity check for 2-adic local symbol | |

---

## 10. Matrix-Level Methods

These operate on integer matrices directly (no lattice wrapper). `M.LLL()` / `M.BKZ()` treat **rows as basis vectors** and return the reduced basis as a new matrix. `M.LLL_gram()` treats M as a Gram matrix and returns the unimodular transformation U such that Uᵀ·M·U is LLL-reduced.

| Method | Description | Tags |
|--------|-------------|------|
| `M.LLL(delta=0.75, eta=0.501, ...)` | LLL-reduce rows; returns new matrix with LLL-reduced rows (= reduced basis, not a transformation matrix) | `[FPLLL]` |
| `M.BKZ(block_size=10, ...)` | BKZ-reduce rows; returns new matrix | `[FPLLL]` |
| `M.LLL_gram(flag=0)` | Given Gram matrix M, returns unimodular U s.t. Uᵀ·M·U is LLL-reduced (flag 0=float rescaling, 1=integral); **correctness guaranteed only for PD; for semidefinite or indefinite inputs the algorithm has no correctness guarantee and may silently return wrong output** | `[PARI, PD only]` |
| `M.smith_form()` | Smith normal form (module structure only, no bilinear form) | |
| `M.hermite_form()` / `M.echelon_form()` | Hermite Normal Form | |
| `M.nrows()` / `M.ncols()` / `M.dimensions()` | Shape information | |
| `M.rref()` / `M.pivots()` / `M.pivot_rows()` | Row-reduction data | |
| `M.rank()` / `M.left_nullity()` / `M.right_nullity()` | Rank and nullities | |
| `M.left_kernel()` / `M.right_kernel()` | Kernel modules | |
| `M.left_kernel_matrix()` / `M.right_kernel_matrix()` / `M.integer_kernel()` | Kernel bases as matrices | |
| `M.charpoly()` / `M.characteristic_polynomial()` / `M.minpoly()` / `M.minimal_polynomial()` | Characteristic/minimal polynomial variants | |
| `M.is_square()` / `M.is_invertible()` / `M.is_unit()` | Basic invertibility predicates | |
| `M.is_symmetric()` / `M.is_hermitian()` / `M.is_diagonal()` | Structure predicates | |
| `M.row_space()` / `M.column_space()` | Row/column span modules | |
| `M.submatrix(...)` / `M.matrix_from_rows(...)` / `M.matrix_from_columns(...)` | Matrix extraction helpers | |
| `M.swap_rows(...)` / `M.swap_columns(...)` / `M.with_swapped_rows(...)` / `M.with_swapped_columns(...)` | Row/column swap operations | |
| `M.add_multiple_of_row(...)` / `M.add_multiple_of_column(...)` / `M.add_to_entry(...)` | Elementary row/column updates | |
| `M.numpy()` / `M.sparse_matrix()` | Conversion helpers | |

---

## 11. Helper / Standalone Functions

### Construction helpers (from `sage.modules.free_quadratic_module_integer_symmetric`)
| Function | Description | Tags |
|----------|-------------|------|
| `IntegralLatticeDirectSum(Ls, return_embeddings=False)` | Orthogonal direct sum of a list of `IntegralLattice` objects; `return_embeddings=True` returns `[L, [φ_i]]` with inclusions | |
| `IntegralLatticeGluing(Ls, glue, return_embeddings=False)` | Overlattice of the direct sum defined by discriminant-group glue vectors; `glue` is a list of lists `[g_1,...,g_n]` where `g_i ∈ discr(L_i)` | |
| `local_modification(M, G, p)` | Replace local structure of `M` at prime `p` so that its genus symbol at p matches that of the lattice with Gram `G`; other completions unchanged | `[INT, ND, PARI]` |

### Quadratic-forms library
| Function | Module | Description | Tags |
|----------|--------|-------------|------|
| `qfsolve(G)` | `sage.quadratic_forms.qfsolve` | Find isotropic vector for rational form; uses PARI `qfsolve` | `[RAT, INDEF, PARI]` |
| `qfparam(G, sol)` | `sage.quadratic_forms.qfsolve` | Parametrize conic G(x)=0; returns triple of polynomials | `[RAT, PARI]` |
| `genera(sig, det, even, max_scale)` | `sage.quadratic_forms.genera.genus` | All genera with given invariants | `[INT]` |
| `collect_small_blocks(...)` | `sage.quadratic_forms.genera.normal_form` | Helper for p-adic/Jordan normal-form block assembly | `[INT]` |
| `count_all_local_good_types_normal_form(...)` | `sage.quadratic_forms.count_local_2` | Enumerate/count local good types in normal-form computations | `[INT]` |
| `Genus_Symbol_p_adic_ring.compartments()` | `sage.quadratic_forms.genera.genus` | Return 2-adic compartments in the genus-symbol representation | `[INT]` |
| `BezoutianQuadraticForm(f, g)` | `sage.quadratic_forms.constructions` | Quadratic form of dim=max(deg f, deg g) whose Gram matrix is the Bézout matrix of f,g; Q(x,y) = (f(x)g(y)−f(y)g(x))/(y−x); requires Singular | `[RING, DEG ok]` |
| `HyperbolicPlane_quadratic_form(R, r=1)` | `sage.quadratic_forms.constructions` | Direct sum of r hyperbolic planes over ring R; each plane has Gram [[0,1],[1,0]]; result is indefinite rank-2r form | `[RING, INDEF]` |
| `quadratic_form_from_invariants(F, rk, det, P, sminus)` | `sage.quadratic_forms.quadratic_form` | Construct a ℚ-form over field F with specified rank, determinant, Hasse prime factor invariants P, and s⁻ signature count; provides a representative of the specified genus | `[FIELD:ℚ or NF, ND]` |

---

## 12. Important Implicit Assumptions by Class

| Class | Non-degenerate | Integer-valued b | Positive definite | Symmetric |
|-------|:-:|:-:|:-:|:-:|
| `FreeQuadraticModule` | ✗ allowed | optional | ✗ allowed | ✗ allowed (not required) |
| `IntegralLattice` | ✓ required | ✓ required | ✗ allowed | ✓ required |
| `IntegerLattice` | ✓ (Gram = B·Bᵀ is PD when full rank) | ✓ (B·Bᵀ ∈ ℤ when B ∈ ℤ^n) | ✓ forced by embedding | ✓ forced |
| `QuadraticForm` | ✗ allowed | optional (ZZ or field) | ✗ allowed | encoded in upper-tri |
| `TorsionQuadraticModule` | bilinear: ✓; qf: ✗ | ✓ (values in ℚ/nℤ) | N/A (finite) | ✓ |
| `BinaryQF` | ✗ allowed | ✓ | ✗ allowed | ✓ |
| `Genus` | ✓ required | ✓ | ✗ allowed | ✓ |
| `GroupOfIsometries` | N/A (group, not module) | N/A | N/A | form it preserves must be symmetric |
| `RootSystem.*_lattice()` | ✓ (Cartan pairing is ND for semisimple types) | ✓ (Cartan pairing ℤ-valued) | ✗ (not PD in general; e.g. affine types degenerate) | ✓ (symmetric form) |
| `NumberFieldFractionalIdeal` | ✓ as ℤ-module | ✓ (as ℤ-module; trace form is ℤ-valued on O_K) | ✓ totally real fields; ✗ mixed signature | ✓ (trace form) — **but inner product NOT stored in .free_module() return** |
| Trace-form `IntegralLattice` | ✓ when K/ℚ is separable | ✓ | ✓ totally real; ✗ mixed signature | ✓ |
| `QuaternionAlgebra.free_module()` | ✓ (reduced norm form is ND) | ✓ (reduced norm is ℤ-valued on maximal orders) | ✗ (indefinite for split algebras) | ✓ |

---

## 13. Pitfalls and Gotchas

- **`IntegralLattice` requires non-degenerate form.** For degenerate forms use `FreeQuadraticModule` directly; many methods will be unavailable.
- **`IntegerLattice` bilinear form is not a free parameter.** It is fixed as the restriction of the ambient Euclidean I_n, so the Gram matrix is always B·Bᵀ (PSD). You cannot represent an indefinite lattice. Algorithms produce new bases for the same lattice using the same induced form — nothing is ignored or bypassed.
- **`lll()` on `IntegralLattice` returns a new `IntegralLattice`**, not a matrix. Contrast with `LLL()` on `IntegerLattice`, which returns a matrix *and* updates `self.reduced_basis` in-place. Both use the lattice's actual bilinear form (PARI vs fplll backends).
- **`orthogonal_group()` / `automorphisms()` on `IntegralLattice`** requires a **definite** lattice (positive or negative definite) for automatic generator computation — indefinite forms raise `NotImplementedError`.
- **`enumerate_short_vectors()` vs `short_vectors()`**: `enumerate_short_vectors()` (new in ≥10.x, Lorenz Panny 2024) is a lazy iterator using the lattice's inner product; **it does not yield vectors in non-decreasing norm order** — vectors with larger norm may appear before vectors with smaller norm. `short_vectors(n)` (older, PARI) returns a complete list of all vectors x with (x,x) ≤ n, unordered, and is `[PD]` only. Do not use `enumerate_short_vectors()` when you need the shortest vector; use `minimum()` or `IntegerLattice.shortest_vector()` for that.
- **`enumerate_close_vectors(target)`** (new in ≥10.x) likewise makes no ordering guarantee: the first element yielded is not the closest vector to `target`. To find the closest vector exactly, use `IntegerLattice.closest_vector(target)` (exact, fplll) or `IntegerLattice.approximate_closest_vector(target)` (approximate, several algorithms).
- **`QuadraticForm` matrix convention.** `matrix()` and `Hessian_matrix()` are **aliases** returning the **Hessian A** where Q(x) = **(1/2) xᵀ A x**; diagonal entries A[i,i] = 2·Q[i,i], off-diagonal A[i,j] = Q[i,j]. `Gram_matrix()` returns the **Gram matrix G = A/2** where Q(x) = xᵀ G x; G[i,i] = Q[i,i], G[i,j] = Q[i,j]/2. `det()` returns det(Hessian) = det(2G); `Gram_det()` and `discriminant()` return det(G). Example: Q = x² + 2xy + 3y² → A = [[2,2],[2,6]], G = [[1,1],[1,3]], det(A)=8, det(G)=2. To reconstruct Q from A: `QuadraticForm(A)`; to reconstruct from G: `QuadraticForm(2*G)`.
- **`discriminant_group()` on `IntegralLattice`** returns `TorsionQuadraticModule` L∨/L with the induced quadratic form. The signature determines even/odd structure.
- **`LLL_gram` on matrices** has no correctness guarantee outside positive definite inputs. The upstream PARI documentation describes the non-PD behavior as "might work in some semidefinite/indefinite cases," which means: the algorithm may return a result, may return an incorrect result without error, or may raise an exception. Do not use `LLL_gram` on indefinite or semidefinite Gram matrices and trust the output.
- **`short_vector_list_up_to_length` on `QuadraticForm`** uses PARI and assumes positive definite; results incorrect for indefinite forms.
- **Signature convention**: `signature_pair()` returns `(p, n)` with p = #positive, n = #negative eigenvalues. `signature()` returns `p − n`.
- **`theta_series`** is only mathematically convergent for `[PD]` forms; both `IntegralLattice.theta_series` and `QuadraticForm.theta_series` assume positive definiteness.
- **`p_neighbor`** requires the lattice to be maximal at p (i.e., `b(L,L) ⊆ ℤ` and maximal); use for genus traversal.
- **`IntegralLatticeGluing` / `maximal_overlattice(p=None)`** require the input lattice to be even when operating at the prime 2 or globally.
- **`QuadraticForm.adjoint_primitive()`** — the correct method name is `adjoint_primitive()`, not `primitive_adjoint()`.
- **`Genus.determinant()`** — returns det(Gram) of the representative lattice (= the determinant of the matrix passed to `Genus(A)`), **not** det(Hessian). Despite the docs using the phrase "Hessian determinant", the example confirms `Genus(diag(1,-2,3,4)).determinant()` = −24 = det(diag(1,-2,3,4)). There is no `Genus.discriminant()` method; when in doubt, use `Genus.representative()` to get the Gram matrix and compute directly.
- **`TorsionQuadraticModule.orthogonal_submodule_to(S)`** — the correct method name is `orthogonal_submodule_to(S)`, **not** `orthogonal_submodule(W)`. The argument is the submodule S whose orthogonal complement you want, not the desired output. The relationship `T.orthogonal_submodule_to(S).V() + S.V() == T.V()` holds.
- **`TorsionQuadraticModule.is_genus(sig, even=True)`** — `sig` is a pair of nonnegative integers `(s_plus, s_minus)` and `even` is a boolean (default `True`). Upstream docs still include TODO `implement the same for odd lattices`, so treat `even=False` as incomplete. Odd-lattice genus construction is documented separately for `TorsionQuadraticModule.genus(sig)`.
- **`TorsionQuadraticModule.orthogonal_group(gens=None)`** — a key workflow pattern: given `O = L.orthogonal_group()`, compute `D.orthogonal_group(O.gens())` to get the image of Aut(L) in Aut(discriminant group). The kernel of `O → D.orthogonal_group(O.gens())` is the subgroup of automorphisms acting trivially on the discriminant form.
- **`BinaryQF.determinant()` ≠ `BinaryQF.discriminant()`** — `discriminant()` returns D = b²−4ac; `determinant()` / `det()` returns det of Gram = −D/4 (rational). Example: x²−xy+67y² → D = −267, determinant = 267/4. The method is `has_fundamental_discriminant()`, not `is_fundamental_discriminant()`. The method for a small prime is `small_prime_value()` (no argument), not `small_prime_values(n)`.
- **`FreeQuadraticModule.discriminant()` ≠ `IntegralLattice.discriminant()`** — on `FreeQuadraticModule_generic`, `discriminant()` is (−1)^r · det(gram_matrix()) where r = rank//2 for even rank or (rank−1)//2 for odd rank. On `IntegralLattice` (which inherits from the module hierarchy but overrides the method), `discriminant()` simply returns det(gram_matrix()) with no sign correction. Do not conflate the two.
- **`FreeQuadraticModule.inner_product_matrix()` is the ambient matrix, not the Gram matrix.** For a submodule M of ambient A, `M.inner_product_matrix()` returns the *ambient* A's matrix (same as `A.inner_product_matrix()`). The Gram matrix of M w.r.t. M's own basis is `M.gram_matrix()` = `M.basis_matrix() · M.inner_product_matrix() · M.basis_matrix().T`. Confusing these two is a common source of incorrect Gram computations.
- **`GroupOfIsometries` acts from the right.** Elements are applied as `x ↦ x·g`, not `x ↦ g·x` (GAP convention). In particular, `g * h` means "first g, then h" in the left-to-right action order — the *opposite* of the usual function-composition convention. This reversal propagates to the `GroupActionOnSubmodule` and `GroupActionOnQuotientModule` helpers.
- **`IntegralLattice.orthogonal_group()` requires a **definite** lattice; `GroupOfIsometries` does not.** The former is a high-level lattice method that computes Aut(L) automatically (needs `sage.libs.gap` and the lattice to be definite — positive or negative definite; indefinite raises `NotImplementedError`). The lower-level `GroupOfIsometries(degree, ZZ, gens, bil)` accepts any generators and any symmetric bilinear form, including indefinite ones — but you must supply the generators yourself; it does not compute them.
- **Root-lattice `.scalar()` is the Cartan pairing, not the Euclidean inner product.** `alpha.scalar(alphacheck)` computes the Cartan matrix entry ⟨α, α∨⟩, which is always a rational number and involves the coroot. It is not symmetric in its two arguments in general. The Euclidean inner product (α,β) is only available in the `ambient_space()` / `ambient_lattice()` realizations via `alpha.inner_product(beta)`.
- **`RootSystem` lattices vs `IntegralLattice` with Cartan string.** `RootSystem(['A',4]).root_lattice()` is a combinatorial ℤ-module in `sage.combinat`; it has `simple_roots()`, `positive_roots()`, Weyl-group action etc., but no `gram_matrix()`, no `discriminant_group()`, and no `lll()`. `IntegralLattice("A4")` is an `IntegralLattice` in `sage.modules`; it has the full lattice-theory API but loses the root-system combinatorics. The two are not directly interoperable — you cannot call `IntegralLattice.gens()` to recover labelled simple roots.
- **Number-field trace form Gram matrix is exact; Minkowski Gram is approximate.** `matrix(QQ, n, n, lambda i,j: (B[i]*B[j]).trace())` is exact and works for all number fields. `M.T * M` where `M = K.minkowski_embedding()` is a floating-point approximation over RDF; for the lattice-theory methods of `IntegralLattice` you need an exact integer or rational Gram matrix — round the Minkowski approximation to ℤ (only valid when the lattice is known to be integral and when precision is sufficient) or use the trace form instead.
- Archived out-of-scope toric/fan/polytope caveats are maintained in:
  `docs/archive/scope_violations/sage/lattice/sagemath_lattice_reference_toric_sections_2026-02-18.md`.
- **`K.minkowski_embedding()` vs `K.Minkowski_embedding()`.** The lowercase form `minkowski_embedding` is the canonical name in current Sage (≥6.x). The capitalised alias `Minkowski_embedding` still exists but is deprecated; use `minkowski_embedding`. The optional first argument `B` is a list of n elements whose images form the columns of the output matrix; omit it to use the power basis {1, α, …, α^{n-1}}. The `prec` keyword controls output precision: `prec=None` gives 53-bit RDF, `prec=200` gives RealField(200). Output is always approximate floating-point — use the trace form (§17.2) for exact Gram matrices.
- **`NumberFieldFractionalIdeal.free_module()` has no inner product.** Number field ideals ARE free ℤ-modules of rank n and their ℤ-basis is natively available via `.basis()` and `.integral_basis()`. However, `.free_module()` returns a bare `FreeModule(ZZ, n)` — not a `FreeQuadraticModule` — so it has no `gram_matrix()` and no `inner_product_matrix()`. The metric must be supplied separately. This is in contrast to `QuaternionFractionalIdeal`, which has `gram_matrix()` (the reduced norm) natively.

---

## 14. `FreeQuadraticModule` Class Hierarchy and Full Method List
`sage.modules.free_quadratic_module`

### 14.1 Class hierarchy

```
FreeQuadraticModule_generic                  # base for all free quadratic modules
    FreeQuadraticModule_generic_pid          # over a PID (incl. ZZ)
        FreeQuadraticModule_generic_field    # over a field (QQ, GF(p), ...)
    FreeQuadraticModule_ambient              # ambient (standard basis) free module
        FreeQuadraticModule_ambient_domain   # ambient over integral domain
            FreeQuadraticModule_ambient_pid  # ambient over PID
                FreeQuadraticModule_ambient_field  # ambient vector space over field
    FreeQuadraticModule_submodule_with_basis_pid       # R-submodule of K^n with explicit basis
        FreeQuadraticModule_submodule_field            # K-subspace with explicit basis
```

**Constructor:** `FreeQuadraticModule(base_ring, rank, inner_product_matrix, sparse=False, inner_product_ring=None)`.

Memoised: calling it twice with the same arguments returns the **same** object.

`FreeModule(R, n, inner_product_matrix=G)` is an alias route and returns the same type.

### 14.2 Ring/field split

The critical behavioral difference is between the PID and field branches:

| Class | `span(gens)` semantics | `submodule` vs `subspace` |
|-------|----------------------|--------------------------|
| `_generic_pid` | Returns the *R*-span as an *R*-submodule (may not lie in `self`) | `submodule_with_basis`, `span`, `span_of_basis` |
| `_generic_field` | Returns the *K*-span as a *K*-subspace; echelonises the basis | `subspace`, `subspace_with_basis`, `span`, `span_of_basis` |

### 14.3 Methods on `FreeQuadraticModule_generic` (all subclasses inherit)

| Method | Description | Notes |
|--------|-------------|-------|
| `inner_product_matrix()` | The *n×n* matrix A stored at the ambient-space level; **not required to be symmetric**; defines the pairing `(u,v) = u·A·vᵀ` | Submodules inherit A from ambient |
| `gram_matrix()` | B·A·Bᵀ where A = `inner_product_matrix()` and B = `basis_matrix()`; **this is the Gram matrix w.r.t. the current basis** | Differs from `inner_product_matrix()` for submodules |
| `determinant()` | det(`gram_matrix()`); i.e. det(B·A·Bᵀ) | |
| `discriminant()` | (−1)^r · det(`gram_matrix()`) where r = rank/2 (rank even) or (rank−1)/2 (rank odd); matches the classical sign convention for quadratic forms | **Different from `IntegralLattice.discriminant()`** which is simply det(Gram) |
| `ambient_module()` | The ambient free module (top of the containment hierarchy) | |

### 14.4 Methods added by `FreeQuadraticModule_generic_pid`

| Method | Description |
|--------|-------------|
| `span(gens, check=True, already_echelonized=False)` | R-span of `gens`; returns a submodule of the ambient module (not necessarily of `self`) |
| `span_of_basis(basis, ...)` | Submodule with the given basis (vectors must be linearly independent) |

### 14.5 Methods added by `FreeQuadraticModule_generic_field`

| Method | Description |
|--------|-------------|
| `span(gens, check=True, already_echelonized=False)` | K-span of `gens`; returns subspace of ambient; basis automatically echelonised |
| `span_of_basis(basis, check=True, already_echelonized=False)` | Subspace with explicit basis; raises `ValueError` if not linearly independent |

### 14.6 Methods added by `FreeQuadraticModule_ambient_domain`

| Method | Description |
|--------|-------------|
| `ambient_vector_space()` | Ambient space tensored with the fraction field; e.g. `ZZ^3` → `QQ^3` with same inner product |

### 14.7 Key asymmetry note

The `inner_product_matrix()` is stored at the ambient level and need not be symmetric. The *symmetric* case is the common use case (and is required by `IntegralLattice`), but `FreeQuadraticModule` documents asymmetric matrices explicitly:

```python
N = FreeModule(ZZ, 2, inner_product_matrix=[[1,-1],[2,5]])
u, v = N.basis()
u.inner_product(v)  # → -1  (= row u · A · col v = 1·(-1) + 0·5 = -1)
v.inner_product(u)  # → 2   (= row v · A · col u = 0·1 + 1·2 = 2)
```

This means `inner_product` is not commutative when A is asymmetric. `gram_matrix()` is B·A·Bᵀ and may be asymmetric; the "Gram matrix" interpretation as a symmetric bilinear form applies only when A is symmetric.

---

## 15. `GroupOfIsometries` and the Isometry Group API
`sage.groups.matrix_gps.isometries`

### 15.1 Overview

`GroupOfIsometries` is the concrete ℤ- or ℚ-lattice isometry group returned by `IntegralLattice.orthogonal_group()` and `TorsionQuadraticModule.orthogonal_group()`. It is a finitely generated matrix group with a GAP backend, and carries the bilinear form it preserves.

**Group action convention:** following GAP, the action is *from the right* — elements act as `x ↦ x·g`, not `x ↦ g·x`.

### 15.2 Constructor

```python
from sage.groups.matrix_gps.isometries import GroupOfIsometries

GroupOfIsometries(
    degree,                   # int: size of matrices (= rank of the lattice)
    base_ring,                # ZZ or QQ
    gens,                     # list of matrices; generators of the group
    invariant_bilinear_form,  # symmetric matrix defining the preserved form
    category=None,
    check=True,               # verify generators actually preserve the form
    invariant_submodule=None,         # if given, registers an action on this submodule
    invariant_quotient_module=None,   # if given, registers an action on this quotient
)
```

`check=True` (default) raises `ValueError` if any generator does not preserve the bilinear form.

### 15.3 Methods

| Method | Description |
|--------|-------------|
| `invariant_bilinear_form()` | Returns the symmetric matrix B defining the preserved pairing; `g` is an isometry iff `g · B · gᵀ = B` |
| `cardinality()` / `order()` | Group order; may be `+Infinity` for infinite groups (e.g. indefinite-signature lattice automorphisms) |
| `conjugacy_classes_representatives()` | Representatives of conjugacy classes (GAP); finite group only |
| `gens()` | List of generator matrices |
| `an_element()` | Any element of the group |

### 15.4 Ancillary action classes

| Class | Purpose |
|-------|---------|
| `GroupActionOnSubmodule(MatrixGroup, submodule)` | Right action of `GroupOfIsometries` on an invariant submodule |
| `GroupActionOnQuotientModule(MatrixGroup, quotient_module)` | Right action on an invariant quotient module; used e.g. to compute the image of Aut(L) acting on L∨/L |

### 15.5 Classical matrix groups with bilinear forms (separate API)

The following are separate from `GroupOfIsometries` and do not carry an explicit bilinear form object; they are defined abstractly by their defining field and rank:

| Constructor | Module | Description |
|-------------|--------|-------------|
| `GO(n, R)` / `GeneralOrthogonalGroup(n, R)` | `sage.groups.matrix_gps.orthogonal` | General orthogonal group over ring R |
| `SO(n, R)` / `SpecialOrthogonalGroup(n, R)` | same | Special orthogonal group |
| `GU(n, q)` / `GeneralUnitaryGroup(n, q)` | `sage.groups.matrix_gps.unitary` | General unitary group over GF(q²) |
| `SU(n, q)` / `SpecialUnitaryGroup(n, q)` | same | Special unitary group |

These use a GAP backend; the preserved bilinear/Hermitian form is hard-coded to the standard one for the type, not user-supplied.

### 15.6 Typical workflow

```python
# Get automorphism group of a PD lattice, then compute its image on discriminant form
L = IntegralLattice("E8").direct_sum(IntegralLattice("E8"))
O = L.orthogonal_group()          # GroupOfIsometries on a PD lattice
D = L.discriminant_group()
D_O = D.orthogonal_group(O.gens())  # image of O in Aut(discriminant form)
kernel_size = O.order() // D_O.order()   # kernel acts trivially on D
```

---

## 16. Root System Lattice Realizations
`sage.combinat.root_system`

### 16.1 Overview and relationship to `IntegralLattice`

Root-system lattices arise in two **distinct** contexts in Sage:

| Context | Object | Where |
|---------|--------|-------|
| **Combinatorial** ℤ-module with Cartan pairing | `RootSystem(type).root_lattice()` etc. | `sage.combinat.root_system` |
| **Arithmetic** lattice with explicit Gram matrix | `IntegralLattice("An")` etc. | `sage.modules.free_quadratic_module_integer_symmetric` |

`IntegralLattice("An")` internally calls `CartanMatrix(["A",n])`, computes its Gram matrix, and wraps it in the `IntegralLattice` framework. The bilinear form is then fully accessible via `gram_matrix()`, `discriminant_group()`, etc. This is the recommended path for lattice-theoretic computations.

The combinatorial realizations are best used when you need root-system structure (Weyl group, weight lattice, coroots, etc.) rather than lattice-theoretic invariants.

### 16.2 Combinatorial realizations: constructors

```python
R = RootSystem(['A', 4])     # root system of type A4
R = RootSystem(['E', 8])
R = RootSystem(['B', 3])
R = RootSystem(['G', 2])
R = RootSystem(['A', 4, 1])  # affine type A4^(1)
```

| Realization | Base ring | Description |
|-------------|-----------|-------------|
| `R.root_lattice()` | ℤ | Free ℤ-module spanned by simple roots α_i; has Cartan pairing |
| `R.coroot_lattice()` | ℤ | Spanned by simple coroots α_i^∨ |
| `R.weight_lattice()` | ℤ | Spanned by fundamental weights Λ_i |
| `R.root_space()` | ℚ | Root lattice ⊗ ℚ |
| `R.weight_space()` | ℚ | Weight lattice ⊗ ℚ |
| `R.ambient_lattice()` | ℤ | Euclidean ℤ-module in ℝ^n (type-dependent; not available for all types) |
| `R.ambient_space()` | ℚ | Euclidean ℚ-module in ℝ^n |

### 16.3 Scalar products and the Cartan pairing

Root lattice realizations do **not** expose a `gram_matrix()` method. The pairing is accessed via element methods:

| Method | Arguments | Returns | Notes |
|--------|-----------|---------|-------|
| `alpha.scalar(alphacheck)` | element, coroot element | scalar (integer or rational) | Cartan pairing ⟨α, α^∨⟩; this is how the Cartan/Dynkin matrix entries are computed |
| `x.inner_product(y)` | two ambient-space elements | scalar | Euclidean inner product in ambient space; only available for `ambient_space` / `ambient_lattice` realizations |
| `alpha.symmetric_form(beta)` | two weight-space elements | scalar | Symmetrised Killing form; extends to `weight_space` and `weight_lattice` |

To build the Cartan matrix explicitly:
```python
L = RootSystem(['A', 4]).root_lattice()
alpha = L.simple_roots()
alphacheck = L.simple_coroots()
cartan = matrix([[alpha[i].scalar(alphacheck[j]) for i in L.index_set()] for j in L.index_set()])
# cartan is the Cartan matrix (= 2·Gram / ⟨α,α⟩ for simply-laced types)
```

To get a proper Gram matrix (symmetric) for a simply-laced root system via `symmetric_form`:
```python
P = RootSystem(['A', 4]).weight_space()
al = P.simple_roots()
gram = matrix([[al[i].symmetric_form(al[j]) for i in P.index_set()] for j in P.index_set()])
```

### 16.4 Key element methods (root/weight lattice elements)

| Method | Description |
|--------|-------------|
| `simple_roots()` | Finite family {i: α_i} |
| `simple_coroots()` | Finite family {i: α_i^∨} |
| `positive_roots()` | All positive roots |
| `highest_root()` | Highest root θ |
| `fundamental_weights()` | Fundamental weights Λ_i |
| `rho()` | Weyl vector ρ = Σ Λ_i |
| `alpha.associated_coroot()` | α^∨ = 2α/(α,α) in coroot space |
| `alpha.is_real()` / `alpha.is_imaginary()` | (affine types) |

### 16.5 Converting to `IntegralLattice`

The recommended bridge from root system to `IntegralLattice` is the Cartan-type string constructor:
```python
L = IntegralLattice("E8")       # rank-8 E8 root lattice as IntegralLattice
L.gram_matrix()                 # 8×8 Cartan matrix (normalised so short roots have norm 2)
L.discriminant_group()          # trivial for E8
L.orthogonal_group()            # Weyl group × {±1} = Aut(E8), order 696729600

# For non-simply-laced or non-standard normalisation, build from Gram:
from sage.combinat.root_system.cartan_matrix import CartanMatrix
G = CartanMatrix(["G", 2]).dense_matrix().change_ring(ZZ)
L = IntegralLattice(G)
```

---

## 17. Number-Field and Quaternion-Algebra Lattices

Number fields and their fractional ideals **are** free ℤ-modules of rank n — they are lattices in the algebraic sense. Sage exposes this ℤ-module structure natively. The key subtlety for this reference is that the **metric** (trace form, norm form, or Minkowski inner product) is not stored inside the free module object returned by `.free_module()`: those return a bare `FreeModule(ZZ, n)` without an `inner_product_matrix`. To obtain a `FreeQuadraticModule` or `IntegralLattice` with full lattice-theory methods, you bridge the two pieces explicitly.

Quaternion algebra ideals behave differently: their `free_module()` and `gram_matrix()` carry the reduced norm form natively.

---

### 17.1 Free ℤ-module structure: `NumberField`, `Order`, and fractional ideals

| Object | `free_module()` returns | `basis()` / `integral_basis()` |
|--------|------------------------|-------------------------------|
| `K` (number field) | `(V, from_V, to_V)` where V ≅ QQ^n; a vector-space isomorphism, **no inner product** | `K.integral_basis()` — ℤ-basis of O_K as elements of K |
| `K.ring_of_integers()` | bare `FreeModule(ZZ, n)` **no inner product** | `OK.basis()` — same ℤ-basis |
| `I` (fractional ideal) | bare `FreeModule(ZZ, n)` as ℤ-span of `I.basis()` **no inner product** | `I.basis()` (may be in random order); `I.integral_basis()` for ℤ-basis of integral version |

In all three cases `.free_module()` returns a **bare ℤ-module** — it is not a `FreeQuadraticModule` and has no `gram_matrix()` method.

Key methods on number fields and ideals as ℤ-modules:

| Method | Object | Description |
|--------|--------|-------------|
| `K.integral_basis()` | `NumberField` | ℤ-basis {b_0, …, b_{n-1}} of O_K; elements of K |
| `K.free_module(base=QQ, map=True)` | `NumberField` | Returns (V, from_V, to_V); V is QQ^n; useful for computing coordinates |
| `K.discriminant()` | `NumberField` | Disc(K/ℚ) = det of trace form Gram matrix w.r.t. integral basis |
| `K.signature()` | `NumberField` | (r, s): r real, s pairs of complex embeddings; determines definiteness of trace form |
| `OK.basis()` | `Order` | Same as `K.integral_basis()` |
| `I.basis()` | `NumberFieldFractionalIdeal` | ℤ-basis of I (order depends on internal representation) |
| `I.integral_basis()` | `NumberFieldFractionalIdeal` | ℤ-basis of the integral part of I |
| `I.coordinates(a)` | `NumberFieldFractionalIdeal` | Coordinates of element a in the ℤ-basis |
| `I.norm()` | `NumberFieldFractionalIdeal` | Norm N(I) = [O_K : I] (as rational number) |

Extended number-field API frequently used alongside lattice bridges:

| Method | Object | Description |
|--------|--------|-------------|
| `K.absolute_degree()` / `K.relative_degree()` | `NumberField` | Absolute/relative extension degree |
| `K.absolute_field()` / `K.base_field()` | `NumberField` | View as absolute field / retrieve base field |
| `K.absolute_polynomial()` / `K.relative_polynomial()` / `K.defining_polynomial()` | `NumberField` | Defining polynomial variants |
| `K.real_embeddings()` / `K.complex_embeddings()` / `K.real_places()` | `NumberField` | Archimedean embedding data |
| `K.is_totally_real()` / `K.is_totally_imaginary()` / `K.is_galois()` | `NumberField` | Signature/Galois predicates |
| `K.class_group()` / `K.narrow_class_group()` / `K.unit_group()` | `NumberField` | Arithmetic invariants used before/after lattice construction |
| `K.S_class_group(S)` / `K.S_unit_group(S)` / `K.S_units(S)` | `NumberField` | S-arithmetic variants |
| `K.maximal_order()` / `K.ring_of_integers()` | `NumberField` | Integral structure objects |
| `K.primes_above(p)` / `K.primes_of_bounded_norm(B)` | `NumberField` | Prime-ideal search for local checks |
| `K.absolute_different()` / `K.relative_discriminant()` | `NumberField` | Different/discriminant data for trace-form analysis |

### 17.2 Trace form (exact, algebraic)

The **trace form** `b(x, y) = Tr_{K/ℚ}(xy)` is a symmetric bilinear form on K. On O_K it is ℤ-valued; on a fractional ideal I it may be rational-valued. Its Gram matrix w.r.t. the integral basis has determinant disc(O_K). The trace form is **positive definite for totally real fields** and **indefinite for fields with complex embeddings** (signature (r, r+2s) → there are s pairs of complex conjugate embeddings that together contribute indefinite directions after the real scaling in the Minkowski map).

```python
x = polygen(ZZ)
K = NumberField(x^3 - 2, 'a')
B = K.integral_basis()     # [1, a, a^2] as K-elements
n = K.degree()             # 3

# Gram matrix of the trace form w.r.t. the integral basis (exact, over ZZ or QQ)
G = matrix(QQ, n, n, lambda i, j: (B[i] * B[j]).trace())
# disc(K/QQ) == det(G) (up to sign convention)

# Bridge to IntegralLattice
L = IntegralLattice(G.change_ring(ZZ))   # works when G is integer-valued
L.discriminant()    # == K.discriminant()

# For a fractional ideal I:
OK = K.ring_of_integers()
I  = OK.ideal(K.gen())
basis_I = [K(b) for b in I.basis()]
G_I = matrix(QQ, n, n, lambda i, j: (basis_I[i] * basis_I[j]).trace())
# G_I is rational-valued in general; use FreeQuadraticModule for the rational case
```

Sage also exposes a single-shot determinant of the trace form via:
```python
# absolute_discriminant(v) = det of trace-pairing matrix on the list v
K.absolute_discriminant(list(K.integral_basis()))   # == K.discriminant()
```

### 17.3 Minkowski embedding (floating-point, real-analytic)

```python
K = NumberField(x^3 - 2, 'a')
M = K.minkowski_embedding()              # 3×3 matrix over RDF; columns = σ(1), σ(a), σ(a²)
M = K.minkowski_embedding(prec=200)      # RealField(200) precision
M = K.minkowski_embedding([1, a+2, a^2-a], prec=100)  # columns = σ on a given basis
```

`K.minkowski_embedding(prec=p)` returns a matrix M whose entries are elements of **RealField(p)** — floating-point numbers, not integers or algebraic numbers. The (k, j) entry of M is the floating-point evaluation, at precision p, of σ_k(b_j), where σ_k is the k-th real or (scaled real/imaginary part of the) complex embedding of K and b_j is the j-th basis element.

The product Mᵀ·M is therefore also a matrix over RealField(p). Its (i,j) entry is the floating-point evaluation of the algebraic number `Σ_k σ_k(b_i)·σ_k(b_j)`, which equals `Tr_{K/ℚ}(b_i·b_j)` exactly. When b_i are an integral basis, `Tr(b_i·b_j)` is an integer — but `(Mᵀ·M)[i,j]` is a floating-point number that approximates that integer with rounding error bounded by O(n · 2^{-p} · max_k|σ_k(b_i)| · max_k|σ_k(b_j)|). It is not the integer itself.

**Use the trace form (§17.2) to get the exact integer Gram matrix.** The Minkowski embedding is useful for numerical geometry-of-numbers work — successive minima estimates, plotting, Minkowski bound computation — but not for constructing `IntegralLattice` objects that require exact integer input.

### 17.4 Quaternion algebra ideals — `gram_matrix()` is natively supported

Unlike number field ideals, quaternion algebra fractional ideals carry the reduced norm form natively:

```python
from sage.all import *
A = QuaternionAlgebra(QQ, -1, -13)
I = A.ideal([2+A.i(), 3*A.i(), 5*A.j(), A.j()+A.k()])

# The free module with inner product = 2 * reduced norm
M = A.free_module()   # FreeQuadraticModule of rank 4 over ZZ with inner product diag(2,2,26,26)

# Gram matrix of a fractional ideal w.r.t. the norm form
I.gram_matrix()       # 4×4 Gram matrix over ZZ; entries are reduced norms of basis elements
                      # = B · (reduced_norm Gram of A) · B^T where B = I.basis_matrix()
```

`A.free_module()` returns a genuine `FreeQuadraticModule` (not a bare FreeModule); `QuaternionFractionalIdeal.gram_matrix()` is a first-class method. This is the principal difference from number field ideals.

### 17.5 Summary of what "bridge" is and isn't needed

| Source object | Is it a FreeQuadraticModule? | Has `gram_matrix()`? | Inner product |
|---------------|:---------------------------:|:--------------------:|---------------|
| `NumberField.ring_of_integers()` | ✗ | ✗ | Must build from `.trace()` |
| `NumberFieldFractionalIdeal.free_module()` | ✗ | ✗ | Must build from `.trace()` |
| `QuaternionAlgebra.free_module()` | ✓ | ✓ (= 2·reduced norm) | Built in |
| `QuaternionFractionalIdeal` | ✗ (but has `free_module()`) | ✓ | Built in |
| `IntegralLattice(G)` from trace form | ✓ | ✓ | Explicit Gram G |

---

## 18. Archived Out-of-Scope Toric/Polyhedral Discussion

Detailed toric/fan/polytope discussion and method notes that are out of active bilinear-form lattice scope were moved to:
`docs/archive/scope_violations/sage/lattice/sagemath_lattice_reference_toric_sections_2026-02-18.md`.

---

## 19. Sources

### Core SageMath documentation
- IntegralLattice and FreeQuadraticModule: `https://doc.sagemath.org/html/en/reference/modules/sage.modules.free_quadratic_module_integer_symmetric.html`
- IntegerLattice (FreeModule_submodule_with_basis_integer): `https://doc.sagemath.org/html/en/reference/modules/sage.modules.free_module_integer.html`
- QuadraticForm: `https://doc.sagemath.org/html/en/reference/quadratic_forms/sage.quadratic_forms.quadratic_form.html`
- TorsionQuadraticModule: `https://doc.sagemath.org/html/en/reference/modules/sage.modules.torsion_quadratic_module.html`
- BinaryQF and TernaryQF: `https://doc.sagemath.org/html/en/reference/special_forms/binary_quadratic_forms.html`
- Genus and LocalGenusSymbol: `https://doc.sagemath.org/html/en/reference/quadratic_forms/genus.html`

### Local upstream snapshots
- `docs/sage/integral_lattice/upstream/free_quadratic_module_integer_symmetric.html`
- `docs/sage/integer_lattice/upstream/free_module_integer.html`
- `docs/sage/quadratic_form/upstream/quadratic_form.html`
- `docs/sage/torsion_quadratic_module/upstream/torsion_quadratic_module.html`
- `docs/sage/special_forms/binary_quadratic_forms/upstream/binary_qf.html`
- `docs/sage/special_forms/ternary_quadratic_forms/upstream/ternary_qf.html`
- `docs/sage/genus/upstream/genus.html`
