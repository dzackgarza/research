r"""Weil divisor class groups."""

from typing import Any

from sage.categories.category import Category


def ClassGroup(module: Any) -> Any:
    r"""Refine the specified framed quotient module as \(\operatorname{Cl}(X)\)."""
    assert module in Modules(ZZ).Framed(), (
        "a class group must declare its quotient framing at construction"
    )
    return refine(module, ClassGroups())


class ClassGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of Weil divisor classes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "class groups"

    def super_categories(self) -> list:
        return [Modules(ZZ).Framed()]
