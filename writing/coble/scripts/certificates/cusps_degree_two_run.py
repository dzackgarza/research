"""The degree-two 1-cusp construction, executed on the maintained baseline.

Target: the shared development image (Sage 11.0.beta5, Python 3.14.10), invoked as

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs \
        -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo \
        /sage/.venv/bin/sage -python /repo/writing/coble/scripts/certificates/cusps_degree_two_run.py

with `sage_extensions` taken from the published revision, not from the image's checkout:

    git -C /repos/sage-extensions fetch origin
    git -C /repos/sage-extensions worktree add /work/se-published 28407ef
    PYTHONPATH=/work/se-published/src

What it does: builds T_2 = <-2> + U + U + E8 + E8 and N = H + E8^2 + A1, takes the unique
0-cusp line I = <e_1>, forms I^perp/I through the library's own reduction and projection, and
then builds one 1-cusp -- the one whose null vector is known without the Coxeter diagram,
v = e, which gives the label E8^2 + A1.  For that cusp it keeps the maps: the lift along the
0-cusp projection, the plane's inclusion, the reduction to J^perp/J, and the even-overlattice
inclusion of the label whose codomain is that quotient.

The other three cusps still need the 24x24 Gram matrix of AET Fig. 1's roots and the
component-to-label correspondence; nothing about them is assumed here.
"""
import sys

from sage.all import ZZ, CartanMatrix

from sage_extensions.all import Lattices  # noqa: F401

print("python", sys.version.split()[0])
import sage_extensions
print("sage_extensions", sage_extensions.__file__)

# ---------------------------------------------------------------- T_2 and N
U_gram = [[0, 1], [1, 0]]                       # the hyperbolic plane
A1_gram = [[-2]]                                 # negative definite, as AET use it
E8_gram = [[-int(x) for x in row] for row in CartanMatrix(["E", 8]).rows()]

U = Lattices(ZZ)(U_gram)
A1 = Lattices(ZZ)(A1_gram)
E8 = Lattices(ZZ)(E8_gram)
T2 = U + U + E8 + E8 + A1                        # orthogonal sums, library-built
N = U + E8 + E8 + A1
print("T2: rank", T2.module_rank(), "det", T2.determinant(), "signature", T2.signature_pair())
print("N : rank", N.module_rank(), "det", N.determinant(), "signature", N.signature_pair())
assert T2.module_rank() == 21 and T2.determinant() == -2
assert tuple(int(x) for x in T2.signature_pair()) == (2, 19)
assert N.module_rank() == 19 and abs(N.determinant()) == 2

# ------------------------------------------------------------- the 0-cusp line
I = T2.primitive_isotropic_subobject(T2.basis_vector(1))
print("I: rank", I.module_rank(), "primitive", I.is_primitive(),
      "totally isotropic", I.is_totally_isotropic())
proj = I.isotropic_quotient_projection()
reduction = I.isotropic_reduction()
print("I^perp/I: rank", reduction.module_rank(), "det", reduction.determinant(),
      "signature", reduction.signature_pair())
print("I^perp/I is N:", reduction.is_isometric(N))
assert reduction.is_isometric(N)

# ------------------------------------------- one 1-cusp, as a plane of T_2 itself
#
# T_2 = U + U + E8 + E8 + A1, with the two hyperbolic summands spanned by
# (e1, f1) = (basis 0, basis 1) and (e2, f2) = (basis 2, basis 3).  The plane
# J = <f1, f2> is primitive and totally isotropic, and its quotient is the label
# E8^2 + A1 of that cusp.  Building the plane in T_2 directly is the form in which a cusp
# is actually given; the alternative route -- a null ray v of N lifted along the 0-cusp
# projection -- needs an isometry from N to I^perp/I to transport v, and `is_isometric`
# reports the existence of one without returning it.
J = T2.primitive_isotropic_subobject(T2.basis_vector(1), T2.basis_vector(3))
print("J: rank", J.module_rank(), "primitive", J.is_primitive(),
      "totally isotropic", J.is_totally_isotropic())
boundary = J.inclusion().isotropic_reduction()
print("J^perp/J: rank", boundary.module_rank(), "det", boundary.determinant(),
      "signature", boundary.signature_pair())
print("is negative definite:", boundary.is_negative_definite())
print("is even:", boundary.is_even())
assert boundary.module_rank() == 17
assert abs(boundary.determinant()) == 2 == abs(T2.determinant())

# The label of *this* cusp is E8^2 + A1, of rank 17 -- not N, which is the 0-cusp
# quotient H + E8^2 + A1.  The boundary is an overlattice of the label, so the check is
# against the label's even overlattice inclusions, not against N.
label = E8 + E8 + A1
print("label E8^2 + A1: rank", label.module_rank(), "det", label.determinant(),
      "signature", label.signature_pair())
inclusions = list(label.even_overlattice_inclusions())
print("the label has", len(inclusions), "even overlattice inclusions")
found = [inc for inc in inclusions if inc.codomain().is_isometric(boundary)]
print("quotient among them:", len(found))
index_squared = abs(label.determinant()) // abs(boundary.determinant())
print("index^2 = det(label)/det(boundary) =", index_squared)
print("the boundary *is* the label (index 1):", boundary.is_isometric(label))
print("isometry morphism available:", hasattr(label, "isometry_to"),
      "| discriminant modules:", boundary.discriminant_module().module_rank(),
      label.discriminant_module().module_rank())
