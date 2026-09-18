r"""A represented category ``Cat`` of categories, functors, and natural transformations."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects as SageObjects
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.element import Element, parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    FixedHomCategory,
    HomCategories,
    HomCategoryConstruction,
    _category_homset,
    _precomposable,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.functors.core import (
    _CompositeFunctor,
    Functor,
    IdentityFunctor,
    NaturalTransformation,
)
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily
from dzack_research.preamble.owned_category import _object_of


class CategoryObject(Parent):
    r"""A Sage category regarded as an object of ``Cat``."""

    def __init__(
        self,
        category_of_categories: Cat,
        represented_category: Category,
    ) -> None:
        self._category_of_categories = category_of_categories
        self._represented_category = represented_category
        Parent.__init__(self, category=category_of_categories)

    def category_of_categories(self) -> Cat:
        return self._category_of_categories

    def represented_category(self) -> Category:
        return self._represented_category

    def _repr_(self) -> str:
        return f"[{self.represented_category()}]"


class CategoryFunctorMorphism(Morphism):
    r"""A live functor regarded as a morphism in ``Cat``."""

    def __init__(self, parent: CategoryFunctorHomset, functor: Functor) -> None:
        Morphism.__init__(self, parent)
        if functor.domain() != self.domain().represented_category():
            raise ValueError("the functor has the wrong Cat-domain")
        if functor.codomain() != self.codomain().represented_category():
            raise ValueError("the functor has the wrong Cat-codomain")
        self._functor = functor

    def functor(self) -> Functor:
        return self._functor

    @overload
    def __call__(self, value: Parent) -> Parent: ...

    @overload
    def __call__(self, value: Map) -> Map: ...

    def __call__(self, value: Parent | Map) -> Parent | Map:
        return self.functor()(value)

    def _call_(self, value):
        return self.functor()(value)

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        left, right = self.functor().factors(), other.functor().factors()
        # Reassociation and insertion/removal of identity functors do not
        # change a composite. Different expressions need not mean different
        # functors, so lack of this equality proof is not inequality.
        if len(left) == len(right) and all(first is second for first, second in zip(left, right)):
            return True
        return Unknown

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        return self.parent().category_of_categories().arrow(
            _CompositeFunctor(other.functor(), self.functor())
        )

    def _repr_(self) -> str:
        return repr(self.functor())


class CategoryFunctorHomset(CategoricalHomset):
    Element = CategoryFunctorMorphism

    def __init__(
        self,
        category_of_categories: Cat,
        domain: CategoryObject,
        codomain: CategoryObject,
    ) -> None:
        self._category_of_categories = category_of_categories
        CategoricalHomset.__init__(
            self, category_of_categories.HomCategory(), domain, codomain
        )

    def category_of_categories(self) -> Cat:
        return self._category_of_categories

    def functor_category(self) -> _FunctorCategory:
        return self.category_of_categories().Mor(self.domain(), self.codomain())

    @property
    def _HomCategory(self) -> type[NaturalTransformationHomCategoryConstruction]:
        return NaturalTransformationHomCategoryConstruction

    def super_categories(self):
        # This runtime Hom-set represents exactly the functors and natural
        # transformations of [C,D], not a discretization of those functors.
        return [self.functor_category()]

    def object(self, functor: Functor | CategoryFunctorMorphism) -> Parent:
        return self.functor_category().object(functor)

    def _hom_endpoint(self, obj: Parent | Functor | CategoryFunctorMorphism) -> Parent:
        return self.functor_category()._hom_endpoint(obj)

    def __contains__(self, candidate: Any) -> bool:
        return candidate in self.functor_category()

    def _element_constructor_(self, functor):
        match functor:
            case CategoryFunctorMorphism():
                if functor.parent() is self:
                    return functor
                functor = functor.functor()
        return CategoryFunctorMorphism(self, functor)

    @cached_method
    def identity(self) -> CategoryFunctorMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism functor Hom-set")

        return self(IdentityFunctor(self.domain().represented_category()))


class FunctorHomCategoryConstruction(HomCategoryConstruction):
    r"""The family ``(C,D) |-> [C,D]``, with its actual natural transformations."""

    def fixed_category_class(self) -> type[_FunctorCategory]:
        return _FunctorCategory

    def fixed_category_class_for(
        self,
        domain: CategoryObject,
        codomain: CategoryObject,
    ) -> type[_FunctorCategory]:
        r"""The realization of ``[C, D]`` for these endpoints.

        One category object for each pair.  Out of the walking arrow
        ``[1] = FiniteOrdinalCategory(2)`` it is the arrow category, whose
        realization adds the vocabulary the shape ``[1]`` names (an arrow,
        its source and target, the two edges of a square) and nothing else.
        """
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _WalkingArrowFunctorCategory,
        )
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        match domain.represented_category():
            case shape if shape is FiniteOrdinalCategory(2):
                return _WalkingArrowFunctorCategory
            case _:
                return self.fixed_category_class()

    def Of(
        self,
        domain: Category | CategoryObject,
        codomain: Category | CategoryObject,
    ) -> _FunctorCategory:
        category = self.base_category()
        source, target = category.object(domain), category.object(codomain)
        cached = self._cached_between(source, target)
        if cached is not None:
            return cached
        return self._remember_between(
            source, target,
            typecall(
                self.fixed_category_class_for(source, target),
                category,
                source.represented_category(),
                target.represented_category(),
            ),
        )

    Between = Of


class Cat(CategoryPacketMethods, Category):
    r"""The represented category of categories.

    A category is an object of ``Cat`` by placement: the owned category bases
    record ``Cat()`` as a category's category when it is built
    (``OwnedCategoryObject`` in ``owned_category.py``), a fixed Hom category
    records ``HomCategories()``, and ``Cat`` records itself.  The expectation
    ``Cat() in Cat()`` (``tests/constructions/test_categorical_constructions_construct.py``)
    is that last placement; ``Cat`` is not built on the owned base, which
    would ask for ``Cat()`` while ``Cat`` is under construction.
    """

    _HomCategory = FunctorHomCategoryConstruction

    def __init__(self) -> None:
        self._arrows = {}
        super().__init__()

    def an_object(self) -> Category:
        r"""The category of sets, which every owned chain roots at."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return Sets()

    def super_categories(self):
        # A category is an object.  This one edge names Sage's ``Objects`` and
        # not the owned one: every owned category is an object of ``Cat``, so
        # an owned supercategory here would have to be constructed while
        # ``Cat`` itself is still under construction.  The owned ``Objects``
        # is a category like any other and is an object of ``Cat``; it is this
        # Sage runtime edge that is Sage's.
        return [SageObjects()]

    def category(self) -> Cat:
        r"""``Cat`` is placed in itself."""
        return self

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is a category, read from its placement.

        Placement answers it for every category whose ``category()`` records
        ``Cat`` or a subcategory of it.  A Hom category realized on Sage's
        ``Homset`` records its enrichment there instead, and its placement
        among Hom categories is recorded by the family that built it, which
        ``HomCategories`` reads.
        """
        return super().__contains__(candidate) or candidate in HomCategories()

    def object(self, category: Category | CategoryObject) -> CategoryObject:
        r"""The Hom endpoint representing ``category`` in ``Cat``.

        Sage's morphisms need a ``Parent`` at each end, and ``Cat`` itself, the
        joins Sage assembles and Sage's own categories are not parents, so
        every category enters ``Cat``'s Homs through one represented endpoint.
        The input is the category or an endpoint already built for it.
        """
        match category:
            case CategoryObject():
                return category
            case Category():
                return self._object_on(category)
            case _:
                raise TypeError("an object of Cat is a category")

    _hom_endpoint = object

    @cached_method(key=lambda self, category: id(category))
    def _object_on(self, category):
        return CategoryObject(self, category)

    @cached_method(key=lambda self, domain, codomain: (id(self.object(domain)), id(self.object(codomain))))
    def functor_homset(
        self,
        domain: Category | CategoryObject,
        codomain: Category | CategoryObject,
    ) -> CategoryFunctorHomset:
        return CategoryFunctorHomset(self, self.object(domain), self.object(codomain))

    def arrow(self, functor: Functor) -> CategoryFunctorMorphism:
        key = id(functor)
        cached = self._arrows.get(key)
        if cached is not None and cached.functor() is functor:
            return cached
        result = self.functor_homset(functor.domain(), functor.codomain())(functor)
        self._arrows[key] = result
        return result

    def Mor(self, domain: Category, codomain: Category) -> _FunctorCategory:
        return self.HomCategory().Of(domain, codomain)

    def identity(self, category: Category) -> CategoryFunctorMorphism:
        return self.functor_homset(category, category).identity()

    def compose(
        self,
        second: CategoryFunctorMorphism,
        first: CategoryFunctorMorphism,
    ) -> CategoryFunctorMorphism:
        if first.codomain() is not second.domain():
            raise ValueError("functors are not composable in Cat")
        return second * first

    class ParentMethods:
        r"""What a category can do, as an object of ``Cat``.

        Sage requires a nested ``ParentMethods`` provider to be a plain class:
        inheriting another implementation class makes category construction
        emit ``ParentMethods should not have a super class`` in a fresh session.
        The Hom-packet operations below are therefore aliases of their single
        implementation in :class:`CategoryPacketMethods`, not a second
        implementation and not a superclass of this provider.

        Every owned category receives this provider through
        ``subcategory_class``; ``CatConstructionsMixin`` on the owned root
        carries it through joins and functorial constructions.
        """

        _hom_endpoint = CategoryPacketMethods._hom_endpoint
        ArrowCategory = CategoryPacketMethods.ArrowCategory
        Core = CategoryPacketMethods.Core
        category_packet = CategoryPacketMethods.category_packet
        HomCategory = CategoryPacketMethods.HomCategory
        EndCategory = CategoryPacketMethods.EndCategory
        MonoCategory = CategoryPacketMethods.MonoCategory
        EpiCategory = CategoryPacketMethods.EpiCategory
        IsoCategory = CategoryPacketMethods.IsoCategory
        AutCategory = CategoryPacketMethods.AutCategory
        Mor = CategoryPacketMethods.Mor
        End = CategoryPacketMethods.End
        Mono = CategoryPacketMethods.Mono
        Epi = CategoryPacketMethods.Epi
        Iso = CategoryPacketMethods.Iso
        Aut = CategoryPacketMethods.Aut

        def inclusion_into(self, supercategory: Category):
            r"""Return the canonical inclusion functor into a declared supercategory."""
            from dzack_research.preamble.categories.functors.core import _CategoryInclusionFunctor

            return _CategoryInclusionFunctor(self, supercategory)

        def domain_functor(self):
            r"""Return the domain functor ``Ar(self) -> self``."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                _domain_functor,
            )

            return _domain_functor(self)

        def codomain_functor(self):
            r"""Return the codomain functor ``Ar(self) -> self``."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                _codomain_functor,
            )

            return _codomain_functor(self)

        def diagonal_functor(self):
            r"""Return the diagonal functor ``self -> self x self``."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                _diagonal_functor,
            )

            return _diagonal_functor(self)

        def product_functor(self):
            r"""Return this category's selected binary-product functor."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                _product_functor,
            )

            return _product_functor(self)

        def coproduct_functor(self):
            r"""Return this category's selected binary-coproduct functor."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                _coproduct_functor,
            )

            return _coproduct_functor(self)

        def limit_functor(self, index_category: Category):
            r"""Return the selected limit functor ``[index_category,self] -> self``."""
            return self.Limits(index_category).defining_functor()

        def colimit_functor(self, index_category: Category):
            r"""Return the selected colimit functor ``[index_category,self] -> self``."""
            return self.Colimits(index_category).defining_functor()

        def Limits(self, index_category: Category) -> Category:
            r"""Return the selected-limit construction category for this target."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _LimitsOfCategory,
            )

            return _LimitsOfCategory(index_category, self)

        def Colimits(self, index_category: Category) -> Category:
            r"""Return the selected-colimit construction category for this target."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _ColimitsOfCategory,
            )

            return _ColimitsOfCategory(index_category, self)

        def Products(self, index_category: Category) -> Category:
            r"""Return the selected-product construction category for this target."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _ProductsOfCategory,
            )

            return _ProductsOfCategory(index_category, self)

        def Coproducts(self, index_category: Category) -> Category:
            r"""Return the selected-coproduct construction category for this target."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _CoproductsOfCategory,
            )

            return _CoproductsOfCategory(index_category, self)

        @property
        def ObjectType(self) -> type[Parent]:
            r"""Return the complete implementation type for objects of this category."""
            return self.parent_class

        @property
        def ElementType(self) -> type[Element]:
            r"""Return the complete implementation type for their elements."""
            return self.element_class

        @abstract_method(optional=True)
        def _categorical_tensor_product(self, left: Parent, right: Parent) -> Parent:
            r"""Return this category's represented tensor product of two objects."""

        @abstract_method(optional=True)
        def _categorical_biproduct(self, left: Parent, right: Parent) -> Parent:
            r"""Return this category's represented biproduct of two objects."""

        @abstract_method(optional=True)
        def _categorical_product(self, left: Parent, right: Parent) -> Parent:
            r"""Return this category's represented product of two objects."""

        @abstract_method(optional=True)
        def _categorical_product_construction(self, factors):
            r"""Return the selected product with its discrete diagram and universal cone."""

        @abstract_method(optional=True)
        def _categorical_coproduct(self, left: Parent, right: Parent) -> Parent:
            r"""Return this category's represented coproduct of two objects."""

        @abstract_method(optional=True)
        def _categorical_coproduct_construction(self, factors):
            r"""Return the selected coproduct with its discrete diagram and universal cocone."""

        @abstract_method(optional=True)
        def _categorical_pushout(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented pushout of a span."""

        @abstract_method(optional=True)
        def _categorical_pullback(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented pullback of a cospan."""

        @abstract_method(optional=True)
        def _categorical_equalizer(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented equalizer of parallel arrows."""

        @abstract_method(optional=True)
        def _categorical_equalizer_construction(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ):
            r"""Return the selected equalizer with its diagram, cone and factorization."""

        @abstract_method(optional=True)
        def _categorical_coequalizer(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented coequalizer of parallel arrows."""

        @abstract_method(optional=True)
        def _categorical_coequalizer_construction(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ):
            r"""Return the selected coequalizer with its diagram, cocone and factorization."""

        @abstract_method(optional=True)
        def _categorical_equalizer_family(self, morphisms: IndexedFamily) -> Parent:
            r"""Return this category's represented equalizer of an indexed arrow family."""

        @abstract_method(optional=True)
        def _categorical_coequalizer_family(self, morphisms: IndexedFamily) -> Parent:
            r"""Return this category's represented coequalizer of an indexed arrow family."""

        def product_construction(self, factors):
            r"""Return this category's selected product construction on ``factors``."""
            construction = self._categorical_product_construction
            assert construction is not NotImplemented, (
                f"{self} does not represent a selected product construction"
            )
            return construction(factors)

        def coproduct_construction(self, factors):
            r"""Return this category's selected coproduct construction on ``factors``."""
            construction = self._categorical_coproduct_construction
            assert construction is not NotImplemented, (
                f"{self} does not represent a selected coproduct construction"
            )
            return construction(factors)

        def equalizer_construction(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ):
            r"""Return this category's selected equalizer construction."""
            assert left_morphism.domain() is right_morphism.domain(), (
                "equalizer arrows have one common domain"
            )
            assert left_morphism.codomain() is right_morphism.codomain(), (
                "equalizer arrows have one common codomain"
            )
            construction = self._categorical_equalizer_construction
            assert construction is not NotImplemented, (
                f"{self} does not represent a selected equalizer construction"
            )
            return construction(left_morphism, right_morphism)

        def coequalizer_construction(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ):
            r"""Return this category's selected coequalizer construction."""
            assert left_morphism.domain() is right_morphism.domain(), (
                "coequalizer arrows have one common domain"
            )
            assert left_morphism.codomain() is right_morphism.codomain(), (
                "coequalizer arrows have one common codomain"
            )
            construction = self._categorical_coequalizer_construction
            assert construction is not NotImplemented, (
                f"{self} does not represent a selected coequalizer construction"
            )
            return construction(left_morphism, right_morphism)

        def equalizer(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented equalizer of a parallel pair."""
            assert left_morphism.domain() is right_morphism.domain(), (
                "equalizer arrows have one common domain"
            )
            assert left_morphism.codomain() is right_morphism.codomain(), (
                "equalizer arrows have one common codomain"
            )
            construction = self._categorical_equalizer
            assert construction is not NotImplemented, (
                f"{self} does not represent equalizers of this parallel pair"
            )
            return construction(left_morphism, right_morphism)

        def coequalizer(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented coequalizer of a parallel pair."""
            assert left_morphism.domain() is right_morphism.domain(), (
                "coequalizer arrows have one common domain"
            )
            assert left_morphism.codomain() is right_morphism.codomain(), (
                "coequalizer arrows have one common codomain"
            )
            construction = self._categorical_coequalizer
            assert construction is not NotImplemented, (
                f"{self} does not represent coequalizers of this parallel pair"
            )
            return construction(left_morphism, right_morphism)

        def equalizer_of_family(self, morphisms) -> Parent:
            r"""Return this category's represented wide equalizer."""
            match morphisms:
                case IndexedFamily():
                    family = morphisms
                case _:
                    from dzack_research.preamble.categories.sets.finite_families import (
                        finite_family,
                    )

                    family = finite_family(tuple(morphisms))
            construction = self._categorical_equalizer_family
            assert construction is not NotImplemented, (
                f"{self} does not represent wide equalizers of this family"
            )
            return construction(family)

        def coequalizer_of_family(self, morphisms) -> Parent:
            r"""Return this category's represented wide coequalizer."""
            match morphisms:
                case IndexedFamily():
                    family = morphisms
                case _:
                    from dzack_research.preamble.categories.sets.finite_families import (
                        finite_family,
                    )

                    family = finite_family(tuple(morphisms))
            construction = self._categorical_coequalizer_family
            assert construction is not NotImplemented, (
                f"{self} does not represent wide coequalizers of this family"
            )
            return construction(family)

        @abstract_method(optional=True)
        def _categorical_product_morphism(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
            source: Parent,
            target: Parent,
        ) -> Morphism:
            r"""Return the induced morphism between represented binary products."""

        @abstract_method(optional=True)
        def _categorical_coproduct_morphism(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
            source: Parent,
            target: Parent,
        ) -> Morphism:
            r"""Return the induced morphism between represented binary coproducts."""

        def fiber_product(self, left_leg: Morphism, right_leg: Morphism) -> Parent:
            r"""Return the fiber product of the cospan these two legs form.

            \(A\times_C B\) is the equalizer of \(f p_A\) and \(g p_B\) on
            \(A\times B\): the subobject on which the two legs agree.  A
            category with products and equalizers has this, so it is defined
            here once, from those; a category with a better construction of its
            own supplies it instead.
            """
            assert left_leg.codomain() is right_leg.codomain(), (
                "a cospan has one common codomain"
            )
            total = self.product([left_leg.domain(), right_leg.domain()])
            return self.equalizer(
                left_leg * total.left_projection(),
                right_leg * total.right_projection(),
            )

        def span(self, left_leg: Morphism, right_leg: Morphism) -> Parent:
            r"""Return the span these two legs form, as an object of this category.

            The span is an object: it has an apex, two legs, a diagram over
            the shape \(\cdot\leftarrow\cdot\rightarrow\cdot\), and its own
            colimit, which it asks this category for.
            """
            from dzack_research.preamble.categories.abstract_categories.products import (
                _discrete_diagram,
            )

            assert left_leg.domain() is right_leg.domain(), "a span has one common domain"
            legs = (left_leg, right_leg)
            diagram = _discrete_diagram(
                (left_leg.codomain(), right_leg.codomain()),
                target_category=self,
            )
            return (diagram).Spans().cone(
                left_leg.domain(),
                lambda index: legs[int(index.value())],
            )

        def ProductCones(self, factors) -> Category:
            r"""Return the category of product cones on ``factors`` in this category."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _discrete_diagram,
            )

            return (_discrete_diagram(factors, target_category=self)).ProductCones()

        def CoproductCocones(self, factors) -> Category:
            r"""Return the category of coproduct cocones on ``factors`` in this category."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _discrete_diagram,
            )

            return (_discrete_diagram(factors, target_category=self)).CoproductCocones()

        def pushout(self, left_leg: Morphism, right_leg: Morphism) -> Parent:
            r"""Return the pushout of the span these two legs form.

            Dual to the fiber product: the coequalizer of \(\iota_A f\) and
            \(\iota_B g\) on \(A\sqcup B\), which identifies \(f(c)\) with
            \(g(c)\).  A category with coproducts and coequalizers has this.
            """
            assert left_leg.domain() is right_leg.domain(), (
                "a span has one common domain"
            )
            total = self.coproduct([left_leg.codomain(), right_leg.codomain()])
            labels = total.index_set()
            return self.coequalizer(
                total.injection(labels(0)) * left_leg,
                total.injection(labels(1)) * right_leg,
            )

        def opposite(self) -> Category:
            r"""Return \(C^{op}\)."""
            from dzack_research.preamble.categories.abstract_categories.category_constructions import (
                _OppositeCategory,
            )

            return _OppositeCategory(self)

        def presheaves(self, value_category: Category | None = None) -> Category:
            r"""Return \(\mathrm{Presh}(C, D) = [C^{op}, D]\), with \(D = \mathbf{Set}\) by default.

            The functor category itself, not a new class: presheaves are its
            objects and natural transformations its morphisms.  Sheaves on
            \(C\) for a coverage are a full subcategory of this one.
            """
            from dzack_research.preamble.categories.sets.set_categories import Sets

            if value_category is None:
                value_category = Sets()
            return Cat().Mor(self.opposite(), value_category)

        def yoneda_embedding(self):
            r"""Return \(y: C \to [C^{op}, \mathbf{Set}]\), \(X \mapsto \mathrm{Mor}_C(-, X)\)."""
            from dzack_research.preamble.categories.abstract_categories.presheaves import (
                _YonedaEmbedding,
            )

            return _YonedaEmbedding(self)

        def EndArrowCategory(self) -> Category:
            r"""Return the full arrow subcategory on endomorphisms."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _EndArrowCategory,
            )

            return _EndArrowCategory(self)
        def IsoArrowCategory(self) -> Category:
            r"""Return the full arrow subcategory on represented isomorphisms."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _IsoArrowCategory,
            )

            return _IsoArrowCategory(self)
        def AutomorphismArrowCategory(self) -> Category:
            r"""Return the full arrow subcategory on automorphisms."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _AutomorphismArrowCategory,
            )

            return _AutomorphismArrowCategory(self)
        def MonomorphismArrowCategory(self) -> Category:
            r"""Return the full arrow subcategory on represented monomorphisms."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _MonomorphismArrowCategory,
            )

            return _MonomorphismArrowCategory(self)
        def EpimorphismArrowCategory(self) -> Category:
            r"""Return the full arrow subcategory on represented epimorphisms."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _EpimorphismArrowCategory,
            )

            return _EpimorphismArrowCategory(self)
        def WideSubcategory(self, arrow_category: Category) -> Category:
            r"""Return the wide subcategory with the selected arrow class."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                _WideSubcategory,
            )

            return _WideSubcategory(self, arrow_category)
        def SliceOver(self, base_object: Parent) -> Category:
            r"""Return the slice \(C/X\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SliceCategory,
            )

            return SliceCategory(self, base_object)
        def CosliceUnder(self, base_object: Parent) -> Category:
            r"""Return the coslice \(X/C\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CosliceCategory,
            )

            return CosliceCategory(self, base_object)
        def SubobjectCategory(self, base_object: Parent) -> Category:
            r"""Return the category of subobjects of ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SubobjectCategory,
            )

            return SubobjectCategory(self, base_object)
        def SuperobjectCategory(self, base_object: Parent) -> Category:
            r"""Return the category of monic superobjects of ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SuperobjectCategory,
            )

            return SuperobjectCategory(self, base_object)
        def CoveringObjectCategory(self, base_object: Parent) -> Category:
            r"""Return the category of epic objects covering ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CoveringObjectCategory,
            )

            return CoveringObjectCategory(self, base_object)
        def CoveredObjectCategory(self, base_object: Parent) -> Category:
            r"""Return the category of epic quotients covered by ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CoveredObjectCategory,
            )

            return CoveredObjectCategory(self, base_object)
        def Subobjects(self, base_object: Parent) -> Category:
            return self.SubobjectCategory(base_object)
        def Superobjects(self, base_object: Parent) -> Category:
            return self.SuperobjectCategory(base_object)
        def CoveringObjects(self, base_object: Parent) -> Category:
            return self.CoveringObjectCategory(base_object)
        def CoveredObjects(self, base_object: Parent) -> Category:
            return self.CoveredObjectCategory(base_object)

    def meet(self, categories: Iterable[Category]) -> Category:
        r"""Return the largest category contained in all of ``categories``.

        Categories are ordered here by inclusion: a subcategory is below its
        supercategories, which is what ``super_categories`` and
        ``is_subcategory`` already say throughout the owned graph.  In that
        order the greatest lower bound of a family is the category of the
        objects lying in every member, so this is the meet, and
        ``Modules(ZZ)`` met with ``FiniteSets()`` is the finite
        ``ZZ``-modules.

        The backend spells it ``Category.join`` because it orders categories
        the other way round, by their axioms: joining the axiom sets gives the
        more structured category, which is the smaller class of objects.
        Neither order is wrong and they are opposite, so the owned graph
        states its own rather than inheriting the backend's words.  The
        backend's *operators* already read in the owned order -- ``A & B`` is
        this meet and ``A | B`` is the join below -- and only the two names
        are inverted.
        """
        members = tuple(categories)
        assert members, "the meet of no categories is not represented"

        # ``Category.join`` builds one dynamic class from every supplied
        # branch.  A strict supercategory contributes no new mathematics to
        # an intersection once one of its subcategories is already present,
        # and retaining both can make Sage linearize the same inherited
        # method provider twice.  Remove only strict supercategories; leave
        # incomparable or merely equivalent categories intact.
        reduced = []
        for member in members:
            if any(
                other is not member
                and other.is_subcategory(member)
                and not member.is_subcategory(other)
                for other in members
            ):
                continue
            if all(member is not known for known in reduced):
                reduced.append(member)

        return reduced[0] if len(reduced) == 1 else Category.join(tuple(reduced))

    def join(self, categories: Iterable[Category]) -> Category:
        r"""Return the smallest category containing all of ``categories``.

        The least upper bound in the inclusion order: the objects of every
        member are objects of it, and it asks of them only what all of them
        ask.  ``Modules(ZZ)`` joined with ``FiniteSets()`` is ``Sets``.

        The backend spells it ``Category.meet``; see :meth:`meet` for why the
        two names arrive inverted.
        """
        members = tuple(categories)
        assert members, "the join of no categories is not represented"
        return Category.meet(members)

    def presheaves(self, category: Category, value_category: Category | None = None) -> Category:
        r"""The presheaf bifunctor on objects: \((C, D) \mapsto [C^{op}, D]\).

        ``Cat`` is not an object of itself here, so the bifunctor
        \(\mathbf{Cat}^{op} \times \mathbf{Cat} \to \mathbf{Cat}\) is stated by its two
        actions: this one on objects and :meth:`presheaf_transport` on arrows.
        """
        return category.presheaves(value_category)

    def presheaf_transport(self, site_functor: Functor, value_functor: Functor) -> Functor:
        r"""The presheaf bifunctor on arrows.

        For \(F: C' \to C\) and \(G: D \to D'\), the functor
        \([C^{op}, D] \to [C'^{op}, D']\) sending \(P \mapsto G \circ P \circ F^{op}\)
        and a natural transformation \(\eta\) to \(G \eta F^{op}\).
        """
        from dzack_research.preamble.categories.abstract_categories.presheaves import (
            _PresheafTransport,
        )

        return _PresheafTransport(site_functor, value_functor)

    def product(self, factors: Iterable[Category]) -> Category:
        r"""Return $\prod_{i \in I} C_i$, the product of a family of categories.

        This is the same word as ``Modules(R).product``: ``Cat`` is a category
        with products, and its objects happen to be categories.  ``C * D`` is
        the operator notation that delegates here.

        The represented product category has objects
        are pairs ``(X, Y)`` addressed as ``first()`` and ``second()`` and over
        which the bifunctors are defined, so only the two-element index set is
        represented.  A larger index set is not folded into nested pairs: that
        object has projections only to the two halves of the nest, which is
        not the product over the index set that was asked for.
        """
        from dzack_research.preamble.categories.abstract_categories.products import (
            _two_factors_of,
        )

        left, right = _two_factors_of(factors, name="Product factors")
        return self._categorical_product(left, right)

    def _categorical_product(self, left, right):
        from dzack_research.preamble.categories.abstract_categories.category_constructions import (
            _ProductCategory,
        )

        return _ProductCategory(left, right)

    def _repr_(self) -> str:
        return "Cat: categories with functors as morphisms"


class NaturalTransformationMorphism(Morphism):
    r"""A natural transformation as a morphism in a functor category."""

    def __init__(
        self,
        parent: NaturalTransformationHomset,
        transformation: NaturalTransformation,
    ) -> None:
        Morphism.__init__(self, parent)
        if transformation.source() is not self.domain().functor():
            raise ValueError("the natural transformation has the wrong source functor")
        if transformation.target() is not self.codomain().functor():
            raise ValueError("the natural transformation has the wrong target functor")
        self._transformation = transformation

    def transformation(self) -> NaturalTransformation:
        return self._transformation

    def component(self, obj: Parent) -> Morphism:
        return self.transformation().component(obj)

    def naturality_target_composite(self, morphism: Map) -> Morphism:
        return self.transformation().naturality_target_composite(morphism)

    def naturality_source_composite(self, morphism: Map) -> Morphism:
        return self.transformation().naturality_source_composite(morphism)

    def naturality_square(self, morphism: Map):
        return self.transformation().naturality_square(morphism)

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if parent(other) is not self.parent():
            return False
        if self.transformation() is other.transformation():
            return True
        # Different component functions need not define different natural
        # transformations, and the source category need not be finite.
        return Unknown

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        if self.domain() is self.codomain() and self is self.parent().identity():
            return other
        if other.domain() is other.codomain() and other is other.parent().identity():
            return self
        source = other.domain().functor()
        target = self.codomain().functor()

        composite = NaturalTransformation(
            source,
            target,
            lambda obj: self.component(obj) * other.component(obj),
        )
        return self.parent().functor_category().Mor(other.domain(), self.codomain())(
            composite
        )


class NaturalTransformationHomset(CategoricalHomset):
    Element = NaturalTransformationMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def functor_category(self) -> _FunctorCategory:
        return self.base_category()

    def source(self) -> Functor:
        return self.domain().functor()

    def target(self) -> Functor:
        return self.codomain().functor()

    def _element_constructor_(self, transformation):
        r"""A natural transformation between these two functors, given as one or by its components."""
        return self._transformation(transformation)

    def _transformation(self, transformation, *, element_class=None, construction_data=None):
        r"""Construct one transformation, optionally with a private realization."""
        match transformation:
            case NaturalTransformationMorphism():
                if transformation.parent() is self and element_class is None and construction_data is None:
                    return transformation
                transformation = transformation.transformation()
            case NaturalTransformation():
                pass
            case _:
                transformation = NaturalTransformation(
                    self.domain().functor(), self.codomain().functor(), transformation
                )
        selected = NaturalTransformationMorphism if element_class is None else element_class
        return selected(self, transformation, **dict(construction_data or {}))

    @cached_method
    def identity(self) -> NaturalTransformationMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism natural-transformation Hom-set")
        functor = self.domain().functor()


        return self(
            NaturalTransformation(
                functor,
                functor,
                lambda obj: _category_homset(
                    functor.codomain(), functor(obj), functor(obj)
                ).identity(),
            )
        )


class NaturalTransformationHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = NaturalTransformationHomset


class _FunctorCategory(FixedHomCategory):
    r"""The category ``[C,D]`` of represented functors and natural transformations.

    Unverified construction specimens: all Cat Hom entrances select one
    category, whose morphisms are actual natural transformations::

        sage: from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: points = finite_ordered_set(("a", "b"))
        sage: category = DiscreteCategory(points)
        sage: cat = Cat()
        sage: hom = cat.Mor(category, category)
        sage: hom is cat.HomCategory().Of(category, category)
        True
        sage: hom is cat.EndCategory().Between(category, cat.object(category))
        True
        sage: hom.arrow_set() is cat.functor_homset(category, category)
        True
        sage: identity = IdentityFunctor(category)
        sage: transformations = identity.natural_transformations_to(identity)
        sage: transformations is hom.Mor(hom(identity), hom(identity))
        True
        sage: transformations is hom.arrow_set().two_hom(identity, identity)
        True
        sage: transformations is hom.arrow_set().category_packet().Homs().Of(identity, identity)
        True
        sage: eta = transformations(lambda obj: category.Mor(obj, obj).identity())
        sage: (eta * eta).component(category("a")) == eta.component(category("a"))
        True
        sage: transformations.identity() * eta is eta
        True
        sage: eta * transformations.identity() is eta
        True
        sage: IdentityFunctor(hom)(eta) is eta
        True
        sage: hom.identity_2(cat.arrow(identity)).parent() is transformations
        True
        sage: arrows = cat.ArrowCategory()
        sage: obj = arrows(cat.arrow(identity))
        sage: square = arrows.Mor(obj, obj).identity()
        sage: square * square == square
        True
    """

    _HomCategory = NaturalTransformationHomCategoryConstruction

    @staticmethod
    def __classcall__(cls, category_of_categories: Cat, domain: Category, codomain: Category):
        r"""``[C, D]`` is built only by ``Cat``'s Hom family, which interns it.

        Naming a realization directly asks that family, so the walking-arrow
        realization is the same object as ``Cat().Mor([1], C)``.  A subclass
        that is a category of its own states its own classcall.
        """
        match cls:
            case DynamicMetaclass():
                return cls.__base__(category_of_categories, domain, codomain)
        return category_of_categories.HomCategory().Of(domain, codomain)

    def __init__(
        self,
        category_of_categories: Cat,
        domain: Category,
        codomain: Category,
    ) -> None:
        self._cat = category_of_categories
        self._domain_category = domain
        self._codomain_category = codomain
        FixedHomCategory.__init__(
            self,
            category_of_categories.HomCategory(),
            category_of_categories.object(domain),
            category_of_categories.object(codomain),
        )

    def _make_named_class_key(self, name):
        return self._cat, self._domain_category, self._codomain_category

    def category_of_categories(self) -> Cat:
        return self._cat

    def domain_category(self) -> Category:
        return self._domain_category

    def codomain_category(self) -> Category:
        return self._codomain_category

    def arrow_set(self) -> CategoryFunctorHomset:
        r"""The canonical Hom-set of functors classified by ``[C,D]``."""
        return self._cat.functor_homset(self.domain_category(), self.codomain_category())

    underlying_homset = arrow_set

    def from_object_map(self, object_map):
        r"""Return the functor induced by an object-set map between discrete categories."""
        from dzack_research.preamble.categories.abstract_categories.functors import (
            _DiscreteFunctor,
        )

        return _DiscreteFunctor(
            self.domain_category(),
            self.codomain_category(),
            object_map,
        )

    def discrete_diagram(self, values):
        r"""Return the diagram on a discrete domain with the selected object family."""
        from dzack_research.preamble.categories.abstract_categories.functors import (
            _DiscreteDiagram,
        )

        return _DiscreteDiagram(
            self.domain_category(),
            self.codomain_category(),
            values,
        )

    def constant_functor(self, value):
        r"""Return the constant functor at ``value`` in this functor category."""
        from dzack_research.preamble.categories.abstract_categories.functors import (
            _ConstantDiagram,
        )

        return _ConstantDiagram(
            self.domain_category(),
            self.codomain_category(),
            value,
        )

    def super_categories(self):
        return [Objects()]

    class ParentMethods:
        r"""A functor ``F: C -> D`` as an object of ``[C, D]``.

        The functor is the defining datum.  It is stored here and nowhere
        else; every other operation on the object reads it.
        """

        def __init__(self, functor: Functor, **rest) -> None:
            self._functor = functor
            super().__init__(**rest)

        def functor(self) -> Functor:
            return self._functor

        def functor_category(self) -> _FunctorCategory:
            r"""``[C, D]`` for the functor's own endpoints, whichever subcategory the object was built in."""
            return self.functor().functor_category()

        def arrow(self) -> CategoryFunctorMorphism:
            r"""Return the same functor as the corresponding morphism in ``Cat``."""
            return Cat().arrow(self.functor())

        def _repr_(self) -> str:
            return f"Functor object ({self.functor()})"

    def object(
        self,
        functor: Functor | CategoryFunctorMorphism,
        *,
        _engine=None,
        construction_data=None,
    ):
        r"""The object of ``[C, D]`` on a functor ``C -> D``: this category's one entry.

        The input is the functor, or the morphism of ``Cat`` that is the same
        functor.  A private realization may retain construction-specific data
        without creating a second public object path.
        """
        match functor:
            case CategoryFunctorMorphism():
                functor = functor.functor()
        if not self._has_endpoints_of(functor):
            raise ValueError("the functor has the wrong functor-category endpoints")
        if _engine is None and construction_data is None:
            return self._object_on(functor)
        return _object_of(
            self,
            _engine=None if _engine is None else (self, _engine, None),
            functor=functor,
            **dict(construction_data or {}),
        )

    def _has_endpoints_of(self, functor: Functor) -> bool:
        r"""Whether ``functor`` runs from this category's domain to its codomain."""
        return functor.domain() == self.domain_category() and functor.codomain() == self.codomain_category()

    @cached_method(key=lambda self, functor: id(functor))
    def _object_on(self, functor: Functor):
        return _object_of(self, functor=functor)

    __call__ = object

    def _hom_endpoint(
        self,
        obj: Parent | Category | Functor | CategoryFunctorMorphism,
    ):
        r"""An endpoint of a natural-transformation Hom: an object, or the functor it is built on."""
        match obj:
            case Functor() | CategoryFunctorMorphism():
                return self.object(obj)
            case _:
                return obj

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is an object of ``[C, D]``.

        An object built by this category's entry, or in a subcategory of it,
        is one by placement.  A functor ``C -> D`` is the defining datum of
        one, and so is the morphism of ``Cat`` that is that functor.
        """
        match candidate:
            case Functor():
                return self._has_endpoints_of(candidate)
            case CategoryFunctorMorphism():
                return self._has_endpoints_of(candidate.functor())
            case _:
                return Category.__contains__(self, candidate)

    def Mor(
        self,
        domain: Parent | Functor | CategoryFunctorMorphism,
        codomain: Parent | Functor | CategoryFunctorMorphism,
    ) -> NaturalTransformationHomset:
        domain = self._hom_endpoint(domain)
        codomain = self._hom_endpoint(codomain)
        if domain not in self or codomain not in self:
            raise TypeError("a natural-transformation Hom requires two parallel functors")
        return self.HomCategory().Of(domain, codomain)

    two_hom = Mor

    def identity_2(self, arrow: Functor | CategoryFunctorMorphism) -> NaturalTransformationMorphism:
        obj = self.object(arrow)
        return self.Mor(obj, obj).identity()

    def identity(self, functor_object: Parent) -> NaturalTransformationMorphism:
        return self.Mor(functor_object, functor_object).identity()

    def _repr_(self) -> str:
        return f"Functor category [{self.domain_category()}, {self.codomain_category()}]"


__all__ = [
    "Cat",
    "CategoryFunctorHomset",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "NaturalTransformationHomset",
    "NaturalTransformationMorphism",
]
