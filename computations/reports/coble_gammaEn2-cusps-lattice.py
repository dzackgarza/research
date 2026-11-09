"""The lattice-side cusps of T_En and the stabilizer images, at the held port revision.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
    .scratch/udocker_dir/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -b $HOME/sage-extensions-cdafca84:/prov -w /repo \\
        /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \\
        PYTHONPATH=/repo/.scratch/port-held/src:/prov/src \\
        /sage/.venv/bin/python /repo/computations/reports/coble_gammaEn2-cusps-lattice.py

Provenance this script requires, and why: the `cusps` call raised the tracked `int(owned element)`
TypeError against the old image pair (sage-indefinite-port 4f0ee50c inside the rootfs, with
sage-extensions 15db925b on PYTHONPATH -- a mixed pair, since that port declares 7b222e86).  It
succeeds against the held port main 991b88b095a42a1e3679569ea42328c900c120f6 (scratch clone
.scratch/port-held, pure Python, imported from /repo/.scratch/port-held/src) with the provider its
pyproject declares, sage-extensions cdafca84065405cb810bba047f8a965299b03762 (snapshot bound at
/prov), on Sage 11.0.beta5.  See coble_gammaEn2-cusps-lattice.md.

What it computes, in order:
  1. the discriminant module A_{T_En} and the order of its orthogonal group;
  2. T_En.cusps(1) -- the O(T_En)-orbits of primitive isotropic lines, i.e. the 0-cusps of
     F_(10,10,0) = D(T_En)/O(T_En).  Published count: two, distinguished by div = 1 and 2
     (AEGS 2025 section 3.2);
  3. for each cusp: a primitive generator v of its representative line (pushed into T_En through the
     subobject's inclusion), its square, its divisibility, the class [v/div(v)], the stabilizer
     generators the record retains, their discriminant images, the order of the group they generate,
     and the order of the stabilizer of that class inside O(A,q).  Equality is the statement that the
     discriminant image of the integral stabilizer of v is the whole stabilizer of its class -- the
     input the fibre argument needs, and `false` is reported rather than assumed;
  4. T_En.cusps(2) -- the O(T_En)-orbits of primitive isotropic planes, i.e. the 1-cusps of
     F_(10,10,0).  This bounds from above the number of finite plane strata that lift.

Nothing here uses a discriminant walk for a subgroup: this is the lattice-level owner.
Transcript: `coble_gammaEn2-cusps-lattice-run.txt`.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

import sage_extensions  # noqa: E402
import sage_indefinite_port  # noqa: E402

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-indefinite-port: %s' % os.path.dirname(sage_indefinite_port.__file__))
print('  sage-extensions:      %s' % os.path.dirname(sage_extensions.__file__))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
A = T.discriminant_quadratic_form()
O = A.orthogonal_group()
print('T_En: rank %d, det %s, signature %s' % (T.rank(), T.determinant(), T.signature_pair()))
print('|A| = %d, |O(A,q)| = %d, isotropic classes %d'
      % (int(A.cardinality()), int(O.order()), len(list(A.isotropic_elements()))))
print('')

start = time.time()
cusps1 = list(T.cusps(1))
print('T_En.cusps(1): %d records   (%.0f s)' % (len(cusps1), time.time() - start))
print('  a cusp is a line Zv, not the vector v; the two generators differ by -id in O(T_En)')
print('')
rho = T.discriminant_representation()
for i, rec in enumerate(cusps1):
    rep = rec.representative()
    gens = list(rep.module_generators())
    if hasattr(rep, 'inclusion'):
        gens = [rep.inclusion()(g) for g in gens]
    v = gens[0]
    cls = T.discriminant_class(T.primitive_dual(v))
    print('cusp %d' % i)
    print('  generator v: square %s, div %s, class q = %s' % (v.q(), T.div(v), A.q(cls)))
    stab = list(rec.stabilizer_generators())
    print('  stabilizer generators retained: %d' % len(stab))
    start = time.time()
    images = tuple(rho(g) for g in stab)
    Gs = O.subgroup(images)
    print('  their discriminant images: built in %.0f s, order %d' % (time.time() - start, int(Gs.order())))
    start = time.time()
    H = O.stabilizer_of_element(cls)
    print('  |Stab_{O(A,q)}(class)| = %d   (%.0f s)' % (int(H.order()), time.time() - start))
    print('  image equals the class stabilizer: %s' % (int(Gs.order()) == int(H.order())))
    print('')

start = time.time()
cusps2 = list(T.cusps(2))
print('T_En.cusps(2): %d records   (%.0f s)' % (len(cusps2), time.time() - start))
for i, rec in enumerate(cusps2):
    print('  cusp %d: %s' % (i, str(rec.representative())[:100].replace('\n', ' ')))
print('')
print('The plane count above bounds the number of finite plane strata that lift; the strata themselves')
print('are in coble_gammaEn2-card-run.txt.  Neither is a Gamma_En,2 count until the subgroup route runs.')
