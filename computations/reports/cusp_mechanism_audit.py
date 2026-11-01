"""The chapter's cusp mechanism, tested on T_2 with the maintained APIs.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/cusp_mechanism_audit.py

Two statements of 450-scattone.md are tested here.

(A) That cusp enumeration reduces to isotropic subgroups of A_{T_{2d}}.  At d = 1 the reduction
fails: A_{T_2} is Z/2, its single non-zero element has q = -1/4, which is not 0 in Q/2Z, so {0} is
the only isotropic subgroup -- one class -- while the Baily-Borel boundary of F_2 has four
1-cusps [@AET23, Sec. 3B].  What classifies the orbits is the quotient I^perp/I together with its
gluing to T_{2d}: the quotient is what the four labels name, and in the degree-four case nine
isometry classes in a single genus give nine orbits, so neither the genus nor the discriminant
form is the classifier.

(B) That the classifying space at a Type III (0-cusp) degeneration is a Type IV domain of
eta^perp/eta.  For a primitive isotropic *line* eta in T_2 that quotient has rank 19 and
signature (1,18), while a Type IV period domain is the one of a lattice of signature (2,n); the
Baily-Borel Type III stratum is a point [@AET23, Sec. 3B].  The plane case is printed next to it
for contrast: I^perp/I is negative definite of rank 17.

The three objects kept apart: the boundary point (or curve) itself, the lattice data carried by
the limiting mixed Hodge structure on the graded piece, and the toroidal data attached at the
cusp.  Only the second is a lattice here.
"""
from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T2_GRAM = block_diagonal_matrix(matrix(ZZ, [[-2]]), U, U, E8, E8)
T2 = Lattices(ZZ)([list(row) for row in T2_GRAM.rows()])
print('T_2: rank %s, determinant %s, signature %s'
      % (T2.module_rank(), T2.determinant(), T2.signature_pair()))

# (A) the discriminant group
A = T2.discriminant_group()
print('A_{T_2}: %s' % A)
print('elements: %d' % len(tuple(A.module_generators())))
# The quadratic value of the non-zero element, exactly: with G the Gram matrix, the dual basis is
# the set of columns of G^{-1}, and q of the class of w is (w, w)/2 in Q/2Z.
G = T2_GRAM
dual = G.inverse()
w = dual.column(0)
q_value = (w * G * w) / 2          # (w, w)/2, w given in the chosen basis
print('q on the non-zero element: %s (in Q/2Z)' % q_value)
assert q_value != 0, 'the non-zero element must not be isotropic for the audit to bite'
print('so {0} is the only isotropic subgroup of A_{T_2}, one class, while the Baily-Borel')
print('boundary of F_2 has four 1-cusps [@AET23, Sec. 3B]')

# (B) the line and the plane
line = T2.primitive_isotropic_subobject(T2.basis_vector(1))
line_quotient = line.isotropic_reduction()
print('eta a primitive isotropic line: eta^perp/eta rank %s, determinant %s, signature %s'
      % (line_quotient.module_rank(), line_quotient.determinant(), line_quotient.signature_pair()))
positive, negative = (int(x) for x in line_quotient.signature_pair())
assert (positive, negative) == (1, 18), (positive, negative)
print('   a Type IV domain needs signature (2,n); (1,18) is not one, and the Baily-Borel')
print('   Type III stratum at such a cusp is a point')

plane = T2.primitive_isotropic_subobject(T2.basis_vector(1), T2.basis_vector(3))
plane_quotient = plane.inclusion().isotropic_reduction()
print('I a primitive isotropic plane: I^perp/I rank %s, determinant %s, signature %s, negative'
      ' definite %s'
      % (plane_quotient.module_rank(), plane_quotient.determinant(),
         plane_quotient.signature_pair(), plane_quotient.is_negative_definite()))
print()
print('So the discriminant group of T_2 cannot index the four plane orbits, and the line quotient')
print('is not a Type IV object: the chapter states neither as a reduction any more.')
