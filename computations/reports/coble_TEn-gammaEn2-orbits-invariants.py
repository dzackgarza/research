"""Why the rho-side count is 2: the invariant that splits the isotropic classes, and the fibres.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
    PYTHONPATH=/repo/.scratch/se-provider-15db925b/src \\
    .scratch/udocker_dir/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_TEn-gammaEn2-orbits-invariants.py

`coble_TEn-gammaEn2-orbits.py` walks the 527 nonzero isotropic classes of A_{T_En} under
H = Stab_{O(q)}(c) and finds two orbits, of sizes 272 and 255.  This record says why that number is 2
and not an artefact of the walk.

The invariant.  c = [h/2] has q(c) = 1, so c is not isotropic, and every g in H fixes c; hence
b(x, c) is constant on each H-orbit, and an H-orbit lies inside one of the level sets of b(., c) on
the isotropic classes.  The script computes those level sets, and their sizes are exactly the two
orbit sizes.  Together with the walk -- which produces a partition of the 527 into exactly two orbits
-- this gives both halves: at least two orbits by invariance, and at most two because the walk
exhibits two.  So H is transitive on each level set, there is no third orbit, and the rho-side count
is 2.  The level sets are:

  b(x, c) = 0     the isotropic classes orthogonal to c, i.e. those of c^perp; 255 of them, which is
                  2^8 - 1 -- the form restricted to c^perp has a 1-dimensional radical (c itself)
                  and descends to an 8-dimensional symplectic space with 2^8 totally isotropic
                  vectors, zero included;
  b(x, c) = 1/2   the rest, 272 of them.

What this decides.  The published count is 5 (AEGS 2025, section 3.3, p. 590: five 0-cusps).  A
Gamma_En,2-orbit maps into an H-orbit, so the H-count is a lower bound; it is 2, not 5, so for this
pair the rho-side count does not see the orbits and the fibres of the map from Gamma_En,2-orbits to
H-orbits are not single points -- in contrast with Gamma_Co, where ker rho lies in Stab(h) and the two
counts must agree.  Nothing about 5 is decided here; the lattice-side count is what decides it.

Transcript: `coble_TEn-gammaEn2-orbits-invariants-run.txt`.
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print('provenance\n  Sage: %s\n  sage-extensions pin 15db925b\n' % SAGE_VERSION)
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
A = T.discriminant_quadratic_form()
h = T.basis_vector(2) + T.basis_vector(3)
c = T.discriminant_class(T.primitive_dual(h))
iso = list(A.isotropic_elements())
zero = iso[0]
nonzero = [x for x in iso if x != zero]
print('c = [h/2]: q(c) = %s  (so c is not isotropic)' % A.q(c))
print('isotropic classes %d, nonzero %d' % (len(iso), len(nonzero)))

levels = {}
for x in nonzero:
    levels.setdefault(A.b(x, c), []).append(x)
print('\nlevel sets of b(., c) on the nonzero isotropic classes:')
for value, points in sorted(levels.items(), key=lambda item: -len(item[1])):
    print('  b(x,c) = %-52s %d classes' % (value, len(points)))

walked = sorted((len(points) for points in levels.values()), reverse=True)
print('\n  sizes sorted: %s' % (walked,))
assert walked == [272, 255], walked
print('  the walk of coble_TEn-gammaEn2-orbits.py found two orbits of exactly these sizes:')
print('    2 orbits, sizes [272, 255]')
print('')
print('WHY THIS IS 2 AND NOT MORE: H fixes c, so b(., c) is constant on every H-orbit and each orbit')
print('lies inside one level set -- at least two orbits.  The walk produces a partition into exactly')
print('two, so the orbits are the level sets themselves and H is transitive on each.')
print('')
print('CONSEQUENCE: the rho-side count is 2 against a published 5.  The fibres of the map from')
print('Gamma_En,2-orbits of primitive isotropic vectors to H-orbits are not single points for this')
print('pair, so the rho-side count is a strict lower bound and does not decide the 5.')
