r"""Basic categorical functors used by the abstract construction layer."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.element import parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.cat import Cat, CategoryObject
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
    _category_mor_parent,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.sets.cardinals import Cardinal, cardinal
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.owned_category import _object_of

SourcePointT = TypeVar("SourcePointT")
TargetPointT = TypeVar("TargetPointT")



class _DomainFunctor(Functor):
    r"""The domain functor ``Arr(C) -> C``."""

    def __init__(self, category: Category) -> None:
        super().__init__(category.ArrowCategory(), category)

    def _apply_object(self, arrow_object: Parent) -> ObjectOfCategory:
        return arrow_object.source_object()

    def _apply_morphism(self, square: Map) -> Map:
        return square.left()


class _CodomainFunctor(Functor):
    r"""The codomain functor ``Arr(C) -> C``."""

    def __init__(self, category: Category) -> None:
        super().__init__(category.ArrowCategory(), category)

    def _apply_object(self, arrow_object: Parent) -> ObjectOfCategory:
        return arrow_object.target_object()

    def _apply_morphism(self, square: Map) -> Map:
        return square.right()



class DiscreteMorphism(Morphism):
    r"""The unique identity arrow of a discrete-category object."""

    def __init__(self, parent: DiscreteMor) -> None:
        Morphism.__init__(self, parent)
        if self.domain() is not self.codomain():
            raise ValueError(
                f"a discrete category has no morphism between distinct objects, but {self.domain()} is not "
                f"{self.codomain()}"
            )

    def __mul__(self, other):
        # A discrete Mor on one object holds its identity only, so the
        # composable arrows are exactly the elements of this parent.
        if parent(other) is not self.parent():
            return NotImplemented
        return self.parent().identity()

    def __eq__(self, other) -> bool:
        return parent(other) is self.parent()

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))


class DiscreteMor(CategoricalMor):
    Element = DiscreteMorphism

    def __init__(
        self,
        family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(
            self, family, domain, codomain
        )

    def discrete_category(self) -> DiscreteCategory:
        return self.base_category()

    def cardinality(self) -> Cardinal:

        return cardinal(1 if self.domain() is self.codomain() else 0)

    def _element_constructor_(self, value=None):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"a discrete category has no morphism between distinct objects, but {self.domain()} is not "
                f"{self.codomain()}"
            )
        if value is not None:
            if parent(value) is not self:
                raise ValueError(
                    f"Mor({self.domain()}, {self.domain()}) in a discrete category contains only the identity, "
                    f"but got {value}"
                )
            return value
        return DiscreteMorphism(self)

    @cached_method
    def identity(self) -> DiscreteMorphism:
        return self()


class DiscreteMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = DiscreteMor


class DiscreteCategory(OwnedCategory):
    r"""The discrete category on one set.

    Unverified specimens retain unhashable labels and distinguish two equal
    underlying sets supplied as different objects::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: labels = finite_ordered_set(([0], [1]))
        sage: category = DiscreteCategory(labels)
        sage: category([0]) is category([0])
        True
        sage: category.objects().value([0]) is category([0])
        True
        sage: category.Mor(category([0]), category([1])).cardinality() == cardinal(0)
        True
        sage: identity = category.identity(category([0]))
        sage: identity * identity == identity
        True
        sage: other_labels = finite_ordered_set(([0], [1]))
        sage: DiscreteCategory(other_labels).object_set() is other_labels
        True
        sage: DiscreteCategory(other_labels) is not category
        True
    """

    _MorCategory = DiscreteMorCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, object_set: (cls, id(object_set)))
    def __classcall__(cls, object_set: Parent):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(object_set)
        return typecall(cls, object_set)

    def an_object(self) -> ObjectOfCategory:
        r"""The object at a point of the underlying set."""
        return self.object(self.object_set().an_element())

    class ParentMethods:
        r"""One object of the discrete category on a set."""

        def __init__(self, value: SourcePointT, **rest) -> None:
            self._value = value
            super().__init__(**rest)

        def discrete_category(self) -> DiscreteCategory:
            return self.category()

        def Mor(self, codomain):
            r"""Return the Mor in this discrete category to ``codomain``."""
            return self.discrete_category().Mor(self, codomain)

        def value(self):
            return self._value

        def _repr_(self) -> str:
            return repr(self.value())

    def __init__(self, object_set: Parent) -> None:
        if object_set not in Sets():
            raise TypeError(
                f"a discrete category is built on a set of objects, but {object_set} is not in the category of sets"
            )
        self._object_set = object_set
        self._objects = indexed_family(
            object_set, lambda value: _object_of(self, value=value),
            name=f"Objects of the discrete category on {object_set}",
        )
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._object_set)

    def object_set(self) -> Sets().ObjectType:
        return self._object_set

    def category(self) -> Category:
        r"""A discrete category is placed among the discrete categories when it is built."""
        return DiscreteCategories()

    def super_categories(self):
        return [Objects()]

    def object(self, value: SourcePointT) -> ObjectOfCategory:
        return self._objects(value)

    __call__ = object

    def objects(self) -> IndexedFamily:
        return self._objects

    @cached_method
    def arrows(self) -> IndexedFamily:
        r"""Return the object-indexed family of identity arrows."""
        return indexed_family(
            self.object_set(),
            lambda value: self.identity(self(value)),
            name=f"Arrows of {self}",
        )

    def Mor(self, domain: Parent, codomain: Parent) -> DiscreteMor:
        if domain not in self or codomain not in self:
            raise TypeError(
                f"a morphism in the discrete category {self} needs two of its objects, but got {domain} and {codomain}"
            )
        return self.MorCategory().Of(domain, codomain)

    def _common_object_of_finite_family(self, factors, *, construction: str):
        r"""Return the forced apex of a finite discrete (co)product, when it exists."""
        from dzack_research.preamble.categories.abstract_categories.products import (
            _finite_factor_family,
        )

        family = _finite_factor_family(factors, name=f"{construction.capitalize()} factors")
        if any(factor not in self for factor in family):
            raise TypeError(
                f"a {construction} in {self} needs every factor to be one of its objects, but the factors are {family}"
            )
        labels = tuple(family.index_set())
        if labels:
            apex = family.value(labels[0])
            for label in labels[1:]:
                factor = family.value(label)
                if factor is not apex:
                    raise ValueError(
                        f"the {construction} of {family} does not exist in {self}: a discrete category has a morphism "
                        f"between two objects only when they are the same object, but the factors include {apex} and {factor}"
                    )
            return family, apex

        if cardinal(self.object_set().cardinality()) != cardinal(1):
            extremum = "terminal" if construction == "product" else "initial"
            raise ValueError(
                f"the empty {construction} does not exist in {self}: it would be a {extremum} object, and a discrete "
                f"category has a {extremum} object exactly when it has one object"
            )
        return family, self.an_object()

    def product(self, factors):
        r"""Return the finite product when its universal cone exists."""
        return self._categorical_product_construction(factors).object()

    def coproduct(self, factors):
        r"""Return the finite coproduct when its universal cocone exists."""
        return self._categorical_coproduct_construction(factors).object()

    def _categorical_product(self, left, right):
        return self.product((left, right))

    def _categorical_coproduct(self, left, right):
        return self.coproduct((left, right))

    def _categorical_product_construction(self, factors):
        from dzack_research.preamble.categories.abstract_categories.products import (
            SelectedLimitConstruction,
            _discrete_diagram,
        )

        family, product = self._common_object_of_finite_family(
            factors,
            construction="product",
        )
        diagram = _discrete_diagram(family, self)
        universal_cone = diagram.ProductCones().cone(
            product,
            lambda index: self.Mor(product, diagram(index)).identity(),
        )

        def factorizer(cone):
            return self.Mor(cone.apex(), product).identity()

        return SelectedLimitConstruction(diagram, universal_cone, factorizer)

    def _categorical_coproduct_construction(self, factors):
        from dzack_research.preamble.categories.abstract_categories.products import (
            SelectedColimitConstruction,
            _discrete_diagram,
        )

        family, coproduct = self._common_object_of_finite_family(
            factors,
            construction="coproduct",
        )
        diagram = _discrete_diagram(family, self)
        universal_cocone = diagram.CoproductCocones().cocone(
            coproduct,
            lambda index: self.Mor(diagram(index), coproduct).identity(),
        )

        def factorizer(cocone):
            return self.Mor(coproduct, cocone.apex()).identity()

        return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

    def _require_parallel_discrete_pair(self, left_morphism, right_morphism) -> None:
        if (
            left_morphism.domain() is not right_morphism.domain()
            or left_morphism.codomain() is not right_morphism.codomain()
        ):
            raise ValueError(
                f"a parallel pair in {self} needs common endpoints, but {left_morphism} is "
                f"{left_morphism.domain()} -> {left_morphism.codomain()} and {right_morphism} is "
                f"{right_morphism.domain()} -> {right_morphism.codomain()}"
            )
        mor = self.Mor(left_morphism.domain(), left_morphism.codomain())
        if parent(left_morphism) is not mor or parent(right_morphism) is not mor:
            raise TypeError(
                f"an equalizer or coequalizer in {self} needs a parallel pair of its morphisms, but got "
                f"{left_morphism} and {right_morphism}"
            )

    def _categorical_equalizer(self, left_morphism, right_morphism):
        return self._categorical_equalizer_construction(
            left_morphism,
            right_morphism,
        ).object()

    def _categorical_equalizer_construction(self, left_morphism, right_morphism):
        from dzack_research.preamble.categories.abstract_categories.products import (
            SelectedLimitConstruction,
            _parallel_pair_diagram,
        )

        self._require_parallel_discrete_pair(left_morphism, right_morphism)
        equalizer = left_morphism.domain()
        diagram = _parallel_pair_diagram(left_morphism, right_morphism, self)
        universal_cone = diagram.Cones().cone(
            equalizer,
            lambda index: self.Mor(equalizer, diagram(index)).identity(),
        )

        def factorizer(cone):
            return self.Mor(cone.apex(), equalizer).identity()

        return SelectedLimitConstruction(diagram, universal_cone, factorizer)

    def _categorical_coequalizer(self, left_morphism, right_morphism):
        return self._categorical_coequalizer_construction(
            left_morphism,
            right_morphism,
        ).object()

    def _categorical_coequalizer_construction(self, left_morphism, right_morphism):
        from dzack_research.preamble.categories.abstract_categories.products import (
            SelectedColimitConstruction,
            _parallel_pair_diagram,
        )

        self._require_parallel_discrete_pair(left_morphism, right_morphism)
        coequalizer = left_morphism.codomain()
        diagram = _parallel_pair_diagram(left_morphism, right_morphism, self)
        universal_cocone = diagram.Cocones().cocone(
            coequalizer,
            lambda index: self.Mor(diagram(index), coequalizer).identity(),
        )

        def factorizer(cocone):
            return self.Mor(coequalizer, cocone.apex()).identity()

        return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

    def _nonempty_discrete_morphism_family_reference(self, morphisms):
        if morphisms.cardinality() == cardinal(0):
            raise ValueError(
                f"a wide equalizer or coequalizer in {self} needs a nonempty family of parallel morphisms"
            )
        reference = morphisms.value(morphisms.index_set().an_element())
        mor = self.Mor(reference.domain(), reference.codomain())
        if parent(reference) is not mor:
            raise TypeError(
                f"a wide equalizer or coequalizer in {self} needs a family of its morphisms, but the family contains {reference}"
            )
        return reference

    def _categorical_equalizer_family(self, morphisms):
        r"""Return the source of a nonempty parallel family, whose arrows are forced equal."""
        return self._nonempty_discrete_morphism_family_reference(morphisms).domain()

    def _categorical_coequalizer_family(self, morphisms):
        r"""Return the target of a nonempty parallel family, whose arrows are forced equal."""
        return self._nonempty_discrete_morphism_family_reference(morphisms).codomain()

    def _categorical_product_morphism(self, left_morphism, right_morphism, source, target):
        return self.Mor(source, target).identity()

    _categorical_coproduct_morphism = _categorical_product_morphism


    def identity(self, obj: Parent) -> DiscreteMorphism:
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Discrete category on {self.object_set()}"


class DiscreteCategories(OwnedCategory):
    r"""The category of represented discrete categories."""

    def an_object(self) -> Category:
        r"""The discrete category on a set."""
        return DiscreteCategory(Sets().an_object())

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [Cat()]


class _DiscreteFunctor(Functor):
    r"""A functor between discrete categories induced by a map of object sets."""

    def __init__(
        self,
        domain: DiscreteCategory,
        codomain: DiscreteCategory,
        object_map: Morphism | Callable[[SourcePointT], TargetPointT],
    ) -> None:
        match object_map:
            case Morphism() if (
                object_map.domain() is not domain.object_set()
                or object_map.codomain() is not codomain.object_set()
            ):
                raise ValueError(
                    f"a functor {domain} -> {codomain} of discrete categories needs a map of object sets "
                    f"{domain.object_set()} -> {codomain.object_set()}, but {object_map} is a map "
                    f"{object_map.domain()} -> {object_map.codomain()}"
                )
        # The set Mor between the object sets builds a map from a rule and
        # keeps a map it already represents.
        self._object_map = Sets().Mor(domain.object_set(), codomain.object_set())(object_map)
        super().__init__(domain, codomain)

    def object_map(self) -> Morphism:
        return self._object_map

    def _apply_object(self, obj: Parent) -> ObjectOfCategory:
        return self.codomain()(self.object_map()(obj.value()))

    def _apply_morphism(self, morphism: Map) -> Map:
        return self.codomain().identity(self(morphism.domain()))


class ObjectSetFunctor(Functor):
    r"""Take the object set of a represented discrete category."""

    def __init__(self) -> None:
        super().__init__(DiscreteCategories(), Sets())

    def _apply_object(self, category: Parent) -> Sets().ObjectType:
        match category:
            case CategoryObject():
                category = category.represented_category()
        return category.object_set()

    def _apply_morphism(self, functor: Map) -> Map:
        return functor.functor().object_map()


class _DiscreteDiagram(Functor):
    r"""A functor from a discrete category, specified on its objects."""

    def __init__(
        self,
        index_category: Category,
        codomain: Category,
        values: IndexedFamily,
    ) -> None:
        if index_category not in DiscreteCategories():
            raise TypeError(
                f"a discrete diagram needs a discrete index category, but {index_category} is not discrete"
            )
        self._values = values
        super().__init__(index_category, codomain)

    def diagram_objects(self) -> IndexedFamily:
        return self._values

    def _apply_object(self, index: Parent) -> ObjectOfCategory:
        return self._values(index.value())

    def _apply_morphism(self, morphism: Map) -> Map:
        image = self(morphism.domain())
        return _category_mor_parent(self.codomain(), image, image).identity()


class _ConstantDiagram(Functor):
    r"""The constant functor from an index category at one object."""

    def __init__(self, index_category: Category, codomain: Category, value: Parent) -> None:
        if value not in codomain:
            raise TypeError(
                f"the constant functor {index_category} -> {codomain} needs its value in {codomain}, but "
                f"{value} is not an object of it"
            )
        self._value = value
        super().__init__(index_category, codomain)

    def constant_value(self) -> ObjectOfCategory:
        return self._value

    def _apply_object(self, index: Parent) -> ObjectOfCategory:
        return self.constant_value()

    def _apply_morphism(self, morphism: Map) -> Map:
        value = self.constant_value()
        return _category_mor_parent(self.codomain(), value, value).identity()






__all__ = [
    "DiscreteCategories",
    "DiscreteCategory",
    "ObjectSetFunctor",
    "CartesianProductFunctor",
    "DisjointUnionFunctor",
]


class _DiagonalFunctor(Functor):
    r"""The diagonal functor ``C -> C x C``."""

    def __init__(self, category: Category) -> None:

        self._product_category = Cat().product((category, category))
        super().__init__(category, self._product_category)

    def product_category(self) -> Category:
        return self._product_category

    def _apply_object(self, obj: Parent) -> ObjectOfCategory:
        return self.product_category()(obj, obj)

    def _apply_morphism(self, morphism: Map) -> Map:
        return self.product_category().Mor(
            self(morphism.domain()), self(morphism.codomain())
        )(morphism, morphism)


class _ProductFunctor(Functor):
    r"""The binary categorical product functor ``C x C -> C`` where represented."""

    def __init__(self, category: Category) -> None:

        self._product_category = Cat().product((category, category))
        super().__init__(self._product_category, category)

    def _apply_object(self, pair: Parent) -> ObjectOfCategory:

        return self.codomain().product((pair.first(), pair.second()))

    def _apply_morphism(self, pair_morphism: Map) -> Map:
        source = self(pair_morphism.domain())
        target = self(pair_morphism.codomain())
        return self.codomain()._categorical_product_morphism(
            pair_morphism.first(), pair_morphism.second(), source=source, target=target
        )


class _CoproductFunctor(Functor):
    r"""The binary categorical coproduct functor ``C x C -> C`` where represented."""

    def __init__(self, category: Category) -> None:

        self._product_category = Cat().product((category, category))
        super().__init__(self._product_category, category)

    def _apply_object(self, pair: Parent) -> ObjectOfCategory:

        return self.codomain().coproduct((pair.first(), pair.second()))

    def _apply_morphism(self, pair_morphism: Map) -> Map:
        source = self(pair_morphism.domain())
        target = self(pair_morphism.codomain())
        return self.codomain()._categorical_coproduct_morphism(
            pair_morphism.first(), pair_morphism.second(), source=source, target=target
        )


class CartesianProductFunctor(_ProductFunctor):
    r"""The binary Cartesian-product functor on Set."""

    def __init__(self) -> None:
        super().__init__(Sets())


class DisjointUnionFunctor(_CoproductFunctor):
    r"""The binary disjoint-union functor on Set."""

    def __init__(self) -> None:
        super().__init__(Sets())


class _LimitFunctor(Functor):
    r"""The selected limit functor ``[J,C] -> C`` for one represented shape."""

    def __init__(self, codomain: Category, index_category: Category) -> None:
        self._index_category = index_category
        self._limits = codomain.Limits(index_category)
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        super().__init__(Cat().Mor(index_category, codomain), codomain)

    def index_category(self) -> Category:
        return self._index_category

    @staticmethod
    def _diagram(diagram_object):
        return diagram_object.functor()

    def _apply_object(self, diagram_object: Parent) -> ObjectOfCategory:
        return self._limits.construction(self._diagram(diagram_object)).object()

    def _apply_morphism(self, transformation_morphism: Map) -> Map:
        transformation = transformation_morphism.transformation()
        source = self._limits.construction(transformation.source())
        target = self._limits.construction(transformation.target())
        return source.induced_map(transformation, target)


class _ColimitFunctor(Functor):
    r"""The selected colimit functor ``[J,C] -> C`` for one represented shape."""

    def __init__(self, codomain: Category, index_category: Category) -> None:
        self._index_category = index_category
        self._colimits = codomain.Colimits(index_category)
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        super().__init__(Cat().Mor(index_category, codomain), codomain)

    def index_category(self) -> Category:
        return self._index_category

    @staticmethod
    def _diagram(diagram_object):
        return diagram_object.functor()

    def _apply_object(self, diagram_object: Parent) -> ObjectOfCategory:
        return self._colimits.construction(self._diagram(diagram_object)).object()

    def _apply_morphism(self, transformation_morphism: Map) -> Map:
        transformation = transformation_morphism.transformation()
        source = self._colimits.construction(transformation.source())
        target = self._colimits.construction(transformation.target())
        return source.induced_map(transformation, target)


@cached_function
def _domain_functor(category: Category) -> _DomainFunctor:
    return _DomainFunctor(category)


@cached_function
def _codomain_functor(category: Category) -> _CodomainFunctor:
    return _CodomainFunctor(category)


@cached_function
def _diagonal_functor(category: Category) -> _DiagonalFunctor:
    return _DiagonalFunctor(category)


@cached_function
def _product_functor(category: Category) -> _ProductFunctor:
    return _ProductFunctor(category)


@cached_function
def _coproduct_functor(category: Category) -> _CoproductFunctor:
    return _CoproductFunctor(category)


@cached_function
def _limit_functor(codomain: Category, index_category: Category) -> _LimitFunctor:
    return _LimitFunctor(codomain, index_category)


@cached_function
def _colimit_functor(codomain: Category, index_category: Category) -> _ColimitFunctor:
    return _ColimitFunctor(codomain, index_category)
