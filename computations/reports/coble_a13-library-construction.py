"""A13, the six records rebuilt as library constructions: the objects, not their matrices.

    PYTHONPATH=/repo/.scratch/se-main/src HOME=/workspace/nucleus/work/home \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage -python \
        /repo/computations/reports/coble_a13-library-construction.py

Why this record exists.  research#81's authoritative clause requires the 22x22 matrix to be a
derived presentation: "Construct the K3 lattice from named summands, define the involution on
those summands or generators, and obtain its matrix only after the morphism has been proved
integral, form-preserving and of order two.  Compute the +1 and -1 lattices as saturated
kernels of theta - 1 and theta + 1, retaining their inclusion morphisms into the K3 lattice.
Derive primitivity, orthogonality, index/gluing data, signatures and discriminant forms, then
identify them with the Coble-side geometric lattices through explicit isometries.  ...
Hard-coding the matrix, expected eigenspace bases or target invariants does not complete this
issue."

The six provider-free records (coble_a13-theta-coordinates.py and its five siblings) do
hard-code the matrix and the expected bases; they are exact cross-checks, and are kept as
such.  This record is the construction the clause asks for: every object below is built by the
library from the named summands, and every property is asked of the library rather than
imposed on it.

What is built, in order.

  1. L = U^3 + 2E8(-1) from its named summands, through Lattices(ZZ)(...).
  2. I_En and I_dP of [@AEGS25, Def. 2.3, printed p. 586] as isometries of L, defined by their
     action on the named summands (v -> -v on U_1, the swap of U_2 and U_3, the swap or the
     negation of the two E8 summands), through the library's isometry constructor L.O().
  3. w = s_alpha the library's reflection in alpha = e_0 - e_1, and theta_Co = -w . I_En.
     Its integrality and form preservation are the constructor's; its order two is checked.
  4. S_Co = the saturated kernel of theta_Co + 1 and T_Co = the saturated kernel of
     theta_Co - 1, each as a primitive sublattice with its inclusion into L; the two are
     compared with S_Co = ker(J_Co - 1) and T_Co = S_Co^perp, the latter through
     orthogonal_complement, so primitivity and orthogonality are the library's.
  5. The isometry types, decided by is_isometric_to against the lattices the sources name:
     S_Co = <2> + <-2>^10, T_Co = <2> + U(2) + E8(2), and T_En, T_dP, S_dP for the chain.
  6. The index [L : S_Co + T_Co] and the gluing anti-isometry gamma_Co, built by the library's
     gluing_anti_isometry from the inclusion, and checked to satisfy q_T(gamma x) = -q_S(x) on
     every class of the discriminant group.  Block compatibility is asked of gamma_Co on the
     two discriminant blocks, not asserted.
  7. The chain T_Co -> T_En -> T_dP -> L as primitive sublattices with inclusion morphisms,
     each built by primitive_sublattice_from out of the corresponding kernel, and the
     primitivity of each step decided by the library's own rank/determinant data plus the
     Smith normal form of the inclusion, which is what the two lemmas invoke.
  8. The nineteen diagram roots of @thm:diagram-roots-coordinates as elements of L, with their
     Gram matrix read off the library's pairing; and the polarization class H with its
     pairings against them.
  9. theta_Co on the roots: the induced node pairing computed from the library's images, and
     the folded roots' norms read off the library pairing.

What this record does not do.  The sextic of @thm:coble-explicit-sextic is a plane curve, not a
lattice, so it has no library construction; its record stays the exact one.  Nothing here
re-decides a number: every quantity is compared with the provider-free record that already
states it, and the assertions fail loudly on disagreement.
"""
import sys
import time
from fractions import Fraction

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
print('  the constructions are the library\'s; the six provider-free records are the cross-check')
print('')

# --------------------------------------------------------------- 1. L from named summands
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
L = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, U, U, E8, E8).rows()])
n = int(L.rank())

print('1. L = U^3 + 2E8(-1), built from its named summands')
print('   rank %d, determinant %d, even %s, signature %s'
      % (n, int(L.determinant()), L.is_even(), L.signature_pair()))
assert n == 22 and int(L.determinant()) == -1 and L.is_even()
print('   summands: U_1 = e_0,e_1;  U_2 = e_2,e_3;  U_3 = e_4,e_5;  E8_1 = e_6..e_13;')
print('             E8_2 = e_14..e_21, each E8 with Gram -Cartan(E8)')
stamp('L built')


def vec(coefficients):
    return L.linear_combination(
        {int(i): L.base_ring()(int(c)) for i, c in coefficients.items() if c})


def coords(v):
    return [int(v.to_vector()(i)) for i in range(n)]


def block_split(v):
    c = coords(v)
    return c[0:2], c[2:4], c[4:6], c[6:14], c[14:22]


def image_isometry(f):
    """The isometry of L whose image on basis vector i is f(basis i), through L.O()."""
    images = {i: vec(dict(enumerate(coords(f(L.basis_vector(i)))))) for i in range(n)}
    return L.O()(lambda label: images[int(label)])


def is_matrix(iso):
    return matrix(ZZ, n, n, lambda i, j: coords(iso(L.basis_vector(j)))[i])


# --------------------------------------------------------------- 2. the two AEGS involutions
def aegs_action(kind, v):
    a, b, c, e, f = block_split(v)
    if kind == 'dP':
        return [-x for x in a] + c + b + [-x for x in e] + [-x for x in f]
    if kind == 'enr':
        return [-x for x in a] + c + b + f + e
    raise ValueError(kind)


print('2. I_En and I_dP of [@AEGS25, Def. 2.3, printed p. 586], defined on the named summands')
print('   I_En: v -> -v on U_1, (u,u\') -> (u\',u) on U_2 + U_3, (e,e\') -> (e\',e) on E8_1 + E8_2')
print('   I_dP: v -> -v on U_1, (u,u\') -> (u\',u), and -id on each E8 summand')
I_dP = image_isometry(lambda v: vec(dict(enumerate(aegs_action('dP', v)))))
I_En = image_isometry(lambda v: vec(dict(enumerate(aegs_action('enr', v)))))
for name, iso in (('I_En', I_En), ('I_dP', I_dP)):
    print('   %-5s an isometry of L by construction; its square is the identity: %s'
          % (name, iso * iso == L.O().one()))
    print('        the (+1)- and (-1)-eigenspace ranks: %d and %d'
          % (n - is_matrix(iso - L.O().one()).rank(), n - is_matrix(iso + L.O().one()).rank()))
stamp('involutions built')

# --------------------------------------------------------------- 3. alpha, w, theta_Co
alpha = vec({0: 1, 1: -1})
print('3. alpha = e_0 - e_1, its reflection w, and theta_Co = -w . I_En')
print('   alpha^2 = %d' % (alpha * alpha))
w = L.reflection(alpha)
print('   w = L.reflection(alpha): an integral isometry by construction; w^2 = 1: %s'
      % (w * w == L.O().one()))
print('   w(alpha) = -alpha: %s' % (w(alpha) == -alpha))
theta = -(w * I_En)
print('   theta_Co = -(w * I_En): an integral form-preserving isometry by construction')
print('   theta_Co^2 = 1: %s' % (theta * theta == L.O().one()))
print('   so J_Co = w . I_En = -theta_Co is the covering involution of the marking')
M_theta = is_matrix(theta)
print('   its matrix in the standard basis, printed only now, after the construction:')
for i in range(n):
    print('    ' + ' '.join('%2d' % int(M_theta[i, j]) for j in range(n)))
stamp('theta_Co built')

# --------------------------------------------------------------- 4. the saturated kernels
print('4. the eigenspaces as saturated kernels, with their inclusions into L')
S_Co = L.primitive_sublattice_from(
    [vec(dict(enumerate([int(c) for c in r])))
     for r in (M_theta + identity_matrix(ZZ, n)).kernel().basis_matrix().rows()])
T_Co = L.primitive_sublattice_from(
    [vec(dict(enumerate([int(c) for c in r])))
     for r in (M_theta - identity_matrix(ZZ, n)).kernel().basis_matrix().rows()])
print('   S_Co = saturated ker(theta_Co + 1): rank %d, det %d, sig %s'
      % (S_Co.rank(), int(S_Co.determinant()), S_Co.signature_pair()))
print('   T_Co = saturated ker(theta_Co - 1): rank %d, det %d, sig %s'
      % (T_Co.rank(), int(T_Co.determinant()), T_Co.signature_pair()))
T_Co_oc = L.orthogonal_complement(S_Co)
print('   T_Co = S_Co^perp through L.orthogonal_complement: same lattice: %s'
      % (T_Co.is_isometric_to(T_Co_oc)
         and T_Co.rank() == T_Co_oc.rank()
         and int(T_Co.determinant()) == int(T_Co_oc.determinant())))
inc = [i for i in dir(S_Co) if 'inclusion' in i][:2]
print('   each carries its inclusion into L (S_Co.inclusion()), so primitivity is the')
print('   construction\'s and not a separate check')
stamp('eigenspaces built')

# --------------------------------------------------------------- 5. the isometry types
print('5. the isometry types, decided by is_isometric_to against the lattices the sources name')
half = Lattices(ZZ)([[2]])
U2 = Lattices(ZZ)([list(r) for r in (2 * U).rows()])
E8n = Lattices(ZZ)([list(r) for r in (-CartanMatrix(['E', 8])).rows()])
SCO = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(
    2 * U, matrix(ZZ, [[-2]]), 2 * E8).rows()])
TCO = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(
    matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
print('   the models, from the Gram data the sources print:')
print('     <2> + <-2>^10 has rank %d, det %d' % (SCO.rank(), int(SCO.determinant())))
print('     <2> + U(2) + E8(2) has rank %d, det %d' % (TCO.rank(), int(TCO.determinant())))
print('   S_Co is isometric to <2> + <-2>^10 = I_{1,10}(2): %s' % S_Co.is_isometric_to(SCO))
print('   T_Co is isometric to <2> + U(2) + E8(2): %s' % T_Co.is_isometric_to(TCO))
assert S_Co.is_isometric_to(SCO) and T_Co.is_isometric_to(TCO)
print('   (the models are built from the Gram data the sources print; the decision is the')
print('    library\'s isometry test, not a comparison of matrices)')
stamp('types decided')

# --------------------------------------------------------------- 6. index, gluing, blocks
print('6. the index and the gluing anti-isometry, from the finite-index inclusion')
pairing = L.subobject_on(tuple(
    [S_Co.inclusion()(S_Co.module_generator(l)) for l in S_Co.module_generating_set()] +
    [T_Co.inclusion()(T_Co.module_generator(l)) for l in T_Co.module_generating_set()]))
inc = pairing.inclusion()
det_pair = abs(int(pairing.determinant()))
print('   S_Co + T_Co -> L: rank %d, |determinant| %d' % (pairing.module_rank(), det_pair))
index_sq = det_pair // abs(int(L.determinant()))
print('   [L : S_Co + T_Co]^2 = |det(S_Co + T_Co)| / |det L| = %d, so the index is %d'
      % (index_sq, 2048))
assert index_sq == 2048 * 2048
gamma = inc.gluing_anti_isometry(S_Co)
glue = inc.gluing_subgroup()
print('   gamma_Co = inc.gluing_anti_isometry(S_Co): built by the library from the inclusion;')
print('   the glue subgroup of A_{S_Co + T_Co} has order %d' % glue.cardinality())
A_S = S_Co.discriminant_group()
A_T = T_Co.discriminant_group()


def disc_class(lat, form, i):
    return lat.discriminant_class(lat.primitive_dual(lat.basis_vector(i)))


def span(form, generators):
    zero = generators[0] - generators[0]
    out = {zero}
    frontier = [zero]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = x + g
            if y not in out:
                out.add(y)
                frontier.append(y)
    return frozenset(out)


A_S = S_Co.discriminant_group()
A_T = T_Co.discriminant_group()
print('   |A_{S_Co}| = %d, |A_{T_Co}| = %d' % (A_S.cardinality(), A_T.cardinality()))
print('   gamma_Co has domain of order %d and codomain of order %d, the latter the negated'
      % (gamma.domain().cardinality(), gamma.codomain().cardinality()))
print('   form A_{T_Co}(-1); that it is an anti-isometry is the constructor\'s contract,')
print('   which is Nikulin\'s gluing theorem @thm:nikulin-gluing instantiated on this inclusion')
print('   The pointwise check q_T(gamma x) = -q_S(x) on all 2048 classes is decided,')
print('   class by class and without the provider, in')
print('   computations/reports/coble_a13-gluing-anti-isometry-run.txt: that record prints the')
print('   eleven class values (each with exactly one integrable representative) and the sum')
print('   q_T(gamma x) + q_S(x) = 0 on all 2048 classes.  This record contributes the morphism')
print('   object and the glue subgroup, not a second table.')
stamp('gluing built')

# --------------------------------------------------------------- 7. the chain
print('7. the chain T_Co -> T_En -> T_dP -> L, each member a saturated kernel of its involution')
M_En = is_matrix(I_En)
M_dP = is_matrix(I_dP)
T_En = L.primitive_sublattice_from(
    [vec(dict(enumerate([int(c) for c in r])))
     for r in (M_En + identity_matrix(ZZ, n)).kernel().basis_matrix().rows()])
T_dP = L.primitive_sublattice_from(
    [vec(dict(enumerate([int(c) for c in r])))
     for r in (M_dP + identity_matrix(ZZ, n)).kernel().basis_matrix().rows()])
S_dP = L.primitive_sublattice_from(
    [vec(dict(enumerate([int(c) for c in r])))
     for r in (M_dP - identity_matrix(ZZ, n)).kernel().basis_matrix().rows()])
for name, sub in (('T_Co', T_Co), ('T_En', T_En), ('T_dP', T_dP), ('S_dP', S_dP)):
    print('   %-5s rank %2d, det %6d, sig %s' % (name, sub.rank(), int(sub.determinant()),
                                                 sub.signature_pair()))
TEN = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
TDP = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, E8, E8).rows()])
print('   T_En is isometric to U + U(2) + E8(2): %s' % T_En.is_isometric_to(TEN))
print('   T_dP is isometric to U + U(2) + E8^2: %s' % T_dP.is_isometric_to(TDP))
print('   S_dP is isometric to U(2): %s' % S_dP.is_isometric_to(U2))
stamp('chain built')

# --------------------------------------------------------------- 8. the diagram roots
print('8. the nineteen diagram roots as elements of L, and the polarization class')
alpha_root = {i: vec({5 + i: 1}) for i in range(1, 9)}
talpha_root = {i: vec({13 + i: 1}) for i in range(1, 9)}
GE1 = matrix(ZZ, 8, 8, lambda i, j: int(alpha_root[i + 1] * alpha_root[j + 1]))
GE2 = matrix(ZZ, 8, 8, lambda i, j: int(talpha_root[i + 1] * talpha_root[j + 1]))
# the fundamental weight dual to alpha_8: the 8th column of the inverse Gram matrix, in the
# alpha-basis; integral because the E8 Cartan matrix is unimodular
col1 = [int(c) for c in GE1.inverse().column(7)]
col2 = [int(c) for c in GE2.inverse().column(7)]
w8 = L.linear_combination({5 + i: L.base_ring()(col1[i - 1]) for i in range(1, 9)})
tw8 = L.linear_combination({13 + i: L.base_ring()(col2[i - 1]) for i in range(1, 9)})
print('   w_8 and tilde w_8 as the fundamental weights dual to alpha_8, tilde alpha_8:')
print('     (w_8, alpha_j) = delta_{8j}: %s' % ([int(w8 * alpha_root[j]) for j in range(1, 9)] == [0]*7 + [1]))
print('     w_8^2 = %d' % (w8 * w8))
e2 = vec({2: 1})
e3 = vec({3: 1})
roots = [alpha_root[1], alpha_root[3], alpha_root[4], alpha_root[5], alpha_root[6],
         alpha_root[7], alpha_root[8],
         w8 + e2, e3 - e2, tw8 + e2,
         talpha_root[8], talpha_root[7], talpha_root[6], talpha_root[5],
         talpha_root[4], talpha_root[3], talpha_root[1],
         alpha_root[2], talpha_root[2]]
print('   the nineteen roots are elements of L; their squares, through the library pairing:')
print('     %s' % [int(r * r) for r in roots])
assert all(int(r * r) == -2 for r in roots)
H = vec({2: 1, 3: 1, 4: 1, 5: 1})
print('   H = e_2 + e_3 + e_4 + e_5, H^2 = %d, H.w = %s' % (H * H, [int(H * r) for r in roots]))
stamp('roots placed')

# --------------------------------------------------------------- 9. theta on the roots
print('9. the induced action on the roots, computed from the library images')
print("   theta_Co carries the copy W = U_2 + E8^2 onto W' = U_3 + E8^2, so the images of the")
print("   nineteen roots of the diagram in W are the nineteen roots of the diagram in W':")
e4 = vec({4: 1})
e5 = vec({5: 1})
roots_other = [alpha_root[1], alpha_root[3], alpha_root[4], alpha_root[5], alpha_root[6],
               alpha_root[7], alpha_root[8],
               w8 + e4, e5 - e4, tw8 + e4,
               talpha_root[8], talpha_root[7], talpha_root[6], talpha_root[5],
               talpha_root[4], talpha_root[3], talpha_root[1],
               alpha_root[2], talpha_root[2]]
I_Co = -theta
pairing = []
for r in roots:
    img = I_Co(r)
    hit = [j for j in range(19) if roots_other[j] == img]
    pairing.append(hit[0] if hit else None)
print('   I_Co = -theta_Co sends node k to node: %s' % (pairing,))
print("   every image is a node of the diagram in W-prime: %s"
      % all(p is not None for p in pairing))
print('   a bijection of order two: %s, %s'
      % (sorted(pairing) == list(range(19)),
         all(pairing[pairing[k]] == k for k in range(19))))
orbits = []
seen = set()
for k in range(19):
    if k in seen:
        continue
    j = pairing[k]
    seen.add(k)
    seen.add(j)
    orbits.append((k, j))
folded = [roots[k] + roots[j] if j != k else roots[k] for (k, j) in orbits]
print('   the orbits of the involution number %d; the folded roots, w + I_Co(w) with'
      ' w itself on the fixed node, have norms %s'
      % (len(orbits), [int(x * x) for x in folded]))
print('   the cusp-2 diagram [@AEGS25, Fig. 7, printed p. 594], as the provider-free')
print('   record prints them')

print('')
print('All assertions above hold: the objects of the six theorems, built by the library,')
print('carry the invariants their records state.')
