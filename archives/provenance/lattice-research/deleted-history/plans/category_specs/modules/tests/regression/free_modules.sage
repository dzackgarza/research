# Tests for Modules(R).Constructors().FreeModule / VectorSpace / span /
# quotient_module / ring-side module constructions.
#
# Assertions sourced from official Sage examples in:
# - sage.modules.free_module
# - doc.sagemath.org reference/modules/free_module.html

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parents[4]))

from sage.all import QQ, ZZ, identity_matrix, infinity, matrix
from category_specs.modules import Modules

MZZ = Modules(ZZ).Constructors()
MQQ = Modules(QQ).Constructors()

# ---------------------------------------------------------------------------
# Ambient free modules and vector spaces  (free_module.py examples)
# ---------------------------------------------------------------------------

F = MZZ.FreeModule(3)
assert F.rank() == 3
assert F.basis_matrix() == identity_matrix(ZZ, 3)

V = MQQ.VectorSpace(3)
assert V.dimension() == 3
assert V.cardinality() == infinity

# ---------------------------------------------------------------------------
# span(...) over a field and over ZZ  (free_module.span doctests)
# ---------------------------------------------------------------------------

Wq = MQQ.span([[1, 2, 5], [2, 2, 2]])
assert Wq.dimension() == 2
assert Wq.basis_matrix() == matrix(QQ, [[1, 0, -3], [0, 1, 4]])

Wz = MZZ.span([[1, 2, 5], [2, 2, 2]])
assert Wz.rank() == 2
assert Wz.basis_matrix() == matrix(ZZ, [[1, 0, -3], [0, 2, 8]])

# ---------------------------------------------------------------------------
# Quotients of vector spaces  (free_module.py quotient examples)
# ---------------------------------------------------------------------------

R = V.span([[1, 0, -1], [1, -1, 0]])
Q = MQQ.quotient_module(V, R)
q = Q.gen(0)

assert Q.cover() == V
assert Q.relations() == R
assert Q.lift_map()(q) == V.gen(0)
assert Q(Q.lift_map()(q)) == q

# ---------------------------------------------------------------------------
# Rings regarded as rank-one modules / ring objects as modules
# ---------------------------------------------------------------------------

R1 = MZZ.ring_as_rank_one_module()
assert R1.rank() == 1
assert R1.basis_matrix() == matrix(ZZ, [[1]])

S = MZZ.polynomial_ring_as_module(name='x')
assert S.base_ring() == ZZ
assert S.structure_ring() == ZZ
assert S.structure_map()(ZZ(3)) == S(3)
