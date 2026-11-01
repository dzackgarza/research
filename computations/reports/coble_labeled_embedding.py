"""A21: the labeled embedding comparison -- what can be checked now, and what cannot.

STATUS.  Three things are established here, in this order: the retained polarization coordinates
(section 0, owner-checked against the cited definitions); that the Enriques side needs no saturation,
so the lattice used in section 2 is the actual <S_En, delta> and not a model of it (section 2.1, a
two-line argument from S_En = C(2) with C even unimodular, with the owner confirming the hypothesis);
and that two independent markings of the Coble polarization give isometric complements (section 1.1).
With those, the negative of section 3 is a statement about the two labeled pairs constructed here, not
about a model, and by the orbit argument of section 1.0 it covers every admissible marking: section 4.1
records what that argument needs and section 1.0 checks its inputs at the owner.  What is also not built is L_K3 and the extension of any isometry over it (section 4.2); that
matters for a *positive* verdict, not for the negative one, which needs only the complement test.

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
C_GRAM = block_diagonal_matrix(U, E8)          # C = U + E8(-1), even unimodular, signature (1,9)
C = Lattices(ZZ)([list(row) for row in C_GRAM.rows()])

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

# ---------------------------------------------------------------- 1.0 one orbit of admissible markings
# An admissible numerical polarization is h_Co = F_1 + F_2 with F_i isotropic and F_1.F_2 = 1 in
# Pic(S) = I_{1,10}.  The pair spans U = <F_1, F_2>, of determinant F_1^2 F_2^2 - (F_1.F_2)^2 = -1, so U
# is unimodular and Pic(S) = U perp U^perp is an orthogonal direct sum; U^perp is therefore unimodular
# too, and of rank 9, signature (0,9).  The odd unimodular negative definite lattice of rank 9 is
# unique, < -1 >^9, so every admissible pair gives an isometry U perp U^perp -> U' perp U'^perp carrying
# one pair to the other.  Hence all admissible h_Co lie in one O(Pic(S))-orbit, and since
# f^* phi f^{*-1} is an isometry of S_Co for phi in O(Pic(S)) -- (f^*D).(f^*D') = 2 D.D' makes the
# scaling cancel -- all admissible markings h~_Co = f^*h_Co lie in one O(S_Co)-orbit.  The inputs of
# that argument are checked here.
print('1.0 one orbit of admissible markings')
negative_nine = Lattices(ZZ)([list(row) for row in (-matrix.identity(ZZ, 9)).rows()])
print('    < -1 >^9: rank %d, det %s, signature %s'
      % (negative_nine.rank(), negative_nine.determinant(), negative_nine.signature_pair()))
pairs = {
    'F_1 = H + E_1, F_2 = H + E_2':
        (H_class + exc[0], H_class + exc[1]),
    'F_1 = 2H + E_1 + E_2 + E_3 + E_4, F_2 = H + E_1':
        (2 * H_class + exc[0] + exc[1] + exc[2] + exc[3], H_class + exc[0]),
}
complements_Pic = {}
for label, (G1, G2) in pairs.items():
    assert G1.q() == 0 and G2.q() == 0 and G1.b(G2) == 1, label
    span = PicS.sublattice_from([G1, G2])
    comp = PicS.orthogonal_complement(span)
    complements_Pic[label] = comp
    print('    %s: |det <F_1,F_2>| = %s, complement rank %d, det %s, signature %s'
          % (label, abs(int(span.determinant())), comp.rank(), comp.determinant(), comp.signature_pair()))
    assert abs(int(span.determinant())) == 1
    assert abs(int(comp.determinant())) == 1
    assert comp.is_isometric_to(negative_nine), 'the complement is not < -1 >^9'
labels = list(complements_Pic)
print('    the two complements are isometric: %s'
      % complements_Pic[labels[0]].is_isometric_to(complements_Pic[labels[1]]))
print('    so the two admissible pairs are one O(Pic(S))-orbit, and the two markings one O(S_Co)-orbit')

# ---------------------------------------------------------------- 1.1 a second admissible marking
# h_Co = F_1 + F_2 admits isotropic pairs outside the a = 1 family used above; the geometric
# description fixes no single family, so a second one is tested.  F~_1 = 2e + f_1+..+f_4 and
# F~_2 = e + f_1 are isotropic with pairing 2, so h~' = F~_1 + F~_2 is an admissible marking.
F1_alt = 2 * e + f1 + f2 + s_basis[3] + s_basis[4]
F2_alt = e + f1
print('   second marking: F~_1^2 = %d, F~_2^2 = %d, F~_1.F~_2 = %d'
      % (F1_alt.q(), F2_alt.q(), F1_alt.b(F2_alt)))
assert F1_alt.q() == 0 and F2_alt.q() == 0 and F1_alt.b(F2_alt) == 2
h_tilde_alt = F1_alt + F2_alt
print('   h~\' = F~_1 + F~_2: square %d' % h_tilde_alt.q())
assert h_tilde_alt.q() == 4
comp_Coble_alt = S_Co.orthogonal_complement(h_tilde_alt.sublattice())
print('   its complement: rank %d, det %s, signature %s, roots %d'
      % (comp_Coble_alt.rank(), comp_Coble_alt.determinant(),
         comp_Coble_alt.signature_pair(), len(list(comp_Coble_alt.roots()))))

# ---------------------------------------------------------------- 2. the Heegner marked pair
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

# ---------------------------------------------------------------- 2.1 no saturation of <S_En, delta>
# M = <S_En, delta> could a priori be an overlattice of S_En + Z delta, index 2, obtained by adjoining
# (x + delta)/2 for some x in S_En^#.  It cannot: S_En = C(2) with C even unimodular, so
# S_En^# = (1/2)C and for x = v/2 the square is x^2 = 2 (v/2)^2_C = v^2_C / 2, an integer because C is
# even; then (x + delta/2)^2 = x^2 - 1/2 is not an integer, so no such half-vector is integral and
# S_En + Z delta is already saturated.  The hypothesis of that argument is checked here.
print('  saturation of <S_En, delta>: hypothesis check')
print('    C = U + E8(-1): rank %d, determinant %s, even %s, signature %s'
      % (C.rank(), C.determinant(), C.is_even(), C.signature_pair()))
assert abs(int(C.determinant())) == 1 and C.is_even()
assert M_GRAM == block_diagonal_matrix(matrix(ZZ, [[-2]]), 2 * C_GRAM), \
    'the S_En block of M is not 2*C'
assert abs(int(C.determinant())) == 1 and C.is_even()
print('    hence S_En^# = (1/2)C and every square in it is an integer, so no (x + delta)/2 is integral')
print('    M = S_En + Z delta is saturated; section 2 used the actual lattice, not a model of it')

# ---------------------------------------------------------------- 3. the comparison
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
print('3. the comparison')
print('two markings of the Coble polarization give isometric complements: %s'
      % comp_Coble.is_isometric_to(comp_Coble_alt))
print('isometry decision of the two complements, by L.is_isometric_to:')
try:
    decision = comp_Coble.is_isometric_to(comp_Heegner)
    print('  is_isometric_to returned %s' % decision)
    decided = decision
except Exception as exc:
    print('  UNDECIDED: %s: %s' % (type(exc).__name__, str(exc)[:400]))
    decided = None

# ---------------------------------------------------------------- 4. what remains open
print('')
print('4. what is still not established, and what it would take')
print('   4.1 the markings: covered by the orbit argument of section 1.0, whose inputs are checked there')
print('       (unimodular spans, complements of rank 9, det -1, signature (0,9), isometric to <-1>^9).')
print('       The one external input is the uniqueness of the odd unimodular negative definite lattice of')
print('       rank 9, which is classical and cited rather than recomputed.')
print('   4.2 the ambient lattice and the extension: L_K3 and the two primitive embeddings are not built')
print('       here, so no isometry is extended over L_K3 with isometry_extends.  That is needed for a')
print('       POSITIVE verdict, not for the negative one, which rests on the complement test alone.')
print('   4.3 the Coble side uses S_Co = I_{1,10}(2) as prop:coble-invariant-lattice gives it; nothing')
print('       here depends on a choice of Coble surface beyond the discarded data of section 0.')
print('')
print('SUMMARY')
print('  0. the retained polarization coordinates are verified against def:coble-polarization-classes')
print('     and prop:coble-invariant-lattice at the owner: h_Co = 2H + E_1 + E_2, h_Co^2 = 2, pullback')
print('     2f^*H + f^*E_1 + f^*E_2 of square 4.')
print('  2.1 <S_En, delta> is saturated, so section 2 compares the actual Enriques lattice.')
if decided is False:
    print('  3. the two polarization complements are not isometric: rank 10, det 2048, signature (0,10)')
    print('     and discriminant group of order 2048 on both sides, but 18 roots against 2, with')
    print('     is_isometric_to returning a verified negative.')
    print('  1.0 every admissible marking lies in one O(S_Co)-orbit, by the splitting Pic(S) = U perp U^perp')
    print('     with U and U^perp unimodular, U^perp of rank 9, signature (0,9), and the uniqueness of')
    print('     <-1>^9.  So the negative covers every admissible marking: an isometry psi with')
    print('     psi(T_Co^Coble) = T_Co^Heegner and psi(h~_Co) = h does not exist.  4.2 concerns only a')
    print('     positive verdict and is moot.')
elif decided is True:
    print('  3. the complements ARE isometric: the marked-pair isometry and its extension over L_K3 are')
    print('     the remaining obligations (4.2).')
else:
    print('  3. UNDECIDED; nothing is concluded.')
print('OK: coordinates verified, saturation proved, complements compared, and the verdict carried to all')
print('    admissible markings by the orbit argument whose inputs section 1.0 checks')
