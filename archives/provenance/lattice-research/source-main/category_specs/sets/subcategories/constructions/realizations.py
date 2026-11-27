r"""Construction category for concrete realizations of a set."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ....cat import RealizationsCategory

if TYPE_CHECKING:
    from ....types import SetElement, SetMorphism, SetWithRealizations


class _Realizations(RealizationsCategory):
    r"""Concrete realization parents of a set with realizations.

    Canonical chain: ``Sets().Realizations()``.
    """

    class ParentMethods:
        @abstractmethod
        def parent_with_realization(self) -> SetWithRealizations:
            r"""Return the abstract parent represented by this realization."""
            ...

        @abstractmethod
        def realization_of(self) -> SetWithRealizations:
            r"""Return the abstract parent represented by this realization."""
            ...

        @abstractmethod
        def to_realization(self, realization: SetWithRealizations) -> SetMorphism:
            r"""Return the change-of-realization morphism to ``realization``."""
            ...

    class ElementMethods:
        @abstractmethod
        def to_realization(self, realization: SetWithRealizations) -> SetElement:
            r"""Return this element represented in ``realization``."""
            ...
