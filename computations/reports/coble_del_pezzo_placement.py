"""The isotropic classes of S_Co pairing 2 against H, enumerated on a definite lattice.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_del_pezzo_placement.py

The question.  Which isotropic classes a of S_Co = <2> + <-2>^10 satisfy a.H = 2?  Each
such a gives b = H - a, also isotropic with a.b = 2, so the pair spans a primitive U(2)
containing H.  If the only solutions are f^*F_1 and f^*F_2 then the rank-two placement of the
del Pezzo slot inside S_Co is unique and the corollary about the candidate covers that case
entirely.

Why this is not an enumeration over an indefinite lattice.  The obvious move --
elements_of_norm(-1) on the dual S_Co^# -- targets the whole indefinite lattice, whose
norm-(-1) fibre is infinite, and it is not a certificate of anything.  The intended problem is
finite, and it is made finite by working inside S_Co with no dual at all:

    a  |->  y := 2a - H

is a bijection from {a in S_Co : a^2 = 0, a.H = 2} onto {y in H^perp cap S_Co : y^2 = -4 and
y = H mod 2S_Co}.  Indeed (2a-H)^2 = 4a^2 - 4 a.H + H^2 = -4 when a^2 = 0 and a.H = 2, and
conversely a = (y+H)/2 is integral exactly when y = H mod 2S_Co, with (y+H)^2 = y^2 + H^2 = 0
and (y+H).H/2 = (0 + H^2)/2 = 2 because y is orthogonal to H.

H^perp cap S_Co is negative definite, since H^2 = 4 > 0, and the provider's
elements_of_norm enumerates the complete fibre precisely on definite lattices.  So the
enumeration below is exhaustive by construction, not by a search bound chosen here.

The completeness argument, stated before the enumerator is run:
  (i) a |-> 2a - H injects the solution set into the norm-(-4) fibre of H^perp cap S_Co;
  (ii) that fibre is finite and the provider returns all of it, the lattice being definite;
  (iii) every fibre element satisfying y = H mod 2S_Co is the image of a solution, by the
        computation above, and the script verifies a^2 = 0 and a.H = 2 for each.
Nothing is inferred from a bounded box.

Scope.  This is a statement about S_Co and H.  It says nothing about a geometric involution,
about Kaehler cones, about the chamber, or about effectivity; those obligations stay with the
geometric tuple, as recorded in the manuscript and TODO.

Provenance.  sage-extensions at provider pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage
11.0.beta5, shared image rootfs read-only, repository bound at /repo.
"""
import sys

from sage.all import ZZ, diagonal_matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, mounted read-only; repo bound at /repo')
print('')

S = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [2] + [-2] * 10).rows()])
ring = S.base_ring()
basis = [S.basis_vector(i) for i in range(11)]


def sparse(d):
    return S.linear_combination({i: ring(c) for i, c in d.items() if c})


H = sparse({0: 6, **{i: -2 for i in range(1, 9)}, 9: -1, 10: -1})
F1 = sparse({0: 3, **{i: -1 for i in range(1, 10)}})
F2 = sparse({0: 3, **{i: -1 for i in range(1, 9)}, 10: -1})
print('S_Co = <2> + <-2>^10 ; H = 6e_0 - 2(e_1+...+e_8) - e_9 - e_10, q(H) = %d' % int(H.q()))
assert int(H.q()) == 4

U = S.primitive_sublattice_from([H])
NH = S.orthogonal_complement(U)
print('H^perp cap S_Co: rank %d, determinant %d' % (NH.module_rank(), int(NH.determinant())))
print('  definite: %s' % (NH.is_definite(),))
assert NH.module_rank() == 10
assert NH.is_definite() is True, 'the complement is not definite: the enumeration would not be exhaustive'

fibre = NH.elements_of_norm(-4)
print('the norm-(-4) fibre of H^perp cap S_Co: cardinality %s' % (fibre.cardinality(),))

inc = NH.inclusion()
sols = []
for y in fibre:
    yS = inc(y)
    coords = [int(c) for c in yS.to_vector()]
    if any((coords[i] + [int(c) for c in H.to_vector()][i]) % 2 for i in range(11)):
        continue
    a = S.linear_combination(
        {i: ring((coords[i] + [int(c) for c in H.to_vector()][i]) // 2) for i in range(11)
         if (coords[i] + [int(c) for c in H.to_vector()][i]) != 0})
    assert int(a.q()) == 0, 'a is not isotropic'
    assert int(S.b(a, H)) == 2, 'a does not pair 2 against H'
    sols.append(a)

print('solution classes a of S_Co with a^2 = 0 and a.H = 2: %d' % len(sols))
for a in sols:
    print('   %s' % ([int(c) for c in a.to_vector()],))

found = {tuple(int(c) for c in a.to_vector()) for a in sols}
expected = {tuple(int(c) for c in F1.to_vector()), tuple(int(c) for c in F2.to_vector())}
print('they are exactly f^*F_1 and f^*F_2: %s' % (found == expected,))
assert found == expected, 'the solution set is not the published pair'

print('')
print('the authored root against the two isotropic summands')
alpha = S.linear_combination({0: 3, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1,
                              9: -1, 10: -1})
print('  alpha = 3e_0 - (e_1 + ... + e_10) : q(alpha) = %s, alpha.H = %s'
      % (int(alpha.q()), int(S.b(alpha, H))))
for name, a in (('f^*F_1', F1), ('f^*F_2', F2)):
    print('  alpha.%s = %s' % (name, int(S.b(alpha, a))))
assert int(alpha.q()) == -2 and int(S.b(alpha, H)) == 0
assert int(S.b(alpha, F1)) == 0 and int(S.b(alpha, F2)) == 0
print('  so alpha lies in the anti-invariant part of the slot: the operator that is +1 on')
print('  <f^*F_1, f^*F_2> and -1 on its complement sends alpha to -alpha.')
print('')
print('CONCLUSION')
print('  The only isotropic classes of S_Co pairing 2 against H are f^*F_1 and f^*F_2.')
print('  They are the two members of one pair, H - f^*F_1 = f^*F_2, so they span one primitive')
print('  U(2) = <f^*F_1, f^*F_2> containing H: inside S_Co the del Pezzo slot has a single')
print('  placement, and the corollary about that candidate covers the rank-two case entirely.')
print('  Also computed: the authored root is orthogonal to both summands, so the rank-two slot')
print('  reverses it.  Not claimed here: any statement about automorphisms, Kaehler cones, the')
print('  chamber or effectivity, and nothing about the case where the slot meets S_Co only in <H>.')
print('')
print('OK: the rank-two placement is unique, by a complete definite-fibre enumeration')
