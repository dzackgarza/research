"""Sterk Fig. 8, p. 22: the twelve-node diagram, and its CoxIter input.

The question this decides (#747).  The tree's CoxIter record
(`sec-coxiter-results-for-cusp-lattices`, "Vertices" column) gives 12 nodes for Sterk's third
cusp.  `computations/coxiter/` held no input for it, so the number had no reproducible source;
and a reading of the plate at 150 dpi counted 13 nodes, which was filed as a disagreement
between the plate and the record.  This script settles both: it derives the diagram from the
maintained reconstruction of Sterk's root vectors, writes nothing, and checks that the
committed input `computations/coxiter/Sterk3.coxiter` is that diagram.

Objects.  Sterk 4.3.7 (p. 22), cusp 3, v = e' + f' + abar_8, K_3 = v^perp/Z v = U + E_8(-2),
rank 10, signature (1,9).  The diagram's vertices are the twelve roots
alpha_1,...,alpha_7, alpha_9,...,alpha_13 of `cusp_epfpa8()` in
`computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`, which writes each from the
closed form Sterk gives on p. 22; alpha_8 is not a vertex of the diagram, it enters only through
the labels of alpha_10, alpha_11 and alpha_13.  Edge weights are the Coxeter exponents of the
root pairings: with b = (x,y) and n_i = x^2, cos(pi/m) = -b/sqrt(n_i n_j), decided exactly by
comparing b^2 against |n_i n_j| (4b^2 = |n_i n_j| gives m = 3, 2b^2 = |n_i n_j| gives m = 4,
b^2 = |n_i n_j| gives m = infinity).  Nothing here uses a vector of the ambient lattice outside
those twelve roots.

Checks, all printed:
  (i)   the twelve norms and the edge list derived from the reconstruction;
  (ii)  the committed .coxiter file carries exactly that vertex list and that edge list, compared
        as sets after the file's own labels are read back;
  (iii) CoxIter's Gram matrix for the file equals the normalisation x.y/sqrt(n_x n_y) of the
        reconstruction's Gram, entry by entry, and has the same inertia and rank.

Run:
  JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo \\
      /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \\
      /sage/.venv/bin/sage /repo/computations/reports/coble_sterk3-coxiter-input.py

PATH must carry /sage/.venv/bin, or sage.all dies in gap_workspace_file() with
FileNotFoundError: 'gap'.  The transcript is `coble_sterk3-coxiter-input-run.txt`; CoxIter's own
output for the committed input is `computations/coxiter/logs/Sterk3.txt`, taken on standard input
(CoxIter reads a file through -i; a bare path argument reports EMPTY_FILE).
"""
import re
import subprocess

from sage.all import QQ, RDF, ZZ, matrix, sqrt, vector, sage_eval

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'
INPUT = '/repo/computations/coxiter/Sterk3.coxiter'
COXITER = '/usr/local/bin/coxiter'

LABELS = ['alpha1', 'alpha2', 'alpha3', 'alpha4', 'alpha5', 'alpha6', 'alpha7',
          'alpha9', 'alpha10', 'alpha11', 'alpha12', 'alpha13']

# --------------------------------------------------------------- the diagram
text = open(SOURCE).read()
for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
    line = '\n%s()\n' % call
    assert text.count(line) == 1, call
    text = text.replace(line, '\npass  # kept in computations/reports/sterk-cusp-diagrams-run.txt\n')
ns = {'__name__': 'sterk_cusp_diagrams'}
exec(compile('from sage.all import *', SOURCE, 'exec'), ns)
exec(compile(text, SOURCE, 'exec'), ns)

roots = ns['cusp_epfpa8']()
ip = ns['ip']
n = len(roots)
assert n == len(LABELS) == 12, n
G = matrix(ZZ, n, n, lambda i, j: ip(roots[i], roots[j]))

print('Sterk 4.3.7, p. 22: v = e\' + f\' + abar_8, K_3 = v^perp/Zv = U + E8(-2)')
print('vertices: %d' % n)
for i in range(n):
    print('  %-8s norm %2d' % (LABELS[i], G[i, i]))
print()

edges = {}
for i in range(n):
    for j in range(i + 1, n):
        b = G[i, j]
        if b == 0:
            continue
        nn = abs(G[i, i] * G[j, j])
        if 4 * b * b == nn:
            m = 3
        elif 2 * b * b == nn:
            m = 4
        elif b * b == nn:
            m = 'inf'
        else:
            raise RuntimeError('pair %s %s: b = %s, b^2/|n_i n_j| = %s is not a Coxeter angle'
                               % (LABELS[i], LABELS[j], b, QQ(b * b, nn)))
        edges[(i, j)] = m
        print('  %-8s %-8s b = %2d   norms %2d %2d   m = %s' % (LABELS[i], LABELS[j], b, G[i, i], G[j, j], m))
print()
print('edges: %d' % len(edges))
print('rank of the Gram: %d' % G.rank())
ev = sorted(RDF(x) for x in G.change_ring(RDF).eigenvalues())
inertia = (sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9),
           sum(1 for x in ev if abs(x) <= 1e-9))
print('inertia of the Gram (n+, n-, n0): %s' % (inertia,))
print()

# ------------------------------------------- check (ii): the committed input
raw = open(INPUT).read().splitlines()
raw = [line.strip() for line in raw if line.strip()]
d, dim = (int(x) for x in raw[0].split())
assert (d, dim) == (n, 9), (d, dim)
assert raw[1].startswith('vertices labels:')
file_labels = raw[1].split(':', 1)[1].split()
assert len(file_labels) == n

INDEX = {lab: i for i, lab in enumerate(LABELS)}
by_file_label = {'a%d' % (i + 1 if i < 7 else i + 2): i for i, lab in enumerate(LABELS)}
assert sorted(by_file_label) == sorted(file_labels), (sorted(by_file_label), sorted(file_labels))

got = {}
for line in raw[2:]:
    u, v, m = line.split()
    key = tuple(sorted((by_file_label[u], by_file_label[v])))
    got[key] = 'inf' if int(m) == 0 else int(m)
assert got == edges, (sorted(got.items()), sorted(edges.items()))
print('check (ii): %s carries %d vertices and the same %d edges with the same weights'
      % (INPUT, d, len(got)))
print()

# ------------------------------- check (iii): CoxIter's own Gram for that file
run = subprocess.run([COXITER, '-pgm'], input='\n'.join(raw) + '\n',
                     capture_output=True, text=True)
assert run.returncode == 0, run.stdout + run.stderr
m = re.search(r'Gram matrix\s*\n\t(.*)\n', run.stdout)
assert m, run.stdout[:2000]
rows = re.findall(r'\[([^\]]*)\]', m.group(1))
assert len(rows) == n, len(rows)
B = [[sage_eval(entry.strip(), locals={'sqrt': sqrt}) for entry in row.split(',')] for row in rows]

def same(a, b):
    """Equality of two elements of Q(sqrt2), structurally or to 30 digits."""
    return bool(a == b) or abs(RR(a) - RR(b)) < RR(10) ** -30

# CoxIter's Gram is B = -x.y / sqrt(n_x n_y), the negative of the normalisation of G: the
# minus sign puts +1 on the diagonal (n_x < 0), and it flips the inertia.
for i in range(n):
    for j in range(n):
        want = QQ(G[i, j] * G[i, j]) / QQ(abs(G[i, i] * G[j, j]))
        expected = 0 if G[i, j] == 0 else (-sqrt(want) if G[i, j] > 0 else sqrt(want))
        assert same(B[i][j], expected), (LABELS[i], LABELS[j], B[i][j], expected)

Bf = matrix(RDF, n, n, lambda i, j: RDF(B[i][j].n()))
evB = sorted(Bf.eigenvalues())
inertiaB = (sum(1 for x in evB if x > 1e-9), sum(1 for x in evB if x < -1e-9),
            sum(1 for x in evB if abs(x) <= 1e-9))
print('check (iii): CoxIter\'s Gram equals -x.y/sqrt(n_x n_y) in every entry, and')
print('             rank %d with inertia (n+, n-, n0) = %s = the sign flip of that of the Gram'
      % (Bf.rank(), inertiaB))
assert Bf.rank() == G.rank()
assert inertiaB == (inertia[1], inertia[0], inertia[2]), (inertiaB, inertia)
# The verdict itself comes from a run with no computation options: with one given, CoxIter
# computes only what was asked and prints "?" for the rest.
full = subprocess.run([COXITER], input='\n'.join(raw) + '\n', capture_output=True, text=True)
assert full.returncode == 0, full.stdout + full.stderr
print('check (iv): CoxIter on the committed input, no options:')
for line in full.stdout.splitlines():
    if any(key in line for key in ('Finite covolume', 'Cocompact', 'f-vector',
                                   'vertices at infinity', 'Euler', 'Dimension',
                                   'Number of vertices', 'Field generated')):
        print('             %s' % line.strip())
assert 'Finite covolume: yes' in full.stdout, full.stdout
assert 'Number of vertices at infinity: 4' in full.stdout, full.stdout
print()
print('VERDICT: twelve vertices, dimension 9, finite covolume; the input and the')
print('         reconstruction encode the same form, and CoxIter certifies the chamber.')
