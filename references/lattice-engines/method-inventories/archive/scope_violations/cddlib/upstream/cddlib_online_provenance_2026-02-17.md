# cddlib Online Provenance Snapshot (2026-02-17 UTC)

Archived from active scope under `docs/archive/scope_violations/`.

Scope: first-class checklist/reference creation for the missing `cddlib` package surface.

---

## 1. Sources surveyed

Canonical package pages:

- `https://github.com/cddlib/cddlib`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node1.html`

Canonical cddlib manual pages used for method extraction:

- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node2.html`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node5.html`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node6.html`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node7.html`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node8.html`
- `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node10.html`

---

## 2. Extracted method surface

From the command and C API pages:

- CLI/driver surface:
  - `cdd [filename]`
  - `cddr+ [filename]`
  - `dd_DDFile2File(infile, outfile)` (programmatic file-to-file driver)
- Representation and conversion:
  - `dd_PolyFile2Matrix(infile, &myErr)`
  - `dd_DDMatrix2Poly(myMatrix, &myErr)`
  - `dd_DDMatrix2Poly2(myMatrix, &myErr)`
  - `dd_DDInputAppend(&myMatrix, myrow)`
- Adjacency/incidence:
  - `dd_DDInputAdjacency`, `dd_DDInputIncidence`
  - `dd_DDInputToAdjacency`, `dd_DDInputToIncidence`
  - `dd_DDMatrix2Adjacency`, `dd_DDMatrix2WeakAdjacency`
- Canonicalization/redundancy/matrix operations:
  - `dd_DDMatrixCanonicalize`, `dd_MatrixCanonicalize`
  - `dd_MatrixRedundancyRemove`, `dd_RedundantRows`, `dd_SRedundantRows`
  - `dd_MatrixRank`, `dd_MatrixAppendTo`, `dd_MatrixNormalizedCopy`, `dd_MatrixCopy`, `dd_MatrixSubmatrix`
- LP functions:
  - `dd_Matrix2LP`, `dd_LPSolve`, `dd_LPSolve0`

---

## 3. Constraint notes captured

- Command/API surfaces are polyhedral and exact-arithmetic oriented (H/V conversion, redundancy, incidence/adjacency, LP).
- Manual signatures are documented with symbolic argument names (for example `myMatrix`, `myErr`) that correspond to cddlib internal pointer/set structures.
- No source-backed contract in these docs indicates indefinite-form genus/isometry classification semantics.
