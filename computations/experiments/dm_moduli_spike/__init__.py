r"""Deligne-Mumford compactification spike."""

from __future__ import annotations

import sage.all  # noqa: F401

from .objects.automorphism_action import AutomorphismAction
from .objects.contraction_orbits import ContractionOrbit
from .objects.contractions import StableGraphContraction
from .objects.curve_types import StableCurveType, StableCurveTypes, StableGraphType, StableGraphTypes
from .objects.model import DMCompactificationModel
from .objects.records import StableGraph, StableGraphRecord
from .objects.strata import (
    ClutchingDatum,
    ClutchingMorphism,
    DMStratum,
    ModuliFactor,
    QuotientStackPresentation,
    QuotientStackSignature,
)
from .objects.stratification import DMStratification, EnumerationResult, StratificationPoset

__all__ = [
    "AutomorphismAction",
    "ClutchingMorphism",
    "ClutchingDatum",
    "ContractionOrbit",
    "DMCompactificationModel",
    "DMStratification",
    "DMStratum",
    "EnumerationResult",
    "ModuliFactor",
    "QuotientStackPresentation",
    "QuotientStackSignature",
    "StableCurveType",
    "StableCurveTypes",
    "StableGraph",
    "StableGraphContraction",
    "StableGraphRecord",
    "StableGraphType",
    "StableGraphTypes",
    "StratificationPoset",
]
