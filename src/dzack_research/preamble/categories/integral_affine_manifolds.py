r"""Integral-affine structures on manifolds and on regular loci of spaces."""

from sage.categories.category_with_axiom import all_axioms
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import SmoothManifolds
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


for _axiom in ("Oriented", "StrictLatticePointAtlas", "Sphere"):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


class IntegralAffineManifoldMor(CategoricalMor):
    r"""Locally integral-affine maps between selected affine manifolds."""

    def _element_constructor_(self, local_affine_map):
        raise NotImplementedError(
            "constructing an integral-affine map needs its chart maps, lattice actions, "
            "and their agreement on overlaps"
        )

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an identity requires the same integral-affine manifold")
        raise NotImplementedError("the integral-affine identity needs the selected atlas")


class IntegralAffineManifoldMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineManifoldMor


class _UnderlyingSmoothManifoldFunctor(Functor):
    r"""Forget the selected affine atlas, on objects and local affine maps."""

    def __init__(self):
        super().__init__(IntegralAffineManifolds(), SmoothManifolds())

    def _apply_object(self, manifold):
        return manifold.underlying_smooth_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_smooth_morphism()


class IntegralAffineManifolds(OwnedCategory):
    r"""Smooth real manifolds equipped with a selected integral-affine atlas.

    Forgetting the atlas changes the object and its morphisms, so the map to
    smooth manifolds is a functor rather than a supercategory inclusion.
    """

    _MorCategory = IntegralAffineManifoldMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine manifolds"

    def an_object(self):
        raise NotImplementedError("an integral-affine manifold needs a selected atlas")

    def on(self, smooth_manifold, affine_atlas):
        r"""Equip the exact smooth manifold with a selected integral-affine atlas."""
        raise NotImplementedError(
            "constructing an integral-affine manifold needs affine chart domains, "
            "transition arrows, and their cocycle"
        )

    @cached_method
    def forget(self):
        return _UnderlyingSmoothManifoldFunctor()

    class ParentMethods:
        def underlying_smooth_manifold(self):
            raise NotImplementedError("the constructor must retain the exact smooth manifold")

        def affine_charts(self):
            raise NotImplementedError("the constructor must retain the selected affine atlas")

        def integral_tangent_lattice(self):
            raise NotImplementedError("the selected atlas must induce its tangent lattice")

    class Oriented(CategoryWithAxiom):
        r"""Integral-affine structures whose linear transitions preserve orientation."""

    class StrictLatticePointAtlas(CategoryWithAxiom):
        r"""Selected atlases whose translations preserve the lattice points."""


class SingularIntegralAffineSpaceMor(CategoricalMor):
    r"""Maps preserving the singular set and the affine regular structure."""

    def _element_constructor_(self, regular_affine_map):
        raise NotImplementedError(
            "a singular integral-affine map needs a topological map, its regular "
            "integral-affine restriction, and their comparison"
        )

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an identity requires the same singular integral-affine space")
        raise NotImplementedError("the singular-space identity needs its regular-locus map")


class SingularIntegralAffineSpaceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SingularIntegralAffineSpaceMor


class _UnderlyingSingularTopologicalSpaceFunctor(Functor):
    r"""Forget the singular affine structure, on objects and morphisms."""

    def __init__(self):
        super().__init__(SingularIntegralAffineSpaces(), TopologicalSpaces())

    def _apply_object(self, space):
        return space.underlying_topological_space()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_morphism()


class SingularIntegralAffineSpaces(OwnedCategory):
    r"""Spaces with a selected singular locus and affine regular complement."""

    _MorCategory = SingularIntegralAffineSpaceMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "singular integral-affine spaces"

    def an_object(self):
        raise NotImplementedError("a singular integral-affine space needs its regular-locus atlas")

    def on(self, topological_space, singular_locus_inclusion, regular_affine_manifold):
        r"""Select the singular subobject and affine structure on its exact complement."""
        raise NotImplementedError(
            "constructing a singular integral-affine space needs the complement "
            "inclusion and its comparison with the supplied affine manifold"
        )

    @cached_method
    def forget(self):
        return _UnderlyingSingularTopologicalSpaceFunctor()

    class ParentMethods:
        def underlying_topological_space(self):
            raise NotImplementedError("the constructor must retain the exact space")

        def singular_locus(self):
            raise NotImplementedError("the constructor must retain the singular inclusion")

        def regular_locus(self):
            raise NotImplementedError("the constructor must retain the exact complement inclusion")

    class Sphere(CategoryWithAxiom):
        r"""Singular integral-affine spaces whose underlying space is a sphere."""
