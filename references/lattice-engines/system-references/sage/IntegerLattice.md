# SageMath IntegerLattice Documentation

Complete reference for `sage.modules.free_module_integer.IntegerLattice` - discrete subgroups of ℤⁿ.

## Constructor

```python
IntegerLattice(basis: list[Vector] | Matrix | OrderElement, lll_reduce: bool = True) -> IntegerLattice
```

Construct integer lattice from basis. Optionally run LLL reduction on construction.

---

**Note:** Named lattices (root lattices A, D, E, etc.) are available via IntegralLattice. See IntegralLattice.md.

---

## Basis Reduction

```python
LLL(**args, **kwds) -> Matrix_integer_dense
```
LLL reduced basis (δ=0.99, η=0.501)

```python
BKZ(**args, **kwds) -> Matrix_integer_dense
```
Block Korkine-Zolotareff reduced basis

```python
HKZ(**args, **kwds) -> Matrix_integer_dense
```
Hermite-Korkine-Zolotareff reduced basis

```python
update_reduced_basis(w: Vector) -> None
```
Inject vector and run LLL to update basis

---

## Vector Search

```python
shortest_vector() -> Vector
```
Shortest nonzero vector in lattice

```python
closest_vector(t: Vector) -> Vector
```
Closest lattice vector to target **t**

```python
approximate_closest_vector(t: Vector, delta: float = 0.99, algorithm: str = 'embedding', *args, **kwargs) -> Vector
```
Approximate closest vector. **algorithm** ∈ {'embedding', 'nearest_plane', 'rounding_off'}

```python
babai(*args, **kwargs) -> Vector
```
Alias for `approximate_closest_vector()`

---

## Lattice Invariants

```python
volume() -> Integer
```
Volume = √(det(B·Bᵀ))

```python
discriminant() -> Integer
```
|det(Gram matrix)|

```python
gaussian_heuristic(exact_form: bool = False) -> float
```
**⚠️ Requires positive-definite form.** Gaussian expected shortest vector norm

```python
hadamard_ratio(use_reduced_basis: bool = True) -> float
```
Normalized Hadamard ratio (1 = orthogonal basis)

---

## Voronoi Cell

```python
voronoi_cell(radius: float | None = None) -> Polyhedron
```
**⚠️ Requires positive-definite form.** Voronoi cell as polytope. Cached for performance.

```python
voronoi_relevant_vectors() -> list[Vector]
```
Vectors defining Voronoi cell

---

## Basis Access

```python
basis() -> list[Vector]
```
User-specified basis vectors

```python
echelonized_basis() -> list[Vector]
```
Basis in row echelon form

```python
echelonized_basis_matrix() -> Matrix
```
Echelon form basis as matrix

```python
basis_matrix(ring: Ring | None = None) -> Matrix
```
Basis as matrix rows

```python
matrix() -> Matrix
```
Basis matrix (alias for `basis_matrix()`)

```python
has_user_basis() -> bool
```
Whether basis is user-specified vs. default echelon form

```python
user_to_echelon_matrix() -> Matrix
```
Transformation matrix (user basis → echelon basis). Acts on right.

---

## Ambient Space & Structure

```python
ambient() -> FreeModule
```
Ambient module

```python
ambient_module() -> FreeModule
```
Ambient ℤⁿ

```python
ambient_vector_space() -> VectorSpace
```
Ambient vector space ℚⁿ with inner product preserved

```python
vector_space(base_field: Field | None = None) -> VectorSpace
```
Vector space via tensor product with fraction field

```python
nonembedded_free_module() -> FreeModule
```
Isomorphic non-embedded free module Rⁿ

---

## Module Arithmetic

```python
intersection(other: FreeModule) -> FreeModule
```
Intersection of two submodules

```python
quotient_module(sub: FreeModule, check: bool = True, **kwds) -> FreeModule
```
Quotient by submodule

```python
saturation() -> FreeModule
```
Saturated submodule of ℤⁿ spanning same vector space

```python
span_of_basis(basis: list[Vector], base_ring: Ring | None = None, check: bool = True, already_echelonized: bool = False) -> FreeModule
```
Module with given basis

```python
submodule_with_basis(basis: list[Vector], check: bool = True, already_echelonized: bool = False) -> FreeModule
```
Submodule with given basis

```python
zero_submodule() -> FreeModule
```
Zero submodule

```python
direct_sum(other: FreeModule) -> FreeModule
```
Direct sum with another module

---

## Lattice Index

```python
denominator() -> Integer
```
LCM of coordinate entries with respect to ambient basis

```python
index_in(other: FreeModule) -> Rational | Infinity
```
Lattice index [other:self]

```python
index_in_saturation() -> Integer
```
Index of this module in its saturation

---

## Vector Space Methods

```python
vector_space_span(gens: list[Vector], check: bool = True) -> VectorSpace
```
Vector subspace with generators

```python
vector_space_span_of_basis(basis: list[Vector], check: bool = True) -> VectorSpace
```
Vector subspace with given basis

---

## Structure & Coordinates

```python
change_ring(R: PrincipalIdealDomain) -> FreeModule
```
Coerce basis into vector space over ring **R**

```python
construction() -> tuple[Functor, Ring]
```
Functorial construction

```python
lift() -> Morphism
```
Embedding map from self to ambient

```python
retract() -> Morphism
```
Partial inverse map from ambient space

```python
linear_combination_of_basis(v: list) -> Element
```
Linear combination of basis from coordinates

```python
relations(vectors: list[Vector], zeros: str = 'left') -> list[Vector]
```
Linear dependence relations. **zeros** ∈ {'left', 'right'}

---

## Dimension & Rank

```python
rank() -> int
```
Rank (number of basis vectors)

```python
dimension() -> int
```
Dimension (same as rank)

```python
degree() -> int
```
Degree (ambient space dimension)

```python
ngens() -> int
```
Number of basis generators

```python
codimension() -> int
```
Codimension = degree - dimension

```python
cardinality() -> int | Infinity
```
Cardinality (Infinity if rank > 0)

---

## Ring & Matrix Properties

```python
base_ring() -> Ring
```
Base ring (ℤ)

```python
coordinate_ring() -> Ring
```
Coordinate ring

```python
inner_product_matrix() -> Matrix
```
Inner product matrix (ambient space)

```python
gram_matrix() -> Matrix
```
Gram matrix = B·A·Bᵀ where A is inner product matrix

---

## Containment & Tests

```python
is_ambient() -> bool
```
Whether this is the ambient module

```python
is_submodule(other: FreeModule) -> bool
```
Whether self is submodule of other

```python
uses_ambient_inner_product() -> bool
```
Whether using ambient inner product

---

## Morphisms

```python
hom(im_gens: list, codomain: Module | None = None, **kwds) -> Homomorphism
```
Homomorphism defined by image generators

---

## Constraints & Definiteness

**⚠️ Positive-definite assumption:** IntegerLattice uses the standard **Euclidean inner product** (identity matrix). The Gram matrix is always **positive-definite** = B·B^T. Methods like `gaussian_heuristic()` and `voronoi_cell()` explicitly require a PD form.

- **Gram matrix:** Implicitly G = B·B^T (Euclidean, identity inner product)
- **Indefinite forms:** Not supported; use Julia `Indefinite.jl` or other systems for indefinite forms
- **Custom bilinear forms:** Not directly supported; only standard Euclidean norm
- **Base ring:** Integer vectors in Euclidean ℝⁿ (ℤⁿ ⊂ ℝⁿ)

---

## Reference

**Source:** `sage.modules.free_module_integer` (Python/Cython)

**Authors:** 
- Martin Albrecht (2014-03): initial version
- Jan Pöschko (2012-08): some code from 2012 GSoC project

**Documentation:** https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module_integer.html

**Related Classes:**
- `IntegralLattice` – positive-definite quadratic forms
- `FreeQuadraticModule` – general quadratic modules with bilinear forms
- `FreeModule` – general free modules over commutative rings
