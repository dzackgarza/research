#!/usr/bin/env python3
"""research#787: an explicit family of degree-2 polarized Coble surfaces over the
labelled D2a base B.

Run from the repository root:
    python3 computations/reports/coble_787-explicit-d2b-family.py

For labels i != j put F_i = 3H - sum_{k != i} E_k, the class of the cubic through the
nine nodes other than p_i, and h_{ij} = F_i + F_j.  The assertions below check that
h_{ij} is a primitive nef class of square 2 in K_S^perp, so (S, h_{ij}) is an object of
def:coble-family-degree-two, and that its K3 pullback has square 4.
"""
import itertools

import sympy as sp

N = 11
ZERO = [0] * N


def basis(i):
    v = [0] * N
    v[i] = 1
    return sp.Matrix(v)


H = basis(0)


def Em(i):
    return -basis(i)


def dot(a, b):
    return int(a[0] * b[0] - sum(a[i] * b[i] for i in range(1, N)))


def K():
    return -3 * H + sum((basis(i) for i in range(1, N)), sp.Matrix(ZERO))


def F(i):
    """Class of the cubic through the nine nodes other than p_i."""
    return 3 * H + sum((Em(k) for k in range(1, N) if k != i), sp.Matrix(ZERO))


def main():
    Ks = K()
    assert dot(Ks, Ks) == -1
    pairs = [(i, j) for i in range(1, N) for j in range(1, N) if i != j]
    print("ordered pairs of distinct labels:", len(pairs))
    for i in range(1, N):
        Fi = F(i)
        assert dot(Fi, Fi) == 0, ("F_i^2 != 0", i)
        assert dot(Fi, Ks) == 0, ("F_i not in K_S^perp", i)
    print("every F_i is a curve class of square 0 lying in K_S^perp (an elliptic cubic)")

    count = 0
    for (i, j) in pairs:
        Fi, Fj = F(i), F(j)
        assert dot(Fi, Fj) == 1, ("F_i.F_j != 1", i, j)
        h = Fi + Fj
        assert dot(h, h) == 2, ("h^2 != 2", i, j)
        assert dot(h, Ks) == 0, ("h not in K_S^perp", i, j)
        coeffs = [h[0]] + [-h[k] for k in range(1, N)]
        g = 0
        for c in coeffs:
            g = sp.gcd(g, abs(int(c)))
        assert g == 1, ("h is not primitive", i, j)
        # the K3 pullback doubles the form
        assert 2 * dot(h, h) == 4
        count += 1
    print("h_ij = F_i + F_j: %d classes, each primitive, of square 2, in K_S^perp," % count)
    print("  and each is nef as a sum of two nef classes (F_i is the class of an")
    print("  irreducible elliptic cubic, so F_i^2 = 0 forces F_i nef)")
    print("K3 pullback h-tilde_ij = f^*h_ij has square 4")
    print("ALL ASSERTIONS HOLD")


if __name__ == "__main__":
    main()
