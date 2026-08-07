r"""Framed algebras over a base ring R.

A framed R-algebra is equipped with a chosen surjection from a free R-algebra on
a set S, exactly as a framed R-module is equipped with a surjection from a free
R-module on S.
"""

from sage.categories.category_types import Category_over_base_ring
from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.map import Map
from sage.misc.abstract_method import abstract_method
from sage.structure.parent import Parent


class Algebras(Category_over_base_ring):
    r"""Associative unital algebras over a base ring (R)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "algebras"

    def __contains__(self, algebra: "Parent") -> bool:
        """Return whether ``algebra`` is an explicit ``R``-algebra witness."""
        # Asked of Sage's category, not of its method with this category as
        # ``self``: this one is not one of Sage's, so its ``super()`` is not
        # Sage's either.
        if algebra in SageAlgebras(self.base_ring()):
            return True

        if not isinstance(algebra, Parent):
            return False

        return bool(algebra.coerce_map_from(self.base_ring()))

    def super_categories(self) -> list:
        return [SageAlgebras(self.base_ring())]

    class ParentMethods:
        def algebra_structure_map(self) -> "Morphism":
            """Return the explicit structure map from the base ring."""
            witness = self.coerce_map_from(self.base_ring())
            if not witness:
                assert False, f"{self} has no structure map from {self.base_ring()}"
            return witness

        def base_change(self, ring_hom: "Morphism") -> "Module":
            r"""Base change this algebra along a ring morphism."""
            # A coercion is a ring map that Sage spells as a ``Map`` and not
            # as a ``Morphism`` -- ``QQ -> CC`` arrives as a composite -- and
            # base change is along a ring map however it was obtained.
            assert isinstance(ring_hom, Map), (
                "base_change requires a ring map"
            )
            assert ring_hom.domain() == self.base_ring(), (
                "the map must have this algebra's base ring as domain"
            )
            if ring_hom.codomain() == self.base_ring():
                return self
            return self.change_ring(ring_hom.codomain())

        def is_algebra(self) -> bool:
            r"""Return whether this parent is declared to be an (R)-algebra."""
            return True

    class SubcategoryMethods:
        def Free(self):
            r"""Return the free-algebra subcategory over this base ring."""
            return FreeAlgebras(self.base_ring())

        def FinitelyPresented(self):
            from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
                FinitelyPresentedAlgebras,
            )
            return FinitelyPresentedAlgebras(self.base_ring())

class FramedAlgebras(Category_over_base_ring):
    r"""R-algebras carrying a specified surjection \(\operatorname{FreeAlg}_R(S) \to A\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed algebras"

    def super_categories(self) -> list:
        return [Algebras(self.base_ring()), FramedModules(self.base_ring())]

    class ParentMethods:

        @abstract_method
        def product_on_algebra_generators(self, s, t) -> object:
            r"""Return the product of algebra_generators labelled by s and t in S."""


class OwnedAlgebra(Parent):
    r"""The \(R\)-algebra a ring map \(R\to A\) presents, as an owned object.

    An \(R\)-algebra *is* that map, so it is the constructor's argument: one
    ring is an algebra over many bases, and \(\mathbb Q\) over \(\mathbb Z\)
    and \(\mathbb Q\) over \(\mathbb Q\) are two algebras that differ in
    nothing but their structure map.

    Constructed from the Sage ring rather than refined onto it, for the
    reason :class:`OwnedGroup` records: refinement gives a foreign parent
    methods that ask for data an owned constructor would have stored.  The
    engine crosses the boundary once, here, and is private afterwards.
    """

    def __init__(self, structure_map: "Map") -> None:
        assert isinstance(structure_map, Map), (
            "an algebra is presented by a ring map into it"
        )
        base_ring = structure_map.domain()
        self._structure_map = structure_map
        self._engine = structure_map.codomain()
        Parent.__init__(self, base=base_ring, category=Algebras(base_ring))

    def algebra_structure_map(self) -> "Map":
        return self._structure_map

    def change_ring(self, ring: "Ring") -> "OwnedAlgebra":
        return own_algebra(self._engine.base_extend(ring).coerce_map_from(ring))

    def _element_constructor_(self, value: "Element") -> "Element":
        return self._engine(value)

    def __contains__(self, value: "Element") -> bool:
        return value in self._engine

    def one(self) -> "Element":
        return self._engine.one()

    def zero(self) -> "Element":
        return self._engine.zero()

    def an_element(self) -> "Element":
        return self._engine.an_element()

    def __hash__(self) -> int:
        return hash((type(self), self._structure_map))

    def __eq__(self, other: object) -> bool:
        return (
            type(other) is type(self)
            and other._structure_map == self._structure_map
        )

    def _repr_(self) -> str:
        return f"{self._engine} as an algebra over {self.base_ring()}"


def own_algebra(structure_map: "Map") -> OwnedAlgebra:
    r"""Return the owned \(R\)-algebra the ring map ``structure_map`` presents."""
    return OwnedAlgebra(structure_map)


_ALGEBRAS_INSTALLED = False


def install_algebras() -> None:
    r"""Register post-init hooks and installation for algebras."""
    global _ALGEBRAS_INSTALLED

    if _ALGEBRAS_INSTALLED:
        return

    _ALGEBRAS_INSTALLED = True
