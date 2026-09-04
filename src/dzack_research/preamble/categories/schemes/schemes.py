"""Owned categories and basic constructors for schemes over a base ring."""

from sage.misc.cachefunc import cached_function, cached_method
from sage.categories.morphism import Morphism
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.affine.affine_space import AffineSpace as _SageAffineSpace
from sage.schemes.generic.scheme import AffineScheme as _SageAffineScheme
from sage.schemes.generic.scheme import Scheme as _SageScheme
from sage.schemes.generic.spec import Spec as _SageSpec
from sage.schemes.projective.projective_space import (
    ProjectiveSpace as _SageProjectiveSpace,
)
from sage.schemes.product_projective.space import (
    ProductProjectiveSpaces as _SageProductProjectiveSpaces,
)

from dzack_research.preamble.categories.abstract_categories.arrow_categories import SliceOver
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    MonoCategoryOf,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.rings.commutative_algebra import (
    refine_commutative_algebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.rings.rings import refine_ring_constructions
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    LocallyRingedSpaces,
    SchemeUnderlyingSpace,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.abstract_categories.constructions import (
    Coproduct,
    Pushout,
    Subobjects,
)
from dzack_research.preamble.categories.abstract_categories.products import _finite_factor_family
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    _engine_algebra_morphism,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import ring_homset
from dzack_research.preamble.categories.sets.finite_families import finite_family


_SCHEME_MORPHISM_WRAPPERS = {}


class SchemeMorphism(Morphism):
    r"""Categorical wrapper around one native Sage scheme morphism."""

    _preamble_coordinate_algebra_morphism = None

    def __init__(
        self,
        native_morphism,
        *,
        domain=None,
        codomain=None,
        homset=None,
        pullback=None,
    ) -> None:
        self._native_morphism = native_morphism
        self._preamble_domain_override = domain
        self._preamble_codomain_override = codomain
        if pullback is not None:
            self._preamble_coordinate_algebra_morphism = pullback
        if homset is None:
            engine = native_morphism.parent()
            homset = _scheme_mor_category(engine.domain(), engine.codomain())
        Morphism.__init__(self, homset)

    def native_morphism(self):
        return self._native_morphism

    def domain(self):
        return (
            self.parent().domain()
            if self._preamble_domain_override is None
            else self._preamble_domain_override
        )

    def codomain(self):
        return (
            self.parent().codomain()
            if self._preamble_codomain_override is None
            else self._preamble_codomain_override
        )

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
        if not isinstance(other, SchemeMorphism):
            return NotImplemented
        # The identity is a two-sided unit.  That is a theorem, so the
        # composite is the other factor itself.
        if self._is_the_identity():
            return other
        if other._is_the_identity():
            return self
        # The composite is a morphism between the stated endpoints, whichever
        # engine route computes it.  Reading the endpoints off the engine's
        # answer lands it on Spec of a coordinate ring instead.
        homset = _scheme_mor_category(other.domain(), self.codomain())
        left_pullback = self._preamble_coordinate_algebra_morphism
        right_pullback = other._preamble_coordinate_algebra_morphism
        if left_pullback is not None and right_pullback is not None:
            composite = affine_spec_morphism(right_pullback * left_pullback)
            # Re-siting the composite in the Hom of the stated endpoints must
            # not drop the pullback it was computed from.
            return SchemeMorphism(
                composite.native_morphism(),
                homset=homset,
                pullback=composite.coordinate_algebra_morphism(),
            )
        return homset(self.native_morphism() * other.native_morphism())

    def _is_the_identity(self) -> bool:
        r"""Return whether this morphism is its Hom object's identity."""
        if self.domain() is not self.codomain():
            return False
        return self is self.parent().identity()

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError("scheme morphisms are not composable")
        return result

    def then(self, after):
        return after.compose(self)

    def evaluate_at(self, point):
        if isinstance(point, SchemeMorphism):
            native_point = point.native_morphism()
            base = self.domain().scheme_base_ring()
            if self.domain() in ProductProjectiveSpaces(base):
                factors = self.domain().factors()
                stored_points = getattr(native_point, "_points", None)
                if stored_points is not None:
                    for index, factor in enumerate(factors):
                        if factor is self.codomain():
                            return categorical_scheme_morphism(stored_points[index])
        return self.compose(point)

    def coordinate_algebra_morphism(self):
        morphism = self._preamble_coordinate_algebra_morphism
        if morphism is None:
            raise NotImplementedError(
                "this scheme morphism has no represented pullback on affine coordinate algebras"
            )
        return morphism

    pullback_on_coordinate_algebras = coordinate_algebra_morphism

    def __eq__(self, other) -> bool:
        r"""Decide equality from represented pullbacks or the native carrier."""
        if not isinstance(other, SchemeMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        if self is other:
            return True
        left_pullback = self._preamble_coordinate_algebra_morphism
        right_pullback = other._preamble_coordinate_algebra_morphism
        if left_pullback is not None and right_pullback is not None:
            return bool(left_pullback == right_pullback)
        from sage.schemes.generic.morphism import SchemeMorphism_id

        left_native = self.native_morphism()
        right_native = other.native_morphism()
        if isinstance(left_native, SchemeMorphism_id) and isinstance(
            right_native, SchemeMorphism_id
        ):
            return True
        return bool(left_native == right_native)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.domain()), id(self.codomain()), id(self.native_morphism())))

    def _repr_(self) -> str:
        return f"Scheme morphism: {self.domain()} -> {self.codomain()}"


def categorical_scheme_morphism(native_morphism, *, domain=None, codomain=None):
    if isinstance(native_morphism, SchemeMorphism):
        if domain is None and codomain is None:
            return native_morphism
        native_morphism = native_morphism.native_morphism()
    if domain is not None or codomain is not None:
        return SchemeMorphism(native_morphism, domain=domain, codomain=codomain)
    key = id(native_morphism)
    cached = _SCHEME_MORPHISM_WRAPPERS.get(key)
    if cached is not None and cached.native_morphism() is native_morphism:
        return cached
    wrapped = SchemeMorphism(native_morphism)
    _SCHEME_MORPHISM_WRAPPERS[key] = wrapped
    return wrapped


class SchemeMorCategory(CategoricalHomset):
    r"""The owned category \(\mathrm{Mor}_{\mathbf{Sch}}(X, Y)\).

    Its objects are the scheme morphisms \(X\to Y\).  Sage's own scheme
    Homset stays underneath as the computation engine: it is what the native
    morphisms are built by, and it never reaches a session.
    """

    Element = SchemeMorphism

    def __init__(self, schemes, domain, codomain) -> None:
        self._engine_homset = _SageScheme._Hom_(domain, codomain)
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(schemes), domain, codomain
        )

    def _engine_homset_crossing(self):
        r"""Return the private Sage Homset these morphisms are computed in."""
        return self._engine_homset

    def _element_constructor_(self, datum):
        if isinstance(datum, SchemeMorphism):
            if datum.parent() is self:
                return datum
            datum = datum.native_morphism()
        return SchemeMorphism(datum, homset=self)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        # Each owned scheme records its identity when it is constructed, built
        # from its engine coordinate ring.  Sage's own Homset identity would
        # ask the owned coordinate algebra for `gens`, which is not a name the
        # owned surface answers.
        return self(self.domain().categorical_identity_morphism())


def _scheme_mor_category(domain, codomain):
    schemes = Schemes(_scheme_base_ring(domain))
    return schemes.Mor(domain, codomain)


def _scheme_base_ring(scheme):
    stored = getattr(scheme, "_preamble_scheme_base_ring", None)
    if stored is not None:
        return stored
    return _own_ring(scheme.base_ring())


def _has_scheme_placement(scheme, category_class) -> bool:
    return any(
        issubclass(dynamic_category_class, category_class)
        for dynamic_category_class in getattr(
            scheme,
            "_preamble_scheme_category_types",
            (),
        )
    )


def _native_scheme_homset(domain, codomain):
    r"""Return Sage's private scheme-Hom runtime carrier for owned schemes."""
    return _SageScheme._Hom_(domain, codomain)


def refine_scheme_morphism(morphism, base_ring):
    r"""Return a categorical wrapper of the native computational morphism."""
    _ = base_ring
    return categorical_scheme_morphism(morphism)


def refine_scheme(scheme, base_ring=None, categories=()):
    r"""Adopt a native Sage scheme into the owned scheme hierarchy."""
    base = _own_ring(scheme.base_ring()) if base_ring is None else _own_ring(base_ring)
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

    def an_object(self):
        r"""The affine line over the base ring."""
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())

    def _repr_object_names(self):
        return f"schemes over {self.base_ring()}"

    def super_categories(self):
        return [LocallyRingedSpaces()]

    def __contains__(self, candidate) -> bool:
        return (
            getattr(candidate, "_preamble_scheme_base_ring", None) is self.base_ring()
            and _has_scheme_placement(candidate, Schemes)
        )

    @cached_method
    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a scheme Hom requires two schemes over the stated base")
        return SchemeMorCategory(self, domain, codomain)

    _MonoCategory = None  # set below, once SchemeMonomorphisms is defined

    class SubcategoryMethods:
        def product(self, factors):
            r"""Return the product of a finite family of objects of this category."""
            return self._fold_construction(
                self._categorical_product, factors, name="Product factors"
            )

        def _categorical_product(self, left, right):
            return scheme_product(left, right)

        def _categorical_pullback(self, left_morphism, right_morphism):
            return scheme_fiber_product(left_morphism, right_morphism)

        def Subobjects(self, ambient):
            r"""Return the category of subobjects of ``ambient``."""
            if ambient not in self:
                raise TypeError("a subobject category is taken of a scheme in this category")
            return Subobjects(ambient, Schemes(ambient.scheme_base_ring()))


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
        def Mor(self, codomain, category=None):
            schemes = Schemes(self.scheme_base_ring())
            if category is None or category.is_subcategory(schemes):
                return schemes.Mor(self, codomain)
            return _SageScheme._Hom_(self, codomain, category=category)

        def scheme_base_ring(self):
            return _scheme_base_ring(self)

        def scheme_category(self):
            return Schemes(self.scheme_base_ring())

        def base_scheme(self):
            return Spec(self.scheme_base_ring())

        def _scheme_underlying_space(self):
            base_ring = self.scheme_base_ring()
            if self in AffineSchemes(base_ring):
                return self.coordinate_algebra().spectrum()
            return SchemeUnderlyingSpace(self)

        def _structure_sheaf_global_sections(self):
            base_ring = self.scheme_base_ring()
            if self in AffineSchemes(base_ring):
                return self.coordinate_algebra()
            if self in ProjectiveSpaces(base_ring):
                return base_ring
            raise NotImplementedError(
                f"global sections of the structure sheaf of {self} are not yet represented"
            )

        def _structure_sheaf_sections_on_distinguished_open(self, distinguished_open):
            base_ring = self.scheme_base_ring()
            if self not in AffineSchemes(base_ring):
                raise NotImplementedError(
                    "distinguished-open structure-sheaf sections are represented for affine schemes"
                )
            spectrum = self.underlying_space()
            if distinguished_open.codomain() is not spectrum:
                raise ValueError(
                    "the distinguished open belongs to a different affine spectrum"
                )
            return distinguished_open.coordinate_ring()

        def _structure_sheaf_stalk(self, point):
            base_ring = self.scheme_base_ring()
            if self not in AffineSchemes(base_ring):
                raise NotImplementedError(
                    "the active stalk construction is represented on affine schemes"
                )
            spectrum = self.underlying_space()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            return point.local_ring()

        def structure_morphism(self):
            selected = getattr(self, "_preamble_structure_morphism", None)
            if selected is not None:
                return selected
            base = self.base_scheme()
            if self is base:
                return self.categorical_identity_morphism()
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
            base = self.scheme_base_ring()
            engine_base = _engine_ring(base)
            engine_coordinates = tuple(
                _engine_element(base, coordinate)
                if getattr(coordinate, "parent", lambda: None)() is base
                else engine_base(coordinate)
                for coordinate in coordinates
            )
            if self in ProductProjectiveSpaces(base):
                factors = self.factors()
                factor_points = []
                offset = 0
                for factor in factors:
                    width = int(factor.relative_dimension()) + 1
                    factor_coordinates = engine_coordinates[offset : offset + width]
                    if len(factor_coordinates) != width:
                        raise ValueError(
                            "a product-projective point has one homogeneous coordinate block per factor"
                        )
                    factor_points.append(
                        factor._point(
                            factor.point_homset(),
                            factor_coordinates,
                            check=False,
                        )
                    )
                    offset += width
                if offset != len(engine_coordinates):
                    raise ValueError(
                        "too many homogeneous coordinates for this product of projective spaces"
                    )
                point = self._point(
                    self.point_homset(),
                    factor_points,
                    check=False,
                )
            else:
                point = self._point(
                    self.point_homset(),
                    engine_coordinates,
                    check=False,
                )
            point_domain = point.domain()
            if point_domain not in Schemes(base):
                categories = [
                    AffineSchemes(base),
                    FiniteTypeSchemes(base),
                    SmoothSchemes(base),
                ]
                if _integral_placement(base):
                    categories.append(IntegralSchemes(base))
                refine_scheme(point_domain, base, categories)
            return refine_scheme_morphism(point, base)

        def categorical_identity_morphism(self):
            selected = getattr(self, "_preamble_identity_morphism", None)
            if selected is not None:
                return selected
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
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("finite-field point counts require a finite base field")

            return finite_family(
                super().count_points(degree), name="Point counts"
            )

        def point_count(self, extension_degree=1):
            r"""Return ``#X(F_{q^n})`` for the stated extension degree ``n``."""
            degree = int(extension_degree)
            return self.point_counts(degree)[degree - 1]

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

    def an_object(self):
        r"""The affine line, separated because it is affine."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return AffineSpace(1, self.base_ring())


class FiniteTypeSchemes(_SchemePropertyCategory):
    property_name = "finite-type"

    class ParentMethods:
        def is_finite_type(self):
            return True

    def an_object(self):
        r"""The affine line, of finite type over the base ring."""
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())


class IntegralSchemes(_SchemePropertyCategory):
    property_name = "integral"

    class ParentMethods:
        def is_integral(self):
            return True

    def an_object(self):
        r"""The affine line, integral because its coordinate algebra is a domain."""
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())


class NormalSchemes(_SchemePropertyCategory):
    property_name = "normal"

    class ParentMethods:
        def is_normal(self):
            return True

    def an_object(self):
        r"""The affine line, normal because its coordinate algebra is."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return AffineSpace(1, self.base_ring())


class SmoothSchemes(_SchemePropertyCategory):
    property_name = "smooth"

    class ParentMethods:
        def is_smooth(self):
            return True

    def an_object(self):
        r"""The affine line, which is smooth over the base ring."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return AffineSpace(1, self.base_ring())


class AffineSchemes(_SchemePropertyCategory):
    property_name = "affine"

    def an_object(self):
        r"""The affine line over the base ring."""
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())

    def super_categories(self):
        # Quasi-affine as well: a scheme is an open subscheme of itself.
        return [
            Schemes(self.base_ring()),
            SeparatedSchemes(self.base_ring()),
            QuasiAffineSchemes(self.base_ring()),
        ]

    class ParentMethods:
        def is_affine(self):
            return True

        def coordinate_algebra(self):
            selected = getattr(self, "_preamble_coordinate_algebra", None)
            if selected is not None:
                return selected
            engine = getattr(self, "_preamble_engine_coordinate_ring", None)
            if engine is None:
                # Some native Sage point Homsets construct a fresh generic
                # affine scheme internally.  Read its coordinate ring through
                # the concrete Sage implementation, never through the public
                # overridden ``coordinate_ring`` method.
                engine = _SageAffineScheme.coordinate_ring(self)
                self._preamble_engine_coordinate_ring = engine
            base = self.scheme_base_ring()
            labels = tuple(getattr(engine, "variable_names", lambda: ())()) or None
            selected = refine_commutative_algebra(_own_ring(engine), base, labels)
            self._preamble_coordinate_algebra = selected
            return selected

        def coordinate_ring(self):
            r"""Return the owned coordinate ring/algebra of this affine scheme."""
            return self.coordinate_algebra()

        def closed_subscheme(self, *equations):

            equations = (
                tuple(equations[0])
                if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                else tuple(equations)
            )
            algebra = self.coordinate_algebra()
            quotient = FinitelyPresentedAlgebra(algebra, equations)
            subscheme = Spec(quotient)
            spec_inclusion = affine_spec_morphism(
                quotient.algebra_presentation_morphism()
            )
            inclusion = categorical_scheme_morphism(
                spec_inclusion.native_morphism(),
                domain=subscheme,
                codomain=self,
            )
            inclusion._preamble_coordinate_algebra_morphism = (
                quotient.algebra_presentation_morphism()
            )
            subscheme._preamble_inclusion = inclusion
            return refine_closed_subscheme(
                subscheme,
                self,
                defining_equations=equations,
            )

        def distinguished_open(self, element):
            r"""Return \(D(f)\subseteq X\), the open locus where ``element`` is a unit.

            \(D(f)=\operatorname{Spec}A[1/f]\), and the localization map
            \(A\to A[1/f]\) induces the open immersion.
            """
            from dzack_research.preamble.categories.rings.commutative_algebra import Localization

            localized = Localization(self.coordinate_algebra(), element)
            localization_map = localized.localization_map()
            spec_inclusion = affine_spec_morphism(localization_map)
            open_subscheme = spec_inclusion.domain()
            inclusion = categorical_scheme_morphism(
                spec_inclusion.native_morphism(),
                domain=open_subscheme,
                codomain=self,
            )
            inclusion._preamble_coordinate_algebra_morphism = localization_map
            open_subscheme._preamble_inclusion = inclusion
            base = self.scheme_base_ring()
            return refine_scheme(open_subscheme, base, [OpenImmersions(self)])


class QuasiAffineSchemes(_SchemePropertyCategory):
    property_name = "quasi-affine"

    def an_object(self):
        r"""The affine line, which is affine."""
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())

    def super_categories(self):
        return [Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]

    class ParentMethods:
        def is_quasi_affine(self):
            return True


class QuasiProjectiveSchemes(_SchemePropertyCategory):
    property_name = "quasi-projective"

    def an_object(self):
        r"""The projective line, which is projective."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return ProjectiveSpace(1, self.base_ring())

    def super_categories(self):
        return [Schemes(self.base_ring()), SeparatedSchemes(self.base_ring())]

    class ParentMethods:
        def is_quasi_projective(self):
            return True


class ProjectiveSchemes(_SchemePropertyCategory):
    property_name = "projective"

    def an_object(self):
        r"""The projective line."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return ProjectiveSpace(1, self.base_ring())

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
            equations = (
                tuple(equations[0])
                if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                else tuple(equations)
            )
            return refine_closed_subscheme(self.subscheme(equations), self)


class AffineSpaces(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The affine line over the base ring."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return AffineSpace(1, self.base_ring())

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
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = refine_ring_constructions(PolynomialRing(rationals, "T"))
            rational_functions = refine_commutative_algebra(
                polynomial.fraction_field(), rationals, ("T",)
            )
            T = rational_functions.algebra_generator("T")
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return 1 / (1 - q**d * T)


class ProjectiveSpaces(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The projective line over the base ring."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return ProjectiveSpace(1, self.base_ring())

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
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.misc.misc_c import prod
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = refine_ring_constructions(PolynomialRing(rationals, "T"))
            rational_functions = refine_commutative_algebra(
                polynomial.fraction_field(), rationals, ("T",)
            )
            T = rational_functions.algebra_generator("T")
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return prod(1 / (1 - q**i * T) for i in range(d + 1))


class ProductSchemes(OwnedCategoryOverBaseRing):
    r"""Scheme products equipped with their stated factors and projections."""

    def an_object(self):
        r"""The affine plane as a product of two affine lines."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        ring = self.base_ring()
        return scheme_product(AffineSpace(1, ring), AffineSpace(1, ring))

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
            r"""Return the family of factors, indexed by the product's own index set."""

            return _finite_factor_family(self._preamble_product_factors, name="Product factors")

        def number_of_factors(self):
            return self.factors().cardinality()

        def projection(self, index):
            return self._preamble_product_projections[index]

        def projections(self):
            return tuple(
                self.projection(index) for index in range(self.number_of_factors())
            )


class ProductProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Finite products of projective spaces over one base ring."""

    def an_object(self):
        r"""The product of two projective lines."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        ring = self.base_ring()
        return scheme_product(ProjectiveSpace(1, ring), ProjectiveSpace(1, ring))

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
        return bool(_engine_ring(base_ring).is_integral_domain())
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return False


@cached_function
def Spec(ring_or_algebra):
    r"""Return the affine scheme ``Spec(A)`` over the represented scalar base.

    If ``A`` is an owned commutative ``R``-algebra, the returned object lies in
    ``Schemes(R)`` and its structure morphism is induced contravariantly by
    ``R -> A``.  A bare commutative ring ``R`` is read as an ``R``-algebra over
    itself, so ``Spec(R)`` remains the terminal affine ``R``-scheme.
    """
    algebra = _own_ring(ring_or_algebra)
    try:
        base = algebra.algebra_base_ring()
    except AttributeError:
        base = algebra
    base = _own_ring(base)

    scheme = _SageSpec(_engine_ring(algebra))
    categories = [AffineSchemes(base)]

    if algebra is base or algebra in FramedAlgebras(base):
        categories.append(FiniteTypeSchemes(base))
    if algebra is base:
        categories.append(SmoothSchemes(base))
    if _integral_placement(algebra):
        categories.append(IntegralSchemes(base))
    refine_scheme(scheme, base, categories)
    scheme._preamble_engine_coordinate_ring = _engine_ring(algebra)
    scheme._preamble_coordinate_algebra = algebra
    engine_identity = _engine_ring(algebra).hom(_engine_ring(algebra))
    scheme._preamble_identity_morphism = refine_scheme_morphism(
        _native_scheme_homset(scheme, scheme)(engine_identity, check=False), base
    )
    if algebra is base:

        coordinate_identity = ring_homset(base, base).identity()
    else:
        coordinate_identity = algebra.Mor(algebra).identity()
    scheme._preamble_identity_morphism._preamble_coordinate_algebra_morphism = (
        coordinate_identity
    )

    if algebra is base:
        scheme._preamble_structure_morphism = scheme._preamble_identity_morphism
    else:
        base_scheme = Spec(base)
        engine_map = _engine_ring(algebra).coerce_map_from(_engine_ring(base))
        if engine_map is None:
            raise NotImplementedError(
                "the affine Spec structure morphism currently requires an exact engine realization of the algebra structure map"
            )
        native = _native_scheme_homset(scheme, base_scheme)(engine_map, check=False)
        scheme._preamble_structure_morphism = refine_scheme_morphism(native, base)
        scheme._preamble_structure_morphism._preamble_coordinate_algebra_morphism = (
            algebra.algebra_structure_morphism()
        )
    return scheme


def affine_spec_morphism(algebra_morphism):
    r"""Return the affine scheme morphism contravariantly induced by an algebra map."""

    source_algebra = algebra_morphism.domain()
    target_algebra = algebra_morphism.codomain()
    ring = source_algebra.base_ring()
    if source_algebra not in Algebras(ring) or target_algebra not in Algebras(ring):
        raise TypeError("affine Spec acts on a represented algebra morphism")
    if source_algebra.base_ring() is not target_algebra.base_ring():
        raise ValueError("affine Spec requires an algebra morphism over one scalar base")
    source_scheme = Spec(target_algebra)
    target_scheme = Spec(source_algebra)
    native = _native_scheme_homset(source_scheme, target_scheme)(
        _engine_algebra_morphism(algebra_morphism), check=False
    )
    morphism = refine_scheme_morphism(native, source_algebra.base_ring())
    morphism._preamble_coordinate_algebra_morphism = algebra_morphism
    return morphism


def AffineSpace(dimension, base_ring, names=None):
    r"""Return the owned affine space ``A^n_R``."""
    base = _own_ring(base_ring)
    engine_dimension = int(_engine_numeral(SageZZ, dimension))
    if names is None:
        scheme = _SageAffineSpace(engine_dimension, _engine_ring(base))
    else:
        scheme = _SageAffineSpace(engine_dimension, _engine_ring(base), names=names)
    engine_coordinate_ring = getattr(
        scheme, "_preamble_engine_coordinate_ring", None
    )
    if engine_coordinate_ring is None:
        engine_coordinate_ring = scheme.coordinate_ring()
    categories = [AffineSpaces(base)]
    if _integral_placement(base):
        categories.append(IntegralSchemes(base))
    refine_scheme(scheme, base, categories)

    labels = tuple(engine_coordinate_ring.variable_names())
    scheme._preamble_engine_coordinate_ring = engine_coordinate_ring
    scheme._preamble_coordinate_algebra = refine_commutative_algebra(
        _own_ring(engine_coordinate_ring),
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )
    scheme._preamble_identity_morphism = refine_scheme_morphism(
        _native_scheme_homset(scheme, scheme)(list(engine_coordinate_ring.gens()), check=False), base
    )
    scheme._preamble_identity_morphism._preamble_coordinate_algebra_morphism = (
        scheme.coordinate_algebra().Mor(scheme.coordinate_algebra()).identity()
    )
    base_scheme = Spec(base)
    engine_map = engine_coordinate_ring.coerce_map_from(_engine_ring(base))
    if engine_map is None:
        raise NotImplementedError(
            "the affine-space structure morphism requires the scalar base injection"
        )
    scheme._preamble_structure_morphism = refine_scheme_morphism(
        _native_scheme_homset(scheme, base_scheme)(engine_map, check=False), base
    )
    scheme._preamble_structure_morphism._preamble_coordinate_algebra_morphism = (
        scheme.coordinate_algebra().algebra_structure_morphism()
    )
    return scheme


def ProjectiveSpace(dimension, base_ring, names=None):
    r"""Return the owned projective space ``P^n_R``."""
    base = _own_ring(base_ring)
    engine_dimension = int(_engine_numeral(SageZZ, dimension))
    if names is None:
        scheme = _SageProjectiveSpace(engine_dimension, _engine_ring(base))
    else:
        scheme = _SageProjectiveSpace(engine_dimension, _engine_ring(base), names=names)
    categories = [ProjectiveSpaces(base)]
    if _integral_placement(base):
        categories.append(IntegralSchemes(base))
    return refine_scheme(scheme, base, categories)


def _product_projection(product, factor, coordinates):
    native = _native_scheme_homset(product, factor)(list(coordinates), check=False)
    projection = categorical_scheme_morphism(native)
    if (
        product in AffineSchemes(product.scheme_base_ring())
        and factor in AffineSchemes(factor.scheme_base_ring())
    ):
        target = product.coordinate_algebra()
        source = factor.coordinate_algebra()
        engine_target = _engine_ring(target)
        owned_coordinates = tuple(
            target._from_engine_element(engine_target(coordinate))
            for coordinate in coordinates
        )
        projection._preamble_coordinate_algebra_morphism = source.Mor(target)(
            {
                label: image
                for label, image in zip(
                    source.algebra_generating_set(),
                    owned_coordinates,
                    strict=True,
                )
            }
        )
    return projection


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
        coordinates = tuple(product._preamble_engine_coordinate_ring.gens())
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
    elif all(scheme in AffineSchemes(base) for scheme in schemes):
        algebras = tuple(scheme.coordinate_algebra() for scheme in schemes)
        algebra = Coproduct(algebras[0], algebras[1])
        factor_maps = list(algebra.coproduct_injections())
        for next_algebra in algebras[2:]:
            new_algebra = Coproduct(algebra, next_algebra)
            left_map, right_map = new_algebra.coproduct_injections()
            factor_maps = [left_map * factor_map for factor_map in factor_maps] + [
                right_map
            ]
            algebra = new_algebra
        product = Spec(algebra)
        projections = [affine_spec_morphism(factor_map) for factor_map in factor_maps]
        refine_scheme(product, base, [ProductSchemes(base)])
    else:
        raise NotImplementedError(
            "mixed affine/projective scheme products are not yet represented"
        )

    product._preamble_product_factors = tuple(schemes)
    product._preamble_product_projections = tuple(projections)
    return product


class FiberProductSchemes(OwnedCategoryOverBaseRing):
    r"""Affine schemes equipped as selected pullbacks of one cospan."""

    def an_object(self):
        r"""``A^1 \times_{Spec R} A^1``, the affine plane as a fiber product."""
        line = AffineSpace(1, self.base_ring())
        return scheme_fiber_product(line.structure_morphism(), line.structure_morphism())

    def super_categories(self):
        return [AffineSchemes(self.base_ring())]

    class ParentMethods:
        def fiber_product_cospan(self):
            return self._preamble_fiber_product_cospan

        def fiber_product_base(self):
            return self.fiber_product_cospan()[0].codomain()

        def fiber_product_projections(self):
            return self._preamble_fiber_product_projections

        def left_projection(self):
            return self.fiber_product_projections()[0]

        def right_projection(self):
            return self.fiber_product_projections()[1]

        def from_pullback_cone(self, left_map, right_map):
            r"""Return the unique represented map into this affine fiber product."""
            if left_map.domain() is not right_map.domain():
                raise ValueError("a pullback cone requires one common source")
            left_projection, right_projection = self.fiber_product_projections()
            if left_map.codomain() is not left_projection.codomain():
                raise ValueError("the left pullback-cone map has the wrong codomain")
            if right_map.codomain() is not right_projection.codomain():
                raise ValueError("the right pullback-cone map has the wrong codomain")
            algebra_pushout = self._preamble_fiber_product_algebra_pushout
            induced = algebra_pushout.from_pushout_cocone(
                left_map.coordinate_algebra_morphism(),
                right_map.coordinate_algebra_morphism(),
            )
            return affine_spec_morphism(induced)


def scheme_fiber_product(left_map, right_map):
    r"""Return ``X x_S Y`` for two represented affine scheme maps to ``S``."""
    if not isinstance(left_map, SchemeMorphism) or not isinstance(
        right_map, SchemeMorphism
    ):
        raise TypeError("a represented scheme fiber product is specified by scheme morphisms")
    if left_map.codomain() is not right_map.codomain():
        raise ValueError("fiber-product maps require one common codomain")

    left = left_map.domain()
    right = right_map.domain()
    base_scheme = left_map.codomain()
    base_ring = left.scheme_base_ring()
    affine = AffineSchemes(base_ring)
    if left not in affine or right not in affine or base_scheme not in affine:
        raise NotImplementedError(
            "the active scheme fiber-product backend currently requires affine schemes"
        )


    algebra_pushout = Pushout(
        left_map.coordinate_algebra_morphism(),
        right_map.coordinate_algebra_morphism(),
    )
    product = Spec(algebra_pushout)
    left_projection = affine_spec_morphism(algebra_pushout.left_pushout_map())
    right_projection = affine_spec_morphism(algebra_pushout.right_pushout_map())
    product._preamble_fiber_product_cospan = (left_map, right_map)
    product._preamble_fiber_product_algebra_pushout = algebra_pushout
    product._preamble_fiber_product_projections = (
        left_projection,
        right_projection,
    )
    return refine_scheme(product, base_ring, [FiberProductSchemes(base_ring)])

class _SchemeSubobjectsOf(OwnedParameterizedCategory):
    r"""Subobjects of one scheme, by the kind of immersion they carry."""

    def ambient_scheme(self):
        r"""Return the scheme these subobjects are subobjects of."""
        return self.base()

    def _repr_object_names(self) -> str:
        return f"{self.immersion_name} into {self.ambient_scheme()}"

    def super_categories(self):
        ambient = self.ambient_scheme()
        return [Subobjects(ambient, Schemes(ambient.scheme_base_ring()))]

    class ParentMethods:
        def inclusion(self):
            r"""Return the chosen monomorphism representing this subobject."""
            return self._preamble_inclusion

        def ambient_scheme(self):
            r"""Return the ambient scheme: the codomain of the inclusion."""
            return self.inclusion().codomain()


class ClosedEmbeddings(_SchemeSubobjectsOf):
    r"""Subobjects of ``X`` whose inclusion is a closed immersion.

    For affine \(X=\operatorname{Spec}A\) this is
    \(\operatorname{Spec}(A/I)\hookrightarrow X\), induced by the quotient
    \(A\twoheadrightarrow A/I\).  Every closed subscheme of \(X\) arises this
    way from a unique ideal \(I\), so no further subclass exists to name; a
    chosen finite generating set of \(I\) presents the coordinate algebra and
    is stated on that algebra.
    """

    immersion_name = "closed embeddings"

    def an_object(self):
        r"""The coordinate axis, cut out of the ambient by its first coordinate."""
        ambient = self.ambient_scheme()
        first = next(iter(ambient.coordinate_algebra().algebra_generators()))
        return ambient.closed_subscheme(first)

    class ParentMethods:
        def codimension(self):
            defining = getattr(self, "_preamble_defining_ideal", None)
            ambient = self.ambient_scheme()
            if defining is not None and hasattr(ambient, "coordinate_algebra"):

                ambient_engine = _engine_ring(ambient.coordinate_algebra())
                ideal_engine = defining._engine_ideal()
                try:
                    quotient_dimension = ideal_engine.dimension()
                    ambient_dimension = ambient_engine.krull_dimension()
                except (AttributeError, NotImplementedError):
                    pass
                else:
                    return int(ambient_dimension - quotient_dimension)
            return self.ambient_scheme().dimension() - self.dimension()

        def defining_equations(self):
            r"""Return the family of equations that cut this subscheme out."""

            selected = getattr(self, "_preamble_defining_equations", None)
            if selected is not None:
                return finite_family(selected, name="Defining equations")
            return finite_family(
                self.defining_polynomials(), name="Defining equations"
            )

        def defining_ideal_owned(self):
            selected = getattr(self, "_preamble_defining_ideal", None)
            if selected is not None:
                return selected
            return self.defining_ideal()


class OpenImmersions(_SchemeSubobjectsOf):
    r"""Subobjects of ``X`` whose inclusion is an open immersion.

    The standard affine specimen is the distinguished open
    \(D(f)=\operatorname{Spec}A[1/f]\subseteq\operatorname{Spec}A\), whose
    inclusion is induced by the localization map \(A\to A[1/f]\).
    """

    immersion_name = "open immersions"

    def an_object(self):
        r"""\(D(f)\) for ``f`` the ambient's first coordinate."""
        ambient = self.ambient_scheme()
        first = next(iter(ambient.coordinate_algebra().algebra_generators()))
        return ambient.distinguished_open(first)


class SchemeMonomorphisms(MonoCategoryOf):
    r"""Monomorphisms of schemes.

    A closed immersion and an open immersion are monomorphisms.  Which of the
    two an inclusion is, is declared where it is constructed, and this reads
    that declaration.  Injectivity on points is neither necessary nor
    sufficient for a scheme monomorphism, so the inherited test does not apply.
    """

    def accepts(self, arrow) -> bool:
        ambient = arrow.codomain()
        source = arrow.domain()
        return source in ClosedEmbeddings(ambient) or source in OpenImmersions(ambient)


def refine_closed_subscheme(
    subscheme,
    ambient=None,
    *,
    defining_equations=None,
):
    ambient = subscheme.ambient_space() if ambient is None else ambient
    base = ambient.scheme_base_ring()
    if defining_equations is not None:
        equations = tuple(defining_equations)
        subscheme._preamble_defining_equations = equations
        subscheme._preamble_defining_ideal = ambient.coordinate_ring().ideal(*equations)
    if getattr(subscheme, "_preamble_inclusion", None) is None:
        # The subobject is the arrow, so a route that did not build one takes
        # the native embedding, retargeted at the stated ambient.
        subscheme._preamble_inclusion = categorical_scheme_morphism(
            subscheme.embedding_morphism(),
            domain=subscheme,
            codomain=ambient,
        )
    return refine_scheme(subscheme, base, [ClosedEmbeddings(ambient)])

__all__ = [
    "AffineSchemes",
    "AffineSpace",
    "AffineSpaces",
    "ClosedEmbeddings",
    "FiberProductSchemes",
    "FiniteTypeSchemes",
    "IntegralSchemes",
    "NormalSchemes",
    "OpenImmersions",
    "ProjectiveSchemes",
    "ProjectiveSpace",
    "ProjectiveSpaces",
    "ProductProjectiveSpaces",
    "ProductSchemes",
    "QuasiAffineSchemes",
    "QuasiProjectiveSchemes",
    "SchemeMonomorphisms",
    "Schemes",
    "SchemeMorphism",
    "SeparatedSchemes",
    "SmoothSchemes",
    "Spec",
    "refine_scheme",
    "refine_scheme_morphism",
    "categorical_scheme_morphism",
    "scheme_product",
    "affine_spec_morphism",
    "refine_closed_subscheme",
    "scheme_fiber_product",
]

Schemes._MonoCategory = SchemeMonomorphisms
