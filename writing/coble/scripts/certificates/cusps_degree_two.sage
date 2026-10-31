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
give the coordinates of the roots.  Recovering the four vertex subsets therefore means
reading Fig. 1, exactly as `computations/scripts/sterk-enriques-cusps/
sterk_cusp_diagrams.sage` does for Sterk's figures; that transcription is what
OPEN_CUSPS records, and it is deliberately left empty rather than guessed.

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
`validate_lift` (`module_morphisms.py:589`).  Those are the names used below.
"""

from sage.all import ZZ, block_diagonal_matrix, matrix  # noqa: F401

from sage_extensions.all import *  # noqa: F401,F403

# ---------------------------------------------------------------- the lattices

# AET's conventions: U = <e, f> with e^2 = f^2 = 0, e.f = 1, and E8 negative
# definite.  T_2 = <-2> + U + U + E8 + E8 has rank 21, signature (2, 19), det -2.
U = matrix(ZZ, [[0, 1], [1, 0]])
E8_neg = -matrix(ZZ, CartanMatrix(["E", 8]).rows())          # negative definite
T2 = Lattices(ZZ)(block_diagonal_matrix([matrix(ZZ, [[-2]]), U, U, E8_neg, E8_neg]))
N = Lattices(ZZ)(block_diagonal_matrix([U, E8_neg, E8_neg, matrix(ZZ, [[-2]])]))

assert T2.signature_pair() == (2, 19)          # the period lattice h^perp
assert T2.det() == -2
assert N.is_isometric(N)                        # N = H + E8^2 + A1, from [1] p. 17

# ----------------------------------------------------------- the 0-cusp line I

# I = <e_1>, the isotropic basis vector of the first hyperbolic summand.  The 0-cusp
# is unique up to Gamma_2 by [1] Sec. 3B, so any primitive isotropic vector may be
# taken as the representative; this one makes I^perp/I isometric to N by inspection.
I = T2.primitive_isotropic_subobject(T2.basis_vector(1))
assert I.is_primitive() and I.is_saturated()    # is_saturated := is_primitive
assert I.is_totally_isotropic() and I.module_rank() == 1
I_perp = I.isotropic_perpendicular()            # I^perp, as a subobject of T_2
proj = I.isotropic_quotient_projection()        # I^perp ->> I^perp/I
zero_cusp_reduction = I.isotropic_reduction()   # the quotient lattice, with its form
assert zero_cusp_reduction.is_nondegenerate()
assert zero_cusp_reduction.is_isometric(N)      # so I^perp/I is the source's N

# ------------------------------------------------------- the four 1-cusp planes

def cusp_plane(null_vector, label):
    r"""The plane J = I + Z*v_tilde for a null ray R_{>=0}v of N, and its quotient.

    Retains both maps: the lift of `null_vector` to T_2 along the reduction of I, and
    the reduction of the plane, so that J^perp/J is computed as the quotient of a
    plane and compared with the label by isometry rather than by invariants.
    """
    assert null_vector.is_isotropic() and null_vector.is_primitive()
    # the lift along the 0-cusp projection, through the library's own section contract
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
    # the finite diagram left by the affine one, i.e. the label
    assert boundary.is_isometric(label), (boundary, label)
    return J, boundary


# E8^2 + A1: v = e, the case fixed without the figure.  v^perp/<v> = E8^2 + A1.
J_E8, B_E8 = cusp_plane(N.basis_vector(0), N)

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
# The rim of the triangle, in cyclic order, is
RIM = (12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# and the first of the four small figures beside Fig. 1 has exactly the rim black and the
# six interior nodes 20, 22, 21, 23, 19, 18 white: an 18-cycle, i.e. an affine A17, whose
# marks are all 1.  So the A~17 cusp's null vector is the sum of the eighteen rim roots.
# `formalization/coble-enriques/CoxeterRim.lean` proves that this mark vector is in the
# kernel of the rim Gram matrix and is isotropic (rim_mulVec_marks, rim_marks_isotropic).
A17_CUSP = dict(vertices=RIM, marks=tuple([1] * 18), label="A(17)")

# The other three vertex subsets, transcribed from the e-print artwork of the same figure
# by `read_fig1.py` (arXiv:1903.09742v3, fig-wD10wE7.pdf, fig-2wE8wA1.pdf,
# fig-wD16wA1.pdf; the small figures' black nodes, matched to the labelled layout).  What
# is verified is the vertex set and its size; the *marks* are attached to the affine
# diagram's nodes and so need the induced graph, which the same artwork encodes in its
# stroke widths and has not been read yet.  So these entries carry the vertex set only.
VERTEX_SETS = {
    "D~10 E~7":    (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20),
    "E~8^2 A~1":   (0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23),
    "D~16 A~1":    (0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23),
}
assert [len(v) for v in VERTEX_SETS.values()] == [19, 20, 19]
assert tuple(sorted(set(range(24)) - set(VERTEX_SETS["E~8^2 A~1"]))) == (3, 12, 21, 22)

OPEN_CUSPS = {name: None for name in VERTEX_SETS}   # marks pending the induced graph

# ---------------------------------------------------- mark recovery, via the root system
#
# The marks of an affine diagram are its null root, and the maintained way to get them is
# Sage's root-system machinery, not a table written out by hand:
#
#     from sage.combinat.root_system.cartan_type import CartanType
#     shape = CartanType(['D', 10, 1])          # the affine diagram, from AET's caption
#     marks = shape.null_root()                 # {index: coefficient}
#
# What is still needed before those calls can run is the correspondence between the
# affine diagram's nodes and the vertex labels of Fig. 1, i.e. the induced graph read off
# the artwork.  The pipeline in `read_fig1.py` recovers the *vertices* (and reproduces the
# 18-cycle for A~17), but on the other three its edge list carries strokes that are not
# edges of G_cox -- for instance (0,18), (3,20), (9,18), (12,20) in the D~10 E~7 figure --
# so an edge is not yet accepted as a diagram edge.  The cross-check that decides it is
# against the edge set of the labelled `fig-Vinberg` artwork, which is the next
# transcription step; until it is done, no mark is assigned and no null vector is formed
# for those three cusps.
#
# Once the edge sets are settled, each cusp is assembled as
#
#     vertices, marks = ...                       # per cusp, from the two transcriptions
#     v = sum(marks[i] * N.basis_vector(i) for i in vertices)
#     J, boundary = cusp_plane(v, label_of[name])  # as for A~17 above
#
# with the isometry to the label and, if wanted, `boundary.discriminant_module()` in place
# of any hand-rolled comparison of invariants.

# What each transcribed entry turns into, unchanged for all four:
#
#     vertices, marks = OPEN_CUSPS[name]
#     v = sum(marks[i] * N.basis_vector(i) for i in vertices)   # null, primitive
#     J, boundary = cusp_plane(v, label_of[name])
#
# and then the glue, if it is still wanted, is a question about `boundary` alone:
#
#     boundary.discriminant_module()          # A of J^perp/J, not of the label
#     label.discriminant_projection()         # A_label -> A of J^perp/J, for the inclusion
#     label.even_overlattice_inclusions()     # the candidate inclusions; one of them is
#                                             # boundary, and the isometry above says which
#
# The last line is the only place where overlattices enter, and it enters as a check on
# a computed quotient, not as a substitute for one.

# ---------------------------------------------------------------- consistency

# The determinant is forced by the splitting lemma, independent of any of the above:
# det(J^perp/J) = +-det(T_2) = +-2 for every primitive isotropic plane J of T_2
# (formalization/coble-enriques/Splitting.lean).  So each of the four boundaries
# computed here must satisfy
assert abs(B_E8.det()) == 2
