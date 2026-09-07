r"""The one-object category ``BG`` and the functor induced by a group map.

The represented group names the unique object. Its elements name the
arrows, and its multiplication is composition. Sage's ``Morphism`` and
the existing owned Hom construction supply the runtime representation;
the group owner supplies multiplication, inverses and equality.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.groups import OwnedGroups, _owned_group


class ClassifyingMorphism(Morphism):
    r"""An arrow of ``BG``, named by its group element."""

    def __init__(self, parent, group_element) -> None:
        self._group_element = parent.homset_category().group()(group_element)
        Morphism.__init__(self, parent)

    def group_element(self):
        return self._group_element

    def __mul__(self, other):
        if not isinstance(other, ClassifyingMorphism) or other.parent() is not self.parent():
            return NotImplemented
        return self.parent()(self.group_element() * other.group_element())

    def inverse(self):
        return self.parent()(~self.group_element())

    __invert__ = inverse

    def _richcmp_(self, other, op):
        if not isinstance(other, ClassifyingMorphism) or other.parent() is not self.parent():
            return NotImplemented
        return richcmp(self.group_element(), other.group_element(), op)

    def _repr_(self):
        return f"{self.group_element()} in B({self.parent().homset_category().group()})"


class ClassifyingHomset(CategoricalHomset):
    r"""The single Hom object of ``BG``."""

    Element = ClassifyingMorphism

    def _element_constructor_(self, datum):
        if isinstance(datum, ClassifyingMorphism):
            assert datum.parent() is self, "the arrow belongs to a different classifying category"
            return datum
        return self.element_class(self, datum)

    @cached_method
    def identity(self):
        return self(self.homset_category().group().one())


class ClassifyingHomCategory(HomCategoryConstruction):
    def fixed_category_class(self):
        return ClassifyingHomset


class ClassifyingCategory(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""The one-object category with endomorphism group ``G``."""

    @staticmethod
    def __classcall__(cls, group):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(group))

    def parameter_category(self):
        return OwnedGroups()

    def group(self):
        return self.parameter()

    def an_object(self):
        return self.group()

    def __contains__(self, candidate) -> bool:
        return candidate is self.an_object()

    def super_categories(self):
        return [Objects()]

    _HomCategory = ClassifyingHomCategory

    def _repr_object_names(self):
        return f"the unique object of B({self.group()})"


class ClassifyingFunctor(Functor):
    r"""``B(phi): BH -> BG`` for a group morphism ``phi: H -> G``."""

    def __init__(self, group_morphism) -> None:
        self._group_morphism = group_morphism
        super().__init__(
            group_morphism.domain().classifying_category(),
            group_morphism.codomain().classifying_category(),
        )

    def group_morphism(self):
        return self._group_morphism

    def _apply_object(self, obj):
        return self.codomain().an_object()

    def _apply_morphism(self, morphism):
        point = self.codomain().an_object()
        return self.codomain().Mor(point, point)(
            self.group_morphism()(morphism.group_element())
        )
