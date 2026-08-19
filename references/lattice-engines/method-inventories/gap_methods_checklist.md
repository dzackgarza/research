# GAP Method Test Gap Checklist

Tracks GAP-relevant lattice methods documented in `docs/gap/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core GAP

### 1.1 Integer-module normal forms and structure

- [x] `NullspaceIntMat(mat)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_nullspace_finds_integer_relation]
- [x] `SolutionIntMat(mat, vec)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_solutionintmat_solves_integral_linear_system]
- [x] `SolutionNullspaceIntMat(mat, vec)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_solutionnullspace_returns_solution_and_kernel_basis]
- [x] `BaseIntMat(mat)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_baseintmat_produces_basis_of_row_module]
- [x] `BaseIntersectionIntMats(m, n)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_baseintersection_returns_expected_sublattice]
- [x] `HermiteNormalFormIntegerMat(M)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_hnf_recovers_expected_diagonal_form]
- [x] `HermiteNormalFormIntegerMatTransform(M)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_hnf_transform_normal_matches_hnf_and_rank]
- [x] `SmithNormalFormIntegerMat(M)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_snf_returns_invariant_factor_diagonal]
- [x] `SmithNormalFormIntegerMatTransforms(M)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_snf_transforms_include_correct_rank_and_normal]
- [ ] `TriangulizedIntegerMat(mat)`
- [ ] `TriangulizedIntegerMatTransform(mat)`
- [ ] `TriangulizeIntegerMat(mat)`
- [ ] `DiagonalizeIntMat(mat)`
- [ ] `NormalFormIntMat(mat, options)`
  - Caveat: `options` is an integer bitmask (0–31): bit 0 selects SNF vs. triangular/HNF, bit 1 reduces off-diagonal, bit 2 adds row transforms, bit 3 adds col transforms, bit 4 (value 16) is destructive; returns a record with `normal`, optionally `rowtrans`/`coltrans`, `signdet`, `rank`. [source: docs/gap/upstream/matint.gd §NormalFormIntMat]
- [ ] `AbelianInvariantsOfList(list)`
- [x] `ComplementIntMat(full, sub)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_complementintmat_returns_direct_summand_data]
- [x] `DeterminantIntMat(mat)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_determinantintmat_matches_exact_determinant]
- [ ] `Decomposition(A, B, depth)`
  - Caveat: `A` must be an m×n cyclotomic matrix of rank m ≤ n; `B` is a list of cyclotomic vectors of length n; `depth` is a nonneg integer or `"nonnegative"` (assumes nonneg solutions, auto-computes iterations, fails per entry if no nonneg solution); p=83 by default, auto-advanced if singular. [source: docs/gap/upstream/chap25.html §25.4-1]
- [ ] `IntegralizedMat(A[, inforec])`
- [ ] `DecompositionInt(A, B, depth)`

### 1.2 LLL and Euclidean search

- [x] `LLLReducedBasis(...)` [test: tests/gap_doc/test_gap_core_static.py::test_gap_lll_reduced_basis_preserves_smith_normal_form]
- [x] `LLLReducedGramMat(G[, y])` [test: tests/gap_doc/test_gap_core_static.py::test_gap_lll_reduced_gram_returns_conjugate_remainder]
- [x] `ShortestVectors(G, m[, "positive"])` [test: tests/gap_doc/test_gap_core_static.py::test_gap_shortestvectors_finds_minimal_shell]
  - Caveat: finite enumeration contracts are in the positive-definite Euclidean regime.
- [x] `OrthogonalEmbeddings(gram[, "positive"][, maxdim])` [test: tests/gap_doc/test_gap_core_static.py::test_gap_orthogonal_embeddings_identity_gram_has_standard_solution]
  - Caveat: Euclidean embedding workflow, not a general indefinite classification API.

---

## 2. GAP Package Ecosystem

### 2.1 Package load surfaces (checklist anchor)

- [ ] `LoadPackage("Cryst")`
- [ ] `LoadPackage("CARATInterface")`
- [ ] `LoadPackage("CrystCat")`
- [ ] `LoadPackage("Forms")`
- [ ] `LoadPackage("HyperCells")`

### 2.2 Cryst/CARAT/CrystCat (canonical)

- [ ] `AffineCrystGroupOnRight(S)`
- [ ] `AsAffineCrystGroupOnRight(S)`
- [ ] `IsAffineCrystGroupOnRight(S)`
- [ ] `AffineCrystGroupOnLeft(S)`
- [ ] `PointGroup(S)`
- [ ] `TranslationsCrystGroup(S)`
- [ ] `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`
- [ ] `WyckoffPositions(S)`
- [ ] `WyckoffOrbit(G, p)`
- [ ] `WyckoffLattice(G, p)`
- [ ] `WyckoffNormalClosure(G, p)`
- [ ] `BravaisGroup(R)`
- [ ] `PointGroupsBravaisClass(R)`
- [ ] `BravaisSubgroups(R)`
- [ ] `BravaisSupergroups(R)`
- [ ] `NormalizerInGLnZ(R)`
- [ ] `CentralizerInGLnZ(R)`
- [ ] `IsBravaisEquivalent(R, S)`
- [ ] `CaratZClass(R)`
- [ ] `CaratZClassNumber(R)`
- [ ] `CaratQClass(R)`
- [ ] `CaratQClassNumber(R)`
- [ ] `RationalClassesMaximalSubgroups(R)`
- [ ] `ZClassRepsQClass(R)`
- [ ] `MaximalSubgroupsRepresentatives(R)`
- [ ] `AffineNormalizer(R)`
- [ ] `IsCaratZClass(R)`
- [ ] `IsCaratQClass(R)`
  - Caveat: crystallographic Euclidean setting, not indefinite arithmetic-lattice classification.
  - Caveat: `normedQclass` is `false` or a normalizer-element list in `GL(d,Z)`; `orbitsQclass` is boolean.
  - Caveat: selector arguments `f`, `s`, and `k` are not treated as active canonical parameters.
  - Legacy aliases triaged out of active canonical surface: `CrystCatZClass(...)`, `CrystCatQClass(...)`, `CrystCatQClasses(...)`.

### 2.3 Archived Out-of-Scope Polyhedral/Toric Surfaces

- Archived umbrella sections for `4ti2Interface`, `NormalizInterface`, `toric`, `NConvex`, and polyhedral `CddInterface` are maintained in:
  `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`.
- Package-level archived checklists remain available under `docs/archive/scope_violations/`.

### 2.4 Forms package (detailed checklist surface)

- [ ] `AsSesquilinearForm(obj[, field][, antiautomorphism])`
- [ ] `AsQuadraticForm(obj[, field])`
- [ ] `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])`
- [ ] `QuadraticFormByMatrix(matrix[, field])`
- [ ] `IsometricForms(form1, form2)`
- [ ] `SimilarityForms(form1, form2)`
- [ ] `PreservedSesquilinearForms(G)`
- [ ] `PreservedQuadraticForms(G)`
- [ ] `OrthogonalSubgroups(G, n[, s])`
- [ ] `WittIndex(form)`
  - Caveat: finite-field form workflow; characteristic and irreducibility assumptions are documented in `docs/forms_methods_checklist.md`.

### 2.5 fplll hooks exposed in GAP

- [ ] `FPLLLReducedBasis(...)`
- [ ] `FPLLLShortestVector(...)`

---

## References

- `docs/gap/lattice/research_readme.md`
- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/lattice/research_readme.md`
- `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`
- `docs/archive/scope_violations/cddinterface_methods_checklist.md`
- `docs/forms_methods_checklist.md`
- `docs/hypercells_methods_checklist.md`
- GAP docs hub: `https://www.gap-system.org/doc/`
- GAP package index: `https://gap-packages.github.io`
- GAP Cryst package manual: `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP Reference Manual (CARAT methods): `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual: `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
- HyperCells package page: `https://gap-packages.github.io/HyperCells/`
- Forms package page: `https://gap-packages.github.io/forms/`
- Forms manual: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
