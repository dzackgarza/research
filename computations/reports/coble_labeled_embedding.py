"""A21: the labeled embedding comparison of the retained Coble polarization with h.

The statement asked for.  A20(2) needs an isometry psi of L_K3 carrying the *Coble-labeled* structure
to the *Enriques-labeled* one and the retained polarization to h:

    psi(T_Co^{Coble}) = T_Co^{Heegner},      psi(h~_Co) = h,

where T_Co^{Coble} = S_Co^{perp L_K3}, T_Co^{Heegner} = delta^{perp T_En} inside T_En, so that
psi(S_Co) = (T_Co^{Heegner})^{perp} = <S_En, delta> and psi(h~_Co) = h.

The marked data are the book's, fixed here and not varied:

  Coble:    S_Co = <2> + <-2>^{10} = I_{1,10}(2) = (11,11,1)_1   (prop:coble-invariant-lattice),
            basis e = f^*H (e^2 = 2) and f_i = f^*E_i (f_i^2 = -2), and
            h~_Co = f^*h_Co = F~_1 + F~_2 with F~_i^2 = 0, F~_1.F~_2 = 2 (def:coble-polarization-classes,
            with f^*D . f^*D' = 2 D.D' from the proof of prop:coble-invariant-lattice).  In these
            coordinates h~_Co = 2e + f_1 + f_2 up to the sign of one f_i, which the isometry
            f_i -> -f_i of S_Co absorbs, so the marked pair (S_Co, h~_Co) is the data.
  Enriques: M = (T_Co^{Heegner})^{perp} = <S_En, delta> with S_En = U(2) + E8(2) = C(2),
            C = U + E8(-1), h = e + f in the U(2) summand, h^2 = 4 (prop:gamma-en-two-gluing), and
            delta the (-2)-vector of lem:coble-heegner-vector orthogonal to S_En.  This script models
            M by S_En + <delta> on the nose, and says below what the saturation would change.

A necessary condition, and where the owner decides it.  Both h~_Co and h are primitive vectors of
square 4, so an isometry of the marked pairs restricts to an isometry of the orthogonal complements
h~_Co^{perp} and h^{perp}; if those complements are not isometric, no psi exists with these markings.
The complements are built by owner operations (v.sublattice() for the rank-one subobject and
orthogonal_complement for its perp), their cheap invariants are printed, and the decision is
L.is_isometric_to, whose contract is a *verified boolean* and which raises rather than returning a
false negative when no exact classification decides the pair.  A False is an obstruction, an exception
is recorded as undecided, and a True is only a necessary condition met -- the marked-pair isometry and
its extension over L_K3 are then the next obligation (Nikulin's criterion, the owner's
isometry_extends / isometry_extension on the ambient gluing).

Scope of the obstruction, stated exactly.  Three things bound it and none of them is silently assumed:

  * the Heegner side is modelled by M = S_En + <delta> on the nose, i.e. with delta primitive in
    <S_En, delta> and no saturation gain in L_K3.  If the saturation of S_En + <delta> is larger, the
    complement tested here is replaced by a sublattice of finite index of it and the comparison has to
    be redone; that is an open side condition, not a conclusion;
  * the Coble marking tested is h~_Co = 2e + f_1 + f_2, coming from F~_i = e + f_i (i = 1, 2) for the
    isotropic pair.  Every admissible pair in the a = 1 family, h~_Co = 2e + f_i +- f_j with i != j,
    lies in one O(S_Co)-orbit -- permute the f's and change signs -- so within that family the marked
    pair is unique.  Whether some isotropic pair outside that family realizes h_Co = F_1 + F_2 as well
    is a separate question this script does not settle;
  * the complements are compared, not the marked pairs, and not the ambient L_K3.  A matching
    complement isometry would still owe the marked-pair condition and its extension; a mismatching one
    already obstructs, which is the case here.

What this script does not do: it does not build L_K3 as the gluing overlattice of either decomposition,
and it does not claim that a matching complement isometry extends.  Those are the phase-two
obligations, stated in the summary and in TODO A21.

Provenance is printed before anything is computed.
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
print('  image rootfs: $HOME/sage-image/rootfs, mounted read-only; repo bound at /repo')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])

# ---------------------------------------------------------------- the Coble marked pair
S_CO_GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10))
S_Co = Lattices(ZZ)([list(row) for row in S_CO_GRAM.rows()])
s_basis = [S_Co.basis_vector(i) for i in range(S_Co.rank())]
e = s_basis[0]
f1, f2 = s_basis[1], s_basis[2]
h_tilde = 2 * e + f1 + f2
print('S_Co = <2> + <-2>^10: rank %d, det %s, signature %s'
      % (S_Co.rank(), S_Co.determinant(), S_Co.signature_pair()))
print('  e^2 = %d, f_i^2 = %d, h~_Co^2 = %d, div(h~_Co) = %d'
      % (e.q(), f1.q(), h_tilde.q(), S_Co.div(h_tilde)))
assert h_tilde.q() == 4

# ---------------------------------------------------------------- the Heegner marked pair
M_GRAM = block_diagonal_matrix(matrix(ZZ, [[-2]]), 2 * U, 2 * E8)
M = Lattices(ZZ)([list(row) for row in M_GRAM.rows()])
m_basis = [M.basis_vector(i) for i in range(M.rank())]
delta = m_basis[0]
h = m_basis[1] + m_basis[2]
print('M = S_En + <delta> = U(2) + E8(2) + <-2>: rank %d, det %s, signature %s'
      % (M.rank(), M.determinant(), M.signature_pair()))
print('  delta^2 = %d, delta.h = %d, h^2 = %d, div(h) = %d'
      % (delta.q(), delta.b(h), h.q(), M.div(h)))
assert h.q() == 4 and delta.b(h) == 0

# ---------------------------------------------------------------- the polarization complements
comp_Coble = S_Co.orthogonal_complement(h_tilde.sublattice())
comp_Heegner = M.orthogonal_complement(h.sublattice())
for name, comp, vector in (('Coble', comp_Coble, h_tilde), ('Heegner', comp_Heegner, h)):
    print('%s: complement of the polarization has rank %d, det %s, signature %s'
          % (name, comp.rank(), comp.determinant(), comp.signature_pair()))
    roots = list(comp.roots())
    print('    roots (square -2 vectors) in the complement: %d' % len(roots))
    print('    |A_complement| = %d' % comp.discriminant_group().cardinality())

# ---------------------------------------------------------------- the owner's verified decision
print('')
print('isometry decision of the two complements, by L.is_isometric_to:')
try:
    decision = comp_Coble.is_isometric_to(comp_Heegner)
    print('  is_isometric_to returned %s' % decision)
    decided = decision
except Exception as exc:
    print('  UNDECIDED: %s: %s' % (type(exc).__name__, str(exc)[:400]))
    decided = None

print('')
print('SUMMARY')
if decided is False:
    print('  OBSTRUCTION: the complements of the two polarizations are not isometric, so no isometry of')
    print('  L_K3 carries h~_Co to h with these markings, and A20(2) cannot be closed by a labeled isometry.')
    print('  The invariant recorded above is the complement lattice itself (rank, determinant, signature,')
    print('  roots, discriminant group), not a single number, so the obstruction is stated as a lattice.')
elif decided is True:
    print('  NECESSARY CONDITION MET, not yet A21: the complements are isometric.  Still owed are the')
    print('  marked-pair isometry h~_Co -> h (the discriminant/gluing condition of Nikulin) and its')
    print('  extension over L_K3 built as the gluing overlattice, through isometry_extends.')
else:
    print('  UNDECIDED: the owner has no exact classification for this pair.  Nothing is concluded, and the')
    print('  handoff is an isometry decision for definite lattices of rank 10 with 2-power discriminant.')
print('  Scope: M = S_En + <delta> unsatured, the Coble marking h~_Co = 2e + f_1 + f_2 (unique up to')
print('  O(S_Co) within the a = 1 family of isotropic pairs), and the complements compared rather than the')
print('  marked pairs or the ambient L_K3.  Nothing is claimed for other markings or for a saturated M.')
print('OK: the comparison was made and its outcome recorded, whatever it is')
