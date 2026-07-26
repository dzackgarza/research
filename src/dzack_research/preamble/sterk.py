r"""Sterk root configurations in $U\oplus U(2)\oplus E_8^2$.

EXAMPLES::

    sage: from dzack_research.preamble.sterk import sterk_roots
    sage: {name: len(roots) for name, roots in sterk_roots().items()}
    {'Sterk_1': 12, 'Sterk_2': 10, 'Sterk_3': 12, 'Sterk_4': 11, 'Sterk_5': 14}
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ

from . import catalogue
from .fixtures import (
    COMPUTED_ROOT_COUNTS,
    RECORDED_ROOT_MATRIX_ROWS,
    STERK_PUBLISHED,
    STERK_ROOT_COUNTS,
)
from .fixtures import (
    L20_BASIS_NAMES as _BASIS_NAMES,
)
from .fixtures import (
    L20_DUAL_NAMES as _DUAL_NAMES,
)
from .fixtures import (
    TEN_BASIS_NAMES as _TEN_BASIS_NAMES,
)
from .fixtures import (
    TEN_DUAL_NAMES as _TEN_DUAL_NAMES,
)

__all__ = [
    "COMPUTED_ROOT_COUNTS",
    "NOT_PORTED",
    "RECORDED_ROOT_MATRIX_ROWS",
    "STERK_PUBLISHED",
    "STERK_ROOT_COUNTS",
    "bilinear_form",
    "gram",
    "gram_of",
    "isotropic_vectors",
    "roots_18_0_0",
    "roots_18_2_0",
    "sterk_roots",
    "sterks_in_ten",
]

NOT_PORTED: tuple[str, ...] = ()


def gram() -> Any:
    r"""Return the Gram matrix of $U\oplus U(2)\oplus E_8^2$."""
    return catalogue.L_20_2_0.gram_matrix()


def _frames() -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the basis and dual basis over ``QQ``."""
    matrix_gram = gram().change_ring(QQ)
    size = matrix_gram.ncols()
    assert size == 20, f"expected rank 20, got {size}"

    basis = {
        name: vector(QQ, [1 if j == i else 0 for j in range(size)])
        for i, name in enumerate(_BASIS_NAMES)
    }
    dual = dict(zip(_DUAL_NAMES, matrix_gram.inverse().columns(), strict=True))

    for i, basis_name in enumerate(_BASIS_NAMES):
        for j, dual_name in enumerate(_DUAL_NAMES):
            expected = 1 if i == j else 0
            assert bilinear_form(basis[basis_name], dual[dual_name]) == expected, (
                f"dual basis is wrong: <{basis_name}, {dual_name}> != {expected}"
            )
    return basis, dual


def bilinear_form(left: Any, right: Any) -> Any:
    r"""Return $\langle x,y\rangle=x^TGy$."""
    return left * gram().change_ring(QQ) * right


def roots_18_2_0() -> dict[str, Any]:
    r"""Return the root vectors $v_1,\ldots,v_{22}$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import roots_18_2_0
        sage: len(roots_18_2_0())
        22
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
    r"""Return the root vectors $w_1,\ldots,w_{19}$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import roots_18_0_0
        sage: len(roots_18_0_0())
        19
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
    r"""Return the five Sterk root configurations.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import sterk_roots
        sage: roots = sterk_roots()
        sage: len(roots["Sterk_4"])
        11
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
        assert len(roots) == STERK_ROOT_COUNTS[name], (
            f"{name}: expected {STERK_ROOT_COUNTS[name]} roots, built {len(roots)}"
        )
        for index, root in enumerate(roots, start=1):
            norm = bilinear_form(root, root)
            assert norm in (-2, -4), (
                f"{name} root {index} has norm {norm}; roots must have norm -2 or -4"
            )
    assert involute(v["v20"]) == v["v22"] + 2 * v["v20"], (
        "Sterk 3: the involution does not equal v22 + 2*v20"
    )
    assert involute(v["v18"]) == v["v22"] + 2 * v["v18"], (
        "Sterk 3: the involution does not equal v22 + 2*v18"
    )
    return configurations


def ten_frames() -> tuple[dict[str, Any], dict[str, Any], Any]:
    r"""Return the named basis, dual basis, and Gram matrix of $T_{En}$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import ten_frames
        sage: basis, dual, G = ten_frames()
        sage: (len(basis), len(dual), G.nrows())
        (12, 12, 12)
    """
    matrix_gram = catalogue.TEn.gram_matrix().change_ring(QQ)
    size = matrix_gram.ncols()
    assert size == 12, f"TEn should have rank 12, got {size}"

    basis = {
        name: vector(QQ, [1 if j == i else 0 for j in range(size)])
        for i, name in enumerate(_TEN_BASIS_NAMES)
    }
    dual = dict(zip(_TEN_DUAL_NAMES, matrix_gram.inverse().columns(), strict=True))

    def form(left: Any, right: Any) -> Any:
        return left * matrix_gram * right

    for i, basis_name in enumerate(_TEN_BASIS_NAMES):
        for j, dual_name in enumerate(_TEN_DUAL_NAMES):
            expected = 1 if i == j else 0
            assert form(basis[basis_name], dual[dual_name]) == expected, (
                f"TEn dual basis is wrong: <{basis_name}, {dual_name}> != {expected}"
            )
    return basis, dual, matrix_gram


def selected_isotropic_vectors() -> dict[str, Any]:
    r"""Return the five selected isotropic vectors in $T_{En}$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import selected_isotropic_vectors
        sage: len(selected_isotropic_vectors())
        5
    """
    basis, dual, matrix_gram = ten_frames()

    def form(left: Any, right: Any) -> Any:
        return left * matrix_gram * right

    omega = 2 * dual["w8"]
    alpha = 2 * dual["w1"]
    assert abs(form(omega, omega)) == 4, (
        f"omega must have absolute norm 4, got {form(omega, omega)}"
    )
    assert abs(form(alpha, alpha)) == 8, (
        f"alpha must have absolute norm 8, got {form(alpha, alpha)}"
    )

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
        assert norm == 0, f"{name} selected vector must be isotropic, has norm {norm}"
    assert len(vectors) == 5, "there are five Sterk cases, one per isotropic vector"
    return vectors


def diagonal_embedding_images() -> dict[str, Any]:
    r"""Return the diagonal images $a_i'$ and $w_i'$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import diagonal_embedding_images
        sage: len(diagonal_embedding_images())
        16
    """
    basis, dual = _frames()
    images = {f"a{i}p": basis[f"a{i}"] + basis[f"a{i}t"] for i in range(1, 9)}
    images.update({f"w{i}p": dual[f"w{i}"] + dual[f"w{i}t"] for i in range(1, 9)})

    a_primes = [images[f"a{i}p"] for i in range(1, 9)]
    induced = matrix(QQ, [[bilinear_form(x, y) for y in a_primes] for x in a_primes])
    expected = catalogue.E8_2.gram_matrix().change_ring(QQ)
    assert induced == expected, (
        "the diagonal images a_i' do not have the Gram matrix of E8(2)"
    )
    return images


def sterk5_in_U_E8_2() -> tuple[Any, tuple[Any, ...]]:
    r"""Return the Sterk 5 configuration in $U\oplus E_8(2)$.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import sterk5_in_U_E8_2
        sage: lattice, roots = sterk5_in_U_E8_2()
        sage: (lattice.rank(), len(roots))
        (10, 14)
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
    assert all(n in (-2, -4) for n in norms), (
        f"getSterk5 vectors must be roots; norms are {sorted(set(norms))}"
    )
    return lattice, vectors


def sterks_in_ten() -> dict[str, tuple[Any, ...]]:
    r"""Return three root configurations in $T_{En}$ coordinates.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import sterks_in_ten
        sage: [len(roots) for roots in sterks_in_ten().values()]
        [12, 10, 12]
    """
    basis, _, matrix_gram = ten_frames()
    e, f, ep, fp = basis["e"], basis["f"], basis["ep"], basis["fp"]
    a = {i: basis[f"a{i}"] for i in range(1, 9)}

    # The first two configurations use columns of 2G^-1.
    doubled = (2 * matrix_gram.inverse()).columns()
    ad2 = {i: doubled[i + 3] for i in range(1, 9)}

    sterks1 = tuple(a[i] for i in range(1, 9)) + (
        fp - ep,
        ad2[8] + 2 * ep,
        2 * ep + 2 * fp + ad2[1] + ad2[8],
        5 * ep + 3 * fp + 2 * ad2[2],
    )
    sterks2 = tuple(a[i] for i in range(1, 9)) + (ad2[8] + 2 * f, e - f)

    # The third configuration uses columns of G^-1.
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


def isotropic_vectors() -> dict[str, Any]:
    r"""Return the recorded isotropic vectors.

    EXAMPLES::

        sage: from dzack_research.preamble.sterk import bilinear_form, isotropic_vectors
        sage: v = isotropic_vectors()["s4_12"]
        sage: bilinear_form(v, v)
        0
    """
    v = roots_18_2_0()
    vectors = {"s4_12": v["v22"] + v["v21"]}

    for name, vector_ in vectors.items():
        norm = bilinear_form(vector_, vector_)
        assert norm == 0, (
            f"{name} was recorded as isotropic but has norm {norm}; if this changes, it may be a root and the Sterk 4 count needs revisiting"
        )
    return vectors


def gram_of(roots: tuple[Any, ...]) -> Any:
    """Return the Gram matrix of a root configuration."""
    return matrix(QQ, [[bilinear_form(x, y) for y in roots] for x in roots])
