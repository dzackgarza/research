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
from sage.matrix.special import diagonal_matrix, identity_matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ

from .categories.integral_lattices import refine_one_lattice
from .fixtures import (
    K3_BASIS_NAMES,
    L20_BASIS_NAMES,
    TEN_BASIS_NAMES,
)

__all__ = ["Lattices"]


def _root_lattice(
    kind: str,
    rank: int,
    names: tuple[str, ...] | None = None,
) -> Any:
    """Return the negative-definite root lattice of the given type."""
    assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
    lattice = IntegralLattice(f"{kind}{rank}")
    refine_one_lattice(lattice)
    lattice = lattice.twist(-1)
    if names is not None:
        lattice._assign_names(names)
    return lattice


def _IPQ(p: int, q: int) -> Any:
    r"""Return the odd unimodular lattice $I_{p,q}$."""
    assert p >= 0 and q >= 0 and p + q > 0, f"empty signature ({p}, {q})"
    lattice = IntegralLattice(diagonal_matrix(ZZ, [1] * p + [-1] * q))
    refine_one_lattice(lattice)
    return lattice


def _integral(data: Any) -> Any:
    lattice = IntegralLattice(data)
    refine_one_lattice(lattice)
    return lattice


def _with_names(lattice: Any, names: tuple[str, ...]) -> Any:
    lattice._assign_names(names)
    return lattice


def _involutions(LK3: Any) -> type:
    """Named automorphisms of ``LK3`` as a namespace class."""
    gens = tuple(LK3.gens())
    assert len(gens) == len(K3_BASIS_NAMES) == 22
    v1, v2, u1, u2, up1, up2, *rest = gens
    e, ep = rest[:8], rest[8:]

    class Involutions:
        I_dP = LK3.Aut()(
            {
                v1: -v1,
                v2: -v2,
                u1: up1,
                u2: up2,
                up1: u1,
                up2: u2,
                **{ei: -ei for ei in e},
                **{epi: -epi for epi in ep},
            }
        )
        I_En = LK3.Aut()(
            {
                v1: -v1,
                v2: -v2,
                u1: up1,
                u2: up2,
                up1: u1,
                up2: u2,
                **{ei: epi for ei, epi in zip(e, ep, strict=True)},
                **{epi: ei for ei, epi in zip(e, ep, strict=True)},
            }
        )
        I_Nik = LK3.Aut()(
            {
                v1: v1,
                v2: v2,
                u1: u1,
                u2: u2,
                up1: up1,
                up2: up2,
                **{ei: -epi for ei, epi in zip(e, ep, strict=True)},
                **{epi: -ei for ei, epi in zip(e, ep, strict=True)},
            }
        )

    Involutions.__qualname__ = "Lattices.Involutions"
    Involutions.__name__ = "Involutions"
    return Involutions


def _coinvariant_inclusion(LK3: Any, involution: Any, domain: Any) -> Any:
    r"""Return the inclusion of ``domain`` as the $-1$-eigenspace of ``involution``.

    The default right-kernel basis of $I+\mathrm{id}$ induces exactly the Gram
    matrix of ``domain`` (the named $T_{\mathrm{En}}$ / $T_{\mathrm{dP}}$), so
    generator $i$ maps to that basis vector in $\Lambda_{K3}$.
    """
    mat = involution.matrix()
    size = LK3.rank()
    basis = list((mat + identity_matrix(ZZ, size)).right_kernel().basis())
    assert len(basis) == domain.rank(), (
        f"coinvariant rank {len(basis)} != domain rank {domain.rank()}"
    )
    images = [LK3(list(row)) for row in basis]
    return domain.Hom(LK3)(images)


def _embeddings(
    Tco: Any,
    TEn: Any,
    TdP: Any,
    E8_2: Any,
    LK3: Any,
    involutions: type,
) -> type:
    r"""Primitive embeddings $T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}
    \hookrightarrow T_{\mathrm{dP}}\hookrightarrow\Lambda_{K3}$.

    Generator images follow the source / AEGS diagonal and
    ``lem:sequence_of_embeddings``: $(h,x,y)\mapsto(\tilde e+\tilde f,x,y,y)$.
    """
    # $T_{\mathrm{En}}=U\oplus U(2)\oplus E_8(2)$, $T_{\mathrm{dP}}=U\oplus U(2)\oplus E_8^2$.
    ten = list(TEn.gens())
    tdp = list(TdP.gens())
    assert len(ten) == 12 and len(tdp) == 20
    # id on $U\oplus U(2)$; $a_i\mapsto a_i+a_i^t$ on the $E_8(2)$ summand.
    ten_into_tdp_images = tdp[:4] + [tdp[i] + tdp[i + 8] for i in range(4, 12)]
    e8_diag_images = [tdp[i] + tdp[i + 8] for i in range(4, 12)]

    # $T_{\mathrm{Co}}=\langle 2\rangle\oplus E_{10}(2)\hookrightarrow T_{\mathrm{En}}$:
    # $h\mapsto e+f$, then the $E_{10}(2)$ summand identically.
    tco = list(Tco.gens())
    assert len(tco) == 11
    e, f = ten[0], ten[1]
    tco_into_ten_images = [e + f] + ten[2:]

    class Embeddings:
        E8_2_into_TdP = E8_2.Hom(TdP)(e8_diag_images)
        TCo_into_TEn = Tco.Hom(TEn)(tco_into_ten_images)
        TEn_into_TdP = TEn.Hom(TdP)(ten_into_tdp_images)
        TEn_into_LK3 = _coinvariant_inclusion(LK3, involutions.I_En, TEn)
        TdP_into_LK3 = _coinvariant_inclusion(LK3, involutions.I_dP, TdP)

    for name, morph in (
        ("E8_2_into_TdP", Embeddings.E8_2_into_TdP),
        ("TCo_into_TEn", Embeddings.TCo_into_TEn),
        ("TEn_into_TdP", Embeddings.TEn_into_TdP),
        ("TEn_into_LK3", Embeddings.TEn_into_LK3),
        ("TdP_into_LK3", Embeddings.TdP_into_LK3),
    ):
        domain, codomain = morph.domain(), morph.codomain()
        for x in domain.gens():
            for y in domain.gens():
                assert domain.b(x, y) == codomain.b(morph(x), morph(y)), (
                    f"{name} does not preserve the form on generators"
                )

    Embeddings.__qualname__ = "Lattices.Embeddings"
    Embeddings.__name__ = "Embeddings"
    return Embeddings


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

    Z = _integral(matrix(ZZ, [1]))
    Z_2 = Z.twist(2)
    H = _integral("H")
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
    LK3 = _with_names(U**3 + E8**2, K3_BASIS_NAMES)
    Sdp = U_2
    # AEGS bases: $T_{\mathrm{dP}}\cong U\oplus U(2)\oplus E_8^2$, $T_{\mathrm{En}}\cong U\oplus E_{10}(2)$.
    TdP = _with_names(U + U_2 + E8**2, L20_BASIS_NAMES)
    SEn = E10_2
    TEn = _with_names(U + E10_2, TEN_BASIS_NAMES)
    Tco = Z_2 + E10_2
    Sco = Z_2.twist(-1) + E10_2
    LpNik = U**3 + E8_2
    LmNik = E8_2
    #: Historical alias for $T_{\mathrm{dP}}$ (same object).
    L_20_2_0 = TdP
    LK3_2 = Z.twist(-2) + U**2 + E8**2
    LK3_4 = Z.twist(-4) + U**2 + E8**2
    Involutions = _involutions(LK3)
    Embeddings = _embeddings(Tco, TEn, TdP, E8_2, LK3, Involutions)

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
