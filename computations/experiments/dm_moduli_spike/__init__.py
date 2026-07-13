r"""Deligne-Mumford compactification spike."""

from __future__ import annotations

import sage.all  # noqa: F401

from .objects.automorphism_action import AutomorphismAction
from .objects.contractions import StableGraphContraction
from .objects.graph_types import StableGraphType, StableGraphTypes
from .objects.model import DMCompactificationModel
from .objects.records import StableGraph, StableGraphRecord
from .objects.strata import (
    ClutchingMorphism,
    DMStratum,
    ModuliFactor,
    QuotientStackPresentation,
)
from .objects.stratification import DMStratification, StratificationPoset

__all__ = [
    "AutomorphismAction",
    "ClutchingMorphism",
    "DMCompactificationModel",
    "DMStratification",
    "DMStratum",
    "ModuliFactor",
    "QuotientStackPresentation",
    "StableGraph",
    "StableGraphContraction",
    "StableGraphRecord",
    "StableGraphType",
    "StableGraphTypes",
    "StratificationPoset",
]
