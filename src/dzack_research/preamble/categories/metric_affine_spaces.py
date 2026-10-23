r"""Euclidean affine spaces and their spherical unit subspaces."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.real_affine_spaces import RealAffineSpaces


class EuclideanSpaceMor(CategoricalMor):
    r"""Affine isometries between selected Euclidean spaces."""

    class ElementMethods:
        def affine_map(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, affine_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a Euclidean identity requires the same space")
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
        pass

    @cached_method
    def forget_metric(self):
        return _ForgetEuclideanMetric()

    class ParentMethods:
        def underlying_affine_space(self):
            pass

        def model_inner_product(self):
            pass

        def point_set(self):
            pass


class SphericalSpaceMor(CategoricalMor):
    r"""Isometries of selected round spheres."""

    class ElementMethods:
        def ambient_isometry(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, ambient_isometry):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a spherical identity requires the same sphere")
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

    def in_space(self, euclidean_space, center, radius):
        if euclidean_space not in EuclideanSpaces():
            raise TypeError(f"{euclidean_space} is not a Euclidean space")
        pass

    class ParentMethods:
        def euclidean_space(self):
            pass

        def center(self):
            pass

        def radius(self):
            pass

        def inclusion(self):
            pass
