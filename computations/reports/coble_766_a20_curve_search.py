"""Curves in P^1 x P^1 over F_p whose preimage in z^2 = f_star(x, y) splits over
F_p-bar: the graphs y = A(x)/B(x) (bidegree (d, 1)) and x = A(y)/B(y)
(bidegree (1, d)), A, B coprime of degree <= d, not both of degree < d.  The
restriction of f_star is a binary form of degree 4 + 4d; the preimage splits
when that form is a constant times a square, i.e. every root (the root at
infinity included) has even multiplicity.
Run: coble_766_a20_curve_search.py p d."""
import sys, itertools
from sage.all import GF, PolynomialRing
C = {(4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4, (2, 4): 3, (2, 2): 2,
     (2, 0): 3, (1, 3): -13, (1, 1): -28, (0, 4): -10, (0, 2): 13}
p, d = int(sys.argv[1]), int(sys.argv[2])
F = GF(p); R = PolynomialRing(F, 't'); t = R.gen()
pw = [t**i for i in range(5)]


def split(G, deg):
    if G == 0:
        return False
    if (deg - G.degree()) % 2:
        return False
    return all(e % 2 == 0 for _, e in G.squarefree_decomposition())


for graph in sys.argv[3:] or ('y = A(x)/B(x)', 'x = A(y)/B(y)'):
    hits = 0
    for coef in itertools.product(range(p), repeat=2 * d + 2):
        if next(c for c in coef + (1,) if c) != 1:
            continue
        A = R(list(coef[:d + 1])); B = R(list(coef[d + 1:]))
        if A == 0 or B == 0 or max(A.degree(), B.degree()) != d or A.gcd(B) != 1:
            continue
        Ap = [A**j for j in range(5)]; Bp = [B**(4 - j) for j in range(5)]
        if graph[0] == 'y':
            G = sum(F(v) * pw[i] * Ap[j] * Bp[j] for (i, j), v in C.items())
        else:
            G = sum(F(v) * pw[j] * Ap[i] * Bp[i] for (i, j), v in C.items())
        if split(G, 4 + 4 * d):
            hits += 1
            print('  %s: A = %s, B = %s, restriction = %s' % (graph, A, B, G.factor()))
    print('p = %d, d = %d, %s: %d curves with split preimage' % (p, d, graph, hits), flush=True)
