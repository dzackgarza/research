# cddlib Lattice Method Reference (Archived Scope Violation)
## Exact H/V polyhedral conversion and LP C API surface

Archived under `docs/archive/scope_violations/` because this surface is polyhedral/LP-focused and outside this project's bilinear-form lattice-theory scope.

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[CAPI]` | C API function surface |
| `[POLY]` | Polyhedral/cone representation workflow |
| `[HREP]` | Halfspace representation surface |
| `[VREP]` | Generator representation surface |
| `[LP]` | Linear-programming surface |
| `[EXACT]` | Exact arithmetic pathway |

---

## 1. Scope

`cddlib` is an exact-arithmetic polyhedral stack for:

- H-representation <-> V-representation conversion,
- redundancy removal and canonicalization,
- adjacency/incidence extraction,
- LP workflows.

Not in scope:

- indefinite arithmetic-form genus/isometry classification methods.

---

## 2. Core CLI Surface

| Command | Synopsis | Contract | Tags |
|---|---|---|---|
| `cdd` | `cdd [filename]` | Core file-driven H/V conversion and polyhedral processing command. | `[CLI, POLY, HREP, VREP, EXACT]` |
| `cddr+` | `cddr+ [filename]` | Floating-point LP variant command in the cdd family. | `[CLI, POLY, LP]` |
| C API equivalent | `dd_DDFile2File(infile, outfile)` | Programmatic file-to-file conversion entry point used by CLI-style workflows. | `[CAPI, POLY, HREP, VREP, EXACT]` |

Documented cdd output/processing keyword surfaces include:

- `adjacency`, `incidence`,
- `input_adjacency`, `input_incidence`,
- `redundant`, `nonredundant`, `explicit`.

---

## 3. C API: Representation Construction and Conversion

| API | Signature | Description | Tags |
|---|---|---|---|
| `dd_PolyFile2Matrix` | `dd_PolyFile2Matrix(infile, &myErr)` | Parse polyhedral input file into matrix representation object. | `[CAPI, POLY, HREP, VREP, EXACT]` |
| `dd_DDMatrix2Poly` | `dd_DDMatrix2Poly(myMatrix, &myErr)` | Build polyhedron object from matrix representation. | `[CAPI, POLY, HREP, VREP, EXACT]` |
| `dd_DDMatrix2Poly2` | `dd_DDMatrix2Poly2(myMatrix, &myErr)` | Alternate matrix-to-polyhedron conversion pathway documented in cddlib API docs. | `[CAPI, POLY, HREP, VREP, EXACT]` |
| `dd_DDInputAppend` | `dd_DDInputAppend(&myMatrix, myrow)` | Append an input row to matrix representation before conversion/analysis. | `[CAPI, POLY, HREP, VREP]` |

---

## 4. C API: Adjacency and Incidence

| API | Signature | Description | Tags |
|---|---|---|---|
| `dd_DDInputAdjacency` | `dd_DDInputAdjacency(myMatrix)` | Compute adjacency data for input representation. | `[CAPI, POLY, HREP, VREP]` |
| `dd_DDInputIncidence` | `dd_DDInputIncidence(myMatrix)` | Compute incidence data for input representation. | `[CAPI, POLY, HREP, VREP]` |
| `dd_DDInputToAdjacency` | `dd_DDInputToAdjacency(myMatrix)` | Convert input representation into adjacency form. | `[CAPI, POLY, HREP, VREP]` |
| `dd_DDInputToIncidence` | `dd_DDInputToIncidence(myMatrix)` | Convert input representation into incidence form. | `[CAPI, POLY, HREP, VREP]` |
| `dd_DDMatrix2Adjacency` | `dd_DDMatrix2Adjacency(myMatrix, &myErr)` | Matrix-level adjacency extraction with error reporting. | `[CAPI, POLY, HREP, VREP]` |
| `dd_DDMatrix2WeakAdjacency` | `dd_DDMatrix2WeakAdjacency(myMatrix, &myErr)` | Weak-adjacency extraction variant. | `[CAPI, POLY, HREP, VREP]` |

---

## 5. C API: Canonicalization and Matrix Operations

| API | Signature | Description | Tags |
|---|---|---|---|
| `dd_DDMatrixCanonicalize` | `dd_DDMatrixCanonicalize(&myMatrix, &impl_linset, &redset, &newpos, &myErr)` | Canonicalize matrix representation and compute implied linearity/redundancy information. | `[CAPI, POLY, HREP, VREP, EXACT]` |
| `dd_MatrixCanonicalize` | `dd_MatrixCanonicalize(&myMatrix, &impl_linset, &redset, &newpos)` | Canonicalize matrix without explicit error handle argument in this signature form. | `[CAPI, POLY, HREP, VREP, EXACT]` |
| `dd_MatrixRedundancyRemove` | `dd_MatrixRedundancyRemove(&M, &redset, &newpos)` | Remove redundant rows and produce position mapping data. | `[CAPI, POLY, HREP, EXACT]` |
| `dd_RedundantRows` | `dd_RedundantRows(M, A, &redset)` | Identify redundant rows relative to matrix/set context. | `[CAPI, POLY, HREP]` |
| `dd_SRedundantRows` | `dd_SRedundantRows(M, A, &redset)` | Strong-redundancy test variant. | `[CAPI, POLY, HREP]` |
| `dd_MatrixRank` | `dd_MatrixRank(M, &r, &ignoredrows, &basisrows)` | Compute matrix rank with ignored-row and basis-row outputs. | `[CAPI, POLY, EXACT]` |
| `dd_MatrixAppendTo` | `dd_MatrixAppendTo(&M1, M2)` | Append matrix `M2` rows into `M1`. | `[CAPI, POLY]` |
| `dd_MatrixNormalizedCopy` | `dd_MatrixNormalizedCopy(M)` | Copy matrix after normalization rules in cddlib matrix model. | `[CAPI, POLY, EXACT]` |
| `dd_MatrixCopy` | `dd_MatrixCopy(M)` | Plain matrix copy constructor in C API. | `[CAPI, POLY]` |
| `dd_MatrixSubmatrix` | `dd_MatrixSubmatrix(M, delset)` | Submatrix extraction by row-deletion set. | `[CAPI, POLY]` |

---

## 6. C API: Linear Programming

| API | Signature | Description | Tags |
|---|---|---|---|
| `dd_Matrix2LP` | `dd_Matrix2LP(M, &err)` | Build LP object from matrix representation. | `[CAPI, LP, POLY]` |
| `dd_LPSolve` | `dd_LPSolve(lp, solver, &err)` | Solve LP with selected solver backend parameter. | `[CAPI, LP]` |
| `dd_LPSolve0` | `dd_LPSolve0(lp, solver, &err)` | Alternate LP solve entry point documented alongside `dd_LPSolve`. | `[CAPI, LP]` |

---

## 7. Assumptions and Constraints

- The cddlib manual signatures use symbolic placeholders (`myMatrix`, `myErr`, `redset`, etc.) that correspond to cddlib internal C pointer/set structures.
- Representation-dependent APIs require correctly formed H-rep or V-rep matrix input and related metadata.
- This surface is for polyhedral/exact LP computations and does not define indefinite-lattice genus/isometry semantics.

---

## 8. Sources

- cddlib repository: `https://github.com/cddlib/cddlib`
- cddlib manual index: `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node1.html`
- cddlib command/API manual pages:
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node2.html`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node5.html`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node6.html`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node7.html`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node8.html`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node10.html`
