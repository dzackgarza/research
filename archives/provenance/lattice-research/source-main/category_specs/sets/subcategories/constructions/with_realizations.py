r"""Construction category for sets with multiple realizations."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.category import Category

from ....cat import WithRealizationsCategory

if TYPE_CHECKING:
    from ....types import SetRealization


class SetsWithRealizations(WithRealizationsCategory):
    r"""Sets whose elements may be represented in several concrete realizations.

    Canonical chain: ``Sets().WithRealizations()``.
    """

    class ParentMethods:
        @abstractmethod
        def a_realization(self) -> SetRealization:
            r"""Return the distinguished default realization."""
            ...

        @abstractmethod
        def realizations(self) -> Sequence[SetRealization]:
            r"""Return the concrete realization parents of this set."""
            ...

        @abstractmethod
        def inject_shorthands(self) -> None:
            r"""Expose named realization parents in the caller's namespace."""
            ...

        @abstractmethod
        def Realizations(self) -> Category:
            r"""Return the category of realizations of this parent."""
            ...

    class ElementMethods: ...
