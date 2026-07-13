r"""Category membership over a common base `B` in `\mathrm{Sch}/B`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import AffineScheme
    from .foundation import ModuliCategory
    from .._landscape.curves.pointed import PointedCurve
    from .._landscape.moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver
    from .._landscape.moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver
    from .._landscape.stratification.stratified import StratifiedStack


def _object_base(obj: object) -> AffineScheme:
    from .._landscape.curves.pointed import PointedCurve
    from .._landscape.moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver
    from .._landscape.moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver

    if isinstance(obj, PointedCurve):
        return obj.base_scheme()
    if isinstance(obj, DeligneMumfordModuliStack):
        return obj.base_scheme()
    if isinstance(obj, DeligneMumfordModuliStackOver):
        return obj.over_scheme()
    if isinstance(obj, CoarseModuliScheme):
        return obj.base_scheme()
    if isinstance(obj, CoarseModuliSchemeOver):
        return obj.over_scheme()
    raise TypeError(f"no base scheme for {type(obj)}")


def stack_in_category(stack: DeligneMumfordModuliStack | DeligneMumfordModuliStackOver, category: ModuliCategory) -> bool:
    from .._landscape.moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver

    if not isinstance(stack, (DeligneMumfordModuliStack, DeligneMumfordModuliStackOver)):
        return False
    return _object_base(stack) is category.base_scheme()


def coarse_in_category(scheme: CoarseModuliScheme | CoarseModuliSchemeOver, category: ModuliCategory) -> bool:
    from .._landscape.moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver

    if not isinstance(scheme, (CoarseModuliScheme, CoarseModuliSchemeOver)):
        return False
    return _object_base(scheme) is category.base_scheme()


def stratified_stack_in_category(stratified: StratifiedStack, category: ModuliCategory) -> bool:
    from .._landscape.stratification.stratified import StratifiedStack

    if not isinstance(stratified, StratifiedStack):
        return False
    return _object_base(stratified.parent_stack()) is category.base_scheme()


def pointed_curve_in_category(curve: PointedCurve, category: ModuliCategory) -> bool:
    r"""True when ``curve`` is a pointed curve over ``category.base_scheme()`` matching `(g,n)` if fixed."""
    from .._landscape.curves.pointed import PointedCurve, SmoothPointedCurve, StablePointedCurve
    from .curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves

    if not isinstance(curve, PointedCurve):
        return False
    if _object_base(curve) is not category.base_scheme():
        return False
    if isinstance(category, StablePointedCurves):
        if not isinstance(curve, StablePointedCurve):
            return False
    elif isinstance(category, PointedCurves):
        if not isinstance(curve, (SmoothPointedCurve, StablePointedCurve, PointedCurve)):
            return False
    elif isinstance(category, SmoothCurves):
        if hasattr(curve, "is_smooth") and not curve.is_smooth():  # type: ignore[attr-defined]
            return False
    elif not isinstance(category, Curves):
        return False
    g = getattr(category, "genus", lambda: None)()
    n = getattr(category, "number_of_markings", lambda: None)()
    if g is not None and curve.arithmetic_genus() != g:
        return False
    if n is not None and curve.number_of_markings() != n:
        return False
    return True
