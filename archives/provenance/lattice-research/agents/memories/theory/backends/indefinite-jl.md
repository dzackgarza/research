# Indefinite.jl: Indefinite quadratic form computations

**Source:** https://github.com/MathieuDutSik/Indefinite.jl

**Paper:** Dawes, "Orbits in Lattices", arXiv:2205.10601

**What it does:** Automorphism groups, isometry testing, orbit representatives for **indefinite** integral quadratic forms. (CARAT cannot do this.)

---

## Automorphism group

```julia
using Indefinite, Oscar, Nemo

# Signature (2,2): U ⊕ <-1> ⊕ <-1>
eGram = matrix(QQ, [
    0  1  0  0
    1  0  0  0
    0  0 -1  0
    0  0  0 -1
])

# Compute generators of Aut(Q)
gens = Indefinite.INDEF_FORM_AutomorphismGroup(eGram)

# Returns: Vector{QQMatrix} (6 generators for this example)
# Each g satisfies: g^T * eGram * g == eGram
```

---

## Isometry testing

```julia
using Indefinite, Oscar, Nemo

# Form 1: signature (2,2)
eGram1 = matrix(QQ, [
    0  1  0  0
    1  0  0  0
    0  0 -1  0
    0  0  0 -1
])

# Form 2: same signature, different basis
eGram2 = matrix(QQ, [
    2  1  0  0
    1  0  0  0
    0  0 -1  0
    0  0  0 -1
])

# Test equivalence, get transformation matrix
T = Indefinite.INDEF_FORM_TestEquivalence(eGram1, eGram2)

# Returns: QQMatrix such that T^T * eGram1 * T == eGram2
# Expected: [1 1 0 0; 1 0 0 0; 0 0 1 0; 0 0 0 1]
```

---

## Orbit representatives (vectors of given norm)

```julia
using Indefinite, Oscar, Nemo

# Lorentzian lattice (signature (1,2))
eGram = zero_matrix(QQ, 3, 3)
eGram[1,1] = 1
eGram[2,2] = -1
eGram[3,3] = -1

# Isotropic vectors (norm 0)
result = Indefinite.INDEF_FORM_GetOrbitRepresentative(eGram, QQ(0))

# Returns: QQMatrix with one row per orbit representative
# Expected: [1 0 -1]
```

---

## Isotropic k-planes

```julia
using Indefinite, Oscar, Nemo

# Signature (2,2): U ⊕ U(2)
eGram = matrix(QQ, [
    0  1  0  0
    1  0  0  0
    0  0  0  2
    0  0  2  0
])

# Isotropic planes (k=2, max for signature (2,2))
planes = Indefinite.INDEF_FORM_GetOrbit_IsotropicKplane(eGram, 2)

# Returns: Vector{QQMatrix}, each matrix represents an isotropic 2-plane
```

---

## Isotropic k-flags

```julia
using Indefinite, Oscar, Nemo

# Same form as above
eGram = matrix(QQ, [
    0  1  0  0
    1  0  0  0
    0  0  0  2
    0  0  2  0
])

# Isotropic flags of length k=2
flags = Indefinite.INDEF_FORM_GetOrbit_IsotropicKflag(eGram, 2)

# Returns: Vector{QQMatrix} representing flag representatives
```

---

## Examples from Dawes paper (arXiv:2205.10601)

### Example 2.2: U ⊕ A₃ - vector equivalence

```julia
using Indefinite, Oscar, Nemo

# L = U ⊕ A₃ (signature (1,4))
G_U = matrix(QQ, [0 1; 1 0])
G_A3 = -matrix(QQ, [2 1 0; 1 2 1; 0 1 2])
Q = block_diag(G_U, G_A3)

# Test vectors (both have norm 20)
v1 = [4, 4, 1, 2, -1]
v2 = [36, 144, 5, -30, 83]

# Result: v1 ~ v2 under Õ⁺(L)
# Equivalence matrix θ found by algorithm:
theta = matrix(QQ, [
    11   5 -11 -13  -9
    43  21 -46 -51 -36
     1   1  -1  -2  -2
    -9  -5  10  12   8
    25  12 -26 -30 -21
])
```

### Example 2.6: U ⊕ A₃ - simpler vectors

```julia
using Indefinite, Oscar, Nemo

# Same lattice L = U ⊕ A₃
G_U = matrix(QQ, [0 1; 1 0])
G_A3 = -matrix(QQ, [2 1 0; 1 2 1; 0 1 2])
Q = block_diag(G_U, G_A3)

# Test vectors (both have norm -2)
v1 = [1, -1, 0, 0, 0]
v2 = [1, 0, 1, 0, 0]

# Result: v1 ~ v2 under SÕ⁺(L)
```

---

## Function reference

| Function | Signature | Returns |
|----------|-----------|---------|
| `INDEF_FORM_AutomorphismGroup` | `(Qmat::QQMatrix)` | `Vector{QQMatrix}` |
| `INDEF_FORM_TestEquivalence` | `(Q1::QQMatrix, Q2::QQMatrix)` | `QQMatrix` |
| `INDEF_FORM_GetOrbitRepresentative` | `(Qmat::QQMatrix, Xval::QQFieldElem)` | `QQMatrix` |
| `INDEF_FORM_GetOrbit_IsotropicKplane` | `(Qmat::QQMatrix, k::Int)` | `Vector{QQMatrix}` |
| `INDEF_FORM_GetOrbit_IsotropicKflag` | `(Qmat::QQMatrix, k::Int)` | `Vector{QQMatrix}` |
