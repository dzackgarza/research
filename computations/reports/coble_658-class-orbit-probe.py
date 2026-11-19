"""research#658 item 1f: the witness and eta(e') are in one class, so one transporter would decide it.

The image of Phi is the set of Gamma_En-classes of primitive isotropic vectors of divisibility 2 that
are orthogonal to some element of Gamma_En.k.  Write w = 2e~ + e~' for the witness of the book's passage
on the exact image locus, and e~' = eta(e') for a vector whose class IS in the image (e~'.k = 0).

What this probe verifies exactly, and what it is worth:

1. w and e~' are primitive isotropic of divisibility 2 and have THE SAME class in A_{T_En}:
   (w/2) - (e~'/2) in T_En.  So the pair is exactly the situation of thm:coble-zero-cusp-count(1) for
   T_Co, one lattice over.
2. Consequence, which is the reduction: if some g in ker(rho_{T_En}) carries e~' to +-w, then
   w = +-g(e~') is orthogonal to +-g(k), and g(k) lies in the Gamma_En-orbit of k, so w IS in the image
   of Phi.  The proof is one line and uses only that g preserves the form: (e~', k) = 0 gives
   (g e~', g k) = 0.  The witness therefore needs no orbit search of its own: it needs ONE transporter,
   and the class equality says the only obstruction to finding it is the transitivity of ker(rho_{T_En})
   on primitive isotropic vectors within a class -- the T_En analogue of thm:coble-zero-cusp-count(1),
   which the book proves for T_Co and not for T_En.
3. The search it runs: reflections in (-2)-vectors generate a subgroup of Gamma_En (integral, isometric,
   trivially acting on A_{T_En}, spinor norm [1]), and the orbit of e~' under words of length at most two
   is examined for +-w.  A hit is a certificate; a miss decides nothing, and the verdict says so.

Usage: python3 computations/reports/coble_658-class-orbit-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import gcd


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
                    [[-2 * x for x in row] for row in e8_cartan()]])
N = len(G)
DEPTH = 2


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


def multiline(name, value):
    print("%-46s %s" % (name, value))


def short_roots():
    cartan = e8_cartan()
    e8_roots = []
    for x in product(range(-2, 3), repeat=8):
        if sum(x[i] * cartan[i][j] * x[j] for i in range(8) for j in range(8)) == 2:
            e8_roots.append(x)
    out = set()
    for a, b, c, d in product(range(-2, 3), repeat=4):
        for rho in [None] + e8_roots:
            v = [a, b, c, d] + ([2 * t for t in rho] if rho else [0] * 8)
            if dot(v, v) == -2:
                out.add(tuple(v))
    return sorted(out)


def main():
    w = [0] * N
    w[0], w[2] = 2, 1
    ep = [0] * N
    ep[2] = 1
    k = [0] * N
    k[0], k[1] = 1, -1

    print("T_En = U + U(2) + E8(2), rank %d" % N)
    multiline("w = 2e~ + e~': square, divisibility", (dot(w, w), gcd(*[abs(sum(w[i] * G[i][j] for i in range(N))) for j in range(N)])))
    multiline("e~': square, divisibility", (dot(ep, ep), gcd(*[abs(sum(ep[i] * G[i][j] for i in range(N))) for j in range(N)])))
    cw = mv(GINV, [F(x, 2) for x in w])
    ce = mv(GINV, [F(x, 2) for x in ep])
    same_class = all((a - b).denominator == 1 for a, b in zip(cw, ce))
    multiline("(w/2) - (e~'/2) lies in T_En", same_class)
    multiline("e~' . k", dot(ep, k))
    assert same_class and dot(w, w) == 0 and dot(ep, ep) == 0 and dot(ep, k) == 0
    print()

    roots = short_roots()
    multiline("(-2)-vectors enumerated", len(roots))
    print("orbit of e~' under words in their reflections, length <= %d:" % DEPTH)
    layer = {tuple(ep)}
    found = None
    for depth in range(1, DEPTH + 1):
        nxt = set()
        for point in layer:
            for r in roots:
                coeff = dot(list(point), list(r))
                image = tuple(point[i] + coeff * r[i] for i in range(N))
                nxt.add(image)
                if image == tuple(w) or image == tuple(-t for t in w):
                    found = (depth, r)
                    break
            if found:
                break
        print("  depth %d: %d points" % (depth, len(nxt)))
        if found:
            break
        layer = nxt
    print()

    if found:
        print("CERTIFICATE: e~' is carried to +-w by a word of reflections of length %d." % found[0])
        print("verdict: the class of w = 2e~ + e~' IS in the image of Phi.")
    else:
        print("verdict: undecided -- no transporter found within length %d." % DEPTH)
        print("  What is decided is the reduction, which does not depend on the bound: w and e~' have the")
        print("  same class in A_{T_En}, so ONE element of ker(rho_{T_En}) carrying e~' to +-w puts w in the")
        print("  image, by (e~', k) = 0 and form preservation.  Whether such an element exists is the")
        print("  transitivity of ker(rho_{T_En}) on primitive isotropic vectors within a class -- the T_En")
        print("  analogue of thm:coble-zero-cusp-count(1), which the book proves for T_Co and not for T_En.")


if __name__ == "__main__":
    main()
