"""J^perp/J for the exhibited plane J = <v_1, v_2> of T_Co, at the maintained isotropic quotient.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/one_cusp_plane_quotient.py

The manuscript's basis, verbatim: T_Co = <2> + U(2) + E8(2) with h the <2> generator, e', f' the U(2)
generators (e'^2 = f'^2 = 0, e'.f' = 2) and a_1,...,a_8 the E8(2) simple roots; then
v_1 = e' and v_2 = 2h + a_1 + a_2, and the claim is J^perp/J = I_{0,7}(2) = A_1^{oplus 7} = (7,7,1).

Two successive maintained isotropic quotients give the plane quotient without a hand-built Gram complement:
K = v_1^perp/v_1 at the vector level, then the image of J there is spanned by the image of v_2, and the
plane quotient is that line's isotropic reduction in K.
"""
import sys
import time

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import EvenTwoElementaryLattices, Lattices

sys.stdout.reconfigure(line_buffering=True)

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
ring = L.base_ring()


def element(coefficients):
    return L.linear_combination({index: ring(int(value)) for index, value in coefficients.items()})


# basis: 0 = h, 1 = e', 2 = f', 3..10 = a_1..a_8
v1 = element({1: 1})
v2 = element({0: 2, 3: 1, 4: 1})
for name, v in (('v_1', v1), ('v_2', v2)):
    print('%s: square %d, divisibility %d (a basis vector, so primitive)' % (name, int(v.b(v)), int(L.div(v))))
    assert int(v.b(v)) == 0
assert int(v1.b(v2)) == 0, 'the plane is not totally isotropic'

start = time.time()
K = v1.isotropic_reduction()
print('K = v_1^perp/v_1: rank %d, signature %s, det %s   (%.1fs)'
      % (K.module_rank(), tuple(int(x) for x in K.signature_pair()), int(K.determinant()),
         time.time() - start))
assert K.module_rank() == 9 and tuple(int(x) for x in K.signature_pair()) == (1, 8)

# The subobject route: the plane as a primitive isotropic subobject, then its reduction.
start = time.time()
try:
    subobject = L.primitive_isotropic_subobject(v1, v2)
    J = subobject.isotropic_reduction()
    route = 'primitive_isotropic_subobject + isotropic_reduction'
except Exception as exc:
    J = None
    route = 'subobject route failed: %r' % (exc,)
print('J^perp/J via %s   (%.1fs)' % (route, time.time() - start))
if J is not None:
    invariants = EvenTwoElementaryLattices(J.base_ring())(J).two_elementary_invariants()
    print('   rank %d, signature %s, det %s, two_elementary %s'
          % (J.module_rank(), tuple(int(x) for x in J.signature_pair()), int(J.determinant()),
             tuple(int(x) for x in invariants)))
    # A_1^{oplus 7}: the diagonal form with seven -2 entries.
    A1_7 = Lattices(ZZ)([list(row) for row in (-2 * matrix.identity(ZZ, 7)).rows()])
    A_inv = EvenTwoElementaryLattices(A1_7.base_ring())(A1_7).two_elementary_invariants()
    print('   A_1^7 reference:  rank %d, signature %s, det %s, two_elementary %s'
          % (A1_7.module_rank(), tuple(int(x) for x in A1_7.signature_pair()),
             int(A1_7.determinant()), tuple(int(x) for x in A_inv)))
    assert J.module_rank() == 7
    assert tuple(int(x) for x in J.signature_pair()) == (0, 7)
    assert int(J.determinant()) == -2 ** 7
    assert tuple(int(x) for x in invariants) == tuple(int(x) for x in A_inv)
    print('   the exhibited plane reproduces I_{0,7}(2) = A_1^7 = (7,7,1)')
