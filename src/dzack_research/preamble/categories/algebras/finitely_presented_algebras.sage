r"""Finitely presented algebras as framed free-algebra quotients."""

from collections.abc import Iterable
from typing import Any, TYPE_CHECKING

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.map import Map
from sage.rings.ideal import Ideal_generic
from sage.structure.parent import Parent

from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


class FinitelyPresentedAlgebras(Category_over_base_ring):
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

        def presentation(self) -> tuple[Any, Any]:
            return (self._presentation_ring, self._presentation_ideal)

        def presentation_ring(self) -> "Parent":
            return self._presentation_ring

        def presentation_ideal(self) -> "Parent":
            return self._presentation_ideal

        def relations(self) -> "OrderedSet":
            return tuple(self._presentation_generators)

        def _base_change_relation(
            self,
            relation: "Element",
            ring_hom: "Morphism",
            target_presentation_ring: "Parent",
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

        def base_change(self, ring_hom: "Morphism") -> "Module":
            """Transport this finitely presented algebra along a base-ring map."""
            assert isinstance(ring_hom, Map), (
                "base_change requires a ring map from the algebra base ring"
            )
            assert ring_hom.domain() == self.base_ring(), (
                "base-change map must have this algebra's base ring as domain"
            )
            if ring_hom.codomain() == self.base_ring():
                return self

            target_base = ring_hom.codomain()
            target_presentation = FreeAlgebraOn(target_base, self.algebra_generating_set())
            relations = tuple(
                self._base_change_relation(relation, ring_hom, target_presentation)
                for relation in self.relations()
            )
            return FinitelyPresentedAlgebra(target_presentation, relations)

        def algebra_generating_set(self) -> "OrderedSet":
            return self.presentation_ring().algebra_generating_set()

        def algebra_generator_morphism(self) -> SetMorphism:
            return self._algebra_generator_morphism

        def algebra_generator(self, label: "Element") -> "Element":
            return self.algebra_generator_morphism()._call_(label)

        def algebra_generators(self) -> "OrderedSet":
            assert self.algebra_generating_set() in Sets().Finite(), (
                "algebra_generators() enumerates only finitely generated algebras"
            )
            return tuple(
                self.algebra_generator(label)
                for label in self.algebra_generating_set()
            )

        def algebra_presentation_morphism(self) -> SetMorphism:
            return self._algebra_presentation_morphism

        def algebra_framing_morphism(self) -> SetMorphism:
            return self._algebra_presentation_morphism


class FramedFGAlgebras(Category_over_base_ring):
    r"""Framed algebras with a finite algebra generating set.

    Not a super category of :class:`FinitelyPresentedAlgebras` and a
    subcategory of it at once: a finite presentation is a finite generating
    set *plus* finitely many relations, so the containment runs one way and
    the reverse edge was a cycle in the poset.
    """

    def super_categories(self) -> list:
        return [FramedAlgebras(self.base_ring())]


_FINITELY_PRESENTED_ALGEBRAS_INSTALLED = False


def _ideal_module_generators(relation_ideal: "Parent") -> "OrderedSet":
    assert isinstance(relation_ideal, Ideal_generic), (
        "relations must be an ideal in the presenting parent"
    )
    return tuple(relation_ideal.gen(i) for i in range(relation_ideal.ngens()))


def _relations_to_ideal(presentation_ring: "Parent", relations: "MorphismMatrix") -> tuple[Any, tuple[Any, ...]]:
    if isinstance(relations, Ideal_generic):
        assert relations.ring() is presentation_ring, (
            "relations must lie in the presenting free algebra"
        )
        return relations, _ideal_module_generators(relations)

    assert isinstance(relations, Iterable), (
        "relations must be an ideal, or an iterable of relation elements"
    )
    relation_generators = tuple(relations)
    return presentation_ring.ideal(relation_generators), relation_generators


def FinitelyPresentedAlgebra(presentation_ring: "Parent", relations: "MorphismMatrix") -> "Parent":
    """Present an algebra as ``presentation_ring/relations`` and expose the data."""
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

    return refine(quotient, FinitelyPresentedAlgebras(presentation_ring.base_ring()))


def FGAlgebra(base_ring: "Ring", algebra_generating_set: "OrderedSet", relations: "MorphismMatrix") -> "Parent":
    """Construct ``FreeAlgebraOn(base_ring, algebra_generating_set) / (relations)``."""
    free = FreeAlgebraOn(base_ring, algebra_generating_set)
    return FinitelyPresentedAlgebra(free, relations)


def install_finitely_presented_algebras() -> None:
    """No-op install hook placeholder for the finitely presented algebra layer."""
    global _FINITELY_PRESENTED_ALGEBRAS_INSTALLED
    if _FINITELY_PRESENTED_ALGEBRAS_INSTALLED:
        return

    _FINITELY_PRESENTED_ALGEBRAS_INSTALLED = True
