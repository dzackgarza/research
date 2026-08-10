r"""Framed algebras over a base ring R.

A framed R-algebra is equipped with a chosen surjection from a free R-algebra on
a set S, exactly as a framed R-module is equipped with a surjection from a free
R-module on S.
"""

from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.map import Map
from sage.misc.abstract_method import abstract_method
from sage.structure.parent import Parent


class Algebras(OwnedCategoryOverBaseRing):
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
        # An associative unital algebra is a ring, and it joins the owned
        # hierarchy at that node like any other: this is what makes
        # \(R[x]^n\) the preamble's free module rather than Sage's.  Sage's
        # own algebra node says the same thing to Sage; saying it here is
        # what puts the owned ``__pow__`` ahead of the inherited one.
        return [SageAlgebras(self.base_ring()), OwnedRings()]

    class ParentMethods:
        def algebra_structure_map(self) -> "Morphism":
            """Return the explicit structure map from the base ring.

            Asked of the engine's copy of the ring: a coercion is registered
            from the ring this parent was constructed over, and the session's
            name for it is a different parent with no map of its own.
            """
            witness = self.coerce_map_from(engine_ring(self.base_ring()))
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
            # Both ends of the map cross to the engine to be compared: a
            # session names owned rings, so the map it obtained runs between
            # them, and only the engine's name is common to both spellings.
            assert engine_ring(ring_hom.domain()) == engine_ring(self.base_ring()), (
                "the map must have this algebra's base ring as domain"
            )
            if engine_ring(ring_hom.codomain()) == engine_ring(self.base_ring()):
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

class FramedAlgebras(OwnedCategoryOverBaseRing):
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


class OwnedAlgebra(OwnedBaseRing, Parent):
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
        # Intake: both ends of the presenting map cross to the engine.  The
        # map may be an owned one, whose ends are the rings a session named;
        # what is computed in is the ring the engine holds.
        base_ring = engine_ring(structure_map.domain())
        self._structure_map = structure_map
        self._engine = engine_ring(structure_map.codomain())
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

    def rank(self) -> "Integer":
        r"""Return the rank of \(A\) as a free module over its base ring."""
        return self._engine.rank()

    def is_commutative(self) -> bool:
        return self._engine.is_commutative()

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
