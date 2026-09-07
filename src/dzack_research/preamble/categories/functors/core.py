r"""Functors, natural transformations, and adjunctions.

These are deliberately small mathematical objects.  The existing Sage/owned
categories remain the domain and codomain; this module adds no parallel
category graph and no registry of relationships.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject


@dataclass(frozen=True)
class _FunctorImageRecord:
    r"""One identity-retaining object or morphism image in a functor's provenance."""

    source_object: Parent | None = None
    target_object: Parent | None = None
    source_morphism: Map | None = None
    target_morphism: Map | None = None


class Functor(SageObject):
    r"""A functor with explicit actions on objects and morphisms."""

    _faithful = False

    def __init__(self, domain: Category, codomain: Category) -> None:
        self._domain = domain
        self._codomain = codomain
        # One identity-based provenance store for everything this functor
        # actually maps.  Keeping the source object/morphism alive in the
        # record also makes ``id`` reuse impossible while the provenance is
        # live.  Reverse lookup is intentionally derived from this same store
        # rather than maintained by a second cache.
        self._provenance: dict[int, _FunctorImageRecord] = {}

    def _cache_key(self) -> int:
        r"""Functors have identity semantics as parameters of categorical constructions."""
        return id(self)

    def domain(self) -> Category:
        return self._domain

    def codomain(self) -> Category:
        return self._codomain

    @abstract_method
    def _apply_object(self, obj: Parent) -> Parent:
        r"""Return the image of one object of the domain."""

    @abstract_method
    def _apply_morphism(self, morphism: Map) -> Map:
        r"""Return the image of one morphism of the domain."""

    def _cached_object_image(self, preimage: Parent) -> Parent | None:
        recorded = self._provenance.get(id(preimage))
        if recorded is not None and recorded.source_object is preimage:
            return recorded.target_object
        return None

    def _record_object_image(self, preimage: Parent, image: Parent) -> Parent:
        key = id(preimage)
        recorded = self._provenance.get(key)
        if (
            recorded is not None
            and recorded.source_object is preimage
            and recorded.target_object is not image
        ):
            raise ValueError(
                "this functor instance already selected a different image for the same preimage"
            )
        self._provenance[key] = _FunctorImageRecord(
            source_object=preimage,
            target_object=image,
        )
        return image

    def _cached_morphism_image(self, preimage: Map) -> Map | None:
        recorded = self._provenance.get(id(preimage))
        if recorded is not None and recorded.source_morphism is preimage:
            return recorded.target_morphism
        return None

    def _record_morphism_image(self, preimage: Map, image: Map) -> Map:
        key = id(preimage)
        recorded = self._provenance.get(key)
        if (
            recorded is not None
            and recorded.source_morphism is preimage
            and recorded.target_morphism is not image
        ):
            raise ValueError(
                "this functor instance already selected a different image for the same preimage"
            )
        self._provenance[key] = _FunctorImageRecord(
            source_morphism=preimage,
            target_morphism=image,
        )
        return image

    def object_image(self, obj: Parent) -> Parent:
        if obj not in self.domain():
            raise TypeError(f"{obj} is not an object of {self.domain()}")
        cached = self._cached_object_image(obj)
        if cached is not None:
            return cached
        image = self._apply_object(obj)
        if image not in self.codomain():
            raise TypeError(
                f"the image of {obj} under {self} is not an object of {self.codomain()}"
            )
        return self._record_object_image(obj, image)

    def chosen_preimage(self, image: Parent) -> Parent:
        r"""Return the unique source object recorded for this exact functor image."""
        matches = [
            record.source_object
            for record in self._provenance.values()
            if record.target_object is image and record.source_object is not None
        ]
        if not matches:
            raise ValueError(f"{image} has no chosen preimage recorded by {self}")
        if len(matches) != 1:
            raise ValueError(
                f"{image} has multiple chosen preimages under {self}; state the source explicitly"
            )
        return matches[0]

    def adopt_object_image(self, preimage: Parent, image: Parent) -> Parent:
        r"""Use a provenance-validated exact image object for ``preimage``."""
        if preimage not in self.domain() or image not in self.codomain():
            raise TypeError("an adopted functor image has endpoints outside the functor")
        return self._record_object_image(preimage, image)

    def on_object(self, obj: Parent) -> Parent:
        return self.object_image(obj)

    def morphism_image(self, morphism: Map) -> Map:
        if not isinstance(morphism, Map):
            raise TypeError("a functor acts on a morphism through its morphism action")
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_homset,
        )

        if morphism not in _category_homset(self.domain(), morphism.domain(), morphism.codomain()):
            raise TypeError("the supplied map is not a morphism of the functor's domain")
        cached = self._cached_morphism_image(morphism)
        if cached is not None:
            return cached
        domain = self.object_image(morphism.domain())
        codomain = self.object_image(morphism.codomain())
        image = self._apply_morphism(morphism)
        if not isinstance(image, Map):
            raise TypeError("the morphism action must return a morphism")
        if image.domain() is not domain or image.codomain() is not codomain:
            raise ValueError(
                "a functor's morphism image must run between the cached images "
                "of the original domain and codomain"
            )
        if image not in _category_homset(self.codomain(), domain, codomain):
            raise TypeError("the image is not a morphism of the functor's codomain")
        return self._record_morphism_image(morphism, image)

    def on_morphism(self, morphism: Map) -> Map:
        return self.morphism_image(morphism)

    @overload
    def __call__(self, value: Parent) -> Parent: ...

    @overload
    def __call__(self, value: Map) -> Map: ...

    def __call__(self, value: Parent | Map) -> Parent | Map:
        return self.morphism_image(value) if isinstance(value, Map) else self.object_image(value)

    def then(self, other: "Functor") -> "CompositeFunctor":
        r"""Return ``other ∘ self``."""
        return CompositeFunctor(self, other)

    def factors(self) -> tuple["Functor", ...]:
        return (self,)

    def is_faithful(self) -> bool:
        return bool(self._faithful)



class IdentityFunctor(Functor):
    def __init__(self, category: Category) -> None:
        super().__init__(category, category)

    def _apply_object(self, obj: Parent) -> Parent:
        return obj

    def _apply_morphism(self, morphism: Map) -> Map:
        return morphism

    def chosen_preimage(self, image: Parent) -> Parent:
        if image not in self.domain():
            raise ValueError(f"{image} is not an object of {self.domain()}")
        return image

    def factors(self) -> tuple[()]:
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

    def __init__(self, subcategory: Category, supercategory: Category) -> None:
        if not subcategory.is_subcategory(supercategory):
            raise ValueError(f"{subcategory} is not a subcategory of {supercategory}")
        super().__init__(subcategory, supercategory)

    def _apply_object(self, obj: Parent) -> Parent:
        return obj

    def _apply_morphism(self, morphism: Map) -> Map:
        return morphism

    def chosen_preimage(self, image: Parent) -> Parent:
        if image not in self.domain():
            raise ValueError(f"{image} is not in the included subcategory {self.domain()}")
        return image

    def _repr_(self):
        return f"Inclusion {self.domain()} -> {self.codomain()}"


def category_inclusion(
    subcategory: Category,
    supercategory: Category,
) -> CategoryInclusionFunctor:
    r"""Return the canonical functor attached to ``subcategory <= supercategory``."""
    return CategoryInclusionFunctor(subcategory, supercategory)


class CompositeFunctor(Functor):
    r"""The composite ``second ∘ first``.

    Unverified specimen: a factor can have more recorded preimages than the
    composite. That does not change the composite's already selected image::

        sage: from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory, ConstantDiagram
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: labels = finite_ordered_set(("a", "b"))
        sage: source = DiscreteCategory(labels)
        sage: points = finite_ordered_set((0, 1))
        sage: first = IdentityFunctor(source)
        sage: second = ConstantDiagram(source, Sets(), points)
        sage: composite = first.then(second)
        sage: composite(source("a")) is points
        True
        sage: second(source("b")) is points
        True
        sage: composite.chosen_preimage(points) is source("a")
        True
        sage: composite.adopt_object_image(source("a"), points) is points
        True
        sage: first(source("b")) is source("b")
        True
        sage: composite.adopt_object_image(source("b"), points) is points
        True
    """

    def __init__(self, first: Functor, second: Functor) -> None:
        if first.codomain() != second.domain():
            raise ValueError("functor composition requires matching middle categories")
        self._first = first
        self._second = second
        super().__init__(first.domain(), second.codomain())

    def _apply_object(self, obj: Parent) -> Parent:
        return self._second(self._first(obj))

    def _apply_morphism(self, morphism: Map) -> Map:
        return self._second(self._first(morphism))

    def chosen_preimage(self, image: Parent) -> Parent:
        # The composite may have seen fewer inputs than either factor.  Its
        # own chosen preimages are authoritative; a factor's independent
        # provenance must not introduce ambiguity into a recorded choice.
        if any(record.target_object is image for record in self._provenance.values()):
            return super().chosen_preimage(image)
        middle = self._second.chosen_preimage(image)
        return self._first.chosen_preimage(middle)

    def adopt_object_image(self, preimage: Parent, image: Parent) -> Parent:
        if preimage not in self.domain() or image not in self.codomain():
            raise TypeError("an adopted composite image has endpoints outside the functor")
        chosen = self._cached_object_image(preimage)
        if chosen is not None:
            if chosen is not image:
                raise ValueError("the composite already selected a different image of this source")
            return chosen
        middle = self._first._cached_object_image(preimage)
        if middle is None:
            middle = self._second.chosen_preimage(image)
        target = self._second._cached_object_image(middle)
        if target is not None and target is not image:
            raise ValueError("the second factor already selected a different image of the intermediate object")
        self._first.adopt_object_image(preimage, middle)
        self._second.adopt_object_image(middle, image)
        return super().adopt_object_image(preimage, image)

    def factors(self) -> tuple[Functor, ...]:
        return self._first.factors() + self._second.factors()

    def is_faithful(self) -> bool:
        return self._first.is_faithful() and self._second.is_faithful()

    def _repr_(self):
        return f"{self._second} ∘ {self._first}"


class NaturalTransformation(SageObject):
    r"""A natural transformation ``source => target`` given by its components."""

    def __init__(
        self,
        source: Functor,
        target: Functor,
        component: Callable[[Parent], Morphism],
    ) -> None:
        if source.domain() != target.domain() or source.codomain() != target.codomain():
            raise ValueError("a natural transformation requires parallel functors")
        if not callable(component):
            raise TypeError("a natural transformation requires a component map")
        self._source = source
        self._target = target
        self._component = component

    def source(self) -> Functor:
        return self._source

    def target(self) -> Functor:
        return self._target

    @cached_method(key=lambda self, obj: id(obj))
    def component(self, obj: Parent) -> Morphism:
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_homset,
        )

        domain, codomain = self.source()(obj), self.target()(obj)
        arrow = self._component(obj)
        if not isinstance(arrow, Morphism):
            raise TypeError("a natural-transformation component must be a morphism")
        if arrow.domain() is not domain or arrow.codomain() is not codomain:
            raise ValueError("a natural-transformation component has the wrong source or target")
        if arrow not in _category_homset(self.source().codomain(), domain, codomain):
            raise TypeError("the component is not a morphism of the common codomain category")
        return arrow

    __call__ = component

    def naturality_square(self, morphism: Map) -> tuple[Morphism, Morphism]:
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

    @abstract_method
    def unit(self, obj: Parent) -> Morphism:
        r"""Return the unit component at ``obj``."""

    @abstract_method
    def counit(self, obj: Parent) -> Morphism:
        r"""Return the counit component at ``obj``."""

    def hom_set_isomorphism_forward(
        self,
        morphism: Morphism,
        source: Parent | None = None,
    ) -> Morphism:
        r"""Transpose ``f:F(A)->B`` to ``U(f) after eta_A``."""
        if source is None:
            source = self.left_adjoint().chosen_preimage(morphism.domain())
        self.left_adjoint().adopt_object_image(source, morphism.domain())
        return self.right_adjoint()(morphism) * self.unit(source)

    def hom_set_isomorphism_inverse(
        self,
        morphism: Morphism,
        codomain: Parent | None = None,
    ) -> Morphism:
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

    def unit(self, obj: Parent) -> Morphism:
        first_unit = self.first().unit(obj)
        second_unit = self.second().unit(self.first().left_adjoint()(obj))
        return self.first().right_adjoint()(second_unit) * first_unit

    def counit(self, obj: Parent) -> Morphism:
        first_counit = self.first().counit(self.second().right_adjoint()(obj))
        return self.second().counit(obj) * self.second().left_adjoint()(first_counit)



def compose_adjunctions(first: Adjunction, second: Adjunction) -> CompositeAdjunction:
    return CompositeAdjunction(first, second)
