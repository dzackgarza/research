r"""Subtree for Cartier divisor groups under the divisors category tree.

A Cartier divisor group CartierDiv(X) is the group of global sections of K_X*/O_X* (locally principal divisors).
Without assuming smoothness, there is a canonical map phi: CartierDiv(X) -> WeilDiv(X).
"""

from typing import Any

from sage.categories.category import Category


class CartierDivisorGroupElement(Element):
    r"""Element of a Cartier divisor group (a Cartier divisor D)."""

    def to_picard_class(self: Any) -> Any:
        r"""Map this Cartier divisor to its class in Pic(X)."""
        return self.parent().canonical_projection()(self)

    def to_weil_divisor(self: Any) -> Any:
        r"""Map this Cartier divisor to its associated Weil divisor via phi: CartierDiv(X) -> WeilDiv(X)."""
        return self.parent().to_weil_divisor_morphism()(self)

    def is_principal(self: Any) -> bool:
        r"""Return whether this Cartier divisor is principal."""
        return self.to_picard_class().is_zero()


class CartierDivisorGroup(Parent):
    r"""A Cartier divisor group CartierDiv(X)."""

    Element = CartierDivisorGroupElement

    def __init__(self, base_ring: Any = ZZ) -> None:
        r"""Initialize the Cartier divisor group and refine into CartierDivisorGroups."""
        Parent.__init__(self, base=base_ring)
        refine(self, CartierDivisorGroups())


class CartierDivisorGroupMorphism(Morphism):
    r"""Morphism of Cartier divisor groups."""


class CartierDivisorGroups(Category):
    r"""Category of Cartier divisor groups."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "cartier divisor groups"

    def super_categories(self) -> list:
        r"""Return Modules(ZZ), of which Cartier divisor groups are modules."""
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Cartier divisor group parent methods."""

        def picard_group(self: Any) -> Any:
            r"""Return the associated Picard group Pic(X) = CartierDiv(X) / Prin(X)."""
            raise NotImplementedError("picard_group must be implemented by concrete CartierDivisorGroup")

        def canonical_projection(self: Any) -> Any:
            r"""Return the canonical projection morphism CartierDiv(X) -> Pic(X)."""
            raise NotImplementedError("canonical_projection must be implemented by concrete CartierDivisorGroup")

        def to_weil_divisor_morphism(self: Any) -> Any:
            r"""Return the canonical homomorphism phi: CartierDiv(X) -> WeilDiv(X)."""
            raise NotImplementedError("to_weil_divisor_morphism must be implemented by concrete CartierDivisorGroup")

    class ElementMethods:
        r"""Cartier divisor group element methods."""

        def to_picard_class(self: Any) -> Any:
            r"""Map this Cartier divisor to its class in Pic(X)."""
            return self.parent().canonical_projection()(self)

        def to_weil_divisor(self: Any) -> Any:
            r"""Map this Cartier divisor to its associated Weil divisor."""
            return self.parent().to_weil_divisor_morphism()(self)

        def is_principal(self: Any) -> bool:
            r"""Return whether this Cartier divisor is principal."""
            return self.to_picard_class().is_zero()

    class MorphismMethods:
        r"""Cartier divisor group morphism methods."""


def install_cartier_divisor_groups() -> None:
    r"""Register post-init hooks and installation for Cartier divisor groups."""
    pass
