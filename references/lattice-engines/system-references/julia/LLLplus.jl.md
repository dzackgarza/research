# LLLplus.jl Documentation

Complete reference for the `LLLplus.jl` Julia package - lattice reduction algorithms.

## LLL Reduction

```julia
lll(H: AbstractMatrix) -> (Matrix, Matrix)
```

Lenstra-Lenstra-Lovász reduction. Returns (B, T) where B is LLL-reduced basis and B = H * T.

---

## Basis Reduction Variants

```julia
seysen(H: AbstractMatrix) -> (Matrix, Matrix)
```

Seysen's lattice reduction algorithm.

```julia
hkz(H: AbstractMatrix) -> (Matrix, Matrix)
```

Hermite-Korkine-Zolotarev reduction (stronger than LLL).

```julia
brun(H: AbstractMatrix) -> (Matrix, Matrix)
```

Brun's integer relation algorithm.

---

## Vector Search

```julia
svp(B: AbstractMatrix) -> Vector
```

Shortest Vector Problem: shortest nonzero vector in lattice.

```julia
cvp(B: AbstractMatrix, t: AbstractVector) -> Vector
```

Closest Vector Problem: lattice vector closest to target.

---

## Verification

```julia
is_reduced(B: AbstractMatrix) -> Bool
```

Test if basis satisfies LLL reduction conditions.

---

## Reference

**Repo:** https://github.com/jamesfolberth/LLLplus.jl
**License:** MIT