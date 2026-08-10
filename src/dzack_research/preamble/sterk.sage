r"""Sterk's five $0$-cusps for degree-$2$ polarized Enriques moduli.

Sterk classifies the Baily--Borel $0$-cusps by $\mathrm{O}$-orbits of
primitive isotropic vectors in $T_{\mathrm{En}}$.  Coordinates and dual
module_generators are those of the named catalogue lattices
(:attr:`~Lattices.TdP`, :attr:`~Lattices.TEn`); the
embedding chain
$T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}\hookrightarrow T_{\mathrm{dP}}
\hookrightarrow\Lambda_{K3}$ lives on :attr:`Embeddings`.

EXAMPLES::

    sage: from dzack_research.preamble.sterk import Sterk
    sage: {name: len(roots) for name, roots in Sterk.sterk_roots().items()}
    {'Sterk_1': 12, 'Sterk_2': 10, 'Sterk_3': 12, 'Sterk_4': 11, 'Sterk_5': 14}
"""

from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import _integral_lattice_with_names
from dzack_research.preamble.catalogue import Lattices
from typing import Any, TYPE_CHECKING

from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


NOT_PORTED: tuple[str, ...] = ()

__all__ = [
    "NOT_PORTED",
    "Sterk",
    "SterkDiagrams",
]

_STERK_DIAGRAM_LAYOUTS: dict[str, dict[int, list[float]]] = {
    "Sterk_1": {
        0: [0, 0],
        1: [4, 0],
        2: [8, 0],
        3: [8, -4],
        4: [8, -8],
        5: [4, -8],
        6: [0, -8],
        7: [0, -4],
        8: [2, -6],
        9: [3.25, -4.75],
        10: [4.5, -3.5],
        11: [6, -2],
    },
    "Sterk_2": {
        0: [0, 0],
        1: [-4, 0],
        2: [-8, 0],
        3: [-7, 4],
        4: [-6, 8],
        5: [-5, 12],
        6: [-4, 16],
        7: [-3, 20],
        8: [-2, 24],
        9: [-2, 6],
    },
    "Sterk_3": {
        0: [0, -4],
        1: [0, 4],
        2: [0, 8],
        3: [0, 12],
        4: [0, 16],
        5: [4, 16],
        6: [8, 16],
        7: [12, 16],
        8: [20, 16],
        9: [4, 12],
        10: [6, 2],
        11: [14, 10],
    },
    "Sterk_4": {
        0: [0, 0],
        1: [0, 4],
        2: [0, 8],
        3: [4, 8],
        4: [8, 8],
        5: [12, 8],
        6: [16, 8],
        7: [16, 4],
        8: [16, 0],
        9: [4, 4],
        10: [12, 4],
    },
    "Sterk_5": {
        0: [0, 0],
        1: [10, 0],
        2: [20, 0],
        3: [20, -10],
        4: [20, -20],
        5: [10, -20],
        6: [0, -20],
        7: [0, -10],
        8: [4, -4],
        9: [16, -4],
        10: [16, -16],
        11: [4, -16],
        12: [8, -8],
        13: [8, -12],
    },
}


def _named_module_generators(lattice: "Lattice") -> dict[str, "ModuleElement"]:
    return dict(
        zip(lattice.variable_names(), lattice.module_generators(), strict=True)
    )


def _in_dual(lattice: "Lattice") -> "Module":
    r"""Return $c: L\to L^\vee$, for writing a vector the way the literature does.

    Sterk's vectors are written as sums of generators and
    dual generators --
    $e'+f'+w_1+\tilde w_8$ -- which is arithmetic in $L\otimes\mathbb Q$ with
    $L\subseteq L^\vee$ left understood.  Here that inclusion is $c$: the sum
    happens in $L^\vee$, with the module_generating vectors carried over by $c$, and
    ``c.lift`` names the element of $L$ it turns out to be.  When it is not one
    -- when the sum is not in $c(L)$ -- there is no such element and the lift
    says so instead of returning a rational vector nobody checked.
    """
    return lattice.correlation()


class Sterk:
    r"""Sterk cusp root configurations recovered from the research log.

    Embeddings of the Coble/Enriques/del Pezzo chain are
    :attr:`Embeddings`, not methods here.
    """

    @staticmethod
    def roots_18_2_0() -> dict[str, Any]:
        r"""Return the $22$ generating vectors $v_1,\ldots,v_{22}$ in $T_{\mathrm{dP}}$."""
        TdP = Lattices.TdP
        b = _named_module_generators(TdP)
        (
            eb, fb, epb, fpb,
            w1, w2, w3, w4, w5, w6, w7, w8,
            w1t, w2t, w3t, w4t, w5t, w6t, w7t, w8t,
        ) = TdP.dual_lattice().module_generators()
        c = _in_dual(TdP)
        v = {
            "v1": b["a8t"],
            "v2": c.lift(c(b["ep"] + b["fp"]) + w1 + w8t),
            "v3": b["a1"],
            "v4": b["a3"],
            "v5": b["a4"],
            "v6": b["a5"],
            "v7": b["a6"],
            "v8": b["a7"],
            "v9": b["a8"],
            "v10": c.lift(c(b["ep"] + b["fp"]) + w8 + w1t),
            "v11": b["a1t"],
            "v12": b["a3t"],
            "v13": b["a4t"],
            "v14": b["a5t"],
            "v15": b["a6t"],
            "v16": b["a7t"],
            "v17": c.lift(c(b["ep"]) + w8t),
            "v18": b["a2"],
            "v19": c.lift(c(b["ep"]) + w8),
            "v20": b["a2t"],
            "v21": b["fp"] - b["ep"],
            "v22": c.lift(c(5 * b["ep"] + 3 * b["fp"]) + 2 * w2 + 2 * w2t),
        }
        assert len(v) == 22
        return v

    @staticmethod
    def roots_18_0_0() -> dict[str, Any]:
        r"""Return the $19$ generating vectors $w_1,\ldots,w_{19}$ in $T_{\mathrm{dP}}$."""
        TdP = Lattices.TdP
        b = _named_module_generators(TdP)
        (
            eb, fb, epb, fpb,
            w1, w2, w3, w4, w5, w6, w7, w8,
            w1t, w2t, w3t, w4t, w5t, w6t, w7t, w8t,
        ) = TdP.dual_lattice().module_generators()
        c = _in_dual(TdP)
        w = {
            "w1": b["a1"],
            "w2": b["a3"],
            "w3": b["a4"],
            "w4": b["a5"],
            "w5": b["a6"],
            "w6": b["a7"],
            "w7": b["a8"],
            "w8": c.lift(c(b["e"]) + w8),
            "w9": b["f"] - b["e"],
            "w10": c.lift(c(b["e"]) + w8t),
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
        TdP = Lattices.TdP
        v = Sterk.roots_18_2_0()
        w = Sterk.roots_18_0_0()

        def reflect(x: "ModuleElement") -> "ModuleElement":
            # The coefficient is $b(v_{22},x)/2$, and it has to be an integer
            # for the result to be in the lattice at all -- which it is
            # because $v_{22}$ has even pairings.  Taken in $\mathbb Z$, so
            # that a lattice element is scaled by a scalar of its own ring and
            # a pairing that ever came out odd says so here.
            half = SageZZ(v["v22"].b(x) / 2)
            return x + half * v["v22"]

        def involute(x: "ModuleElement") -> "ModuleElement":
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
        TEn = Lattices.TEn
        b = _named_module_generators(TEn)
        ed, fd, epd, fpd, w1, w2, w3, w4, w5, w6, w7, w8 = (
            TEn.dual_lattice().module_generators()
        )
        c = _in_dual(TEn)
        omega = 2 * w8
        alpha = 2 * w1
        assert abs(omega.b(omega)) == 4
        assert abs(alpha.b(alpha)) == 8
        e, f, ep, fp = b["e"], b["f"], b["ep"], b["fp"]
        vectors = {
            "Sterk_1": e,
            "Sterk_2": ep,
            "Sterk_3": c.lift(c(ep + fp) + omega),
            "Sterk_4": c.lift(c(ep + 2 * fp) + alpha),
            "Sterk_5": c.lift(c(2 * e + 2 * f) + alpha),
        }
        for name, vector_ in vectors.items():
            assert vector_.q() == 0, name
        return vectors

    @staticmethod
    def diagonal_embedding() -> "ModuleMorphism":
        r"""Return $E_8(2)\hookrightarrow T_{\mathrm{dP}}$ (AEGS diagonal).

        Alias of :attr:`Embeddings.E8_2_into_TdP`.
        """
        return Embeddings.E8_2_into_TdP

    @staticmethod
    def sterk5_in_U_E8_2() -> tuple[Any, tuple[Any, ...]]:
        r"""Return Sterk $5$'s $14$ roots inside $U\oplus E_8(2)$."""
        lattice = Lattices.U.direct_sum([Lattices.E8_2])
        module_generators = list(lattice.module_generators())
        e, f = module_generators[0], module_generators[1]
        a = {i: module_generators[i + 1] for i in range(1, 9)}
        dual = lattice.dual_lattice().module_generators()
        ad = {i: dual[i + 1] for i in range(1, 9)}
        c = _in_dual(lattice)
        vectors = (
            a[2],
            a[4],
            a[5],
            a[6],
            a[7],
            a[8],
            c.lift(2 * ad[8]),
            c.lift(c(2 * e) + 2 * (ad[2] - ad[3])),
            f - e,
            c.lift(c(e + f) + 2 * (ad[6] - ad[3])),
            c.lift(c(e + f) + 2 * (ad[1] + ad[8] - ad[3])),
            e + f + a[3],
            a[1],
            2 * e - a[1],
        )
        assert len(vectors) == 14
        for index, v in enumerate(vectors, start=1):
            norm = v.q()
            assert norm in (-2, -4), f"Sterk5 vector {index} has norm {norm}"
        return lattice, vectors

    @staticmethod
    def sterks_in_ten() -> dict[str, tuple[Any, ...]]:
        r"""Return Sterk configurations $1$–$3$ in $T_{\mathrm{En}}$ coordinates."""
        TEn = Lattices.TEn
        b = _named_module_generators(TEn)
        e, f, ep, fp = b["e"], b["f"], b["ep"], b["fp"]
        a = {i: b[f"a{i}"] for i in range(1, 9)}
        dual = TEn.dual_lattice().module_generators()
        ad2 = {i: 2 * dual[i + 3] for i in range(1, 9)}
        ad1 = {i: dual[i + 3] for i in range(1, 9)}
        c = _in_dual(TEn)
        sterks1 = tuple(a[i] for i in range(1, 9)) + (
            fp - ep,
            c.lift(c(2 * ep) + ad2[8]),
            c.lift(c(2 * ep + 2 * fp) + ad2[1] + ad2[8]),
            c.lift(c(5 * ep + 3 * fp) + 2 * ad2[2]),
        )
        sterks2 = tuple(a[i] for i in range(1, 9)) + (
            c.lift(c(2 * f) + ad2[8]),
            e - f,
        )
        sterks3 = tuple(a[i] for i in range(1, 8)) + (
            f - e,
            c.lift(c(2 * fp) + 2 * ad1[8]),
            c.lift(c(2 * e - 2 * fp) - 2 * ad1[8]),
            c.lift(c(2 * e) + 2 * (ad1[1] - ad1[8])),
            (e + f) + (a[8] - fp),
        )
        assert len(sterks1) == 12 and len(sterks2) == 10 and len(sterks3) == 12
        return {"sterks1": sterks1, "sterks2": sterks2, "sterks3": sterks3}

    @staticmethod
    def isotropic_vectors() -> dict[str, Any]:
        r"""Return the recorded isotropic cusp $s_{4,12}=v_{22}+v_{21}$."""
        TdP = Lattices.TdP
        v = Sterk.roots_18_2_0()
        s = v["v22"] + v["v21"]
        assert TdP.b(s, s) == 0
        return {"s4_12": s}


def _sterk_diagram(name: str, roots: "OrderedSet") -> "Graph":
    r"""Construct one named Sterk diagram from actual roots in ``Lattices.TdP``."""
    # The roots are elements of TdP already: they were built from its
    # module_generators.  Reading them as coordinates was a recast that only made
    # sense while a lattice element was an integer vector.
    rooted = tuple(roots)
    positions = {
        index: tuple(coordinates)
        for index, coordinates in _STERK_DIAGRAM_LAYOUTS[name].items()
    }
    return FiniteCoxeterDiagram.from_roots(
        rooted,
        # Identifier names; Sage derives the LaTeX form r_{i} itself
        # (``latex_variable_names``) — brace-form names fail ``certify_names``.
        names=tuple(f"r_{index + 1}" for index in range(len(rooted))),
        positions=positions,
    )


_STERK_ROOTS = Sterk.sterk_roots()


class SterkDiagrams:
    r"""Sterk's five rooted Coxeter diagrams."""

    Sterk_1 = _sterk_diagram("Sterk_1", _STERK_ROOTS["Sterk_1"])
    Sterk_2 = _sterk_diagram("Sterk_2", _STERK_ROOTS["Sterk_2"])
    Sterk_3 = _sterk_diagram("Sterk_3", _STERK_ROOTS["Sterk_3"])
    Sterk_4 = _sterk_diagram("Sterk_4", _STERK_ROOTS["Sterk_4"])
    Sterk_5 = _sterk_diagram("Sterk_5", _STERK_ROOTS["Sterk_5"])
