r"""Category obligation examples for the public matrix-ring constructor split."""

import sys

sys.path.insert(0, "/home/dzack/research")

from category_specs.rings import Rings
from sage.all import ZZ, identity_matrix, matrix

NR = Rings().Constructors()
M = NR.MatrixRing(ZZ, 2)

assert M.nrows() == 2
assert M.ncols() == 2
assert M.base_ring() is ZZ
assert M in Rings().MatrixAlgebras(ZZ, 2, 2)

A = matrix(ZZ, [[1, 2], [3, 4]])

assert M.matrix_from_matrix(A) == A
assert M.matrix_from_entries([1, 2, 3, 4]) == A
assert M.matrix_from_rows([[1, 2], [3, 4]]) == A
assert M.scalar_matrix(3) == 3 * identity_matrix(ZZ, 2)
