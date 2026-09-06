"""Owned categories and basic constructors for schemes over a base ring."""

from itertools import combinations
from typing import Any, cast

from sage.categories.category import Category
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
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
from sage.structure.category_object import CategoryObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CosliceUnder,
    Isomorphism,
    SliceOver,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    MonoCategoryOf,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.rings.commutative_algebra import (
    QuotientRings,
    refine_commutative_algebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
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
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.categories.abstract_categories.constructions import (
    Coproduct,
    Pushout,
    Subobjects,
)
from dzack_research.preamble.categories.abstract_categories.products import _finite_factor_family
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    FramedAlgebras,
    _engine_algebra_morphism,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    ring_homset,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family


_SCHEME_MORPHISM_WRAPPERS = {}
_AFFINE_SPECTRA = {}


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
            if (domain is None) != (codomain is None):
                raise ValueError(
                    "an owned scheme-morphism endpoint override requires both endpoints"
                )
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
        if self._is_the_structure_morphism():
            structure = other.domain().structure_morphism()
            if structure.codomain() is self.codomain():
                return structure
        # The composite is a morphism between the stated endpoints, whichever
        # engine route computes it.  Reading the endpoints off the engine's
        # answer lands it on Spec of a coordinate ring instead.
        homset = _scheme_mor_category(other.domain(), self.codomain())
        left_pullback = self._preamble_coordinate_algebra_morphism
        right_pullback = other._preamble_coordinate_algebra_morphism
        if left_pullback is not None and right_pullback is not None:
            composite_pullback = ring_homset(
                left_pullback.domain(),
                right_pullback.codomain(),
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
                if stored_points is not None:
                    for index, factor in enumerate(factors):
                        if factor is self.codomain():
                            return categorical_scheme_morphism(
                                stored_points[index],
                                domain=point.domain(),
                                codomain=factor,
                            )
        return self.compose(point)

    def coordinate_algebra_morphism(self):
        morphism = self._preamble_coordinate_algebra_morphism
        if morphism is None:
            raise NotImplementedError(
                "this scheme morphism has no represented pullback on affine coordinate algebras"
            )
        return morphism

    pullback_on_coordinate_algebras = coordinate_algebra_morphism

    @cached_method
    def graph_morphism(self):
        r"""``Gamma_f = (id, f): X -> X x_S Y``."""
        identity = self.domain().categorical_identity_morphism()
        return scheme_product(self.domain(), self.codomain()).from_product_cone(
            (identity, self)
        )

    @cached_method
    def graph_subscheme(self):
        r"""The closed subscheme ``Gamma_f <= X x_S Y`` cut out by ``1 tensor b - f^#(b) tensor 1``.

        The graph is the inverse image of the diagonal of ``Y`` under
        ``f x id``, so it is closed whenever ``Y`` is separated; affine ``Y``
        is.  The graph morphism factors through it as an isomorphism.
        """
        base = self.codomain().scheme_base_ring()
        assert self.codomain() in AffineSchemes(base), (
            "the graph is represented as a closed subscheme for affine targets"
        )
        product = scheme_product(self.domain(), self.codomain())
        to_domain = product.projection(0).coordinate_algebra_morphism()
        to_codomain = product.projection(1).coordinate_algebra_morphism()
        pullback = self.coordinate_algebra_morphism()
        algebra = self.codomain().coordinate_algebra()
        equations = tuple(
            to_codomain(algebra.algebra_generator(label))
            - to_domain(pullback(algebra.algebra_generator(label)))
            for label in algebra.algebra_generating_set()
        )
        return product.closed_subscheme(equations)

    def base_change(self, ring_map):
        r"""``f_{R'}: X_{R'} -> Y_{R'}``, the morphism the base-change functor induces.

        The square with the two projections commutes, so an automorphism of
        ``X`` over ``R`` becomes an automorphism of ``X_{R'}`` over ``R'``.
        """
        from dzack_research.preamble.categories.schemes.base_change import (
            scheme_base_change_functor,
        )

        return scheme_base_change_functor(ring_map)(self)

    def inverse_image(self, closed_subscheme):
        r"""``f^{-1}(Z) = X x_Y Z`` as a closed subscheme of ``X``.

        For ``Z = V(I) <= Spec B`` and ``f: Spec A -> Spec B`` this is
        ``V(f^#(I) A)``; the restriction ``f^{-1}(Z) -> Z`` of ``f`` is the
        corestriction of ``f`` composed with the inclusion.
        """
        assert closed_subscheme.inclusion().codomain() is self.codomain(), (
            "the inverse image is taken of a closed subscheme of the codomain"
        )
        base = self.domain().scheme_base_ring()
        assert self.domain() in AffineSchemes(base) and self.codomain() in AffineSchemes(base), (
            "the represented inverse image currently requires affine schemes"
        )
        pullback = self.coordinate_algebra_morphism()
        equations = tuple(
            pullback(equation) for equation in closed_subscheme.defining_equations()
        )
        return self.domain().closed_subscheme(equations)

    def fixed_subscheme(self):
        r"""``X^f = Eq(f, id_X)``, the fixed subscheme of an endomorphism."""
        assert self.domain() is self.codomain(), "a fixed subscheme is that of an endomorphism"
        return Schemes(self.domain().scheme_base_ring()).equalizer(
            self,
            self.domain().categorical_identity_morphism(),
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
        assert source_algebra in FramedAlgebras(source_algebra.base_ring()), (
            "the engine realization requires a chosen algebra generating set on the codomain algebra"
        )
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
        assert self.domain() in AffineSchemes(base) and self.codomain() in AffineSchemes(base), (
            "the represented scheme-theoretic image currently requires affine schemes"
        )
        kernel = self._engine_pullback_with_trivial_base_map().kernel()
        algebra = self.codomain().coordinate_algebra()
        equations = tuple(algebra._from_engine_element(generator) for generator in kernel.gens())
        return self.codomain().closed_subscheme(equations)

    def direct_image(self, sheaf):
        r"""``f_* N~ = (Res_{f^#} N)~`` for affine ``f: Spec B -> Spec A`` (Stacks, Tag 01I8)."""
        assert sheaf.scheme() is self.domain(), "a direct image is taken of a sheaf on the source"
        module = sheaf.module().restrict_scalars(self.coordinate_algebra_morphism())
        return self.codomain().associated_module_sheaf(module)

    def module_pullback(self, sheaf):
        r"""``f^* M~ = (M tensor_A B)~``, scalar extension along ``f^#`` (Stacks, Tag 01I8).

        This is the pullback of quasi-coherent modules, ``O_X tensor f^{-1}
        O_Y f^{-1} M~``; the inverse-image sheaf ``f^{-1} M~`` itself is not
        quasi-coherent and is not represented here.
        """
        assert sheaf.scheme() is self.codomain(), "a module pullback is taken of a sheaf on the target"
        module = sheaf.module().base_change(self.coordinate_algebra_morphism())
        return self.domain().associated_module_sheaf(module)

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
        assert self.domain() in AffineSchemes(base) and self.codomain() in AffineSchemes(base), (
            "closed immersions are currently decided for affine schemes"
        )
        return bool(self._engine_pullback_with_trivial_base_map().is_surjective())

    def __eq__(self, other) -> bool:
        r"""Decide equality from represented pullbacks or the native scheme."""
        if not isinstance(other, SchemeMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        if self is other:
            return True
        left_pullback = self._preamble_coordinate_algebra_morphism
        right_pullback = other._preamble_coordinate_algebra_morphism
        if left_pullback is not None and right_pullback is not None:
            base = _scheme_base_ring(self.codomain())
            if self.codomain() in AffineSchemes(base):
                algebra = self.codomain().coordinate_algebra()
                if algebra in FramedAlgebras(base):
                    labels = algebra.algebra_generating_set()
                    if labels.cardinality().is_finite():
                        return all(
                            left_pullback(algebra.algebra_generator(label))
                            == right_pullback(algebra.algebra_generator(label))
                            for label in labels
                        )
                if algebra in LocalizationRings():
                    source_algebra = algebra.localization_source()
                    if source_algebra in FramedAlgebras(base):
                        labels = source_algebra.algebra_generating_set()
                        if labels.cardinality().is_finite():
                            localization_map = algebra.localization_map()
                            return all(
                                left_pullback(
                                    localization_map(
                                        source_algebra.algebra_generator(label)
                                    )
                                )
                                == right_pullback(
                                    localization_map(
                                        source_algebra.algebra_generator(label)
                                    )
                                )
                                for label in labels
                            )
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


class _RepresentedAffineSchemeMorphism(SchemeMorphism):
    r"""An affine scheme morphism carried exactly by its coordinate pullback."""

    def __init__(self, parent, pullback) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._preamble_coordinate_algebra_morphism = pullback
        self._native_realization = None

    def native_morphism(self):
        if self._native_realization is None:
            self._native_realization = _affine_morphism_from_pullback(
                self.domain(),
                self.codomain(),
                self.coordinate_algebra_morphism(),
            ).native_morphism()
        return self._native_realization

    __hash__ = None


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
        if (
            isinstance(datum, Morphism)
            and self.domain() in AffineSchemes(_scheme_base_ring(self.domain()))
            and self.codomain() in AffineSchemes(_scheme_base_ring(self.domain()))
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


def _has_scheme_placement(scheme, category_class) -> bool:
    return any(
        issubclass(dynamic_category_class, category_class)
        for dynamic_category_class in getattr(
            scheme,
            "_preamble_scheme_category_types",
            (),
        )
    )


def _placed_over_stated_base(candidate, category, placement_class) -> bool:
    r"""Membership in a category stated relative to its base ring.

    Affine spaces, projective spaces and products are constructions over one
    base: ``A^n_Q`` is a ``Z``-scheme but not an affine space over ``Z``.
    """
    return (
        candidate in Schemes(category.base_ring())
        and candidate.scheme_base_ring() is category.base_ring()
        and _has_scheme_placement(candidate, placement_class)
    )


def _native_scheme_homset(domain, codomain):
    r"""Return Sage's private scheme-Hom runtime homset for owned schemes."""
    return _SageScheme._Hom_(domain, codomain)


def refine_scheme_morphism(
    morphism,
    base_ring,
    *,
    domain=None,
    codomain=None,
):
    r"""Return the native morphism in the Hom of its stated owned schemes."""
    base = _own_ring(base_ring)
    if (domain is None) != (codomain is None):
        raise ValueError("scheme-morphism refinement requires both stated endpoints")
    if domain is not None:
        schemes = Schemes(base)
        if domain not in schemes or codomain not in schemes:
            raise TypeError("scheme-morphism endpoints must be schemes over the stated base")
    return categorical_scheme_morphism(
        morphism,
        domain=domain,
        codomain=codomain,
    )


def refine_scheme(scheme, base_ring=None, categories=()):
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
        from dzack_research.preamble.categories.schemes.affine_spec import AffineSpecFunctor
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

        ring = self.base_ring()
        return AffineSpecFunctor(ring)(CommutativeAlgebras(ring).an_object())

    def _repr_object_names(self):
        return f"schemes over {self.base_ring()}"

    def super_categories(self):
        r"""A scheme over ``R`` is a scheme over the scalar base of ``R``.

        Composing ``X -> Spec R`` with ``Spec R -> Spec R_0`` for the structure
        map ``R_0 -> R`` places every ``R``-scheme in ``Sch/R_0``; the same
        tower ``Algebras(R) <= Algebras(R_0)`` sits underneath affine ones.
        """
        base = _proper_restriction_base_ring(self.base_ring())
        if base is None:
            return [LocallyRingedSpaces()]
        return [LocallyRingedSpaces(), Schemes(base)]

    def __contains__(self, candidate) -> bool:
        stated = getattr(candidate, "_preamble_scheme_base_ring", None)
        return (
            stated is not None
            and any(base is self.base_ring() for base in _scheme_base_tower(stated))
            and _has_scheme_placement(candidate, Schemes)
        )

    @cached_method
    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a scheme Hom requires two schemes over the stated base")
        return domain._scheme_homset(self, codomain)

    _MonoCategory = None  # set below, once SchemeMonomorphisms is defined

    class SubcategoryMethods:
        def product(self, factors):
            r"""Return the product of a finite family of objects of this category."""
            return self._fold_construction(
                self._categorical_product, factors, name="Product factors"
            )

        def _categorical_product(self, left, right):
            return scheme_product(left, right)

        def fiber_product(self, left_leg, right_leg):
            r"""Return the fiber product of the cospan these two legs form."""
            assert left_leg.codomain() is right_leg.codomain(), (
                "a cospan has one common codomain"
            )
            return self._categorical_pullback(left_leg, right_leg)

        def _categorical_pullback(self, left_morphism, right_morphism):
            return scheme_fiber_product(left_morphism, right_morphism)

        def equalizer(self, left, right):
            r"""Return the equalizer ``Eq(f, g) -> X`` of two parallel morphisms."""
            assert left.domain() is right.domain() and left.codomain() is right.codomain(), (
                "an equalizer is taken of two parallel morphisms"
            )
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
            assert source in AffineSchemes(base) and target in AffineSchemes(base), (
                "the represented equalizer currently requires affine schemes"
            )
            target_algebra = target.coordinate_algebra()
            assert target_algebra in FramedAlgebras(target_algebra.base_ring()), (
                "the represented equalizer requires a chosen algebra generating set on the target"
            )
            left_pullback = left.coordinate_algebra_morphism()
            right_pullback = right.coordinate_algebra_morphism()
            equations = tuple(
                left_pullback(target_algebra.algebra_generator(label))
                - right_pullback(target_algebra.algebra_generator(label))
                for label in target_algebra.algebra_generating_set()
            )
            equalizer = source.closed_subscheme(equations)
            assert left * equalizer.inclusion() == right * equalizer.inclusion(), (
                "the equalizer inclusion does not equalize the two morphisms"
            )
            return equalizer


    @cached_method
    def base_scheme(self):
        ring = self.base_ring()
        return Spec(ring, base_ring=ring)

    @cached_method
    def slice_category(self):
        return SliceOver(self, self.base_scheme())

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
        return CosliceUnder(self, self.base_scheme())

    def as_coslice_object(self, point):
        r"""Read a morphism ``Spec R -> X`` as a pointed ``R``-scheme."""
        assert point.domain() is self.base_scheme(), (
            "a pointed R-scheme is a morphism out of Spec R"
        )
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

        def base_scheme(self):
            ring = self.scheme_base_ring()
            return Spec(ring, base_ring=ring)

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
            if getattr(
                distinguished_open,
                "_preamble_distinguished_open_ambient",
                None,
            ) is self:
                return distinguished_open.coordinate_algebra()
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
            try:
                morphism = _SageScheme.base_morphism(self)
            except (AttributeError, NotImplementedError):
                scheme_base = self.scheme_base_ring()
                if self not in AffineSchemes(scheme_base):
                    raise
                algebra = self.coordinate_algebra()
                engine_map = _engine_ring(algebra).coerce_map_from(
                    _engine_ring(scheme_base)
                )
                if engine_map is None:
                    raise NotImplementedError(
                        "the affine structure morphism requires the scalar-base injection"
                    ) from None
                morphism = _native_scheme_homset(self, base)(engine_map, check=False)
            if morphism.codomain() is not base:
                raise ArithmeticError(
                    "the native structure morphism does not land in the represented base scheme"
                )
            wrapped = refine_scheme_morphism(
                morphism,
                self.scheme_base_ring(),
                domain=self,
                codomain=base,
            )
            if self in AffineSchemes(self.scheme_base_ring()):
                wrapped._preamble_coordinate_algebra_morphism = (
                    self.coordinate_algebra().algebra_structure_morphism()
                )
            self._preamble_structure_morphism = wrapped
            return wrapped

        def relative_dimension(self):
            if self is self.base_scheme():
                return 0
            return self.dimension_relative()

        def base_change(self, ring_map):
            r"""``X_{R'} = X x_{Spec R} Spec R'`` along a scalar morphism ``R -> R'``.

            The functor is applied to this object; the result is equipped as
            the fibre product of ``X -> Spec R <- Spec R'``, so its two
            projections and the universal factorization are available on it.
            """
            from dzack_research.preamble.categories.schemes.base_change import (
                scheme_base_change_functor,
            )

            assert self in Schemes(_own_ring(ring_map.domain())), (
                "a scheme is base-changed along a morphism out of its own scalar base"
            )
            return scheme_base_change_functor(ring_map)(self)

        def as_slice_object(self):
            return self.scheme_category().as_slice_object(self)

        @cached_method
        def diagonal_morphism(self):
            r"""``Delta: X -> X x_S X``, the cone map with both legs the identity."""
            identity = self.categorical_identity_morphism()
            return scheme_product(self, self).from_product_cone((identity, identity))

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
            assert self in AffineSchemes(base), (
                "the diagonal is represented as a closed subscheme for affine schemes; "
                "for a glued scheme it is closed exactly when the scheme is separated"
            )
            product = scheme_product(self, self)
            left = product.projection(0).coordinate_algebra_morphism()
            right = product.projection(1).coordinate_algebra_morphism()
            algebra = self.coordinate_algebra()
            equations = tuple(
                left(algebra.algebra_generator(label)) - right(algebra.algebra_generator(label))
                for label in algebra.algebra_generating_set()
            )
            return product.closed_subscheme(equations)

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
            wrapped = refine_scheme_morphism(
                point,
                base,
                domain=point_domain,
                codomain=self,
            )
            if self in AffineSchemes(base):
                source_algebra = self.coordinate_algebra()
                target_algebra = point_domain.coordinate_algebra()
                if source_algebra in FramedAlgebras(base):
                    labels = tuple(source_algebra.algebra_generating_set())
                    if len(labels) != len(engine_coordinates):
                        raise ValueError(
                            "an affine point needs one coordinate per algebra generator"
                        )
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
                    wrapped._preamble_coordinate_algebra_morphism = pullback
            return wrapped

        def categorical_identity_morphism(self):
            selected = getattr(self, "_preamble_identity_morphism", None)
            if selected is not None:
                return selected
            return refine_scheme_morphism(
                self.identity_morphism(),
                self.scheme_base_ring(),
                domain=self,
                codomain=self,
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
    r"""A full subcategory of ``Sch/R`` cut out by one property.

    A property is *absolute* when it descends the base tower: an affine,
    integral or normal ``R``-scheme is affine, integral or normal as a scheme
    over every scalar base of ``R``, and separatedness descends because
    ``Spec R -> Spec R_0`` is affine, hence separated, and separated
    morphisms compose.  Finite type, smoothness and (quasi-)projectivity are
    stated relative to the base and are read only over the stated one.
    """

    property_name = "scheme property"
    absolute = False

    def _repr_object_names(self):
        return f"{self.property_name} schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        if not _has_scheme_placement(candidate, type(self).__mro__[1]):
            return False
        if candidate not in Schemes(self.base_ring()):
            return False
        return self.absolute or candidate.scheme_base_ring() is self.base_ring()


class SeparatedSchemes(_SchemePropertyCategory):
    property_name = "separated"
    absolute = True

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
    absolute = True

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
    absolute = True

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
        return AffineSpace(1, base)


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
    absolute = True

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
            quotient_operation = getattr(
                algebra,
                "_quotient_by_algebra_elements",
                None,
            )
            if quotient_operation is None:
                raise NotImplementedError(
                    "a closed affine subscheme requires a represented polynomial "
                    "presentation of its coordinate algebra"
                )
            quotient, quotient_map = quotient_operation(equations)
            subscheme = Spec(quotient, base_ring=self.scheme_base_ring())
            spec_inclusion = affine_spec_morphism(quotient_map)
            inclusion = categorical_scheme_morphism(
                spec_inclusion.native_morphism(),
                domain=subscheme,
                codomain=self,
            )
            inclusion._preamble_coordinate_algebra_morphism = quotient_map
            subscheme._preamble_inclusion = inclusion
            return refine_closed_subscheme(
                subscheme,
                self,
                defining_equations=equations,
            )

        @cached_method
        def relative_differentials(self):
            r"""Return the affine module of relative Kähler differentials."""

            from dzack_research.preamble.categories.algebras.kahler_differentials import (
                KahlerDifferentials,
            )

            return KahlerDifferentials(self.coordinate_algebra())

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
                raise NotImplementedError(
                    "the represented singular subscheme currently requires a field base"
                )
            algebra = self.coordinate_algebra()
            if algebra not in AlgebrasWithChosenFinitePresentation(base):
                raise NotImplementedError(
                    "the represented singular subscheme requires a chosen finite algebra presentation"
                )
            dimension = int(algebra.krull_dimension())
            engine_algebra = _engine_ring(algebra)
            defining_ideal = getattr(engine_algebra, "defining_ideal", lambda: None)()
            if defining_ideal is not None:
                try:
                    minimal_components = defining_ideal.minimal_associated_primes()
                except (AttributeError, NotImplementedError) as error:
                    raise NotImplementedError(
                        "the represented singular subscheme requires a represented equidimensionality check"
                    ) from error
                if any(
                    int(component.dimension()) != dimension
                    for component in minimal_components
                ):
                    raise NotImplementedError(
                        "the represented singular subscheme requires equidimensional fibres"
                    )
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
                raise NotImplementedError(
                    "the relative nonsmooth Fitting criterion requires represented flatness"
                )
            base = self.scheme_base_ring()
            algebra = self.coordinate_algebra()
            if algebra not in AlgebrasWithChosenFinitePresentation(base):
                raise NotImplementedError(
                    "the relative nonsmooth locus requires a chosen finite algebra presentation"
                )

            base_engine = _engine_ring(base)
            try:
                coefficient_field = base_engine.base_ring()
                supported_perfect_base = (
                    base_engine.ngens() == 1
                    and bool(coefficient_field.is_field())
                    and bool(coefficient_field.is_perfect())
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                supported_perfect_base = False
            if not supported_perfect_base:
                raise NotImplementedError(
                    "the relative hypersurface smoothness criterion currently requires k[t] with k perfect"
                )

            relative_dimension = (
                algebra._represented_primitive_hypersurface_relative_dimension()
            )
            return self.differential_rank_drop_subscheme(relative_dimension)

        def distinguished_open(self, element):
            r"""Return \(D(f)\subseteq X\), the open locus where ``element`` is a unit.

            \(D(f)=\operatorname{Spec}A[1/f]\), and the localization map
            \(A\to A[1/f]\) induces the open immersion.
            """
            from dzack_research.preamble.categories.rings.commutative_algebra import Localization

            algebra = self.coordinate_algebra()
            element = algebra(element)
            cache = getattr(self, "_preamble_distinguished_open_cache", ())
            for cached_element, cached_open in cache:
                if cached_element == element:
                    return cached_open
            localized = Localization(algebra, element)
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
            open_subscheme._preamble_distinguished_open_ambient = self
            open_subscheme._preamble_distinguished_open_element = element
            base = self.scheme_base_ring()
            open_subscheme = refine_scheme(open_subscheme, base, [OpenImmersions(self)])
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
            assert algebra_structure.domain() is self.coordinate_algebra(), (
                "a quasi-coherent algebra on Spec A is stated by an algebra map out of A"
            )
            structure_morphism = affine_spec_morphism(algebra_structure)
            return self.scheme_category().SliceOver(self)(structure_morphism)


class _AffineGSchemes(OwnedCategory):
    r"""Represented affine schemes with a chosen action of one group.

    This is the affine specialization of ``GObjects(G, Schemes(R))``.  It is
    private because the public category is the generic ``GObjects`` category;
    this level only supplies the affine construction and fixed-locus methods.
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
            AffineSchemes(self.base_ring()),
        ]

    def _repr_object_names(self):
        return (
            f"affine {self.acting_group()}-schemes over {self.base_ring()}"
        )

    def an_object(self):
        scheme = AffineSpace(1, self.base_ring())
        identity = scheme.categorical_identity_morphism()
        return affine_g_scheme(
            scheme,
            self.acting_group(),
            lambda _group_element: identity,
        )

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
                raise NotImplementedError(
                    "the represented common fixed ideal requires a chosen finite group generating set"
                )
            algebra = self.coordinate_algebra()
            base = self.scheme_base_ring()
            if algebra not in FramedAlgebras(base):
                raise NotImplementedError(
                    "the represented common fixed ideal requires a framed affine coordinate algebra"
                )
            labels = algebra.algebra_generating_set()
            if not labels.cardinality().is_finite():
                raise NotImplementedError(
                    "the represented common fixed ideal requires finitely many algebra generators"
                )

            equations = []
            for group_generator in group.group_generators():
                pullback = self.action_of(
                    group_generator
                ).coordinate_algebra_morphism()
                if (
                    pullback.domain() is not algebra
                    or pullback.codomain() is not algebra
                ):
                    raise ValueError(
                        "an affine scheme action must act by endomorphisms of its coordinate algebra"
                    )
                for label in labels:
                    generator = algebra.algebra_generator(label)
                    equations.append(pullback(generator) - generator)
            return algebra.ideal(*equations)

        @cached_method
        def fixed_subscheme(self):
            r"""Return the common fixed subscheme ``X^G`` of this affine action."""
            return self.closed_subscheme(
                tuple(self.fixed_ideal().ideal_generators())
            )

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

        @cached_method
        def affine_quotient(self: Any) -> Any:
            r"""Return ``Spec(A^G)`` for the supported affine linear action."""
            return Spec(self.invariant_algebra(), base_ring=self.scheme_base_ring())

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
            if target not in AffineSchemes(base):
                raise NotImplementedError(
                    "the represented quotient universal property currently targets affine schemes"
                )
            target_algebra = target.coordinate_algebra()
            if target_algebra not in FramedAlgebras(base):
                raise NotImplementedError(
                    "the represented quotient factorization requires a framed target coordinate algebra"
                )
            labels = target_algebra.algebra_generating_set()
            if not labels.cardinality().is_finite():
                raise NotImplementedError(
                    "the represented quotient factorization requires finitely many target generators"
                )

            source_algebra = self.coordinate_algebra()
            pullback = morphism.coordinate_algebra_morphism()
            if pullback.domain() is not target_algebra or pullback.codomain() is not source_algebra:
                raise ValueError("the affine morphism has the wrong represented coordinate pullback")

            invariant_algebra, inclusion, engine_invariants = self._invariant_algebra_data()
            group_generators = tuple(self.acting_group().group_generators())
            engine_source = _engine_ring(source_algebra)

            generator_images = {}
            for label in labels:
                image = pullback(target_algebra.algebra_generator(label))
                if any(
                    self.action_of(group_generator).coordinate_algebra_morphism()(image)
                    != image
                    for group_generator in group_generators
                ):
                    raise ValueError("the stated affine morphism is not invariant under the represented group action")
                if not engine_invariants:
                    generator_images[label] = invariant_algebra(image)
                    continue
                engine_image = engine_source(_engine_element(source_algebra, image))
                certificate = engine_image.in_subalgebra(
                    engine_invariants,
                    algorithm="groebner",
                    certificate="invariant",
                )
                if certificate is None:
                    raise ArithmeticError(
                        "the invariant-ring backend did not express a verified invariant in its selected generators"
                    )
                generator_images[label] = _evaluate_polynomial_in_algebra(
                    certificate,
                    invariant_algebra,
                )

            factor_pullback = target_algebra.Mor(invariant_algebra)(generator_images)
            factor = _affine_morphism_from_pullback(
                self.affine_quotient(),
                target,
                factor_pullback,
            )
            if factor * self.quotient_morphism() != morphism:
                raise ArithmeticError("the represented affine quotient factorization failed its defining triangle")
            if any(
                inclusion(factor_pullback(target_algebra.algebra_generator(label)))
                != pullback(target_algebra.algebra_generator(label))
                for label in labels
            ):
                raise ArithmeticError("the represented quotient factorization disagrees on a target generator")
            return factor


class QuasiAffineSchemes(_SchemePropertyCategory):
    property_name = "quasi-affine"
    absolute = True

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
            r"""``V_+(f_1, ..., f_k)``, cut out by homogeneous equations."""
            equations = (
                tuple(equations[0])
                if len(equations) == 1 and isinstance(equations[0], (tuple, list))
                else tuple(equations)
            )
            for equation in equations:
                assert equation.is_homogeneous(), (
                    f"{equation} is not homogeneous, so it cuts out no closed subscheme of {self}"
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
        return _placed_over_stated_base(candidate, self, AffineSpaces)

    class ParentMethods:
        def zeta_function(self):
            r"""Return ``Z(A^d/F_q,T)=1/(1-q^d T)``."""
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = PolynomialRing(rationals, "T")
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
        return _placed_over_stated_base(candidate, self, ProjectiveSpaces)

    class ParentMethods:
        def _standard_chart_coordinate_name(self, chart_index, numerator_index):
            r"""The name of the coordinate ``x_k / x_i`` on the ``i``-th standard chart."""
            return f"x{int(numerator_index)}_over_x{int(chart_index)}"

        def _standard_chart_coordinate(self, chart_index, numerator_index):
            r"""``x_k / x_i`` as a generator of the ``i``-th chart's coordinate algebra."""
            algebra = self.standard_affine_chart(chart_index).coordinate_algebra()
            return algebra.algebra_generator(
                self._standard_chart_coordinate_name(chart_index, numerator_index)
            )

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
                AffineSpace(
                    dimension,
                    base,
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
            r"""``U_i cap U_j = D(x_j/x_i)``, an open of the ``i``-th chart.

            Inside ``U_i`` the locus where ``x_j`` does not vanish is where the
            ratio ``x_j/x_i`` is invertible, so the overlap is the
            distinguished open of that coordinate.
            """
            chart = self.standard_affine_chart(chart_index)
            return chart.distinguished_open(
                self._standard_chart_coordinate(chart_index, other_index)
            )

        def _standard_chart_change(self, source_index, target_index):
            r"""``U_i cap U_j -> U_j cap U_i``, read on coordinates."""
            source_index = int(source_index)
            target_index = int(target_index)
            assert source_index != target_index, (
                "a chart change joins two distinct standard charts"
            )
            dimension = int(self.relative_dimension())
            source_overlap = self.standard_chart_overlap(source_index, target_index)
            target_overlap = self.standard_chart_overlap(target_index, source_index)
            target_chart = self.standard_affine_chart(target_index)
            restriction = source_overlap.inclusion().coordinate_algebra_morphism()
            inverse_ratio = restriction(
                self._standard_chart_coordinate(source_index, target_index)
            ).inverse_of_unit()
            images = {}
            for numerator in range(dimension + 1):
                if numerator == target_index:
                    continue
                name = self._standard_chart_coordinate_name(target_index, numerator)
                if numerator == source_index:
                    images[name] = inverse_ratio
                else:
                    images[name] = (
                        restriction(
                            self._standard_chart_coordinate(source_index, numerator)
                        )
                        * inverse_ratio
                    )
            into_target_chart = source_overlap.Mor(target_chart)(
                target_chart.coordinate_algebra().Mor(
                    source_overlap.coordinate_algebra()
                )(images)
            )
            return target_overlap.corestriction(into_target_chart)

        def standard_chart_transition(self, source_index, target_index):
            r"""``phi_{ji}: U_i cap U_j -> U_j cap U_i``, the chart change and its inverse.

            On coordinates ``x_k/x_j = (x_k/x_i)(x_j/x_i)^{-1}`` and
            ``x_i/x_j = (x_j/x_i)^{-1}``, which is defined because ``x_j/x_i``
            is invertible on the overlap.  Exchanging the two indices gives the
            inverse map, so the overlaps are isomorphic and these are the
            transitions of the standard atlas (Stacks, Tag 01MM).
            """
            return Isomorphism(
                self._standard_chart_change(source_index, target_index),
                self._standard_chart_change(target_index, source_index),
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
                tuple(
                    self.standard_chart_transition(left, right)
                    for left, right in combinations(indices, 2)
                ),
            )

        def zeta_function(self):
            r"""Return ``Z(P^d/F_q,T)=prod_{i=0}^d(1-q^i T)^(-1)``."""
            base = _engine_ring(self.scheme_base_ring())
            if not bool(base.is_finite()) or not bool(base.is_field()):
                raise TypeError("the arithmetic zeta function here requires a finite field")
            from sage.misc.misc_c import prod
            from sage.rings.rational_field import QQ as SageQQ

            rationals = _own_ring(SageQQ)
            polynomial = PolynomialRing(rationals, "T")
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
        return _placed_over_stated_base(candidate, self, ProductSchemes)

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

        def from_product_cone(self, legs):
            r"""The unique morphism ``T -> prod_i X_i`` with the stated legs.

            A cone over the product is the family of legs ``f_i: T -> X_i``,
            indexed the way the factors are, so that is the datum this takes.

            For affine factors the product is ``Spec`` of the coproduct of
            coordinate algebras, so the cone map is the cocone map on
            algebras: each generator of the product algebra is the image of a
            factor generator under a projection pullback, and it is sent to
            that generator's image under the corresponding leg.
            """
            factors = self.factors()
            legs = _finite_factor_family(legs, name="Product cone legs")
            assert legs.cardinality() == factors.cardinality(), (
                "a product cone has one leg per factor"
            )
            leg_labels = tuple(legs.index_set())
            source = legs[leg_labels[0]].domain()
            base = self.scheme_base_ring()
            assert all(legs[label].domain() is source for label in leg_labels), (
                "a cone has one apex"
            )
            assert self in AffineSchemes(base) and source in AffineSchemes(base), (
                "the represented product cone map currently requires affine schemes"
            )
            product_algebra = self.coordinate_algebra()
            images = {}
            for index, label in enumerate(leg_labels):
                leg = legs[label]
                factor = factors[index]
                assert leg.codomain() is factor, f"leg {index} must land in factor {index}"
                projection_pullback = self.projection(index).coordinate_algebra_morphism()
                leg_pullback = leg.coordinate_algebra_morphism()
                factor_algebra = factor.coordinate_algebra()
                for label in factor_algebra.algebra_generating_set():
                    generator = factor_algebra.algebra_generator(label)
                    images[_algebra_generator_label(product_algebra, projection_pullback(generator))] = (
                        leg_pullback(generator)
                    )
            pullback = product_algebra.Mor(source.coordinate_algebra())(images)
            cone = _affine_morphism_from_pullback(source, self, pullback)
            for index, label in enumerate(leg_labels):
                assert self.projection(index) * cone == legs[label], (
                    f"the product cone map does not recover leg {index}"
                )
            return cone


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
        return _placed_over_stated_base(candidate, self, ProductProjectiveSpaces)


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
    categories = [AffineSchemes(base)]
    if algebra is base or algebra in FramedAlgebras(base):
        categories.append(FiniteTypeSchemes(base))
    if algebra is base:
        categories.append(SmoothSchemes(base))
        if _normal_placement(base):
            categories.append(NormalSchemes(base))
    if _integral_placement(algebra):
        categories.append(IntegralSchemes(base))
    categories.extend(extra_categories)

    refine_scheme(scheme, base, categories)
    scheme._preamble_engine_coordinate_ring = _engine_ring(algebra)
    scheme._preamble_coordinate_algebra = algebra

    engine_identity = _engine_ring(algebra).hom(_engine_ring(algebra))
    coordinate_identity = (
        ring_homset(base, base).identity()
        if algebra is base
        else algebra.Mor(algebra).identity()
    )
    scheme._preamble_identity_morphism = SchemeMorphism(
        _native_scheme_homset(scheme, scheme)(engine_identity, check=False),
        domain=scheme,
        codomain=scheme,
        pullback=coordinate_identity,
    )

    if is_base_scheme:
        scheme._preamble_structure_morphism = scheme._preamble_identity_morphism
        return scheme

    base_scheme = Spec(base, base_ring=base)
    engine_map = _engine_ring(algebra).coerce_map_from(_engine_ring(base))
    if engine_map is None:
        raise NotImplementedError(
            "the affine Spec structure morphism currently requires an exact "
            "engine realization of the algebra structure map"
        )
    structure_pullback = (
        coordinate_identity
        if algebra is base
        else algebra.algebra_structure_morphism()
    )
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


def Spec(ring_or_algebra, base_ring=None):
    r"""Return the affine scheme ``Spec(A)`` over the represented scalar base.

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
            base = (
                algebra
                if _engine_ring(declared_base) is _engine_ring(algebra)
                else _own_ring(declared_base)
            )
    else:
        base = _own_ring(base_ring)

    cache_key = (id(algebra), id(base))
    cached = _AFFINE_SPECTRA.get(cache_key)
    if (
        cached is not None
        and cached.coordinate_algebra() is algebra
        and cached.scheme_base_ring() is base
    ):
        return cached

    scheme = _initialize_owned_affine_spectrum(
        _SageSpec(_engine_ring(algebra), _engine_ring(base)),
        algebra,
        base,
        is_base_scheme=algebra is base,
    )
    _AFFINE_SPECTRA[cache_key] = scheme
    return scheme


def _engine_affine_pullback(pullback):
    r"""Return the private Sage ring map realizing an affine pullback."""
    if isinstance(pullback, RingMorphism):
        return pullback._engine_morphism_crossing()
    return _engine_algebra_morphism(pullback)


def _affine_morphism_from_pullback(
    domain: Any,
    codomain: Any,
    pullback: Any,
) -> SchemeMorphism:
    r"""Site one represented coordinate pullback on the stated affine endpoints."""
    domain_algebra = domain.coordinate_algebra()
    codomain_algebra = codomain.coordinate_algebra()
    if pullback.domain() is not codomain_algebra or pullback.codomain() is not domain_algebra:
        raise ValueError(
            "an affine scheme morphism requires a pullback from the codomain algebra to the domain algebra"
        )
    native = _native_scheme_homset(domain, codomain)(
        _engine_affine_pullback(pullback),
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
        raise NotImplementedError(
            "the represented invariant algebra currently requires a finite group with a chosen finite generating set"
        )
    algebra = scheme.coordinate_algebra()
    base = scheme.scheme_base_ring()
    if algebra not in SymmetricAlgebras(base) or algebra not in FramedAlgebras(base):
        raise NotImplementedError(
            "the represented invariant-ring backend currently requires a polynomial coordinate algebra"
        )
    labels = tuple(algebra.algebra_generating_set())
    if not algebra.algebra_generating_set().cardinality().is_finite():
        raise NotImplementedError(
            "the represented invariant-ring backend requires finitely many polynomial generators"
        )
    engine_algebra = _engine_ring(algebra)
    variables = tuple(engine_algebra.gens())
    if len(variables) != len(labels):
        raise ArithmeticError("the selected polynomial framing disagrees with its computation engine")
    engine_base = _engine_ring(base)
    if not bool(engine_base.is_field()):
        raise NotImplementedError(
            "the selected Singular invariant-ring backend currently requires a field of coefficients"
        )

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
            image = engine_algebra(
                _engine_element(algebra, pullback(algebra.algebra_generator(label)))
            )
            row = []
            linear_part = engine_algebra.zero()
            for variable in variables:
                coefficient = image.monomial_coefficient(variable)
                row.append(engine_base(coefficient))
                linear_part += coefficient * variable
            if image != linear_part:
                raise NotImplementedError(
                    "the selected invariant-ring backend currently requires a linear action on polynomial generators"
                )
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
        raise NotImplementedError(
            "Sage/Singular does not support invariant generation for this coefficient field and linear action"
        ) from error
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
    invariant_elements = tuple(
        algebra._from_engine_element(invariant)
        for invariant in engine_invariants
    )
    if any(
        pullback(invariant) != invariant
        for pullback in pullbacks
        for invariant in invariant_elements
    ):
        raise ArithmeticError(
            "the backend invariant generators do not match the represented coordinate action"
        )

    invariant_labels = tuple(f"invariant_{index}" for index in range(len(engine_invariants)))
    presentation = SymmetricAlgebraOn(base, invariant_labels)
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
        relations.append(
            presentation._from_engine_element(
                presentation_engine(relation_terms)
            )
        )
    invariant_algebra = (
        presentation
        if not relations
        else FinitelyPresentedAlgebra(presentation, tuple(relations))
    )
    invariant_labels = tuple(invariant_algebra.algebra_generating_set())
    inclusion = invariant_algebra.Mor(algebra)(
        {
            label: invariant_elements[index]
            for index, label in enumerate(invariant_labels)
        }
    )
    return invariant_algebra, inclusion, engine_invariants


def affine_g_scheme(scheme, group, action):
    r"""Equip a represented affine scheme with a chosen left ``group``-action.

    The returned affine scheme is a fresh mathematical object carrying the
    action; the selected unacted ``Spec(A)`` is never mutated.  ``action(g)``
    is a represented scheme automorphism of the supplied scheme, and its
    coordinate pullback is transported to the fresh copy.
    """
    from dzack_research.preamble.categories.group.groups import _owned_group

    base = scheme.scheme_base_ring()
    if scheme not in AffineSchemes(base):
        raise TypeError("equipping a represented G-scheme currently requires an affine scheme")
    group = _owned_group(group)
    algebra = scheme.coordinate_algebra()

    acted = typecall(
        _SageAffineScheme,
        _engine_ring(algebra),
        _engine_ring(base),
    )
    acted._preamble_acting_group = group
    acted._preamble_underlying_category = Schemes(base)
    acted._preamble_unacted_scheme = scheme
    _initialize_owned_affine_spectrum(
        acted,
        algebra,
        base,
        extra_categories=(_AffineGSchemes(group, base),),
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


def affine_spec_morphism(algebra_morphism):
    r"""Return the affine scheme morphism contravariantly induced by an algebra map."""

    source_algebra = algebra_morphism.domain()
    target_algebra = algebra_morphism.codomain()
    ring = source_algebra.base_ring()
    if source_algebra not in Algebras(ring) or target_algebra not in Algebras(ring):
        raise TypeError("affine Spec acts on a represented algebra morphism")
    if source_algebra.base_ring() is not target_algebra.base_ring():
        raise ValueError("affine Spec requires an algebra morphism over one scalar base")
    source_scheme = Spec(target_algebra, base_ring=ring)
    target_scheme = Spec(source_algebra, base_ring=ring)
    try:
        engine_morphism = _engine_algebra_morphism(algebra_morphism)
    except (NotImplementedError, ValueError) as error:
        # A relative selected presentation can have a flattened Sage quotient
        # engine whose polynomial generators include generators of the scalar
        # ring.  The owned algebra morphism still contains the right map, but
        # the generic framed-algebra bridge cannot reconstruct that flattened
        # native map from the relative algebra generators alone.  A canonical
        # Sage coercion is an admissible private realization only after checking
        # it on finite generating families for both the algebra and its scalar
        # ring.
        base = source_algebra.base_ring()
        scalar_base = base.base_ring()
        if (
            source_algebra not in FramedAlgebras(base)
            or base not in FramedAlgebras(scalar_base)
        ):
            raise error
        algebra_labels = source_algebra.algebra_generating_set()
        scalar_labels = base.algebra_generating_set()
        if (
            not algebra_labels.cardinality().is_finite()
            or not scalar_labels.cardinality().is_finite()
        ):
            raise error
        engine_source = _engine_ring(source_algebra)
        engine_target = _engine_ring(target_algebra)
        engine_morphism = engine_target.coerce_map_from(engine_source)
        if engine_morphism is None:
            raise error

        test_values = tuple(
            source_algebra.algebra_generator(label)
            for label in algebra_labels
        ) + tuple(
            source_algebra(
                source_algebra.algebra_structure_morphism()(
                    base.algebra_generator(label)
                )
            )
            for label in scalar_labels
        )
        if any(
            engine_morphism(_engine_element(source_algebra, value))
            != _engine_element(target_algebra, algebra_morphism(value))
            for value in test_values
        ):
            raise error
    native = _native_scheme_homset(source_scheme, target_scheme)(
        engine_morphism, check=False
    )
    morphism = refine_scheme_morphism(
        native,
        source_algebra.base_ring(),
        domain=source_scheme,
        codomain=target_scheme,
    )
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
    if _normal_placement(base):
        categories.append(NormalSchemes(base))
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
        _native_scheme_homset(scheme, scheme)(
            list(engine_coordinate_ring.gens()),
            check=False,
        ),
        base,
        domain=scheme,
        codomain=scheme,
    )
    scheme._preamble_identity_morphism._preamble_coordinate_algebra_morphism = (
        scheme.coordinate_algebra().Mor(scheme.coordinate_algebra()).identity()
    )
    base_scheme = Spec(base, base_ring=base)
    engine_map = engine_coordinate_ring.coerce_map_from(_engine_ring(base))
    if engine_map is None:
        raise NotImplementedError(
            "the affine-space structure morphism requires the scalar base injection"
        )
    scheme._preamble_structure_morphism = refine_scheme_morphism(
        _native_scheme_homset(scheme, base_scheme)(engine_map, check=False),
        base,
        domain=scheme,
        codomain=base_scheme,
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
    if _normal_placement(base):
        categories.append(NormalSchemes(base))
    return refine_scheme(scheme, base, categories)


def _product_projection(product, factor, coordinates):
    native = _native_scheme_homset(product, factor)(list(coordinates), check=False)
    projection = categorical_scheme_morphism(
        native,
        domain=product,
        codomain=factor,
    )
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
        # Each factor brings its own homogeneous coordinates x0..xn, so the
        # product needs one name per coordinate of the whole; the affine branch
        # above indexes them by factor for the same reason.
        names = tuple(
            f"x{factor}_{coordinate}"
            for factor, scheme in enumerate(schemes)
            for coordinate in range(int(scheme.relative_dimension()) + 1)
        )
        product = _SageProductProjectiveSpaces(
            [int(scheme.relative_dimension()) for scheme in schemes],
            _engine_ring(base),
            names=names,
        )
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
        product = Spec(algebra, base_ring=base)
        projections = [affine_spec_morphism(factor_map) for factor_map in factor_maps]
        refine_scheme(product, base, [ProductSchemes(base)])
    else:
        # A^m_R x_R P^n_R is P^n over the affine factor's coordinate algebra,
        # because base change carries P^n_R along Spec A -> Spec R.  The object
        # is therefore already constructible; its two projections are not.  The
        # projection onto the affine factor is the structure morphism of
        # P^n_A, whose codomain is Spec(A) rather than the affine space object
        # a caller passed in, and the projection onto P^n_R is a morphism
        # between schemes over two different scalar rings, which the backend's
        # projective Hom does not represent.  Both are missing morphisms, not a
        # missing scheme.
        assert False, (
            "the mixed product A^m_R x P^n_R is P^n over the affine factor's coordinate "
            "algebra, but neither projection is represented: onto the affine factor it is "
            "the structure morphism of P^n_A, whose codomain is Spec(A) and not the affine "
            "space object, and onto P^n_R it is a morphism between schemes over two "
            "different scalar rings"
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
            return affine_spec_morphism(induced)


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
        equations = tuple(
            other_pullback(generator)
            for generator in quotient.defining_ideal().ideal_generators()
        )
        try:
            pushout, other_to_pushout = other._quotient_by_algebra_elements(
                equations
            )
        except NotImplementedError:
            return None

        engine_quotient_to_pushout = _engine_ring(pushout).coerce_map_from(
            _engine_ring(quotient)
        )
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
            if (
                left_to_target.domain() is not left_pullback.codomain()
                or right_to_target.domain() is not right_pullback.codomain()
            ):
                raise ValueError("the pushout cocone maps have the wrong domains")

            other_to_target = (
                left_to_target if quotient_on_right else right_to_target
            )
            target = other_to_target.codomain()
            labels = pushout.algebra_generating_set()
            return pushout.Mor(target)(
                {
                    label: other_to_target(other.algebra_generator(label))
                    for label in labels
                }
            )

        return pushout, left_to_pushout, right_to_pushout, factor

    represented = realize(left_pullback, right_pullback, quotient_on_right=True)
    if represented is not None:
        return represented
    return realize(right_pullback, left_pullback, quotient_on_right=False)


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


    left_pullback = left_map.coordinate_algebra_morphism()
    right_pullback = right_map.coordinate_algebra_morphism()
    cocone_factorization = None
    if base_scheme is left.base_scheme():
        # Spec R is terminal in Sch/R, so both legs are the structure
        # morphisms and the span sits under R, the initial object of CAlg_R.
        # A colimit under the initial object is the colimit of the discrete
        # diagram, so X x_{Spec R} Y = Spec(A tensor_R B) and the induced map
        # out of it is the coproduct's own factorization.
        algebra_pushout = Coproduct(
            left.coordinate_algebra(),
            right.coordinate_algebra(),
        )
        left_pushout_map, right_pushout_map = algebra_pushout.coproduct_injections()
        cocone_factorization = algebra_pushout.from_cocone
    else:
        try:
            algebra_pushout = Pushout(left_pullback, right_pullback)
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
    product = Spec(algebra_pushout, base_ring=base_ring)
    left_projection = affine_spec_morphism(left_pushout_map)
    right_projection = affine_spec_morphism(right_pushout_map)
    product._preamble_fiber_product_cospan = (left_map, right_map)
    product._preamble_fiber_product_algebra_pushout = algebra_pushout
    if cocone_factorization is not None:
        product._preamble_fiber_product_cocone_factorization = cocone_factorization
    product._preamble_fiber_product_projections = (
        left_projection,
        right_projection,
    )
    return refine_scheme(product, base_ring, [FiberProductSchemes(base_ring)])

class _SchemeSubobjectsOf(OwnedParameterizedCategory):
    r"""Subobjects of one scheme, by the kind of immersion they carry."""

    def base_object(self):
        r"""Return the scheme these subobjects are subobjects of."""
        return self.base()

    def _repr_object_names(self) -> str:
        return f"{self.immersion_name} into {self.base_object()}"

    def super_categories(self):
        base_object = self.base_object()
        return [
            Schemes(base_object.scheme_base_ring()).SubobjectCategory(base_object)
        ]

    class ParentMethods:
        def inclusion(self):
            r"""Return the chosen monomorphism representing this subobject.

            A subobject of ``X`` is the pair ``(Z, i: Z -> X)``, so the scheme
            it sits inside is ``i.codomain()`` and is never separate data.
            """
            return self._preamble_inclusion


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
        def codimension(self):
            defining = getattr(self, "_preamble_defining_ideal", None)
            codomain = self.inclusion().codomain()
            if defining is not None and hasattr(codomain, "coordinate_algebra"):

                codomain_engine = _engine_ring(codomain.coordinate_algebra())
                ideal_engine = defining._engine_ideal()
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

        def corestriction(self, morphism):
            r"""The factorization ``T -> Z`` of a morphism ``T -> X`` landing in ``Z``.

            A morphism into ``X`` factors through the closed subscheme
            ``Z = V(I)`` exactly when its pullback kills ``I`` (Stacks, Tag
            01QP); for affine endpoints the factor is ``Spec`` of the induced
            map ``A/I -> O(T)`` on the presentation's generators.
            """
            assert morphism.codomain() is self.inclusion().codomain(), (
                "a corestriction is taken of a morphism into the codomain of the inclusion"
            )
            source = morphism.domain()
            base = source.scheme_base_ring()
            assert source in AffineSchemes(base) and self in AffineSchemes(base), (
                "the represented corestriction currently requires affine schemes"
            )
            pullback = morphism.coordinate_algebra_morphism()
            for equation in self.defining_equations():
                assert pullback(equation) == source.coordinate_algebra().zero(), (
                    f"{morphism} does not factor through {self}: its pullback does not kill {equation}"
                )
            quotient_map = self.inclusion().coordinate_algebra_morphism()
            algebra = self.coordinate_algebra()
            factor_pullback = algebra.Mor(source.coordinate_algebra())(
                {
                    label: pullback(
                        morphism.codomain().coordinate_algebra().algebra_generator(label)
                    )
                    for label in algebra.algebra_generating_set()
                }
            )
            factor = _affine_morphism_from_pullback(source, self, factor_pullback)
            assert self.inclusion() * factor == morphism, (
                "the corestriction does not recover the morphism through the inclusion"
            )
            assert quotient_map.domain() is morphism.codomain().coordinate_algebra()
            return factor

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
            assert other.inclusion().codomain() is codomain, (
                "a scheme-theoretic intersection is taken inside one scheme"
            )
            return codomain.closed_subscheme(
                (*self.defining_equations(), *other.defining_equations())
            )

        def intersection_multiplicity(self, other, point):
            r"""``i(p; Z . W)``, the multiplicity of the intersection at ``p``.

            The definition is the length of the stalk at ``p`` of the
            structure sheaf of ``Z cap W``, taken over ``O_{X,p}``, and it
            is the intersection multiplicity exactly when the intersection is
            proper at ``p``; for an improper intersection the number is
            Serre's alternating sum of the lengths of
            ``Tor_i^{O_{X,p}}(O_{Z,p}, O_{W,p})``.

            Both readings need one operation the preamble does not own: the
            composition length of a finitely generated module over a local
            ring.  Every other part is here -- ``intersection`` builds the
            subscheme, ``direct_image`` reads its structure sheaf as an
            ``O_X``-module, the stalk localizes it at ``p``, and ``Tor`` is
            already a functor on modules -- so this body is the composite

                ``self.intersection(other).structure_sheaf_pushforward()``
                ``.stalk(point).length()``

            once that length answers.
            """
            assert False, (
                "the intersection multiplicity is the length of O_{Z cap W, p} over O_{X,p}, "
                "and no composition length of a finitely generated module over a local ring is "
                "owned; the scheme-theoretic intersection itself is `intersection`, and its "
                "stalk at p is available through the direct image of its structure sheaf"
            )

        def ideal_sheaf(self):
            r"""``I_Z = I~``, the quasi-coherent ideal sheaf of ``Z = V(I)`` on affine ``X``."""
            codomain = self.inclusion().codomain()
            assert codomain in AffineSchemes(codomain.scheme_base_ring()), (
                "the ideal sheaf is represented on an affine scheme"
            )
            return codomain.associated_module_sheaf(self.defining_ideal_owned())


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
        line = AffineSpace(1, self.base_ring())
        first = next(iter(line.coordinate_algebra().algebra_generators()))
        return line.closed_subscheme(first)

    def _repr_object_names(self):
        return f"closed subschemes of schemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return candidate in Schemes(self.base_ring()) and _has_scheme_placement(
            candidate, ClosedEmbeddings
        )


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
            return (
                getattr(self, "_preamble_distinguished_open_ambient", None)
                is self.inclusion().codomain()
            )

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
            assert morphism.codomain() is codomain, (
                "a corestriction is taken of a morphism into the codomain of the inclusion"
            )
            assert self.is_distinguished_open(), (
                "the represented open corestriction requires a distinguished open"
            )
            source = morphism.domain()
            assert source in AffineSchemes(codomain.scheme_base_ring()), (
                "the represented open corestriction currently requires an affine source"
            )
            source_algebra = source.coordinate_algebra()
            open_algebra = self.coordinate_algebra()
            pullback = morphism.coordinate_algebra_morphism()
            defining_element = codomain.coordinate_algebra()(
                self.distinguished_open_element()
            )
            assert source_algebra(pullback(defining_element)).is_unit(), (
                "the morphism does not land in this distinguished open: it does not send the "
                "defining element to a unit"
            )

            def factor_pullback(element):
                numerator, denominator = open_algebra.localization_fraction_data(element)
                return (
                    source_algebra(pullback(numerator))
                    * source_algebra(pullback(denominator)).inverse_of_unit()
                )

            factor = source.Mor(self)(
                ring_morphism(open_algebra, source_algebra, factor_pullback)
            )
            assert self.inclusion() * factor == morphism, (
                "the corestriction does not recover the morphism through the inclusion"
            )
            return factor

        def inclusion_into(self, larger_open):
            r"""The open immersion ``D(g) -> D(f)`` when ``D(g) <= D(f)`` in one affine scheme.

            Its pullback is the restriction ``O(D(f)) -> O(D(g))`` of the
            structure sheaf, which exists exactly when ``f`` is a unit on
            ``D(g)``; composed with the inclusion of ``D(f)`` it is the
            inclusion of ``D(g)``.
            """
            codomain = self.inclusion().codomain()
            assert larger_open.inclusion().codomain() is codomain, (
                "an inclusion between distinguished opens is taken in one affine scheme"
            )
            restriction = codomain.structure_sheaf().restriction_map(larger_open, self)
            inclusion = _affine_morphism_from_pullback(self, larger_open, restriction)
            assert larger_open.inclusion() * inclusion == self.inclusion(), (
                "the inclusion between distinguished opens does not compose to the inclusion into the scheme"
            )
            return inclusion


class SchemeMonomorphisms(MonoCategoryOf):
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
        open_image_isomorphism = arrow.__dict__.get(
            "_preamble_open_image_isomorphism"
        )
        if open_image is None or open_image_isomorphism is None:
            return False
        return (
            open_image in OpenImmersions(codomain)
            and open_image_isomorphism.forward().domain() is source
            and open_image_isomorphism.forward().codomain() is open_image
        )


def refine_closed_subscheme(
    subscheme,
    codomain=None,
    *,
    defining_equations=None,
):
    codomain = subscheme.ambient_space() if codomain is None else codomain
    base = codomain.scheme_base_ring()
    if defining_equations is not None:
        equations = tuple(defining_equations)
        subscheme._preamble_defining_equations = equations
        subscheme._preamble_defining_ideal = codomain.coordinate_ring().ideal(*equations)
    if getattr(subscheme, "_preamble_inclusion", None) is None:
        # The subobject is the arrow, so a route that did not build one takes
        # the native embedding, retargeted at the stated codomain.
        subscheme._preamble_inclusion = categorical_scheme_morphism(
            subscheme.embedding_morphism(),
            domain=subscheme,
            codomain=codomain,
        )
    return refine_scheme(
        subscheme,
        base,
        [ClosedEmbeddings(codomain), ClosedSubschemes(base)],
    )

__all__ = [
    "AffineSchemes",
    "AffineSpace",
    "AffineSpaces",
    "ClosedEmbeddings",
    "ClosedSubschemes",
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
