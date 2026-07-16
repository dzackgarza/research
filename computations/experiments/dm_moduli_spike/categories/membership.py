r"""Category membership helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..categories.base import AffineScheme

if TYPE_CHECKING:
    from .foundation import ModuliCategory


def _object_base(obj: object) -> AffineScheme:
    r"""Base scheme of a geometric object exposing :meth:`base_scheme`."""
    assert hasattr(obj, "base_scheme"), f"expected object with base_scheme(); found {type(obj)!r}; obj={obj!r}; owned boundary=membership._object_base"
    base = obj.base_scheme()
    assert isinstance(base, AffineScheme), f"base_scheme() must return AffineScheme; found {type(base)!r}; obj={obj!r}"
    return base


def stack_in_category(stack: object, category: ModuliCategory) -> bool:
    return bool(stack in category)


def coarse_in_category(scheme: object, category: ModuliCategory) -> bool:
    return bool(scheme in category)


def stratified_stack_in_category(stratified: object, category: ModuliCategory) -> bool:
    return bool(stratified in category)


def pointed_curve_in_category(curve: object, category: ModuliCategory) -> bool:
    from ..curves.pointed import Curve, PointedCurve, SmoothPointedCurve, StablePointedCurve
    from .curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves

    if not isinstance(curve, Curve):
        return False
    base = curve.base_scheme()
    if base is not category.base_scheme():
        return False
    if isinstance(category, StablePointedCurves):
        return isinstance(curve, StablePointedCurve)
    if isinstance(category, PointedCurves):
        return isinstance(curve, PointedCurve)
    if isinstance(category, SmoothCurves):
        if isinstance(curve, (SmoothPointedCurve, StablePointedCurve)):
            return bool(curve.is_smooth())
        return isinstance(curve, Curve) and curve.is_smooth() and not isinstance(curve, PointedCurve)
    if isinstance(category, Curves):
        return True
    return False
