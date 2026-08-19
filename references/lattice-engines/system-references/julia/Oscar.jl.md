# Oscar.jl Documentation (Lattices & Quadratic Forms)

Complete reference for Oscar.jl methods for lattice reduction and quadratic space manipulation.

**Note:** Oscar.jl lattice operations are backed by Hecke.jl; use Hecke.jl docs for `lattice()` and `quadratic_space()` constructors.

## Lattice Reduction

```julia
lll(L: ZZLat, redo: Bool = false) -> ZZLat
```

LLL-reduced lattice.

```julia
lll(M: MatElem, context: LLLContext) -> MatElem
```

LLL-reduced matrix.

```julia
bkz(M: MatElem, block_size: Int) -> MatElem
```

BKZ-reduced matrix with given block size.

---

## Integer Lattices (ZZLat)

```julia
integer_lattice_with_isometry(L: ZZLat, f: QQMatrix) -> ZZLatWithIsom
```

Lattice with attached isometry.

```julia
genus(L: ZZLat) -> ZZGenus
```

Global genus symbol.

```julia
mass(L: ZZLat) -> QQFieldElem
```

Mass of lattice genus.

---

## Quadratic Spaces (QuadSpace)

```julia
quadratic_space(K: Field, G: MatElem) -> QuadSpace
```

Quadratic space from Gram matrix.

```julia
is_equivalent(V1: QuadSpace, V2: QuadSpace) -> Bool
```

True if spaces are isometric over base field.

```julia
hasse_invariant(V: QuadSpace, p: Place) -> Int
```

Hasse invariant at prime/place p (±1).

```julia
witt_invariant(V: QuadSpace, p: Place) -> Int
```

Witt invariant at prime/place p.

---

## Reference

**Repo:** https://github.com/oscar-system/Oscar.jl
**License:** BSD-2-Clause