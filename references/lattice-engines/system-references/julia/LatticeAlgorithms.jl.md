# LatticeAlgorithms.jl Documentation

Lattice reduction and vector search algorithms in Julia.

## Reduction Algorithms

```julia
lll(B: Matrix) -> (Matrix, Matrix)
```

LLL basis reduction. Returns (reduced_basis, transformation).

```julia
kz(B: Matrix) -> (Matrix, Matrix)
```

Korkine-Zolotarev reduction.

```julia
minkowski(B: Matrix) -> (Matrix, Matrix)
```

Minkowski reduction.

---

## Vector Search

```julia
cvp(B: Matrix, t: Vector) -> Vector
```

Closest Vector Problem. Finds lattice vector closest to target t.

```julia
svp(B: Matrix) -> Vector
```

Shortest Vector Problem. Returns shortest nonzero vector.

```julia
enum(B: Matrix, B_star: Matrix, mu: Matrix, d: Vector, r: Real, R_sq: Real) -> Vector
```

Fincke-Pohst enumeration with pruning.

---

## Gram-Schmidt

```julia
gram_schmidt(B: Matrix) -> (Matrix, Vector, Matrix)
```

Gram-Schmidt orthogonalization. Returns (B_star, norms, mu).

---

## Reference

**Repo:** https://github.com/JuliaPackages/LatticeAlgorithms.jl
**License:** MIT
