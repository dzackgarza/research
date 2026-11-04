"""Exact check: the claimed component-switching map v |-> v, w |-> w + tv is not an isometry.

In the hyperbolic plane with basis v, w and (v,v) = 0, (v,w) = 1, (w,w) = 0, one has
(w + tv)^2 = 0 + 2t(v,w) + t^2(v,v) = 2t, so w + tv has square 2t and the map fails Gram preservation for
every t != 0.  This is the disproof of the map used in an earlier draft of prop:rank-nine-line-transitivity,
recorded so that the withdrawal rests on a computation rather than on prose.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/sigma_t_not_an_isometry.py
"""
from sage.all import ZZ, matrix

from sage_extensions.all import Lattices

P = Lattices(ZZ)([list(row) for row in matrix(ZZ, [[0, 1], [1, 0]]).rows()])
ring = P.base_ring()
v = P.linear_combination({0: ring(1)})
w = P.linear_combination({1: ring(1)})
print('(v,v) = %d, (v,w) = %d, (w,w) = %d' % (int(v.b(v)), int(v.b(w)), int(w.b(w))))
assert (int(v.b(v)), int(v.b(w)), int(w.b(w))) == (0, 1, 0)
for t in (0, 1, 2):
    shifted = w + t * v
    square = int(shifted.b(shifted))
    verdict = 'AGREE' if square == 0 else '*** NOT AN ISOMETRY'
    print('t=%d: sigma_t(w) = w + %dv has square %2d, an isometry would need 0   %s'
          % (t, t, square, verdict))
    assert (square == 0) == (t == 0)
print()
print('so v |-> v, w |-> w + tv is an isometry only for t = 0, and the earlier claim that it switches')
print('the component is withdrawn: (w + tv)^2 = 2t, not 0.')
