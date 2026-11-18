"""Exact level sets of the discriminant quadratic forms of S_Co and T_Co (research#671).

The two lattices are the ones the corpus fixes:

    S_Co = <2> + <-2>^{10}          Dolgachev--Kondo, Izv. 77:3 (2013), printed p. 511:
                                    M = <2> + <-2>^{10}, signature (1,10), A_M = (Z/2Z)^{11}
    T_Co = <2> + U(2) + E8(2)       prop:coble-transcendental of the heegner report

Both are 2-elementary, so 2 L^* is contained in L and every class of A_L = L^*/L has a
representative of the form v = (1/2) sum eps_i e_i with eps in {0,1}^n.  The discriminant
quadratic form is, with the convention of the report's own proof of prop:coble-transcendental
(where q(eta/2) is computed as (eta/2)^2),

    q_L(x) = v^2  mod 2Z          for any lift v in L^*.

The script enumerates all 2^11 classes of each lattice in exact rational arithmetic and
prints the number of classes at each of the four values q takes.  It also prints the negation
of the S-row, which must reproduce the T-row because q_{N_X} = -q_M (Dolgachev--Kondo,
printed p. 513).
"""
from fractions import Fraction as F
from itertools import product


def e8_negative():
    """The negative definite E8 root lattice, Cartan matrix negated."""
    C = [[2, -1, 0, 0, 0, 0, 0, 0],
         [-1, 2, -1, 0, 0, 0, 0, 0],
         [0, -1, 2, -1, 0, 0, 0, -1],
         [0, 0, -1, 2, -1, 0, 0, 0],
         [0, 0, 0, -1, 2, -1, 0, 0],
         [0, 0, 0, 0, -1, 2, -1, 0],
         [0, 0, 0, 0, 0, -1, 2, 0],
         [0, 0, -1, 0, 0, 0, 0, 2]]
    return [[-C[i][j] for j in range(8)] for i in range(8)]


def block_diag(blocks):
    n = sum(len(b) for b in blocks)
    M = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                M[off + i][off + j] = b[i][j]
        off += len(b)
    return M


def determinant(G):
    """Exact determinant by fraction-free enough Gaussian elimination over Q."""
    n = len(G)
    M = [row[:] for row in G]
    d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = F(M[r][c], M[c][c])
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return d


def levels(G):
    """q-value of every class of A_L, the classes being indexed by eps in {0,1}^n."""
    n = len(G)
    out = {}
    for eps in product((0, 1), repeat=n):
        v = [F(e, 2) for e in eps]
        sq = sum(v[i] * G[i][j] * v[j] for i in range(n) for j in range(n))
        out[eps] = F(sq) % 2
    return out


def report(name, G):
    q = levels(G)
    counts = {}
    for val in q.values():
        counts[val] = counts.get(val, 0) + 1
    print(f"{name}")
    print(f"  rank {len(G)}, |det G| = {abs(determinant(G))}, |A_L| = {len(q)}")
    for k in sorted(counts):
        print(f"    q = {k}: {counts[k]} classes")
    return counts


def main():
    E8 = e8_negative()
    G_S = block_diag([[[2]]] + [[[-2]] for _ in range(10)])
    G_T = block_diag([[[2]], [[0, 2], [2, 0]], [[2 * x for x in r] for r in E8]])
    cS = report("S_Co = <2> + <-2>^10  (Dolgachev--Kondo, printed p. 511)", G_S)
    cT = report("T_Co = <2> + U(2) + E8(2)  (prop:coble-transcendental)", G_T)
    negS = {}
    for k, v in cS.items():
        negS[(-k) % 2] = negS.get((-k) % 2, 0) + v
    print("negation of the S-row (must equal the T-row, q_T = -q_S, DK13 printed p. 513):")
    for k in sorted(negS):
        print(f"    q = {k}: {negS[k]} classes")
    print("rows agree:", negS == cT)
    print("level 0 count of T_Co is 528 = 527 + 1, the 527 nonzero singular classes of")
    print("thm:coble-zero-cusp-count(2) and the zero class")


if __name__ == "__main__":
    main()
