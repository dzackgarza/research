# Tests for Modules(ZZ).Constructors().IntegerLattice and
# Modules(ZZ).Constructors().TorsionQuadraticForm.
#
# Assertions sourced from official Sage examples in:
# - sage.modules.free_module_integer
# - sage.modules.torsion_quadratic_module
# - doc.sagemath.org reference/modules/free_module_integer.html
# - doc.sagemath.org reference/modules/torsion_quadratic_module.html

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parents[4]))

from sage.all import QQ, ZZ, diagonal_matrix, matrix, vector
from category_specs.modules import Modules

MZZ = Modules(ZZ).Constructors()

# ---------------------------------------------------------------------------
# IntegerLattice(...)  (free_module_integer docs)
# ---------------------------------------------------------------------------

L = MZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]])
assert L.basis_matrix() == matrix(ZZ, [[-2, 0, 0], [0, 2, 1], [1, -2, 2]])
assert L.gram_matrix() == matrix(ZZ, [[4, 0, -2], [0, 5, -2], [-2, -2, 9]])
assert L.shortest_vector() == vector(ZZ, [-2, 0, 0])

# ---------------------------------------------------------------------------
# TorsionQuadraticForm(q1)  (torsion_quadratic_module docstring)
# ---------------------------------------------------------------------------

q1 = matrix(QQ, 2, [1, QQ(1) / 2, QQ(1) / 2, 1])
T1 = MZZ.TorsionQuadraticForm(q1)
assert T1.invariants() == (2, 2)
assert T1.gram_matrix_quadratic() == matrix(QQ, [[1, QQ(1) / 2], [QQ(1) / 2, 1]])
assert T1.gram_matrix_bilinear() == matrix(QQ, [[0, QQ(1) / 2], [QQ(1) / 2, 0]])

# ---------------------------------------------------------------------------
# TorsionQuadraticForm(q2)  (torsion_quadratic_module docstring)
# ---------------------------------------------------------------------------

q2 = diagonal_matrix(QQ, [QQ(1) / 4, QQ(1) / 3])
T2 = MZZ.TorsionQuadraticForm(q2)
assert T2.invariants() == (12,)
assert T2.gram_matrix_quadratic() == matrix(QQ, [[QQ(7) / 12]])
