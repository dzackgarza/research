r"""Pointed stable and smooth curves and families."""

from __future__ import annotations

from .families import (
    Curve,
    CurveFamily,
    NormalizationMorphism,
    PointedCurve,
    PointedCurveFamily,
    StablePointedCurve as StablePointedCurveBase,
    StablePointedCurveFamily,
)
from .pointed import PointedCurve as LandscapePointedCurve  # noqa: F401
from .pointed import SmoothPointedCurve, StablePointedCurve

__all__ = [
    "Curve",
    "CurveFamily",
    "NormalizationMorphism",
    "PointedCurve",
    "PointedCurveFamily",
    "SmoothPointedCurve",
    "StablePointedCurve",
    "StablePointedCurveFamily",
]
