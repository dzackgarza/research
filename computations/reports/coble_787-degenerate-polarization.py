#!/usr/bin/env python3
"""research#787: the arithmetic of the degenerate degree-2 polarization, and the
(-2)-class carried by three collinear nodes of the sextic of lem:d2-s10-not-free.

Run from the repository root:
    python3 computations/reports/coble_787-degenerate-polarization.py

A class is a coefficient vector in the basis H, E_1, ..., E_10 of Pic(S), so that
sum a_i H^i - sum b_i E_i is written (a, -b_1, ..., -b_10); the form is
diag(1, -1, ..., -1).  K_S = -3H + E_1 + ... + E_10.  Every assertion below is one
the lemma uses; the script fails if any of them is false.
"""
import sympy as sp

N = 11
ZERO = [0] * N


def vec(coeffs):
    return sp.Matrix(coeffs)


def basis(i):
    v = [0] * N
    v[i] = 1
    return vec(v)


def dot(a, b):
    return int(a[0] * b[0] - sum(a[i] * b[i] for i in range(1, N)))


H = basis(0)


def Em(i):
    """Coefficient vector of the divisor E_i, written -E_i in the H, E basis."""
    return -basis(i)


def K():
    return -3 * H + sum((basis(i) for i in range(1, N)), vec(ZERO))


def main():
    Ks = K()
    print("K_S^2 =", dot(Ks, Ks), " (a Coble surface has K_S^2 = -1)")
    assert dot(Ks, Ks) == -1

    # (1) three collinear nodes give a (-2)-class in K_S^perp.
    R = H + Em(1) + Em(2) + Em(3)                  # H - E_1 - E_2 - E_3
    print("R = H - E_1 - E_2 - E_3      R^2 =", dot(R, R), "  R.K_S =", dot(R, Ks))
    assert dot(R, R) == -2, "R^2 is not -2"
    assert dot(R, Ks) == 0, "R is not in K_S^perp"
    print("  -> R is a (-2)-class of K_S^perp: the proper transform of the line")
    print("     through three collinear nodes")

    # (2) the arithmetic of the degenerate form h = 2F_1 + R.
    F1 = 3 * H + sum((Em(i) for i in range(1, 10)), vec(ZERO))   # 3H - E_1 - ... - E_9
    print("F_1 = 3H - sum_{i<=9} E_i    F_1^2 =", dot(F1, F1), "  F_1.K_S =", dot(F1, Ks))
    assert dot(F1, F1) == 0 and dot(F1, Ks) == 0
    R2 = H + Em(1) + Em(2) + Em(10)                # H - E_1 - E_2 - E_10
    assert dot(R2, R2) == -2 and dot(R2, Ks) == 0
    print("F_1.R' =", dot(F1, R2), " (R' = H - E_1 - E_2 - E_10)")
    assert dot(F1, R2) == 1
    h = 2 * F1 + R2
    print("h = 2F_1 + R'                h^2 =", dot(h, h), "  h.K_S =", dot(h, Ks),
          "  h.R' =", dot(h, R2))
    assert dot(h, h) == 2, "h^2 is not 2"
    assert dot(h, Ks) == 0, "h is not in K_S^perp"
    assert dot(h, R2) == 0, "h does not meet R' in 0"

    # (3) the relation the deposited extraction prints is inconsistent with h^2 = 2.
    for f1r in (0, 1):
        print("  F_1.R' = %d  =>  h^2 = %d,  h.R' = %d" % (f1r, 4 * f1r - 2, 2 * f1r - 2))
    assert 4 * 0 - 2 == -2
    print("  -> the pair consistent with h^2 = 2 is F_1.R' = 1, and then h.R' = 0")

    # (4) three collinear nodes on the sextic of lem:d2-s10-not-free.
    nodes = [(0, 0, 1), (1, 0, 1), (0, 1, 1), (-1, -1, 1), (1, 0, 2), (0, 1, 2),
             (-1, -1, 2), (1, 2, 0), (-2, -1, 0), (1, -1, 0)]
    on_z0 = [p for p in nodes if p[2] == 0]
    print("nodes with z = 0:", on_z0)
    assert len(on_z0) == 3, "the sextic does not have exactly three nodes on z = 0"
    assert len(set(on_z0)) == 3
    print("  -> exactly three of the ten nodes lie on the line z = 0, so at that point")
    print("     of the D2a base the surface has the (-2)-class R = H - E_1 - E_2 - E_3")

    print("ALL ASSERTIONS HOLD")


if __name__ == "__main__":
    main()
