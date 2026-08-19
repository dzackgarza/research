# QuadSpace Documentation (Quadratic Spaces in Julia)

Complete reference for the `QuadSpace` class in Hecke.jl/Oscar.jl - quadratic spaces over fields.

## Construction

```julia
quadratic_space(K: Field, n: Int) -> QuadSpace
```

Quadratic space over K with identity Gram matrix (dimension n).

```julia
quadratic_space(K: Field, G: MatElem) -> QuadSpace
```

Quadratic space over K from Gram matrix G.

---

## Properties & Invariants

```julia
dimension(V: QuadSpace) -> Int
```

Dimension of space.

```julia
rank(V: QuadSpace) -> Int
```

Rank of Gram matrix.

```julia
gram_matrix(V: QuadSpace) -> MatElem
```

Gram matrix.

```julia
determinant(V: QuadSpace) -> FieldElem
```

Determinant of Gram matrix (as class in K*/(K*)²).

```julia
discriminant(V: QuadSpace) -> FieldElem
```

Discriminant of space.

```julia
signature(V: QuadSpace) -> (Int, Int, Int)
```

Signature (p, n, z) over real embeddings (p = positive, n = negative, z = zero). **Note:** Only available for ℚ-spaces with real embeddings; use `hasse_invariant` for p-adic information.

---

## Local Invariants

```julia
hasse_invariant(V: QuadSpace, p: Place) -> Int
```

Hasse invariant (±1) at prime/place p.

```julia
witt_invariant(V: QuadSpace, p: Place) -> Int
```

Witt invariant at prime/place p.

---

## Equivalence & Representation

```julia
is_equivalent(V1: QuadSpace, V2: QuadSpace) -> Bool
```

True if spaces are isometric over base field.

```julia
is_represented_by(a: FieldElem, V: QuadSpace) -> Bool
```

True if value a is represented by space.

---

## Reference

**Docs:** https://docs.oscar-system.org/