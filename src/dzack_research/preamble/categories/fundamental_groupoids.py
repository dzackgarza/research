r"""Fundamental groupoids of owned topological spaces."""

from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces


class FundamentalPathMor(CategoricalMor):
    r"""Endpoint-preserving path-homotopy classes between selected points."""

    class ElementMethods:
        def __init__(self, parent, path_class):
            Morphism.__init__(self, parent)
            self._path_class = path_class

        def path_class(self):
            return self._path_class

        def inverse(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, path_class):
        pass

    @object_level
    def identity(self):
        pass


class FundamentalPathMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = FundamentalPathMor


class FundamentalGroupoid(OwnedParameterizedCategory):
    r"""The groupoid of points and path-homotopy classes of one space."""

    _MorCategory = FundamentalPathMorCategoryConstruction

    def parameter_category(self):
        return TopologicalSpaces()

    def category(self):
        return FundamentalGroupoids()

    def super_categories(self):
        return [Objects()]

    def space(self):
        return self.parameter()

    def an_object(self):
        pass

    def point(self, value):
        r"""The object at a point of the selected topological space."""
        pass

    class ParentMethods:
        def __init__(self, point, **rest):
            self._point = point
            super().__init__(**rest)

        def point(self):
            return self._point


class FundamentalGroupoids(OwnedCategory):
    r"""Fundamental groupoids with functors as their arrows."""

    def super_categories(self):
        return [Cat()]

    def an_object(self):
        pass


class _FundamentalGroupoidFunctor(Functor):
    r"""Send spaces and continuous maps to their fundamental groupoids."""

    def __init__(self):
        super().__init__(TopologicalSpaces(), FundamentalGroupoids())

    def _apply_object(self, space):
        return space.fundamental_groupoid()

    def _apply_morphism(self, continuous_map):
        pass
