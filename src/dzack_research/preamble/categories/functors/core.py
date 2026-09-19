r"""Functors, natural transformations, and adjunctions.

These are deliberately small mathematical objects.  The existing Sage/owned
categories remain the domain and codomain; this module adds no parallel
category graph and no registry of relationships.

A functor ``F: C -> D`` is an object of the functor category ``[C, D]``, which
is ``Cat().Mor(C, D)``; a natural transformation ``F => G`` is an arrow of that
category; an adjunction ``F -| U`` is the pair of functors together with its
unit and counit.  ``Cat`` owns the functor category and its morphisms.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import final, overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent


class Functor:
    r"""Construction data for a functor with explicit object and arrow actions.

    The mathematical object is ``self.object()`` in the existing functor
    category ``[C,D]``.  This class is the retained action engine used by that
    object and by the corresponding arrow of ``Cat``; it is not a second
    uncategorized functor object.

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

    @cached_method
    def Image(self):
        r"""Return the category of functor outputs with an explicit chosen preimage."""
        from dzack_research.preamble.categories.abstract_categories.functor_images import (
            ImageOfFunctor,
        )

        return ImageOfFunctor(self)

    def adopt_object_image(self, preimage: Parent, image: Parent) -> Parent:
        r"""Use the stated exact object as this functor instance's forward image of ``preimage``."""
        if preimage not in self.domain() or image not in self.codomain():
            raise TypeError("an adopted functor image has endpoints outside the functor")
        return self._record_object_image(preimage, image)

    def on_object(self, obj: Parent) -> Parent:
        return self.object_image(obj)

    def morphism_image(self, morphism: Map) -> Map:
        r"""The image ``F(f): F(A) -> F(B)`` of an arrow ``f: A -> B`` of the domain.

        Both sides are decided by the Hom categories that own them: ``f`` is
        an arrow of ``Hom_C(A, B)``, and its image is an arrow of
        ``Hom_D(F(A), F(B))``, a membership that also fixes both endpoints.
        """
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
        r"""Apply the object action to an object of the domain, the arrow action otherwise.

        Whether ``value`` is an object is the domain category's question.
        Asking it first is what lets a functor out of a Hom category, whose
        objects are themselves arrows, read an arrow as the object it is.
        """
        match value:
            case _ if value in self.domain():
                return self.object_image(value)
            case _:
                return self.morphism_image(value)

    def then(self, other: Functor) -> Functor:
        r"""Return ``other ∘ self``, retaining the nonidentity factor when possible.

        An identity functor is the composite of no factors, so a side with no
        factors is dropped.
        """
        if self.codomain() != other.domain():
            raise ValueError("functor composition requires matching middle categories")
        if not self.factors():
            return other
        if not other.factors():
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

    def object(self):
        r"""Return this datum as the object of its functor category ``[C,D]``."""
        return self.functor_category().object(self)

    def arrow(self):
        r"""Return this same functor as the corresponding morphism in ``Cat``."""
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return Cat().arrow(self)

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

    def _repr_(self) -> str:
        r"""The functor's standard name; a functor with none is named only by its endpoints."""
        return "Functor"

    def __repr__(self) -> str:
        r"""Display the mathematical arrow together with any standard operation name."""
        label = self._repr_()
        endpoints = f"{self.domain()} -> {self.codomain()}"
        return label if endpoints in label else f"{label}: {endpoints}"


class IdentityFunctor(Functor):
    def __init__(self, category: Category) -> None:
        super().__init__(category, category)

    def _apply_object(self, obj: Parent) -> Parent:
        return obj

    def _apply_morphism(self, morphism: Map) -> Map:
        return morphism

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

    def _repr_(self):
        return f"Inclusion {self.domain()} -> {self.codomain()}"



class _CompositeFunctor(Functor):
    r"""The composite ``second ∘ first`` with the ordinary cached forward action."""

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

    def adopt_object_image(self, preimage: Parent, image: Parent) -> Parent:
        if preimage not in self.domain() or image not in self.codomain():
            raise TypeError("an adopted composite image has endpoints outside the functor")
        chosen = self._cached_object_image(preimage)
        if chosen is not None:
            if chosen is not image:
                raise ValueError("the composite already selected a different image of this source")
            return chosen
        middle = self._first(preimage)
        target = self._second(middle)
        if target is not image:
            raise ValueError(
                "the supplied image is not the composite's selected forward image of this source"
            )
        return super().adopt_object_image(preimage, image)

    def factors(self) -> tuple[Functor, ...]:
        return self._first.factors() + self._second.factors()

    def is_faithful(self) -> bool:
        return self._first.is_faithful() and self._second.is_faithful()

    def _repr_(self):
        return f"{self._second} ∘ {self._first}"


class NaturalTransformation:
    r"""Construction data for a natural transformation ``source => target``.

    The datum is the family of components ``eta_X: F(X) -> G(X)`` indexed by
    the objects of the common domain.  Naturality is the equation
    ``G(f) eta_A = eta_B F(f)`` for every ``f: A -> B``; it is a property of
    the family that its constructor states, not a check performed per arrow.
    """

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
        r"""The component ``eta_X``, an arrow of ``Hom_D(F(X), G(X))``.

        Membership in that Hom category is the whole requirement: it decides
        both that the component is an arrow of the common codomain category
        and that its endpoints are ``F(X)`` and ``G(X)``.
        """
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_hom,
        )

        domain, codomain = self.source()(obj), self.target()(obj)
        arrow = self._component(obj)
        if arrow not in _category_hom(self.source().codomain(), domain, codomain):
            raise TypeError(
                "a natural-transformation component at an object X is an arrow "
                "F(X) -> G(X) of the common codomain category"
            )
        return arrow

    __call__ = component

    def naturality_target_composite(self, morphism: Map) -> Morphism:
        r"""Return ``G(f) o eta_A`` for this transformation ``eta:F=>G``."""
        return self.target()(morphism) * self.component(morphism.domain())

    def naturality_source_composite(self, morphism: Map) -> Morphism:
        r"""Return ``eta_B o F(f)`` for this transformation ``eta:F=>G``."""
        return self.component(morphism.codomain()) * self.source()(morphism)

    def naturality_square(self, morphism: Map):
        r"""Return the two paths of the naturality square at ``f: A -> B``.

        The square has two paths ``F(A) -> G(B)``, indexed by the two-element
        set ``Sets.Δ[1]``: ``0`` is ``G(f) o eta_A`` and ``1`` is
        ``eta_B o F(f)``.  Its value is one element of the product of the
        family of the Hom-sets holding those two composites over that index
        set (`CON-15`); projecting at an index recovers that path in its own
        Hom-set.  Naturality is the statement that the two components agree.
        """
        from dzack_research.preamble.categories.sets.indexed_families import indexed_family
        from dzack_research.preamble.categories.sets.set_categories import Sets

        paths = Sets.Δ[1]
        target_composite = self.naturality_target_composite(morphism)
        source_composite = self.naturality_source_composite(morphism)

        def path(index):
            return target_composite if int(index) == 0 else source_composite

        product = Sets().product(indexed_family(paths, lambda index: path(index).parent()))
        return product(path)

    def _repr_(self) -> str:
        return f"{self.source()} => {self.target()}"

    def __repr__(self) -> str:
        return self._repr_()

    def morphism(self):
        r"""Return this datum as the arrow ``F => G`` of the functor category."""
        return self.source().functor_category().Mor(self.source(), self.target())(self)


class _UnitCounitPresentation:
    r"""One fixed unit-counit presentation of an adjunction.

    This is the complete defining datum consumed by :class:`Adjunction`: the
    two adjoint functors and the two component families.  It validates the
    actual component endpoints once at their shared owner.  Hom transposes,
    natural transformations and the public component accessors are derived
    from this presentation rather than supplied as parallel interfaces.
    """

    def __init__(
        self,
        left_adjoint: Functor,
        right_adjoint: Functor,
        unit_component: Callable[[Parent], Morphism],
        counit_component: Callable[[Parent], Morphism],
    ) -> None:
        match (
            left_adjoint.domain() == right_adjoint.codomain(),
            left_adjoint.codomain() == right_adjoint.domain(),
        ):
            case (True, True):
                pass
            case (False, _):
                raise ValueError("the right adjoint must return to the left adjoint's domain")
            case (_, False):
                raise ValueError("the adjoints must run between the same two categories")
        self._left_adjoint = left_adjoint
        self._right_adjoint = right_adjoint
        self._unit_component = unit_component
        self._counit_component = counit_component

    def left_adjoint(self) -> Functor:
        return self._left_adjoint

    def right_adjoint(self) -> Functor:
        return self._right_adjoint

    def unit(self, obj: Parent) -> Morphism:
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_hom,
        )

        category = self.left_adjoint().domain()
        match obj in category:
            case True:
                pass
            case False:
                raise TypeError("a unit component is indexed by an object of the left-adjoint domain")
        target = self.right_adjoint()(self.left_adjoint()(obj))
        arrow = self._unit_component(obj)
        match arrow in _category_hom(category, obj, target):
            case True:
                pass
            case False:
                raise TypeError("the selected unit component has the wrong adjunction endpoints")
        return arrow

    def counit(self, obj: Parent) -> Morphism:
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_hom,
        )

        category = self.right_adjoint().domain()
        match obj in category:
            case True:
                pass
            case False:
                raise TypeError("a counit component is indexed by an object of the right-adjoint domain")
        source = self.left_adjoint()(self.right_adjoint()(obj))
        arrow = self._counit_component(obj)
        match arrow in _category_hom(category, source, obj):
            case True:
                pass
            case False:
                raise TypeError("the selected counit component has the wrong adjunction endpoints")
        return arrow


class Adjunction:
    r"""Construction/proof data for an adjunction ``F ⊣ U``.

    Unlike a functor or a natural transformation, the current category tree
    has no category whose objects are adjunction presentations.  This retained
    record therefore does not pretend to be a Sage mathematical object: its
    constituent functors and its unit/counit are placed at their actual owners.

    The defining datum is the unit-counit presentation (Mathlib,
    ``CategoryTheory.Adjunction.CoreUnitCounit``): functors
    ``F: C -> D`` and ``U: D -> C`` with natural transformations
    ``eta: 1_C => UF`` and ``epsilon: FU => 1_D`` satisfying the triangle
    identities ``U(epsilon) o eta_U = 1_U`` and ``epsilon_F o F(eta) = 1_F``.
    A subclass supplies exactly this datum through the private component
    formulas :meth:`_unit_component` and :meth:`_counit_component`.  Construction
    fixes those formulas in one :class:`_UnitCounitPresentation`; subclasses
    cannot replace any of the public equivalent-data interfaces independently.

    Everything else is derived from it and is not supplied again: the natural
    Hom-set bijection ``Phi: Hom_D(F(A), B) -> Hom_C(A, U(B))``, with
    ``Phi(f) = U(f) o eta_A`` and ``Phi^{-1}(g) = epsilon_B o F(g)``, and the
    unit and counit as natural transformations.  The triangle identities are
    theorems about the supplied datum, established where it is constructed,
    not re-checked here.
    """

    _DERIVED_PUBLIC_INTERFACES = frozenset((
        "unit",
        "counit",
        "hom_set_isomorphism_forward",
        "hom_set_isomorphism_inverse",
        "unit_transformation",
        "counit_transformation",
    ))

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        independently_supplied = cls._DERIVED_PUBLIC_INTERFACES.intersection(cls.__dict__)
        match len(independently_supplied):
            case 0:
                pass
            case _:
                names = ", ".join(sorted(independently_supplied))
                raise TypeError(
                    f"an adjunction subclass supplies only _unit_component and _counit_component; "
                    f"the equivalent public data are derived ({names})"
                )

    def __init__(self, left_adjoint: Functor, right_adjoint: Functor) -> None:
        self._presentation = _UnitCounitPresentation(
            left_adjoint,
            right_adjoint,
            self._unit_component,
            self._counit_component,
        )

    def _unit_counit_presentation(self) -> _UnitCounitPresentation:
        r"""Return this adjunction's one selected complete defining datum."""
        return self._presentation

    def left_adjoint(self) -> Functor:
        return self._unit_counit_presentation().left_adjoint()

    def right_adjoint(self) -> Functor:
        return self._unit_counit_presentation().right_adjoint()

    def then(self, second: "Adjunction") -> "Adjunction":
        r"""Compose this adjunction with ``second``."""
        return _CompositeAdjunction(self, second)

    def _repr_(self) -> str:
        r"""The adjunction's standard name; one with none is named only by its categories."""
        return "Adjunction"

    def __repr__(self) -> str:
        label = self._repr_()
        left = self.left_adjoint()
        endpoints = f"{left.domain()} <-> {left.codomain()}"
        return label if endpoints in label else f"{label}: {endpoints}"

    @abstract_method
    def _unit_component(self, obj: Parent) -> Morphism:
        r"""Construct the selected unit component before shared endpoint admission."""

    @abstract_method
    def _counit_component(self, obj: Parent) -> Morphism:
        r"""Construct the selected counit component before shared endpoint admission."""

    @final
    def unit(self, obj: Parent) -> Morphism:
        r"""Return the unit component ``eta_A: A -> U(F(A))`` from the selected presentation."""
        return self._unit_counit_presentation().unit(obj)

    @final
    def counit(self, obj: Parent) -> Morphism:
        r"""Return the counit component ``epsilon_B: F(U(B)) -> B`` from the selected presentation."""
        return self._unit_counit_presentation().counit(obj)

    @final
    def hom_set_isomorphism_forward(
        self,
        morphism: Morphism,
        source: Parent,
    ) -> Morphism:
        r"""Transpose ``f:F(A)->B`` to ``U(f) after eta_A`` for the stated ``A``.

        Derived from the unit; a subclass never supplies it.  ``A`` is stated
        because a left-adjoint image ``F(A)`` need not determine ``A``.
        """
        if source not in self.left_adjoint().domain():
            raise TypeError("the stated adjunction source is outside the left-adjoint domain")
        if self.left_adjoint()(source) is not morphism.domain():
            raise ValueError("the morphism domain is not the left-adjoint image of the stated source")
        return self.right_adjoint()(morphism) * self.unit(source)

    @final
    def hom_set_isomorphism_inverse(
        self,
        morphism: Morphism,
        codomain: Parent,
    ) -> Morphism:
        r"""Transpose ``g:A->U(B)`` to ``epsilon_B after F(g)`` for the stated ``B``.

        Derived from the counit; a subclass never supplies it.
        """
        if codomain not in self.right_adjoint().domain():
            raise TypeError("the stated adjunction codomain is outside the right-adjoint domain")
        if self.right_adjoint()(codomain) is not morphism.codomain():
            raise ValueError("the morphism codomain is not the right-adjoint image of the stated codomain")
        return self.counit(codomain) * self.left_adjoint()(morphism)

    @final
    def unit_transformation(self):
        r"""The unit ``eta: 1_C => UF`` as a natural transformation, from :meth:`unit`."""
        return NaturalTransformation(
            IdentityFunctor(self.left_adjoint().domain()),
            _CompositeFunctor(self.left_adjoint(), self.right_adjoint()),
            self.unit,
        ).morphism()

    @final
    def counit_transformation(self):
        r"""The counit ``epsilon: FU => 1_D`` as a natural transformation, from :meth:`counit`."""
        return NaturalTransformation(
            _CompositeFunctor(self.right_adjoint(), self.left_adjoint()),
            IdentityFunctor(self.left_adjoint().codomain()),
            self.counit,
        ).morphism()


class _CompositeAdjunction(Adjunction):
    r"""The composite of ``F ⊣ U`` and ``G ⊣ V`` as ``GF ⊣ UV``.

    Its unit and counit are the standard composites (Mathlib,
    ``Adjunction.comp_unit_app`` and ``comp_counit_app``): ``eta = U(eta') o eta`` and ``epsilon = epsilon' o G(epsilon)``.
    """

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

    def _unit_component(self, obj: Parent) -> Morphism:
        first_unit = self.first().unit(obj)
        second_unit = self.second().unit(self.first().left_adjoint()(obj))
        return self.first().right_adjoint()(second_unit) * first_unit

    def _counit_component(self, obj: Parent) -> Morphism:
        first_counit = self.first().counit(self.second().right_adjoint()(obj))
        return self.second().counit(obj) * self.second().left_adjoint()(first_counit)
