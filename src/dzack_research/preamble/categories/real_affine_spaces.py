r"""Real affine spaces as torsors over a selected real vector space."""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method

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
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    VectorSpaces,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.rings.real import RR


class RealVectorSpaces(OwnedParameterizedCategory):
    r"""Full category of real vector spaces of one fixed finite dimension."""

    @staticmethod
    def __classcall__(cls, dimension):
        dimension = _owned_integers()(dimension)
        if dimension < 0:
            raise ValueError(f"a real vector-space dimension must be nonnegative, not {dimension}")
        return Category.__classcall__(cls, dimension)

    def dimension(self):
        return self.parameter()

    def super_categories(self):
        return [VectorSpaces(RR)]

    def _repr_object_names(self):
        return f"real vector spaces of dimension {self.dimension()}"

    def an_object(self):
        pass

    def on(self, vector_space):
        r"""Place the exact real vector space in its dimension stratum."""
        pass


class RealAffineSpaceMor(CategoricalMor):
    r"""Affine maps with a linear part and an equivariant point map."""

    class ElementMethods:
        def __init__(self, parent, linear_part, point_map):
            Morphism.__init__(self, parent)
            self._linear_part = linear_part
            self._point_map = point_map

        def linear_part(self):
            return self._linear_part

        def point_map(self):
            return self._point_map

        def _call_(self, point):
            return self._point_map(point)

        def __mul__(self, other):
            pass

    def _element_constructor_(self, linear_part, point_map):
        return self.element_class(self, linear_part, point_map)

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


class _AffineModelVectorSpaceFunctor(Functor):
    r"""Take the translation space and linear part of an affine map."""

    def __init__(self):
        super().__init__(RealAffineSpaces(), VectorSpaces(RR))

    def _apply_object(self, affine_space):
        return affine_space.model_vector_space()

    def _apply_morphism(self, morphism):
        return morphism.linear_part()


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
        return _object_of(
            self,
            model_vector_space=model_vector_space,
            point_set=point_set,
            translation_action=translation_action,
        )

    @cached_method
    def forget(self):
        return _AffineUnderlyingSetFunctor()

    @cached_method
    def model_vector_space(self):
        return _AffineModelVectorSpaceFunctor()

    class ParentMethods:
        def __init__(self, model_vector_space, point_set, translation_action, **rest):
            self._model_vector_space = model_vector_space
            self._point_set = point_set
            self._translation_action = translation_action
            super().__init__(**rest)

        def point_set(self):
            return self._point_set

        def model_vector_space(self):
            return self._model_vector_space

        def translation_action(self):
            return self._translation_action


class AffineSpaceWithLatticeMor(CategoricalMor):
    r"""Affine maps whose linear parts carry the selected lattice into the target lattice."""

    class ElementMethods:
        def __init__(self, parent, affine_map, lattice_map):
            Morphism.__init__(self, parent)
            self._affine_map = affine_map
            self._lattice_map = lattice_map

        def affine_map(self):
            return self._affine_map

        def linear_part(self):
            return self._affine_map.linear_part()

        def lattice_map(self):
            return self._lattice_map

        def _call_(self, point):
            return self._affine_map(point)

        def __mul__(self, other):
            pass

    def _element_constructor_(self, affine_map, lattice_map):
        return self.element_class(self, affine_map, lattice_map)

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


class _AffineLatticeFunctor(Functor):
    r"""Take the selected integral lattice and induced linear lattice map."""

    def __init__(self):
        super().__init__(AffineSpacesWithLattice(), FinitelyGeneratedFreeModules(_owned_integers()))

    def _apply_object(self, space):
        return space.affine_lattice()

    def _apply_morphism(self, morphism):
        return morphism.lattice_map()


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
        return _object_of(
            self,
            affine_space=affine_space,
            lattice_inclusion=lattice_inclusion,
        )

    @cached_method
    def forget(self):
        return _UnderlyingAffineSpaceFunctor()

    @cached_method
    def lattice(self):
        return _AffineLatticeFunctor()

    class ParentMethods:
        def __init__(self, affine_space, lattice_inclusion, **rest):
            self._affine_space = affine_space
            self._lattice_inclusion = lattice_inclusion
            super().__init__(**rest)

        def underlying_affine_space(self):
            return self._affine_space

        def lattice_inclusion(self):
            return self._lattice_inclusion

        def affine_lattice(self):
            return self._lattice_inclusion.domain()

        def integral_affine_group(self):
            pass

        def integral_affine_group_action(self):
            pass
