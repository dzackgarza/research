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
            raise NotImplementedError("the isometry must retain its affine map")

        def __mul__(self, other):
            raise NotImplementedError("isometry composition needs its affine maps")

    def _element_constructor_(self, affine_map):
        raise NotImplementedError("an affine isometry needs preservation of the selected metrics")

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a Euclidean identity requires the same space")
        raise NotImplementedError("the identity needs its underlying affine identity")


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
        raise NotImplementedError("a Euclidean space needs an affine space and metric")

    def on(self, affine_space, positive_definite_form):
        if affine_space not in RealAffineSpaces():
            raise TypeError(f"{affine_space} is not a real affine space")
        raise NotImplementedError("construction needs a positive-definite form on the model space")

    @cached_method
    def forget_metric(self):
        return _ForgetEuclideanMetric()

    class ParentMethods:
        def underlying_affine_space(self):
            raise NotImplementedError("the constructor must retain the exact affine space")

        def model_inner_product(self):
            raise NotImplementedError("the constructor must retain its positive-definite form")

        def point_set(self):
            raise NotImplementedError("the constructor must retain the affine point set")


class SphericalSpaceMor(CategoricalMor):
    r"""Isometries of selected round spheres."""

    class ElementMethods:
        def ambient_isometry(self):
            raise NotImplementedError("the spherical map must retain its ambient isometry")

        def __mul__(self, other):
            raise NotImplementedError("composition needs the two ambient isometries")

    def _element_constructor_(self, ambient_isometry):
        raise NotImplementedError("a spherical map needs the commuting sphere inclusions")

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a spherical identity requires the same sphere")
        raise NotImplementedError("the identity needs the selected sphere inclusion")


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
        raise NotImplementedError("a sphere needs its Euclidean ambient space")

    def in_space(self, euclidean_space, center, radius):
        if euclidean_space not in EuclideanSpaces():
            raise TypeError(f"{euclidean_space} is not a Euclidean space")
        raise NotImplementedError("construction needs the metric sphere and its inclusion")

    class ParentMethods:
        def euclidean_space(self):
            raise NotImplementedError("the sphere constructor must retain its ambient space")

        def center(self):
            raise NotImplementedError("the sphere constructor must retain its center")

        def radius(self):
            raise NotImplementedError("the sphere constructor must retain its radius")

        def inclusion(self):
            raise NotImplementedError("the sphere constructor must retain its ambient inclusion")
