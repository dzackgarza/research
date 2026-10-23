r"""Selected integral-affine collars along faces of affine pieces."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.integral_affine_manifolds import (
    IntegralAffineManifoldsWithBoundary,
)


class IntegralAffineCollarMor(CategoricalMor):
    r"""Affine maps of collar neighborhoods compatible with the selected faces."""

    class ElementMethods:
        def face_map(self):
            pass

        def neighborhood_affine_map(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, face_map, neighborhood_affine_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a collar identity requires the same source and target")
        pass


class IntegralAffineCollarMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineCollarMor


class _CollarNeighborhoodFunctor(Functor):
    r"""Forget the selected face and collar chart on objects and maps."""

    def __init__(self):
        super().__init__(IntegralAffineCollars(), IntegralAffineManifoldsWithBoundary())

    def _apply_object(self, collar):
        return collar.underlying_affine_manifold()

    def _apply_morphism(self, morphism):
        return morphism.neighborhood_affine_map()


class IntegralAffineCollars(OwnedCategory):
    r"""Affine neighborhood collars with a specified face inclusion."""

    _MorCategory = IntegralAffineCollarMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine collars"

    def an_object(self):
        pass

    def on(self, affine_piece, face_inclusion, neighborhood_inclusion, collar_chart):
        r"""Select a face, its neighborhood in the piece, and an affine collar chart."""
        pass

    def comparison(self, source_collar, target_collar, face_map, neighborhood_affine_map):
        r"""Select an affine extension of a specified face pairing."""
        pass

    @cached_method
    def forget_face(self):
        return _CollarNeighborhoodFunctor()

    class ParentMethods:
        def underlying_affine_manifold(self):
            pass

        def face_inclusion(self):
            pass

        def neighborhood_inclusion(self):
            pass

        def collar_chart(self):
            pass

        def face(self):
            pass

        def affine_piece(self):
            pass
