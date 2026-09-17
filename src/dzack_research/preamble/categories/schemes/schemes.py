r"""Owned categories and constructors for schemes over a base ring.

Every scheme a session receives is an object of its category, built by that
category's one entry (``CON-16``) and threaded through ``Schemes(R)`` down to
the owned root.  Each level stores only the datum it introduces:

* ``Schemes(R)`` the base ring ``R`` the scheme lies over, and the private
  Sage scheme realizing it when the construction has one;
* ``Schemes(R).Affine()`` the coordinate algebra ``A`` of ``Spec A``;
* ``AffineSpaces(R)`` and ``ProjectiveSpaces(R)`` nothing beyond the chosen
  coordinates their construction put into ``A`` or into the realization;
* a subobject category ``ClosedEmbeddings(X)`` or ``OpenImmersions(X)`` the
  codomain ``X`` and the defining datum of the inclusion into it, from which
  the inclusion arrow is built once the subobject exists;
* ``ClosedEmbeddings(X)`` the family of equations cutting the subscheme out;
* ``ProductSchemes(R)`` the indexed family of factors and the defining data
  of the projections; ``FiberProductSchemes(R)`` the selected pullback
  construction.

The Sage scheme that realizes a represented scheme is a private engine
(``OWN-06``).  It is computed by the construction that knows it -- ``Spec``
of the coordinate algebra's engine, Sage's projective space on the chosen
coordinates, the Sage subscheme cut out by the equations -- and passed as
construction data.  A scheme presented without one, a glued scheme, answers
everything its data determine and asserts that frontier where a native
computation is asked of it.

Membership is placement at construction (``CAT-23``).  A scheme over ``R'``
is a scheme over ``R`` only through the restriction-of-base functor along a
ring map ``R -> R'`` (``CAT-16``), which ``_scheme_mor_category`` applies
when an arrow joins schemes over two bases of one scalar tower.
"""

from itertools import combinations
from itertools import product as cartesian_product

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings as _SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.rings.integer import Integer as SageInteger
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.affine.affine_space import AffineSpace as _SageAffineSpace
from sage.schemes.generic.algebraic_scheme import (
    AlgebraicScheme_quasi as _SageAlgebraicSchemeQuasi,
    AlgebraicScheme_subscheme as _SageAlgebraicSchemeSubscheme,
)
from sage.schemes.generic.morphism import SchemeMorphism as _SageSchemeMorphism
from sage.schemes.generic.morphism import SchemeMorphism_id as _SageSchemeMorphismIdentity
from sage.schemes.generic.morphism import (
    SchemeMorphism_polynomial as _SageSchemeMorphismPolynomial,
)
from sage.schemes.generic.morphism import SchemeMorphism_spec as _SageSchemeMorphismSpec
from sage.schemes.generic.scheme import AffineScheme as _SageAffineScheme
from sage.schemes.product_projective.space import (
    ProductProjectiveSpaces as _SageProductProjectiveSpaces,
)
from sage.schemes.projective.projective_space import (
    ProjectiveSpace as _SageProjectiveSpace,
)

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    _MonoCategoryOf,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.products import _finite_factor_family
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    _engine_algebra_morphism,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.rings.commutative_algebra import (
    QuotientRings,
    _refine_commutative_algebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedRings,
    OwnedIntegralDomains,
    OwnedPrincipalIdealDomains,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _own_ring,
    _ring_morphisms_equal,
    _proper_restriction_base_ring,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    LocallyRingedSpaces,
    LocallyRingedHomCategoryConstruction,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

for _scheme_axiom in (
    "Affine",
    "QuasiAffine",
    "Projective",
    "QuasiProjective",
    "Separated",
    "FiniteType",
    "Integral",
    "Normal",
):
    if _scheme_axiom not in all_axioms:
        all_axioms.add(_scheme_axiom)


# ---------------------------------------------------------------------------
# Private engine adapters (OWN-06).
#
# Semantic operation: realize an owned scheme, scheme morphism or polynomial
# datum in Sage's scheme library and raise the results.  Owning callers: the
# scheme categories of this module.  Upstream operations: Sage's
# ``AffineScheme``, ``AffineSpace``, ``ProjectiveSpace``,
# ``ProductProjectiveSpaces``, ``AlgebraicScheme_subscheme`` and the scheme
# Hom-sets of ``sage.schemes.generic.homset``.  Every inspection of a Sage
# scheme or Sage morphism class is one of the functions in this block.
# ---------------------------------------------------------------------------


def _engine_scheme(scheme):
    r"""The private Sage scheme ``scheme`` computes in.

    It was computed from the owned datum by the construction that built
    ``scheme`` and stored at the ``Schemes(R)`` level; a scheme presented
    without a Sage realization asserts that frontier here.
    """
    return scheme._scheme_engine()


def _is_gluing_realization(realization) -> bool:
    r"""Whether the ``scheme_engine`` of a scheme is the realization of an affine gluing datum.

    The ``Schemes(R)`` level holds one private realization: a Sage scheme, or
    ``schemes.gluing``'s realization of a scheme glued from an affine gluing
    datum (Stacks, Tag 01JA).  Which of the two it is, is a representation
    question, answered here and nowhere else.
    """
    from dzack_research.preamble.categories.schemes.gluing import _GluedScheme

    match realization:
        case _GluedScheme():
            return True
        case _:
            return False


def _native_scheme_homset(domain, codomain):
    r"""Sage's scheme Hom between the engines of two owned schemes."""
    return _engine_scheme(domain)._Hom_(_engine_scheme(codomain))


def _engine_defining_polynomials(native):
    r"""The coordinate polynomials of a Sage polynomial scheme morphism.

    Sage represents a morphism between affine or projective spaces by the
    polynomials giving its coordinates, and the identity as its own class
    carrying none; both are read here.
    """
    match native:
        case _SageSchemeMorphismIdentity():
            return tuple(native.domain().coordinate_ring().gens())
        case _SageSchemeMorphismPolynomial():
            return tuple(native.defining_polynomials())
        case _:
            assert False, (
                f"{native} is not represented by coordinate polynomials, so it has no "
                "homogeneous coordinate data to read"
            )


def _engine_coordinate_pullback_of(native, domain_algebra, codomain_algebra):
    r"""The owned pullback ``O(Y) -> O(X)`` of a Sage morphism ``X -> Y`` of affine engines.

    A morphism of affine schemes is its pullback on coordinate algebras.  Sage
    spells that map three ways: the identity, ``Spec`` of a ring morphism, and
    a polynomial map between affine spaces, whose pullback sends the
    coordinate of the target to the polynomial giving it.
    """
    match native:
        case _SageSchemeMorphismIdentity():
            return codomain_algebra.Mor(domain_algebra).identity()
        case _SageSchemeMorphismSpec():
            return codomain_algebra.Mor(domain_algebra)(native.ring_homomorphism())
        case _SageSchemeMorphismPolynomial():
            return codomain_algebra.Mor(domain_algebra)(
                _engine_ring(codomain_algebra).hom(
                    list(native.defining_polynomials()),
                    _engine_ring(domain_algebra),
                )
            )
        case _:
            assert False, (
                f"{native} is not a Sage morphism of affine schemes with a readable pullback"
            )


def _engine_polynomial_algebra(engine_polynomial_ring, base):
    r"""The owned polynomial algebra over ``base`` whose engine is a Sage polynomial ring.

    Affine and projective spaces present their coordinates through Sage's
    polynomial rings; this is the one place such a ring is raised to the owned
    free, graded free and symmetric algebra it is.
    """
    return _refine_commutative_algebra(
        _own_ring(engine_polynomial_ring),
        base,
        tuple(engine_polynomial_ring.variable_names()),
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )


def _engine_affine_spectrum(algebra, base):
    r"""Sage's ``Spec A`` over ``Spec R`` for the engines of ``A`` and ``R``."""
    return _SageAffineScheme(_engine_ring(algebra), _engine_ring(base))


def _engine_coercion_agreeing_on(pullback, determining):
    r"""The canonical Sage coercion realizing ``pullback``, checked on a determining family.

    Agreement on a family on which two maps out of the source already agree is
    agreement everywhere, so the coercion is an admissible realization exactly
    when it exists and matches the owned morphism there.
    """
    source = pullback.domain()
    target = pullback.codomain()
    engine_morphism = _engine_ring(target).coerce_map_from(_engine_ring(source))
    assert engine_morphism is not None, (
        f"no Sage coercion realizes the pullback {pullback}; its source has no chosen "
        "finite algebra framing from which to rebuild one"
    )
    assert all(
        engine_morphism(_engine_element(source, value)) == _engine_element(target, pullback(value))
        for value in determining
    ), f"the Sage coercion between the engines of {source} and {target} is not {pullback}"
    return engine_morphism


def _engine_coordinate_pullback(pullback):
    r"""The private Sage ring map realizing one coordinate pullback.

    A framed source rebuilds the native map from the images of its algebra
    generators through the algebra bridge.  A localization has no algebra
    generating family, and a map out of ``S^{-1}A`` is determined by its
    restriction along ``A -> S^{-1}A``, so its realization is the canonical
    coercion checked on the family of the framed algebra at the foot of the
    localization tower.  Any other source supplies the realization its ring
    morphism selected when it was built.
    """
    source = pullback.domain()
    base = source.base_ring()
    # Declared engine adapter: a selected native ring map includes its own
    # coefficient map, which rebuilding an R-algebra map would erase.
    native = getattr(pullback, "_engine_morphism", None)
    if native is not None:
        return native
    match source:
        case _ if source in LocalizationRings():
            determining = _elements_determining_maps_out_of(source, base)
            assert determining is not None, (
                f"no finite family determines maps out of the localization {source}"
            )
            return _engine_coercion_agreeing_on(pullback, determining)
        case _ if source in FramedAlgebras(base):
            return _engine_algebra_morphism(pullback)
        case _:
            from dzack_research.preamble.categories.functors.algebra_scalar_change import _engine_ring_map

            return _engine_ring_map(pullback)


def _polynomial_exponents(exponent, variable_count: int) -> tuple[int, ...]:
    r"""Normalize a Sage polynomial dictionary exponent to one exponent per variable.

    Sage keys a univariate polynomial's dictionary by an integer and a
    multivariate one by an exponent tuple; both are read here.
    """
    match exponent:
        case int() | SageInteger():
            assert variable_count == 1, "an integer exponent keys a univariate polynomial"
            return (int(exponent),)
        case _:
            return tuple(int(value) for value in exponent)


def _copy_polynomial_by_exponents(polynomial, target_ring, target_variables):
    r"""Copy a Sage polynomial onto name-independent variables by its exponent dictionary."""
    source = polynomial.parent()
    variable_count = len(source.gens())
    assert len(target_variables) == variable_count, (
        "polynomial transport requires the same number of variables"
    )
    result = target_ring.zero()
    for exponent, coefficient in polynomial.dict().items():
        term = target_ring(coefficient)
        for variable, power in zip(target_variables, _polynomial_exponents(exponent, variable_count), strict=True):
            term *= variable**power
        result += term
    return result


def _evaluate_owned_homogeneous_polynomial_on_coordinates(
    polynomial,
    polynomial_ring,
    coordinates,
    *,
    coefficient_map=None,
):
    r"""Evaluate one owned homogeneous polynomial on an owned coordinate family.

    The scalar coefficients are carried into the ring of the coordinates by
    its algebra structure morphism, so the substitution is an ``R``-algebra
    map and never reads a coefficient off the target engine.
    """
    polynomial = polynomial_ring(polynomial)
    labels = tuple(polynomial_ring.algebra_generating_set())
    coordinates = tuple(coordinates)
    assert len(coordinates) == len(labels), (
        "homogeneous substitution needs one coordinate per target variable"
    )
    source_ring = coordinates[0].parent()
    assert all(coordinate.parent() is source_ring for coordinate in coordinates), (
        "projective homogeneous coordinates lie in one source ring"
    )
    base = polynomial_ring.base_ring()
    scalar_map = _restriction_to_base(source_ring, base) if coefficient_map is None else coefficient_map
    assert scalar_map.domain() is base and scalar_map.codomain() is source_ring, (
        "polynomial substitution retains the stated map on coefficients"
    )
    engine = _engine_ring(polynomial_ring)
    engine_base = _engine_ring(base)
    backend = engine(_engine_element(polynomial_ring, polynomial))
    result = source_ring.zero()
    for exponent, coefficient in backend.monomial_coefficients().items():
        powers = _polynomial_exponents(exponent, len(labels))
        term = scalar_map(base._from_engine_element(engine_base(coefficient)))
        for coordinate, power in zip(coordinates, powers, strict=True):
            term *= coordinate**power
        result += term
    return source_ring(result)


def _evaluate_polynomial_in_algebra(polynomial, algebra):
    r"""Evaluate an engine polynomial on the chosen algebra generators of ``algebra``."""
    labels = tuple(algebra.algebra_generating_set())
    source = polynomial.parent()
    assert len(source.gens()) == len(labels), (
        "the polynomial certificate has the wrong number of invariant variables"
    )
    base = algebra.base_ring()
    engine_base = _engine_ring(base)
    structure = algebra.algebra_structure_morphism()
    result = algebra.zero()
    for exponent, coefficient in polynomial.dict().items():
        powers = _polynomial_exponents(exponent, len(labels))
        term = structure(base._from_engine_element(engine_base(coefficient)))
        for label, power in zip(labels, powers, strict=True):
            term *= algebra.algebra_generator(label) ** power
        result += term
    return algebra(result)


# ---------------------------------------------------------------------------
# Maps out of algebras: the finite families on which two maps already agree.
# ---------------------------------------------------------------------------


def _localization_refines(finer, coarser) -> bool:
    r"""Whether every element ``coarser`` inverts is a unit in ``finer``.

    Both are localizations of one ring, so this is exactly the condition under
    which the canonical map ``coarser -> finer`` exists.
    """
    unit = finer.localization_map()
    return all(
        unit(generator).is_unit()
        for generator in coarser.localization_submonoid().monoid_generators()
    )


def _elements_determining_maps_out_of(algebra, base):
    r"""Elements of ``algebra`` on which two base-ring maps out of it already agree.

    A map out of a framed ``R``-algebra is fixed by the images of its algebra
    generators together with its restriction to ``R``.  When the represented
    scheme base is a smaller ring ``k``, that restriction is determined
    recursively by a finite family for ``R/k``, carried into the algebra by its
    structure morphism.  A map out of ``S^{-1}A`` is fixed by its restriction
    along ``A -> S^{-1}A``, so localization towers recurse to the framed
    algebra at their foot.  ``None`` states that no represented finite
    determining family is available.
    """
    if algebra is base:
        return ()
    match algebra:
        case _ if algebra in FramedAlgebras(algebra.base_ring()):
            algebra_base = algebra.base_ring()
            labels = algebra.algebra_generating_set()
            if not labels.cardinality().is_finite():
                return None
            generators = tuple(algebra.algebra_generator(label) for label in labels)
            if algebra_base is base:
                return generators
            scalar_generators = _elements_determining_maps_out_of(algebra_base, base)
            if scalar_generators is None:
                return None
            structure = algebra.algebra_structure_morphism()
            return generators + tuple(structure(element) for element in scalar_generators)
        case _ if algebra in LocalizationRings():
            if base in LocalizationRings():
                if algebra.localization_source() is base:
                    return ()
                if algebra.localization_source() is base.localization_source() and _localization_refines(algebra, base):
                    return ()
            below = _elements_determining_maps_out_of(algebra.localization_source(), base)
            if below is None:
                return None
            localization_map = algebra.localization_map()
            return tuple(localization_map(element) for element in below)
        case _:
            return None


def _algebra_generator_label(algebra, generator):
    r"""The label of an element that is one of the algebra's chosen generators."""
    label = next(
        (label for label in algebra.algebra_generating_set() if algebra.algebra_generator(label) == generator),
        None,
    )
    assert label is not None, f"{generator} is not a chosen algebra generator of {algebra}"
    return label


# ---------------------------------------------------------------------------
# Morphisms of schemes.
# ---------------------------------------------------------------------------


class SchemeConeMorphismConstruction:
    r"""The selected universal-cone target and legs defining an induced map.

    A map into a product or a fibre product is the factorization of a cone
    through its universal cone; the target and the legs are that cone, and
    composing the factorization with a projection returns the leg.
    """

    def __init__(self, target, legs, projections) -> None:
        self._target = target
        self._legs = legs
        self._projection_legs = tuple(zip(projections, legs, strict=True))

    def target(self):
        return self._target

    def legs(self):
        return self._legs

    def leg_of_projection(self, projection):
        r"""The leg of this particular universal cone at ``projection``.

        One scheme may carry both a product and a pullback construction.
        The projections, not its category membership, select the cone.
        """
        return next((leg for arrow, leg in self._projection_legs if arrow is projection), None)

    def image_of(self, image):
        r"""Return ``image`` retaining this cone as the datum it was induced by."""
        return image.with_cone_construction(self)


class SchemeMorphism(Morphism):
    r"""A morphism of owned schemes, an element of the owned Hom of its endpoints.

    The defining datum is one of: the coordinate pullback ``O(Y) -> O(X)``
    between affine endpoints; homogeneous coordinates into a projective space
    (:class:`_ProjectiveCoordinateMorphism`); or a native Sage morphism
    between the engines of the endpoints.  The endpoints are always the owned
    schemes of the Hom, never read off the engine.  A morphism induced by a
    universal cone additionally retains that cone.

    Protected contract, used only by composition and equality inside this
    class family: :meth:`_represented_coordinate_pullback` returns the
    pullback datum or ``None``, and :meth:`_represented_point_coordinates`
    the selected point coordinates or ``None``.
    """

    _native_morphism = None
    _coordinate_pullback = None
    _cone_construction = None
    _point_coordinates = None

    def __init__(
        self,
        native_morphism,
        *,
        homset,
        pullback=None,
        cone_construction=None,
        point_coordinates=None,
    ) -> None:
        self._native_morphism = native_morphism
        self._coordinate_pullback = pullback
        self._cone_construction = cone_construction
        self._point_coordinates = point_coordinates
        Morphism.__init__(self, homset)

    def with_cone_construction(self, construction):
        r"""This morphism, retaining the universal cone it was induced by."""
        return SchemeMorphism(
            self._native_morphism,
            homset=self.parent(),
            pullback=self._coordinate_pullback,
            cone_construction=construction,
            point_coordinates=self._point_coordinates,
        )

    def cone_construction(self):
        r"""Return the selected universal-cone datum defining this map, or ``None``."""
        return self._cone_construction

    def _in_homset(self, homset):
        r"""Re-site this representation in a Hom with the same endpoints.

        Protected arrow-engine contract of ``SchemeMorCategory``.  Its
        constructor checks endpoints and any added scalar condition first;
        a representation without a native morphism supplies its own copy of
        the same defining data.  In particular chart maps never need a native
        realization merely to forget the relative-base condition.
        """
        return SchemeMorphism(
            self.native_morphism(), homset=homset,
            cone_construction=self.cone_construction(),
            point_coordinates=self._represented_point_coordinates(),
        )

    def _represented_coordinate_pullback(self):
        return self._coordinate_pullback

    def _represented_point_coordinates(self):
        return self._point_coordinates

    def native_morphism(self):
        r"""The Sage morphism between the engines this morphism computes in."""
        assert self._native_morphism is not None, (
            f"{self} is represented by its owned datum and selected no native Sage realization"
        )
        return self._native_morphism

    def point_coordinates(self):
        r"""Return the selected owned coordinate family of this represented point."""
        assert self._point_coordinates is not None, (
            "this scheme morphism was not constructed from selected point coordinates"
        )
        return self._point_coordinates

    def _call_(self, point):
        r"""Evaluate at a point ``T -> X`` of the domain: the composite ``T -> Y``."""
        return self.compose(point)

    def _projected_cone_leg(self, before):
        r"""Reduce a projection after the factorization through its own cone."""
        construction = before.cone_construction()
        if construction is not None and construction.target() is self.domain():
            return construction.leg_of_projection(self)
        return None

    def __mul__(self, other):
        r"""``self o other``, composition of scheme morphisms.

        The identity is a two-sided unit; ``Spec R`` is terminal in ``Sch/R``,
        so a composite landing there is the structure morphism of its domain;
        a projection composed with a cone factorization is the leg.  Otherwise
        affine composites compose their pullbacks and the remaining ones
        compose their realizations.
        """
        assert other.codomain() is self.domain(), (
            f"{self} and {other} are not composable: the codomain of the second is not the domain of the first"
        )
        if self._is_the_identity():
            return other
        if other._is_the_identity():
            return self
        relative = Schemes(self.codomain().scheme_base_ring())
        if (
            self.parent().homset_category().is_subcategory(relative)
            and other.parent().homset_category().is_subcategory(relative)
            and self.codomain() is other.domain().base_scheme()
        ):
            return other.domain().structure_morphism()

        cone_leg = self._projected_cone_leg(other)
        if cone_leg is not None:
            return cone_leg

        homset = _scheme_composition_hom(self, other)
        left_pullback = self._represented_coordinate_pullback()
        right_pullback = other._represented_coordinate_pullback()
        if left_pullback is not None and right_pullback is not None:
            return homset(right_pullback * left_pullback)
        if (left_pullback is not None
                and other.codomain() is other.domain().base_scheme()
                and other.parent().homset_category().is_subcategory(Schemes(other.domain().scheme_base_ring()))):
            return _ScalarStructureSchemeMorphism(homset, left_pullback)
        structured = other._postcompose_with(self)
        if structured is not None:
            return structured
        return SchemeMorphism(self.native_morphism() * other.native_morphism(), homset=homset)

    def _is_the_identity(self) -> bool:
        r"""Whether this morphism is its Hom object's selected identity."""
        return self.domain() is self.codomain() and self is self.parent().identity()

    def _postcompose_with(self, after):
        r"""``after o self`` for a representation with its own composite, else ``None``."""
        return None

    def compose(self, before):
        return self * before

    def then(self, after):
        return after * self

    def evaluate_at(self, point):
        r"""The image of a represented point under this morphism.

        A projection out of a product of projective spaces sends a point given
        by its homogeneous coordinate blocks to the block of its factor; every
        other represented morphism composes with the point.
        """
        domain = self.domain()
        base = domain.scheme_base_ring()
        coordinates = point._represented_point_coordinates()
        if domain in ProductProjectiveSpaces(base) and coordinates is not None:
            factors = domain.factors()
            values = tuple(coordinates)
            offset = 0
            for label in factors.index_set():
                width = int(factors[label].relative_dimension()) + 1
                block = values[offset : offset + width]
                offset += width
                if self is domain.projection(label):
                    return factors[label].point_morphism(block)
        return self * point

    def coordinate_algebra_morphism(self):
        r"""``f^#: O(Y) -> O(X)``, the pullback representing a morphism of affine schemes."""
        pullback = self._represented_coordinate_pullback()
        assert pullback is not None, (
            "a coordinate pullback represents a morphism between affine schemes; "
            f"{self} has an endpoint that is not affine, so it carries none"
        )
        return pullback

    pullback_on_coordinate_algebras = coordinate_algebra_morphism

    @cached_method
    def graph_morphism(self):
        r"""``Gamma_f = (id, f): X -> X x_S Y``."""
        identity = self.domain().categorical_identity_morphism()
        return _scheme_product(self.domain(), self.codomain()).from_product_cone((identity, self))

    @cached_method
    def graph_subscheme(self):
        r"""The closed subscheme ``Gamma_f <= X x_S Y`` cut out by ``1 tensor b - f^#(b) tensor 1``.

        The graph is the inverse image of the diagonal of ``Y`` under
        ``f x id``, so it is closed whenever ``Y`` is separated; affine ``Y``
        is.  The graph morphism factors through it as an isomorphism.
        """
        base = self.codomain().scheme_base_ring()
        assert self.codomain() in Schemes(base).Affine(), "the graph is represented as a closed subscheme for affine targets"
        product = _scheme_product(self.domain(), self.codomain())
        to_domain = product.projection(0).coordinate_algebra_morphism()
        to_codomain = product.projection(1).coordinate_algebra_morphism()
        pullback = self.coordinate_algebra_morphism()
        algebra = self.codomain().coordinate_algebra()
        equations = tuple(
            to_codomain(algebra.algebra_generator(label)) - to_domain(pullback(algebra.algebra_generator(label)))
            for label in algebra.algebra_generating_set()
        )
        return product.closed_subscheme(equations)

    def base_change(self, ring_map):
        r"""``f_{R'}: X_{R'} -> Y_{R'}``, the morphism the base-change functor induces.

        The square with the two projections commutes, so an automorphism of
        ``X`` over ``R`` becomes an automorphism of ``X_{R'}`` over ``R'``.
        """
        return self.domain().scheme_category().base_change_functor(ring_map)(self)

    def slice_base_change_adjunction(self):
        r"""Return ``Sigma_self -| self^*`` between the two scheme slice categories."""
        from dzack_research.preamble.categories.schemes.base_change import (
            _slice_base_change_adjunction,
        )

        return _slice_base_change_adjunction(self)

    def inverse_image(self, closed_subscheme):
        r"""``f^{-1}(Z) = X x_Y Z`` as a closed subscheme of ``X``.

        For ``Z = V(I) <= Spec B`` and ``f: Spec A -> Spec B`` this is
        ``V(f^#(I) A)``.
        """
        assert closed_subscheme.inclusion().codomain() is self.codomain(), "the inverse image is taken of a closed subscheme of the codomain"
        base = self.domain().scheme_base_ring()
        assert self.domain() in Schemes(base).Affine() and self.codomain() in Schemes(base).Affine(), "the represented inverse image currently requires affine schemes"
        pullback = self.coordinate_algebra_morphism()
        equations = tuple(pullback(equation) for equation in closed_subscheme.defining_equations())
        return self.domain().closed_subscheme(equations)

    def fixed_subscheme(self):
        r"""``X^f = Eq(f, id_X)``, the fixed subscheme of an endomorphism.

        On a product of projective spaces a retained product-cone map
        ``f=(f_i)`` is fixed exactly when ``f_i(x)=pi_i(x)`` in every factor.
        Equality of two projective points is cut out by the ``2 x 2`` minors of
        their homogeneous coordinate pairs, so these minors give the
        scheme-theoretic equalizer without choosing affine charts.
        """
        assert self.domain() is self.codomain(), "a fixed subscheme is that of an endomorphism"
        domain = self.domain()
        base = domain.scheme_base_ring()
        construction = self.cone_construction()
        if (
            domain in ProductProjectiveSpaces(base)
            and construction is not None
            and construction.target() is domain
        ):
            legs = construction.legs()
            equations = []
            for label in domain.factors().index_set():
                moved_values = _engine_defining_polynomials(legs[label].native_morphism())
                fixed_values = _engine_defining_polynomials(domain.projection(label).native_morphism())
                assert len(moved_values) == len(fixed_values), (
                    "parallel projective maps expose different coordinate arities"
                )
                equations.extend(
                    moved_values[left] * fixed_values[right] - moved_values[right] * fixed_values[left]
                    for left, right in combinations(range(len(moved_values)), 2)
                )
            return domain.closed_subscheme(tuple(equations))
        return Schemes(base).equalizer(self, domain.categorical_identity_morphism())

    def _engine_pullback_with_trivial_base_map(self):
        r"""The pullback ``B -> A`` realized in the engine over one coefficient ring.

        Sage computes kernels and surjectivity of a ring map by Groebner
        elimination on its graph ideal, which it refuses for a map stated with
        a separate base map.  Both coordinate algebras here lie over one scalar
        ring, so the map is restated on the generators alone.
        """
        pullback = self.coordinate_algebra_morphism()
        source_algebra = pullback.domain()
        target_algebra = pullback.codomain()
        assert source_algebra in FramedAlgebras(source_algebra.base_ring()), "the engine realization requires a chosen algebra generating set on the codomain algebra"
        target_engine = _engine_ring(target_algebra)
        return _engine_ring(source_algebra).hom(
            [
                target_engine(_engine_element(target_algebra, pullback(source_algebra.algebra_generator(label))))
                for label in source_algebra.algebra_generating_set()
            ],
            target_engine,
        )

    @cached_method
    def scheme_theoretic_image(self):
        r"""The closed subscheme ``V(ker f^#) <= Y`` for affine ``f: Spec A -> Spec B``.

        The scheme-theoretic image is the smallest closed subscheme through
        which ``f`` factors; for affine ``f`` its ideal sheaf is the kernel of
        ``f^#`` (Stacks, Tag 01R7).  The kernel is computed by the engine's
        elimination on the graph ideal.
        """
        base = self.domain().scheme_base_ring()
        assert self.domain() in Schemes(base).Affine() and self.codomain() in Schemes(base).Affine(), "the represented scheme-theoretic image currently requires affine schemes"
        kernel = self._engine_pullback_with_trivial_base_map().kernel()
        algebra = self.codomain().coordinate_algebra()
        equations = tuple(algebra._from_engine_element(generator) for generator in kernel.gens())
        return self.codomain().closed_subscheme(equations)

    @cached_method
    def quasi_coherent_adjunction(self):
        r"""Return the affine adjunction ``f^* -| f_*`` on represented quasi-coherent sheaves."""
        from dzack_research.preamble.categories.schemes.sheaf_functors import (
            _affine_quasi_coherent_adjunction,
        )

        return _affine_quasi_coherent_adjunction(self)

    def module_pullback_functor(self):
        r"""Return ``f^* : QCoh(Y) -> QCoh(X)`` for this affine morphism."""
        return self.quasi_coherent_adjunction().pullback_functor()

    def direct_image_functor(self):
        r"""Return ``f_* : QCoh(X) -> QCoh(Y)`` for this affine morphism."""
        return self.quasi_coherent_adjunction().direct_image_functor()

    def direct_image(self, sheaf):
        r"""``f_* N~ = (Res_{f^#} N)~`` for affine ``f: Spec B -> Spec A`` (Stacks, Tag 01I8)."""
        return self.direct_image_functor().on_object(sheaf)

    def module_pullback(self, sheaf):
        r"""``f^* M~ = (M tensor_A B)~``, scalar extension along ``f^#`` (Stacks, Tag 01I8).

        This is the pullback of quasi-coherent modules, ``O_X tensor f^{-1}O_Y
        f^{-1} M~``; the inverse-image sheaf ``f^{-1} M~`` itself is not
        quasi-coherent and is not represented here.
        """
        return self.module_pullback_functor().on_object(sheaf)

    def inverse_image_sheaf(self, sheaf):
        r"""``f^{-1} F``, the topological inverse image of a sheaf."""
        assert False, (
            "the inverse image f^{-1} of a quasi-coherent sheaf is not quasi-coherent, and no "
            "sheaf on the underlying space beyond the distinguished-open basis is represented; "
            "the quasi-coherent pullback f^* = O_X tensor f^{-1}(-) is module_pullback"
        )

    def is_open_immersion(self) -> bool:
        r"""Whether this arrow is the inclusion of an open subscheme of its codomain.

        An open immersion is an isomorphism onto an open subscheme followed by
        its inclusion (Stacks, Tag 01IN); here the open subscheme is placed in
        ``OpenImmersions(Y)`` at its construction and this arrow is its
        inclusion.  A representation whose arrows factor that way by their
        construction states it by overriding this method.
        """
        source = self.domain()
        return source in OpenImmersions(self.codomain()) and self is source.inclusion()

    def is_closed_immersion(self) -> bool:
        r"""Whether ``f^#`` is surjective, for affine ``f`` (Stacks, Tag 01HV)."""
        base = self.domain().scheme_base_ring()
        assert self.domain() in Schemes(base).Affine() and self.codomain() in Schemes(base).Affine(), "closed immersions are currently decided for affine schemes"
        return bool(self._engine_pullback_with_trivial_base_map().is_surjective())

    def __eq__(self, other) -> bool:
        r"""Decide equality on represented pullbacks, else on the native realizations.

        Two affine morphisms are equal when their pullbacks agree on a family
        determining maps out of the codomain algebra; a finite framing or the
        foot of a localization tower supplies one.
        """
        if self is other:
            return True
        if not isinstance(other, SchemeMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        left_pullback = self._represented_coordinate_pullback()
        right_pullback = other._represented_coordinate_pullback()
        if left_pullback is not None and right_pullback is not None:
            base = self.codomain().scheme_base_ring()
            determining = _elements_determining_maps_out_of(self.codomain().coordinate_algebra(), base)
            relative = Schemes(base)
            if (
                determining is not None
                and self.parent().homset_category().is_subcategory(relative)
                and other.parent().homset_category().is_subcategory(relative)
            ):
                return all(left_pullback(element) == right_pullback(element) for element in determining)
            return _ring_morphisms_equal(left_pullback, right_pullback)
        return bool(self.native_morphism() == other.native_morphism())

    def __ne__(self, other):
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash((id(self.domain()), id(self.codomain())))

    def _repr_(self) -> str:
        return f"Scheme morphism: {self.domain()} -> {self.codomain()}"


class _ScalarStructureSchemeMorphism(SchemeMorphism):
    r"""``X -> Spec S -> Spec R`` with the actual pullback ``R -> S``.

    This is the composition of the structure map of X with Spec of a ring
    map.  Keeping that ring map avoids treating two opaque native function
    compositions as distinct maps.  It introduces no scheme or category.
    """

    def __init__(self, homset, scalar_pullback, *, cone_construction=None) -> None:
        assert scalar_pullback.codomain() is homset.domain().scheme_base_ring(), (
            "a scalar composition uses the domain's stated base ring"
        )
        assert homset.codomain() is Schemes(scalar_pullback.domain()).base_scheme(), (
            "the scalar composition lands in the spectrum of its scalar domain"
        )
        self._scalar_pullback = scalar_pullback
        super().__init__(None, homset=homset, cone_construction=cone_construction)

    def scalar_pullback(self):
        return self._scalar_pullback

    def with_cone_construction(self, construction):
        return _ScalarStructureSchemeMorphism(self.parent(), self.scalar_pullback(), cone_construction=construction)

    def native_morphism(self):
        base_arrow = LocallyRingedSpaces().Mor(self.domain().base_scheme(), self.codomain())(self.scalar_pullback())
        return base_arrow.native_morphism() * self.domain().structure_morphism().native_morphism()

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, _ScalarStructureSchemeMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        equal = _ring_morphisms_equal(self.scalar_pullback(), other.scalar_pullback())
        # Equal scalar maps always give equal composites.  For projective
        # space Gamma(P^n_S,O)=S also gives the converse.  For an arbitrary
        # scheme the converse needs its global-section pullback.
        if equal is True or self.domain() in ProjectiveSpaces(self.domain().scheme_base_ring()):
            return equal
        return Unknown

    def __ne__(self, other):
        equal = self == other
        return Unknown if equal is Unknown else not equal

    __hash__ = SchemeMorphism.__hash__


class _OpenComplementInclusion(SchemeMorphism):
    r"""The open immersion ``X - Z -> X`` defined by its closed complement ``Z``."""

    def __init__(self, homset, closed_complement, *, cone_construction=None) -> None:
        self._closed_complement = closed_complement
        SchemeMorphism.__init__(self, None, homset=homset, cone_construction=cone_construction)

    def with_cone_construction(self, construction):
        return _OpenComplementInclusion(self.parent(), self.closed_complement(), cone_construction=construction)

    def _in_homset(self, homset):
        return _OpenComplementInclusion(homset, self.closed_complement(), cone_construction=self.cone_construction())

    def closed_complement(self):
        return self._closed_complement

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _OpenComplementInclusion)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and other.closed_complement() is self.closed_complement()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = SchemeMorphism.__hash__

    def _repr_(self):
        return f"Open immersion {self.domain()} -> {self.codomain()} complementing {self.closed_complement()}"


def _open_complement_inclusion(closed_complement):
    r"""The arrow realization rule ``hom -> (X - Z -> X)`` for the closed complement ``Z``."""

    def realize(homset):
        return _OpenComplementInclusion(homset, closed_complement)

    return realize


def _projective_coordinate_blocks(scheme):
    r"""The homogeneous coordinate blocks of a projective presentation."""
    base = scheme.scheme_base_ring()
    match scheme:
        case _ if scheme in ProductProjectiveSpaces(base):
            return tuple(int(factor.relative_dimension()) + 1 for factor in scheme.factors())
        case _ if scheme in ProjectiveSpaces(base):
            return (int(scheme.relative_dimension()) + 1,)
        case _:
            return _projective_coordinate_blocks(scheme.inclusion().codomain())


def _projective_coordinate_morphism(morphism):
    r"""Read an existing polynomial morphism in its owned coordinate presentation.

    Engine adapter (OWN-06): native polynomial morphisms use the canonical
    map on coefficients.  An already owned coordinate map keeps its stated
    coefficient map instead, including a noncanonical scalar base change.
    """
    match morphism:
        case _ProjectiveCoordinateMorphism():
            return morphism
    coordinates = morphism._represented_point_coordinates()
    if coordinates is not None:
        return _ProjectiveCoordinateMorphism(
            morphism.parent(), tuple(coordinates), point_coordinates=coordinates,
        )
    source = morphism.domain()
    base = source.scheme_base_ring()
    native = morphism.native_morphism()
    if source in Schemes(base).Affine():
        ring = source.coordinate_algebra()
    else:
        ambient, _ = _engine_projective_ambient(_engine_scheme(source))
        ring = _engine_polynomial_algebra(ambient.coordinate_ring(), base)
    engine = _engine_ring(ring)
    values = tuple(ring._from_engine_element(engine(value)) for value in _engine_defining_polynomials(native))
    return _ProjectiveCoordinateMorphism(morphism.parent(), values)


@cached_function(key=lambda scheme, ring: (id(scheme), id(ring)))
def _projective_section_restriction(scheme, ring):
    r"""Read coordinate polynomials modulo the equations on the stated source.

    Engine adapter of the scheme-morphism owner.  On ``Proj(P/I)`` a
    homogeneous section vanishes exactly when it vanishes on every standard
    open, hence when it belongs to ``I:B^infinity`` (Stacks, Tag 01M7).
    For a product the standard opens invert one coordinate from each block,
    so ``B`` is the product of the block ideals.  On ``X - V(J)`` the further
    saturation by ``J`` expresses restriction to that open, with nilpotents
    retained.  Saturation is computed by the existing ideal owner, not by a
    finite test of points.  The quotient here represents equality of
    homogeneous sections; it is not advertised as ``Gamma(X, O_X)``.
    """
    if scheme in Schemes(scheme.scheme_base_ring()).Affine():
        algebra = scheme.coordinate_algebra()
        return OwnedRings().Mor(ring, algebra).elementwise(algebra)
    native = _engine_scheme(scheme)
    ambient, equations = _engine_projective_ambient(native)
    engine = _engine_ring(ring)
    variables = tuple(engine.gens())

    def owned(polynomial):
        return ring._from_engine_element(
            _copy_polynomial_by_exponents(polynomial, engine, variables)
        )

    ideal = ring.ideal(*(owned(equation) for equation in equations))
    owned_variables = tuple(ring._from_engine_element(variable) for variable in variables)
    blocks = []
    offset = 0
    for width in _projective_coordinate_blocks(scheme):
        blocks.append(owned_variables[offset:offset + width])
        offset += width
    assert offset == len(variables), "the coordinate ring has the source's projective blocks"
    from sage.misc.misc_c import prod

    irrelevant = ring.ideal(*(prod(choice, ring.one()) for choice in cartesian_product(*blocks)))
    ideal = ideal.ideal_saturation(irrelevant)
    match native:
        case _SageAlgebraicSchemeQuasi():
            excluded = ring.ideal(*(owned(equation) for equation in native.Y().defining_polynomials()))
            ideal = ideal.ideal_saturation(excluded)
    return ring.quotient_ring(ideal).quotient_map()


def _scalar_maps_equal_on_scheme(scheme, left, right):
    r"""Compare scalar maps after restricting their images to this scheme."""
    if scheme._is_glued_from_affine_atlas():
        decisions = tuple(
            _scalar_maps_equal_on_scheme(chart, left, right)
            for chart in scheme.gluing_datum().charts()
        )
        if any(answer is False for answer in decisions):
            return False
        return True if all(answer is True for answer in decisions) else Unknown
    base = scheme.scheme_base_ring()
    if scheme in Schemes(base).Affine():
        restriction = scheme.structure_morphism().coordinate_algebra_morphism()
    else:
        ambient, _ = _engine_projective_ambient(_engine_scheme(scheme))
        ring = _engine_polynomial_algebra(ambient.coordinate_ring(), base)
        restriction = _projective_section_restriction(scheme, ring) * _restriction_to_base(ring, base)
    hom = OwnedRings().Mor(left.domain(), restriction.codomain())
    return _ring_morphisms_equal(
        hom.elementwise(lambda scalar: restriction(left(scalar))),
        hom.elementwise(lambda scalar: restriction(right(scalar))),
    )


class _ProjectiveCoordinateMorphism(SchemeMorphism):
    r"""A projective morphism given by coordinate sections and its coefficient map.

    The coefficients of the target act in the source coordinate ring by the
    retained ring map.  Thus the projection along R -> R' keeps that map,
    not a natural coercion between engines.  In each projective block the
    sections generate the line bundle on the stated source; on affine charts
    this is the usual homogeneous-coordinate construction (Stacks, 01ND).
    """

    def __init__(self, homset, coordinates, *, coefficient_map=None,
                 cone_construction=None, point_coordinates=None) -> None:
        coordinates = tuple(coordinates)
        assert coordinates, "a projective coordinate presentation has a nonempty block"
        ring = coordinates[0].parent()
        assert all(value.parent() is ring for value in coordinates), (
            "coordinate sections are written in one source coordinate ring"
        )
        target_base = homset.codomain().scheme_base_ring()
        if coefficient_map is None:
            coefficient_map = _restriction_to_base(ring, target_base)
        assert coefficient_map.domain() is target_base and coefficient_map.codomain() is ring, (
            "the coefficient map goes from the target base to the source coordinate ring"
        )
        assert sum(_projective_coordinate_blocks(homset.codomain())) == len(coordinates), (
            "the coordinate family has the blocks of the target projective presentation"
        )
        self._homogeneous_coordinates = finite_family(coordinates, name="Homogeneous coordinates")
        self._coefficient_map = coefficient_map
        super().__init__(None, homset=homset, cone_construction=cone_construction,
                         point_coordinates=point_coordinates)

    def with_cone_construction(self, construction):
        return _ProjectiveCoordinateMorphism(
            self.parent(), tuple(self.homogeneous_coordinates()),
            coefficient_map=self.coefficient_map(), cone_construction=construction,
            point_coordinates=self._represented_point_coordinates(),
        )

    def coefficient_map(self):
        r"""The map from the target scalar ring into the source coordinate ring."""
        return self._coefficient_map

    def homogeneous_coordinates(self):
        return self._homogeneous_coordinates

    @cached_method
    def native_morphism(self):
        r"""The native polynomial map, when its scalar coercion is the stated map.

        This is a private engine boundary.  Sage's polynomial-map entry has
        no coefficient-map argument; a different map must not be erased.
        Owned substitution and point evaluation do not require this entry.
        """
        ring = self.coefficient_map().codomain()
        base = self.coefficient_map().domain()
        native_scalar = _engine_ring(ring).coerce_map_from(_engine_ring(base))
        assert native_scalar is not None, "the polynomial engine has no matching scalar coercion"
        natural = OwnedRings().Mor(base, ring)(native_scalar)
        assert _ring_morphisms_equal(self.coefficient_map(), natural) is True, (
            "this polynomial engine cannot realize the noncanonical coefficient map"
        )
        return _native_scheme_homset(self.domain(), self.codomain())(
            [_engine_element(ring, value) for value in self.homogeneous_coordinates()], check=False,
        )

    def _map_to_target_base(self):
        r"""The composite to the target's scalar spectrum, retaining coefficients."""
        source = self.domain()
        base = self.coefficient_map().domain()
        target = Schemes(base).base_scheme()
        hom = LocallyRingedSpaces().Mor(source, target)
        if source in Schemes(source.scheme_base_ring()).Affine():
            return hom(self.coefficient_map())
        # In a homogeneous polynomial presentation degree-zero polynomials
        # are scalars.  Read that constant at the engine boundary; a rational
        # section on a more general presentation is not such a polynomial.
        ring = self.coefficient_map().codomain()
        source_base = source.scheme_base_ring()

        def scalar(value):
            polynomial = _engine_element(ring, self.coefficient_map()(value))
            assert polynomial.is_constant(), "a homogeneous coefficient has degree zero"
            return source_base._from_engine_element(_engine_ring(source_base)(polynomial.constant_coefficient()))

        scalar_map = OwnedRings().Mor(base, source_base).elementwise(scalar)
        base_arrow = LocallyRingedSpaces().Mor(source.base_scheme(), target)(scalar_map)
        return base_arrow * source.structure_morphism()

    def image_of_point(self, point):
        return self * point

    def __mul__(self, other):
        assert other.codomain() is self.domain(), "the morphisms are not composable"
        cone_leg = self._projected_cone_leg(other)
        if cone_leg is not None:
            return cone_leg
        if other._is_the_identity():
            return self
        hom = _scheme_composition_hom(self, other)
        source = other.domain()
        if self.domain() in Schemes(self.domain().scheme_base_ring()).Affine():
            pullback = other.coordinate_algebra_morphism()
            return _ProjectiveCoordinateMorphism(
                hom, tuple(pullback(value) for value in self.homogeneous_coordinates()),
                coefficient_map=OwnedRings().Mor(self.coefficient_map().domain(), pullback.codomain()).elementwise(
                    lambda value: pullback(self.coefficient_map()(value))
                ),
            )
        if source._is_glued_from_affine_atlas():
            return other._postcompose_with(self)
        before = _projective_coordinate_morphism(other)
        source_ring = self.coefficient_map().codomain()
        images = tuple(before.homogeneous_coordinates())

        def substitute(polynomial):
            return _evaluate_owned_homogeneous_polynomial_on_coordinates(
                polynomial, source_ring, images, coefficient_map=before.coefficient_map(),
            )

        coefficients = OwnedRings().Mor(self.coefficient_map().domain(), before.coefficient_map().codomain()).elementwise(
            lambda value: substitute(self.coefficient_map()(value))
        )
        values = tuple(substitute(value) for value in self.homogeneous_coordinates())
        point_values = None
        if before._represented_point_coordinates() is not None:
            point_values = finite_family(values, name="Point coordinates")
        return _ProjectiveCoordinateMorphism(hom, values, coefficient_map=coefficients, point_coordinates=point_values)

    def _postcompose_with(self, after):
        relative = Schemes(self.codomain().scheme_base_ring())
        if (after.codomain() is self.codomain().base_scheme()
                and after.parent().homset_category().is_subcategory(relative)):
            return self._map_to_target_base()
        if after.codomain() in Schemes(after.codomain().scheme_base_ring()).Projective():
            return _projective_coordinate_morphism(after) * self
        return None

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, SchemeMorphism) or other.domain() is not self.domain() or other.codomain() is not self.codomain():
            return False
        other = _projective_coordinate_morphism(other)
        ring = self.coefficient_map().codomain()
        restriction = _projective_section_restriction(self.domain(), ring)
        hom = OwnedRings().Mor(self.coefficient_map().domain(), restriction.codomain())
        coefficients_equal = _ring_morphisms_equal(
            hom.elementwise(lambda scalar: restriction(self.coefficient_map()(scalar))),
            hom.elementwise(lambda scalar: restriction(ring(other.coefficient_map()(scalar)))),
        )
        if coefficients_equal is False:
            return False
        left = tuple(self.homogeneous_coordinates())
        right = tuple(ring(value) for value in other.homogeneous_coordinates())
        offset = 0
        for width in _projective_coordinate_blocks(self.codomain()):
            if any(not restriction(left[i] * right[j] - left[j] * right[i]).is_zero()
                   for i, j in combinations(range(offset, offset + width), 2)):
                return False
            offset += width
        return coefficients_equal

    def __ne__(self, other):
        equal = self == other
        return Unknown if equal is Unknown else not equal

    __hash__ = SchemeMorphism.__hash__

    def _repr_(self):
        return f"Projective morphism from {self.domain()} to {self.codomain()} defined by {tuple(self.homogeneous_coordinates())}"


class _RepresentedAffineSchemeMorphism(SchemeMorphism):
    r"""A morphism of affine schemes, which is its coordinate pullback."""

    def __init__(self, homset, pullback, *, cone_construction=None, point_coordinates=None) -> None:
        SchemeMorphism.__init__(
            self,
            None,
            homset=homset,
            pullback=pullback,
            cone_construction=cone_construction,
            point_coordinates=point_coordinates,
        )

    def with_cone_construction(self, construction):
        return _RepresentedAffineSchemeMorphism(
            self.parent(),
            self.coordinate_algebra_morphism(),
            cone_construction=construction,
            point_coordinates=self._represented_point_coordinates(),
        )

    @cached_method
    def native_morphism(self):
        r"""``Spec`` of the pullback on the engines of the two spectra."""
        if self._is_the_identity():
            return _engine_scheme(self.domain()).identity_morphism()
        return _native_scheme_homset(self.domain(), self.codomain())(
            _engine_coordinate_pullback(self.coordinate_algebra_morphism()),
            check=False,
        )


class SchemeMorCategory(CategoricalHomset):
    r"""The owned category \(\mathrm{Mor}_{\mathbf{Sch}/R}(X, Y)\).

    Its objects are the scheme morphisms \(X\to Y\) over ``R``.  An arrow is
    constructed from its defining datum (``CON-16``):

    * an owned scheme morphism with these endpoints, returned, or re-sited
      between affine endpoints through its pullback;
    * an owned ring morphism ``O(Y) -> O(X)`` when both endpoints are affine;
    * a native Sage scheme morphism between the engines of the endpoints;
    * an arrow realization rule, a callable ``hom -> morphism`` returning an
      element parented by this Hom.  The rule is the datum of arrows whose
      representation class belongs to another construction owner -- the open
      inclusions of a glued scheme, the complement of a projective closed
      subscheme -- and of the inclusion of a subobject, which cannot be built
      before the subobject it starts at.

    Sage's scheme Hom between the two engines stays underneath as the
    computation engine for native realizations; it is built when first asked
    for, so a Hom whose endpoint has no engine still constructs.
    """

    Element = SchemeMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    @cached_method
    def _engine_homset_crossing(self):
        r"""Return the private Sage Hom-set these morphisms are computed in."""
        return _native_scheme_homset(self.domain(), self.codomain())

    def _element_constructor_(self, datum):
        domain = self.domain()
        codomain = self.codomain()
        base = codomain.scheme_base_ring()
        affine_endpoints = domain in Schemes(domain.scheme_base_ring()).Affine() and codomain in Schemes(base).Affine()
        match datum:
            case SchemeMorphism() if datum.parent() is self:
                return datum
            case _ProjectiveCoordinateMorphism():
                assert datum.domain() is domain and datum.codomain() is codomain, "a coordinate morphism keeps its endpoints"
                if self.homset_category().is_subcategory(Schemes(base)):
                    scalar_structure = _restriction_to_base(datum.coefficient_map().codomain(), base)
                    assert _ring_morphisms_equal(datum.coefficient_map(), scalar_structure) is not False, (
                        "the projective morphism does not commute with the stated scalar structures"
                    )
                return _ProjectiveCoordinateMorphism(
                    self, tuple(datum.homogeneous_coordinates()), coefficient_map=datum.coefficient_map(),
                    cone_construction=datum.cone_construction(), point_coordinates=datum._represented_point_coordinates(),
                )
            case _ScalarStructureSchemeMorphism():
                assert datum.domain() is domain and datum.codomain() is codomain, "a scalar composite keeps its endpoints"
                if self.homset_category().is_subcategory(Schemes(base)):
                    assert _scalar_maps_equal_on_scheme(domain, datum.scalar_pullback(), base.Mor(base).identity()) is not False, (
                        "the scalar composite does not commute with the stated scalar structures"
                    )
                return _ScalarStructureSchemeMorphism(self, datum.scalar_pullback(), cone_construction=datum.cone_construction())
            case SchemeMorphism() if affine_endpoints:
                assert datum.domain() is domain and datum.codomain() is codomain, (
                    "re-siting an affine morphism preserves its two scheme endpoints"
                )
                admitted = self(datum.coordinate_algebra_morphism())
                return _RepresentedAffineSchemeMorphism(
                    self, admitted.coordinate_algebra_morphism(),
                    cone_construction=datum.cone_construction(),
                    point_coordinates=datum._represented_point_coordinates(),
                )
            case SchemeMorphism():
                assert datum.domain() is domain and datum.codomain() is codomain, (
                    "a scheme morphism with a non-affine endpoint is re-sited only onto its own endpoints"
                )
                return datum._in_homset(self)
            case _SageSchemeMorphism():
                assert datum.domain() is _engine_scheme(domain) and datum.codomain() is _engine_scheme(codomain), (
                    "the native morphism joins the engines of these exact owned endpoints"
                )
                if affine_endpoints:
                    return self(_engine_coordinate_pullback_of(datum, domain.coordinate_algebra(), codomain.coordinate_algebra()))
                return SchemeMorphism(datum, homset=self)
            case Morphism():
                assert affine_endpoints, (
                    "a ring morphism defines a scheme morphism between affine schemes, contravariantly"
                )
                assert datum.domain() is codomain.coordinate_algebra() and datum.codomain() is domain.coordinate_algebra(), (
                    f"the pullback {datum} does not join the coordinate algebras of {codomain} and {domain}"
                )
                relative = Schemes(domain.scheme_base_ring())
                if self.homset_category().is_subcategory(relative):
                    ring = relative.base_ring()
                    target_algebra = domain.coordinate_algebra()
                    source_structure = codomain.structure_morphism().coordinate_algebra_morphism()
                    target_structure = domain.structure_morphism().coordinate_algebra_morphism()
                    ring_hom = OwnedRings().Mor(ring, target_algebra)
                    composed = ring_hom.elementwise(lambda scalar: datum(source_structure(scalar)))
                    structural = ring_hom.elementwise(target_structure)
                    assert _ring_morphisms_equal(composed, structural) is not False, (
                        "the coordinate pullback does not commute with the stated scalar structures"
                    )
                return _RepresentedAffineSchemeMorphism(self, datum)
            case _ if callable(datum):
                realized = datum(self)
                assert realized.parent() is self, (
                    "an arrow realization rule returns a morphism of the Hom it was given"
                )
                return realized
            case _:
                assert False, (
                    f"{datum} is not a defining datum of a morphism {domain} -> {codomain}"
                )

    @cached_method
    def identity(self):
        r"""``id_X``: the identity pullback on an affine scheme, else the engine identity."""
        assert self.domain() is self.codomain(), "identity is defined only on an endomorphism Hom"
        scheme = self.domain()
        match scheme:
            case _ if scheme in Schemes(scheme.scheme_base_ring()).Affine():
                algebra = scheme.coordinate_algebra()
                return _RepresentedAffineSchemeMorphism(self, algebra.Mor(algebra).identity())
            case _:
                return SchemeMorphism(_engine_scheme(scheme).identity_morphism(), homset=self)


def _restriction_to_base(ring, base_ring):
    r"""The composite ring morphism ``base_ring -> ring`` along the scalar tower of ``ring``.

    ``ring`` is an algebra over its own base, that base over its base, and so
    on down to ``ZZ``; ``base_ring`` is one of the rings of that tower.  The
    composite of the structure morphisms is the structure morphism of
    ``ring`` as a ``base_ring``-algebra, which is the defining datum of the
    restriction of base along ``Spec ring -> Spec base_ring``.
    """
    if ring is base_ring:
        return ring.Mor(ring).identity()
    below = _proper_restriction_base_ring(ring)
    assert below is not None, f"{base_ring} is not a ring of the scalar tower of {ring}"
    match ring.base_ring():
        case _ if ring.base_ring() is below:
            step = ring.algebra_structure_morphism()
        case _:
            # ``below`` is the initial ring, and the ring map out of it is unique.
            step = below.Mor(ring)(lambda integer: ring(integer))
    return step * _restriction_to_base(below, base_ring)


def _scheme_mor_category(domain, codomain, *, category=None):
    r"""The chosen Hom of two schemes, without changing either scalar structure.

    Two schemes with the same stated base use the Hom over that base.
    Across bases an arrow is a morphism of their locally ringed spaces;
    its coordinate pullback retains the actual scalar map.  In particular
    two evaluations of a parameter at different values do not mutate one
    cached spectrum into two incompatible structures (Stacks, Tag 01I1).
    """
    match category:
        case None:
            base = codomain.scheme_base_ring()
            match domain.scheme_base_ring() is base:
                case True:
                    category = Schemes(base)
                case False:
                    category = LocallyRingedSpaces()
    return category.Mor(domain, codomain)


def _scheme_composition_hom(after, before):
    r"""The Hom of a composite, retaining a common base only when both arrows do."""
    category = after.parent().homset_category()
    match before.parent().homset_category().is_subcategory(category):
        case True:
            return category.Mor(before.domain(), after.codomain())
        case False:
            return LocallyRingedSpaces().Mor(before.domain(), after.codomain())


def _affine_structure_morphism_to_base(scheme, base_ring):
    r"""Return ``scheme -> Spec(base_ring)`` in ``Sch/base_ring``.

    Over its own base this is the structure morphism.  Over a coarser base of
    its scalar tower it is ``Spec`` of the composite scalar map, a morphism of
    the scheme restricted to that base.
    """
    base_ring = _own_ring(base_ring)
    own_base = scheme.scheme_base_ring()
    assert scheme in Schemes(own_base).Affine(), "a represented affine structure morphism requires an affine scheme"
    if own_base is base_ring:
        return scheme.structure_morphism()
    scalar_map = scheme.structure_morphism().coordinate_algebra_morphism() * _restriction_to_base(own_base, base_ring)
    return _scheme_mor_category(scheme, Schemes(base_ring).base_scheme())(scalar_map)


def _scheme_isomorphism(forward, inverse):
    r"""Return the selected inverse pair in the core of the scheme category.

    A chart overlap can carry distinct open-subobject placements on its two
    sides.  Those placements strengthen the objects, not the category in which
    their transition is an isomorphism: chart changes are arrows in ``Sch/R``.
    """
    assert forward.domain() is inverse.codomain() and forward.codomain() is inverse.domain(), (
        "an inverse pair must reverse the same two scheme endpoints"
    )
    schemes = Schemes(forward.codomain().scheme_base_ring())
    return schemes.Core().Mor(forward.domain(), forward.codomain())(forward, inverse)


def _affine_morphism_from_pullback(domain, codomain, pullback):
    r"""The affine morphism ``domain -> codomain`` defined by its coordinate pullback."""
    return _scheme_mor_category(domain, codomain)(pullback)


def _affine_spec_morphism(algebra_morphism):
    r"""``Spec(phi): Spec B -> Spec A`` for an algebra morphism ``phi: A -> B``."""
    source_algebra = algebra_morphism.domain()
    target_algebra = algebra_morphism.codomain()
    assert source_algebra in Algebras(source_algebra.base_ring()).Associative().Unital().Commutative(), (
        "affine Spec acts on a morphism of commutative algebras"
    )
    assert target_algebra in Algebras(target_algebra.base_ring()).Associative().Unital().Commutative(), (
        "affine Spec acts on a morphism of commutative algebras"
    )
    return _affine_morphism_from_pullback(
        target_algebra.affine_spectrum(),
        source_algebra.affine_spectrum(),
        algebra_morphism,
    )


# ---------------------------------------------------------------------------
# The category of schemes over a base ring and its axioms.
# ---------------------------------------------------------------------------


def _normal_placement(base_ring) -> bool:
    r"""Whether \(\mathbb{A}^n_R\) and \(\mathbb{P}^n_R\) over ``base_ring`` are placed as normal.

    A scheme is normal when its local rings are integrally closed domains.
    Affine ``n``-space over ``R`` is covered by the single polynomial ring
    ``R[x_1,...,x_n]``, and projective ``n``-space by the degree-zero parts of
    its graded localizations, which are again polynomial rings on ``n``
    variables.  A polynomial ring over an integrally closed domain is
    integrally closed, and so is every localization of one, so both spaces are
    normal exactly when ``R`` is.

    The hypothesis stated here is that ``R`` is a principal ideal domain, hence
    a unique factorization domain, hence integrally closed; that covers
    \(\mathbb{Z}\), every field, and every polynomial ring in one variable over
    a field.  Normality is not placed over a base outside that hypothesis.
    """
    return base_ring in OwnedPrincipalIdealDomains()


def _integral_placement(ring) -> bool:
    r"""Whether ``Spec`` of ``ring`` is integral: ``ring`` is placed as an integral domain.

    ``Spec A`` is integral exactly when ``A`` is a domain (Stacks, Tag 01OK);
    the placement of ``A`` is read, and no primality is decided here.
    """
    return ring in OwnedIntegralDomains()


def _affine_scheme(algebra, base, placements=(), **level_data):
    r"""Construct ``Spec A`` over ``Spec R`` in ``Schemes(R).Affine()`` joined with ``placements``.

    This is the construction behind the entry ``Schemes(R).Affine()(A)``;
    specialized affine constructions -- a distinguished open, an affine closed
    subscheme, an affine product, an acted scheme -- reach it with their own
    placement and the level data those placements declare.  The placements
    implied by ``A`` are stated here once: a framed algebra is of finite type,
    hence quasi-projective (Stacks, Tag 01VW for affine morphisms of finite
    type); ``Spec R`` is smooth over itself; a domain gives an integral scheme.
    """
    schemes = Schemes(base)
    categories = [schemes.Affine()]
    if algebra is base or (algebra in FramedAlgebras(base) and algebra.algebra_generating_set().cardinality().is_finite()):
        categories.extend((schemes.FiniteType(), schemes.QuasiProjective()))
    if algebra is base:
        categories.append(schemes.Smooth())
        if _normal_placement(base):
            categories.append(schemes.Normal())
    if _integral_placement(algebra):
        categories.append(schemes.Integral())
    return _object_of(
        Category.join((*categories, *placements)),
        scheme_base_ring=base,
        scheme_engine=_engine_affine_spectrum(algebra, base),
        coordinate_algebra=algebra,
        **level_data,
    )


@cached_function(key=lambda algebra, base: (id(algebra), id(base)))
def _affine_spectrum_over(algebra, base):
    r"""The selected ``Spec A`` over ``Spec R``, one object for each ``(A, R)``."""
    return _affine_scheme(algebra, base)


def _affine_spectrum(ring_or_algebra, base_ring=None):
    r"""Return the affine scheme ``Spec(A)`` over its scalar base.

    If ``A`` is an owned commutative ``R``-algebra, the result lies in
    ``Schemes(R)`` and its structure morphism is ``Spec`` of ``R -> A``.  A
    ring stated as its own base, ``Spec(R, base_ring=R)``, is the terminal
    affine ``R``-scheme.  Omitting the base retains the algebra's own base; a
    ring whose base is itself, or whose base has the same engine, is over
    itself.
    """
    algebra = _own_ring(ring_or_algebra)
    match base_ring:
        case None:
            declared = algebra.base_ring()
            base = algebra if declared is None or _engine_ring(declared) is _engine_ring(algebra) else _own_ring(declared)
        case _:
            base = _own_ring(base_ring)
    return Schemes(base).Affine()(algebra)


class SchemeHomCategoryConstruction(LocallyRingedHomCategoryConstruction):
    r"""Morphisms commuting with the chosen structure maps to ``Spec R``.

    Unlike an axiom on an R-scheme, specifying R restricts the morphisms:
    its Hom is not the unrestricted locally ringed-space Hom.
    """

    def _inherits_morphisms_from(self, supercategory, domain, codomain):
        return supercategory.is_subcategory(Schemes(self.base_category().base_ring()))


class Schemes(OwnedCategoryOverBaseRing):
    r"""Schemes over ``Spec(R)`` for the represented base ring ``R``.

    Objects are schemes ``X`` with a structure morphism ``X -> Spec R``;
    morphisms are morphisms over ``Spec R``.  The level datum is ``R`` itself
    and the private Sage scheme realizing ``X``, or ``None`` for a scheme
    presented without one.
    """

    def an_object(self):
        r"""The affine line over the base ring."""
        return AffineSpaces(self.base_ring())(1)

    def _repr_object_names(self):
        return f"schemes over {self.base_ring()}"

    def super_categories(self):
        r"""A scheme is a locally ringed space.

        Restriction along ``Spec R -> Spec R_0`` is a functor obtained from
        this category, never a supercategory declaration: Sage applies every
        axiom along a declared edge, and finite type, smoothness and
        projectivity do not descend that composite.
        """
        return [LocallyRingedSpaces()]

    _HomCategory = SchemeHomCategoryConstruction

    def Mor(self, domain, codomain):
        r"""``Mor_{Sch/R}(X, Y)``, the single Hom selected by its category family."""
        return self.HomCategory().Of(domain, codomain)

    _MonoCategory = None  # set below, once SchemeMonomorphisms is defined

    class SubcategoryMethods:
        def base_change_functor(self, ring_map):
            r"""Return ``- x_{Spec R} Spec R' : Sch/R -> Sch/R'`` along ``R -> R'``."""
            from dzack_research.preamble.categories.schemes.base_change import (
                _scheme_base_change_functor,
            )

            assert _own_ring(ring_map.domain()) is self.base_ring(), (
                "scheme base change is owned by the scheme category over the ring-map domain"
            )
            return _scheme_base_change_functor(ring_map)

        def product(self, factors):
            r"""Return $\prod_{i \in I} X_i$ for an indexed family of schemes.

            The product is taken over the index set: the coordinates of every
            factor sit side by side in the one product, so the projection to
            the factor at $i$ is an arrow out of that product rather than a
            composite through nested binary products.
            """
            return _scheme_product(_finite_factor_family(factors, name="Product factors"))

        def _categorical_product(self, left, right):
            return _scheme_product(left, right)

        def fiber_product(self, left_leg, right_leg):
            r"""Return the fiber product of the cospan these two legs form."""
            assert left_leg.codomain() is right_leg.codomain(), "a cospan has one common codomain"
            return self._categorical_pullback(left_leg, right_leg)

        def _categorical_pullback(self, left_morphism, right_morphism):
            return _scheme_fiber_product(left_morphism, right_morphism)

        def equalizer(self, left, right):
            r"""Return the equalizer ``Eq(f, g) -> X`` of two parallel morphisms."""
            assert left.domain() is right.domain() and left.codomain() is right.codomain(), "an equalizer is taken of two parallel morphisms"
            return self._categorical_equalizer(left, right)

        def _categorical_equalizer(self, left, right):
            r"""``Eq(f, g)`` for affine ``f, g: Spec A -> Spec B``.

            The equalizer is the closed subscheme cut out by the ideal
            ``(f^#(b) - g^#(b) : b in B)``; a chosen generating set of ``B``
            generates that ideal because both pullbacks are ``R``-algebra maps.
            Its universal property is that of the closed immersion: ``h: T -> X``
            factors through it exactly when ``h^#`` kills the ideal, which is
            ``f h = g h`` (Stacks, Tag 01JR).
            """
            source = left.domain()
            target = left.codomain()
            base = source.scheme_base_ring()
            assert source in Schemes(base).Affine() and target in Schemes(base).Affine(), "the represented equalizer currently requires affine schemes"
            target_algebra = target.coordinate_algebra()
            assert target_algebra in FramedAlgebras(target_algebra.base_ring()), "the represented equalizer requires a chosen algebra generating set on the target"
            left_pullback = left.coordinate_algebra_morphism()
            right_pullback = right.coordinate_algebra_morphism()
            equations = tuple(
                left_pullback(target_algebra.algebra_generator(label)) - right_pullback(target_algebra.algebra_generator(label))
                for label in target_algebra.algebra_generating_set()
            )
            equalizer = source.closed_subscheme(equations)
            assert left * equalizer.inclusion() == right * equalizer.inclusion(), "the equalizer inclusion does not equalize the two morphisms"
            return equalizer

        def Affine(self):
            r"""Return this category with the axiom that its objects are affine."""
            return self._with_axiom("Affine")

        def QuasiAffine(self):
            r"""Return this category with the axiom that its objects are quasi-affine."""
            return self._with_axiom("QuasiAffine")

        def Projective(self):
            r"""Return this category with the axiom that its objects are projective over the base."""
            return self._with_axiom("Projective")

        def QuasiProjective(self):
            r"""Return this category with the axiom that its objects are quasi-projective over the base."""
            return self._with_axiom("QuasiProjective")

        def Separated(self):
            r"""Return this category with the axiom that its objects are separated."""
            return self._with_axiom("Separated")

        def FiniteType(self):
            r"""Return this category with the axiom that its objects are of finite type over the base."""
            return self._with_axiom("FiniteType")

        def Integral(self):
            r"""Return this category with the axiom that its objects are integral."""
            return self._with_axiom("Integral")

        def Normal(self):
            r"""Return this category with the axiom that its objects are normal."""
            return self._with_axiom("Normal")

        def Smooth(self):
            r"""Return this category with the axiom that its objects are smooth over the base."""
            return self._with_axiom("Smooth")

    @cached_method
    def base_scheme(self):
        r"""``Spec R``, the terminal object of ``Sch/R``."""
        return self.Affine()(self.base_ring())

    @cached_method
    def slice_category(self):
        return self.SliceOver(self.base_scheme())

    def as_slice_object(self, scheme):
        assert scheme in self, f"{scheme} is not an object of {self}"
        return self.slice_category()(scheme.structure_morphism())

    @cached_method
    def coslice_category(self):
        r"""``Spec R / Sch_R``, where the pointed ``R``-schemes live.

        An object is a morphism ``Spec R -> X`` and a morphism is a triangle
        under ``Spec R``.  A family ``X -> S`` is an object of the slice and a
        point of ``X`` is an object of the coslice; the two constructions are
        opposite and neither stands in for the other.
        """
        return self.CosliceUnder(self.base_scheme())

    def as_coslice_object(self, point):
        r"""Read a morphism ``Spec R -> X`` as a pointed ``R``-scheme."""
        assert point.domain() is self.base_scheme(), "a pointed R-scheme is a morphism out of Spec R"
        assert point.codomain() in self, "a pointed R-scheme is pointed in an R-scheme"
        return self.coslice_category()(point)

    def glue_affine_charts(self, left_chart, right_chart, transition):
        r"""Glue two affine charts along the represented open isomorphism ``transition``."""
        from dzack_research.preamble.categories.schemes.gluing import (
            _TwoChartSchemeGluingDatum,
        )

        return _TwoChartSchemeGluingDatum(self, left_chart, right_chart, transition).scheme()

    def glue_affine_atlas(self, charts, transitions, placements=(), **level_data):
        r"""Glue a finite affine atlas with represented distinguished-open transitions.

        ``placements`` are further categories the glued scheme is an object of
        by its construction, with the level data they declare: the open
        complement of a closed subscheme is glued as an object of
        ``OpenImmersions(X)``, a mixed product as an object of
        ``ProductSchemes(R)``.
        """
        from dzack_research.preamble.categories.schemes.gluing import (
            _FiniteSchemeGluingDatum,
        )

        return _FiniteSchemeGluingDatum(
            self,
            charts,
            transitions,
            placements=placements,
            level_data=level_data,
        ).scheme()

    class ParentMethods:
        def __init__(self, scheme_base_ring, scheme_engine=None, **rest) -> None:
            r"""``R`` and the private Sage scheme realizing this scheme.

            The realization is private computation state, not a mathematical
            datum: a scheme glued from charts is presented without one, and
            omits it.
            """
            self._scheme_base_ring = scheme_base_ring
            self._scheme_engine_realization = scheme_engine
            super().__init__(base=scheme_base_ring, **rest)

        def _scheme_engine(self):
            r"""The private Sage scheme realizing this scheme (``OWN-06``)."""
            assert self._scheme_engine_realization is not None, (
                f"{self} is presented without a Sage scheme realization, so a native "
                "scheme computation is not available for it"
            )
            match self._is_glued_from_affine_atlas():
                case True:
                    return self._scheme_engine_realization.native_realization()
                case False:
                    return self._scheme_engine_realization

        def _is_glued_from_affine_atlas(self) -> bool:
            r"""Whether this scheme is realized by the affine gluing datum it was glued from."""
            return _is_gluing_realization(self._scheme_engine_realization)

        def gluing_datum(self):
            r"""The affine gluing datum this scheme was glued from (Stacks, Tag 01JA).

            Charts ``U_i``, overlaps ``U_ij <= U_i`` and transition isomorphisms
            satisfying the cocycle condition: the chosen presentation of a
            scheme built by :meth:`Schemes.glue_affine_atlas` or
            :meth:`Schemes.glue_affine_charts`, whose charts, overlaps and
            chart embeddings are read from it.
            """
            assert self._is_glued_from_affine_atlas(), f"{self} was not glued from an affine gluing datum"
            return self._scheme_engine_realization.gluing_datum()

        def chartwise_closed_subscheme(self, local_closed_subschemes, *, name="Chartwise closed subscheme"):
            r"""The closed subscheme glued from closed subschemes ``Z_i <= U_i`` that agree on the overlaps."""
            assert self._is_glued_from_affine_atlas(), "a chartwise closed subscheme is glued on the charts of a gluing datum"
            return self._scheme_engine_realization.chartwise_closed_subscheme(local_closed_subschemes, name=name)

        def chartwise_fixed_subscheme(self, local_automorphisms):
            r"""The fixed subscheme of an automorphism preserving each chart, glued from the charts' fixed subschemes."""
            assert self._is_glued_from_affine_atlas(), "a chartwise fixed subscheme is glued on the charts of a gluing datum"
            return self._scheme_engine_realization.chartwise_fixed_subscheme(local_automorphisms)

        def c2_chartwise_invariant_quotient(self, acting_group, local_actions):
            r"""This scheme modulo a ``C_2`` action preserving each chart, glued from the charts' invariant quotients."""
            assert self._is_glued_from_affine_atlas(), "a chartwise invariant quotient is glued on the charts of a gluing datum"
            return self._scheme_engine_realization.c2_chartwise_invariant_quotient(self, acting_group, local_actions)

        def _locally_ringed_homset_class(self):
            r"""The arrow engine for this scheme's affine/native or gluing presentation."""
            match self._is_glued_from_affine_atlas():
                case True:
                    return self._scheme_engine_realization.scheme_homset_class()
                case False:
                    return SchemeMorCategory

        def Mor(self, codomain, category=None):
            return _scheme_mor_category(self, codomain, category=category)

        def scheme_base_ring(self):
            return self._scheme_base_ring

        def scheme_category(self):
            return Schemes(self.scheme_base_ring())

        def log_pair(self, boundary_divisor):
            r"""Return the log pair ``(self, boundary_divisor)``."""
            from dzack_research.preamble.categories.schemes.log_pairs import _log_pair

            return _log_pair(self, boundary_divisor)

        def base_scheme(self):
            return self.scheme_category().base_scheme()

        @cached_method
        def structure_morphism(self):
            r"""``X -> Spec R``: ``Spec`` of the algebra structure for affine ``X``, glued from the charts' for a glued ``X``, else the realization's."""
            base_scheme = self.base_scheme()
            base = self.scheme_base_ring()
            match self:
                case _ if self is base_scheme:
                    return self.categorical_identity_morphism()
                case _ if self._is_glued_from_affine_atlas():
                    return self._scheme_engine_realization.structure_morphism(self)
                case _ if self in Schemes(base).Affine():
                    algebra = self.coordinate_algebra()
                    pullback = _restriction_to_base(algebra, base)
                    return _RepresentedAffineSchemeMorphism(_scheme_mor_category(self, base_scheme), pullback)
                case _:
                    return _scheme_mor_category(self, base_scheme)(_engine_scheme(self).base_morphism())

        def dimension(self):
            r"""The Krull dimension of ``Spec A`` for affine ``X``, else the realization's."""
            match self:
                case _ if self in Schemes(self.scheme_base_ring()).Affine():
                    return self.coordinate_algebra().krull_dimension()
                case _:
                    return _engine_scheme(self).dimension()

        def relative_dimension(self):
            r"""The relative dimension of ``X -> Spec R``.

            Zero for ``Spec R``; the number of coordinates of an affine space;
            ``dim A - dim R`` for another affine scheme, the relative dimension
            of an equidimensional scheme of finite type and flat over an
            integral base; the sum over the factors of a product; otherwise the
            realization's.
            """
            base = self.scheme_base_ring()
            match self:
                case _ if self is self.base_scheme():
                    return 0
                case _ if self in AffineSpaces(base):
                    return self.coordinate_algebra().algebra_generating_set().cardinality()
                case _ if self in ProductSchemes(base):
                    return sum(int(factor.relative_dimension()) for factor in self.factors())
                case _ if self in Schemes(base).Affine():
                    return self.dimension() - base.krull_dimension()
                case _:
                    return _engine_scheme(self).dimension_relative()

        def is_smooth(self) -> bool:
            r"""Whether ``X -> Spec R`` is smooth: by placement, else by the realization's Jacobian criterion."""
            match self:
                case _ if self in Schemes(self.scheme_base_ring()).Smooth():
                    return True
                case _:
                    return bool(_engine_scheme(self).is_smooth())

        def base_change(self, ring_map):
            r"""``X_{R'} = X x_{Spec R} Spec R'`` along a scalar morphism ``R -> R'``.

            The functor is applied to this object; the result is constructed
            as the fibre product of ``X -> Spec R <- Spec R'``, so its two
            projections and the universal factorization are available on it.
            """
            return self.scheme_category().base_change_functor(ring_map)(self)

        def as_slice_object(self):
            return self.scheme_category().as_slice_object(self)

        def fiber(self, base_morphism):
            r"""``X x_{Spec R} T``, the fibre of ``X -> Spec R`` over a morphism ``T -> Spec R``."""
            assert base_morphism.codomain() is self.base_scheme(), "a fibre is taken over a morphism into the base scheme"
            return self.scheme_category().fiber_product(self.structure_morphism(), base_morphism)

        def fiber_over_ideal(self, ideal):
            r"""The fibre over the closed subscheme ``V(I) <= Spec R`` of an ideal ``I`` of ``R``."""
            return self.fiber(self.base_scheme().closed_subscheme(tuple(ideal.ideal_generators())).inclusion())

        def generic_fiber(self):
            r"""``X x_{Spec R} Spec Frac(R)``, the base change to the fraction field of a domain."""
            return self.base_change(self.scheme_base_ring().fraction_field_map())

        def special_fiber(self):
            r"""``X x_{Spec R} Spec R/m``, the base change to the residue field of a local base."""
            return self.base_change(self.scheme_base_ring().residue_map())

        def base_change_to_completion(self):
            r"""``X x_{Spec R} Spec R^``, the base change to the ``m``-adic completion of a local base."""
            base = self.scheme_base_ring()
            return self.base_change(base.adic_completion(base.maximal_ideal()).completion_map())

        def special_fiber_comparison(self):
            r"""The isomorphism ``(X_{R^})_k -> X_k`` of the two special fibres over a local base."""
            from dzack_research.preamble.categories.schemes.families import (
                _special_fiber_comparison,
            )

            return _special_fiber_comparison(self)

        @cached_method
        def diagonal_morphism(self):
            r"""``Delta: X -> X x_S X``, the cone map with both legs the identity."""
            identity = self.categorical_identity_morphism()
            return _scheme_product(self, self).from_product_cone((identity, identity))

        @cached_method
        def diagonal_subscheme(self):
            r"""The closed subscheme ``Delta(X) <= X x_S X`` for affine ``X``.

            For ``X = Spec A`` the diagonal is ``Spec`` of the multiplication
            ``A tensor_R A -> A``, whose kernel is generated by
            ``a tensor 1 - 1 tensor a`` over a generating set of ``A``; an affine
            scheme is separated, so this is a closed immersion.
            """
            base = self.scheme_base_ring()
            assert self in Schemes(base).Affine(), (
                "the diagonal is represented as a closed subscheme for affine schemes; for a glued scheme it is closed exactly when the scheme is separated"
            )
            product = _scheme_product(self, self)
            left = product.projection(0).coordinate_algebra_morphism()
            right = product.projection(1).coordinate_algebra_morphism()
            algebra = self.coordinate_algebra()
            equations = tuple(
                left(algebra.algebra_generator(label)) - right(algebra.algebra_generator(label))
                for label in algebra.algebra_generating_set()
            )
            return product.closed_subscheme(equations)

        def point_morphism(self, coordinates):
            r"""The ``R``-point ``Spec R -> X`` with the stated coordinates.

            On an affine scheme with chosen algebra generators the point is
            the algebra map sending each generator to its coordinate.  On a
            product of projective spaces the coordinates are the concatenated
            homogeneous blocks of the factors; on another realized scheme they
            are its native point coordinates.
            """
            base = self.scheme_base_ring()
            owned_coordinates = tuple(base(coordinate) for coordinate in coordinates)
            selected = finite_family(owned_coordinates, name=f"Selected coordinates of point on {self}")
            hom = Schemes(base).Mor(self.base_scheme(), self)
            match self:
                case _ if self in Schemes(base).Affine():
                    algebra = self.coordinate_algebra()
                    assert algebra in FramedAlgebras(base), "an affine point is stated in chosen algebra generators"
                    labels = tuple(algebra.algebra_generating_set())
                    assert len(labels) == len(owned_coordinates), "an affine point needs one coordinate per algebra generator"
                    pullback = algebra.Mor(base)(dict(zip(labels, owned_coordinates, strict=True)))
                    return _RepresentedAffineSchemeMorphism(hom, pullback, point_coordinates=selected)
                case _ if self in ProductProjectiveSpaces(base):
                    engine_coordinates = tuple(_engine_element(base, coordinate) for coordinate in owned_coordinates)
                    factor_points = []
                    offset = 0
                    for factor in self.factors():
                        width = int(factor.relative_dimension()) + 1
                        block = engine_coordinates[offset : offset + width]
                        assert len(block) == width, "a product-projective point has one homogeneous coordinate block per factor"
                        factor_engine = _engine_scheme(factor)
                        factor_points.append(factor_engine._point(factor_engine.point_homset(), block, check=False))
                        offset += width
                    assert offset == len(engine_coordinates), "too many homogeneous coordinates for this product of projective spaces"
                    engine = _engine_scheme(self)
                    native = engine._point(engine.point_homset(), factor_points, check=False)
                    return SchemeMorphism(native, homset=hom, point_coordinates=selected)
                case _:
                    engine = _engine_scheme(self)
                    native = engine._point(
                        engine.point_homset(),
                        [_engine_element(base, coordinate) for coordinate in owned_coordinates],
                        check=False,
                    )
                    return SchemeMorphism(native, homset=hom, point_coordinates=selected)

        def projective_morphism_from_coordinates(self, target, coordinates):
            r"""Return the projective morphism defined by a basepoint-free coordinate family.

            ``coordinates`` are owned homogeneous sections on the projective
            presentation.  The caller has selected this exact source as a
            domain on which they have no common zero; retaining that open domain
            and the coordinate family is the complete defining datum of the
            morphism.  No larger rational-map domain is substituted.
            """
            base = self.scheme_base_ring()
            assert target in ProjectiveSpaces(base), "projective homogeneous coordinates require a projective-space target"
            coordinates = tuple(coordinates)
            assert len(coordinates) == int(target.relative_dimension()) + 1, (
                "a projective morphism has one homogeneous coordinate per target coordinate"
            )
            return _ProjectiveCoordinateMorphism(_scheme_mor_category(self, target), coordinates)

        def categorical_identity_morphism(self):
            r"""``id_X``, the identity of this scheme's endomorphism Hom."""
            return _scheme_mor_category(self, self).identity()

        def product_with(self, other):
            r"""Return ``X x_S Y``, the product asked of the two objects.

            One argument is distinguished, so this is the operator spelling of
            the binary case.  A product over an index set that is part of the
            mathematics is named and taken over that set with
            ``Schemes(R).product(family)`` (`CON-14`).
            """
            schemes = self.scheme_category()
            assert other in schemes, "a product of schemes is taken between two schemes over one base"
            factors = (self, other)
            return schemes.product(indexed_family(Sets.Δ[1], lambda index: factors[int(index)]))

        def point_counts(self, extension_degree):
            r"""Return ``(#X(F_q),...,#X(F_{q^n}))`` for a finite base field."""
            degree = int(extension_degree)
            assert degree >= 1, "the extension degree must be positive"
            base = self.scheme_base_ring()
            assert base in OwnedFields() and base.cardinality().is_finite(), (
                "finite-field point counts require a finite base field"
            )
            return finite_family(tuple(_engine_scheme(self).count_points(degree)), name="Point counts")

        def point_count(self, extension_degree=1):
            r"""Return ``#X(F_{q^n})`` for the stated extension degree ``n``."""
            degree = int(extension_degree)
            return self.point_counts(degree)[degree - 1]

    class Separated(CategoryWithAxiom):
        r"""Schemes whose diagonal is a closed immersion."""

        class ParentMethods:
            def is_separated(self):
                return True

        def an_object(self):
            r"""The affine line, separated because it is affine."""
            return AffineSpaces(self.base_ring())(1)

    class FiniteType(CategoryWithAxiom):
        r"""Schemes of finite type over the base."""

        class ParentMethods:
            def is_finite_type(self):
                return True

        def an_object(self):
            r"""The affine line, of finite type over the base ring."""
            return AffineSpaces(self.base_ring())(1)

    class Integral(CategoryWithAxiom):
        r"""Schemes that are reduced and irreducible."""

        class ParentMethods:
            def is_integral(self):
                return True

        def an_object(self):
            r"""The affine line, integral because ``R[x]`` is a domain when ``R`` is."""
            base = self.base_ring()
            assert _integral_placement(base), (
                f"the affine line over {base} is integral exactly when {base} is a domain"
            )
            return AffineSpaces(base)(1)

    class Normal(CategoryWithAxiom):
        r"""Schemes whose local rings are integrally closed domains."""

        class ParentMethods:
            def is_normal(self):
                return True

        def an_object(self):
            r"""The affine line, normal because ``R[x]`` is integrally closed when ``R`` is."""
            base = self.base_ring()
            assert _normal_placement(base), (
                f"the affine line over {base} is normal exactly when {base} is, and the "
                "criterion available here is that the base is a principal ideal domain"
            )
            return AffineSpaces(base)(1)

    class Smooth(CategoryWithAxiom):
        r"""Schemes smooth over the base."""

        class ParentMethods:
            def is_smooth(self):
                return True

        def an_object(self):
            r"""The affine line, which is smooth over the base ring."""
            return AffineSpaces(self.base_ring())(1)

    class Affine(CategoryWithAxiom):
        r"""Schemes isomorphic to ``Spec A``.

        The level datum is the coordinate algebra ``A``; ``Spec`` is an
        equivalence ``CAlg_R^op -> AffSch_R`` (Stacks, Tag 01I1), so ``A``
        determines the scheme and is no choice.
        """

        def an_object(self):
            r"""The affine line over the base ring."""
            return AffineSpaces(self.base_ring())(1)

        def _call_(self, algebra):
            r"""``Spec A`` over this category's base, one object for each algebra."""
            return _affine_spectrum_over(_own_ring(algebra), self.base_ring())

        def extra_super_categories(self):
            # Quasi-affine as well: a scheme is an open subscheme of itself.
            return [Schemes(self.base_ring()).QuasiAffine()]

        class ParentMethods:
            def __init__(self, coordinate_algebra, **rest) -> None:
                self._coordinate_algebra = coordinate_algebra
                super().__init__(**rest)

            def coordinate_algebra(self):
                r"""``A = Gamma(X, O_X)``, the coordinate algebra of ``X = Spec A``."""
                return self._coordinate_algebra

            def coordinate_ring(self):
                r"""The coordinate algebra, under the name the ring layer uses."""
                return self.coordinate_algebra()

            def is_affine(self):
                return True

            def _prime_point(self, point):
                r"""``point`` as an element of ``Spec A``: a prime point, or the prime it is given by."""
                spectrum = self.underlying_space()
                match point.parent():
                    case _ if point.parent() is spectrum:
                        return point
                    case _:
                        return spectrum(point)

            def is_regular_at(self, point) -> bool:
                r"""Return whether ``O_{X,p}`` is a regular local ring."""
                return bool(self._prime_point(point).is_regular())

            def is_singular_at(self, point) -> bool:
                r"""Return the negation of local regularity at ``p``."""
                return not self.is_regular_at(point)

            def is_locally_factorial_at(self, point) -> bool:
                r"""Return local factoriality at ``p`` in the supported regular regime."""
                return bool(self._prime_point(point).is_locally_factorial())

            def cycle_group(self, cycle_dimension):
                r"""Return the algebraic cycle group ``Z_k(self)`` in dimension ``k``."""
                from dzack_research.preamble.categories.divisors.chow_groups import (
                    _affine_cycle_group,
                )

                return _affine_cycle_group(self, cycle_dimension)

            def full_weil_divisor_group(self):
                r"""Return the full height-one Weil divisor group of this affine scheme."""
                from dzack_research.preamble.categories.divisors.general_divisors import (
                    _affine_normal_weil_divisor_group,
                )

                return _affine_normal_weil_divisor_group(self)

            def weil_cycle_isomorphism(self):
                r"""Identify full Weil divisors with codimension-one cycles."""
                from dzack_research.preamble.categories.divisors.chow_groups import (
                    _affine_weil_cycle_isomorphism,
                )

                return _affine_weil_cycle_isomorphism(self)

            def closed_subscheme(self, *equations, placements=(), **level_data):
                r"""``V(f_1, ..., f_k) = Spec A/(f_1, ..., f_k)``, with its closed immersion.

                The equations are given one by one or as a single finite family.
                The inclusion is ``Spec`` of the quotient map ``A -> A/I``.  A
                construction whose closed subscheme is also an object of further
                categories states them in ``placements``, with their level data.
                """
                equations = _equation_family(equations)
                algebra = self.coordinate_algebra()
                base = self.scheme_base_ring()
                quotient, quotient_map = algebra._quotient_by_algebra_elements(tuple(equations))
                return _affine_scheme(
                    quotient,
                    base,
                    (ClosedEmbeddings(self), ClosedSubschemes(base), *placements),
                    inclusion_codomain=self,
                    inclusion_datum=quotient_map,
                    defining_equations=equations,
                    **level_data,
                )

            @cached_method
            def relative_differentials(self):
                r"""Return the affine module of relative Kähler differentials."""
                return self.coordinate_algebra().kahler_differentials()

            def is_flat(self) -> bool:
                r"""Return whether this represented affine scheme is flat over its base."""
                return bool(self.coordinate_algebra().is_flat())

            def differential_rank_drop_subscheme(self, rank):
                r"""Return the closed Fitting stratum ``V(Fitt_rank(Omega^1_{X/S}))``."""
                ideal = self.relative_differentials().fitting_ideal(int(rank))
                return self.closed_subscheme(tuple(ideal.ideal_generators()))

            def singular_subscheme(self):
                r"""Return the nonsmooth closed subscheme in the supported equidimensional field case.

                This uses ``Fitt_d(Omega^1_{X/k})`` when the affine morphism is
                flat and finitely presented with equidimensional fibres of
                dimension ``d``.  The base is a field, so flatness is automatic;
                the chosen finite algebra presentation and the minimal
                components of its defining ideal verify the remaining
                hypotheses.
                """
                base = self.scheme_base_ring()
                assert base in OwnedFields(), "the represented singular subscheme requires a field base"
                algebra = self.coordinate_algebra()
                assert algebra in AlgebrasWithChosenFinitePresentation(base), (
                    "the represented singular subscheme requires a chosen finite algebra presentation"
                )
                dimension = int(algebra.krull_dimension())
                minimal_components = _engine_ring(algebra).defining_ideal().minimal_associated_primes()
                assert all(int(component.dimension()) == dimension for component in minimal_components), (
                    "the represented singular subscheme requires equidimensional fibres"
                )
                return self.differential_rank_drop_subscheme(dimension)

            def relative_nonsmooth_subscheme(self):
                r"""Return the relative nonsmooth locus in the supported flat hypersurface regime.

                For a flat morphism locally of finite presentation, smoothness at
                a point is smoothness of the fibre there (Stacks, Tags 01V8 and
                01V9).  For a primitive hypersurface over a univariate polynomial
                ring over a perfect field, every fibre is a hypersurface of the
                same dimension and the Jacobian criterion is detected by the
                corresponding Fitting ideal of relative differentials.
                """
                assert self.is_flat(), "the relative nonsmooth Fitting criterion requires represented flatness"
                base = self.scheme_base_ring()
                algebra = self.coordinate_algebra()
                assert algebra in AlgebrasWithChosenFinitePresentation(base), (
                    "the relative nonsmooth locus requires a chosen finite algebra presentation"
                )
                coefficient_field = base.base_ring()
                assert (
                    coefficient_field in OwnedFields()
                    and base in SymmetricAlgebras(coefficient_field)
                    and base.algebra_generating_set().cardinality() == 1
                    and bool(_engine_ring(coefficient_field).is_perfect())
                ), "the relative hypersurface smoothness criterion currently requires k[t] with k perfect"
                relative_dimension = algebra._represented_primitive_hypersurface_relative_dimension()
                return self.differential_rank_drop_subscheme(relative_dimension)

            @cached_method
            def distinguished_open(self, element):
                r"""Return \(D(f)\subseteq X\), the open locus where ``element`` is a unit.

                \(D(f)=\operatorname{Spec}A[1/f]\), and the localization map
                \(A\to A[1/f]\) is the pullback of the open immersion.
                """
                algebra = self.coordinate_algebra()
                element = algebra(element)
                localized = algebra.localization(element)
                return _affine_scheme(
                    localized,
                    self.scheme_base_ring(),
                    (OpenImmersions(self),),
                    inclusion_codomain=self,
                    inclusion_datum=localized.localization_map(),
                )

            def distinguished_open_cover(self, *elements):
                r"""Return the finite cover by ``D(f_i)`` when the ``f_i`` generate the unit ideal."""
                from dzack_research.preamble.categories.schemes.ringed_spaces import (
                    DistinguishedAffineCovers,
                )

                return DistinguishedAffineCovers(self)(tuple(_equation_family(elements)))

            def associated_module_sheaf(self, module):
                r"""Return the quasi-coherent sheaf ``M~`` of an ``A``-module ``M``."""
                from dzack_research.preamble.categories.schemes.ringed_spaces import (
                    QuasiCoherentSheaves,
                )

                return self.structure_sheaf().associated_module_sheaf(module)

            def relative_spectrum(self, algebra_structure):
                r"""``Spec_X(B~) -> X`` for the ``O_X``-algebra given by ``A -> B`` (Stacks, Tag 01LQ).

                On affine ``X = Spec A`` a quasi-coherent ``O_X``-algebra is an
                ``A``-algebra, stated as the ``R``-algebra morphism ``A -> B``;
                its relative spectrum is ``Spec B`` with the structure morphism
                ``Spec`` of that map, an object of ``Sch/X``.
                """
                assert algebra_structure.domain() is self.coordinate_algebra(), "a quasi-coherent algebra on Spec A is stated by an algebra map out of A"
                structure_morphism = _affine_spec_morphism(algebra_structure)
                return self.scheme_category().SliceOver(self)(structure_morphism)

    class QuasiAffine(CategoryWithAxiom):
        r"""Schemes that are open subschemes of an affine scheme."""

        def an_object(self):
            r"""The affine line, which is affine."""
            return AffineSpaces(self.base_ring())(1)

        def extra_super_categories(self):
            return [Schemes(self.base_ring()).Separated()]

        class ParentMethods:
            def is_quasi_affine(self):
                return True

        class FiniteType(CategoryWithAxiom):
            r"""Quasi-affine schemes of finite type over the base.

            A quasi-affine morphism of finite type is quasi-projective (Stacks,
            Tag 0B3H, Lemma 29.41.7), so this join declares quasi-projectivity.
            Neither hypothesis alone gives it.
            """

            def an_object(self):
                r"""The affine line, which is affine and of finite type."""
                return AffineSpaces(self.base_ring())(1)

            def extra_super_categories(self):
                return [Schemes(self.base_ring()).QuasiProjective()]

    class QuasiProjective(CategoryWithAxiom):
        r"""Schemes quasi-projective over the base."""

        def an_object(self):
            r"""The projective line, which is projective."""
            return ProjectiveSpaces(self.base_ring())(1)

        def extra_super_categories(self):
            return [Schemes(self.base_ring()).Separated()]

        class ParentMethods:
            def is_quasi_projective(self):
                return True

    class Projective(CategoryWithAxiom):
        r"""Schemes projective over the base."""

        def an_object(self):
            r"""The projective line."""
            return ProjectiveSpaces(self.base_ring())(1)

        def extra_super_categories(self):
            return [
                Schemes(self.base_ring()).QuasiProjective(),
                Schemes(self.base_ring()).FiniteType(),
            ]

        class ParentMethods:
            def is_projective(self):
                return True

            def closed_subscheme(self, *equations, placements=(), **level_data):
                r"""``V_+(f_1, ..., f_k)``, cut out by homogeneous equations.

                The equations are owned homogeneous polynomials, or elements of
                the realization's coordinate ring, which are raised into the
                owned ring of that engine before they are retained.  The Sage
                subscheme they cut out is the realization, and its embedding is
                the inclusion.  A construction whose closed subscheme is also an
                object of further categories -- a complete intersection, a blowup
                -- states them in ``placements``, with their level data.
                """
                return _projective_closed_subscheme(self, equations, placements=placements, **level_data)


def _projective_closed_subscheme(ambient, equations, placements=(), *, _engine=None, **level_data):
    r"""The one projective closed-subscheme construction, with its inclusion.

    The private engine argument is used by a construction that must decide
    a property of the defining ideal before placing its resulting scheme,
    such as the complete-intersection criterion.  No owned provisional
    scheme is allocated to make that decision.
    """
    equations = _projective_equation_family(_equation_family(equations))
    base = ambient.scheme_base_ring()
    engine = _engine_projective_subscheme(_engine_scheme(ambient), equations) if _engine is None else _engine
    return _object_of(
        Category.join((Schemes(base).Projective(), ClosedEmbeddings(ambient), ClosedSubschemes(base), *placements)),
        scheme_base_ring=base, scheme_engine=engine,
        inclusion_codomain=ambient, inclusion_datum=_native_embedding_rule,
        defining_equations=equations, **level_data,
    )


def AffineSchemes(base_ring):
    r"""``Schemes(R).Affine()``, under the name the session catalogue uses."""
    return Schemes(base_ring).Affine()


def ProjectiveSchemes(base_ring):
    r"""``Schemes(R).Projective()``, under the name the session catalogue uses."""
    return Schemes(base_ring).Projective()


def IntegralSchemes(base_ring):
    r"""``Schemes(R).Integral()``, under the name the session catalogue uses."""
    return Schemes(base_ring).Integral()


def NormalSchemes(base_ring):
    r"""``Schemes(R).Normal()``, under the name the session catalogue uses."""
    return Schemes(base_ring).Normal()


def SmoothSchemes(base_ring):
    r"""``Schemes(R).Smooth()``, under the name the session catalogue uses."""
    return Schemes(base_ring).Smooth()


def _family_ingress(arguments):
    r"""Read arguments given one by one, or as one finite family, as that family.

    This is syntax ingress for calls such as ``closed_subscheme(f)``,
    ``closed_subscheme(f, g)`` and ``closed_subscheme((f, g))``: a single
    argument that is a Python sequence or an indexed family is the family
    itself.
    """
    match arguments:
        case ((tuple() | list() | IndexedFamily()) as family,):
            return family
        case _:
            return arguments


def _equation_family(equations):
    r"""The finite family of equations given one by one or as one family."""
    return finite_family(tuple(_family_ingress(equations)), name="Defining equations")


def _projective_equation_family(equations):
    r"""Raise engine-ring equations into the owned ring of that engine; keep owned ones.

    A homogeneous equation already in an owned polynomial ring is retained as
    it is.  One given in a Sage polynomial ring is the same polynomial seen
    through the private realization, and it is raised through the owned ring
    of that engine so every retained equation is owned mathematics.
    """
    raised = []
    for equation in equations:
        parent = equation.parent()
        match parent:
            case _ if parent in _SageRings():
                owned = _own_ring(parent)
                raised.append(owned._from_engine_element(equation))
            case _:
                raised.append(equation)
    assert all(equation.is_homogeneous() for equation in raised), (
        "a closed subscheme of a projective scheme is cut out by homogeneous equations"
    )
    return finite_family(tuple(raised), name="Homogeneous defining equations")


def _engine_projective_ambient(engine):
    r"""The Sage projective or multiprojective space a realization lies in, with its equations.

    Engine adapter (``OWN-06``): the one place the class of a Sage projective
    realization is inspected, for the projective closed-subscheme construction.
    A Sage subscheme records its ambient space and defining polynomials, and a
    closed subscheme of it is cut out in that ambient space by those
    polynomials together with the new equations; an ambient space is its own,
    with none.
    """
    match engine:
        case _SageAlgebraicSchemeQuasi():
            return engine.ambient_space(), tuple(engine.X().defining_polynomials())
        case _SageAlgebraicSchemeSubscheme():
            return engine.ambient_space(), tuple(engine.defining_polynomials())
        case _:
            return engine, ()


def _engine_projective_subscheme(engine, equations):
    r"""The Sage subscheme of the realization ``engine`` cut out by owned homogeneous equations.

    Each equation is copied by its exponent dictionary onto the coordinates of
    the ambient space, so the owned ring it was written in need not share the
    realization's variable names.
    """
    ambient, ambient_equations = _engine_projective_ambient(engine)
    ambient_ring = ambient.coordinate_ring()
    ambient_variables = tuple(ambient_ring.gens())
    return ambient.subscheme(
        ambient_equations
        + tuple(
            _copy_polynomial_by_exponents(
                _engine_element(equation.parent(), equation),
                ambient_ring,
                ambient_variables,
            )
            for equation in equations
        )
    )


def _native_embedding_rule(homset):
    r"""The arrow realization rule for the inclusion of a realized closed subscheme into its codomain.

    Both realizations lie in one ambient space, and the inclusion keeps every
    homogeneous coordinate.
    """
    ambient, _ambient_equations = _engine_projective_ambient(_engine_scheme(homset.codomain()))
    return SchemeMorphism(
        _native_scheme_homset(homset.domain(), homset.codomain())(list(ambient.coordinate_ring().gens()), check=False),
        homset=homset,
    )


class AffineGSchemes(OwnedCategory):
    r"""Represented affine schemes with a chosen action of one group.

    This is the affine specialization of ``GObjects(G, Schemes(R))`` and the
    construction owner for represented affine actions.  An object is ``Spec A``
    with the chosen left action ``rho: G -> Aut(Spec A)``; the scheme the
    action was stated on is retained as the constructor's input and returned
    by :meth:`unacted_scheme`.
    """

    @staticmethod
    def __classcall__(cls, group, base_ring):
        from dzack_research.preamble.categories.group.groups import _owned_group

        return Category.__classcall__(cls, _owned_group(group), _own_ring(base_ring))

    def __init__(self, group, base_ring) -> None:
        self._group = group
        self._base_ring = base_ring
        OwnedCategory.__init__(self)

    def acting_group(self):
        return self._group

    def base_ring(self):
        return self._base_ring

    def super_categories(self):
        from dzack_research.preamble.categories.group.g_objects import GObjects

        return [
            GObjects(self.acting_group(), Schemes(self.base_ring())),
            Schemes(self.base_ring()).Affine(),
        ]

    def _repr_object_names(self):
        return f"affine {self.acting_group()}-schemes over {self.base_ring()}"

    def an_object(self):
        scheme = AffineSpaces(self.base_ring())(1)
        identity = scheme.categorical_identity_morphism()
        return self(scheme, lambda _group_element: identity)

    def global_sections_functor(self):
        r"""Return ``Gamma(-, O): AffGSch_G^op -> Modules(R[G])``.

        For a left action on ``X``, the induced left action on sections is
        ``g . s = (g^{-1})^* s``; the inverse is forced by pullback
        contravariance.
        """
        from dzack_research.preamble.categories.schemes.quotients import (
            _AffineSectionModuleFunctor,
        )

        return _AffineSectionModuleFunctor(self.acting_group(), self.base_ring())

    def _call_(self, scheme, action):
        r"""``Spec A`` with the left action ``g |-> action(g)`` of this group.

        The result is a new affine scheme on the coordinate algebra of
        ``scheme``, constructed in this category; the action datum it receives
        is the coordinate pullback of each action morphism, which is the datum
        a morphism of affine schemes is.
        """
        base = self.base_ring()
        assert scheme in Schemes(base).Affine(), f"an object of {self} is constructed from an affine scheme over {base}"
        source_endomorphisms = Schemes(base).Mor(scheme, scheme)

        def action_pullback(group_element):
            return source_endomorphisms(action(group_element)).coordinate_algebra_morphism()

        return _affine_scheme(
            scheme.coordinate_algebra(),
            base,
            (self,),
            acting_group=self.acting_group(),
            action=action_pullback,
            underlying_category=Schemes(base),
            unacted_scheme=scheme,
        )

    class ParentMethods:
        def __init__(self, unacted_scheme, **rest) -> None:
            self._unacted_scheme = unacted_scheme
            super().__init__(**rest)

        def Mor(self, codomain, category=None):
            from dzack_research.preamble.categories.group.g_objects import GObjects

            acted_schemes = GObjects(self.acting_group(), self.underlying_category())
            match category:
                case None:
                    return acted_schemes.Mor(self, codomain)
                case _ if category.is_subcategory(acted_schemes):
                    return acted_schemes.Mor(self, codomain)
                case _:
                    return _scheme_mor_category(self, codomain)

        def unacted_scheme(self):
            r"""Return the affine scheme the action was stated on."""
            return self._unacted_scheme

        @cached_method
        def fixed_ideal(self):
            r"""Return the ideal defining the common fixed subscheme ``X^G``.

            For ``X = Spec(A)`` and chosen generators ``s`` of ``G``, the fixed
            ideal is generated by ``s^*(a) - a`` on a chosen algebra generating
            family of ``A``.  Those equations generate the full equalizer ideal
            because every ``s^*`` is an ``R``-algebra map: modulo them each
            ``s^*`` fixes the scalar image and every algebra generator, hence is
            the identity; since the ``s`` generate ``G``, so is every element.
            """
            from dzack_research.preamble.categories.group.groups import (
                GroupsWithChosenFiniteGeneratingSet,
            )

            group = self.acting_group()
            assert group in GroupsWithChosenFiniteGeneratingSet(), (
                "the represented common fixed ideal requires a chosen finite group generating set"
            )
            algebra = self.coordinate_algebra()
            base = self.scheme_base_ring()
            assert algebra in FramedAlgebras(base), "the represented common fixed ideal requires a framed affine coordinate algebra"
            labels = algebra.algebra_generating_set()
            assert labels.cardinality().is_finite(), "the represented common fixed ideal requires finitely many algebra generators"
            equations = []
            for group_generator in group.group_generators():
                pullback = self.action_of(group_generator).coordinate_algebra_morphism()
                assert pullback.domain() is algebra and pullback.codomain() is algebra, (
                    "an affine scheme action acts by endomorphisms of its coordinate algebra"
                )
                equations.extend(
                    pullback(algebra.algebra_generator(label)) - algebra.algebra_generator(label)
                    for label in labels
                )
            return algebra.ideal(*equations)

        @cached_method
        def fixed_subscheme(self):
            r"""Return the common fixed subscheme ``X^G`` of this affine action."""
            return self.closed_subscheme(tuple(self.fixed_ideal().ideal_generators()))

        @cached_method
        def _invariant_algebra_data(self):
            r"""Return the selected ``(A^G, A^G -> A, engine invariants)``."""
            return _affine_linear_invariant_algebra_data(self)

        def invariant_algebra(self):
            r"""Return the represented invariant algebra ``A^G``.

            The current backend supports finite linear actions on a polynomial
            algebra over a field accepted by Sage's Singular invariant-ring
            interface.  The result carries a chosen finite polynomial
            presentation, not merely a membership predicate.
            """
            return self._invariant_algebra_data()[0]

        def invariant_algebra_inclusion(self):
            r"""Return the represented inclusion ``A^G -> A``."""
            return self._invariant_algebra_data()[1]

        def invariant_algebra_element(self, element):
            r"""Express one invariant element of ``A`` in ``A^G``.

            The invariant-ring backend used by the affine quotient returns a
            polynomial certificate in its selected invariant generators; the
            certificate is evaluated in the owned invariant algebra.
            """
            source_algebra = self.coordinate_algebra()
            element = source_algebra(element)
            assert all(
                self.action_of(group_generator).coordinate_algebra_morphism()(element) == element
                for group_generator in self.acting_group().group_generators()
            ), "the selected coordinate-algebra element is not invariant"
            invariant_algebra, inclusion, engine_invariants = self._invariant_algebra_data()
            if not engine_invariants:
                return invariant_algebra(element)
            engine_source = _engine_ring(source_algebra)
            certificate = engine_source(_engine_element(source_algebra, element)).in_subalgebra(
                engine_invariants,
                algorithm="groebner",
                certificate="invariant",
            )
            assert certificate is not None, (
                "the invariant-ring backend did not express a verified invariant in its selected generators"
            )
            result = _evaluate_polynomial_in_algebra(certificate, invariant_algebra)
            assert inclusion(result) == element, "the invariant-algebra certificate does not map back to the selected element"
            return result

        @cached_method
        def affine_quotient(self):
            r"""Return ``Spec(A^G)`` for the supported affine linear action."""
            return self.invariant_algebra().affine_spectrum(base_ring=self.scheme_base_ring())

        def quotient_base_change_comparison(self, ring_map):
            from dzack_research.preamble.categories.schemes.quotients import (
                AffineInvariantQuotientBaseChangeComparison,
            )

            return AffineInvariantQuotientBaseChangeComparison(self, ring_map)

        @cached_method
        def quotient_morphism(self):
            r"""Return the represented affine quotient map ``Spec(A) -> Spec(A^G)``."""
            return _affine_morphism_from_pullback(self, self.affine_quotient(), self.invariant_algebra_inclusion())

        def factor_through_affine_quotient(self, morphism):
            r"""Factor one invariant affine morphism uniquely through ``Spec(A^G)``.

            If ``f : Spec(A) -> Spec(C)`` is invariant, every selected
            generator of ``C`` pulls back to an element of ``A^G``, and the
            subalgebra-membership certificate expresses that pullback in the
            selected invariant generators.  These expressions define
            ``C -> A^G`` and hence the factor ``Spec(A^G) -> Spec(C)``.
            Uniqueness follows because the selected presentation of ``A^G`` was
            obtained from the kernel of the map from the polynomial algebra on
            those invariant generators to ``A``; its inclusion is injective.
            """
            assert morphism.domain() is self, "the quotient factorization starts at this acted affine scheme"
            target = morphism.codomain()
            base = self.scheme_base_ring()
            assert target in Schemes(base).Affine(), "the represented quotient universal property currently targets affine schemes"
            target_algebra = target.coordinate_algebra()
            assert target_algebra in FramedAlgebras(base), "the represented quotient factorization requires a framed target coordinate algebra"
            labels = target_algebra.algebra_generating_set()
            assert labels.cardinality().is_finite(), "the represented quotient factorization requires finitely many target generators"
            pullback = morphism.coordinate_algebra_morphism()
            invariant_algebra, inclusion, _engine_invariants = self._invariant_algebra_data()
            factor_pullback = target_algebra.Mor(invariant_algebra)(
                {label: self.invariant_algebra_element(pullback(target_algebra.algebra_generator(label))) for label in labels}
            )
            factor = _affine_morphism_from_pullback(self.affine_quotient(), target, factor_pullback)
            assert factor * self.quotient_morphism() == morphism, "the represented affine quotient factorization fails its defining triangle"
            return factor

        def descend_invariant_family(self, family_morphism):
            r"""Descend an invariant affine family map through the quotient.

            A family here is a morphism to an affine parameter scheme; if that
            morphism is invariant, its unique quotient factor is the family
            carried by ``X/G``.
            """
            return self.factor_through_affine_quotient(family_morphism)


def _affine_linear_invariant_algebra_data(scheme):
    r"""Return a finite presentation of ``A^G`` and its inclusion into ``A``.

    Private computation boundary (``OWN-06``) for the supported affine quotient
    regime: ``A`` is a polynomial algebra over a field, ``G`` is finite with
    chosen generators, and the pullbacks are linear on the chosen polynomial
    generators.  Sage's matrix-group ``invariant_generators`` routes invariant
    generation to Singular; Sage's elimination ideal computes the kernel of the
    polynomial map on the returned invariant generators.
    """
    from sage.groups.matrix_gps.finitely_generated import MatrixGroup
    from sage.matrix.constructor import matrix as sage_matrix
    from sage.rings.polynomial.polynomial_ring_constructor import (
        PolynomialRing as SagePolynomialRing,
    )

    from dzack_research.preamble.categories.group.groups import (
        GroupsWithChosenFiniteGeneratingSet,
    )

    group = scheme.acting_group()
    assert group.is_finite() is True and group in GroupsWithChosenFiniteGeneratingSet(), (
        "the represented invariant algebra requires a finite group with a chosen finite generating set"
    )
    algebra = scheme.coordinate_algebra()
    base = scheme.scheme_base_ring()
    assert algebra in SymmetricAlgebras(base) and algebra in FramedAlgebras(base), (
        "the represented invariant-ring backend requires a polynomial coordinate algebra"
    )
    assert algebra.algebra_generating_set().cardinality().is_finite(), (
        "the represented invariant-ring backend requires finitely many polynomial generators"
    )
    assert base in OwnedFields(), "the Singular invariant-ring backend requires a field of coefficients"
    labels = tuple(algebra.algebra_generating_set())
    engine_algebra = _engine_ring(algebra)
    variables = tuple(engine_algebra.gens())
    assert len(variables) == len(labels), "the selected polynomial framing disagrees with its computation engine"
    engine_base = _engine_ring(base)

    # The polynomial algebra on no generators is the scalar field itself, which
    # every automorphism over the base fixes pointwise.
    if not variables:
        return algebra, algebra.Mor(algebra).identity(), ()
    group_generators = tuple(group.group_generators())
    if not group_generators:
        return algebra, algebra.Mor(algebra).identity(), variables

    backend_matrices = []
    pullbacks = []
    for group_generator in group_generators:
        pullback = scheme.action_of(group_generator).coordinate_algebra_morphism()
        pullbacks.append(pullback)
        rows = []
        for label in labels:
            image = engine_algebra(_engine_element(algebra, pullback(algebra.algebra_generator(label))))
            row = [engine_base(image.monomial_coefficient(variable)) for variable in variables]
            linear_part = sum((coefficient * variable for coefficient, variable in zip(row, variables, strict=True)), engine_algebra.zero())
            assert image == linear_part, "the invariant-ring backend requires a linear action on polynomial generators"
            # Sage/Singular's matrix-group invariant convention acts on the
            # coordinate variables by the transpose of the supplied matrix, so
            # the rows are the actual pullback images of the chosen variables.
            rows.append(row)
        backend_matrices.append(sage_matrix(engine_base, rows))

    backend_invariants = tuple(MatrixGroup(backend_matrices).invariant_generators())
    assert backend_invariants, "a positive-dimensional polynomial invariant ring needs algebra generators"
    engine_invariants = tuple(
        _copy_polynomial_by_exponents(invariant, engine_algebra, variables) for invariant in backend_invariants
    )
    invariant_elements = tuple(algebra._from_engine_element(invariant) for invariant in engine_invariants)
    assert all(pullback(invariant) == invariant for pullback in pullbacks for invariant in invariant_elements), (
        "the backend invariant generators do not match the represented coordinate action"
    )

    invariant_labels = tuple(f"invariant_{index}" for index in range(len(engine_invariants)))
    presentation = base.free_module(invariant_labels).symmetric_algebra()
    presentation_engine = _engine_ring(presentation)
    ambient_count = len(variables)
    invariant_count = len(engine_invariants)
    combined = SagePolynomialRing(
        engine_base,
        ambient_count + invariant_count,
        names=tuple(f"ambient_{index}" for index in range(ambient_count))
        + tuple(f"invariant_{index}" for index in range(invariant_count)),
    )
    ambient_variables = tuple(combined.gens()[:ambient_count])
    invariant_variables = tuple(combined.gens()[ambient_count:])
    graph_ideal = combined.ideal(
        tuple(
            invariant_variables[index] - _copy_polynomial_by_exponents(invariant, combined, ambient_variables)
            for index, invariant in enumerate(engine_invariants)
        )
    )
    kernel = graph_ideal.elimination_ideal(ambient_variables)
    relations = []
    for relation in kernel.gens():
        if relation == combined.zero():
            continue
        relation_terms = {}
        for exponent, coefficient in relation.dict().items():
            powers = _polynomial_exponents(exponent, ambient_count + invariant_count)
            assert not any(powers[:ambient_count]), "the elimination backend returned a non-eliminated relation"
            relation_terms[powers[ambient_count:]] = coefficient
        relations.append(presentation._from_engine_element(presentation_engine(relation_terms)))
    invariant_algebra = presentation if not relations else presentation.quotient_by_relations(tuple(relations))
    invariant_labels = tuple(invariant_algebra.algebra_generating_set())
    inclusion = invariant_algebra.Mor(algebra)(
        {label: invariant_elements[index] for index, label in enumerate(invariant_labels)}
    )
    return invariant_algebra, inclusion, engine_invariants


# ---------------------------------------------------------------------------
# Affine and projective spaces, with their chosen coordinates.
# ---------------------------------------------------------------------------


def _normalized_space_names(names):
    r"""Coordinate names as Sage's space constructors read them: ``None``, a string, or a tuple."""
    match names:
        case None | str():
            return names
        case _:
            return tuple(str(name) for name in names)


def _space_placements(base):
    r"""The integral and normal placements of ``A^n_R`` and ``P^n_R``, read from ``R``."""
    schemes = Schemes(base)
    return tuple(
        category
        for category, holds in (
            (schemes.Integral(), _integral_placement(base)),
            (schemes.Normal(), _normal_placement(base)),
        )
        if holds
    )


def _affine_space_coordinates(base, dimension, names):
    r"""Sage's affine ``n``-space on the chosen names, and its owned polynomial coordinate algebra.

    The coordinate algebra is the owned polynomial algebra on the coordinate
    names, which is the free, graded free and symmetric algebra on them.
    """
    engine = _SageAffineSpace(int(dimension), _engine_ring(base), names=_normalized_space_names(names))
    return engine, _engine_polynomial_algebra(engine.coordinate_ring(), base)


def _affine_space(base, coordinates, placements=(), **level_data):
    r"""Construct ``A^n_R = Spec R[x_1, ..., x_n]`` from :func:`_affine_space_coordinates`.

    ``placements`` and ``level_data`` are those of a specialized construction
    -- a product of affine spaces, a scalar base change -- whose object is also
    an affine space.
    """
    engine, algebra = coordinates
    return _object_of(
        Category.join((AffineSpaces(base), *_space_placements(base), *placements)),
        scheme_base_ring=base,
        scheme_engine=engine,
        coordinate_algebra=algebra,
        **level_data,
    )


@cached_function(key=lambda base, dimension, names: (id(base), int(dimension), names))
def _canonical_affine_space(base, dimension, names):
    r"""The selected ordinary ``A^n_R`` for one coordinate datum."""
    return _affine_space(base, _affine_space_coordinates(base, dimension, names))


class AffineSpaces(OwnedCategoryOverBaseRing):
    r"""Affine spaces ``A^n_R`` with chosen coordinates ``x_1, ..., x_n``.

    The chosen coordinates are the free generators of the coordinate algebra,
    so an object is ``Spec`` of a polynomial algebra with its generators; the
    same scheme with another coordinate system is another object.
    """

    def analytification(self, scalar_embedding):
        r"""Return affine-space analytification along this base embedding."""
        assert _own_ring(scalar_embedding.domain()) is self.base_ring(), (
            "affine-space analytification is owned by the affine-space category over the embedding source"
        )
        from dzack_research.preamble.categories.schemes.analytic_families import (
            _affine_space_analytification_functor,
        )

        return _affine_space_analytification_functor(scalar_embedding)

    def an_object(self):
        r"""The affine line over the base ring."""
        return self(1)

    def _call_(self, dimension, names=None):
        r"""Construct ``A^n_R`` on the chosen coordinate names, one object for each datum."""
        return _canonical_affine_space(
            self.base_ring(),
            int(_engine_numeral(SageZZ, dimension)),
            _normalized_space_names(names),
        )

    def _repr_object_names(self):
        return f"affine spaces over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Affine().FiniteType().Smooth()]

    class ParentMethods:
        @cached_method
        def picard_group(self):
            r"""Return ``Pic(A^n_k) = 0`` over a field."""
            base = self.scheme_base_ring()
            assert base in OwnedFields(), "the represented affine-space Picard group requires a field base"
            from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups

            return PicardGroups().trivial(self)

        @cached_method
        def class_group(self):
            r"""Return ``Cl(A^n_k) = 0`` over a field."""
            base = self.scheme_base_ring()
            assert base in OwnedFields(), "the represented affine-space class group requires a field base"
            from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            return ClassGroups()(_own_ring(SageZZ).free_module(finite_ordered_set(())), scheme=self)

        def basic_open(self, element):
            r"""Archived spelling for the distinguished open ``D(element)``."""
            return self.distinguished_open(element)

        def zeta_function(self):
            r"""Return ``Z(A^d/F_q, T) = 1/(1 - q^d T)``."""
            base = self.scheme_base_ring()
            assert base in OwnedFields() and base.cardinality().is_finite(), (
                "the arithmetic zeta function here requires a finite field"
            )
            rational_functions, T = _rational_functions_in_T()
            q = int(base.cardinality().finite_value())
            d = int(self.relative_dimension())
            return rational_functions.one() / (rational_functions.one() - q**d * T)


def _rational_functions_in_T():
    r"""The owned rational function field ``QQ(T)`` and its variable ``T``."""
    from sage.rings.rational_field import QQ as SageQQ

    rationals = _own_ring(SageQQ)
    polynomial = rationals.polynomial_ring("T")
    rational_functions = _refine_commutative_algebra(polynomial.fraction_field(), rationals, ("T",))
    return rational_functions, rational_functions.algebra_generator("T")


def _projective_space(base, dimension, names, placements=(), **level_data):
    r"""Construct ``P^n_R = Proj R[x_0, ..., x_n]`` on the chosen homogeneous coordinates.

    The realization is Sage's projective space on the same names; the chosen
    coordinates are the data it is built from.
    """
    engine = _SageProjectiveSpace(int(dimension), _engine_ring(base), names=_normalized_space_names(names))
    return _object_of(
        Category.join((ProjectiveSpaces(base), *_space_placements(base), *placements)),
        scheme_base_ring=base,
        scheme_engine=engine,
        **level_data,
    )


@cached_function(key=lambda base, dimension, names: (id(base), int(dimension), names))
def _canonical_projective_space(base, dimension, names):
    r"""The selected ordinary ``P^n_R`` for one coordinate datum."""
    return _projective_space(base, dimension, names)


class ProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Projective spaces ``P^n_R`` with chosen homogeneous coordinates ``x_0, ..., x_n``."""

    def an_object(self):
        r"""The projective line over the base ring."""
        return self(1)

    def _call_(self, dimension, names=None):
        r"""Construct ``P^n_R`` on the chosen coordinate names, one object for each datum."""
        return _canonical_projective_space(
            self.base_ring(),
            int(_engine_numeral(SageZZ, dimension)),
            _normalized_space_names(names),
        )

    def _repr_object_names(self):
        return f"projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Projective().Smooth()]

    class ParentMethods:
        def variable_names(self):
            r"""The names of the chosen homogeneous coordinates ``x_0, ..., x_n``."""
            return tuple(str(name) for name in _engine_scheme(self).variable_names())

        def coordinate_swap_action(self, group=None):
            r"""Return the C2 action interchanging the two coordinates of this projective line."""
            from dzack_research.preamble.categories.divisors.linearizations import (
                _projective_line_coordinate_swap_action,
            )

            return _projective_line_coordinate_swap_action(self, group)

        @cached_method
        def fan(self):
            r"""Return the owned standard fan of ``P^n``."""
            from dzack_research.preamble.categories.schemes.toric.fans import RationalPolyhedralFans

            lattice = _own_ring(SageZZ).free_module(int(self.relative_dimension()))
            return RationalPolyhedralFans(lattice).projective_space_fan()

        def point_blowup(self, point):
            r"""Blow up this represented projective plane at ``point``."""
            from dzack_research.preamble.categories.schemes.blowups import (
                _projective_point_blowup,
            )

            return _projective_point_blowup(self, point)

        @cached_method
        def divisor_class_theory(
            self,
            base_picard_group=None,
            base_class_group=None,
            base_picard_to_class=None,
        ):
            r"""Return the projective-bundle comparison ``Pic(P^n_S) -> Cl(P^n_S)``.

            Over a nonfield base the base Picard group, base class group and
            their comparison are the data of the projective-bundle formula and
            are supplied together; over a field they are the trivial groups of
            ``Spec k``.
            """
            from dzack_research.preamble.categories.divisors.general_divisors import (
                _projective_space_divisor_class_theory,
            )

            supplied = (base_picard_group, base_class_group, base_picard_to_class)
            match supplied:
                case (None, None, None):
                    base = self.scheme_base_ring()
                    assert base in OwnedFields(), (
                        "the projective-space divisor class groups over a nonfield base require the "
                        "base Picard group, base class group, and their comparison"
                    )
                    from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
                    from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups
                    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

                    zero_module = _own_ring(SageZZ).free_module(finite_ordered_set(()))
                    base_scheme = self.base_scheme()
                    base_picard = PicardGroups().trivial(base_scheme)
                    base_class = ClassGroups()(zero_module, scheme=base_scheme)
                    comparison = base_picard.module_category().Mor(base_picard, base_class)({})
                    return _projective_space_divisor_class_theory(self, base_picard, base_class, comparison)
                case _:
                    assert all(value is not None for value in supplied), (
                        "projective divisor-class theory requires the base Picard group, "
                        "base class group, and their comparison together"
                    )
                    return _projective_space_divisor_class_theory(self, *supplied)

        def picard_group(self, base_picard_group=None):
            r"""Return the represented Picard group of this projective space.

            With no supplied base Picard group, use the field-base divisor-class
            theory.  Supplying ``Pic(S)`` invokes the projective bundle formula
            ``Pic(P^n_S) = Pic(S) direct_sum ZZ[O(1)]``.
            """
            match base_picard_group:
                case None:
                    return self.divisor_class_theory().picard_group()
                case _:
                    from dzack_research.preamble.categories.divisors.general_divisors import (
                        _projective_space_picard_group,
                    )

                    return _projective_space_picard_group(self, base_picard_group)

        def class_group(self):
            return self.divisor_class_theory().class_group()

        def homogeneous_coordinate_generators(self):
            r"""Return the chosen homogeneous coordinate generators of this projective space."""
            return self.O(1).global_sections().homogeneous_coordinate_ring().algebra_generators()

        def hyperplane(self, index=0):
            r"""Return the coordinate hyperplane ``V(x_index)``."""
            return self.closed_subscheme(tuple(self.homogeneous_coordinate_generators())[int(index)])

        def basic_open(self, homogeneous_element):
            r"""Return ``D_+(homogeneous_element)`` as the complement of its zero locus."""
            return self.closed_subscheme(homogeneous_element).open_complement()

        def _standard_chart_coordinate_name(self, chart_index, numerator_index):
            r"""The name of the coordinate ``x_k / x_i`` on the ``i``-th standard chart."""
            return f"x{int(numerator_index)}_over_x{int(chart_index)}"

        def _standard_chart_coordinate(self, chart_index, numerator_index):
            r"""``x_k / x_i`` as a generator of the ``i``-th chart's coordinate algebra."""
            algebra = self.standard_affine_chart(chart_index).coordinate_algebra()
            return algebra.algebra_generator(self._standard_chart_coordinate_name(chart_index, numerator_index))

        @cached_method
        def standard_affine_charts(self):
            r"""The family ``(U_0, ..., U_n)`` of standard affine charts of ``P^n_R``.

            ``U_i = D_+(x_i)`` is the spectrum of the degree-zero part of the
            graded localization at ``x_i``, the polynomial ring on the ``n``
            ratios ``x_k/x_i`` with ``k`` other than ``i``; each chart is affine
            ``n``-space and its coordinate names record which ratio each
            variable is (Stacks, Tag 01M3).
            """
            dimension = int(self.relative_dimension())
            base = self.scheme_base_ring()
            charts = tuple(
                AffineSpaces(base)(
                    dimension,
                    names=tuple(
                        self._standard_chart_coordinate_name(index, numerator)
                        for numerator in range(dimension + 1)
                        if numerator != index
                    ),
                )
                for index in range(dimension + 1)
            )
            return finite_family(charts, name="Standard affine charts")

        def standard_affine_chart(self, index):
            r"""``U_i = D_+(x_i)``, the ``i``-th standard affine chart."""
            return self.standard_affine_charts()[int(index)]

        def standard_chart_overlap(self, chart_index, other_index):
            r"""``U_i cap U_j = D(x_j/x_i)``, an open of the ``i``-th chart."""
            chart = self.standard_affine_chart(chart_index)
            return chart.distinguished_open(self._standard_chart_coordinate(chart_index, other_index))

        def _standard_chart_change(self, source_index, target_index):
            r"""``U_i cap U_j -> U_j cap U_i``, read on coordinates."""
            source_index = int(source_index)
            target_index = int(target_index)
            assert source_index != target_index, "a chart change joins two distinct standard charts"
            dimension = int(self.relative_dimension())
            source_overlap = self.standard_chart_overlap(source_index, target_index)
            target_overlap = self.standard_chart_overlap(target_index, source_index)
            target_chart = self.standard_affine_chart(target_index)
            restriction = source_overlap.inclusion().coordinate_algebra_morphism()
            inverse_ratio = restriction(self._standard_chart_coordinate(source_index, target_index)).inverse_of_unit()
            images = {
                self._standard_chart_coordinate_name(target_index, numerator): (
                    inverse_ratio
                    if numerator == source_index
                    else restriction(self._standard_chart_coordinate(source_index, numerator)) * inverse_ratio
                )
                for numerator in range(dimension + 1)
                if numerator != target_index
            }
            into_target_chart = _scheme_mor_category(source_overlap, target_chart)(
                target_chart.coordinate_algebra().Mor(source_overlap.coordinate_algebra())(images)
            )
            return target_overlap.corestriction(into_target_chart)

        def standard_chart_transition(self, source_index, target_index):
            r"""``phi_{ji}: U_i cap U_j -> U_j cap U_i``, the chart change and its inverse.

            On coordinates ``x_k/x_j = (x_k/x_i)(x_j/x_i)^{-1}`` and
            ``x_i/x_j = (x_j/x_i)^{-1}``, defined because ``x_j/x_i`` is
            invertible on the overlap (Stacks, Tag 01MM).
            """
            return _scheme_isomorphism(
                self._standard_chart_change(source_index, target_index),
                self._standard_chart_change(target_index, source_index),
            )

        def O(self, degree):
            r"""Return the standard invertible sheaf ``O(d)`` on this projective space."""
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                _projective_o,
            )

            return _projective_o(self, degree)

        def coordinate_hyperplane_section_restriction(self, degree, coordinate_index):
            r"""Restrict ``O(degree)`` sections to the selected coordinate hyperplane."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _coordinate_hyperplane_section_restriction,
            )

            return _coordinate_hyperplane_section_restriction(self, degree, coordinate_index)

        def coordinate_point_jet_evaluation(self, degree, coordinate_index, jet_order):
            r"""Evaluate ``O(degree)`` jets at the selected coordinate point."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _coordinate_point_jet_evaluation,
            )

            return _coordinate_point_jet_evaluation(self, degree, coordinate_index, jet_order)

        def sections_vanishing_to_order(self, degree, coordinate_index, vanishing_order):
            r"""Return ``O(degree)`` sections vanishing to the stated order."""
            return self.coordinate_point_jet_evaluation(degree, coordinate_index, vanishing_order).kernel()

        def imposed_multiplicity_linear_system(self, degree, coordinate_index, vanishing_order):
            r"""Projectivize sections satisfying a coordinate-point multiplicity condition."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _coordinate_imposed_multiplicity_linear_system,
            )

            return _coordinate_imposed_multiplicity_linear_system(self, degree, coordinate_index, vanishing_order)

        @cached_method
        def canonical_line_bundle(self):
            r"""Return ``omega_{P^n_R} = O(-n-1)`` in the standard smooth projective regime."""
            return self.O(-int(self.relative_dimension()) - 1)

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            r"""Return ``omega_{P^n_R}^{-1} = O(n+1)``."""
            return self.O(int(self.relative_dimension()) + 1)

        anticanonical_bundle = anticanonical_line_bundle

        @cached_method
        def standard_affine_atlas(self):
            r"""Return the verified standard affine atlas on this exact projective space."""
            from dzack_research.preamble.categories.schemes.gluing import (
                FiniteAffineAtlasPresentation,
            )

            indices = tuple(range(int(self.relative_dimension()) + 1))
            return FiniteAffineAtlasPresentation(
                self,
                tuple(self.standard_affine_chart(index) for index in indices),
                tuple(self.standard_chart_transition(left, right) for left, right in combinations(indices, 2)),
                tuple(_standard_projective_chart_embedding(self, index) for index in indices),
            )

        def glued_from_standard_charts(self):
            r"""``P^n_R`` presented as the gluing of its standard affine charts.

            The atlas verifies the inverse and triple-cocycle conditions on the
            overlaps, so this is the scheme those charts and transitions
            determine (Stacks, Tag 01JA), as opposed to the realized space this
            method is called on.
            """
            indices = range(int(self.relative_dimension()) + 1)
            return Schemes(self.scheme_base_ring()).glue_affine_atlas(
                tuple(self.standard_affine_chart(index) for index in indices),
                tuple(self.standard_chart_transition(left, right) for left, right in combinations(indices, 2)),
            )

        def zeta_function(self):
            r"""Return ``Z(P^d/F_q, T) = prod_{i=0}^d (1 - q^i T)^{-1}``."""
            base = self.scheme_base_ring()
            assert base in OwnedFields() and base.cardinality().is_finite(), (
                "the arithmetic zeta function here requires a finite field"
            )
            rational_functions, T = _rational_functions_in_T()
            q = int(base.cardinality().finite_value())
            d = int(self.relative_dimension())
            result = rational_functions.one()
            for i in range(d + 1):
                result *= rational_functions.one() / (rational_functions.one() - q**i * T)
            return result


def _standard_projective_chart_embedding(projective, chart_index):
    r"""Return the standard open-chart morphism ``U_i -> P^n``.

    The affine chart has coordinates ``x_k/x_i``; its map to projective space
    is the homogeneous family with coordinate ``i`` equal to one and every
    other coordinate the corresponding ratio.
    """
    chart_index = int(chart_index)
    chart = projective.standard_affine_chart(chart_index)
    algebra = chart.coordinate_algebra()
    coordinates = tuple(
        algebra.one() if numerator == chart_index else projective._standard_chart_coordinate(chart_index, numerator)
        for numerator in range(int(projective.relative_dimension()) + 1)
    )
    return _ProjectiveCoordinateMorphism(_scheme_mor_category(chart, projective), coordinates)


# ---------------------------------------------------------------------------
# Products.
# ---------------------------------------------------------------------------


class ProductSchemes(OwnedCategoryOverBaseRing):
    r"""Products ``prod_{i in I} X_i`` of schemes, with their indexed factors and projections.

    The level data are the indexed family of factors and, over the same index
    set, the defining datum of each projection in ``Mor(X, X_i)``; the
    projection arrows are built from those data once the product exists.
    """

    def an_object(self):
        r"""The affine plane as a product of two affine lines."""
        line = AffineSpaces(self.base_ring())(1)
        return _scheme_product(line, line)

    def _repr_object_names(self):
        return f"scheme products over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    class ParentMethods:
        def __init__(self, factors, projection_data, **rest) -> None:
            self._product_factors = factors
            self._projection_data = projection_data
            super().__init__(**rest)

        def factors(self):
            r"""Return the exact indexed family whose product this is."""
            return self._product_factors

        def number_of_factors(self):
            return self.factors().cardinality()

        @cached_method
        def projection(self, index):
            r"""Return the projection to the factor at ``index``."""
            return _scheme_mor_category(self, self.factors()[index])(self._projection_data[index])

        @cached_method
        def projections(self):
            r"""Return the projections, indexed by the same set as :meth:`factors`."""
            return indexed_family(
                self.factors().index_set(),
                self.projection,
                name="Scheme product projections",
            )

        def projection_label(self, projection):
            r"""Return the factor label selected by one of this product's projections."""
            assert projection.domain() is self, "a product projection has this product as its domain"
            label = next(
                (label for label in self.factors().index_set() if projection is self.projection(label)),
                None,
            )
            assert label is not None, "this morphism is not one of the selected product projections"
            return label

        def from_product_cone(self, legs):
            r"""Return the unique represented map into this product.

            The cone carries the index set of the factor family.  An affine
            product factors through the coordinate-algebra coproduct; a product
            of projective spaces concatenates the homogeneous coordinates of
            its legs on Sage's multiprojective realization.  A glued mixed
            product has its projections but no represented map into it.
            """
            factors = self.factors()
            factor_indices = factors.index_set()
            factor_labels = tuple(factor_indices)
            legs = _finite_factor_family(legs, name="Product cone legs")
            assert legs.index_set().cardinality() == factor_indices.cardinality(), "a product cone has one leg per factor"
            source = legs[factor_labels[0]].domain()
            assert all(legs[label].domain() is source for label in factor_labels), "a product cone has one apex"
            assert all(legs[label].codomain() is factors[label] for label in factor_labels), (
                "each leg of a product cone lands in its indexed factor"
            )

            base = self.scheme_base_ring()
            match self:
                case _ if self in Schemes(base).Affine():
                    assert source in Schemes(base).Affine(), "the affine product factorization requires an affine cone apex"
                    product_algebra = self.coordinate_algebra()
                    images = {}
                    for factor_label in factor_labels:
                        leg = legs[factor_label]
                        factor_algebra = factors[factor_label].coordinate_algebra()
                        if factor_algebra is base:
                            assert leg == source.structure_morphism(), (
                                "the cone leg to the terminal base scheme is the structure morphism"
                            )
                            continue
                        projection_pullback = self.projection(factor_label).coordinate_algebra_morphism()
                        leg_pullback = leg.coordinate_algebra_morphism()
                        for generator_label in factor_algebra.algebra_generating_set():
                            generator = factor_algebra.algebra_generator(generator_label)
                            images[_algebra_generator_label(product_algebra, projection_pullback(generator))] = leg_pullback(generator)
                    pullback = (
                        source.structure_morphism().coordinate_algebra_morphism()
                        if product_algebra is base
                        else product_algebra.Mor(source.coordinate_algebra())(images)
                    )
                    cone = _affine_morphism_from_pullback(source, self, pullback)
                case _ if self in ProductProjectiveSpaces(base):
                    coordinate_legs = tuple(_projective_coordinate_morphism(legs[label]) for label in factor_labels)
                    coefficients = coordinate_legs[0].coefficient_map()
                    assert all(_ring_morphisms_equal(coefficients, leg.coefficient_map()) is True for leg in coordinate_legs), (
                        "a product over Spec R has the same coefficient map on every factor"
                    )
                    coordinates = tuple(value for leg in coordinate_legs for value in leg.homogeneous_coordinates())
                    cone = _ProjectiveCoordinateMorphism(
                        LocallyRingedSpaces().Mor(source, self), coordinates, coefficient_map=coefficients,
                    )
                case _:
                    assert False, "a map into a glued mixed scheme product is not represented"

            cone = SchemeConeMorphismConstruction(
                self, legs, (self.projection(index) for index in factors.index_set()),
            ).image_of(cone)
            assert all(self.projection(label) * cone == legs[label] for label in factor_labels), (
                "the product cone map does not recover its legs"
            )
            return cone


def _projective_projection_rule(offset, width, scalar_map=None):
    r"""The arrow realization rule for the projection of a multiprojective space to one factor.

    The projection sends a point to the block of homogeneous coordinates
    ``x_offset, ..., x_{offset + width - 1}``; it is realized on Sage's
    multiprojective space by those coordinates.
    """

    def realize(homset):
        source = homset.domain()
        ambient, _ = _engine_projective_ambient(_engine_scheme(source))
        ring = _engine_polynomial_algebra(ambient.coordinate_ring(), source.scheme_base_ring())
        coordinates = tuple(
            ring._from_engine_element(value)
            for value in ambient.coordinate_ring().gens()[offset : offset + width]
        )
        coefficient_map = None
        if scalar_map is not None:
            structure = _restriction_to_base(ring, scalar_map.codomain())
            coefficient_map = OwnedRings().Mor(scalar_map.domain(), ring).elementwise(
                lambda value: structure(scalar_map(value))
            )
        return _ProjectiveCoordinateMorphism(homset, coordinates, coefficient_map=coefficient_map)

    return realize


class ProductProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Finite products of projective spaces over one base ring, on Sage's multiprojective realization."""

    def an_object(self):
        r"""The product of two projective lines."""
        line = ProjectiveSpaces(self.base_ring())(1)
        return _scheme_product(line, line)

    def _repr_object_names(self):
        return f"products of projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [
            ProductSchemes(self.base_ring()),
            Schemes(self.base_ring()).Projective().Smooth(),
        ]

    class ParentMethods:
        def c2_diagonal_sign_action(self, group=None):
            r"""Return the diagonal sign action on every projective-line factor."""
            from dzack_research.preamble.categories.divisors.linearizations import (
                _c2_diagonal_product_projective_action,
            )

            return _c2_diagonal_product_projective_action(self, group)

        @cached_method
        def standard_affine_atlas(self):
            r"""Return the product of the factors' standard affine atlases."""
            from dzack_research.preamble.categories.schemes.gluing import (
                FiniteAffineAtlasPresentation,
            )

            factors = self.factors()
            factor_indices = factors.index_set()
            factor_labels = tuple(factor_indices)
            positions = {label: position for position, label in enumerate(factor_labels)}
            choices = tuple(
                cartesian_product(*(range(int(factors[label].relative_dimension()) + 1) for label in factor_labels))
            )
            charts = {}
            embeddings = {}
            for choice in choices:
                chart = _scheme_product(
                    indexed_family(
                        factor_indices,
                        lambda label, choice=choice: factors[label].standard_affine_chart(choice[positions[label]]),
                        name="Standard affine factors of a multiprojective chart",
                    )
                )
                charts[choice] = chart
                chart_algebra = chart.coordinate_algebra()
                engine_coordinates = []
                for label in factor_labels:
                    factor = factors[label]
                    selected = choice[positions[label]]
                    pullback = chart.projection(label).coordinate_algebra_morphism()
                    engine_coordinates.extend(
                        _engine_element(
                            chart_algebra,
                            chart_algebra.one()
                            if coordinate == selected
                            else pullback(factor._standard_chart_coordinate(selected, coordinate)),
                        )
                        for coordinate in range(int(factor.relative_dimension()) + 1)
                    )
                embeddings[choice] = _scheme_mor_category(chart, self)(_native_scheme_homset(chart, self)(engine_coordinates, check=False))

            @cached_function
            def overlap(source_choice, target_choice):
                chart = charts[source_choice]
                element = chart.coordinate_algebra().one()
                for label in factor_labels:
                    source_index = source_choice[positions[label]]
                    target_index = target_choice[positions[label]]
                    if source_index != target_index:
                        pullback = chart.projection(label).coordinate_algebra_morphism()
                        element *= pullback(factors[label]._standard_chart_coordinate(source_index, target_index))
                return chart.distinguished_open(element)

            def transition(source_choice, target_choice):
                source_chart = charts[source_choice]
                inclusion = overlap(source_choice, target_choice).inclusion()

                def leg(label):
                    factor = factors[label]
                    source_index = source_choice[positions[label]]
                    target_index = target_choice[positions[label]]
                    local_projection = source_chart.projection(label) * inclusion
                    if source_index == target_index:
                        return local_projection
                    into_factor_overlap = factor.standard_chart_overlap(source_index, target_index).corestriction(local_projection)
                    changed = factor._standard_chart_change(source_index, target_index) * into_factor_overlap
                    return factor.standard_chart_overlap(target_index, source_index).inclusion() * changed

                into_target = charts[target_choice].from_product_cone(
                    indexed_family(factor_indices, leg, name="Coordinatewise multiprojective chart transition legs")
                )
                return overlap(target_choice, source_choice).corestriction(into_target)

            transitions = {
                (left, right): _scheme_isomorphism(transition(left, right), transition(right, left))
                for left, right in combinations(choices, 2)
            }
            return FiniteAffineAtlasPresentation(self, charts, transitions, embeddings)

        def O(self, *degrees):
            r"""Return ``O(d_1, ..., d_r)`` on this product of projective spaces."""
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                ProductProjectiveLineBundle,
            )

            return ProductProjectiveLineBundle(self, _family_ingress(degrees))

        @cached_method
        def canonical_line_bundle(self):
            return self.O(*(-int(factor.relative_dimension()) - 1 for factor in self.factors()))

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            return self.O(*(int(factor.relative_dimension()) + 1 for factor in self.factors()))

        anticanonical_bundle = anticanonical_line_bundle


def _scheme_product(*schemes, placements=(), **level_data):
    r"""Return the categorical product in the supported scheme regimes.

    The defining datum is an indexed family.  Positional arguments and one
    sequence are syntactic ingress for the family on the canonical finite
    ordinal; an explicit :class:`IndexedFamily` keeps its exact index set, so
    repeated factors still have distinct roles.

    Affine spaces use ``A^m x A^n = A^{m+n}``; affine factors use the
    coproduct of their coordinate algebras; projective spaces use Sage's
    multiprojective realization; finite mixtures of affine schemes and
    projective spaces are glued from products of their affine charts.  Every
    route constructs the product with its indexed factors and the data of its
    projections.
    """
    factors = _finite_factor_family(_family_ingress(schemes), name="Product factors")
    index_set = factors.index_set()
    assert index_set.cardinality() >= 2, "a represented scheme product has at least two factors"
    scheme_values = tuple(factors[label] for label in index_set)
    base = scheme_values[0].scheme_base_ring()
    assert all(scheme in Schemes(base) and scheme.scheme_base_ring() is base for scheme in scheme_values), (
        "the factors of a scheme product are schemes over one base"
    )
    rank = index_set.ranking_map()

    def projection_family(values):
        r"""The projection data, indexed by the factor index set in its order."""
        return indexed_family(
            index_set,
            lambda label: values[int(rank(label))],
            name="Scheme product projection data",
        )

    match scheme_values:
        case _ if all(scheme in AffineSpaces(base) for scheme in scheme_values):
            dimensions = tuple(int(scheme.relative_dimension()) for scheme in scheme_values)
            names = tuple(
                f"x{factor}_{coordinate}"
                for factor, dimension in enumerate(dimensions)
                for coordinate in range(dimension)
            )
            coordinates = _affine_space_coordinates(base, sum(dimensions), names)
            product_algebra = coordinates[1]
            product_labels = tuple(product_algebra.algebra_generating_set())
            pullbacks = []
            offset = 0
            for factor, dimension in zip(scheme_values, dimensions, strict=True):
                factor_algebra = factor.coordinate_algebra()
                pullbacks.append(
                    factor_algebra.Mor(product_algebra)(
                        {
                            label: product_algebra.algebra_generator(product_labels[offset + position])
                            for position, label in enumerate(factor_algebra.algebra_generating_set())
                        }
                    )
                )
                offset += dimension
            return _affine_space(
                base,
                coordinates,
                (ProductSchemes(base), *placements),
                factors=factors,
                projection_data=projection_family(pullbacks),
                **level_data,
            )
        case _ if all(scheme in ProjectiveSpaces(base) for scheme in scheme_values):
            widths = tuple(int(scheme.relative_dimension()) + 1 for scheme in scheme_values)
            names = tuple(
                f"x{factor}_{coordinate}"
                for factor, width in enumerate(widths)
                for coordinate in range(width)
            )
            engine = _SageProductProjectiveSpaces(
                [width - 1 for width in widths],
                _engine_ring(base),
                names=names,
            )
            offsets = tuple(sum(widths[:position]) for position in range(len(widths)))
            return _object_of(
                Category.join((ProductProjectiveSpaces(base), *_space_placements(base), *placements)),
                scheme_base_ring=base,
                scheme_engine=engine,
                factors=factors,
                projection_data=projection_family(
                    tuple(_projective_projection_rule(offset, width) for offset, width in zip(offsets, widths, strict=True))
                ),
                **level_data,
            )
        case _ if all(scheme in Schemes(base).Affine() for scheme in scheme_values):
            return _affine_scheme_product(factors, scheme_values, base, projection_family, placements, level_data)
        case _ if all(scheme in Schemes(base).Affine() or scheme in ProjectiveSpaces(base) for scheme in scheme_values):
            return _mixed_affine_projective_product(factors, base, placements, level_data)
        case _:
            assert False, (
                "the represented product supports affine schemes, projective spaces, "
                "and finite mixtures of those regimes"
            )


def _affine_scheme_product(factors, scheme_values, base, projection_family, placements, level_data):
    r"""``Spec(A_1 tensor_R ... tensor_R A_n)`` with the coproduct injections as projection pullbacks.

    ``Spec R`` is terminal in ``Sch/R``: a terminal factor contributes nothing
    to the coordinate algebra and its projection is the structure morphism,
    whose pullback is the algebra structure morphism.
    """
    base_scheme = Schemes(base).base_scheme()
    nonterminal_positions = tuple(position for position, scheme in enumerate(scheme_values) if scheme is not base_scheme)
    commutative_algebras = Algebras(base).Associative().Unital().Commutative()
    match len(nonterminal_positions):
        case 0:
            algebra = base
            maps = []
        case 1:
            algebra = scheme_values[nonterminal_positions[0]].coordinate_algebra()
            maps = [algebra.Mor(algebra).identity()]
        case _:
            algebras = tuple(scheme_values[position].coordinate_algebra() for position in nonterminal_positions)
            algebra = commutative_algebras.coproduct((algebras[0], algebras[1]))
            maps = list(algebra.coproduct_injections())
            for next_algebra in algebras[2:]:
                extended = commutative_algebras.coproduct((algebra, next_algebra))
                left_map, right_map = extended.coproduct_injections()
                maps = [left_map * factor_map for factor_map in maps] + [right_map]
                algebra = extended
    injection_at = dict(zip(nonterminal_positions, maps, strict=True))
    structure_pullback = base.Mor(base).identity() if algebra is base else algebra.algebra_structure_morphism()
    pullbacks = tuple(
        injection_at[position] if position in injection_at else structure_pullback
        for position in range(len(scheme_values))
    )
    return _affine_scheme(
        algebra,
        base,
        (ProductSchemes(base), *placements),
        factors=factors,
        projection_data=projection_family(pullbacks),
        **level_data,
    )


def _mixed_affine_projective_product(factors, base, placements, level_data):
    r"""Glue a finite product containing affine and projective factors.

    For each projective factor choose one standard affine chart.  The product
    of those charts with all affine factors is affine.  Two such product charts
    overlap where every changed homogeneous coordinate ratio is a unit, hence
    on one distinguished open, the product of those ratios.  Coordinatewise
    projective chart changes and identities on the affine factors give the
    finite gluing.  The local factor projections agree on overlaps, so they
    glue to the categorical projections, which are constructed from those
    local maps as the product is glued.
    """
    factors = _finite_factor_family(factors, name="Product factors")
    schemes = tuple(factors)
    projective_positions = tuple(position for position, scheme in enumerate(schemes) if scheme in ProjectiveSpaces(base))
    chart_labels = tuple(cartesian_product(*(range(int(schemes[position].relative_dimension()) + 1) for position in projective_positions)))
    projective_slot = {position: slot for slot, position in enumerate(projective_positions)}
    charts = {
        label: _scheme_product(
            tuple(
                scheme.standard_affine_chart(label[projective_slot[position]]) if position in projective_slot else scheme
                for position, scheme in enumerate(schemes)
            )
        )
        for label in chart_labels
    }

    @cached_function
    def overlap(source_label, target_label):
        chart = charts[source_label]
        element = chart.coordinate_algebra().one()
        for position in projective_positions:
            slot = projective_slot[position]
            if source_label[slot] != target_label[slot]:
                pullback = chart.projection(position).coordinate_algebra_morphism()
                element *= pullback(schemes[position]._standard_chart_coordinate(source_label[slot], target_label[slot]))
        return chart.distinguished_open(element)

    def transition(source_label, target_label):
        source_chart = charts[source_label]
        inclusion = overlap(source_label, target_label).inclusion()
        legs = []
        for position, scheme in enumerate(schemes):
            local_projection = source_chart.projection(position) * inclusion
            if position not in projective_slot or source_label[projective_slot[position]] == target_label[projective_slot[position]]:
                legs.append(local_projection)
                continue
            source_index = source_label[projective_slot[position]]
            target_index = target_label[projective_slot[position]]
            into_factor_overlap = scheme.standard_chart_overlap(source_index, target_index).corestriction(local_projection)
            changed = scheme._standard_chart_change(source_index, target_index) * into_factor_overlap
            legs.append(scheme.standard_chart_overlap(target_index, source_index).inclusion() * changed)
        into_target_chart = charts[target_label].from_product_cone(tuple(legs))
        return overlap(target_label, source_label).corestriction(into_target_chart)

    transitions = tuple(
        _scheme_isomorphism(transition(left, right), transition(right, left))
        for left, right in combinations(chart_labels, 2)
    )
    # The projection to a factor is given chartwise, in the order of the charts
    # of the gluing; on a chart the local projection lands in the factor, or in
    # its standard chart followed by that chart's embedding.
    local_projection_families = tuple(
        tuple(
            _standard_projective_chart_embedding(factor, label[projective_slot[position]]) * charts[label].projection(position)
            if position in projective_slot
            else charts[label].projection(position)
            for label in chart_labels
        )
        for position, factor in enumerate(schemes)
    )

    schemes_over_base = Schemes(base)
    placements = [ProductSchemes(base), *placements]
    placements.extend(
        placement
        for placement in (schemes_over_base.Separated(), schemes_over_base.FiniteType(), schemes_over_base.Smooth())
        if all(factor in placement for factor in schemes)
    )
    # A finite-type affine scheme is quasi-projective and projective spaces are
    # projective, so the product of those is quasi-projective.
    if all(
        factor in schemes_over_base.QuasiProjective()
        or (factor in schemes_over_base.Affine() and factor in schemes_over_base.FiniteType())
        for factor in schemes
    ):
        placements.append(schemes_over_base.QuasiProjective())
    # For products of the standard spaces the charts are polynomial rings over
    # the base, so integral and normal placements are read from the base.
    if all(factor in AffineSpaces(base) or factor in ProjectiveSpaces(base) for factor in schemes):
        placements.extend(_space_placements(base))
    return schemes_over_base.glue_affine_atlas(
        tuple(charts[label] for label in chart_labels),
        transitions,
        placements=tuple(placements),
        factors=factors,
        projection_data=indexed_family(
            factors.index_set(),
            lambda label: local_projection_families[int(factors.index_set().ranking_map()(label))],
            name="Glued product projection data",
        ),
        **level_data,
    )


# ---------------------------------------------------------------------------
# Fibre products.
# ---------------------------------------------------------------------------


class SchemeFiberProductConstruction:
    r"""The selected cospan, projection data, and universal factorization of one pullback.

    ``X x_S Y`` is the limit of the cospan ``X -> S <- Y``.  The construction
    retains the cospan, the defining data of the two projections in
    ``Mor(X x_S Y, X)`` and ``Mor(X x_S Y, Y)``, and the realization of the
    universal factorization: the coordinate-algebra pushout, a factorization
    of pushout cocones, or a factorization of scheme cones.
    """

    def __init__(
        self,
        cospan,
        projection_data,
        *,
        algebra_pushout=None,
        scheme_factorization=None,
        cocone_factorization=None,
    ) -> None:
        left_leg, right_leg = cospan
        assert left_leg.codomain() is right_leg.codomain(), "a fiber-product cospan has one common codomain"
        self._cospan = (left_leg, right_leg)
        self._projection_data = tuple(projection_data)
        assert len(self._projection_data) == 2, "a fiber product has two projections"
        self._algebra_pushout = algebra_pushout
        self._scheme_factorization = scheme_factorization
        self._cocone_factorization = cocone_factorization

    def cospan(self):
        return self._cospan

    def projection_data(self):
        return self._projection_data

    def algebra_pushout(self):
        return self._algebra_pushout

    def scheme_factorization(self):
        return self._scheme_factorization

    def cocone_factorization(self):
        return self._cocone_factorization


class FiberProductSchemes(OwnedCategoryOverBaseRing):
    r"""Schemes constructed as the selected pullback of one cospan.

    The level datum is the :class:`SchemeFiberProductConstruction`.
    """

    def an_object(self):
        r"""``A^1 x_{Spec R} A^1``, the affine plane as a fiber product."""
        line = AffineSpaces(self.base_ring())(1)
        return _scheme_fiber_product(line.structure_morphism(), line.structure_morphism())

    def _repr_object_names(self):
        return f"fiber products of schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    class ParentMethods:
        def __init__(self, fiber_product_construction, **rest) -> None:
            self._fiber_product_construction = fiber_product_construction
            super().__init__(**rest)

        def fiber_product_construction(self):
            r"""Return the selected pullback construction defining this scheme."""
            return self._fiber_product_construction

        def fiber_product_cospan(self):
            return self.fiber_product_construction().cospan()

        def fiber_product_base(self):
            return self.fiber_product_cospan()[0].codomain()

        @cached_method
        def fiber_product_projections(self):
            r"""``(X x_S Y -> X, X x_S Y -> Y)``, built from their defining data."""
            left_leg, right_leg = self.fiber_product_cospan()
            left_datum, right_datum = self.fiber_product_construction().projection_data()
            relative = Schemes(self.scheme_base_ring())
            category = relative if all(
                leg.parent().homset_category().is_subcategory(relative)
                for leg in (left_leg, right_leg)
            ) else LocallyRingedSpaces()
            return (
                category.Mor(self, left_leg.domain())(left_datum),
                category.Mor(self, right_leg.domain())(right_datum),
            )

        def left_projection(self):
            return self.fiber_product_projections()[0]

        def right_projection(self):
            return self.fiber_product_projections()[1]

        def from_pullback_cone(self, left_map, right_map):
            r"""Return the factorization of a cone through this pullback."""
            assert left_map.domain() is right_map.domain(), "a pullback cone has one common source"
            left_projection, right_projection = self.fiber_product_projections()
            assert left_map.codomain() is left_projection.codomain(), "the left pullback-cone map has the wrong codomain"
            assert right_map.codomain() is right_projection.codomain(), "the right pullback-cone map has the wrong codomain"
            construction = self.fiber_product_construction()
            left_leg, right_leg = construction.cospan()
            assert left_leg * left_map == right_leg * right_map, (
                "a pullback cone commutes over the common base"
            )
            scheme_factorization = construction.scheme_factorization()
            cocone_factorization = construction.cocone_factorization()
            match construction:
                case _ if scheme_factorization is not None:
                    factorization = scheme_factorization(left_map, right_map)
                case _ if cocone_factorization is not None:
                    factorization = LocallyRingedSpaces().Mor(left_map.domain(), self)(
                        cocone_factorization(left_map.coordinate_algebra_morphism(), right_map.coordinate_algebra_morphism())
                    )
                case _:
                    algebra_pushout = construction.algebra_pushout()
                    assert algebra_pushout is not None, (
                        "this fiber-product construction has no algebra pushout or selected factorization"
                    )
                    factorization = _affine_morphism_from_pullback(
                        left_map.domain(),
                        self,
                        algebra_pushout.from_pushout_cocone(left_map.coordinate_algebra_morphism(), right_map.coordinate_algebra_morphism()),
                    )
            return SchemeConeMorphismConstruction(
                self, (left_map, right_map), (left_projection, right_projection),
            ).image_of(factorization)


def _structure_morphism_rule(homset):
    r"""The arrow realization rule for the structure morphism of the Hom's domain."""
    return homset(homset.domain().structure_morphism())


def _quotient_base_change_pushout(left_pullback, right_pullback):
    r"""Realize ``A tensor_T T/I`` as ``A/IA`` in the represented quotient regime.

    This is the affine algebra realization for base change along a quotient of
    the scalar ring, used when the general algebra pushout does not own the
    span because ``T/I`` has no selected algebra framing.  The quotient
    presentation supplies the pushout object, its two canonical maps, and the
    universal cocone factorization.  ``None`` states that the span is not of
    this shape.
    """
    base = left_pullback.domain()
    assert right_pullback.domain() is base, "a quotient base-change span has one scalar source"

    def realize(other_pullback, quotient_pullback, quotient_on_right):
        other = other_pullback.codomain()
        quotient = quotient_pullback.codomain()
        if quotient not in QuotientRings() or quotient.quotient_source() is not base:
            return None
        if other not in AlgebrasWithChosenFinitePresentation(base):
            return None
        equations = tuple(other_pullback(generator) for generator in quotient.defining_ideal().ideal_generators())
        pushout, other_to_pushout = other._quotient_by_algebra_elements(equations)
        engine_quotient_to_pushout = _engine_ring(pushout).coerce_map_from(_engine_ring(quotient))
        assert engine_quotient_to_pushout is not None, (
            f"the quotient {quotient} has no canonical map into the presented pushout {pushout}"
        )
        quotient_to_pushout = quotient.Mor(pushout)(engine_quotient_to_pushout)
        maps = (other_to_pushout, quotient_to_pushout) if quotient_on_right else (quotient_to_pushout, other_to_pushout)

        def factor(left_to_target, right_to_target):
            assert left_to_target.codomain() is right_to_target.codomain(), "a pushout cocone has one common codomain"
            other_to_target = left_to_target if quotient_on_right else right_to_target
            return pushout.Mor(other_to_target.codomain())(
                {label: other_to_target(other.algebra_generator(label)) for label in pushout.algebra_generating_set()}
            )

        return pushout, maps[0], maps[1], factor

    represented = realize(left_pullback, right_pullback, True)
    return represented if represented is not None else realize(right_pullback, left_pullback, False)


def _projective_base_change_factorization(changed, projective_map, scalar_map):
    r"""The map to the changed projective presentation defined by both cone legs.

    The coordinate sections come from the map to the original presentation;
    coefficients act through the specified map to the changed scalar base.
    On a glued apex the construction is applied on its affine charts.
    """
    source = projective_map.domain()
    if source._is_glued_from_affine_atlas():
        datum = source.gluing_datum()
        return LocallyRingedSpaces().Mor(source, changed)(
            indexed_family(
                datum.chart_index_set(),
                lambda index: _projective_base_change_factorization(
                    changed, projective_map * datum.chart_embedding(index),
                    scalar_map * datum.chart_embedding(index),
                ),
                name="Local projective base-change factorizations",
            )
        )
    coordinates = _projective_coordinate_morphism(projective_map)
    ring = coordinates.coefficient_map().codomain()
    if source in Schemes(source.scheme_base_ring()).Affine():
        coefficients = scalar_map.coordinate_algebra_morphism()
    else:
        assert scalar_map == source.structure_morphism(), (
            "a non-affine polynomial cone uses its stated scalar structure; "
            "an arbitrary non-affine cone requires its affine atlas"
        )
        coefficients = _restriction_to_base(ring, changed.scheme_base_ring())
    return _ProjectiveCoordinateMorphism(
        LocallyRingedSpaces().Mor(source, changed),
        tuple(coordinates.homogeneous_coordinates()), coefficient_map=coefficients,
    )


def _projective_space_scalar_base_change(left_map, right_map):
    r"""Realize the pullback of ``P^n_R`` along ``Spec R' -> Spec R``.

    ``None`` states that the cospan is not this specialization.  The result is
    projective space over ``R'`` on the same coordinates, constructed as the
    fibre product with its projection to ``P^n_R``, its structure morphism to
    ``Spec R'``, and a factorization of cones.
    """
    base_scheme = left_map.codomain()
    if right_map.codomain() is not base_scheme:
        return None
    for projective_leg, scalar_leg, projective_on_left in ((left_map, right_map, True), (right_map, left_map, False)):
        projective = projective_leg.domain()
        scalar_scheme = scalar_leg.domain()
        source_base = projective.scheme_base_ring()
        if (projective not in ProjectiveSpaces(source_base)
                or base_scheme is not projective.base_scheme()
                or projective_leg != projective.structure_morphism()):
            continue
        if scalar_scheme is not scalar_scheme.base_scheme():
            continue
        target_base = scalar_scheme.scheme_base_ring()
        width = int(projective.relative_dimension()) + 1
        projective_projection = _projective_projection_rule(0, width, scalar_leg.coordinate_algebra_morphism())
        projection_data = (
            (projective_projection, _structure_morphism_rule)
            if projective_on_left
            else (_structure_morphism_rule, projective_projection)
        )

        def factor(left_cone_map, right_cone_map, projective_on_left=projective_on_left):
            projective_cone_map = left_cone_map if projective_on_left else right_cone_map
            scalar_cone_map = right_cone_map if projective_on_left else left_cone_map
            return _projective_base_change_factorization(changed, projective_cone_map, scalar_cone_map)

        changed = _projective_space(
            target_base,
            width - 1,
            projective.variable_names(),
            (FiberProductSchemes(target_base),),
            fiber_product_construction=SchemeFiberProductConstruction(
                (left_map, right_map),
                projection_data,
                scheme_factorization=factor,
            ),
        )
        # The projection retains the scalar leg, even for an endomorphism
        # of the same scalar ring; neither projective space is mutated.
        return changed
    return None


def _scheme_fiber_product(left_map, right_map):
    r"""Return ``X x_S Y`` in the represented affine and scalar-projective regimes."""
    assert left_map.codomain() is right_map.codomain(), "fiber-product maps have one common codomain"
    projective_base_change = _projective_space_scalar_base_change(left_map, right_map)
    if projective_base_change is not None:
        return projective_base_change

    left = left_map.domain()
    right = right_map.domain()
    base_scheme = left_map.codomain()
    # Scalar base change includes noncanonical maps and endomorphisms of R.
    # Choose it before the coproduct shortcut for two R-linear structure maps.
    for scheme_leg, scalar_leg, on_left in ((left_map, right_map, True), (right_map, left_map, False)):
        scheme = scheme_leg.domain()
        scalar_scheme = scalar_leg.domain()
        if (scheme in Schemes(scheme.scheme_base_ring()).Affine()
                and scheme_leg.codomain() is scheme.base_scheme()
                and scalar_scheme is scalar_scheme.base_scheme()
                and scheme_leg == scheme.structure_morphism()):
            functor = Schemes(scheme.scheme_base_ring()).base_change_functor(scalar_leg.coordinate_algebra_morphism())
            return functor._affine_object(scheme, cospan=(left_map, right_map), scheme_on_left=on_left)
    base_ring = left.scheme_base_ring()
    affine = Schemes(base_ring).Affine()
    assert left in affine and right in affine and base_scheme in affine, (
        "the scheme fiber-product realization requires affine schemes"
    )
    left_pullback = left_map.coordinate_algebra_morphism()
    right_pullback = right_map.coordinate_algebra_morphism()
    commutative_algebras = Algebras(base_ring).Associative().Unital().Commutative()
    match base_scheme:
        case _ if (base_scheme is left.base_scheme()
                   and left_map.parent().homset_category().is_subcategory(Schemes(base_ring))
                   and right_map.parent().homset_category().is_subcategory(Schemes(base_ring))):
            # Spec R is terminal in Sch/R, so both legs are structure morphisms
            # and the span sits under R, the initial object of CAlg_R: the
            # pushout is the coproduct A tensor_R B with its own factorization.
            algebra_pushout = commutative_algebras.coproduct((left.coordinate_algebra(), right.coordinate_algebra()))
            left_pushout_map, right_pushout_map = algebra_pushout.coproduct_injections()
            cocone_factorization = algebra_pushout.from_cocone
        case _:
            quotient_base_change = _quotient_base_change_pushout(left_pullback, right_pullback)
            match quotient_base_change:
                case None:
                    algebra_pushout = commutative_algebras.pushout(left_pullback, right_pullback)
                    left_pushout_map = algebra_pushout.left_pushout_map()
                    right_pushout_map = algebra_pushout.right_pushout_map()
                    cocone_factorization = None
                case _:
                    algebra_pushout, left_pushout_map, right_pushout_map, cocone_factorization = quotient_base_change
    return _affine_scheme(
        algebra_pushout,
        base_ring,
        (FiberProductSchemes(base_ring),),
        fiber_product_construction=SchemeFiberProductConstruction(
            (left_map, right_map),
            (left_pushout_map, right_pushout_map),
            algebra_pushout=algebra_pushout,
            cocone_factorization=cocone_factorization,
        ),
    )


# ---------------------------------------------------------------------------
# Subobjects of a scheme.
# ---------------------------------------------------------------------------


class _SchemeSubobjectsOf(OwnedParameterizedCategory):
    r"""Subobjects of one scheme ``X``, by the kind of immersion they carry.

    A subobject is the pair ``(Z, i: Z -> X)``.  The level data are the
    codomain ``X`` and the defining datum of ``i`` in ``Mor(Z, X)``; ``i`` is
    built from them once ``Z`` exists, because an arrow cannot be constructed
    before its domain.
    """

    def base_object(self):
        r"""Return the scheme these subobjects are subobjects of."""
        return self.base()

    def _repr_object_names(self) -> str:
        return f"{self.immersion_name} into {self.base_object()}"

    def super_categories(self):
        return [Schemes(self.base_object().scheme_base_ring()).SubobjectCategory(self.base_object())]

    class ParentMethods:
        def __init__(self, inclusion_codomain, inclusion_datum, **rest) -> None:
            self._inclusion_codomain = inclusion_codomain
            self._inclusion_datum = inclusion_datum
            super().__init__(**rest)

        @cached_method
        def inclusion(self):
            r"""Return the chosen monomorphism ``i: Z -> X`` representing this subobject.

            The scheme it sits inside is ``i.codomain()`` and is never separate
            data.
            """
            return _scheme_mor_category(self, self._inclusion_codomain)(self._inclusion_datum)


def _distinguished_overlap_transition(left_chart, left_element, right_chart, right_element):
    r"""The isomorphism ``D_i(f_j) -> D_j(f_i)`` of the two presentations of ``D(f_i f_j)``.

    For ``left_chart = D(f_i)`` and ``right_chart = D(f_j)`` inside one affine
    scheme, the overlap is the locus where both elements are units.  It is
    presented once over each chart, and the two presentations are compared by
    the universal property alone: a map into ``D(f_j)`` is a map into ``X``
    inverting ``f_j``, so each direction is the corestriction of one overlap's
    inclusion through the other chart and then through the other overlap.
    """
    left_overlap = left_chart.distinguished_open(right_element)
    right_overlap = right_chart.distinguished_open(left_element)
    return _scheme_isomorphism(
        right_overlap.corestriction(right_chart.corestriction(left_chart.inclusion() * left_overlap.inclusion())),
        left_overlap.corestriction(left_chart.corestriction(right_chart.inclusion() * right_overlap.inclusion())),
    )


class ClosedEmbeddings(_SchemeSubobjectsOf):
    r"""Subobjects of ``X`` whose inclusion is a closed immersion.

    For affine \(X=\operatorname{Spec}A\) this is
    \(\operatorname{Spec}(A/I)\hookrightarrow X\), induced by the quotient
    \(A\twoheadrightarrow A/I\).  The level datum is the finite family of
    equations cutting the subscheme out.
    """

    immersion_name = "closed embeddings"

    def an_object(self):
        r"""The coordinate axis, cut out by the first coordinate of ``X``."""
        base_object = self.base_object()
        first = next(iter(base_object.coordinate_algebra().algebra_generators()))
        return base_object.closed_subscheme(first)

    class ParentMethods:
        def __init__(self, defining_equations=None, **rest) -> None:
            self._defining_equations = defining_equations
            super().__init__(**rest)

        def defining_equations(self):
            r"""The supplied global equation family; chartwise presentations keep their local ideals."""
            assert self._defining_equations is not None, (
                "this closed immersion is presented chartwise, not by a global equation family"
            )
            return self._defining_equations

        def codimension(self):
            r"""``dim X - dim Z``; for affine ``X`` the codimension of the defining ideal."""
            codomain = self.inclusion().codomain()
            match codomain:
                case _ if codomain in Schemes(codomain.scheme_base_ring()).Affine():
                    ideal_engine = self.defining_ideal_owned()._engine_ideal()
                    return int(_engine_ring(codomain.coordinate_algebra()).krull_dimension() - ideal_engine.dimension())
                case _:
                    return codomain.dimension() - self.dimension()

        def homogeneous_defining_equations(self, coordinate_ring):
            r"""Raise projective defining equations into a selected owned coordinate algebra."""
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            assert codomain in ProjectiveSpaces(base), "homogeneous defining equations require a projective-space codomain"
            assert coordinate_ring.base_ring() is base, "homogeneous coordinates and the projective codomain share a scalar base"
            engine_target = _engine_ring(coordinate_ring)
            target_variables = tuple(engine_target.gens())
            return finite_family(
                tuple(
                    coordinate_ring._from_engine_element(
                        _copy_polynomial_by_exponents(
                            _engine_element(equation.parent(), equation),
                            engine_target,
                            target_variables,
                        )
                    )
                    for equation in self.defining_equations()
                ),
                name=f"Homogeneous defining equations of {self}",
            )

        @cached_method
        def defining_ideal_owned(self):
            r"""Return the ideal generated by the equations cutting this subscheme out.

            For affine ``X = Spec A`` it is an ideal of ``A``; for a projective
            ``X`` it is the homogeneous ideal the equations generate in the
            ring they are written in.  The ideal is derived from the equations
            when asked for: its module presentation is a separate question.
            """
            codomain = self.inclusion().codomain()
            equations = tuple(self.defining_equations())
            match codomain:
                case _ if codomain in Schemes(codomain.scheme_base_ring()).Affine():
                    return codomain.coordinate_algebra().ideal(*equations)
                case _:
                    return equations[0].parent().ideal(*equations)

        def is_empty(self) -> bool:
            r"""Return whether this closed subscheme is empty."""
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            match codomain:
                case _ if codomain in Schemes(base).Affine():
                    return self.defining_ideal_owned().contains_ambient_element(codomain.coordinate_algebra().one())
                case _ if codomain in Schemes(base).Projective():
                    # Sage's projective dimension is -1 exactly for the empty Proj.
                    return int(self.dimension()) < 0
                case _:
                    assert False, "emptiness of this closed subscheme has no selected computation"

        def corestriction(self, morphism):
            r"""The factorization ``T -> Z`` of a morphism ``T -> X`` landing in ``Z``.

            In the affine case the factor is induced by the quotient coordinate
            algebra.  For a homogeneous-coordinate morphism into projective
            space, the coordinates factor through ``Z`` exactly when every
            homogeneous defining equation vanishes on them, and the factor
            retains those coordinates in ``Mor(T, Z)``.
            """
            codomain = self.inclusion().codomain()
            assert morphism.codomain() is codomain, "a corestriction is taken of a morphism into the codomain of the inclusion"
            source = morphism.domain()
            base = source.scheme_base_ring()
            match source:
                case _ if source in Schemes(base).Affine() and self in Schemes(base).Affine():
                    pullback = morphism.coordinate_algebra_morphism()
                    assert all(pullback(equation) == source.coordinate_algebra().zero() for equation in self.defining_equations()), (
                        f"{morphism} does not factor through {self}: its pullback does not kill the defining equations"
                    )
                    algebra = self.coordinate_algebra()
                    factor = _scheme_mor_category(source, self)(
                        algebra.Mor(source.coordinate_algebra())(
                            {label: pullback(codomain.coordinate_algebra().algebra_generator(label)) for label in algebra.algebra_generating_set()}
                        )
                    )
                    assert self.inclusion() * factor == morphism, "the corestriction does not recover the morphism through the inclusion"
                    return factor
                case _ if codomain in ProjectiveSpaces(base):
                    coordinates = tuple(morphism.homogeneous_coordinates())
                    target_ring = codomain.O(1).global_sections().homogeneous_coordinate_ring()
                    assert all(
                        _evaluate_owned_homogeneous_polynomial_on_coordinates(equation, target_ring, coordinates).is_zero()
                        for equation in self.homogeneous_defining_equations(target_ring)
                    ), f"{morphism} does not factor through {self}: a homogeneous defining equation does not vanish"
                    return _ProjectiveCoordinateMorphism(_scheme_mor_category(source, self), coordinates)
                case _:
                    assert False, (
                        "the closed corestriction supports affine maps, or homogeneous-coordinate maps into projective space"
                    )

        def intersection(self, other):
            r"""``Z cap W = V(I + J)``, the scheme-theoretic intersection in ``X``.

            It is the fibre product ``Z x_X W`` (Stacks, Tag 0C4H): a morphism
            into ``X`` factors through it exactly when its pullback kills both
            ideals.
            """
            codomain = self.inclusion().codomain()
            assert other.inclusion().codomain() is codomain, "a scheme-theoretic intersection is taken inside one scheme"
            return codomain.closed_subscheme((*self.defining_equations(), *other.defining_equations()))

        @cached_method
        def O(self, degree):
            r"""Return ``O_Z(d) = i^* O_P(d)`` for a closed subscheme of projective space."""
            codomain = self.inclusion().codomain()
            assert codomain in ProjectiveSpaces(self.scheme_base_ring()), "O_Z(d) here requires a projective-space codomain"
            return codomain.O(degree).restrict_to(self)

        def fundamental_cycle(self):
            r"""Return this closed subscheme's cycle with generic local multiplicities."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _fundamental_cycle,
            )

            return _fundamental_cycle(self)

        def proper_pushforward_cycle(self, cycle):
            r"""Push ``cycle`` forward along this closed immersion."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _closed_immersion_cycle_pushforward,
            )

            return _closed_immersion_cycle_pushforward(self, cycle)

        def serre_intersection(self, other, point):
            r"""Return the local Tor intersection with ``other`` at ``point``."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _serre_intersection,
            )

            return _serre_intersection(self, other, point)

        def serre_intersection_multiplicity(self, other, point):
            r"""Return Serre's alternating Tor-length intersection multiplicity."""
            return self.serre_intersection(other, point).multiplicity()

        def intersection_multiplicity(self, other, point):
            r"""``i(p; Z . W)``, the multiplicity of the intersection at ``p``.

            For two effective hypersurfaces meeting properly in a smooth affine
            surface over a field, this is ``length_{O_{X,p}} O_{X,p}/(f,g)``.
            The polynomial realization computes a primary decomposition of
            ``(f,g)``; the component whose radical is the maximal ideal of ``p``
            is the local Artinian factor ``Q_p``, and
            ``dim_k(P/Q_p) = length(P_p/Q_p P_p) [kappa(p):k]``, so dividing by
            the residue degree returns the composition length even at a
            nonrational closed point.  Outside the proper hypersurface case the
            intersection product is Serre's alternating Tor length.
            """
            codomain = self.inclusion().codomain()
            assert other.inclusion().codomain() is codomain, "an intersection multiplicity is taken inside one scheme"
            base = codomain.scheme_base_ring()
            assert base in OwnedFields(), "the colength formula requires an affine surface over a field"
            assert codomain in AffineSpaces(base) and int(codomain.relative_dimension()) == 2, "the intersection multiplicity requires a smooth affine surface"
            assert self.codimension() == other.codimension() == 1, "the local colength formula requires two hypersurfaces"
            assert self.defining_equations().cardinality() == 1 and other.defining_equations().cardinality() == 1, (
                "each hypersurface has one defining equation"
            )
            spectrum = codomain.underlying_space()
            match point.parent():
                case _ if point.parent() is spectrum:
                    pass
                case _:
                    point = spectrum(point)
            point_ideal = point.ideal()
            assert point_ideal.is_maximal(), "intersection multiplicity here is taken at a closed point"
            backend_meeting = self.intersection(other).defining_ideal_owned()._engine_ideal()
            backend_point = point_ideal._engine_ideal()
            local_components = tuple(
                component for component in backend_meeting.primary_decomposition() if component.radical() == backend_point
            )
            match len(local_components):
                case 0:
                    return _own_ring(SageZZ).zero()
                case 1:
                    component = local_components[0]
                case _:
                    assert False, "a zero-dimensional primary decomposition has one component at the selected point"
            assert int(component.dimension()) == 0, "the two hypersurfaces do not meet properly at the selected point"
            colength = SageZZ(component.vector_space_dimension())
            residue_degree = SageZZ(backend_point.vector_space_dimension())
            assert residue_degree > 0 and colength % residue_degree == 0, (
                "the local primary colength is incompatible with the selected residue field"
            )
            return _own_ring(SageZZ)(colength // residue_degree)

        def ideal_sheaf(self):
            r"""``I_Z = I~``, the quasi-coherent ideal sheaf of ``Z = V(I)`` on affine ``X``."""
            codomain = self.inclusion().codomain()
            assert codomain in Schemes(codomain.scheme_base_ring()).Affine(), "the ideal sheaf is represented on an affine scheme"
            return codomain.associated_module_sheaf(self.defining_ideal_owned())

        def open_complement(self):
            r"""``X - Z``, the open subscheme on which the ideal of ``Z`` is the unit ideal.

            A prime of ``X = Spec A`` lies outside ``Z = V(I)`` exactly when it
            fails to contain some ``f in I``, so the complement is the union of
            the ``D(f_i)`` for the equations ``f_i`` cutting ``Z`` out.  A single
            equation gives the affine ``D(f)``; several give the scheme glued
            from the ``D(f_i)`` along ``D(f_i f_j)``, whose inclusion is given
            chartwise by the inclusions of the ``D(f_i)``.

            For a projective ``X`` the complement is Sage's quasi-projective
            subscheme ``X - Z``, and its inclusion is defined by ``Z``.
            """
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            match codomain:
                case _ if codomain in Schemes(base).Projective():
                    return _object_of(
                        Category.join((OpenImmersions(codomain), Schemes(base).QuasiProjective())),
                        scheme_base_ring=base,
                        scheme_engine=_SageAlgebraicSchemeSubscheme.complement(_engine_scheme(self), _engine_scheme(codomain)),
                        inclusion_codomain=codomain,
                        inclusion_datum=_open_complement_inclusion(self),
                    )
                case _ if codomain in Schemes(base).Affine():
                    equations = self.defining_equations()
                    indices = equations.index_set()
                    charts = {index: codomain.distinguished_open(equations[index]) for index in indices}
                    match equations.cardinality():
                        case 0:
                            return codomain.distinguished_open(codomain.coordinate_algebra().zero())
                        case 1:
                            return charts[next(iter(indices))]
                        case _:
                            return Schemes(base).glue_affine_atlas(
                                charts,
                                {
                                    (left, right): _distinguished_overlap_transition(
                                        charts[left], equations[left], charts[right], equations[right]
                                    )
                                    for left, right in combinations(tuple(indices), 2)
                                },
                                placements=(OpenImmersions(codomain),),
                                inclusion_codomain=codomain,
                                inclusion_datum={index: chart.inclusion() for index, chart in charts.items()},
                            )
                case _:
                    assert False, "the open complement is represented in an affine or projective scheme"


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Closed subschemes of schemes over ``R``: a scheme with its closed immersion.

    ``ClosedEmbeddings(X)`` is the fibre of this category over one scheme
    ``X``; this category collects those fibres over all ``R``-schemes so that
    being a closed subscheme is a placement a session can ask without naming
    the codomain of the immersion.  Its objects are constructed in both.
    """

    def an_object(self):
        r"""The origin of the affine line."""
        line = AffineSpaces(self.base_ring())(1)
        return line.closed_subscheme(next(iter(line.coordinate_algebra().algebra_generators())))

    def _repr_object_names(self):
        return f"closed subschemes of schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]


class OpenImmersions(_SchemeSubobjectsOf):
    r"""Subobjects of ``X`` whose inclusion is an open immersion.

    ``X.distinguished_open(f)`` builds ``D(f) = Spec A_f`` here, included by
    ``Spec`` of the localization map ``A -> A_f``.  The element ``f`` is not a
    function of the open subscheme (``D(f) = D(uf) = D(f^2)``); it is the
    localization datum the coordinate algebra ``A_f`` retains, and the
    operations below that need it read it there.
    """

    immersion_name = "open immersions"

    def an_object(self):
        r"""\(D(f)\) for ``f`` the first coordinate of ``X``."""
        base_object = self.base_object()
        return base_object.distinguished_open(next(iter(base_object.coordinate_algebra().algebra_generators())))

    class ParentMethods:
        def is_distinguished_open(self):
            r"""Whether this open is ``D(f)`` for an element ``f`` of the coordinate algebra of its affine codomain.

            An affine open whose coordinate algebra is the localization of the
            codomain's coordinate algebra at one element is that element's
            ``D(f)``.  Whether an open presented otherwise equals some ``D(f)``
            is whether its closed complement is ``V(f)`` up to radical, which is
            not decided here, and the answer is then ``Unknown``.
            """
            codomain = self.inclusion().codomain()
            affine = Schemes(codomain.scheme_base_ring()).Affine()
            match self:
                case _ if (
                    codomain in affine
                    and self in affine
                    and self.coordinate_algebra() in LocalizationRings()
                    and self.coordinate_algebra().localization_source() is codomain.coordinate_algebra()
                    and self.coordinate_algebra().inverted_elements().cardinality() == 1
                ):
                    return True
                case _:
                    return Unknown

        def distinguished_open_element(self):
            r"""The element ``f`` with this open equal to ``D(f)``, read from its coordinate algebra ``A_f``."""
            assert self.is_distinguished_open() is True, (
                "a defining element is read from an open whose coordinate algebra is a localization "
                "of the codomain's coordinate algebra at one element"
            )
            return self.coordinate_algebra().inverted_element()

        def contains_image_of(self, morphism):
            r"""Whether ``g: T -> X`` lands in this open ``U <= X``, that is, factors through ``U``.

            An open immersion ``U -> X`` is a monomorphism, and ``g`` factors
            through it exactly when the image of ``g`` lies in ``U``.  For
            ``U = D(f)`` and ``T`` affine that is ``g^#(f)`` being a unit of
            ``O(T)``, by the universal property of ``A_f`` (Stacks, Tag 01HR);
            that is the case decided here.
            """
            codomain = self.inclusion().codomain()
            assert morphism.codomain() is codomain, "a morphism lands in an open of its own codomain"
            source = morphism.domain()
            assert self.is_distinguished_open() is True and source in Schemes(source.scheme_base_ring()).Affine(), (
                "whether a morphism lands in an open is decided for a distinguished open and an affine source"
            )
            defining_element = codomain.coordinate_algebra()(self.distinguished_open_element())
            return source.coordinate_algebra()(morphism.coordinate_algebra_morphism()(defining_element)).is_unit()

        def corestriction(self, morphism):
            r"""The factorization ``T -> U`` of a morphism ``g: T -> X`` landing in this open ``U``.

            It exists exactly when :meth:`contains_image_of` holds, and it is
            unique because the inclusion is a monomorphism.  For ``U = D(f)``
            the universal property of ``A_f`` sends ``a/f^k`` to
            ``g^#(a) g^#(f)^{-k}`` (Stacks, Tag 01HR).
            """
            assert self.contains_image_of(morphism), (
                "the morphism does not land in this open: it does not send the defining element to a unit"
            )
            source = morphism.domain()
            factor = _scheme_mor_category(source, self)(
                self.coordinate_algebra().induced_morphism(morphism.coordinate_algebra_morphism())
            )
            assert self.inclusion() * factor == morphism, "the corestriction does not recover the morphism through the inclusion"
            return factor

        def inclusion_into(self, larger_open):
            r"""The open immersion ``D(g) -> D(f)`` when ``D(g) <= D(f)`` in one affine scheme.

            Its pullback is the map ``A_f -> A_g`` the universal property of
            the localization gives, which exists exactly when ``f`` is a unit on
            ``D(g)``; it is the restriction of the structure sheaf, and composed
            with the inclusion of ``D(f)`` it is the inclusion of ``D(g)``.
            """
            from dzack_research.preamble.categories.schemes.ringed_spaces import (
                _localization_restriction_map,
            )

            codomain = self.inclusion().codomain()
            assert larger_open.inclusion().codomain() is codomain, "an inclusion between distinguished opens is taken in one affine scheme"
            restriction = _localization_restriction_map(larger_open.coordinate_algebra(), self.coordinate_algebra())
            inclusion = _scheme_mor_category(self, larger_open)(restriction)
            assert larger_open.inclusion() * inclusion == self.inclusion(), (
                "the inclusion between distinguished opens does not compose to the inclusion into the scheme"
            )
            return inclusion

        def flat_pullback_cycle(self, cycle):
            r"""Pull ``cycle`` back along this flat open immersion."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _distinguished_open_cycle_pullback,
            )

            return _distinguished_open_cycle_pullback(self, cycle)


class SchemeMonomorphisms(_MonoCategoryOf):
    r"""Monomorphisms of schemes.

    A closed immersion and an open immersion are monomorphisms.  Which of the
    two an inclusion is, is placed where the subobject is constructed, and
    this reads that placement; a glued chart embedding is a monomorphism
    because it factors as an isomorphism onto an open subscheme followed by its
    inclusion.  Injectivity on points is neither necessary nor sufficient for a
    scheme monomorphism.
    """

    def accepts(self, arrow) -> bool:
        codomain = arrow.codomain()
        source = arrow.domain()
        match source:
            case _ if source in ClosedEmbeddings(codomain):
                return arrow is source.inclusion()
            case _:
                return arrow.is_open_immersion()


__all__ = [
    "AffineSchemes",
    "AffineSpaces",
    "ClosedEmbeddings",
    "ClosedSubschemes",
    "FiberProductSchemes",
    "IntegralSchemes",
    "NormalSchemes",
    "OpenImmersions",
    "ProjectiveSchemes",
    "ProjectiveSpaces",
    "ProductProjectiveSpaces",
    "ProductSchemes",
    "SchemeMonomorphisms",
    "Schemes",
    "SchemeMorphism",
    "SmoothSchemes",
]

Schemes._MonoCategory = SchemeMonomorphisms
