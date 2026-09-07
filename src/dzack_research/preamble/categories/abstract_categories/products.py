r"""Diagrams, cones, cocones, and selected finite product constructions."""

from collections.abc import Callable, Iterable
from typing import Any

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _category_homset,
)
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.unknown import Unknown, UnknownClass
from sage.misc.cachefunc import cached_function
from sage.misc.classcall_metaclass import typecall
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent
from sage.structure.dynamic_class import DynamicMetaclass

from dzack_research.preamble.categories.abstract_categories.cat import Cat, FunctorCategory
from dzack_research.preamble.categories.abstract_categories.objects import Objects as OwnedObjects
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.abstract_categories.functors import (
    ConstantDiagram,
    DiscreteCategory,
    DiscreteDiagram,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.functors.core import Functor, NaturalTransformation


class DiagramCategory(FunctorCategory):
    r"""The functor category ``[J,C]`` of diagrams of one shape."""

    @staticmethod
    @cached_function(key=lambda cls, index_category, target_category: (cls, id(index_category), id(target_category)))
    def __classcall__(cls, index_category: Category, target_category: Category):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(index_category, target_category)
        return typecall(cls, index_category, target_category)

    def __init__(self, index_category: Category, target_category: Category) -> None:
        super().__init__(Cat(), index_category, target_category)

    def index_category(self) -> Category:
        return self.domain_category()

    def target_category(self) -> Category:
        return self.codomain_category()

    def super_categories(self):
        return [Cat().Mor(self.index_category(), self.target_category())]


class DirectedSystem(DiagramCategory):
    r"""A diagram category whose index category represents a directed order."""


class InverseSystem(DiagramCategory):
    r"""A diagram category read contravariantly as an inverse system."""




def _commutes_with_diagram(source, target, apex_map, cocone=False) -> bool:
    for index in source.diagram().domain().objects():
        if cocone:
            left = apex_map * source.costructure_morphism(index)
            right = target.costructure_morphism(index)
        else:
            left = target.structure_morphism(index) * apex_map
            right = source.structure_morphism(index)
        if (left == right) is not True:
            return False
    return True


class ConeMorphism(Morphism):
    r"""A morphism of cones, determined by its apex map."""

    def __init__(self, parent: "ConeHomset", apex_map: Morphism, *, verify: bool = True) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cone map has the wrong codomain apex")
        if apex_map not in _category_homset(
            parent.cone_category().target_category(), self.domain().apex(), self.codomain().apex()
        ):
            raise ValueError("the apex map is not a morphism of the diagram's target category")
        if verify and not _commutes_with_diagram(self.domain(), self.codomain(), apex_map):
            raise ValueError("the apex map does not commute with the cone legs")
        self._apex_map = apex_map

    def apex_map(self) -> Morphism:
        return self._apex_map

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if not isinstance(other, ConeMorphism) or other.parent() is not self.parent():
            return False
        return self.apex_map() == other.apex_map()

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not isinstance(other, ConeMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        # Each leg satisfies r_i g = q_i and q_i f = p_i, hence r_i(gf)=p_i.
        parent = self.parent().cone_category().Mor(other.domain(), self.codomain())
        return ConeMorphism(
            parent, self.apex_map() * other.apex_map(), verify=False
        )


class CoconeMorphism(Morphism):
    r"""A morphism of cocones, determined by its apex map."""

    def __init__(self, parent: "CoconeHomset", apex_map: Morphism, *, verify: bool = True) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cocone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cocone map has the wrong codomain apex")
        if apex_map not in _category_homset(
            parent.cocone_category().target_category(), self.domain().apex(), self.codomain().apex()
        ):
            raise ValueError("the apex map is not a morphism of the diagram's target category")
        if verify and not _commutes_with_diagram(
            self.domain(), self.codomain(), apex_map, cocone=True
        ):
            raise ValueError("the apex map does not commute with the cocone legs")
        self._apex_map = apex_map

    def apex_map(self) -> Morphism:
        return self._apex_map

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if not isinstance(other, CoconeMorphism) or other.parent() is not self.parent():
            return False
        return self.apex_map() == other.apex_map()

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not isinstance(other, CoconeMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        # Dually, g q_i = r_i and f p_i = q_i imply (gf)p_i = r_i.
        parent = self.parent().cocone_category().Mor(other.domain(), self.codomain())
        return CoconeMorphism(
            parent, self.apex_map() * other.apex_map(), verify=False
        )


class ConeHomset(CategoricalHomset):
    Element = ConeMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def cone_category(self) -> "ConeCategory":
        return self.base_category()

    def _element_constructor_(self, apex_map):
        if isinstance(apex_map, ConeMorphism):
            if apex_map.parent() is self:
                return apex_map
            if apex_map.domain() is not self.domain() or apex_map.codomain() is not self.codomain():
                raise ValueError("the cone morphism has the wrong endpoints")
            apex_map = apex_map.apex_map()
        return ConeMorphism(self, apex_map)

    def identity(self) -> ConeMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one cone")
        apex = self.domain().apex()
        return ConeMorphism(
            self,
            _category_homset(self.cone_category().target_category(), apex, apex).identity(),
            verify=False,
        )


class CoconeHomset(CategoricalHomset):
    Element = CoconeMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def cocone_category(self) -> "CoconeCategory":
        return self.base_category()

    def _element_constructor_(self, apex_map):
        if isinstance(apex_map, CoconeMorphism):
            if apex_map.parent() is self:
                return apex_map
            if apex_map.domain() is not self.domain() or apex_map.codomain() is not self.codomain():
                raise ValueError("the cocone morphism has the wrong endpoints")
            apex_map = apex_map.apex_map()
        return CoconeMorphism(self, apex_map)

    def identity(self) -> CoconeMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one cocone")
        apex = self.domain().apex()
        return CoconeMorphism(
            self,
            _category_homset(self.cocone_category().target_category(), apex, apex).identity(),
            verify=False,
        )


class ConeHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = ConeHomset


class CoconeHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = CoconeHomset


class ConeCategory(OwnedCategory):
    r"""The category of cones over one represented diagram.

    Unverified specimens test nonidentity maps of cones and cocones, including
    the identity on an object with nontrivial legs::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: labels = finite_ordered_set(("j",))
        sage: index = DiscreteCategory(labels)
        sage: points = finite_ordered_set(("a", "b"))
        sage: one = finite_ordered_set(("*",))
        sage: diagram = ConstantDiagram(index, Sets(), one)
        sage: category = ConeCategory(diagram)
        sage: leg = Sets().Mor(points, one)(lambda point: "*")
        sage: cone = category.cone(points, lambda obj: leg)
        sage: hom = category.Mor(cone, cone)
        sage: hom is category.HomCategory().Of(cone, cone)
        True
        sage: swap = Sets().Mor(points, points)(lambda point: "b" if point == "a" else "a")
        sage: hom(swap) * hom(swap) == hom.identity()
        True
        sage: cocones = CoconeCategory(diagram)
        sage: leg = Sets().Mor(one, points)(lambda point: "a")
        sage: cocone = cocones.cocone(points, lambda obj: leg)
        sage: hom = cocones.Mor(cocone, cocone)
        sage: hom is cocones.HomCategory().Of(cocone, cocone)
        True
        sage: collapse = hom(Sets().Mor(points, points)(lambda point: "a"))
        sage: hom.identity() * collapse == collapse
        True
        sage: collapse * collapse == collapse
        True
    """

    _HomCategory = ConeHomCategoryConstruction

    class ParentMethods:
        def __init__(
            self,
            apex: Parent,
            transformation: NaturalTransformation,
            **rest,
        ) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cone_category(self) -> "ConeCategory":
            return self.category()

        def diagram(self) -> Functor:
            return self.cone_category().diagram()

        def apex(self) -> Parent:
            return self._apex

        def transformation(self) -> NaturalTransformation:
            return self._transformation

        def structure_morphism(self, index: Parent) -> Morphism:
            return self.transformation().component(index)

        def structure_morphisms(self) -> IndexedFamily:
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.structure_morphism(domain(label)),
                name=f"Structure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cone with apex {self.apex()} over {self.diagram()}"

    def __init__(self, diagram: Functor) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self) -> Functor:
        return self._diagram

    def target_category(self) -> Category:
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        category = getattr(candidate, "category", lambda: None)()
        return (
            isinstance(category, ConeCategory)
            and category.diagram() is self.diagram()
        )

    def cone(
        self,
        apex: Parent,
        components: Callable[[Parent], Morphism],
    ) -> Parent:

        constant = ConstantDiagram(self.diagram().domain(), self.target_category(), apex)
        transformation = NaturalTransformation(constant, self.diagram(), components)
        return object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain: Parent, codomain: Parent) -> ConeHomset:
        if domain not in self or codomain not in self:
            raise TypeError("a cone Hom requires two cones over the same diagram")
        return self.HomCategory().Of(domain, codomain)



class CoconeCategory(OwnedCategory):
    r"""The category of cocones under one represented diagram."""

    _HomCategory = CoconeHomCategoryConstruction

    class ParentMethods:
        def __init__(
            self,
            apex: Parent,
            transformation: NaturalTransformation,
            **rest,
        ) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cocone_category(self) -> "CoconeCategory":
            return self.category()

        def diagram(self) -> Functor:
            return self.cocone_category().diagram()

        def apex(self) -> Parent:
            return self._apex

        def transformation(self) -> NaturalTransformation:
            return self._transformation

        def costructure_morphism(self, index: Parent) -> Morphism:
            return self.transformation().component(index)

        def costructure_morphisms(self) -> IndexedFamily:
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.costructure_morphism(domain(label)),
                name=f"Costructure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cocone with apex {self.apex()} under {self.diagram()}"

    def __init__(self, diagram: Functor) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self) -> Functor:
        return self._diagram

    def target_category(self) -> Category:
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        category = getattr(candidate, "category", lambda: None)()
        return (
            isinstance(category, CoconeCategory)
            and category.diagram() is self.diagram()
        )

    def cocone(
        self,
        apex: Parent,
        components: Callable[[Parent], Morphism],
    ) -> Parent:

        constant = ConstantDiagram(self.diagram().domain(), self.target_category(), apex)
        transformation = NaturalTransformation(self.diagram(), constant, components)
        return object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain: Parent, codomain: Parent) -> CoconeHomset:
        if domain not in self or codomain not in self:
            raise TypeError("a cocone Hom requires two cocones under the same diagram")
        return self.HomCategory().Of(domain, codomain)



class SpanCategory(ConeCategory):
    r"""Spans in one category, over the shape ``. <- . -> .``.

    That shape needs no new vocabulary.  A span :math:`A\leftarrow C\to B` is
    an apex with one arrow to each of two objects, which is exactly a cone
    over the discrete diagram on those two, so ``ConeCategory`` already owns
    it and this is that category read as spans.

    A span is an object here rather than a pair of arguments, so it has an
    apex, two legs, a diagram, and its own colimit.  The colimit is computed
    in the category the span lives in, which is where a pushout belongs and
    which is what lets a category with a construction of its own supply it.
    """

    def super_categories(self):
        return [ConeCategory(self.diagram())]

    class ParentMethods:
        def target_category(self) -> Category:
            r"""The category the span lives in."""
            return self.cone_category().target_category()

        def left_leg(self) -> Morphism:
            return self.structure_morphism(self.diagram().domain()(0))

        def right_leg(self) -> Morphism:
            return self.structure_morphism(self.diagram().domain()(1))

        def pushout(self) -> Parent:
            r"""Return the pushout of this span, the colimit of its diagram."""
            return self.target_category().pushout(self.left_leg(), self.right_leg())

        def _repr_(self) -> str:
            return f"Span {self.left_leg().codomain()} <- {self.apex()} -> {self.right_leg().codomain()}"


def Span(left_leg: Morphism, right_leg: Morphism) -> Parent:
    r"""Return the span the two legs form, as an object.

    The legs share a domain, which is the apex; their codomains are the two
    feet.
    """
    assert left_leg.domain() is right_leg.domain(), "a span has one common domain"
    legs = (left_leg, right_leg)
    diagram = _discrete_diagram((left_leg.codomain(), right_leg.codomain()))
    return SpanCategory(diagram).cone(
        left_leg.domain(),
        lambda index: legs[int(index.value())],
    )


class ProductConeCategory(ConeCategory):
    r"""Selected product cones over one finite discrete diagram."""

    def super_categories(self):
        return [ConeCategory(self.diagram())]


class CoproductCoconeCategory(CoconeCategory):
    r"""Selected coproduct cocones under one finite discrete diagram."""

    def super_categories(self):
        return [CoconeCategory(self.diagram())]


class LimitsOfCategory(Category):
    def __init__(self, index_category: Category, target_category: Category) -> None:
        self._index_category = index_category
        self._target_category = target_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._index_category, self._target_category

    def super_categories(self):
        return [OwnedObjects()]


class ColimitsOfCategory(LimitsOfCategory):
    pass


class ProductsOfCategory(LimitsOfCategory):
    pass


class CoproductsOfCategory(ColimitsOfCategory):
    pass


def _factor_family(factors, *, name="Selected factors"):
    r"""Return the indexed family a construction is taken over.

    A construction is taken over an index set, so its datum is the family and
    never an arity.  A bare sequence is syntactic ingress: it denotes the
    family on the canonical labels ``Sets.Δ[n-1]``, and this is the one
    boundary at which that normalization happens.
    """
    if isinstance(factors, IndexedFamily):
        return factors
    values = tuple(factors)
    labels = Sets.Δ[len(values) - 1]
    return indexed_family(
        labels,
        lambda label: values[int(labels.ranking_map()(label))],
        name=name,
    )


def _finite_factor_family(factors, *, name="Selected factors"):
    r"""Return the family, where the construction is represented over finite index sets."""
    family = _factor_family(factors, name=name)
    if not family.cardinality().is_finite():
        raise TypeError("the current product/coproduct construction requires finitely many factors")
    return family


def _two_factors_of(factors, *, name="Selected factors"):
    r"""Return the two factors, where the construction is represented binary.

    A backend that takes exactly two objects cannot answer over a larger
    index set.  Folding it would return an object satisfying the same
    universal property, but a different one: its projections and injections
    are composites through a nest, so there is no arrow to or from the factor
    at a given index.  A site with such a backend names that hypothesis here
    rather than folding.
    """
    family = _factor_family(factors, name=name)
    assert family.cardinality() == cardinal(2), (
        f"{name.lower()} over an index set other than a two-element one is "
        "defined, but the represented construction takes exactly two factors"
    )
    labels = tuple(family.index_set())
    return family[labels[0]], family[labels[1]]


class BiproductCategory(Category):
    r"""Objects equipped with the selected finite biproduct structure."""

    def __init__(self, factors: IndexedFamily | Iterable[Parent]) -> None:
        self._factors = _finite_factor_family(factors, name="Biproduct factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def factors(self) -> IndexedFamily:
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        try:
            return candidate.biproduct_factors() == self.factors()
        except (AttributeError, TypeError, ValueError):
            return False


DirectSumCategory = BiproductCategory


class TensorProductCategory(Category):
    r"""Objects equipped with a chosen tensor-product universal bilinear map."""

    def __init__(self, factors: IndexedFamily | Iterable[Parent]) -> None:
        self._factors = _finite_factor_family(factors, name="Tensor factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def tensor_factors(self) -> IndexedFamily:
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        try:
            return candidate.tensor_factors() == self.tensor_factors()
        except (AttributeError, TypeError, ValueError):
            return False


def common_category_of(objects: IndexedFamily | Iterable[Parent]) -> Category:
    family = _finite_factor_family(objects)
    if family.cardinality() == cardinal(0):
        raise ValueError("a common category requires at least one object")
    return Category.meet([obj.category() for obj in family])


def Cone(
    diagram: Functor,
    apex: Parent,
    components: Callable[[Parent], Morphism],
) -> Parent:
    return ConeCategory(diagram).cone(apex, components)


def Cocone(
    diagram: Functor,
    apex: Parent,
    components: Callable[[Parent], Morphism],
) -> Parent:
    return CoconeCategory(diagram).cocone(apex, components)


def _discrete_diagram(factors, target_category=None):
    family = _finite_factor_family(factors)
    if family.cardinality() == cardinal(0):
        raise ValueError("the current selected finite product requires at least one factor")
    target = common_category_of(family) if target_category is None else target_category

    index = DiscreteCategory(family.index_set())
    return DiscreteDiagram(index, target, family)


def product_cone_category(
    factors: IndexedFamily | Iterable[Parent],
    target_category: Category | None = None,
) -> ProductConeCategory:
    return ProductConeCategory(_discrete_diagram(factors, target_category))


def coproduct_cocone_category(
    factors: IndexedFamily | Iterable[Parent],
    target_category: Category | None = None,
) -> CoproductCoconeCategory:
    return CoproductCoconeCategory(_discrete_diagram(factors, target_category))


__all__ = [
    "BiproductCategory",
    "Cocone",
    "CoconeCategory",
    "CoconeMorphism",
    "ColimitsOfCategory",
    "Cone",
    "ConeCategory",
    "ConeMorphism",
    "CoproductCoconeCategory",
    "CoproductsOfCategory",
    "DiagramCategory",
    "DirectSumCategory",
    "DirectedSystem",
    "InverseSystem",
    "LimitsOfCategory",
    "ProductConeCategory",
    "ProductsOfCategory",
    "Span",
    "SpanCategory",
    "TensorProductCategory",
    "common_category_of",
    "coproduct_cocone_category",
    "product_cone_category",
]
