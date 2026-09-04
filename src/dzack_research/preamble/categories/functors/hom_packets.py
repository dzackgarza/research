r"""Functorial transport of Hom/End/Aut category packets."""

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CategoricalIsomorphism,
    Isomorphism,
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomArrowIdentity,
    category_packet,
)
from dzack_research.preamble.categories.functors.core import Functor


class InducedHomFunctor(Functor):
    r"""The functor ``Hom_C(A,B) -> Hom_D(F(A),F(B))`` induced by ``F``."""

    def __init__(self, functor, domain_object, codomain_object) -> None:
        self._functor = functor
        source = category_packet(functor.domain()).Homs().Of(
            domain_object,
            codomain_object,
        )
        target = category_packet(functor.codomain()).Homs().Of(
            functor.on_object(domain_object),
            functor.on_object(codomain_object),
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    @staticmethod
    def _underlying_arrow(value):
        try:
            return value.arrow()
        except AttributeError:
            return value

    def object_image(self, arrow_object):
        arrow = self._underlying_arrow(arrow_object)
        if arrow not in self.domain():
            raise TypeError(f"{arrow} is not an object of {self.domain()}")
        image = self.base_functor().on_morphism(arrow)
        if image not in self.codomain():
            raise TypeError(f"{image} is not an object of {self.codomain()}")
        return image

    def morphism_image(self, morphism):
        if not isinstance(morphism, HomArrowIdentity):
            raise TypeError(
                "the represented Hom categories currently have only identity 2-arrows"
            )
        source_image = self.on_object(morphism.domain())
        target_image = self.on_object(morphism.codomain())
        return self.codomain().two_hom(source_image, target_image).identity()

    def __call__(self, value):
        return (
            self.on_morphism(value)
            if isinstance(value, HomArrowIdentity)
            else self.on_object(value)
        )

    def _repr_(self):
        return f"Hom functor induced by {self.base_functor()}"


class InducedEndFunctor(Functor):
    r"""The functor ``End_C(A) -> End_D(F(A))`` induced by ``F``."""

    def __init__(self, functor, obj) -> None:
        self._functor = functor
        source = category_packet(functor.domain()).Ends().Of(obj)
        target = category_packet(functor.codomain()).Ends().Of(
            functor.on_object(obj)
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def object_image(self, arrow_object):
        arrow = InducedHomFunctor._underlying_arrow(arrow_object)
        image = self.base_functor().on_morphism(arrow)
        return self.codomain()(image)

    def morphism_image(self, morphism):
        if not isinstance(morphism, HomArrowIdentity):
            raise TypeError(
                "the represented End categories currently have only identity 2-arrows"
            )
        source_image = self.on_object(morphism.domain())
        target_image = self.on_object(morphism.codomain())
        return self.codomain().two_hom(source_image, target_image).identity()

    def __call__(self, value):
        return (
            self.on_morphism(value)
            if isinstance(value, HomArrowIdentity)
            else self.on_object(value)
        )

    def _repr_(self):
        return f"End functor induced by {self.base_functor()}"


class InducedAutFunctor(Functor):
    r"""The functor ``Aut_C(A) -> Aut_D(F(A))`` induced by ``F``."""

    def __init__(self, functor, obj) -> None:
        self._functor = functor
        source = category_packet(functor.domain()).Auts().Of(obj)
        target = category_packet(functor.codomain()).Auts().Of(
            functor.on_object(obj)
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def object_image(self, arrow_object):
        isomorphism = InducedHomFunctor._underlying_arrow(arrow_object)
        if not isinstance(isomorphism, CategoricalIsomorphism):
            raise TypeError("an Aut object is represented by a categorical isomorphism")
        forward = self.base_functor().on_morphism(isomorphism.forward())
        inverse = self.base_functor().on_morphism(isomorphism.inverse())
        return self.codomain()(_isomorphism_from_known_inverse_pair(forward, inverse))

    def morphism_image(self, morphism):
        if not isinstance(morphism, HomArrowIdentity):
            raise TypeError(
                "the represented Aut categories currently have only identity 2-arrows"
            )
        source_image = self.on_object(morphism.domain())
        target_image = self.on_object(morphism.codomain())
        return self.codomain().two_hom(source_image, target_image).identity()

    def __call__(self, value):
        return (
            self.on_morphism(value)
            if isinstance(value, HomArrowIdentity)
            else self.on_object(value)
        )

    def _repr_(self):
        return f"Aut functor induced by {self.base_functor()}"


def induced_hom_functor(functor, domain_object, codomain_object) -> InducedHomFunctor:
    return InducedHomFunctor(functor, domain_object, codomain_object)


def induced_end_functor(functor, obj) -> InducedEndFunctor:
    return InducedEndFunctor(functor, obj)


def induced_aut_functor(functor, obj) -> InducedAutFunctor:
    return InducedAutFunctor(functor, obj)


__all__ = [
    "InducedAutFunctor",
    "InducedEndFunctor",
    "InducedHomFunctor",
    "induced_aut_functor",
    "induced_end_functor",
    "induced_hom_functor",
]
