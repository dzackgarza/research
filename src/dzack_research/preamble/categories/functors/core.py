r"""Functors, natural transformations, and adjunctions.

These are deliberately small mathematical objects.  The existing Sage/owned
categories remain the domain and codomain; this module adds no parallel
category graph and no registry of relationships.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject


class Functor(SageObject):
    r"""A functor with explicit actions on objects and morphisms.

    Unverified specimen: a proposed identity on underlying sets is not a
    functor to the category of injections when applied to a noninjective map::

        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: injections = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())
        sage: class ProposedInclusion(Functor):
        ....:     def __init__(self):
        ....:         super().__init__(Sets(), injections)
        ....:     def _apply_object(self, obj):
        ....:         return obj
        ....:     def _apply_morphism(self, arrow):
        ....:         return arrow
        sage: points = finite_ordered_set(("a", "b"))
        sage: maps = Sets().Mor(points, points)
        sage: swap = maps(lambda point: {"a": "b", "b": "a"}[point])
        sage: proposed = ProposedInclusion()
        sage: proposed(swap) is swap
        True
        sage: proposed(maps(lambda point: "a"))
        Traceback (most recent call last):
        ...
        TypeError: the image is not a morphism of the functor's codomain
    """

    _faithful = False

    def __init__(self, domain: Category, codomain: Category) -> None:
        self._domain = domain
        self._codomain = codomain
        # Cache the forward action by source identity.  A codomain object does
        # not determine a preimage; chosen preimages belong to ImageOfFunctor.
        self._object_images: dict[int, tuple[Parent, Parent]] = {}
        self._morphism_images: dict[int, tuple[Map, Map]] = {}

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
        recorded = self._object_images.get(id(preimage))
        if recorded is not None and recorded[0] is preimage:
            return recorded[1]
        return None

    def _record_object_image(self, preimage: Parent, image: Parent) -> Parent:
        key = id(preimage)
        recorded = self._object_images.get(key)
        if recorded is not None and recorded[0] is preimage and recorded[1] is not image:
            raise ValueError(
                "this functor instance already selected a different image for the same preimage"
            )
        self._object_images[key] = (preimage, image)
        return image

    def _cached_morphism_image(self, preimage: Map) -> Map | None:
        recorded = self._morphism_images.get(id(preimage))
        if recorded is not None and recorded[0] is preimage:
            return recorded[1]
        return None

    def _record_morphism_image(self, preimage: Map, image: Map) -> Map:
        key = id(preimage)
        recorded = self._morphism_images.get(key)
        if recorded is not None and recorded[0] is preimage and recorded[1] is not image:
            raise ValueError(
                "this functor instance already selected a different image for the same preimage"
            )
        self._morphism_images[key] = (preimage, image)
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

    def chosen_preimage(self, image: Parent | Map) -> Parent | Map:
        r"""Return the unique source recorded for this exact functor image.

        Object and morphism images share the same provenance store, so reverse
        lookup must inspect the corresponding half of each record rather than
        silently treating every target as an object.
        """
        matches: list[Parent | Map] = []
        for record in self._provenance.values():
            if record.target_object is image and record.source_object is not None:
                matches.append(record.source_object)
            if record.target_morphism is image and record.source_morphism is not None:
                matches.append(record.source_morphism)
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
            _category_hom,
        )

        if morphism not in _category_hom(self.domain(), morphism.domain(), morphism.codomain()):
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
        if image not in _category_hom(self.codomain(), domain, codomain):
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

    def then(self, other: Functor) -> Functor:
        r"""Return ``other ∘ self``, retaining the nonidentity factor when possible."""
        if isinstance(self, IdentityFunctor):
            return other
        if isinstance(other, IdentityFunctor):
            return self
        return _CompositeFunctor(self, other)

    def restrict(self, indexing_functor: Functor) -> Functor:
        r"""Return this diagram precomposed by ``indexing_functor``."""
        from dzack_research.preamble.categories.abstract_categories.products import (
            RestrictedDiagram,
        )

        return RestrictedDiagram(self, indexing_functor)

    def Cones(self):
        r"""Return the category of cones over this diagram."""
        from dzack_research.preamble.categories.abstract_categories.products import _ConeCategory

        return _ConeCategory(self)

    def Cocones(self):
        r"""Return the category of cocones under this diagram."""
        from dzack_research.preamble.categories.abstract_categories.products import _CoconeCategory

        return _CoconeCategory(self)

    @cached_method
    def algebras(self):
        r"""Return the category of algebras ``T(X) -> X`` of this endofunctor."""
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _EndofunctorAlgebraCategory,
        )

        return _EndofunctorAlgebraCategory(self)

    def ProductCones(self):
        r"""Return the category of product cones over this discrete diagram."""
        from dzack_research.preamble.categories.abstract_categories.products import (
            _ProductConeCategory,
        )

        return _ProductConeCategory(self)

    def CoproductCocones(self):
        r"""Return the category of coproduct cocones under this discrete diagram."""
        from dzack_research.preamble.categories.abstract_categories.products import (
            _CoproductCoconeCategory,
        )

        return _CoproductCoconeCategory(self)

    def Spans(self):
        r"""Return the span category carried by this discrete diagram."""
        from dzack_research.preamble.categories.abstract_categories.products import _SpanCategory

        return _SpanCategory(self)

    def functor_category(self):
        r"""Return the represented functor category containing this functor."""
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return Cat().Mor(self.domain(), self.codomain())

    def natural_transformations_to(self, target: Functor):
        r"""Return the Hom of natural transformations ``self ⇒ target``."""
        if self.domain() != target.domain() or self.codomain() != target.codomain():
            raise ValueError("natural transformations require parallel functors")
        category = self.functor_category()
        return category.Mor(self, target)

    def natural_isomorphism_to(
        self,
        target: Functor,
        components: Callable[[Parent], Morphism],
        inverse_components: Callable[[Parent], Morphism],
    ):
        r"""Return the selected natural isomorphism ``self ≅ target``."""
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _isomorphism_from_known_inverse_pair,
        )

        forward = self.natural_transformations_to(target)(components)
        inverse = target.natural_transformations_to(self)(inverse_components)
        return _isomorphism_from_known_inverse_pair(forward, inverse)

    def induced_hom_functor(self, domain_object: Parent, codomain_object: Parent):
        r"""Return the functor induced by this functor on one Hom category."""
        from dzack_research.preamble.categories.functors.hom_packets import _InducedHomFunctor

        return _InducedHomFunctor(self, domain_object, codomain_object)

    def induced_end_functor(self, obj: Parent):
        r"""Return the functor induced by this functor on ``End(obj)``."""
        from dzack_research.preamble.categories.functors.hom_packets import _InducedEndFunctor

        return _InducedEndFunctor(self, obj)

    def induced_aut_functor(self, obj: Parent):
        r"""Return the functor induced by this functor on ``Aut(obj)``."""
        from dzack_research.preamble.categories.functors.hom_packets import _InducedAutFunctor

        return _InducedAutFunctor(self, obj)

    def factors(self) -> tuple[Functor, ...]:
        return (self,)

    def is_faithful(self) -> bool:
        return bool(self._faithful)

    def _semantic_display_label(self) -> str:
        r"""Return the subclass's mathematical label without treating it as the whole display."""
        for cls in type(self).__mro__:
            if cls is Functor:
                break
            method = cls.__dict__.get("_repr_")
            if method is not None:
                return str(method(self))
        name = type(self).__name__
        return name[:-7] if name.endswith("Functor") else name

    def __repr__(self) -> str:
        r"""Display the mathematical arrow together with any standard operation name."""
        label = self._semantic_display_label()
        endpoints = f"{self.domain()} -> {self.codomain()}"
        return label if endpoints in label else f"{label}: {endpoints}"


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


class _CategoryInclusionFunctor(Functor):
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



class _CompositeFunctor(Functor):
    r"""The composite ``second ∘ first``.

    Unverified specimen: a factor can have more recorded preimages than the
    composite. That does not change the composite's already selected image::

        sage: from dzack_research.preamble.categories.abstract_categories.cat import Cat
        sage: from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: labels = finite_ordered_set(("a", "b"))
        sage: source = DiscreteCategory(labels)
        sage: points = finite_ordered_set((0, 1))
        sage: first = IdentityFunctor(source)
        sage: second = Cat().Mor(source, Sets()).constant_functor(points)
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
            _category_hom,
        )

        domain, codomain = self.source()(obj), self.target()(obj)
        arrow = self._component(obj)
        if not isinstance(arrow, Morphism):
            raise TypeError("a natural-transformation component must be a morphism")
        if arrow.domain() is not domain or arrow.codomain() is not codomain:
            raise ValueError("a natural-transformation component has the wrong source or target")
        if arrow not in _category_hom(self.source().codomain(), domain, codomain):
            raise TypeError("the component is not a morphism of the common codomain category")
        return arrow

    __call__ = component

    def naturality_target_composite(self, morphism: Map) -> Morphism:
        r"""Return ``G(f) o eta_A`` for this transformation ``eta:F=>G``."""
        return self.target()(morphism) * self.component(morphism.domain())

    def naturality_source_composite(self, morphism: Map) -> Morphism:
        r"""Return ``eta_B o F(f)`` for this transformation ``eta:F=>G``."""
        return self.component(morphism.codomain()) * self.source()(morphism)

    def naturality_square(self, morphism: Map):
        r"""Return the two naturality composites as an element of their owned product."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        target_composite = self.naturality_target_composite(morphism)
        source_composite = self.naturality_source_composite(morphism)
        product = Sets().product((target_composite.parent(), source_composite.parent()))
        return product((target_composite, source_composite))

    def _repr_(self) -> str:
        return f"{self.source()} => {self.target()}"


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

    def then(self, second: "Adjunction") -> "Adjunction":
        r"""Compose this adjunction with ``second``."""
        return _CompositeAdjunction(self, second)

    def _semantic_display_label(self) -> str:
        r"""Return a subclass operation label while the base owns the categorical endpoints."""
        for cls in type(self).__mro__:
            if cls is Adjunction:
                break
            method = cls.__dict__.get("_repr_")
            if method is not None:
                return str(method(self))
        name = type(self).__name__
        return name[:-10] if name.endswith("Adjunction") else name

    def __repr__(self) -> str:
        label = self._semantic_display_label()
        left = self.left_adjoint()
        endpoints = f"{left.domain()} <-> {left.codomain()}"
        return label if endpoints in label else f"{label}: {endpoints}"

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
            _CompositeFunctor(self.left_adjoint(), self.right_adjoint()),
            self.unit,
        )

    def counit_transformation(self) -> NaturalTransformation:
        return NaturalTransformation(
            _CompositeFunctor(self.right_adjoint(), self.left_adjoint()),
            IdentityFunctor(self.left_adjoint().codomain()),
            self.counit,
        )


class _CompositeAdjunction(Adjunction):
    r"""The composite of ``F ⊣ U`` and ``G ⊣ V`` as ``GF ⊣ UV``."""

    def __init__(self, first: Adjunction, second: Adjunction) -> None:
        if first.left_adjoint().codomain() != second.left_adjoint().domain():
            raise ValueError("adjunction composition requires matching middle categories")
        self._first = first
        self._second = second
        super().__init__(
            _CompositeFunctor(first.left_adjoint(), second.left_adjoint()),
            _CompositeFunctor(second.right_adjoint(), first.right_adjoint()),
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
