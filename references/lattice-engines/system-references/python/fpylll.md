# fpylll - Python LLL/BKZ Lattice Reduction Documentation

Complete reference for fpylll, the Python wrapper for fplll lattice reduction library.

## Installation

```bash
pip install fpylll
```

Requires: GMP/MPIR, MPFR, fplll C++ library

---

## Core Classes

### Integer Matrices

```python
from fpylll import IntegerMatrix

IntegerMatrix(rows: int, cols: int) -> IntegerMatrix
```

Create m×n integer matrix (dense).

```python
IntegerMatrix.random(rows: int, kind: str, **kwargs) -> IntegerMatrix
```

Generate random lattice matrix. Kinds:
- `'uniform'` – uniform random entries
- `'qary'` – q-ary lattice (param: `k=rank`, `q=modulus`, `bits=bit_length`)
- `'intrel'` – integer relation (param: `bits=bit_length`)
- `'ntrulike'` – NTRU-like matrix

**Example:**
```python
B = IntegerMatrix.random(50, "qary", k=25, q=7681)
```

---

### Gram-Schmidt Orthogonalization

```python
from fpylll import GSO

GSO.Mat(B: IntegerMatrix, update: bool = False, float_type: str = "d", 
        U: IntegerMatrix | None = None, UinvT: IntegerMatrix | None = None) -> MatGSO
```

Create Gram-Schmidt object for matrix B.

**Parameters:**
- `B` – Integer matrix (basis rows)
- `update` – Compute GSO on creation
- `float_type` – Precision: 'd' (double), 'dd' (double-double), 'qd' (quad-double), 'mpfr'
- `U`, `UinvT` – Transformation matrices

**Methods:**
- `update_gso() -> None` – Compute/update Gram-Schmidt
- `get_r(i: int, j: int) -> float` – Get GSO R-factor
- `babai(v: Vector, gso: bool = False) -> Vector` – Babai's nearest plane algorithm
- `multiply_left(v: Vector) -> Vector` – v * B
- `from_canonical(v: Vector) -> Vector` – Convert to lattice coordinates

---

## LLL Reduction

```python
from fpylll import LLL

LLL.reduction(B: IntegerMatrix, U: IntegerMatrix | None = None,
              delta: float = 0.99, eta: float = 0.51,
              method: str | None = None, float_type: str | None = None,
              precision: int = 0, flags: int = 0) -> IntegerMatrix
```

Run LLL reduction, modifying B in-place.

**Parameters:**
- `B` – Integer matrix (modified in-place)
- `U` – Optional transformation matrix
- `delta` – LLL parameter, 0.25 < δ ≤ 1
- `eta` – LLL parameter, 0.5 ≤ η < √δ
- `method` – 'wrapper' (auto), 'proved', 'heuristic', 'fast', or None
- `float_type` – Precision type
- `precision` – Bit precision for 'mpfr'
- `flags` – LLL_VERBOSE, LLL_EARLY_RED, LLL_SIEGEL, etc.

**Output:**
- Modified matrix B

**Example:**
```python
from fpylll import LLL, IntegerMatrix

B = IntegerMatrix.random(40, "qary", k=20)
LLL.reduction(B, delta=0.99, eta=0.51)
print(B[0].norm())  # First vector norm
```

---

```python
LLL.is_LLL_reduced(M: MatGSO | IntegerMatrix, 
                  delta: float = 0.99, eta: float = 0.51) -> bool
```

Test if basis satisfies LLL reduction conditions.

---

## Lattice Enumeration

```python
from fpylll import Enumeration

Enumeration(M: MatGSO, strategy: str = "BEST_N_SOLUTIONS", 
            sub_solutions: bool = False) -> Enumeration
```

Create enumeration object for SVP/CVP/BDD.

**Methods:**
- `enumerate(first: int, last: int, max_dist: float, max_dist_expo: int,
             target: Vector | None = None, subtree: ... = None, 
             pruning: ... = None, dual: bool = False) -> list[tuple[int, float]]`
  - Find vectors in sublattice with ‖v‖² ≤ max_dist
  - Returns list of (coefficient_vector, norm²) pairs
  - target=None: SVP, target set: CVP/BDD

**Example:**
```python
from fpylll import Enumeration, GSO, LLL, IntegerMatrix

B = IntegerMatrix.random(45, "qary", k=25)
M = GSO.Mat(B)
LLL.reduction(M)
M.update_gso()

enum = Enumeration(M)
result = enum.enumerate(0, 45, 0.9 * M.get_r(0, 0), 0)
for coeff, norm_sq in result:
    print(f"Norm² = {norm_sq}")
```

---

## BKZ Reduction

```python
from fpylll.algorithms.bkz import BKZReduction

BKZReduction(B: IntegerMatrix | MatGSO) -> BKZReduction
```

Create BKZ reduction object.

**Methods:**
- `__call__(params: BKZ.Param, tracer: ... | None = None) -> ..._
  - Run BKZ with given parameters
  - Optional tracer for statistics

```python
class BKZ.Param:
    def __init__(self, block_size: int, 
                 strategies: list | None = None,
                 max_loops: int | None = None,
                 flags: int = 0,
                 ...):
        pass
    
    # Preset parameters
    @staticmethod
    EasyParam(block_size: int, max_loops: int | None = None) -> Param
```

**Flags:**
- `BKZ.AUTO_ABORT` – Stop on no improvement
- `BKZ.MAX_LOOPS` – Use max_loops limit
- `BKZ.VERBOSE` – Print progress

**Example:**
```python
from fpylll.algorithms.bkz import BKZReduction, BKZ

B = IntegerMatrix.random(60, "qary", k=30)
bkz = BKZReduction(B)
bkz(BKZ.EasyParam(20, max_loops=8))
print(B[0].norm())  # After BKZ
```

---

## Utilities

```python
from fpylll import FPLLL

FPLLL.set_random_seed(seed: int) -> None
FPLLL.set_precision(bits: int) -> None
FPLLL.set_temp_precision(bits: int) -> int
```

Configure global FPLLL state.

---

```python
from fpylll.util import vector_norm, gaussian_heuristic, get_root

vector_norm(v: list | Vector) -> float
```

Euclidean norm of vector.

```python
gaussian_heuristic(M: MatGSO | list[float]) -> float
```

Gaussian heuristic for expected shortest vector.

---

## Configuration

```python
from fpylll import config

config.float_types  # Available: ('d', 'dd', 'qd', 'mpfr')
config.default_float_type  # Current default
```

---

## Constraints & Notes

**⚠️ Positive-definite assumption:** fpylll assumes lattices have **positive-definite Gram matrices**. All reduction (LLL, BKZ) and enumeration (SVP/CVP) require the standard Euclidean inner product with positive-definite quadratic form. Indefinite forms are **not supported**.

- **Base ring:** Integer vectors only (no rational lattices via coeff multiplication)
- **Gram matrix:** Implicitly = B·B^T (Euclidean)
- **Custom bilinear forms:** Not supported; use SageMath `IntegralLattice` or Julia `Indefinite.jl` instead

---

## Reference

**Docs:** https://fpylll.readthedocs.io
**Repo:** https://github.com/fplll/fpylll
**License:** GNU Lesser General Public License v2.1+
