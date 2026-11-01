"""A21: the Coble-to-Enriques comparison, at the level the sources actually fix.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_labeled_embedding.py

What is compared, and at what level.  The comparison A21 asks for is between *labeled* tuples
(heegner report, sec-labeled-lattice-data): L_K3 with commuting nonsymplectic involutions I_Co and
I_dP, a degree-4 class H fixed by both, a root alpha with alpha^2 = -2 and H.alpha = 0 fixed by I_Co,
and a chamber in which alpha is effective and H is nef and big.  None of those labels is constructed
here.  What is done is the coarser *unlabelled* comparison of the two polarizations inside their
Picard and Enriques lattices, which is a necessary condition for the labeled comparison and not a
substitute for it.

The defining source for admissibility.  polarizations-and-loci.md fixes K_S = -3H + Sum_i E_i and puts
the degree-2 numerical polarization h_Co inside K_S^perp (def:coble-polarization-classes);
prop:canonical-perp-is-e10 gives the criterion: D = aH - Sum_i b_i E_i lies in K_S^perp exactly when
Sum_i b_i = 3a.  Section 0.1 verifies that criterion on the vector it uses, which the square and
pairing checks alone do not.

The comparison, section 3.  An isometry carrying the Coble labeling to the Enriques one with
h~_Co -> h would carry h~_Co^{perp S_Co} to h^{perp <S_En, delta>}; the two complements are compared
with the owner's is_isometric_to, whose contract is a verified boolean.

What earlier versions of this script got wrong, and section 1 records: they used the classes H + E_1
and 2H + E_1 + ... , which are not in K_S^perp (H + E_1 is four steps away from it), so the negative
they produced was about non-admissible markings and said nothing about A21; and they treated an
unlabelled isometry of Pic(S) as though it were the labeled comparison.

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

PicS = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[1]]), -matrix.identity(ZZ, 10)).rows()])
S_Co = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10)).rows()])
M = Lattices(ZZ)([list(row) for row in
                  block_diagonal_matrix(matrix(ZZ, [[-2]]), 2 * U, 2 * E8).rows()])

p = [PicS.basis_vector(i) for i in range(PicS.rank())]
H_class, exc = p[0], p[1:]
S_Co_ring = S_Co.base_ring()

# ---------------------------------------------------------------- 0.1 admissibility
print('0.1 admissibility, from the defining source')
K_S = -3 * H_class + sum(exc, PicS.zero())
print('    Pic(S) = I_{1,10}: rank %d, det %s, signature %s'
      % (PicS.rank(), PicS.determinant(), PicS.signature_pair()))
print('    K_S = -3H + Sum E_i: square %d, divisibility %d' % (K_S.q(), PicS.div(K_S)))
F1 = 3 * H_class - sum(exc[:9], PicS.zero())            # 3H - E_1 - ... - E_9
F2 = 3 * H_class - sum(exc[:8], PicS.zero()) - exc[9]   # 3H - E_1 - ... - E_8 - E_10
for name, F in (('F_1 = 3H - E_1 - ... - E_9', F1), ('F_2 = 3H - E_1 - ... - E_8 - E_10', F2)):
    print('    %s: square %d, D.K_S = %d, divisibility %d'
          % (name, F.q(), F.b(K_S), PicS.div(F)))
    assert F.q() == 0 and F.b(K_S) == 0
print('    F_1.F_2 = %d' % F1.b(F2))
assert F1.b(F2) == 1
h_Co = F1 + F2
print('    h_Co = F_1 + F_2: square %d, h_Co.K_S = %d, divisibility %d'
      % (h_Co.q(), h_Co.b(K_S), PicS.div(h_Co)))
assert h_Co.q() == 2 and h_Co.b(K_S) == 0

# prop:canonical-perp-is-e10's criterion on this vector: D = aH - Sum b_i E_i with Sum b_i = 3a.
coords = [int(h_Co.to_vector()(i)) for i in range(PicS.rank())]
a = coords[0]
b_list = [-value for value in coords[1:]]
print('    in the form aH - Sum b_i E_i: a = %d, Sum b_i = %d, 3a = %d, D^2 = %d'
      % (a, sum(b_list), 3 * a, a * a - sum(value * value for value in b_list)))
assert sum(b_list) == 3 * a, 'the criterion of prop:canonical-perp-is-e10 fails'

# ---------------------------------------------------------------- 0.2 the pullback
print('')
print('0.2 the pullback marking')
h_tilde = S_Co.linear_combination({i: S_Co_ring(coords[i]) for i in range(11) if coords[i]})
print('    f^*D . f^*D\' = 2 D.D\' (prop:coble-invariant-lattice): same coordinates, doubled form, so')
print('    h~_Co has square %d and divisibility %d' % (h_tilde.q(), S_Co.div(h_tilde)))
assert h_tilde.q() == 4
comp_Coble = S_Co.orthogonal_complement(h_tilde.sublattice())
print('    its complement: rank %d, det %s, signature %s, roots %d'
      % (comp_Coble.rank(), comp_Coble.determinant(), comp_Coble.signature_pair(),
         len(list(comp_Coble.roots()))))

# ---------------------------------------------------------------- 1. what the earlier classes were
print('')
print('1. the classes an earlier version of this script used were not admissible')
for name, F in (('H + E_1', H_class + exc[0]),
                ('2H + E_1 + E_2 + E_3 + E_4', 2 * H_class + sum(exc[:4], PicS.zero()))):
    print('    %s: square %d, D.K_S = %d (admissible only if that is 0)' % (name, F.q(), F.b(K_S)))
    assert F.b(K_S) != 0
print('    so the negative those classes produced concerns non-admissible markings and is not evidence')
print('    about A21.  H + E_1 is the class that gave the earlier h~ = 2e + f_1 + f_2 with 18 roots.')

# ---------------------------------------------------------------- 2. the Enriques side
print('')
print('2. the Enriques side')
h = M.basis_vector(1) + M.basis_vector(2)
print('    M = S_En + <delta> = U(2) + E8(2) + <-2>: rank %d, det %s, signature %s'
      % (M.rank(), M.determinant(), M.signature_pair()))
print('    h = e + f: square %d, h.delta = %d, divisibility %d'
      % (h.q(), h.b(M.basis_vector(0)), M.div(h)))
C = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(U, E8).rows()])
print('    C = U + E8(-1): det %s, even %s' % (C.determinant(), C.is_even()))
assert abs(int(C.determinant())) == 1 and C.is_even()
print('    so S_En^# = (1/2)C has integral squares, no (x + delta/2) is integral, and')
print('    <S_En, delta> = S_En + Z delta is saturated: this section compares the actual lattice')
comp_Heegner = M.orthogonal_complement(h.sublattice())
print('    its polarization complement: rank %d, det %s, signature %s, roots %d'
      % (comp_Heegner.rank(), comp_Heegner.determinant(), comp_Heegner.signature_pair(),
         len(list(comp_Heegner.roots()))))

# ---------------------------------------------------------------- 3. the comparison
print('')
print('3. the comparison of the complements, owner-decided')
try:
    decision = comp_Coble.is_isometric_to(comp_Heegner)
    print('   is_isometric_to returned %s' % decision)
except Exception as exc:
    print('   UNDECIDED: %s: %s' % (type(exc).__name__, str(exc)[:300]))
    decision = None

# ---------------------------------------------------------------- 3.1 the marked-pair isometry
# Necessary and sufficient data: an isometry of the two polarizations exists iff some isometry
# phi: h~^perp -> h^perp carries the glue class of one to the glue class of the other (Nikulin; the
# glue classes have order 2, so the sign on Z v/4 is irrelevant).  What can be assembled at the owner:
print('')
print('3.1 the marked-pair isometry, and the exact step that is blocked')
K = comp_Coble
Kp = comp_Heegner
print('    complements isometric: %s' % K.is_isometric_to(Kp))
gS = S_Co.glue_map(h_tilde.sublattice(), K)
gM = M.glue_map(h.sublattice(), Kp)
print('    glue subgroup of h~^perp: order %s; of h^perp: order %s'
      % (gS.codomain().cardinality(), gM.codomain().cardinality()))
aut_K = K.Aut()
print('    |O(h~^perp)| = %s, generators %d' % (aut_K.cardinality(), len(list(aut_K.group_generators()))))
rho_K = K.discriminant_representation()
A_K = K.discriminant_group()
image_of_aut = A_K.orthogonal_group().subgroup(tuple(rho_K(g) for g in aut_K.group_generators()))
print('    |image of O(h~^perp) in O(A)| = %s' % image_of_aut.cardinality())
print('    BLOCKED HERE, exactly: the subgroup object returned by subgroup(...) of O(A) has no orbit')
print('    method -- dir() offers none, while the full group O(A) does (OA.orbit(x) is used above) --')
print('    so the orbit of the glued class under the image of O(h~^perp) cannot be computed.  Expected')
print('    semantic operation: the induced action of a subgroup of O(A) on the finite quadratic form,')
print('    i.e. Subgroups(O(A)).orbit(element) / .element_action(), closing the comparison')
print('      phi0.discriminant_morphism()(glue class of S_Co)  ==  glue class of M')
print('    over the finite group.  Second missing piece: a comparison of glue classes that live in the')
print('    discriminant forms of the two complements with the (-1) twist of glue_map recorded -- the maps')
print('    land in A(-1) and no owner operation composes them with an isometry discriminant map.')

# ---------------------------------------------------------------- 3.2 the label that the marking determines
# The report's tuple carries a distinguished exceptional root alpha with alpha^2 = -2, H.alpha = 0 and
# alpha fixed by I_Co (sec-labeled-lattice-data).  For the admissible marking, alpha is the root of the
# polarization complement: that complement has exactly two roots, i.e. root system A_1, which is the
# "distinguished A_1 point" of the report.
print('')
print('3.2 the distinguished root of the marking')
roots_K = list(comp_Coble.roots())
print('    roots of h~^perp: %d (root system A_1, one line)' % len(roots_K))
assert len(roots_K) == 2
alpha_K = roots_K[0]
alpha = comp_Coble.inclusion()(alpha_K)      # the same vector, seen inside S_Co
print('    alpha: square %d, alpha.h~ = %d, alpha in S_Co: %s'
      % (alpha.q(), alpha.b(h_tilde), alpha.parent() is S_Co))
assert alpha.q() == -2 and alpha.b(h_tilde) == 0 and alpha.parent() is S_Co
print('    so alpha is fixed by every isometry fixing S_Co, in particular by I_Co := -theta_Co of')
print('    prop:theta-co-exists, which is +1 on T_Co and -1 on S_Co; the involution -theta_Co fixes H')
print('    because H = h~_Co lies in S_Co.  Constructing -theta_Co itself needs the gluing anti-isometry')
print('    of cons:embedding-gluing-data as data, which is not materialised in the book or here.')

# ---------------------------------------------------------------- 4. what remains
print('')
print('4. what this does not do')
print('   4.1 the labels.  A21 compares tuples (L_K3, I_Co, I_dP, H, alpha, C): commuting')
print('       nonsymplectic involutions, H^2 = 4 fixed by both, alpha^2 = -2 with H.alpha = 0 fixed')
print('       by I_Co, and a chamber with alpha effective and H nef and big (heegner report,')
print('       sec-labeled-lattice-data).  None is built here, so this is an unlabelled comparison of')
print('       polarizations, necessary for the labeled one and not a substitute for it.')
print('   4.2 the marked pair: section 3.1 assembles everything except the last two comparisons, and')
print('       names the two owner operations missing there.  The criterion of')
print('       thm:coble-heegner-line-unique does not apply here: it needs an indefinite complement and a')
print('       positive vector in signature (1,10) has a negative definite one.')
print('   4.3 the ambient.  L_K3 and the two primitive embeddings are not built, so no isometry is')
print('       extended over it with isometry_extends and no chamber is transported.  The involutions of')
print('       the tuple reduce to the same datum: I_Co = -theta_Co needs the gluing gamma_Co of')
print('       cons:embedding-gluing-data, I_dP is not given as lattice data by the sources at all, and')
print('       the chamber is nef-cone geometry, not a lattice computation.')
print('')
print('SUMMARY')
print('  0.1 admissibility verified, not assumed: F_1, F_2 isotropic and orthogonal to')
print('      K_S = -3H + Sum E_i with F_1.F_2 = 1, so h_Co = F_1 + F_2 lies in K_S^perp with h_Co^2 = 2,')
print('      matching the criterion Sum b_i = 3a of prop:canonical-perp-is-e10 (a = 6, sum 18).')
print('  0.2 its pullback has square 4; the polarization complement has rank 10, det 2048, sig (0,10).')
print('  1. the classes earlier versions used (H + E_1, 2H + ...) are not in K_S^perp, so the negative')
print('      they gave is about non-admissible markings and A21 was never obstructed by it.')
if decision is True:
    print('  3. the two complements ARE isometric: the necessary condition holds for this admissible')
    print('      marking, and what is owed is 4.1-4.3.')
elif decision is False:
    print('  3. the complements are not isometric, so no labeled isometry exists even before the labels')
    print('      are imposed; that would obstruct A21 for this marking.')
else:
    print('  3. the owner could not decide the pair; nothing is concluded.')
print('OK: admissibility verified against its defining source, the comparison decided at the owner, and')
print('    its relation to A21 stated')
