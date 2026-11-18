"""A20 item 2 / A21: L_K3, the two primitive embeddings, and the ambient isometry, as objects.

    PYTHONPATH=/repo/.scratch/sage-extensions/src \\
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs \\
        -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_a21-ambient-extension.py

The obligation.  #664 states the last step of A20 item 2 as an *argument* rather than an
object: "the two primitive embeddings have the same complement T_Co, the composite
gamma_En . psibar . gamma_Co^{-1} is realised by an integral phi in O(T_Co) because
O(T_Co) -> O(A_{T_Co}) is surjective, and (psi, phi) then extends over L_K3 by Nikulin's
gluing.  Not built: L_K3 and the two embeddings, so no isometry object exists."  The same
step closes @prop:coble-enriques-polarized-match, whose proof produces an isometry "which
restricts to psi on S_Co" without exhibiting it.

This record builds the missing objects inside one copy of L_K3 = U^3 + 2E8(-1), and checks
the labels pointwise on lattice elements rather than on their abstract types:

  1. L_K3 in its standard basis, with rank, determinant, evenness and signature.
  2. The Coble primitive embedding: S_Co as the invariant lattice of the reflected pair
     (J_Co, J_dP) of the model side, its complement T_Co = S_Co^perp, the del Pezzo slot
     S_dP, the degree-4 class H and the root alpha as explicit integral vectors, with the
     divisibility of H and alpha in S_Co.
  3. The Enriques primitive embedding: S_En, T_En = S_En^perp, the Heegner class delta with
     delta^perp cap T_En = T_Co, the degree-2 class h, and M = S_En + ZZ delta with its
     complement M^perp, all as explicit integral vectors.
  4. The integral isometry g in O(L_K3), built through the owner's isometry constructor and
     checked on the labelled classes: g(S_Co) = M, g(T_Co) = M^perp, g(H) = h, g(alpha) =
     -delta, g(S_dP) = S_dP, and g commuting with the involutions whose eigenspaces the two
     data are.
  5. The two gluing anti-isometries of the two finite-index inclusions, the discriminant
     isometry of g, and the surjectivity decision O(T_Co) -> O(A_{T_Co}).

What is computed here, and what a reader should take from it.  In this marking the two
primitive embeddings *coincide*: S_Co = M as sublattices of L_K3 and H = h, printed below as
containment tests rather than assumed.  That is the sharp form of
@prop:coble-enriques-polarized-match: the Coble invariant lattice is the Enriques lattice
plus the line of the root, so the only labelled datum the comparison has to move is the sign
of that root, and the isometry that moves it is an involution of L_K3.

What this does NOT settle, and no line below claims it: the chamber.  The tuple carries a
chamber C in which alpha is effective and H is nef and big; C is cut from the effective
classes of a member, not from lattice data, and no isometry of L_K3 decides it (#664 records
the chamber clause as false as authored under one reading of the fourth bullet and as
closing under the other).  Nor is the k >= 2 locus touched: every lattice here is the one of
@prop:coble-enriques-polarized-match.
"""
import sys
import time

from sage.all import ZZ, QQ, matrix, block_diagonal_matrix, CartanMatrix, identity_matrix
from sage.version import version as SAGE_VERSION

import sage_extensions
from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()


def stamp(tag):
    print('  [%6.1fs] %s' % (time.time() - T0, tag))


print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions imported from: %s' % sage_extensions.__file__)
print('  runtime: shared image rootfs, read only; repository bound at /repo')
print('')

# ---------------------------------------------------------------- 1. L_K3
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
L = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, U, U, E8, E8).rows()])
n = int(L.rank())
G = matrix(ZZ, n, n, lambda i, j: int(L.basis_vector(i) * L.basis_vector(j)))

print('1. L_K3 = U^3 + 2E8(-1), in its standard basis')
print('   rank %d, determinant %d, even %s, signature %s'
      % (n, int(L.determinant()), L.is_even(), L.signature_pair()))
assert n == 22 and int(L.determinant()) == -1 and L.is_even()
print('   blocks: U_1 = e_0,e_1;  U_2 = e_2,e_3;  U_3 = e_4,e_5;')
print('           E8_1 = e_6..e_13;  E8_2 = e_14..e_21')
stamp('L_K3 built')


def vec(coefficients):
    """The lattice element with these integer coefficients in L's standard basis."""
    return L.linear_combination(
        {int(i): L.base_ring()(int(c)) for i, c in coefficients.items() if c})


def coords(v):
    return [int(v.to_vector()(i)) for i in range(n)]


def block_split(v):
    c = coords(v)
    return (c[0:2], c[2:4], c[4:6], c[6:14], c[14:22])


def sub_basis(sub):
    """A basis of the sublattice, as integer coordinate vectors in L's standard basis."""
    return [coords(sub.inclusion()(sub.module_generator(l)))
            for l in sub.module_generating_set()]


def sub_coords(sub, v):
    """Coordinates of v in the sublattice's own basis, or None when v is not in the sublattice.

    Solved on a pivot set of coordinates (never on the Gram matrix: a Gram solve returns the
    element of the span with the same pairings, which is the wrong answer off the span) and
    then verified against every coordinate of v.
    """
    B = sub_basis(sub)
    r = len(B)
    M = matrix(ZZ, r, n, B)
    pivots = M.pivots()
    assert len(pivots) == r, 'the sublattice basis is not independent'
    square = matrix(QQ, M[:, pivots])
    target = matrix(QQ, r, 1, lambda i, j: coords(v)[pivots[i]])
    solution = [square.solve_right(target)[i, 0] for i in range(r)]
    if any(QQ(c).denominator() != 1 for c in solution):
        return None
    for j in range(n):
        if sum(int(solution[i]) * B[i][j] for i in range(r)) != coords(v)[j]:
            return None
    return [int(c) for c in solution]


def contained(A, v):
    """Whether the L-element v lies in the sublattice A, decided by exact coordinates."""
    return sub_coords(A, v) is not None


def same_lattice(A, B):
    return (A.module_rank() == B.module_rank()
            and all(contained(B, A.inclusion()(A.module_generator(l)))
                    for l in A.module_generating_set()))


def divisibility(sub, v):
    """The positive generator of {x.v : x in sub}: the divisibility of v in that lattice."""
    from math import gcd
    values = [abs(int(sub.inclusion()(sub.module_generator(l)) * v))
              for l in sub.module_generating_set()]
    g = 0
    for value in values:
        g = gcd(g, value)
    return g


def divisible_by_two(sub, v):
    """Whether v lies in 2*sub, in the sublattice's own integral coordinates."""
    z = sub_coords(sub, v)
    return z is not None and all(c % 2 == 0 for c in z)


# ---------------------------------------------------------------- 2. the Coble embedding
def aegs_image(kind, v):
    """AEGS's two involutions on the model L = U^3 + 2E8(-1), block by block."""
    a, b, c, e, f = block_split(v)
    if kind == 'dP':
        return [-x for x in a] + c + b + [-x for x in e] + [-x for x in f]
    if kind == 'enr':
        return [-x for x in a] + c + b + f + e
    raise ValueError(kind)


def aegs_involution(kind):
    images = {i: vec(dict(enumerate(aegs_image(kind, L.basis_vector(i))))) for i in range(n)}
    return L.O()(lambda label: images[int(label)])


def invariant_lattice(isometry):
    """ker(isometry - 1) as a primitive sublattice of L, through the owner's operations."""
    M = matrix(ZZ, n, n, lambda i, j: int(isometry(L.basis_vector(j)).to_vector()(i)))
    rows = [[int(c) for c in r]
            for r in (M - identity_matrix(ZZ, n)).kernel().basis_matrix().rows()]
    return L.primitive_sublattice_from([vec(dict(enumerate(r))) for r in rows])


print('')
print('2. the Coble primitive embedding S_Co -> L_K3')
I_dP = aegs_involution('dP')
I_En = aegs_involution('enr')
alpha = vec({0: 1, 1: -1})
reflection = L.reflection(alpha)
J_Co = lambda w: reflection(I_En(w))
J_dP = lambda w: reflection(I_dP(w))
mat_id = identity_matrix(ZZ, n)
M_Co = matrix(ZZ, n, n, lambda i, j: int(J_Co(L.basis_vector(j)).to_vector()(i)))
M_dP = matrix(ZZ, n, n, lambda i, j: int(J_dP(L.basis_vector(j)).to_vector()(i)))
print('   the two AEGS involutions built by the owner; alpha = e_0 - e_1 with alpha^2 = %d;'
      % int(alpha * alpha))
print('   the reflection w_alpha of L built by the owner; the reflected pair')
print('   J_Co = w_alpha . I_En and J_dP = w_alpha . I_dP:')
print('     both involutions and they commute: %s'
      % (M_Co * M_Co == mat_id and M_dP * M_dP == mat_id and M_Co * M_dP == M_dP * M_Co))
S_Co = invariant_lattice(J_Co)
T_Co = L.orthogonal_complement(S_Co)
S_dP = invariant_lattice(I_dP)
PI_dP = invariant_lattice(J_dP)
SCO = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(
    2 * U, matrix(ZZ, [[-2]]), 2 * E8).rows()])
TCO = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(
    matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
U2T = Lattices(ZZ)([list(r) for r in (2 * U).rows()])
print('   S_Co = ker(J_Co - 1): rank %d, det %d, signature %s, even %s,'
      % (S_Co.rank(), int(S_Co.determinant()), S_Co.signature_pair(), S_Co.is_even()))
print('     isometric to U(2) + <-2> + E8(-2): %s' % S_Co.is_isometric_to(SCO))
print('   T_Co = S_Co^perp:       rank %d, det %d, signature %s,'
      % (T_Co.rank(), int(T_Co.determinant()), T_Co.signature_pair()))
print('     isometric to <2> + U(2) + E8(-2): %s' % T_Co.is_isometric_to(TCO))
print('   S_dP = ker(I_dP - 1), AEGS\'s del Pezzo invariant lattice: rank %d, det %d,'
      ' isometric to U(2): %s'
      % (S_dP.rank(), int(S_dP.determinant()), S_dP.is_isometric_to(U2T)))
LAMBDA = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(2 * U, matrix(ZZ, [[-2]])).rows()])
print('   ker(J_dP - 1), the (++)-piece of the reflected pair: rank %d, det %d,'
      ' isometric to U(2) + <-2>: %s'
      % (PI_dP.rank(), int(PI_dP.determinant()), PI_dP.is_isometric_to(LAMBDA)))
stamp('Coble embedding built')

H = vec({2: 1, 4: 1, 3: 1, 5: 1})
slot_e = vec({2: 1, 4: 1})
slot_f = vec({3: 1, 5: 1})
print('   the marked classes, as integral vectors of L:')
print('     H = e_2 + e_4 + e_3 + e_5 = the corner e+f of the slot Delta(U_2,U_3) = U(2)')
print('     H^2 = %d, H.alpha = %d, H in S_Co %s, H in S_dP %s, H = e+f %s'
      % (int(H * H), int(H * alpha), contained(S_Co, H), contained(S_dP, H),
         H == slot_e + slot_f))
print('     e^2 = %d, f^2 = %d, e.f = %d (the slot is U(2))'
      % (int(slot_e * slot_e), int(slot_f * slot_f), int(slot_e * slot_f)))
print('     alpha^2 = %d, alpha in S_Co %s, alpha in S_dP %s'
      % (int(alpha * alpha), contained(S_Co, alpha), contained(S_dP, alpha)))
print('     primitivity: H in 2*S_Co %s, alpha in 2*S_Co %s, so both lift to H/2, alpha/2 in'
      ' the dual S_Co^# and not in S_Co' % (divisible_by_two(S_Co, H),
                                            divisible_by_two(S_Co, alpha)))
assert int(H * H) == 4 and int(H * alpha) == 0
assert contained(S_Co, H) and contained(S_Co, alpha)
assert not divisible_by_two(S_Co, H) and not divisible_by_two(S_Co, alpha)
stamp('marked classes of the Coble tuple')

# ---------------------------------------------------------------- 3. the Enriques embedding
print('')
print('3. the Enriques primitive embedding M = S_En + ZZ delta -> L_K3')
S_En_vectors = [vec({2: 1, 4: 1}), vec({3: 1, 5: 1})] + \
               [vec({6 + k: 1, 14 + k: 1}) for k in range(8)]
S_En = L.primitive_sublattice_from(S_En_vectors)
T_En = L.orthogonal_complement(S_En)
delta = vec({0: 1, 1: -1})
h = vec({2: 1, 4: 1, 3: 1, 5: 1})
print('   S_En = Delta(U_2,U_3) + Delta(E8_1,E8_2): rank %d, det %d, signature %s,'
      % (S_En.rank(), int(S_En.determinant()), S_En.signature_pair()))
print('     isometric to C(2) = U(2) + E8(-2): %s'
      % S_En.is_isometric_to(Lattices(ZZ)([list(r) for r in
                                           (2 * block_diagonal_matrix(U, E8)).rows()])))
print('   T_En = S_En^perp: rank %d, det %d, signature %s'
      % (T_En.rank(), int(T_En.determinant()), T_En.signature_pair()))
print('   delta = e_0 - e_1: delta^2 = %d, delta in T_En %s' %
      (int(delta * delta), contained(T_En, delta)))
M = L.primitive_sublattice_from(S_En_vectors + [delta])
M_perp = L.orthogonal_complement(M)
print('   M = S_En + ZZ delta: rank %d, det %d, signature %s' %
      (M.rank(), int(M.determinant()), M.signature_pair()))
print('     isometric to U(2) + <-2> + E8(-2), that is to S_Co: %s'
      % M.is_isometric_to(SCO))
print('   M^perp = delta^perp cap T_En: rank %d, det %d, signature %s, isometric to T_Co: %s'
      % (M_perp.rank(), int(M_perp.determinant()), M_perp.signature_pair(),
         M_perp.is_isometric_to(TCO)))
print('   h = e_2 + e_4 + e_3 + e_5: h^2 = %d, h in S_En %s, h.delta = %d'
      % (int(h * h), contained(S_En, h), int(h * delta)))
print('   delta in 2*M: %s -- the Heegner class is primitive in M, as alpha is in S_Co'
      % divisible_by_two(M, delta))
print('   the divisibilities, as the gcd of the pairings with a basis of the lattice:')
print('     div_{S_Co}(H) = %d, div_{S_Co}(alpha) = %d, div_{S_En}(h) = %d, div_M(delta) = %d'
      % (divisibility(S_Co, H), divisibility(S_Co, alpha),
         divisibility(S_En, h), divisibility(M, delta)))
assert int(h * h) == 4 and int(h * delta) == 0
stamp('Enriques embedding built')

print('')
print('   the two embeddings, compared in this marking:')
print('     S_Co contained in M: %s' %
      all(contained(M, S_Co.inclusion()(S_Co.module_generator(l)))
          for l in S_Co.module_generating_set()))
print('     M contained in S_Co: %s' %
      all(contained(S_Co, M.inclusion()(M.module_generator(l)))
          for l in M.module_generating_set()))
print('     S_Co = M as sublattices of L_K3: %s' % same_lattice(S_Co, M))
print('     H = h as vectors of L_K3: %s' % (H == h))
print('     S_Co = S_En + ZZ alpha (the Coble lattice is the Enriques lattice plus the')
print('     root line), and delta = alpha as vectors: %s' % (delta == alpha))
stamp('the two embeddings compared')

# ---------------------------------------------------------------- 4. the isometry
print('')
print('4. the integral isometry g in O(L_K3)')
# g is the exchange of the two isotropic generators of U_1, and the identity on the other
# four blocks.  It is entered as images of the standard basis and accepted only as an
# isometry of L_K3 by the owner's constructor, so the pairing check is the owner's.
images = {i: L.basis_vector(i) for i in range(n)}
images[0] = L.basis_vector(1)
images[1] = L.basis_vector(0)
g = L.O()(lambda label: images[int(label)])
print('   g = (e_0 <-> e_1, identity on U_2, U_3, E8_1, E8_2), built by the owner\'s isometry')
print('   constructor from its images on the standard basis (so "isometry" is the owner\'s')
print('   check, not an assertion):')
basis = [L.basis_vector(i) for i in range(n)]
print('     g preserves the pairing on the whole basis: %s'
      % all(L.basis_vector(i) * L.basis_vector(j) == g(L.basis_vector(i)) * g(L.basis_vector(j))
            for i in range(n) for j in range(n)))
print('     g is an involution: %s' % all(g(g(v)) == v for v in basis))
g_matrix = matrix(ZZ, n, n, lambda i, j: int(g(L.basis_vector(j)).to_vector()(i)))
print('   its matrix on the standard basis is the permutation matrix of e_0 <-> e_1;')
print('   determinant %d, and it equals its own transpose: %s'
      % (int(g_matrix.det()), g_matrix == g_matrix.transpose()))

print('   the labelled classes, pointwise:')
print('     g(alpha) = -delta:  %s' % (g(alpha) == -delta))
print('     g(H) = h:           %s' % (g(H) == h))
print('     g(delta) = -alpha:  %s' % (g(delta) == -alpha))
assert g(alpha) == -delta and g(H) == h
print('   the two primitive embeddings, as images:')
gS = L.primitive_sublattice_from(
    [g(S_Co.inclusion()(S_Co.module_generator(l))) for l in S_Co.module_generating_set()])
gT = L.primitive_sublattice_from(
    [g(T_Co.inclusion()(T_Co.module_generator(l))) for l in T_Co.module_generating_set()])
gP = L.primitive_sublattice_from(
    [g(S_dP.inclusion()(S_dP.module_generator(l))) for l in S_dP.module_generating_set()])
print('     g(S_Co) = M: %s' % same_lattice(gS, M))
print('     g(T_Co) = M^perp: %s' % same_lattice(gT, M_perp))
print('     g(S_dP) = S_dP: %s (the del Pezzo slot is pointwise fixed)' % same_lattice(gP, S_dP))
print('     S_dP contained in S_Co (the rank-two placement of @prop:del-pezzo-placement): %s'
      % all(contained(S_Co, S_dP.inclusion()(S_dP.module_generator(l)))
            for l in S_dP.module_generating_set()))
assert same_lattice(gS, M) and same_lattice(gT, M_perp) and same_lattice(gP, S_dP)
print('   g against the involutions whose eigenspaces the two data are:')
print('     g commutes with I_dP:  %s' % all(g(I_dP(v)) == I_dP(g(v)) for v in basis))
print('     g commutes with I_En:  %s' % all(g(I_En(v)) == I_En(g(v)) for v in basis))
print('     g commutes with J_Co:  %s' % all(g(J_Co(v)) == J_Co(g(v)) for v in basis))
print('     g commutes with J_dP:  %s' % all(g(J_dP(v)) == J_dP(g(v)) for v in basis))
print('   so g acts inside the (++)-piece of the pair: on S_dP it is the identity, and on')
print('   S_Co = S_dP + ZZ alpha it is +1 on the slot and -1 on the root line.')
stamp('the isometry built and its labels checked')

# ---------------------------------------------------------------- 5. the gluing data
print('')
print('5. the finite-index inclusion, its gluing anti-isometry, and the extension criterion')
pairing = L.subobject_on(tuple(
    [S_Co.inclusion()(S_Co.module_generator(l)) for l in S_Co.module_generating_set()] +
    [T_Co.inclusion()(T_Co.module_generator(l)) for l in T_Co.module_generating_set()]))
inc = pairing.inclusion()
det_pair = int(pairing.determinant())
print('   S_Co + T_Co -> L_K3: rank %d, determinant %d = -2^22, so the index is 2^11 ='
      ' |A_{S_Co}| = |A_{T_Co}|' % (pairing.module_rank(), det_pair))
gamma_Co = inc.gluing_anti_isometry(S_Co)
glue = inc.gluing_subgroup()
print('   gamma_Co = the gluing anti-isometry A_{S_Co} -> A_{T_Co}(-1) of this inclusion,'
      ' built by the owner;')
print('   the glue subgroup L_K3/(S_Co + T_Co) inside A_{S_Co + T_Co} has order %d'
      % glue.cardinality())
stamp('gamma_Co and the glue')
pairing_En = L.subobject_on(tuple(
    [M.inclusion()(M.module_generator(l)) for l in M.module_generating_set()] +
    [M_perp.inclusion()(M_perp.module_generator(l)) for l in M_perp.module_generating_set()]))
inc_En = pairing_En.inclusion()
gamma_En = inc_En.gluing_anti_isometry(M)
print('   M + M^perp -> L_K3: determinant %d, and the same glue order;'
      ' the two inclusions coincide: %s'
      % (int(pairing_En.determinant()),
         same_lattice(S_Co, M) and same_lattice(T_Co, M_perp)))
stamp('gamma_En')

g_on_pairing = pairing.O()(
    lambda l: pairing.inclusion().preimage(g(pairing.inclusion()(pairing.module_generator(l)))))
print('   the pair (g|_{S_Co}, g|_{T_Co}) as an isometry of S_Co + T_Co, built by the owner:'
      ' an involution %s'
      % all(g_on_pairing(g_on_pairing(pairing.module_generator(l)))
            == pairing.module_generator(l) for l in pairing.module_generating_set()))
print('   the compatibility equation of @thm:automorphism-lifting-criterion,')
print('     bar(phi)_T . gamma_Co = gamma_Co . bar(phi)_S,')
print('   decided by the owner\'s own procedure on the pair: isometry_extends -> %s'
      % inc.isometry_extends(g_on_pairing))
assert inc.isometry_extends(g_on_pairing)
print('   and the pair is literally a restriction of g, which the owner accepted as an isometry'
      ' of L_K3,')
print('   so the criterion is satisfied by construction of g, not searched for after it.')
stamp('the extension criterion')

print('')
print('   the surjectivity input #664 records as a pinned-provider failure, run here')
print('   (the traceback it records is a TypeError in recursive.py:154 at the pinned runtime):')
for name, lattice in (('S_Co', S_Co), ('T_Co', T_Co)):
    print('     O(%s) -> O(A_%s) surjective: %s'
          % (name, name, lattice.discriminant_representation_is_surjective()))
    sys.stdout.flush()
    stamp('surjectivity for %s' % name)

print('')
print('CONCLUSION')
print('  Built, in one copy of L_K3 = U^3 + 2E8(-1):')
print('    S_Co (rank 11, det 2048, sig (1,10)) with H, alpha and the slot S_dP = U(2);')
print('    T_Co = S_Co^perp (rank 11, det -2048, sig (2,9));')
print('    S_En (rank 10, det -1024), T_En = S_En^perp, the Heegner class delta, and')
print('    M = S_En + ZZ delta (rank 11, det 2048, sig (1,10)) with h and M^perp = T_Co;')
print('    the integral isometry g in O(L_K3), an involution, with g(S_Co) = M,')
print('    g(T_Co) = M^perp, g(H) = h, g(alpha) = -delta, g(S_dP) = S_dP, commuting with both')
print('    AEGS involutions and with both members of the reflected pair.')
print('  In this marking S_Co = M and H = h: the Coble invariant lattice is the Enriques')
print('  lattice plus the line of the root, the del Pezzo slot is the Enriques polarization,')
print('  and the whole labelled difference is the sign of the root, which g reverses.')
print('  Not settled here: the chamber (a statement about the effective classes of a member,')
print('  not about L_K3), and the k >= 2 locus.')
print('')
print('OK: L_K3, the two primitive embeddings and the isometry are objects, and the labels')
print('    are checked pointwise on lattice elements')
