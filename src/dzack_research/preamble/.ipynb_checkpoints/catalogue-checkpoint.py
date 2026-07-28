r"""Named integral lattices used by the preamble.

Root lattices use the negative-definite convention.

EXAMPLES::

    sage: from dzack_research.preamble.catalogue import E8, root_lattice
    sage: root_lattice("A", 2).signature_pair()
    (0, 2)
    sage: E8.rank()
    8
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.matrix.special import diagonal_matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ

from .fixtures import (
    CITATIONS,
    INVOLUTION_IMAGES,
    K3_BASIS_NAMES,
    RECORDED_RESULTS,
    TWO_ELEMENTARY_8_6_0_INVARIANTS,
    TWO_ELEMENTARY_BUILDING_BLOCKS,
    UNBUILT_TWO_ELEMENTARY,
)

__all__ = [
    "CITATIONS",
    "IPQ",
    "NAMED",
    "RECORDED_RESULTS",
    "TWO_ELEMENTARY_8_6_0_INVARIANTS",
    "TWO_ELEMENTARY_BUILDING_BLOCKS",
    "UNBUILT_TWO_ELEMENTARY",
    "involution",
    "involutions",
    "namespace",
    "root_lattice",
    "two_elementary_lattices",
]


def root_lattice(
    kind: str,
    rank: int,
    names: tuple[str, ...] | None = None,
) -> Any:
    """Return the negative-definite root lattice of the given type.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import root_lattice
        sage: D4.<alpha1, alpha2, alpha3, alpha4> = root_lattice("D", 4)
        sage: D4.rank()
        4
        sage: alpha1.parent() is D4
        True
    """
    assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
    lattice = IntegralLattice(f"{kind}{rank}").twist(-1)
    if names is not None:
        lattice._assign_names(names)
    return lattice


def IPQ(p: int, q: int) -> Any:
    r"""Return the odd unimodular lattice $I_{p,q}$.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import IPQ
        sage: L = IPQ(2, 1)
        sage: (L.rank(), L.signature_pair(), L.determinant())
        (3, (2, 1), -1)
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

#: The summand order fixes the coordinates used by the Sterk vectors.
E10 = U.direct_sum(E8)
E10_2 = E10.twist(2)

#: The K3 lattice $U^3 \oplus E_8^2$.
LK3 = U.direct_sum(U).direct_sum(U).direct_sum(E8).direct_sum(E8)

# Literature names.
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
    r"""Return $\langle -2d\rangle \oplus U^2 \oplus E_8^2$.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import LK3_2d
        sage: L = LK3_2d(3)
        sage: (L.rank(), L.signature_pair())
        (21, (2, 19))
    """
    assert degree >= 1, f"degree must be positive, got {degree}"
    return (
        Z.twist(-2 * degree).direct_sum(U).direct_sum(U).direct_sum(E8).direct_sum(E8)
    )


LK3_2 = LK3_2d(1)
LK3_4 = LK3_2d(2)


def _named_involution_matrix(name: str) -> Any:
    """Return the matrix of a named LK3 involution from fixture images."""
    from sage.matrix.special import identity_matrix

    images = INVOLUTION_IMAGES[name]
    index = {basis_name: i for i, basis_name in enumerate(K3_BASIS_NAMES)}
    size = len(K3_BASIS_NAMES)
    assert len(images) == size, f"need {size} images, got {len(images)}"
    columns = []
    for basis_name, sign in images:
        column = [0] * size
        column[index[basis_name]] = sign
        columns.append(column)
    mat = matrix(ZZ, columns).transpose()
    assert mat * mat == identity_matrix(ZZ, size), (
        f"{name} is not an involution: I^2 != id"
    )
    return mat


def involution(name: str) -> Any:
    r"""Return a named automorphism of ``LK3``.

    The Coble/K3 names ``I_dP``, ``I_En``, ``I_Nik`` are signed basis
    permutations of ``LK3``, constructed as ``LK3.Aut()(matrix)``.

    EXAMPLES::

        sage: from dzack_research.preamble import install
        sage: install(vendor_paths=False, red_tracebacks=False)
        {...}
        sage: from dzack_research.preamble.catalogue import involution
        sage: I = involution("I_En")
        sage: (I * I).is_identity()
        True
    """
    assert name in INVOLUTION_IMAGES, (
        f"unknown involution {name!r}; have {sorted(INVOLUTION_IMAGES)}"
    )
    return LK3.Aut()(_named_involution_matrix(name))


def involutions() -> dict[str, Any]:
    """Return all named automorphisms of ``LK3``."""
    return {name: involution(name) for name in INVOLUTION_IMAGES}


def __getattr__(name: str) -> Any:
    """Expose ``I_dP``, ``I_En``, ``I_Nik`` as catalogue attributes."""
    if name in INVOLUTION_IMAGES:
        return involution(name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


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


def two_elementary_lattices() -> dict[str, Any]:
    r"""Return the constructed two-elementary lattices by $(r,a,\delta)$.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import two_elementary_lattices
        sage: table = two_elementary_lattices()
        sage: table["(8,8,0)"].rank()
        8
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
        assert lattice.rank() == rank, (
            f"{key}: table says rank {rank}, lattice has rank {lattice.rank()}"
        )
    return table


def namespace() -> dict[str, Any]:
    """Return the named lattices and root-lattice families.

    EXAMPLES::

        sage: from dzack_research.preamble.catalogue import namespace
        sage: names = namespace()
        sage: (names["A3"].rank(), names["LK3"].rank())
        (3, 22)
    """
    names = dict(NAMED)
    names.update({f"A{n}": root_lattice("A", n) for n in range(1, 22)})
    names.update({f"D{n}": root_lattice("D", n) for n in range(2, 23)})
    return names
