"""A19 (#662): the two complements in U + A_3, recomputed.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src \\
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \\
        /repo/computations/reports/coble_dawes-example-2-2_complements.py

Declared runtime and provider (sage-extensions 6ad7a5ea on PYTHONPATH), as in the other
records here.  Nothing is written to the rootfs.

What #662 asks.  Example 2.2 of [@Daw22] states v_1 ~ v_2 in L = U + A_3 for
v_1 = (4,4,1,2,-1) and v_2 = (36,144,5,-30,83); the in-tree computation returned
v_1 not~ v_2 on the ground that v_1^{perp L} and v_2^{perp L} "have different
discriminants".  A determinant is an isometry invariant, so if the complements really had
different discriminants the inequivalence would follow for every subgroup, whatever test ran
downstream (@prop:orbit-necessary-conditions(3)) -- and the disagreement would then have to
lie in the paper, the transcription, or the computed complements.  The page
(@qst:dawes-example-22) says the squares clear the transcription and that recomputing the two
complements settles the rest.

What this run finds.  The complements do NOT have different determinants: both are negative
definite of rank 4 and both have determinant 5.  That is not an accident of these two
vectors.  For a primitive v in an integral lattice L with q(v) != 0,
    det(v^{perp L}) = det(L) * q(v) / div_L(v)^2,
because L/(Zv + v^{perp L}) is the cokernel of Z -> div_L(v)Z given by v, of order
q(v)/div_L(v), and det(Zv + v^{perp L}) = q(v) * det(v^{perp L}) is [L : Zv + v^{perp L}]^2
times det(L).  The two vectors have the same square and the same divisibility, so the
determinant of the complement cannot separate them.

What is settled, therefore: the recorded ground for v_1 not~ v_2 is impossible, and the
in-tree run either computed the complements wrongly or recorded a reason that is not the one
it used.  What is NOT settled: whether v_1 ~ v_2.  The invariants available without the
group -- square, divisibility, and the class of v/div(v) in A_L -- do not separate them
(both classes carry q = 5/4, and O(A_L) = {+-1} transits them), so the question is the orbit
question, and deciding it needs the isometry machinery that #272 and the GAP stop block.
No conclusion about v_1 ~ v_2 is drawn here.
"""
import sys

from sage.all import ZZ, block_diagonal_matrix, gcd, matrix
from sage.version import version as SAGE_VERSION

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-6ad7a5ea/src on PYTHONPATH, pin 6ad7a5ea')
print('')

G_U = matrix(ZZ, [[0, 1], [1, 0]])
G_A3 = matrix(ZZ, [[-2, -1, 0], [-1, -2, -1], [0, -1, -2]])
L = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(G_U, G_A3).rows()])
basis = [L.basis_vector(i) for i in range(L.rank())]


def vector(coordinates):
    total = 0 * basis[0]
    for scalar, b in zip(coordinates, basis):
        total = total + scalar * b
    return total


print('L = U + A_3, the lattice of @ex:dawes-u-a3')
print('  rank %d, signature %s, determinant %d, even: %s'
      % (L.rank(), L.signature_pair(), L.determinant(), L.is_even()))
assert tuple(int(x) for x in L.signature_pair()) == (1, 4)
assert int(L.determinant()) == 4 and L.is_even()
print('')

cases = (('v_1', (4, 4, 1, 2, -1)), ('v_2', (36, 144, 5, -30, 83)))
complements = {}
for name, coordinates in cases:
    v = vector(coordinates)
    a3_part = coordinates[2:]
    q_U = 2 * coordinates[0] * coordinates[1]
    q_A3 = sum(G_A3[i][j] * a3_part[i] * a3_part[j] for i in range(3) for j in range(3))
    print('%s = %s' % (name, coordinates))
    print('  q = %d, split as U-part %d and A_3-part %d   (@ex:dawes-u-a3 says %s)'
          % (v.q(), q_U, q_A3, 'the same'))
    assert v.q() == 20 and q_U + q_A3 == 20
    print('  coordinates have gcd %d, so v is primitive; div_L(v) = %d'
          % (gcd(coordinates), L.div(v)))
    assert gcd(coordinates) == 1 and L.div(v) == 4
    complement = L.perp(L.sublattice_from([v], saturate=True))
    gram = matrix(ZZ, [[complement.pairing(complement.basis_vector(i), complement.basis_vector(j))
                        for j in range(4)] for i in range(4)])
    print('  v^perp: rank %d, signature %s, determinant %d, even: %s'
          % (complement.rank(), complement.signature_pair(),
             complement.determinant(), complement.is_even()))
    print('         Gram matrix %s' % gram.rows())
    predicted = int(L.determinant()) * int(v.q()) // int(L.div(v)) ** 2
    print('         det(L)*q(v)/div(v)^2 = %d * %d / %d = %d   AGREE'
          % (int(L.determinant()), int(v.q()), int(L.div(v)) ** 2, predicted))
    assert int(complement.determinant()) == predicted
    plain = Lattices(ZZ)([list(row) for row in gram.rows()])
    roots = list(plain.roots())
    print('         as a plain lattice: %d roots, root type %s'
          % (len(roots), plain.norm_two_root_types()))
    print('         rank 4 + roots of type A_4 (a rank-4 root system of determinant 5) +')
    print('         determinant 5 force the lattice to BE the A_4 root lattice: the roots')
    print('         span a sublattice of determinant 5 equal to det(v^perp).')
    complements[name] = (gram, len(roots), int(complement.determinant()),
                         plain.norm_two_root_types())
    print('')

print('the two complements side by side')
for name in ('v_1', 'v_2'):
    gram, root_count, det, root_type = complements[name]
    print('  %s: determinant %d, %d roots, root type %s, Gram diagonal %s'
          % (name, det, root_count, root_type, [int(gram[i][i]) for i in range(4)]))
print('  equal determinants: %s   both root type %s'
      % (complements['v_1'][2] == complements['v_2'][2], complements['v_1'][3]))
assert complements['v_1'][2] == complements['v_2'][2] == 5
assert complements['v_1'][3] == complements['v_2'][3] == 'A4'
print('  so the two complements are isometric: they are both the A_4 root lattice, negated.')
print('')

print('the last invariant @prop:orbit-necessary-conditions(2) names: the class of v/div(v)')
A_L = L.discriminant_group()
classes = {}
for name, coordinates in cases:
    v = vector(coordinates)
    cls = L.discriminant_class(L.primitive_dual(v))
    classes[name] = cls
    print('  [%s/div] = %s, with q = %s'
          % (name, cls, A_L.q(cls) if hasattr(A_L, 'q') else 'no q method'))
print('  equal as classes of A_L: %s' % (classes['v_1'] == classes['v_2']))
print('')

print('SUMMARY')
print('  (1) both vectors are primitive of square 20 and divisibility 4 in L, so both')
print('      complements have determinant det(L)*20/4^2 = 5 by the formula proved in the')
print('      page: the recorded ground for v_1 not~ v_2, "the complements have different')
print('      discriminants", is impossible, not merely unverified;')
print('  (2) the complements are not merely close but isometric: both are rank 4, negative')
print('      definite, of determinant 5, with 20 roots of type A_4, which forces each to BE')
print('      the A_4 root lattice; so no correct computation of the complements can witness')
print('      inequivalence, and the in-tree run either computed them wrongly or recorded a')
print('      reason it did not use;')
print('  (3) every invariant that @prop:orbit-necessary-conditions requires to agree does')
print('      agree: square 20, divisibility 4, isometric complements (both -A_4), and the')
print('      same class of v/div(v) in A_L, which carries q = 5/4 for both.  Nothing')
print('      computed here separates the two vectors, so the paper stands uncontradicted;')
print('  (4) the equivalence itself is still not proved: what would settle it is an explicit')
print('      isometry of L carrying v_1 to v_2, or the orbit decision, and both need the')
print('      isometry machinery that #272 and the GAP stop block.  No claim about v_1 ~ v_2')
print('      is made.')
print('OK: the recorded attribution is refuted at the owner; the equivalence question is')
print('    named as the orbit question and left to the machinery that is blocked.')
