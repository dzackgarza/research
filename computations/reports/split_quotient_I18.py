"""The line quotient in the split unimodular model: l^perp/l is I_{1,8}, so planes through l are its lines.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/split_quotient_I18.py

B = I_{2,9} = I_{1,1} + I_{1,8} by cor:hyperbolic-splitting and thm:indefinite-unimodular-classification.
For l = Z(v + w) spanned by an isotropic vector of the odd hyperbolic plane, l^perp_B/l should be I_{1,8}:
then isotropic planes through l correspond to isotropic lines of I_{1,8}, and every isometry of I_{1,8}
extends to B as id + phi, fixing l.  This checks the first of those two facts at the owner.
"""
import sys

from sage.all import ZZ, diagonal_matrix

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

# I_{1,1} = diag(1, -1); its isotropic vectors are v +- w.
# I_{0,7} = -1_7; I_{1,8} = I_{1,1} + I_{0,7}, so B = I_{1,1} + I_{1,1} + I_{0,7} = diag(1,-1,1,-1,-1,...,-1).
gram = diagonal_matrix(ZZ, [1, -1, 1, -1] + [-1] * 7)
B = Lattices(ZZ)([list(row) for row in gram.rows()])
print('B: rank %d, signature %s, det %s' % (B.module_rank(), tuple(int(x) for x in B.signature_pair()),
                                             int(B.determinant())))
assert int(B.determinant()) in (1, -1)

ring = B.base_ring()
v = B.linear_combination({0: ring(1)})
w = B.linear_combination({1: ring(1)})
ell = v + w
print('the line l = <v+w>: square %d, primitive %s' % (int(ell.b(ell)), int(B.div(ell)) == 1))
assert int(ell.b(ell)) == 0 and int(B.div(ell)) == 1

quotient = ell.isotropic_reduction()
invariants = quotient.signature_pair()
print('l^perp/l: rank %d, signature %s, det %s'
      % (quotient.module_rank(), tuple(int(x) for x in invariants), int(quotient.determinant())))

print('   rank %d, signature %s, det %s'
      % (quotient.module_rank(), tuple(int(x) for x in invariants), int(quotient.determinant())))
assert quotient.module_rank() == 9
assert tuple(int(x) for x in invariants) == (1, 8)
assert int(quotient.determinant()) in (1, -1)

print()
print('so l^perp/l is unimodular of rank 9 and signature (1,8), hence I_{1,8} by the indefinite')
print('classification, and the isotropic planes through l are exactly the isotropic lines of that quotient.')
print('Every isometry phi of the quotient extends to B as id_P + phi, which fixes every point of P and')
print('hence the line l: the restriction is surjective in the split model, with no discriminant condition.')
