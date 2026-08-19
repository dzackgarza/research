r"""
Verify that the rational sextic from the parametrization [P(t):R(t):Q(t)]
has exactly 10 A1 nodes (ordinary double points) and no other singularities.

Parametrization:
    P(t) = t^6 - t^5 - t^4 + t
    R(t) = -t^6 - t^5 + t^4 + t^2 - 1
    Q(t) = -t^6 + t^5 + t^3 - t^2 + 1

All verification steps are exact (over QQ / QQbar).
"""

from __future__ import annotations

import pytest
from sage.all import QQ, Ideal, PolynomialRing, QQbar

# ---------------------------------------------------------------------------
# Fixtures: compute the implicit equation once
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def parametrization():
    """Return the three parametrization polynomials in QQ[t]."""
    R_t = PolynomialRing(QQ, "t")
    t = R_t.gen()
    P = t**6 - t**5 - t**4 + t
    R = -(t**6) - t**5 + t**4 + t**2 - 1
    Q = -(t**6) + t**5 + t**3 - t**2 + 1
    return P, R, Q


@pytest.fixture(scope="module")
def implicit_affine(parametrization):
    """Compute the affine implicit equation F(x,y) via resultant."""
    P_poly, R_poly, Q_poly = parametrization
    Rxy = PolynomialRing(QQ, ["x", "y"])
    Rxyt = PolynomialRing(Rxy, "t")
    x, y = Rxy.gens()

    # Lift parametrization to Rxyt
    P_t = Rxyt(P_poly)
    R_t = Rxyt(R_poly)
    Q_t = Rxyt(Q_poly)

    Px = P_t - Rxyt(x) * Q_t
    Rx = R_t - Rxyt(y) * Q_t
    return Px.resultant(Rx)


@pytest.fixture(scope="module")
def homogeneous_F(implicit_affine):
    """Homogenize the affine implicit equation to P^2."""
    R3 = PolynomialRing(QQ, ["X", "Y", "Z"])
    X, Y, Z = R3.gens()
    return R3(implicit_affine).homogenize(Z)


@pytest.fixture(scope="module")
def affine_singular_points(implicit_affine):
    """Compute singular points in chart z=1 via Groebner basis."""
    R2 = PolynomialRing(QQ, ["u", "v"])
    u, v = R2.gens()
    f = R2(implicit_affine)
    singular_ideal = Ideal([f, f.derivative(u), f.derivative(v)])
    return singular_ideal.variety(QQbar), f


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestRationalSextic:
    """Verify the rational sextic has exactly 10 A1 nodes."""

    def test_degree_six(self, implicit_affine):
        assert implicit_affine.total_degree() == 6

    def test_irreducible(self, implicit_affine):
        factors = implicit_affine.factor()
        assert len(factors) == 1
        assert factors[0][1] == 1

    def test_ten_singular_points(self, affine_singular_points):
        V, _ = affine_singular_points
        assert len(V) == 10

    def test_no_singularities_at_infinity(self, homogeneous_F):
        R3 = homogeneous_F.parent()
        X, Y, Z = R3.gens()
        F_inf = homogeneous_F.subs({Z: 0})
        R1 = PolynomialRing(QQ, "w")
        w = R1.gen()
        F_inf_w = R1(F_inf.subs({X: w, Y: 1}))
        g = F_inf_w.gcd(F_inf_w.derivative(w))
        assert g.degree() == 0

    def test_all_singularities_are_a1(self, affine_singular_points):
        V, f = affine_singular_points
        u, v = f.parent().gens()
        f_uu = f.derivative(u, 2)
        f_vv = f.derivative(v, 2)
        f_uv = f.derivative(u).derivative(v)
        hessian = f_uu * f_vv - f_uv**2
        for pt in V:
            h_val = QQbar(hessian.subs({u: pt[u], v: pt[v]}))
            assert h_val != 0

    @pytest.mark.slow
    def test_twenty_ordered_self_intersection_pairs(self, parametrization):
        """10 nodes => 20 ordered (t,s) pairs with t != s."""
        S2 = PolynomialRing(QQ, ["t", "s"])
        t, s = S2.gens()

        P_t = t**6 - t**5 - t**4 + t
        R_t = -(t**6) - t**5 + t**4 + t**2 - 1
        Q_t = -(t**6) + t**5 + t**3 - t**2 + 1

        P_s = s**6 - s**5 - s**4 + s
        R_s = -(s**6) - s**5 + s**4 + s**2 - 1
        Q_s = -(s**6) + s**5 + s**3 - s**2 + 1

        minor_PR = P_t * R_s - P_s * R_t
        minor_PQ = P_t * Q_s - P_s * Q_t
        minor_RQ = R_t * Q_s - R_s * Q_t

        minor_PR_off = minor_PR // (t - s)
        minor_PQ_off = minor_PQ // (t - s)
        minor_RQ_off = minor_RQ // (t - s)

        I_self = Ideal([minor_PR_off, minor_PQ_off, minor_RQ_off])
        V_self = I_self.variety(QQbar)
        assert len(V_self) == 20
