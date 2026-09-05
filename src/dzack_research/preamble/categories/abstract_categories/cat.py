r"""A represented category ``Cat`` of categories, functors, and natural transformations."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from sage.categories.objects import Objects as SageObjects
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    fold_construction,
)
from dzack_research.preamble.categories.functors.core import (
    CompositeFunctor,
    IdentityFunctor,
    NaturalTransformation,
)



class CategoryObject(Parent):
    r"""A Sage category regarded as an object of ``Cat``."""

    def __init__(self, category_of_categories, represented_category) -> None:
        self._category_of_categories = category_of_categories
        self._represented_category = represented_category
        Parent.__init__(self, category=category_of_categories)

    def category_of_categories(self):
        return self._category_of_categories

    def represented_category(self):
        return self._represented_category

    def _repr_(self) -> str:
        return f"[{self.represented_category()}]"


class CategoryFunctorMorphism(Morphism):
    r"""A live functor regarded as a morphism in ``Cat``."""

    def __init__(self, parent, functor) -> None:
        Morphism.__init__(self, parent)
        if functor.domain() != self.domain().represented_category():
            raise ValueError("the functor has the wrong Cat-domain")
        if functor.codomain() != self.codomain().represented_category():
            raise ValueError("the functor has the wrong Cat-codomain")
        self._functor = functor

    def functor(self):
        return self._functor

    def __call__(self, value):
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

    def __init__(self, category_of_categories, domain, codomain) -> None:
        self._category_of_categories = category_of_categories
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(category_of_categories), domain, codomain
        )

    def category_of_categories(self):
        return self._category_of_categories

    def _element_constructor_(self, functor):
        return CategoryFunctorMorphism(self, functor)

    def identity(self):
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


    def super_categories(self):
        # A category is an object.  This one edge names Sage's ``Objects`` and
        # not the owned one: every owned category is an object of ``Cat``, so
        # an owned supercategory here would have to be constructed while
        # ``Cat`` itself is still under construction.  The owned ``Objects``
        # is a category like any other and is an object of ``Cat``; it is this
        # Sage runtime edge that is Sage's.
        return [SageObjects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, (Category, CategoryObject))

    def object(self, category):
        if isinstance(category, CategoryObject):
            return category
        if not isinstance(category, Category):
            raise TypeError("an object of Cat is a category")
        return self._object_on(category)

    @cached_method
    def _object_on(self, category):
        return CategoryObject(self, category)

    def functor_homset(self, domain, codomain):
        return CategoryFunctorHomset(self, self.object(domain), self.object(codomain))

    def arrow(self, functor):
        key = id(functor)
        cached = self._arrows.get(key)
        if cached is not None and cached.functor() is functor:
            return cached
        result = self.functor_homset(functor.domain(), functor.codomain())(functor)
        self._arrows[key] = result
        return result

    def Mor(self, domain, codomain):
        return FunctorCategory(self, domain, codomain)

    def identity(self, category):
        return self.functor_homset(category, category).identity()

    def compose(self, second, first):
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
        def ObjectType(self):
            r"""Return the complete implementation type for objects of this category."""
            return self.parent_class

        @property
        def ElementType(self):
            r"""Return the complete implementation type for their elements."""
            return self.element_class

        def fiber_product(self, left_leg, right_leg):
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

        def pushout(self, left_leg, right_leg):
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

        def opposite(self):
            r"""Return \(C^{op}\)."""
            from dzack_research.preamble.categories.abstract_categories.category_constructions import (
                OppositeCategory,
            )

            return OppositeCategory(self)
        def Core(self):
            r"""Return the maximal groupoid inside this category."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CoreCategory,
            )

            return CoreCategory(self)
        def ArrowCategory(self):
            r"""Return \(\mathrm{Ar}(C)=\mathrm{Fun}([1],C)\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                ArrowCategory as _ArrowCategory,
            )

            return _ArrowCategory(self)
        def SliceOver(self, base_object):
            r"""Return the slice \(C/X\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SliceCategory,
            )

            return SliceCategory(self, base_object)
        def CosliceUnder(self, base_object):
            r"""Return the coslice \(X/C\)."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                CosliceCategory,
            )

            return CosliceCategory(self, base_object)
        def SubobjectCategory(self, base_object):
            r"""Return the category of subobjects of ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SubobjectCategory,
            )

            return SubobjectCategory(self, base_object)
        def SuperobjectCategory(self, base_object):
            r"""Return the category of superobjects of ``base_object`` here."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SuperobjectCategory,
            )

            return SuperobjectCategory(self, base_object)
        def _fold_construction(self, binary_construction, factors, *, name):
            r"""Return the construction over a finite family, from the binary one."""
            return fold_construction(binary_construction, factors, name=name)

    def ArrowCategory(self):
        r"""Return the arrow category of ``Cat``.

        Its own method because ``Cat`` is not an object of ``Cat``, so it
        does not inherit the constructions every other category gets.
        """
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            ArrowCategory as _ArrowCategory,
        )

        return _ArrowCategory(self)

    def product(self, factors):
        r"""Return the product of a finite family of categories.

        This is the same word as ``Modules(R).product``: ``Cat`` is a category
        with products, and its objects happen to be categories.  ``C * D`` is
        the operator notation that delegates here.
        """
        return fold_construction(
            self._categorical_product, factors, name="Product factors"
        )

    def _categorical_product(self, left, right):
        from dzack_research.preamble.categories.abstract_categories.category_constructions import (
            ProductCategory,
        )

        return ProductCategory(left, right)

    def _repr_(self) -> str:
        return "Category of categories"


class NaturalTransformationMorphism(Morphism):
    r"""A natural transformation as a morphism in a functor category."""

    def __init__(self, parent, transformation) -> None:
        Morphism.__init__(self, parent)
        if transformation.source() is not self.domain().arrow().functor():
            raise ValueError("the natural transformation has the wrong source functor")
        if transformation.target() is not self.codomain().arrow().functor():
            raise ValueError("the natural transformation has the wrong target functor")
        self._transformation = transformation

    def transformation(self):
        return self._transformation

    def component(self, obj):
        return self.transformation().component(obj)

    def naturality_square(self, morphism):
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

    def __init__(self, functor_category, domain, codomain) -> None:
        self._functor_category = functor_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(functor_category), domain, codomain
        )

    def functor_category(self):
        return self._functor_category

    def _element_constructor_(self, transformation):

        if callable(transformation) and not isinstance(transformation, NaturalTransformation):
            transformation = NaturalTransformation(
                self.domain().arrow().functor(), self.codomain().arrow().functor(), transformation
            )
        return NaturalTransformationMorphism(self, transformation)

    def identity(self):
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

    def __init__(self, category_of_categories, domain, codomain) -> None:
        self._cat = category_of_categories
        self._domain_category = domain
        self._codomain_category = codomain
        super().__init__()

    def _make_named_class_key(self, name):
        return self._cat, self._domain_category, self._codomain_category

    def domain_category(self):
        return self._domain_category

    def codomain_category(self):
        return self._codomain_category

    def super_categories(self):
        return [Objects()]

    def object(self, functor):
        if functor.domain() != self.domain_category() or functor.codomain() != self.codomain_category():
            raise ValueError("the functor has the wrong functor-category endpoints")
        return self._object_on(functor)

    @cached_method
    def _object_on(self, functor):
        return self._cat.ArrowCategory()(self._cat.arrow(functor))

    __call__ = object

    def __contains__(self, candidate) -> bool:
        try:
            arrow = candidate.arrow()
        except AttributeError:
            return False
        return (
            isinstance(arrow, CategoryFunctorMorphism)
            and arrow.functor().domain() == self.domain_category()
            and arrow.functor().codomain() == self.codomain_category()
        )

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a natural-transformation Hom requires two parallel functors")
        return NaturalTransformationHomset(self, domain, codomain)


    def identity(self, functor_object):
        return self.Mor(functor_object, functor_object).identity()

    def _repr_(self) -> str:
        return f"Functor category [{self.domain_category()}, {self.codomain_category()}]"


class NaturalIsomorphism:
    r"""A selected pair of mutually inverse natural transformations."""

    def __init__(self, forward, inverse) -> None:
        if forward.domain() is not inverse.codomain() or forward.codomain() is not inverse.domain():
            raise ValueError("inverse natural transformations have reversed endpoints")
        self._forward = forward
        self._inverse = inverse

    def forward(self):
        return self._forward

    def inverse(self):
        return self._inverse

    def component(self, obj):
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
