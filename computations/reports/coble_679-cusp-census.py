#!/usr/bin/env python3
"""The census of 0-cusps of F_{2d} by the triple (p, a, k).

Sources.  AE23, Section 10C, printed p. 37: the 0-cusps of F_{2d} are parametrized by
d = N^2 d_0 with d_0 squarefree, the cusp being the class {+-q} of q in Z/N, with printed
invariant delta^* = 2qNd_0.  The page's lem:cusp-census, proved there from this
parametrization, states with h = gcd(q,N), p = N/h, a = q/h and k = d/p^2 that

    p = 1        <=>  q = 0 mod N              (the unigonal cusp),
    k            =    d_0 h^2,
    k in {1,2}   <=>  h = 1 and d_0 in {1,2}   (d = N^2 or d = 2N^2, q a unit mod N),

and that the classes {+-q} number floor((N+2)/2).

The computation.  Pure integer arithmetic: for every d <= D the classes {+-q} of Z/N are
enumerated once, (h, p, a, k) is formed, and the four assertions above are checked.  No
lattice operation is used; this is arithmetic on A_L = Z/2d, and it is the census that
turns lem:generalized-unigonal-constraint into a statement about which d it applies to.
"""

D = 60


def factor(n):
    f, m, p = {}, n, 2
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def split(d):
    """d = N^2 d_0 with d_0 squarefree."""
    f = factor(d)
    N = 1
    for p, e in f.items():
        N *= p ** (e // 2)
    d0 = d // (N * N)
    assert all(d0 % (p * p) for p in factor(d0)), (d, d0)
    return N, d0


def classes(N):
    return [q for q in range(N) if (N - q) % N >= q]


rows, n_classes, n_p_gt_1, n_k12 = [], 0, 0, 0
d_neither = []
for d in range(1, D + 1):
    N, d0 = split(d)
    reps = classes(N)
    assert len(reps) == (N + 2) // 2, (d, N)
    for q in reps:
        from math import gcd
        h = gcd(q, N)
        p, a, k = N // h, q // h, d // ((N // h) ** 2)
        assert N * N % (p * p) == 0 and d % (p * p) == 0
        assert k == d0 * h * h, (d, q, k, d0, h)
        assert (p == 1) == (q % N == 0), (d, q, p)
        assert (k in (1, 2)) == (h == 1 and d0 in (1, 2)), (d, q, k, h, d0)
        n_classes += 1
        n_p_gt_1 += p > 1
        n_k12 += (k in (1, 2) and p > 1)
        rows.append((d, N, d0, q, h, p, a, k))
    if all(d0_ != 1 and d0_ != 2 for _, d0_ in [split(d)]):
        d_neither.append((d, sum(1 for r in rows if r[0] == d and r[5] > 1)))

print("cusp census of F_{2d} for d <= %d" % D)
print()
print("   d   N   d_0   q   h   p   a    k")
for d, N, d0, q, h, p, a, k in rows:
    if d <= 12:
        print("%4d %3d %5d %3d %3d %3d %3d %4d" % (d, N, d0, q, h, p, a, k))
print()
print("classes checked: %d" % n_classes)
print("cusps with p_* > 1: %d" % n_p_gt_1)
print("cusps with p_* > 1 and k in {1,2}: %d" % n_k12)
print("d <= %d neither a square nor twice a square: %d" % (D, len(d_neither)))
print("  of these, cusps with p_* > 1 in total: %d" % sum(n for _, n in d_neither))
print()
print("PASS: p = 1 exactly for q = 0 mod N (every d <= %d)" % D)
print("PASS: k = d_0 h^2 (every class)")
print("PASS: k in {1,2} exactly for h = 1 and d_0 in {1,2} (every class)")
print("PASS: floor((N+2)/2) classes (every d <= %d)" % D)
