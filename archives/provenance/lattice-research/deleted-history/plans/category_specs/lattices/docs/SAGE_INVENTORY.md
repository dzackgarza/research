# SAGE_INVENTORY.md — Lattices Subtree

Indexes every Sage class and method relevant to the lattices hierarchy, with on-disk
paths and line numbers. Consult this before searching Sage source directly.

`SAGE_LIB` below expands to:
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage`

---

## Tier 0 — Generic modules with inner product (free, over commutative ring)

### `FreeQuadraticModule_generic`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:258`  
**Inherits:** `free_module.FreeModule_generic`  
**Role:** Base class for all free quadratic modules; carries an inner product matrix.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 310 | `__init__` | `(base_ring, rank, degree, inner_product_matrix, sparse=False)` | |
| 369 | `ambient_module` | `(self)` | ambient quadratic module |
| 390 | `determinant` | `(self)` | det of Gram matrix |
| 408 | `discriminant` | `(self)` | `(-1)^r * det(gram_matrix)` |
| 439 | `gram_matrix` | `(self)` | `B·A·B^T` where `A` = inner product matrix, `B` = basis |
| 472 | `inner_product_matrix` | `(self)` | raw inner product matrix |

### `FreeQuadraticModule_generic_pid`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:588`  
**Inherits:** `FreeModule_generic_pid`, `FreeQuadraticModule_generic`

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 610 | `span` | `(self, gens, check=True, already_echelonized=False)` | R-span, need not be submodule |
| 637 | `span_of_basis` | `(self, basis, check=True, already_echelonized=False)` | free R-module on basis |
| 680 | `zero_submodule` | `(self)` | zero submodule |

### `FreeQuadraticModule_generic_field`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:696`  
**Inherits:** `FreeModule_generic_field`, `FreeQuadraticModule_generic_pid`

| Line | Method | Notes |
|------|--------|-------|
| 731 | `span` | K-span |
| 771 | `span_of_basis` | K-basis |

### Ambient/submodule variants (inherit all above; no new math methods)
- `FreeQuadraticModule_ambient` (line 822)
- `FreeQuadraticModule_ambient_domain` (line 947) — adds `ambient_vector_space()` (line 1013)
- `FreeQuadraticModule_ambient_pid` (line 1038)
- `FreeQuadraticModule_ambient_field` (line 1126)
- `FreeQuadraticModule_submodule_with_basis_pid` (line 1210) — adds `change_ring(R)` (line 1351)
- `FreeQuadraticModule_submodule_pid` (line 1398)
- `FreeQuadraticModule_submodule_with_basis_field` (line 1471)
- `FreeQuadraticModule_submodule_field` (line 1610)

---

## Tier 1 — Finitely generated modules over PID (V/W presentation, possibly torsion)

### `FGP_Module_class`
**File:** `SAGE_LIB/modules/fg_pid/fgp_module.py:293`  
**Inherits:** `Module`  
**Role:** Quotient `V/W` for `V`, `W` free modules over a PID. Represents the full
finitely-generated-module-over-PID stratum, including torsion.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 339 | `__init__` | `(self, V, W, check=True)` | |
| 707 | `submodule` | `(self, x)` | submodule defined by x |
| 798 | `is_submodule` | `(self, A)` | inclusion check |
| 837 | `V` | `(self)` | cover module |
| 855 | `cover` | `(self)` | alias for V() |
| 875 | `W` | `(self)` | relations module |
| 893 | `relations` | `(self)` | alias for W() |
| 940 | `_smith_form` | `(self)` | Smith normal form matrices |
| 962 | `base_ring` | `(self)` | base PID |
| 977 | `invariants` | `(self, include_ones=False)` | diagonal of Smith form |
| 1016 | `gens` | `(self)` | generators tuple |
| 1040 | `smith_form_gens` | `(self)` | Smith form generators |
| 1071 | `gens_to_smith` | `(self)` | change-of-basis matrix |
| 1185 | `gens_vector` | `(self, x, reduce=False)` | coordinates w.r.t. gens |
| 1247 | `coordinate_vector` | `(self, x, reduce=False)` | optimized coordinates |
| 1406 | `optimized` | `(self)` | isomorphic module in optimized form |
| 1480 | `hom` | `(self, im_gens, codomain=None, check=True)` | morphism by images |
| 1690 | `_Hom_` | `(self, N, category=None)` | homset construction |
| 1755 | `cardinality` | `(self)` | cardinality of underlying set |
| 1788 | `list` | `(self)` | list of all elements |
| 1867 | `is_finite` | `(self)` | True iff finite (iff torsion) |
| 1886 | `annihilator` | `(self)` | ideal `Ann_R(M)` |
| 1920 | `ngens` | `(self)` | number of generators |
| 1957 | `quotient_map` | `(self)` | natural map V → V/W |

### `FGP_Element`
**File:** `SAGE_LIB/modules/fg_pid/fgp_element.py:58`  
**Inherits:** `ModuleElement`

| Line | Method | Notes |
|------|--------|-------|
| 85 | `lift` | lift to cover V |
| 312 | `vector` | vector representation |
| 414 | `additive_order` | order in the group |

### `FGP_Morphism`
**File:** `SAGE_LIB/modules/fg_pid/fgp_morphism.py:73`  
**Inherits:** `Morphism`

| Line | Method | Notes |
|------|--------|-------|
| 137 | `im_gens` | images of domain generators |
| 226 | `__call__` | evaluate on element or submodule |
| 299 | `kernel` | kernel as FGP module |
| 327 | `inverse_image` | preimage of submodule |
| 368 | `image` | image as FGP module |
| 386 | `lift` | lift element from codomain to domain |

---

## Tier 2 — Torsion bilinear/quadratic modules (discriminant group level)

### `TorsionQuadraticModule`
**File:** `SAGE_LIB/modules/torsion_quadratic_module.py`  
**Inherits:** `FGP_Module_class`, `CachedRepresentation`  
**Role:** `V/W` with a `Q/Z`-valued quadratic form (or `Q/2Z` for even); the canonical
model for discriminant groups of lattices.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 363 | `all_submodules` | `(self)` | all submodules |
| 408 | `brown_invariant` | `(self)` | Brown invariant (global invariant of torsion QF) |
| 457 | `gram_matrix_bilinear` | `(self)` | Gram matrix of bilinear form (entries in Q/mZ) |
| 487 | `gram_matrix_quadratic` | `(self)` | Gram matrix of quadratic form (diagonal = q values) |
| 520 | `gens` | `(self)` | generators tuple |
| 539 | `genus` | `(self, signature_pair)` | genus from discriminant form + signature |
| 743 | `is_genus` | `(self, signature_pair, even=True)` | test realizability |
| 816 | `orthogonal_group` | `(self, gens=None, check=False)` | Aut of torsion QF |
| 890 | `orthogonal_submodule_to` | `(self, S)` | orthogonal complement of submodule |
| 939 | `normal_form` | `(self, partial=False)` | canonical normal form |
| 1113 | `primary_part` | `(self, m)` | m-primary part |
| 1149 | `submodule_with_gens` | `(self, gens)` | submodule on given generators |
| 1207 | `twist` | `(self, s)` | scale form by s |
| 1251 | `value_module` | `(self)` | `Q/mZ` (bilinear form values) |
| 1271 | `value_module_qf` | `(self)` | `Q/nZ` (quadratic form values) |

### `TorsionQuadraticModuleElement`
**File:** `SAGE_LIB/modules/torsion_quadratic_module.py`  
**Inherits:** `FGP_Element`

| Line | Method | Alias | Notes |
|------|--------|-------|-------|
| 121 | `_mul_` / `inner_product` / `b` | lines 151–152 | bilinear form evaluation |
| 154 | `quadratic_product` / `q` | line 185 | quadratic form evaluation |

---

## Tier 3 — Integral lattices over ZZ (free, symmetric, nondegenerate, integral)

### `FreeQuadraticModule_integer_symmetric`
**File:** `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py:625`  
**Inherits:** `FreeQuadraticModule_submodule_with_basis_pid`  
**Role:** The canonical "integral lattice" in Sage: `ZZ`-free, finite rank, symmetric
nondegenerate bilinear form with integer values.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 736 | `is_even` | `(self)` | diagonal Gram entries all even |
| 753 | `dual_lattice` | `(self)` | `L^∨ = {x ∈ L⊗Q : (x,l) ∈ Z ∀l}` |
| 779 | `discriminant_group` | `(self, s=0)` | `L^∨/L` (s-primary part if s≠0) |
| 839 | `signature` | `(self)` | `n_+ - n_-` |
| 855 | `signature_pair` | `(self)` | `(n_+, n_-)` |
| 871 | `direct_sum` | `(self, M)` | orthogonal direct sum |
| 901 | `is_primitive` | `(self, M)` | M is primitive submodule (quotient torsion-free) |
| 931 | `orthogonal_complement` | `(self, M)` | `M^⊥` inside self |
| 972 | `sublattice` | `(self, basis)` | sublattice spanned by basis |
| 1008 | `overlattice` | `(self, gens)` | lattice spanned by self and extra gens |
| 1030 | `maximal_overlattice` | `(self, p=None)` | max even integral overlattice |
| 1155 | `orthogonal_group` | `(self, gens=None, is_finite=None)` | `O(L)` as matrix group |
| 1313 | `automorphisms` | (alias) | alias for orthogonal_group |
| 1315 | `genus` | `(self)` | genus of the lattice |
| 1332 | `tensor_product` | `(self, other, discard_basis=False)` | tensor product with form |
| 1393 | `quadratic_form` | `(self)` | associated `QuadraticForm` via `q(x)=(x,x)` |
| 1409 | `minimum` | `(self)` | min `{β(x,x) : x ∈ L\{0}}` |
| 1435 | `maximum` | `(self)` | max `{β(x,x) : x ∈ L\{0}}` |
| 1460 | `min`, `max` | (aliases) | |
| 1463 | `LLL` | `(self)` | LLL-reduced basis |
| 1498 | `lll` | (alias) | |
| 1500 | `short_vectors` | `(self, n, **kwargs)` | vectors of length < n |
| 1596 | `enumerate_short_vectors` | `(self)` | iterator, shortest first |
| 1631 | `enumerate_close_vectors` | `(self, target)` | iterator near target |
| 1653 | `twist` | `(self, s, discard_basis=False)` | scale inner product by s |

---

## Tier 4 — Quadratic forms (separate Sage type; closely related)

### `QuadraticForm`
**File:** `SAGE_LIB/quadratic_forms/quadratic_form.py:185`  
**Inherits:** `SageObject`  
**Role:** Symmetric bilinear form encoded via upper-triangular coefficient matrix.
Distinct from `FreeQuadraticModule_integer_symmetric` but closely related for ZZ.

Key methods relevant to our hierarchy:

| Line | Method | Notes |
|------|--------|-------|
| 736 | `_repr_` | upper-triangular display |
| 1150 | `matrix` | Hessian matrix `A` where `Q(X)=(1/2)X^T A X` |
| 1190 | `Gram_matrix_rational` | Gram matrix over Frac(R) |
| 1214 | `Gram_matrix` | Gram matrix over base ring |
| 1451 | `dim` | number of variables |
| 1470 | `base_ring` | |
| 1482 | `coefficients` | upper-triangular coefficients |
| 1495 | `det` | det of Hessian |
| 1523 | `Gram_det` | det of Gram matrix |
| 1541 | `change_ring` | base ring change |
| 1586 | `level` | level over PID |
| 1689 | `bilinear_map` | `B(v,w)` associated bilinear map |
| 1393 | `is_primitive` | form not a scalar multiple of another |
| 1301 | `polynomial` | form as polynomial |

Signature/definiteness (lazy-imported from submodules):
- `is_positive_definite`, `is_negative_definite`, `is_indefinite` — `quadratic_form__local_field_invariants`
- `signature_vector`, `signature` — same submodule
- `hasse_invariant`, `anisotropic_primes` — local invariants

Genus (lazy-imported):
- `global_genus_symbol`, `local_genus_symbol`, `CS_genus_symbol_list` — `quadratic_form__genus`

Automorphisms (lazy-imported):
- `automorphism_group`, `automorphisms`, `basis_of_short_vectors` — `quadratic_form__automorphisms`

---

## Reference: existing `src/lattices/categories/` method surfaces

These files are the pre-existing implementation; read for method names, not structure.

### `BilinearModules` (src/lattices/categories/bilinear_modules.py)

**ParentMethods** (abstract unless noted):
`bilinear_form`, `gens`, `zero`, `base_ring`, `free_part`, `torsion_part`, `Hom`,
`dual`, `twist`, `span`, `cardinality`

**ParentMethods** (derived — one-liners):
`b(v,w)` (delegates to `bilinear_form().evaluate(v,w)`),
`gram_matrix()` (fills matrix with `b(e_i, e_j)` — **note**: this is placed here in
src/, but correct placement is `Free + Bilinear`; see MAPPING.md),
`End()`, `symbolic_form()`, `direct_sum(other)`, `__add__`, `__pow__`, `__mul__`

**ElementMethods** (abstract): `parent`, `__add__`, `__neg__`, `__rmul__`, `__eq__`,
`__hash__`, `to_vector`

**ElementMethods** (derived): `__mul__` (= b(self, other)), `self_product` (= b(v,v)),
`is_isotropic`, `span`, `__sub__`

**MorphismMethods** (abstract): `domain`, `codomain`, `__call__`, `to_matrix`,
`kernel`, `image`, `cokernel`, `is_isometry`

**MorphismMethods** (derived): `is_injective`, `is_surjective`, `is_bijective`,
`is_isomorphism`, `__mul__` (composition), `direct_sum`

### `FreeBilinearModules` (src/lattices/categories/free_bilinear_modules.py)

**ParentMethods** (abstract): `rank`, `is_nondegenerate`, `is_positive_definite`,
`is_negative_definite`

**ParentMethods** (derived — overrides): `free_part` (= self), `torsion_part` (= 0),
`cardinality` (= ∞ if rank > 0)

**ParentMethods** (derived): `is_definite`, `is_indefinite`

**ElementMethods** (abstract): `divisibility`

**ElementMethods** (derived): `is_primitive`, `discriminant_class`

**SubcategoryMethods**: `NonDegenerate()`

### `Lattices` (src/lattices/categories/lattices.py)

**ParentMethods** (abstract): `signature_pair`, `determinant`, `is_even`,
`nikulin_invariants`, `dual`, `inclusion_morphism`, `discriminant_group`,
`is_isometric_to`, `is_rationally_isometric_to`, `is_locally_isometric_to`,
`rational_span`, `to_quadratic_module`

**ParentMethods** (derived): `signature`, `discriminant`, `is_odd`, `is_unimodular`,
`genus`, `O()` / `orthogonal_group()`

**ElementMethods** (abstract): `norm`, `is_root`

**ElementMethods** (derived): `is_isotropic`, `reflection`, `perp`

**SubcategoryMethods**: `Even()`, `Unimodular()`

### `RationalLattices` (src/lattices/categories/rational_lattices.py)

**ParentMethods** (abstract): `signature_pair`, `base_change_to`, `orthogonal_complement_of`

**ParentMethods** (derived): `signature`, `is_positive_definite`, `is_negative_definite`

**ElementMethods** (abstract): `is_integral`

**ElementMethods** (derived): `perp`

### `TorsionBilinearModules` (src/lattices/categories/torsion_bilinear_modules.py)

**ParentMethods** (abstract): `invariants`, `is_p_elementary`, `p_part`, `jordan_decomposition`

**ParentMethods** (derived overrides): `free_part` (= 0), `torsion_part` (= self),
`cardinality` (= product of invariants)

**ElementMethods** (abstract): `additive_order`, `lift`

### `DiscriminantQuadraticForms` (src/lattices/categories/discriminant_quadratic_forms.py)

Thin category: `super_categories` only; no additional method surface yet.
