# Lattices.jl Documentation

Duck-typed lattice definitions and operations in Julia.

## Lattice Construction

```julia
Lattice(basis: Matrix, metric: Matrix | Nothing = Nothing) -> Lattice
```

Create lattice from basis matrix and optional metric.

```julia
reciprocal_lattice(L: Lattice) -> Lattice
```

Reciprocal (dual) lattice.

---

## Lattice Properties

```julia
basis_vectors(L: Lattice) -> Matrix
```

Basis vectors of lattice.

```julia
volume(L: Lattice) -> Real
```

Volume of fundamental region.

```julia
dimension(L: Lattice) -> Int
```

Dimension of lattice.

---

## Vector Operations

```julia
in_lattice(v: Vector, L: Lattice) -> Bool
```

Test if vector is in lattice.

```julia
basis_coords(v: Vector, L: Lattice) -> Vector
```

Coordinates of v with respect to lattice basis.

```julia
lattice_reduce(v: Vector, L: Lattice) -> Vector
```

Reduce vector modulo lattice.

---

## Lattice Arithmetic

```julia
intersection(L1: Lattice, L2: Lattice) -> Lattice
```

Intersection of two lattices.

```julia
sum(L1: Lattice, L2: Lattice) -> Lattice
```

Sum of two lattices.

---

## Reference

**Repo:** https://github.com/JuliaLattices/Lattices.jl
**License:** MIT
