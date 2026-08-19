# NTL Lattice and Integer-Matrix Reference
## Core `ZZ` matrix reduction and normal-form APIs

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[ZZMOD]` | Integer matrix / `ZZ`-module model |
| `[RED]` | Reduction workflow |
| `[SOLVE]` | Integer linear solve workflow |
| `[NF]` | Normal-form algorithm |
| `[CPP]` | C++ API surface |

---

## 1. Scope

NTL exposes lattice-relevant routines through integer matrix APIs over `ZZ`, especially:

- LLL/BKZ-style basis reduction,
- image/kernel and integer-solution helpers tied to reduced bases,
- Hermite normal form.

Representation convention in these APIs: lattice/module bases are given by matrix rows.

---

## 2. Exact LLL and Integer Solve Surface

| API | Description | Tags |
|-----|-------------|------|
| `long LLL(ZZ& det2, mat_ZZ& B, long verbose=0)` | Exact LLL; default `delta=3/4`; returns rank `r`; first `m-r` rows of `B` become zero; `det2` is set to the squared determinant of the reduced lattice. Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |
| `long LLL(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)` | Exact LLL with unimodular transform `U` s.t. `U * old_B = new_B`; first `m-r` rows of `U` span the kernel of `old_B`. Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |
| `long LLL(ZZ& det2, mat_ZZ& B, long a, long b, long verbose=0)` | Exact LLL with rational reduction parameter `delta = a/b`; requires `1/4 < a/b <= 1`, `a,b` positive integers. Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |
| `long LLL(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long a, long b, long verbose=0)` | Exact LLL with rational `delta = a/b` plus unimodular transform output `U`. Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |
| `long LLL_plus(vec_ZZ& D, mat_ZZ& B, long verbose=0)` | LLL variant returning Gram-Schmidt squared-length vector `D`: `D[0]=1`, and for `i=1..r`, `D[i]/D[i-1]` is the squared length of the i-th Gram-Schmidt basis vector; `D[r]` equals `det2` from plain LLL. Returns rank `r`. Default `delta=3/4`. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"LLL_plus" | `[ZZMOD, RED, CPP]` |
| `long LLL_plus(vec_ZZ& D, mat_ZZ& B, mat_ZZ& U, long verbose=0)` | Same as above with unimodular transform output `U`. Default `delta=3/4`. Returns rank `r`. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"LLL_plus" | `[ZZMOD, RED, CPP]` |
| `long LLL_plus(vec_ZZ& D, mat_ZZ& B, long a, long b, long verbose=0)` | Same Gram-Schmidt vector output as above with explicit rational reduction parameter `delta = a/b`; requires `1/4 < a/b <= 1`, `a,b` positive integers. Returns rank `r`. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"LLL_plus" | `[ZZMOD, RED, CPP]` |
| `long LLL_plus(vec_ZZ& D, mat_ZZ& B, mat_ZZ& U, long a, long b, long verbose=0)` | Same as above with unimodular transform output `U` and explicit `delta = a/b`; requires `1/4 < a/b <= 1`. Returns rank `r`. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"LLL_plus" | `[ZZMOD, RED, CPP]` |
| `long image(ZZ& det2, mat_ZZ& B, long verbose=0)` | Cheap image/kernel computation: performs size reduction but only swaps vectors when linear dependencies are found (not a full LLL). Returns rank `r`; first `m-r` rows of `B` become zero; `det2` has same meaning as in `LLL`. Practical for computing kernels: apply to kernel output for shorter basis vectors. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"Computing Images and Kernels" | `[ZZMOD, RED, CPP]` |
| `long image(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)` | Same as above with unimodular transform output: `U * old_B = new_B`; first `m-r` rows of `U` form a basis (as a lattice) for the kernel of `old_B`. Source: `LLL.cpp`; see also `docs/ntl/upstream/LLL.txt` §"Computing Images and Kernels" | `[ZZMOD, RED, CPP]` |
| `long LatticeSolve(vec_ZZ& x, const mat_ZZ& A, const vec_ZZ& y, long reduce=0)` | Solves `x*A = y` over integers when possible; sets `x` to a solution and returns `1` if solvable, leaves `x` unchanged and returns `0` if no integer solution exists. Optional `reduce` (0/1/2) controls quality of solution when the solution is not unique: 0=no effort, 1=size reduction on kernel, 2=LLL on kernel (provably near-optimal). Source: `LLL.cpp` | `[ZZMOD, SOLVE, CPP]` |

---

## 3. Floating LLL and BKZ Surface

| API family | Description | Tags |
|------------|-------------|------|
| `long [G_]LLL_{FP,QP,XD,RR}(mat_ZZ& B[, mat_ZZ& U], double delta=0.99, long deep=0, LLLCheckFct check=0, long verbose=0)` | Floating-point LLL family over integer-basis input (`FP/QP/XD/RR` variants); returns rank. **`delta` constraint: `0.50 <= delta < 1`** (note: lower bound is `1/2`, not `1/4` as in exact LLL; upper bound is exclusive). Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |
| `long [G_]BKZ_{FP,QP,QP1,XD,RR}(mat_ZZ& B[, mat_ZZ& U], double delta=0.99, long BlockSize=10, long prune=0, LLLCheckFct check=0, long verbose=0)` | BKZ family over the same integer-basis model; returns rank. **`delta` constraint: `0.50 <= delta < 1`** (same as floating LLL). **`BlockSize` constraint: `2 <= BlockSize <= m`** where `m` is the number of rows of `B`. `prune=0` disables pruning; `prune > 0` enables Volume Heuristic (Schnorr-Horner). `QP1` variant uses quad_float for Gram-Schmidt but double in block reduction search phase. Source: `LLL.cpp` | `[ZZMOD, RED, CPP]` |

Important caveats from upstream docs:

- `delta` for floating-point LLL/BKZ variants must satisfy `0.50 <= delta < 1` (upstream explicitly states this range for FP variants); this is distinct from the exact LLL/LLL_plus constraint `1/4 < delta <= 1` where delta is expressed as rational `a/b`. Source: `LLL.cpp` ("may be set so that 0.50 <= delta < 1").
- `deep` is documented as deprecated in modern NTL usage; Givens-based variants (`G_LLL_*`) do not support `deep != 0` and will raise an error.
- `BlockSize` and `prune` materially affect BKZ quality/runtime tradeoffs; upstream notes `BlockSize` should be between 2 and the number of rows of `B`.
- `LLLCheckFct check` is a callback `typedef long (*LLLCheckFct)(const vec_ZZ&)` invoked after each size reduction; if it returns non-zero, the routine terminates immediately and the reported rank may be too large.
- APIs operate on row-basis matrices over `ZZ`; these are Euclidean reduction routines, not indefinite genus/isometry classification APIs.

---

## 4. Hermite Normal Form Surface

| API | Description | Tags |
|-----|-------------|------|
| `HNF(mat_ZZ& W, const mat_ZZ& A, const ZZ& D)` | Computes Hermite normal form for full-column-rank integer matrix input under documented determinant multiple precondition. Source: `docs/ntl/upstream/LLL.cpp.html` (section "HNF") | `[ZZMOD, NF, CPP]` |

Upstream preconditions summarized:

- `A` is `n x m` with rank `m` and `n >= m`,
- `D` is a positive multiple of the determinant of the lattice generated by columns of `A`.

---

## 5. Domain Caveat

NTL's lattice-reduction APIs here are integer-matrix and Euclidean-reduction oriented. They do not provide high-level indefinite arithmetic-form classification contracts (genus/discriminant-form/isometry-class APIs).

---

## 6. Additional Utility APIs

| API | Description | Tags |
|-----|-------------|------|
| `void ComputeGS(const mat_ZZ& B, mat_RR& mu, vec_RR& c)` | Computes Gramm-Schmidt data for B. Assumes B is an m x n matrix of rank m. Let {B^*(i)} be the orthogonal basis, then c(i) = |B^*(i)|^2, and B^*(i) = B(i) - sum_{j=1}^{i-1} mu(i,j) B^*(j). Uses classical Gramm-Schmidt orthogonalization. Source: `docs/ntl/upstream/LLL.cpp.html` | `[ZZMOD, CPP]` |
| `void NearVector(vec_ZZ& w, const mat_ZZ& B, const vec_ZZ& a)` | Computes a vector w that is an approximation to the closest vector in the lattice spanned by B to a, using the "closest plane" algorithm from Babai (Combinatorica 6:1-13, 1986). B must be a square matrix, and it is assumed that B is already LLL or BKZ reduced (the better the reduction the better the approximation). Uses RR arithmetic with current precision. Source: `docs/ntl/upstream/LLL.cpp.html` | `[ZZMOD, CPP]` |

---

## 7. Sources

- NTL module map (LLL + HNF listed): `https://libntl.org/doc/tour-modules.html`
- NTL LLL/BKZ and solve API docs: `https://libntl.org/doc/LLL.cpp.html`
- NTL HNF API docs: `https://libntl.org/doc/HNF.cpp.html`
- NTL lattice-reduction tutorial examples: `https://libntl.org/doc/tour-ex4.html`
- Local upstream snapshot: `docs/ntl/upstream/LLL.txt` (exact LLL, all four LLL_plus overloads including a/b delta variants, image, LatticeSolve, ComputeGS, NearVector signatures and FP delta constraint `0.50 <= delta < 1` verified from this file)
- Local upstream snapshot: `docs/ntl/upstream/LLL.cpp.html` (HTML-rendered version of same LLL surface)
- Local upstream snapshot: `docs/ntl/upstream/mat_ZZ.cpp.html` (mat_ZZ type definitions)

