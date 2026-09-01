r"""Diagrams, cones, cocones, and selected finite product constructions."""

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.cat import Cat, FunctorCategory
from dzack_research.preamble.categories.sets import finite_ordered_set


class DiagramCategory(FunctorCategory):
    r"""The functor category ``[J,C]`` of diagrams of one shape."""

    def __init__(self, index_category, ambient_category) -> None:
        super().__init__(Cat(), index_category, ambient_category)

    def index_category(self):
        return self.domain_category()

    def ambient_category(self):
        return self.codomain_category()


class DirectedSystem(DiagramCategory):
    r"""A diagram category whose index category represents a directed order."""


class InverseSystem(DiagramCategory):
    r"""A diagram category read contravariantly as an inverse system."""


class ConeObject(Parent):
    r"""A cone ``Delta(A) => D`` over a diagram ``D:J->C``."""

    def __init__(self, cone_category, apex, transformation) -> None:
        self._cone_category = cone_category
        self._apex = apex
        self._transformation = transformation
        Parent.__init__(self, category=SageSets())

    def cone_category(self):
        return self._cone_category

    def diagram(self):
        return self.cone_category().diagram()

    def apex(self):
        return self._apex

    def transformation(self):
        return self._transformation

    def structure_morphism(self, index):
        return self.transformation().component(index)

    def structure_morphisms(self):
        return tuple(
            self.structure_morphism(index) for index in self.diagram().domain().objects()
        )

    def _repr_(self) -> str:
        return f"Cone with apex {self.apex()} over {self.diagram()}"


class CoconeObject(Parent):
    r"""A cocone ``D => Delta(A)`` under a diagram ``D:J->C``."""

    def __init__(self, cocone_category, apex, transformation) -> None:
        self._cocone_category = cocone_category
        self._apex = apex
        self._transformation = transformation
        Parent.__init__(self, category=SageSets())

    def cocone_category(self):
        return self._cocone_category

    def diagram(self):
        return self.cocone_category().diagram()

    def apex(self):
        return self._apex

    def transformation(self):
        return self._transformation

    def costructure_morphism(self, index):
        return self.transformation().component(index)

    def costructure_morphisms(self):
        return tuple(
            self.costructure_morphism(index) for index in self.diagram().domain().objects()
        )

    def _repr_(self) -> str:
        return f"Cocone with apex {self.apex()} under {self.diagram()}"


def _morphisms_agree_on_diagram(source, target, apex_map, cocone=False) -> bool:
    for index in source.diagram().domain().objects():
        if cocone:
            left = apex_map * source.costructure_morphism(index)
            right = target.costructure_morphism(index)
        else:
            left = target.structure_morphism(index) * apex_map
            right = source.structure_morphism(index)
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _morphisms_agree,
        )

        if not _morphisms_agree(left, right):
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
        if not _morphisms_agree_on_diagram(self.domain(), self.codomain(), apex_map):
            raise ValueError("the apex map does not commute with the cone legs")
        self._apex_map = apex_map

    def apex_map(self):
        return self._apex_map

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().cone_category().hom(other.domain(), self.codomain())(
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
        if not _morphisms_agree_on_diagram(
            self.domain(), self.codomain(), apex_map, cocone=True
        ):
            raise ValueError("the apex map does not commute with the cocone legs")
        self._apex_map = apex_map

    def apex_map(self):
        return self._apex_map

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().cocone_category().hom(other.domain(), self.codomain())(
            self.apex_map() * other.apex_map()
        )


class ConeHomset(Homset):
    Element = ConeMorphism

    def __init__(self, cone_category, domain, codomain) -> None:
        self._cone_category = cone_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def cone_category(self):
        return self._cone_category

    def _element_constructor_(self, apex_map):
        return ConeMorphism(self, apex_map)


class CoconeHomset(Homset):
    Element = CoconeMorphism

    def __init__(self, cocone_category, domain, codomain) -> None:
        self._cocone_category = cocone_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def cocone_category(self):
        return self._cocone_category

    def _element_constructor_(self, apex_map):
        return CoconeMorphism(self, apex_map)


class ConeCategory(Category):
    r"""The category of cones over one represented diagram."""

    def __init__(self, diagram) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self):
        return self._diagram

    def ambient_category(self):
        return self.diagram().codomain()

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, ConeObject) and candidate.diagram() is self.diagram()

    def cone(self, apex, components):
        from dzack_research.preamble.categories.abstract_categories.functors import ConstantDiagram
        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        constant = ConstantDiagram(self.diagram().domain(), self.ambient_category(), apex)
        transformation = NaturalTransformation(constant, self.diagram(), components)
        return ConeObject(self, apex, transformation)

    def hom(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a cone Hom requires two cones over the same diagram")
        return ConeHomset(self, domain, codomain)

    Hom = hom


class CoconeCategory(Category):
    r"""The category of cocones under one represented diagram."""

    def __init__(self, diagram) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self):
        return self._diagram

    def ambient_category(self):
        return self.diagram().codomain()

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, CoconeObject) and candidate.diagram() is self.diagram()

    def cocone(self, apex, components):
        from dzack_research.preamble.categories.abstract_categories.functors import ConstantDiagram
        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        constant = ConstantDiagram(self.diagram().domain(), self.ambient_category(), apex)
        transformation = NaturalTransformation(self.diagram(), constant, components)
        return CoconeObject(self, apex, transformation)

    def hom(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a cocone Hom requires two cocones under the same diagram")
        return CoconeHomset(self, domain, codomain)

    Hom = hom


class ProductConeCategory(ConeCategory):
    r"""Selected product cones over one finite discrete diagram."""


class CoproductCoconeCategory(CoconeCategory):
    r"""Selected coproduct cocones under one finite discrete diagram."""


class LimitsOfCategory(Category):
    def __init__(self, index_category, ambient_category) -> None:
        self._index_category = index_category
        self._ambient_category = ambient_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._index_category, self._ambient_category

    def super_categories(self):
        return [Objects()]


class ColimitsOfCategory(LimitsOfCategory):
    pass


class ProductsOfCategory(LimitsOfCategory):
    pass


class CoproductsOfCategory(ColimitsOfCategory):
    pass


class BiproductCategory(Category):
    r"""Objects equipped with the selected finite biproduct structure."""

    def __init__(self, factors) -> None:
        self._factors = tuple(factors)
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def factors(self):
        return self._factors

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        try:
            return tuple(candidate.biproduct_factors()) == self.factors()
        except AttributeError:
            return False


DirectSumCategory = BiproductCategory


class TensorProductCategory(Category):
    r"""Objects equipped with a chosen tensor-product universal bilinear map."""

    def __init__(self, factors) -> None:
        self._factors = tuple(factors)
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def tensor_factors(self):
        return self._factors

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        try:
            return tuple(candidate.tensor_factors()) == self.tensor_factors()
        except AttributeError:
            return False


def ambient_category_of(objects):
    objects = tuple(objects)
    if not objects:
        raise ValueError("a common category requires at least one object")
    return Category.meet([obj.category() for obj in objects])


def Cone(diagram, apex, components):
    return ConeCategory(diagram).cone(apex, components)


def Cocone(diagram, apex, components):
    return CoconeCategory(diagram).cocone(apex, components)


def _discrete_diagram(factors, ambient_category=None):
    factors = tuple(factors)
    if not factors:
        raise ValueError("the current selected finite product requires at least one factor")
    ambient = ambient_category_of(factors) if ambient_category is None else ambient_category
    from dzack_research.preamble.categories.abstract_categories.functors import (
        DiscreteCategory,
        DiscreteDiagram,
    )

    labels = finite_ordered_set(range(len(factors)))
    index = DiscreteCategory(labels)
    return DiscreteDiagram(index, ambient, lambda position: factors[int(position)])


def product_cone_category(factors, ambient_category=None):
    return ProductConeCategory(_discrete_diagram(factors, ambient_category))


def coproduct_cocone_category(factors, ambient_category=None):
    return CoproductCoconeCategory(_discrete_diagram(factors, ambient_category))


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
    "ambient_category_of",
    "coproduct_cocone_category",
    "product_cone_category",
]
