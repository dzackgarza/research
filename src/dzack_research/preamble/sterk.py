r"""Sterk's five $0$-cusps for degree-$2$ polarized Enriques moduli.

Sterk classifies the Baily--Borel $0$-cusps by $\mathrm{O}$-orbits of
primitive isotropic vectors in $T_{\mathrm{En}}$.  Coordinates and dual
generators are those of the named catalogue lattices
(:attr:`~catalogue.Lattices.TdP`, :attr:`~catalogue.Lattices.TEn`); the
embedding chain
$T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}\hookrightarrow T_{\mathrm{dP}}
\hookrightarrow\Lambda_{K3}$ lives on :attr:`catalogue.Lattices.Embeddings`.

EXAMPLES::

    sage: from dzack_research.preamble.sterk import Sterk
    sage: {name: len(roots) for name, roots in Sterk.sterk_roots().items()}
    {'Sterk_1': 12, 'Sterk_2': 10, 'Sterk_3': 12, 'Sterk_4': 11, 'Sterk_5': 14}
"""

from __future__ import annotations

from typing import Any

from sage.rings.rational_field import QQ

from . import catalogue
from .fixtures import (
    COMPUTED_ROOT_COUNTS,
    L20_DUAL_NAMES,
    RECORDED_ROOT_MATRIX_ROWS,
    STERK_PUBLISHED,
    STERK_ROOT_COUNTS,
    TEN_DUAL_NAMES,
)
from .refine import without_element_wrap

#: Empty: the research-log Sterk section is fully ported.
NOT_PORTED: tuple[str, ...] = ()

__all__ = [
    "COMPUTED_ROOT_COUNTS",
    "NOT_PORTED",
    "RECORDED_ROOT_MATRIX_ROWS",
    "STERK_PUBLISHED",
    "STERK_ROOT_COUNTS",
    "Sterk",
]


def _named_basis(lattice: Any) -> dict[str, Any]:
    return dict(zip(lattice.variable_names(), lattice.gens(), strict=True))


def _named_dual(lattice: Any, dual_names: tuple[str, ...]) -> dict[str, Any]:
    return dict(zip(dual_names, lattice.dual_basis(), strict=True))


class Sterk:
    r"""Sterk cusp root configurations recovered from the research log.

    Embeddings of the Coble/Enriques/del Pezzo chain are
    :attr:`catalogue.Lattices.Embeddings`, not methods here.
    """

    @staticmethod
    def roots_18_2_0() -> dict[str, Any]:
        r"""Return the $22$ generating vectors $v_1,\ldots,v_{22}$ in $T_{\mathrm{dP}}$."""
        TdP = catalogue.Lattices.TdP
        with without_element_wrap():
            b = _named_basis(TdP)
            d = _named_dual(TdP, L20_DUAL_NAMES)
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
        assert len(v) == 22
        return v

    @staticmethod
    def roots_18_0_0() -> dict[str, Any]:
        r"""Return the $19$ generating vectors $w_1,\ldots,w_{19}$ in $T_{\mathrm{dP}}$."""
        TdP = catalogue.Lattices.TdP
        with without_element_wrap():
            b = _named_basis(TdP)
            d = _named_dual(TdP, L20_DUAL_NAMES)
            w = {
                "w1": b["a1"],
                "w2": b["a3"],
                "w3": b["a4"],
                "w4": b["a5"],
                "w5": b["a6"],
                "w6": b["a7"],
                "w7": b["a8"],
                "w8": b["e"] + d["w8"],
                "w9": b["f"] - b["e"],
                "w10": b["e"] + d["w8t"],
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
        assert len(w) == 19
        return w

    @staticmethod
    def sterk_roots() -> dict[str, tuple[Any, ...]]:
        r"""Return Sterk's five cusp root configurations in $T_{\mathrm{dP}}$.

        EXAMPLES::

            sage: from dzack_research.preamble.sterk import Sterk
            sage: len(Sterk.sterk_roots()["Sterk_4"])
            11
        """
        TdP = catalogue.Lattices.TdP
        v = Sterk.roots_18_2_0()
        w = Sterk.roots_18_0_0()

        def reflect(x: Any) -> Any:
            return x + QQ((1, 2)) * TdP.b(v["v22"], x) * v["v22"]

        def involute(x: Any) -> Any:
            return x + reflect(x)

        with without_element_wrap():
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
                norm = TdP.b(root, root)
                assert norm in (-2, -4), (
                    f"{name} root {index} has norm {norm}"
                )
        assert involute(v["v20"]) == v["v22"] + 2 * v["v20"]
        assert involute(v["v18"]) == v["v22"] + 2 * v["v18"]
        return configurations

    @staticmethod
    def selected_isotropic_vectors() -> dict[str, Any]:
        r"""Return Sterk's five generating isotropic lines in $T_{\mathrm{En}}$."""
        TEn = catalogue.Lattices.TEn
        with without_element_wrap():
            b = _named_basis(TEn)
            d = _named_dual(TEn, TEN_DUAL_NAMES)
            omega = 2 * d["w8"]
            alpha = 2 * d["w1"]
            assert abs(TEn.b(omega, omega)) == 4
            assert abs(TEn.b(alpha, alpha)) == 8
            e, f, ep, fp = b["e"], b["f"], b["ep"], b["fp"]
            vectors = {
                "Sterk_1": e,
                "Sterk_2": ep,
                "Sterk_3": ep + fp + omega,
                "Sterk_4": ep + 2 * fp + alpha,
                "Sterk_5": 2 * e + 2 * f + alpha,
            }
        for name, vector_ in vectors.items():
            assert TEn.b(vector_, vector_) == 0, name
        return vectors

    @staticmethod
    def diagonal_embedding() -> Any:
        r"""Return $E_8(2)\hookrightarrow T_{\mathrm{dP}}$ (AEGS diagonal).

        Alias of :attr:`catalogue.Lattices.Embeddings.E8_2_into_TdP`.
        """
        return catalogue.Lattices.Embeddings.E8_2_into_TdP

    @staticmethod
    def sterk5_in_U_E8_2() -> tuple[Any, tuple[Any, ...]]:
        r"""Return Sterk $5$'s $14$ roots inside $U\oplus E_8(2)$."""
        lattice = catalogue.Lattices.U.direct_sum(catalogue.Lattices.E8_2)
        with without_element_wrap():
            gens = list(lattice.gens())
            e, f = gens[0], gens[1]
            a = {i: gens[i + 1] for i in range(1, 9)}
            dual = lattice.dual_basis()
            ad = {i: dual[i + 1] for i in range(1, 9)}
            vectors = (
                a[2],
                a[4],
                a[5],
                a[6],
                a[7],
                a[8],
                2 * ad[8],
                2 * e + 2 * (ad[2] - ad[3]),
                f - e,
                e + f + 2 * (ad[6] - ad[3]),
                e + f + 2 * (ad[1] + ad[8] - ad[3]),
                e + f + a[3],
                a[1],
                2 * e - a[1],
            )
        assert len(vectors) == 14
        for index, v in enumerate(vectors, start=1):
            norm = lattice.b(v, v)
            assert norm in (-2, -4), f"Sterk5 vector {index} has norm {norm}"
        return lattice, vectors

    @staticmethod
    def sterks_in_ten() -> dict[str, tuple[Any, ...]]:
        r"""Return Sterk configurations $1$–$3$ in $T_{\mathrm{En}}$ coordinates."""
        TEn = catalogue.Lattices.TEn
        with without_element_wrap():
            b = _named_basis(TEn)
            e, f, ep, fp = b["e"], b["f"], b["ep"], b["fp"]
            a = {i: b[f"a{i}"] for i in range(1, 9)}
            dual = TEn.dual_basis()
            ad2 = {i: 2 * dual[i + 3] for i in range(1, 9)}
            ad1 = {i: dual[i + 3] for i in range(1, 9)}
            sterks1 = tuple(a[i] for i in range(1, 9)) + (
                fp - ep,
                2 * ep + ad2[8],
                2 * ep + 2 * fp + ad2[1] + ad2[8],
                5 * ep + 3 * fp + 2 * ad2[2],
            )
            sterks2 = tuple(a[i] for i in range(1, 9)) + (2 * f + ad2[8], e - f)
            sterks3 = tuple(a[i] for i in range(1, 8)) + (
                f - e,
                2 * fp + 2 * ad1[8],
                2 * e - 2 * fp - 2 * ad1[8],
                2 * e + 2 * (ad1[1] - ad1[8]),
                (e + f) + (a[8] - fp),
            )
        assert len(sterks1) == 12 and len(sterks2) == 10 and len(sterks3) == 12
        return {"sterks1": sterks1, "sterks2": sterks2, "sterks3": sterks3}

    @staticmethod
    def isotropic_vectors() -> dict[str, Any]:
        r"""Return the recorded isotropic cusp $s_{4,12}=v_{22}+v_{21}$."""
        TdP = catalogue.Lattices.TdP
        v = Sterk.roots_18_2_0()
        with without_element_wrap():
            s = v["v22"] + v["v21"]
        assert TdP.b(s, s) == 0
        return {"s4_12": s}
