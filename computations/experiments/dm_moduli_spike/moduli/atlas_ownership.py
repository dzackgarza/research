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
Open genus-1 ownership is likewise **parametric**: Legendre / Hesse rows own
every open ``M_{1,n}`` for ``n ≥ 1``. Compact genus-1 ownership is also
**parametric**: Legendre / Hesse rows own every proper ``Mbar_{1,n}`` for
``n ≥ 1`` via :func:`~.instances._legendre_compact_M1n_covering_space` /
:func:`~.instances._hesse_compact_M1n_covering_space`. Call
:func:`owned_etale_atlas_presentations` with ``expand_open_m0n_through`` /
``expand_open_m1n_through`` / ``expand_compact_m1n_through`` to materialize
inspectable per-``n`` rows. This module does **not** invent charts for unowned
types (e.g. ``M_{2,0}``, ``Mbar_{0,n}`` for ``n > 6``).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..categories.base import AffineScheme
    from ..geometry.stacks import AlgebraicSpace, AtlasMorphism
    from .instances import ModuliStack

BaseHypothesis = Literal["none", "two_invertible", "three_invertible"]
GroupoidKind = Literal["none", "legendre_s3", "hesse_sl2_f3"]

# Default inspectable expansion of parametric families.
OPEN_M0N_INSPECTABLE_MAX = 8
OPEN_M1N_INSPECTABLE_MAX = 4
COMPACT_M1N_INSPECTABLE_MAX = 4

# Sentinel markings on parametric rows (not a concrete n).
_PARAMETRIC_OPEN_M0N_MARKINGS = -1
_PARAMETRIC_OPEN_M1N_MARKINGS = -1
_PARAMETRIC_COMPACT_M1N_MARKINGS = -1


@dataclass(frozen=True, slots=True)
class OwnedAtlasPresentation:
    r"""One owned equation-level étale-atlas presentation.

    Keys are ``(genus, markings, proper)``. Parametric open Knudsen uses sentinel
    ``markings = -1`` with ``parametric_open_m0n=True`` (every open ``M_{0,n}``,
    ``n ≥ 3``). Parametric open Legendre/Hesse uses the same sentinel with
    ``parametric_open_m1n=True`` (every open ``M_{1,n}``, ``n ≥ 1``). Parametric
    compact Legendre/Hesse uses ``parametric_compact_m1n=True`` (every proper
    ``Mbar_{1,n}``, ``n ≥ 1``). Genus-1 rows require a base hypothesis (``2`` or
    ``3`` a unit); matching prefers Legendre when both apply.
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

    @property
    def key(self) -> tuple[int, int, bool]:
        return (self.genus, self.markings, self.proper)

    def as_dict(self) -> dict[str, object]:
        if self.parametric_open_m0n:
            markings: object = "n>=3"
        elif self.parametric_open_m1n or self.parametric_compact_m1n:
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
        }
        if self.parametric_open_m0n:
            out["markings_min"] = 3
        if self.parametric_open_m1n or self.parametric_compact_m1n:
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

# Non-parametric rows: proper genus-0 proving set only.
# Genus-1 open/compact rows are parametric (see above).
_NONPARAMETRIC_ETALE_ATLAS_PRESENTATIONS: tuple[OwnedAtlasPresentation, ...] = (
    OwnedAtlasPresentation(0, 3, True, "moduli_affine_etale_chart", "point_spec", "none"),
    OwnedAtlasPresentation(0, 4, True, "moduli_scheme_affine_cover", "projective_line_affine_cover", "none"),
    OwnedAtlasPresentation(0, 5, True, "moduli_scheme_affine_cover", "kapranov_blowup_four_points_p2", "none"),
    OwnedAtlasPresentation(0, 6, True, "moduli_scheme_affine_cover", "kapranov_blowup_five_points_p3", "none"),
)

_OWNED_ETALE_ATLAS_PRESENTATIONS: tuple[OwnedAtlasPresentation, ...] = (
    _PARAMETRIC_OPEN_M0N_ROW,
    _PARAMETRIC_OPEN_M1N_LEGENDRE_ROW,
    _PARAMETRIC_OPEN_M1N_HESSE_ROW,
    _PARAMETRIC_COMPACT_M1N_LEGENDRE_ROW,
    _PARAMETRIC_COMPACT_M1N_HESSE_ROW,
) + _NONPARAMETRIC_ETALE_ATLAS_PRESENTATIONS


def owned_etale_atlas_presentations(
    *,
    expand_open_m0n_through: int | None = None,
    expand_open_m1n_through: int | None = None,
    expand_compact_m1n_through: int | None = None,
) -> tuple[OwnedAtlasPresentation, ...]:
    r"""Owned equation-level étale-atlas presentations.

    Default: one parametric open-Knudsen row, two parametric open-``M_{1,n}``
    rows, two parametric compact-``Mbar_{1,n}`` rows, plus non-parametric proper
    genus-0 rows (cardinality 9).

    When ``expand_open_m0n_through`` is set to an integer ``N ≥ 3``, the
    parametric Knudsen row is replaced by concrete open ``M_{0,3}``…``M_{0,N}``.
    When ``expand_open_m1n_through`` is set to an integer ``N ≥ 1``, the two
    parametric open-``M_{1,n}`` rows are replaced by concrete Legendre+Hesse
    pairs for ``n = 1…N``. When ``expand_compact_m1n_through`` is set to an
    integer ``N ≥ 1``, the two parametric compact-``Mbar_{1,n}`` rows are
    replaced by concrete Legendre+Hesse pairs for ``n = 1…N``.
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

    return open_m0n + open_m1n + compact_m1n + _NONPARAMETRIC_ETALE_ATLAS_PRESENTATIONS


def owned_etale_atlas_cardinality(
    *,
    expand_open_m0n_through: int | None = None,
    expand_open_m1n_through: int | None = None,
    expand_compact_m1n_through: int | None = None,
) -> int:
    r"""Number of owned presentation rows from :func:`owned_etale_atlas_presentations`."""
    return len(
        owned_etale_atlas_presentations(
            expand_open_m0n_through=expand_open_m0n_through,
            expand_open_m1n_through=expand_open_m1n_through,
            expand_compact_m1n_through=expand_compact_m1n_through,
        )
    )


def owned_etale_atlas_type_keys(
    *,
    expand_open_m0n_through: int = OPEN_M0N_INSPECTABLE_MAX,
    expand_open_m1n_through: int = OPEN_M1N_INSPECTABLE_MAX,
    expand_compact_m1n_through: int = COMPACT_M1N_INSPECTABLE_MAX,
) -> tuple[tuple[int, int, bool], ...]:
    r"""Inspectable ``(genus, markings, proper)`` keys.

    Expands parametric open Knudsen through ``expand_open_m0n_through``,
    parametric open ``M_{1,n}`` through ``expand_open_m1n_through``, and
    parametric compact ``Mbar_{1,n}`` through ``expand_compact_m1n_through`` so
    the returned tuple is a finite concrete sample; ownership itself is
    unbounded in ``n`` for open ``M_{0,n}`` (``n ≥ 3``), open ``M_{1,n}``
    (``n ≥ 1``), and compact ``Mbar_{1,n}`` (``n ≥ 1``).
    """
    rows = owned_etale_atlas_presentations(
        expand_open_m0n_through=expand_open_m0n_through,
        expand_open_m1n_through=expand_open_m1n_through,
        expand_compact_m1n_through=expand_compact_m1n_through,
    )
    seen: list[tuple[int, int, bool]] = []
    for row in rows:
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


def is_owned_etale_atlas_type(genus: int, markings: int, *, proper: bool) -> bool:
    r"""True when the registry owns a presentation for ``(g,n,proper)``.

    Open ``M_{0,n}`` for every ``n ≥ 3``, open ``M_{1,n}`` for every ``n ≥ 1``,
    and compact ``Mbar_{1,n}`` for every ``n ≥ 1`` are owned parametrically.
    Genus-1 types remain owned at the type level even when a concrete base fails
    Legendre/Hesse hypotheses (those bases get a structured gap, not a silent
    equation-level stamp).
    """
    if genus == 0 and is_open_m0n_knudsen_owned(markings, proper=proper):
        return True
    if genus == 1 and is_open_m1n_level_owned(markings, proper=proper):
        return True
    if genus == 1 and is_compact_m1n_level_owned(markings, proper=proper):
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
    Open ``M_{1,n}`` (``n ≥ 1``) and compact ``Mbar_{1,n}`` (``n ≥ 1``) resolve
    to concrete Legendre/Hesse alias rows under the matching base hypothesis.
    When ``base`` is omitted, returns the first matching row (do not treat as
    runtime atlas resolution without a base for genus-1 hypothesis rows).
    """
    if genus == 0 and is_open_m0n_knudsen_owned(markings, proper=proper):
        row = _open_m0n_concrete_row(markings)
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
    for row in _OWNED_ETALE_ATLAS_PRESENTATIONS:
        if row.parametric_open_m0n or row.parametric_open_m1n or row.parametric_compact_m1n:
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
        ProjectiveLineAlgebraicSpace,
    )
    from .instances import (
        _hesse_compact_M1n_covering_space,
        _hesse_open_M1n_affine_scheme,
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
    raise AssertionError(f"unowned construction name in registry: {name!r}")


def _group_for_presentation(row: OwnedAtlasPresentation) -> object | None:
    from .instances import _hesse_galois_group, _legendre_galois_group

    if row.groupoid == "none":
        return None
    if row.groupoid == "legendre_s3":
        return _legendre_galois_group()
    if row.groupoid == "hesse_sl2_f3":
        return _hesse_galois_group()
    raise AssertionError(f"unknown groupoid kind {row.groupoid!r}")


def etale_atlas_gap_from_registry(stack: ModuliStack) -> dict[str, object] | None:
    r"""Structured gap when :func:`resolve_owned_etale_atlas` is ``None``.

    Returns ``None`` precisely when an owned equation-level presentation matches.
    """
    if resolve_owned_etale_atlas(stack) is not None:
        return None

    from .instances import _legendre_and_hesse_unavailable

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

    owned_rows = [row.as_dict() for row in owned_etale_atlas_presentations()]
    gap["reason"] = "no_owned_affine_etale_presentation"
    gap["alternate_proving_sets"] = (
        {
            "name": "general_dm_moduli_etale_atlas",
            "status": "not_in_spike",
            "requires": "research constructions (level structures, clutching, blowups) beyond proving set",
            "note": (
                "Owned proving-set presentations are the rows of "
                "owned_etale_atlas_presentations(); open M_{0,n} for every n≥3, "
                "open M_{1,n} for every n≥1, and compact Mbar_{1,n} for every n≥1 "
                "(Legendre/Hesse under unit hypotheses) are owned parametrically "
                "(expand via expand_open_m0n_through / expand_open_m1n_through / "
                "expand_compact_m1n_through). Proper Mbar_{0,n} is owned for "
                "n≤6 (Kapranov). Do not invent charts — in particular do not fake "
                "Kapranov Mbar_{0,n} for n>6; literature name for the gap is "
                "kapranov_iterated_blowup_P_{n-3}."
            ),
            "owned_registry_cardinality": owned_etale_atlas_cardinality(),
            "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            "owned_registry_rows": owned_rows,
            "parametric_open_m0n": True,
            "parametric_open_m1n": True,
            "parametric_compact_m1n": True,
            "open_m0n_knudsen_inspectable_max": OPEN_M0N_INSPECTABLE_MAX,
            "open_m1n_level_inspectable_max": OPEN_M1N_INSPECTABLE_MAX,
            "compact_m1n_level_inspectable_max": COMPACT_M1N_INSPECTABLE_MAX,
            "proper_m0n_gap_construction": "kapranov_iterated_blowup_P_{n-3}",
            "proper_m0n_owned_max": 6,
        },
    )
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
        FormallyEtaleSchemeCertificate,
        _proving_set_etale_certificates,
    )

    row = resolve_owned_etale_atlas(stack)
    if row is None:
        return DeligneMumfordStack.etale_atlas(stack)

    domain = _domain_for_presentation(stack, row)
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
