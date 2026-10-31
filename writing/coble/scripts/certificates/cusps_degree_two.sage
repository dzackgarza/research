r"""
The four 1-cusps of F_2 as primitive isotropic planes of T_2.

UNEXECUTED.  Target: the research image's Sage development baseline (Python 3.14),
where `sage_extensions` imports.  Nothing here has been run, and no output of it is
evidence until it is; see `writing/dissertation/GAPS.md`.

Sources
-------
[1] V. Alexeev, P. Engel, A. Thompson, *Stable pair compactification of moduli of K3
    surfaces of degree 2*, arXiv:1903.09742v3, = bibliography key `AET23`.  Sec. 3B
    (p. 16): the boundary of F_2 is four curves through one point, the curves
    correspond to four orbits of rank 2 primitive isotropic J in h^perp, and
    "J^perp/J contains a finite index root sublattice, which can be used as a label":
    A17, D10 + E7, E8^2 + A1, D16 + A1.  Sec. 4A-4C (pp. 21-26): the Coxeter diagram
    G_cox of N = H + E8^2 + A1 (their Fig. 1, p. 22), Thm 4.3 (Type II rays
    R_{>=0} v with v^2 = 0 come from the maximal parabolic subdiagrams), Lem. 4.5
    (mod S_3 there are four, the four affine diagrams named in the caption).
[2] F. Scattone, *On the compactification of moduli spaces for algebraic K3
    surfaces*, Mem. AMS 70 (1987), no. 374, ch. 5 (rank two isotropic sublattices)
    and 6.2 (the fan).  Cited by [1] for the fan; not read here.

What a cusp is
--------------
Fix the 0-cusp line I in T_2.  By [1] Thm 4.3 each of the four 1-cusps is the cone
over one maximal parabolic subdiagram of G_cox: a null ray R_{>=0} v of N = I^perp/I,
and the cusp is the primitive isotropic plane

    J = I + Z*v_tilde        in T_2,

where v_tilde is the lift of v along the reduction T_2 -> N (which is the isotropic
reduction of I).  The label is the finite diagram obtained from the affine one by
deleting the null root, and J^perp/J = v^perp/Zv.  So the four cusps are four null
vectors of G_cox, and the construction below takes those vectors, not root labels, as
its input: the reduction of a *plane* is computed, never an enumeration of
overlattices of a label.

The parametrization of the null rays of N
-----------------------------------------
Write N = H + E8^2 + A1 with H = <e, f>, and let w lie in E8^2 + A1.  A vector of
N whose e-coefficient is 1 is

    v = e + n*f + w,   n = -w^2/2,

and it is isotropic exactly then, w^2 being even throughout E8^2 + A1.  ONE cusp is of
this shape: w = 0 gives v = e, and

    v^perp/<v> = E8^2 + A1,

the label E8^2 + A1, matching E~8^2 A~1 in [1]'s list.  This is NOT a claim that the
other three rays have a representative with e-coefficient 1: a general isotropic vector
is a*e + b*f + w with 2ab + w^2 = 0, and whether a can be taken 1 for each of the four
classes is a separate question, not checked here and not assumed below.  The script
takes the four null vectors as its input, in whatever coordinates they are transcribed
in, and never divides by the e-coefficient.

Why the transcription is not in the source text
-----------------------------------------------
[1] print G_cox as a *figure* with the 24 vertex labels and the edge multiplicities
(inner products 0, 1, 2, 6), and state that the 24 roots generate N, but they do not
give the coordinates of the roots.  The vertex subsets are transcribed from the figure's
own vector artwork (`read_fig1.py`) and recorded in VERTEX_SETS.  Two data are still
missing, and both are needed before a null vector can be formed for three of the four
cusps: the 24x24 Gram matrix of the roots (GRAM_GCOX), and the identification of each
affine component's Cartan-type nodes with Fig. 1 labels.  They are left explicit rather
than guessed, and no diagram label is ever used as a lattice coordinate: the roots are a
family of 24 vectors in a rank 19 lattice.

API.  The calls below are written against the documented methods of
`sage_extensions.categories.lattices` at revision
441519c574cec12ada06ad586f6c3862fbca96d0: `primitive_isotropic_subobject` (:7312),
`isotropic_reduction` (:5688, :8414), `is_primitive` (:8379) with
`is_saturated := is_primitive` (`module_morphisms.py:1671`), `saturation` (:2990),
`discriminant_module` (:5583), `discriminant_projection` (:5588),
`even_overlattice_inclusions` (:5937).  The retained maps of a reduction are owned in
`sage_extensions.categories.isotropic_parabolics`: `isotropic_perpendicular` (:84),
`into_perpendicular` (:93), `isotropic_quotient` (:104),
`isotropic_quotient_projection` (:120), plus `parabolic_subgroup` (:145),
`is_equivalent_to` (:306) and `transporter_witness_to` (:315); the lift along the
projection is the library's own morphism `lift`, whose section contract is validated by
`validate_lift` (`module_morphisms.py:589`).  Those are the names used below.  For the
marks, `CartanType(...).a()` and `RootSystem(...).root_lattice().null_root()` are the
verified accessors (see the marks section); `CartanType.null_root()` does not exist.
"""

from sage.all import ZZ, block_diagonal_matrix, matrix  # noqa: F401
from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.root_system.root_system import RootSystem

from sage_extensions.all import *  # noqa: F401,F403

# ---------------------------------------------------------------- the two models of N
#
# Two different models of N = H + E8^2 + A1 are needed and they are not interchangeable.
#
# (a) The standard model: an explicit basis, H = <e, f> with e^2 = f^2 = 0, e.f = 1, and
#     E8 negative definite.  This is the model in which the vector e is written down, i.e.
#     the one cusp whose null vector does not come from the Coxeter diagram.
#
# (b) The root-family model: the 24 numbered roots r_0..r_23 of AET Fig. 1, as a *family*
#     generating N.  The diagram gives their pairwise inner products and says they generate
#     N, so the realization is the lattice spanned by 24 generators of a rank 19 lattice --
#     24 vectors, not a basis, and the label i is an index into the family, never a basis
#     coordinate.  Concretely: the free module on the r_i with Gram matrix GRAM_GCOX, modulo
#     its radical; the library has to be asked for that lattice, not told coordinates.
#
# The script therefore never writes N.basis_vector(i) for a diagram label i.

U_gram = [[0, 1], [1, 0]]
A1_gram = [[-2]]
E8_gram = [[-int(x) for x in row] for row in CartanMatrix(["E", 8]).rows()]
U_lattice, A1_lattice, E8_neg_lattice = (Lattices(ZZ)(U_gram), Lattices(ZZ)(A1_gram),
                                        Lattices(ZZ)(E8_gram))
T2 = U_lattice + U_lattice + E8_neg_lattice + E8_neg_lattice + A1_lattice
N_standard = U_lattice + E8_neg_lattice + E8_neg_lattice + A1_lattice

assert T2.signature_pair() == (2, 19)          # the period lattice h^perp
assert T2.det() == -2
assert N_standard.module_rank() == 19 and abs(N_standard.det()) == 2

# The Gram matrix of the 24 roots, in the labels 0..23 of Fig. 1.  NOT YET TRANSCRIBED: the
# figure prints the diagram and the inner products 0, 1, 2, 6, and neither the article's
# text nor the repository carries the matrix.  It is the one datum the family model needs.
GRAM_GCOX = None

if GRAM_GCOX is not None:
    # the lattice spanned by the family: 24 generators with GRAM_GCOX, rank 19
    N_family = Lattices(ZZ)(GRAM_GCOX)          # the span, with its Gram
    assert N_family.module_rank() == 19
    assert N_family.is_even()
    # and it is the source's N, which is what licenses moving a null vector across
    assert N_family.is_isometric(N_standard)
    roots = [N_family.basis_vector(i) for i in range(24)]     # r_i, generators of N

# ----------------------------------------------------------- the 0-cusp line I

# I = <e_1>, the isotropic basis vector of the first hyperbolic summand.  The 0-cusp is
# unique up to Gamma_2 by [1] Sec. 3B, so any primitive isotropic vector may represent it.
I = T2.primitive_isotropic_subobject(T2.basis_vector(1))
assert I.is_primitive() and I.is_saturated()    # is_saturated := is_primitive
assert I.is_totally_isotropic() and I.module_rank() == 1
proj = I.isotropic_quotient_projection()        # I^perp ->> I^perp/I
zero_cusp_reduction = I.isotropic_reduction()   # the quotient lattice, with its form
assert zero_cusp_reduction.is_nondegenerate()
assert zero_cusp_reduction.is_isometric(N_standard)   # so I^perp/I is the source's N

# ------------------------------------------------------- the four 1-cusp planes

def cusp_plane(null_vector, label):
    r"""The plane J = I + Z*v_tilde for a primitive isotropic v in N, and J^perp/J.

    The label is a finite-index sublattice of J^perp/J, not generally the whole of it, so
    what is checked is that one of the even overlattices of the label *is* J^perp/J, with
    the index recorded.  Isometry with the label itself is asserted only in the index-1
    case; asserting it in general would be the error this contract exists to prevent.
    """
    assert null_vector.is_isotropic() and null_vector.is_primitive()
    lifted = proj.lift(null_vector.underlying_element())
    assert lifted is not None, (
        "the projection I^perp ->> I^perp/I returned no lift of this vector: either the "
        "vector is not in the image, or a lift has to be supplied explicitly"
    )
    J = T2.primitive_isotropic_subobject(T2.basis_vector(1), lifted)
    assert J.is_primitive() and J.is_saturated()
    assert J.module_rank() == 2

    boundary = J.inclusion().isotropic_reduction()
    assert boundary.module_rank() == 17
    assert boundary.is_negative_definite()
    # the determinant, forced by the splitting lemma (formalization/coble-enriques/
    # Splitting.lean), and the index of the label inside the boundary
    assert abs(boundary.det()) == abs(T2.det()) == 2
    det_label = abs(label.det())
    index_squared = det_label // abs(boundary.det())        # k^2 = det(label)/det(boundary)
    # J^perp/J is an even overlattice of the label: one of the label's even overlattice
    # inclusions has it as codomain.
    inclusions = [inc for inc in label.even_overlattice_inclusions()
                  if inc.codomain().is_isometric(boundary)]
    assert inclusions, (
        "J^perp/J is not an even overlattice of the label: the label is not a finite-index "
        "sublattice of the boundary lattice of this cusp"
    )
    if index_squared == 1:
        assert boundary.is_isometric(label)                  # the label is the boundary
    return J, boundary, inclusions[0], index_squared

# E8^2 + A1: the one null vector that does not come from the diagram.  In the standard
# model N = <e,f> + E8^2 + A1 the vector e is primitive isotropic and v^perp/Zv = E8^2 + A1.
# The label is that rank-17 lattice, NOT N: N is the 0-cusp quotient H + E8^2 + A1, of rank
# 19, and conflating the two is exactly the error the boundary contract above guards against.
LABEL_E8 = E8_neg_lattice + E8_neg_lattice + A1_lattice          # E8^2 + A1, rank 17
J_E8, B_E8, inc_E8, idx_E8 = cusp_plane(N_standard.basis_vector(0), LABEL_E8)
assert idx_E8 == 1                          # executed on the maintained baseline: see
                                           # cusps_degree_two_run.py and its output

# The vertex layout of [1] Fig. 1 (p. 22), rows top to bottom, as printed:
#
#     12
#     13  11
#     14  20  10
#     15  22  21   9
#     16            8
#     17  18  23  19   7
#      0   1   2   3   4   5   6
#
# The four vertex subsets, transcribed from the e-print artwork of the figure
# (`read_fig1.py`: the small figures' black disks, matched to the printed node positions).
VERTEX_SETS = {
    "A~17":     tuple(range(18)),                                   # the rim, an 18-cycle
    "D~10 E~7": (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20),
    "E~8^2 A~1":(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23),
    "D~16 A~1": (0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23),
}
assert [len(v) for v in VERTEX_SETS.values()] == [18, 19, 20, 19]
assert set(range(24)) - set(VERTEX_SETS["A~17"]) == {18, 19, 20, 21, 22, 23}

# --------------------------------------------------------- marks, from the root system
#
# The marks are the Kac marks of the affine Cartan type, and both maintained accessors are
# verified in the installed source, not guessed:
#
#   CartanType(["D", 10, 1]).a()                     indexed Kac marks (dict)
#   RootSystem(["D", 10, 1]).root_lattice().null_root()   the null root as a root-lattice
#                                                    element (docstring at
#                                                    root_lattice_realizations.py:1349,
#                                                    implemented as sum(a[k]*alpha[k]))
#
# CartanType.null_root() does not exist: CartanType carries a(), dynkin_diagram() and
# cartan_matrix() (cartan_type.py:1607 ff.), and null_root belongs to the root lattice
# realization.  So the call is
#
#     marks = CartanType(shape).a()                # {node index in the Cartan type: mark}
#
# and the node index is the one of the *Cartan type*, which has to be identified with the
# Fig. 1 labels through the induced graph; it is not the Fig. 1 label itself.
SHAPES = {"D~10 E~7": [["D", 10, 1], ["E", 7, 1]],   # the two components, per [1]'s caption
          "E~8^2 A~1": [["E", 8, 1], ["E", 8, 1], ["A", 1, 1]],
          "D~16 A~1": [["D", 16, 1], ["A", 1, 1]]}

# `CartanType(shape).dynkin_diagram()` is the maintained object to validate a transcribed
# component against (cartan_type.py:1607; cartan_matrix() builds the Cartan matrix from it),
# so a transcription is accepted only when its edge-labelled induced graph is isomorphic to
# the diagram of the Cartan type it is claimed to be.
MARKS = {name: [CartanType(s).a() for s in shapes] for name, shapes in SHAPES.items()}
# A~17 is the one component whose correspondence needs no matching: a cycle, so its marks
# are all 1, and CoxeterRim.lean proves that mark vector is null for the rim Gram matrix.
MARKS["A~17"] = [{i: 1 for i in range(18)}]

# Assemble each cusp's null vector *in the family model*, through the root family, never
# through basis coordinates:
#
#     for name, vertices in VERTEX_SETS.items():
#         components = component_vertex_lists[name]           # from the induced graph
#         v = N_family.zero()
#         for comp_vertices, marks in zip(components, MARKS[name]):
#             for node, mark in marks.items():
#                 v += mark * roots[comp_vertices[node]]       # roots[i] = r_i, i = Fig.1 label
#         J, boundary, inclusion, index = cusp_plane(v, label_lattice[name])
#
# The two data still missing for the last three cusps are exactly:
#   * GRAM_GCOX, the 24x24 Gram matrix of the roots (inner products 0, 1, 2, 6), which the
#     figure prints but which is not yet transcribed; and
#   * component_vertex_lists, the identification of each affine component's Cartan-type
#     nodes with Fig. 1 labels, which comes from the induced graph.

# ---------------------------------------------------------------- consistency

# The determinant is forced by the splitting lemma, independent of any of the above:
# det(J^perp/J) = +-det(T_2) = +-2 for every primitive isotropic plane J of T_2
# (formalization/coble-enriques/Splitting.lean).  So each of the four boundaries computed
# here must satisfy the assertion inside cusp_plane.
