"""Owned categories and basic constructors for schemes over a base ring."""

from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism
from sage.schemes.affine.affine_space import AffineSpace as _SageAffineSpace
from sage.schemes.generic.scheme import Scheme as _SageScheme
from sage.schemes.generic.spec import Spec as _SageSpec
from sage.schemes.projective.projective_space import (
    ProjectiveSpace as _SageProjectiveSpace,
)
from sage.schemes.product_projective.space import (
    ProductProjectiveSpaces as _SageProductProjectiveSpaces,
)

from dzack_research.preamble.categories.abstract_categories import SliceOver
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    own_ring,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    LocallyRingedSpaces,
)
from dzack_research.preamble.refine import refine


_SCHEME_MORPHISM_WRAPPERS = {}


class SchemeMorphism(Morphism):
    r"""Categorical wrapper around one native Sage scheme morphism."""

    def __init__(self, native_morphism) -> None:
        self._native_morphism = native_morphism
        Morphism.__init__(self, native_morphism.parent())

    def native_morphism(self):
        return self._native_morphism

    def _call_(self, value):
        native_value = (
            value.native_morphism()
            if isinstance(value, SchemeMorphism)
            else value
        )
        return self.native_morphism()(native_value)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        other_native = (
            other.native_morphism()
            if isinstance(other, SchemeMorphism)
            else other
        )
        return categorical_scheme_morphism(self.native_morphism() * other_native)

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError("scheme morphisms are not composable")
        return result

    def then(self, after):
        return after.compose(self)

    def evaluate_at(self, point):
        return self.compose(point)

    def _repr_(self) -> str:
        return repr(self.native_morphism())


def categorical_scheme_morphism(native_morphism):
    if isinstance(native_morphism, SchemeMorphism):
        return native_morphism
    key = id(native_morphism)
    cached = _SCHEME_MORPHISM_WRAPPERS.get(key)
    if cached is not None and cached.native_morphism() is native_morphism:
        return cached
    wrapped = SchemeMorphism(native_morphism)
    _SCHEME_MORPHISM_WRAPPERS[key] = wrapped
    return wrapped


def _scheme_base_ring(scheme):
    stored = getattr(scheme, "_preamble_scheme_base_ring", None)
    if stored is not None:
        return stored
    return own_ring(scheme.base_ring())


def _has_scheme_placement(scheme, category_class) -> bool:
    return any(
        issubclass(dynamic_category_class, category_class)
        for dynamic_category_class in getattr(
            scheme,
            "_preamble_scheme_category_types",
            (),
        )
    )


def refine_scheme_morphism(morphism, base_ring):
    r"""Return a categorical wrapper of the native computational morphism."""
    _ = base_ring
    return categorical_scheme_morphism(morphism)


def refine_scheme(scheme, base_ring=None, categories=()):
    r"""Adopt a native Sage scheme into the owned scheme hierarchy."""
    base = own_ring(scheme.base_ring()) if base_ring is None else own_ring(base_ring)
    scheme._preamble_scheme_base_ring = base
    placements = [Schemes(base), *categories]
    category_types = set(getattr(scheme, "_preamble_scheme_category_types", ()))
    for placement in placements:
        for category in placement.all_super_categories(proper=False):
            category_types.add(type(category))
    scheme._preamble_scheme_category_types = frozenset(category_types)
    return refine(scheme, placements)


class Schemes(OwnedCategoryOverBaseRing):
    r"""Schemes over ``Spec(R)`` for the represented base ring ``R``."""

    def _repr_object_names(self):
        return f"schemes over {self.base_ring()}"

    def super_categories(self):
        return [LocallyRingedSpaces()]

    def __contains__(self, candidate) -> bool:
        return (
            getattr(candidate, "_preamble_scheme_base_ring", None) is self.base_ring()
            and _has_scheme_placement(candidate, Schemes)
        )

    def homset(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a scheme Hom requires two schemes over the stated base")
        return domain.Hom(codomain)

    Hom = homset

    @cached_method
    def base_scheme(self):
        return Spec(self.base_ring())

    @cached_method
    def slice_category(self):
        return SliceOver(LocallyRingedSpaces(), self.base_scheme())

    def as_slice_object(self, scheme):
        if scheme not in self:
            raise TypeError(f"{scheme} is not an object of {self}")
        return self.slice_category()(scheme.structure_morphism())

    def product(self, *schemes):
        return scheme_product(*schemes)

    def Affine(self):
        return AffineSchemes(self.base_ring())

    def Projective(self):
        return ProjectiveSchemes(self.base_ring())

    def QuasiAffine(self):
        return QuasiAffineSchemes(self.base_ring())

    def QuasiProjective(self):
        return QuasiProjectiveSchemes(self.base_ring())

    def Integral(self):
        return IntegralSchemes(self.base_ring())

    def Separated(self):
        return SeparatedSchemes(self.base_ring())

    def FiniteType(self):
        return FiniteTypeSchemes(self.base_ring())

    def Normal(self):
        return NormalSchemes(self.base_ring())

    def Smooth(self):
        return SmoothSchemes(self.base_ring())

    class ParentMethods:
        def scheme_base_ring(self):
            return _scheme_base_ring(self)

        def scheme_category(self):
            return Schemes(self.scheme_base_ring())

        def base_scheme(self):
            return Spec(self.scheme_base_ring())

        def structure_morphism(self):
            base = self.base_scheme()
            if self is base:
                return refine_scheme_morphism(self.identity_morphism(), self.scheme_base_ring())
            morphism = _SageScheme.base_morphism(self)
            if morphism.codomain() is not base:
                raise ArithmeticError(
                    "the native structure morphism does not land in the represented base scheme"
                )
            return refine_scheme_morphism(morphism, self.scheme_base_ring())

        def relative_dimension(self):
            if self is self.base_scheme():
                return 0
            return self.dimension_relative()

        def as_slice_object(self):
            return self.scheme_category().as_slice_object(self)

        def point_morphism(self, coordinates):
            point = self(coordinates)
            point_domain = point.domain()
            base = self.scheme_base_ring()
            if point_domain not in Schemes(base):
                categories = [
                    AffineSchemes(base),
                    FiniteTypeSchemes(base),
                    SmoothSchemes(base),
                ]
                if _integral_placement(base):
                    categories.append(IntegralSchemes(base))
                refine_scheme(point_domain, base, categories)
            return refine_scheme_morphism(point, self.scheme_base_ring())

        def categorical_identity_morphism(self):
            return refine_scheme_morphism(
                self.identity_morphism(),
                self.scheme_base_ring(),
            )

        def product(self, *others):
            return scheme_product(self, *others)

        def point_counts(self, extension_degree):
            r"""Return ``(#X(F_q),...,#X(F_{q^n}))`` for a finite base field."""
            degree = int(extension_degree)
            if degree < 1:
                raise ValueError("the extension degree must be positive")
            base = engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("finite-field point counts require a finite base field")
            return tuple(super().count_points(degree))

        def point_count(self, extension_degree=1):
            r"""Return ``#X(F_{q^n})`` for the stated extension degree ``n``."""
            return self.point_counts(extension_degree)[-1]

class _SchemePropertyCategory(OwnedCategoryOverBaseRing):
    property_name = "scheme property"

    def _repr_object_names(self):
        return f"{self.property_name} schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, type(self).__mro__[1])
        )


class SeparatedSchemes(_SchemePropertyCategory):
    property_name = "separated"

    class ParentMethods:
        def is_separated(self):
            return True


class FiniteTypeSchemes(_SchemePropertyCategory):
    property_name = "finite-type"

    class ParentMethods:
        def is_finite_type(self):
            return True


class IntegralSchemes(_SchemePropertyCategory):
    property_name = "integral"

    class ParentMethods:
        def is_integral(self):
            return True


class NormalSchemes(_SchemePropertyCategory):
    property_name = "normal"

    class ParentMethods:
        def is_normal(self):
            return True


class SmoothSchemes(_SchemePropertyCategory):
    property_name = "smooth"

    class ParentMethods:
        def is_smooth(self):
            return True


class AffineSchemes(_SchemePropertyCategory):
    property_name = "affine"

    def super_categories(self):
        return [Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]

    class ParentMethods:
        def is_affine(self):
            return True

        def closed_subscheme(self, *equations):
            from dzack_research.preamble.categories.schemes.subschemes import (
                refine_closed_subscheme,
            )

            equations = (
                tuple(equations[0])
                if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                else tuple(equations)
            )
            return refine_closed_subscheme(self.subscheme(equations), self)


class QuasiAffineSchemes(_SchemePropertyCategory):
    property_name = "quasi-affine"

    def super_categories(self):
        return [Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]

    class ParentMethods:
        def is_quasi_affine(self):
            return True


class QuasiProjectiveSchemes(_SchemePropertyCategory):
    property_name = "quasi-projective"

    def super_categories(self):
        return [Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]

    class ParentMethods:
        def is_quasi_projective(self):
            return True


class ProjectiveSchemes(_SchemePropertyCategory):
    property_name = "projective"

    def super_categories(self):
        return [
            Schemes(self.base_ring()),
            QuasiProjectiveSchemes(self.base_ring()),
            FiniteTypeSchemes(self.base_ring()),
            SeparatedSchemes(self.base_ring()),
        ]

    class ParentMethods:
        def is_projective(self):
            return True

        def closed_subscheme(self, *equations):
            from dzack_research.preamble.categories.schemes.subschemes import (
                refine_closed_subscheme,
            )

            equations = (
                tuple(equations[0])
                if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                else tuple(equations)
            )
            return refine_closed_subscheme(self.subscheme(equations), self)


class AffineSpaces(OwnedCategoryOverBaseRing):
    def _repr_object_names(self):
        return f"affine spaces over {self.base_ring()}"

    def super_categories(self):
        return [
            AffineSchemes(self.base_ring()),
            FiniteTypeSchemes(self.base_ring()),
            SmoothSchemes(self.base_ring()),
        ]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, AffineSpaces)
        )

    class ParentMethods:
        def zeta_function(self):
            r"""Return ``Z(A^d/F_q,T)=1/(1-q^d T)``."""
            base = engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
            from sage.rings.rational_field import QQ as SageQQ

            rational_functions = PolynomialRing(SageQQ, "T").fraction_field()
            T = rational_functions.gen()
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return 1 / (1 - q**d * T)


class ProjectiveSpaces(OwnedCategoryOverBaseRing):
    def _repr_object_names(self):
        return f"projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [
            ProjectiveSchemes(self.base_ring()),
            SmoothSchemes(self.base_ring()),
        ]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, ProjectiveSpaces)
        )

    class ParentMethods:
        def zeta_function(self):
            r"""Return ``Z(P^d/F_q,T)=prod_{i=0}^d(1-q^i T)^(-1)``."""
            base = engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.misc.misc_c import prod
            from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
            from sage.rings.rational_field import QQ as SageQQ

            rational_functions = PolynomialRing(SageQQ, "T").fraction_field()
            T = rational_functions.gen()
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return prod(1 / (1 - q**i * T) for i in range(d + 1))


class ProductSchemes(OwnedCategoryOverBaseRing):
    r"""Scheme products equipped with their stated factors and projections."""

    def _repr_object_names(self):
        return f"scheme products over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, ProductSchemes)
        )

    class ParentMethods:
        def factors(self):
            return self._preamble_product_factors

        def number_of_factors(self):
            return len(self.factors())

        def projection(self, index):
            return self._preamble_product_projections[index]

        def projections(self):
            return tuple(
                self.projection(index) for index in range(self.number_of_factors())
            )


class ProductProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Finite products of projective spaces over one base ring."""

    def _repr_object_names(self):
        return f"products of projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [
            ProductSchemes(self.base_ring()),
            ProjectiveSchemes(self.base_ring()),
            SmoothSchemes(self.base_ring()),
        ]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, ProductProjectiveSpaces)
        )


def _integral_placement(base_ring):
    try:
        return bool(engine_ring(base_ring).is_integral_domain())
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return False


def Spec(base_ring):
    r"""Return ``Spec(R)`` as the terminal object of the represented ``Sch/R``."""
    base = own_ring(base_ring)
    scheme = _SageSpec(engine_ring(base))
    categories = [
        AffineSchemes(base),
        FiniteTypeSchemes(base),
        SmoothSchemes(base),
    ]
    if _integral_placement(base):
        categories.append(IntegralSchemes(base))
    return refine_scheme(scheme, base, categories)


def AffineSpace(dimension, base_ring, names=None):
    r"""Return the owned affine space ``A^n_R``."""
    base = own_ring(base_ring)
    if names is None:
        scheme = _SageAffineSpace(dimension, engine_ring(base))
    else:
        scheme = _SageAffineSpace(dimension, engine_ring(base), names=names)
    categories = [AffineSpaces(base)]
    if _integral_placement(base):
        categories.append(IntegralSchemes(base))
    return refine_scheme(scheme, base, categories)


def ProjectiveSpace(dimension, base_ring, names=None):
    r"""Return the owned projective space ``P^n_R``."""
    base = own_ring(base_ring)
    if names is None:
        scheme = _SageProjectiveSpace(dimension, engine_ring(base))
    else:
        scheme = _SageProjectiveSpace(dimension, engine_ring(base), names=names)
    categories = [ProjectiveSpaces(base)]
    if _integral_placement(base):
        categories.append(IntegralSchemes(base))
    return refine_scheme(scheme, base, categories)


def _product_projection(product, factor, coordinates):
    native = product.Hom(factor)(list(coordinates))
    return categorical_scheme_morphism(native)


def scheme_product(*schemes):
    r"""Return the categorical product in the currently supported scheme regimes.

    Affine spaces use ``A^m x A^n = A^{m+n}``; products of projective spaces
    use Sage's genuine multiprojective scheme backend.  In both cases the
    returned scheme retains the stated factors and actual projection
    morphisms.  General affine schemes and mixed products belong to the same
    surface but require the coordinate-algebra tensor-product/fiber-product
    layer and are not silently represented as products of underlying sets.
    """
    if len(schemes) == 1 and isinstance(schemes[0], (tuple, list)):
        schemes = tuple(schemes[0])
    if len(schemes) < 2:
        raise ValueError("a represented scheme product requires at least two factors")
    base = schemes[0].scheme_base_ring()
    if any(scheme not in Schemes(base) for scheme in schemes):
        raise TypeError("all product factors must be schemes over the same base")
    if any(scheme.scheme_base_ring() is not base for scheme in schemes):
        raise ValueError("all product factors must have the same represented base ring")

    if all(scheme in AffineSpaces(base) for scheme in schemes):
        dimensions = tuple(int(scheme.relative_dimension()) for scheme in schemes)
        names = tuple(
            f"x{factor}_{coordinate}"
            for factor, dimension in enumerate(dimensions)
            for coordinate in range(dimension)
        )
        product = AffineSpace(sum(dimensions), base, names=names)
        refine_scheme(product, base, [ProductSchemes(base)])
        coordinates = tuple(product.coordinate_ring().gens())
        projections = []
        offset = 0
        for factor, dimension in zip(schemes, dimensions, strict=True):
            projections.append(
                _product_projection(
                    product,
                    factor,
                    coordinates[offset : offset + dimension],
                )
            )
            offset += dimension
    elif all(scheme in ProjectiveSpaces(base) for scheme in schemes):
        product = _SageProductProjectiveSpaces(list(schemes))
        categories = [ProductProjectiveSpaces(base)]
        if _integral_placement(base):
            categories.append(IntegralSchemes(base))
        refine_scheme(product, base, categories)
        coordinates = tuple(product.coordinate_ring().gens())
        projections = []
        offset = 0
        for factor in schemes:
            width = int(factor.relative_dimension()) + 1
            projections.append(
                _product_projection(
                    product,
                    factor,
                    coordinates[offset : offset + width],
                )
            )
            offset += width
    else:
        raise NotImplementedError(
            "general or mixed scheme products require the affine tensor-product/fiber-product layer"
        )

    product._preamble_product_factors = tuple(schemes)
    product._preamble_product_projections = tuple(projections)
    return product


__all__ = [
    "AffineSchemes",
    "AffineSpace",
    "AffineSpaces",
    "FiniteTypeSchemes",
    "IntegralSchemes",
    "NormalSchemes",
    "ProjectiveSchemes",
    "ProjectiveSpace",
    "ProjectiveSpaces",
    "ProductProjectiveSpaces",
    "ProductSchemes",
    "QuasiAffineSchemes",
    "QuasiProjectiveSchemes",
    "Schemes",
    "SchemeMorphism",
    "SeparatedSchemes",
    "SmoothSchemes",
    "Spec",
    "refine_scheme",
    "refine_scheme_morphism",
    "categorical_scheme_morphism",
    "scheme_product",
]
