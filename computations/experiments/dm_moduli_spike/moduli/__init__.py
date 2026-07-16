r"""Concrete moduli stacks M_{g,I} and Mbar_{g,I}."""

from __future__ import annotations

from .atlas_ownership import (
    OwnedAtlasPresentation,
    is_owned_etale_atlas_type,
    lookup_owned_etale_atlas,
    owned_etale_atlas_cardinality,
    owned_etale_atlas_presentations,
    owned_etale_atlas_type_keys,
    resolve_owned_etale_atlas,
)
from .instances import (
    Groupoid,
    M_gI,
    M_gn,
    Mbar_gI,
    Mbar_gn,
    ModuliProblem,
    ModuliStack,
    SmoothPointedCurveModuliProblem,
    StablePointedCurveModuliProblem,
)

__all__ = [
    "Groupoid",
    "M_gI",
    "M_gn",
    "Mbar_gI",
    "Mbar_gn",
    "ModuliProblem",
    "ModuliStack",
    "OwnedAtlasPresentation",
    "SmoothPointedCurveModuliProblem",
    "StablePointedCurveModuliProblem",
    "is_owned_etale_atlas_type",
    "lookup_owned_etale_atlas",
    "owned_etale_atlas_cardinality",
    "owned_etale_atlas_presentations",
    "owned_etale_atlas_type_keys",
    "resolve_owned_etale_atlas",
]
