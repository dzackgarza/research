r"""Euclidean affine spaces and their spherical unit subspaces."""

from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.real_affine_spaces import RealAffineSpaces
from dzack_research.preamble.owned_category import _object_of


class EuclideanSpaceMor(CategoricalMor):
    r"""Affine isometries between selected Euclidean spaces."""

    class ElementMethods:
        def __init__(self, parent, affine_map):
            Morphism.__init__(self, parent)
            self._affine_map = affine_map

        def affine_map(self):
            return self._affine_map

        def _call_(self, point):
            return self._affine_map(point)

        def __mul__(self, other):
            pass

    def _element_constructor_(self, affine_map):
        if (
            affine_map.domain() is not self.domain().underlying_affine_space()
            or affine_map.codomain() is not self.codomain().underlying_affine_space()
        ):
            raise ValueError("the affine map must join the selected Euclidean affine spaces")
        return self.element_class(self, affine_map)

    @object_level
    def identity(self):
        pass


class EuclideanSpaceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = EuclideanSpaceMor


class _ForgetEuclideanMetric(Functor):
    def __init__(self):
        super().__init__(EuclideanSpaces(), RealAffineSpaces())

    def _apply_object(self, space):
        return space.underlying_affine_space()

    def _apply_morphism(self, morphism):
        return morphism.affine_map()


class EuclideanSpaces(OwnedCategory):
    r"""Real affine spaces with a selected positive-definite model-space form."""

    _MorCategory = EuclideanSpaceMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "Euclidean affine spaces"

    def an_object(self):
        pass

    def on(self, affine_space, positive_definite_form):
        if affine_space not in RealAffineSpaces():
            raise TypeError(f"{affine_space} is not a real affine space")
        return _object_of(
            self,
            affine_space=affine_space,
            positive_definite_form=positive_definite_form,
        )

    @cached_method
    def forget_metric(self):
        return _ForgetEuclideanMetric()

    class ParentMethods:
        def __init__(self, affine_space, positive_definite_form, **rest):
            self._affine_space = affine_space
            self._positive_definite_form = positive_definite_form
            super().__init__(**rest)

        def underlying_affine_space(self):
            return self._affine_space

        def model_inner_product(self):
            return self._positive_definite_form

        def point_set(self):
            return self._affine_space.point_set()


class SphericalSpaceMor(CategoricalMor):
    r"""Isometries of selected round spheres."""

    class ElementMethods:
        def __init__(self, parent, ambient_isometry):
            Morphism.__init__(self, parent)
            self._ambient_isometry = ambient_isometry

        def ambient_isometry(self):
            return self._ambient_isometry

        def _call_(self, point):
            return self._ambient_isometry(point)

        def __mul__(self, other):
            pass

    def _element_constructor_(self, ambient_isometry):
        if (
            ambient_isometry.domain() is not self.domain().euclidean_space()
            or ambient_isometry.codomain() is not self.codomain().euclidean_space()
        ):
            raise ValueError("the isometry must join the selected Euclidean ambient spaces")
        return self.element_class(self, ambient_isometry)

    @object_level
    def identity(self):
        pass


class SphericalSpaceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SphericalSpaceMor


class SphericalSpaces(OwnedCategory):
    r"""Round spheres with selected center, radius and Euclidean inclusion."""

    _MorCategory = SphericalSpaceMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "round spherical spaces"

    def an_object(self):
        pass

    def in_space(self, euclidean_space, center, radius, inclusion):
        if euclidean_space not in EuclideanSpaces():
            raise TypeError(f"{euclidean_space} is not a Euclidean space")
        return _object_of(
            self,
            euclidean_space=euclidean_space,
            center=center,
            radius=radius,
            inclusion=inclusion,
        )

    class ParentMethods:
        def __init__(self, euclidean_space, center, radius, inclusion, **rest):
            self._euclidean_space = euclidean_space
            self._center = center
            self._radius = radius
            self._inclusion = inclusion
            super().__init__(**rest)

        def euclidean_space(self):
            return self._euclidean_space

        def center(self):
            return self._center

        def radius(self):
            return self._radius

        def inclusion(self):
            return self._inclusion
