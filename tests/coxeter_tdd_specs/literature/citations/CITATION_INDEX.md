# Citation Index

## Mathematical Facts → Source Files

### Matrix Relationships
- **Schläfli Matrix Formula**: `C_ij = -2 cos(π/M_ij)`
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_from_coxeter_type_A2`

### Classification Theorems
- **Eigenvalue Classification**:
  - All negative → finite type
  - All non-negative (≥1 zero) → affine type  
  - Some positive → hyperbolic type
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_eigenvalue_calculation`

- **Signature Classification**:
  - (0,n,0) → finite type
  - (0,n-1,1) → affine type
  - (p,q,0) with p≥1 → hyperbolic type
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_signature_classification`

### Mathematical Conventions
- **Gram Matrix Symmetry**: Inherent from inner product definition
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_symmetric_matrix_validation`

### Literature Examples
- **A2 Triangle Group**: Gram matrix [[-2,1],[1,-2]], determinant 3
  - Source: `research/wikiwand/coxeter_schlaefli_matrices.md`
  - Tests: `tests/unit/test_gram_matrices.py::test_wikiwand_triangle_example`

### Zariski Density Theory
- **Limit Set Characterization**: Zariski dense iff limit set not in hypersphere
  - Source: `research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md`
  - Tests: (To be added in system tests)

## Source Files → Mathematical Facts

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