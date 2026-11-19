"""Item 1f: the transitivity shortcut is not available -- T_En is 2-elementary, not unimodular.

A draft route to item 1f was to prove that Gamma_En is transitive on the primitive isotropic
vectors of T_En (then every divisibility-2 class would be orthogonal to a root, and Phi would be
onto the divisibility-2 locus).  The route transplants the proof of lem:I29-plus-line-transitivity,
which splits the lattice at a primitive isotropic vector by cor:hyperbolic-splitting -- and that
corollary requires the lattice to be *unimodular*.

T_En is not unimodular.  The common confusion is with the Enriques lattice U + E8(-1), which is
unimodular of signature (1,9) and rank 10, but T_En is the transcendental lattice U + U(2) + E8(2)
of the report: rank 12, signature (2,10), even, 2-elementary with A_{T_En} = (Z/2)^10 by
[@AEGS25, Def. 2.3, printed p. 586].  This probe computes those invariants and records the
consequence: the splitting route does not apply, and Gamma_En = O~^+(T_En) is a *proper* subgroup of
O^+(T_En), so the same phenomenon that gives 527 orbits for T_Co rather than one is present here.

Usage: python3 computations/reports/coble_658-ten-transitivity-probe.py
"""

from __future__ import annotations


def e8_cartan():
    c = [[0] * 8 for _ in range(8)]
    for i in range(8):
        c[i][i] = 2
    for i in range(6):
        c[i][i + 1] = c[i + 1][i] = -1
    c[2][7] = c[7][2] = -1
    return c


def block_diagonal(blocks):
    n = sum(len(b) for b in blocks)
    g = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                g[off + i][off + j] = b[i][j]
        off += len(b)
    return g


U = [[0, 1], [1, 0]]
U2 = [[0, 2], [2, 0]]                                    # U(2)
E82 = [[-2 * x for x in row] for row in e8_cartan()]     # E8(2): squares 2*(-2) = -4 on the roots
TEN = block_diagonal([U, U2, E82])                       # T_En = U + U(2) + E8(2), rank 12
ENR = block_diagonal([U, [[-x for x in row] for row in e8_cartan()]])   # the Enriques lattice U + E8(-1)


def det_bareiss(m):
    a = [[x for x in row] for row in m]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next(r for r in range(k + 1, n) if a[r][k] != 0)
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
        prev = a[k][k]
    return sign * a[n - 1][n - 1]


def signature(m):
    """Sylvester's law of inertia numerically: the sign counts are exact for these small integer forms."""
    import numpy as np
    w = np.linalg.eigvalsh(np.array(m, dtype=float))
    return int((w > 1e-9).sum()), int((w < -1e-9).sum())


def main():
    for name, g in (("T_En = U+U(2)+E8(2)", TEN), ("U + E8(-1) (Enriques)", ENR)):
        n = len(g)
        even = all(g[i][i] % 2 == 0 for i in range(n))   # even lattice: the diagonal, not every entry
        d = det_bareiss(g)
        p, q = signature(g)
        print("%-18s rank %2d   even %s   det %+d   signature (%d,%d)"
              % (name, n, even, d, p, q))
        assert even
    print()
    print("T_En is even of signature (2,10) with |det| = 1024 = 2^10: 2-elementary, NOT unimodular.")
    print("The Enriques lattice U + E8(-1) is the unimodular one, of signature (1,9) and rank 10.")
    print()
    print("verdict: the transitivity shortcut for item 1f is REFUTED.  cor:hyperbolic-splitting needs a")
    print("  unimodular lattice, so it does not split T_En at an isotropic vector; and since")
    print("  A_{T_En} = (Z/2)^10 is nonzero, Gamma_En = O~^+(T_En) is a proper subgroup of O^+(T_En),")
    print("  acting through its image in O(A_{T_En}).  The map v |-> v* in A_{T_En} is invariant under")
    print("  all of O(T_En), so Gamma_En-orbits are refined by discriminant classes: transitivity cannot")
    print("  follow from an O^+-transitivity theorem even if T_En were unimodular.  Item 1f's content")
    print("  is the orbit computation itself, as it was for the 527 orbits of T_Co.")


if __name__ == "__main__":
    main()
