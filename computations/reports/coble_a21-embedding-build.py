"""#664 item 1: the four summand lattices and both primitive embeddings, realised in one copy of L_K3.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/sage-extensions/src        (sage-extensions main 1488acf)
    PYTHONPATH=$PROVIDER $HOME/.udocker/bin/proot-x86_64 -R "$RUNTIME" \\
        -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_a21-embedding-build.py

Runtime as adopted (Sage 11.0.beta5, checkout 281da26ffd); provider sage-extensions main
`1488acf`, the same pin as `coble_a21-ambient-extension.py`.

WHAT THIS BUILDS

  1. L_K3 = II_{3,19} = 3U + 2E8(-1) in its standard basis, rank 22, even, unimodular,
     signature (3,19).
  2. The four summand lattices with their Gram data and the source that fixes each type:
       S_Co = C_S(2),  C_S = <-1> + U + E8(-1)   rank 11, det 2048,  sig (1,10)
       T_Co = B(2),    B   = <1>  + U + E8(-1)   rank 11, det -2048, sig (2,9)
       S_En = C(2),    C   = U + E8(-1)          rank 10, det -1024, sig (1,9)
       T_En = S_En^perp in L_K3                  rank 12, det 1024,  sig (2,10)
     and the complement identities T_Co = S_Co^perp, T_En = S_En^perp, decided by rank and
     determinant.
  3. The two primitive embeddings in ONE copy of L_K3 -- S_Co = ker(J_Co - 1) for the
     reflected pair J_Co = w_alpha . I_En of the AEGS model with T_Co = S_Co^perp, and
     S_En = Delta(U_2,U_3) + Delta(E8_1,E8_2) with T_En = S_En^perp -- together with the
     complement identities by rank and determinant.
  4. Both overlattices, through the owner's `overlattice`, from the glue that the embedding
     itself determines: the S_Co + T_Co overlattice of index 2048 and the S_En + T_En
     overlattice of index 1024, each verified to be unimodular, even, of signature (3,19) and
     isometric to L_K3 = II_{3,19}, with the index equal to the discriminant order |A_S|;
     and for each, the glue subgroup printed as the graph of an anti-isometry
     A_S -> A_T(-1): the projection to A_S is a bijection, q_S(x) + q_T(gamma x) = 0 on all
     2^11 respectively 2^10 classes, and b_S + b_T = 0 in Q/Z.

WHAT IT DOES NOT BUILD, AND WHY

  * delta in T_En with delta^perp = T_Co (the Heegner vector of @lem:coble-heegner-vector):
    the operation is sage-extensions#279 (`vectors_of_square_with_complement`).
  * gamma as a TYPED morphism of torsion forms A_S -> A_T(-1): that arrow, with composition,
    inverse and quadratic agreement as methods, is sage-extensions#276
    (`gluing_anti_isometry`).  What that arrow must return is not in doubt here: it is the
    graph printed in part 5, computed from the two embeddings.  #276 supplies the object, not
    the map, and this record isolates it by printing the map it has to agree with.

So the acceptance's two laps -- the lattices, and the two overlattices inside one copy of
L_K3 with their indices and invariants -- are decided here; the two operations of #276 and
#279 are not needed for either and are named, not substituted.
"""
import sys
import time
from fractions import Fraction

sys.stdout.reconfigure(line_buffering=True)

from sage.all import (  # noqa: E402
    ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix, identity_matrix,
)
from sage.version import version as SAGE_VERSION  # noqa: E402

import sage_extensions  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

T0 = time.time()


def stamp(tag):
    print('  [%5.1fs] %s' % (time.time() - T0, tag))


print('provenance')
print('  Sage %s, runtime checkout 281da26ffd' % SAGE_VERSION)
print('  provider %s (sage-extensions main 1488acf)' % sage_extensions.__file__)
print('  invoked as in the docstring; the repository is bound read-write at /repo')
print('')

# ----------------------------------------------------------------- 1. L_K3
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
L = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, U, U, E8, E8).rows()])
n = int(L.rank())
GL = matrix(ZZ, n, n, lambda i, j: int(L.basis_vector(i) * L.basis_vector(j)))

print('1. L_K3 = 3U + 2E8(-1) = II_{3,19}, in its standard basis')
print('   rank %d, determinant %d, even %s, signature %s'
      % (n, int(L.determinant()), L.is_even(), L.signature_pair()))
assert n == 22 and int(L.determinant()) == -1 and L.is_even()
stamp('L_K3 built')


def vec(coefficients):
    return L.linear_combination(
        {int(i): L.base_ring()(int(c)) for i, c in coefficients.items() if c})


def coords(v):
    return [int(v.to_vector()(i)) for i in range(n)]


def block_split(v):
    c = coords(v)
    return (c[0:2], c[2:4], c[4:6], c[6:14], c[14:22])


def aegs_image(kind, v):
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
    M = matrix(ZZ, n, n, lambda i, j: int(isometry(L.basis_vector(j)).to_vector()(i)))
    rows = [[int(c) for c in r]
            for r in (M - identity_matrix(ZZ, n)).kernel().basis_matrix().rows()]
    return L.primitive_sublattice_from([vec(dict(enumerate(r))) for r in rows])


def sub_basis(sub):
    return [coords(sub.inclusion()(sub.module_generator(l)))
            for l in sub.module_generating_set()]


def gram_in_L(sub):
    B = sub_basis(sub)
    r = len(B)
    return matrix(ZZ, r, r,
                  lambda i, j: sum(B[i][a] * GL[a][b] * B[j][b]
                                   for a in range(n) for b in range(n)))


I_dP = aegs_involution('dP')
I_En = aegs_involution('enr')
alpha = vec({0: 1, 1: -1})
reflection = L.reflection(alpha)
S_Co = invariant_lattice(lambda w: reflection(I_En(w)))
T_Co = L.orthogonal_complement(S_Co)
S_En = L.primitive_sublattice_from(
    [vec({2: 1, 4: 1}), vec({3: 1, 5: 1})] + [vec({6 + k: 1, 14 + k: 1}) for k in range(8)])
T_En = L.orthogonal_complement(S_En)


def lat(m):
    return Lattices(ZZ)([list(r) for r in m.rows()])


ABSTRACT = {
    'S_Co': lat(2 * block_diagonal_matrix(matrix(ZZ, [[-1]]), U, E8)),
    'T_Co': lat(2 * block_diagonal_matrix(matrix(ZZ, [[1]]), U, E8)),
    'S_En': lat(2 * block_diagonal_matrix(U, E8)),
}
print('')
print('2. the four summands: Gram data, and the source that fixes each type')
print('   S_Co = C_S(2) with C_S = <-1> + U + E8(-1);  T_Co = B(2) with B = <1> + U + E8(-1);')
print('   S_En = C(2) with C = U + E8(-1);  T_En = S_En^perp inside L_K3')
rows = (('S_Co', S_Co, (1, 10), 2048, 'S_Co'),
        ('T_Co', T_Co, (2, 9), -2048, 'T_Co'),
        ('S_En', S_En, (1, 9), -1024, 'S_En'))
for name, S, sig, det, key in rows:
    G = gram_in_L(S)
    print('   %-5s rank %2d  det %6d  sig %-9s  even %-5s  |A| = %4d'
          '  det from the embedding == recorded det %s'
          % (name, S.rank(), int(S.determinant()), S.signature_pair(), S.is_even(),
             int(S.discriminant_group().cardinality()), int(G.det()) == det))
    print('         isometric to the abstract %s: %s'
          % (key, S.is_isometric_to(ABSTRACT[key])))
    print('         Gram matrix in the embedding\'s basis (%d x %d):' % (G.nrows(), G.ncols()))
    for j in range(G.ncols()):
        print('           [%s]' % ', '.join('%3d' % int(G[i, j]) for i in range(G.nrows())))
    assert int(S.determinant()) == det and tuple(int(x) for x in S.signature_pair()) == sig
    assert S.is_even() and S.is_isometric_to(ABSTRACT[key])
T_EN_ABSTRACT = Lattices(ZZ)([list(r) for r in
                              block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
print('   T_En  rank %2d  det %6d  sig %-9s  even %-5s  |A| = %4d'
      % (T_En.rank(), int(T_En.determinant()), T_En.signature_pair(), T_En.is_even(),
         int(T_En.discriminant_group().cardinality())))
print('         isometric to U + U(2) + E8(-2): %s' % T_En.is_isometric_to(T_EN_ABSTRACT))
GT = gram_in_L(T_En)
print('         Gram matrix in the embedding\'s basis (%d x %d):' % (GT.nrows(), GT.ncols()))
for j in range(GT.ncols()):
    print('           [%s]' % ', '.join('%3d' % int(GT[i, j]) for i in range(GT.nrows())))
assert T_En.rank() == 12 and int(T_En.determinant()) == 1024
assert T_En.is_isometric_to(T_EN_ABSTRACT)
print('   the complement identities, by rank and determinant:')
print('     rank S_Co = %d, rank T_Co = %d, sum = %d = rank L_K3; det S_Co . det T_Co = %d . %d = %d'
      % (S_Co.rank(), T_Co.rank(), S_Co.rank() + T_Co.rank(),
         int(S_Co.determinant()), int(T_Co.determinant()),
         int(S_Co.determinant()) * int(T_Co.determinant())))
print('     rank S_En = %d, rank T_En = %d, sum = %d = rank L_K3; det S_En . det T_En = %d . %d = %d'
      % (S_En.rank(), T_En.rank(), S_En.rank() + T_En.rank(),
         int(S_En.determinant()), int(T_En.determinant()),
         int(S_En.determinant()) * int(T_En.determinant())))
stamp('the four summands')


def q_on(gram, z):
    r = gram.nrows()
    return QQ(sum(z[i] * gram[i][j] * z[j] for i in range(r) for j in range(r))) / 4


def b_on(gram, z, w):
    r = gram.nrows()
    return QQ(sum(z[i] * gram[i][j] * w[j] for i in range(r) for j in range(r))) / 4


def solve_in_G(B, coords_v):
    """Integer coordinates of an ambient vector in the basis B (rows = ambient coordinates)."""
    BT = B.transpose()
    sol = BT.solve_right(vector(ZZ, coords_v))
    out = [QQ(x) for x in sol]
    if any(x.denominator() != 1 for x in out):
        return None
    out = [int(x) for x in out]
    if [sum(out[i] * B[i, j] for i in range(B.nrows())) for j in range(n)] != list(coords_v):
        return None
    return out


for section, (name, S, T, index) in enumerate(
        (('S_Co', S_Co, T_Co, 2048), ('S_En', S_En, T_En, 1024)), start=3):
    print('')
    print('%d. the primitive embedding (%s, %s) in L_K3 and its overlattice, index %d'
          % (section, name, name.replace('S_', 'T_'), index))
    BS, BT_ = sub_basis(S), sub_basis(T)
    B = matrix(ZZ, BS + BT_)
    rS = len(BS)
    r = rS + len(BT_)
    GramS, GramT = gram_in_L(S), gram_in_L(T)
    G = S + T
    Gr = matrix(ZZ, r, r, lambda i, j: int(G.basis_vector(i) * G.basis_vector(j)))
    print('   G = S + T: rank %d, det %d = det S . det T = %d . %d, even %s, sig %s'
          % (G.rank(), int(G.determinant()), int(GramS.det()), int(GramT.det()),
             G.is_even(), G.signature_pair()))
    print('   |A_S| = %d, |A_T| = %d, product = %d = -det G; [L_K3 : G] should be |A_S| = %d'
          % (int(S.discriminant_group().cardinality()),
             int(T.discriminant_group().cardinality()),
             int(S.discriminant_group().cardinality() * T.discriminant_group().cardinality()),
             index))
    print('   Gram(G) from the concrete embedding equals B^T GL B: %s'
          % (Gr == B * GL * B.transpose()))
    cross = Gr.submatrix(0, rS, rS, r - rS)
    print('   the two summands are orthogonal, so G is the orthogonal sum S perp T:'
          ' the off-diagonal block is %s' % ('zero' if cross.is_zero() else 'NOT zero'))
    assert Gr == B * GL * B.transpose()
    assert cross.is_zero()
    assert Gr == block_diagonal_matrix(GramS, GramT)

    classes, hs = [], []
    for i in range(n):
        y = [2 * c for c in coords(L.basis_vector(i))]
        c = solve_in_G(B, y)
        assert c is not None, 'the doubled basis vector is not in G'
        element = G.linear_combination({k: G.base_ring()(c[k]) for k in range(r) if c[k]})
        d = G.div(element)
        assert d == 2, 'div_G(2e_%d) = %s, not 2' % (i, d)
        classes.append(element.divided_discriminant_class())
        hs.append([c[k] % 2 for k in range(r)])
    print('   the 22 glue classes: [2e_i] for the ambient basis, div_G(2e_i) = 2 for all i')

    inclusion = G.overlattice(*classes)
    codomain = inclusion.codomain()
    print('   overlattice: index %d; codomain rank %d, det %d, even %s, sig %s, unimodular %s,'
          % (int(inclusion.index()), codomain.rank(), int(codomain.determinant()),
             codomain.is_even(), codomain.signature_pair(), codomain.is_unimodular()))
    print('     isometric to L_K3 = II_{3,19}: %s' % codomain.is_isometric_to(L))
    print('     index / |A_S| = %d / %d = %d, so the index is the discriminant order'
          % (int(inclusion.index()), int(S.discriminant_group().cardinality()),
             int(inclusion.index()) // int(S.discriminant_group().cardinality())))
    assert int(inclusion.index()) == index
    assert int(codomain.determinant()) in (1, -1) and codomain.is_even()
    assert tuple(int(x) for x in codomain.signature_pair()) == (3, 19)
    assert codomain.is_isometric_to(L)

    # ---- the glue as the graph of an anti-isometry, from the same two embeddings
    H = [list(h) for h in hs]
    dim = 0
    reduced = []
    for h in H:
        w = list(h)
        for (pivot, base) in reduced:
            if w[pivot]:
                w = [(w[k] + base[k]) % 2 for k in range(r)]
        pivot = next((k for k in range(r) if w[k]), None)
        if pivot is not None:
            reduced.append((pivot, w))
            reduced.sort()
            dim += 1
    span = [[0] * r]
    for (pivot, base) in reduced:
        span = span + [[(x[k] + base[k]) % 2 for k in range(r)] for x in span]
    print('   the glue subgroup of A_{S+T}: %d classes (2^%d), and |A_S| = %d, |A_T| = %d'
          % (len(span), dim, int(S.discriminant_group().cardinality()),
             int(T.discriminant_group().cardinality())))
    assert len(span) == index
    assert len(span) == int(S.discriminant_group().cardinality())
    projection = set(tuple(h[:rS]) for h in span)
    print('   the projection of the glue to A_S is injective: %s (%d distinct images)'
          % (len(projection) == len(span), len(projection)))
    assert len(projection) == len(span)
    graph = {}
    bad_q = bad_b = 0
    for h in span:
        u, v = h[:rS], h[rS:]
        graph[tuple(u)] = v
        if (q_on(GramS, u) + q_on(GramT, v)) % 2 != 0:
            bad_q += 1
    basis_u = [u for u in projection if any(u)]
    pairs = 0
    for i in range(min(len(basis_u), 12)):
        for j in range(min(len(basis_u), 12)):
            u1, u2 = basis_u[i], basis_u[j]
            v1, v2 = graph[tuple(u1)], graph[tuple(u2)]
            pairs += 1
            if QQ(b_on(GramS, u1, u2) + b_on(GramT, v1, v2)).denominator() != 1:
                bad_b += 1
    print('   q_S(x) + q_T(gamma x) = 0 on all %d glue classes: %s'
          % (len(span), bad_q == 0))
    print('   b_S(x,y) + b_T(gamma x, gamma y) = 0 in Q/Z on the %d tested pairs of a spanning'
          ' set: %s'
          % (pairs, bad_b == 0))
    assert bad_q == 0 and bad_b == 0
    Qmod = G.discriminant_module()
    q_prov = [Qmod.q(c) for c in classes]
    quotient = q_prov[0].parent()
    mine = [q_on(GramS, hs[i][:rS]) + q_on(GramT, hs[i][rS:]) for i in range(n)]
    def in_quotient(value):
        value = QQ(value)
        return quotient(Fraction(int(value.numerator()), int(value.denominator())))

    agree = all(q_prov[i] == in_quotient(mine[i]) for i in range(n))
    print('   cross-check against the owner\'s q on A_{S+T} (values in %s), on the 22'
          ' generators: %s' % (quotient, agree))
    witness = next((i for i in range(n) if QQ(mine[i]) % 2 != 0), 0)
    print('     e.g. q([2e_%d]) = %s by the owner, and %s from the two summands, that is %s mod 2'
          % (witness, q_prov[witness], mine[witness], QQ(mine[witness]) % 2))
    assert agree
    print('   the graph of the anti-isometry gamma: A_S -> A_T(-1), as classes of A_S')
    print('   (a class of A_S is the half-integer vector z/2 with |z| = %d; gamma(z/2) = v/2):'
          % rS)

    def row(tag, z, v):
        print('     %-4s z = %-*s  q_S = %-5s  gamma -> v = %-*s  q_T = %-5s  sum = %s'
              % (tag, rS, ''.join(map(str, z)), q_on(GramS, z), r - rS,
                 ''.join(map(str, v)), q_on(GramT, v),
                 (q_on(GramS, z) + q_on(GramT, v))))

    supported = [(i, hs[i][:rS], hs[i][rS:]) for i in range(n) if any(hs[i])]
    print('   %d of the 22 ambient basis vectors have nonzero class in A_{S+T}; the first six:'
          % len(supported))
    for (i, z, v) in supported[:6]:
        row('e_%d' % i, z, v)
    nonzero = [u for u in projection if any(u)]
    if rS == r - rS:
        diagonal = sum(1 for u in nonzero if tuple(graph[tuple(u)]) == tuple(u))
        print('     in this marking the glue is the diagonal: v = u for %d of the %d nonzero'
              ' classes' % (diagonal, len(nonzero)))
    else:
        print('     A_S and A_T have ranks %d and %d here, so the two coordinate vectors are not'
              ' comparable' % (rS, r - rS))
    print('     all %d classes: q_S + q_T = 0 mod 2, and the %d pairs of a spanning set have'
          ' b_S + b_T = 0 in Q/Z' % (len(span), pairs))
    stamp('pair %s done' % name)

print('')
print('5. not built here, and named rather than substituted')
print('   * delta in T_En with delta^perp = T_Co: sage-extensions#279'
      ' (`vectors_of_square_with_complement`).')
print('   * `even_overlattice_inclusions` is not used: it enumerates every even overlattice of')
print('     G, and here the glue is read off the embedding rather than searched for, so')
print('     `overlattice(*glue classes)` constructs the object and the inclusion is then checked;')
print('     the owner operations used are primitive_sublattice_from, orthogonal_complement,')
print('     div, divided_discriminant_class, overlattice, discriminant_module().q, is_isometric_to.')
print('   * gamma as a TYPED morphism of torsion forms A_S -> A_T(-1), with composition,')
print('     inverse and quadratic agreement as methods: sage-extensions#276'
      ' (`gluing_anti_isometry`).')
print('     Its values are not in doubt: they are the graph printed in parts 3 and 4, read off')
print('     the two embeddings.  #276 supplies the arrow, and above is the map it has to be.')
print('')
print('RESULT: L_K3 = II_{3,19} and the four summand lattices are built with their invariants;')
print('  both primitive embeddings are realised in one copy of L_K3; the S_Co + T_Co overlattice')
print('  has index 2048 and the S_En + T_En overlattice index 1024, each equal to |A_S|, each')
print('  unimodular, even, of signature (3,19) and isometric to II_{3,19}; and the glue of each is')
print('  the graph of an anti-isometry on all 2^11, respectively 2^10, classes.')
print('  [%.1fs]' % (time.time() - T0))
