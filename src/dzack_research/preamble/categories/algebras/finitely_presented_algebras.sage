r"""Finitely presented algebras as framed free-algebra quotients."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import Module
    from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from collections.abc import Iterable
from typing import Protocol, TYPE_CHECKING

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.map import Map
from sage.misc.cachefunc import cached_method
from sage.rings.ideal import Ideal_generic
from sage.structure.parent import Parent

from sage.categories.rings import Rings as SageRings

from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    # What this node requires of the two parents a presentation runs
    # between.  Sage binds ``ParentMethods`` onto a parent by COPYING the
    # methods into a dynamic class, so the object a method runs on is never
    # an instance of the class the method is written in: ``self`` is
    # annotated with what its placement gives it.

    class PresentingAlgebraParent(Protocol):
        r"""The free algebra a presentation is a quotient of.

        It names the generating set \(S\), and it forms the quotient by an
        ideal of relations -- which is what a finite presentation is.
        """

        def base_ring(self) -> "Ring": ...
        def zero(self) -> "Element": ...
        def one(self) -> "Element": ...
        def algebra_generating_set(self) -> "OrderedSet": ...
        def algebra_generator(self, label: "Element") -> "Element": ...
        def module_generator(self, monomial: "Element") -> "Element": ...
        def product_on_algebra_generators(
            self, s: "Element", t: "Element"
        ) -> "Element": ...
        def ideal(self, generators: "OrderedSet") -> "Ideal_generic": ...
        def quotient(self, relations: "Ideal_generic") -> "PresentedAlgebraParent": ...
        def hom(
            self, images: dict, codomain: "PresentedAlgebraParent"
        ) -> "Morphism": ...

    class PresentedAlgebraParent(Protocol):
        r"""A parent in ``FinitelyPresentedAlgebras(R)``: the quotient, once
        :func:`FinitelyPresentedAlgebra` has bound the presentation onto it.
        """

        _presentation_ring: "PresentingAlgebraParent"
        _presentation_ideal: "Ideal_generic"
        _presentation_generators: tuple["Element", ...]
        _algebra_generator_morphism: SetMorphism
        _algebra_presentation_morphism: "Morphism"

        def __call__(self, representative: "Element") -> "Element": ...
        def base_ring(self) -> "Ring": ...
        def relations(self) -> "OrderedSet": ...
        def algebra_generating_set(self) -> "OrderedSet": ...
        def algebra_generator(self, label: "Element") -> "Element": ...
        def algebra_generator_morphism(self) -> SetMorphism: ...
        def algebra_presentation_morphism(self) -> "Morphism": ...
        def presentation_ring(self) -> "PresentingAlgebraParent": ...
        def _base_change_relation(
            self,
            relation: "Element",
            ring_hom: "Morphism",
            target_presentation_ring: "PresentingAlgebraParent",
        ) -> "Element": ...


class FinitelyPresentedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras presented as a quotient of a free algebra by finitely many relations."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented algebras"

    def super_categories(self) -> list:
        return [
            FramedFGAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True

        def presentation(
            self: "PresentedAlgebraParent",
        ) -> tuple["PresentingAlgebraParent", "Ideal_generic"]:
            return (self._presentation_ring, self._presentation_ideal)

        def presentation_ring(
            self: "PresentedAlgebraParent",
        ) -> "PresentingAlgebraParent":
            return self._presentation_ring

        def presentation_ideal(self: "PresentedAlgebraParent") -> "Ideal_generic":
            return self._presentation_ideal

        def relations(self: "PresentedAlgebraParent") -> "OrderedSet":
            return tuple(self._presentation_generators)

        def _base_change_relation(
            self,
            relation: "Element",
            ring_hom: "Morphism",
            target_presentation_ring: "PresentingAlgebraParent",
        ) -> "Element":
            mapped_relation = target_presentation_ring.zero()
            assert isinstance(ring_hom, Map), (
                "base map must be a ring map"
            )
            for monomial, coefficient in relation.coefficients().items():
                monomial_image = target_presentation_ring.one()
                for label, exponent in monomial.dict().items():
                    factor = target_presentation_ring.algebra_generator(label)
                    monomial_image *= factor**exponent
                mapped_relation += ring_hom(coefficient) * monomial_image
            return mapped_relation

        def base_change(
            self: "PresentedAlgebraParent", ring_hom: "Morphism"
        ) -> "Module":
            """Transport this finitely presented algebra along a base-ring map."""
            # Local: both modules import this one, so module-level imports
            # here would close those cycles; they are built by call time.
            from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn
            from dzack_research.preamble.categories.rings.rings import engine_ring

            assert isinstance(ring_hom, Map), (
                "base_change requires a ring map from the algebra base ring"
            )
            # Both ends of the map cross to the engine to be compared.  A
            # session names owned rings, so the map it obtained runs between
            # them; the ring a map is *between* is the same ring either way,
            # and only the engine's name for it is common to both spellings.
            assert engine_ring(ring_hom.domain()) == engine_ring(self.base_ring()), (
                "base-change map must have this algebra's base ring as domain"
            )
            if engine_ring(ring_hom.codomain()) == engine_ring(self.base_ring()):
                return self

            target_base = ring_hom.codomain()
            target_presentation = FreeAlgebraOn(target_base, self.algebra_generating_set())
            relations = tuple(
                self._base_change_relation(relation, ring_hom, target_presentation)
                for relation in self.relations()
            )
            return FinitelyPresentedAlgebra(target_presentation, relations)

        def algebra_generating_set(self: "PresentedAlgebraParent") -> "OrderedSet":
            return self.presentation_ring().algebra_generating_set()

        def algebra_generator_morphism(
            self: "PresentedAlgebraParent",
        ) -> SetMorphism:
            return self._algebra_generator_morphism

        def algebra_generator(
            self: "PresentedAlgebraParent", label: "Element"
        ) -> "Element":
            return self.algebra_generator_morphism()._call_(label)

        def algebra_generators(self: "PresentedAlgebraParent") -> "OrderedSet":
            assert self.algebra_generating_set() in Sets().Finite(), (
                "algebra_generators() enumerates only finitely generated algebras"
            )
            return tuple(
                self.algebra_generator(label)
                for label in self.algebra_generating_set()
            )

        def algebra_presentation_morphism(
            self: "PresentedAlgebraParent",
        ) -> "Morphism":
            return self._algebra_presentation_morphism

        def algebra_framing_morphism(
            self: "PresentedAlgebraParent",
        ) -> "Morphism":
            return self._algebra_presentation_morphism

        @cached_method
        def framing_morphism(self: "PresentedAlgebraParent") -> "FramingMorphism":
            r"""Return the module framing \(F_R(\operatorname{Mon}(S))\to A\).

            The presentation *is* the framing.  The cover is free on the
            monomials in \(S\) as a module, and \(\pi:F\to F/I\) is surjective
            by construction, so the framing of \(A\) is the cover's framing
            followed by \(\pi\): each monomial goes to its own class.  That
            class is already reduced, since the quotient constructs its
            elements through the ideal's normal form.
            """
            # Local: at module level this closes an import cycle; the morphism
            # module is built by the time a presented algebra is refined.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism

            cover = self.presentation_ring()
            return framing_morphism(
                cover,
                self,
                lambda monomial: self(cover.module_generator(monomial)),
            )

        def product_on_algebra_generators(
            self: "PresentedAlgebraParent", s: "Element", t: "Element"
        ) -> "Element":
            r"""Return the product of the algebra generators labelled \(s,t\).

            The projection is an algebra map, so the product of the images is
            the image of the product: the cover multiplies its own generators,
            and \(A\) reads the answer through \(\pi\).
            """
            return self.algebra_presentation_morphism()(
                self.presentation_ring().product_on_algebra_generators(s, t)
            )


class FramedFGAlgebras(OwnedCategoryOverBaseRing):
    r"""Framed algebras with a finite algebra generating set.

    Not a super category of :class:`FinitelyPresentedAlgebras` and a
    subcategory of it at once: a finite presentation is a finite generating
    set *plus* finitely many relations, so the containment runs one way and
    the reverse edge was a cycle in the poset.
    """

    def super_categories(self) -> list:
        # Local: algebras imports this module, so a module-level import here
        # would close that cycle; it is built by the time this runs.
        from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras

        return [FramedAlgebras(self.base_ring())]


_FINITELY_PRESENTED_ALGEBRAS_INSTALLED = False


def _ideal_module_generators(relation_ideal: "Ideal_generic") -> "OrderedSet":
    assert isinstance(relation_ideal, Ideal_generic), (
        "relations must be an ideal in the presenting parent"
    )
    return tuple(relation_ideal.gen(i) for i in range(relation_ideal.ngens()))


def _relations_to_ideal(
    presentation_ring: "PresentingAlgebraParent",
    relations: "Ideal_generic | Iterable[Element]",
) -> tuple["Ideal_generic", tuple["Element", ...]]:
    if isinstance(relations, Ideal_generic):
        # ``Ideal_generic.ring()`` reports the ring an ideal was formed in,
        # which for these relations is the presenting algebra itself.
        ideal_ring: "PresentingAlgebraParent | Parent" = relations.ring()
        assert ideal_ring is presentation_ring, (
            "relations must lie in the presenting free algebra"
        )
        return relations, _ideal_module_generators(relations)

    assert isinstance(relations, Iterable), (
        "relations must be an ideal, or an iterable of relation elements"
    )
    relation_generators = tuple(relations)
    return presentation_ring.ideal(relation_generators), relation_generators


def FinitelyPresentedAlgebra(
    presentation_ring: "PresentingAlgebraParent", relations: "MorphismMatrix"
) -> "Parent":
    """Present an algebra as ``presentation_ring/relations`` and expose the data."""
    # Local: free_algebras imports this module, so a module-level import here
    # would close that cycle; both are built by the time this runs.
    from dzack_research.preamble.categories.algebras.free_algebras import FreeAlgebras
    from dzack_research.preamble.refine import refine

    assert isinstance(presentation_ring, Parent), (
        "a finitely presented algebra starts from a parent"
    )
    assert presentation_ring in FreeAlgebras(presentation_ring.base_ring()), (
        "a finitely presented algebra must be presented by a free algebra"
    )
    assert presentation_ring.algebra_generating_set() in Sets().Finite(), (
        "a finitely presented algebra requires finitely many generators"
    )

    presentation_ideal, relation_generators = _relations_to_ideal(
        presentation_ring, relations
    )
    quotient = presentation_ring.quotient(presentation_ideal)
    quotient._presentation_generators = relation_generators

    quotient._presentation_ring = presentation_ring
    quotient._presentation_ideal = presentation_ideal
    generator_set = presentation_ring.algebra_generating_set()
    quotient._algebra_generator_morphism = SetMorphism(
        Hom(
            generator_set,
            UnderlyingSet(quotient),
            Sets(),
        ),
        lambda label: quotient(presentation_ring.algebra_generator(label)),
    )
    quotient._algebra_presentation_morphism = presentation_ring.hom(
        {
            label: quotient(presentation_ring.algebra_generator(label))
            for label in generator_set
        },
        quotient,
    )

    presented: "Parent" = refine(
        quotient, FinitelyPresentedAlgebras(presentation_ring.base_ring())
    )
    return presented


def FGAlgebra(base_ring: "Ring", algebra_generating_set: "OrderedSet", relations: "MorphismMatrix") -> "Parent":
    """Construct ``FreeAlgebraOn(base_ring, algebra_generating_set) / (relations)``."""
    # Local: framed_free_algebras imports this module, so a module-level
    # import here would close that cycle.
    from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn

    free = FreeAlgebraOn(base_ring, algebra_generating_set)
    return FinitelyPresentedAlgebra(free, relations)


def install_finitely_presented_algebras() -> None:
    """No-op install hook placeholder for the finitely presented algebra layer."""
    global _FINITELY_PRESENTED_ALGEBRAS_INSTALLED
    if _FINITELY_PRESENTED_ALGEBRAS_INSTALLED:
        return

    _FINITELY_PRESENTED_ALGEBRAS_INSTALLED = True


install_finitely_presented_algebras()
