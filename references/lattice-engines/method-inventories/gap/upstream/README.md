# GAP Upstream Documentation — Local Copies

Fetched: 2026-02-18

## Sources

- **GitHub repo**: https://github.com/gap-system/gap
- **Online docs**: https://docs.gap-system.org/doc/ref/

## Files

### HTML Reference Manual Chapters
| File | Chapter | Description |
|------|---------|-------------|
| `chap24.html` | 24 — Matrices | General matrix operations, `DeterminantMat`, `TransposedMat`, `InverseMatMod`, etc. |
| `chap25.html` | 25 — Integral Matrices and Lattices | **Core lattice chapter**: HNF, SNF, `NormalFormIntMat`, `NullspaceIntMat`, `SolutionIntMat`, `BaseIntersectionIntMats`, `ShortestVectors`, `OrthogonalEmbeddings`, `Decomposition` |
| `chap26.html` | 26 — Vector and Matrix Objects | MatObj API, vector/matrix object interface |

### XML Doc Sources (from `doc/ref/`)
| File | Content |
|------|---------|
| `matint.xml` | Integral matrices & lattices doc markup |
| `matrix.xml` | General matrix operations doc markup |
| `integers.xml` | Integer arithmetic doc markup |
| `matobj.xml` | Vector/matrix objects doc markup |
| `grpmat.xml` | Matrix groups doc markup |
| `numtheor.xml` | Number theory functions |
| `orders.xml` | Orders and orderings |
| `cyclotom.xml` | Cyclotomic numbers |
| `combinat.xml` | Combinatorics |

### GAP Library Source (from `lib/`)
| File | Content |
|------|---------|
| `matint.gd` | Declarations for integral matrix operations (19 KB) |
| `matint.gi` | Implementations for integral matrix operations (30 KB) |

## Key APIs for Lattice Interface (from chap25)

### 25.1 — Linear Equations over Integers
- `NullspaceIntMat(mat)` — integral nullspace basis
- `SolutionIntMat(mat, vec)` — integer solution to x·mat = vec
- `SolutionNullspaceIntMat(mat, vec)` — solution + nullspace
- `BaseFixedPointRingByTriangulation(mat)` — fixed-point subring basis
- `BaseIntersectionIntMats(m, n)` — intersection of row spaces
- `ComplementIntMat(full, sub)` — complement sublattice

### 25.2 — Normal Forms
- `TriangulizedIntegerMat(mat)` / `TriangulizeIntegerMat(mat)` — upper triangular form
- `TriangulizedIntegerMatTransform(mat)` — with transformation matrix
- `HermiteNormalFormIntegerMat(mat)` — Hermite normal form
- `HermiteNormalFormIntegerMatTransform(mat)` — HNF with Q s.t. Q·A = H
- `SmithNormalFormIntegerMat(mat)` — Smith normal form
- `SmithNormalFormIntegerMatTransforms(mat)` — SNF with P,Q s.t. P·A·Q = S
- `DiagonalizeIntMat(mat)` — in-place SNF
- `NormalFormIntMat(mat, options)` — general workhorse (options bitmask: 0/1=tri/SNF, 2=reduce, 4=rowQ, 8=colQ, 16=destructive)

### 25.3 — Determinant
- `DeterminantIntMat(mat)` — integer determinant via normal form

### 25.4 — Decompositions
- `Decomposition(A, B, depth)` — p-adic decomposition

### 25.5 — Lattice Bases
- `LLLReducedBasis(L)` — LLL-reduced basis
- `LLLReducedGramMat(G)` — LLL on Gram matrix

### 25.6 — Orthogonal Embeddings
- `OrthogonalEmbeddings(gram)` — find orthogonal embeddings
- `ShortestVectors(G, m)` — vectors with norm ≤ m
