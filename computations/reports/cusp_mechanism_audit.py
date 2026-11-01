"""The chapter's cusp mechanism, tested on T_2 with the owned discriminant module.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/cusp_mechanism_audit.py

Two statements of 450-scattone.md are tested.

(A) That cusp enumeration reduces to isotropic subgroups of A_{T_{2d}}.  At d = 1 the reduction
fails, and the count is made where the library keeps it: A is the owned discriminant module
A = (T_2)^*/T_2, its elements are enumerated by the module, and the quadratic form is the retained
one, discriminant_quadratic_form(), evaluated in its own codomain.  A has order 2 and its
non-zero element is not isotropic, so its only isotropic subgroup is {0} --- one class --- while
the Baily-Borel boundary of F_2 has four 1-cusps [@AET23, Sec. 3B].  No Gram entry is inverted or
halved here: an earlier version of this file counted module *generators* of the embedding as
elements and hand-divided a Gram value, and it is retired.

(B) That the classifying space at a Type III (0-cusp) degeneration is a Type IV domain of
eta^perp/eta.  For a primitive isotropic line eta in T_2 that quotient has rank 19 and signature
(1,18), while a Type IV period domain is the one of a lattice of signature (2,n); the Baily-Borel
Type III stratum is a point [@AET23, Sec. 3B].  The fan data at that point is a separate and real
object: [@AET23, Sec. 3C] puts a fan on the rational closure of the positive cone of exactly this
(1,18) lattice, and for the unique 0-cusp of F_2 constructs it as the Coxeter fan [@AET23, Sec. 4A,
4C].  The plane case is printed for contrast: I^perp/I is negative definite of rank 17.
"""
from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T2 = Lattices(ZZ)([list(row) for row in
                   block_diagonal_matrix(matrix(ZZ, [[-2]]), U, U, E8, E8).rows()])
print('T_2: rank %s, determinant %s, signature %s'
      % (T2.module_rank(), T2.determinant(), T2.signature_pair()))

# (A) the discriminant module, its elements, and the retained quadratic form
A = T2.discriminant_module()
print('A_{T_2} = (T_2)^*/T_2 : %s' % A)
elements = tuple(A.elements())
print('A has %d elements' % len(elements))
q_A = T2.discriminant_quadratic_form()
values = [q_A(element) for element in elements]
zero = q_A(elements[0])
print('the quadratic form takes values in %s' % values[0].parent())
for element, value in zip(elements, values):
    print('   %s -> %s%s' % (element, value, '   (isotropic)' if value == zero else ''))
isotropic = [element for element, value in zip(elements, values) if value == zero]
print('isotropic elements: %d of %d, so the isotropic subgroups number one'
      % (len(isotropic), len(elements)))
assert len(elements) == 2 and len(isotropic) == 1
print('one class from the discriminant group, against four 1-cusps of F_2 [@AET23, Sec. 3B]')

# (B) the line and the plane
line = T2.primitive_isotropic_subobject(T2.basis_vector(1))
line_quotient = line.isotropic_reduction()
print('eta a primitive isotropic line: eta^perp/eta rank %s, determinant %s, signature %s'
      % (line_quotient.module_rank(), line_quotient.determinant(), line_quotient.signature_pair()))
assert tuple(int(x) for x in line_quotient.signature_pair()) == (1, 18)
print('   (1,18) is not a Type IV signature, and the Baily-Borel Type III stratum is a point;')
print('   the fan that AET put at that point lives on the rational closure of this cone')

plane = T2.primitive_isotropic_subobject(T2.basis_vector(1), T2.basis_vector(3))
plane_quotient = plane.inclusion().isotropic_reduction()
print('I a primitive isotropic plane: I^perp/I rank %s, determinant %s, signature %s, negative'
      ' definite %s'
      % (plane_quotient.module_rank(), plane_quotient.determinant(),
         plane_quotient.signature_pair(), plane_quotient.is_negative_definite()))
