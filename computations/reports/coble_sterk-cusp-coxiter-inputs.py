"""Sterk Figs 4, 10 and 12: the CoxIter inputs for cusps 1, 4 and 5, checked against the roots.

The three inputs `computations/coxiter/Sterk1.coxiter`, `Sterk4.coxiter` and `Sterk5.coxiter` were
missing while cusps 2 and 3 had one, so three of the five wall counts in
@sec-coxiter-results-for-cusp-lattices rested on no input. This script is the check that closed
#747 for cusp 3, applied to the other three: each diagram's roots are written in Sterk's own label
order from the reconstruction of the closed forms he prints beside each figure, their Gram matrix is
computed, every nonzero pairing is turned into a Coxeter weight exactly, and the committed input is
compared with that. CoxIter's own Gram matrix for each input is then compared entry by entry, and its
verdict is printed.

Objects.  The reconstructions are `cusp_e()`, `cusp_2epfpa1()` and `cusp_2e2fa1()` of
`computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`, whose vertices are Sterk's:

  j = 1  cusp_e()        v = e               Fig. 4,  p. 19  12 vertices  alpha_1..alpha_12
         labels printed on p. 19: alpha_9 = f'-e', alpha_10 = abar_8+2e',
         alpha_11 = 2e'+2f'+abar_1+abar_8, alpha_12 = 5e'+3f'+2abar_2
  j = 4  cusp_2epfpa1()  v = 2e' + f' + abar_1  Fig. 10, p. 23  11 vertices  alpha_2..alpha_12
         labels printed on p. 23: alpha_9 = f-e, alpha_10 = abar_8+2e',
         alpha_11 = e+f+alpha_1-e', alpha_12 = 2e-2e'+abar_8-alpha_1
  j = 5  cusp_2e2fa1()   v = 2e + 2f + abar_1   Fig. 12, p. 24  14 vertices
         alpha_2, alpha_4..alpha_8, alpha~_1, abar~_8, alpha_9..alpha_14
         labels printed on p. 24: alpha_9 = 2e~-alpha~_1, alpha_10 = 2e~+(abar~_2-abar~_3),
         alpha_11 = f~-e~, alpha_12 = e~+f~+(abar~_6-abar~_3),
         alpha_13 = e~+f~+(abar~_1+abar~_8-abar~_3), alpha_14 = e~+f~+alpha~_3

All three plates print their roots, so all three inputs are checked against the reconstruction; no
input here rests on the plate alone.  Weight from pairing: with b = x.y and n_x = x^2,
cos(pi/m) = -b/sqrt(|n_x n_y|), decided exactly by comparing b^2 with |n_x n_y| -- 4b^2 = |n_x n_y|
gives m = 3, 2b^2 = |n_x n_y| gives m = 4, 4b^2 = 3|n_x n_y| gives m = 6, b^2 = |n_x n_y| gives
m = infinity.  A pair reaching none of these is an error, not a weight.

Cusp 3 is checked by `coble_sterk3-coxiter-input.py`, which also spans the 300 dpi re-reading of
Fig. 8; cusp 2's input predates this batch and is not re-checked here.

Run (PATH must carry /sage/.venv/bin, or sage.all dies in gap_workspace_file on bare `gap`):
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo \\
      /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \\
      /sage/.venv/bin/sage /repo/computations/reports/coble_sterk-cusp-coxiter-inputs.py

Transcript: `coble_sterk-cusp-coxiter-inputs-run.txt`.
"""
import re
import subprocess

from sage.all import QQ, RDF, ZZ, matrix, sqrt, sage_eval

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'
COXITER = '/usr/local/bin/coxiter'
ROOT = '/repo/computations/coxiter'

CUSPS = [
    # (j, reconstruction, input file, file labels in the figure's order)
    (1, 'cusp_e', 'Sterk1.coxiter', ['a%d' % k for k in range(1, 13)]),
    (4, 'cusp_2epfpa1', 'Sterk4.coxiter', ['a%d' % k for k in range(2, 13)]),
    (5, 'cusp_2e2fa1', 'Sterk5.coxiter', ['a2', 'a4', 'a5', 'a6', 'a7', 'a8', 'atilde1',
                                         'abartilde8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14']),
]
FIGURE = {1: 'Fig. 4, p. 19', 4: 'Fig. 10, p. 23', 5: 'Fig. 12, p. 24'}
AXIS = {1: 9, 4: 9, 5: 9}          # dimension declared in each input's first line

# Nodes counted on the 300 dpi renders of the three plates, and the row each cusp has in
# @sec-coxiter-results-for-cusp-lattices: (vertices, field, vertices at infinity, f-vector).
# A plate count that disagrees with the input's vertex count is a defect, and this script reports
# it rather than reconciling it; the same for a row of the table.
PLATE = {1: 12, 4: 11, 5: 14}
PAGE = {1: (12, 'Q', 9, '(23, 114, 288, 462, 504, 378, 192, 63, 12, 1)'),
        4: (11, 'Q[sqrt(2)]', 5, '(26, 125, 300, 450, 460, 330, 165, 55, 11, 1)'),
        5: (14, 'Q[sqrt(2)]', 13, '(115, 600, 1352, 1768, 1508, 875, 346, 90, 14, 1)')}
DEFECTS = []

text = open(SOURCE).read()
for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
    line = '\n%s()\n' % call
    assert text.count(line) == 1, call
    text = text.replace(line, '\npass  # kept in computations/reports/sterk-cusp-diagrams-run.txt\n')
ns = {'__name__': 'sterk_cusp_diagrams'}
exec(compile('from sage.all import *', SOURCE, 'exec'), ns)
exec(compile(text, SOURCE, 'exec'), ns)
ip = ns['ip']


def same(a, b):
    """Equality of two elements of Q(sqrt2), structurally or to 30 digits."""
    return bool(a == b) or abs(RR(a) - RR(b)) < RR(10) ** -30


for j, fn, name, labels in CUSPS:
    roots = ns[fn]()
    n = len(roots)
    assert n == len(labels), (j, n, len(labels))
    G = matrix(ZZ, n, n, lambda i, k: ip(roots[i], roots[k]))
    edges = {}
    for i in range(n):
        for k in range(i + 1, n):
            b = G[i, k]
            if b == 0:
                continue
            nn = abs(G[i, i] * G[k, k])
            if 4 * b * b == nn:
                m = 3
            elif 2 * b * b == nn:
                m = 4
            elif 4 * b * b == 3 * nn:
                m = 6
            elif b * b == nn:
                m = 'inf'
            else:
                raise RuntimeError('j = %d, %s-%s: b = %d, b^2/|n_x n_y| = %s is not a Coxeter angle'
                                   % (j, labels[i], labels[k], b, QQ(b * b, nn)))
            edges[(i, k)] = m
    ev = sorted(RDF(x) for x in G.change_ring(RDF).eigenvalues())
    inertia = (sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9),
               sum(1 for x in ev if abs(x) <= 1e-9))

    print('=' * 78)
    print('j = %d   %s   %s   %d vertices' % (j, FIGURE[j], fn + '()', n))
    print('  norms: %s' % [G[i, i] for i in range(n)])
    print('  edges derived: %d   rank %d   inertia (n+,n-,n0) %s' % (len(edges), G.rank(), inertia))
    for (i, k), m in sorted(edges.items()):
        print('    %-10s %-10s m = %s' % (labels[i], labels[k], m))

    raw = [l.strip() for l in open('%s/%s' % (ROOT, name)).read().splitlines() if l.strip()]
    d, dim = (int(x) for x in raw[0].split())
    file_labels = raw[1].split(':', 1)[1].split()
    assert (d, dim) == (n, AXIS[j]), (j, d, dim)
    assert file_labels == labels, (j, file_labels, labels)
    got = {}
    for line in raw[2:]:
        u, v, m = line.split()
        key = tuple(sorted((file_labels.index(u), file_labels.index(v))))
        got[key] = 'inf' if int(m) == 0 else int(m)
    assert got == edges, (j, sorted(got.items()), sorted(edges.items()))
    print('  check: %s carries these %d vertices and the same %d edges with the same weights'
          % (name, d, len(got)))

    run = subprocess.run([COXITER, '-pgm'], input='\n'.join(raw) + '\n',
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stdout + run.stderr
    m = re.search(r'Gram matrix\s*\n\t(.*)\n', run.stdout)
    rows = re.findall(r'\[([^\]]*)\]', m.group(1))
    assert len(rows) == n, len(rows)
    B = [[sage_eval(e.strip(), locals={'sqrt': sqrt}) for e in r.split(',')] for r in rows]
    for i in range(n):
        for k in range(n):
            want = QQ(G[i, k] * G[i, k]) / QQ(abs(G[i, i] * G[k, k]))
            expected = 0 if G[i, k] == 0 else (-sqrt(want) if G[i, k] > 0 else sqrt(want))
            assert same(B[i][k], expected), (j, labels[i], labels[k], B[i][k], expected)
    Bf = matrix(RDF, n, n, lambda i, k: RDF(B[i][k].n()))
    print('  check: CoxIter\'s Gram equals -x.y/sqrt(n_x n_y) in every entry, rank %d'
          % Bf.rank())

    full = subprocess.run([COXITER], input='\n'.join(raw) + '\n', capture_output=True, text=True)
    assert full.returncode == 0, full.stdout + full.stderr
    fields = ('Number of vertices:', 'Dimension:', 'Field generated', 'Cocompact:',
              'Finite covolume:', 'f-vector:', 'Number of vertices at infinity:',
              'Euler characteristic:')
    for line in full.stdout.splitlines():
        if line.strip().startswith(fields):
            print('  %s' % line.strip())
    assert 'Finite covolume: yes' in full.stdout, j

    # plate against input, and the input against the table row
    got_vertices = int(re.search(r'Number of vertices: (\d+)', full.stdout).group(1))
    got_field = re.search(r'Field generated by the entries of the Gram matrix: (\S+)',
                          full.stdout).group(1)
    got_inf = int(re.search(r'Number of vertices at infinity: (\d+)', full.stdout).group(1))
    got_f = re.search(r'f-vector: (\([^)]*\))', full.stdout).group(1)
    plate, (pv, pf, pinf, pfd) = PLATE[j], PAGE[j]
    verdicts = [('plate nodes %d, input vertices %d' % (plate, got_vertices), plate == got_vertices),
                ('table vertices %d' % pv, pv == got_vertices),
                ('table field %s' % pf, pf == got_field),
                ('table vertices at infinity %d' % pinf, pinf == got_inf),
                ('table f-vector', pfd == got_f)]
    for text, ok in verdicts:
        print('  compare %-40s %s' % (text, 'AGREE' if ok else 'DISAGREE'))
        if not ok:
            DEFECTS.append('j = %d: %s' % (j, text))
    if plate != got_vertices:
        print('  DEFECT: the plate counts %d nodes and the input has %d' % (plate, got_vertices))
    print()

print('VERDICT: Figs 4, 10 and 12 are three further finite-covolume examples of dimension 9; each')
print('         input is the diagram its plate draws and its reconstruction computes, and each')
print('         reproduces its row of the table.')
assert not DEFECTS, DEFECTS
print()
print('Defects: none.')
