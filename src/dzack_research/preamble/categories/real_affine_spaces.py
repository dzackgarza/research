r"""Real affine spaces as torsors over a selected real vector space."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.rings.real import RR


class RealAffineSpaceMor(CategoricalMor):
    r"""Affine maps with a linear part and an equivariant point map."""

    class ElementMethods:
        def linear_part(self):
            pass

        def point_map(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, linear_part, point_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an affine identity requires the same source and target")
        pass


class RealAffineSpaceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = RealAffineSpaceMor


class _AffineUnderlyingSetFunctor(Functor):
    r"""Forget the translation action, on affine spaces and affine maps."""

    def __init__(self):
        super().__init__(RealAffineSpaces(), Sets())

    def _apply_object(self, affine_space):
        return affine_space.point_set()

    def _apply_morphism(self, morphism):
        return morphism.point_map()


class RealAffineSpaces(OwnedCategory):
    r"""Torsors for additive real vector spaces, with affine maps."""

    _MorCategory = RealAffineSpaceMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "real affine spaces"

    def an_object(self):
        pass

    def on(self, model_vector_space, point_set, translation_action):
        r"""Select a free transitive action of the model space on ``point_set``."""
        if model_vector_space not in VectorSpaces(RR):
            raise TypeError(f"{model_vector_space} is not a real vector space")
        pass

    @cached_method
    def forget(self):
        return _AffineUnderlyingSetFunctor()

    class ParentMethods:
        def point_set(self):
            pass

        def model_vector_space(self):
            pass

        def translation_action(self):
            pass


class AffineSpaceWithLatticeMor(CategoricalMor):
    r"""Affine maps whose linear parts carry the selected lattice into the target lattice."""

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
            raise ValueError("a lattice-affine identity requires the same source and target")
        pass


class AffineSpaceWithLatticeMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = AffineSpaceWithLatticeMor


class _UnderlyingAffineSpaceFunctor(Functor):
    r"""Forget the selected lattice embedding, on spaces and maps."""

    def __init__(self):
        super().__init__(AffineSpacesWithLattice(), RealAffineSpaces())

    def _apply_object(self, space):
        return space.underlying_affine_space()

    def _apply_morphism(self, morphism):
        return morphism.affine_map()


class AffineSpacesWithLattice(OwnedCategory):
    r"""Real affine spaces with a selected full lattice in their model space."""

    _MorCategory = AffineSpaceWithLatticeMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "real affine spaces with a selected lattice"

    def an_object(self):
        pass

    def on(self, affine_space, lattice_inclusion):
        r"""Select a full integral lattice in the model of ``affine_space``."""
        if affine_space not in RealAffineSpaces():
            raise TypeError(f"{affine_space} is not a real affine space")
        pass

    @cached_method
    def forget(self):
        return _UnderlyingAffineSpaceFunctor()

    class ParentMethods:
        def underlying_affine_space(self):
            pass

        def lattice_inclusion(self):
            pass

        def integral_affine_group(self):
            pass
