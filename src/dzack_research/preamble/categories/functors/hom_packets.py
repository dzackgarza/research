r"""Functorial transport of Hom/End/Aut category packets."""

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.functors.core import Functor


def _arrow_of(hom_category, arrow_object):
    r"""The arrow that an object of a Hom category is.

    The objects of ``Hom_C(A, B)`` are the arrows ``A -> B``; the Hom category
    presents one either as the arrow or as its arrow object.  Its discrete
    2-Hom at that object has the object as its source, normalized by the Hom
    category itself, so the arrow is read from there for either presentation.
    ``two_hom`` is the spelling both Hom-category shapes share and that no
    enrichment of the Hom object (a group of automorphisms, say) rebinds.
    """
    return hom_category.two_hom(arrow_object, arrow_object).domain().arrow()


def _identity_two_arrow_image(functor, two_arrow):
    r"""The image of a 2-arrow of a represented Hom category.

    Those Hom categories are discrete: the only 2-arrow on an arrow object is
    its identity, so the image is the identity on the image object.
    """
    assert two_arrow in functor.domain().two_hom(two_arrow.domain(), two_arrow.codomain()), (
        "a 2-arrow of a represented Hom category is the identity of its discrete 2-Hom"
    )
    source_image = functor.on_object(two_arrow.domain())
    target_image = functor.on_object(two_arrow.codomain())
    return functor.codomain().two_hom(source_image, target_image).identity()


class _InducedHomFunctor(Functor):
    r"""The functor ``Hom_C(A,B) -> Hom_D(F(A),F(B))`` induced by ``F``."""

    def __init__(self, functor, domain_object, codomain_object) -> None:
        self._functor = functor
        source = functor.domain().category_packet().Homs().Of(
            domain_object,
            codomain_object,
        )
        target = functor.codomain().category_packet().Homs().Of(
            functor.on_object(domain_object),
            functor.on_object(codomain_object),
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def object_image(self, arrow_object):
        if arrow_object not in self.domain():
            raise TypeError(f"{arrow_object} is not an object of {self.domain()}")
        image = self.base_functor().on_morphism(_arrow_of(self.domain(), arrow_object))
        if image not in self.codomain():
            raise TypeError(f"{image} is not an object of {self.codomain()}")
        return image

    def morphism_image(self, morphism):
        return _identity_two_arrow_image(self, morphism)

    def _repr_(self):
        return f"Hom functor induced by {self.base_functor()}"


class _InducedEndFunctor(Functor):
    r"""The functor ``End_C(A) -> End_D(F(A))`` induced by ``F``."""

    def __init__(self, functor, obj) -> None:
        self._functor = functor
        source = functor.domain().category_packet().Ends().Of(obj)
        target = functor.codomain().category_packet().Ends().Of(
            functor.on_object(obj)
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def object_image(self, arrow_object):
        if arrow_object not in self.domain():
            raise TypeError(f"{arrow_object} is not an object of {self.domain()}")
        image = self.base_functor().on_morphism(_arrow_of(self.domain(), arrow_object))
        return self.codomain()(image)

    def morphism_image(self, morphism):
        return _identity_two_arrow_image(self, morphism)

    def _repr_(self):
        return f"End functor induced by {self.base_functor()}"


class _InducedAutFunctor(Functor):
    r"""The functor ``Aut_C(A) -> Aut_D(F(A))`` induced by ``F``.

    An object of ``Aut_C(A)`` is an isomorphism, the pair of mutually inverse
    arrows; a functor preserves inverses, so the image pair is again one.
    """

    def __init__(self, functor, obj) -> None:
        self._functor = functor
        source = functor.domain().category_packet().Auts().Of(obj)
        target = functor.codomain().category_packet().Auts().Of(
            functor.on_object(obj)
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def object_image(self, arrow_object):
        if arrow_object not in self.domain():
            raise TypeError(f"{arrow_object} is not an automorphism in {self.domain()}")
        isomorphism = _arrow_of(self.domain(), arrow_object)
        forward = self.base_functor().on_morphism(isomorphism.forward())
        inverse = self.base_functor().on_morphism(isomorphism.inverse())
        return self.codomain()(_isomorphism_from_known_inverse_pair(forward, inverse))

    def morphism_image(self, morphism):
        return _identity_two_arrow_image(self, morphism)

    def _repr_(self):
        return f"Aut functor induced by {self.base_functor()}"
