r"""Functorial transport of Mor/End/Aut category packets."""

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.functors.core import Functor


def _arrow_of(mor_category, arrow_object):
    r"""The arrow that an object of a Mor category is.

    The objects of ``Hom_C(A, B)`` are the arrows ``A -> B``; the Mor category
    presents one either as the arrow or as its arrow object.  Its discrete
    2-Mor at that object has the object as its source, normalized by the Mor
    category itself, so the arrow is read from there for either presentation.
    ``two_mor`` is the spelling both Mor-category shapes share and that no
    enrichment of the Mor object (a group of automorphisms, say) rebinds.
    """
    return mor_category.two_mor(arrow_object, arrow_object).domain().arrow()


def _identity_two_arrow_image(functor, two_arrow):
    r"""The image of a 2-arrow of a represented Mor category.

    Those Mor categories are discrete: the only 2-arrow on an arrow object is
    its identity, so the image is the identity on the image object.
    """
    assert two_arrow in functor.domain().two_mor(two_arrow.domain(), two_arrow.codomain()), (
        "a 2-arrow of a represented Mor category is the identity of its discrete 2-Mor"
    )
    source_image = functor.on_object(two_arrow.domain())
    target_image = functor.on_object(two_arrow.codomain())
    return functor.codomain().two_mor(source_image, target_image).identity()


class _InducedMorFunctor(Functor):
    r"""The induced ``Hom_C(A,B) -> Hom_D(F(A),F(B))`` for discrete fixed Mors.

    The target's constructor admits the image arrow and gives its selected
    representation: an element of an enriched Mor, or a constructed object
    of an unenriched fixed category.  Raw-arrow membership is not object
    placement in the latter.  The common functor action owns admission and
    caches both objects and identity 2-arrows, as for End and Aut below.
    The identity-only action does not supply the extra action required on
    nonidentity natural transformations in a represented functor category.
    """

    def __init__(self, functor, domain_object, codomain_object) -> None:
        self._functor = functor
        source = functor.domain().category_packet().Mors().Of(
            domain_object,
            codomain_object,
        )
        target = functor.codomain().category_packet().Mors().Of(
            functor.on_object(domain_object),
            functor.on_object(codomain_object),
        )
        super().__init__(source, target)

    def base_functor(self):
        return self._functor

    def _apply_object(self, arrow_object):
        image = self.base_functor().on_morphism(_arrow_of(self.domain(), arrow_object))
        return self.codomain()(image)

    def _apply_morphism(self, morphism):
        return _identity_two_arrow_image(self, morphism)

    def _repr_(self):
        return f"Mor functor induced by {self.base_functor()}"


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

    def _apply_object(self, arrow_object):
        image = self.base_functor().on_morphism(_arrow_of(self.domain(), arrow_object))
        return self.codomain()(image)

    def _apply_morphism(self, morphism):
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

    def _apply_object(self, arrow_object):
        isomorphism = _arrow_of(self.domain(), arrow_object)
        forward = self.base_functor().on_morphism(isomorphism.forward())
        inverse = self.base_functor().on_morphism(isomorphism.inverse())
        return self.codomain()(
            _isomorphism_from_known_inverse_pair(
                forward, inverse, base_category=self.codomain().base_category()
            )
        )

    def _apply_morphism(self, morphism):
        return _identity_two_arrow_image(self, morphism)

    def _repr_(self):
        return f"Aut functor induced by {self.base_functor()}"
