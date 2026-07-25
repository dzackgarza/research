r"""Sterk's five root configurations in $L_{20,2,0} = U \oplus U(2) \oplus E_8^2$.

Ported from the Sterk section of the old init.sage. Two things about that source
made a naive transcription unsafe, and both are handled here by *not* reusing names:

**The ``w`` rebinding.** Line 400 bound ``w1..w8``, ``w1t..w8t`` to the columns of
$G^{-1}$, i.e. the dual basis. Lines 465-483 then rebound ``w1..w19`` to the
$(18,0,0)$ root vectors -- and line 472 read the old meaning to define the new one
(``w8 = w8 + e``). The file is only correct when executed strictly in order. Here the
dual vectors are ``DUAL[...]`` and the roots are ``roots_18_0_0()``, so no name ever
means two things.

**The ``a`` rebinding.** Line 399 bound ``e, f, ep, fp, a1..a8, a1t..a8t`` to the
$L_{20,2,0}$ basis; line 592 rebound ``e, f, ep, fp, a1..a8`` to the *$T_{En}$* basis
for the later ``sterks1/2/3`` lists. Those are different lattices of different rank,
so the two halves of the section are not in the same coordinates. This module ports
the $L_{20,2,0}$ half -- the one the ``Sterk_roots`` dict is built from. See
:data:`NOT_PORTED` for the rest.

Everything is carried as coordinate vectors over $\mathbf{Q}$ with the form applied
as $x^{T} G y$: the configurations mix basis vectors with dual vectors, so they do not
all live in the lattice itself, and pretending otherwise would force spurious
coercions.
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ

from . import catalogue

__all__ = [
    "NOT_PORTED",
    "STERK_ROOT_COUNTS",
    "bilinear_form",
    "gram",
    "gram_of",
    "isotropic_vectors",
    "roots_18_0_0",
    "roots_18_2_0",
    "sterk_roots",
    "sterks_in_ten",
    "RECORDED_ROOT_MATRIX_ROWS",
]

#: Root counts per case. These match the old file's section headers ("Sterk 1: 12
#: roots"), but a comment is not an oracle: the counts are independently justified by
#: :func:`sterk_roots`, which asserts every listed vector has root norm -2 or -4. The
#: one vector that disagreed with a header turned out to be isotropic, not a missing
#: root -- see :func:`isotropic_vectors`.
STERK_ROOT_COUNTS: dict[str, int] = {
    "Sterk_1": 12,
    "Sterk_2": 10,
    "Sterk_3": 12,
    "Sterk_4": 11,
    "Sterk_5": 14,
}

#: Sterk's published root counts, broken down by norm, exactly as the old file's
#: annotations record them ("Sterk had 12: 12x -4 roots").
STERK_PUBLISHED: dict[str, dict[str, int]] = {
    "Sterk_1": {"total": 12, "norm_-4": 12, "norm_-2": 0},
    "Sterk_2": {"total": 10, "norm_-4": 9, "norm_-2": 1},
    "Sterk_3": {"total": 12, "norm_-4": 10, "norm_-2": 2},
    "Sterk_4": {"total": 11, "norm_-4": 9, "norm_-2": 2},
    "Sterk_5": {"total": 14, "norm_-4": 10, "norm_-2": 4},
}

#: Results of two *independent* computational runs recorded in the old file (lines
#: 720-855) as explicit coordinate matrices, with timings and ideal-vertex counts.
#: This is an open discrepancy, not settled bookkeeping: both implementations find
#: about ten roots where Sterk publishes more, and both report ideal vertices --
#: cusps -- separately from roots.
#:
#: The distinction matters and is the same one that resolved ``s4_12``: an ideal
#: vertex is an isotropic vector, a cusp of the hyperbolic polyhedron, not a facet.
#: ``s4_12`` is isotropic and Sterk 4 is recorded as having 2 ideal vertices, so it
#: is plausibly one of them -- a check worth doing rather than a conclusion.
#:
#: The source annotates Sterk 2 "Almost exactly matches Sterk."
COMPUTED_ROOT_COUNTS: dict[str, dict[str, Any]] = {
    "Sterk_1": {"julia": 9, "vinal": 10, "ideal_vertices": 1},
    "Sterk_2": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_3": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_4": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_5": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
}

#: Nothing from the Sterk section remains unported. ``sterks1``/``sterks2``/
#: ``sterks3`` are :func:`sterks_in_ten`; the commented ``sterks4``/``sterks5`` and the
#: ``tilde_*`` change of basis (old lines 630-664) are alternative derivations of the
#: same configurations, superseded by :func:`sterk5_in_U_E8_2` which the source itself
#: kept as live code.
NOT_PORTED: tuple[str, ...] = ()

_BASIS_NAMES = ["e", "f", "ep", "fp"] + [f"a{i}" for i in range(1, 9)] + [f"a{i}t" for i in range(1, 9)]
_DUAL_NAMES = ["eb", "fb", "epb", "fpb"] + [f"w{i}" for i in range(1, 9)] + [f"w{i}t" for i in range(1, 9)]


def gram() -> Any:
    r"""Gram matrix of $L_{20,2,0} = U \oplus U(2) \oplus E_8^2$."""
    return catalogue.L_20_2_0.gram_matrix()


def _frames() -> tuple[dict[str, Any], dict[str, Any]]:
    """The basis and its dual, as coordinate vectors over QQ."""
    matrix_gram = gram().change_ring(QQ)
    size = matrix_gram.ncols()
    assert size == 20, f"expected rank 20, got {size}"

    basis = {name: vector(QQ, [1 if j == i else 0 for j in range(size)]) for i, name in enumerate(_BASIS_NAMES)}
    dual = dict(zip(_DUAL_NAMES, matrix_gram.inverse().columns(), strict=True))

    # The defining property of the dual frame, asserted rather than trusted: the old
    # file obtained it as the columns of the inverse Gram matrix without checking.
    for i, basis_name in enumerate(_BASIS_NAMES):
        for j, dual_name in enumerate(_DUAL_NAMES):
            expected = 1 if i == j else 0
            assert bilinear_form(basis[basis_name], dual[dual_name]) == expected, f"dual frame is wrong: <{basis_name}, {dual_name}> != {expected}"
    return basis, dual


def bilinear_form(left: Any, right: Any) -> Any:
    r"""$\langle x, y\rangle = x^{T} G y$, for vectors in $L \otimes \mathbf{Q}$.

    The old file called ``L_20_2_0.b(v22, x)`` for this; Sage's integral lattices have
    no ``b`` method, so that call site was dead like several others in the file.
    """
    return left * gram().change_ring(QQ) * right


def roots_18_2_0() -> dict[str, Any]:
    r"""The 22 root vectors $v_1, \ldots, v_{22}$ for $(18, 2, 0)$.

    Built from the basis and the *dual* frame, exactly as old lines 435-458 -- before
    the ``w`` rebinding, so ``w1``, ``w2``, ``w8``, ``w1t``, ``w2t``, ``w8t`` here are
    the dual vectors.
    """
    b, d = _frames()
    v = {
        "v1": b["a8t"],
        "v2": b["ep"] + b["fp"] + d["w1"] + d["w8t"],
        "v3": b["a1"],
        "v4": b["a3"],
        "v5": b["a4"],
        "v6": b["a5"],
        "v7": b["a6"],
        "v8": b["a7"],
        "v9": b["a8"],
        "v10": b["ep"] + b["fp"] + d["w8"] + d["w1t"],
        "v11": b["a1t"],
        "v12": b["a3t"],
        "v13": b["a4t"],
        "v14": b["a5t"],
        "v15": b["a6t"],
        "v16": b["a7t"],
        "v17": b["ep"] + d["w8t"],
        "v18": b["a2"],
        "v19": b["ep"] + d["w8"],
        "v20": b["a2t"],
        "v21": b["fp"] - b["ep"],
        "v22": 5 * b["ep"] + 3 * b["fp"] + 2 * d["w2"] + 2 * d["w2t"],
    }
    assert len(v) == 22, f"expected 22 vectors, built {len(v)}"
    return v


def roots_18_0_0() -> dict[str, Any]:
    r"""The 19 root vectors $w_1, \ldots, w_{19}$ for $(18, 0, 0)$.

    Old lines 465-483. ``w8`` is the case the rebinding made delicate: the source
    wrote ``w8 = w8 + e``, whose right-hand side is the *dual* vector ``w8``, so the
    root is $w_8^{\vee} + e$. ``w10 = w8t + e`` reads ``w8t``, which the rebinding
    never touched, so it is the dual vector too.
    """
    b, d = _frames()
    w = {
        "w1": b["a1"],
        "w2": b["a3"],
        "w3": b["a4"],
        "w4": b["a5"],
        "w5": b["a6"],
        "w6": b["a7"],
        "w7": b["a8"],
        "w8": d["w8"] + b["e"],
        "w9": b["f"] - b["e"],
        "w10": d["w8t"] + b["e"],
        "w11": b["a8t"],
        "w12": b["a7t"],
        "w13": b["a6t"],
        "w14": b["a5t"],
        "w15": b["a4t"],
        "w16": b["a3t"],
        "w17": b["a1t"],
        "w18": b["a2"],
        "w19": b["a2t"],
    }
    assert len(w) == 19, f"expected 19 vectors, built {len(w)}"
    return w


def sterk_roots() -> dict[str, tuple[Any, ...]]:
    r"""The five Sterk root configurations, with their counts asserted.

    Cases 1, 3, 4, 5 are built from the $(18,2,0)$ roots; case 2 from $(18,0,0)$.

    Two source details preserved deliberately:

    - Sterk 4's ``s4_12 = v22 + v21`` (old line 559) is omitted from the root list at
      line 561, and that omission is correct on mathematical grounds, not because the
      line is dead: its norm is **0**, so it is not a root. See
      :func:`isotropic_vectors`, which keeps it.
    - Sterk 3's last two entries apply the involution
      $x \mapsto x + \tfrac{1}{2}\langle v_{22}, x\rangle v_{22}$ via the old
      ``inv``/``wa`` lambdas, whose commented alternatives read ``v22 + 2*v20`` and
      ``v22 + 2*v18``. The lambda form is used, and the comments' claim is asserted.
    """
    v = roots_18_2_0()
    w = roots_18_0_0()

    def reflect(x: Any) -> Any:
        return x + QQ((1, 2)) * bilinear_form(v["v22"], x) * v["v22"]

    def involute(x: Any) -> Any:
        return x + reflect(x)

    configurations: dict[str, tuple[Any, ...]] = {
        "Sterk_1": (
            v["v3"] + v["v11"],
            v["v4"] + v["v12"],
            v["v5"] + v["v13"],
            v["v6"] + v["v14"],
            v["v7"] + v["v15"],
            v["v8"] + v["v16"],
            v["v9"] + v["v1"],
            v["v10"] + v["v2"],
            v["v17"] + v["v19"],
            v["v21"],
            v["v22"],
            v["v18"] + v["v20"],
        ),
        "Sterk_2": (
            w["w1"] + w["w17"],
            w["w2"] + w["w16"],
            w["w3"] + w["w15"],
            w["w4"] + w["w14"],
            w["w5"] + w["w13"],
            w["w6"] + w["w12"],
            w["w7"] + w["w11"],
            w["w8"] + w["w10"],
            w["w9"],
            w["w18"] + w["w19"],
        ),
        "Sterk_3": (
            v["v13"],
            v["v14"] + v["v12"],
            v["v15"] + v["v11"],
            v["v16"] + v["v10"],
            v["v1"] + v["v9"],
            v["v2"] + v["v8"],
            v["v3"] + v["v7"],
            v["v4"] + v["v6"],
            v["v5"],
            v["v17"] + v["v19"],
            involute(v["v20"]),
            involute(v["v18"]),
        ),
        "Sterk_4": (
            v["v15"],
            v["v16"] + v["v14"],
            v["v1"] + v["v13"],
            v["v2"] + v["v12"],
            v["v3"] + v["v11"],
            v["v4"] + v["v10"],
            v["v5"] + v["v9"],
            v["v6"] + v["v8"],
            v["v7"],
            v["v17"] + v["v20"],
            v["v18"] + v["v19"],
        ),
        "Sterk_5": (
            v["v16"] + 2 * v["v1"] + v["v2"],
            v["v2"] + 2 * v["v3"] + v["v4"],
            v["v4"] + 2 * v["v5"] + v["v6"],
            v["v6"] + 2 * v["v7"] + v["v8"],
            v["v8"] + 2 * v["v9"] + v["v10"],
            v["v10"] + 2 * v["v11"] + v["v12"],
            v["v12"] + 2 * v["v13"] + v["v14"],
            v["v14"] + 2 * v["v15"] + v["v16"],
            v["v17"],
            v["v18"],
            v["v19"],
            v["v20"],
            v["v21"],
            v["v22"],
        ),
    }

    for name, roots in configurations.items():
        assert len(roots) == STERK_ROOT_COUNTS[name], f"{name}: source header says {STERK_ROOT_COUNTS[name]} roots, built {len(roots)}"
        # The transcription check that actually bites: a root has norm -2 or -4 in
        # this repo's negative-definite convention, and a mistyped coordinate in any
        # of these ~60 vectors would almost certainly land outside that set.
        for index, root in enumerate(roots, start=1):
            norm = bilinear_form(root, root)
            assert norm in (-2, -4), f"{name} root {index} has norm {norm}; roots must have norm -2 or -4"
    assert involute(v["v20"]) == v["v22"] + 2 * v["v20"], "Sterk 3: the involution disagrees with the source's commented form v22 + 2*v20"
    assert involute(v["v18"]) == v["v22"] + 2 * v["v18"], "Sterk 3: the involution disagrees with the source's commented form v22 + 2*v18"
    return configurations


_TEN_BASIS_NAMES = ["e", "f", "ep", "fp"] + [f"a{i}" for i in range(1, 9)]
_TEN_DUAL_NAMES = ["ed", "fd", "epd", "fpd"] + [f"w{i}" for i in range(1, 9)]


def ten_frames() -> tuple[dict[str, Any], dict[str, Any], Any]:
    r"""The named basis and dual frame of $T_{En} = U \oplus E_{10}(2)$.

    Old lines 326-335, where the source wrote the basis with Sage's ellipsis
    generator syntax and took ``TEn.dual_basis()``. This is the blocking dependency
    for everything in the Enriques half of the file.
    """
    matrix_gram = catalogue.TEn.gram_matrix().change_ring(QQ)
    size = matrix_gram.ncols()
    assert size == 12, f"TEn should have rank 12, got {size}"

    basis = {name: vector(QQ, [1 if j == i else 0 for j in range(size)]) for i, name in enumerate(_TEN_BASIS_NAMES)}
    dual = dict(zip(_TEN_DUAL_NAMES, matrix_gram.inverse().columns(), strict=True))

    def form(left: Any, right: Any) -> Any:
        return left * matrix_gram * right

    for i, basis_name in enumerate(_TEN_BASIS_NAMES):
        for j, dual_name in enumerate(_TEN_DUAL_NAMES):
            expected = 1 if i == j else 0
            assert form(basis[basis_name], dual[dual_name]) == expected, f"TEn dual frame is wrong: <{basis_name}, {dual_name}> != {expected}"
    return basis, dual, matrix_gram


def generating_isotropic_vectors() -> dict[str, Any]:
    r"""The five isotropic vectors of $T_{En}$ that generate the Sterk cases.

    Old lines 337-352 -- the derivation the root configurations come from, and the
    answer to *why there are five Sterk cases*:

    $$\text{Sterk}_j := e_j^{\perp} / \langle e_j \rangle, \qquad j = 1, \ldots, 5.$$

    The source labels ``omega = 2*w8`` a "Square 4 vector" and ``alpha = 2*w1`` a
    "Square 8 vector". Those labels are checkable, and are asserted here -- they also
    confirm the basis ordering, since ``E10 = U @ E8`` and ``E8 @ U`` give isomorphic
    lattices whose coordinates disagree.
    """
    basis, dual, matrix_gram = ten_frames()

    def form(left: Any, right: Any) -> Any:
        return left * matrix_gram * right

    omega = 2 * dual["w8"]
    alpha = 2 * dual["w1"]
    assert abs(form(omega, omega)) == 4, f"source calls omega a square-4 vector; it has norm {form(omega, omega)}"
    assert abs(form(alpha, alpha)) == 8, f"source calls alpha a square-8 vector; it has norm {form(alpha, alpha)}"

    e, f, ep, fp = basis["e"], basis["f"], basis["ep"], basis["fp"]
    vectors = {
        "Sterk_1": e,
        "Sterk_2": ep,
        "Sterk_3": ep + fp + omega,
        "Sterk_4": ep + 2 * fp + alpha,
        "Sterk_5": 2 * e + 2 * f + alpha,
    }
    for name, vector_ in vectors.items():
        norm = form(vector_, vector_)
        assert norm == 0, f"{name} generator must be isotropic, has norm {norm}"
    assert len(vectors) == 5, "there are five Sterk cases, one per isotropic vector"
    return vectors


def diagonal_embedding_images() -> dict[str, Any]:
    r"""$a_i' = a_i + \tilde a_i$ and $w_i' = w_i + \tilde w_i$ in $L_{20,2,0}$.

    Old lines 406-422, computed and then never used. The source's comment states what
    they are: *"The primes are the image of the diagonal embedding from $E_8(2)$"* --
    the two $E_8$ summands of $L_{20,2,0}$ mapped in diagonally.

    That claim is checkable and is asserted: the span of the eight $a_i'$ is isometric
    to $E_8(2)$.
    """
    basis, dual = _frames()
    images = {f"a{i}p": basis[f"a{i}"] + basis[f"a{i}t"] for i in range(1, 9)}
    images.update({f"w{i}p": dual[f"w{i}"] + dual[f"w{i}t"] for i in range(1, 9)})

    a_primes = [images[f"a{i}p"] for i in range(1, 9)]
    induced = matrix(QQ, [[bilinear_form(x, y) for y in a_primes] for x in a_primes])
    expected = catalogue.E8_2.gram_matrix().change_ring(QQ)
    assert induced == expected, "the a_i' do not span E8(2); the source's diagonal-embedding claim fails"
    return images


def sterk5_in_U_E8_2() -> tuple[Any, tuple[Any, ...]]:
    r"""Sterk 5's configuration inside $U \oplus E_8(2)$, from ``getSterk5()``.

    Old lines 666-680: live code, a second presentation of the Sterk 5 case in a
    rank-10 lattice rather than the rank-20 $L_{20,2,0}$ used by :func:`sterk_roots`.
    Returns the lattice and its 14 vectors, in the source's order, which the commented
    label list at line 682 gives as::

        a2, a4, a5, a6, a7, a8, a8d, a10, a11, a12, a13, a14, a1, a9

    Fourteen vectors, matching Sterk 5's published count.
    """
    lattice = catalogue.U.direct_sum(catalogue.E8_2)
    gram_matrix = lattice.gram_matrix().change_ring(QQ)
    assert gram_matrix.ncols() == 10, f"expected rank 10, got {gram_matrix.ncols()}"

    size = 10
    unit = [vector(QQ, [1 if j == i else 0 for j in range(size)]) for i in range(size)]
    e, f = unit[0], unit[1]
    a = {i: unit[i + 1] for i in range(1, 9)}
    dual_columns = gram_matrix.inverse().columns()
    ad = {i: dual_columns[i + 1] for i in range(1, 9)}

    a9 = 2 * e - a[1]
    a10 = 2 * e + 2 * (ad[2] - ad[3])
    a11 = f - e
    a12 = e + f + 2 * (ad[6] - ad[3])
    a13 = e + f + 2 * (ad[1] + ad[8] - ad[3])
    a14 = e + f + a[3]

    vectors = (
        a[2],
        a[4],
        a[5],
        a[6],
        a[7],
        a[8],
        2 * ad[8],
        a10,
        a11,
        a12,
        a13,
        a14,
        a[1],
        a9,
    )
    assert len(vectors) == 14, f"expected 14 vectors, got {len(vectors)}"

    def form(left: Any, right: Any) -> Any:
        return left * gram_matrix * right

    norms = [form(v, v) for v in vectors]
    assert all(n in (-2, -4) for n in norms), f"getSterk5 vectors must be roots; norms are {sorted(set(norms))}"
    return lattice, vectors


def sterks_in_ten() -> dict[str, tuple[Any, ...]]:
    r"""``sterks1``, ``sterks2``, ``sterks3`` in $T_{En}$ coordinates (old lines 585-628).

    A second family of configurations, in $T_{En}$ rather than $L_{20,2,0}$. Three
    details of the source are load-bearing and easy to lose:

    - **The dual scaling differs between blocks.** ``sterks1``/``sterks2`` take their
      dual vectors from the columns of $2G^{-1}$ (the source's ``dualize`` lambda);
      ``sterks3`` re-derives them from $G^{-1}$ (old line 611). Using one scaling
      throughout silently changes every ``a_i d`` vector.
    - ``a9``..``a13`` are **rebound between blocks**, so each configuration must be
      built before the next block's assignments happen.
    - The lists were written ``[a1, ..., a12]`` with an ellipsis in a *list literal*,
      which Sage does not expand for lattice elements; the ranges are spelled out here.
    """
    basis, _, matrix_gram = ten_frames()
    e, f, ep, fp = basis["e"], basis["f"], basis["ep"], basis["fp"]
    a = {i: basis[f"a{i}"] for i in range(1, 9)}

    # sterks1 / sterks2: dual frame scaled by 2, per the source's ``dualize`` lambda.
    doubled = (2 * matrix_gram.inverse()).columns()
    ad2 = {i: doubled[i + 3] for i in range(1, 9)}

    sterks1 = tuple(a[i] for i in range(1, 9)) + (
        fp - ep,
        ad2[8] + 2 * ep,
        2 * ep + 2 * fp + ad2[1] + ad2[8],
        5 * ep + 3 * fp + 2 * ad2[2],
    )
    sterks2 = tuple(a[i] for i in range(1, 9)) + (ad2[8] + 2 * f, e - f)

    # sterks3: dual frame NOT scaled (old line 611 re-derives from Ginv).
    plain = matrix_gram.inverse().columns()
    ad1 = {i: plain[i + 3] for i in range(1, 9)}

    sterks3 = tuple(a[i] for i in range(1, 8)) + (
        f - e,
        2 * fp + 2 * ad1[8],
        2 * e - 2 * fp - 2 * ad1[8],
        2 * e + 2 * (ad1[1] - ad1[8]),
        (e + f) + (a[8] - fp),
    )

    configurations = {"sterks1": sterks1, "sterks2": sterks2, "sterks3": sterks3}
    assert len(sterks1) == 12, len(sterks1)
    assert len(sterks2) == 10, len(sterks2)
    assert len(sterks3) == 12, len(sterks3)
    return configurations


#: The explicit rank-10 root matrix recorded at old lines 845-861, kept as data. The
#: source gives no lattice for it beyond its position in the file, next to the
#: ``IIPQ(1,17)`` citation, so it is not interpreted here -- only preserved.
RECORDED_ROOT_MATRIX_ROWS: tuple[tuple[int, ...], ...] = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
    (0, 2, 0, 0, -2, -1, -4, -3, -2, -1),
    (1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
    (4, 4, 0, 0, -10, -5, -21, -17, -13, -9),
    (-6, -6, 1, 0, 16, 7, 31, 25, 19, 13),
)


def isotropic_vectors() -> dict[str, Any]:
    r"""Isotropic vectors the source computed alongside the root configurations.

    ``s4_12 = v_{22} + v_{21}`` (old line 559) was computed and then left out of the
    Sterk 4 list at line 561. That is not an oversight and not dead code: its norm is
    $0$, so it is not a root -- the roots in these configurations have norm $-2$ or
    $-4$. An isotropic vector in the closure of the fundamental cone is a **cusp**, an
    ideal vertex of the hyperbolic polyhedron, which is a different kind of object
    from a facet and so has no place in a root list.

    It is recorded here because the source recorded it. The old file was as much a
    log of what was computed as a library, and a vector the author derived is a
    finding whether or not a later list used it.

    Note also that $v_{21}$ and $v_{22}$ appear as separate *roots* in Sterk 1
    (``s1_10``, ``s1_11``) and Sterk 5 (``s5_13``, ``s5_14``); it is specifically
    their sum, formed only in the Sterk 4 block, that is isotropic.
    """
    v = roots_18_2_0()
    vectors = {"s4_12": v["v22"] + v["v21"]}

    for name, vector_ in vectors.items():
        norm = bilinear_form(vector_, vector_)
        assert norm == 0, f"{name} was recorded as isotropic but has norm {norm}; if this changes, it may be a root and the Sterk 4 count needs revisiting"
    return vectors


def gram_of(roots: tuple[Any, ...]) -> Any:
    """Gram matrix of a root configuration, for feeding the Coxeter diagram."""
    return matrix(QQ, [[bilinear_form(x, y) for y in roots] for x in roots])
