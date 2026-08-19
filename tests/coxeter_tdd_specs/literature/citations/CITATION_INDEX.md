# Citation Index

## Mathematical Facts → Source Files

### Matrix Relationships
- **Schläfli matrix** (literature convention): `C_ij = -2 cos(π/M_ij)`
  - Diagonal `C_ii = -2 cos(π) = 2`; an edge of order 3 gives `-2 cos(π/3) = -1`
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md`
- **Gram matrix** (project convention): `B_ij = 2 cos(π/M_ij) = -C_ij`
  - `B` is the negative of the Schläfli matrix; equivalently `B = -2 G`, where `G` is the
    Gram matrix of unit mirror normals, `G_ij = -cos(π/M_ij)`
  - Source: `PROJECT_CONVENTIONS.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_from_coxeter_type_A2`

### Classification Theorems

Every row below is stated for the **project convention** matrix `B = -C`, which is what the
tests assert against. The literature statement is the same row with all signs reversed.

- **Eigenvalue classification** (eigenvalues of `B`, project convention):
  - all negative → finite (elliptic) type
  - all non-positive with at least one zero → affine (parabolic) type
  - exactly one positive and the rest negative, none zero → hyperbolic (Lorentzian) type
  - at least two positive and at least one negative → indefinite of higher signature,
    which is not hyperbolic
  - Literature convention (`C`): all positive → finite; all non-negative with at least one
    zero → affine; exactly one negative and the rest positive → hyperbolic.
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md` (stated there in the
    literature convention), `PROJECT_CONVENTIONS.md` (the negation)
  - Tests: `tests/unit/test_gram_matrices.py::test_A2_eigenvalue_calculation`

- **Signature classification** — signature `(p, q, r)` of `B` counts positive, negative and
  zero eigenvalues, with rank `n = p + q + r`:
  - `(0, n, 0)` → finite type
  - `(0, n-1, 1)` → affine type
  - `(1, n-1, 0)` → hyperbolic (Lorentzian) type
  - `p ≥ 2` and `q ≥ 1` → indefinite, of higher signature than Lorentzian
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`,
    `PROJECT_CONVENTIONS.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_signature_classification`

- **Determinant of the Schläfli matrix**: the sign of `det C` classifies the type only in
  rank ≤ 2, where the determinant is the product of the two eigenvalues; `det C = 0` detects
  a radical in any rank. In rank 4 a form of signature (2,2) has `det C > 0` and is
  indefinite, so the unrestricted determinant rule is false.
  - Source: `research/wikipedia/coxeter_dynkin_diagrams.md` (the rank restriction is stated
    in the article this extract was distilled from)
  - Tests: `tests/unit/test_gram_matrices.py::test_zero_determinant_affine`

### Mathematical Conventions
- **Gram Matrix Symmetry**: Inherent from inner product definition
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_symmetric_matrix_validation`

### Literature Examples
- **A2 Triangle Group**: Coxeter matrix M = [[1,3],[3,1]]
  - Literature Schläfli matrix C = [[2,-1],[-1,2]], eigenvalues 1 and 3, det 3
  - Project Gram matrix B = -C = [[-2,1],[1,-2]], eigenvalues -1 and -3, det 3
    (the determinants agree because the rank is even)
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md` (M and C),
    `PROJECT_CONVENTIONS.md` (B = -C)
  - Tests: `tests/unit/test_gram_matrices.py::test_wikiwand_triangle_example`

### Zariski Density Theory
- **Limit Set Characterization**: Zariski dense iff limit set not in hypersphere
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`
  - Tests: (To be added in system tests)

## Source Files → Mathematical Facts

Paths written `research/<dir>/<file>.md` in this index and in the `# CITATION:` comments of
the test corpus resolve in-tree to `tests/coxeter_tdd_specs/literature/<dir>/<file>.md`.

### `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`
**Key Results**:
1. Zariski density characterization via limit sets
2. Eigenvalue classification of Coxeter groups
3. Signature-based type classification
4. Thin group enumeration theorems
5. Vinberg algorithm produces infinite sequences

**Test Coverage**:
- Eigenvalue classification tests
- Signature classification tests
- Zariski density tests (planned)

### `research/wikiwand/coxeter_schlaefli_matrices.md`
**Key Results**:
1. Coxeter-Schläfli matrix relationship: C_ij = -2 cos(π/M_ij)
2. A2 triangle example with specific matrices
3. Symmetry properties of Gram matrices
4. Eigenvalue classification criteria

**Test Coverage**:
- A2 construction tests
- Matrix symmetry validation
- Coxeter-Schläfli formula tests (planned)

### `research/wikipedia/coxeter_groups_overview.md`
**Key Results**:
1. Complete finite type classification (An, Bn, Dn, exceptional)
2. Affine type enumeration
3. Hyperbolic type existence
4. Application domains

**Test Coverage**:
- Classification tests (planned)
- Finite-type orders: `system/test_literature_examples.py` (via
  `research/wikipedia/finite_coxeter_group_invariants.md`)

### `research/wikipedia/coxeter_dynkin_diagrams.md`
**Key Results**:
1. Type classification by the signature of the Schläfli matrix
2. Determinant criterion, valid in rank ≤ 2 (and the zero case in every rank)
3. Compact (Lannér) and paracompact (Koszul) hyperbolic subdivision
4. Diagram notation conventions

**Test Coverage**:
- `system/test_classification_examples.py` (finite/affine/hyperbolic examples)

### `research/wikipedia/finite_coxeter_group_invariants.md`
**Key Results**:
1. Rank, bracket notation, reflection count, Coxeter number, order and group structure of
   every finite irreducible Coxeter group
2. B_n and C_n share a Coxeter group
3. Which finite Coxeter groups are not Weyl groups

**Test Coverage**:
- `system/test_literature_examples.py::test_wikiwand_bracket_notation_examples`
- `system/test_literature_examples.py::test_wikipedia_weyl_group_isomorphisms`
- `system/test_literature_examples.py::test_dynkin_diagram_invariant_recovery`

### `research/wikipedia/schlaefli_determinants_by_family.md`
**Key Results**:
1. Rank-2 Schläfli matrices and determinants, det C = 4 sin²(π/p)
2. Schläflian by rank per family: det A_n = n+1, det B_n = 2, det D_n = 4, det E_n = 9-n,
   det F_n = 5-n, det G_n = 3-n
3. Where each extended series turns affine, hyperbolic and Lorentzian (E_9, E_10, E_11)
4. Compact and paracompact hyperbolic subdivision

**Test Coverage**:
- `unit/test_gram_matrices.py::test_zero_determinant_affine` (the p = ∞ rank-2 row)
- The rank-2 table supplies the specimen `test_hyperbolic_negative_determinant` still lacks
- Higher-rank rows: oracle for a Schläfli-matrix method not yet implemented
- Type enumeration tests (planned)

## Test Files → Citations Used

### `tests/unit/test_gram_matrices.py`
**Citations**:
1. `research/wikiwand/coxeter_schlaefli_matrices.md` (4 tests)
2. `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md` (2 tests)

**Mathematical Facts Tested**:
- A2 Gram matrix construction
- Eigenvalue classification
- Signature classification  
- Matrix symmetry validation
- Literature example verification

## Citation Coverage Statistics

### By Source Type
- Research Papers: 1 file, 2 test citations
- Wikiwand Articles: 1 file, 4 test citations  
- Wikipedia Articles: 1 file, 0 test citations

### By Mathematical Domain
- Linear Algebra: 6 citations
- Group Theory: 2 citations
- Classification Theory: 2 citations

### Implementation Status
- ✅ Unit tests with citations: 6 tests
- 🔄 Integration tests: 0 tests (planned)
- 🔄 System tests: 0 tests (planned)
- 🔄 Sage verification: 0 tests (planned)

## Missing Citations (TODO)

### High Priority
1. Complete finite type classification tests
2. Affine type characterization tests  
3. Hyperbolic type existence tests
4. Vinberg algorithm correctness tests

### Medium Priority
1. Bourbaki convention verification
2. Dynkin diagram relationships
3. Root system constructions
4. Weyl group properties

### Low Priority  
1. Historical context validation
2. Alternative notation systems
3. Performance characteristics
4. Computational complexity