r"""Subtree for Weil class groups under the divisors category tree.

A Weil class group Cl(X) = WeilDiv(X) / Prin(X) is represented as a cokernel in formed modules:
the cokernel of the principal Weil divisor inclusion p_Weil: Prin(X) -> WeilDiv(X).
"""

from typing import Any

from sage.categories.category import Category


def ClassGroup(formed: Any) -> FormModule:
    r"""Refine a formed cokernel as a Weil class group."""
    assert isinstance(formed, FormModule), "ClassGroup requires a formed module"
    refine(formed, ClassGroups())
    formed._initialize_framing()
    return formed


class ClassGroups(Category):
    r"""Category of class groups (represented as formed module cokernels)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "class groups"

    def super_categories(self) -> list:
        r"""Return FormModules(), of which class groups are formed module cokernels."""
        return [FormModules()]

    class ParentMethods:
        r"""Class group parent methods."""

        def presentation(self: Any) -> Any:
            r"""Return the presentation morphism p_Weil: Prin(X) -> WeilDiv(X)."""
            return self.forget_form().presentation()

        def weil_divisor_group(self: Any) -> Any:
            r"""Return the associated Weil divisor group WeilDiv(X)."""
            return self.presentation().codomain()

        def canonical_projection(self: Any) -> Any:
            r"""Return the canonical projection morphism WeilDiv(X) -> Cl(X)."""
            return self.weil_divisor_group().canonical_projection()

        def lift_to_divisor(self: Any, element: Any) -> Any:
            r"""Lift a class to a representative Weil divisor in WeilDiv(X)."""
            raise NotImplementedError("lift_to_divisor must be implemented by concrete ClassGroup")

    class ElementMethods:
        r"""Class group element methods."""

        def lift(self: Any) -> Any:
            r"""Lift this class to a representative Weil divisor in WeilDiv(X)."""
            return self.parent().lift_to_divisor(self)

    class MorphismMethods:
        r"""Class group morphism methods."""


def install_class_groups() -> None:
    r"""Register post-init hooks and installation for class groups."""
    pass
