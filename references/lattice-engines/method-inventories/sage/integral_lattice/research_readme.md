# SageMath `IntegralLattice` / `FreeQuadraticModule_integer_symmetric` Reference
## Integral lattice = free ℤ-module with non-degenerate symmetric bilinear form

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Requires or only meaningful for **positive definite** forms |
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[INDEF]` | Works correctly for **indefinite** signatures |
| `[DEFINITE]` | Requires **definite** form (positive-definite or negative-definite); indefinite forms raise `NotImplementedError` |
| `[EVEN]` | Requires even lattice (all $(x,x) \in 2\mathbb{Z}$) |
| `[INT]` | Defined over **ℤ** (integer-valued bilinear form) |
| `[RAT]` | Involves rational coefficients |
| `[PARI]` | Delegates to **PARI/GP** |
| `[FPLLL]` | Delegates to **fplll/fpylll** |

---

## 1. Constructor Functions

### 1.1 `IntegralLattice(data, basis=None)` `[INT, ND]`
`sage.modules.free_quadratic_module_integer_symmetric`

Constructs a symmetric non-degenerate integral lattice. Allows indefinite signatures.

`data` accepts:

| Input | Result |
|-------|--------|
| `Matrix(ZZ/QQ, n, n)` symmetric | Gram matrix as ambient space |
| integer `n` | Rank-n Euclidean lattice ($I_n$) |
| Cartan type string e.g. `"E8"` | Root lattice by Cartan matrix — requires `sage.graphs` |
| Cartan type list e.g. `["A",3]` | Same |
| `"U"` / `"H"` | Hyperbolic plane $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ `[INDEF]` |

`basis` — optional matrix/list of vectors; rows span the sublattice in the ambient space.

```python
IntegralLattice(matrix(ZZ, [[2,1],[1,-2]]))         # indefinite, rank 2
IntegralLattice(3)                                   # I_3  [PD]
IntegralLattice("E8")                                # E8 root lattice  [PD]
IntegralLattice("U")                                 # hyperbolic plane U  [INDEF]
IntegralLattice(matrix.identity(3), [[1,-1,0],[0,1,-1]])  # A2 from ambient I_3
```

### 1.2 `IntegralLatticeDirectSum(Lattices, return_embeddings=False)` `[INT, ND]`
`sage.modules.free_quadratic_module_integer_symmetric`

Orthogonal direct sum of a list of `IntegralLattice` objects.

| Parameter | Description |
|-----------|-------------|
| `Lattices` | List of `IntegralLattice` objects |
| `return_embeddings` | If `True`, returns `[L, [φ_1, …, φ_k]]` with inclusion maps |

```python
L1 = IntegralLattice("A2")
L2 = IntegralLattice("U")
S = IntegralLatticeDirectSum([L1, L2])                   # rank 4, sig (3,1)
S, embs = IntegralLatticeDirectSum([L1, L2], return_embeddings=True)
```

### 1.3 `IntegralLatticeGluing(Lattices, glue, return_embeddings=False)` `[INT, ND]`
`sage.modules.free_quadratic_module_integer_symmetric`

Overlattice of the orthogonal direct sum defined by discriminant-group glue vectors.

| Parameter | Description |
|-----------|-------------|
| `Lattices` | List of `IntegralLattice` objects |
| `glue` | List of lists `[g_1, …, g_k]` where $g_i \in \operatorname{discr}(L_i)$; each inner list gives a glue vector in the direct sum of discriminant groups |
| `return_embeddings` | If `True`, returns `[L, [φ_1, …, φ_k]]` with inclusion maps |

The resulting overlattice is integral iff each glue vector has trivial quadratic form value in $\mathbb{Q}/2\mathbb{Z}$.

```python
L1 = IntegralLattice(matrix(ZZ, [[2,1],[1,2]]))
L2 = IntegralLattice(matrix(ZZ, [[-2,-1],[-1,-2]]))
D1 = L1.discriminant_group()
D2 = L2.discriminant_group()
g1 = D1.gens()[0]
g2 = D2.gens()[0]
G = IntegralLatticeGluing([L1, L2], [[g1, g2]])
```

---

## 2. Intrinsic Data and Predicates

`FreeQuadraticModule_integer_symmetric` methods. `[INT, ND]` unless otherwise noted.

| Method | Description | Tags |
|--------|-------------|------|
| `gram_matrix()` | Gram matrix $B \cdot M \cdot B^T$ where $B$ = `basis_matrix()` and $M$ = `inner_product_matrix()`; this is the Gram matrix of the lattice w.r.t. its current basis | inherited |
| `basis_matrix()` | Matrix whose rows form the current basis of the lattice in the ambient space | inherited |
| `inner_product_matrix()` | Gram matrix of the ambient space (not the lattice's own Gram matrix for submodules) | inherited |
| `rank()` | Rank of the lattice (number of basis vectors) | inherited |
| `degree()` | Dimension of the ambient space | inherited |
| `determinant()` | $\det(\text{gram\_matrix}())$; equivalently $\det(B M B^T)$ | inherited |
| `discriminant()` | Alias for `determinant()`; returns $\det(\text{gram\_matrix}())$ with no sign correction. Differs from `FreeQuadraticModule_generic.discriminant()` which applies $(−1)^r$ sign factor where $r = \lfloor\text{rank}/2\rfloor$ | inherited |
| `signature()` | Signature $p - n$ where $(p, n)$ = `signature_pair()`. Source: upstream `signature` method docs | `[INDEF ok]` |
| `signature_pair()` | Signature pair $(p, n)$: counts of positive / negative eigenvalues of the Gram matrix. Source: upstream `signature_pair` method docs (lines 1405-1422) | `[INDEF ok]` |
| `is_even()` | Whether all diagonal entries of the Gram matrix are even, i.e. $(x,x) \in 2\mathbb{Z}$ for all basis vectors. Source: upstream `is_even` method docs (line 792) | |
| `is_positive_definite()` | Whether the form is positive definite. Inherited from parent class | |
| `is_negative_definite()` | Whether the form is negative definite. Inherited from parent class | |
| `is_definite()` | Positive or negative definite. Inherited from parent class | |

---

## 3. Dual and Discriminant

| Method | Description | Tags |
|--------|-------------|------|
| `dual_lattice()` | Dual lattice $L^\vee = \{x \in L \otimes \mathbb{Q} : (x, \ell) \in \mathbb{Z}\ \forall \ell \in L\}$; returned as a `FreeQuadraticModule_integer_symmetric` in the same ambient space. Source: upstream `dual_lattice` method docs (line 601) | |
| `discriminant_group(s=0)` | Discriminant group $L^\vee / L$ as a `TorsionQuadraticModule` with the induced $\mathbb{Q}/\mathbb{Z}$-valued bilinear form and $\mathbb{Q}/2\mathbb{Z}$-valued quadratic form. If $s \neq 0$, returns the $s$-primary part (the subgroup of elements whose order is a power of $s$). Source: upstream `discriminant_group` method docs (lines 546-595) | |

```python
L = IntegralLattice("A2")
D = L.discriminant_group()    # Z/3Z
D.gram_matrix_quadratic()     # quadratic form on discriminant group
L.dual_lattice().gram_matrix()
```

---

## 4. Module Operations

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(M)` | Orthogonal direct sum of `self` with lattice `M`; returns a new `IntegralLattice` | |
| `sublattice(basis)` | Sublattice spanned by the given `basis` vectors; the vectors must lie in `self` and the resulting sublattice must be integral | `[INT]` |
| `overlattice(gens)` | Overlattice spanned by $L \cup \text{gens}$; `gens` are vectors in $L \otimes \mathbb{Q}$; the result must be integral | `[RAT]` |
| `maximal_overlattice(p=None)` | Maximal even integral overlattice of `self`. If `p` is given, maximise only at the prime `p`. Requires `self` to be even when `p=None` or `p=2` | `[EVEN if p=None or p=2]` |
| `orthogonal_complement(M)` | Orthogonal complement of submodule `M` in `self`; $M^\perp = \{x \in L : (x,m) = 0\ \forall m \in M\}$ | |
| `is_primitive(M)` | Whether the submodule `M` is primitive in `self`, i.e. $L/M$ is torsion-free | |
| `tensor_product(other, discard_basis=False)` | Tensor product of lattices; Gram matrix is the Kronecker product of the two Gram matrices. If `discard_basis=True`, the result uses the standard basis | |
| `twist(s, discard_basis=False)` | Rescale the inner product by scalar $s$: new form is $s \cdot (\ ,\ )$. If `discard_basis=True`, the result uses the standard basis | |

```python
L = IntegralLattice("E8")
U = IntegralLattice("U")
K3 = L.direct_sum(L).direct_sum(U).direct_sum(U).direct_sum(U)  # K3 lattice
K3.signature_pair()    # (3, 19)

S = L.sublattice([L.basis()[0] + L.basis()[1]])
L.is_primitive(S)
L.orthogonal_complement(S)

L_neg = L.twist(-1)   # negative definite E8(-1)
```

---

## 5. Reduction

| Method | Description | Tags |
|--------|-------------|------|
| `LLL()` | Returns a new `IntegralLattice` with LLL-reduced basis. Uses PARI `qflll`/`qflllgram`, which handles indefinite forms. Returns a lattice object, not a matrix. Source: upstream `LLL` method docs (lines 1474+) | `[INDEF ok, PARI]` |
| `lll()` | Alias for `LLL()` | `[INDEF ok, PARI]` |

**Caveats:**
- For positive definite lattices, LLL reduction produces a basis with provably short vectors.
- For indefinite lattices, the algorithm runs (via PARI) but "short" is relative to a majorant form, not the indefinite form itself — the result is a valid basis but the reduction quality has limited geometric meaning.
- Contrast with `IntegerLattice.LLL()`, which returns a matrix and uses fplll (PD only).

```python
L = IntegralLattice(matrix(ZZ, [[4,2],[2,4]]))
L_red = L.LLL()
L_red.gram_matrix()
```

---

## 6. Vector Enumeration

| Method | Description | Tags |
|--------|-------------|------|
| `short_vectors(n, **kwargs)` | List of all nonzero vectors $v$ with $(v,v) < n$. Uses PARI `qfminim`. Returns list `L` where `L[k]` is the list of vectors of norm exactly $k$; keyword `up_to_sign_flag=True` returns only one representative per $\pm v$ pair. Source: upstream `short_vectors` method docs | `[PD, PARI]` |
| `enumerate_short_vectors()` | Lazy iterator over all nonzero lattice vectors modulo sign, starting from shorter vectors. Uses fplll. **Does not guarantee non-decreasing norm order** — vectors with larger norm may appear before shorter ones. Source: upstream `enumerate_short_vectors` method docs (lines 690-747) | `[PD, FPLLL]` |
| `enumerate_close_vectors(target)` | Lazy iterator over lattice vectors close to `target`. Uses fplll. **No ordering guarantee** — the first yielded vector is not necessarily the closest | `[PD, FPLLL]` |
| `minimum()` / `min()` | Minimum norm $(v,v)$ over all nonzero vectors $v \in L$. Uses PARI | `[PD, PARI]` |
| `maximum()` / `max()` | Maximum norm $(v,v)$ over all nonzero vectors $v \in L$. Meaningful only for negative definite lattices (the "minimum" of $\lvert(v,v)\rvert$) | `[ND (negative definite)]` |

**Caveats:**
- `short_vectors`, `minimum`, `maximum` require definite forms; results are incorrect or raise errors on indefinite input.
- `enumerate_short_vectors` and `enumerate_close_vectors` (added ≥10.x, Lorenz Panny 2024) are lazy iterators without strict ordering — do not rely on them for finding the actual shortest or closest vector.

```python
L = IntegralLattice("A2")
L.short_vectors(4)            # vectors with norm ≤ 4
L.minimum()                   # 2 (shortest root length in A2)

for v in L.enumerate_short_vectors():
    print(v)
    break
```

---

## 7. Automorphisms

| Method | Description | Tags |
|--------|-------------|------|
| `orthogonal_group(gens=None, is_finite=None)` | Orthogonal group $O(L)$ as a `GroupOfIsometries` (matrix group preserving the bilinear form). If `gens` is given, returns the subgroup generated by `gens`. `is_finite` can be set to `True`/`False` to hint whether the group is finite. **Automatic generator computation requires definite form**; indefinite raises `NotImplementedError`. Source: upstream `orthogonal_group` method docs (lines 1062-1085) | `[DEFINITE]` |
| `automorphisms` | Alias for `orthogonal_group()` | `[DEFINITE]` |

**Caveats:**
- Automatic computation of generators requires a **definite** lattice (positive definite or negative definite); indefinite forms raise `NotImplementedError` (use `GroupOfIsometries` directly with manually supplied generators for indefinite lattices).
- The group action follows the GAP convention: **right action** $x \mapsto x \cdot g$.

```python
L = IntegralLattice("D4")
O = L.orthogonal_group()
O.order()                      # |Aut(D4)|
O.gens()                       # generator matrices
```

---

## 8. Classification

| Method | Description | Tags |
|--------|-------------|------|
| `genus()` | Genus symbol of the lattice, via `sage.quadratic_forms.genera.genus.Genus`. Encodes local invariants at all primes; two lattices in the same genus are locally isometric at every prime and over $\mathbb{R}$. Source: upstream `genus` method docs (lines 760-782) | `[INDEF ok]` |
| `quadratic_form()` | Associated `QuadraticForm` $q(x) = (x,x)$; the Hessian matrix of $q$ is $2G$ where $G$ is the Gram matrix | |

```python
L = IntegralLattice(matrix(ZZ, [[2,1],[1,2]]))
g = L.genus()
g.determinant()
g.signature_pair_of_matrix()

q = L.quadratic_form()
q.det()                        # det of Hessian = det(2G)
```

---

## 9. Module-Level Function

### `local_modification(M, G, p, check=True)` `[INT, ND, PARI]`
`sage.modules.free_quadratic_module_integer_symmetric`

Replace the local structure of lattice `M` at prime `p` so that its genus symbol at `p` matches that of the lattice with Gram matrix `G`. All other local completions and the signature remain unchanged.

| Parameter | Description |
|-----------|-------------|
| `M` | An `IntegralLattice` |
| `G` | A symmetric integer matrix (Gram matrix of the target local structure) |
| `p` | A prime number |
| `check` | If `True` (default), verify that `M` and `G` have the same signature and genus away from `p` |

Returns a new `IntegralLattice` whose genus agrees with `M` at all primes $\neq p$ and agrees with the lattice defined by `G` at the prime `p`.

```python
L = IntegralLattice(matrix(ZZ, [[2,0],[0,2]]))
G_target = matrix(ZZ, [[1,0],[0,1]])
L_mod = local_modification(L, G_target, 2)
L_mod.genus()
```

---

## 10. Definiteness Constraints Summary

| Regime | Available methods |
|--------|------------------|
| **PD** | All: LLL, `short_vectors`, `minimum`, `enumerate_short_vectors`, `enumerate_close_vectors`, `orthogonal_group` (automatic), genus, discriminant group, module operations |
| **ND** | `orthogonal_group` (automatic), genus, discriminant group, module operations; use `twist(-1)` to get a PD lattice for `short_vectors`/`minimum`/`enumerate_short_vectors`/`enumerate_close_vectors` |
| **INDEF** | `LLL`/`lll` (runs via PARI, limited geometric meaning); genus; discriminant group; `signature_pair`; module operations (`direct_sum`, `sublattice`, `overlattice`, `orthogonal_complement`); `tensor_product`; `twist`. No automatic `orthogonal_group` (raises `NotImplementedError`); no `short_vectors`/`minimum` |

---

## Sources

- SageMath source: `sage.modules.free_quadratic_module_integer_symmetric`
- SageMath documentation: [IntegralLattice](https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_quadratic_module_integer_symmetric.html)
- Cross-reference: `sagemath_lattice_reference.md` (broader SageMath lattice ecosystem)
- Cross-reference: `julia_lattice_methods_reference.md` (Julia/Hecke equivalents)
