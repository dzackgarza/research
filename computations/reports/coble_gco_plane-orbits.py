"""Orbits of G_Co on the totally singular planes of A_{S_En}, and on planes decorated by a star.

A_{S_En} = C/2C with C = U + E8(-1) and S_En = C(2).  The discriminant form is
Q(x) = (x,x)_C / 2 mod 2, with polar form beta(x, y) = (x,y)_C mod 2.  The nine generators of
G_Co are the discriminant images of the reflections of S_En in u_0 - w_0 and in the eight simple
roots of E8(2).  Each such root r has (r,r)_C = -2, so the reflection acts on C/2C as the
transvection x -> x + beta(x,r) r.

For a totally singular plane J, the quotient J^perp/J is a six-dimensional quadratic space of
plus type, and its isometry group is S_8.  A star is a set of seven nonsingular vectors of
J^perp/J that are pairwise non-orthogonal; there are eight stars, and they form the natural
S_8-set.  A star is stored as the set of the 28 elements of A_{S_En} in its seven cosets of J.
"""
import itertools

import numpy as np

E8_EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]
G = np.zeros((10, 10), dtype=int)
G[0, 1] = G[1, 0] = 1
for i in range(8):
    G[2 + i, 2 + i] = -2
for a, b in E8_EDGES:
    G[1 + a, 1 + b] = G[1 + b, 1 + a] = 1
VEC = np.array([[(n >> k) & 1 for k in range(10)] for n in range(1024)])
GRAM = VEC @ G @ VEC.T
Q = [int(GRAM[n, n]) // 2 % 2 for n in range(1024)]
BETA = GRAM % 2

ROOTS = [0b11] + [1 << (2 + i) for i in range(8)]
GENS = [tuple(n ^ (r if BETA[n, r] else 0) for n in range(1024)) for r in ROOTS]
for g in GENS:
    assert all(Q[g[n]] == Q[n] for n in range(1024))
    assert (BETA[np.ix_(g, g)] == BETA).all()

SINGULAR = [n for n in range(1, 1024) if Q[n] == 0]
PLANES = {frozenset((u, v, u ^ v)) for u in SINGULAR for v in SINGULAR
          if u < v and BETA[u, v] == 0 and Q[u ^ v] == 0}
print("nonzero singular vectors:", len(SINGULAR), " totally singular planes:", len(PLANES))


def orbits(points, act):
    """The orbits of G_Co on a finite invariant set, as a list of sets."""
    remaining, result = set(points), []
    while remaining:
        start = remaining.pop()
        orbit, todo = {start}, [start]
        while todo:
            x = todo.pop()
            for g in GENS:
                y = act(g, x)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        remaining -= orbit
        result.append(orbit)
    return result


vector_orbits = orbits(SINGULAR, lambda g, x: g[x])
size_of = {x: len(o) for o in vector_orbits for x in o}
print("G_Co-orbit sizes on nonzero singular vectors:", sorted(len(o) for o in vector_orbits))

plane_orbits = orbits(PLANES, lambda g, P: frozenset(g[x] for x in P))
for o in sorted(plane_orbits, key=len):
    kinds = {tuple(sorted(size_of[x] for x in P)) for P in o}
    print(f"  plane orbit of size {len(o):5d}; vector-orbit sizes of its nonzero classes: {sorted(kinds)}")


def stars(J):
    """The eight stars of J^perp/J."""
    span = [0, *J]
    perp = [n for n in range(1024) if all(BETA[n, j] == 0 for j in J)]
    cosets = {frozenset(n ^ j for j in span) for n in perp}
    nonsingular = [c for c in cosets if Q[min(c)] == 1]
    assert len(cosets) == 64 and len(nonsingular) == 28
    meets = {a: {b for b in nonsingular if BETA[min(a), min(b)] == 1} for a in nonsingular}
    found = set()
    for a in nonsingular:
        for b in meets[a]:
            common = meets[a] & meets[b]
            star = {a, b} | {x for x in common if meets[x] & common}
            if len(star) == 7 and all(y in meets[x] for x, y in itertools.combinations(star, 2)):
                found.add(frozenset(x for c in star for x in c))
    assert len(found) == 8
    return found


decorated = {(J, s) for o in plane_orbits for J in [next(iter(o))] for s in stars(J)}
decorated_orbits = orbits(decorated, lambda g, d: (frozenset(g[x] for x in d[0]), frozenset(g[x] for x in d[1])))
flags = {(J, s, c) for (J, s) in {d for o in decorated_orbits for d in [next(iter(o))]} for c in J}
flag_orbits = orbits(flags, lambda g, f: (frozenset(g[x] for x in f[0]), frozenset(g[x] for x in f[1]), g[f[2]]))
assert sum(len(o) for o in decorated_orbits) == 8 * len(PLANES)
assert sum(len(o) for o in flag_orbits) == 24 * len(PLANES)
print("star-decorated plane orbits:", len(decorated_orbits), sorted(len(o) for o in decorated_orbits))
print("star-decorated flag orbits:", len(flag_orbits), sorted(len(o) for o in flag_orbits))
