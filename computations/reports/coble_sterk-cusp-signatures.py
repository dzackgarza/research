"""The "Signature line" column of the Sterk cusp table, and what it is a signature of.

@sec-coxiter-results-for-cusp-lattices tabulates, per cusp, the number of vertices, the Gram field,
the number of vertices at infinity, a "Signature line", and the f-vector.  This script decides what
that column is by reproducing all five entries from Sterk's root systems, and it distinguishes it
from CoxIter's own `Signature (numerically)` line, which is a different number at one of the five.

Objects.  The five cusps of Sterk 4.2.3-4.3.9, with the roots of each diagram in the order the
figures label them, as reconstructed in
`computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`:

    j = 1  cusp_e()        v = e                12 vertices  alpha_1..alpha_12
    j = 2  cusp_ep()       v = e'               10 vertices  alpha_1..alpha_10
    j = 3  cusp_epfpa8()   v = e' + f' + abar_8 12 vertices  alpha_1..alpha_7, alpha_9..alpha_13
    j = 4  cusp_2epfpa1()  v = 2e' + f' + abar_1 11 vertices alpha_2..alpha_12
    j = 5  cusp_2e2fa1()   v = 2e + 2f + abar_1 14 vertices alpha_1..alpha_14 re-based

Each diagram's Gram matrix is the matrix of pairings of those roots in L_- = H + H(2) + E8(-2).
The column prints the inertia of that Gram with its overall sign flipped, i.e. (n+, n-, n0) of
-x.y, which is the Schlaefli form of v^perp/Zv with its +1 direction first.  Every row has rank 10
and one +1 direction, so the column reads (9, 1, nullity) and the nullity is the number of linear
dependencies among the roots of that diagram.

Run (PATH must carry /sage/.venv/bin, or sage.all dies on bare `gap`):
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo \\
      /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \\
      /sage/.venv/bin/sage /repo/computations/reports/coble_sterk-cusp-signatures.py

Transcript: `coble_sterk-cusp-signatures-run.txt`.
"""
from sage.all import QQ, RDF, ZZ, matrix

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'

# Read off the table of @sec-coxiter-results-for-cusp-lattices, columns "Vertices" and
# "Signature line", in Sterk's order j = 1..5.
PAGE = {1: (12, '9,1,2'), 2: (10, '9,1,0'), 3: (12, '9,1,2'), 4: (11, '9,1,1'), 5: (14, '9,1,4')}
CUSP = {1: ('cusp_e', 'e'),
        2: ('cusp_ep', "e'"),
        3: ('cusp_epfpa8', "e' + f' + abar_8"),
        4: ('cusp_2epfpa1', "2e' + f' + abar_1"),
        5: ('cusp_2e2fa1', '2e + 2f + abar_1')}

text = open(SOURCE).read()
for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
    line = '\n%s()\n' % call
    assert text.count(line) == 1, call
    text = text.replace(line, '\npass  # kept in computations/reports/sterk-cusp-diagrams-run.txt\n')
ns = {'__name__': 'sterk_cusp_diagrams'}
exec(compile('from sage.all import *', SOURCE, 'exec'), ns)
exec(compile(text, SOURCE, 'exec'), ns)
ip = ns['ip']

ok = True
for j in range(1, 6):
    fn, v = CUSP[j]
    roots = ns[fn]()
    n = len(roots)
    G = matrix(ZZ, n, n, lambda i, k: ip(roots[i], roots[k]))
    ev = [RDF(x) for x in G.change_ring(RDF).eigenvalues()]
    inertia = (sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9),
               sum(1 for x in ev if abs(x) <= 1e-9))
    flipped = (inertia[1], inertia[0], inertia[2])
    got = '%d,%d,%d' % flipped
    same = (n == PAGE[j][0] and got == PAGE[j][1])
    ok = ok and same
    print('j = %d  v = %-16s %s()' % (j, v, fn))
    print('      %2d vertices, Gram of rank %2d, inertia %s of  x.y , i.e. %s of  -x.y'
          % (n, G.rank(), inertia, flipped))
    print('      page: %2d vertices, %s   %s' % (PAGE[j][0], PAGE[j][1], 'MATCH' if same else 'DIFFERS'))
    assert G.rank() == 10, (j, G.rank())
    assert flipped[0] == 9 and flipped[1] == 1, (j, flipped)
print()
print('All five rows of the column are the inertia of the sign-flipped Gram of the roots.')
print('CoxIter\'s own "Signature (numerically)" line is not that number: at Sterk 3 it reads')
print('10,2,0 for a Gram of rank 10 and inertia (9,1,2) (computations/coxiter/logs/Sterk3.txt).')
assert ok
print()
print('VERDICT: the column reproduces as (9, 1, nullity) of the Schlaefli form at all five cusps.')
