r"""Subtree for class groups under the divisors category tree.

A class group Cl(X) = Div(X) / Prin(X) is the quotient of a divisor group by principal divisors.
It receives the canonical projection Div(X) -> Cl(X).
"""

from typing import Any

from sage.categories.category import Category


class ClassGroupElement(Element):
    r"""Element of a class group (a divisor class [D])."""

    def lift(self: Any) -> Any:
        r"""Lift this class to a representative divisor in Div(X)."""
        return self.parent().lift_to_divisor(self)


class ClassGroup(Parent):
    r"""A class group Cl(X)."""

    Element = ClassGroupElement

    def __init__(self, base_ring: Any = ZZ) -> None:
        r"""Initialize the class group and refine into ClassGroups."""
        Parent.__init__(self, base=base_ring)
        refine(self, ClassGroups())


class ClassGroupMorphism(Morphism):
    r"""Morphism of class groups."""


class ClassGroups(Category):
    r"""Category of class groups."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "class groups"

    def super_categories(self) -> list:
        r"""Return Modules(ZZ), of which class groups are modules."""
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Class group parent methods."""

        def divisor_group(self: Any) -> Any:
            r"""Return the associated divisor group Div(X)."""
            raise NotImplementedError("divisor_group must be implemented by concrete ClassGroup")

        def canonical_projection(self: Any) -> Any:
            r"""Return the canonical projection morphism Div(X) -> Cl(X)."""
            return self.divisor_group().canonical_projection()

        def lift_to_divisor(self: Any, element: Any) -> Any:
            r"""Lift a class to a representative divisor in Div(X)."""
            raise NotImplementedError("lift_to_divisor must be implemented by concrete ClassGroup")

    class ElementMethods:
        r"""Class group element methods."""

        def lift(self: Any) -> Any:
            r"""Lift this class to a representative divisor in Div(X)."""
            return self.parent().lift_to_divisor(self)

    class MorphismMethods:
        r"""Class group morphism methods."""


def install_class_groups() -> None:
    r"""Register post-init hooks and installation for class groups."""
    pass
