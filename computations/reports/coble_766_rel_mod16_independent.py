"""Exact integral mod-16 certificates for Coble REL, independent of Sage.

Every inserted pivot is a word in norm -1 reflections: sifting multiplies
by inverses of existing words, and the closure loop uses squares and
commutators. Distinct leading pivots at level 3 certify 55 independent
elements of the actual reflection image in Gamma(8)/Gamma(16).
"""
import itertools
import numpy as np

n = 11
G = np.array([1, 1] + [-1] * 9, dtype=np.int64)
I = np.eye(n, dtype=np.int64)
mod = 16
mul = lambda a, b: (a @ b) % mod
inv = lambda a: ((a.T * G) * G[:, None]) % mod
piv = {}
new = []

def lead(a):
    d = (a - I) % mod
    for j in (1, 2, 3):
        if np.any((d // (2**j)) % 2):
            v = ((d // (2**j)) % 2).ravel()
            return j, int(np.flatnonzero(v)[0])
    return None

def sift(a, insert=True):
    a = a.copy()
    while (key := lead(a)) is not None:
        if key not in piv:
            if insert:
                piv[key] = a.copy()
                new.append(a.copy())
            return False
        a = mul(inv(piv[key]), a)
    assert np.array_equal(a, I)
    return True

count = 0
for t in itertools.product((-1, 0, 1), repeat=n):
    if next((x for x in t if x), 0) != 1:
        continue
    v = np.array(t, dtype=np.int64)
    if (v * v * G).sum() != -1:
        continue
    count += 1
    s = I + 2 * np.outer(v, v * G)
    assert np.array_equal(mul(s, s), I)
    sift(s % mod)
assert count == 1641
print("root reflections", count, flush=True)
k = 0
while k < len(new):
    a = new[k]
    sift(mul(a, a))
    for b in new[:k]:
        sift(mul(mul(mul(a, b), inv(a)), inv(b)))
    k += 1
ranks = [sum(key[0] == j for key in piv) for j in (1, 2, 3)]
assert ranks == [55, 54, 55]
print("ranks", ranks, flush=True)
# Characteristic positive unit in I_(1,8) on e0,e2,...,e9.
# Its perpendicular is even negative definite unimodular of rank 8,
# i.e. E8(-1); its orthogonal complement in B is <1> + U.
c = np.array([3, 0] + [1] * 8 + [0], dtype=np.int64)
assert (c * c * G).sum() == 1
D = I.copy()
ix = [0] + list(range(2, 10))
D[ix, ix] = -1
D += 2 * np.outer(c, c * G)
assert np.array_equal(D @ D, I)
assert np.array_equal((D.T * G) @ D, np.diag(G))
assert sift(D % mod, False)
assert sift(-I % mod, False)
print("E8 block sign mod16 membership: True")
print("-id mod16 membership: True")
