# Tests for Modules(R).Constructors().CombinatorialFreeModule and related
# submodule / quotient workflows.
#
# Assertions sourced from official Sage examples in:
# - sage.combinat.free_module
# - sage.categories.modules_with_basis
# - doc.sagemath.org reference/modules/modules_with_basis.html

import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parents[4]))

from sage.all import QQ, ZZ
from category_specs.modules import Modules

MQQ = Modules(QQ).Constructors()
MZZ = Modules(ZZ).Constructors()

# ---------------------------------------------------------------------------
# Basic named-basis operations  (combinat.free_module docstring)
# ---------------------------------------------------------------------------

F = MQQ.CombinatorialFreeModule(['a', 'b', 'c'])
b = F.basis()

assert F.monomial('a') == b['a']
assert F.monomial('c') == b['c']
assert (2 * b['a'] + 3 * b['b']).monomial_coefficients() == {'a': 2, 'b': 3}

# ---------------------------------------------------------------------------
# module_morphism(on_basis=...)  (with_basis.morphism / combinat docs)
# ---------------------------------------------------------------------------

X = MZZ.CombinatorialFreeModule([-2, -1, 1, 2])
Y = MZZ.CombinatorialFreeModule([1, 2])
x = X.basis()
y = Y.basis()

phi = X.module_morphism(on_basis=Y.monomial * abs, codomain=Y)
assert phi(x[-2]) == y[2]
assert phi(x[-1] + x[2]) == y[1] + y[2]

# ---------------------------------------------------------------------------
# quotient_module(...) for modules with basis  (modules_with_basis docs)
# ---------------------------------------------------------------------------

QX = MQQ.CombinatorialFreeModule(range(3), prefix='x')
qx = QX.basis()
QY = MQQ.quotient_module(
    QX,
    QX.submodule([qx[0] - qx[1], qx[1] - qx[2]], already_echelonized=True),
    already_echelonized=True,
)
qy = QY.basis()

assert list(qy.keys()) == [2]
assert qy[2].lift() == qx[2]
assert QY.retract(qx[0] + 2 * qx[1]) == 3 * qy[2]
