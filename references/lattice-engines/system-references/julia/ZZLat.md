# ZZLat Documentation (Integer Lattices in Julia)

Complete reference for the `ZZLat` class in Hecke.jl/Oscar.jl - integer lattices (ℤ-submodules of quadratic spaces over ℚ).

## Construction

```julia
integer_lattice(B: MatElem, gram: MatElem) -> ZZLat
```

Integer lattice from basis matrix B and optional Gram matrix.

```julia
quadratic_lattice(QQ, B: MatElem) -> ZZLat
```

Integer lattice over ℚ from basis matrix.

---

## Properties & Invariants

```julia
ambient_space(L: ZZLat) -> QuadSpace
```

Ambient rational quadratic space ℚ⊗ℤ L.

```julia
basis_matrix(L: ZZLat) -> QQMatrix
```

Basis matrix (rows = lattice basis vectors).

```julia
gram_matrix(L: ZZLat) -> QQMatrix
```

Gram matrix of basis.

```julia
determinant(L: ZZLat) -> QQFieldElem
```

Determinant of Gram matrix.

```julia
rank(L: ZZLat) -> Int
```

Rank of lattice.

```julia
is_integral(L: ZZLat) -> Bool
```

True if Gram matrix has integer entries.

```julia
is_even(L: ZZLat) -> Bool
```

True if diagonal of Gram matrix is all even.

```julia
is_unimodular(L: ZZLat) -> Bool
```

True if determinant is ±1.

---

## Vector Search

```julia
shortest_vector(L: ZZLat) -> QQVector
```

Shortest nonzero vector.

```julia
short_vectors(L: ZZLat, bound: QQFieldElem) -> Vector{(QQVector, QQFieldElem)}
```

All vectors with squared norm ≤ bound.

```julia
minimum(L: ZZLat) -> QQFieldElem
```

Minimum squared norm of nonzero vector.

---

## Reduction & Transformation

```julia
lll(L: ZZLat) -> ZZLat
```

LLL-reduced lattice.

```julia
lll(B: MatElem) -> MatElem
```

LLL reduction of basis matrix.

```julia
bkz(B: MatElem, block_size: Int) -> MatElem
```

BKZ reduction of basis matrix with given block size.

---

## Isometries & Automorphisms

```julia
automorphism_group(L: ZZLat) -> MatrixGroup
```

Group of isometries (automorphisms) of lattice.

```julia
is_isometric(L1: ZZLat, L2: ZZLat) -> Bool
```

True if lattices are isometric.

---

## Genus Theory

```julia
genus(L: ZZLat) -> ZZGenus
```

Global genus symbol.

```julia
mass(L: ZZLat) -> QQFieldElem
```

Mass of genus.

```julia
genus_representatives(L: ZZLat) -> Vector{ZZLat}
```

All lattice classes in genus of L.

```julia
local_symbol(L: ZZLat, p: Integer) -> LocalGenusSymbol
```

Local genus symbol at prime p.

---

## Neighbors & Evolution

```julia
neighbor(L: ZZLat, v: Vector, p: Integer) -> ZZLat
```

p-neighbor with respect to vector v.

```julia
random_neighbor(L: ZZLat, p: Integer) -> ZZLat
```

Random p-neighbor.

---

## Reference

**Docs:** https://docs.oscar-system.org/