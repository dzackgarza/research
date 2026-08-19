# NTL (Number Theory Library) Lattice Reduction Documentation

Complete reference for NTL C++ lattice reduction and basis manipulation functions.

**⚠️ Positive-definite assumption:** Per lattice theory (Espitau et al.), standard lattice reduction (LLL/BKZ) is defined only for positive-definite quadratic forms. NTL assumes the **Euclidean inner product** and cannot handle indefinite or general bilinear forms. See [DEFINITENESS_NOTES.md](../DEFINITENESS_NOTES.md) for cross-system comparison.

## Installation

```bash
# Download from: https://www.shoup.net/ntl/
./configure
make
make install
```

**Requirements:** GMP (optional, recommended for performance)

---

## Core Types

```cpp
#include <NTL/LLL.h>
#include <NTL/matrix.h>
#include <NTL/ZZ.h>

typedef Vec<ZZ> vec_ZZ;
typedef Mat<ZZ> mat_ZZ;
```

Integer vectors and matrices for lattice algorithms.

---

## LLL Reduction

```cpp
long LLL_FP(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long verbose = 0)
```
LLL reduction using floating-point Gram-Schmidt. **Fastest**, **in-place**.

**Parameters:**
- `B` – basis matrix (rows are lattice vectors); modified in-place
- `U` – optional transformation matrix (B_new = U · B_old); can be 0
- `delta` – LLL parameter, 0.5 < δ ≤ 1 (default 0.99)
- `verbose` – print progress if nonzero

**Output:**
- Return value: number of swap operations performed
- B is LLL-reduced

**Example:**
```cpp
#include <NTL/LLL.h>
using namespace NTL;

mat_ZZ B;
// ... initialize B ...
mat_ZZ U;
long swaps = LLL_FP(B, U, 0.99);
cout << "Swaps: " << swaps << endl;
```

---

```cpp
long LLL_QP(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long verbose = 0)
```
LLL reduction using quad-precision arithmetic. **More numerically stable** than FP, **slower**.

---

```cpp
long LLL_XD(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long verbose = 0)
```
LLL reduction using extended-precision (via MPFR if available).

---

```cpp
long LLL_RR(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long verbose = 0)
```
LLL reduction using arbitrary-precision RR (real) arithmetic. **Most stable, slowest**.

---

## BKZ Reduction

```cpp
void BKZ_FP(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long blocksize = 10, long verbose = 0)
```
Block Korkine-Zolotareff (BKZ) reduction using floating-point. **In-place**.

**Parameters:**
- `B` – basis matrix; modified in-place
- `U` – optional transformation matrix
- `delta` – LLL parameter (default 0.99)
- `blocksize` – BKZ block size (typically 10–50)
- `verbose` – progress output

**Example:**
```cpp
mat_ZZ B;
// ... initialize B ...
BKZ_FP(B, 0, 0.99, 20);  // BKZ with block size 20
```

---

```cpp
void BKZ_QP(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long blocksize = 10, long verbose = 0)
void BKZ_XD(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long blocksize = 10, long verbose = 0)
void BKZ_RR(mat_ZZ& B, mat_ZZ& U, double delta = 0.99, long blocksize = 10, long verbose = 0)
```

BKZ with different precision levels (QP, XD, RR).

---

## Gram-Schmidt Orthogonalization

```cpp
void ComputeGS(const mat_ZZ& B, vec_RR& b, vec_vec_RR& mu)
```
Compute Gram-Schmidt coefficients for basis B.

**Output:**
- `b` – squared norms ‖b_i*‖²
- `mu` – Gram-Schmidt coefficients μ[i][j]

---

```cpp
double max_log_b(const mat_ZZ& B)
```
Maximum log₂(‖b_i*‖) over all basis vectors.

---

## Shortest Vector Problem (SVP)

```cpp
void LLL(mat_ZZ& B, long verbose = 0)
void LLL(mat_ZZ& B, mat_ZZ& U, long verbose = 0)
```
Default LLL reduction (wraps fastest available method).

**Note:** For explicit SVP solvers, use external tools (e.g., enumeration via fpylll or custom code).

---

## Determinant & Lattice Invariants

```cpp
void det(ZZ& determinant, const mat_ZZ& B)
```
Compute determinant using Gaussian elimination.

```cpp
ZZ determinant(const mat_ZZ& B)
```
Return determinant directly.

---

```cpp
ZZ content(const vec_ZZ& v)
```
GCD of vector entries.

---

## Normal Forms

```cpp
long RowEchelon(mat_ZZ& A, long &rank)
```
Row echelon form (destructive). Returns rank.

---

## Modular & p-adic Methods

```cpp
void mul(mat_ZZ& X, const mat_ZZ& A, const mat_ZZ& B)
void add(mat_ZZ& X, const mat_ZZ& A, const mat_ZZ& B)
void sub(mat_ZZ& X, const mat_ZZ& A, const mat_ZZ& B)
```
Exact integer matrix arithmetic.

---

```cpp
#include <NTL/ZZ_p.h>

typedef Vec<ZZ_p> vec_ZZ_p;
typedef Mat<ZZ_p> mat_ZZ_p;

ZZ_p::init(p);  // Set modulus p
```

Modular arithmetic (p-adic) over ℤ/pℤ.

---

## Vector & Matrix Operations

```cpp
vec_ZZ v(10);  // Vector of size 10
mat_ZZ B(10, 10);  // 10×10 matrix

v[i] = ...;
B[i][j] = ...;

long n = v.length();
long m = B.NumRows(), n = B.NumCols();
```

Basic construction and access.

---

```cpp
void transpose(mat_ZZ& X, const mat_ZZ& A)
```
Matrix transpose.

---

```cpp
void ident(mat_ZZ& X, long n)
```
Identity matrix of size n×n.

---

## Input/Output

```cpp
#include <NTL/matrix.h>

cout << B;  // Print matrix
cin >> B;   // Read matrix
```

---

## Precision Selection

| Function | Precision | Speed | Stability |
|----------|-----------|-------|-----------|
| `LLL_FP` | double (53-bit) | Very fast | Moderate |
| `LLL_QP` | quad-double (212-bit) | Fast | Good |
| `LLL_XD` | extended (256+ bit) | Medium | Very good |
| `LLL_RR` | arbitrary (RR) | Slow | Excellent |

---

## Constraints & Notes

- **Positive-definite assumption:** LLL/BKZ assume Euclidean inner product; use custom implementations for indefinite forms.
- **In-place modification:** Most functions modify B directly (no copying).
- **Transformation matrix:** Optional U captures row operations; U · B_old = B_new.
- **Numerical stability:** Choose precision based on matrix condition number; larger delta (closer to 1) requires higher precision.
- **Memory:** Large matrices benefit from QP/XD over RR.

---

## Example: Complete Workflow

```cpp
#include <NTL/LLL.h>
#include <iostream>
using namespace NTL;

int main() {
    // Create random basis
    mat_ZZ B;
    B.SetDims(20, 20);
    for (long i = 0; i < 20; i++) {
        for (long j = 0; j < 20; j++) {
            RandomBits(B[i][j], 32);  // Random 32-bit entries
        }
    }

    // Apply LLL reduction
    mat_ZZ U;
    long swaps = LLL_FP(B, U, 0.99, 1);  // verbose=1

    // Check first vector norm
    ZZ norm_sq = 0;
    for (long j = 0; j < 20; j++) {
        norm_sq += B[0][j] * B[0][j];
    }
    cout << "First vector norm²: " << norm_sq << endl;

    return 0;
}
```

Compile:
```bash
g++ -o lattice_reduce lattice_reduce.cpp -lntl -lgmp
./lattice_reduce
```

---

## Reference

**Website:** https://www.shoup.net/ntl/
**Author:** Victor Shoup
**License:** GNU General Public License (GPL) v2+
