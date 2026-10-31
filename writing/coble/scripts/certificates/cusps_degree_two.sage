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
Write N = H + E8^2 + A1 with H = <e, f>, and let w lie in E8^2 + A1.  Then

    v = e + n*f + w,   n = -w^2/2,

is isotropic exactly when w^2 is even, which holds throughout E8^2 + A1.  So the null
rays are parametrized by (w, n), and the four O^+(N)-classes of them are the four
cusps.  One is immediate: w = 0 gives v = e, and

    v^perp/<v> = E8^2 + A1,

which is the label E8^2 + A1 and matches the affine diagram E~8^2 A~1 in [1]'s list.
The other three (w a root of E8, or w of square -4, ...) need the class computation;
the transcription slots are OPEN_CUSPS below.

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
`even_overlattice_inclusions` (:5937).  The accessors of the retained maps of a
reduction -- the projection out of S^perp and the lift back -- are documented only as
"the quotient retains its inclusion, perpendicular, projection lifts and parabolic
data" (`lattices.py:5695`), so their names carry a `# confirm` below and the first run
on the supported baseline is expected to fix them.  That is a signature detail of an
unexecuted call, not a claim about the library.
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
zero_cusp_reduction = I.inclusion().isotropic_reduction()
assert zero_cusp_reduction.is_nondegenerate()
assert zero_cusp_reduction.is_isometric(N)      # so T_2 -> N is the reduction of I
lift = zero_cusp_reduction.lift                # confirm: the retained lift back to T_2

# ------------------------------------------------------- the four 1-cusp planes

def cusp_plane(null_vector, label):
    r"""The plane J = I + Z*v_tilde for a null ray R_{>=0}v of N, and its quotient.

    Retains both maps: the lift of `null_vector` to T_2 along the reduction of I, and
    the reduction of the plane, so that J^perp/J is computed as the quotient of a
    plane and compared with the label by isometry rather than by invariants.
    """
    assert null_vector.is_isotropic() and null_vector.is_primitive()
    J = T2.primitive_isotropic_subobject(T2.basis_vector(1), lift(null_vector))
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

# The other three cusps.  Each entry is the vertex subset of [1] Fig. 1 (p. 22) for
# the named affine diagram, together with the affine marks that make the sum null.
# Transcription of the figure is outstanding; nothing is inserted by guesswork, and
# no label is being turned into a lattice in its place.
OPEN_CUSPS = {
    "A~17": None,          # [1] Fig. 1, left-most of the four small diagrams
    "D~10 E~7": None,      # [1] Fig. 1, second
    "D~16 A~1": None,      # [1] Fig. 1, third
}
#                    ("E~8^2 A~1" is the one computed above, as v = e.)

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
