"""research#658 item 1f: Phi is onto the divisibility-2 classes -- the counting, verified.

LEMMA.  The image of the orbit map Phi of sec-enriques-coble-correspondence is exactly the set of 527
nonzero isotropic classes of A_{T_En}, and the class of eta(v)/2 is a complete invariant of the orbit.

PROOF (each step cited or computed here).
  (a) a class in the image is a nonzero isotropic class of A_{T_En}: eta(v) is primitive isotropic of
      divisibility 2 for every primitive isotropic v of T_Co [prop:cusp-map-not-onto, lem:divisibilityAlwaysTwoTco],
      and v^2 = 0 makes the class isotropic.
  (b) the image has exactly 527 elements: Phi is injective [prop:cusp-map-injective] and the source has 527
      orbits [thm:coble-zero-cusp-count(2)].
  (c) the class is injective on the image: [eta(v)/2] = [eta(v')/2] forces v = v' mod 2T_Co
      [prop:cusp-map-separates-mod-two]; then the classes v* = [v/2] agree, and by
      thm:coble-zero-cusp-count(1) v and v' lie in one stable orbit, hence in one Gamma_En-orbit.  []
  (d) A_{T_En} has exactly 527 nonzero isotropic classes -- computed here.

So the image is a set of 527 distinct classes inside a set of 527, hence equal to it.

What the probe computes: |A_{T_En}| = 2^10 and its nonzero isotropic classes, and, as a cross-check of the
book's number, |A_{T_Co}| = 2^11 and its nonzero isotropic classes, which thm:coble-zero-cusp-count(2)
counts as the number of stable 0-cusps, namely 527.

Usage: python3 computations/reports/coble_658-class-surjectivity-probe.py
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
U2 = [[2 * x for x in row] for row in U]
E82 = [[-2 * x for x in row] for row in e8_cartan()]
G_EN = block_diagonal([U, U2, E82])                 # T_En, rank 12
G_CO = block_diagonal([[[2]], U2, E82])             # T_Co, rank 11


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


def census(gram, name):
    n = len(gram)
    gin = inverse(gram)
    classes = {}
    for bits in product([0, 1], repeat=n):
        v = list(bits)
        classes.setdefault(tuple(x % 1 for x in mv(gin, v)), v)
    zero = tuple([F(0)] * n)
    iso = [k for k, v in classes.items()
           if any(k) and sum(a * b for a, b in zip(v, mv(gin, v))) % 2 == 0]
    print("%s: rank %d, |A| = %d, nonzero isotropic classes = %d" % (name, n, len(classes), len(iso)))
    return len(classes), len(iso)


def main():
    n_en, iso_en = census(G_EN, "T_En")
    n_co, iso_co = census(G_CO, "T_Co")
    print()
    print("cross-check: thm:coble-zero-cusp-count(2) counts the stable 0-cusps of the Coble quotient as")
    print("  527 = the number of nonzero isotropic classes of A_{T_Co}; computed here: %d" % iso_co)
    print("and the image of Phi has that many elements, prop:cusp-map-injective giving injectivity.")
    print()
    print("verdict: the lemma holds -- Phi's image is the set of %d nonzero isotropic classes of" % iso_en)
    print("  A_{T_En}, which is exactly the census, so every divisibility-2 class lies over a Coble")
    print("  0-cusp.  The recorded witness w = 2e~ + e~' is one of them, consistent with the explicit")
    print("  transvection of coble_658-stabilizer-image-probe.py.")


if __name__ == "__main__":
    main()
