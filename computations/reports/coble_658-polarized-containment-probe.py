"""research#658 item 1e: if the polarized monodromy sits in the unpolarized one, the item fails.

LEMMA.  If Gamma_{Co,2} <= Gamma_Co then item 1e fails; consequently item 1e implies that Gamma_Co is a
proper subgroup of Gamma_{Co,2}.

PROOF.  The swap s of the two isotropic generators e', f' of the U(2) block is an integral isometry of T_Co
whose class action preserves the decomposition [h/2]^perp = A_{U(2)} + A_{E_8(2)} and is not the identity,
so s lies in rho^{-1}(P) = Gamma_{Co,2} and outside ker(rho_{T_Co}) (verified in
coble_658-polarized-not-kernel-probe.py).  If Gamma_{Co,2} <= Gamma_Co, then s lies in Gamma_Co, so
rho(Gamma_Co) is nontrivial, and by the dichotomy (coble_658-dichotomy-probe.py) item 1e fails.  []

The probe re-verifies the two facts about s: that it is an isometry of T_Co acting non-trivially on
A_{T_Co}, and that its class action fixes the E8(2) part, hence lies in P.

What the lemma does not say: which of the two holdings of the containment is true.  It says the natural
intuition -- the unpolarized family carries at least the polarized family's monodromy -- is incompatible with
item 1e.

Usage: python3 computations/reports/coble_658-polarized-containment-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F


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
G = block_diagonal([[[2]], [[2 * x for x in row] for row in U],
                    [[-2 * x for x in row] for row in e8_cartan()]])
N = len(G)


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def transpose(m):
    cols = len(m[0])
    return [[m[j][i] for j in range(len(m))] for i in range(cols)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def inverse(m):
    n = len(m)
    a = [[F(m[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if a[r][col] != 0)
        a[col], a[piv] = a[piv], a[col]
        pv = a[col][col]
        a[col] = [x / pv for x in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


GINV = inverse(G)


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(m):
    return is_integral(m) and matmul(transpose(m), matmul(G, m)) == G


def acts_trivially(m):
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(m, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def main():
    swap = [[int(i == j) for j in range(N)] for i in range(N)]
    swap[1][1] = swap[2][2] = 0
    swap[1][2] = swap[2][1] = 1                    # e' <-> f'
    print("T_Co = <2> + U(2) + E8(2), rank %d" % N)
    print("the swap s of e', f': isometry %s, acts trivially on A_{T_Co} %s"
          % (is_isometry(swap), acts_trivially(swap)))
    preserved = all(abs(mv(swap, [1 if i == k else 0 for i in range(N)])[j]) == 0
                    for k in range(3, N) for j in range(3))
    print("  preserves the E8(2) part, so rho(s) lies in P: %s" % preserved)
    assert is_isometry(swap) and not acts_trivially(swap) and preserved
    print()
    print("verdict: the lemma holds.  Since s lies in rho^{-1}(P) = Gamma_{Co,2} and has rho(s) != 1,")
    print("  any containment Gamma_{Co,2} <= Gamma_Co puts s in Gamma_Co and falsifies item 1e.  So item")
    print("  1e implies Gamma_Co is a PROPER subgroup of Gamma_{Co,2}: the unpolarized family cannot carry")
    print("  all the polarized monodromy if the item holds.")


if __name__ == "__main__":
    main()
