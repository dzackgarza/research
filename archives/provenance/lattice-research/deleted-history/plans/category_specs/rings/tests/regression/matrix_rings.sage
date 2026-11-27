# Tests for Rings().Constructors().MatrixRing()
# Assertions sourced from sage.matrix.matrix_space doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.rings import Rings
from sage.all import ZZ, QQ, GF, matrix, identity_matrix

NR = Rings().Constructors()

# ---------------------------------------------------------------------------
# MatrixRing(QQ, 2) = M_2(QQ)  (MatrixSpace class docstring)
# ---------------------------------------------------------------------------

M2Q = NR.MatrixRing(QQ, 2)

assert M2Q.nrows() == 2
assert M2Q.ncols() == 2
assert M2Q.base_ring() is QQ
assert M2Q.is_commutative_ring() is False
assert M2Q.characteristic() == 0
assert M2Q.is_field() is False
assert M2Q.is_integral_domain() is False   # has zero divisors

# Identity element
I2 = M2Q.one()
assert I2 == identity_matrix(QQ, 2)
assert M2Q.zero() == matrix(QQ, 2, 2)

# Arithmetic: matrix multiplication is associative and non-commutative
A = M2Q([[1, 2], [3, 4]])
B = M2Q([[5, 6], [7, 8]])
assert A * B == M2Q([[19, 22], [43, 50]])
assert B * A == M2Q([[23, 34], [31, 46]])
assert A * B != B * A   # explicitly non-commutative

# Zero divisors: nilpotent element
N = M2Q([[0, 1], [0, 0]])
assert N ** 2 == M2Q.zero()
assert N != M2Q.zero()

# Invertible elements (units)
assert A.is_unit() is True   # det(A) = 4 - 6 = -2 ≠ 0
assert N.is_unit() is False  # det(N) = 0

# ---------------------------------------------------------------------------
# MatrixRing(ZZ, 3) = M_3(ZZ)
# ---------------------------------------------------------------------------

M3Z = NR.MatrixRing(ZZ, 3)

assert M3Z.nrows() == 3
assert M3Z.base_ring() is ZZ
assert M3Z.characteristic() == 0

# ---------------------------------------------------------------------------
# MatrixRing(GF(2), 2) = M_2(GF(2))
# ---------------------------------------------------------------------------

M2F2 = NR.MatrixRing(GF(2), 2)

assert M2F2.characteristic() == 2
assert M2F2.is_finite() is True
assert M2F2.cardinality() == 16  # |M_2(GF(2))| = 2^4

# ---------------------------------------------------------------------------
# Determinant, trace, rank
# ---------------------------------------------------------------------------

A_det = M2Q([[2, 3], [1, 4]])
assert A_det.determinant() == 5
assert A_det.trace() == 6
assert A_det.rank() == 2

A_sing = M2Q([[1, 2], [2, 4]])
assert A_sing.determinant() == 0
assert A_sing.is_unit() is False
assert A_sing.rank() == 1

# ---------------------------------------------------------------------------
# Category membership via spec
# ---------------------------------------------------------------------------

from plans.category_specs.rings import Rings as _Rings

assert M2Q in _Rings()
assert M2Q not in _Rings().CommutativeRings()
assert M2Q not in _Rings().Fields()
assert M2Q not in _Rings().IntegralDomains()
