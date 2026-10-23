r"""Integral-affine structures on manifolds and on regular loci of spaces."""

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
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
from dzack_research.preamble.categories.manifold_dimension_strata import PureDimensionalManifolds
from dzack_research.preamble.categories.manifolds import SmoothManifolds
from dzack_research.preamble.categories.manifolds_with_boundary import (
    SmoothManifoldsWithBoundary,
    SmoothManifoldsWithCorners,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


for _axiom in (
    "Oriented",
    "StrictLatticePointAtlas",
    "FiniteSingularSet",
    "Sphere",
    "Disk",
    "RealProjectivePlane",
):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


class IntegralAffineManifoldMor(CategoricalMor):
    r"""Locally integral-affine maps between selected affine manifolds."""

    class ElementMethods:
        def underlying_smooth_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, local_affine_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an identity requires the same integral-affine manifold")
        pass


class IntegralAffineManifoldMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineManifoldMor


class _UnderlyingSmoothManifoldFunctor(Functor):
    r"""Forget the selected affine atlas, on objects and local affine maps."""

    def __init__(self, source, target):
        super().__init__(source, target)

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

    @staticmethod
    def __classcall__(cls, dimension=None):
        if dimension is not None:
            return IntegralAffineManifoldsOfDimension(dimension)
        return Category.__classcall__(cls)

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine manifolds"

    def an_object(self):
        pass

    def on(self, smooth_manifold, affine_atlas):
        r"""Equip the exact smooth manifold with a selected integral-affine atlas."""
        pass

    @cached_method
    def forget(self):
        return _UnderlyingSmoothManifoldFunctor(self, SmoothManifolds())

    class ParentMethods:
        def underlying_smooth_manifold(self):
            pass

        def affine_charts(self):
            pass

        def affine_atlas(self):
            pass

        def integral_tangent_lattice(self):
            pass

        def tangent_lattice_inclusion(self):
            r"""Return the lattice local system's inclusion in the tangent bundle."""
            pass

        def transition_derivative_comparison(self, source_chart, target_chart):
            r"""Compare the chart derivative with its integral lattice action."""
            pass

        def regular_open(self, open_inclusion):
            pass

        def regular_open_inclusion(self, open_affine_manifold):
            pass

        def holonomy(self, base_point, affine_frame):
            pass

        def holonomy_conjugacy_class(self, base_point):
            pass

    class Oriented(CategoryWithAxiom):
        r"""Integral-affine structures whose linear transitions preserve orientation."""

    class StrictLatticePointAtlas(CategoryWithAxiom):
        r"""Selected atlases whose translations preserve the lattice points."""


class IntegralAffineManifoldsOfDimension(OwnedParameterizedCategory):
    r"""Full dimension-``n`` stratum of the general integral-affine category."""

    @staticmethod
    def __classcall__(cls, dimension):
        dimension = _owned_integers()(dimension)
        if dimension < 0:
            raise ValueError(f"an integral-affine dimension must be nonnegative, not {dimension}")
        return Category.__classcall__(cls, dimension)

    def dimension(self):
        return self.parameter()

    def super_categories(self):
        return [IntegralAffineManifolds()]

    def _repr_object_names(self):
        return f"integral-affine manifolds of dimension {self.dimension()}"

    def an_object(self):
        pass

    def on(self, smooth_manifold, affine_atlas):
        pass

    @cached_method
    def forget(self):
        return _UnderlyingSmoothManifoldFunctor(
            self,
            PureDimensionalManifolds(SmoothManifolds(), self.dimension()),
        )


class IntegralAffineLocalIsomorphismMor(CategoricalMor):
    r"""Local affine isomorphisms with invertible integral linear parts."""

    class ElementMethods:
        def underlying_affine_morphism(self):
            pass

        def underlying_smooth_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, affine_morphism):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a local isomorphism identity requires the same manifold")
        pass


class IntegralAffineLocalIsomorphismMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineLocalIsomorphismMor


class _LocalIsomorphismInclusionFunctor(Functor):
    r"""Include local affine isomorphisms among all integral-affine maps."""

    def __init__(self):
        super().__init__(IntegralAffineLocalIsomorphisms(), IntegralAffineManifolds())

    def _apply_object(self, manifold):
        return manifold.underlying_integral_affine_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_affine_morphism()


class IntegralAffineLocalIsomorphisms(OwnedCategory):
    r"""The wide subcategory with local integral-affine isomorphisms as maps."""

    _MorCategory = IntegralAffineLocalIsomorphismMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine manifolds and local isomorphisms"

    def an_object(self):
        pass

    def on(self, affine_manifold):
        pass

    @cached_method
    def inclusion(self):
        return _LocalIsomorphismInclusionFunctor()

    class ParentMethods:
        def underlying_integral_affine_manifold(self):
            pass


class _StratifiedIntegralAffineMapMethods:
    def underlying_smooth_stratified_map(self):
        pass

    def interior_affine_map(self):
        pass

    def __mul__(self, other):
        pass


class _StratifiedIntegralAffineMor(CategoricalMor):
    ElementMethods = _StratifiedIntegralAffineMapMethods

    def _element_constructor_(self, smooth_stratified_map, local_affine_maps):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an affine identity requires the same source and target")
        pass


class IntegralAffineBoundaryMor(_StratifiedIntegralAffineMor):
    r"""Local integral-affine maps preserving the specified boundary."""


class IntegralAffineCornerMor(_StratifiedIntegralAffineMor):
    r"""Local integral-affine maps preserving every corner-depth stratum."""


class IntegralAffineBoundaryMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineBoundaryMor


class IntegralAffineCornerMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineCornerMor


class _StratifiedAffineForgetfulFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, manifold):
        return manifold.underlying_smooth_stratified_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_smooth_stratified_map()


class _StratifiedAffineInteriorFunctor(Functor):
    def __init__(self, source):
        super().__init__(source, IntegralAffineManifolds())

    def _apply_object(self, manifold):
        return manifold.interior_affine_manifold()

    def _apply_morphism(self, morphism):
        return morphism.interior_affine_map()


class _StratifiedAffineManifoldMethods:
    def underlying_smooth_stratified_manifold(self):
        pass

    def affine_atlas(self):
        pass

    def depth_stratum(self, depth):
        pass

    def interior_affine_manifold(self):
        pass

    def interior_inclusion(self):
        pass


class IntegralAffineManifoldsWithCorners(OwnedCategory):
    r"""Smooth corner manifolds with selected compatible integral-affine charts."""

    _MorCategory = IntegralAffineCornerMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine manifolds with corners"

    def an_object(self):
        pass

    def on(self, smooth_corner_manifold, affine_atlas):
        if smooth_corner_manifold not in SmoothManifoldsWithCorners():
            raise TypeError(f"{smooth_corner_manifold} is not a smooth corner manifold")
        pass

    @cached_method
    def forget(self):
        return _StratifiedAffineForgetfulFunctor(self, SmoothManifoldsWithCorners())

    @cached_method
    def interior(self):
        return _StratifiedAffineInteriorFunctor(self)

    class ParentMethods(_StratifiedAffineManifoldMethods):
        pass


class IntegralAffineManifoldsWithBoundary(OwnedCategory):
    r"""Smooth half-space manifolds with selected integral-affine charts."""

    _MorCategory = IntegralAffineBoundaryMorCategoryConstruction

    def super_categories(self):
        return [IntegralAffineManifoldsWithCorners()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine manifolds with boundary"

    def an_object(self):
        pass

    def on(self, smooth_boundary_manifold, affine_atlas):
        if smooth_boundary_manifold not in SmoothManifoldsWithBoundary():
            raise TypeError(f"{smooth_boundary_manifold} is not a smooth boundary manifold")
        pass

    @cached_method
    def forget(self):
        return _StratifiedAffineForgetfulFunctor(self, SmoothManifoldsWithBoundary())

    @cached_method
    def interior(self):
        return _StratifiedAffineInteriorFunctor(self)

    class ParentMethods(_StratifiedAffineManifoldMethods):
        def boundary(self):
            pass


class SingularIntegralAffineSpaceMor(CategoricalMor):
    r"""Maps preserving the singular set and the affine regular structure."""

    class ElementMethods:
        def underlying_topological_morphism(self):
            pass

        def singular_locus_morphism(self):
            pass

        def regular_affine_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, regular_affine_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an identity requires the same singular integral-affine space")
        pass


class SingularIntegralAffineSpaceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SingularIntegralAffineSpaceMor


class _UnderlyingSingularTopologicalSpaceFunctor(Functor):
    r"""Forget the singular affine structure, on objects and morphisms."""

    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, space):
        return space.underlying_topological_space()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_morphism()


class _RegularIntegralAffineLocusFunctor(Functor):
    r"""Restrict a singular affine space and its maps to the regular loci."""

    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, space):
        return space.regular_affine_manifold()

    def _apply_morphism(self, morphism):
        return morphism.regular_affine_morphism()


class _SingularLocusSubobjectFunctor(Functor):
    r"""Send each singular locus to its selected topological inclusion."""

    def __init__(self, source):
        super().__init__(source, TopologicalSpaces().MonomorphismArrowCategory())

    def _apply_object(self, space):
        return self.codomain().object(space.singular_locus_inclusion())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return self.codomain().Mor(source, target)(
            morphism.singular_locus_morphism(),
            morphism.underlying_topological_morphism(),
        )


class SingularIntegralAffineSpaces(OwnedCategory):
    r"""Spaces with a selected singular locus and affine regular complement."""

    _MorCategory = SingularIntegralAffineSpaceMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, dimension=None):
        if dimension is not None:
            return SingularIntegralAffineSpacesOfDimension(dimension)
        return Category.__classcall__(cls)

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "singular integral-affine spaces"

    def an_object(self):
        pass

    def on(self, topological_space, singular_locus_inclusion, regular_affine_manifold):
        r"""Select the singular subobject and affine structure on its exact complement."""
        pass

    def from_face_gluing(self, gluing_cocone, singular_locus_inclusion, affine_collars):
        r"""Select an affine structure from a complex quotient and collar data."""
        pass

    @cached_method
    def forget(self):
        return _UnderlyingSingularTopologicalSpaceFunctor(self, TopologicalSpaces())

    @cached_method
    def regular_locus(self):
        return _RegularIntegralAffineLocusFunctor(self, IntegralAffineManifolds())

    @cached_method
    def singular_locus_functor(self):
        return _SingularLocusSubobjectFunctor(self)

    class ParentMethods:
        def underlying_topological_space(self):
            pass

        def singular_locus(self):
            pass

        def singular_locus_inclusion(self):
            pass

        def regular_locus(self):
            pass

        def regular_locus_inclusion(self):
            pass

        def regular_affine_manifold(self):
            pass

        def gluing_cocone(self):
            pass

        def affine_collars(self):
            pass

        def local_monodromy(self, singular_point, loop, affine_frame):
            pass

    class FiniteSingularSet(CategoryWithAxiom):
        r"""Singular affine spaces whose selected singular locus is finite."""

    class Sphere(CategoryWithAxiom):
        r"""Singular integral-affine spaces whose underlying space is a sphere."""

    class Disk(CategoryWithAxiom):
        r"""Singular integral-affine spaces whose underlying space is a closed ball."""

    class RealProjectivePlane(CategoryWithAxiom):
        r"""Dimension-two singular affine spaces with underlying real projective plane."""


class SingularIntegralAffineSpacesOfDimension(OwnedParameterizedCategory):
    r"""Full dimension-``n`` stratum with specified singular local models."""

    @staticmethod
    def __classcall__(cls, dimension):
        dimension = _owned_integers()(dimension)
        if dimension < 1:
            raise ValueError(f"a singular affine dimension must be positive, not {dimension}")
        return Category.__classcall__(cls, dimension)

    def dimension(self):
        return self.parameter()

    @cached_method
    def local_model_category(self):
        return SingularIntegralAffineLocalModels(self.dimension())

    def super_categories(self):
        return [SingularIntegralAffineSpaces()]

    def _repr_object_names(self):
        return f"singular integral-affine spaces of dimension {self.dimension()}"

    def an_object(self):
        pass

    def on(
        self,
        topological_space,
        singular_locus_inclusion,
        regular_affine_manifold,
        local_models=None,
    ):
        pass

    def from_face_gluing(
        self,
        gluing_cocone,
        singular_locus_inclusion,
        affine_collars,
        local_models,
    ):
        pass

    @cached_method
    def forget(self):
        return _UnderlyingSingularTopologicalSpaceFunctor(self, TopologicalSpaces())

    @cached_method
    def regular_locus(self):
        return _RegularIntegralAffineLocusFunctor(self, IntegralAffineManifolds(self.dimension()))

    @cached_method
    def singular_locus_functor(self):
        return _SingularLocusSubobjectFunctor(self)

    class ParentMethods:
        def local_models(self):
            pass

        def local_model_at(self, singular_point):
            pass


class SingularIntegralAffineLocalModelMor(CategoricalMor):
    r"""Pointed local maps preserving the affine regular loci."""

    class ElementMethods:
        def underlying_pointed_map(self):
            pass

        def singular_locus_morphism(self):
            pass

        def regular_affine_morphism(self):
            pass

        def underlying_singular_affine_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, pointed_map, singular_locus_map, regular_affine_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a local-model identity requires the same source and target")
        pass


class SingularIntegralAffineLocalModelMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SingularIntegralAffineLocalModelMor


class _UnpointedSingularLocalModelFunctor(Functor):
    r"""Forget the selected singular point on a local model and map."""

    def __init__(self, source):
        super().__init__(source, SingularIntegralAffineSpaces(source.dimension()))

    def _apply_object(self, model):
        return model.underlying_singular_affine_space()

    def _apply_morphism(self, morphism):
        return morphism.underlying_singular_affine_morphism()


class SingularIntegralAffineLocalModels(OwnedParameterizedCategory):
    r"""Pointed dimension-``n`` neighbourhoods with affine regular complements."""

    _MorCategory = SingularIntegralAffineLocalModelMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, dimension):
        dimension = _owned_integers()(dimension)
        if dimension < 1:
            raise ValueError(f"a singular affine local-model dimension must be positive, not {dimension}")
        return Category.__classcall__(cls, dimension)

    def dimension(self):
        return self.parameter()

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"singular integral-affine local models of dimension {self.dimension()}"

    def an_object(self):
        pass

    def on(
        self,
        topological_neighborhood,
        singular_locus_inclusion,
        regular_affine_manifold,
        singular_point,
    ):
        pass

    @cached_method
    def forget_point(self):
        return _UnpointedSingularLocalModelFunctor(self)

    class ParentMethods:
        def underlying_singular_affine_space(self):
            pass

        def topological_neighborhood(self):
            pass

        def singular_locus_inclusion(self):
            pass

        def regular_affine_manifold(self):
            pass

        def singular_point(self):
            pass

        def link(self):
            pass

        def monodromy(self, loop, affine_frame):
            pass
