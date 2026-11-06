"""#668: Vinberg's algorithm on I_{1,8}, per Vinberg 1972 (Math. USSR Sb. 16) pp. 29-31.

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_I18_vinberg-chamber.py

Recipe transcribed from p. 30 (PDF p. 14): v_0..v_n a basis with (v_0,v_0)=1, (v_i,v_i)=-1;
initial roots e_i = -v_i + v_{i+1} (i=1..n-1), e_n = -v_n; a root is e = sum k_i v_i with k_i
coprime and (e,e) = -eps, eps in {1,2}, i.e. k_1^2+...+k_n^2 = k_0^2+eps, with k_0 >= 0 and
k_1 >= ... >= k_n >= 0; candidates in increasing nu = k_0^2/eps, a candidate a wall iff its pairing
with every wall already found is <= 0.
Candidates are streamed in nu-order rather than stored, so memory stays flat.
"""
import sys
from math import acos, gcd, pi, sqrt

n = 8
BOUND = 14


def sq(k):
    return k[0] * k[0] - sum(x * x for x in k[1:])


def pair(a, b):
    return a[0] * b[0] - sum(a[i] * b[i] for i in range(1, n + 1))


walls = []
for i in range(1, n):
    k = [0] * (n + 1); k[i] = -1; k[i + 1] = 1
    walls.append(tuple(k))
k = [0] * (n + 1); k[n] = -1
walls.append(tuple(k))
print('initial roots: %d' % len(walls))
for w in walls:
    print('  %s  square %d' % (list(w), sq(w)))
print('')


def solutions(target, limit):
    """Nonincreasing n-tuples of nonnegatives with sum of squares = target, first <= limit."""
    out = []

    def rec(pos, remaining, prev, acc):
        if pos == n:
            if remaining == 0:
                out.append(tuple(acc))
            return
        if remaining < 0:
            return
        top = min(prev, int(sqrt(remaining)))
        for x in range(top, -1, -1):
            rec(pos + 1, remaining - x * x, x, acc + [x])

    rec(0, target, limit, [])
    return out


# Vinberg's recursion enumerates the roots with (e, v_0) > 0, i.e. k_0 >= 1: the roots
# orthogonal to v_0 are those of the finite system of Stab(v_0) = O(I_{0,8}) = B_8, whose
# simple system is exactly the initial e_1, ..., e_8.
order = sorted(((k0 * k0) / e, k0, e) for e in (1, 2) for k0 in range(1, BOUND + 1))
seen = set(walls)
found = []
for nu, k0, eps in order:
    for seq in solutions(k0 * k0 + eps, int(sqrt(k0 * k0 + eps))):
        k = (k0,) + seq
        if all(x == 0 for x in k):
            continue
        g = 0
        for x in k:
            g = gcd(g, x)
        if g != 1 or k in seen:
            continue
        # negative-square convention: adjacent walls of a Coxeter chamber pair POSITIVELY
        if all(pair(k, w) >= 0 for w in walls):
            walls.append(k); seen.add(k); found.append((nu, k))
print('walls added by the recursion: %d' % len(found))
for nu, k in found:
    print('  %s  square %d  nu %.3f' % (list(k), sq(k), nu))
print('')
N = len(walls)
print('THE CHAMBER')
print('  walls: %d' % N)
Gram = [[pair(a, b) for b in walls] for a in walls]
print('  Gram matrix:')
for row in Gram:
    print('    %s' % row)
print('  norms: %s' % [sq(w) for w in walls])
edges = []
for i in range(N):
    for j in range(i + 1, N):
        b = Gram[i][j]
        if b == 0:
            continue
        # for negative-square roots the pairing of adjacent walls is positive, and the label is
        # given by cos(pi/m) = |b| / sqrt(|a||c|)
        value = float(abs(b)) / (sqrt(abs(Gram[i][i])) * sqrt(abs(Gram[j][j])))
        m = int(round(pi / acos(max(-1.0, min(1.0, value)))))
        edges.append((i + 1, j + 1, m))
print('  edges (i, j, label): %s' % (edges,))
print('  label counts: %s' % {m: sum(1 for e in edges if e[2] == m) for m in sorted({e[2] for e in edges})})
deg = [sum(1 for e in edges if i + 1 in (e[0], e[1])) for i in range(N)]
print('  degrees: %s' % deg)
print('  is a chain (all degrees <= 2): %s' % all(d <= 2 for d in deg))
