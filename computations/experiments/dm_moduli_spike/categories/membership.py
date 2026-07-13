r"""Category membership helpers for moduli landscape objects."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .foundation import ModuliCategory
    from ..moduli.coarse import CoarseModuliSpace
    from ..moduli.stack import DeligneMumfordModuliStack
    from ..stratification.stratified import StratifiedStack


def _same_moduli_base(category: ModuliCategory, base: object) -> bool:
    from ..categories.base import ModuliBase

    if not isinstance(base, ModuliBase):
        return False
    return category.moduli_base() is base


def stack_in_category(stack: DeligneMumfordModuliStack, category: ModuliCategory) -> bool:
    from ..moduli.stack import DeligneMumfordModuliStack

    if not isinstance(stack, DeligneMumfordModuliStack):
        return False
    return _same_moduli_base(category, stack.base())


def coarse_in_category(space: CoarseModuliSpace, category: ModuliCategory) -> bool:
    from ..moduli.coarse import CoarseModuliSpace

    if not isinstance(space, CoarseModuliSpace):
        return False
    return _same_moduli_base(category, space.base())


def stratified_stack_in_category(stratified: StratifiedStack, category: ModuliCategory) -> bool:
    from ..stratification.stratified import StratifiedStack

    if not isinstance(stratified, StratifiedStack):
        return False
    return _same_moduli_base(category, stratified.parent_stack().base())
