# GAP Lattice Methods Reference
## Lattice functionality in GAP: core integer-lattice methods + package ecosystem

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CORE]` | Part of core GAP functionality |
| `[PKG]` | Provided by a GAP package |
| `[ZZMOD]` | Works at the level of $\mathbb{Z}$-modules / integer matrices |
| `[EUCLID]` | Euclidean-lattice algorithmic setting |
| `[PD]` | Effectively positive-definite assumptions/setting |
| `[INDEF]` | Intended for indefinite forms/signatures |
| `[HYP]` | Hyperbolic periodic-cell workflow |
| `[POLY]` | Polyhedral / cone / affine-monoid setting |
| `[TORIC]` | Toric/lattice-point algebraic-geometry setting |
| `[FFORM]` | Finite-field forms (no real-signature definiteness notion) |
| `[GRP]` | Matrix-group action / preserved-form setting |
| `[DECOMP]` | Orthogonal decomposition or Witt-index workflow |

**Table columns:** Tags indicate domain/rigidity constraints; Source citations point to local upstream documentation.

---

## 1. Core GAP

### 1.1 Normal forms and $\mathbb{Z}$-module structure

These are lattice operations in the $\mathbb{Z}$-module sense (integer row/column modules), not quadratic-form classification methods.

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `NullspaceIntMat(mat)` | `mat`: integer matrix | `list` (list of integer vectors; basis of integral nullspace) | Returns a basis of the integral nullspace of `mat`: vectors `x` with integer entries satisfying `x * mat = 0` | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"NullspaceIntMat" |
| `SolutionIntMat(mat, vec)` | `mat`: integer matrix; `vec`: integer vector (list) | integer vector or `fail` | Returns integer vector `x` satisfying `x * mat = vec`, or `fail` if no integral solution exists | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"SolutionIntMat" |
| `SolutionNullspaceIntMat(mat, vec)` | `mat`: integer matrix; `vec`: integer vector (list) | `[solution_or_fail, nullspace_basis]` (list of 2 elements) | Combined call: first element is `SolutionIntMat(mat, vec)`, second is `NullspaceIntMat(mat)`; computed faster than two separate calls | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"SolutionNullspaceIntMat" |
| `BaseIntMat(mat)` | `mat`: integer matrix | `list` (list of integer vectors; basis of integral row module) | Returns a basis of the integral row space of `mat`: the set of integer linear combinations of the rows | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"BaseIntMat" |
| `BaseIntersectionIntMats(m, n)` | `m`, `n`: integer matrices | `list` (list of integer vectors; basis of intersection) | Returns a basis of the intersection of the integral row spaces of `m` and `n` | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"BaseIntersectionIntMats" |
| `HermiteNormalFormIntegerMat(M)` | `M`: integer matrix | `Matrix` (immutable; HNF) | Hermite normal form of `M` | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"HermiteNormalFormIntegerMat" |
| `HermiteNormalFormIntegerMatTransform(M)` | `M`: integer matrix | `record` with `.normal` (matrix H), `.rowtrans` (matrix Q s.t. Q·M = H), `.rank`, `.signdet` | Hermite normal form plus unimodular row-transformation matrix | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"HermiteNormalFormIntegerMatTransform" |
| `SmithNormalFormIntegerMat(M)` | `M`: integer matrix | `Matrix` (immutable; SNF) | Smith normal form (invariant-factor decomposition) of `M` | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"SmithNormalFormIntegerMat" |
| `SmithNormalFormIntegerMatTransforms(M)` | `M`: integer matrix | `record` with `.normal` (matrix S), `.rowtrans` (P), `.coltrans` (Q s.t. P·M·Q = S), `.rank`, `.signdet` | Smith normal form plus unimodular row and column transformation matrices | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"SmithNormalFormIntegerMatTransforms" |
| `TriangulizedIntegerMat(mat)` | `mat`: integer matrix | `Matrix` (mutable; upper triangular) | Upper-triangular form of an integer matrix; returns a new mutable matrix | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"TriangulizedIntegerMat" |
| `TriangulizedIntegerMatTransform(mat)` | `mat`: integer matrix | `record` with `.normal` (upper triangular matrix), `.rowtrans`, `.rank`, `.signdet` | Upper-triangular form plus unimodular row-transformation matrix | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"TriangulizedIntegerMatTransform" |
| `TriangulizeIntegerMat(mat)` | `mat`: mutable integer matrix | (side-effect only; modifies `mat` in-place) | Changes `mat` to upper-triangular form in-place; errors if `mat` is immutable | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"TriangulizeIntegerMat" |
| `DiagonalizeIntMat(mat)` | `mat`: mutable integer matrix | (side-effect only; modifies `mat` in-place to SNF) | Changes `mat` to its Smith normal form in-place; errors if `mat` is immutable | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"DiagonalizeIntMat" |
| `NormalFormIntMat(mat, options)` | `mat`: integer matrix; `options`: integer bitmask (bit 0: SNF vs. triangular/HNF; bit 1: reduce off-diagonal; bit 2: include row transforms; bit 3: include col transforms; bit 4 (value 16): destructive) | `record` with `.normal` (computed form), `.rank`, `.signdet`; conditionally `.rowtrans` (unimodular) and/or `.coltrans` (unimodular) | General integer normal-form computation; the workhorse routine underlying all HNF/SNF/triangular-form functions | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"NormalFormIntMat" |
| `AbelianInvariantsOfList(list)` | `list`: list of non-negative integers | `list` (sorted list: prime power factors of positive entries, plus all zeros) | Returns prime power factors of the positive invariant factors and zeros; the basis for abelian group structure | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"AbelianInvariantsOfList" |
| `ComplementIntMat(full, sub)` | `full`: integer matrix (generating module M); `sub`: integer matrix (submodule S of M) | `record` with `.complement` (vectors b_{n+1}…b_m generating complement to S), `.sub` (basis for S), `.moduli` (scaling factors x_i s.t. x_i·b_i is basis for S) | Extends the basis of S to a free basis B for M; the moduli relate S's basis to B | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"ComplementIntMat" |
| `DeterminantIntMat(mat)` | `mat`: integer matrix | `Integer` | Determinant of an integer matrix; faster than `DeterminantMat` for matrices larger than 20×20 | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"DeterminantIntMat" |
| `Decomposition(A, B, depth)` | `A`: m×n cyclotomic matrix of rank m ≤ n; `B`: list of cyclotomic vectors of length n; `depth`: non-negative integer or `"nonnegative"` (auto-computes depth, requires first column of A positive) | `list` (each entry: integer solution vector or `fail`) | For each `B[i]`, finds integer vector `x` s.t. `x * A = B[i]` via p-adic series (prime p=83); `"nonnegative"` mode asserts non-negative-integer solution and returns `fail` if none | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"Decomposition" |
| `IntegralizedMat(A[, inforec])` | `A`: cyclotomic matrix; `inforec` (optional): record from prior call (for compatible encoding of related matrix B) | `record` with `.mat` (rational matrix with cyclotomic families replaced by integral-basis columns) and `.inforec` (encoding info) | Encodes each family of algebraically conjugate columns of `A` as integer columns; output `.inforec` enables compatible encoding of other matrices | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"IntegralizedMat" |
| `DecompositionInt(A, B, depth)` | `A`: integer matrix of rank m ≤ n; `B`: integer matrix with rows of length n; `depth`: non-negative integer | `list` (each entry: integer solution vector or `fail`) | Integer-specialized version of `Decomposition`; requires `A` and `B` integral and `depth` an integer (not `"nonnegative"`) | `[CORE, ZZMOD]` | `docs/gap/upstream/matint.xml` §"DecompositionInt" |

Definiteness note:
- Not applicable here; these methods do not require a quadratic form.

### 1.2 LLL reduction

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `LLLReducedBasis([L, ]vectors[, y][, "linearcomb"][, lllout])` | `L` (optional): lattice with `ScalarProduct`; `vectors`: list of vectors; `y` (optional): rational in `(1/4,1]`, default `3/4`; `"linearcomb"` (optional): string flag; `lllout` (optional): record with `.mue`, `.B` for incremental calls | record: `.basis` (LLL-reduced basis list), `.mue`, `.B`; if `"linearcomb"`: also `.relations`, `.transformation` | LLL-reduced basis spanning the same lattice as `vectors`; if `L` given, uses `ScalarProduct(L,v,w)`; otherwise uses `ScalarProduct(v,w)` | `[CORE, EUCLID]` | `docs/gap/upstream/matint.xml` §"LLLReducedBasis" |
| `LLLReducedGramMat(G[, y])` | `G`: square symmetric integer matrix (Gram matrix); `y` (optional): rational in `(1/4,1]`, default `3/4` | record: `.remainder` (reduced Gram matrix; lower-triangular if `G` is), `.mue`, `.B`, `.relations`, `.transformation` (unimodular matrix `U` s.t. `U * G * TransposedMat(U) = .remainder`) | LLL reduction on Gram matrix, following Cohen §3.5; `.remainder` is the Gram matrix of the LLL-reduced basis | `[CORE, EUCLID]` | `docs/gap/upstream/matint.xml` §"LLLReducedGramMat" |

Definiteness note:
- LLL is an algorithmic Euclidean reduction procedure.
- When used through a Gram matrix input, interpretation depends on the provided matrix/model; this is not a full general-purpose indefinite-lattice classification API.

### 1.3 Short vectors and embedding routines

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `ShortestVectors(G, m[, "positive"])` | `G`: regular symmetric integer matrix of bilinear form; `m`: nonneg integer (norm bound); `"positive"` (optional): string flag to restrict to vectors with nonneg entries | record: `.vectors` (list of vectors `x` with `x*G*x^tr ≤ m`, one per `{x,-x}` pair), `.norms` (corresponding norm values) | Enumerate integer vectors `x` satisfying `x * G * x^tr ≤ m`; upstream requires `G` regular (nondegenerate); finite only for PD constraints | `[CORE, EUCLID, PD]` | `docs/gap/upstream/matint.xml` §"ShortestVectors" |
| `OrthogonalEmbeddings(gram[, "positive"][, maxdim])` | `gram`: symmetric PD integer matrix; `"positive"` (optional): restrict rows to nonneg entries (useful for character-table contexts); `maxdim` (optional): positive integer, maximum solution dimension to compute | record: `.vectors` (list of possible row vectors up to sign, characterized by `v * gram^{-1} * v^tr ≤ 1`), `.norms`, `.solutions` (list of index-set encodings of valid row selections) | Solve `X^tr * X = gram` over integers and encode all solutions; solutions are encoded as index lists into `.vectors` | `[CORE, EUCLID, PD]` | `docs/gap/upstream/matint.xml` §"OrthogonalEmbeddings" |

Definiteness note:
- `ShortestVectors` is mathematically finite in the standard setting only for positive-definite quadratic constraints (up to sign convention).
- `OrthogonalEmbeddings` is naturally compatible with positive-semidefinite/definite Gram constraints in the real Euclidean model.

---

## 2. Package Ecosystem

### 2.1 Crystallographic lattice stack

| Package | Role | Tags |
|---------|------|------|
| `Cryst` | Affine crystallographic groups, space-group and Wyckoff workflows | `[PKG, EUCLID, PD, GRP]` |
| `CARATInterface` | CARAT-backed class and normalizer workflows for integral matrix groups | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCat` | Catalog/index support for crystallographic classes and data | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

Representative `Cryst` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `AffineCrystGroupOnRight(S)` | Convert `S` to an affine crystallographic group with right-action convention | `[PKG, EUCLID, PD, GRP]` |
| `AsAffineCrystGroupOnRight(S)` | Coerce to right-action affine crystallographic representation when possible | `[PKG, EUCLID, PD, GRP]` |
| `IsAffineCrystGroupOnRight(S)` | Predicate for right-action affine crystallographic objects | `[PKG, EUCLID, PD, GRP]` |
| `AffineCrystGroupOnLeft(S)` | Convert `S` to an affine crystallographic group with left-action convention | `[PKG, EUCLID, PD, GRP]` |
| `PointGroup(S)` | Point-group object of crystallographic object `S` | `[PKG, EUCLID, PD, GRP]` |
| `TranslationsCrystGroup(S)` | Translation subgroup/lattice part of crystallographic object `S` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])` | Enumerate/classify space groups with point-group data `P` | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffPositions(S)` | Compute Wyckoff-position classes for space group `S` | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffOrbit(G, p)` | Return Wyckoff orbit of point `p` under group `G` | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffLattice(G, p)` | Return lattice/stabilizer data attached to Wyckoff computation at `(G, p)` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `WyckoffNormalClosure(G, p)` | Compute normal-closure object in the Wyckoff workflow for `(G, p)` | `[PKG, EUCLID, PD, GRP]` |

Representative `CARAT/Bravais` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `BravaisGroup(R)` | Compute Bravais group for matrix-group object `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `PointGroupsBravaisClass(R)` | Point-group data for the Bravais class associated to `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSubgroups(R)` | Enumerate Bravais subgroups of class/group input `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSupergroups(R)` | Enumerate Bravais supergroups of class/group input `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `NormalizerInGLnZ(R)` | Compute normalizer of the Bravais/class object `R` in `GL(n,Z)` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CentralizerInGLnZ(R)` | Compute centralizer of `R` in `GL(n,Z)` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsBravaisEquivalent(R, S)` | Decide Bravais equivalence of class/group objects `R`, `S` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClass(R)` / `CaratZClassNumber(R)` | CARAT Z-class object and class index for `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClass(R)` / `CaratQClassNumber(R)` | CARAT Q-class object and class index for `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `RationalClassesMaximalSubgroups(R)` | Rational-class maximal-subgroup representatives from input `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `ZClassRepsQClass(R)` | Z-class representatives inside the Q-class of `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `MaximalSubgroupsRepresentatives(R)` | Maximal subgroup representatives in the CARAT class workflow | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `AffineNormalizer(R)` | Affine normalizer associated with the class/group object `R` | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsCaratZClass(R)` / `IsCaratQClass(R)` | Predicates for CARAT class-object types | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

Definiteness note:
- Intrinsically Euclidean/crystallographic; not a general indefinite quadratic-lattice framework.
- For `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`, `normedQclass` is `false`
  or a normalizer-element list in `GL(d,Z)`, and `orbitsQclass` is boolean.
- Selector arguments `f`, `s`, and `k` are not treated as active canonical CARAT parameters in this surface.
- Legacy alias names `CrystCatZClass(...)`, `CrystCatQClass(...)`, and `CrystCatQClasses(...)` are triaged
  out of the active canonical method surface.
- Canonical signature anchors are maintained in:
  `docs/crystallographic_stack/lattice/research_readme.md` and
  `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`.

### 2.2 Archived out-of-scope polyhedral/toric surfaces

- The umbrella sections for `4ti2Interface`, `NormalizInterface`, `toric`, `NConvex`, and polyhedral `CddInterface`
  were moved out of active scope and archived at:
  `docs/archive/scope_violations/gap/lattice/gap_lattice_methods_reference_polyhedral_sections_2026-02-18.md`.
- Package-level archived references remain under `docs/archive/scope_violations/`.

### 2.3 Float package fplll hooks

| Function | Description | Tags |
|----------|-------------|------|
| `FPLLLReducedBasis` | fplll-backed basis reduction | `[PKG, EUCLID]` |
| `FPLLLShortestVector` | fplll-backed shortest-vector routine | `[PKG, EUCLID]` |

### 2.4 Forms package

| Package | Role | Tags |
|---------|------|------|
| `Forms` | Bilinear/sesquilinear/quadratic forms and isometry groups over finite fields | `[PKG, FFORM]` |

Representative `Forms` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `AsSesquilinearForm(obj[, field][, antiautomorphism])` / `AsQuadraticForm(obj[, field])` | Coercion constructors for sesquilinear/quadratic form objects | `[PKG, FFORM]` |
| `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])` / `QuadraticFormByMatrix(matrix[, field])` | Matrix-backed form constructors | `[PKG, FFORM]` |
| `MatrixOfSesquilinearForm(form)` / `MatrixOfQuadraticForm(form)` / `RankOfForm(form)` / `BaseField(form)` | Core structural attributes/invariants | `[PKG, FFORM]` |
| `IsometricForms(form1, form2)` / `SimilarityForms(form1, form2)` | Form equivalence checks | `[PKG, FFORM]` |
| `IsometryGroup(form)` / `SimilarityGroup(form)` | Isometry/similarity group constructors | `[PKG, FFORM]` |
| `InvariantBilinearForm(G[, involution][, isom])` / `InvariantQuadraticForm(G[, involution][, isom])` | Matrix-group invariant form extraction | `[PKG, FFORM]` |
| `PreservedSesquilinearForms(G)` / `PreservedQuadraticForms(G)` | Preserved-form families for matrix groups | `[PKG, FFORM, GRP]` |
| `OrthogonalSubgroups(G, n[, s])` / `OrthogonalSubgroupsAsList(G, n[, s])` | Orthogonal subgroup decomposition helpers | `[PKG, FFORM, DECOMP]` |
| `OrthogonalComponents(G, n)` / `OrthogonalComponentsOfSubgroup(U, n)` / `WittIndex(form)` | Orthogonal component and Witt-index workflows | `[PKG, FFORM, DECOMP]` |

Detailed method inventory is maintained in `docs/forms_methods_checklist.md` and `docs/forms/lattice/research_readme.md`.

Definiteness note:
- Real-signature PD/INDEF language is not applicable in the finite-field setting.

### 2.5 HyperCells package

| Package | Role | Tags |
|---------|------|------|
| `HyperCells` | Hyperbolic/Euclidean periodic cell-complex methods via triangle-group and supercell workflows | `[PKG, HYP, EUCLID]` |

Representative methods:

| Function | Description | Tags |
|----------|-------------|------|
| `TGCell(...)` / `TGSuperCell(...)` / `TGSuperCellModelGraph(...)` | Core constructors for primitive cells, supercells, and supercell model graphs | `[PKG, HYP, EUCLID]` |
| `HyperCell(...)` | Constructor for regular compact primitive cells in dimensions 2-4 from modified SNF data | `[PKG, HYP, EUCLID]` |
| `TGCellGraph(...)` / `TGCellModelGraph(...)` | Cell-graph and model-graph construction workflows | `[PKG, HYP, EUCLID]` |
| `IsomorphicCell(...)` / `IsomorphicCellGraph(...)` / `IsomorphicSuperCellModelGraph(...)` | Isomorphism/equivalence workflows for cells and model graphs | `[PKG, HYP, EUCLID]` |
| `TGSuperCellModelGraphQClass*`, `TGSuperCellQClass*`, `TGSuperCellModelGraphZClass*`, `TGSuperCellZClass*` | Supercell Q-class and Z-class classification/enumeration methods | `[PKG, HYP, EUCLID]` |
| `TGCellMSNFsByType*`, `TGCellModelGraphsByType*`, `TGCellGraphsByType*` | Database extraction methods by type/species/genus/length | `[PKG, HYP, EUCLID]` |
| `TGCellPointGroup*` family | Point-group representation, class, family, and genus workflows | `[PKG, HYP, EUCLID]` |

Detailed method-level inventory is maintained in `docs/hypercells_methods_checklist.md` and `docs/hypercells/lattice/research_readme.md`.

Definiteness note:
- HyperCells focuses on periodic cell-complex geometry over translation/point-group actions (Euclidean and hyperbolic regimes), not arithmetic PD-vs-INDEF genus classification contracts.

### 2.6 Subgroup lattices (terminology warning)

GAP also uses “lattice” to mean subgroup lattice (poset), which is unrelated to geometric/integer lattices and basis-reduction or Gram-matrix workflows.

---

## 3. Definiteness Regime Summary

| Area | PD / INDEF relevance |
|------|----------------------|
| Core HNF/SNF/complement methods | Not applicable (pure $\mathbb{Z}$-module algebra) |
| Core LLL methods | Euclidean algorithmic setting; not a full indefinite form-classification framework |
| Core short-vector / embedding methods | Effectively positive-definite/finite-enumeration regime |
| Cryst/CARAT/CrystCat | Euclidean crystallographic (PD setting) |
| 4ti2/Normaliz/toric/NConvex/Cdd | Archived out-of-scope polyhedral/toric surfaces |
| Forms | Finite-field forms (no real-signature definiteness notion) |
| HyperCells | Hyperbolic/Euclidean periodic cell-complex workflows; not an arithmetic genus/discriminant-form API |

---

## 4. Consolidated Method Index

### 4.1 Core GAP methods

- `AbelianInvariantsOfList`
- `BaseIntMat`
- `BaseIntersectionIntMats`
- `ComplementIntMat`
- `Decomposition`
- `DecompositionInt`
- `DeterminantIntMat`
- `DiagonalizeIntMat`
- `HermiteNormalFormIntegerMat`
- `HermiteNormalFormIntegerMatTransform`
- `IntegralizedMat`
- `LLLReducedBasis`
- `LLLReducedGramMat`
- `NormalFormIntMat`
- `NullspaceIntMat`
- `OrthogonalEmbeddings`
- `SolutionIntMat`
- `SolutionNullspaceIntMat`
- `ShortestVectors`
- `SmithNormalFormIntegerMat`
- `SmithNormalFormIntegerMatTransforms`
- `TriangulizeIntegerMat`
- `TriangulizedIntegerMat`
- `TriangulizedIntegerMatTransform`

### 4.2 Float (fplll hooks)

- `FPLLLReducedBasis`
- `FPLLLShortestVector`

### 4.3 Package names (lattice-related)

- `CARATInterface`
- `Cryst`
- `CrystCat`
- `Forms`
- `HyperCells`
- Archived out-of-scope package families: `4ti2Interface`, `CddInterface`, `NConvex`, `NormalizInterface`, `toric`
  (see `docs/archive/scope_violations/gap/lattice/gap_lattice_methods_reference_polyhedral_sections_2026-02-18.md`).

### 4.4 Cryst/CARAT methods (canonical)

- `AffineCrystGroupOnLeft`
- `AffineCrystGroupOnRight`
- `AsAffineCrystGroupOnRight`
- `AffineNormalizer`
- `BravaisGroup`
- `BravaisSubgroups`
- `BravaisSupergroups`
- `CaratQClass`
- `CaratQClassNumber`
- `CaratZClass`
- `CaratZClassNumber`
- `CentralizerInGLnZ`
- `IsAffineCrystGroupOnRight`
- `IsBravaisEquivalent`
- `IsCaratQClass`
- `IsCaratZClass`
- `MaximalSubgroupsRepresentatives`
- `PointGroup`
- `PointGroupsBravaisClass`
- `RationalClassesMaximalSubgroups`
- `NormalizerInGLnZ`
- `SpaceGroupsByPointGroupOnRight`
- `TranslationsCrystGroup`
- `WyckoffLattice`
- `WyckoffNormalClosure`
- `WyckoffOrbit`
- `WyckoffPositions`
- `ZClassRepsQClass`

### 4.5 Forms methods

- `AsSesquilinearForm`
- `AsQuadraticForm`
- `SesquilinearFormByMatrix`
- `QuadraticFormByMatrix`
- `IsSesquilinearForm`
- `IsQuadraticForm`
- `UnderlyingVectorSpace`
- `MatrixOfSesquilinearForm`
- `MatrixOfQuadraticForm`
- `RankOfForm`
- `BaseField`
- `IsReflexiveForm`
- `IsSymmetricForm`
- `IsAlternatingForm`
- `IsDegenerateForm`
- `RadicalOfForm`
- `IsometricForms`
- `SimilarityForms`
- `IsometryGroup`
- `SimilarityGroup`
- `InvariantBilinearForm`
- `InvariantQuadraticForm`
- `PreservedSesquilinearForms`
- `PreservedQuadraticForms`
- `OrthogonalSubgroups`
- `OrthogonalSubgroupsAsList`
- `OrthogonalComponents`
- `OrthogonalComponentsOfSubgroup`
- `WittIndex`

### 4.6 HyperCells methods (top-level entry points)

- `HyperCell`
- `TGCell`
- `TGCellGraph`
- `TGCellModelGraph`
- `TGSuperCell`
- `TGSuperCellModelGraph`
- `IsomorphicCell`
- `IsomorphicCellGraph`
- `IsomorphicSuperCellModelGraph`
- `TGSuperCells`
- `TGSuperCellModelGraphQClasses`
- `TGSuperCellQClasses`
- `TGSuperCellModelGraphZClasses`
- `TGSuperCellZClasses`
- `TGCellMSNFsByType`
- `TGCellMSNFsByTypeAndSpeciesAndGenus`
- `TGCellModelGraphsByType`
- `TGCellGraphsByType`
- `TGCellPointGroupReps`
- `TGCellPointGroupQClasses`
- `TGCellPointGroupZClasses`
- `TGCellPointGroupFamilies`
- `TGCellPointGroupGenera`

---

## 5. Sources

### Core GAP documentation
- Integer matrix operations (HNF, SNF, LLL): `https://www.gap-system.org/Manuals/doc/ref/chap64.html`
- Normal forms and integer linear algebra: `https://www.gap-system.org/Manuals/doc/ref/chap63.html`

### GAP packages
- Cryst package: `https://gap-packages.github.io/cryst/`
- CARATInterface: `https://gap-packages.github.io/carat/`
- CrystCat: `https://gap-packages.github.io/crystcat/`
- Forms package: `https://gap-packages.github.io/forms/`
- HyperCells package: `https://gap-packages.github.io/hypercells/`

### Local upstream snapshots
- Core integer matrices: `docs/gap/upstream/matint.gd`, `docs/gap/upstream/matint.gi`
- GAP integer matrix docs: `docs/gap/upstream/matint.xml`
- GAP manual chapters 24-26: `docs/gap/upstream/chap24.html`, `docs/gap/upstream/chap25.html`, `docs/gap/upstream/chap26.html`
- Crystallographic packages: `docs/crystallographic_stack/upstream/cryst/`, `docs/crystallographic_stack/upstream/caratinterface/`, `docs/crystallographic_stack/upstream/crystcat/`
- HyperCells: `docs/hypercells/upstream/`
- Forms: `docs/forms/lattice/research_readme.md`
