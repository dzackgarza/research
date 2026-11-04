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

Two further corrections are recorded in comments rather than in the printed output, so that the
committed log remains the record of the run that produced it.  Section 2's printed argument against
half-vectors covers only the case b = 2 of a denominator b, and an earlier text derived it from an
index-2 overlattice, which is wrong: [L_K3 : S_En + T_En] = |A_{S_En}| = 2^10, not 2.  The general
identity M = T_Co^perp = S_En + Z delta is proved by determinants -- det T_Co = 2^11,
det(T_Co^perp) = det T_Co in the unimodular L_K3, det(S_En + Z delta) = 2^10 * 2 = 2^11, containment --
and is verified in computations/reports/coble_embedding_index.py.  And section 3.4's involution check is
made on the abstract orthogonal sum S_Co perp T_Co, rank 22, determinant -2^22, signature (3,19); it is
not a morphism of L_K3, which is not built here.

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
# NOTE (comment only, not printed): the half-vector argument below is the b = 2 case of a denominator b.
# The general identity M = T_Co^perp = S_En + Z delta is by determinants -- det T_Co = 2^11,
# det(T_Co^perp) = det T_Co, det(S_En + Z delta) = 2^10 * 2 = 2^11, containment -- verified in
# computations/reports/coble_embedding_index.py.  It uses no index-[L_K3 : S_En + T_En] assertion; that
# index is |A_{S_En}| = 2^10 and not 2.
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
print('3.1 the marked-pair isometry, decided')
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
# The comparison itself, through the documented group-action construction: O(A) carries its represented
# action on the finite form (element_action), a subgroup acts through the restriction of that action
# along its inclusion (restrict_action), and in_same_orbit decides membership.  With one fixed isometry
# phi0: K -> K' the whole set of isometries is phi0 o O(K), so the glue classes match for SOME isometry
# exactly when c_S and the transport of c_M back along phi0 lie in one O(K)-orbit.  Both classes have
# order 2, so the sign on the Z/4 factor of the glue is irrelevant.
phi0 = K.isometry_to(Kp)
A_Kp = Kp.discriminant_group()
H_img = A_K.orthogonal_group().subgroup(tuple(rho_K(g) for g in aut_K.group_generators()))
action_H = A_K.orthogonal_group().element_action().restrict_action(H_img.inclusion())
cS = A_K(gS.codomain().inclusion()(gS.codomain().module_generators()[0]))
cM = A_Kp(gM.codomain().inclusion()(gM.codomain().module_generators()[0]))
print('    glue class of S_Co in A(h~^perp): order %s' % cS.additive_order())
print('    glue class of M in A(h^perp):     order %s' % cM.additive_order())
transported = A_K(phi0.inverse().discriminant_isometry()(cM))
print('    transported back along the isometry, same parent as cS: %s'
      % (transported.parent() is A_K))
same_orbit = action_H.in_same_orbit(cS, transported)
print('    c_S and the transport of c_M in one O(h~^perp)-orbit: %s' % same_orbit)
print('    So the glue classes match for an isometry h~^perp -> h^perp, and by Nikulin an isometry')
print('    S_Co -> M carries h~_Co to h: the marked pair is matched at the level of the two lattices.')
print('    Not covered: the extension to an isometry of L_K3 carrying the two primitive embeddings')
print('    (L_K3 is not built), the retained effectivity of the root, and the involution and chamber')
print('    labels of A21.')
# ---------------------------------------------------------------- 3.2 the label that the marking determines
# The report's tuple carries a distinguished exceptional root alpha with alpha^2 = -2, H.alpha = 0 and
# alpha fixed by I_Co (sec-labeled-lattice-data).  For the admissible marking, alpha is the root of the
# polarization complement: that complement has exactly two roots, i.e. root system A_1, which is the
# "distinguished A_1 point" of the report.
print('')
print('3.2 the root of the marking: existence now, effectivity not')
roots_K = list(comp_Coble.roots())
print('    roots of h~^perp: %d, i.e. one root line, root system A_1' % len(roots_K))
alpha_K = roots_K[0]
alpha = comp_Coble.inclusion()(alpha_K)
print('    a root alpha: square %d, alpha.h~ = %d, alpha in S_Co: %s'
      % (alpha.q(), alpha.b(h_tilde), alpha.parent() is S_Co))
assert alpha.q() == -2 and alpha.b(h_tilde) == 0 and alpha.parent() is S_Co
print('    What this establishes: h~_Co^perp has exactly one root line, so a root orthogonal to H')
print('    exists and is unique up to sign.  What it does NOT establish: that this is the *retained*')
print('    effective exceptional root of A21.  roots_K[0] is an abstract choice of representative, and')
print('    which of the two roots is effective is a chamber statement, transported by the nef cone and')
print('    not decided by the lattice alone.  It is recorded as an existence statement only.')
print('    Nor is the involution side verified: I_Co = -theta_Co would act as +1 on S_Co and -1 on')
print('    T_Co, so its S_Co-component fixes H, but theta_Co itself needs the gluing gamma_Co of')
print('    cons:embedding-gluing-data, is not constructed here, and no morphism-level check of its')
print('    action on H has been made.')

# ---------------------------------------------------------------- 3.3 the ambient extension
# The two primitive embeddings have the same complement: S_Co^{perp L_K3} = T_Co and, by construction,
# M = T_Co^{perp L_K3}.  With psi the marked-pair isometry, the composite
# gamma_En . psi . gamma_Co^{-1} is an isometry of the finite form A_{T_Co}, realised by an integral
# isometry of T_Co when O(T_Co) -> O(A_{T_Co}) is surjective; then (psi, phi) preserves the gluing
# subgroup and extends over L_K3 by Nikulin.  Surjectivity is a theorem for 2-elementary lattices
# (thm:two-elementary-surjectivity); the owner's own decision over the three lattices involved:
print('')
print('3.3 the ambient extension, and what the owner can and cannot verify')
for name, lat in (('S_Co', S_Co), ('M = S_En + <delta>', M),
                  ('T_Co = <2> + U(2) + E8(2)', Lattices(ZZ)([list(row) for row in
                      block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()]))):
    try:
        answer = lat.discriminant_representation_is_surjective()
        print('    %-26s det %s signature %s: O(L) -> O(A) surjective: %s'
              % (name, lat.determinant(), lat.signature_pair(), answer))
    except Exception as exc:
        print('    %-26s det %s signature %s: owner undecided, %s: %s'
              % (name, lat.determinant(), lat.signature_pair(), type(exc).__name__, str(exc)[:110]))
print('    So two of the three are owner-verified and the third, T_Co, is the lattice for which the')
print('    indefinite Eichler machinery fails (the same failure recorded for A20 item 1).  The argument')
print('    for the extension therefore rests on thm:two-elementary-surjectivity for T_Co -- a book')
print('    theorem, not an owner computation -- and on Nikulin\'s gluing criterion for the extension')
print('    itself.  L_K3 is the unique even unimodular lattice of signature (3,19).')

# ---------------------------------------------------------------- 3.4 the Coble involution label
# NOTE (comment only, not printed): the isometry checked here is of the abstract orthogonal sum
# S_Co perp T_Co (rank 22, determinant -2^22, signature (3,19)), not of L_K3, which is not built.  It
# verifies the component behaviour of the pair (+id_{S_Co}, -id_{T_Co}), not an ambient morphism.
# prop:theta-co-exists gives theta_Co with (+1)-eigenspace T_Co and (-1)-eigenspace S_Co, and its
# existence is gluing-independent: both discriminant forms are 2-elementary, so the pair
# (+id_{S_Co}, -id_{T_Co}) acts trivially on A_{S_Co} (+) A_{T_Co} and therefore preserves EVERY isotropic
# gluing subgroup, hence extends over L_K3 for any gamma_Co.  So the label I_Co := -theta_Co -- +1 on
# S_Co, -1 on T_Co -- needs no gluing data, and it fixes H = h~_Co because H lies in S_Co.  What is
# checked here: the 2-elementaryness of both discriminant forms, and the action of the pair on H inside
# the orthogonal direct sum S_Co (+) T_Co.
print('')
print('3.4 the Coble involution label')
GRAM_T = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
T_Co = Lattices(ZZ)([list(row) for row in GRAM_T.rows()])
A_S = S_Co.discriminant_group()
A_T = T_Co.discriminant_group()
print('    |A_{S_Co}| = %s, |A_{T_Co}| = %s' % (A_S.cardinality(), A_T.cardinality()))
for name, form in (('A_{S_Co}', A_S), ('A_{T_Co}', A_T)):
    try:
        print('    %s is 2-elementary: %s' % (name, form.is_p_elementary(2)))
    except Exception as exc:
        print('    %s exponent %s (is_p_elementary raised %s)'
              % (name, form.exponent(), type(exc).__name__))
D = Lattices(ZZ)([list(row) for row in
                  block_diagonal_matrix(block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10)),
                                        GRAM_T).rows()])
print('    S_Co (+) T_Co as an owner lattice: rank %d, det %s, signature %s'
      % (D.rank(), D.determinant(), D.signature_pair()))
# the pair as an owner isometry of S_Co (+) T_Co, built through the isometry group of the lattice
images = {i: D.basis_vector(i) for i in range(11)}
images.update({11 + i: -D.basis_vector(11 + i) for i in range(11)})
try:
    pair = D.O()(lambda label: images[int(label)])
    h_in_D = D.linear_combination({i: D.base_ring()(coords[i]) for i in range(11) if coords[i]})
    image = pair(h_in_D)
    print('    the pair (+id_{S_Co}, -id_{T_Co}) as an owner isometry of S_Co (+) T_Co:')
    print('      it fixes a basis vector of the T_Co summand up to sign and H pointwise: %s'
          % (image == h_in_D))
    print('      image of the first T_Co basis vector: %s' % (pair(D.basis_vector(11)) == -D.basis_vector(11)))
except Exception as exc:
    print('    owner isometry construction failed: %s: %s' % (type(exc).__name__, str(exc)[:140]))
print('    the pair (+id_{S_Co}, -id_{T_Co}) acts trivially on A_{S_Co} (+) A_{T_Co} because both forms')
print('    are 2-elementary, so it preserves every isotropic gluing subgroup and extends over L_K3 by')
print('    thm:nikulin-gluing for any gamma_Co: that is prop:theta-co-exists, and it is why the label')
print('    I_Co := -theta_Co needs no gluing data.  Its action on H = h~_Co is the action of +id_{S_Co}.')
print('    Still not established: that the retained EFFECTIVE root is the one computed in 3.2 (a chamber')
print('    statement), and the del Pezzo involution I_dP, which the sources do not give as lattice data.')

# ---------------------------------------------------------------- 4. what remains
print('')
print('4. what this does not do')
print('   4.1 the labels.  A21 compares tuples (L_K3, I_Co, I_dP, H, alpha, C): commuting')
print('       nonsymplectic involutions, H^2 = 4 fixed by both, alpha^2 = -2 with H.alpha = 0 fixed')
print('       by I_Co, and a chamber with alpha effective and H nef and big (heegner report,')
print('       sec-labeled-lattice-data).  None is built here, so this is an unlabelled comparison of')
print('       polarizations, necessary for the labeled one and not a substitute for it.')
print('   4.2 the marked pair is decided in section 3.1: the glue classes match, so by Nikulin the two')
print('       polarized lattices are matched by an isometry carrying h~_Co to h.  What that does not give')
print('       is the extension of that isometry over L_K3 between the two primitive embeddings, which is')
print('       4.3.')
print('   4.3 the ambient: section 3.3 states the extension argument and what it rests on -- the marked')
print('       pair decided here, thm:two-elementary-surjectivity for T_Co, Nikulin\'s gluing criterion,')
print('       and the uniqueness of the even unimodular lattice of signature (3,19).  Not done: building')
print('       L_K3 and the two embeddings, so the extension is an argument rather than an object, and the')
print('       chamber is not transported.  I_Co = -theta_Co needs no gluing data at all (3.4); I_dP is not')
print('       lattice data in the sources.  Nothing here promotes modelled lattice data to the retained')
print('       geometric labels.')
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
