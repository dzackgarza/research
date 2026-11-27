r"""Ring objects regarded as modules."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Ring, RingMorphism, RModuleElement


class _RingObjectsAsModules(Category_over_base_ring):
    r"""Ring objects regarded as modules over their structure ring.

    Constructor target: ``Modules(R).Constructors().RingObjectAsModule(...)``
    and related forgetful bridges refine here.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Modules(R)]

    class ParentMethods:
        @override
        @final
        def is_ring_object_as_module(self) -> bool:
            return True

        @abstractmethod
        def structure_ring(self) -> Ring: ...

        @abstractmethod
        def structure_map(self) -> RingMorphism: ...

        @abstractmethod
        def module_generators(self) -> tuple[RModuleElement, ...]: ...

    class ElementMethods: ...
