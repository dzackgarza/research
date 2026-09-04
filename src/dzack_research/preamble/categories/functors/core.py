r"""Functors, natural transformations, and adjunctions.

These are deliberately small mathematical objects.  The existing Sage/owned
categories remain the domain and codomain; this module adds no parallel
category graph and no registry of relationships.
"""

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.structure.sage_object import SageObject


class Functor(SageObject):
    r"""A functor with explicit actions on objects and morphisms."""

    _faithful = False

    def __init__(self, domain, codomain) -> None:
        self._domain = domain
        self._codomain = codomain
        self._object_images: dict[int, tuple[object, object]] = {}
        self._chosen_preimages: dict[int, tuple[object, list[object]]] = {}

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
        image_key = id(image)
        recorded = self._chosen_preimages.get(image_key)
        if recorded is None or recorded[0] is not image:
            self._chosen_preimages[image_key] = (image, [obj])
        elif all(preimage is not obj for preimage in recorded[1]):
            recorded[1].append(obj)
        return image

    def chosen_preimage(self, image):
        r"""Return the unique source object recorded for this exact functor image."""
        recorded = self._chosen_preimages.get(id(image))
        if recorded is None or recorded[0] is not image:
            raise ValueError(f"{image} has no chosen preimage recorded by {self}")
        if len(recorded[1]) != 1:
            raise ValueError(
                f"{image} has multiple chosen preimages under {self}; state the source explicitly"
            )
        return recorded[1][0]

    def adopt_object_image(self, preimage, image):
        r"""Use a provenance-validated exact image object for ``preimage``."""
        if preimage not in self.domain() or image not in self.codomain():
            raise TypeError("an adopted functor image has endpoints outside the functor")
        key = id(preimage)
        cached = self._object_images.get(key)
        if cached is not None and cached[0] is preimage and cached[1] is not image:
            raise ValueError(
                "this functor instance already selected a different image for the same object"
            )
        self._object_images[key] = (preimage, image)
        image_key = id(image)
        recorded = self._chosen_preimages.get(image_key)
        if recorded is None or recorded[0] is not image:
            self._chosen_preimages[image_key] = (image, [preimage])
        elif all(source is not preimage for source in recorded[1]):
            recorded[1].append(preimage)
        return image

    def on_object(self, obj):
        return self.object_image(obj)

    def morphism_image(self, morphism):
        if not isinstance(morphism, Map):
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
        return self.morphism_image(value) if isinstance(value, Map) else self.object_image(value)

    def then(self, other):
        r"""Return ``other ∘ self``."""
        return CompositeFunctor(self, other)

    def factors(self):
        return (self,)

    def is_faithful(self) -> bool:
        return bool(self._faithful)



class IdentityFunctor(Functor):
    def __init__(self, category) -> None:
        super().__init__(category, category)

    def _apply_object(self, obj):
        return obj

    def _apply_morphism(self, morphism):
        return morphism

    def chosen_preimage(self, image):
        if image not in self.domain():
            raise ValueError(f"{image} is not an object of {self.domain()}")
        return image

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

    def chosen_preimage(self, image):
        if image not in self.domain():
            raise ValueError(f"{image} is not in the included subcategory {self.domain()}")
        return image

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

    def chosen_preimage(self, image):
        middle = self._second.chosen_preimage(image)
        return self._first.chosen_preimage(middle)

    def adopt_object_image(self, preimage, image):
        middle = self._second.chosen_preimage(image)
        self._first.adopt_object_image(preimage, middle)
        self._second.adopt_object_image(middle, image)
        return super().adopt_object_image(preimage, image)

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

    def hom_set_isomorphism_forward(self, morphism, source=None):
        r"""Transpose ``f:F(A)->B`` to ``U(f) after eta_A``."""
        if source is None:
            source = self.left_adjoint().chosen_preimage(morphism.domain())
        self.left_adjoint().adopt_object_image(source, morphism.domain())
        return self.right_adjoint()(morphism) * self.unit(source)

    def hom_set_isomorphism_inverse(self, morphism, codomain=None):
        r"""Transpose ``g:A->U(B)`` to ``epsilon_B after F(g)``."""
        if codomain is None:
            codomain = self.right_adjoint().chosen_preimage(morphism.codomain())
        self.right_adjoint().adopt_object_image(codomain, morphism.codomain())
        return self.counit(codomain) * self.left_adjoint()(morphism)

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



def compose_adjunctions(first: Adjunction, second: Adjunction) -> CompositeAdjunction:
    return CompositeAdjunction(first, second)
