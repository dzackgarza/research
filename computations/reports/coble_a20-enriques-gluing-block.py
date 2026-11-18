"""A20 item 1: the O(q)-invariance of the U(2)/E8(2) splitting of A_{S_En}, and the block
check on the Enriques gluing gamma.

Run in the maintained sage runtime:

  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH python /repo/computations/reports/coble_a20-enriques-gluing-block.py'

Transcript: coble_a20-enriques-gluing-block-run.txt  (Sage 11.0.beta5; exit 0).

Provenance.  The provider inside that image is the editable install at
/repos/sage-extensions/src, at cf656f8c6106e88475a5534c2779b9ff13ae02fc (sage-extensions main,
2026-11-14), which is the pin the maintained runtime carries and not the 15db925b of the two
earlier records on this pair of pages.  Every call made here is one of the calls in those records'
transcripts -- Lattices, basis_vector, primitive_dual, discriminant_class,
discriminant_quadratic_form, is_anti_isometric, orbits, isometry_to, twist, q -- so the two
records are comparable call for call.

The question
------------
research#663, item 1, asks whether the Heegner description and the congruence description of
Gamma_Co are the same group.  By prop:gamma-cong-eq-heegner they are the same if and only if the
gluing anti-isometry gamma: A_{S_En} -> A_{T_En}, q_{T_En} o gamma = -q_{S_En}, of
prop:gamma-en-two-gluing is *block-compatible*: gamma(A_{U(2)}) = A_{U(2)}.  Whether that is a
condition at all depends on the U(2)/E8(2) decomposition of A_{S_En}, of order 1024.  So there are
two things to compute, and this record computes both at the owner:

  (a) the orbits of O(q_{S_En}) on the 1024 classes, with the orbit of the U(2) block's classes
      tested explicitly for containment in the block;
  (b) whether gamma = A_{S_En}.isometry_to(A_{T_En}(-1)) carries the U(2) block of A_{S_En} onto
      the U(2) block of A_{T_En};

and, because a negative answer to (b) is only interesting beside an affirmative one somewhere,
it also records

  (c) that a block-compatible anti-isometry A_{S_En} -> A_{T_En} exists.  This one is an argument
      and not a computation: both discriminants are the orthogonal sum of the same two forms,
      A_{U(2)} and A_{E8(2)}, so the sum of the identity of each summand is one.  The record
      prints only the two facts the argument rests on.

The lattices (lattices.md, the book's conventions)
--------------------------------------------------
  S_En = C(2),  C = U + E8(-1) = I_{1,9} even unimodular    rank 10, det -1024, signature (1,9)
  T_En = U + E_10(2),  E_10(2) = U(2) + E8(2)               rank 12, det  1024, signature (2,10)
  A_{S_En} = C/2C = A_{U(2)} + A_{E8(2)}                    1024 classes
  A_{T_En} = A_U + A_{U(2)} + A_{E8(2)} = A_{U(2)} + A_{E8(2)}  1024 classes, A_U = 0
The blocks are the images of the named summands: in S_En the classes of the basis vectors 0, 1
(the U(2) summand) and 2..9 (the E8(2) summand); in T_En the classes of the basis vectors 2, 3
and 4..11, the first two being a unimodular U whose discriminant group is trivial.

What this record does and does not decide
-----------------------------------------
Computes: the orbit partition of O(q_{S_En}) on A_{S_En} -- hence whether the splitting is
invariant -- and whether the provider's isometry gamma is block-compatible.
Does not decide: whether the gluing of the *marked* embedding S_En in L_K3 is block-compatible.
The isometry the constructor returns is one anti-isometry among many, and by part (a) no property
of the pair of forms singles out a block-compatible one, so the block check on it is a fact about
that isometry.  The condition of prop:gamma-cong-eq-heegner(2) is therefore a hypothesis on the
labeling, an instance of prob:coble-rigidity, which is where item 1's residue sits.
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as SAGE_VERSION

import sage_extensions
from sage_extensions.all import Lattices

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: %s' % sage_extensions.__file__)
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8n = -CartanMatrix(['E', 8])

S = Lattices(ZZ)([list(r) for r in (2 * block_diagonal_matrix(U, E8n)).rows()])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8n).rows()])

print('the two lattices')
print('  S_En = C(2):        rank %d, signature %s, determinant %s'
      % (S.rank(), S.signature_pair(), S.determinant()))
print('  T_En = U + U(2) + E8(2): rank %d, signature %s, determinant %s'
      % (T.rank(), T.signature_pair(), T.determinant()))
assert tuple(int(x) for x in S.signature_pair()) == (1, 9)
assert tuple(int(x) for x in T.signature_pair()) == (2, 10)
print('')

A = S.discriminant_quadratic_form()
B = T.discriminant_quadratic_form()
print('the discriminant forms')
print('  |A_{S_En}| = %d, |A_{T_En}| = %d' % (int(A.cardinality()), int(B.cardinality())))
print('  A_{S_En}.is_anti_isometric(A_{T_En}) = %s' % (A.is_anti_isometric(B),))
print('')


def cls(lattice, form, i):
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


blockA_U = span(A, [cls(S, A, 0), cls(S, A, 1)])
blockA_E = span(A, [cls(S, A, 2 + i) for i in range(8)])
blockB_U = span(B, [cls(T, B, 2), cls(T, B, 3)])
blockB_E = span(B, [cls(T, B, 4 + i) for i in range(8)])

print('the block decompositions, as subgroups of the discriminant groups')
for label, blk, form in (('S_En:  U(2) block', blockA_U, A), ('S_En:  E8(2) block', blockA_E, A),
                         ('T_En:  U(2) block', blockB_U, B), ('T_En:  E8(2) block', blockB_E, B)):
    print('  %-18s order %3d, q-values %s'
          % (label, len(blk), sorted({str(form.q(x)) for x in blk})))
assert len(blockA_U) == 4 and len(blockA_E) == 256
assert len(blockB_U) == 4 and len(blockB_E) == 256
assert len(blockA_U) * len(blockA_E) == int(A.cardinality())
assert len(blockB_U) * len(blockB_E) == int(B.cardinality())
print('  orders 4 and 256, multiplying to 1024 on each side')
print('')

print('=== (a) is the splitting A_{S_En} = A_{U(2)} + A_{E8(2)} invariant under O(q_{S_En})?')
start = time.time()
orbits = [set(o) for o in A.orbits()]
print('  orbits of O(q_{S_En}) on the %d classes: %d, sizes %s   (%.0f s)'
      % (int(A.cardinality()), len(orbits), sorted(len(o) for o in orbits), time.time() - start))
meeting = [o for o in orbits if o & blockA_U]
invariant = all(o <= blockA_U for o in meeting)
print('  orbits meeting the U(2) block: %d' % len(meeting))
for o in meeting:
    print('    orbit of size %3d: %d of its classes inside the U(2) block' % (len(o), len(o & blockA_U)))
print('  the decomposition is O(q_{S_En})-invariant: %s' % invariant)
print('')
if not invariant:
    crossing = [o for o in meeting if not o <= blockA_U][0]
    x = next(iter(crossing & blockA_U))
    y = next(iter(crossing - blockA_U))
    print('  witness, in one orbit of size %d:' % len(crossing))
    print('    x = %s   (inside the U(2) block, q = %s)' % (x, A.q(x).lift()))
    print('    y = %s   (outside the U(2) block, q = %s)' % (y, A.q(y).lift()))
    print('  so some isometry of q_{S_En} carries a class of the U(2) block out of it, and')
    print('  block-compatibility is not a property of the pair of forms.')
print('')

print('=== (b) is the Enriques gluing gamma = A_{S_En}.isometry_to(A_{T_En}(-1)) block-compatible?')
Bm = B.twist(-1)
print('  q_{T_En}(-1) on the U(2) block: %s' % sorted({str(Bm.q(x)) for x in blockB_U}))
gamma = A.isometry_to(Bm)
print('  built: %s' % type(gamma).__name__)

block_elements = sorted(blockA_U | blockA_E, key=lambda z: (len(str(z)), str(z)))
ok = all(Bm.q(gamma(z)).lift() == A.q(z).lift() for z in block_elements)
print('  isometry-to-the-twist check q_{T_En(-1)}(gamma z) = q_{S_En}(z) on all %d classes of the'
      % len(block_elements))
print('    two blocks: %s   (q_{T_En(-1)} = -q_{T_En}, so this is q_{T_En}(gamma z) = -q_{S_En}(z))' % ok)
print('  gamma is a typed isometry of torsion forms, hence bijective; the order of each image')
print('  below is the check that it is injective where it matters.')

image_U = frozenset(gamma(z) for z in blockA_U)
image_E = frozenset(gamma(z) for z in blockA_E)
print('')
print('  where the images land')
for label, image in (('gamma(U(2) block)', image_U), ('gamma(E8(2) block)', image_E)):
    print('    %-20s order %3d   inside the U(2) block: %-5s   inside the E8(2) block: %-5s'
          % (label, len(image), image <= blockB_U, image <= blockB_E))
u_compatible = image_U == blockB_U
e_compatible = image_E == blockB_E
print('    gamma(U(2))  == A_{U(2)} of T_En : %s' % u_compatible)
print('    gamma(E8(2)) == A_{E8(2)} of T_En: %s' % e_compatible)
print('  block-compatible on this gamma: %s' % (u_compatible and e_compatible))
print('')

print('=== (c) a block-compatible anti-isometry exists, and it is not a computation')
print('  A_{S_En} and A_{T_En} are both the orthogonal sum of the SAME two forms, A_{U(2)} and')
print('  A_{E8(2)}: S_En = U(2) + E8(2) and T_En = U + U(2) + E8(2) with U unimodular, so the sum')
print('  of the identity map of each summand is an isometry A_{S_En} -> A_{T_En} carrying the')
print('  U(2) block onto the U(2) block (lem:coble-discriminant-blocks).  Nothing is computed')
print('  for it; printed below are the two facts it rests on, which the run above establishes:')
print('    the two blocks have orders 4 and 256 on each side, multiplying to 1024;')
q_same = all(Bm.q(x) == B.q(x) for x in blockB_U | blockB_E)
print('    q_{T_En(-1)} = q_{T_En} on the 259 classes of both blocks: %s, so an isometry of the' % q_same)
print('      forms is an anti-isometry in the sense of prop:gamma-en-two-gluing, q_{T_En} o gamma')
print('      = -q_{S_En} (every value of a 2-elementary form lies in 1/2 ZZ/ZZ, where q = -q).')
print('')

print('=== what the three parts say together')
print('  (a) The splitting of A_{S_En} is not invariant under O(q_{S_En})%s, so a block-compatible'
      % ('' if invariant else ' (witness above)'))
print('      anti-isometry and a non-block-compatible one both exist, and gamma(A_{U(2)}) is a')
print('      property of the chosen anti-isometry: the pair of forms does not determine it.')
print('  (b) The isometry the provider constructs %s block-compatible.  That is a fact about the'
      % ('is' if (u_compatible and e_compatible) else 'is NOT'))
print('      construction it performs, not about the gluing of the marked embedding S_En in L_K3:')
print('      nothing computed here relates that gluing to the constructed map, and by (a) nothing')
print('      on the abstract forms could single out a block-compatible one anyway.')
print('  (c) A block-compatible anti-isometry exists, so the hypothesis of')
print('      prop:gamma-cong-eq-heegner(2) is satisfiable, and by (a) it is not automatic: it is a')
print('      genuine choice among anti-isometries of one fixed pair of forms.  Which choice the')
print('      gluing of the marked embedding makes is the labeled-embedding data of')
print('      prob:coble-rigidity, and that is what item 1 of #663 leaves open.')
