# Mathematica/Wolfram Language Lattice Reduction Documentation

Complete reference for Wolfram Language lattice reduction functions.

## Basic Lattice Reduction

```mathematica
LatticeReduce[basis: list[list[int]]] -> list[list[int]]
```
LLL-reduced basis of integer lattice. Performs basis reduction to minimize vector lengths and orthogonalize.

**Parameters:**
- `basis` – list of integer vectors (lattice basis rows)

**Output:**
- LLL-reduced basis (vectors as rows)

**Example:**
```mathematica
B = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
LatticeReduce[B]  (* Identity in this case *)

B = {{1, 2}, {3, 4}};
LatticeReduce[B]  (* Returns reduced basis *)
```

---

## Integer Nullspace & Kernels

```mathematica
FindIntegerNullVector[matrix: list[list[int]]] -> list[int] | None
```
Find nonzero integer vector x such that x · matrix = 0 (kernel element).

**Parameters:**
- `matrix` – integer matrix

**Output:**
- Single nonzero integer vector in kernel, or None if kernel is trivial

**Example:**
```mathematica
A = {{1, 2, 3}, {4, 5, 6}};
FindIntegerNullVector[A]
```

---

```mathematica
NullSpace[matrix: list[list[int]], Modulus -> None] -> list[list[int]]
```
Nullspace basis (requires Modulus parameter for integer version, or use on exact rationals).

**Alternative:** Use `RowReduce` with method selection for controlled nullspace computation.

---

## Hermite & Smith Normal Forms

```mathematica
HermiteDecomposition[matrix: list[list[int]]] -> {U: Matrix, H: Matrix}
```
Hermite Normal Form (HNF) decomposition. Returns matrices U and H where U · A = H, with H upper triangular.

**Output:**
- `U` – unimodular transformation matrix
- `H` – Hermite Normal Form (upper triangular, diagonal entries positive)

**Example:**
```mathematica
A = {{1, 0}, {1, 1}, {0, 1}};
{U, H} = HermiteDecomposition[A];
U . A == H  (* True *)
```

---

```mathematica
SmithDecomposition[matrix: list[list[int]]] -> {U: Matrix, S: Matrix, V: Matrix}
```
Smith Normal Form (SNF) decomposition. Returns matrices U, S, V where U · A · V = S.

**Output:**
- `U`, `V` – unimodular transformation matrices
- `S` – Smith Normal Form (diagonal, entries divide each other)

**Example:**
```mathematica
A = {{1, 2}, {3, 4}};
{U, S, V} = SmithDecomposition[A];
U . A . V == S  (* True *)
```

---

## Lattice Invariants

```mathematica
Det[matrix: list[list[int]]] -> int
```
Determinant of integer matrix.

```mathematica
GramMatrix[basis: list[list[int]]] -> list[list[int]]
```
Gram matrix G = B · B^T (requires `LinearAlgebra` context or manual multiplication).

**Workaround:**
```mathematica
B = basis;
G = B . Transpose[B];
```

---

## Row Echelon & Basis Operations

```mathematica
RowReduce[matrix: list[list[int]]] -> list[list[int]]
```
Row echelon form over rationals. For integer-preserving reductions, use `HermiteDecomposition`.

```mathematica
MatrixRank[matrix: list[list[int]]] -> int
```
Rank of integer matrix.

---

## Vector Operations

```mathematica
Norm[vector: list[int]] -> float
```
Euclidean norm (‖v‖ = √(v · v)).

```mathematica
Normalize[vector: list[int]] -> list[float]
```
Unit vector (normalized).

```mathematica
Orthogonalize[basis: list[list[int]]] -> list[list[float]]
```
Gram-Schmidt orthogonalization. Returns orthogonal vectors (floating-point).

**Example:**
```mathematica
B = {{1, 0}, {1, 1}};
Orthogonalize[B]  (* {{1, 0}, {0, 1}} *)
```

---

## Modular Arithmetic & Lattices

```mathematica
Reduce[expr, modulus: int] -> int
```
Modular reduction.

```mathematica
Mod[a: int, b: int] -> int
```
Modular reduction a mod b.

---

## Related Functions

```mathematica
GCD[a: int, b: int, ...] -> int
```
Greatest common divisor (extended GCD available via `ExtendedGCD`).

```mathematica
ExtendedGCD[a: int, b: int] -> {g: int, s: int, t: int}
```
Extended GCD: g = s*a + t*b.

```mathematica
Partition[list: list, n: int] -> list[list]
```
Partition list into chunks of size n (for reformatting basis vectors).

---

## Constraints & Notes

**⚠️ Positive-definite assumption:** Functions like `LatticeReduce` work on general integer lattices but assume **Euclidean (standard) inner product**. All reduction methods implicitly use the identity matrix as the inner product matrix.

- **Gram matrix:** Implicitly G = B·B^T (Euclidean only)
- **Indefinite forms:** Not directly supported; use Julia `Indefinite.jl` or SageMath `IntegralLattice` with custom Gram for custom bilinear forms
- **Custom bilinear forms:** Not supported; only standard Euclidean norm available
- **Floating-point precision:** Orthogonalization (`Orthogonalize`) and norm operations use floating-point; for exact arithmetic, use `Rationalize` or work with exact forms
- **Base ring:** Integer vectors ℤⁿ
- **Modular arithmetic:** Use `Mod` context or `Modulus` option for p-adic methods

---

## Reference

**Docs:** https://reference.wolfram.com/language/
**License:** Proprietary (Wolfram Research)
