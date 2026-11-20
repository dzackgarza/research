#!/usr/bin/env python3
"""research#797: whether A = 2H - E1 - E2 - E3 is a second plane model.

Run from the repository root:
    python3 computations/reports/coble_797-plane-models.py

A plane model of S is a contraction pi: S -> P^2 of ten disjoint (-1)-curves G_k
whose pullback A of the line class satisfies A.G_k = 0, A^2 = 1 and
-K_S = 3A - sum_k G_k.  The first two hold for A = 2H - E1 - E2 - E3 and the ten
curves H-E1-E2, H-E1-E3, H-E2-E3, E_4, ..., E_10; the third is checked below.
"""
import sympy as sp

N = 11
Z0 = [0] * N


def vec(coeffs):
    return sp.Matrix(coeffs)


H = vec([1] + [0] * (N - 1))


def Em(i):
    v = [0] * N
    v[i] = -1
    return vec(v)


def dot(a, c):
    return int(a[0] * c[0] - sum(a[i] * c[i] for i in range(1, N)))


def add(*vs):
    return sum(vs, vec(Z0))


def main():
    K = add(-3 * H, *[vec([1 if j == i else 0 for j in range(N)]) for i in range(1, N)])
    D = add(6 * H, *[2 * Em(i) for i in range(1, N)])
    assert D == -2 * K and dot(D, D) == -4
    print("K_S^2 =", dot(K, K), "  D = -2K_S, D^2 =", dot(D, D))

    G = [add(H, Em(1), Em(2)), add(H, Em(1), Em(3)), add(H, Em(2), Em(3))] + [Em(i) for i in range(4, N)]
    for g in G:
        assert dot(g, g) == -1
    for i in range(10):
        for j in range(i + 1, 10):
            assert dot(G[i], G[j]) == 0
    print("ten pairwise disjoint (-1)-curves: OK")

    A = add(2 * H, Em(1), Em(2), Em(3))
    print("A = 2H - E1 - E2 - E3:  A^2 =", dot(A, A), "  A.D =", dot(A, D),
          "  A.G_k =", sorted({dot(A, g) for g in G}))
    assert dot(A, A) == 1 and all(dot(A, g) == 0 for g in G)

    lhs = add(3 * A, *[-g for g in G])
    print("-K_S            =", list(-K))
    print("3A - sum_k G_k  =", list(lhs))
    assert lhs != -K, "the identity holds after all"
    print("=> 3A - sum_k G_k =/= -K_S, so (A, G_1..G_10) is NOT a plane model of S:")
    print("   A is orthogonal to the ten curves and has square 1, but the contraction")
    print("   they define is not the plane model that A comes from.")
    print("ALL ASSERTIONS HOLD")


if __name__ == "__main__":
    main()
