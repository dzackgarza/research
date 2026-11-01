"""A21: the labeled embedding comparison -- what can be checked now, and what cannot.

STATUS.  This script does not decide A21 and does not produce a counterexample to it.  It checks one
premise of the comparison at the owner (the retained polarization coordinates, section 0) and reports
the outcome of the comparison *on the modelled inputs it builds* (sections 2-3), which is conditional
on two premises it does not establish.  The premises are named in section 4.  The verified negative
recorded in section 3 is a statement about those models and is upgraded to a statement about A21 only
when sections 4.1-4.2 are discharged.

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

# ---------------------------------------------------------------- 0. the polarization coordinates
# prop:coble-invariant-lattice fixes Pic(S) = <H, E_1, ..., E_10> = I_{1,10} with H^2 = 1 and
# E_i^2 = -1, all orthogonal, and its proof fixes f^*D . f^*D' = 2 D.D'.  def:coble-polarization-classes
# takes h_Co = F_1 + F_2 with F_i^2 = 0, F_1.F_2 = 1 in the non-degenerate case.  Sections 0.1-0.2 check
# that such classes exist, that h_Co has the stated square, and that its pullback is the vector used
# below.
PIC_GRAM = block_diagonal_matrix(matrix(ZZ, [[1]]), -matrix.identity(ZZ, 10))
PicS = Lattices(ZZ)([list(row) for row in PIC_GRAM.rows()])
p_basis = [PicS.basis_vector(i) for i in range(PicS.rank())]
H_class, exc = p_basis[0], p_basis[1:]
print('0. the retained polarization, from its definition')
print('   Pic(S) = I_{1,10}: rank %d, det %s, signature %s'
      % (PicS.rank(), PicS.determinant(), PicS.signature_pair()))
F1 = H_class + exc[0]
F2 = H_class + exc[1]
print('   F_1 = H + E_1, F_2 = H + E_2: F_1^2 = %d, F_2^2 = %d, F_1.F_2 = %d'
      % (F1.q(), F2.q(), F1.b(F2)))
assert F1.q() == 0 and F2.q() == 0 and F1.b(F2) == 1
h_Co = F1 + F2
print('   h_Co = F_1 + F_2: h_Co^2 = %d, div(h_Co) = %d' % (h_Co.q(), PicS.div(h_Co)))
assert h_Co.q() == 2
print('   the book\'s pullback formula f^*D . f^*D\' = 2 D.D\' doubles coordinates and form, so')
print('   h_Co = 2H + E_1 + E_2 pulls back to 2 f^*H + f^*E_1 + f^*E_2, which is the vector used below')

# ---------------------------------------------------------------- 1. the Coble marked pair
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

# ---------------------------------------------------------------- 2. the Heegner marked pair (MODELLED)
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

# ---------------------------------------------------------------- 3. the comparison, on the modelled inputs
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
print('3. the comparison, on the modelled inputs only')
print('isometry decision of the two complements, by L.is_isometric_to:')
try:
    decision = comp_Coble.is_isometric_to(comp_Heegner)
    print('  is_isometric_to returned %s' % decision)
    decided = decision
except Exception as exc:
    print('  UNDECIDED: %s: %s' % (type(exc).__name__, str(exc)[:400]))
    decided = None

# ---------------------------------------------------------------- 4. the premises
print('')
print('4. premises this verdict is conditional on')
print('   4.1 the Enriques side is modelled by M = S_En + <delta> unsatured.  The actual lattice is')
print('       M = <S_En, delta> saturated in L_K3, and its saturation is governed by the gluing')
print('       anti-isometry gamma of cons:embedding-gluing-data, which the book supplies as a')
print('       construction and not as explicit matrices.  A different gamma gives a different M,')
print('       possibly with a different polarization complement.')
print('   4.2 the Coble marking is the isotropic pair F_1 = H + E_1, F_2 = H + E_2 of Pic(S), checked in')
print('       section 0 to satisfy the definition.  Other isotropic pairs of Pic(S) realize h_Co as')
print('       well; inside the family used they lie in one O(S_Co)-orbit, but the family is not proved')
print('       to be the only one.')
print('   4.3 neither L_K3 nor the two embeddings are built, so nothing here tests the extension of any')
print('       isometry over the ambient lattice.')
print('')
print('SUMMARY')
print('  0. the retained polarization coordinates are verified against def:coble-polarization-classes')
print('     and prop:coble-invariant-lattice at the owner: h_Co = 2H + E_1 + E_2, h_Co^2 = 2, and its')
print('     pullback is 2f^*H + f^*E_1 + f^*E_2 of square 4.')
if decided is False:
    print('  3. CONDITIONAL: for the modelled inputs the two polarization complements are not isometric')
    print('     (both rank 10, det 2048, signature (0,10), |A| = 2048; 18 roots against 2), and')
    print('     is_isometric_to returns False.  This is NOT yet a counterexample to A21: it is a')
    print('     statement about M = S_En + <delta> unsaturated and the marking of 4.2.')
elif decided is True:
    print('  3. CONDITIONAL POSITIVE: for the modelled inputs the complements are isometric; the marked')
    print('     pair isometry and its extension over L_K3 are still owed (4.3).')
else:
    print('  3. UNDECIDED for the modelled inputs; nothing is concluded.')
print('  To promote either verdict to A21 the premises 4.1-4.3 have to be discharged with the gluing')
print('  and saturation built as maintained semantic constructions, and the extension tested by')
print('  isometry_extends.  Until then A21 is open and no obstruction is recorded.')
print('OK: one premise verified, one comparison reported as conditional, no obstruction claimed')
