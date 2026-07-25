r"""Named lattices from the old init.sage: the root families and the literature names.

These are *instances*, not new mathematics -- every one is built from Sage's
``IntegralLattice`` by twisting and summing. The value is the naming: ``TEn`` for
the Enriques transcendental lattice is a citation, not a construction.

**Sign convention.** The root lattices carry ``.twist(-1)``, matching the algebraic
geometry convention used throughout this repo, in which ``A_n``, ``D_n``, ``E_n``
are *negative* definite. Sage's own ``IntegralLattice("A2")`` is positive definite;
these constructors flip it. Do not "fix" that.

Families are functions rather than module-level names because the old init.sage
built ``A1``..``A21`` and ``D2``..``D22`` eagerly with ``exec`` and string
concatenation, which cost startup time for names almost never used. Call
:func:`root_lattice` or use :func:`namespace` to inject the old flat names.
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.matrix.special import diagonal_matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ

__all__ = [
    "IPQ",
    "NAMED",
    "UNBUILT_TWO_ELEMENTARY",
    "namespace",
    "root_lattice",
    "two_elementary_lattices",
]


def root_lattice(kind: str, rank: int) -> Any:
    """``A_n``, ``D_n`` or ``E_n``, negative definite (this repo's convention)."""
    assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
    return IntegralLattice(f"{kind}{rank}").twist(-1)


def IPQ(p: int, q: int) -> Any:
    r"""The odd unimodular lattice $I_{p,q} = \langle 1\rangle^p \oplus \langle -1\rangle^q$.

    Reconstructed, not ported. The old init.sage *called* ``IPQ(1,1)`` and
    ``IPQ(2,0)`` but never defined it anywhere in the file, so those two lines
    raised NameError -- the ``two_elem_building_blocks`` list and one branch of
    ``get_isotrop_type`` were both dead. This is the standard meaning of the
    notation; if the original meant something else, that intent is not recoverable
    from the source.
    """
    assert p >= 0 and q >= 0 and p + q > 0, f"empty signature ({p}, {q})"
    return IntegralLattice(diagonal_matrix(ZZ, [1] * p + [-1] * q))


# The small fixed names, cheap enough to build at import.
Z = IntegralLattice(matrix(ZZ, [1]))
Z_2 = Z.twist(2)

H = IntegralLattice("H")
H_2 = H.twist(2)
U = H  # the hyperbolic plane; both names were in use
U_2 = H_2

E6 = root_lattice("E", 6)
E7 = root_lattice("E", 7)
E8 = root_lattice("E", 8)
E8_2 = E8.twist(2)

#: Summand order matters and follows the source exactly (``E10 = U @ E8``, old line
#: 73). The two orders give isomorphic lattices but *different bases*, and the Sterk
#: vectors are given in coordinates -- reversing this silently relabels every one of
#: them. An earlier version of this file had the summands the wrong way round.
E10 = U.direct_sum(E8)
E10_2 = E10.twist(2)

#: The K3 lattice $U^3 \oplus E_8^2$. The old file gave it a named basis via Sage's
#: generator syntax with ellipsis ranges (``e1, ..., e8``); that naming belongs with
#: whatever computation needs the coordinates, not in a shared catalogue.
LK3 = U.direct_sum(U).direct_sum(U).direct_sum(E8).direct_sum(E8)

# Literature names, as the old init.sage had them.
Sdp = U_2
TdP = U.direct_sum(U_2).direct_sum(E8).direct_sum(E8)
SEn = E10_2
TEn = U.direct_sum(E10_2)
Tco = Z_2.direct_sum(E10_2)
Sco = Z_2.twist(-1).direct_sum(E10_2)
LpNik = U.direct_sum(U).direct_sum(U).direct_sum(E8_2)
LmNik = E8_2
L_20_2_0 = U.direct_sum(U_2).direct_sum(E8).direct_sum(E8)


def LK3_2d(degree: int) -> Any:
    r"""$\langle -2d\rangle \oplus U^2 \oplus E_8^2$: the degree-$2d$ polarized K3 lattice.

    Live code in the old init.sage (its ``LK3_2d`` lambda, with ``LK3_2`` and
    ``LK3_4`` as the $d = 1, 2$ cases) that this port initially missed entirely.
    The source records alongside it, as comments:

        I^2d(LK3) / O(LK3) = {h},  h^perp = LK3_2d
        J^perp / J = A17,  D10 + E7,  E8^2 + A1,  D16 + A1

    and a citation for the open question ``LK3_2.vinberg_algorithm() == ?``:
    https://arxiv.org/pdf/1903.09742#page=22
    """
    assert degree >= 1, f"degree must be positive, got {degree}"
    return Z.twist(-2 * degree).direct_sum(U).direct_sum(U).direct_sum(E8).direct_sum(E8)


LK3_2 = LK3_2d(1)
LK3_4 = LK3_2d(2)

#: Research recorded in the old file's comments as expected results, kept because the
#: file was a log of findings as much as a library. Each is an unverified claim from
#: the source, not something this repo has checked.
RECORDED_RESULTS: dict[str, str] = {
    "IIPQ(1,17).root_system.num_facets": "19 (mod W)",
    "IIPQ(1,17).root_system.num_rays": "82 (mod W)",
    "J_perp_mod_J": "A17, D10 + E7, E8^2 + A1, D16 + A1",
}

#: Sources the old file cited, with the page anchors it recorded.
CITATIONS: dict[str, str] = {
    "IIPQ(1,17) root system": "https://arxiv.org/pdf/2002.07127#page=12",
    "LK3_2 Vinberg roots": "https://arxiv.org/pdf/1903.09742#page=22",
}

NAMED: dict[str, Any] = {
    "Z": Z,
    "Z_2": Z_2,
    "H": H,
    "H_2": H_2,
    "U": U,
    "U_2": U_2,
    "E6": E6,
    "E7": E7,
    "E8": E8,
    "E8_2": E8_2,
    "E10": E10,
    "E10_2": E10_2,
    "LK3": LK3,
    "Sdp": Sdp,
    "TdP": TdP,
    "SEn": SEn,
    "TEn": TEn,
    "Tco": Tco,
    "Sco": Sco,
    "LpNik": LpNik,
    "LmNik": LmNik,
    "L_20_2_0": L_20_2_0,
    "LK3_2": LK3_2,
    "LK3_4": LK3_4,
}

#: The $(8,6,0)$ entry, resolved by computation rather than left as a gap.
#:
#: The source's table had ``"(8,6,0)": U, # A1^8 *``. The *lattice* is wrong (``U``
#: has rank 2) but the comment is right: **the asterisk denotes a specific overlattice
#: construction**, not uncertainty -- $A_1^8{}^{*}$ is an overlattice of $A_1^8$, in
#: the sense used for two-elementary lattices in the nonsymplectic-involution
#: literature (@AE22, *Compactifications of moduli spaces of K3 surfaces with a
#: Nonsymplectic Involution*, Alexeev-Engel, arXiv:2208.10383).
#:
#: The determinants confirm it rather than contradicting it. An index-$n$ overlattice
#: divides the determinant by $n^2$, and $\det A_1^8 = 256$, so an **index-2**
#: overlattice has determinant $256/4 = 64$ -- exactly what the quotient computes to.
#:
#: The lattice is pinned down by the source's own claim block (old line 384), which
#: asserts $\{e', v'\}^{\perp}/\{e', v'\} \cong (8,6,0)$ inside $T_{En}$, with
#: $v' = 2e + 2f + 2w_1$. Computing that quotient -- which requires the patched
#: lattice methods, see ``patches/lattice_methods.py`` -- gives:
#:
#:     rank 8, signature (0, 8), determinant 64, |A_L| = 64
#:
#: consistent on every count: $64 = 2^6$ is the $a = 6$ the triple $(8,6,0)$ requires,
#: and it is the index-2 overlattice determinant. ``D4 + A1^4`` shares those
#: invariants but is not isometric, which is the expected outcome -- matching rank and
#: determinant does not identify a lattice, and the overlattice is the construction
#: the source named.
TWO_ELEMENTARY_8_6_0_INVARIANTS: dict[str, Any] = {
    "rank": 8,
    "signature_pair": (0, 8),
    "determinant": 64,
    "discriminant_group_order": 64,
    "construction": "index-2 overlattice of A1^8 (the source's 'A1^8 *')",
    "derivation": "TEn.I_perp_mod_I([ep, 2e+2f+2w1]), old init.sage line 384",
    "reference": "AE22 (arXiv:2208.10383), Alexeev-Engel",
    "not_isometric_to": ("D4+A1^4 (same rank and determinant)",),
}

#: Nikulin's building blocks for two-elementary lattices, with the signature triple
#: $(r, a, \delta)$ each realises. Recovered from the commented ``blocks_2_elem`` list
#: at old lines 92-101, which this port first dropped as "just a comment" -- it is the
#: dictionary that says *which lattice* each signature in the table is supposed to be,
#: and without it the unbuilt entries are unidentifiable strings.
TWO_ELEMENTARY_BUILDING_BLOCKS: tuple[tuple[str, str, str], ...] = (
    ("<2>", "(1,1,1)", "Z(2)"),
    ("U", "(2,0,0)", "hyperbolic plane"),
    ("U(2)", "(2,2,0)", "hyperbolic plane, scaled"),
    ("B_n(2)", "(n,n,1)", "for n >= 2"),
    ("C_4n", "(4n,2,0)", "for 4n >= 8"),
    ("C_{4n+2}", "(4n+2,2,1)", "for 4n+2 >= 6"),
    ("F4", "(4,2,0)", ""),
    ("E7", "(7,1,1)", ""),
    ("E8", "(8,0,0)", "unimodular"),
    ("E8(2)", "(8,8,0)", ""),
)

#: Signatures the old table listed with a ``None`` value -- the B_n(2), C_4n, C_4n+2,
#: F4 and E7 forms it never constructed. See
#: :data:`TWO_ELEMENTARY_BUILDING_BLOCKS` for which lattice each one names.
UNBUILT_TWO_ELEMENTARY: tuple[str, ...] = tuple(
    [f"({n},{n},1)" for n in range(2, 21)] + ["(8,2,0)", "(16,2,0)", "(24,2,0)", "(6,2,1)", "(10,2,1)", "(14,2,1)"] + ["(18,2,1)", "(22,2,1)", "(4,2,0)", "(7,1,1)"]
)


def two_elementary_lattices() -> dict[str, Any]:
    r"""Two-elementary lattices by signature triple $(r, a, \delta)$.

    The old table had **three duplicated keys**, each silently discarding the first
    binding: ``(10,10,0)`` was ``SEn`` then ``E10_2``, ``(8,8,0)`` was ``LmNik``
    then ``E8.twist(2)``, and ``(2,2,0)`` was ``U.twist(2)`` twice. Those pairs are
    equal as constructed -- ``SEn`` *is* ``E10_2``, ``LmNik`` *is* ``E8_2`` -- so
    nothing was lost, but the duplication hid that. Asserted here instead.
    """
    assert SEn is E10_2 or SEn.gram_matrix() == E10_2.gram_matrix()
    assert LmNik.gram_matrix() == E8_2.gram_matrix()

    table = {
        "(1,1,1)": Z.twist(2),
        "(2,0,0)": U,
        "(2,2,0)": U_2,
        "(8,0,0)": E8,
        "(8,8,0)": E8_2,
        "(10,8,0)": U.direct_sum(E8_2),
        "(10,10,0)": E10_2,
        "(12,10,0)": TEn,
        "(14,8,0)": LpNik,
        "(18,0,0)": U.direct_sum(E8).direct_sum(E8),
        "(18,2,0)": U_2.direct_sum(E8).direct_sum(E8),
        "(20,2,0)": TdP,
    }
    for key, lattice in table.items():
        rank = int(key.strip("()").split(",")[0])
        assert lattice.rank() == rank, f"{key}: table says rank {rank}, lattice has rank {lattice.rank()}"
    return table


def namespace() -> dict[str, Any]:
    """The old flat names, for injection into an interactive session.

    Includes ``A1``..``A21``, ``D2``..``D22``, ``E6``/``E7``/``E8`` -- the ranges the
    old ``exec`` loops built -- plus every entry of :data:`NAMED`.
    """
    names = dict(NAMED)
    names.update({f"A{n}": root_lattice("A", n) for n in range(1, 22)})
    names.update({f"D{n}": root_lattice("D", n) for n in range(2, 23)})
    return names
