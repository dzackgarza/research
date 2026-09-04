r"""Basic categorical functors used by the abstract construction layer."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.categories.homset import Hom, Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
)
from dzack_research.preamble.categories.functors.core import (
    CompositeFunctor,
    Functor,
    IdentityFunctor,
    NaturalTransformation,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.set_categories import Sets


class ContravariantFunctor(Functor):
    r"""A functor ``C^op -> D`` with convenience calls on arrows of ``C``."""

    def __init__(self, domain, codomain) -> None:
        from dzack_research.preamble.categories.abstract_categories.category_constructions import OppositeCategory

        self._base_domain = domain
        super().__init__(OppositeCategory(domain), codomain)

    def base_domain(self):
        return self._base_domain

    def _apply_contravariant_object(self, obj):
        raise NotImplementedError

    def _apply_contravariant_morphism(self, morphism):
        raise NotImplementedError

    def _apply_object(self, opposite_object):
        return self._apply_contravariant_object(opposite_object.underlying_object())

    def _apply_morphism(self, opposite_morphism):
        return self._apply_contravariant_morphism(opposite_morphism.underlying_arrow())

    def object_image(self, obj):
        if obj in self.base_domain():
            obj = self.domain()(obj)
        return super().object_image(obj)

    def morphism_image(self, morphism):
        from dzack_research.preamble.categories.abstract_categories.category_constructions import OppositeMorphism

        if not isinstance(morphism, Map):
            raise TypeError("a contravariant functor acts on morphisms")
        if not isinstance(morphism, OppositeMorphism):
            source = self.domain()(morphism.codomain())
            target = self.domain()(morphism.domain())
            morphism = self.domain().mor(source, target)(morphism)
        return super().morphism_image(morphism)

    def chosen_preimage(self, image):
        return super().chosen_preimage(image).underlying_object()

    def adopt_object_image(self, preimage, image):
        if preimage in self.base_domain():
            preimage = self.domain()(preimage)
        return super().adopt_object_image(preimage, image)


class Bifunctor(Functor):
    r"""A functor ``C x D -> E`` with a two-argument convenience API."""

    def __init__(self, left_domain, right_domain, codomain) -> None:
        from dzack_research.preamble.categories.abstract_categories.category_constructions import ProductCategory

        super().__init__(ProductCategory(left_domain, right_domain), codomain)

    def left_domain(self):
        return self.domain().first_category()

    def right_domain(self):
        return self.domain().second_category()

    def _apply_pair_object(self, left, right):
        raise NotImplementedError

    def _apply_pair_morphism(self, left_morphism, right_morphism):
        raise NotImplementedError

    def _apply_object(self, pair):
        return self._apply_pair_object(pair.first(), pair.second())

    def _apply_morphism(self, pair_morphism):
        return self._apply_pair_morphism(
            pair_morphism.first(), pair_morphism.second()
        )

    def object_image(self, left, right=None):
        pair = left if right is None else self.domain()(left, right)
        return super().object_image(pair)

    def morphism_image(self, left_morphism, right_morphism=None):
        if right_morphism is None:
            return super().morphism_image(left_morphism)
        if not isinstance(left_morphism, Map) or not isinstance(right_morphism, Map):
            raise TypeError("a bifunctor acts on a pair of morphisms")
        source = self.domain()(left_morphism.domain(), right_morphism.domain())
        target = self.domain()(left_morphism.codomain(), right_morphism.codomain())
        pair = self.domain().mor(source, target)(left_morphism, right_morphism)
        return super().morphism_image(pair)

    def __call__(self, left, right=None):
        if right is None:
            return super().__call__(left)
        if isinstance(left, Map) or isinstance(right, Map):
            return self.morphism_image(left, right)
        return self.object_image(left, right)


def _identity(obj):
    try:
        return Hom(obj, obj).identity()
    except (TypeError, ValueError):
        return Sets().mor(obj, obj).identity()


class ImageInclusionFunctor(Functor):
    r"""Forget the chosen preimage of a presented functor-image object."""

    _faithful = True

    def __init__(self, image_category) -> None:
        self._image_category = image_category
        super().__init__(image_category, image_category.functor().codomain())

    def image_category(self):
        return self._image_category

    def _apply_object(self, presented):
        return presented.image_object()

    def _apply_morphism(self, morphism):
        return morphism.codomain_arrow()

    def _repr_(self):
        return f"Inclusion of {self.image_category()} into {self.codomain()}"


class DomainFunctor(Functor):
    r"""The domain functor ``Arr(C) -> C``."""

    def __init__(self, category) -> None:
        super().__init__(ArrowCategory(category), category)

    def _apply_object(self, arrow_object):
        return arrow_object.source_object()

    def _apply_morphism(self, square):
        return square.left()


class CodomainFunctor(Functor):
    r"""The codomain functor ``Arr(C) -> C``."""

    def __init__(self, category) -> None:
        super().__init__(ArrowCategory(category), category)

    def _apply_object(self, arrow_object):
        return arrow_object.target_object()

    def _apply_morphism(self, square):
        return square.right()


class DiscreteObject(Parent):
    r"""One object of the discrete category on a set."""

    def __init__(self, discrete_category, value) -> None:
        self._discrete_category = discrete_category
        self._value = value
        Parent.__init__(self, category=SageSets())

    def discrete_category(self):
        return self._discrete_category

    def value(self):
        return self._value

    def _repr_(self) -> str:
        return repr(self.value())


class DiscreteMorphism(Morphism):
    r"""The unique identity arrow of a discrete-category object."""

    def __init__(self, parent) -> None:
        Morphism.__init__(self, parent)
        if self.domain() is not self.codomain():
            raise ValueError("a discrete category has no arrow between distinct objects")

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().discrete_category().mor(other.domain(), self.codomain()).identity()


class DiscreteHomset(OwnedHomset):
    Element = DiscreteMorphism

    def __init__(self, discrete_category, domain, codomain) -> None:
        self._discrete_category = discrete_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def discrete_category(self):
        return self._discrete_category

    def cardinality(self):
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        return cardinal(1 if self.domain() is self.codomain() else 0)

    def _element_constructor_(self, value=None):
        if self.domain() is not self.codomain():
            raise ValueError("there is no arrow between distinct discrete objects")
        return DiscreteMorphism(self)

    def identity(self):
        return self()


class DiscreteCategory(Category):
    r"""The discrete category on one set."""

    def __init__(self, object_set) -> None:
        if object_set not in Sets():
            raise TypeError("a discrete category is constructed from a set")
        self._object_set = object_set
        super().__init__()

    def _make_named_class_key(self, name):
        return self._object_set

    def object_set(self):
        return self._object_set

    def super_categories(self):
        return [Objects()]

    def object(self, value):
        return self._object_on(self.object_set()(value))

    @cached_method
    def _object_on(self, normalized):
        return DiscreteObject(self, normalized)

    __call__ = object

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, DiscreteObject)
            and candidate.discrete_category().object_set() is self.object_set()
        )

    def objects(self):
        from dzack_research.preamble.categories.sets.indexed_families import indexed_family

        return indexed_family(
            self.object_set(),
            self,
            name=f"Objects of {self}",
        )

    def mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a discrete Hom requires two objects of the discrete category")
        return DiscreteHomset(self, domain, codomain)

    Mor = mor

    def identity(self, obj):
        return self.mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Discrete category on {self.object_set()}"


class DiscreteCategories(Category):
    r"""The category of represented discrete categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        from dzack_research.preamble.categories.abstract_categories.cat import CategoryObject

        if isinstance(candidate, CategoryObject):
            candidate = candidate.represented_category()
        return isinstance(candidate, DiscreteCategory)


class DiscreteFunctor(Functor):
    r"""A functor between discrete categories induced by a map of object sets."""

    def __init__(self, domain, codomain, object_map) -> None:
        if not isinstance(object_map, Morphism):
            object_map = SetMorphism(
                Sets().mor(domain.object_set(), codomain.object_set()),
                object_map,
            )
        if object_map.domain() is not domain.object_set() or object_map.codomain() is not codomain.object_set():
            raise ValueError("the object map has the wrong discrete-category endpoints")
        self._object_map = object_map
        super().__init__(domain, codomain)

    def object_map(self):
        return self._object_map

    def _apply_object(self, obj):
        return self.codomain()(self.object_map()(obj.value()))

    def _apply_morphism(self, morphism):
        return self.codomain().identity(self(morphism.domain()))


class ObjectSetFunctor(Functor):
    r"""Take the object set of a represented discrete category."""

    def __init__(self) -> None:
        super().__init__(DiscreteCategories(), Sets())

    def _apply_object(self, category):
        from dzack_research.preamble.categories.abstract_categories.cat import CategoryObject

        if isinstance(category, CategoryObject):
            category = category.represented_category()
        return category.object_set()

    def _apply_morphism(self, functor):
        return functor.functor().object_map()


class DiscreteDiagram(Functor):
    r"""A functor from a discrete category, specified on its objects."""

    def __init__(self, index_category, codomain, values) -> None:
        if index_category not in DiscreteCategories():
            raise TypeError("a discrete diagram requires a discrete index category")
        self._values = values
        super().__init__(index_category, codomain)

    def diagram_objects(self):
        return self._values

    def _apply_object(self, index):
        return self._values(index.value())

    def _apply_morphism(self, morphism):
        return _identity(self(morphism.domain()))


class ConstantDiagram(Functor):
    r"""The constant functor from an index category at one object."""

    def __init__(self, index_category, codomain, value) -> None:
        if value not in codomain:
            raise TypeError("the constant value lies outside the codomain")
        self._value = value
        super().__init__(index_category, codomain)

    def constant_value(self):
        return self._value

    def _apply_object(self, index):
        return self.constant_value()

    def _apply_morphism(self, morphism):
        return _identity(self.constant_value())


def compose_functors(second, first):
    r"""Return ``second ∘ first`` in the current functor core."""
    if first.codomain() != second.domain():
        raise ValueError("functors compose only when their middle category agrees")
    if isinstance(first, IdentityFunctor):
        return second
    if isinstance(second, IdentityFunctor):
        return first
    return CompositeFunctor(first, second)


ComposedFunctor = CompositeFunctor


def NaturalTransformations(source, target):
    r"""Return the represented type of natural transformations between parallel functors."""
    if source.domain() != target.domain() or source.codomain() != target.codomain():
        raise ValueError("natural transformations require parallel functors")
    return NaturalTransformationSpace(source, target)


class NaturalTransformationSpace(Parent):
    r"""The represented Hom-object of natural transformations ``F => G``."""

    def __init__(self, source, target) -> None:
        self._source = source
        self._target = target
        Parent.__init__(self, category=SageSets())

    def source(self):
        return self._source

    def target(self):
        return self._target

    def _element_constructor_(self, components):
        return NaturalTransformation(self.source(), self.target(), components)


def NaturalIsomorphism(source, target, components, inverse_components):
    r"""Return mutually inverse natural transformations as a categorical pair."""
    return (
        NaturalTransformation(source, target, components),
        NaturalTransformation(target, source, inverse_components),
    )


__all__ = [
    "CodomainFunctor",
    "ComposedFunctor",
    "ConstantDiagram",
    "DiscreteCategories",
    "DiscreteCategory",
    "DiscreteDiagram",
    "DiscreteFunctor",
    "DomainFunctor",
    "ImageInclusionFunctor",
    "NaturalIsomorphism",
    "NaturalTransformationSpace",
    "NaturalTransformations",
    "ObjectSetFunctor",
    "compose_functors",
    "CartesianProductFunctor",
    "ColimitFunctor",
    "CoproductFunctor",
    "DiagonalFunctor",
    "DisjointUnionFunctor",
    "LimitFunctor",
    "ProductFunctor",
]


class DiagonalFunctor(Functor):
    r"""The diagonal functor ``C -> C x C``."""

    def __init__(self, category) -> None:
        from dzack_research.preamble.categories.abstract_categories.category_constructions import (
            ProductCategory,
        )

        self._product_category = ProductCategory(category, category)
        super().__init__(category, self._product_category)

    def product_category(self):
        return self._product_category

    def _apply_object(self, obj):
        return self.product_category()(obj, obj)

    def _apply_morphism(self, morphism):
        return self.product_category().mor(
            self(morphism.domain()), self(morphism.codomain())
        )(morphism, morphism)


class ProductFunctor(Functor):
    r"""The binary categorical product functor ``C x C -> C`` where represented."""

    def __init__(self, category) -> None:
        from dzack_research.preamble.categories.abstract_categories.category_constructions import (
            ProductCategory,
        )

        self._product_category = ProductCategory(category, category)
        super().__init__(self._product_category, category)

    def _apply_object(self, pair):
        from dzack_research.preamble.categories.abstract_categories.constructions import Product

        return Product(pair.first(), pair.second())

    def _apply_morphism(self, pair_morphism):
        source = self(pair_morphism.domain())
        target = self(pair_morphism.codomain())
        from dzack_research.preamble.categories.abstract_categories.constructions import _ProductMorphism
        return _ProductMorphism(
            pair_morphism.first(), pair_morphism.second(), source=source, target=target
        )


class CoproductFunctor(Functor):
    r"""The binary categorical coproduct functor ``C x C -> C`` where represented."""

    def __init__(self, category) -> None:
        from dzack_research.preamble.categories.abstract_categories.category_constructions import (
            ProductCategory,
        )

        self._product_category = ProductCategory(category, category)
        super().__init__(self._product_category, category)

    def _apply_object(self, pair):
        from dzack_research.preamble.categories.abstract_categories.constructions import Coproduct

        return Coproduct(pair.first(), pair.second())

    def _apply_morphism(self, pair_morphism):
        source = self(pair_morphism.domain())
        target = self(pair_morphism.codomain())
        from dzack_research.preamble.categories.abstract_categories.constructions import _CoproductMorphism
        return _CoproductMorphism(
            pair_morphism.first(), pair_morphism.second(), source=source, target=target
        )


class CartesianProductFunctor(ProductFunctor):
    r"""The binary Cartesian-product functor on Set."""

    def __init__(self) -> None:
        super().__init__(Sets())


class DisjointUnionFunctor(CoproductFunctor):
    r"""The binary disjoint-union functor on Set."""

    def __init__(self) -> None:
        super().__init__(Sets())


class LimitFunctor(ProductFunctor):
    r"""The represented binary limit functor; binary products are its discrete case."""


class ColimitFunctor(CoproductFunctor):
    r"""The represented binary colimit functor; binary coproducts are its discrete case."""
