# Indefinite.jl Documentation

Complete reference for the Indefinite.jl Julia package - working with integral indefinite quadratic forms.

## Equivalence Testing

```julia
IsometricEquivalent(form1::Matrix{Int}, form2::Matrix{Int}) -> (bool, Matrix{Int} | nothing)
```

Test if two indefinite forms are equivalent under GL(ℤ) action.

**Input:**
- `form1` – Square integer matrix (Gram matrix of first form)
- `form2` – Square integer matrix (Gram matrix of second form)

**Output:**
- Tuple (is_equivalent, change_of_basis)
- `is_equivalent` – true if forms equivalent under integer linear transformations
- `change_of_basis` – Unimodular matrix M where M·form1·Mᵀ = form2 (or nothing if not equivalent)

**Example:**
```julia
A = [2 0; 0 -2]
B = [1 0; 0 -4]
equiv, M = IsometricEquivalent(A, B)
```

---

## Automorphism Groups

```julia
FindAutomorphisms(form::Matrix{Int}) -> Vector{Matrix{Int}}
```

Compute finite generating set of automorphism group of indefinite form.

**Input:**
- `form` – Square integer Gram matrix

**Output:**
- List of generating matrices. All elements of Aut(form) are products of these generators.

**Example:**
```julia
A = [2 0 0; 0 -2 0; 0 0 1]
gens = FindAutomorphisms(A)
```

---

## Isotropic Vectors

```julia
IsotropicVectors(form::Matrix{Int}, C::Int) -> Vector{Vector{Int}}
```

Find orbit representatives of solutions to A[v] = C.

**Input:**
- `form` – Indefinite Gram matrix
- `C` – Target value (integer)

**Output:**
- List of representative vectors v where v·form·vᵀ = C, modulo automorphisms

**Special case:** If C = 0, returns orbit representatives of **primitive isotropic vectors**.

**Example:**
```julia
A = [1 0; 0 -1]
isotropic = IsotropicVectors(A, 0)  # Find isotropic vectors
```

---

## Isotropic Subspaces

```julia
IsotropicSubspaces(form::Matrix{Int}, k::Int) -> Vector{Matrix{Int}}
```

Find orbit representatives of k-dimensional isotropic subspaces.

**Parameters:**
- `form` – Indefinite form with signature (p, q)
- `k` – Dimension (must satisfy k ≤ min(p, q))

**Output:**
- List of basis matrices for k-dimensional totally isotropic subspaces, one from each orbit

**Properties:**
- Each returned matrix has k rows
- All rows lie in the isotropic cone (A[v] = 0)
- Subspaces are maximal among representatives

**Example:**
```julia
# Hyperbolic plane with signature (1,1)
H = [0 1; 1 0]
subsp = IsotropicSubspaces(H, 1)  # 1-dim isotropic lines
```

---

## Isotropic Flags

```julia
IsotropicFlags(form::Matrix{Int}, k::Int) -> Vector{Vector{Matrix{Int}}}
```

Find orbit representatives of k-length flags of isotropic subspaces.

**Parameters:**
- `form` – Indefinite form with signature (p, q)
- `k` – Flag length (must satisfy k ≤ min(p, q))

**Output:**
- List of flag representatives. Each flag is list [V₀, V₁, ..., Vₖ] where:
  - V₀ ⊂ V₁ ⊂ ... ⊂ Vₖ
  - Each Vᵢ is i-dimensional and totally isotropic

**Example:**
```julia
# Signature (3,3) - can have flags of length ≤ 3
form = diag([1, 1, 1, -1, -1, -1])
flags = IsotropicFlags(form, 2)  # 2-length flags
```

---

## Signature Computation

```julia
Signature(form::Matrix{Real}) -> (Int, Int)
```

Compute signature (p, q) of quadratic form.

**Input:**
- `form` – Real symmetric matrix

**Output:**
- Tuple (p, q) where p = # positive eigenvalues, q = # negative eigenvalues

**Example:**
```julia
A = [2 0; 0 -3]
p, q = Signature(A)  # Returns (1, 1)
```

---

## Form Invariants

```julia
Discriminant(form::Matrix{Int}) -> Int
```

Compute discriminant |det(form)| of integer form.

```julia
IsEven(form::Matrix{Int}) -> Bool
```

Check if form is even (all diagonal entries even).

```julia
IsSymmetric(form::Matrix) -> Bool
```

Verify form is symmetric matrix.

---

## Utility Functions

```julia
GramMatrix(vectors::Vector{Vector{Int}}) -> Matrix{Int}
```

Compute Gram matrix from list of vectors.

**Input:**
- `vectors` – List of integer vectors

**Output:**
- Gram matrix G where G[i,j] = vectors[i]·vectors[j]

```julia
ReducedBasis(form::Matrix{Int}) -> Matrix{Int}
```

Compute LLL-reduced basis of lattice defined by form.

---

## Reference

**Repo:** https://github.com/MathieuDutSik/Indefinite.jl
**Author:** Mathieu Dutour Sikirić
**License:** GPL-2.0
