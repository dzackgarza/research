#!/usr/bin/env python3
"""research#797: the second plane model of a ten-nodal Coble surface.

Run from the repository root:
    python3 computations/reports/coble_797-plane-models.py

A class is a coefficient vector c = (c_0, c_1, ..., c_10) in the basis
(H, E_1, ..., E_10), so that c represents c_0 H + sum c_i E_i; the form is
diag(1, -1, ..., -1).  K_S = -3H + sum E_i and D = -2K_S = 6H - 2 sum E_i.

The quadratic Cremona involution centred at p_1, p_2, p_3 replaces the plane model
with line class H by the plane model with line class A = 2H - E_1 - E_2 - E_3 and
exceptional curves H - E_1 - E_2, H - E_1 - E_3, H - E_2 - E_3, E_4, ..., E_10.
"""
import sympy as sp

N = 11
Z0 = [0] * N
H = sp.Matrix([1] + [0] * (N - 1))


def E(i):
    """Coefficient vector of the divisor E_i."""
    v = [0] * N
    v[i] = 1
    return sp.Matrix(v)


def dot(a, c):
    return int(a[0] * c[0] - sum(a[i] * c[i] for i in range(1, N)))


def add(*vs):
    return sum(vs, sp.Matrix(Z0))


def main():
    K = add(-3 * H, *[E(i) for i in range(1, N)])
    D = add(6 * H, *[-2 * E(i) for i in range(1, N)])
    assert D == -2 * K and dot(D, D) == -4 and dot(K, K) == -1
    print("K_S^2 = %d, D = -2K_S, D^2 = %d" % (dot(K, K), dot(D, D)))

    G = [add(H, -E(1), -E(2)), add(H, -E(1), -E(3)), add(H, -E(2), -E(3))]
    G += [E(i) for i in range(4, N)]
    assert len(G) == 10
    for g in G:
        assert dot(g, g) == -1, list(g)
    for i in range(10):
        for j in range(i + 1, 10):
            assert dot(G[i], G[j]) == 0, (i, j)
    print("ten pairwise disjoint (-1)-curves: OK")

    A = add(2 * H, -E(1), -E(2), -E(3))
    assert dot(A, A) == 1 and all(dot(A, g) == 0 for g in G)
    assert dot(A, D) == 6
    print("A = 2H - E1 - E2 - E3:  A^2 = 1,  A.G_k = 0 for all k,  A.D = 6")

    lhs = add(3 * A, *[-g for g in G])
    print("3A - sum_k G_k =", list(lhs))
    print("-K_S           =", list(-K))
    assert lhs == -K, "the plane-model identity fails"
    print("3A - sum_k G_k = -K_S: the fourth plane-model condition HOLDS")

    print("G_k.D =", sorted({dot(g, D) for g in G}), "(each exceptional curve meets the")
    print("  branch divisor in 2, so its image is a double point of the image sextic)")
    assert all(dot(g, D) == 2 for g in G)
    assert A != H
    print("A != H, so the two plane models differ")
    print("ALL ASSERTIONS HOLD")


if __name__ == "__main__":
    main()
