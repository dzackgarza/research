r"""Named integral lattices used by the preamble.

Root lattices use the negative-definite convention.

One export::

    from dzack_research.preamble.catalogue import Lattices

    Lattices.U
    Lattices.LK3
    Lattices.Involutions.I_En
    Lattices.TwoElementary[8, 8, 0]
    Lattices.root_lattice("A", 2)
    Lattices.LK3_2d(3)

EXAMPLES::

    sage: from dzack_research.preamble.catalogue import Lattices
    sage: Lattices.root_lattice("A", 2).signature_pair()
    (0, 2)
    sage: Lattices.E8.rank()
    8
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.matrix.special import diagonal_matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ

from . import categories
from .fixtures import (
    K3_BASIS_NAMES,
    L20_BASIS_NAMES,
    TEN_BASIS_NAMES,
)

# Post-init hooks refine every ``IntegralLattice`` before the catalogue body runs.
categories.install()

__all__ = ["Lattices"]


def _root_lattice(
    kind: str,
    rank: int,
    names: tuple[str, ...] | None = None,
) -> Any:
    """Return the negative-definite root lattice of the given type."""
    assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
    lattice = IntegralLattice(f"{kind}{rank}").twist(-1)
    if names is not None:
        lattice._assign_names(names)
    return lattice


def _IPQ(p: int, q: int) -> Any:
    r"""Return the odd unimodular lattice $I_{p,q}$."""
    assert p >= 0 and q >= 0 and p + q > 0, f"empty signature ({p}, {q})"
    return IntegralLattice(diagonal_matrix(ZZ, [1] * p + [-1] * q))


def _assert_form_preserving(name: str, morph: Any) -> None:
    domain, codomain = morph.domain(), morph.codomain()
    for x in domain.gens():
        for y in domain.gens():
            assert domain.b(x, y) == codomain.b(morph(x), morph(y)), (
                f"{name} does not preserve the form on generators"
            )


class Lattices:
    r"""Catalogue of named integral lattices and related constructions.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import Lattices
        sage: Lattices.U.rank()
        2
        sage: Lattices.LK3.rank()
        22
        sage: D4.<alpha1, alpha2, alpha3, alpha4> = Lattices.root_lattice("D", 4)
        sage: D4.rank()
        4
        sage: Lattices.IPQ(2, 1).signature_pair()
        (2, 1)
        sage: Lattices.LK3_2d(3).rank()
        21
        sage: Lattices.TwoElementary[8, 8, 0] is Lattices.E8_2
        True
        sage: Lattices.Involutions.I_En.domain() is Lattices.LK3
        True
        sage: Lattices.Embeddings.TEn_into_TdP.matrix().dimensions()
        (12, 20)
    """

    Z = IntegralLattice(matrix(ZZ, [1]))
    Z_2 = Z.twist(2)
    H = IntegralLattice("H")
    H_2 = H.twist(2)
    U = H  # hyperbolic plane; both names were in use
    U_2 = H_2
    E6 = _root_lattice("E", 6)
    E7 = _root_lattice("E", 7)
    E8 = _root_lattice("E", 8)
    E8_2 = E8.twist(2)
    # Summand order fixes the coordinates used by the Sterk vectors.
    E10 = U + E8
    E10_2 = E10.twist(2)
    # The K3 lattice $U^3 \oplus E_8^2$.
    LK3 = U**3 + E8**2
    LK3._assign_names(K3_BASIS_NAMES)
    Sdp = U_2
    # Fine summands: $U\oplus U(2)\oplus E_8(2)$ and $U\oplus U(2)\oplus E_8^2$.
    TdP = U + U_2 + E8**2
    TdP._assign_names(L20_BASIS_NAMES)
    SEn = E10_2
    TEn = U + U_2 + E8_2
    TEn._assign_names(TEN_BASIS_NAMES)
    Tco = Z_2 + U_2 + E8_2
    Sco = Z_2.twist(-1) + U_2 + E8_2
    LpNik = U**3 + E8_2
    LmNik = E8_2
    #: Historical alias for $T_{\mathrm{dP}}$ (same object).
    L_20_2_0 = TdP
    LK3_2 = Z.twist(-2) + U**2 + E8**2
    LK3_4 = Z.twist(-4) + U**2 + E8**2

    # $\Lambda_{K3}=U\oplus U\oplus U\oplus E_8\oplus E_8$; block handles for Aut/Hom.
    _v, _uu, _up, _ea, _ep = LK3.summands()
    _c1, _c2, _c3 = Tco.summands()
    _e1, _e2, _e3 = TEn.summands()
    _d1, _d2, _d3, _d4 = TdP.summands()
    (_e8,) = E8_2.summands()

    class Involutions:
        r"""Named automorphisms of $\Lambda_{K3}$ as block Aut maps."""

    Involutions.I_dP = LK3.Aut()(
        {_v: -_v, _uu: _up, _up: _uu, _ea: -_ea, _ep: -_ep}
    )
    Involutions.I_En = LK3.Aut()(
        {_v: -_v, _uu: _up, _up: _uu, _ea: _ep, _ep: _ea}
    )
    Involutions.I_Nik = LK3.Aut()(
        {_v: _v, _uu: _uu, _up: _up, _ea: -_ep, _ep: -_ea}
    )

    class Embeddings:
        r"""Primitive embeddings
        $T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}
        \hookrightarrow T_{\mathrm{dP}}\hookrightarrow\Lambda_{K3}$.

        Block Hom columns: $(h,x,y)\mapsto(\tilde e+\tilde f,x,y,y)$, and
        $E_8(2)\hookrightarrow E_8\oplus E_8$ by $a_i\mapsto a_i+a_i^t$.
        """

    Embeddings.E8_2_into_TdP = E8_2.Hom(TdP)({_e8: _d3 + _d4})
    Embeddings.TCo_into_TEn = Tco.Hom(TEn)(
        {_c1: _e1[0] + _e1[1], _c2: _e2, _c3: _e3}
    )
    Embeddings.TEn_into_TdP = TEn.Hom(TdP)({_e1: _d1, _e2: _d2, _e3: _d3 + _d4})
    Embeddings.TEn_into_LK3 = LK3.coinvariant_inclusion(Involutions.I_En)
    Embeddings.TdP_into_LK3 = LK3.coinvariant_inclusion(Involutions.I_dP)

    #: Indexed by Nikulin invariants $(r, a, \delta)$.
    TwoElementary = {
        (1, 1, 1): Z.twist(2),
        (2, 0, 0): U,
        (2, 2, 0): U_2,
        (8, 0, 0): E8,
        (8, 8, 0): E8_2,
        (10, 8, 0): U + E8_2,
        (10, 10, 0): E10_2,
        (12, 10, 0): TEn,
        (14, 8, 0): LpNik,
        (18, 0, 0): U + E8**2,
        (18, 2, 0): U_2 + E8**2,
        (20, 2, 0): TdP,
    }

    root_lattice = staticmethod(_root_lattice)
    IPQ = staticmethod(_IPQ)

    @staticmethod
    def LK3_2d(degree: int) -> Any:
        r"""Return $\langle -2d\rangle \oplus U^2 \oplus E_8^2$."""
        assert degree >= 1, f"degree must be positive, got {degree}"
        return Lattices.Z.twist(-2 * degree) + Lattices.U**2 + Lattices.E8**2

    @staticmethod
    def namespace() -> dict[str, Any]:
        """Return the named lattices and root-lattice families."""
        names = {
            name: value
            for name, value in vars(Lattices).items()
            if not name.startswith("_") and hasattr(value, "gram_matrix")
        }
        names.update({f"A{n}": _root_lattice("A", n) for n in range(1, 22)})
        names.update({f"D{n}": _root_lattice("D", n) for n in range(2, 23)})
        return names


for _name, _morph in (
    ("E8_2_into_TdP", Lattices.Embeddings.E8_2_into_TdP),
    ("TCo_into_TEn", Lattices.Embeddings.TCo_into_TEn),
    ("TEn_into_TdP", Lattices.Embeddings.TEn_into_TdP),
    ("TEn_into_LK3", Lattices.Embeddings.TEn_into_LK3),
    ("TdP_into_LK3", Lattices.Embeddings.TdP_into_LK3),
):
    _assert_form_preserving(_name, _morph)

del _name, _morph
