r"""A represented category ``Cat`` of categories, functors, and natural transformations."""

from collections.abc import Iterable
from typing import Any, overload

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.element import Element
from sage.structure.parent import Parent

from sage.categories.objects import Objects as SageObjects
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily
from dzack_research.preamble.categories.functors.core import (
    CompositeFunctor,
    Functor,
    IdentityFunctor,
    NaturalTransformation,
)



class CategoryObject(Parent):
    r"""A Sage category regarded as an object of ``Cat``."""

    def __init__(
        self,
        category_of_categories: "Cat",
        represented_category: Category,
    ) -> None:
        self._category_of_categories = category_of_categories
        self._represented_category = represented_category
        Parent.__init__(self, category=category_of_categories)

    def category_of_categories(self) -> "Cat":
        return self._category_of_categories

    def represented_category(self) -> Category:
        return self._represented_category

    def _repr_(self) -> str:
        return f"[{self.represented_category()}]"


class CategoryFunctorMorphism(Morphism):
    r"""A live functor regarded as a morphism in ``Cat``."""

    def __init__(self, parent: "CategoryFunctorHomset", functor: Functor) -> None:
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

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented

        return self.parent().category_of_categories().arrow(
            CompositeFunctor(other.functor(), self.functor())
        )

    def _repr_(self) -> str:
        return repr(self.functor())


class CategoryFunctorHomset(CategoricalHomset):
    Element = CategoryFunctorMorphism

    def __init__(
        self,
        category_of_categories: "Cat",
        domain: CategoryObject,
        codomain: CategoryObject,
    ) -> None:
        self._category_of_categories = category_of_categories
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(category_of_categories), domain, codomain
        )

    def category_of_categories(self) -> "Cat":
        return self._category_of_categories

    def _element_constructor_(self, functor):
        return CategoryFunctorMorphism(self, functor)

    def identity(self) -> CategoryFunctorMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism functor Hom-set")

        return self(IdentityFunctor(self.domain().represented_category()))


class Cat(Category):
    r"""The represented category of categories.

    ``Cat`` deliberately does not take the owned base that makes a category an
    object of ``Cat``.  Applying it here would assert a self-membership
    statement and would make ``Cat().Mor(Cat(), Cat())`` an apparent
    1-categorical construction; that higher level is not modelled.  Every
    other owned category is such an object.
    """

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

    def __contains__(self, candidate: Any) -> bool:
        return isinstance(candidate, (Category, CategoryObject))

    def object(self, category: Category | CategoryObject) -> CategoryObject:
        if isinstance(category, CategoryObject):
            return category
        if not isinstance(category, Category):
            raise TypeError("an object of Cat is a category")
        return self._object_on(category)

    @cached_method
    def _object_on(self, category):
        return CategoryObject(self, category)

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

    def Mor(self, domain: Category, codomain: Category) -> "FunctorCategory":
        return FunctorCategory(self, domain, codomain)

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

        One home for the operations on categories.  Every owned category
        receives them through ``subcategory_class``, which
        ``CatConstructionsMixin`` on the owned root builds with this class
        among its bases -- not through parenthood, which states separately
        that a category is an object of ``Cat``.
        """

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
        def _categorical_coproduct(self, left: Parent, right: Parent) -> Parent:
            r"""Return this category's represented coproduct of two objects."""

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
        def _categorical_coequalizer(
            self,
            left_morphism: Morphism,
            right_morphism: Morphism,
        ) -> Parent:
            r"""Return this category's represented coequalizer of parallel arrows."""

        @abstract_method(optional=True)
        def _categorical_equalizer_family(self, morphisms: IndexedFamily) -> Parent:
            r"""Return this category's represented equalizer of an indexed arrow family."""

        @abstract_method(optional=True)
        def _categorical_coequalizer_family(self, morphisms: IndexedFamily) -> Parent:
            r"""Return this category's represented coequalizer of an indexed arrow family."""

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
                Span,
            )

            return Span(left_leg, right_leg)

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
            return self.coequalizer(
                total.left_injection() * left_leg,
                total.right_injection() * right_leg,
            )

        def opposite(self) -> Category:
            r"""Return \(C^{op}\)."""
            from dzack_research.preamble.categories.abstract_categories.category_constructions import (
                OppositeCategory,
            )

            return OppositeCategory(self)
        def Core(self) -> Category:
            r"""Return the maximal groupoid inside this category."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CoreCategory,
            )

            return CoreCategory(self)
        def ArrowCategory(self) -> Category:
            r"""Return \(\mathrm{Ar}(C)=\mathrm{Fun}([1],C)\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                ArrowCategory as _ArrowCategory,
            )

            return _ArrowCategory(self)
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
            r"""Return the category of superobjects of ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SuperobjectCategory,
            )

            return SuperobjectCategory(self, base_object)

    def ArrowCategory(self) -> Category:
        r"""Return the arrow category of ``Cat``.

        Its own method because ``Cat`` is not an object of ``Cat``, so it
        does not inherit the constructions every other category gets.
        """
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            ArrowCategory as _ArrowCategory,
        )

        return _ArrowCategory(self)

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
        return Category.join(members)

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

    def product(self, factors: Iterable[Category]) -> Category:
        r"""Return $\prod_{i \in I} C_i$, the product of a family of categories.

        This is the same word as ``Modules(R).product``: ``Cat`` is a category
        with products, and its objects happen to be categories.  ``C * D`` is
        the operator notation that delegates here.

        The represented product category is ``ProductCategory``, whose objects
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
            ProductCategory,
        )

        return ProductCategory(left, right)

    def _repr_(self) -> str:
        return "Category of categories"


class NaturalTransformationMorphism(Morphism):
    r"""A natural transformation as a morphism in a functor category."""

    def __init__(
        self,
        parent: "NaturalTransformationHomset",
        transformation: NaturalTransformation,
    ) -> None:
        Morphism.__init__(self, parent)
        if transformation.source() is not self.domain().arrow().functor():
            raise ValueError("the natural transformation has the wrong source functor")
        if transformation.target() is not self.codomain().arrow().functor():
            raise ValueError("the natural transformation has the wrong target functor")
        self._transformation = transformation

    def transformation(self) -> NaturalTransformation:
        return self._transformation

    def component(self, obj: Parent) -> Morphism:
        return self.transformation().component(obj)

    def naturality_square(self, morphism: Map) -> tuple[Morphism, Morphism]:
        return self.transformation().naturality_square(morphism)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain().arrow().functor()
        target = self.codomain().arrow().functor()

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
        functor_category: "FunctorCategory",
        domain: Parent,
        codomain: Parent,
    ) -> None:
        self._functor_category = functor_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(functor_category), domain, codomain
        )

    def functor_category(self) -> "FunctorCategory":
        return self._functor_category

    def _element_constructor_(self, transformation):

        if callable(transformation) and not isinstance(transformation, NaturalTransformation):
            transformation = NaturalTransformation(
                self.domain().arrow().functor(), self.codomain().arrow().functor(), transformation
            )
        return NaturalTransformationMorphism(self, transformation)

    def identity(self) -> NaturalTransformationMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism natural-transformation Hom-set")
        functor = self.domain().arrow().functor()


        return self(
            NaturalTransformation(
                functor,
                functor,
                lambda obj: functor.codomain().Mor(
                    functor(obj), functor(obj)
                ).identity(),
            )
        )


class FunctorCategory(Category):
    r"""The category ``[C,D]`` of represented functors and natural transformations."""

    def __init__(
        self,
        category_of_categories: Cat,
        domain: Category,
        codomain: Category,
    ) -> None:
        self._cat = category_of_categories
        self._domain_category = domain
        self._codomain_category = codomain
        super().__init__()

    def _make_named_class_key(self, name):
        return self._cat, self._domain_category, self._codomain_category

    def domain_category(self) -> Category:
        return self._domain_category

    def codomain_category(self) -> Category:
        return self._codomain_category

    def super_categories(self):
        return [Objects()]

    def object(self, functor: Functor) -> Parent:
        if functor.domain() != self.domain_category() or functor.codomain() != self.codomain_category():
            raise ValueError("the functor has the wrong functor-category endpoints")
        return self._object_on(functor)

    @cached_method
    def _object_on(self, functor):
        return self._cat.ArrowCategory()(self._cat.arrow(functor))

    __call__ = object

    def __contains__(self, candidate: Any) -> bool:
        try:
            arrow = candidate.arrow()
        except AttributeError:
            return False
        return (
            isinstance(arrow, CategoryFunctorMorphism)
            and arrow.functor().domain() == self.domain_category()
            and arrow.functor().codomain() == self.codomain_category()
        )

    def Mor(self, domain: Parent, codomain: Parent) -> NaturalTransformationHomset:
        if domain not in self or codomain not in self:
            raise TypeError("a natural-transformation Hom requires two parallel functors")
        return NaturalTransformationHomset(self, domain, codomain)


    def identity(self, functor_object: Parent) -> NaturalTransformationMorphism:
        return self.Mor(functor_object, functor_object).identity()

    def _repr_(self) -> str:
        return f"Functor category [{self.domain_category()}, {self.codomain_category()}]"


class NaturalIsomorphism:
    r"""A selected pair of mutually inverse natural transformations."""

    def __init__(self, forward: Morphism, inverse: Morphism) -> None:
        if forward.domain() is not inverse.codomain() or forward.codomain() is not inverse.domain():
            raise ValueError("inverse natural transformations have reversed endpoints")
        self._forward = forward
        self._inverse = inverse

    def forward(self) -> Morphism:
        return self._forward

    def inverse(self) -> Morphism:
        return self._inverse

    def component(self, obj: Parent) -> Morphism:
        return self.forward().component(obj)


__all__ = [
    "Cat",
    "CategoryFunctorHomset",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "FunctorCategory",
    "NaturalIsomorphism",
    "NaturalTransformationHomset",
    "NaturalTransformationMorphism",
]
