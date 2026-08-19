# SageMath IntegralLattice Documentation

Complete reference for `sage.modules.free_quadratic_module_integer_symmetric.IntegralLattice` - integral lattices with non-degenerate symmetric bilinear forms.

## Constructor

```python
IntegralLattice(data: Matrix | int | str, basis: Matrix | list[Vector] | None = None) -> IntegralLattice
```

Return the integral lattice spanned by basis in the ambient space.

**Parameters:**
- `data` – descriptor of the lattice:
  - **Cartan type string** – root lattice (e.g., 'A2', 'D4', 'E8') [primary use]
  - `'U'` or `'H'` – hyperbolic lattices
  - Symmetric matrix over ℚ – inner product matrix (requires special handling)
- `basis` – (optional) matrix rows or list of elements forming basis; defaults to standard basis

**Examples:**
```python
# From Gram matrix
G = Matrix([[2, 1], [1, 2]])
L = IntegralLattice(G)

# Root lattice
L = IntegralLattice('A2')
L = IntegralLattice(['E', 8])

# Hyperbolic lattice
L = IntegralLattice('U')
L = IntegralLattice('H')

# With custom basis
B = Matrix([[1, 0], [1, 1]])
L = IntegralLattice(G, basis=B)
```

---

## Core Methods

```python
gram_matrix() -> Matrix
```
Inner product matrix of the lattice.

```python
basis() -> list[Vector]
```
Distinguished basis vectors.

```python
rank() -> Integer
```
Rank (dimension) of lattice.

```python
determinant() -> Integer
```
Determinant of Gram matrix.

---

## Properties

```python
signature() -> Integer
```
Signature = (# positive eigenvalues) - (# negative eigenvalues) of Gram matrix.

```python
signature_pair() -> tuple[Integer, Integer]
```
Signature tuple (n_+, n_-): number of positive and negative eigenvalues.

```python
is_even() -> bool
```
True if all vector norms are even.

```python
dual_lattice() -> FreeQuadraticModule
```
Dual lattice L^∨ = {x ∈ L ⊗ ℚ : (x, l) ∈ ℤ for all l ∈ L}.

```python
discriminant_group(s: int = 0) -> FiniteQuadraticModule
```
Discriminant group L^∨/L (or s-primary part if s > 0).

---

## Reduction

```python
LLL() -> IntegralLattice
```
LLL-reduced basis of this lattice.

---

## Shortest/Maximum Vectors

```python
maximum() -> Integer
```
Maximum norm: max{x² | x ∈ L \ {0}}.

```python
maximal_overlattice(p: int | None = None) -> IntegralLattice
```
Maximal even integral overlattice (or p-maximal if p given).

---

## Lattice Operations

```python
sublattice(basis: list[Vector]) -> IntegralLattice
```
Sublattice spanned by basis elements.

```python
direct_sum(M: FreeQuadraticModule) -> IntegralLattice
```
Direct sum with another lattice.

```python
tensor_product(other: IntegralLattice, discard_basis: bool = False) -> IntegralLattice
```
Tensor product of two lattices.

```python
twist(s: int, discard_basis: bool = False) -> IntegralLattice
```
Lattice with inner product scaled by s.

```python
automorphisms(gens: list | None = None, is_finite: bool | None = None) -> MatrixGroup
```
**⚠️ Requires definite (positive or negative) form.** Returns orthogonal group of isometries. For indefinite lattices, pass explicit `gens` parameter or raises NotImplementedError.

---

## Utility Constructors

```python
IntegralLatticeDirectSum(lattices: list[IntegralLattice], return_embeddings: bool = False) -> IntegralLattice | tuple
```
Direct sum of multiple lattices. Returns embeddings if return_embeddings=True.

```python
IntegralLatticeGluing(lattices: list[IntegralLattice], glue: list[list], return_embeddings: bool = False) -> IntegralLattice | tuple
```
Overlattice glued from multiple lattices via discriminant group elements.

---

## Vector Enumeration Methods

```python
enumerate_short_vectors() -> Iterator[Vector]
```
Iterates over all short vectors in the lattice.

```python
enumerate_close_vectors(target: Vector) -> Iterator[Vector]
```
Iterates over lattice vectors close to target vector.

```python
short_vectors(n: Integer) -> list[list[Vector]]
```
Returns short vectors of length < n. Returns list L where L[k] is vectors of norm k.

---

## Extremal Vectors

```python
minimum() -> Rational
```
Returns minimum nonzero norm in lattice.

```python
max() -> Rational
```
Returns maximum norm (for bounded cases).

```python
min() -> Rational
```
Returns minimum norm (alias for `minimum()`).

---

## Orthogonal Structure

```python
orthogonal_complement(M: FreeQuadraticModule) -> FreeQuadraticModule
```
Returns orthogonal complement of submodule M (for sublattices in ambient space).

```python
orthogonal_group() -> MatrixGroup
```
Returns group of orthogonal automorphisms.

---

## Lattice Extensions

```python
overlattice(gens: list[Vector] | Matrix) -> IntegralLattice
```
Returns lattice spanned by this lattice and given generators. **⚠️ Result must be integral.**

---

## Reduction

```python
lll() -> IntegralLattice
```
Returns LLL-reduced lattice (variant/alias).

---

## Genus & Classification

```python
genus() -> Genus
```
Returns the genus symbol of the integral lattice.

---

## Local Methods

```python
local_modification(M: IntegralLattice, G: Matrix, p: int, check: bool = True) -> IntegralLattice
```
Local modification of ℤ_p-maximal lattice to match Gram matrix at prime p.

---

## Constraints & Notes

- **Gram matrix:** Non-degenerate, symmetric over ℚ; can be positive-definite or indefinite
- **Base ring:** Integer coefficients (ℤⁿ as abelian group)
- **Definiteness:** Supports both positive-definite (signature (n, 0)) and indefinite (mixed signature)
- **Vector search:** Limited to maximum/shortest under specific norms
- **Reference:** https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_quadratic_module_integer_symmetric.html
