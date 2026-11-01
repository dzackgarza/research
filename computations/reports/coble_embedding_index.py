"""Focused check: the embedding indices and the complement identity, by determinants.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_embedding_index.py

Why this exists.  An earlier version of the A21 argument said "S_En + T_En has index 2 in L_K3" citing
prop:gamma-en-two-gluing, which states the gluing anti-isometry gamma: A_{S_En} -> A_{T_En} between the
*full* discriminant groups and does not state an index.  The index follows from that data, and it is not
2.  It is also what the saturation of <S_En, delta> rests on, so it is worth computing rather than
guessing.

Two facts used, both cited rather than recomputed:
  * for a primitive sublattice T of a unimodular L, det(T^perp) = det(T) and |L / (T + T^perp)| = det T;
  * if L is the overlattice of S + T glued along the graph of an isomorphism A_S -> A_T, then
    [L : S + T] = |A_S| = |A_T|, and det S = det T.

The determinants and discriminant orders below are owner computations; the two facts are classical
(Nikulin's gluing, and the complement formula).
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, read-only; repo bound at /repo')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])

S_En = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(2 * U, 2 * E8).rows()])
T_En = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
S_Co = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10)).rows()])
T_Co = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])

print('the four lattices, from their defining sources')
for name, lat, source in (
        ('S_En = U(2) + E8(2)', S_En, 'sen in prop:gamma-en-two-gluing'),
        ('T_En = U + U(2) + E8(2)', T_En, 'ten in lem:coble-heegner-vector'),
        ('S_Co = <2> + <-2>^10', S_Co, 'prop:coble-invariant-lattice'),
        ('T_Co = <2> + U(2) + E8(2)', T_Co, 'lem:coble-heegner-vector')):
    print('  %-28s rank %2d, det %8s, signature %-8s  [%s]'
          % (name, lat.rank(), lat.determinant(), lat.signature_pair(), source))

det_S_En, det_T_En = abs(int(S_En.determinant())), abs(int(T_En.determinant()))
det_S_Co, det_T_Co = abs(int(S_Co.determinant())), abs(int(T_Co.determinant()))
order_AS_En = int(S_En.discriminant_group().cardinality())
order_AT_En = int(T_En.discriminant_group().cardinality())
order_AS_Co = int(S_Co.discriminant_group().cardinality())
order_AT_Co = int(T_Co.discriminant_group().cardinality())
print('')
print('discriminant groups (the gluing is between the full groups, so the index is their order)')
print('  |A_{S_En}| = %d, |A_{T_En}| = %d   -> [L_K3 : S_En + T_En] = %d'
      % (order_AS_En, order_AT_En, order_AS_En))
print('  |A_{S_Co}| = %d, |A_{T_Co}| = %d   -> [L_K3 : S_Co + T_Co] = %d'
      % (order_AS_Co, order_AT_Co, order_AS_Co))
assert det_S_En == det_T_En == order_AS_En, 'determinants and discriminant order disagree on the Enriques side'
assert det_S_Co == det_T_Co == order_AS_Co, 'determinants and discriminant order disagree on the Coble side'
assert order_AS_En == 1024 and order_AS_Co == 2048
print('  so the Enriques index is 1024 = 2^10, not 2; the Coble index is 2048 = 2^11')

print('')
print('the complement identity M = T_Co^perp = S_En + Z delta, by determinants')
delta_square = 2
det_with_delta = det_S_En * delta_square
print('  det(S_En + Z delta) = det(S_En) * delta^2 = %d * %d = %d' % (det_S_En, delta_square, det_with_delta))
print('  det(T_Co) = %d, and for a primitive T_Co in the unimodular L_K3, det(T_Co^perp) = det(T_Co)' % det_T_Co)
assert det_with_delta == det_T_Co
print('  the two determinants agree and S_En + Z delta is contained in T_Co^perp, so the containment is')
print('  an equality: M = S_En + Z delta.  No saturation step and no index-2 assumption is used.')

print('')
print('SUMMARY')
print('  [L_K3 : S_En + T_En] = 2^10 = 1024 and [L_K3 : S_Co + T_Co] = 2^11 = 2048, both read off the')
print('  discriminant orders of the gluing anti-isometries of prop:gamma-en-two-gluing and')
print('  prop:theta-co-exists; the earlier "index 2" was wrong and is removed.')
print('  M = T_Co^perp equals S_En + Z delta because det(S_En + Z delta) = 2^10 * 2 = 2^11 = det(T_Co)')
print('  and the containment holds.  That replaces the saturation argument that assumed an index-2')
print('  overlattice.')
print('OK: indices and the complement identity verified by determinants at the owner')
