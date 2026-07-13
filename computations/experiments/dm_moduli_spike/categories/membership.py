r"""Category membership helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import AffineScheme
    from .foundation import ModuliCategory
    from ..curves.pointed import PointedCurve
    from ..geometry.stacks import AlgebraicSpace, Stack
    from ..moduli.instances import ModuliStack


def stack_in_category(stack: object, category: ModuliCategory) -> bool:
    return stack in category


def coarse_in_category(scheme: object, category: ModuliCategory) -> bool:
    return scheme in category


def stratified_stack_in_category(stratified: object, category: ModuliCategory) -> bool:
    return stratified in category


def pointed_curve_in_category(curve: object, category: ModuliCategory) -> bool:
    from ..curves.pointed import PointedCurve, SmoothPointedCurve, StablePointedCurve
    from .curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves

    if not isinstance(curve, PointedCurve):
        return False
    base = curve.base_scheme()
    if base is not category.base_scheme():
        return False
    if isinstance(category, StablePointedCurves):
        return isinstance(curve, StablePointedCurve)
    if isinstance(category, PointedCurves):
        return True
    if isinstance(category, SmoothCurves):
        return curve.is_smooth()
    if isinstance(category, Curves):
        return True
    return False
