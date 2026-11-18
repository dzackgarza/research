"""An independent reproduction of the seven decorated-plane and thirteen flag orbits of Gamma_{Co,2}.

research#645 (A2) turns on two finite numbers the Heegner chapter quotes from the
enumeration in ``coble_gco_plane-orbits.py``: Gamma_{Co,2} = rho^{-1}(G_Co) has
seven orbits of primitive isotropic planes and thirteen of incident line-in-plane
flags on T_Co.  This file recomputes both from the discriminant module alone, with
no Sage and no provider call, so the acceptance does not rest on one transcript.

Model.  C = U + E8(-1), S_En = C(2), A = C/2C = F_2^{10} with coordinates
(a, b, e_1, ..., e_8) for the hyperbolic pair (u, w) and the eight simple roots:

    q(x)    = (a*b - e^T Cartan(E8) e / 2) mod 2,
    beta(x,y) = (a d + b c - e^T Cartan(E8) f) mod 2,

and the nine generators of G_Co are the discriminant images of the integral
reflections in u_0 - w_0 and in the eight simple roots of E8(2).  Each root r has
(r,r)_C = -2, so its reflection acts on A as the transvection x -> x + beta(x,r) r.

Objects.  A primitive isotropic plane is a two-dimensional totally singular
subspace J = {0, u, v, u+v}.  The 28 nonsingular vectors of the six-dimensional
plus-type quotient J^perp/J are the classes of q = 1 in J^perp, one per coset of
J; a star is one of the eight seven-element sets of pairwise nonorthogonal ones,
and a decorated plane is a pair (J, star).  A flag is a triple (J, star, c) with
0 != c in J.  Orbits are the connected components of the graph whose edges join
each object to its images under the nine generators.

Counts printed, with the values the chapter states in parentheses:

    nonzero isotropic classes of A                       527
    isotropic 2-planes                                   23715
    nonsingular vectors of J^perp/J, each J                  28
    stars of each J                                           8
    decorated planes                                   189720
    G_Co-orbits of decorated planes                           7
    G_Co-orbits of flags                                     13

Run: ``python3 computations/reports/coble_a2-plane-flag-orbit-reproduction.py``.
Pass ``--planes N`` to stop after the first N planes (a smoke run; it prints the
counts it reached and asserts nothing about the totals).
"""

from __future__ import annotations

import itertools
import sys

N = 1 << 10
MASK_FULL = (1 << N) - 1
CARTAN = [[2, -1, 0, 0, 0, 0, 0, 0],
          [-1, 2, -1, 0, 0, 0, 0, 0],
          [0, -1, 2, -1, 0, 0, 0, -1],
          [0, 0, -1, 2, -1, 0, 0, 0],
          [0, 0, 0, -1, 2, -1, 0, 0],
          [0, 0, 0, 0, -1, 2, -1, 0],
          [0, 0, 0, 0, 0, -1, 2, 0],
          [0, 0, -1, 0, 0, 0, 0, 2]]


def qval(x):
    a, b = x & 1, (x >> 1) & 1
    e = [(x >> i) & 1 for i in range(2, 10)]
    s = sum(e[i] * CARTAN[i][j] * e[j] for i in range(8) for j in range(8))
    assert s % 2 == 0
    return (a * b - s // 2) % 2


# beta(x, .) as a 1024-bit mask: beta is bilinear, so the row of x is the xor of
# the rows of its basis vectors.
def beta_rows():
    rows = [0] * N
    for i in range(10):
        row = 0
        for y in range(N):
            a, b = (1 << i) & 1, ((1 << i) >> 1) & 1
            c, d = y & 1, (y >> 1) & 1
            e = [1 if i == 2 + k else 0 for k in range(8)]
            f = [(y >> k) & 1 for k in range(2, 10)]
            val = (a * d + b * c - sum(e[k] * CARTAN[k][l] * f[l] for k in range(8) for l in range(8))) % 2
            if val:
                row |= 1 << y
        rows[1 << i] = row
    for x in range(N):
        if x and not rows[x]:
            r = 0
            for i in range(10):
                if (x >> i) & 1:
                    r ^= rows[1 << i]
            rows[x] = r
    return rows


ROWS = beta_rows()
Q = [qval(x) for x in range(N)]
ROOTS = [0b11] + [1 << (2 + i) for i in range(8)]
GEN = []
for r in ROOTS:
    row = ROWS[r]
    GEN.append([x ^ (r if (row >> x) & 1 else 0) for x in range(N)])


def beta(x, y):
    return (ROWS[x] >> y) & 1


ISO = [x for x in range(1, N) if Q[x] == 0]


def planes_of(A):
    out = {}
    for i, u in enumerate(A):
        ru = ROWS[u]
        for v in A[i + 1:]:
            if (ru >> v) & 1:
                continue
            w = u ^ v
            if Q[w] == 0:
                out[frozenset((u, v, w))] = None
    return list(out)


def coset_rep(y, u, v):
    """The chosen representative of y's coset modulo the plane {0, u, v, u^v}."""
    return min(y, y ^ u, y ^ v, y ^ u ^ v)


def maximal_cliques(nodes, adj):
    out = []

    def bk(R, P, X):
        if not P and not X:
            out.append(frozenset(R))
            return
        u = max(P | X, key=lambda v: len(adj[v] & P)) if (P | X) else None
        for v in list(P - (adj[u] if u is not None else set())):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}

    bk(set(), set(nodes), set())
    return out


def stars_of(J):
    """The eight stars of J: the seven-element maximal cliques of the nonorthogonality graph."""
    u, v = sorted(J)[:2]
    mask = MASK_FULL & ~(ROWS[u] | ROWS[v])
    reps, seen = [], set()
    while mask:
        low = mask & -mask
        x = low.bit_length() - 1
        mask ^= low
        if Q[x] != 1 or x in seen:
            continue
        seen |= {x, x ^ u, x ^ v, x ^ (u ^ v)}
        reps.append(x)
    assert len(reps) == 28, len(reps)
    adj = {x: {y for y in reps if y != x and beta(x, y)} for x in reps}
    stars = [c for c in maximal_cliques(reps, adj) if len(c) == 7]
    assert len(stars) == 8, len(stars)
    return stars


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

    def sizes(self):
        out = {}
        for i in range(len(self.p)):
            r = self.find(i)
            out[r] = out.get(r, 0) + 1
        return sorted(out.values(), reverse=True)


def main(argv):
    limit = None
    if "--planes" in argv:
        limit = int(argv[argv.index("--planes") + 1])

    print("nonzero isotropic classes of A:", len(ISO), "(527)")
    assert len(ISO) == 527
    planes = planes_of(ISO)
    print("isotropic 2-planes:", len(planes), "(23715)")
    if limit is None:
        assert len(planes) == 23715
    else:
        planes = planes[:limit]
        print("smoke run over", len(planes), "planes; totals not asserted")

    index = {J: i for i, J in enumerate(planes)}
    star_of, class_to_star = [], []
    for J in planes:
        stars = stars_of(J)
        star_of.append(stars)
        table = {}
        for sid, s in enumerate(stars):
            for x in s:
                table.setdefault(x, []).append(sid)
        class_to_star.append(table)
    print("stars of each J:", len(star_of[0]), "(8)")
    assert all(len(s) == 8 for s in star_of)
    if limit is not None:
        print("smoke run: plane and star enumeration only; totals not asserted")
        return 0

    gplane = [[index[frozenset(g[x] for x in J)] for g in GEN] for J in planes]
    gstar = []
    for p in range(len(planes)):
        per_g = []
        for k in range(len(GEN)):
            row = []
            gp = gplane[p][k]
            g = GEN[k]
            gu, gv = sorted(planes[gp])[:2]
            for sid in range(8):
                x1, x2 = sorted(star_of[p][sid])[:2]
                c1 = class_to_star[gp][coset_rep(g[x1], gu, gv)]
                c2 = class_to_star[gp][coset_rep(g[x2], gu, gv)]
                cand = set(c1) & set(c2)
                assert len(cand) == 1, cand
                row.append(cand.pop())
            per_g.append(row)
        gstar.append(per_g)

    uf = UF(len(planes) * 8)
    for p in range(len(planes)):
        for k, g in enumerate(GEN):
            gp, row = gplane[p][k], gstar[p][k]
            for sid in range(8):
                uf.union(p * 8 + sid, gp * 8 + row[sid])
    dec = uf.sizes()
    print("decorated planes:", len(planes) * 8, "(189720)")
    print("G_Co-orbits of decorated planes:", len(dec), "(7)")
    print("  sizes:", dec)

    pairs = [(p, sid, c) for p, J in enumerate(planes) for sid in range(8) for c in sorted(J)]
    fid = {t: i for i, t in enumerate(pairs)}
    uf2 = UF(len(pairs))
    for (p, sid, c), i in fid.items():
        for k, g in enumerate(GEN):
            gp = gplane[p][k]
            uf2.union(i, fid[(gp, gstar[p][k][sid], g[c])])
    fl = uf2.sizes()
    print("flags:", len(pairs), "(569160)")
    print("G_Co-orbits of flags:", len(fl), "(13)")
    print("  sizes:", fl)

    assert dec == [75600, 69120, 22680, 9450, 7560, 3150, 2160], dec
    assert fl == [151200, 138240, 75600, 69120, 45360, 28350, 22680, 15120, 9450, 7560, 2160, 2160, 2160], fl
    print("reproduced: 7 decorated-plane orbits and 13 flag orbits")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
