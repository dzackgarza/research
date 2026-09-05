r"""Diagrams, cones, cocones, and selected finite product constructions."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

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
from dzack_research.preamble.categories.functors.core import NaturalTransformation


class DiagramCategory(FunctorCategory):
    r"""The functor category ``[J,C]`` of diagrams of one shape."""

    def __init__(self, index_category, target_category) -> None:
        super().__init__(Cat(), index_category, target_category)

    def index_category(self):
        return self.domain_category()

    def target_category(self):
        return self.codomain_category()


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
        if left != right:
            return False
    return True


class ConeMorphism(Morphism):
    r"""A morphism of cones, determined by its apex map."""

    def __init__(self, parent, apex_map) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cone map has the wrong codomain apex")
        if not _commutes_with_diagram(self.domain(), self.codomain(), apex_map):
            raise ValueError("the apex map does not commute with the cone legs")
        self._apex_map = apex_map

    def apex_map(self):
        return self._apex_map

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().cone_category().Mor(other.domain(), self.codomain())(
            self.apex_map() * other.apex_map()
        )


class CoconeMorphism(Morphism):
    r"""A morphism of cocones, determined by its apex map."""

    def __init__(self, parent, apex_map) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cocone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cocone map has the wrong codomain apex")
        if not _commutes_with_diagram(
            self.domain(), self.codomain(), apex_map, cocone=True
        ):
            raise ValueError("the apex map does not commute with the cocone legs")
        self._apex_map = apex_map

    def apex_map(self):
        return self._apex_map

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().cocone_category().Mor(other.domain(), self.codomain())(
            self.apex_map() * other.apex_map()
        )


class ConeHomset(CategoricalHomset):
    Element = ConeMorphism

    def __init__(self, cone_category, domain, codomain) -> None:
        self._cone_category = cone_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(cone_category), domain, codomain
        )

    def cone_category(self):
        return self._cone_category

    def _element_constructor_(self, apex_map):
        return ConeMorphism(self, apex_map)


class CoconeHomset(CategoricalHomset):
    Element = CoconeMorphism

    def __init__(self, cocone_category, domain, codomain) -> None:
        self._cocone_category = cocone_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(cocone_category), domain, codomain
        )

    def cocone_category(self):
        return self._cocone_category

    def _element_constructor_(self, apex_map):
        return CoconeMorphism(self, apex_map)


class ConeCategory(OwnedCategory):
    r"""The category of cones over one represented diagram."""

    class ParentMethods:
        def __init__(self, apex, transformation, **rest) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cone_category(self):
            return self.category()

        def diagram(self):
            return self.cone_category().diagram()

        def apex(self):
            return self._apex

        def transformation(self):
            return self._transformation

        def structure_morphism(self, index):
            return self.transformation().component(index)

        def structure_morphisms(self):
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.structure_morphism(domain(label)),
                name=f"Structure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cone with apex {self.apex()} over {self.diagram()}"

    def __init__(self, diagram) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self):
        return self._diagram

    def target_category(self):
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate) -> bool:
        category = getattr(candidate, "category", lambda: None)()
        return (
            isinstance(category, ConeCategory)
            and category.diagram() is self.diagram()
        )

    def cone(self, apex, components):

        constant = ConstantDiagram(self.diagram().domain(), self.target_category(), apex)
        transformation = NaturalTransformation(constant, self.diagram(), components)
        return object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a cone Hom requires two cones over the same diagram")
        return ConeHomset(self, domain, codomain)



class CoconeCategory(OwnedCategory):
    r"""The category of cocones under one represented diagram."""

    class ParentMethods:
        def __init__(self, apex, transformation, **rest) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cocone_category(self):
            return self.category()

        def diagram(self):
            return self.cocone_category().diagram()

        def apex(self):
            return self._apex

        def transformation(self):
            return self._transformation

        def costructure_morphism(self, index):
            return self.transformation().component(index)

        def costructure_morphisms(self):
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.costructure_morphism(domain(label)),
                name=f"Costructure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cocone with apex {self.apex()} under {self.diagram()}"

    def __init__(self, diagram) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self):
        return self._diagram

    def target_category(self):
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate) -> bool:
        category = getattr(candidate, "category", lambda: None)()
        return (
            isinstance(category, CoconeCategory)
            and category.diagram() is self.diagram()
        )

    def cocone(self, apex, components):

        constant = ConstantDiagram(self.diagram().domain(), self.target_category(), apex)
        transformation = NaturalTransformation(self.diagram(), constant, components)
        return object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a cocone Hom requires two cocones under the same diagram")
        return CoconeHomset(self, domain, codomain)



class ProductConeCategory(ConeCategory):
    r"""Selected product cones over one finite discrete diagram."""


class CoproductCoconeCategory(CoconeCategory):
    r"""Selected coproduct cocones under one finite discrete diagram."""


class LimitsOfCategory(Category):
    def __init__(self, index_category, target_category) -> None:
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


def _finite_factor_family(factors, *, name="Selected factors"):
    if isinstance(factors, IndexedFamily):
        family = factors
    else:
        values = tuple(factors)
        labels = Sets.Δ[len(values) - 1]
        family = indexed_family(
            labels,
            lambda label: values[int(labels.rank(label))],
            name=name,
        )
    if not family.cardinality().is_finite():
        raise TypeError("the current product/coproduct construction requires finitely many factors")
    return family


class BiproductCategory(Category):
    r"""Objects equipped with the selected finite biproduct structure."""

    def __init__(self, factors) -> None:
        self._factors = _finite_factor_family(factors, name="Biproduct factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def factors(self):
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate) -> bool:
        try:
            return candidate.biproduct_factors() == self.factors()
        except (AttributeError, TypeError, ValueError):
            return False


DirectSumCategory = BiproductCategory


class TensorProductCategory(Category):
    r"""Objects equipped with a chosen tensor-product universal bilinear map."""

    def __init__(self, factors) -> None:
        self._factors = _finite_factor_family(factors, name="Tensor factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def tensor_factors(self):
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate) -> bool:
        try:
            return candidate.tensor_factors() == self.tensor_factors()
        except (AttributeError, TypeError, ValueError):
            return False


def common_category_of(objects):
    family = _finite_factor_family(objects)
    if family.cardinality() == cardinal(0):
        raise ValueError("a common category requires at least one object")
    return Category.meet([obj.category() for obj in family])


def Cone(diagram, apex, components):
    return ConeCategory(diagram).cone(apex, components)


def Cocone(diagram, apex, components):
    return CoconeCategory(diagram).cocone(apex, components)


def _discrete_diagram(factors, target_category=None):
    family = _finite_factor_family(factors)
    if family.cardinality() == cardinal(0):
        raise ValueError("the current selected finite product requires at least one factor")
    target = common_category_of(family) if target_category is None else target_category

    index = DiscreteCategory(family.index_set())
    return DiscreteDiagram(index, target, family)


def product_cone_category(factors, target_category=None):
    return ProductConeCategory(_discrete_diagram(factors, target_category))


def coproduct_cocone_category(factors, target_category=None):
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
    "TensorProductCategory",
    "common_category_of",
    "coproduct_cocone_category",
    "product_cone_category",
]
