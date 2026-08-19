# Lattice Definiteness Assumptions Across CAS Systems

This document consolidates definiteness constraints and bilinear form support across all documented systems.

---

## Executive Summary

| System | Gram Matrix | Indefinite Forms | Custom Bilinear | Base Ring | Notes |
|--------|-------------|------------------|-----------------|-----------|-------|
| **SageMath IntegerLattice** | ✓ Euclidean (PD) | ✗ No | ✗ No | ℤⁿ | Identity IP only |
| **SageMath IntegralLattice** | ✓ Both | ✓ Yes | ✓ Yes (via Gram) | ℤⁿ | Custom bilinear forms |
| **GAP IntegerLattices** | ✓ PD (implicit) | ✗ No | ✗ No | ℤⁿ | Integral matrix operations |
| **Macaulay2 LLLBases** | ✓ PD (Euclidean) | ✗ No | ✗ No | ℤⁿ | Euclidean lattices only |
| **Julia Indefinite.jl** | ✓ Both | ✓ Yes | ✓ Yes | ℤⁿ | Explicit indefinite support |
| **Julia LatticeAlgorithms.jl** | ✓ PD (implied) | ✗ No | ✗ No | ℤⁿ | LLL, Korkine-Zolotareff |
| **Julia Oscar.jl (Hecke)** | ✓ PD + indefinite | ✓ Yes | ✓ Yes (genus) | ℤⁿ | Via QuadSpace |
| **Julia ZZLat.jl** | ✓ PD + indefinite | ✓ Yes | ✓ Yes (genus) | ℤⁿ | Genus theory |
| **Julia Lattices.jl** | ✓ PD + indefinite | ✓ Yes | ~ Flexible | ℤⁿ | Duck-typed interface |
| **Julia QuadSpace** | ✓ Both | ✓ Yes | ✓ Yes | ℚⁿ fields | General bilinear forms |
| **PARI/GP qflll** | ✓ PD (implied) | ✗ No | ✗ No | ℤ, ℚ | SVP/CVP require PD |
| **Python fpylll** | ✓ PD (Euclidean) | ✗ No | ✗ No | ℤⁿ | Euclidean only |
| **Mathematica** | ✓ PD (Euclidean) | ✗ No | ✗ No | ℤⁿ | Standard Euclidean norm |
| **C++ NTL** | ✓ PD (Euclidean) | ✗ No | ✗ No | ℤⁿ | Floating-point reduction |

---

## System Details

### SageMath IntegerLattice

```python
# Euclidean lattice: Gram matrix = B·B^T (identity inner product)
L = IntegerLattice([[1, 0], [1, 1]])
print(L.gram_matrix())  # Returns B·B^T, positive-definite
```

**Constraints:**
- ✓ **Gram matrix:** Always positive-definite (Euclidean, standard inner product)
- ✗ **Indefinite forms:** Not supported; methods like `gaussian_heuristic()`, `voronoi_cell()` assume PD
- ✗ **Custom bilinear forms:** Only identity inner product available
- **Base ring:** ℤⁿ (integer vectors in Euclidean ℝⁿ)

**Methods affected by PD assumption:**
- `gaussian_heuristic()` – requires PD
- `voronoi_cell()` – requires PD
- LLL/BKZ/HKZ – work on PD forms

**See also:** `IntegralLattice` for positive-definite quadratic forms with custom Gram matrices.

---

### SageMath IntegralLattice

```python
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

# From Gram matrix (positive-definite or indefinite)
G = Matrix([[2, 1], [1, 2]])
L = IntegralLattice(G)

# Root lattices
L = IntegralLattice('A2')
L = IntegralLattice(['E', 8])

# Hyperbolic lattices
L = IntegralLattice('U')
L = IntegralLattice('H')
```

**Constraints:**
- ✓ **Gram matrix:** Non-degenerate, symmetric over ℚ; can be PD or indefinite
- ✓ **Indefinite forms:** Fully supported; signature_pair() returns (n_+, n_-)
- ✓ **Custom bilinear forms:** Via explicit Gram matrix input
- **Base ring:** Integer coefficients ℤⁿ as abelian group

---

### GAP IntegerLattices

```gap
# Lattice from integer matrix (basis columns)
L := Lattice( [ [1, 0], [1, 1] ] );
```

**Constraints:**
- ✓ **Gram matrix:** Implicitly positive-definite (Euclidean)
- ✗ **Indefinite forms:** Not directly supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ (integer vector operations)

**Operations:**
- `LLLReducedBasis()` – LLL on positive-definite form
- `NullspaceIntMat()` – general integer matrix kernel
- `HermiteNormalFormIntegerMat()` – HNF (base ring = ℤ)

---

### Macaulay2 LLLBases

```m2
B = {{1, 0}, {1, 1}};
lllBasis(B)  -- LLL-reduced basis
```

**Constraints:**
- ✓ **Gram matrix:** Euclidean (positive-definite)
- ✗ **Indefinite forms:** Not supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ (Euclidean lattices)

**Note:** `LLLBases` is a thin wrapper around Euclidean lattice reduction.

---

### Julia Indefinite.jl

```julia
# Indefinite lattices via Gram matrix
using Indefinite

G = [2 1; 1 -2]  # Signature (1, 1) -- indefinite!
L = Lattice(G)

# Test equivalence (works for indefinite)
are_isometric(L1, L2)  # true if indefinite forms are equivalent
```

**Constraints:**
- ✓ **Gram matrix:** Both positive-definite and indefinite supported
- ✓ **Indefinite forms:** **Primary use case**; Gram matrix can have negative eigenvalues
- ✓ **Custom bilinear forms:** Via explicit Gram matrix input
- **Base ring:** ℤⁿ (integer lattices)

**Key difference:** Unlike SageMath/fpylll, Indefinite.jl **expects** indefinite forms:
- `FindAutomorphisms(L)` – automorphism group (works for indefinite)
- `IsometricEquivalent(L1, L2)` – equivalence test (indefinite)
- No SVP/CVP (these require PD); use enumeration utilities instead

---

### Julia LatticeAlgorithms.jl

```julia
using LatticeAlgorithms

B = [1 0; 1 1]
reduced, U = lll(B)  # LLL reduction
```

**Constraints:**
- ✓ **Gram matrix:** Positive-definite (Euclidean)
- ✗ **Indefinite forms:** Not supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ

**Note:** Pure Julia implementation; slower than fplll-based packages.

---

### Julia Oscar.jl (Hecke Module)

```julia
using Oscar

# Via Gram matrix (positive-definite)
G = [2 1; 1 2]
L = lattice(G)

# Genus-based (supports indefinite)
Lndef = lattice(:hyperbolic, 2, 0)  # Indefinite hyperbolic plane
```

**Constraints:**
- ✓ **Gram matrix:** Both PD and indefinite
- ✓ **Indefinite forms:** Via genus specification (e.g., hyperbolic, split)
- ✓ **Custom bilinear forms:** Via explicit Gram matrix or genus theory
- **Base ring:** ℤⁿ (integer lattices), ℚⁿ (number fields via Nemo/Hecke)

**Key methods:**
- `is_positive_definite()` – checks PD
- `signature()` – returns (r, s)
- `genus()` – returns genus (includes indefinite case)

**See also:** Julia QuadSpace for general quadratic spaces.

---

### Julia ZZLat.jl

```julia
using ZZLat

# Positive-definite
L = ZZLat(gram_matrix)

# Indefinite (via genus theory)
g = Genus(signature=(1,1), level=2)
L = ZZLat(g)
```

**Constraints:**
- ✓ **Gram matrix:** Both PD and indefinite
- ✓ **Indefinite forms:** Via explicit genus or signature
- ✓ **Custom bilinear forms:** Via explicit Gram matrix
- **Base ring:** ℤⁿ (genus theory lattices)

**Key methods:**
- `is_positive_definite()` – PD check
- `signature()` – (r, s) pair
- `genus()` – genus invariants (handles indefinite)

---

### Julia QuadSpace

```julia
using Oscar

# Over rationals with indefinite form
F = QQ
q = [1, 0, -1]  -- diagonal form 1*x^2 - z^2
V = quadratic_space(F, q)

# Indefinite quadratic space
```

**Constraints:**
- ✓ **Gram matrix:** Both PD and indefinite
- ✓ **Indefinite forms:** Designed for general bilinear forms
- ✓ **Custom bilinear forms:** Via quadratic form specification
- **Base ring:** Any field in Nemo (ℚ, finite fields, number fields, etc.)

**Note:** QuadSpace is **not** a lattice per se, but a quadratic vector space. Used as foundation for ZZLat, Oscar lattice operations.

---

### PARI/GP qflll

```gp
M = [1, 0; 1, 1]
T = qflll(M)  -- LLL reduction
```

**Constraints:**
- ✓ **Gram matrix:** Positive-definite (Euclidean, implicit)
- ✗ **Indefinite forms:** Not supported (SVP/CVP explicitly require PD)
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤ, ℚ (exact/rational/floating-point)

**Base ring details:**
- `qflll()` – works on ℤ, ℚ, or floats
- `mathnf()`, `mathnfmod()` – base ring ℤ only
- `qfminim()`, `qfcvp()` – require PD form

**Reference (official docs):**
> "For qfminim/qfcvp, the matrix must correspond to a positive-definite quadratic form."

---

### Python fpylll

```python
from fpylll import IntegerMatrix, LLL

B = IntegerMatrix(2, 2)
B[0] = [1, 0]
B[1] = [1, 1]
LLL.reduction(B)
```

**Constraints:**
- ✓ **Gram matrix:** Euclidean (positive-definite), implicit = B·B^T
- ✗ **Indefinite forms:** Not supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ (integer vectors only)

**Note:** fpylll is the Python wrapper around **fplll** C++ library. All reduction (LLL, BKZ) and enumeration (SVP, CVP) assume Euclidean inner product.

**Workaround for custom forms:** Use SageMath `IntegralLattice` or Julia `Indefinite.jl`.

---

### Mathematica/Wolfram Language

```mathematica
B = {{1, 0}, {1, 1}};
LatticeReduce[B]
```

**Constraints:**
- ✓ **Gram matrix:** Euclidean (positive-definite), implicit
- ✗ **Indefinite forms:** Not supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ (integer vectors)

**Note:** `LatticeReduce` uses standard Euclidean norm. No built-in indefinite support.

---

### C++ NTL

```cpp
#include <NTL/LLL.h>

mat_ZZ B;
// ... initialize B ...
LLL_FP(B, 0, 0.99);  // LLL reduction
```

**Constraints:**
- ✓ **Gram matrix:** Euclidean (positive-definite)
- ✗ **Indefinite forms:** Not supported
- ✗ **Custom bilinear forms:** Not supported
- **Base ring:** ℤⁿ (arbitrary-precision integers)

**Note:** NTL provides precision-selectable reduction (FP, QP, XD, RR) but all assume Euclidean inner product.

---

## Decision Tree: Choosing the Right System

**Q: Do you need indefinite forms?**

- **Yes** → Julia (Oscar.jl, ZZLat.jl, Indefinite.jl, Lattices.jl) or SageMath IntegralLattice
- **No** → Any system works; choose based on other criteria (speed, features, etc.)

**Q: Do you need custom bilinear forms (non-Euclidean)?**

- **Yes, positive-definite** → SageMath IntegralLattice, Julia Oscar.jl/ZZLat.jl
- **Yes, indefinite** → Julia Indefinite.jl, Oscar.jl, ZZLat.jl, Lattices.jl, SageMath IntegralLattice
- **No** → Any system

**Q: Do you need SVP/CVP enumeration?**

- **Yes, positive-definite** → fpylll (fastest), NTL, SageMath IntegerLattice, PARI/GP qfminim/qfcvp
- **Yes, indefinite** → Julia Indefinite.jl utilities, Oscar.jl (limited)
- **No** → Any system

**Q: What's the base ring?**

- **ℤⁿ (integers)** → All systems support
- **ℚⁿ (rationals)** → PARI/GP qflll, SageMath (via FreeQuadraticModule), Julia QuadSpace
- **Number fields / Finite fields** → Julia Oscar.jl, Julia QuadSpace

---

## References

- **SageMath:** https://doc.sagemath.org/html/en/reference/modules/
- **GAP:** https://www.gap-system.org/
- **Macaulay2:** https://macaulay2.com/
- **Julia Indefinite.jl:** https://github.com/...
- **Julia Oscar.jl:** https://www.oscar-system.org/
- **PARI/GP:** https://pari.math.u-bordeaux.fr/
- **fpylll:** https://fpylll.readthedocs.io/
- **NTL:** https://www.shoup.net/ntl/
