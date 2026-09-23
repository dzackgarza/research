r"""The one-object category ``BG`` and the functor induced by a group map.

The category constructs one formal object. The represented group's elements
name its endomorphisms, and group multiplication is composition. Sage's ``Morphism`` and
the existing owned Mor construction supply the runtime representation;
the group owner supplies multiplication, inverses and equality.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoryPacketMethods,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.groups import OwnedGroups, _owned_group
from dzack_research.preamble.owned_category import _object_of


class ClassifyingMorphism(Morphism):
    r"""An arrow of ``BG``, named by its group element."""

    def __init__(self, parent, group_element) -> None:
        self._group_element = parent.mor_category().group()(group_element)
        Morphism.__init__(self, parent)

    def group_element(self):
        return self._group_element

    def _composition(self, right):
        r"""Composition in ``BG`` is the group law; Sage's ``Map.__mul__`` has checked ``right`` is a map into the one object."""
        if right.parent() is not self.parent():
            return NotImplemented
        return self.parent()(self.group_element() * right.group_element())

    def inverse(self):
        return self.parent()(~self.group_element())

    __invert__ = inverse

    def _richcmp_(self, other, op):
        r"""Compare two arrows of ``BG`` by their group elements; Sage calls this with one parent."""
        return richcmp(self.group_element(), other.group_element(), op)

    def _repr_(self):
        return f"{self.group_element()} in B({self.parent().mor_category().group()})"


class ClassifyingMor(CategoricalMor):
    r"""The single Mor object of ``BG``."""

    Element = ClassifyingMorphism

    def _element_constructor_(self, datum):
        if isinstance(datum, ClassifyingMorphism):
            assert datum.parent() is self, "the arrow belongs to a different classifying category"
            return datum
        return self.element_class(self, datum)

    @cached_method
    def identity(self):
        return self(self.mor_category().group().one())


class ClassifyingMorCategory(MorCategoryConstruction):
    def fixed_category_class(self):
        return ClassifyingMor


class ClassifyingCategory(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""The one-object category with endomorphism group ``G``."""

    @staticmethod
    def __classcall__(cls, group):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(group))

    def parameter_category(self):
        return OwnedGroups()

    def group(self):
        return self.parameter()

    class ParentMethods:
        r"""The unique formal object of ``BG``; ``G`` lives in its endomorphisms."""

        def classifying_category(self):
            return self.category()

        def _repr_(self):
            return f"* in B({self.classifying_category().group()})"

    @cached_method
    def object(self):
        return _object_of(self)

    def an_object(self):
        return self.object()

    def super_categories(self):
        return [Objects()]

    _MorCategory = ClassifyingMorCategory

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
