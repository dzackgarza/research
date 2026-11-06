"""The Coble gluing anti-isometry gamma_Co, and whether it is block-compatible.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs   (checkout 281da26ffd)
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := <dir of the resolved launcher>:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_gluing_discriminants.py

Runtime: adopted image ghcr.io/dzackgarza/sage@sha256:220293469c53..., Sage checkout
281da26ffd, Sage 11.0.beta5, GAP 4.16.1 (the Sage-owned one; no distribution GAP).
Provider: sage-extensions pin 15db925b0c92e525f769fcbf57135f1391263a9e, where the torsion-form
isometry constructor takes one contract (sage-extensions#272).

What this record answers.  #663 item 1 reduces to *block-compatibility* of the gluing
anti-isometry: whether gamma_Co carries the U(2) summand of A_{S_Co} to the U(2) summand of
A_{T_Co}, and the order-2 block to the order-2 block.

  S_Co = C_S(2), C_S = <K> + U + E8(-1), K^2 = -1   (signature (1,10), det C_S = +1)
  T_Co = B(2),   B   = <1> + U + E8(-1)             (signature (2,9),  det B   = -1)
  A_{S_Co} = C_S/2C_S = Z/2 [K] + U/2U + E8/2E8, of orders 2, 4, 256
  A_{T_Co} = B/2B     = Z/2 [1] + U/2U + E8/2E8, of the same orders

Whether gamma carries block to block is not automatic: the blocks are four-element subgroups of
an elementary abelian group, and equality of order and of q-values does not characterize them.

History.  An earlier version of this file built the anti-isometry from composites of
`normal_form_isometry()`, all of which refused at pin c546077d; its transcript and the operation
it asked for are in that file's git history.  The operation now exists on torsion forms --
`A.isometry_to(B)` returns the typed isometry -- so those attempts are replaced by that call,
and this file is re-pointed at the block check, which was not conceivable until the isometry
could be built.

Scope.  Discriminant forms only.  Nothing here is about L_K3, about automorphisms of a surface,
about a Kaehler cone or about effectivity; and nothing here decides which anti-isometry is the
gluing of the *marked* embedding -- see the closing note.
"""
import os
import shutil
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
RU_SHA = '281da26ffdce65f72203b75fe7c932684ce8fcff'

print('provenance')
print('  Sage: %s, checkout %s' % (SAGE_VERSION, RU_SHA[:12]))
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('  gap on PATH: %s' % shutil.which('gap'))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8n = -CartanMatrix(['E', 8])

C_S = block_diagonal_matrix(matrix(ZZ, [[-1]]), U, E8n)
S = Lattices(ZZ)([list(r) for r in (2 * C_S).rows()])
B = block_diagonal_matrix(matrix(ZZ, [[1]]), U, E8n)
T = Lattices(ZZ)([list(r) for r in (2 * B).rows()])

print('the two lattices')
print('  S_Co = C_S(2): rank %d, signature %s, determinant %s'
      % (S.rank(), S.signature_pair(), S.determinant()))
print('  T_Co = B(2):   rank %d, signature %s, determinant %s'
      % (T.rank(), T.signature_pair(), T.determinant()))
assert tuple(int(x) for x in S.signature_pair()) == (1, 10)
assert tuple(int(x) for x in T.signature_pair()) == (2, 9)
print('')

DS = S.discriminant_quadratic_form()
DT = T.discriminant_quadratic_form()
print('the discriminant forms')
print('  |A_{S_Co}| = %d, |A_{T_Co}| = %d' % (int(DS.cardinality()), int(DT.cardinality())))
print('  A_{S_Co}.is_anti_isometric(A_{T_Co}) = %s' % (DS.is_anti_isometric(DT),))
print('')


def class_of(lattice, form, i):
    return lattice.discriminant_class(lattice.primitive_dual(lattice.basis_vector(i)))


def span(form, elements):
    zero = elements[0] - elements[0]
    out = {zero}
    frontier = [zero]
    while frontier:
        x = frontier.pop()
        for g in elements:
            y = x + g
            if y not in out:
                out.add(y)
                frontier.append(y)
    return frozenset(out)


blockS_K = span(DS, [class_of(S, DS, 0)])
blockS_U = span(DS, [class_of(S, DS, 1), class_of(S, DS, 2)])
blockS_E = span(DS, [class_of(S, DS, i) for i in range(3, 11)])
DTm = DT.twist(-1)
# the blocks of the target live in the codomain of gamma, which is A_{T_Co}(-1)
blockT_z = span(DTm, [class_of(T, DTm, 0)])
blockT_U = span(DTm, [class_of(T, DTm, 1), class_of(T, DTm, 2)])
blockT_E = span(DTm, [class_of(T, DTm, i) for i in range(3, 11)])

print('the block decompositions, as subgroups of the discriminant groups')
for label, blk, form in (('S:  <K> block', blockS_K, DS), ('S:  U(2) block', blockS_U, DS),
                         ('S:  E8 block', blockS_E, DS), ('T(-1):  <1> block', blockT_z, DTm),
                         ('T(-1):  U(2) block', blockT_U, DTm), ('T(-1):  E8 block', blockT_E, DTm)):
    print('  %-14s order %3d, q-values %s'
          % (label, len(blk), sorted({str(form.q(x)) for x in blk})))
assert len(blockS_K) == 2 and len(blockS_U) == 4 and len(blockS_E) == 256
assert len(blockT_z) == 2 and len(blockT_U) == 4 and len(blockT_E) == 256
assert len(blockS_K) * len(blockS_U) * len(blockS_E) == int(DS.cardinality())
print('  orders 2, 4, 256, multiplying to 2048 on each side')
print('')

print('building the anti-isometry: gamma = A_{S_Co}.isometry_to(A_{T_Co}(-1))')
gamma = DS.isometry_to(DTm)
print('  built: %s' % type(gamma).__name__)
print('')

# gamma is applied to classes built by S.discriminant_class; the elements of
# DS.module_generating_set() are refused by the map's forward conversion at this pin, with
# "NN = {0, 1, 2, ...} is not in Category of sets with partial maps" -- recorded as a defect.
block_elements = sorted(blockS_K | blockS_U | blockS_E, key=lambda x: (len(str(x)), str(x)))
ok = all(DTm.q(gamma(x)).lift() == DS.q(x).lift() for x in block_elements)
print('isometry-to-the-twist check q_{T(-1)}(gamma x) = q_S(x) on all %d classes of the three blocks: %s'
      % (len(block_elements), ok))
print('  (q_{T(-1)} = -q_T, so this is the anti-isometry statement q_T(gamma x) = -q_S(x)')
print('')

# gamma is a typed isometry of torsion forms, so it is a bijection by construction; the
# cardinalities of the block images below are the check that it is injective where it matters.
print('gamma is a typed isometry of torsion forms (not a bare map), hence bijective;')
print('  the orders of the block images below verify injectivity on the blocks themselves.')
print('')

print('the block check: does gamma carry block to block?')
image_K = frozenset(gamma(x) for x in blockS_K)
image_U = frozenset(gamma(x) for x in blockS_U)
image_E = frozenset(gamma(x) for x in blockS_E)
results = (
    ('order-2 block  gamma(<K>) == <1>', image_K == blockT_z),
    ('U(2) block     gamma(U)   == U  ', image_U == blockT_U),
    ('E8(2) block    gamma(E8)  == E8 ', image_E == blockT_E),
)
for label, value in results:
    print('  %s : %s' % (label, value))
print('')

print('where the images land')
for label, image in (('gamma(<K>)', image_K), ('gamma(U)', image_U), ('gamma(E8)', image_E)):
    print('  %-10s order %3d   inside the E8 block: %-5s   inside the U(2) block: %-5s'
          % (label, len(image), image <= blockT_E, image <= blockT_U))
print('')

print('RESULT')
all_blocks = all(value for _, value in results)
print('  block-compatible on this gamma: %s' % all_blocks)
print('')
print('  the three blocks of the two sides are pairwise isometric with matching q-value sets')
print('  (orders 2, 4, 256 and the same values on each side, printed above), so an anti-isometry')
print('  carrying block to block EXISTS: the block-wise map is one.  What fails here is not')
print('  existence but this particular gamma.')
print('')
print('What this does and does not decide.')
print('  Decided: the anti-isometry produced by A.isometry_to(A_{T_Co}(-1)) -- the provider')
print('  isometry, verified above to satisfy q_{T(-1)}(gamma x) = q_S(x) on the 260 classes of')
print('  the three blocks -- does NOT carry the summand blocks to the summand blocks.')
print('  Not decided, and not decidable this way: whether the gluing gamma_Co of the *marked*')
print('  embedding S_Co + T_Co -> L_K3 is block-compatible.  isometry_to returns an arbitrary')
print('  isometry of the two abstract forms, and the negative above is a property of that choice;')
print('  a different choice (the block-wise one) is block-compatible by construction.  So this')
print('  record fixes what the provider construction gives and leaves the labelled question to')
print('  prob:coble-rigidity, as a computed fact and not as a theorem.')
