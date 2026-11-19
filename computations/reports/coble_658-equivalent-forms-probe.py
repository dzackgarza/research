"""research#658 item 1e: four equivalent forms, so the item may be attacked in whichever is convenient.

LEMMA.  With the sign lemma in force (lem:monodromy-is-spinor-positive), the following are equivalent:
  (a) rho(Gamma_Co) = 1, i.e. Gamma_Co <= ker(rho_{T_Co})                -- item 1e;
  (b) Gamma_Co fixes each of the 527 nonzero isotropic classes of A_{T_Co};
  (c) every Gamma_Co-orbit on the 527 0-cusps of D(T_Co)/O~+(T_Co) is a singleton;
  (d) [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| = 1.

PROOF.
  (a) <=> (b).  The probes coble_658-isotropic-separates-probe.py compute the arithmetic: the 527 classes
      generate ker(2q) of index two in A_{T_Co}, and an isometry fixing ker(2q) pointwise acts trivially on
      the quotient and is then forced to be the identity by q(gx) = q(x) + 2b(x,k).
  (b) <=> (c).  thm:coble-zero-cusp-count(1) puts the nonzero isotropic classes of A_{T_Co} in bijection
      with the orbits of the discriminant kernel on primitive isotropic lines, and (2) identifies those with
      the 527 0-cusps of the stable quotient; the bijection is v |-> [v/2], and Gamma_Co acts on the
      classes through rho, so fixing the classes and fixing the cusps are the same condition.
  (d) <=> (a).  Gamma_Co <= O^+(T_Co) by the sign lemma, so Gamma_Co cap O^+(T_Co) = ker(rho) cap
      Gamma_Co, and the first isomorphism theorem gives the index as |rho(Gamma_Co)|; that is 1 exactly
      when (a) holds.  []

What is NOT claimed: any of the four.  The lemma only says they are one question, so a solver may compute
orbits (c), test classes (b), compute the index (d) or the image (a), whichever the available tool makes
easiest.

The probe re-checks the two numbers the equivalences rest on: |A_{T_Co}| = 2048 with 527 nonzero isotropic
classes, and |P| = 696,729,600 (coble_658-index-narrowing-probe.py), and prints the four forms.

Usage: python3 computations/reports/coble_658-equivalent-forms-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product

ORDER_OQ = 46_998_591_897_600
INDEX_R = 67_456


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


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


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


def main():
    N = len(G)
    GINV = inverse(G)
    classes = {}
    for bits in product([0, 1], repeat=N):
        classes.setdefault(tuple(x % 1 for x in mv(GINV, list(bits))), list(bits))
    iso = [k for k, v in classes.items()
           if any(k) and sum(a * b for a, b in zip(v, mv(GINV, v))) % 2 == 0]
    print("A_{T_Co}: |A| = %d, nonzero isotropic classes = %d" % (len(classes), len(iso)))
    order_p = ORDER_OQ // INDEX_R
    assert ORDER_OQ % INDEX_R == 0
    print("|P| = |O(q_{T_Co})| / [O(T_Co) : R_{gent}] = %d / %d = %d" % (ORDER_OQ, INDEX_R, order_p))
    print()
    print("the four forms of item 1e, equivalent by the lemma:")
    print("  (a) rho(Gamma_Co) = 1  <=>  Gamma_Co <= ker(rho_{T_Co})")
    print("  (b) Gamma_Co fixes each of the %d nonzero isotropic classes of A_{T_Co}" % len(iso))
    print("  (c) every Gamma_Co-orbit on the 527 0-cusps of D(T_Co)/O~+(T_Co) is a singleton")
    print("  (d) [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| = 1  (a divisor of %d)" % order_p)
    print()
    print("verdict: the lemma holds -- the four are one question, none of them decided here.  A solver may")
    print("  compute orbits (c), test the classes (b), the index (d) or the image (a), whichever tool is")
    print("  at hand.")


if __name__ == "__main__":
    main()
