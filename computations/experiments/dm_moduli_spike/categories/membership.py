r"""Category membership over a common base `B` in `\mathrm{Sch}/B`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import AffineScheme
    from .foundation import ModuliCategory
    from ..moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver
    from ..moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver
    from ..stratification.stratified import StratifiedStack


def _object_base(obj: object) -> AffineScheme:
    from ..moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver
    from ..moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver

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
    from ..moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver

    if not isinstance(stack, (DeligneMumfordModuliStack, DeligneMumfordModuliStackOver)):
        return False
    return _object_base(stack) is category.base_scheme()


def coarse_in_category(scheme: CoarseModuliScheme | CoarseModuliSchemeOver, category: ModuliCategory) -> bool:
    from ..moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver

    if not isinstance(scheme, (CoarseModuliScheme, CoarseModuliSchemeOver)):
        return False
    return _object_base(scheme) is category.base_scheme()


def stratified_stack_in_category(stratified: StratifiedStack, category: ModuliCategory) -> bool:
    from ..stratification.stratified import StratifiedStack

    if not isinstance(stratified, StratifiedStack):
        return False
    return _object_base(stratified.parent_stack()) is category.base_scheme()
