# SageMath `TorsionQuadraticModule` Reference
## Finite ℤ-module A = V/W with bilinear and quadratic forms

`sage.modules.torsion_quadratic_module`

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[INT]` | Defined over **ℤ** (integer-valued bilinear form on the ambient lattice) |
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[EVEN]` | Requires even lattice (all (x,x) ∈ 2ℤ) |

---

## 1. Constructors

| Constructor | Description | Tags |
|-------------|-------------|------|
| `TorsionQuadraticModule(V, W, gens=None, modulus=None, modulus_qf=None, check=True)` | Construct the torsion quadratic module A = V/W where W ⊆ V are free ℤ-modules with a symmetric bilinear form. `gens` — explicit generators (default: Smith-form generators). `modulus` — denominator m for the bilinear form values in ℚ/mℤ (default: gcd of (V,W)). `modulus_qf` — denominator n for the quadratic form values in ℚ/nℤ (default: 2·modulus or gcd of (w,w) for w ∈ W). `check` — verify W ⊆ V. | `[INT]` |
| `TorsionQuadraticForm(q)` | Convenience constructor from a rational symmetric matrix q. Builds V = ℤ^n with inner product matrix q and W = ℤ^n so that A = V/W has bilinear form induced by q. Requires q non-degenerate. | `[INT, ND]` |

### Construction examples

```python
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

# From an integral lattice's discriminant group
L = IntegralLattice("A2")
D = L.discriminant_group()                       # TorsionQuadraticModule, ℤ/3

# From free modules directly
V = FreeQuadraticModule(ZZ, 2, matrix([[2,1],[1,2]]))
W = V.span([ V([1,0]), V([0,1]) ])
T = TorsionQuadraticModule(V.span([ V([1/3, 2/3]) ]), W)

# From a rational Gram matrix
from sage.modules.torsion_quadratic_module import TorsionQuadraticForm
T = TorsionQuadraticForm(matrix(QQ, [[2/3]]))    # ℤ/3 with q(1)=2/3
```

---

## 2. Element Methods (`TorsionQuadraticModuleElement`)

Elements `x` of a `TorsionQuadraticModule` carry the induced bilinear and quadratic forms directly.

| Method | Description | Tags |
|--------|-------------|------|
| `x.inner_product(y)` | Bilinear form value b(x, y) ∈ ℚ/mℤ, where m is the modulus of the module's `value_module()`. Symmetric: `x.inner_product(y) == y.inner_product(x)`. | |
| `x.b(y)` | Alias for `x.inner_product(y)`. | |
| `x.quadratic_product()` | Quadratic form value q(x) ∈ ℚ/nℤ, where n is the modulus of the module's `value_module_qf()`. Satisfies q(x+y) = q(x) + q(y) + b(x,y). | |
| `x.q()` | Alias for `x.quadratic_product()`. | |

### Element examples

```python
L = IntegralLattice(matrix(ZZ, [[2,1],[1,2]]))
D = L.discriminant_group()
g = D.gens()[0]
g.q()                           # quadratic form value q(g) in Q/2Z
g.b(g)                          # bilinear form value b(g,g) in Q/Z
g.inner_product(g) == g.b(g)    # True
g.quadratic_product() == g.q()  # True
```

---

## 3. Module Methods (`TorsionQuadraticModule`)

### 3.1 Underlying Data

| Method | Description | Tags |
|--------|-------------|------|
| `T.gens()` | Generators of T as a ℤ-module. No minimality guarantee; typically Smith-form generators unless overridden at construction. | |
| `T.gram_matrix_bilinear()` | Gram matrix of the bilinear form w.r.t. `gens()`. Entries are representatives in ℚ; the form takes values in ℚ/mℤ where m = `value_module().n`. | |
| `T.gram_matrix_quadratic()` | Gram matrix of the quadratic form w.r.t. `gens()`. Off-diagonal entries = bilinear form b(gᵢ, gⱼ); diagonal entries = quadratic form q(gᵢ). | |
| `T.value_module()` | The codomain ℚ/mℤ of the bilinear form, returned as a `QmodnZ` object. `m` = modulus. | |
| `T.value_module_qf()` | The codomain ℚ/nℤ of the quadratic form, returned as a `QmodnZ` object. `n` = modulus_qf; typically n = 2m or smaller when all (w,w) ∈ 2ℤ. | |
| `T.V()` | Ambient free quadratic module V (the numerator of V/W). | |
| `T.W()` | Submodule W (the denominator of V/W). | |
| `T.order()` | Group order \|T\| = \|det(V)\|/\|det(W)\|. Inherited from abelian group parent. | |
| `T.invariants()` | Invariants of the underlying abelian group, e.g. `(2, 6)` for ℤ/2 ⊕ ℤ/6. | |

### 3.2 Structural Operations

| Method | Description | Tags |
|--------|-------------|------|
| `T.direct_sum(other)` | Direct orthogonal sum of two `TorsionQuadraticModule` objects. The bilinear/quadratic forms are block-diagonal. | |
| `T.twist(s)` | Rescale the quadratic form by rational number s: q ↦ s·q, b ↦ s·b. Value modules scale accordingly. Returns a new `TorsionQuadraticModule`. | |
| `T.submodule(gens)` | Sub-`TorsionQuadraticModule` spanned by the given generators, with induced forms. | |
| `T.submodule_with_gens(gens)` | Sub-`TorsionQuadraticModule` with an explicitly supplied (possibly redundant) generator list. Useful when a specific Gram matrix presentation is needed. | |
| `T.orthogonal_submodule_to(S)` | Sub-`TorsionQuadraticModule` of all elements orthogonal to the submodule S under the bilinear form. Satisfies `T.orthogonal_submodule_to(S).V() + S.V() == T.V()` when bilinear form is non-degenerate. | |
| `T.primary_part(m)` | The m-primary submodule: all elements annihilated by some power of m. Returns a sub-`TorsionQuadraticModule` with induced forms. | |
| `T.all_submodules()` | List of all submodules. **Warning:** exponential in rank — use only for small groups. | |
| `T.quotient(W)` | Quotient torsion module T/W. Inherited from `FGP_Module`. | |

### 3.3 Classification and Genus

| Method | Description | Tags |
|--------|-------------|------|
| `T.normal_form(partial=False)` | Miranda–Morrison canonical normal form; unique up to isomorphism for non-degenerate forms. `partial=True` returns a partial (non-unique) normal form that still exposes p-adic invariants. | `[ND]` |
| `T.brown_invariant()` | Brown invariant Br(T, q) ∈ ℤ/8ℤ. Requires the quadratic form to be valued in ℚ/2ℤ (even lattice case). Additive over direct sums: Br(T₁ ⊕ T₂) = Br(T₁) + Br(T₂). | `[EVEN]` |
| `T.genus(signature_pair)` | `Genus` object compatible with this discriminant form and the given signature pair (p, n). Raises `ValueError` if no such genus exists. | |
| `T.is_genus(signature_pair, even=True)` | Whether there exists a lattice with this discriminant form and signature `signature_pair`. Upstream docs carry an explicit TODO for odd lattices; use `even=False` with caution because odd-lattice handling is not documented as complete. | |

### 3.4 Symmetry

| Method | Description | Tags |
|--------|-------------|------|
| `T.orthogonal_group(gens=None, check=False)` | Isometry group of T preserving both the bilinear and quadratic forms. If `gens` is given (e.g. from `IntegralLattice.orthogonal_group()`), restricts to the subgroup generated by those elements. `check=False` skips verification that generators preserve forms. | |

---

## 4. Relationship to Other Sage Objects

| Source | Method | Result |
|--------|--------|--------|
| `IntegralLattice` | `.discriminant_group()` | `TorsionQuadraticModule` L∨/L |
| `IntegralLattice` | `.discriminant_group(s=p)` | p-primary part of L∨/L |
| `Genus` | `.discriminant_form()` | `TorsionQuadraticModule` associated to the genus |
| `TorsionQuadraticModule` | `.genus(sig)` | `Genus` compatible with this discriminant form |

---

## 5. Value Module Conventions

The bilinear and quadratic forms of a `TorsionQuadraticModule` take values in quotient rings of ℚ:

| Object | Codomain | Accessor |
|--------|----------|----------|
| Bilinear form b(x, y) | ℚ/mℤ | `T.value_module()` |
| Quadratic form q(x) | ℚ/nℤ | `T.value_module_qf()` |

The moduli satisfy n \| 2m. For even lattices, n = 2m. The `QmodnZ` object supports arithmetic in ℚ/nℤ and comparison of representatives.

---

## 6. Summary of Aliases

| Preferred name | Alias | Context |
|----------------|-------|---------|
| `x.inner_product(y)` | `x.b(y)` | Element bilinear form |
| `x.quadratic_product()` | `x.q()` | Element quadratic form |
