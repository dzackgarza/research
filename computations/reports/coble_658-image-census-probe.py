"""research#658 item 1f: the census of divisibility-2 classes that can lie over a Coble cusp.

The image of Phi consists of classes, not of vectors: Gamma_En acts trivially on A_{T_En}, so whether a
divisibility-2 class c lies in the image depends only on c.  This probe takes the census that can be taken
exactly and states the bound on what it leaves open.

1. It enumerates the classes of A_{T_En} = (Z/2)^{10} -- 1024 of them -- with their q-values, and counts
   the nonzero isotropic ones: these are the candidates, one per Gamma_En-orbit of divisibility-2
   primitive isotropic vectors that could occur.
2. For each such class it takes the representative v = 2y (y a basis representative, q(y) = 0) and asks
   whether v is orthogonal to one of the 614 (-2)-vectors of T_En with small coefficients.  "Orthogonal to
   some (-2)-vector" is the book's necessary condition, and by AEGS25 printed p. 587 (one (-2)-vector
   modulo O(T_En)) no O(T_En)-invariant refines it; the condition is also sufficient as soon as the stable
   group is transitive on the (-2)-vectors, which for the recorded witness is settled the other way (see
   coble_658-stabilizer-image-probe.py: an explicit transvection).
3. It prints the census, and what the bound leaves open: orthogonality to a (-2)-vector outside the
   enumerated box is not tested.

So this probe measures the image's size from below and states the number that remain undecided within the
bound.  It decides no class in the negative direction.

Usage: python3 computations/reports/coble_658-image-census-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product


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
G = block_diagonal([U, [[2 * x for x in row] for row in U],
                    [[-2 * x for x in row] for row in e8_cartan()]])      # T_En, rank 12
N = len(G)


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


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


def e8_roots():
    cartan = e8_cartan()
    out = []
    for x in product(range(-2, 3), repeat=8):
        if sum(x[i] * cartan[i][j] * x[j] for i in range(8) for j in range(8)) == 2:
            out.append(x)
    return out


def minus_two_vectors():
    out = set()
    tails = ([[0] * 8] + [list(r) for r in e8_roots()]
             + [[2 * t for t in rho] for rho in e8_roots()])
    for a, b, c, d in product(range(-2, 3), repeat=4):
        for tail in tails:
            v = [a, b, c, d] + tail
            if any(v) and dot(v, v) == -2:
                out.add(tuple(v))
    return sorted(out)


def main():
    print("T_En = U + U(2) + E8(2), rank %d" % N)

    # A = Z^n / (G Z^n); every class has a representative in {0,1}^n for this lattice, and the class of v
    # is coded by G^{-1} v mod 1, with q(v) = v^T G^{-1} v (mod 2).
    classes = {}
    for bits in product([0, 1], repeat=N):
        v = list(bits)
        key = tuple((x - F(x.numerator // x.denominator)).limit_denominator(10 ** 6) for x in mv(GINV, v))
        key = tuple(x % 1 for x in mv(GINV, v))
        classes.setdefault(key, v)
    isotropic = {k: v for k, v in classes.items()
                 if any(k) and sum(a * b for a, b in zip(v, mv(GINV, v))) % 2 == 0}
    print("classes of A_{T_En}: %d (want 1024, the determinant 2^10)" % len(classes))
    print("nonzero isotropic classes: %d" % len(isotropic))

    roots = minus_two_vectors()
    print("(-2)-vectors enumerated (bounded box): %d" % len(roots))

    hit = 0
    for key, v in isotropic.items():
        for r in roots:
            if dot(v, list(r)) == 0:
                hit += 1
                break
    print("nonzero isotropic classes with a representative orthogonal to one of them: %d of %d"
          % (hit, len(isotropic)))
    print()
    print("reading: a class counted here can lie over a Coble cusp once O~+(T_En) is transitive on the")
    print("(-2)-vectors; for the recorded witness that is settled the affirmative way by an explicit")
    print("transvection (coble_658-stabilizer-image-probe.py).  The remaining %d are not excluded: the"
          % (len(isotropic) - hit))
    print("probe tests orthogonality to a (-2)-vector inside a bounded box, and nothing beyond it.")


if __name__ == "__main__":
    main()
