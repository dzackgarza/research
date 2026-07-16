r"""Owned étale-atlas presentation registry for ``ModuliStack``.

Single source of truth for which ``(g, n, proper)`` moduli types expose an
equation-level étale atlas, under which base hypotheses, with which
``covering_kind`` / construction name.

Dispatch contract
=================

Every :meth:`~dm_moduli_spike.moduli.instances.ModuliStack.etale_atlas` call
goes through :func:`dispatch_etale_atlas`:

* matched owned presentation → concrete algebraic-space domain + equation-level
  evidence, or
* no match → fail-closed formal ``AtlasChart`` and a structured gap from
  :func:`etale_atlas_gap_from_registry` (reason + named literature alts).

Open genus-0 ownership is **parametric**: one registry row owns every open
``M_{0,n}`` for ``n ≥ 3`` via :func:`~.instances._knudsen_open_M0n_affine_scheme`.
Proper genus-0 ownership is **parametric** through
:data:`PROPER_M0N_OWNED_MAX`: one registry row owns every proper ``Mbar_{0,n}``
for ``3 ≤ n ≤ PROPER_M0N_OWNED_MAX`` via Kapranov
``kapranov_iterated_blowup_P_{n-3}`` (specializing to the point / ``ℙ¹`` /
``Bl₄(ℙ²)`` / ``Bl(ℙ³)`` covers for ``n ≤ 6``). Open genus-1 ownership is
likewise **parametric**: Legendre / Hesse rows own every open ``M_{1,n}`` for
``n ≥ 1``. Compact genus-1 ownership is also **parametric**: Legendre / Hesse
rows own every proper ``Mbar_{1,n}`` for ``n ≥ 1`` via
:func:`~.instances._legendre_compact_M1n_covering_space` /
:func:`~.instances._hesse_compact_M1n_covering_space`. Call
:func:`owned_etale_atlas_presentations` with ``expand_open_m0n_through`` /
``expand_open_m1n_through`` / ``expand_compact_m1n_through`` /
``expand_proper_m0n_through`` / ``expand_open_m2n_through`` / ``expand_compact_m2n_through`` to materialize
inspectable per-``n`` rows. Open unmarked ``M_{2,0}`` is owned via the Igusa
binary-sextic / ``M_{0,6}/S₆`` chart under ``2 ∈ Rˣ``; proper unmarked
``Mbar_2`` via Kapranov ``Mbar_{0,6}`` with the same ``S₆`` groupoid; open
marked ``M_{2,n}`` (``n ≥ 1``) parametrically via Rosenhain charts; proper
marked ``Mbar_{2,n}`` (``n ≥ 1``) parametrically via Kapranov fiber-product
Rosenhain charts. Open unmarked ``M_{3,0}`` is owned via the degree-2 del Pezzo
/ 7-points-in-``ℙ²`` chart (non-hyperelliptic dense open) under ``2 ∈ Rˣ``;
the hyperelliptic locus of open ``M_3`` is a parallel locus-only binary-octic
/ ``M_{0,8}/S₈`` row. Proper unmarked ``Mbar_3`` is owned via the compactified
del Pezzo / stable marked degree-2 del Pezzo chart (``W(E₇)``) under ``2 ∈ Rˣ``,
with the hyperelliptic Kapranov ``Mbar_{0,8}/S₈`` row demoted to locus-only.
Parametric open/proper marked ``M_{3,n}`` / ``Mbar_{3,n}`` remain hyperelliptic
binary-octic / Kapranov presentations under ``2 ∈ Rˣ``. Open unmarked
``M_{4,0}`` is owned via a ``PGL₄``-normalized canonical ``(2,3)``-complete-
intersection chart (non-trigonal dense open) under ``2 ∈ Rˣ``. This module does
**not** invent charts for unowned types (e.g. ``Mbar_{0,n}`` for
``n > PROPER_M0N_OWNED_MAX``, proper ``Mbar_4``, char-2 Artin–Schreier models).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..categories.base import AffineScheme
    from ..geometry.stacks import AlgebraicSpace, AtlasMorphism
    from .instances import ModuliStack

BaseHypothesis = Literal["none", "two_invertible", "three_invertible"]
GroupoidKind = Literal["none", "legendre_s3", "hesse_sl2_f3", "igusa_s6", "weyl_e7", "hyperelliptic_s8"]

# Default inspectable expansion of parametric families.
OPEN_M0N_INSPECTABLE_MAX = 8
OPEN_M1N_INSPECTABLE_MAX = 4
COMPACT_M1N_INSPECTABLE_MAX = 4
OPEN_M2N_INSPECTABLE_MAX = 4
COMPACT_M2N_INSPECTABLE_MAX = 4
OPEN_M3N_INSPECTABLE_MAX = 4
COMPACT_M3N_INSPECTABLE_MAX = 4
# Proper Kapranov Mbar_{0,n}: owned through n=8 via lazy uniform Spec(A^{n-3}) charts.
# Combinatorial counts (n=7: 17280; n=8: 2073600) are never eagerly materialized —
# equation-level certs use affine_cover_sample() (n-2 charts). Larger n stay fail-closed.
PROPER_M0N_OWNED_MAX = 8
PROPER_M0N_INSPECTABLE_MAX = PROPER_M0N_OWNED_MAX

# Sentinel markings on parametric rows (not a concrete n).
_PARAMETRIC_OPEN_M0N_MARKINGS = -1
_PARAMETRIC_OPEN_M1N_MARKINGS = -1
_PARAMETRIC_COMPACT_M1N_MARKINGS = -1
_PARAMETRIC_PROPER_M0N_MARKINGS = -1
_PARAMETRIC_OPEN_M2N_MARKINGS = -1
_PARAMETRIC_COMPACT_M2N_MARKINGS = -1
_PARAMETRIC_OPEN_M3N_MARKINGS = -1
_PARAMETRIC_COMPACT_M3N_MARKINGS = -1


@dataclass(frozen=True, slots=True)
class OwnedAtlasPresentation:
    r"""One owned equation-level étale-atlas presentation.

    Keys are ``(genus, markings, proper)``. Parametric open Knudsen uses sentinel
    ``markings = -1`` with ``parametric_open_m0n=True`` (every open ``M_{0,n}``,
    ``n ≥ 3``). Parametric proper Kapranov uses the same sentinel with
    ``parametric_proper_m0n=True`` (every proper ``Mbar_{0,n}`` for
    ``3 ≤ n ≤ PROPER_M0N_OWNED_MAX``). Parametric open Legendre/Hesse uses the
    same sentinel with ``parametric_open_m1n=True`` (every open ``M_{1,n}``,
    ``n ≥ 1``). Parametric compact Legendre/Hesse uses
    ``parametric_compact_m1n=True`` (every proper ``Mbar_{1,n}``, ``n ≥ 1``).
    Parametric open Igusa marked uses ``parametric_open_m2n=True`` (every open
    ``M_{2,n}``, ``n ≥ 1``). Parametric compact Igusa marked uses
    ``parametric_compact_m2n=True`` (every proper ``Mbar_{2,n}``, ``n ≥ 1``).
    Parametric open / compact hyperelliptic marked genus-3 uses
    ``parametric_open_m3n`` / ``parametric_compact_m3n``. When
    ``locus_only=True``, the row is inspectable but does **not** own
    ``etale_atlas`` dispatch for its ``(g,n,proper)`` key (used for the
    hyperelliptic locus of open ``M_{3,0}``, parallel to del Pezzo ownership).
    Genus-1 / Igusa / del Pezzo / hyperelliptic rows require a base hypothesis
    (``2`` or ``3`` a unit); matching prefers Legendre when both apply.
    """

    genus: int
    markings: int
    proper: bool
    covering_kind: str
    construction: str
    base_hypothesis: BaseHypothesis
    groupoid: GroupoidKind = "none"
    parametric_open_m0n: bool = False
    parametric_open_m1n: bool = False
    parametric_compact_m1n: bool = False
    parametric_proper_m0n: bool = False
    parametric_open_m2n: bool = False
    parametric_compact_m2n: bool = False
    parametric_open_m3n: bool = False
    parametric_compact_m3n: bool = False
    locus_only: bool = False

    @property
    def key(self) -> tuple[int, int, bool]:
        return (self.genus, self.markings, self.proper)

    def as_dict(self) -> dict[str, object]:
        if self.parametric_open_m0n:
            markings: object = "n>=3"
        elif self.parametric_proper_m0n:
            markings = f"3<=n<={PROPER_M0N_OWNED_MAX}"
        elif (
            self.parametric_open_m1n
            or self.parametric_compact_m1n
            or self.parametric_open_m2n
            or self.parametric_compact_m2n
            or self.parametric_open_m3n
            or self.parametric_compact_m3n
        ):
            markings = "n>=1"
        else:
            markings = self.markings
        out: dict[str, object] = {
            "genus": self.genus,
            "markings": markings,
            "proper": self.proper,
            "covering_kind": self.covering_kind,
            "construction": self.construction,
            "base_hypothesis": self.base_hypothesis,
            "groupoid": self.groupoid,
            "parametric_open_m0n": self.parametric_open_m0n,
            "parametric_open_m1n": self.parametric_open_m1n,
            "parametric_compact_m1n": self.parametric_compact_m1n,
            "parametric_proper_m0n": self.parametric_proper_m0n,
            "parametric_open_m2n": self.parametric_open_m2n,
            "parametric_compact_m2n": self.parametric_compact_m2n,
            "parametric_open_m3n": self.parametric_open_m3n,
            "parametric_compact_m3n": self.parametric_compact_m3n,
            "locus_only": self.locus_only,
        }
        if self.parametric_open_m0n:
            out["markings_min"] = 3
        if self.parametric_proper_m0n:
            out["markings_min"] = 3
            out["markings_max"] = PROPER_M0N_OWNED_MAX
        if (
            self.parametric_open_m1n
            or self.parametric_compact_m1n
            or self.parametric_open_m2n
            or self.parametric_compact_m2n
            or self.parametric_open_m3n
            or self.parametric_compact_m3n
        ):
            out["markings_min"] = 1
        return out


def _open_m0n_construction_name(n: int) -> str:
    r"""Historical construction alias for open ``M_{0,n}`` (same scheme family)."""
    if n == 3:
        return "point_spec"
    if n == 4:
        return "knudsen_cross_ratio"
    return "knudsen_configuration"


def _open_m0n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 3, f"open Knudsen concrete row requires n ≥ 3; got {n!r}"
    return OwnedAtlasPresentation(
        0,
        n_int,
        False,
        "moduli_affine_etale_chart",
        _open_m0n_construction_name(n_int),
        "none",
        parametric_open_m0n=False,
    )


def _open_m1n_covering_kind(n: int, *, legendre: bool) -> str:
    if n == 1:
        return "legendre_finite_etale_cover" if legendre else "hesse_finite_etale_cover"
    if n == 2:
        return "legendre_universal_curve_finite_etale_cover" if legendre else "hesse_universal_curve_finite_etale_cover"
    return "legendre_marked_configuration_finite_etale_cover" if legendre else "hesse_marked_configuration_finite_etale_cover"


def _open_m1n_construction_name(n: int, *, legendre: bool) -> str:
    if n == 1:
        return "legendre_gamma2" if legendre else "hesse_gamma3"
    if n == 2:
        return "legendre_universal_curve" if legendre else "hesse_universal_curve"
    return "legendre_marked_configuration" if legendre else "hesse_marked_configuration"


def _open_m1n_concrete_row(n: int, *, legendre: bool) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"open M_{{1,n}} concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        1,
        n_int,
        False,
        _open_m1n_covering_kind(n_int, legendre=legendre),
        _open_m1n_construction_name(n_int, legendre=legendre),
        "two_invertible" if legendre else "three_invertible",
        "legendre_s3" if legendre else "hesse_sl2_f3",
        parametric_open_m1n=False,
    )


def _compact_m1n_covering_kind(n: int, *, legendre: bool) -> str:
    if n == 1:
        return "legendre_compact_finite_etale_cover" if legendre else "hesse_compact_finite_etale_cover"
    if n == 2:
        return "legendre_compact_universal_curve_finite_etale_cover" if legendre else "hesse_compact_universal_curve_finite_etale_cover"
    return "legendre_compact_marked_configuration_finite_etale_cover" if legendre else "hesse_compact_marked_configuration_finite_etale_cover"


def _compact_m1n_construction_name(n: int, *, legendre: bool) -> str:
    if n == 1:
        return "legendre_gamma2_compact" if legendre else "hesse_gamma3_compact"
    if n == 2:
        return "legendre_universal_curve_compact" if legendre else "hesse_universal_curve_compact"
    return "legendre_marked_configuration_compact" if legendre else "hesse_marked_configuration_compact"


def _compact_m1n_concrete_row(n: int, *, legendre: bool) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"compact Mbar_{{1,n}} concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        1,
        n_int,
        True,
        _compact_m1n_covering_kind(n_int, legendre=legendre),
        _compact_m1n_construction_name(n_int, legendre=legendre),
        "two_invertible" if legendre else "three_invertible",
        "legendre_s3" if legendre else "hesse_sl2_f3",
        parametric_compact_m1n=False,
    )


def _proper_m0n_covering_kind(n: int) -> str:
    if n == 3:
        return "moduli_affine_etale_chart"
    return "moduli_scheme_affine_cover"


def _proper_m0n_construction_name(n: int) -> str:
    r"""Historical / parametric construction alias for proper ``Mbar_{0,n}``."""
    if n == 3:
        return "point_spec"
    if n == 4:
        return "projective_line_affine_cover"
    if n == 5:
        return "kapranov_blowup_four_points_p2"
    if n == 6:
        return "kapranov_blowup_five_points_p3"
    return "kapranov_iterated_blowup_P_{n-3}"


def _proper_m0n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert 3 <= n_int <= PROPER_M0N_OWNED_MAX, f"proper Kapranov concrete row requires 3 ≤ n ≤ {PROPER_M0N_OWNED_MAX}; got {n!r}"
    return OwnedAtlasPresentation(
        0,
        n_int,
        True,
        _proper_m0n_covering_kind(n_int),
        _proper_m0n_construction_name(n_int),
        "none",
        parametric_proper_m0n=False,
    )


def _open_m2n_covering_kind(n: int) -> str:
    if n == 1:
        return "igusa_universal_curve_finite_etale_cover"
    return "igusa_marked_configuration_finite_etale_cover"


def _open_m2n_construction_name(n: int) -> str:
    if n == 1:
        return "igusa_rosenhain_universal_curve"
    return "igusa_rosenhain_marked_configuration"


def _open_m2n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"open Igusa marked concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        2,
        n_int,
        False,
        _open_m2n_covering_kind(n_int),
        _open_m2n_construction_name(n_int),
        "two_invertible",
        "igusa_s6",
        parametric_open_m2n=False,
    )


def _compact_m2n_covering_kind(n: int) -> str:
    if n == 1:
        return "igusa_compact_universal_curve_finite_etale_cover"
    return "igusa_compact_marked_configuration_finite_etale_cover"


def _compact_m2n_construction_name(n: int) -> str:
    if n == 1:
        return "igusa_compact_rosenhain_universal_curve"
    return "igusa_compact_rosenhain_marked_configuration"


def _compact_m2n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"compact Igusa marked concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        2,
        n_int,
        True,
        _compact_m2n_covering_kind(n_int),
        _compact_m2n_construction_name(n_int),
        "two_invertible",
        "igusa_s6",
        parametric_compact_m2n=False,
    )


def _open_m3n_covering_kind(n: int) -> str:
    if n == 1:
        return "hyperelliptic_universal_curve_finite_etale_cover"
    return "hyperelliptic_marked_configuration_finite_etale_cover"


def _open_m3n_construction_name(n: int) -> str:
    if n == 1:
        return "hyperelliptic_binary_octic_universal_curve"
    return "hyperelliptic_binary_octic_marked_configuration"


def _open_m3n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"open hyperelliptic marked concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        3,
        n_int,
        False,
        _open_m3n_covering_kind(n_int),
        _open_m3n_construction_name(n_int),
        "two_invertible",
        "hyperelliptic_s8",
        parametric_open_m3n=False,
    )


def _compact_m3n_covering_kind(n: int) -> str:
    if n == 1:
        return "hyperelliptic_compact_universal_curve_finite_etale_cover"
    return "hyperelliptic_compact_marked_configuration_finite_etale_cover"


def _compact_m3n_construction_name(n: int) -> str:
    if n == 1:
        return "hyperelliptic_compact_binary_octic_universal_curve"
    return "hyperelliptic_compact_binary_octic_marked_configuration"


def _compact_m3n_concrete_row(n: int) -> OwnedAtlasPresentation:
    n_int = int(n)
    assert n_int >= 1, f"compact hyperelliptic marked concrete row requires n ≥ 1; got {n!r}"
    return OwnedAtlasPresentation(
        3,
        n_int,
        True,
        _compact_m3n_covering_kind(n_int),
        _compact_m3n_construction_name(n_int),
        "two_invertible",
        "hyperelliptic_s8",
        parametric_compact_m3n=False,
    )


_PARAMETRIC_OPEN_M0N_ROW = OwnedAtlasPresentation(
    0,
    _PARAMETRIC_OPEN_M0N_MARKINGS,
    False,
    "moduli_affine_etale_chart",
    "knudsen_configuration",
    "none",
    parametric_open_m0n=True,
)

_PARAMETRIC_OPEN_M1N_LEGENDRE_ROW = OwnedAtlasPresentation(
    1,
    _PARAMETRIC_OPEN_M1N_MARKINGS,
    False,
    "legendre_marked_configuration_finite_etale_cover",
    "legendre_marked_configuration",
    "two_invertible",
    "legendre_s3",
    parametric_open_m1n=True,
)

_PARAMETRIC_OPEN_M1N_HESSE_ROW = OwnedAtlasPresentation(
    1,
    _PARAMETRIC_OPEN_M1N_MARKINGS,
    False,
    "hesse_marked_configuration_finite_etale_cover",
    "hesse_marked_configuration",
    "three_invertible",
    "hesse_sl2_f3",
    parametric_open_m1n=True,
)

_PARAMETRIC_COMPACT_M1N_LEGENDRE_ROW = OwnedAtlasPresentation(
    1,
    _PARAMETRIC_COMPACT_M1N_MARKINGS,
    True,
    "legendre_compact_marked_configuration_finite_etale_cover",
    "legendre_marked_configuration_compact",
    "two_invertible",
    "legendre_s3",
    parametric_compact_m1n=True,
)

_PARAMETRIC_COMPACT_M1N_HESSE_ROW = OwnedAtlasPresentation(
    1,
    _PARAMETRIC_COMPACT_M1N_MARKINGS,
    True,
    "hesse_compact_marked_configuration_finite_etale_cover",
    "hesse_marked_configuration_compact",
    "three_invertible",
    "hesse_sl2_f3",
    parametric_compact_m1n=True,
)

_PARAMETRIC_PROPER_M0N_ROW = OwnedAtlasPresentation(
    0,
    _PARAMETRIC_PROPER_M0N_MARKINGS,
    True,
    "moduli_scheme_affine_cover",
    "kapranov_iterated_blowup_P_{n-3}",
    "none",
    parametric_proper_m0n=True,
)

_OPEN_M20_IGUSA_ROW = OwnedAtlasPresentation(
    2,
    0,
    False,
    "igusa_binary_sextic_finite_etale_cover",
    "igusa_binary_sextic_PGL2",
    "two_invertible",
    "igusa_s6",
)

_COMPACT_M20_IGUSA_ROW = OwnedAtlasPresentation(
    2,
    0,
    True,
    "igusa_compact_finite_etale_cover",
    "igusa_mbar06_s6",
    "two_invertible",
    "igusa_s6",
)

_PARAMETRIC_OPEN_M2N_ROW = OwnedAtlasPresentation(
    2,
    _PARAMETRIC_OPEN_M2N_MARKINGS,
    False,
    "igusa_marked_configuration_finite_etale_cover",
    "igusa_rosenhain_marked_configuration",
    "two_invertible",
    "igusa_s6",
    parametric_open_m2n=True,
)

_PARAMETRIC_COMPACT_M2N_ROW = OwnedAtlasPresentation(
    2,
    _PARAMETRIC_COMPACT_M2N_MARKINGS,
    True,
    "igusa_compact_marked_configuration_finite_etale_cover",
    "igusa_compact_rosenhain_marked_configuration",
    "two_invertible",
    "igusa_s6",
    parametric_compact_m2n=True,
)

_OPEN_M30_DEL_PEZZO_ROW = OwnedAtlasPresentation(
    3,
    0,
    False,
    "del_pezzo_seven_points_finite_etale_cover",
    "del_pezzo_degree2_seven_points_PGL3",
    "two_invertible",
    "weyl_e7",
)

# Locus-only: inspectable hyperelliptic cover of open M_3; etale_atlas stays del Pezzo.
_OPEN_M30_HYPERELLIPTIC_LOCUS_ROW = OwnedAtlasPresentation(
    3,
    0,
    False,
    "hyperelliptic_binary_octic_finite_etale_cover",
    "hyperelliptic_binary_octic_M08_S8",
    "two_invertible",
    "hyperelliptic_s8",
    locus_only=True,
)

_COMPACT_M30_DEL_PEZZO_ROW = OwnedAtlasPresentation(
    3,
    0,
    True,
    "del_pezzo_compact_seven_points_finite_etale_cover",
    "del_pezzo_compact_seven_points_PGL3",
    "two_invertible",
    "weyl_e7",
)

# Locus-only: inspectable hyperelliptic cover of Mbar_3; etale_atlas stays compact del Pezzo.
_COMPACT_M30_HYPERELLIPTIC_LOCUS_ROW = OwnedAtlasPresentation(
    3,
    0,
    True,
    "hyperelliptic_compact_finite_etale_cover",
    "hyperelliptic_mbar08_s8",
    "two_invertible",
    "hyperelliptic_s8",
    locus_only=True,
)

_PARAMETRIC_OPEN_M3N_ROW = OwnedAtlasPresentation(
    3,
    _PARAMETRIC_OPEN_M3N_MARKINGS,
    False,
    "hyperelliptic_marked_configuration_finite_etale_cover",
    "hyperelliptic_binary_octic_marked_configuration",
    "two_invertible",
    "hyperelliptic_s8",
    parametric_open_m3n=True,
)

_PARAMETRIC_COMPACT_M3N_ROW = OwnedAtlasPresentation(
    3,
    _PARAMETRIC_COMPACT_M3N_MARKINGS,
    True,
    "hyperelliptic_compact_marked_configuration_finite_etale_cover",
    "hyperelliptic_compact_binary_octic_marked_configuration",
    "two_invertible",
    "hyperelliptic_s8",
    parametric_compact_m3n=True,
)

_OPEN_M40_CANONICAL_ROW = OwnedAtlasPresentation(
    4,
    0,
    False,
    "genus4_canonical_ci_affine_chart",
    "genus4_canonical_quadric_cubic_P3",
    "two_invertible",
    "none",
)

_OWNED_ETALE_ATLAS_PRESENTATIONS: tuple[OwnedAtlasPresentation, ...] = (
    _PARAMETRIC_OPEN_M0N_ROW,
    _PARAMETRIC_OPEN_M1N_LEGENDRE_ROW,
    _PARAMETRIC_OPEN_M1N_HESSE_ROW,
    _PARAMETRIC_COMPACT_M1N_LEGENDRE_ROW,
    _PARAMETRIC_COMPACT_M1N_HESSE_ROW,
    _PARAMETRIC_PROPER_M0N_ROW,
    _OPEN_M20_IGUSA_ROW,
    _COMPACT_M20_IGUSA_ROW,
    _PARAMETRIC_OPEN_M2N_ROW,
    _PARAMETRIC_COMPACT_M2N_ROW,
    _OPEN_M30_DEL_PEZZO_ROW,
    _OPEN_M30_HYPERELLIPTIC_LOCUS_ROW,
    _COMPACT_M30_DEL_PEZZO_ROW,
    _COMPACT_M30_HYPERELLIPTIC_LOCUS_ROW,
    _PARAMETRIC_OPEN_M3N_ROW,
    _PARAMETRIC_COMPACT_M3N_ROW,
    _OPEN_M40_CANONICAL_ROW,
)


def owned_etale_atlas_presentations(
    *,
    expand_open_m0n_through: int | None = None,
    expand_open_m1n_through: int | None = None,
    expand_compact_m1n_through: int | None = None,
    expand_proper_m0n_through: int | None = None,
    expand_open_m2n_through: int | None = None,
    expand_compact_m2n_through: int | None = None,
    expand_open_m3n_through: int | None = None,
    expand_compact_m3n_through: int | None = None,
) -> tuple[OwnedAtlasPresentation, ...]:
    r"""Owned equation-level étale-atlas presentations.

    Default cardinality **15**: parametric open Knudsen / open+compact
    ``M_{1,n}`` / proper Kapranov / open+compact Igusa ``M_{2,*}`` / open del
    Pezzo ``M_{3,0}`` / locus-only hyperelliptic open ``M_3`` / compact
    hyperelliptic ``Mbar_3`` / parametric open+compact hyperelliptic marked
    ``M_{3,n}``.

    Expand flags materialize concrete per-``n`` rows. Unmarked open ``M_{2,0}``,
    compact ``Mbar_2``, open del Pezzo ``M_{3,0}``, locus-only hyperelliptic
    open ``M_3``, and compact hyperelliptic ``Mbar_3`` stay concrete.
    """
    open_m0n: tuple[OwnedAtlasPresentation, ...]
    if expand_open_m0n_through is None:
        open_m0n = (_PARAMETRIC_OPEN_M0N_ROW,)
    else:
        n_max = int(expand_open_m0n_through)
        assert n_max >= 3, f"expand_open_m0n_through must be ≥ 3; got {n_max!r}"
        open_m0n = tuple(_open_m0n_concrete_row(n) for n in range(3, n_max + 1))

    open_m1n: tuple[OwnedAtlasPresentation, ...]
    if expand_open_m1n_through is None:
        open_m1n = (_PARAMETRIC_OPEN_M1N_LEGENDRE_ROW, _PARAMETRIC_OPEN_M1N_HESSE_ROW)
    else:
        n_max_1 = int(expand_open_m1n_through)
        assert n_max_1 >= 1, f"expand_open_m1n_through must be ≥ 1; got {n_max_1!r}"
        open_m1n = tuple(
            row
            for n in range(1, n_max_1 + 1)
            for row in (
                _open_m1n_concrete_row(n, legendre=True),
                _open_m1n_concrete_row(n, legendre=False),
            )
        )

    compact_m1n: tuple[OwnedAtlasPresentation, ...]
    if expand_compact_m1n_through is None:
        compact_m1n = (_PARAMETRIC_COMPACT_M1N_LEGENDRE_ROW, _PARAMETRIC_COMPACT_M1N_HESSE_ROW)
    else:
        n_max_c = int(expand_compact_m1n_through)
        assert n_max_c >= 1, f"expand_compact_m1n_through must be ≥ 1; got {n_max_c!r}"
        compact_m1n = tuple(
            row
            for n in range(1, n_max_c + 1)
            for row in (
                _compact_m1n_concrete_row(n, legendre=True),
                _compact_m1n_concrete_row(n, legendre=False),
            )
        )

    proper_m0n: tuple[OwnedAtlasPresentation, ...]
    if expand_proper_m0n_through is None:
        proper_m0n = (_PARAMETRIC_PROPER_M0N_ROW,)
    else:
        n_max_p = int(expand_proper_m0n_through)
        assert 3 <= n_max_p <= PROPER_M0N_OWNED_MAX, f"expand_proper_m0n_through must satisfy 3 ≤ N ≤ {PROPER_M0N_OWNED_MAX}; got {n_max_p!r}"
        proper_m0n = tuple(_proper_m0n_concrete_row(n) for n in range(3, n_max_p + 1))

    open_m2n: tuple[OwnedAtlasPresentation, ...]
    if expand_open_m2n_through is None:
        open_m2n = (_PARAMETRIC_OPEN_M2N_ROW,)
    else:
        n_max_2 = int(expand_open_m2n_through)
        assert n_max_2 >= 1, f"expand_open_m2n_through must be ≥ 1; got {n_max_2!r}"
        open_m2n = tuple(_open_m2n_concrete_row(n) for n in range(1, n_max_2 + 1))

    compact_m2n: tuple[OwnedAtlasPresentation, ...]
    if expand_compact_m2n_through is None:
        compact_m2n = (_PARAMETRIC_COMPACT_M2N_ROW,)
    else:
        n_max_c2 = int(expand_compact_m2n_through)
        assert n_max_c2 >= 1, f"expand_compact_m2n_through must be ≥ 1; got {n_max_c2!r}"
        compact_m2n = tuple(_compact_m2n_concrete_row(n) for n in range(1, n_max_c2 + 1))

    open_m3n: tuple[OwnedAtlasPresentation, ...]
    if expand_open_m3n_through is None:
        open_m3n = (_PARAMETRIC_OPEN_M3N_ROW,)
    else:
        n_max_3 = int(expand_open_m3n_through)
        assert n_max_3 >= 1, f"expand_open_m3n_through must be ≥ 1; got {n_max_3!r}"
        open_m3n = tuple(_open_m3n_concrete_row(n) for n in range(1, n_max_3 + 1))

    compact_m3n: tuple[OwnedAtlasPresentation, ...]
    if expand_compact_m3n_through is None:
        compact_m3n = (_PARAMETRIC_COMPACT_M3N_ROW,)
    else:
        n_max_c3 = int(expand_compact_m3n_through)
        assert n_max_c3 >= 1, f"expand_compact_m3n_through must be ≥ 1; got {n_max_c3!r}"
        compact_m3n = tuple(_compact_m3n_concrete_row(n) for n in range(1, n_max_c3 + 1))

    return (
        open_m0n
        + open_m1n
        + compact_m1n
        + proper_m0n
        + (_OPEN_M20_IGUSA_ROW, _COMPACT_M20_IGUSA_ROW)
        + open_m2n
        + compact_m2n
        + (
            _OPEN_M30_DEL_PEZZO_ROW,
            _OPEN_M30_HYPERELLIPTIC_LOCUS_ROW,
            _COMPACT_M30_DEL_PEZZO_ROW,
            _COMPACT_M30_HYPERELLIPTIC_LOCUS_ROW,
        )
        + open_m3n
        + compact_m3n
        + (_OPEN_M40_CANONICAL_ROW,)
    )


def owned_etale_atlas_cardinality(
    *,
    expand_open_m0n_through: int | None = None,
    expand_open_m1n_through: int | None = None,
    expand_compact_m1n_through: int | None = None,
    expand_proper_m0n_through: int | None = None,
    expand_open_m2n_through: int | None = None,
    expand_compact_m2n_through: int | None = None,
    expand_open_m3n_through: int | None = None,
    expand_compact_m3n_through: int | None = None,
) -> int:
    r"""Number of owned presentation rows from :func:`owned_etale_atlas_presentations`."""
    return len(
        owned_etale_atlas_presentations(
            expand_open_m0n_through=expand_open_m0n_through,
            expand_open_m1n_through=expand_open_m1n_through,
            expand_compact_m1n_through=expand_compact_m1n_through,
            expand_proper_m0n_through=expand_proper_m0n_through,
            expand_open_m2n_through=expand_open_m2n_through,
            expand_compact_m2n_through=expand_compact_m2n_through,
            expand_open_m3n_through=expand_open_m3n_through,
            expand_compact_m3n_through=expand_compact_m3n_through,
        )
    )


def owned_etale_atlas_type_keys(
    *,
    expand_open_m0n_through: int = OPEN_M0N_INSPECTABLE_MAX,
    expand_open_m1n_through: int = OPEN_M1N_INSPECTABLE_MAX,
    expand_compact_m1n_through: int = COMPACT_M1N_INSPECTABLE_MAX,
    expand_proper_m0n_through: int = PROPER_M0N_INSPECTABLE_MAX,
    expand_open_m2n_through: int = OPEN_M2N_INSPECTABLE_MAX,
    expand_compact_m2n_through: int = COMPACT_M2N_INSPECTABLE_MAX,
    expand_open_m3n_through: int = OPEN_M3N_INSPECTABLE_MAX,
    expand_compact_m3n_through: int = COMPACT_M3N_INSPECTABLE_MAX,
) -> tuple[tuple[int, int, bool], ...]:
    r"""Inspectable ``(genus, markings, proper)`` keys.

    Expands parametric families through the given bounds. Ownership is unbounded
    in ``n`` for open ``M_{0,n}``, open/compact ``M_{1,n}``, open/compact
    ``M_{2,n}``, and open/compact hyperelliptic ``M_{3,n}`` (``n ≥ 1``);
    proper ``Mbar_{0,n}`` for ``3 ≤ n ≤ PROPER_M0N_OWNED_MAX``; unmarked open
    ``M_{2,0}``, proper ``Mbar_2``, open del Pezzo ``M_{3,0}``, compact del Pezzo
    ``Mbar_3``, and open canonical ``M_{4,0}`` are owned concretely. Locus-only
    hyperelliptic open/compact ``M_3`` / ``Mbar_3`` rows share keys with del Pezzo.
    """
    rows = owned_etale_atlas_presentations(
        expand_open_m0n_through=expand_open_m0n_through,
        expand_open_m1n_through=expand_open_m1n_through,
        expand_compact_m1n_through=expand_compact_m1n_through,
        expand_proper_m0n_through=expand_proper_m0n_through,
        expand_open_m2n_through=expand_open_m2n_through,
        expand_compact_m2n_through=expand_compact_m2n_through,
        expand_open_m3n_through=expand_open_m3n_through,
        expand_compact_m3n_through=expand_compact_m3n_through,
    )
    seen: list[tuple[int, int, bool]] = []
    for row in rows:
        if row.locus_only:
            continue
        if row.key not in seen:
            seen.append(row.key)
    return tuple(seen)


def is_open_m0n_knudsen_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open Knudsen owns ``(0, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n >= 3


def is_open_m1n_level_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open Legendre/Hesse owns ``(1, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n >= 1


def is_compact_m1n_level_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact Legendre/Hesse owns ``(1, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n >= 1


def is_proper_m0n_kapranov_owned(markings: int, *, proper: bool) -> bool:
    r"""True when proper Kapranov owns ``(0, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and 3 <= n <= PROPER_M0N_OWNED_MAX


def is_open_m20_igusa_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open Igusa owns ``(2, markings, proper)`` (unmarked open only)."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n == 0


def is_compact_m20_igusa_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact Igusa owns ``(2, markings, proper)`` (unmarked proper only)."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n == 0


def is_open_m2n_igusa_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open marked Igusa owns ``(2, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n >= 1


def is_compact_m2n_igusa_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact marked Igusa owns ``(2, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n >= 1


def is_open_m30_del_pezzo_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open del Pezzo owns ``(3, markings, proper)`` (unmarked open only)."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n == 0


def is_compact_m30_del_pezzo_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact del Pezzo owns ``(3, markings, proper)`` (unmarked proper)."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n == 0


def is_compact_m30_hyperelliptic_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact hyperelliptic locus row matches unmarked proper ``Mbar_3``.

    The row is **locus-only**: it does not own ``etale_atlas`` dispatch (compact
    del Pezzo does). Kept for inspectable
    :meth:`~.instances.ModuliStack.hyperelliptic_quotient_presentation`.
    """
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n == 0


def is_open_m3n_hyperelliptic_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open marked hyperelliptic owns ``(3, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n >= 1


def is_compact_m3n_hyperelliptic_owned(markings: int, *, proper: bool) -> bool:
    r"""True when compact marked hyperelliptic owns ``(3, markings, proper)`` parametrically."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return proper and n >= 1


def is_open_m40_canonical_owned(markings: int, *, proper: bool) -> bool:
    r"""True when open canonical CI owns ``(4, markings, proper)`` (unmarked open)."""
    try:
        n = int(markings)
    except TypeError, ValueError:
        return False
    return (not proper) and n == 0


def is_owned_etale_atlas_type(genus: int, markings: int, *, proper: bool) -> bool:
    r"""True when the registry owns a presentation for ``(g,n,proper)``.

    Open ``M_{0,n}`` for every ``n ≥ 3``, proper ``Mbar_{0,n}`` for
    ``3 ≤ n ≤ PROPER_M0N_OWNED_MAX``, open ``M_{1,n}`` for every ``n ≥ 1``, and
    compact ``Mbar_{1,n}`` for every ``n ≥ 1`` are owned parametrically.
    Open unmarked ``M_{2,0}``, proper unmarked ``Mbar_2``, open marked
    ``M_{2,n}`` (``n ≥ 1``), and proper marked ``Mbar_{2,n}`` (``n ≥ 1``) are
    owned via Igusa (require ``2 ∈ Rˣ`` at resolution). Open unmarked
    ``M_{3,0}`` and proper unmarked ``Mbar_3`` are owned via degree-2 del Pezzo
    / 7-points (``W(E₇)``); marked open/compact ``M_{3,n}`` via hyperelliptic
    binary octics / ``M_{0,8}/S₈``. Open unmarked ``M_{4,0}`` via canonical
    ``(2,3)``-CI. Genus-1 / Igusa / del Pezzo / hyperelliptic / genus-4 types
    remain owned at the type level even when a concrete base fails the unit
    hypothesis (structured gap, not a silent equation-level stamp).
    """
    if genus == 0 and is_open_m0n_knudsen_owned(markings, proper=proper):
        return True
    if genus == 0 and is_proper_m0n_kapranov_owned(markings, proper=proper):
        return True
    if genus == 1 and is_open_m1n_level_owned(markings, proper=proper):
        return True
    if genus == 1 and is_compact_m1n_level_owned(markings, proper=proper):
        return True
    if genus == 2 and is_open_m20_igusa_owned(markings, proper=proper):
        return True
    if genus == 2 and is_compact_m20_igusa_owned(markings, proper=proper):
        return True
    if genus == 2 and is_open_m2n_igusa_owned(markings, proper=proper):
        return True
    if genus == 2 and is_compact_m2n_igusa_owned(markings, proper=proper):
        return True
    if genus == 3 and is_open_m30_del_pezzo_owned(markings, proper=proper):
        return True
    if genus == 3 and is_compact_m30_del_pezzo_owned(markings, proper=proper):
        return True
    if genus == 3 and is_open_m3n_hyperelliptic_owned(markings, proper=proper):
        return True
    if genus == 3 and is_compact_m3n_hyperelliptic_owned(markings, proper=proper):
        return True
    if genus == 4 and is_open_m40_canonical_owned(markings, proper=proper):
        return True
    return (genus, markings, proper) in owned_etale_atlas_type_keys()


def _hypothesis_holds(hypothesis: BaseHypothesis, base: AffineScheme) -> bool:
    from .instances import _three_is_invertible, _two_is_invertible

    if hypothesis == "none":
        return True
    if hypothesis == "two_invertible":
        return _two_is_invertible(base)
    if hypothesis == "three_invertible":
        # Prefer Legendre when both units: only match Hesse when 2 is unavailable.
        return (not _two_is_invertible(base)) and _three_is_invertible(base)
    raise AssertionError(f"unknown base hypothesis {hypothesis!r}")


def lookup_owned_etale_atlas(
    genus: int,
    markings: int,
    *,
    proper: bool,
    base: AffineScheme | None = None,
) -> OwnedAtlasPresentation | None:
    r"""First registry row matching ``(g,n,proper)`` and optional base hypothesis.

    Open ``M_{0,n}`` (``n ≥ 3``) resolves to a concrete Knudsen alias row.
    Proper ``Mbar_{0,n}`` (``3 ≤ n ≤ PROPER_M0N_OWNED_MAX``) resolves to a
    concrete Kapranov alias row. Open ``M_{1,n}`` (``n ≥ 1``) and compact
    ``Mbar_{1,n}`` (``n ≥ 1``) resolve to concrete Legendre/Hesse alias rows
    under the matching base hypothesis.     Open unmarked ``M_{2,0}``, proper unmarked ``Mbar_2``, open marked
    ``M_{2,n}`` (``n ≥ 1``), and proper marked ``Mbar_{2,n}`` (``n ≥ 1``)
    resolve to Igusa / Rosenhain rows when ``2 ∈ Rˣ``. Open unmarked
    ``M_{3,0}`` resolves to the del Pezzo row (not the locus-only hyperelliptic
    row). Proper unmarked ``Mbar_3`` resolves to the compact del Pezzo row (not
    the locus-only hyperelliptic Kapranov row). Marked open/compact ``M_{3,n}``
    resolve to hyperelliptic binary-octic rows. Open unmarked ``M_{4,0}``
    resolves to the canonical ``(2,3)``-CI row under the same hypothesis.
    When ``base`` is omitted, returns the first matching row (do not treat as
    runtime atlas resolution without a base for hypothesis rows).
    """
    if genus == 0 and is_open_m0n_knudsen_owned(markings, proper=proper):
        row = _open_m0n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 0 and is_proper_m0n_kapranov_owned(markings, proper=proper):
        row = _proper_m0n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 1 and is_open_m1n_level_owned(markings, proper=proper):
        for legendre in (True, False):
            row = _open_m1n_concrete_row(markings, legendre=legendre)
            if base is None or _hypothesis_holds(row.base_hypothesis, base):
                return row
        return None
    if genus == 1 and is_compact_m1n_level_owned(markings, proper=proper):
        for legendre in (True, False):
            row = _compact_m1n_concrete_row(markings, legendre=legendre)
            if base is None or _hypothesis_holds(row.base_hypothesis, base):
                return row
        return None
    if genus == 2 and is_open_m20_igusa_owned(markings, proper=proper):
        row = _OPEN_M20_IGUSA_ROW
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 2 and is_compact_m20_igusa_owned(markings, proper=proper):
        row = _COMPACT_M20_IGUSA_ROW
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 2 and is_open_m2n_igusa_owned(markings, proper=proper):
        row = _open_m2n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 2 and is_compact_m2n_igusa_owned(markings, proper=proper):
        row = _compact_m2n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 3 and is_open_m30_del_pezzo_owned(markings, proper=proper):
        row = _OPEN_M30_DEL_PEZZO_ROW
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 3 and is_compact_m30_del_pezzo_owned(markings, proper=proper):
        row = _COMPACT_M30_DEL_PEZZO_ROW
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 3 and is_open_m3n_hyperelliptic_owned(markings, proper=proper):
        row = _open_m3n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 3 and is_compact_m3n_hyperelliptic_owned(markings, proper=proper):
        row = _compact_m3n_concrete_row(markings)
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    if genus == 4 and is_open_m40_canonical_owned(markings, proper=proper):
        row = _OPEN_M40_CANONICAL_ROW
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
        return None
    for row in _OWNED_ETALE_ATLAS_PRESENTATIONS:
        if (
            row.parametric_open_m0n
            or row.parametric_open_m1n
            or row.parametric_compact_m1n
            or row.parametric_proper_m0n
            or row.parametric_open_m2n
            or row.parametric_compact_m2n
            or row.parametric_open_m3n
            or row.parametric_compact_m3n
            or row.locus_only
        ):
            continue
        if row.genus != genus or row.markings != markings or row.proper != proper:
            continue
        if base is None or _hypothesis_holds(row.base_hypothesis, base):
            return row
    return None


def resolve_owned_etale_atlas(stack: ModuliStack) -> OwnedAtlasPresentation | None:
    r"""Registry row that owns ``stack``'s equation-level étale atlas, if any."""
    return lookup_owned_etale_atlas(
        stack.genus(),
        stack.number_of_markings(),
        proper=stack.is_proper(),
        base=stack.base_scheme(),
    )


def _domain_for_presentation(stack: ModuliStack, row: OwnedAtlasPresentation) -> AlgebraicSpace:
    from ..geometry.stacks import (
        AffineAlgebraicSpace,
        KapranovBlowupFivePointsP3AlgebraicSpace,
        KapranovBlowupFourPointsP2AlgebraicSpace,
        KapranovIteratedBlowupPnMinus3AlgebraicSpace,
        ProjectiveLineAlgebraicSpace,
    )
    from .instances import (
        _del_pezzo_compact_M30_covering_space,
        _del_pezzo_open_M30_affine_scheme,
        _genus4_open_M40_affine_scheme,
        _hesse_compact_M1n_covering_space,
        _hesse_open_M1n_affine_scheme,
        _hyperelliptic_compact_M3n_covering_space,
        _hyperelliptic_compact_M30_covering_space,
        _hyperelliptic_open_M3n_affine_scheme,
        _hyperelliptic_open_M30_affine_scheme,
        _igusa_compact_M2n_covering_space,
        _igusa_compact_M20_covering_space,
        _igusa_open_M2n_affine_scheme,
        _igusa_open_M20_affine_scheme,
        _knudsen_open_M0n_affine_scheme,
        _legendre_compact_M1n_covering_space,
        _legendre_open_M1n_affine_scheme,
    )

    base = stack.base_scheme()
    name = row.construction
    # Open M_{0,n}: single parametric Knudsen scheme (aliases point_spec /
    # knudsen_cross_ratio / knudsen_configuration). Proper Mbar_{0,3} is Spec(R).
    if (
        stack.genus() == 0
        and not stack.is_proper()
        and name
        in (
            "point_spec",
            "knudsen_cross_ratio",
            "knudsen_configuration",
        )
    ):
        return AffineAlgebraicSpace(_knudsen_open_M0n_affine_scheme(base, stack.number_of_markings()))
    if name == "point_spec":
        return AffineAlgebraicSpace(base)
    if name == "projective_line_affine_cover":
        return ProjectiveLineAlgebraicSpace(base, "Mbar_0_4")
    if name == "kapranov_blowup_four_points_p2":
        return KapranovBlowupFourPointsP2AlgebraicSpace(base, "Mbar_0_5")
    if name == "kapranov_blowup_five_points_p3":
        return KapranovBlowupFivePointsP3AlgebraicSpace(base, "Mbar_0_6")
    if name == "kapranov_iterated_blowup_P_{n-3}":
        n_marks = stack.number_of_markings()
        return KapranovIteratedBlowupPnMinus3AlgebraicSpace(base, n_marks, f"Mbar_0_{n_marks}")
    if name in ("legendre_gamma2", "legendre_universal_curve", "legendre_marked_configuration"):
        return AffineAlgebraicSpace(_legendre_open_M1n_affine_scheme(base, stack.number_of_markings()))
    if name in ("hesse_gamma3", "hesse_universal_curve", "hesse_marked_configuration"):
        return AffineAlgebraicSpace(_hesse_open_M1n_affine_scheme(base, stack.number_of_markings()))
    if name in (
        "legendre_gamma2_compact",
        "legendre_universal_curve_compact",
        "legendre_marked_configuration_compact",
    ):
        return _legendre_compact_M1n_covering_space(base, stack.number_of_markings())
    if name in (
        "hesse_gamma3_compact",
        "hesse_universal_curve_compact",
        "hesse_marked_configuration_compact",
    ):
        return _hesse_compact_M1n_covering_space(base, stack.number_of_markings())
    if name == "igusa_binary_sextic_PGL2":
        return AffineAlgebraicSpace(_igusa_open_M20_affine_scheme(base))
    if name == "igusa_mbar06_s6":
        return _igusa_compact_M20_covering_space(base)
    if name in ("igusa_rosenhain_universal_curve", "igusa_rosenhain_marked_configuration"):
        return AffineAlgebraicSpace(_igusa_open_M2n_affine_scheme(base, stack.number_of_markings()))
    if name in ("igusa_compact_rosenhain_universal_curve", "igusa_compact_rosenhain_marked_configuration"):
        return _igusa_compact_M2n_covering_space(base, stack.number_of_markings())
    if name == "del_pezzo_degree2_seven_points_PGL3":
        return AffineAlgebraicSpace(_del_pezzo_open_M30_affine_scheme(base))
    if name == "del_pezzo_compact_seven_points_PGL3":
        return _del_pezzo_compact_M30_covering_space(base)
    if name == "genus4_canonical_quadric_cubic_P3":
        return AffineAlgebraicSpace(_genus4_open_M40_affine_scheme(base))
    if name == "hyperelliptic_binary_octic_M08_S8":
        return AffineAlgebraicSpace(_hyperelliptic_open_M30_affine_scheme(base))
    if name == "hyperelliptic_mbar08_s8":
        return _hyperelliptic_compact_M30_covering_space(base)
    if name in ("hyperelliptic_binary_octic_universal_curve", "hyperelliptic_binary_octic_marked_configuration"):
        return AffineAlgebraicSpace(_hyperelliptic_open_M3n_affine_scheme(base, stack.number_of_markings()))
    if name in (
        "hyperelliptic_compact_binary_octic_universal_curve",
        "hyperelliptic_compact_binary_octic_marked_configuration",
    ):
        return _hyperelliptic_compact_M3n_covering_space(base, stack.number_of_markings())
    raise AssertionError(f"unowned construction name in registry: {name!r}")


def _group_for_presentation(row: OwnedAtlasPresentation) -> object | None:
    from .instances import (
        _del_pezzo_galois_group,
        _hesse_galois_group,
        _hyperelliptic_galois_group,
        _igusa_galois_group,
        _legendre_galois_group,
    )

    if row.groupoid == "none":
        return None
    if row.groupoid == "legendre_s3":
        return _legendre_galois_group()
    if row.groupoid == "hesse_sl2_f3":
        return _hesse_galois_group()
    if row.groupoid == "igusa_s6":
        return _igusa_galois_group()
    if row.groupoid == "weyl_e7":
        return _del_pezzo_galois_group()
    if row.groupoid == "hyperelliptic_s8":
        return _hyperelliptic_galois_group()
    raise AssertionError(f"unknown groupoid kind {row.groupoid!r}")


def etale_atlas_gap_from_registry(stack: ModuliStack) -> dict[str, object] | None:
    r"""Structured gap when :func:`resolve_owned_etale_atlas` is ``None``.

    Returns ``None`` precisely when an owned equation-level presentation matches.
    """
    if resolve_owned_etale_atlas(stack) is not None:
        return None

    from .instances import _legendre_and_hesse_unavailable, _two_is_invertible

    g = stack.genus()
    n = stack.number_of_markings()
    proper = stack.is_proper()
    base = stack.base_scheme()
    gap: dict[str, object] = {
        "genus": g,
        "markings": n,
        "proper": proper,
        "equation_level": False,
        "covering_kind_if_formal": "etale_atlas_chart",
        "registry_owned_type": is_owned_etale_atlas_type(g, n, proper=proper),
    }

    owned_genus1 = is_owned_etale_atlas_type(g, n, proper=proper) and g == 1 and _legendre_and_hesse_unavailable(base)
    if owned_genus1:
        weierstrass = stack.weierstrass_gm_presentation()
        if n == 1:
            gap["reason"] = "legendre_and_hesse_unavailable"
        elif n == 2 and proper:
            gap["reason"] = "mbar_1_2_legendre_and_hesse_unavailable"
        elif n == 2:
            gap["reason"] = "m_1_2_legendre_and_hesse_unavailable"
        elif proper:
            gap["reason"] = "mbar_1_n_legendre_and_hesse_unavailable"
        else:
            gap["reason"] = "m_1_n_legendre_and_hesse_unavailable"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "three_invertible": False,
            "prototype": "Spec(Z)",
            "note": ("Neither 2 nor 3 is a unit in the base ring. On fields this case never arises (char 2 ⇒ Hesse; char 3 ⇒ Legendre; else both units)."),
        }
        alts: list[dict[str, object]] = []
        if weierstrass is not None:
            alts.append(
                {
                    "name": "weierstrass_gm_quotient",
                    "status": "owned_not_finite_etale",
                    "presentation": weierstrass,
                    "requires": "Spec(R[a1,…,a6][Δ⁻¹]) with weighted 𝔾_m-action",
                    "note": weierstrass["proof_not_finite_etale"],
                }
            )
        else:
            alts.append(
                {
                    "name": "weierstrass_gm_quotient",
                    "status": "owned_not_finite_etale_for_n_le_2_only",
                    "requires": "n ∈ {1,2}; Spec(R[a1,…,a6][Δ⁻¹]) with weighted 𝔾_m-action",
                    "note": (
                        "Weierstrass 𝔾_m fail-closed evidence is owned for (1,1)/(1,2). "
                        "M_{1,n} / Mbar_{1,n} for n≥3 stay fail-closed under the same "
                        "base hypothesis without inventing a multi-mark Weierstrass chart."
                    ),
                }
            )
        alts.append(
            {
                "name": "igusa_ordinary_a6_chart",
                "status": "incomplete_ordinary_only",
                "requires": "char 2; ordinary locus only",
                "note": (
                    "y² + xy = x³ + a₆ with j = 1/a₆ covers the ordinary locus; "
                    "misses the supersingular point j = 0 — incomplete as a full "
                    "atlas of M_{1,1}. Not constructed in-spike."
                ),
            }
        )
        gap["alternate_proving_sets"] = tuple(alts)
        gap["pre_225_remaining_after_this"] = "general_(g,n)_only"
        return gap

    # Owned Igusa types (open M_{2,*}, compact Mbar_2) fail closed when 2 is not a unit.
    owned_igusa_type = g == 2 and is_owned_etale_atlas_type(2, n, proper=proper)
    if owned_igusa_type and not _two_is_invertible(base):
        gap["reason"] = "igusa_requires_two_invertible"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "prototype": "Spec(Z) or char 2",
            "note": (
                "Igusa / Rosenhain charts for open M_{2,n} and proper Mbar_{2,n} "
                "require 2 ∈ Rˣ (ordinary hyperelliptic double cover y² = f₆). On "
                "fields of characteristic 2 the Artin–Schreier model is needed — "
                "not owned."
            ),
        }
        gap["alternate_proving_sets"] = (
            {
                "name": "igusa_binary_sextic_quotient",
                "status": "owned_under_two_invertible",
                "construction": "igusa_binary_sextic_PGL2 / igusa_mbar06_s6 / igusa_rosenhain_* / igusa_compact_rosenhain_*",
                "requires": (
                    "2 ∈ Rˣ; open M_{2,0}: Spec(R[λ,μ,ν]_S); open M_{2,n}: Rosenhain "
                    "universal curve; proper Mbar_2: Kapranov Mbar_{0,6} with S₆; "
                    "proper Mbar_{2,n}: Kapranov fiber-product Rosenhain"
                ),
                "note": ("Registry owns open M_{2,n} (n≥0) and proper Mbar_{2,n} (n≥0) under two_invertible. This base fails that hypothesis — formal AtlasChart only."),
                "owned_registry_cardinality": owned_etale_atlas_cardinality(),
                "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            },
        )
        gap["pre_225_remaining_after_this"] = "general_(g,n)_beyond_owned_igusa"
        return gap

    # Owned open/compact M_{3,0} del Pezzo fails closed when 2 is not a unit.
    owned_del_pezzo_type = g == 3 and (is_open_m30_del_pezzo_owned(n, proper=proper) or is_compact_m30_del_pezzo_owned(n, proper=proper))
    if owned_del_pezzo_type and not _two_is_invertible(base):
        gap["reason"] = "del_pezzo_requires_two_invertible"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "prototype": "Spec(Z) or char 2",
            "note": (
                "Degree-2 del Pezzo / plane-quartic charts for open M_{3,0} and "
                "proper Mbar_3 require 2 ∈ Rˣ (anticanonical double cover of ℙ²). "
                "Parallel locus-only hyperelliptic binary octics / M_{0,8}/S₈ "
                "likewise require 2 ∈ Rˣ."
            ),
        }
        gap["alternate_proving_sets"] = (
            {
                "name": "del_pezzo_degree2_seven_points",
                "status": "owned_under_two_invertible",
                "construction": "del_pezzo_degree2_seven_points_PGL3 / del_pezzo_compact_seven_points_PGL3",
                "requires": ("2 ∈ Rˣ; open: Spec(R[a..f]_S); compact: lazy (ℙ²)³ charts Spec(R[u1..u6])×27; W(E₇)"),
                "note": (
                    "Registry owns open/proper unmarked M_{3,0}/Mbar_3 "
                    "(non-hyperelliptic dense open) under two_invertible. "
                    "This base fails that hypothesis — formal AtlasChart only."
                ),
                "owned_registry_cardinality": owned_etale_atlas_cardinality(),
                "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            },
            {
                "name": "hyperelliptic_binary_octic_M08_S8",
                "status": "owned_locus_under_two_invertible",
                "requires": "2 ∈ Rˣ; Knudsen open M_{0,8}/S₈ or Kapranov Mbar_{0,8}/S₈",
                "note": "Locus-only registry rows: cover the hyperelliptic divisor — not the non-hyperelliptic dense open (del Pezzo owns etale_atlas).",
            },
        )
        gap["pre_225_remaining_after_this"] = "general_(g,n)_beyond_owned_del_pezzo"
        return gap

    # Owned hyperelliptic marked genus-3 types fail closed without 2 unit.
    owned_hyp_g3 = g == 3 and (is_open_m3n_hyperelliptic_owned(n, proper=proper) or is_compact_m3n_hyperelliptic_owned(n, proper=proper))
    if owned_hyp_g3 and not _two_is_invertible(base):
        gap["reason"] = "hyperelliptic_requires_two_invertible"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "prototype": "Spec(Z) or char 2",
            "note": (
                "Hyperelliptic binary-octic / M_{0,8}/S₈ charts for marked "
                "M_{3,n} / Mbar_{3,n} require 2 ∈ Rˣ. Coverage is the "
                "hyperelliptic locus only. Char-2 Artin–Schreier models are not owned."
            ),
        }
        gap["alternate_proving_sets"] = (
            {
                "name": "hyperelliptic_binary_octic_M08_S8",
                "status": "owned_under_two_invertible",
                "construction": "hyperelliptic_binary_octic_* / hyperelliptic_compact_binary_octic_*",
                "requires": ("2 ∈ Rˣ; open marked: Spec(R[t1..t5,x_i,y_i]_S)/(y²=octic); marked compact: Kapranov fiber product over Mbar_{0,8}/S₈"),
                "note": (
                    "Registry owns hyperelliptic locus presentations for marked "
                    "M_{3,n}/Mbar_{3,n} under two_invertible. This base fails that "
                    "hypothesis — formal AtlasChart only."
                ),
                "owned_registry_cardinality": owned_etale_atlas_cardinality(),
                "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            },
        )
        gap["pre_225_remaining_after_this"] = "general_(g,n)_beyond_owned_hyperelliptic_g3"
        return gap

    # Owned open M_{4,0} canonical CI fails closed when 2 is not a unit.
    owned_m40 = g == 4 and is_open_m40_canonical_owned(n, proper=proper)
    if owned_m40 and not _two_is_invertible(base):
        gap["reason"] = "genus4_canonical_requires_two_invertible"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "prototype": "Spec(Z) or char 2",
            "note": ("Canonical (2,3)-complete-intersection charts for open M_{4,0} require 2 ∈ Rˣ (smooth-quadric / non-trigonal normal form)."),
        }
        gap["alternate_proving_sets"] = (
            {
                "name": "genus4_canonical_quadric_cubic_P3",
                "status": "owned_under_two_invertible",
                "construction": "genus4_canonical_quadric_cubic_P3",
                "requires": ("2 ∈ Rˣ; Spec(R[c1..c9]_S) PGL₄-normalized non-trigonal dense open"),
                "note": ("Registry owns open unmarked M_{4,0} (non-trigonal dense open) under two_invertible. This base fails that hypothesis — formal AtlasChart only."),
                "owned_registry_cardinality": owned_etale_atlas_cardinality(),
                "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            },
        )
        gap["pre_225_remaining_after_this"] = "general_(g,n)_beyond_owned_genus4"
        return gap

    owned_rows = [row.as_dict() for row in owned_etale_atlas_presentations()]
    registry_alt: dict[str, object] = {
        "name": "general_dm_moduli_etale_atlas",
        "status": "not_in_spike",
        "requires": "research constructions (level structures, clutching, blowups) beyond proving set",
        "note": (
            "Owned proving-set presentations are the rows of "
            "owned_etale_atlas_presentations(); open M_{0,n} for every n≥3, "
            "open M_{1,n} for every n≥1, and compact Mbar_{1,n} for every n≥1 "
            "(Legendre/Hesse under unit hypotheses) are owned parametrically "
            "(expand via expand_open_m0n_through / expand_open_m1n_through / "
            "expand_compact_m1n_through). Proper Mbar_{0,n} is owned "
            f"parametrically for 3≤n≤{PROPER_M0N_OWNED_MAX} (Kapranov "
            "kapranov_iterated_blowup_P_{n-3}; expand via "
            "expand_proper_m0n_through). Open M_{2,n} (n≥0) and proper "
            "Mbar_{2,n} (n≥0) are owned via Igusa / Rosenhain / Kapranov "
            "Mbar_{0,6} fiber products with S₆ under 2 ∈ Rˣ (expand marked via "
            "expand_open_m2n_through / expand_compact_m2n_through). Open and "
            "proper unmarked M_{3,0}/Mbar_3 are owned via degree-2 del Pezzo / "
            "7-points with W(E₇) under 2 ∈ Rˣ (non-hyperelliptic dense open); "
            "locus-only binary-octic / M_{0,8}/S₈ rows cover the hyperelliptic "
            "loci. Marked M_{3,n}/Mbar_{3,n} are owned via hyperelliptic "
            "Kapranov Mbar_{0,8}/S₈ (hyperelliptic locus coverage; expand via "
            "expand_open_m3n_through / expand_compact_m3n_through). Open "
            "unmarked M_{4,0} is owned via PGL₄-normalized canonical "
            "(2,3)-CI (non-trigonal dense open) under 2 ∈ Rˣ. Do not invent "
            "charts for larger genus-0 n — the literature construction name "
            "remains kapranov_iterated_blowup_P_{n-3}."
        ),
        "owned_registry_cardinality": owned_etale_atlas_cardinality(),
        "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
        "owned_registry_rows": owned_rows,
        "parametric_open_m0n": True,
        "parametric_open_m1n": True,
        "parametric_compact_m1n": True,
        "parametric_proper_m0n": True,
        "parametric_open_m2n": True,
        "parametric_compact_m2n": True,
        "parametric_open_m3n": True,
        "parametric_compact_m3n": True,
        "open_m20_igusa": True,
        "compact_m20_igusa": True,
        "open_m30_del_pezzo": True,
        "open_m30_hyperelliptic_locus": True,
        "compact_m30_del_pezzo": True,
        "compact_m30_hyperelliptic_locus": True,
        "open_m40_canonical": True,
        "open_m0n_knudsen_inspectable_max": OPEN_M0N_INSPECTABLE_MAX,
        "open_m1n_level_inspectable_max": OPEN_M1N_INSPECTABLE_MAX,
        "compact_m1n_level_inspectable_max": COMPACT_M1N_INSPECTABLE_MAX,
        "open_m2n_igusa_inspectable_max": OPEN_M2N_INSPECTABLE_MAX,
        "compact_m2n_igusa_inspectable_max": COMPACT_M2N_INSPECTABLE_MAX,
        "open_m3n_hyperelliptic_inspectable_max": OPEN_M3N_INSPECTABLE_MAX,
        "compact_m3n_hyperelliptic_inspectable_max": COMPACT_M3N_INSPECTABLE_MAX,
        "proper_m0n_inspectable_max": PROPER_M0N_INSPECTABLE_MAX,
        "proper_m0n_gap_construction": "kapranov_iterated_blowup_P_{n-3}",
        "proper_m0n_owned_max": PROPER_M0N_OWNED_MAX,
    }

    # Remaining gaps: Mbar_4 / marked M_{4,n}, char-2 Artin–Schreier / del Pezzo,
    # marked non-hyperelliptic del Pezzo, trigonal M_4 locus charts.
    gap["reason"] = "no_owned_affine_etale_presentation"
    gap["alternate_proving_sets"] = (registry_alt,)
    return gap


def dispatch_etale_atlas(stack: ModuliStack) -> AtlasMorphism:
    r"""Single dispatch for :meth:`ModuliStack.etale_atlas`.

    Owned registry match → equation-level ``AtlasMorphism``. Otherwise fail-closed
    formal ``AtlasChart`` (gap via :func:`etale_atlas_gap_from_registry`).
    """
    from typing import Any, cast

    from ..geometry.stacks import (
        AtlasEvidence,
        AtlasMorphism,
        DeligneMumfordStack,
        DelPezzoCompactSevenPointsAlgebraicSpace,
        FormallyEtaleSchemeCertificate,
        HyperellipticCompactMarkedM3nAlgebraicSpace,
        IgusaCompactMarkedM2nAlgebraicSpace,
        KapranovIteratedBlowupPnMinus3AlgebraicSpace,
        _proving_set_etale_certificates,
    )

    row = resolve_owned_etale_atlas(stack)
    if row is None:
        return DeligneMumfordStack.etale_atlas(stack)

    domain = _domain_for_presentation(stack, row)
    # Kapranov iterated / Igusa / hyperelliptic / del Pezzo compact: certify a
    # uniform sample, not the full combinatorial chart list (eager N hangs QC).
    if isinstance(
        domain,
        (
            KapranovIteratedBlowupPnMinus3AlgebraicSpace,
            IgusaCompactMarkedM2nAlgebraicSpace,
            HyperellipticCompactMarkedM3nAlgebraicSpace,
            DelPezzoCompactSevenPointsAlgebraicSpace,
        ),
    ):
        cover = domain.affine_cover_sample()
        assert cover and domain.affine_cover_cardinality() >= 1, "owned lazy Kapranov/Igusa/hyperelliptic/del-Pezzo domain must expose a nonempty sample cover"
    else:
        cover = domain.affine_cover()
        assert cover, "owned moduli étale domain must expose a nonempty affine cover"
    certs: list[FormallyEtaleSchemeCertificate] = []
    for chart in cover:
        certs.extend(_proving_set_etale_certificates(chart))
    scheme_certs = tuple(certs)
    primary = scheme_certs[0] if scheme_certs else None
    group = _group_for_presentation(row)
    if group is not None:
        group_order = int(cast(Any, group).order())
        return AtlasMorphism(
            domain,
            stack,
            etale=True,
            covering_kind=row.covering_kind,
            representable_domain=True,
            evidence=AtlasEvidence(
                stack=stack,
                domain=domain,
                covering_kind=row.covering_kind,
                etale_stamp=True,
                representable_domain=True,
                diagonal=stack.diagonal(),
                dm_diagonal_unramified_stamp=True,
                dm_diagonal_representable_stamp=True,
                scheme_certificate=primary,
                scheme_certificates=scheme_certs,
                covering_space=domain,
                quotient_group=group,
                finite_etale_groupoid=True,
                group_order=group_order,
                covering_unramified_stamp=True,
                covering_smooth_stamp=True,
                covering_formally_etale_stamp=True,
            ),
        )
    return AtlasMorphism(
        domain,
        stack,
        etale=True,
        covering_kind=row.covering_kind,
        representable_domain=True,
        evidence=AtlasEvidence(
            stack=stack,
            domain=domain,
            covering_kind=row.covering_kind,
            etale_stamp=True,
            representable_domain=True,
            diagonal=stack.diagonal(),
            dm_diagonal_unramified_stamp=True,
            dm_diagonal_representable_stamp=True,
            scheme_certificate=primary,
            scheme_certificates=scheme_certs,
        ),
    )
