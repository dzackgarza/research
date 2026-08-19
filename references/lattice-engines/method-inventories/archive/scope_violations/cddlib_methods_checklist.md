# cddlib Method Test Gap Checklist (Archived Scope Violation)

Archived from active scope. Tracks cddlib polyhedral methods documented in
`docs/archive/scope_violations/cddlib/lattice/cddlib_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core CLI Surface

- [ ] `cdd [filename]`
- [ ] `cddr+ [filename]`
- [ ] `dd_DDFile2File(infile, outfile)`

## 2. C API: Polyhedron Construction and Representation Conversion

- [ ] `dd_PolyFile2Matrix(infile, &myErr)`
- [ ] `dd_DDMatrix2Poly(myMatrix, &myErr)`
- [ ] `dd_DDMatrix2Poly2(myMatrix, &myErr)`
- [ ] `dd_DDInputAppend(&myMatrix, myrow)`

## 3. C API: Adjacency and Incidence Surface

- [ ] `dd_DDInputAdjacency(myMatrix)`
- [ ] `dd_DDInputIncidence(myMatrix)`
- [ ] `dd_DDInputToAdjacency(myMatrix)`
- [ ] `dd_DDInputToIncidence(myMatrix)`
- [ ] `dd_DDMatrix2Adjacency(myMatrix, &myErr)`
- [ ] `dd_DDMatrix2WeakAdjacency(myMatrix, &myErr)`

## 4. C API: Canonicalization and Matrix Operations

- [ ] `dd_DDMatrixCanonicalize(&myMatrix, &impl_linset, &redset, &newpos, &myErr)`
- [ ] `dd_MatrixCanonicalize(&myMatrix, &impl_linset, &redset, &newpos)`
- [ ] `dd_MatrixRedundancyRemove(&M, &redset, &newpos)`
- [ ] `dd_RedundantRows(M, A, &redset)`
- [ ] `dd_SRedundantRows(M, A, &redset)`
- [ ] `dd_MatrixRank(M, &r, &ignoredrows, &basisrows)`
- [ ] `dd_MatrixAppendTo(&M1, M2)`
- [ ] `dd_MatrixNormalizedCopy(M)`
- [ ] `dd_MatrixCopy(M)`
- [ ] `dd_MatrixSubmatrix(M, delset)`

## 5. C API: LP Surface

- [ ] `dd_Matrix2LP(M, &err)`
- [ ] `dd_LPSolve(lp, solver, &err)`
- [ ] `dd_LPSolve0(lp, solver, &err)`

## 6. CLI Output-Keyword Surface

- [ ] `adjacency`
- [ ] `incidence`
- [ ] `input_adjacency`
- [ ] `input_incidence`
- [ ] `redundant`
- [ ] `nonredundant`
- [ ] `explicit`

---

## Domain Caveats

- cddlib is an exact polyhedral H/V conversion, redundancy, adjacency/incidence, and LP stack.
- It is not an arithmetic indefinite-lattice genus/isometry classification API.

---

## References

- `docs/archive/scope_violations/cddlib/lattice/cddlib_lattice_reference.md`
- `docs/archive/scope_violations/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`
- cddlib repository: `https://github.com/cddlib/cddlib`
- cddlib manual index: `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node1.html`
