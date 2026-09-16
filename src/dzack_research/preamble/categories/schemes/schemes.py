"""Owned categories and basic constructors for schemes over a base ring."""

from itertools import combinations
from itertools import product as cartesian_product
from typing import Any, cast

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.affine.affine_space import AffineSpace as _SageAffineSpace
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as _SageAlgebraicSchemeSubscheme
from sage.schemes.generic.scheme import AffineScheme as _SageAffineScheme
from sage.schemes.generic.scheme import Scheme as _SageScheme
from sage.schemes.product_projective.space import (
    ProductProjectiveSpaces as _SageProductProjectiveSpaces,
)
from sage.schemes.projective.projective_space import (
    ProjectiveSpace as _SageProjectiveSpace,
)
from sage.structure.category_object import CategoryObject

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
    AlgebrasWithChosenFinitePresentation,
    Algebras,
    FramedAlgebras,
    _engine_algebra_morphism,
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
    OwnedPrincipalIdealDomains,
    RingMorphism,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _own_ring,
    _proper_restriction_base_ring,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    LocallyRingedSpaces,
    SchemeUnderlyingSpace,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import realize_owned_category

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

_SCHEME_MORPHISM_WRAPPERS = {}
_AFFINE_SPECTRA = {}


def _elements_determining_maps_out_of(algebra, base):
    r"""Elements of ``algebra`` on which two base-ring maps out of it already agree.

    A map out of a framed ``R``-algebra is fixed by the images of its algebra
    generators together with its restriction to ``R``.  When the represented
    scheme base is a smaller ring ``k``, determine that restriction recursively
    from a finite family for ``R/k`` and carry those scalars into the algebra by
    its structure morphism.  A map out of ``S^{-1}A`` is fixed by its
    restriction along ``A -> S^{-1}A``, so localization towers recurse to the
    framed algebra at their foot.  ``None`` says no represented finite
    determining family is available.
    """
    if algebra is base:
        return ()

    algebra_base = getattr(algebra, "algebra_base_ring", lambda: None)()
    if algebra_base is not None and algebra in FramedAlgebras(algebra_base):
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

    if algebra in LocalizationRings():
        if algebra is base:
            return ()
        if base in LocalizationRings():
            if algebra.localization_source() is base:
                return ()
            if algebra.localization_source() is base.localization_source():
                try:
                    base.restriction_to(algebra)
                except (AssertionError, NotImplementedError, TypeError, ValueError):
                    pass
                else:
                    return ()
        below = _elements_determining_maps_out_of(algebra.localization_source(), base)
        if below is None:
            return None
        localization_map = algebra.localization_map()
        return tuple(localization_map(element) for element in below)
    return None


class SchemeMorphism(Morphism):
    r"""Categorical wrapper around one native Sage scheme morphism."""

    _coordinate_pullback = None

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
            self._coordinate_pullback = pullback
        if homset is None:
            if (domain is None) != (codomain is None):
                raise ValueError("an owned scheme-morphism endpoint override requires both endpoints")
            if domain is None:
                engine = native_morphism.parent()
                homset = _scheme_mor_category(engine.domain(), engine.codomain())
            else:
                homset = _scheme_mor_category(domain, codomain)
        else:
            if domain is not None and domain is not homset.domain():
                raise ValueError("the stated scheme-morphism domain disagrees with its Hom")
            if codomain is not None and codomain is not homset.codomain():
                raise ValueError("the stated scheme-morphism codomain disagrees with its Hom")
        Morphism.__init__(self, homset)

    def native_morphism(self):
        return self._native_morphism

    def domain(self):
        return self.parent().domain() if self._preamble_domain_override is None else self._preamble_domain_override

    def codomain(self):
        return self.parent().codomain() if self._preamble_codomain_override is None else self._preamble_codomain_override

    def point_coordinates(self):
        r"""Return the selected owned coordinate family when this morphism is a represented point."""
        coordinates = getattr(self, "_preamble_point_coordinates", None)
        if coordinates is None:
            raise ValueError("this scheme morphism was not constructed from selected point coordinates")
        return coordinates

    def _call_(self, value):
        native_value = value.native_morphism() if isinstance(value, SchemeMorphism) else value
        return self.native_morphism()(native_value)

    def __mul__(self, other):
        if not isinstance(other, SchemeMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        # The identity is a two-sided unit.  That is a theorem, so the
        # composite is the other factor itself.
        if self._is_the_identity():
            return other
        if other._is_the_identity():
            return self
        if self._is_the_structure_morphism():
            structure = other.domain().structure_morphism()
            if structure.codomain() is self.codomain():
                return structure

        projection_label = getattr(
            self,
            "_preamble_product_projection_label",
            None,
        )
        product_cone_target = getattr(
            other,
            "_preamble_product_cone_target",
            None,
        )
        product_cone_legs = getattr(
            other,
            "_preamble_product_cone_legs",
            None,
        )
        if (
            projection_label is not None
            and product_cone_target is self.domain()
            and product_cone_legs is not None
        ):
            return product_cone_legs[projection_label]

        fiber_projection_index = getattr(
            self,
            "_preamble_fiber_projection_index",
            None,
        )
        fiber_cone_target = getattr(
            other,
            "_preamble_fiber_product_cone_target",
            None,
        )
        fiber_cone_legs = getattr(
            other,
            "_preamble_fiber_product_cone_legs",
            None,
        )
        if (
            fiber_projection_index is not None
            and fiber_cone_target is self.domain()
            and fiber_cone_legs is not None
        ):
            return fiber_cone_legs[fiber_projection_index]

        # The composite is a morphism between the stated endpoints, whichever
        # engine route computes it.  Reading the endpoints off the engine's
        # answer lands it on Spec of a coordinate ring instead.
        homset = _scheme_mor_category(other.domain(), self.codomain())
        left_pullback = self._coordinate_pullback
        right_pullback = other._coordinate_pullback
        if left_pullback is not None and right_pullback is not None:
            composite_pullback = left_pullback.domain().Mor(
                right_pullback.codomain()
            ).elementwise(
                lambda element: right_pullback(left_pullback(element))
            )
            return _RepresentedAffineSchemeMorphism(
                homset,
                composite_pullback,
            )
        structured = other._postcompose_with(self)
        if structured is not NotImplemented:
            return structured
        return homset(self.native_morphism() * other.native_morphism())

    def _is_the_identity(self) -> bool:
        r"""Return whether this morphism is its Hom object's identity."""
        if self.domain() is not self.codomain():
            return False
        return self is self.parent().identity()

    def _is_the_structure_morphism(self) -> bool:
        r"""Return whether this is the selected map to the domain's base scheme."""
        return getattr(self.domain(), "_preamble_structure_morphism", None) is self

    def _postcompose_with(self, after):
        r"""Return ``after ∘ self`` for structured maps without a native composite."""

        _ = after
        return NotImplemented

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
                factor_label = getattr(
                    self,
                    "_preamble_product_projection_label",
                    None,
                )
                if stored_points is not None and factor_label is not None:
                    labels = tuple(factors.index_set())
                    for position, label in enumerate(labels):
                        if label == factor_label:
                            return _categorical_scheme_morphism(
                                stored_points[position],
                                domain=point.domain(),
                                codomain=factors[label],
                            )
        return self.compose(point)

    def coordinate_algebra_morphism(self):
        morphism = self._coordinate_pullback
        if morphism is None:
            raise NotImplementedError("this scheme morphism has no represented pullback on affine coordinate algebras")
        return morphism

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
        equations = tuple(to_codomain(algebra.algebra_generator(label)) - to_domain(pullback(algebra.algebra_generator(label))) for label in algebra.algebra_generating_set())
        return product.closed_subscheme(equations)

    def base_change(self, ring_map):
        r"""``f_{R'}: X_{R'} -> Y_{R'}``, the morphism the base-change functor induces.

        The square with the two projections commutes, so an automorphism of
        ``X`` over ``R`` becomes an automorphism of ``X_{R'}`` over ``R'``.
        """
        return self.domain().scheme_category().base_change_functor(ring_map)(self)

    def slice_base_change_adjunction(self):
        r"""Return ``Sigma_self ⊣ self^*`` between the two scheme slice categories."""
        from dzack_research.preamble.categories.schemes.base_change import (
            _slice_base_change_adjunction,
        )

        return _slice_base_change_adjunction(self)

    def inverse_image(self, closed_subscheme):
        r"""``f^{-1}(Z) = X x_Y Z`` as a closed subscheme of ``X``.

        For ``Z = V(I) <= Spec B`` and ``f: Spec A -> Spec B`` this is
        ``V(f^#(I) A)``; the restriction ``f^{-1}(Z) -> Z`` of ``f`` is the
        corestriction of ``f`` composed with the inclusion.
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
        Equality of two projective points is cut out by the ``2 x 2`` minors
        of their homogeneous coordinate pairs, so these minors give the
        scheme-theoretic equalizer without choosing affine charts.
        """
        assert self.domain() is self.codomain(), "a fixed subscheme is that of an endomorphism"
        domain = self.domain()
        base = domain.scheme_base_ring()
        if domain in ProductProjectiveSpaces(base):
            target = getattr(self, "_preamble_product_cone_target", None)
            legs = getattr(self, "_preamble_product_cone_legs", None)
            if target is domain and legs is not None:
                equations = []
                for label in domain.factors().index_set():
                    moved = legs[label].native_morphism()
                    fixed = domain.projection(label).native_morphism()
                    moved_coordinates = getattr(moved, "defining_polynomials", None)
                    fixed_coordinates = getattr(fixed, "defining_polynomials", None)
                    if moved_coordinates is None or fixed_coordinates is None:
                        raise NotImplementedError(
                            "projective-product fixed loci require retained homogeneous coordinate legs"
                        )
                    moved_values = tuple(moved_coordinates())
                    fixed_values = tuple(fixed_coordinates())
                    if len(moved_values) != len(fixed_values):
                        raise ArithmeticError(
                            "parallel projective maps expose different coordinate arities"
                        )
                    equations.extend(
                        moved_values[left] * fixed_values[right]
                        - moved_values[right] * fixed_values[left]
                        for left in range(len(moved_values))
                        for right in range(left + 1, len(moved_values))
                    )
                return domain.closed_subscheme(tuple(equations))
        return Schemes(base).equalizer(
            self,
            domain.categorical_identity_morphism(),
        )

    def _engine_pullback_with_trivial_base_map(self):
        r"""The pullback ``B -> A`` realized in the engine over one coefficient ring.

        Sage computes kernels and surjectivity of a ring map by Gröbner
        elimination on its graph ideal, which it refuses for a map stated
        with a separate base map.  Both coordinate algebras here lie over one
        scalar ring, so the map is restated on the generators alone.
        """
        pullback = self.coordinate_algebra_morphism()
        source_algebra = pullback.domain()
        target_algebra = pullback.codomain()
        assert source_algebra in FramedAlgebras(source_algebra.base_ring()), "the engine realization requires a chosen algebra generating set on the codomain algebra"
        target_engine = _engine_ring(target_algebra)
        return _engine_ring(source_algebra).hom(
            [target_engine(_engine_element(target_algebra, pullback(source_algebra.algebra_generator(label)))) for label in source_algebra.algebra_generating_set()],
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
        r"""Return the affine adjunction ``f^* \dashv f_*`` on represented QCoh."""
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

        This is the pullback of quasi-coherent modules, ``O_X tensor f^{-1}
        O_Y f^{-1} M~``; the inverse-image sheaf ``f^{-1} M~`` itself is not
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

    def is_closed_immersion(self) -> bool:
        r"""Whether ``f^#`` is surjective, for affine ``f`` (Stacks, Tag 01HV)."""
        base = self.domain().scheme_base_ring()
        assert self.domain() in Schemes(base).Affine() and self.codomain() in Schemes(base).Affine(), "closed immersions are currently decided for affine schemes"
        return bool(self._engine_pullback_with_trivial_base_map().is_surjective())

    def __eq__(self, other) -> bool:
        r"""Decide equality from represented pullbacks or the native scheme."""
        if not isinstance(other, SchemeMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        if self is other:
            return True
        left_pullback = self._coordinate_pullback
        right_pullback = other._coordinate_pullback
        if left_pullback is not None and right_pullback is not None:
            base = _scheme_base_ring(self.codomain())
            if self.codomain() in Schemes(base).Affine():
                determining = _elements_determining_maps_out_of(self.codomain().coordinate_algebra(), base)
                if determining is not None:
                    return all(left_pullback(element) == right_pullback(element) for element in determining)
            return bool(left_pullback == right_pullback)
        from sage.schemes.generic.morphism import SchemeMorphism_id

        left_native = self.native_morphism()
        right_native = other.native_morphism()
        if isinstance(left_native, SchemeMorphism_id) and isinstance(right_native, SchemeMorphism_id):
            return True
        return bool(left_native == right_native)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.domain()), id(self.codomain()), id(self.native_morphism())))

    def _repr_(self) -> str:
        return f"Scheme morphism: {self.domain()} -> {self.codomain()}"


class _OpenComplementInclusion(SchemeMorphism):
    r"""The open immersion ``X \ Z -> X`` retained by its closed complement."""

    def __init__(self, homset, closed_complement) -> None:
        Morphism.__init__(self, homset)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._coordinate_pullback = None
        self._native_morphism = None
        self._preamble_closed_complement = closed_complement

    def native_morphism(self):
        raise NotImplementedError(
            "this open immersion is retained by its exact closed complement rather than a native polynomial map"
        )

    def closed_complement(self):
        return self._preamble_closed_complement

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _OpenComplementInclusion)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and other.closed_complement() is self.closed_complement()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Open immersion {self.domain()} -> {self.codomain()} complementing {self.closed_complement()}"


class _ProjectiveCoordinateMorphism(SchemeMorphism):
    r"""A map to projective space retained by its basepoint-free homogeneous coordinates."""

    def __init__(self, homset, coordinates) -> None:
        Morphism.__init__(self, homset)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._coordinate_pullback = None
        self._native_morphism = None
        self._preamble_projective_coordinate_sections = finite_family(
            tuple(coordinates),
            name="Homogeneous coordinates of a projective morphism",
        )

    def native_morphism(self):
        raise NotImplementedError(
            "this projective morphism is retained by owned homogeneous-coordinate sections on its exact open domain"
        )

    def homogeneous_coordinates(self):
        return self._preamble_projective_coordinate_sections

    def image_of_point(self, point):
        r"""Evaluate this retained homogeneous-coordinate map at a represented point."""
        if point.codomain() is not self.domain():
            raise ValueError("the evaluated point belongs to a different source scheme")
        point_coordinates = tuple(point.point_coordinates())
        values = tuple(
            _evaluate_owned_homogeneous_polynomial_on_coordinates(
                coordinate,
                coordinate.parent(),
                point_coordinates,
            )
            for coordinate in self.homogeneous_coordinates()
        )
        return self.codomain().point_morphism(values)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if other._is_the_identity():
            return self
        try:
            pullback = other.coordinate_algebra_morphism()
        except NotImplementedError:
            return super().__mul__(other)
        coordinates = tuple(
            pullback(coordinate) for coordinate in self.homogeneous_coordinates()
        )
        return _ProjectiveCoordinateMorphism(
            _scheme_mor_category(other.domain(), self.codomain()),
            coordinates,
        )

    def __eq__(self, other) -> bool:
        if (
            not isinstance(other, _ProjectiveCoordinateMorphism)
            or other.domain() is not self.domain()
            or other.codomain() is not self.codomain()
        ):
            return False
        left = tuple(self.homogeneous_coordinates())
        right = tuple(other.homogeneous_coordinates())
        return all(
            left[i] * right[j] == left[j] * right[i]
            for i in range(len(left))
            for j in range(i + 1, len(left))
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Projective morphism from {self.domain()} to {self.codomain()} defined by {tuple(self.homogeneous_coordinates())}"


class _RepresentedAffineSchemeMorphism(SchemeMorphism):
    r"""An affine scheme morphism carried exactly by its coordinate pullback."""

    def __init__(self, parent, pullback) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._coordinate_pullback = pullback
        self._native_realization = None

    def native_morphism(self):
        if self._native_realization is None:
            self._native_realization = _affine_morphism_from_pullback(
                self.domain(),
                self.codomain(),
                self.coordinate_algebra_morphism(),
            ).native_morphism()
        return self._native_realization

    def __eq__(self, other) -> bool:
        r"""Compare represented affine maps on a determining generator family.

        Native Sage morphisms need not share the same carrier after the owned
        construction has retained exact endpoints.  Equality of affine scheme
        maps is equality of the contravariant coordinate-ring maps, and a
        finite framing (or the foot of a localization tower) determines those
        maps.
        """
        if self is other:
            return True
        if (
            not isinstance(other, SchemeMorphism)
            or other.domain() is not self.domain()
            or other.codomain() is not self.codomain()
        ):
            return False
        try:
            other_pullback = other.coordinate_algebra_morphism()
        except NotImplementedError:
            return False
        codomain_algebra = self.codomain().coordinate_algebra()
        determining = _elements_determining_maps_out_of(
            codomain_algebra,
            self.codomain().scheme_base_ring(),
        )
        if determining is None:
            return self.coordinate_algebra_morphism() is other_pullback
        pullback = self.coordinate_algebra_morphism()
        return all(pullback(element) == other_pullback(element) for element in determining)

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None


def _categorical_scheme_morphism(
    native_morphism,
    *,
    domain=None,
    codomain=None,
    pullback=None,
):
    if isinstance(native_morphism, SchemeMorphism):
        if domain is None and codomain is None and pullback is None:
            return native_morphism
        native_morphism = native_morphism.native_morphism()
    if domain is not None or codomain is not None or pullback is not None:
        return SchemeMorphism(
            native_morphism,
            domain=domain,
            codomain=codomain,
            pullback=pullback,
        )
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
        try:
            self._engine_homset = _SageScheme._Hom_(domain, codomain)
        except TypeError:
            self._engine_homset = None
        CategoricalHomset.__init__(self, schemes.HomCategory(), domain, codomain)

    def _engine_homset_crossing(self):
        r"""Return the private Sage Homset these morphisms are computed in."""
        if self._engine_homset is None:
            raise NotImplementedError(
                "these owned scheme endpoints have no common native Sage Homset"
            )
        return self._engine_homset

    def _element_constructor_(self, datum):
        if isinstance(datum, SchemeMorphism):
            if datum.parent() is self:
                return datum
            try:
                pullback = datum.coordinate_algebra_morphism()
            except NotImplementedError:
                pullback = None
            if (
                pullback is not None
                and self.domain() in Schemes(_scheme_base_ring(self.domain())).Affine()
                and self.codomain() in Schemes(_scheme_base_ring(self.codomain())).Affine()
                and pullback.domain() is self.codomain().coordinate_algebra()
                and pullback.codomain() is self.domain().coordinate_algebra()
            ):
                return _RepresentedAffineSchemeMorphism(self, pullback)
            datum = datum.native_morphism()
        if (
            isinstance(datum, Morphism)
            and self.domain() in Schemes(_scheme_base_ring(self.domain())).Affine()
            and self.codomain() in Schemes(_scheme_base_ring(self.codomain())).Affine()
            and datum.domain() is self.codomain().coordinate_algebra()
            and datum.codomain() is self.domain().coordinate_algebra()
        ):
            return _RepresentedAffineSchemeMorphism(self, datum)
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
    r"""Return ``Mor_{Sch/S}(X, Y)`` for the finest base ``S`` both schemes lie over.

    A scheme over ``R`` is a scheme over every ring ``R`` restricts to, so the
    Hom between two schemes is taken in the slice over the first common base
    in the domain's restriction tower; ``ZZ`` is the terminal case, and every
    scheme lies over it.
    """
    for base in _scheme_base_tower(_scheme_base_ring(domain)):
        if codomain in Schemes(base):
            return Schemes(base).Mor(domain, codomain)
    assert False, "every scheme is a scheme over the integers"


def _scheme_base_tower(base_ring):
    r"""Yield ``R``, then each proper scalar base below it, ending at ``ZZ``."""
    while base_ring is not None:
        yield base_ring
        base_ring = _proper_restriction_base_ring(base_ring)


def _scheme_base_ring(scheme):
    stored = getattr(scheme, "_preamble_scheme_base_ring", None)
    if stored is not None:
        return stored
    return _own_ring(scheme.base_ring())


def _algebra_structure_morphism_from_base(algebra, base_ring):
    r"""Return the retained scalar map ``base_ring -> algebra`` along its algebra tower."""

    base_ring = _own_ring(base_ring)
    if algebra is base_ring:
        return base_ring.Mor(base_ring).identity()
    algebra_base = getattr(algebra, "algebra_base_ring", lambda: None)()
    if algebra_base is None:
        raise ValueError(f"{algebra} has no represented algebra structure over {base_ring}")
    upper = algebra.algebra_structure_morphism()
    if algebra_base is base_ring:
        return upper
    lower = _algebra_structure_morphism_from_base(algebra_base, base_ring)
    return base_ring.Mor(algebra).elementwise(
        lambda scalar: upper(lower(scalar))
    )


def _affine_structure_morphism_to_base(scheme, base_ring):
    r"""Return ``scheme -> Spec(base_ring)`` from the retained scalar tower."""

    base_ring = _own_ring(base_ring)
    if scheme not in Schemes(base_ring).Affine():
        raise TypeError("a represented affine structure morphism requires an affine scheme over the stated base")
    if scheme.scheme_base_ring() is base_ring:
        return scheme.structure_morphism()
    base_scheme = (base_ring).affine_spectrum(base_ring=base_ring)
    pullback = _algebra_structure_morphism_from_base(
        scheme.coordinate_algebra(),
        base_ring,
    )
    return _RepresentedAffineSchemeMorphism(
        Schemes(base_ring).Mor(scheme, base_scheme),
        pullback,
    )


def _scheme_isomorphism(forward, inverse):
    r"""Return the selected inverse pair in the core of the scheme category.

    A chart overlap can carry distinct open-subobject placements on its two
    sides.  Those placements strengthen the objects, not the ambient category
    in which their transition is an isomorphism: chart changes are arrows in
    ``Sch/R``.  Selecting that owner explicitly avoids manufacturing a Hom in
    the join of two unrelated subobject fibres.
    """
    if forward.domain() is not inverse.codomain() or forward.codomain() is not inverse.domain():
        raise ValueError("an inverse pair must reverse the same two scheme endpoints")
    base = forward.domain().scheme_base_ring()
    schemes = Schemes(base)
    return schemes.Core().Mor(forward.domain(), forward.codomain())(forward, inverse)


def _has_scheme_placement(scheme, category_class) -> bool:
    return any(
        issubclass(dynamic_category_class, category_class)
        for dynamic_category_class in getattr(
            scheme,
            "_preamble_scheme_category_types",
            (),
        )
    )


def _placed_with_scheme_axiom(category, candidate, *, absolute: bool) -> bool:
    r"""Membership in an axiom category on ``Schemes``.

    A property that descends ``Spec R -> Spec R_0`` (``absolute``: affine,
    quasi-affine, separated, integral, normal) is read over every lower base
    of the candidate; one stated relative to the base (finite type, smooth,
    projective, quasi-projective) only over the stated one.
    """
    if candidate not in Schemes(category.base_ring()):
        return False
    if not _has_scheme_placement(candidate, type(category).__mro__[1]):
        return False
    return absolute or candidate.scheme_base_ring() is category.base_ring()


def _placed_over_stated_base(candidate, category, placement_class) -> bool:
    r"""Membership in a category stated relative to its base ring.

    Affine spaces, projective spaces and products are constructions over one
    base: ``A^n_Q`` is a ``Z``-scheme but not an affine space over ``Z``.
    """
    return candidate in Schemes(category.base_ring()) and candidate.scheme_base_ring() is category.base_ring() and _has_scheme_placement(candidate, placement_class)


def _native_scheme_homset(domain, codomain):
    r"""Return Sage's private scheme-Hom runtime homset for owned schemes."""
    return _SageScheme._Hom_(domain, codomain)


def _refine_scheme_morphism(
    morphism,
    base_ring,
    *,
    domain=None,
    codomain=None,
    pullback=None,
):
    r"""Return the native morphism in the Hom of its stated owned schemes."""
    base = _own_ring(base_ring)
    if (domain is None) != (codomain is None):
        raise ValueError("scheme-morphism refinement requires both stated endpoints")
    if domain is not None:
        schemes = Schemes(base)
        if domain not in schemes or codomain not in schemes:
            raise TypeError("scheme-morphism endpoints must be schemes over the stated base")
    return _categorical_scheme_morphism(
        morphism,
        domain=domain,
        codomain=codomain,
        pullback=pullback,
    )


def _refine_scheme(scheme, base_ring=None, categories=()):
    r"""Adopt a native Sage scheme at the scheme-constructor boundary.

    This is structural placement, not property refinement: the native scheme
    is not an owned scheme until this adapter has installed its base and full
    category placement.  Keep that operation separate from :func:`refine`,
    whose post-construction role is restricted to verified properties/axioms.
    """
    base = _own_ring(scheme.base_ring()) if base_ring is None else _own_ring(base_ring)
    scheme._preamble_scheme_base_ring = base
    placements = [Schemes(base), *categories]
    category_types = set(getattr(scheme, "_preamble_scheme_category_types", ()))
    for placement in placements:
        for category in placement.all_super_categories(proper=False):
            category_types.add(type(category))
    scheme._preamble_scheme_category_types = frozenset(category_types)
    CategoryObject._refine_category_(scheme, Category.join(tuple(placements)))
    realize_owned_category(scheme)
    return scheme


class Schemes(OwnedCategoryOverBaseRing):
    r"""Schemes over ``Spec(R)`` for the represented base ring ``R``."""

    def an_object(self):
        r"""The affine line over the base ring."""
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        ring = self.base_ring()
        return Algebras(ring).Associative().Unital().Commutative().spectrum()(Algebras(ring).Associative().Unital().Commutative().an_object())

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

    def __contains__(self, candidate) -> bool:
        stated = getattr(candidate, "_preamble_scheme_base_ring", None)
        return stated is not None and any(base is self.base_ring() for base in _scheme_base_tower(stated)) and _has_scheme_placement(candidate, Schemes)

    @cached_method(key=lambda self, domain, codomain: (id(domain), id(codomain)))
    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a scheme Hom requires two schemes over the stated base")
        return domain._scheme_homset(self, codomain)

    _MonoCategory = None  # set below, once SchemeMonomorphisms is defined

    class SubcategoryMethods:
        def base_change_functor(self, ring_map):
            r"""Return ``- x_{Spec R} Spec R' : Sch/R -> Sch/R'`` along ``R -> R'``."""
            from dzack_research.preamble.categories.schemes.base_change import (
                _scheme_base_change_functor,
            )

            if _own_ring(ring_map.domain()) is not self.base_ring():
                raise ValueError(
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
            from dzack_research.preamble.categories.abstract_categories.products import (
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name="Product factors")
            return _scheme_product(family)

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
            generates that ideal because both pullbacks are ``R``-algebra
            maps.  Its universal property is that of the closed immersion:
            ``h: T -> X`` factors through it exactly when ``h^#`` kills the
            ideal, which is ``f h = g h`` (Stacks, Tag 01JR).
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
        ring = self.base_ring()
        return (ring).affine_spectrum(base_ring=ring)

    @cached_method
    def slice_category(self):
        return self.SliceOver(self.base_scheme())

    def as_slice_object(self, scheme):
        if scheme not in self:
            raise TypeError(f"{scheme} is not an object of {self}")
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

        return _TwoChartSchemeGluingDatum(
            self,
            left_chart,
            right_chart,
            transition,
        ).scheme()

    def glue_affine_atlas(self, charts, transitions):
        r"""Glue a finite affine atlas with represented distinguished-open transitions."""

        from dzack_research.preamble.categories.schemes.gluing import (
            _FiniteSchemeGluingDatum,
        )

        return _FiniteSchemeGluingDatum(
            self,
            charts,
            transitions,
        ).scheme()

    class ParentMethods:
        def _scheme_homset(self, schemes, codomain):
            homset_class = self.__dict__.get("_preamble_scheme_homset_class")
            if homset_class is None:
                homset_class = SchemeMorCategory
            return homset_class(schemes, self, codomain)

        def Mor(self, codomain, category=None):
            schemes = Schemes(self.scheme_base_ring())
            if category is None or category.is_subcategory(schemes):
                return schemes.Mor(self, codomain)
            return _SageScheme._Hom_(self, codomain, category=category)

        def scheme_base_ring(self):
            return _scheme_base_ring(self)

        def scheme_category(self):
            return Schemes(self.scheme_base_ring())

        def log_pair(self, boundary_divisor):
            r"""Return the log pair ``(self, boundary_divisor)``."""
            from dzack_research.preamble.categories.schemes.log_pairs import _log_pair

            return _log_pair(self, boundary_divisor)

        def base_scheme(self):
            ring = self.scheme_base_ring()
            return (ring).affine_spectrum(base_ring=ring)

        def _scheme_underlying_space(self):
            base_ring = self.scheme_base_ring()
            if self in Schemes(base_ring).Affine():
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    PrimeSpectra,
                )
                from dzack_research.preamble.owned_category import _object_of

                return _object_of(
                    PrimeSpectra(),
                    ring=self.coordinate_algebra(),
                    ringed_space=self,
                )
            return SchemeUnderlyingSpace(self)

        def _structure_sheaf_global_sections(self):
            base_ring = self.scheme_base_ring()
            if self in Schemes(base_ring).Affine():
                return self.coordinate_algebra()
            if self in ProjectiveSpaces(base_ring):
                return base_ring
            raise NotImplementedError(f"global sections of the structure sheaf of {self} are not yet represented")

        def _structure_sheaf_sections_on_distinguished_open(self, distinguished_open):
            base_ring = self.scheme_base_ring()
            if self not in Schemes(base_ring).Affine():
                raise NotImplementedError("distinguished-open structure-sheaf sections are represented for affine schemes")
            if (
                getattr(
                    distinguished_open,
                    "_preamble_distinguished_open_ambient",
                    None,
                )
                is self
            ):
                return distinguished_open.coordinate_algebra()
            spectrum = self.underlying_space()
            if distinguished_open.codomain() is not spectrum:
                raise ValueError("the distinguished open belongs to a different affine spectrum")
            return distinguished_open.coordinate_ring()

        def _structure_sheaf_stalk(self, point):
            base_ring = self.scheme_base_ring()
            if self not in Schemes(base_ring).Affine():
                raise NotImplementedError("the active stalk construction is represented on affine schemes")
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
            try:
                morphism = _SageScheme.base_morphism(self)
            except (AttributeError, NotImplementedError):
                scheme_base = self.scheme_base_ring()
                if self not in Schemes(scheme_base).Affine():
                    raise
                algebra = self.coordinate_algebra()
                engine_map = _engine_ring(algebra).coerce_map_from(_engine_ring(scheme_base))
                if engine_map is None:
                    raise NotImplementedError("the affine structure morphism requires the scalar-base injection") from None
                morphism = _native_scheme_homset(self, base)(engine_map, check=False)
            if morphism.codomain() is not base:
                raise ArithmeticError("the native structure morphism does not land in the represented base scheme")
            pullback = (
                self.coordinate_algebra().algebra_structure_morphism()
                if self in Schemes(self.scheme_base_ring()).Affine()
                else None
            )
            wrapped = _refine_scheme_morphism(
                morphism,
                self.scheme_base_ring(),
                domain=self,
                codomain=base,
                pullback=pullback,
            )
            self._preamble_structure_morphism = wrapped
            return wrapped

        def relative_dimension(self):
            selected = getattr(self, "_preamble_relative_dimension", None)
            if selected is not None:
                return selected
            if self is self.base_scheme():
                return 0
            return self.dimension_relative()

        def base_change(self, ring_map):
            r"""``X_{R'} = X x_{Spec R} Spec R'`` along a scalar morphism ``R -> R'``.

            The functor is applied to this object; the result is equipped as
            the fibre product of ``X -> Spec R <- Spec R'``, so its two
            projections and the universal factorization are available on it.
            """
            assert self in Schemes(_own_ring(ring_map.domain())), "a scheme is base-changed along a morphism out of its own scalar base"
            return self.scheme_category().base_change_functor(ring_map)(self)

        def as_slice_object(self):
            return self.scheme_category().as_slice_object(self)

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
            scheme is separated, so this is a closed immersion.  The diagonal
            morphism factors through it as an isomorphism.
            """
            base = self.scheme_base_ring()
            assert self in Schemes(base).Affine(), (
                "the diagonal is represented as a closed subscheme for affine schemes; for a glued scheme it is closed exactly when the scheme is separated"
            )
            product = _scheme_product(self, self)
            left = product.projection(0).coordinate_algebra_morphism()
            right = product.projection(1).coordinate_algebra_morphism()
            algebra = self.coordinate_algebra()
            equations = tuple(left(algebra.algebra_generator(label)) - right(algebra.algebra_generator(label)) for label in algebra.algebra_generating_set())
            return product.closed_subscheme(equations)

        def point_morphism(self, coordinates):
            base = self.scheme_base_ring()
            owned_coordinates = tuple(
                coordinate
                if getattr(coordinate, "parent", lambda: None)() is base
                else base(coordinate)
                for coordinate in coordinates
            )
            engine_coordinates = tuple(
                _engine_element(base, coordinate)
                for coordinate in owned_coordinates
            )
            if self in ProductProjectiveSpaces(base):
                factors = self.factors()
                factor_points = []
                offset = 0
                for factor in factors:
                    width = int(factor.relative_dimension()) + 1
                    factor_coordinates = engine_coordinates[offset : offset + width]
                    if len(factor_coordinates) != width:
                        raise ValueError("a product-projective point has one homogeneous coordinate block per factor")
                    factor_points.append(
                        factor._point(
                            factor.point_homset(),
                            factor_coordinates,
                            check=False,
                        )
                    )
                    offset += width
                if offset != len(engine_coordinates):
                    raise ValueError("too many homogeneous coordinates for this product of projective spaces")
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
                    Schemes(base).Affine(),
                    Schemes(base).FiniteType(),
                    Schemes(base).Smooth(),
                ]
                if _integral_placement(base):
                    categories.append(Schemes(base).Integral())
                _refine_scheme(point_domain, base, categories)
            pullback = None
            if self in Schemes(base).Affine():
                source_algebra = self.coordinate_algebra()
                target_algebra = point_domain.coordinate_algebra()
                if source_algebra in FramedAlgebras(base):
                    labels = tuple(source_algebra.algebra_generating_set())
                    if len(labels) != len(engine_coordinates):
                        raise ValueError("an affine point needs one coordinate per algebra generator")
                    pullback = source_algebra.Mor(target_algebra)(
                        {
                            label: target_algebra._from_engine_element(coordinate)
                            for label, coordinate in zip(
                                labels,
                                engine_coordinates,
                                strict=True,
                            )
                        }
                    )
            wrapped = _refine_scheme_morphism(
                point,
                base,
                domain=point_domain,
                codomain=self,
                pullback=pullback,
            )
            wrapped._preamble_point_coordinates = finite_family(
                owned_coordinates,
                name=f"Selected coordinates of point on {self}",
            )
            return wrapped

        def projective_morphism_from_coordinates(self, target, coordinates):
            r"""Return the projective morphism defined by a basepoint-free coordinate family.

            ``coordinates`` are owned homogeneous sections on the ambient
            projective presentation.  The caller has selected this exact source
            as a domain on which they have no common zero; retaining that open
            domain and the coordinate family is the complete defining datum of
            the morphism.  No larger rational-map domain is silently substituted.
            """
            base = self.scheme_base_ring()
            if target not in ProjectiveSpaces(base):
                raise TypeError("projective homogeneous coordinates require a projective-space target")
            coordinates = tuple(coordinates)
            if len(coordinates) != int(target.relative_dimension()) + 1:
                raise ValueError("a projective morphism has one homogeneous coordinate per target coordinate")
            return _ProjectiveCoordinateMorphism(
                self.Mor(target),
                coordinates,
            )

        def categorical_identity_morphism(self):
            selected = getattr(self, "_preamble_identity_morphism", None)
            if selected is not None:
                return selected
            return _refine_scheme_morphism(
                self.identity_morphism(),
                self.scheme_base_ring(),
                domain=self,
                codomain=self,
            )

        def product_with(self, other):
            r"""Return ``X x_S Y``, the product asked of the two objects.

            One argument is distinguished, so this is the operator spelling of
            the binary case.  A product over an index set that is part of the
            mathematics is named and taken over that set with
            ``Schemes(R).product(family)``, which is the same word one level
            up (`CON-14`).
            """
            schemes = self.scheme_category()
            assert other in schemes, "a product of schemes is taken between two schemes over one base"
            factors = (self, other)
            return schemes.product(indexed_family(Sets.Δ[1], lambda index: factors[int(index)]))

        def point_counts(self, extension_degree):
            r"""Return ``(#X(F_q),...,#X(F_{q^n}))`` for a finite base field."""
            degree = int(extension_degree)
            if degree < 1:
                raise ValueError("the extension degree must be positive")
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("finite-field point counts require a finite base field")

            return finite_family(super().count_points(degree), name="Point counts")

        def point_count(self, extension_degree=1):
            r"""Return ``#X(F_{q^n})`` for the stated extension degree ``n``."""
            degree = int(extension_degree)
            return self.point_counts(degree)[degree - 1]

    class Separated(CategoryWithAxiom):
        r"""Schemes whose diagonal is a closed immersion."""

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=True)

        class ParentMethods:
            def is_separated(self):
                return True

        def an_object(self):
            r"""The affine line, separated because it is affine."""
            return AffineSpaces(self.base_ring())(1)

    class FiniteType(CategoryWithAxiom):
        r"""Schemes of finite type over the base."""

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=False)

        class ParentMethods:
            def is_finite_type(self):
                return True

        def an_object(self):
            r"""The affine line, of finite type over the base ring."""
            from dzack_research.preamble.categories.algebras.algebras import Algebras
            ring = self.base_ring()
            return Algebras(ring).Associative().Unital().Commutative().spectrum()(Algebras(ring).Associative().Unital().Commutative().an_object())

    class Integral(CategoryWithAxiom):
        r"""Schemes that are reduced and irreducible."""

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=True)

        class ParentMethods:
            def is_integral(self):
                return True

        def an_object(self):
            r"""The affine line, integral because its coordinate algebra is a domain."""
            from dzack_research.preamble.categories.algebras.algebras import Algebras
            ring = self.base_ring()
            return Algebras(ring).Associative().Unital().Commutative().spectrum()(Algebras(ring).Associative().Unital().Commutative().an_object())

    class Normal(CategoryWithAxiom):
        r"""Schemes whose local rings are integrally closed domains."""

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=True)

        class ParentMethods:
            def is_normal(self):
                return True

        def an_object(self):
            r"""The affine line, normal because ``R[x]`` is integrally closed when ``R`` is."""
            base = self.base_ring()
            assert _normal_placement(base), (
                f"the affine line over {base} is normal exactly when {base} is, and the "
                "criterion available here is that the base is a principal ideal domain; "
                "a normal scheme over a base outside it needs a normality predicate on "
                "the ring, which the owned ring hierarchy does not yet state"
            )
            return AffineSpaces(base)(1)

    class Smooth(CategoryWithAxiom):
        r"""Schemes smooth over the base."""

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=False)

        class ParentMethods:
            def is_smooth(self):
                return True

        def an_object(self):
            r"""The affine line, which is smooth over the base ring."""
            return AffineSpaces(self.base_ring())(1)

    class Affine(CategoryWithAxiom):
        r"""Schemes isomorphic to ``Spec A``."""

        def an_object(self):
            r"""The affine line over the base ring."""
            from dzack_research.preamble.categories.algebras.algebras import Algebras
            ring = self.base_ring()
            return Algebras(ring).Associative().Unital().Commutative().spectrum()(Algebras(ring).Associative().Unital().Commutative().an_object())

        def _call_(self, algebra):
            r"""Construct ``Spec(A)`` over this category's represented scalar base."""
            algebra = _own_ring(algebra)
            return _affine_spectrum_from_owned_algebra(algebra, self.base_ring())

        def extra_super_categories(self):
            # Quasi-affine as well: a scheme is an open subscheme of itself.
            return [Schemes(self.base_ring()).QuasiAffine()]

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=True)

        class ParentMethods:
            def is_regular_at(self, point) -> bool:
                r"""Return whether ``O_{X,p}`` is a regular local ring."""
                spectrum = self.underlying_space()
                if point.parent() is not spectrum:
                    point = spectrum(point)
                return bool(point.is_regular())

            def is_singular_at(self, point) -> bool:
                r"""Return the negation of local regularity at ``p``."""
                return not self.is_regular_at(point)

            def is_locally_factorial_at(self, point) -> bool:
                r"""Return local factoriality at ``p`` in the supported regular regime."""
                spectrum = self.underlying_space()
                if point.parent() is not spectrum:
                    point = spectrum(point)
                return bool(point.is_locally_factorial())

            def is_affine(self):
                return True

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

            def dimension(self):
                r"""The Krull dimension of ``Spec A``, which is that of ``A``."""
                return self.coordinate_algebra().krull_dimension()

            def relative_dimension(self):
                r"""``dim A - dim R`` for ``Spec A -> Spec R``.

                This is the relative dimension of an equidimensional scheme of
                finite type and flat over an integral base; it is the number the
                engine's ``dimension_relative`` reports for affine space, and it
                extends that value to every affine spectrum.
                """
                return self.dimension() - self.scheme_base_ring().krull_dimension()

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
                selected = _refine_commutative_algebra(_own_ring(engine), base, labels)
                self._preamble_coordinate_algebra = selected
                return selected

            def coordinate_ring(self):
                r"""Return the owned coordinate ring/algebra of this affine scheme."""
                return self.coordinate_algebra()

            def closed_subscheme(self, *equations):

                equations = tuple(equations[0]) if len(equations) == 1 and isinstance(equations[0], (tuple, list)) else tuple(equations)
                algebra = self.coordinate_algebra()
                quotient_operation = getattr(
                    algebra,
                    "_quotient_by_algebra_elements",
                    None,
                )
                if quotient_operation is None:
                    raise NotImplementedError("a closed affine subscheme requires a represented polynomial presentation of its coordinate algebra")
                quotient, quotient_map = quotient_operation(equations)
                subscheme = (quotient).affine_spectrum(base_ring=self.scheme_base_ring())
                spec_inclusion = _affine_spec_morphism(quotient_map)
                inclusion = _categorical_scheme_morphism(
                    spec_inclusion.native_morphism(),
                    domain=subscheme,
                    codomain=self,
                    pullback=quotient_map,
                )
                subscheme._preamble_inclusion = inclusion
                return _refine_closed_subscheme(
                    subscheme,
                    self,
                    defining_equations=equations,
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

                This uses ``Fitt_d(Omega^1_{X/k})`` only when the represented
                affine morphism is flat and finitely presented with equidimensional
                fibres of dimension ``d``.  Here the base is a field, so flatness
                is automatic, and the selected finite algebra presentation and
                backend minimal components verify the remaining hypotheses.
                """

                base = self.scheme_base_ring()
                engine_base = _engine_ring(base)
                if not bool(engine_base.is_field()):
                    raise NotImplementedError("the represented singular subscheme currently requires a field base")
                algebra = self.coordinate_algebra()
                if algebra not in AlgebrasWithChosenFinitePresentation(base):
                    raise NotImplementedError("the represented singular subscheme requires a chosen finite algebra presentation")
                dimension = int(algebra.krull_dimension())
                engine_algebra = _engine_ring(algebra)
                defining_ideal = getattr(engine_algebra, "defining_ideal", lambda: None)()
                if defining_ideal is not None:
                    try:
                        minimal_components = defining_ideal.minimal_associated_primes()
                    except (AttributeError, NotImplementedError) as error:
                        raise NotImplementedError("the represented singular subscheme requires a represented equidimensionality check") from error
                    if any(int(component.dimension()) != dimension for component in minimal_components):
                        raise NotImplementedError("the represented singular subscheme requires equidimensional fibres")
                return self.differential_rank_drop_subscheme(dimension)

            def relative_nonsmooth_subscheme(self):
                r"""Return the relative nonsmooth locus in the supported flat hypersurface regime.

                For a flat morphism locally of finite presentation, smoothness at a
                point is equivalent to smoothness of the fibre there (Stacks
                Project, Tags 01V8 and 01V9).  For a primitive hypersurface over a
                univariate polynomial ring over a perfect field, every fibre is a
                hypersurface of the same represented dimension and the Jacobian
                criterion is detected by the corresponding Fitting ideal of
                relative differentials.
                """

                if not self.is_flat():
                    raise NotImplementedError("the relative nonsmooth Fitting criterion requires represented flatness")
                base = self.scheme_base_ring()
                algebra = self.coordinate_algebra()
                if algebra not in AlgebrasWithChosenFinitePresentation(base):
                    raise NotImplementedError("the relative nonsmooth locus requires a chosen finite algebra presentation")

                base_engine = _engine_ring(base)
                try:
                    coefficient_field = base_engine.base_ring()
                    supported_perfect_base = base_engine.ngens() == 1 and bool(coefficient_field.is_field()) and bool(coefficient_field.is_perfect())
                except (AttributeError, NotImplementedError, TypeError, ValueError):
                    supported_perfect_base = False
                if not supported_perfect_base:
                    raise NotImplementedError("the relative hypersurface smoothness criterion currently requires k[t] with k perfect")

                relative_dimension = algebra._represented_primitive_hypersurface_relative_dimension()
                return self.differential_rank_drop_subscheme(relative_dimension)

            def distinguished_open(self, element):
                r"""Return \(D(f)\subseteq X\), the open locus where ``element`` is a unit.

                \(D(f)=\operatorname{Spec}A[1/f]\), and the localization map
                \(A\to A[1/f]\) induces the open immersion.
                """
                algebra = self.coordinate_algebra()
                element = algebra(element)
                cache = getattr(self, "_preamble_distinguished_open_cache", ())
                for cached_element, cached_open in cache:
                    if cached_element == element:
                        return cached_open
                localized = algebra.localization(element)
                localization_map = localized.localization_map()
                base = self.scheme_base_ring()
                canonical_ambient = (algebra).affine_spectrum(base_ring=base)
                if self is canonical_ambient:
                    open_subscheme = _refine_scheme(
                        (localized).affine_spectrum(base_ring=base),
                        base,
                        (OpenImmersions(self),),
                    )
                else:
                    open_subscheme = _fresh_affine_spectrum(
                        localized,
                        base,
                        extra_categories=(OpenImmersions(self),),
                    )
                inclusion = _affine_morphism_from_pullback(
                    open_subscheme,
                    self,
                    localization_map,
                )
                open_subscheme._preamble_inclusion = inclusion
                open_subscheme._preamble_distinguished_open_ambient = self
                open_subscheme._preamble_distinguished_open_element = element
                self._preamble_distinguished_open_cache = (
                    *cache,
                    (element, open_subscheme),
                )
                return open_subscheme

            def distinguished_open_cover(self, *elements):
                r"""Return the finite cover by ``D(f_i)`` when the ``f_i`` generate the unit ideal."""

                if len(elements) == 1 and isinstance(elements[0], (tuple, list)):
                    elements = tuple(elements[0])
                from dzack_research.preamble.categories.schemes.ringed_spaces import (
                    DistinguishedAffineCover,
                )

                return DistinguishedAffineCover(self, elements)

            def associated_module_sheaf(self, module):
                r"""Return ``M~`` on the represented distinguished-open basis of this affine scheme."""

                return self.structure_sheaf().associated_module_sheaf(module)

            def relative_spectrum(self, algebra_structure):
                r"""``Spec_X(B~) -> X`` for the ``O_X``-algebra given by ``A -> B`` (Stacks, Tag 01LQ).

                On affine ``X = Spec A`` a quasi-coherent ``O_X``-algebra is an
                ``A``-algebra, stated as the ``R``-algebra morphism ``A -> B``
                that makes ``B`` one; its relative spectrum is ``Spec B`` with the
                structure morphism ``Spec`` of that map, an object of ``Sch/X``.
                Base change along ``X' -> X`` gives ``Spec_{X'}(B tensor_A A')``,
                which is the fibre product ``Spec_X(B) x_X X'``.
                """
                assert algebra_structure.domain() is self.coordinate_algebra(), "a quasi-coherent algebra on Spec A is stated by an algebra map out of A"
                structure_morphism = _affine_spec_morphism(algebra_structure)
                return self.scheme_category().SliceOver(self)(structure_morphism)

    class QuasiAffine(CategoryWithAxiom):
        r"""Schemes that are open subschemes of an affine scheme."""

        def an_object(self):
            r"""The affine line, which is affine."""
            from dzack_research.preamble.categories.algebras.algebras import Algebras
            ring = self.base_ring()
            return Algebras(ring).Associative().Unital().Commutative().spectrum()(Algebras(ring).Associative().Unital().Commutative().an_object())

        def extra_super_categories(self):
            return [Schemes(self.base_ring()).Separated()]

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=True)

        class ParentMethods:
            def is_quasi_affine(self):
                return True

        class FiniteType(CategoryWithAxiom):
            r"""Quasi-affine schemes of finite type over the base.

            A quasi-affine morphism of finite type is quasi-projective
            (Stacks Tag 0B3H, Lemma 29.41.7), so this join declares
            quasi-projectivity.  Neither hypothesis alone gives it: a
            quasi-affine scheme need not be of finite type, and finite type
            says nothing about an ample sheaf.
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

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=False)

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

        def __contains__(self, candidate) -> bool:
            return _placed_with_scheme_axiom(self, candidate, absolute=False)

        class ParentMethods:
            def is_projective(self):
                return True

            def closed_subscheme(self, *equations):
                r"""``V_+(f_1, ..., f_k)``, cut out by homogeneous equations."""
                equations = (
                    tuple(equations[0])
                    if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                    else tuple(equations)
                )
                engine_equations = []
                retain_owned_equations = True
                ambient_engine = self.coordinate_ring()
                ambient_variables = tuple(ambient_engine.gens())
                for equation in equations:
                    if not equation.is_homogeneous():
                        raise ValueError(
                            f"{equation} is not homogeneous, so it cuts out no closed subscheme of {self}"
                        )
                    parent = getattr(equation, "parent", lambda: None)()
                    try:
                        backend = _engine_element(parent, equation)
                    except (AttributeError, TypeError, ValueError):
                        backend = equation
                        retain_owned_equations = False
                    engine_equations.append(
                        _copy_polynomial_by_exponents(
                            backend,
                            ambient_engine,
                            ambient_variables,
                        )
                    )
                return _refine_closed_subscheme(
                    self.subscheme(tuple(engine_equations)),
                    self,
                    defining_equations=equations if retain_owned_equations else None,
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


class AffineGSchemes(OwnedCategory):
    r"""Represented affine schemes with a chosen action of one group.

    This is the affine specialization of ``GObjects(G, Schemes(R))`` and the
    construction owner for represented affine actions.  The generic
    ``GObjects`` category remains the functor category ``[BG, C]``.
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
        r"""Equip an affine scheme with the chosen left action of this group.

        The result is a fresh affine scheme carrying the action.  The supplied
        ``Spec(A)`` is not mutated; each action morphism is transported to the
        fresh copy through its represented pullback on ``A``.
        """
        base = self.base_ring()
        if scheme not in Schemes(base).Affine():
            raise TypeError(f"an object of {self} is constructed from an affine scheme over {base}")
        algebra = scheme.coordinate_algebra()
        acted = typecall(
            _SageAffineScheme,
            _engine_ring(algebra),
            _engine_ring(base),
        )
        acted._preamble_acting_group = self.acting_group()
        acted._preamble_underlying_category = Schemes(base)
        acted._preamble_unacted_scheme = scheme
        _initialize_owned_affine_spectrum(
            acted,
            algebra,
            base,
            extra_categories=(self,),
        )

        source_endomorphisms = Schemes(base).Mor(scheme, scheme)

        def acted_action(group_element):
            source_morphism = source_endomorphisms(action(group_element))
            return _affine_endomorphism_from_pullback(
                acted,
                source_morphism.coordinate_algebra_morphism(),
            )

        acted._preamble_action_datum = acted_action
        return acted

    class ParentMethods:
        def Mor(self, codomain, category=None):
            from dzack_research.preamble.categories.group.g_objects import GObjects

            acted_schemes = GObjects(
                self.acting_group(),
                self.underlying_category(),
            )
            if category is None or category.is_subcategory(acted_schemes):
                return acted_schemes.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def unacted_scheme(self):
            r"""Return the represented affine scheme before the action was equipped."""
            return self._preamble_unacted_scheme

        @cached_method
        def fixed_ideal(self):
            r"""Return the ideal defining the common fixed subscheme ``X^G``.

            For ``X = Spec(A)`` and chosen generators ``s`` of ``G``, the
            fixed ideal is generated by ``s^*(a) - a`` on a chosen algebra
            generating family of ``A``.  Those equations generate the full
            equalizer ideal because every ``s^*`` is an ``R``-algebra map:
            modulo these equations each ``s^*`` fixes the scalar image and
            every algebra generator, hence is the identity.  Since the chosen
            ``s`` generate ``G``, every group element is then the identity on
            the quotient as well.
            """
            from dzack_research.preamble.categories.group.groups import (
                GroupsWithChosenFiniteGeneratingSet,
            )

            group = self.acting_group()
            if group not in GroupsWithChosenFiniteGeneratingSet():
                raise NotImplementedError("the represented common fixed ideal requires a chosen finite group generating set")
            algebra = self.coordinate_algebra()
            base = self.scheme_base_ring()
            if algebra not in FramedAlgebras(base):
                raise NotImplementedError("the represented common fixed ideal requires a framed affine coordinate algebra")
            labels = algebra.algebra_generating_set()
            if not labels.cardinality().is_finite():
                raise NotImplementedError("the represented common fixed ideal requires finitely many algebra generators")

            equations = []
            for group_generator in group.group_generators():
                pullback = self.action_of(group_generator).coordinate_algebra_morphism()
                if pullback.domain() is not algebra or pullback.codomain() is not algebra:
                    raise ValueError("an affine scheme action must act by endomorphisms of its coordinate algebra")
                for label in labels:
                    generator = algebra.algebra_generator(label)
                    equations.append(pullback(generator) - generator)
            return algebra.ideal(*equations)

        @cached_method
        def fixed_subscheme(self):
            r"""Return the common fixed subscheme ``X^G`` of this affine action."""
            return self.closed_subscheme(tuple(self.fixed_ideal().ideal_generators()))

        @cached_method
        def _invariant_algebra_data(
            self: Any,
        ) -> tuple[Any, Any, tuple[Any, ...]]:
            r"""Return the selected represented ``(A^G, A^G -> A, generators)``."""
            return _affine_linear_invariant_algebra_data(self)

        def invariant_algebra(self: Any) -> Any:
            r"""Return the represented invariant algebra ``A^G``.

            The current backend supports finite linear actions on a polynomial
            algebra over a field accepted by Sage's Singular invariant-ring
            interface.  The result carries a chosen finite polynomial
            presentation, not merely a membership predicate.
            """
            return self._invariant_algebra_data()[0]

        def invariant_algebra_inclusion(self: Any) -> Any:
            r"""Return the represented inclusion ``A^G -> A``."""
            return self._invariant_algebra_data()[1]

        def invariant_algebra_element(self: Any, element: Any) -> Any:
            r"""Express one verified invariant element of ``A`` in ``A^G``.

            The same invariant-ring backend used by the affine quotient returns
            a polynomial certificate in its selected invariant generators.  The
            certificate is evaluated in the owned invariant algebra, so callers
            can descend stable principal opens without reaching into Singular.
            """
            source_algebra = self.coordinate_algebra()
            element = source_algebra(element)
            group_generators = tuple(self.acting_group().group_generators())
            if any(
                self.action_of(group_generator).coordinate_algebra_morphism()(element)
                != element
                for group_generator in group_generators
            ):
                raise ValueError("the selected coordinate-algebra element is not invariant")
            invariant_algebra, _inclusion, engine_invariants = self._invariant_algebra_data()
            if not engine_invariants:
                return invariant_algebra(element)
            engine_source = _engine_ring(source_algebra)
            engine_element = engine_source(_engine_element(source_algebra, element))
            certificate = engine_element.in_subalgebra(
                engine_invariants,
                algorithm="groebner",
                certificate="invariant",
            )
            if certificate is None:
                raise ArithmeticError(
                    "the invariant-ring backend did not express a verified invariant in its selected generators"
                )
            result = _evaluate_polynomial_in_algebra(
                certificate,
                invariant_algebra,
            )
            if self.invariant_algebra_inclusion()(result) != element:
                raise ArithmeticError("the invariant-algebra certificate does not map back to the selected element")
            return result

        @cached_method
        def affine_quotient(self: Any) -> Any:
            r"""Return ``Spec(A^G)`` for the supported affine linear action."""
            return (self.invariant_algebra()).affine_spectrum(base_ring=self.scheme_base_ring())

        def quotient_base_change_comparison(self, ring_map):
            from dzack_research.preamble.categories.schemes.quotients import (
                AffineInvariantQuotientBaseChangeComparison,
            )

            return AffineInvariantQuotientBaseChangeComparison(self, ring_map)

        @cached_method
        def quotient_morphism(self: Any) -> SchemeMorphism:
            r"""Return the represented affine quotient map ``Spec(A) -> Spec(A^G)``."""
            return _affine_morphism_from_pullback(
                self,
                self.affine_quotient(),
                self.invariant_algebra_inclusion(),
            )

        def factor_through_affine_quotient(
            self: Any,
            morphism: Any,
        ) -> SchemeMorphism:
            r"""Factor one invariant affine morphism uniquely through ``Spec(A^G)``.

            If ``f : Spec(A) -> Spec(C)`` is invariant, every selected
            generator of ``C`` pulls back to an element of ``A^G``.  The
            Singular-backed subalgebra-membership certificate expresses that
            pullback in the selected invariant generators.  These expressions
            define ``C -> A^G`` and hence the required factor
            ``Spec(A^G) -> Spec(C)``.  Uniqueness follows because the selected
            presentation of ``A^G`` was obtained from the kernel of the map
            from the polynomial algebra on those invariant generators to
            ``A``; its represented inclusion is therefore injective.
            """
            if not isinstance(morphism, SchemeMorphism) or morphism.domain() is not self:
                raise ValueError("the quotient factorization starts at this acted affine scheme")
            target = morphism.codomain()
            base = self.scheme_base_ring()
            if target not in Schemes(base).Affine():
                raise NotImplementedError("the represented quotient universal property currently targets affine schemes")
            target_algebra = target.coordinate_algebra()
            if target_algebra not in FramedAlgebras(base):
                raise NotImplementedError("the represented quotient factorization requires a framed target coordinate algebra")
            labels = target_algebra.algebra_generating_set()
            if not labels.cardinality().is_finite():
                raise NotImplementedError("the represented quotient factorization requires finitely many target generators")

            source_algebra = self.coordinate_algebra()
            pullback = morphism.coordinate_algebra_morphism()
            if pullback.domain() is not target_algebra or pullback.codomain() is not source_algebra:
                raise ValueError("the affine morphism has the wrong represented coordinate pullback")

            invariant_algebra, inclusion, _engine_invariants = self._invariant_algebra_data()

            generator_images = {}
            for label in labels:
                image = pullback(target_algebra.algebra_generator(label))
                generator_images[label] = self.invariant_algebra_element(image)

            factor_pullback = target_algebra.Mor(invariant_algebra)(generator_images)
            factor = _affine_morphism_from_pullback(
                self.affine_quotient(),
                target,
                factor_pullback,
            )
            if factor * self.quotient_morphism() != morphism:
                raise ArithmeticError("the represented affine quotient factorization failed its defining triangle")
            if any(inclusion(factor_pullback(target_algebra.algebra_generator(label))) != pullback(target_algebra.algebra_generator(label)) for label in labels):
                raise ArithmeticError("the represented quotient factorization disagrees on a target generator")
            return factor

        def descend_invariant_family(self, family_morphism):
            r"""Descend an invariant affine family map through the quotient.

            A family here is simply a morphism to an affine parameter scheme.
            If that morphism is invariant, its unique quotient factor is the
            family carried by ``X/G``; no separate family quotient object is
            introduced.
            """
            return self.factor_through_affine_quotient(family_morphism)


class AffineSpaces(OwnedCategoryOverBaseRing):
    def analytification(self, scalar_embedding):
        r"""Return affine-space analytification along this base embedding."""
        if _own_ring(scalar_embedding.domain()) is not self.base_ring():
            raise ValueError(
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
        r"""Construct the selected affine space over this category's base."""
        return _affine_space_from_owned_data(
            self.base_ring(),
            int(_engine_numeral(SageZZ, dimension)),
            _normalized_space_names(names),
        )

    def _repr_object_names(self):
        return f"affine spaces over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Affine().FiniteType().Smooth()]

    def __contains__(self, candidate) -> bool:
        return _placed_over_stated_base(candidate, self, AffineSpaces)

    class ParentMethods:
        @cached_method
        def picard_group(self):
            r"""Return ``Pic(A^n_k)=0`` over a field."""
            base = self.scheme_base_ring()
            if base not in OwnedFields():
                raise NotImplementedError(
                    "the represented affine-space Picard group currently requires a field base"
                )
            from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups

            return PicardGroups().trivial(self)

        @cached_method
        def class_group(self):
            r"""Return ``Cl(A^n_k)=0`` over a field."""
            base = self.scheme_base_ring()
            if base not in OwnedFields():
                raise NotImplementedError(
                    "the represented affine-space class group currently requires a field base"
                )
            from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            integers = _own_ring(SageZZ)
            return ClassGroups()(
                integers.free_module(finite_ordered_set(())), scheme=self
            )

        def basic_open(self, element):
            r"""Archived spelling for the distinguished open ``D(element)``."""
            return self.distinguished_open(element)

        def zeta_function(self):
            r"""Return ``Z(A^d/F_q,T)=1/(1-q^d T)``."""
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = rationals.polynomial_ring("T")
            rational_functions = _refine_commutative_algebra(polynomial.fraction_field(), rationals, ("T",))
            T = rational_functions.algebra_generator("T")
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return 1 / (1 - q**d * T)


class ProjectiveSpaces(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The projective line over the base ring."""
        return self(1)

    def _call_(self, dimension, names=None):
        r"""Construct the selected projective space over this category's base."""
        return _projective_space_from_owned_data(
            self.base_ring(),
            int(_engine_numeral(SageZZ, dimension)),
            _normalized_space_names(names),
        )

    def _repr_object_names(self):
        return f"projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Projective().Smooth()]

    def __contains__(self, candidate) -> bool:
        return _placed_over_stated_base(candidate, self, ProjectiveSpaces)

    class ParentMethods:
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

            integers = _own_ring(SageZZ)
            lattice = integers.free_module(int(self.relative_dimension()))
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
            r"""Return the projective-bundle comparison ``Pic(P^n_S) -> Cl(P^n_S)``."""
            from dzack_research.preamble.categories.divisors.general_divisors import (
                _projective_space_divisor_class_theory,
            )

            supplied = (base_picard_group, base_class_group, base_picard_to_class)
            if any(value is not None for value in supplied):
                if any(value is None for value in supplied):
                    raise ValueError(
                        "projective divisor-class theory requires the base Picard group, "
                        "base class group, and their comparison together"
                    )
                return _projective_space_divisor_class_theory(
                    self,
                    base_picard_group,
                    base_class_group,
                    base_picard_to_class,
                )

            base = self.scheme_base_ring()
            if base not in OwnedFields():
                raise NotImplementedError(
                    "the represented projective-space divisor class groups over a nonfield base "
                    "require the base Picard group, base class group, and their comparison"
                )
            from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
            from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            integers = _own_ring(SageZZ)
            zero_module = integers.free_module(finite_ordered_set(()))
            base_scheme = self.base_scheme()
            base_picard = PicardGroups().trivial(base_scheme)
            base_class = ClassGroups()(zero_module, scheme=base_scheme)
            comparison = base_picard.module_category().Mor(base_picard, base_class)({})
            return _projective_space_divisor_class_theory(
                self, base_picard, base_class, comparison
            )

        def picard_group(self, base_picard_group=None):
            r"""Return the represented Picard group of this projective space.

            With no supplied base Picard group, use the represented field-base
            divisor-class theory.  Supplying ``Pic(S)`` invokes the projective
            bundle formula ``Pic(P^n_S) = Pic(S) direct_sum ZZ[O(1)]``.
            """
            if base_picard_group is None:
                return self.divisor_class_theory().picard_group()
            from dzack_research.preamble.categories.divisors.general_divisors import (
                _projective_space_picard_group,
            )

            return _projective_space_picard_group(self, base_picard_group)

        def class_group(self):
            return self.divisor_class_theory().class_group()

        def homogeneous_coordinate_generators(self):
            r"""Return the selected homogeneous coordinate generators of this projective space."""
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

            ``P^n_R = Proj R[x_0,...,x_n]`` and ``U_i = D_+(x_i)`` is the
            spectrum of the degree-zero part of the graded localization at
            ``x_i``.  That degree-zero part is the polynomial ring on the ``n``
            ratios ``x_k/x_i`` with ``k`` other than ``i``, because
            ``x_i/x_i = 1``, so each chart is affine ``n``-space and the
            coordinate names record which ratio each variable is (Stacks, Tag
            01M3).
            """
            dimension = int(self.relative_dimension())
            base = self.scheme_base_ring()
            charts = tuple(
                AffineSpaces(base)(
                    dimension,
                    names=tuple(self._standard_chart_coordinate_name(index, numerator) for numerator in range(dimension + 1) if numerator != index),
                )
                for index in range(dimension + 1)
            )
            return finite_family(charts, name="Standard affine charts")

        def standard_affine_chart(self, index):
            r"""``U_i = D_+(x_i)``, the ``i``-th standard affine chart."""
            return self.standard_affine_charts()[int(index)]

        def standard_chart_overlap(self, chart_index, other_index):
            r"""``U_i cap U_j = D(x_j/x_i)``, an open of the ``i``-th chart.

            Inside ``U_i`` the locus where ``x_j`` does not vanish is where the
            ratio ``x_j/x_i`` is invertible, so the overlap is the
            distinguished open of that coordinate.
            """
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
            images = {}
            for numerator in range(dimension + 1):
                if numerator == target_index:
                    continue
                name = self._standard_chart_coordinate_name(target_index, numerator)
                if numerator == source_index:
                    images[name] = inverse_ratio
                else:
                    images[name] = restriction(self._standard_chart_coordinate(source_index, numerator)) * inverse_ratio
            into_target_chart = source_overlap.Mor(target_chart)(target_chart.coordinate_algebra().Mor(source_overlap.coordinate_algebra())(images))
            return target_overlap.corestriction(into_target_chart)

        def standard_chart_transition(self, source_index, target_index):
            r"""``phi_{ji}: U_i cap U_j -> U_j cap U_i``, the chart change and its inverse.

            On coordinates ``x_k/x_j = (x_k/x_i)(x_j/x_i)^{-1}`` and
            ``x_i/x_j = (x_j/x_i)^{-1}``, which is defined because ``x_j/x_i``
            is invertible on the overlap.  Exchanging the two indices gives the
            inverse map, so the overlaps are isomorphic and these are the
            transitions of the standard atlas (Stacks, Tag 01MM).
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

            return _coordinate_hyperplane_section_restriction(
                self, degree, coordinate_index
            )

        def coordinate_point_jet_evaluation(self, degree, coordinate_index, jet_order):
            r"""Evaluate ``O(degree)`` jets at the selected coordinate point."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _coordinate_point_jet_evaluation,
            )

            return _coordinate_point_jet_evaluation(
                self, degree, coordinate_index, jet_order
            )

        def sections_vanishing_to_order(
            self, degree, coordinate_index, vanishing_order
        ):
            r"""Return ``O(degree)`` sections vanishing to the stated order."""
            return self.coordinate_point_jet_evaluation(
                degree, coordinate_index, vanishing_order
            ).kernel()

        def imposed_multiplicity_linear_system(
            self, degree, coordinate_index, vanishing_order
        ):
            r"""Projectivize sections satisfying a coordinate-point multiplicity condition."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _coordinate_imposed_multiplicity_linear_system,
            )

            return _coordinate_imposed_multiplicity_linear_system(
                self, degree, coordinate_index, vanishing_order
            )

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

            dimension = int(self.relative_dimension())
            indices = tuple(range(dimension + 1))
            return FiniteAffineAtlasPresentation(
                self,
                tuple(self.standard_affine_chart(index) for index in indices),
                tuple(
                    self.standard_chart_transition(left, right)
                    for left, right in combinations(indices, 2)
                ),
                tuple(
                    _standard_projective_chart_embedding(self, index)
                    for index in indices
                ),
            )

        def glued_from_standard_charts(self):
            r"""``P^n_R`` presented as the gluing of its standard affine charts.

            The atlas verifies the inverse and triple-cocycle conditions on the
            represented overlaps, so this is the scheme those charts and
            transitions determine (Stacks, Tag 01JA).  It is the owned
            construction of projective space, as opposed to the adopted
            backend space this method is called on.
            """
            dimension = int(self.relative_dimension())
            indices = range(dimension + 1)
            return Schemes(self.scheme_base_ring()).glue_affine_atlas(
                tuple(self.standard_affine_chart(index) for index in indices),
                tuple(self.standard_chart_transition(left, right) for left, right in combinations(indices, 2)),
            )

        def zeta_function(self):
            r"""Return ``Z(P^d/F_q,T)=prod_{i=0}^d(1-q^i T)^(-1)``."""
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.misc.misc_c import prod
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = rationals.polynomial_ring("T")
            rational_functions = _refine_commutative_algebra(polynomial.fraction_field(), rationals, ("T",))
            T = rational_functions.algebra_generator("T")
            q = int(base.cardinality())
            d = int(self.relative_dimension())
            return prod(1 / (1 - q**i * T) for i in range(d + 1))


class ProductSchemes(OwnedCategoryOverBaseRing):
    r"""Scheme products equipped with their stated factors and projections."""

    def an_object(self):
        r"""The affine plane as a product of two affine lines."""
        ring = self.base_ring()
        line = AffineSpaces(ring)(1)
        return _scheme_product(line, line)

    def _repr_object_names(self):
        return f"scheme products over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return _placed_over_stated_base(candidate, self, ProductSchemes)

    class ParentMethods:
        def factors(self):
            r"""Return the exact indexed family whose product this is."""

            return self._preamble_product_factors

        def number_of_factors(self):
            return self.factors().cardinality()

        def projection(self, index):
            r"""Return the projection to the factor carrying label ``index``."""
            return self._preamble_product_projections[index]

        def projections(self):
            r"""Return the projections indexed by the same set as :meth:`factors`."""
            return self._preamble_product_projections

        def from_product_cone(self, legs):
            r"""Return the unique represented map into this selected product.

            The cone carries the same index set as the retained factor family.
            Affine products factor through the coordinate-algebra coproduct.
            Products of projective spaces use Sage's maintained polynomial
            morphism realization after concatenating the coordinate data of the
            labelled legs.  Glued mixed targets retain their projections but do
            not yet have a represented general map *into* the gluing.
            """
            factors = self.factors()
            factor_indices = factors.index_set()
            factor_labels = tuple(factor_indices)
            if isinstance(legs, IndexedFamily):
                if legs.index_set() is not factor_indices:
                    raise ValueError(
                        "a product cone is indexed by the product's exact factor index set"
                    )
            else:
                leg_values = tuple(legs)
                if len(leg_values) != len(factor_labels):
                    raise ValueError("a product cone has one leg per factor")

                def leg_at(label):
                    for position, known_label in enumerate(factor_labels):
                        if known_label == label:
                            return leg_values[position]
                    raise KeyError(label)

                legs = indexed_family(
                    factor_indices,
                    leg_at,
                    name="Product cone legs",
                )

            source = legs[factor_labels[0]].domain()
            if any(legs[label].domain() is not source for label in factor_labels):
                raise ValueError("a product cone has one apex")
            for factor_label in factor_labels:
                if legs[factor_label].codomain() is not factors[factor_label]:
                    raise ValueError(
                        f"the leg at {factor_label} must land in its indexed factor"
                    )

            base = self.scheme_base_ring()
            if self in Schemes(base).Affine():
                if source not in Schemes(base).Affine():
                    raise NotImplementedError(
                        "the affine product factorization currently requires an affine cone apex"
                    )
                product_algebra = self.coordinate_algebra()
                images = {}
                for factor_label in factor_labels:
                    leg = legs[factor_label]
                    factor = factors[factor_label]
                    projection_pullback = self.projection(
                        factor_label
                    ).coordinate_algebra_morphism()
                    leg_pullback = leg.coordinate_algebra_morphism()
                    factor_algebra = factor.coordinate_algebra()
                    if factor_algebra is base:
                        if leg != source.structure_morphism():
                            raise ValueError(
                                "the cone leg to the terminal base scheme must be the structure morphism"
                            )
                        continue
                    for generator_label in factor_algebra.algebra_generating_set():
                        generator = factor_algebra.algebra_generator(generator_label)
                        images[
                            _algebra_generator_label(
                                product_algebra,
                                projection_pullback(generator),
                            )
                        ] = leg_pullback(generator)
                pullback = (
                    source.structure_morphism().coordinate_algebra_morphism()
                    if product_algebra is base
                    else product_algebra.Mor(source.coordinate_algebra())(images)
                )
                cone = _affine_morphism_from_pullback(source, self, pullback)
            elif self in ProductProjectiveSpaces(base):
                coordinates = []
                for factor_label in factor_labels:
                    leg = legs[factor_label]
                    native = leg.native_morphism()
                    from sage.schemes.generic.morphism import SchemeMorphism_id

                    if isinstance(native, SchemeMorphism_id):
                        leg_coordinates = tuple(leg.domain().coordinate_ring().gens())
                    else:
                        defining_polynomials = getattr(
                            native,
                            "defining_polynomials",
                            None,
                        )
                        if defining_polynomials is None:
                            raise NotImplementedError(
                                "a map into a product of projective spaces requires each "
                                "represented leg to carry polynomial coordinate data"
                            )
                        leg_coordinates = tuple(defining_polynomials())
                    coordinates.extend(leg_coordinates)
                native = _native_scheme_homset(source, self)(
                    coordinates,
                    check=False,
                )
                cone = _categorical_scheme_morphism(
                    native,
                    domain=source,
                    codomain=self,
                )
            else:
                raise NotImplementedError(
                    "a general map into a glued mixed scheme product is not yet represented"
                )

            cone._preamble_product_cone_target = self
            cone._preamble_product_cone_legs = legs
            for factor_label in factor_labels:
                if self.projection(factor_label) * cone != legs[factor_label]:
                    raise ArithmeticError(
                        f"the product cone map does not recover leg {factor_label}"
                    )
            return cone



class ProductProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Finite products of projective spaces over one base ring."""

    def an_object(self):
        r"""The product of two projective lines."""
        ring = self.base_ring()
        line = ProjectiveSpaces(ring)(1)
        return _scheme_product(line, line)

    def _repr_object_names(self):
        return f"products of projective spaces over {self.base_ring()}"

    def super_categories(self):
        return [
            ProductSchemes(self.base_ring()),
            Schemes(self.base_ring()).Projective().Smooth(),
        ]

    def __contains__(self, candidate) -> bool:
        return _placed_over_stated_base(candidate, self, ProductProjectiveSpaces)

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
                cartesian_product(
                    *(
                        range(int(factors[label].relative_dimension()) + 1)
                        for label in factor_labels
                    )
                )
            )
            charts = {}
            embeddings = {}
            for choice in choices:
                local_factors = indexed_family(
                    factor_indices,
                    lambda label, choice=choice: factors[label].standard_affine_chart(
                        choice[positions[label]]
                    ),
                    name="Standard affine factors of a multiprojective chart",
                )
                chart = _scheme_product(local_factors)
                charts[choice] = chart
                chart_algebra = chart.coordinate_algebra()
                engine_coordinates = []
                for label in factor_labels:
                    factor = factors[label]
                    selected = choice[positions[label]]
                    pullback = chart.projection(label).coordinate_algebra_morphism()
                    for coordinate in range(int(factor.relative_dimension()) + 1):
                        value = (
                            chart_algebra.one()
                            if coordinate == selected
                            else pullback(
                                factor._standard_chart_coordinate(selected, coordinate)
                            )
                        )
                        engine_coordinates.append(_engine_element(chart_algebra, value))
                embeddings[choice] = _categorical_scheme_morphism(
                    _native_scheme_homset(chart, self)(engine_coordinates, check=False),
                    domain=chart,
                    codomain=self,
                )

            overlap_cache = {}

            def overlap(source_choice, target_choice):
                key = (source_choice, target_choice)
                cached = overlap_cache.get(key)
                if cached is not None:
                    return cached
                chart = charts[source_choice]
                element = chart.coordinate_algebra().one()
                for label in factor_labels:
                    position = positions[label]
                    source_index = source_choice[position]
                    target_index = target_choice[position]
                    if source_index == target_index:
                        continue
                    factor = factors[label]
                    pullback = chart.projection(label).coordinate_algebra_morphism()
                    element *= pullback(
                        factor._standard_chart_coordinate(source_index, target_index)
                    )
                cached = chart.distinguished_open(element)
                overlap_cache[key] = cached
                return cached

            def transition(source_choice, target_choice):
                source_chart = charts[source_choice]
                source_open = overlap(source_choice, target_choice)
                inclusion = source_open.inclusion()

                def leg(label):
                    position = positions[label]
                    factor = factors[label]
                    source_index = source_choice[position]
                    target_index = target_choice[position]
                    local_projection = source_chart.projection(label) * inclusion
                    if source_index == target_index:
                        return local_projection
                    source_factor_overlap = factor.standard_chart_overlap(
                        source_index,
                        target_index,
                    )
                    into_factor_overlap = source_factor_overlap.corestriction(
                        local_projection
                    )
                    changed = (
                        factor._standard_chart_change(source_index, target_index)
                        * into_factor_overlap
                    )
                    return (
                        factor.standard_chart_overlap(target_index, source_index).inclusion()
                        * changed
                    )

                into_target = charts[target_choice].from_product_cone(
                    indexed_family(
                        factor_indices,
                        leg,
                        name="Coordinatewise multiprojective chart transition legs",
                    )
                )
                return overlap(target_choice, source_choice).corestriction(into_target)

            transitions = {
                (left, right): _scheme_isomorphism(
                    transition(left, right),
                    transition(right, left),
                )
                for left, right in combinations(choices, 2)
            }
            return FiniteAffineAtlasPresentation(
                self,
                charts,
                transitions,
                embeddings,
            )

        def O(self, *degrees):
            r"""Return ``O(d_1,...,d_r)`` on this product of projective spaces."""
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                ProductProjectiveLineBundle,
            )

            degree_data = degrees[0] if len(degrees) == 1 and isinstance(degrees[0], (tuple, list, IndexedFamily)) else degrees
            return ProductProjectiveLineBundle(self, degree_data)

        @cached_method
        def canonical_line_bundle(self):
            return self.O(
                *(
                    -int(factor.relative_dimension()) - 1
                    for factor in self.factors()
                )
            )

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            return self.O(
                *(
                    int(factor.relative_dimension()) + 1
                    for factor in self.factors()
                )
            )

        anticanonical_bundle = anticanonical_line_bundle


def _algebra_generator_label(algebra, generator):
    r"""The label of an element that is one of the algebra's chosen generators."""
    for label in algebra.algebra_generating_set():
        if algebra.algebra_generator(label) == generator:
            return label
    assert False, f"{generator} is not a chosen algebra generator of {algebra}"


def _normal_placement(base_ring):
    r"""Whether \(\mathbb{A}^n_R\) and \(\mathbb{P}^n_R\) over ``base_ring`` are normal.

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
    a field.  Normality is not asserted over a base outside that hypothesis,
    which is why this is a criterion applied at construction and not a
    supercategory of ``AffineSpaces``.
    """
    return base_ring in OwnedPrincipalIdealDomains()


def _integral_placement(base_ring):
    try:
        return bool(_engine_ring(base_ring).is_integral_domain())
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return False


def _initialize_owned_affine_spectrum(
    scheme,
    algebra,
    base,
    *,
    extra_categories=(),
    is_base_scheme=False,
):
    r"""Install the owned affine-scheme structure on one native spectrum.

    Ordinary ``Spec(A)`` and fresh structured copies of the same affine scheme
    must carry exactly the same coordinate algebra, identity and structure
    morphism.  Only the ordinary ``Spec(R)`` over itself is the selected base
    scheme; a fresh copy of it still maps to that selected base scheme.
    """
    categories = [Schemes(base).Affine()]
    if algebra is base or algebra in FramedAlgebras(base):
        categories.extend(
            (
                Schemes(base).FiniteType(),
                Schemes(base).QuasiProjective(),
            )
        )
    if algebra is base:
        categories.append(Schemes(base).Smooth())
        if _normal_placement(base):
            categories.append(Schemes(base).Normal())
    if _integral_placement(algebra):
        categories.append(Schemes(base).Integral())
    categories.extend(extra_categories)

    _refine_scheme(scheme, base, categories)
    scheme._preamble_engine_coordinate_ring = _engine_ring(algebra)
    scheme._preamble_coordinate_algebra = algebra

    engine_identity = _engine_ring(algebra).hom(_engine_ring(algebra))
    coordinate_identity = base.Mor(base).identity() if algebra is base else algebra.Mor(algebra).identity()
    scheme._preamble_identity_morphism = SchemeMorphism(
        _native_scheme_homset(scheme, scheme)(engine_identity, check=False),
        domain=scheme,
        codomain=scheme,
        pullback=coordinate_identity,
    )

    if is_base_scheme:
        scheme._preamble_structure_morphism = scheme._preamble_identity_morphism
        return scheme

    base_scheme = (base).affine_spectrum(base_ring=base)
    engine_map = _engine_ring(algebra).coerce_map_from(_engine_ring(base))
    if engine_map is None:
        raise NotImplementedError("the affine Spec structure morphism currently requires an exact engine realization of the algebra structure map")
    structure_pullback = coordinate_identity if algebra is base else algebra.algebra_structure_morphism()
    scheme._preamble_structure_morphism = SchemeMorphism(
        _native_scheme_homset(scheme, base_scheme)(engine_map, check=False),
        domain=scheme,
        codomain=base_scheme,
        pullback=structure_pullback,
    )
    return scheme


def _fresh_affine_spectrum(algebra, base, *, extra_categories=()):
    r"""Return a fresh affine spectrum carrying the stated owned coordinate algebra."""

    return _initialize_owned_affine_spectrum(
        typecall(
            _SageAffineScheme,
            _engine_ring(algebra),
            _engine_ring(base),
        ),
        algebra,
        base,
        extra_categories=extra_categories,
    )


@cached_function
def _affine_spectrum_from_owned_algebra(algebra, base):
    r"""Private constructor for one selected affine spectrum over ``base``."""
    cache_key = (id(algebra), id(base))
    cached = _AFFINE_SPECTRA.get(cache_key)
    if cached is not None and cached.coordinate_algebra() is algebra and cached.scheme_base_ring() is base:
        return cached

    scheme = _initialize_owned_affine_spectrum(
        typecall(
            _SageAffineScheme,
            _engine_ring(algebra),
            _engine_ring(base),
        ),
        algebra,
        base,
        is_base_scheme=algebra is base,
    )
    _AFFINE_SPECTRA[cache_key] = scheme
    return scheme


def _affine_spectrum(ring_or_algebra, base_ring=None):
    r"""Return the category-owned affine scheme ``Spec(A)`` over its scalar base.

    If ``A`` is an owned commutative ``R``-algebra, the returned object lies in
    ``Schemes(R)`` and its structure morphism is induced contravariantly by
    ``R -> A``.  A bare commutative ring ``R`` is read as an ``R``-algebra over
    itself when it is supplied as the explicit ``base_ring``, so
    ``Spec(R, base_ring=R)`` is the terminal affine ``R``-scheme.  Omitting the
    base retains the coordinate algebra's represented scalar base.
    """
    algebra = _own_ring(ring_or_algebra)
    if base_ring is None:
        try:
            declared_base = algebra.algebra_base_ring()
        except AttributeError:
            base = algebra
        else:
            # A bare owned ring is canonically an algebra over itself.  Some
            # constructor-owned refinements (notably the public QQ view) share an
            # engine with the foundational owned ring returned by the generic
            # algebra-base accessor, but are a different owned parent.  Spec(R)
            # must stay over the stated R, not silently switch to that second view.
            base = algebra if _engine_ring(declared_base) is _engine_ring(algebra) else _own_ring(declared_base)
    else:
        base = _own_ring(base_ring)

    return Schemes(base).Affine()(algebra)


def _selected_or_rebuilt_engine_morphism(pullback):
    r"""The realization the morphism chose when it was built, else one rebuilt from a framing.

    A ring morphism answers with its selected realization and otherwise
    declines, which is not the end of the question: a framed domain still lets
    the generic bridge rebuild the native map from the images of the algebra
    generators, and that is where a plain ``Spec`` of a localization map is
    answered.  A semilinear algebra map retains an ordinary algebra morphism
    into the restricted-scalar target; that target has the same computation
    ring as the stated target algebra, so the retained map is also the native
    realization of the underlying ring pullback.
    """
    if isinstance(pullback, RingMorphism):
        try:
            return pullback._engine_morphism_crossing()
        except NotImplementedError:
            pass
    algebra_morphism = getattr(pullback, "algebra_morphism", None)
    if callable(algebra_morphism):
        represented = algebra_morphism()
        if (
            _engine_ring(represented.domain()) is _engine_ring(pullback.domain())
            and _engine_ring(represented.codomain()) is _engine_ring(pullback.codomain())
        ):
            return _engine_algebra_morphism(represented)
    return _engine_algebra_morphism(pullback)


def _engine_coordinate_pullback(pullback):
    r"""Return the private Sage ring map realizing one coordinate pullback.

    A morphism that selected an engine realization when it was built supplies
    it, and a framed algebra lets the generic bridge rebuild one from the
    images of the algebra generators.  Where neither holds, a canonical Sage
    coercion between the two engines is an admissible realization once it is
    checked against the owned morphism on a finite family of elements that
    already determines a map out of the source, since agreeing there is
    agreeing everywhere.

    Two sources supply such a family.  A relative selected presentation can
    have a flattened Sage quotient engine whose polynomial generators include
    generators of the scalar ring, so the owned morphism holds the right map
    while the bridge cannot rebuild the flattened one; there the family is the
    algebra generators together with the scalar generators through the
    structure morphism.  A localization has no algebra generating family at
    all, and a map out of ``S^{-1}A`` is determined by its restriction along
    the map from the ring below, so there the family comes from the framed
    algebra at the foot of the localization tower.  That is the case a
    distinguished open of a distinguished open reaches, where the two engines
    are one-step Sage localizations of one ring and the coercion between them
    is the map over that ring.
    """
    try:
        return _selected_or_rebuilt_engine_morphism(pullback)
    except (NotImplementedError, ValueError) as error:
        source_algebra = pullback.domain()
        target_algebra = pullback.codomain()
        base = source_algebra.base_ring()
        if source_algebra in LocalizationRings():
            test_values = _elements_determining_maps_out_of(source_algebra, base)
            if test_values is None:
                raise error
        else:
            scalar_base = base.base_ring()
            if source_algebra not in FramedAlgebras(base) or base not in FramedAlgebras(scalar_base):
                raise error
            algebra_labels = source_algebra.algebra_generating_set()
            scalar_labels = base.algebra_generating_set()
            if not algebra_labels.cardinality().is_finite() or not scalar_labels.cardinality().is_finite():
                raise error
            test_values = tuple(source_algebra.algebra_generator(label) for label in algebra_labels) + tuple(
                source_algebra(source_algebra.algebra_structure_morphism()(base.algebra_generator(label))) for label in scalar_labels
            )
        engine_morphism = _engine_ring(target_algebra).coerce_map_from(_engine_ring(source_algebra))
        if engine_morphism is None:
            raise error
        if any(engine_morphism(_engine_element(source_algebra, value)) != _engine_element(target_algebra, pullback(value)) for value in test_values):
            raise error
        return engine_morphism


def _affine_morphism_from_pullback(
    domain: Any,
    codomain: Any,
    pullback: Any,
) -> SchemeMorphism:
    r"""Site one represented coordinate pullback on the stated affine endpoints."""
    domain_algebra = domain.coordinate_algebra()
    codomain_algebra = codomain.coordinate_algebra()
    if pullback.domain() is not codomain_algebra or pullback.codomain() is not domain_algebra:
        raise ValueError("an affine scheme morphism requires a pullback from the codomain algebra to the domain algebra")
    native = _native_scheme_homset(domain, codomain)(
        _engine_coordinate_pullback(pullback),
        check=False,
    )
    return SchemeMorphism(
        native,
        domain=domain,
        codomain=codomain,
        pullback=pullback,
    )


def _affine_endomorphism_from_pullback(
    scheme: Any,
    pullback: Any,
) -> SchemeMorphism:
    r"""Site a represented coordinate pullback on the stated affine scheme."""
    return _affine_morphism_from_pullback(scheme, scheme, pullback)


def _polynomial_exponents(exponent: Any, variable_count: int) -> tuple[int, ...]:
    r"""Normalize a Sage polynomial dictionary exponent to a tuple."""
    if variable_count == 1 and not isinstance(exponent, tuple):
        return (int(exponent),)
    return tuple(int(value) for value in exponent)


def _copy_polynomial_by_exponents(
    polynomial: Any,
    target_ring: Any,
    target_variables: tuple[Any, ...],
) -> Any:
    r"""Copy a polynomial to named-independent variables by its exponent dictionary."""
    source = polynomial.parent()
    variable_count = len(source.gens())
    if len(target_variables) != variable_count:
        raise ValueError("polynomial transport requires the same number of variables")
    result = target_ring.zero()
    for exponent, coefficient in polynomial.dict().items():
        powers = _polynomial_exponents(exponent, variable_count)
        term = target_ring(coefficient)
        for variable, power in zip(target_variables, powers):
            term *= variable**power
        result += term
    return result


def _evaluate_owned_homogeneous_polynomial_on_coordinates(
    polynomial,
    polynomial_ring,
    coordinates,
):
    r"""Evaluate one owned homogeneous polynomial on an owned coordinate family."""
    polynomial = polynomial_ring(polynomial)
    labels = tuple(polynomial_ring.algebra_generating_set())
    coordinates = tuple(coordinates)
    if len(coordinates) != len(labels):
        raise ValueError("homogeneous substitution needs one coordinate per target variable")
    source_ring = coordinates[0].parent()
    if any(coordinate.parent() is not source_ring for coordinate in coordinates):
        raise ValueError("projective homogeneous coordinates must lie in one source ring")
    base = polynomial_ring.base_ring()
    if source_ring.base_ring() is not base:
        raise ValueError("projective substitution requires one scalar base")
    scalar_map = source_ring.algebra_structure_morphism()
    backend = _engine_element(polynomial_ring, polynomial)
    engine = _engine_ring(polynomial_ring)
    engine_base = _engine_ring(base)
    result = source_ring.zero()
    for exponent, coefficient in engine(backend).monomial_coefficients().items():
        powers = _polynomial_exponents(exponent, len(labels))
        term = scalar_map(base._from_engine_element(engine_base(coefficient)))
        for coordinate, power in zip(coordinates, powers, strict=True):
            if power:
                term *= coordinate**power
        result += term
    return source_ring(result)


def _evaluate_polynomial_in_algebra(polynomial: Any, algebra: Any) -> Any:
    r"""Evaluate a backend polynomial on the selected generators of ``algebra``."""
    labels = tuple(algebra.algebra_generating_set())
    source = polynomial.parent()
    if len(source.gens()) != len(labels):
        raise ValueError("the polynomial certificate has the wrong number of invariant variables")
    base = algebra.base_ring()
    engine_base = _engine_ring(base)
    result = algebra.zero()
    for exponent, coefficient in polynomial.dict().items():
        powers = _polynomial_exponents(exponent, len(labels))
        term = algebra.algebra_structure_morphism()(base._from_engine_element(engine_base(coefficient)))
        for label, power in zip(labels, powers):
            term *= algebra.algebra_generator(label) ** power
        result += term
    return algebra(result)


def _affine_linear_invariant_algebra_data(
    scheme: Any,
) -> tuple[Any, Any, tuple[Any, ...]]:
    r"""Return a finite presentation of ``A^G`` and its inclusion into ``A``.

    This is the private computation boundary for the first supported affine
    quotient regime: ``A`` is a polynomial algebra over a field, ``G`` is
    finite with chosen generators, and the represented pullbacks are linear on
    the selected polynomial generators.  Sage's matrix-group interface routes
    invariant generation to Singular; Sage's elimination ideal computes the
    kernel of the polynomial map on the returned invariant generators.
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
    if group.is_finite() is not True or group not in GroupsWithChosenFiniteGeneratingSet():
        raise NotImplementedError("the represented invariant algebra currently requires a finite group with a chosen finite generating set")
    algebra = scheme.coordinate_algebra()
    base = scheme.scheme_base_ring()
    if algebra not in SymmetricAlgebras(base) or algebra not in FramedAlgebras(base):
        raise NotImplementedError("the represented invariant-ring backend currently requires a polynomial coordinate algebra")
    labels = tuple(algebra.algebra_generating_set())
    if not algebra.algebra_generating_set().cardinality().is_finite():
        raise NotImplementedError("the represented invariant-ring backend requires finitely many polynomial generators")
    engine_algebra = _engine_ring(algebra)
    variables = tuple(engine_algebra.gens())
    if len(variables) != len(labels):
        raise ArithmeticError("the selected polynomial framing disagrees with its computation engine")
    engine_base = _engine_ring(base)
    if not bool(engine_base.is_field()):
        raise NotImplementedError("the selected Singular invariant-ring backend currently requires a field of coefficients")

    # The polynomial algebra on no generators is the scalar field itself.
    # Every represented scheme automorphism is over the stated base, hence its
    # pullback fixes that algebra pointwise; there is nothing for Singular to
    # generate in this zero-dimensional case.
    if not variables:
        return (
            algebra,
            algebra.Mor(algebra).identity(),
            (),
        )

    group_generators = tuple(group.group_generators())
    if not group_generators:
        return (
            algebra,
            algebra.Mor(algebra).identity(),
            tuple(variables),
        )

    backend_matrices = []
    pullbacks = []
    for group_generator in group_generators:
        pullback = scheme.action_of(group_generator).coordinate_algebra_morphism()
        pullbacks.append(pullback)
        image_rows = []
        for label in labels:
            image = engine_algebra(_engine_element(algebra, pullback(algebra.algebra_generator(label))))
            row = []
            linear_part = engine_algebra.zero()
            for variable in variables:
                coefficient = image.monomial_coefficient(variable)
                row.append(engine_base(coefficient))
                linear_part += coefficient * variable
            if image != linear_part:
                raise NotImplementedError("the selected invariant-ring backend currently requires a linear action on polynomial generators")
            # Sage/Singular's matrix-group invariant convention acts on the
            # coordinate variables by the transpose of the supplied matrix.
            # Rows here are therefore the actual pullback images of the chosen
            # variables, so the backend receives the needed transpose matrix.
            image_rows.append(row)
        backend_matrices.append(sage_matrix(engine_base, image_rows))

    backend_group = cast(Any, MatrixGroup(backend_matrices))
    try:
        backend_invariants = tuple(backend_group.invariant_generators())
    except (NotImplementedError, TypeError, ValueError) as error:
        raise NotImplementedError("Sage/Singular does not support invariant generation for this coefficient field and linear action") from error
    if not backend_invariants:
        raise ArithmeticError("a positive-dimensional polynomial invariant ring needs algebra generators")

    engine_invariants = tuple(
        _copy_polynomial_by_exponents(
            invariant,
            engine_algebra,
            variables,
        )
        for invariant in backend_invariants
    )
    invariant_elements = tuple(algebra._from_engine_element(invariant) for invariant in engine_invariants)
    if any(pullback(invariant) != invariant for pullback in pullbacks for invariant in invariant_elements):
        raise ArithmeticError("the backend invariant generators do not match the represented coordinate action")

    invariant_labels = tuple(f"invariant_{index}" for index in range(len(engine_invariants)))
    presentation = base.free_module(invariant_labels).symmetric_algebra()
    presentation_engine = _engine_ring(presentation)

    ambient_count = len(variables)
    invariant_count = len(engine_invariants)
    combined = SagePolynomialRing(
        engine_base,
        ambient_count + invariant_count,
        names=tuple(f"ambient_{index}" for index in range(ambient_count)) + tuple(f"invariant_{index}" for index in range(invariant_count)),
    )
    ambient_variables = tuple(combined.gens()[:ambient_count])
    invariant_variables = tuple(combined.gens()[ambient_count:])
    graph_ideal = combined.ideal(
        tuple(
            invariant_variables[index]
            - _copy_polynomial_by_exponents(
                invariant,
                combined,
                ambient_variables,
            )
            for index, invariant in enumerate(engine_invariants)
        )
    )
    kernel = cast(Any, graph_ideal).elimination_ideal(ambient_variables)
    relations = []
    for relation in kernel.gens():
        if relation == combined.zero():
            continue
        relation_terms = {}
        for exponent, coefficient in relation.dict().items():
            powers = _polynomial_exponents(
                exponent,
                ambient_count + invariant_count,
            )
            if any(powers[:ambient_count]):
                raise ArithmeticError("the elimination backend returned a non-eliminated relation")
            relation_terms[powers[ambient_count:]] = coefficient
        relations.append(presentation._from_engine_element(presentation_engine(relation_terms)))
    invariant_algebra = presentation if not relations else (presentation).quotient_by_relations(tuple(relations))
    invariant_labels = tuple(invariant_algebra.algebra_generating_set())
    inclusion = invariant_algebra.Mor(algebra)({label: invariant_elements[index] for index, label in enumerate(invariant_labels)})
    return invariant_algebra, inclusion, engine_invariants


def _affine_spec_morphism(algebra_morphism):
    r"""Return the affine scheme morphism contravariantly induced by an algebra map."""

    source_algebra = algebra_morphism.domain()
    target_algebra = algebra_morphism.codomain()
    source_base = source_algebra.base_ring()
    target_base = target_algebra.base_ring()
    if (
        source_algebra not in Algebras(source_base).Associative().Unital().Commutative()
        or target_algebra not in Algebras(target_base).Associative().Unital().Commutative()
    ):
        raise TypeError("affine Spec acts on a represented algebra morphism")
    return _affine_morphism_from_pullback(
        (target_algebra).affine_spectrum(),
        (source_algebra).affine_spectrum(),
        algebra_morphism,
    )


def _normalized_space_names(names):
    if names is None or isinstance(names, str):
        return names
    return tuple(names)


def _fresh_affine_space_from_owned_data(base, engine_dimension, names):
    r"""Construct one fresh owned affine-space carrier from the stated data.

    Sage's public ``AffineSpace`` constructor interns equal spaces.  That is
    correct for the ordinary ``A^n_R`` constructor but wrong for structured
    products: two chart products with equal coordinate presentation can carry
    different factor roles and projection maps.  Build a fresh instance of the
    selected Sage implementation class here; the cached public wrapper below
    still supplies canonical ordinary affine spaces.
    """
    engine_base = _engine_ring(base)
    prototype = (
        _SageAffineSpace(engine_dimension, engine_base)
        if names is None
        else _SageAffineSpace(engine_dimension, engine_base, names=names)
    )
    normalized_names = prototype.coordinate_ring().variable_names()
    scheme = typecall(
        type(prototype),
        engine_dimension,
        engine_base,
        normalized_names,
        None,
        None,
    )
    engine_coordinate_ring = getattr(scheme, "_preamble_engine_coordinate_ring", None)
    if engine_coordinate_ring is None:
        engine_coordinate_ring = scheme.coordinate_ring()
    categories = [AffineSpaces(base)]
    if _integral_placement(base):
        categories.append(Schemes(base).Integral())
    if _normal_placement(base):
        categories.append(Schemes(base).Normal())
    _refine_scheme(scheme, base, categories)

    labels = tuple(engine_coordinate_ring.variable_names())
    scheme._preamble_engine_coordinate_ring = engine_coordinate_ring
    scheme._preamble_coordinate_algebra = _refine_commutative_algebra(
        _own_ring(engine_coordinate_ring),
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )
    scheme._preamble_identity_morphism = _refine_scheme_morphism(
        _native_scheme_homset(scheme, scheme)(
            list(engine_coordinate_ring.gens()),
            check=False,
        ),
        base,
        domain=scheme,
        codomain=scheme,
        pullback=scheme.coordinate_algebra().Mor(
            scheme.coordinate_algebra()
        ).identity(),
    )
    base_scheme = (base).affine_spectrum(base_ring=base)
    engine_map = engine_coordinate_ring.coerce_map_from(_engine_ring(base))
    if engine_map is None:
        raise NotImplementedError("the affine-space structure morphism requires the scalar base injection")
    scheme._preamble_structure_morphism = _refine_scheme_morphism(
        _native_scheme_homset(scheme, base_scheme)(engine_map, check=False),
        base,
        domain=scheme,
        codomain=base_scheme,
        pullback=scheme.coordinate_algebra().algebra_structure_morphism(),
    )
    return scheme


@cached_function
def _affine_space_from_owned_data(base, engine_dimension, names):
    r"""Return the canonical ordinary affine space for this constructor datum."""
    return _fresh_affine_space_from_owned_data(base, engine_dimension, names)



def _fresh_projective_space_from_owned_data(base, engine_dimension, names):
    r"""Construct one fresh owned projective-space carrier from the stated data.

    As for affine spaces, structured constructions need a carrier whose retained
    maps cannot be overwritten through Sage's canonical parent cache.  Ordinary
    ``ProjectiveSpace`` remains canonical through ``_projective_space_from_owned_data``.
    """
    engine_base = _engine_ring(base)
    prototype = (
        _SageProjectiveSpace(engine_dimension, engine_base)
        if names is None
        else _SageProjectiveSpace(engine_dimension, engine_base, names=names)
    )
    normalized_names = prototype.coordinate_ring().variable_names()
    scheme = typecall(
        type(prototype),
        engine_dimension,
        engine_base,
        normalized_names,
    )
    categories = [ProjectiveSpaces(base)]
    if _integral_placement(base):
        categories.append(Schemes(base).Integral())
    if _normal_placement(base):
        categories.append(Schemes(base).Normal())
    return _refine_scheme(scheme, base, categories)


@cached_function
def _projective_space_from_owned_data(base, engine_dimension, names):
    r"""Return the canonical ordinary projective space for this constructor datum."""
    return _fresh_projective_space_from_owned_data(base, engine_dimension, names)



def _product_projection(product, factor, coordinates):
    native = _native_scheme_homset(product, factor)(list(coordinates), check=False)
    pullback = None
    if product in Schemes(product.scheme_base_ring()).Affine() and factor in Schemes(factor.scheme_base_ring()).Affine():
        target = product.coordinate_algebra()
        source = factor.coordinate_algebra()
        engine_target = _engine_ring(target)
        owned_coordinates = tuple(target._from_engine_element(engine_target(coordinate)) for coordinate in coordinates)
        pullback = source.Mor(target)(
            {
                label: image
                for label, image in zip(
                    source.algebra_generating_set(),
                    owned_coordinates,
                    strict=True,
                )
            }
        )
    return _categorical_scheme_morphism(
        native,
        domain=product,
        codomain=factor,
        pullback=pullback,
    )


def _standard_projective_chart_embedding(projective, chart_index):
    r"""Return the standard open-chart morphism ``U_i -> P^n``.

    The affine chart has coordinates ``x_k/x_i``.  Its map to projective
    space is therefore the homogeneous tuple with coordinate ``i`` equal to
    one and every other coordinate equal to the corresponding affine ratio.
    The native projective Hom is private; the returned arrow has the selected
    owned endpoints.
    """
    chart_index = int(chart_index)
    chart = projective.standard_affine_chart(chart_index)
    algebra = chart.coordinate_algebra()
    coordinates = []
    for numerator in range(int(projective.relative_dimension()) + 1):
        if numerator == chart_index:
            coordinates.append(algebra.one())
        else:
            coordinates.append(
                projective._standard_chart_coordinate(chart_index, numerator)
            )
    return _ProjectiveCoordinateMorphism(
        _scheme_mor_category(chart, projective),
        coordinates,
    )


def _install_scheme_product_data(product, factors, projections):
    r"""Retain one indexed factor family and the correspondingly indexed projections."""
    factors = _finite_factor_family(factors, name="Product factors")
    labels = tuple(factors.index_set())
    projection_values = tuple(projections)
    if len(labels) != len(projection_values):
        raise ValueError("a scheme product has exactly one projection for each factor label")

    def projection_at(label):
        for position, known_label in enumerate(labels):
            if known_label == label:
                return projection_values[position]
        raise KeyError(label)

    for position, label in enumerate(labels):
        projection_values[position]._preamble_product_projection_label = label

    product._preamble_product_factors = factors
    product._preamble_product_projections = indexed_family(
        factors.index_set(),
        projection_at,
        name="Scheme product projections",
    )
    return product


def _mixed_affine_projective_product(factors, base):
    r"""Glue a finite product containing affine and projective factors.

    For each projective factor choose one standard affine chart.  The product
    of those charts with all affine factors is affine.  Two such product
    charts overlap where every changed homogeneous coordinate ratio is a unit,
    hence on one represented distinguished open (the product of those ratios).
    Coordinatewise projective chart changes and identities on the affine
    factors give the finite gluing.  The local factor projections agree on
    overlaps, so they glue to the categorical product projections.
    """
    factors = _finite_factor_family(factors, name="Product factors")
    schemes = tuple(factors)
    projective_positions = tuple(position for position, scheme in enumerate(schemes) if scheme in ProjectiveSpaces(base))
    chart_labels = tuple(cartesian_product(*(range(int(schemes[position].relative_dimension()) + 1) for position in projective_positions)))
    projective_slot = {position: slot for slot, position in enumerate(projective_positions)}
    charts = {}
    for label in chart_labels:
        local_factors = []
        for position, scheme in enumerate(schemes):
            if position in projective_slot:
                local_factors.append(scheme.standard_affine_chart(label[projective_slot[position]]))
            else:
                local_factors.append(scheme)
        charts[label] = _scheme_product(tuple(local_factors))

    overlap_cache = {}

    def overlap(source_label, target_label):
        key = (source_label, target_label)
        cached = overlap_cache.get(key)
        if cached is not None:
            return cached
        chart = charts[source_label]
        algebra = chart.coordinate_algebra()
        element = algebra.one()
        for position in projective_positions:
            slot = projective_slot[position]
            source_index = source_label[slot]
            target_index = target_label[slot]
            if source_index == target_index:
                continue
            projective = schemes[position]
            pullback = chart.projection(position).coordinate_algebra_morphism()
            element *= pullback(projective._standard_chart_coordinate(source_index, target_index))
        cached = chart.distinguished_open(element)
        overlap_cache[key] = cached
        return cached

    def transition(source_label, target_label):
        source_chart = charts[source_label]
        target_chart = charts[target_label]
        source_open = overlap(source_label, target_label)
        inclusion = source_open.inclusion()
        legs = []
        for position, scheme in enumerate(schemes):
            local_projection = source_chart.projection(position) * inclusion
            if position not in projective_slot:
                legs.append(local_projection)
                continue
            slot = projective_slot[position]
            source_index = source_label[slot]
            target_index = target_label[slot]
            if source_index == target_index:
                legs.append(local_projection)
                continue
            source_factor_overlap = scheme.standard_chart_overlap(
                source_index,
                target_index,
            )
            into_factor_overlap = source_factor_overlap.corestriction(local_projection)
            changed = scheme._standard_chart_change(source_index, target_index) * into_factor_overlap
            legs.append(scheme.standard_chart_overlap(target_index, source_index).inclusion() * changed)
        into_target_chart = target_chart.from_product_cone(tuple(legs))
        return overlap(target_label, source_label).corestriction(into_target_chart)

    transitions = tuple(
        _scheme_isomorphism(
            transition(left, right),
            transition(right, left),
        )
        for left, right in combinations(chart_labels, 2)
    )
    product = Schemes(base).glue_affine_atlas(
        tuple(charts[label] for label in chart_labels),
        transitions,
    )
    datum = product.gluing_datum()
    projections = []
    for position, factor in enumerate(schemes):
        local_maps = []
        for label in chart_labels:
            chart = charts[label]
            local_projection = chart.projection(position)
            if position in projective_slot:
                chart_index = label[projective_slot[position]]
                local_projection = _standard_projective_chart_embedding(factor, chart_index) * local_projection
            local_maps.append(local_projection)
        projections.append(product.Mor(factor)(tuple(local_maps)))

    categories = [ProductSchemes(base)]
    for placement in (
        Schemes(base).Separated(),
        Schemes(base).FiniteType(),
        Schemes(base).Smooth(),
    ):
        if all(factor in placement for factor in schemes):
            categories.append(placement)

    # A finite-type affine morphism is quasi-projective; projective spaces are
    # projective, hence quasi-projective.  This criterion is strictly about the
    # represented mixed regime and does not tag arbitrary affine schemes that
    # have no finite-type placement.
    if all(
        factor in Schemes(base).QuasiProjective()
        or (factor in Schemes(base).Affine() and factor in Schemes(base).FiniteType())
        for factor in schemes
    ):
        categories.append(Schemes(base).QuasiProjective())

    # For products of the standard affine/projective spaces the local charts
    # are polynomial rings over the base.  Hence integral/normal placement is
    # inherited from the same base criteria used by the individual spaces.
    standard_spaces = all(
        factor in AffineSpaces(base) or factor in ProjectiveSpaces(base)
        for factor in schemes
    )
    if standard_spaces and _integral_placement(base):
        categories.append(Schemes(base).Integral())
    if standard_spaces and _normal_placement(base):
        categories.append(Schemes(base).Normal())
    _refine_scheme(product, base, categories)
    product._preamble_relative_dimension = sum(int(factor.relative_dimension()) for factor in schemes)
    _install_scheme_product_data(product, factors, projections)
    product._preamble_mixed_product_gluing_datum = datum
    return product


def _scheme_product(*schemes):
    r"""Return the categorical product in the currently supported scheme regimes.

    The defining datum is an indexed family.  Positional arguments and one
    tuple/list are syntactic ingress for the family on the canonical finite
    ordinal; an explicit :class:`IndexedFamily` keeps its exact index set, so
    repeated equal or identical factors still have distinct mathematical roles.

    Affine spaces use ``A^m x A^n = A^{m+n}``; general represented affine
    factors use the coproduct of their coordinate algebras; projective spaces
    use Sage's multiprojective computation privately; finite mixtures of affine
    schemes and projective spaces are glued from products of their affine charts.
    Every route retains the same indexed factors and actual projection morphisms.
    """
    factor_input = (
        schemes[0]
        if len(schemes) == 1 and isinstance(schemes[0], (tuple, list, IndexedFamily))
        else schemes
    )
    factors = _finite_factor_family(factor_input, name="Product factors")
    factor_labels = tuple(factors.index_set())
    if len(factor_labels) < 2:
        raise ValueError("a represented scheme product requires at least two factors")
    scheme_values = tuple(factors[label] for label in factor_labels)
    base = scheme_values[0].scheme_base_ring()
    if any(scheme not in Schemes(base) for scheme in scheme_values):
        raise TypeError("all product factors must be schemes over the same base")
    if any(scheme.scheme_base_ring() is not base for scheme in scheme_values):
        raise ValueError("all product factors must have the same represented base ring")

    if all(scheme in AffineSpaces(base) for scheme in scheme_values):
        dimensions = tuple(int(scheme.relative_dimension()) for scheme in scheme_values)
        names = tuple(
            f"x{factor}_{coordinate}"
            for factor, dimension in enumerate(dimensions)
            for coordinate in range(dimension)
        )
        product = _fresh_affine_space_from_owned_data(
            base,
            sum(dimensions),
            _normalized_space_names(names),
        )
        _refine_scheme(product, base, [ProductSchemes(base)])
        coordinates = tuple(product._preamble_engine_coordinate_ring.gens())
        projections = []
        offset = 0
        for factor, dimension in zip(scheme_values, dimensions, strict=True):
            projections.append(
                _product_projection(
                    product,
                    factor,
                    coordinates[offset : offset + dimension],
                )
            )
            offset += dimension
    elif all(scheme in ProjectiveSpaces(base) for scheme in scheme_values):
        names = tuple(
            f"x{factor}_{coordinate}"
            for factor, scheme in enumerate(scheme_values)
            for coordinate in range(int(scheme.relative_dimension()) + 1)
        )
        product = _SageProductProjectiveSpaces(
            [int(scheme.relative_dimension()) for scheme in scheme_values],
            _engine_ring(base),
            names=names,
        )
        categories = [ProductProjectiveSpaces(base)]
        if _integral_placement(base):
            categories.append(Schemes(base).Integral())
        if _normal_placement(base):
            categories.append(Schemes(base).Normal())
        _refine_scheme(product, base, categories)
        coordinates = tuple(product.coordinate_ring().gens())
        projections = []
        offset = 0
        for factor in scheme_values:
            width = int(factor.relative_dimension()) + 1
            projections.append(
                _product_projection(
                    product,
                    factor,
                    coordinates[offset : offset + width],
                )
            )
            offset += width
    elif all(scheme in Schemes(base).Affine() for scheme in scheme_values):
        base_scheme = (base).affine_spectrum(base_ring=base)
        nonterminal_positions = tuple(
            position
            for position, scheme in enumerate(scheme_values)
            if scheme is not base_scheme
        )
        if len(nonterminal_positions) != len(scheme_values):
            # ``Spec(R)`` is terminal in ``Sch/R``.  A selected product that
            # includes terminal factors is therefore a fresh copy of the
            # product of the remaining factors, with the omitted projections
            # supplied by its structure morphism.  Keeping the copy fresh
            # retains this product's exact factor family without attaching
            # caller-specific product data to a pre-existing scheme.
            if not nonterminal_positions:
                reduced = base_scheme
            elif len(nonterminal_positions) == 1:
                reduced = scheme_values[nonterminal_positions[0]]
            else:
                reduced = _scheme_product(
                    tuple(scheme_values[position] for position in nonterminal_positions)
                )
            algebra = reduced.coordinate_algebra()
            product = _fresh_affine_spectrum(
                algebra,
                base,
                extra_categories=(ProductSchemes(base),),
            )
            identity_pullback = (
                base.Mor(base).identity()
                if algebra is base
                else algebra.Mor(algebra).identity()
            )
            to_reduced = _affine_morphism_from_pullback(
                product, reduced, identity_pullback
            )
            nonterminal_rank = {
                original: rank
                for rank, original in enumerate(nonterminal_positions)
            }
            projections = []
            for position, factor in enumerate(scheme_values):
                if factor is base_scheme:
                    projections.append(product.structure_morphism())
                elif len(nonterminal_positions) == 1:
                    projections.append(to_reduced)
                else:
                    projections.append(
                        reduced.projection(nonterminal_rank[position]) * to_reduced
                    )
        else:
            algebras = tuple(scheme.coordinate_algebra() for scheme in scheme_values)
            commutative_algebras = Algebras(base).Associative().Unital().Commutative()
            algebra = commutative_algebras.coproduct((algebras[0], algebras[1]))
            factor_maps = list(algebra.coproduct_injections())
            for next_algebra in algebras[2:]:
                new_algebra = commutative_algebras.coproduct((algebra, next_algebra))
                left_map, right_map = new_algebra.coproduct_injections()
                factor_maps = [left_map * factor_map for factor_map in factor_maps] + [right_map]
                algebra = new_algebra
            product = _fresh_affine_spectrum(
                algebra,
                base,
                extra_categories=(ProductSchemes(base),),
            )
            projections = [
                _affine_morphism_from_pullback(product, factor, factor_map)
                for factor, factor_map in zip(scheme_values, factor_maps, strict=True)
            ]
    elif all(
        scheme in Schemes(base).Affine() or scheme in ProjectiveSpaces(base)
        for scheme in scheme_values
    ):
        return _mixed_affine_projective_product(factors, base)
    else:
        raise NotImplementedError(
            "the represented product currently supports affine schemes, projective spaces, "
            "and arbitrary finite mixtures of those regimes"
        )

    return _install_scheme_product_data(product, factors, projections)


class FiberProductSchemes(OwnedCategoryOverBaseRing):
    r"""Schemes equipped as selected pullbacks of one represented cospan."""

    def an_object(self):
        r"""``A^1 \times_{Spec R} A^1``, the affine plane as a fiber product."""
        line = AffineSpaces(self.base_ring())(1)
        return _scheme_fiber_product(line.structure_morphism(), line.structure_morphism())

    def super_categories(self):
        return [Schemes(self.base_ring())]

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
            r"""Return the represented factorization of a cone through this pullback."""
            if left_map.domain() is not right_map.domain():
                raise ValueError("a pullback cone requires one common source")
            left_projection, right_projection = self.fiber_product_projections()
            if left_map.codomain() is not left_projection.codomain():
                raise ValueError("the left pullback-cone map has the wrong codomain")
            if right_map.codomain() is not right_projection.codomain():
                raise ValueError("the right pullback-cone map has the wrong codomain")

            scheme_factorization = getattr(
                self,
                "_preamble_fiber_product_scheme_factorization",
                None,
            )
            if scheme_factorization is not None:
                factorization = scheme_factorization(left_map, right_map)
            else:
                left_pullback = left_map.coordinate_algebra_morphism()
                right_pullback = right_map.coordinate_algebra_morphism()
                selected_factorization = getattr(
                    self,
                    "_preamble_fiber_product_cocone_factorization",
                    None,
                )
                if selected_factorization is None:
                    algebra_pushout = self._preamble_fiber_product_algebra_pushout
                    induced = algebra_pushout.from_pushout_cocone(
                        left_pullback,
                        right_pullback,
                    )
                else:
                    induced = selected_factorization(left_pullback, right_pullback)
                factorization = _affine_morphism_from_pullback(
                    left_map.domain(),
                    self,
                    induced,
                )

            factorization._preamble_fiber_product_cone_target = self
            factorization._preamble_fiber_product_cone_legs = (
                left_map,
                right_map,
            )
            return factorization


def _quotient_base_change_pushout(left_pullback, right_pullback):
    r"""Realize ``A tensor_T T/I`` as ``A/IA`` in the represented quotient regime.

    This is the affine algebra backend for base change along a represented
    quotient of the scalar ring.  It is used only when the general algebra
    pushout cannot own the span because ``T/I`` has no selected algebra
    framing.  The quotient presentation supplies the pushout object, its two
    canonical maps, and the universal cocone factorization.
    """

    base = left_pullback.domain()
    if right_pullback.domain() is not base:
        raise ValueError("a quotient base-change span requires one scalar source")

    def realize(other_pullback, quotient_pullback, *, quotient_on_right):
        other = other_pullback.codomain()
        quotient = quotient_pullback.codomain()
        if quotient not in QuotientRings():
            return None
        if quotient.quotient_source() is not base:
            return None

        if other not in AlgebrasWithChosenFinitePresentation(base):
            return None
        equations = tuple(other_pullback(generator) for generator in quotient.defining_ideal().ideal_generators())
        try:
            pushout, other_to_pushout = other._quotient_by_algebra_elements(equations)
        except NotImplementedError:
            return None

        engine_quotient_to_pushout = _engine_ring(pushout).coerce_map_from(_engine_ring(quotient))
        if engine_quotient_to_pushout is None:
            return None
        quotient_to_pushout = quotient.Mor(pushout)(engine_quotient_to_pushout)

        if quotient_on_right:
            left_to_pushout = other_to_pushout
            right_to_pushout = quotient_to_pushout
        else:
            left_to_pushout = quotient_to_pushout
            right_to_pushout = other_to_pushout

        def factor(left_to_target, right_to_target):
            if left_to_target.codomain() is not right_to_target.codomain():
                raise ValueError("a pushout cocone requires one common codomain")
            if left_to_target.domain() is not left_pullback.codomain() or right_to_target.domain() is not right_pullback.codomain():
                raise ValueError("the pushout cocone maps have the wrong domains")

            other_to_target = left_to_target if quotient_on_right else right_to_target
            target = other_to_target.codomain()
            labels = pushout.algebra_generating_set()
            return pushout.Mor(target)({label: other_to_target(other.algebra_generator(label)) for label in labels})

        return pushout, left_to_pushout, right_to_pushout, factor

    represented = realize(left_pullback, right_pullback, quotient_on_right=True)
    if represented is not None:
        return represented
    return realize(right_pullback, left_pullback, quotient_on_right=False)


def _projective_base_change_factorization(changed, projective_map):
    r"""Raise a map to ``P^n_R`` from an ``R'``-scheme to ``P^n_{R'}``.

    This is the scheme-side factorization in the scalar-base-change pullback.
    On an affine/projective represented source, Sage's maintained polynomial
    scheme-morphism implementation transports the already-selected coordinate
    functions.  On a finite glued source, the same operation is applied on each
    affine chart and then descended through the glued-scheme Hom owner.
    """
    source = projective_map.domain()
    if hasattr(source, "gluing_datum"):
        datum = source.gluing_datum()
        return source.Mor(changed)(
            indexed_family(
                datum.chart_index_set(),
                lambda index: _projective_base_change_factorization(
                    changed,
                    projective_map * datum.chart_embedding(index),
                ),
                name="Local projective base-change factorizations",
            )
        )

    native = projective_map.native_morphism()
    defining_polynomials = getattr(native, "defining_polynomials", None)
    if defining_polynomials is None:
        raise NotImplementedError(
            "projective base-change factorization requires a represented polynomial map "
            "or a finite affine gluing of such maps"
        )
    lifted_native = _native_scheme_homset(source, changed)(
        list(defining_polynomials()),
        check=False,
    )
    return _categorical_scheme_morphism(
        lifted_native,
        domain=source,
        codomain=changed,
    )


def _projective_space_scalar_base_change(left_map, right_map):
    r"""Realize the pullback of ``P^n_R`` along ``Spec R' -> Spec R``.

    Return ``None`` when the cospan is not this specialization.  The result is
    the ordinary owned projective-space constructor over ``R'`` together with
    its actual projection to ``P^n_R``, its structure map to ``Spec R'``, and a
    represented cone factorization.
    """
    base_scheme = left_map.codomain()
    if right_map.codomain() is not base_scheme:
        return None

    candidates = (
        (left_map, right_map, True),
        (right_map, left_map, False),
    )
    for projective_leg, scalar_leg, projective_on_left in candidates:
        projective = projective_leg.domain()
        scalar_scheme = scalar_leg.domain()
        source_base = projective.scheme_base_ring()
        if projective not in ProjectiveSpaces(source_base):
            continue
        if base_scheme is not projective.base_scheme():
            continue
        target_base = scalar_scheme.scheme_base_ring()
        if scalar_scheme is not scalar_scheme.base_scheme():
            continue

        changed = _fresh_projective_space_from_owned_data(
            target_base,
            int(projective.relative_dimension()),
            _normalized_space_names(projective.variable_names()),
        )
        engine_coordinates = tuple(changed.coordinate_ring().gens())
        projection_native = _native_scheme_homset(changed, projective)(
            list(engine_coordinates),
            check=False,
        )
        projective_projection = _categorical_scheme_morphism(
            projection_native,
            domain=changed,
            codomain=projective,
        )
        scalar_projection = changed.structure_morphism()
        if scalar_projection.codomain() is not scalar_scheme:
            raise ArithmeticError(
                "the projective base change has the wrong scalar projection codomain"
            )

        projections = (
            (projective_projection, scalar_projection)
            if projective_on_left
            else (scalar_projection, projective_projection)
        )
        for index, projection in enumerate(projections):
            projection._preamble_fiber_projection_index = index
        changed._preamble_fiber_product_cospan = (left_map, right_map)
        changed._preamble_fiber_product_projections = projections

        def factor(left_cone_map, right_cone_map):
            projective_cone_map = (
                left_cone_map if projective_on_left else right_cone_map
            )
            scalar_cone_map = (
                right_cone_map if projective_on_left else left_cone_map
            )
            apex = projective_cone_map.domain()
            if apex not in Schemes(target_base):
                raise NotImplementedError(
                    "the represented projective base-change factorization requires "
                    "the cone apex to carry its R'-scheme structure"
                )
            if scalar_cone_map != apex.structure_morphism():
                raise NotImplementedError(
                    "the represented projective base-change factorization currently "
                    "uses the apex's selected R'-structure morphism"
                )
            return _projective_base_change_factorization(
                changed,
                projective_cone_map,
            )

        changed._preamble_fiber_product_scheme_factorization = factor
        return _refine_scheme(
            changed,
            target_base,
            [FiberProductSchemes(target_base)],
        )
    return None


def _scheme_fiber_product(left_map, right_map):
    r"""Return ``X x_S Y`` in the represented affine and scalar-projective regimes."""
    if not isinstance(left_map, SchemeMorphism) or not isinstance(right_map, SchemeMorphism):
        raise TypeError("a represented scheme fiber product is specified by scheme morphisms")
    if left_map.codomain() is not right_map.codomain():
        raise ValueError("fiber-product maps require one common codomain")

    projective_base_change = _projective_space_scalar_base_change(
        left_map,
        right_map,
    )
    if projective_base_change is not None:
        return projective_base_change

    left = left_map.domain()
    right = right_map.domain()
    base_scheme = left_map.codomain()
    base_ring = left.scheme_base_ring()
    affine = Schemes(base_ring).Affine()
    if left not in affine or right not in affine or base_scheme not in affine:
        raise NotImplementedError("the active scheme fiber-product backend currently requires affine schemes")

    left_pullback = left_map.coordinate_algebra_morphism()
    right_pullback = right_map.coordinate_algebra_morphism()
    cocone_factorization = None
    if base_scheme is left.base_scheme():
        # Spec R is terminal in Sch/R, so both legs are the structure
        # morphisms and the span sits under R, the initial object of CAlg_R.
        # A colimit under the initial object is the colimit of the discrete
        # diagram, so X x_{Spec R} Y = Spec(A tensor_R B) and the induced map
        # out of it is the coproduct's own factorization.
        algebra_pushout = Algebras(base_ring).Associative().Unital().Commutative().coproduct(
            (left.coordinate_algebra(), right.coordinate_algebra())
        )
        left_pushout_map, right_pushout_map = algebra_pushout.coproduct_injections()
        cocone_factorization = algebra_pushout.from_cocone
    else:
        try:
            algebra_pushout = Algebras(base_ring).Associative().Unital().Commutative().pushout(
                left_pullback,
                right_pullback,
            )
            left_pushout_map = algebra_pushout.left_pushout_map()
            right_pushout_map = algebra_pushout.right_pushout_map()
        except NotImplementedError:
            quotient_base_change = _quotient_base_change_pushout(
                left_pullback,
                right_pullback,
            )
            if quotient_base_change is None:
                raise
            (
                algebra_pushout,
                left_pushout_map,
                right_pushout_map,
                cocone_factorization,
            ) = quotient_base_change
    product = _fresh_affine_spectrum(
        algebra_pushout,
        base_ring,
        extra_categories=(FiberProductSchemes(base_ring),),
    )
    left_projection = _affine_morphism_from_pullback(
        product,
        left,
        left_pushout_map,
    )
    right_projection = _affine_morphism_from_pullback(
        product,
        right,
        right_pushout_map,
    )
    product._preamble_fiber_product_cospan = (left_map, right_map)
    product._preamble_fiber_product_algebra_pushout = algebra_pushout
    if cocone_factorization is not None:
        product._preamble_fiber_product_cocone_factorization = cocone_factorization
    product._preamble_fiber_product_projections = (
        left_projection,
        right_projection,
    )
    left_projection._preamble_fiber_projection_index = 0
    right_projection._preamble_fiber_projection_index = 1
    return product


class _SchemeSubobjectsOf(OwnedParameterizedCategory):
    r"""Subobjects of one scheme, by the kind of immersion they carry."""

    def base_object(self):
        r"""Return the scheme these subobjects are subobjects of."""
        return self.base()

    def _repr_object_names(self) -> str:
        return f"{self.immersion_name} into {self.base_object()}"

    def super_categories(self):
        base_object = self.base_object()
        return [Schemes(base_object.scheme_base_ring()).SubobjectCategory(base_object)]

    class ParentMethods:
        def inclusion(self):
            r"""Return the chosen monomorphism representing this subobject.

            A subobject of ``X`` is the pair ``(Z, i: Z -> X)``, so the scheme
            it sits inside is ``i.codomain()`` and is never separate data.
            """
            return self._preamble_inclusion


def _distinguished_overlap_transition(
    left_chart,
    left_element,
    right_chart,
    right_element,
):
    r"""The isomorphism ``D_i(f_j) -> D_j(f_i)`` of the two presentations of ``D(f_i f_j)``.

    For ``left_chart = D(f_i)`` and ``right_chart = D(f_j)`` inside one affine
    scheme, the overlap is the locus where both elements are units.  It is
    presented once over each chart, and the two presentations are compared by
    the universal property alone: a map into ``D(f_j)`` is a map into ``X``
    inverting ``f_j``, and a map into a distinguished open of ``D(f_j)`` is
    that map inverting ``f_i`` as well, so each direction is the corestriction
    of one overlap's inclusion through the other chart and then through the
    other overlap.
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
    \(A\twoheadrightarrow A/I\).  Every closed subscheme of \(X\) arises this
    way from a unique ideal \(I\), so no further subclass exists to name; a
    chosen finite generating set of \(I\) presents the coordinate algebra and
    is stated on that algebra.
    """

    immersion_name = "closed embeddings"

    def an_object(self):
        r"""The coordinate axis, cut out by the first coordinate of ``X``."""
        base_object = self.base_object()
        first = next(iter(base_object.coordinate_algebra().algebra_generators()))
        return base_object.closed_subscheme(first)

    class ParentMethods:
        def _recorded_defining_equations(self):
            r"""The equations this subobject was cut out by, or ``None``.

            A closed subobject built from equations records them; one reached
            through the backend's own subscheme constructor does not, and
            reads its equations back off that instead.  The datum is stamped
            at construction because the scheme layer installs owned methods
            onto Sage scheme parents and there is no owned class to declare a
            field on; this is the one place that reads it.
            """
            return getattr(self, "_preamble_defining_equations", None)

        def codimension(self):
            codomain = self.inclusion().codomain()
            if self._recorded_defining_equations() is not None and codomain in Schemes(codomain.scheme_base_ring()).Affine():
                codomain_engine = _engine_ring(codomain.coordinate_algebra())
                ideal_engine = self.defining_ideal_owned()._engine_ideal()
                try:
                    quotient_dimension = ideal_engine.dimension()
                    codomain_dimension = codomain_engine.krull_dimension()
                except (AttributeError, NotImplementedError):
                    pass
                else:
                    return int(codomain_dimension - quotient_dimension)
            return codomain.dimension() - self.dimension()

        def defining_equations(self):
            r"""Return the family of equations that cut this subscheme out."""

            selected = self._recorded_defining_equations()
            if selected is not None:
                return finite_family(selected, name="Defining equations")
            return finite_family(self.defining_polynomials(), name="Defining equations")

        def homogeneous_defining_equations(self, coordinate_ring):
            r"""Raise projective defining equations into a selected owned coordinate algebra."""
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            if codomain not in ProjectiveSpaces(base):
                raise TypeError("homogeneous defining equations require a projective-space ambient")
            if coordinate_ring.base_ring() is not base:
                raise ValueError("homogeneous coordinates and the projective ambient must share a scalar base")
            engine_target = _engine_ring(coordinate_ring)
            target_variables = tuple(engine_target.gens())
            raised = []
            for equation in self.defining_equations():
                parent = getattr(equation, "parent", lambda: None)()
                try:
                    backend = _engine_element(parent, equation)
                except (AttributeError, TypeError, ValueError):
                    backend = equation
                copied = _copy_polynomial_by_exponents(
                    backend,
                    engine_target,
                    target_variables,
                )
                raised.append(coordinate_ring._from_engine_element(copied))
            return finite_family(
                tuple(raised),
                name=f"Homogeneous defining equations of {self}",
            )

        @cached_method
        def defining_ideal_owned(self):
            r"""Return ``I <= O(X)``, generated by the equations cutting this out.

            The ideal is derived from the equations when it is asked for, not
            stored beside them.  A closed subobject of ``Spec A`` is
            ``Spec(A/I)`` presented by those equations, and the owned ideal
            additionally carries a module presentation of ``I``; computing that
            presentation is a separate question, and asking it at construction
            makes the subobject unbuildable wherever the presentation has no
            backend.
            """
            equations = self._recorded_defining_equations()
            if equations is None:
                return self.defining_ideal()
            return self.inclusion().codomain().coordinate_ring().ideal(*equations)

        def is_empty(self) -> bool:
            r"""Return whether this represented closed subscheme is empty."""
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            if codomain in Schemes(base).Affine():
                return self.defining_ideal_owned().contains_ambient_element(
                    codomain.coordinate_algebra().one()
                )
            if codomain in Schemes(base).Projective():
                # Sage's projective dimension is ``-1`` exactly for the empty
                # Proj; this is the maintained projective-ideal computation.
                return int(self.dimension()) < 0
            raise NotImplementedError(
                "emptiness of this represented closed subscheme has no selected computation"
            )

        def corestriction(self, morphism):
            r"""The factorization ``T -> Z`` of a morphism ``T -> X`` landing in ``Z``.

            In the affine case the factor is induced by the quotient coordinate
            algebra.  For a projective-coordinate morphism into projective
            space, the retained homogeneous coordinates factor through ``Z``
            exactly when every homogeneous defining equation vanishes after
            substitution.  The factor retains those same coordinates, now in
            ``Mor(T,Z)``.
            """
            assert morphism.codomain() is self.inclusion().codomain(), "a corestriction is taken of a morphism into the codomain of the inclusion"
            source = morphism.domain()
            base = source.scheme_base_ring()
            codomain = morphism.codomain()
            if source in Schemes(base).Affine() and self in Schemes(base).Affine():
                pullback = morphism.coordinate_algebra_morphism()
                for equation in self.defining_equations():
                    assert pullback(equation) == source.coordinate_algebra().zero(), f"{morphism} does not factor through {self}: its pullback does not kill {equation}"
                quotient_map = self.inclusion().coordinate_algebra_morphism()
                algebra = self.coordinate_algebra()
                factor_pullback = algebra.Mor(source.coordinate_algebra())(
                    {label: pullback(codomain.coordinate_algebra().algebra_generator(label)) for label in algebra.algebra_generating_set()}
                )
                factor = _affine_morphism_from_pullback(source, self, factor_pullback)
                assert self.inclusion() * factor == morphism, "the corestriction does not recover the morphism through the inclusion"
                assert quotient_map.domain() is codomain.coordinate_algebra()
                return factor
            if codomain in ProjectiveSpaces(base) and isinstance(
                morphism, _ProjectiveCoordinateMorphism
            ):
                coordinates = tuple(morphism.homogeneous_coordinates())
                target_ring = codomain.O(1).global_sections().homogeneous_coordinate_ring()
                for equation in self.homogeneous_defining_equations(target_ring):
                    value = _evaluate_owned_homogeneous_polynomial_on_coordinates(
                        equation,
                        target_ring,
                        coordinates,
                    )
                    if value != value.parent().zero():
                        raise ValueError(
                            f"{morphism} does not factor through {self}: a homogeneous defining equation does not vanish"
                        )
                factor = _ProjectiveCoordinateMorphism(
                    source.Mor(self),
                    coordinates,
                )
                factor._preamble_projective_corestriction_ambient_morphism = morphism
                factor._preamble_projective_corestriction_closed_subscheme = self
                return factor
            raise NotImplementedError(
                "the represented closed corestriction currently supports affine maps or retained projective-coordinate maps into projective space"
            )

        def intersection(self, other):
            r"""``Z cap W = V(I + J)``, the scheme-theoretic intersection in ``X``.

            The intersection of two closed subschemes of ``X`` is the closed
            subscheme whose ideal is the sum of the two ideals, and that is
            the fibre product ``Z x_X W`` (Stacks, Tag 0C4H): a morphism into
            ``X`` factors through it exactly when its pullback kills both
            ideals, which is exactly factoring through each of ``Z`` and
            ``W``.  Each factorization is the corestriction of this
            subscheme's inclusion along the corresponding one.
            """
            codomain = self.inclusion().codomain()
            assert other.inclusion().codomain() is codomain, "a scheme-theoretic intersection is taken inside one scheme"
            return codomain.closed_subscheme((*self.defining_equations(), *other.defining_equations()))

        @cached_method
        def O(self, degree):
            r"""Return ``O_X(d)=i^*O_P(d)`` for a projective closed subscheme."""
            ambient = self.inclusion().codomain()
            base = self.scheme_base_ring()
            if ambient not in ProjectiveSpaces(base):
                raise TypeError("O_X(d) here requires a projective-space ambient")
            return ambient.O(degree).restrict_to(self)

        def fundamental_cycle(self):
            r"""Return this closed subscheme's cycle with generic local multiplicities."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _fundamental_cycle,
            )

            return _fundamental_cycle(self)

        def proper_pushforward_cycle(self, cycle):
            r"""Push ``cycle`` to the ambient scheme along this closed immersion."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _closed_immersion_cycle_pushforward,
            )

            return _closed_immersion_cycle_pushforward(self, cycle)

        def serre_intersection(self, other, point):
            r"""Return the supported local Tor intersection with ``other`` at ``point``."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _serre_intersection,
            )

            return _serre_intersection(self, other, point)

        def serre_intersection_multiplicity(self, other, point):
            r"""Return Serre's alternating Tor-length intersection multiplicity."""
            return self.serre_intersection(other, point).multiplicity()

        def intersection_multiplicity(self, other, point):
            r"""``i(p; Z . W)``, the multiplicity of the intersection at ``p``.

            For two effective hypersurfaces meeting properly in a smooth
            affine surface over a field, this is

            ``length_{O_{X,p}} O_{X,p}/(f,g)``.

            The private polynomial backend computes a primary decomposition of
            ``(f,g)``.  The component whose radical is the maximal ideal of
            ``p`` is exactly the local Artinian factor.  If ``Q_p`` is that
            component, then

            ``dim_k(P/Q_p) = length(P_p/Q_p P_p) * [kappa(p):k]``;

            dividing by the residue degree therefore returns the composition
            length even at a non-rational closed point.  These hypotheses are
            stated explicitly: outside the proper hypersurface case the
            intersection product is Serre's alternating Tor length and is not
            replaced by this simpler colength formula.
            """
            ambient = self.inclusion().codomain()
            assert other.inclusion().codomain() is ambient, "an intersection multiplicity is taken inside one ambient scheme"
            base = ambient.scheme_base_ring()
            assert base in OwnedFields(), "the represented colength formula requires an affine surface over a field"
            assert ambient in AffineSpaces(base) and int(ambient.relative_dimension()) == 2, "the represented intersection multiplicity requires a smooth affine surface"
            assert self.codimension() == other.codimension() == 1, "the represented local colength formula requires two hypersurfaces"
            assert len(tuple(self.defining_equations())) == 1 and len(tuple(other.defining_equations())) == 1, "each represented hypersurface must have one defining equation"

            spectrum = ambient.underlying_space()
            if point.parent() is not spectrum:
                point = spectrum(point)
            point_ideal = point.ideal()
            assert point_ideal.is_maximal(), "intersection multiplicity here is represented at a closed point"

            meeting_ideal = self.intersection(other).defining_ideal_owned()
            backend_meeting = meeting_ideal._engine_ideal()
            backend_point = point_ideal._engine_ideal()
            components = tuple(backend_meeting.primary_decomposition())
            local_components = tuple(component for component in components if component.radical() == backend_point)
            if not local_components:
                return _own_ring(SageZZ).zero()
            if len(local_components) != 1:
                raise ArithmeticError("a zero-dimensional primary decomposition has more than one component at the selected point")
            component = local_components[0]
            if int(component.dimension()) != 0:
                raise ValueError("the two hypersurfaces do not meet properly at the selected point")

            colength = SageZZ(component.vector_space_dimension())
            residue_degree = SageZZ(backend_point.vector_space_dimension())
            if residue_degree <= 0 or colength % residue_degree != 0:
                raise ArithmeticError("the local primary colength is incompatible with the selected residue field")
            return _own_ring(SageZZ)(colength // residue_degree)

        def ideal_sheaf(self):
            r"""``I_Z = I~``, the quasi-coherent ideal sheaf of ``Z = V(I)`` on affine ``X``."""
            codomain = self.inclusion().codomain()
            assert codomain in Schemes(codomain.scheme_base_ring()).Affine(), "the ideal sheaf is represented on an affine scheme"
            return codomain.associated_module_sheaf(self.defining_ideal_owned())

        def open_complement(self):
            r"""``X \ Z``, the open subscheme on which the ideal of ``Z`` is the unit ideal.

            A prime of ``X = Spec A`` lies outside ``Z = V(I)`` exactly when
            it fails to contain some ``f in I``, so the complement is
            ``D(I) = union_{f in I} D(f)``, and the ``D(f)`` for ``f`` running
            over a generating family of ``I`` already cover it.  The equations
            that cut ``Z`` out are such a family, so they are the atlas: the
            chart at ``f_i`` is ``D(f_i) = Spec A[1/f_i]``, glued to the chart
            at ``f_j`` along ``D(f_i) cap D(f_j) = D(f_i f_j)``.

            A single equation is its own union, and ``D(f)`` is affine.  The
            complement of the origin in the affine line is ``G_m``, and the
            complement of the origin in the plane is the punctured plane, which
            is the standard quasi-affine scheme that is not affine.

            The immersion into ``X`` is the map out of the glued scheme given
            chartwise by the inclusions of the ``D(f_i)``, which agree on the
            overlaps because each is an open of ``X`` to begin with.
            """
            codomain = self.inclusion().codomain()
            base = codomain.scheme_base_ring()
            if codomain in Schemes(base).Projective():
                native = _SageAlgebraicSchemeSubscheme.complement(self, codomain)
                opened = _refine_scheme(
                    native,
                    base,
                    [OpenImmersions(codomain), Schemes(base).QuasiProjective()],
                )
                opened._preamble_inclusion = _OpenComplementInclusion(
                    opened.Mor(codomain),
                    self,
                )
                opened._preamble_open_complement_closed_subscheme = self
                return opened
            if codomain not in Schemes(base).Affine():
                raise NotImplementedError(
                    "the represented open complement requires an affine or projective ambient scheme"
                )
            equations = self.defining_equations()
            indices = equations.index_set()
            charts = {index: codomain.distinguished_open(equations[index]) for index in indices}
            if equations.cardinality() == 1:
                return charts[next(iter(indices))]
            glued = Schemes(base).glue_affine_atlas(
                charts,
                {
                    (left, right): _distinguished_overlap_transition(
                        charts[left],
                        equations[left],
                        charts[right],
                        equations[right],
                    )
                    for left, right in combinations(tuple(indices), 2)
                },
            )
            glued._preamble_inclusion = glued.Mor(codomain)({index: chart.inclusion() for index, chart in charts.items()})
            return _refine_scheme(glued, base, [OpenImmersions(codomain)])


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Closed subschemes of schemes over ``R``: a scheme with its closed immersion.

    An object is a scheme ``Z`` together with the chosen closed immersion
    ``Z -> X``.  ``ClosedEmbeddings(X)`` is the fibre of this category over
    one scheme ``X``, where the subobject order and the ideal-sheaf data
    live; this category collects those fibres over all ``R``-schemes so that
    "is a closed subscheme" is a placement a session can ask without naming
    the codomain of the immersion.
    """

    def an_object(self):
        r"""The origin of the affine line."""
        line = AffineSpaces(self.base_ring())(1)
        first = next(iter(line.coordinate_algebra().algebra_generators()))
        return line.closed_subscheme(first)

    def _repr_object_names(self):
        return f"closed subschemes of schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return candidate in Schemes(self.base_ring()) and _has_scheme_placement(candidate, ClosedEmbeddings)


class OpenImmersions(_SchemeSubobjectsOf):
    r"""Subobjects of ``X`` whose inclusion is an open immersion.

    The standard affine specimen is the distinguished open
    \(D(f)=\operatorname{Spec}A[1/f]\subseteq\operatorname{Spec}A\), whose
    inclusion is induced by the localization map \(A\to A[1/f]\).
    """

    immersion_name = "open immersions"

    def an_object(self):
        r"""\(D(f)\) for ``f`` the first coordinate of ``X``."""
        base_object = self.base_object()
        first = next(iter(base_object.coordinate_algebra().algebra_generators()))
        return base_object.distinguished_open(first)

    class ParentMethods:
        def is_distinguished_open(self):
            return getattr(self, "_preamble_distinguished_open_ambient", None) is self.inclusion().codomain()

        def distinguished_open_element(self):
            if not self.is_distinguished_open():
                raise ValueError("this open immersion is not represented by one distinguished element")
            return self._preamble_distinguished_open_element

        def corestriction(self, morphism):
            r"""The factorization ``T -> D(f)`` of a morphism ``T -> X`` landing in ``D(f)``.

            A morphism ``g: T -> X`` factors through the open ``D(f)`` exactly
            when ``g^#(f)`` is a unit on ``T``, and the factor is unique: the
            universal property of ``O(D(f)) = A[1/f]`` sends ``a/f^k`` to
            ``g^#(a) g^#(f)^{-k}``, which is the only map compatible with the
            localization (Stacks, Tag 01HR).  This is the open-immersion
            counterpart of the closed-immersion corestriction, and it is the
            same statement: a subobject absorbs the morphisms that land in it.
            """
            codomain = self.inclusion().codomain()
            assert morphism.codomain() is codomain, "a corestriction is taken of a morphism into the codomain of the inclusion"
            assert self.is_distinguished_open(), "the represented open corestriction requires a distinguished open"
            source = morphism.domain()
            assert source in Schemes(source.scheme_base_ring()).Affine(), "the represented open corestriction currently requires an affine source"
            source_algebra = source.coordinate_algebra()
            open_algebra = self.coordinate_algebra()
            pullback = morphism.coordinate_algebra_morphism()
            defining_element = codomain.coordinate_algebra()(self.distinguished_open_element())
            if not source_algebra(pullback(defining_element)).is_unit():
                raise ValueError(
                    "the morphism does not land in this distinguished open: it does not send the defining element to a unit"
                )

            inclusion_pullback = self.inclusion().coordinate_algebra_morphism()
            factorizer = getattr(inclusion_pullback, "induced_morphism", None)
            factor_pullback = (
                factorizer(pullback)
                if callable(factorizer)
                else open_algebra.induced_morphism(pullback)
            )
            factor = _scheme_mor_category(source, self)(factor_pullback)
            assert self.inclusion() * factor == morphism, "the corestriction does not recover the morphism through the inclusion"
            return factor

        def flat_pullback_cycle(self, cycle):
            r"""Pull ``cycle`` back along this flat open immersion."""
            from dzack_research.preamble.categories.divisors.chow_groups import (
                _distinguished_open_cycle_pullback,
            )

            return _distinguished_open_cycle_pullback(self, cycle)

        def inclusion_into(self, larger_open):
            r"""The open immersion ``D(g) -> D(f)`` when ``D(g) <= D(f)`` in one affine scheme.

            Its pullback is the restriction ``O(D(f)) -> O(D(g))`` of the
            structure sheaf, which exists exactly when ``f`` is a unit on
            ``D(g)``; composed with the inclusion of ``D(f)`` it is the
            inclusion of ``D(g)``.
            """
            codomain = self.inclusion().codomain()
            assert larger_open.inclusion().codomain() is codomain, "an inclusion between distinguished opens is taken in one affine scheme"
            restriction = codomain.structure_sheaf().restriction_map(larger_open, self)
            inclusion = _affine_morphism_from_pullback(self, larger_open, restriction)
            assert larger_open.inclusion() * inclusion == self.inclusion(), "the inclusion between distinguished opens does not compose to the inclusion into the scheme"
            return inclusion


class SchemeMonomorphisms(_MonoCategoryOf):
    r"""Monomorphisms of schemes.

    A closed immersion and an open immersion are monomorphisms.  Which of the
    two an inclusion is, is declared where it is constructed, and this reads
    that declaration.  Injectivity on points is neither necessary nor
    sufficient for a scheme monomorphism, so the inherited test does not apply.
    """

    def accepts(self, arrow) -> bool:
        codomain = arrow.codomain()
        source = arrow.domain()
        if source in ClosedEmbeddings(codomain) or source in OpenImmersions(codomain):
            return True
        open_image = arrow.__dict__.get("_preamble_open_image")
        open_image_isomorphism = arrow.__dict__.get("_preamble_open_image_isomorphism")
        if open_image is None or open_image_isomorphism is None:
            return False
        return open_image in OpenImmersions(codomain) and open_image_isomorphism.forward().domain() is source and open_image_isomorphism.forward().codomain() is open_image


def _refine_closed_subscheme(
    subscheme,
    codomain=None,
    *,
    defining_equations=None,
):
    codomain = subscheme.ambient_space() if codomain is None else codomain
    base = codomain.scheme_base_ring()
    if defining_equations is not None:
        subscheme._preamble_defining_equations = tuple(defining_equations)
    native_inclusion = (
        subscheme.embedding_morphism()
        if getattr(subscheme, "_preamble_inclusion", None) is None
        else None
    )
    if subscheme not in Schemes(base):
        # The inclusion is an arrow in ``Sch/base``.  Establish that endpoint
        # before asking the owned scheme Hom to construct the arrow.  Capture
        # Sage's native embedding first: refining the endpoint changes its Hom
        # category, but not the underlying closed immersion being retained.
        _refine_scheme(subscheme, base)
    if getattr(subscheme, "_preamble_inclusion", None) is None:
        # The subobject is the arrow, so a route that did not build one takes
        # the native embedding, retargeted at the stated codomain.
        subscheme._preamble_inclusion = _categorical_scheme_morphism(
            native_inclusion,
            domain=subscheme,
            codomain=codomain,
        )
    return _refine_scheme(
        subscheme,
        base,
        [ClosedEmbeddings(codomain), ClosedSubschemes(base)],
    )


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
