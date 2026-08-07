r"""Picard groups."""

from sage.categories.category import Category


def PicardGroup(module: "Module") -> "Module":
    r"""Refine the specified framed quotient module as \(\operatorname{Pic}(X)\)."""
    assert module in Modules(ZZ).Framed(), (
        "a Picard group must declare its quotient framing at construction"
    )
    return refine(module, PicardGroups())


class PicardGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of line-bundle classes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "Picard groups"

    def super_categories(self) -> list:
        return [Modules(ZZ).Framed()]
