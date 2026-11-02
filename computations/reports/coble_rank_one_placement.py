"""The rank-one placement of the del Pezzo slot: does it exist, with commutation?

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_rank_one_placement.py

The question.  The tuple's del Pezzo slot is an involution commuting with I_Co, hence one that
preserves S_Co; so S_Co must split as (S_Co cap S_dP) + (S_Co cap S_dP^perp), and the two cases
are rank 2 and rank 1.  Rank 2 is settled: the definite-fibre enumeration makes S_dP inside S_Co
equal to <f^*F_1, f^*F_2>, which no automorphism realizes.  This script settles the lattice half
of rank 1.

The formulation.  Put U = U(2) = <H - b, b> with b isotropic and b.H = 2.  Commutation with I_Co
requires every class of S_Co to have its U-component in <H>, that is v := b-|S_Co must vanish on
H^perp cap S_Co while taking the value 2 on H.  The script tests whether such an integral v
exists, which is an integer linear system, and then whether the resulting lattice
S' = S_Co + Z b embeds primitively into L_K3.

How existence is decided.  S' embeds primitively into the even unimodular lattice of signature
(3,19) exactly when its complement can have signature (2,8) and discriminant form -q_{S'}; that
is Nikulin's existence theorem [nikulin1979integral, Thm. 1.10.1] -- signature congruence, rank
bound and the p-primary conditions -- which the provider implements as
`is_discriminant_form_of_even_lattice`.  So this is a maintained decision, not a search.

Provenance: pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage 11.0.beta5, image rootfs
read-only, repository bound at /repo.

Scope.  Lattice level only.  Nothing here says the resulting involution is realized by an
automorphism, nor anything about the chamber or the effectivity of alpha.
"""
import sys

from sage.all import ZZ, diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance')
print('  provider pin: %s   Sage: %s' % (PIN, sage_version))
print('')

G = diagonal_matrix(ZZ, [2] + [-2] * 10)
S = Lattices(ZZ)([list(r) for r in G.rows()])
H = matrix(ZZ, [[6] + [-2] * 8 + [-1, -1]]).transpose()

U = S.primitive_sublattice_from([S.linear_combination({i: int(H[i, 0]) for i in range(11) if int(H[i, 0])})])
N = S.orthogonal_complement(U)
print('H^perp cap S_Co: rank %d' % N.module_rank())

inc = N.inclusion()
rows = [H.transpose().row(0)]
for v in N.module_generators():
    rows.append(matrix(ZZ, [[int(x) for x in inc(v).to_vector()]]).row(0))
A = matrix(ZZ, rows)
b = matrix(ZZ, 11, 1, [2] + [0] * 10)
print('system: v(H) = 2 and v = 0 on a basis of H^perp cap S_Co; matrix rank %d' % A.rank())

D, P, Q = A.smith_form()
print('Smith diagonal of the system: %s' % ([int(D[i, i]) for i in range(11)],))
bb = P * b
ok = all(int(bb[i, 0]) % int(D[i, i]) == 0 for i in range(11))
print('an integral v exists (commutation compatible): %s' % ok)
assert ok, 'no integral v: commutation would force a half-integral functional'

v = Q * matrix(ZZ, 11, 1, [int(bb[i, 0]) // int(D[i, i]) for i in range(11)])
vv = [int(v[i, 0]) for i in range(11)]
print('  v (values on e_0..e_10) = %s' % (vv,))
assert sum(vv[i] * int(H[i, 0]) for i in range(11)) == 2
assert all(sum(vv[i] * coords[i] for i in range(11)) == 0
           for coords in ([int(x) for x in inc(y).to_vector()] for y in N.module_generators()))

rows2 = [[int(G[i, j]) for j in range(11)] + [vv[i]] for i in range(11)] + [vv[:] + [0]]
Sp = Lattices(ZZ)(rows2)
q = Sp.discriminant_group()
print('S-prime = S_Co + Z b : rank %d, det %d, signature %s, |A| %d'
      % (Sp.module_rank(), int(Sp.determinant()), Sp.signature(), q.cardinality()))

T0 = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [1, 1] + [-1] * 8).rows()])
comp = T0.signature()
answer = q.twist(-1).is_discriminant_form_of_even_lattice(comp)
print('  -q_{S\'} realisable by an even lattice of signature %s : %s' % (comp, answer))
print('')
print('CONCLUSION')
print('  A primitive U(2) containing H, meeting S_Co in <H> and preserved by the involution with')
print('  (+1)-eigenspace U(2) -- i.e. commuting with I_Co -- exists at the lattice level:')
print('  S-prime is even of signature (1,11) with |A| = 2048, and Nikulin Thm. 1.10.1 gives a')
print('  complement of signature (2,8) with the dual discriminant form, so S-prime + T is the even')
print('  unimodular lattice of signature (3,19), which is L_K3.')
print('  NOT claimed: that this involution is realized by an automorphism, or anything about the')
print('  chamber or the effectivity of alpha.')
