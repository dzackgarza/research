r"""Pure-dimensional strata of the represented manifold categories."""

from sage.categories.category import Category

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.manifolds import (
    ComplexManifolds,
    DifferentiableManifolds,
    SmoothManifolds,
    TopologicalManifolds,
)
from dzack_research.preamble.categories.manifolds_with_boundary import (
    SmoothManifoldsWithBoundary,
    SmoothManifoldsWithCorners,
    TopologicalManifoldsWithBoundary,
    TopologicalManifoldsWithCorners,
)
from dzack_research.preamble.categories.real_ck_manifolds import RealCkManifolds
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers


class PureDimensionalManifolds(OwnedCategory):
    r"""The full subcategory of manifolds pure of dimension ``n``.

    The dimension is real except when the selected base is
    ``ComplexManifolds()``, where it is complex dimension. Morphisms are
    exactly those of the selected base category between objects in this
    stratum; restricting objects does not change a hom set.
    """

    @staticmethod
    def __classcall__(cls, base_category, dimension):
        if base_category not in (
            TopologicalManifolds(),
            DifferentiableManifolds(),
            SmoothManifolds(),
            ComplexManifolds(),
            TopologicalManifoldsWithBoundary(),
            SmoothManifoldsWithBoundary(),
            TopologicalManifoldsWithCorners(),
            SmoothManifoldsWithCorners(),
        ) and not isinstance(base_category, RealCkManifolds):
            raise TypeError(f"{base_category} is not a selected manifold category")
        dimension = _owned_integers()(dimension)
        if dimension < 0:
            raise ValueError(f"a manifold dimension must be nonnegative, not {dimension}")
        return Category.__classcall__(cls, base_category, dimension)

    def __init__(self, base_category, dimension):
        self._base_category = base_category
        self._dimension = dimension
        super().__init__()

    def base_category(self):
        return self._base_category

    def dimension(self):
        return self._dimension

    def super_categories(self):
        return [self.base_category()]

    def _repr_object_names(self):
        return f"pure {self.dimension()}-dimensional {self.base_category()}"

    def an_object(self):
        raise NotImplementedError("the base constructor must present a pure-dimensional manifold")

    def on(self, manifold):
        r"""Place the exact base manifold in its pure-dimension stratum."""
        if manifold not in self.base_category():
            raise TypeError(f"{manifold} is not in {self.base_category()}")
        raise NotImplementedError(
            "stratum construction needs the dimension of every connected component "
            "and must retain the exact manifold and its maps"
        )
