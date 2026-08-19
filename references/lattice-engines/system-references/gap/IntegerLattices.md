# GAP Integer Lattices Documentation

Complete reference for lattice functions in GAP (Chapter 25: Integral matrices and lattices).

## Basis & Kernel

```gap
NullspaceIntMat(mat: Matrix) -> list[Vector]
```
Integral nullspace of integer matrix. Returns basis of vectors with integral entries in ker(mat).

```gap
BaseIntMat(mat: Matrix) -> list[Vector]
```
Integral row space basis of integer matrix.

```gap
BaseIntersectionIntMats(m: Matrix, n: Matrix) -> list[Vector]
```
Basis of intersection of integral row spaces of m and n.

---

## Linear System Solving

```gap
SolutionIntMat(mat: Matrix, vec: Vector) -> Vector | fail
```
Solution x to x*mat = vec with integer entries. Returns fail if no solution exists.

```gap
ComplementIntMat(full: list[Vector], sub: list[Vector]) -> record
```
Extends submodule basis S to full module M. Returns record with:
- `complement` – vectors generating complement to S
- `sub` – basis vectors for S  
- `moduli` – factors x_i

---

## Normal Forms

```gap
TriangulizedIntegerMat(mat: Matrix) -> Matrix
```
Upper triangular form of integer matrix (mutable).

```gap
HermiteNormalFormIntegerMat(mat: Matrix) -> Matrix
```
Hermite Normal Form (immutable).

```gap
HermiteNormalFormIntegerMatTransform(mat: Matrix) -> record
```
HNF with transformation. Returns record:
- `normal` – matrix H in HNF
- `rowtrans` – matrix Q where Q*A = H

```gap
SmithNormalFormIntegerMat(mat: Matrix) -> Matrix
```
Smith Normal Form (immutable).

```gap
SmithNormalFormIntegerMatTransforms(mat: Matrix) -> record
```
SNF with transformations. Returns record:
- `normal` – matrix S in SNF
- `rowtrans` – matrix P
- `coltrans` – matrix Q
where P*A*Q = S

```gap
DiagonalizeIntMat(mat: Matrix) -> void
```
Transform mat in-place to SNF (destructive). Modifies mat, uses less memory.

```gap
NormalFormIntMat(mat: Matrix, options: int) -> Matrix | record
```
General normal form computation with bit options:
- 0/1: Triangular / Smith Normal Form
- 2: Reduce off-diagonal entries
- 4: Row transformations
- 8: Column transformations
- 16: Destructive mode

---

## Determinant

```gap
DeterminantIntMat(mat: Matrix) -> Integer
```
Determinant of integer matrix using NormalFormIntMat strategy. Fast for large matrices (>20×20).

---

## Lattice Reduction

```gap
LLLReducedBasis(vectors: list[Vector], y: float = 3/4, lllout: record | None = None) -> record
```
LLL reduced basis of lattice. Supports incremental computation via lllout parameter.

**Parameters:**
- `y` – sensitivity parameter (1/4 < y ≤ 1), default 3/4

**Returns record with:**
- `basis` – LLL reduced basis vectors
- `mue` – scalar products used in algorithm
- `B` – norms of basis vectors
- `transformation` – matrix T expressing new basis in terms of old

```gap
LLLReducedBasis(L: float, vectors: list[Vector], ...) -> record
```
Alternative with explicit L parameter (related to delta).

```gap
LLLReducedGramMat(G: Matrix, y: float = 3/4) -> record
```
LLL reduction of Gram matrix. Returns record with:
- `remainder` – reduced Gram matrix
- `relations` – basis of orthogonal relations
- `transformation` – matrix T where T·G·Tᵀ is remainder

---

## Vector Search

```gap
ShortestVectors(G: Matrix, m: int, positive: bool = false) -> record
```
Find all vectors x with x·G·xᵀ ≤ m. Returns record with:
- `vectors` – nonzero vectors (one of each pair ±x)
- `norms` – norms according to Gram matrix G

**Parameters:**
- `positive` – if given, only vectors with nonnegative entries

---

## Decomposition & Coefficients

```gap
Decomposition(A: Matrix, B: list[Vector], depth: int) -> list[Vector | fail]
```
Solve x*A = B[i] using p-adic expansion to given depth. Returns solutions or fail for each entry.

```gap
PadicCoefficients(A: Matrix, Amodpinv: Matrix, b: Vector, prime: int, depth: int) -> Vector
```
p-adic coefficients for solving x*A ≡ b (mod p).

```gap
IntegralizedMat(A: Matrix, inforec: record | None = None) -> record
```
Encode cyclotomic matrix into rational matrix. Returns:
- `intmat.mat` – rational matrix encoding
- `intmat.inforec` – encoding information

```gap
DecompositionInt(A: Matrix, B: list[Vector], depth: int) -> list
```
Integer decomposition using p-adic method.

```gap
LinearIndependentColumns(mat: Matrix) -> list[int]
```
Indices of linearly independent columns.

---

## Orthogonal Embeddings & Forms

```gap
OrthogonalEmbeddings(gram: Matrix, positive: str | None = None, maxdim: int | None = None) -> list[Matrix]
```
Find orthogonal embeddings of Gram matrix. Optional constraint to positive-definite forms.

**Parameters:**
- `positive` – restrict to positive-definite embeddings (string "positive")
- `maxdim` – maximum embedding dimension

---

## Reference

**Source:** GAP Chapter 25: Integral matrices and lattices

**Related Functions:**
- Chapter 39: Group subgroup lattices (`LatticeSubgroups`, `ConjugacyClassesSubgroups`)
- Forms package: Sesquilinear and quadratic forms

**Documentation:** https://docs.gap-system.org/doc/ref/chap25.html
