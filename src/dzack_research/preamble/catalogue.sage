r"""Named integral lattices used by the preamble.

Root lattices use the negative-definite convention.

Requires category installation first (``install_integral_lattices``), so that
generator sugar ``L.<gens> = ...`` works for the lattices that use it.

Call :meth:`Lattices.install` (``init.sage`` does this) to bind specimens and
the $\Lambda_{K3}$ generators into the session namespace.

``TwoElementary`` is Nikulin's table of 75 even indefinite 2-elementary
lattices of signature $(1,r-1)$, keyed by $(r,a,\delta)$.
"""

from sage.matrix.constructor import matrix
from sage.matrix.special import diagonal_matrix
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
    IntegralLattice,
)
from sage.rings.integer_ring import ZZ

__all__ = ["Embeddings", "Involutions", "Lattices", "TwoElementary"]


class Lattices:
    r"""Catalogue of named integral lattices.

    Most specimens are plain lattice objects.  Lattices that the session treats
    as named bases ($\Lambda_{K3}$, $T_{\mathrm{En}}$, $T_{\mathrm{dP}}$) use
    ``L.<gens> = ...``.  :meth:`install` binds every specimen attribute into the
    notebook namespace and injects the named generators.
    """

    Z = IntegralLattice(matrix(ZZ, [1]))
    Z_2 = Z.twist(2)

    H = IntegralLattice("H")
    H_2 = H.twist(2)
    U = H
    U_2 = H_2

    A1 = IntegralLattice("A1").twist(-1)
    A2 = IntegralLattice("A2").twist(-1)
    A3 = IntegralLattice("A3").twist(-1)
    A4 = IntegralLattice("A4").twist(-1)
    A5 = IntegralLattice("A5").twist(-1)
    A6 = IntegralLattice("A6").twist(-1)
    A7 = IntegralLattice("A7").twist(-1)
    A8 = IntegralLattice("A8").twist(-1)
    A9 = IntegralLattice("A9").twist(-1)
    A10 = IntegralLattice("A10").twist(-1)
    A11 = IntegralLattice("A11").twist(-1)
    A12 = IntegralLattice("A12").twist(-1)
    A13 = IntegralLattice("A13").twist(-1)
    A14 = IntegralLattice("A14").twist(-1)
    A15 = IntegralLattice("A15").twist(-1)
    A16 = IntegralLattice("A16").twist(-1)
    A17 = IntegralLattice("A17").twist(-1)
    A18 = IntegralLattice("A18").twist(-1)
    A19 = IntegralLattice("A19").twist(-1)
    A20 = IntegralLattice("A20").twist(-1)
    A21 = IntegralLattice("A21").twist(-1)

    D2 = IntegralLattice("D2").twist(-1)
    D3 = IntegralLattice("D3").twist(-1)
    D4 = IntegralLattice("D4").twist(-1)
    D5 = IntegralLattice("D5").twist(-1)
    D6 = IntegralLattice("D6").twist(-1)
    D7 = IntegralLattice("D7").twist(-1)
    D8 = IntegralLattice("D8").twist(-1)
    D9 = IntegralLattice("D9").twist(-1)
    D10 = IntegralLattice("D10").twist(-1)
    D11 = IntegralLattice("D11").twist(-1)
    D12 = IntegralLattice("D12").twist(-1)
    D13 = IntegralLattice("D13").twist(-1)
    D14 = IntegralLattice("D14").twist(-1)
    D15 = IntegralLattice("D15").twist(-1)
    D16 = IntegralLattice("D16").twist(-1)
    D17 = IntegralLattice("D17").twist(-1)
    D18 = IntegralLattice("D18").twist(-1)
    D19 = IntegralLattice("D19").twist(-1)
    D20 = IntegralLattice("D20").twist(-1)
    D21 = IntegralLattice("D21").twist(-1)
    D22 = IntegralLattice("D22").twist(-1)

    E6 = IntegralLattice("E6").twist(-1)
    E7 = IntegralLattice("E7").twist(-1)
    E8 = IntegralLattice("E8").twist(-1)
    E8_2 = E8.twist(2)

    E10 = U @ E8
    E10_2 = U_2 @ E8_2

    Sdp = U_2
    SEn = E10_2
    Tco = Z_2 @ U_2 @ E8_2
    Sco = Z_2.twist(-1) @ U_2 @ E8_2
    LpNik = U**3 @ E8_2
    LmNik = E8_2
    LK3_2 = Z.twist(-2) @ U**2 @ E8**2
    LK3_4 = Z.twist(-4) @ U**2 @ E8**2

    # Named bases — matching the old init.sage session.
    LK3.<v1, v2, u1, u2, up1, up2, e1, ..., e8, ep1, ..., ep8> = (U**3).direct_sum(E8**2)
    TEn.<e, f, ep, fp, a1, ..., a8> = U.direct_sum(E10_2)
    TdP.<e, f, ep, fp, a1, ..., a8, a1t, ..., a8t> = U.direct_sum(U_2, E8, E8)
    L_20_2_0 = TdP

    @staticmethod
    def root_lattice(kind, rank):
        """Return the negative-definite root lattice of the given type."""
        assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
        return getattr(Lattices, f"{kind}{rank}")

    @staticmethod
    def IPQ(p, q):
        r"""Return the odd unimodular lattice $I_{p,q}$."""
        assert p >= 0 and q >= 0 and p + q > 0, f"empty signature ({p}, {q})"
        return IntegralLattice(diagonal_matrix(ZZ, [1] * p + [-1] * q))

    @staticmethod
    def LK3_2d(degree):
        r"""Return $\langle -2d\rangle \oplus U^2 \oplus E_8^2$."""
        assert degree >= 1, f"degree must be positive, got {degree}"
        return Lattices.Z.twist(-2 * degree) @ Lattices.U**2 @ Lattices.E8**2

    @classmethod
    def install(cls, scope=None):
        r"""Bind catalogue specimens and named generators into *scope*."""
        if scope is None:
            import inspect

            frame = inspect.currentframe()
            try:
                assert frame is not None and frame.f_back is not None
                scope = frame.f_back.f_globals
            finally:
                del frame

        for name, obj in vars(cls).items():
            if isinstance(obj, FreeQuadraticModule_integer_symmetric):
                scope[name] = obj

        scope.update(
            I_dP=Involutions.I_dP,
            I_En=Involutions.I_En,
            I_Nik=Involutions.I_Nik,
        )

        # Shared short names: inject TdP after TEn so session ``e`` is TdP's.
        cls.TEn.inject_variables(scope)
        cls.TdP.inject_variables(scope)
        cls.LK3.inject_variables(scope)

        ed, fd, epd, fpd, w1, w2, w3, w4, w5, w6, w7, w8 = cls.TEn.dual_basis()
        scope.update(
            ed=ed, fd=fd, epd=epd, fpd=fpd,
            w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8,
        )

        (
            eb, fb, epb, fpb,
            w1, w2, w3, w4, w5, w6, w7, w8,
            w1t, w2t, w3t, w4t, w5t, w6t, w7t, w8t,
        ) = cls.TdP.dual_basis()
        scope.update(
            eb=eb, fb=fb, epb=epb, fpb=fpb,
            w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8,
            w1t=w1t, w2t=w2t, w3t=w3t, w4t=w4t,
            w5t=w5t, w6t=w6t, w7t=w7t, w8t=w8t,
        )


# Nikulin's 75 even indefinite 2-elementary lattices of signature $(1,r-1)$,
# keyed by $(r,a,\delta)$.  Source: Nikulin (1979); Alexeev–Engel–et al.,
# arXiv:2208.10383 Fig. 1.  Hyperbolic constructions from the standard
# building blocks are filled; the rest are ``None``.
TwoElementary = {
        (1, 1, 1): Lattices.Z.twist(2),
        (2, 0, 0): Lattices.U,
        (2, 2, 0): Lattices.U_2,
        (2, 2, 1): None,
        (3, 1, 1): Lattices.U @ Lattices.A1,
        (3, 3, 1): Lattices.U_2 @ Lattices.A1,
        (4, 2, 1): Lattices.U @ Lattices.A1**2,
        (4, 4, 1): Lattices.U_2 @ Lattices.A1**2,
        (5, 3, 1): None,
        (5, 5, 1): None,
        (6, 2, 0): Lattices.U @ Lattices.D4,
        (6, 4, 0): Lattices.U_2 @ Lattices.D4,
        (6, 4, 1): None,
        (6, 6, 1): None,
        (7, 3, 1): None,
        (7, 5, 1): Lattices.U_2 @ Lattices.A1 @ Lattices.D4,
        (7, 7, 1): None,
        (8, 2, 1): Lattices.U @ Lattices.D6,
        (8, 4, 1): Lattices.U_2 @ Lattices.D6,
        (8, 6, 1): Lattices.U_2 @ Lattices.A1**2 @ Lattices.D4,
        (8, 8, 1): None,
        (9, 1, 1): Lattices.U @ Lattices.E7,
        (9, 3, 1): Lattices.U_2 @ Lattices.E7,
        (9, 5, 1): Lattices.U_2 @ Lattices.A1 @ Lattices.D6,
        (9, 7, 1): None,
        (9, 9, 1): None,
        (10, 0, 0): Lattices.E10,
        (10, 2, 0): Lattices.U @ Lattices.D8,
        (10, 2, 1): None,
        (10, 4, 0): Lattices.U_2 @ Lattices.D8,
        (10, 4, 1): None,
        (10, 6, 0): Lattices.U_2 @ Lattices.D4**2,
        (10, 6, 1): None,
        (10, 8, 0): Lattices.U @ Lattices.E8_2,
        (10, 8, 1): None,
        (10, 10, 0): Lattices.E10_2,
        (10, 10, 1): None,
        (11, 1, 1): None,
        (11, 3, 1): None,
        (11, 5, 1): None,
        (11, 7, 1): None,
        (11, 9, 1): Lattices.U @ Lattices.A1 @ Lattices.E8_2,
        (11, 11, 1): Lattices.U_2 @ Lattices.A1 @ Lattices.E8_2,
        (12, 2, 1): None,
        (12, 4, 1): None,
        (12, 6, 1): Lattices.U_2 @ Lattices.D4 @ Lattices.D6,
        (12, 8, 1): None,
        (12, 10, 1): Lattices.U @ Lattices.A1**2 @ Lattices.E8_2,
        (13, 3, 1): None,
        (13, 5, 1): Lattices.U_2 @ Lattices.D4 @ Lattices.E7,
        (13, 7, 1): None,
        (13, 9, 1): None,
        (14, 2, 0): Lattices.U @ Lattices.D4 @ Lattices.E8,
        (14, 4, 0): Lattices.U @ Lattices.D4 @ Lattices.D8,
        (14, 4, 1): None,
        (14, 6, 0): Lattices.U_2 @ Lattices.D4 @ Lattices.D8,
        (14, 6, 1): Lattices.U_2 @ Lattices.D6**2,
        (14, 8, 1): None,
        (15, 3, 1): None,
        (15, 5, 1): Lattices.U_2 @ Lattices.D6 @ Lattices.E7,
        (15, 7, 1): None,
        (16, 2, 1): Lattices.U @ Lattices.D6 @ Lattices.E8,
        (16, 4, 1): Lattices.U @ Lattices.D6 @ Lattices.D8,
        (16, 6, 1): Lattices.U_2 @ Lattices.D6 @ Lattices.D8,
        (17, 1, 1): Lattices.U @ Lattices.E7 @ Lattices.E8,
        (17, 3, 1): Lattices.U @ Lattices.D8 @ Lattices.E7,
        (17, 5, 1): Lattices.U_2 @ Lattices.D8 @ Lattices.E7,
        (18, 0, 0): Lattices.U @ Lattices.E8**2,
        (18, 2, 0): Lattices.U @ Lattices.D8 @ Lattices.E8,
        (18, 2, 1): None,
        (18, 4, 0): Lattices.U @ Lattices.D8**2,
        (18, 4, 1): None,
        (19, 1, 1): None,
        (19, 3, 1): None,
        (20, 2, 1): None,
}


class Involutions:
    r"""Named automorphisms of $\Lambda_{K3}$ as block Aut maps."""

    v, uu, up, ea, ep = Lattices.LK3.summands()

    I_dP = Lattices.LK3.Aut()({v: -v, uu: up, up: uu, ea: -ea, ep: -ep})
    I_En = Lattices.LK3.Aut()({v: -v, uu: up, up: uu, ea: ep, ep: ea})
    I_Nik = Lattices.LK3.Aut()({v: v, uu: uu, up: up, ea: -ep, ep: -ea})


class Embeddings:
    r"""Primitive embeddings
    $T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}
    \hookrightarrow T_{\mathrm{dP}}\hookrightarrow\Lambda_{K3}$.
    """

    c1, c2, c3 = Lattices.Tco.summands()
    e1, e2, e3 = Lattices.TEn.summands()
    d1, d2, d3, d4 = Lattices.TdP.summands()
    (e8,) = Lattices.E8_2.summands()

    E8_2_into_TdP = Lattices.E8_2.Hom(Lattices.TdP)({e8: d3 + d4})
    TCo_into_TEn = Lattices.Tco.Hom(Lattices.TEn)(
        {c1: e1[0] + e1[1], c2: e2, c3: e3}
    )
    TEn_into_TdP = Lattices.TEn.Hom(Lattices.TdP)({e1: d1, e2: d2, e3: d3 + d4})
    TEn_into_LK3 = Lattices.LK3.coinvariant_inclusion(Involutions.I_En)
    TdP_into_LK3 = Lattices.LK3.coinvariant_inclusion(Involutions.I_dP)
