"""The chapter's cusp mechanism, tested on T_2 with the formed discriminant module.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/cusp_mechanism_audit.py

Two statements of 450-scattone.md are tested.

(A) That cusp enumeration reduces to isotropic subgroups of A_{T_{2d}}.  At d = 1 the reduction
fails.  The object is the formed finite module D = T_{2d}.discriminant_quadratic_form(), which is
the module A_L *together with* its quadratic form: D(x) coerces an element, and the form is
evaluated by D.q(x), with values in D.quadratic_value_module() --- QQ/2Z here, so the convention is
Nikulin's mod 2Z and nothing is hand-divided.  Isotropy is then a question for the same object,
asked through D.isotropic_elements() and its cardinality.  For T_2 the form is anisotropic, one
isotropic element, so the only isotropic subgroup is the zero one --- a single class --- while the
Baily-Borel boundary of F_2 has four 1-cusps [@AET23, Sec. 3B].

(B) That the classifying space at a Type III (0-cusp) degeneration is a Type IV domain of
eta^perp/eta.  For a primitive isotropic line eta in T_2 that quotient has rank 19 and signature
(1,18), while a Type IV period domain is the one of a lattice of signature (2,n); the Baily-Borel
Type III stratum is a point [@AET23, Sec. 3B], while the fan data over it is a separate and real
object living on that (1,18) lattice [@AET23, Sec. 3C, 4A, 4C].  The plane case is printed for
contrast: I^perp/I is negative definite of rank 17.
"""
from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T2 = Lattices(ZZ)([list(row) for row in
                   block_diagonal_matrix(matrix(ZZ, [[-2]]), U, U, E8, E8).rows()])
print('T_2: rank %s, determinant %s, signature %s'
      % (T2.module_rank(), T2.determinant(), T2.signature_pair()))

# (A) the formed discriminant module: elements, values, isotropy
D = T2.discriminant_quadratic_form()
values = D.quadratic_value_module()
zero = values.zero()
print('D = A_{T_2} with its quadratic form: %s' % D)
print('the values live in %s' % values)
print('cardinality of A_{T_2}: %s' % D.cardinality())
for element in D.elements():
    print('   %s -> q = %s%s' % (element, D.q(element), '   (isotropic)' if D.q(element) == zero else ''))
isotropic_elements = D.isotropic_elements()
print('isotropic elements: %s' % isotropic_elements.cardinality())
print('the form is anisotropic: %s' % D.is_anisotropic())
assert D.cardinality() == 2
assert D.isotropic_elements().cardinality() == 1
assert D.is_anisotropic()
nonzero = [element for element in D.elements() if element != D.zero()]
assert len(nonzero) == 1 and D.q(nonzero[0]) != zero
print('so the only isotropic subgroup of A_{T_2} is {0}, one class, against the four 1-cusps')
print('of F_2 [@AET23, Sec. 3B]')

# (B) the line and the plane
line = T2.primitive_isotropic_subobject(T2.basis_vector(1))
line_quotient = line.isotropic_reduction()
print('eta a primitive isotropic line: eta^perp/eta rank %s, determinant %s, signature %s'
      % (line_quotient.module_rank(), line_quotient.determinant(), line_quotient.signature_pair()))
assert tuple(int(x) for x in line_quotient.signature_pair()) == (1, 18)
print('   (1,18) is not a Type IV signature; the Baily-Borel Type III stratum is a point, and')
print('   the fan that AET put at that point lives on this lattice')

plane = T2.primitive_isotropic_subobject(T2.basis_vector(1), T2.basis_vector(3))
plane_quotient = plane.inclusion().isotropic_reduction()
print('I a primitive isotropic plane: I^perp/I rank %s, determinant %s, signature %s, negative'
      ' definite %s'
      % (plane_quotient.module_rank(), plane_quotient.determinant(),
         plane_quotient.signature_pair(), plane_quotient.is_negative_definite()))
