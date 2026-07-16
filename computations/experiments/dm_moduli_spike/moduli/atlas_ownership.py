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

This module does **not** invent charts for arbitrary ``(g, n)``. Unowned types
(e.g. ``M_{2,0}``, ``Mbar_{0,6}``) stay gap-only until a literature-backed
construction is registered here.
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


@dataclass(frozen=True, slots=True)
class OwnedAtlasPresentation:
    r"""One owned equation-level étale-atlas presentation.

    Keys are ``(genus, markings, proper)``. Genus-1 rows additionally require a
    base hypothesis (``2`` or ``3`` a unit); matching prefers Legendre when both
    apply.
    """

    genus: int
    markings: int
    proper: bool
    covering_kind: str
    construction: str
    base_hypothesis: BaseHypothesis
    groupoid: GroupoidKind = "none"

    @property
    def key(self) -> tuple[int, int, bool]:
        return (self.genus, self.markings, self.proper)

    def as_dict(self) -> dict[str, object]:
        return {
            "genus": self.genus,
            "markings": self.markings,
            "proper": self.proper,
            "covering_kind": self.covering_kind,
            "construction": self.construction,
            "base_hypothesis": self.base_hypothesis,
            "groupoid": self.groupoid,
        }


# Ordered: for a fixed (g,n,proper), first matching hypothesis wins
# (Legendre before Hesse, matching historical dispatch).
_OWNED_ETALE_ATLAS_PRESENTATIONS: tuple[OwnedAtlasPresentation, ...] = (
    OwnedAtlasPresentation(0, 3, False, "moduli_affine_etale_chart", "point_spec", "none"),
    OwnedAtlasPresentation(0, 3, True, "moduli_affine_etale_chart", "point_spec", "none"),
    OwnedAtlasPresentation(0, 4, False, "moduli_affine_etale_chart", "knudsen_cross_ratio", "none"),
    OwnedAtlasPresentation(0, 4, True, "moduli_scheme_affine_cover", "projective_line_affine_cover", "none"),
    OwnedAtlasPresentation(0, 5, False, "moduli_affine_etale_chart", "knudsen_configuration", "none"),
    OwnedAtlasPresentation(0, 5, True, "moduli_scheme_affine_cover", "kapranov_blowup_four_points_p2", "none"),
    OwnedAtlasPresentation(0, 6, False, "moduli_affine_etale_chart", "knudsen_configuration", "none"),
    OwnedAtlasPresentation(
        1,
        1,
        False,
        "legendre_finite_etale_cover",
        "legendre_gamma2",
        "two_invertible",
        "legendre_s3",
    ),
    OwnedAtlasPresentation(
        1,
        1,
        True,
        "legendre_compact_finite_etale_cover",
        "legendre_gamma2_compact",
        "two_invertible",
        "legendre_s3",
    ),
    OwnedAtlasPresentation(
        1,
        1,
        False,
        "hesse_finite_etale_cover",
        "hesse_gamma3",
        "three_invertible",
        "hesse_sl2_f3",
    ),
    OwnedAtlasPresentation(
        1,
        1,
        True,
        "hesse_compact_finite_etale_cover",
        "hesse_gamma3_compact",
        "three_invertible",
        "hesse_sl2_f3",
    ),
    OwnedAtlasPresentation(
        1,
        2,
        False,
        "legendre_universal_curve_finite_etale_cover",
        "legendre_universal_curve",
        "two_invertible",
        "legendre_s3",
    ),
    OwnedAtlasPresentation(
        1,
        2,
        True,
        "legendre_compact_universal_curve_finite_etale_cover",
        "legendre_universal_curve_compact",
        "two_invertible",
        "legendre_s3",
    ),
    OwnedAtlasPresentation(
        1,
        2,
        False,
        "hesse_universal_curve_finite_etale_cover",
        "hesse_universal_curve",
        "three_invertible",
        "hesse_sl2_f3",
    ),
    OwnedAtlasPresentation(
        1,
        2,
        True,
        "hesse_compact_universal_curve_finite_etale_cover",
        "hesse_universal_curve_compact",
        "three_invertible",
        "hesse_sl2_f3",
    ),
)


def owned_etale_atlas_presentations() -> tuple[OwnedAtlasPresentation, ...]:
    r"""All currently owned equation-level étale-atlas presentations."""
    return _OWNED_ETALE_ATLAS_PRESENTATIONS


def owned_etale_atlas_cardinality() -> int:
    r"""Number of owned presentation rows (not unique ``(g,n,proper)`` keys)."""
    return len(_OWNED_ETALE_ATLAS_PRESENTATIONS)


def owned_etale_atlas_type_keys() -> tuple[tuple[int, int, bool], ...]:
    r"""Unique ``(genus, markings, proper)`` keys with at least one owned row."""
    seen: list[tuple[int, int, bool]] = []
    for row in _OWNED_ETALE_ATLAS_PRESENTATIONS:
        if row.key not in seen:
            seen.append(row.key)
    return tuple(seen)


def is_owned_etale_atlas_type(genus: int, markings: int, *, proper: bool) -> bool:
    r"""True when the registry lists any presentation for ``(g,n,proper)``.

    Genus-1 types remain owned at the type level even when a concrete base fails
    Legendre/Hesse hypotheses (those bases get a structured gap, not a silent
    equation-level stamp).
    """
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

    When ``base`` is omitted, returns the first row for that type key (inspect
    the static registry; do not treat this as a runtime atlas resolution).
    """
    for row in _OWNED_ETALE_ATLAS_PRESENTATIONS:
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
        KapranovBlowupFourPointsP2AlgebraicSpace,
        ProjectiveLineAlgebraicSpace,
    )
    from .instances import (
        _configuration_M05_affine_scheme,
        _configuration_M06_affine_scheme,
        _cross_ratio_affine_scheme,
        _hesse_affine_scheme,
        _hesse_M12_affine_scheme,
        _hesse_Mbar12_algebraic_space,
        _legendre_affine_scheme,
        _legendre_M12_affine_scheme,
        _legendre_Mbar12_algebraic_space,
    )

    base = stack.base_scheme()
    name = row.construction
    if name == "point_spec":
        return AffineAlgebraicSpace(base)
    if name == "knudsen_cross_ratio":
        return AffineAlgebraicSpace(_cross_ratio_affine_scheme(base))
    if name == "projective_line_affine_cover":
        return ProjectiveLineAlgebraicSpace(base, "Mbar_0_4")
    if name == "knudsen_configuration":
        n = stack.number_of_markings()
        if n == 5:
            return AffineAlgebraicSpace(_configuration_M05_affine_scheme(base))
        if n == 6:
            return AffineAlgebraicSpace(_configuration_M06_affine_scheme(base))
        raise AssertionError(f"knudsen_configuration owns open M_{{0,5}} and M_{{0,6}} only; got n={n}")
    if name == "kapranov_blowup_four_points_p2":
        return KapranovBlowupFourPointsP2AlgebraicSpace(base, "Mbar_0_5")
    if name == "legendre_gamma2":
        return AffineAlgebraicSpace(_legendre_affine_scheme(base))
    if name == "legendre_gamma2_compact":
        return ProjectiveLineAlgebraicSpace(base, "Mbar_Gamma2")
    if name == "hesse_gamma3":
        return AffineAlgebraicSpace(_hesse_affine_scheme(base))
    if name == "hesse_gamma3_compact":
        return ProjectiveLineAlgebraicSpace(base, "Mbar_Gamma3")
    if name == "legendre_universal_curve":
        return AffineAlgebraicSpace(_legendre_M12_affine_scheme(base))
    if name == "legendre_universal_curve_compact":
        return _legendre_Mbar12_algebraic_space(base)
    if name == "hesse_universal_curve":
        return AffineAlgebraicSpace(_hesse_M12_affine_scheme(base))
    if name == "hesse_universal_curve_compact":
        return _hesse_Mbar12_algebraic_space(base)
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

    if is_owned_etale_atlas_type(g, n, proper=proper) and g == 1 and n in (1, 2) and _legendre_and_hesse_unavailable(base):
        weierstrass = stack.weierstrass_gm_presentation()
        assert weierstrass is not None, "Weierstrass Gm presentation must be owned when Legendre/Hesse unavailable"
        if n == 1:
            gap["reason"] = "legendre_and_hesse_unavailable"
        elif proper:
            gap["reason"] = "mbar_1_2_legendre_and_hesse_unavailable"
        else:
            gap["reason"] = "m_1_2_legendre_and_hesse_unavailable"
        gap["base_hypothesis"] = {
            "two_invertible": False,
            "three_invertible": False,
            "prototype": "Spec(Z)",
            "note": ("Neither 2 nor 3 is a unit in the base ring. On fields this case never arises (char 2 ⇒ Hesse; char 3 ⇒ Legendre; else both units)."),
        }
        gap["alternate_proving_sets"] = (
            {
                "name": "weierstrass_gm_quotient",
                "status": "owned_not_finite_etale",
                "presentation": weierstrass,
                "requires": "Spec(R[a1,…,a6][Δ⁻¹]) with weighted 𝔾_m-action",
                "note": weierstrass["proof_not_finite_etale"],
            },
            {
                "name": "igusa_ordinary_a6_chart",
                "status": "incomplete_ordinary_only",
                "requires": "char 2; ordinary locus only",
                "note": (
                    "y² + xy = x³ + a₆ with j = 1/a₆ covers the ordinary locus; "
                    "misses the supersingular point j = 0 — incomplete as a full "
                    "atlas of M_{1,1}. Not constructed in-spike."
                ),
            },
        )
        gap["pre_225_remaining_after_this"] = "general_(g,n)_only"
        return gap

    owned_rows = [row.as_dict() for row in _OWNED_ETALE_ATLAS_PRESENTATIONS]
    gap["reason"] = "no_owned_affine_etale_presentation"
    gap["alternate_proving_sets"] = (
        {
            "name": "general_dm_moduli_etale_atlas",
            "status": "not_in_spike",
            "requires": "research constructions (level structures, clutching, blowups) beyond proving set",
            "note": (
                "Owned proving-set presentations are exactly the rows of "
                "owned_etale_atlas_presentations(); general (g,n) atlases need "
                "constructions not present in this spike. Do not invent charts."
            ),
            "owned_registry_cardinality": owned_etale_atlas_cardinality(),
            "owned_registry_type_keys": list(owned_etale_atlas_type_keys()),
            "owned_registry_rows": owned_rows,
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
