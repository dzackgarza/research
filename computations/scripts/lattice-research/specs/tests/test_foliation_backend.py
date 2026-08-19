from __future__ import annotations

from ore_algebra.differential_operator_1_1 import (
    UnivariateDifferentialOperatorOverUnivariateRing,
)
from sage.all import QQ, SR, I, PolynomialRing, QQbar, matrix, pi
from sage.rings.polynomial.term_order import TermOrder
from src.coble_geometry_varieties import FamilyOfVarieties


class _ToyHypersurface:
    def __init__(self, equation):
        self._equation = equation

    def is_hypersurface(self):
        return True

    def equations(self):
        return [self._equation]


class _ToyDisc:
    def dimension(self):
        return 1


class _ToyHypersurfaceFamily(FamilyOfVarieties):
    def __init__(self, equation):
        self._domain = _ToyHypersurface(equation)
        self._codomain = _ToyDisc()

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def degree(self):
        return 1

    def is_finite(self):
        return False

    def is_étale(self):
        return False

    def fiber(self, s):
        return self._domain

    def specialization(self, s):
        return self._domain


def _elliptic_legendre_family():
    ring = PolynomialRing(
        QQ,
        names=("x", "y", "u"),
        order=TermOrder("wdegrevlex", (2, 3, 1)),
    )
    x, y, u = ring.gens()
    return _ToyHypersurfaceFamily(y**2 - x * (x - 1) * (x - u))


def test_legendre_family_picard_fuchs_data():
    family = _elliptic_legendre_family()

    assert family.milnor_number() == 2

    operator = family.picard_fuchs_operator()
    t = operator.base_ring().gen()
    alpha = family.indicial_polynomial().parent().gen()

    assert isinstance(operator, UnivariateDifferentialOperatorOverUnivariateRing)
    assert str(t) == "t"
    assert str(operator.parent().gen()) == "Dt"
    assert operator.order() == 2
    assert operator.list() == [
        -3 * t + 3,
        12 * t**2 + 8 * t - 4,
        12 * t**3 - 8 * t**2 - 4 * t,
    ]
    assert operator.leading_coefficient() == 12 * t**3 - 8 * t**2 - 4 * t
    assert str(operator) == ("(12*t^3 - 8*t^2 - 4*t)*Dt^2 + (12*t^2 + 8*t - 4)*Dt - 3*t + 3")
    assert family.indicial_polynomial() == -4 * alpha**2


def test_legendre_family_monodromy_data():
    family = _elliptic_legendre_family()
    monodromy = family.hodge_theoretic_monodromy()

    assert monodromy.log_monodromy_jordan_form == matrix(QQbar, [[0, 1], [0, 0]])
    assert monodromy.nilpotent_log_monodromy == matrix(QQbar, [[0, 1], [0, 0]])
    assert monodromy.semisimple_log_monodromy == matrix(QQbar, [[0, 0], [0, 0]])
    assert monodromy.nilpotent_monodromy_matrix == matrix(
        SR,
        [[0, 2 * I * pi], [0, 0]],
    )
    assert monodromy.unipotent_monodromy_matrix == matrix(
        SR,
        [[1, 2 * I * pi], [0, 1]],
    )
    assert family.monodromy_matrix() == matrix(SR, [[1, 2 * I * pi], [0, 1]])
    assert family.monodromy_jordan_form() == matrix(SR, [[1, 1], [0, 1]])

    assert len(monodromy.jordan_blocks) == 1
    assert monodromy.jordan_blocks[0].size == 2
    assert monodromy.jordan_blocks[0].exponent == 0
    assert monodromy.jordan_blocks[0].eigenvalue == 1
