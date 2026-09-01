r"""Functors, natural transformations, and adjunctions.

These are deliberately small mathematical objects.  The existing Sage/owned
categories remain the domain and codomain; this module adds no parallel
category graph and no registry of relationships.
"""

from sage.categories.morphism import Morphism
from sage.structure.sage_object import SageObject


class Functor(SageObject):
    r"""A functor with explicit actions on objects and morphisms."""

    def __init__(self, domain, codomain) -> None:
        self._domain = domain
        self._codomain = codomain
        self._object_images: dict[int, tuple[object, object]] = {}

    def _cache_key(self):
        r"""Functors have identity semantics as parameters of categorical constructions."""
        return id(self)

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def _apply_object(self, obj):
        raise NotImplementedError("a functor must specify its action on objects")

    def _apply_morphism(self, morphism):
        raise NotImplementedError("a functor must specify its action on morphisms")

    def object_image(self, obj):
        if obj not in self.domain():
            raise TypeError(f"{obj} is not an object of {self.domain()}")
        key = id(obj)
        cached = self._object_images.get(key)
        if cached is not None and cached[0] is obj:
            return cached[1]
        image = self._apply_object(obj)
        if image not in self.codomain():
            raise TypeError(
                f"the image of {obj} under {self} is not an object of {self.codomain()}"
            )
        self._object_images[key] = (obj, image)
        return image

    def on_object(self, obj):
        return self.object_image(obj)

    def morphism_image(self, morphism):
        if not isinstance(morphism, Morphism):
            raise TypeError("a functor acts on a morphism through its morphism action")
        domain = self.object_image(morphism.domain())
        codomain = self.object_image(morphism.codomain())
        image = self._apply_morphism(morphism)
        if image.domain() is not domain or image.codomain() is not codomain:
            raise ValueError(
                "a functor's morphism image must run between the cached images "
                "of the original domain and codomain"
            )
        return image

    def on_morphism(self, morphism):
        return self.morphism_image(morphism)

    def __call__(self, value):
        return self.morphism_image(value) if isinstance(value, Morphism) else self.object_image(value)

    def then(self, other):
        r"""Return ``other ∘ self``."""
        return CompositeFunctor(self, other)

    def factors(self):
        return (self,)

    def is_faithful(self) -> bool:
        return bool(getattr(self, "_faithful", False))

    def Image(self):
        r"""Return the category of outputs equipped with chosen preimages."""
        from dzack_research.preamble.categories.abstract_categories.functor_images import (
            ImageOfFunctor,
        )

        return ImageOfFunctor(self)

    def on_hom(self, domain_object, codomain_object):
        r"""Return the induced functor on the fixed-endpoint Hom categories."""
        from dzack_research.preamble.categories.functors.hom_packets import (
            induced_hom_functor,
        )

        return induced_hom_functor(self, domain_object, codomain_object)

    def on_end(self, obj):
        r"""Return the induced functor on endomorphism categories."""
        from dzack_research.preamble.categories.functors.hom_packets import (
            induced_end_functor,
        )

        return induced_end_functor(self, obj)

    def on_aut(self, obj):
        r"""Return the induced functor on automorphism categories."""
        from dzack_research.preamble.categories.functors.hom_packets import (
            induced_aut_functor,
        )

        return induced_aut_functor(self, obj)


class ContravariantFunctor(SageObject):
    r"""A contravariant functor ``C -> D``, equivalently ``C^op -> D``."""

    def __init__(self, domain, codomain) -> None:
        self._domain = domain
        self._codomain = codomain
        self._object_images = {}

    def _cache_key(self):
        return id(self)

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def _apply_object(self, obj):
        raise NotImplementedError

    def _apply_morphism(self, morphism):
        raise NotImplementedError

    def object_image(self, obj):
        if obj not in self.domain():
            raise TypeError(f"{obj} is not an object of {self.domain()}")
        key = id(obj)
        cached = self._object_images.get(key)
        if cached is not None and cached[0] is obj:
            return cached[1]
        image = self._apply_object(obj)
        if image not in self.codomain():
            raise TypeError(f"{image} is not an object of {self.codomain()}")
        self._object_images[key] = (obj, image)
        return image

    def morphism_image(self, morphism):
        if not isinstance(morphism, Morphism):
            raise TypeError("a contravariant functor acts on morphisms")
        source_image = self.object_image(morphism.codomain())
        target_image = self.object_image(morphism.domain())
        image = self._apply_morphism(morphism)
        if image.domain() is not source_image or image.codomain() is not target_image:
            raise ValueError(
                "a contravariant morphism image must reverse the cached object images"
            )
        return image

    def __call__(self, value):
        return self.morphism_image(value) if isinstance(value, Morphism) else self.object_image(value)


class Bifunctor(SageObject):
    r"""A functor ``C x D -> E`` with a two-argument object/morphism API."""

    def __init__(self, left_domain, right_domain, codomain) -> None:
        self._left_domain = left_domain
        self._right_domain = right_domain
        self._codomain = codomain
        self._object_images = {}

    def _cache_key(self):
        return id(self)

    def left_domain(self):
        return self._left_domain

    def right_domain(self):
        return self._right_domain

    def codomain(self):
        return self._codomain

    def _apply_object(self, left, right):
        raise NotImplementedError

    def _apply_morphism(self, left_morphism, right_morphism):
        raise NotImplementedError

    def object_image(self, left, right):
        if left not in self.left_domain() or right not in self.right_domain():
            raise TypeError("the bifunctor arguments lie outside its product domain")
        key = (id(left), id(right))
        cached = self._object_images.get(key)
        if cached is not None and cached[0] is left and cached[1] is right:
            return cached[2]
        image = self._apply_object(left, right)
        if image not in self.codomain():
            raise TypeError(f"{image} is not an object of {self.codomain()}")
        self._object_images[key] = (left, right, image)
        return image

    def morphism_image(self, left_morphism, right_morphism):
        if not isinstance(left_morphism, Morphism) or not isinstance(right_morphism, Morphism):
            raise TypeError("a bifunctor acts on a pair of morphisms")
        source = self.object_image(left_morphism.domain(), right_morphism.domain())
        target = self.object_image(left_morphism.codomain(), right_morphism.codomain())
        image = self._apply_morphism(left_morphism, right_morphism)
        if image.domain() is not source or image.codomain() is not target:
            raise ValueError("a bifunctor morphism image has the wrong cached endpoints")
        return image

    def __call__(self, left, right):
        if isinstance(left, Morphism) or isinstance(right, Morphism):
            return self.morphism_image(left, right)
        return self.object_image(left, right)


class IdentityFunctor(Functor):
    def __init__(self, category) -> None:
        super().__init__(category, category)

    def _apply_object(self, obj):
        return obj

    def _apply_morphism(self, morphism):
        return morphism

    def factors(self):
        return ()

    def is_faithful(self) -> bool:
        return True

    def _repr_(self):
        return f"Identity functor of {self.domain()}"


class CategoryInclusionFunctor(Functor):
    r"""The canonical functor along a declared subcategory inclusion.

    If ``C`` is a subcategory of ``D``, every object and morphism of ``C`` is
    already an object and morphism of ``D``.  The functor therefore changes
    only the category in which the same mathematical data is read.
    """

    _faithful = True

    def __init__(self, subcategory, supercategory) -> None:
        if not subcategory.is_subcategory(supercategory):
            raise ValueError(f"{subcategory} is not a subcategory of {supercategory}")
        super().__init__(subcategory, supercategory)

    def _apply_object(self, obj):
        return obj

    def _apply_morphism(self, morphism):
        return morphism

    def _repr_(self):
        return f"Inclusion {self.domain()} -> {self.codomain()}"


def category_inclusion(subcategory, supercategory) -> CategoryInclusionFunctor:
    r"""Return the canonical functor attached to ``subcategory <= supercategory``."""
    return CategoryInclusionFunctor(subcategory, supercategory)


class CompositeFunctor(Functor):
    r"""The composite ``second ∘ first``."""

    def __init__(self, first: Functor, second: Functor) -> None:
        if first.codomain() != second.domain():
            raise ValueError("functor composition requires matching middle categories")
        self._first = first
        self._second = second
        super().__init__(first.domain(), second.codomain())

    def _apply_object(self, obj):
        return self._second(self._first(obj))

    def _apply_morphism(self, morphism):
        return self._second(self._first(morphism))

    def factors(self):
        return self._first.factors() + self._second.factors()

    def is_faithful(self) -> bool:
        return self._first.is_faithful() and self._second.is_faithful()

    def _repr_(self):
        return f"{self._second} ∘ {self._first}"


class NaturalTransformation(SageObject):
    r"""A natural transformation ``source => target`` given by its components."""

    def __init__(self, source: Functor, target: Functor, component) -> None:
        if source.domain() != target.domain() or source.codomain() != target.codomain():
            raise ValueError("a natural transformation requires parallel functors")
        self._source = source
        self._target = target
        self._component = component

    def source(self) -> Functor:
        return self._source

    def target(self) -> Functor:
        return self._target

    def component(self, obj):
        arrow = self._component(obj)
        if arrow.domain() is not self.source()(obj) or arrow.codomain() is not self.target()(obj):
            raise ValueError("a natural-transformation component has the wrong source or target")
        return arrow

    __call__ = component

    def naturality_square(self, morphism):
        r"""Return the two composites that naturality asserts are equal."""
        left = self.target()(morphism) * self.component(morphism.domain())
        right = self.component(morphism.codomain()) * self.source()(morphism)
        return left, right


class Adjunction(SageObject):
    r"""An adjunction ``F ⊣ U`` with its unit, counit, and Hom-set bijection."""

    def __init__(self, left_adjoint: Functor, right_adjoint: Functor) -> None:
        if left_adjoint.domain() != right_adjoint.codomain():
            raise ValueError("the right adjoint must return to the left adjoint's domain")
        if left_adjoint.codomain() != right_adjoint.domain():
            raise ValueError("the adjoints must run between the same two categories")
        self._left_adjoint = left_adjoint
        self._right_adjoint = right_adjoint

    def left_adjoint(self) -> Functor:
        return self._left_adjoint

    def right_adjoint(self) -> Functor:
        return self._right_adjoint

    def unit(self, obj):
        raise NotImplementedError("an adjunction must supply its unit")

    def counit(self, obj):
        raise NotImplementedError("an adjunction must supply its counit")

    def hom_set_isomorphism_forward(self, morphism):
        raise NotImplementedError("an adjunction must supply the forward Hom-set bijection")

    def hom_set_isomorphism_inverse(self, morphism, codomain=None):
        raise NotImplementedError("an adjunction must supply the inverse Hom-set bijection")

    def unit_transformation(self) -> NaturalTransformation:
        return NaturalTransformation(
            IdentityFunctor(self.left_adjoint().domain()),
            CompositeFunctor(self.left_adjoint(), self.right_adjoint()),
            self.unit,
        )

    def counit_transformation(self) -> NaturalTransformation:
        return NaturalTransformation(
            CompositeFunctor(self.right_adjoint(), self.left_adjoint()),
            IdentityFunctor(self.left_adjoint().codomain()),
            self.counit,
        )


class CompositeAdjunction(Adjunction):
    r"""The composite of ``F ⊣ U`` and ``G ⊣ V`` as ``GF ⊣ UV``."""

    def __init__(self, first: Adjunction, second: Adjunction) -> None:
        if first.left_adjoint().codomain() != second.left_adjoint().domain():
            raise ValueError("adjunction composition requires matching middle categories")
        self._first = first
        self._second = second
        super().__init__(
            CompositeFunctor(first.left_adjoint(), second.left_adjoint()),
            CompositeFunctor(second.right_adjoint(), first.right_adjoint()),
        )

    def first(self) -> Adjunction:
        return self._first

    def second(self) -> Adjunction:
        return self._second

    def unit(self, obj):
        first_unit = self.first().unit(obj)
        second_unit = self.second().unit(self.first().left_adjoint()(obj))
        return self.first().right_adjoint()(second_unit) * first_unit

    def counit(self, obj):
        first_counit = self.first().counit(self.second().right_adjoint()(obj))
        return self.second().counit(obj) * self.second().left_adjoint()(first_counit)

    def hom_set_isomorphism_forward(self, morphism):
        return self.first().hom_set_isomorphism_forward(
            self.second().hom_set_isomorphism_forward(morphism)
        )

    def hom_set_isomorphism_inverse(self, morphism, codomain=None):
        if codomain is None:
            raise TypeError("the composite adjunction transpose requires the final codomain")
        middle_codomain = self.second().right_adjoint()(codomain)
        first_transpose = self.first().hom_set_isomorphism_inverse(
            morphism,
            codomain=middle_codomain,
        )
        return self.second().hom_set_isomorphism_inverse(
            first_transpose,
            codomain=codomain,
        )


def compose_adjunctions(first: Adjunction, second: Adjunction) -> CompositeAdjunction:
    return CompositeAdjunction(first, second)
