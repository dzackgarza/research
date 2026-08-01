r"""Subtree for Picard groups under the divisors category tree.

A Picard group Pic(X) = CartierDiv(X) / Prin(X) is represented as a cokernel in formed modules:
the cokernel of the principal Cartier divisor inclusion p_Cartier: Prin(X) -> CartierDiv(X).

Without assuming smoothness, the canonical map CartierDiv(X) -> WeilDiv(X) induces the canonical map
bar_phi: Pic(X) -> Cl(X) mapping line bundle / Cartier classes to Weil divisor classes.
"""

from typing import Any

from sage.categories.category import Category


def PicardGroup(formed: Any) -> FormModule:
    r"""Refine a formed cokernel as a Picard group."""
    assert isinstance(formed, FormModule), "PicardGroup requires a formed module"
    refine(formed, PicardGroups())
    formed._initialize_framing()
    return formed


class PicardGroups(Category):
    r"""Category of Picard groups (represented as formed module cokernels)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "picard groups"

    def super_categories(self) -> list:
        r"""Return FormModules(), of which Picard groups are formed module cokernels."""
        return [FormModules()]

    class ParentMethods:
        r"""Picard-specific parent methods."""

        def picard_number(self: Any) -> Any:
            r"""Return the Picard number $\rho(X)$ (alias for rank)."""
            return self.forget_form().rank()

        def presentation(self: Any) -> Any:
            r"""Return the presentation morphism p_Cartier: Prin(X) -> CartierDiv(X)."""
            return self.forget_form().presentation()

        def cartier_divisor_group(self: Any) -> Any:
            r"""Return the associated Cartier divisor group CartierDiv(X)."""
            return self.presentation().codomain()

        def to_class_group_morphism(self: Any) -> Any:
            r"""Return the canonical induced homomorphism bar_phi: Pic(X) -> Cl(X)."""
            raise NotImplementedError("to_class_group_morphism must be implemented by concrete PicardGroup")

    class ElementMethods:
        r"""Picard-specific element methods."""

        def intersection(self: Any, other: Any) -> Any:
            r"""Return $D_1 \cdot D_2$."""
            return self.b(other)

        def self_intersection(self: Any) -> Any:
            r"""Return $D^2$."""
            return self.norm()

        def to_class_group_class(self: Any) -> Any:
            r"""Map this class in Pic(X) to its Weil divisor class in Cl(X)."""
            return self.parent().to_class_group_morphism()(self)

    class MorphismMethods:
        r"""Picard-specific morphism methods."""


def install_picard_groups() -> None:
    r"""Register post-init hooks and installation for Picard groups."""
    pass
