r"""Owned algebraic-cycle and Chow groups."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.divisors.divisor_groups import _cokernel_in_category
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    FreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedNoetherianRings,
    _own_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class AlgebraicCycleGroups(OwnedCategoryOverBaseRing):
    r"""Free groups of algebraic cycles of one dimension on one scheme.

    An object is the free module \(\bigoplus_V R\,[V]\) on a set of
    \(k\)-dimensional integral closed subschemes \(V\) of a scheme \(X\): all of
    \(Z_k(X)\) when the set is every such subscheme, and the subgroup they
    generate otherwise.  The set is consumed by the free-module level; this
    level adds \(X\) and \(k\).
    """

    @classmethod
    def _repr_object_names(cls):
        return "algebraic cycle groups"

    def super_categories(self):
        return [FreeModules(self.base_ring())]

    def _call_(self, scheme, cycle_dimension, prime_cycles):
        r"""The free group on the set ``prime_cycles`` of ``cycle_dimension``-dimensional prime cycles of ``scheme``."""
        return self.base_ring()._fresh_free_module_on(
            prime_cycles,
            _extra_categories=(self,),
            _extra_construction_data={
                "cycle_scheme": scheme,
                "cycle_dimension": cycle_dimension,
            },
        )

    class ParentMethods:
        def __init__(self, cycle_scheme, cycle_dimension, **rest) -> None:
            self._cycle_scheme = cycle_scheme
            self._cycle_dimension = int(cycle_dimension)
            super().__init__(**rest)

        def cycle_scheme(self):
            r"""The scheme whose cycles this group is framed by."""
            return self._cycle_scheme

        def cycle_dimension(self):
            r"""The dimension \(k\) of the prime cycles framing this group."""
            return self._cycle_dimension

        def cycle_codimension(self):
            return int(self.cycle_scheme().dimension()) - int(self.cycle_dimension())

        def prime_cycle(self, point):
            return self.module_generator(point)


class ChowGroups(OwnedCategoryOverBaseRing):
    r"""Chow groups \(A_k(X)\) of one scheme, with a chosen presentation.

    An object is \(\operatorname{coker}(\rho)\) of a rational-equivalence
    morphism \(\rho\) into a group of \(k\)-cycles on \(X\), framed by the
    generators of that group.  The presentation is consumed by the
    presented-module level; this level adds \(X\) and \(k\).
    """

    @classmethod
    def _repr_object_names(cls):
        return "Chow groups"

    def super_categories(self):
        return [FinitelyPresentedModules(self.base_ring())]

    def _call_(self, scheme, cycle_dimension, rational_equivalence):
        r"""\(Z_k/\operatorname{im}(\rho)\) for the rational-equivalence morphism ``rational_equivalence`` \(\rho\)."""
        assert rational_equivalence.codomain().base_ring() is self.base_ring(), (
            "a Chow group uses the base ring of the cycles it is presented on"
        )
        return _cokernel_in_category(
            rational_equivalence,
            self,
            chow_scheme=scheme,
            cycle_dimension=cycle_dimension,
        )

    def class_to_chow_isomorphism(
        self,
        class_group,
        weil_presentation_into_full_weil,
    ):
        r"""The isomorphism \(\operatorname{Cl}(X) \cong A_{\dim X - 1}(X)\) on a normal affine scheme.

        ``class_group`` is \(\operatorname{coker}\rho_W\) for its principal-divisor
        morphism \(\rho_W\colon P \to D\) into a finite Weil-divisor presentation
        \(D\), and ``weil_presentation_into_full_weil`` embeds \(D\) into the full
        Weil divisor group.  Through the scheme's Weil/cycle isomorphism \(D\)
        becomes a finite presentation inside the codimension-one cycle group,
        and the *same* principal divisors present the Chow quotient, which is
        built here; its ``rational_equivalence_morphism()`` is that composite.
        """
        scheme = class_group.class_group_scheme()
        principal_to_weil = class_group.principal_to_weil_morphism()
        finite_weil = principal_to_weil.codomain()
        assert weil_presentation_into_full_weil.domain() is finite_weil, (
            "the Weil presentation embedding has the wrong source"
        )
        assert weil_presentation_into_full_weil.codomain().divisor_scheme() is scheme, (
            "the full Weil-divisor group belongs to a different scheme"
        )
        into_full_cycles = (
            scheme.weil_cycle_isomorphism().forward() * weil_presentation_into_full_weil
        )
        cycle_presentation = into_full_cycles.image()
        cycle_inclusion = cycle_presentation.inclusion()
        weil_to_cycles = finite_weil.module_category().Mor(finite_weil, cycle_presentation)(
            {
                label: cycle_inclusion.lift(into_full_cycles(finite_weil.module_generator(label)))
                for label in finite_weil.module_generating_set()
            }
        )
        chow = self(
            scheme,
            int(scheme.dimension()) - 1,
            weil_to_cycles * principal_to_weil,
        )
        cycle_class_projection = chow.cokernel_projection()
        class_projection = class_group.cokernel_projection()
        class_to_chow = class_group.module_category().Mor(class_group, chow)(
            {
                label: cycle_class_projection(weil_to_cycles(finite_weil.module_generator(label)))
                for label in class_group.module_generating_set()
            }
        )
        cycles_to_weil = weil_to_cycles.inverse()
        chow_to_class = chow.module_category().Mor(chow, class_group)(
            {
                label: class_projection(cycles_to_weil(cycle_presentation.module_generator(label)))
                for label in chow.module_generating_set()
            }
        )
        return class_group.module_category().Core().Mor(class_group, chow)(
            class_to_chow,
            chow_to_class,
        )

    class ParentMethods:
        def __init__(self, chow_scheme, cycle_dimension, **rest) -> None:
            self._chow_scheme = chow_scheme
            self._cycle_dimension = int(cycle_dimension)
            super().__init__(**rest)

        def chow_scheme(self):
            r"""The scheme whose Chow group this presents."""
            return self._chow_scheme

        def cycle_dimension(self):
            r"""The dimension \(k\) of \(A_k(X)\)."""
            return self._cycle_dimension

        def cycle_codimension(self):
            return int(self.chow_scheme().dimension()) - int(self.cycle_dimension())

        def rational_equivalence_morphism(self):
            r"""The rational-equivalence morphism \(\rho\) into the \(k\)-cycles with \(A_k(X) = \operatorname{coker}\rho\).

            This is the defining morphism the presented-module level retains
            for this cokernel.
            """
            rational_equivalence = self.cokernel_morphism()
            assert rational_equivalence is not None, (
                "this Chow group was not built as the cokernel of a rational-equivalence morphism"
            )
            return rational_equivalence


class TorusInvariantCycleGroups(OwnedCategoryOverBaseRing):
    r"""Free groups on the torus-orbit closures of one dimension on a toric scheme."""

    @classmethod
    def _repr_object_names(cls):
        return "torus-invariant cycle groups"

    def super_categories(self):
        return [AlgebraicCycleGroups(self.base_ring())]

    def _call_(self, scheme, cycle_dimension, orbit_closures):
        r"""The free group on ``orbit_closures``, the ``cycle_dimension``-dimensional orbit closures of ``scheme``."""
        return self.base_ring()._fresh_free_module_on(
            orbit_closures,
            _extra_categories=(self,),
            _extra_construction_data={
                "cycle_scheme": scheme,
                "cycle_dimension": cycle_dimension,
            },
        )


def _affine_cycle_group(scheme, cycle_dimension):
    r"""``Z_k(X)`` for a represented Noetherian affine scheme ``X``.

    The framing is the condition set of *all* prime points whose closures have
    dimension ``k``.  It is not enumerated; cycle elements remain finite-support
    sparse sums, as algebraic cycles do mathematically.
    """
    from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

    assert scheme in AffineSchemes(scheme.scheme_base_ring()), (
        "this cycle-group construction requires a represented affine scheme"
    )
    ring = scheme.coordinate_algebra()
    assert ring in OwnedNoetherianRings(), (
        "this cycle-group construction requires a Noetherian coordinate ring"
    )
    cycle_dimension = int(cycle_dimension)
    assert 0 <= cycle_dimension <= int(scheme.dimension()), (
        "cycle dimension lies between zero and the scheme dimension"
    )
    return AlgebraicCycleGroups(_own_ring(SageZZ))(
        scheme,
        cycle_dimension,
        ring.spectrum().condition_set(lambda point: point.closure_dimension() == cycle_dimension),
    )


def _affine_weil_cycle_isomorphism(scheme):
    r"""Identify Weil divisors with codimension-one cycles on normal affine ``scheme``.

    Both groups are free abelian on the height-one points of the same spectrum;
    the comparison changes only the mathematical role attached to that common
    sparse framing.
    """
    weil = scheme.full_weil_divisor_group()
    cycles = scheme.cycle_group(int(scheme.dimension()) - 1)
    forward = weil.module_category().Mor(weil, cycles)(
        lambda point: cycles.prime_cycle(point)
    )
    inverse = cycles.module_category().Mor(cycles, weil)(
        lambda point: weil.prime_divisor(point)
    )
    return _isomorphism_from_known_inverse_pair(forward, inverse)


def _serre_intersection(left, right, point):
    r"""The Tor modules \(i \mapsto \operatorname{Tor}_i^{\mathcal{O}_X}(\mathcal{O}_Y, \mathcal{O}_Z)\) of a supported intersection.

    For closed subschemes ``Y,Z`` of a smooth affine space ``X`` meeting only
    at the closed point ``p``, localization gives

    ``Tor_i^{O_X}(O_Y,O_Z)_p = Tor_i^{O_{X,p}}(O_{Y,p},O_{Z,p})``,

    so each global Tor module is supported at ``p``.  The family is indexed by
    the degrees \(0 \le i \le \dim X\), beyond which Tor vanishes on a regular
    ambient scheme.
    """
    from dzack_research.preamble.categories.schemes.schemes import AffineSpaces

    ambient = left.inclusion().codomain()
    assert right.inclusion().codomain() is ambient, (
        "a local intersection is taken inside one ambient scheme"
    )
    assert ambient in AffineSpaces(ambient.scheme_base_ring()), (
        "the represented Serre intersection currently requires a smooth affine space"
    )
    point = ambient.underlying_space()(point)
    assert point.ideal().is_maximal(), (
        "the represented Serre intersection is supported at a closed point"
    )
    assert left.intersection(right).defining_ideal_owned().radical() == point.ideal(), (
        "the represented Tor intersection must be supported only at the selected closed point"
    )
    left_module = left.defining_ideal_owned().inclusion().cokernel()
    right_module = right.defining_ideal_owned().inclusion().cokernel()
    return finite_indexed_family(
        Sets.Δ[int(ambient.relative_dimension())],
        lambda degree: left_module.tor(right_module, degree=int(degree)),
        name="Tor modules of the local intersection",
    )


def _serre_intersection_multiplicity(left, right, point):
    r"""Serre's multiplicity \(\sum_i (-1)^i \operatorname{length} \operatorname{Tor}_i(\mathcal{O}_Y, \mathcal{O}_Z)_p\)."""
    tor_modules = _serre_intersection(left, right, point)
    point = left.inclusion().codomain().underlying_space()(point)
    integers = _own_ring(SageZZ)
    return sum(
        (
            integers(-1) ** int(degree) * _length_at_closed_point(tor_modules[degree], point)
            for degree in tor_modules.index_set()
        ),
        integers.zero(),
    )


def _length_at_closed_point(module, point):
    r"""The length of a module supported at the closed point ``point``; the zero module has length zero."""
    if module.is_zero():
        return _own_ring(SageZZ).zero()
    return module.finite_length_at_closed_point(point)


def _closed_immersion_cycle_pushforward(closed_subscheme, cycle):
    r"""Push a cycle forward along its represented closed immersion.

    A closed immersion is proper.  On a prime component it preserves dimension
    and residue field and sends the point by contraction along the quotient map;
    hence the coefficient is unchanged.
    """
    source = cycle.parent()
    assert source in AlgebraicCycleGroups(_own_ring(SageZZ)), (
        "proper cycle pushforward starts with a represented algebraic cycle"
    )
    assert source.cycle_scheme() is closed_subscheme, (
        "the cycle belongs to a different source scheme"
    )
    ambient = closed_subscheme.inclusion().codomain()
    target = ambient.cycle_group(source.cycle_dimension())
    quotient_map = closed_subscheme.inclusion().coordinate_algebra_morphism()
    ambient_spectrum = ambient.underlying_space()
    coefficients = {}
    for point, coefficient in source.framing_coefficients(cycle).items():
        image_point = ambient_spectrum(quotient_map.contraction_of_ideal(point.ideal()))
        coefficients[image_point] = coefficients.get(
            image_point, target.base_ring().zero()
        ) + coefficient
    return target.linear_combination(coefficients)


def _distinguished_open_cycle_pullback(open_subscheme, cycle):
    r"""Pull a cycle back along a represented distinguished open immersion.

    Open immersions are flat of relative dimension zero.  A prime component
    survives exactly when it meets the open; then its ideal extends to the
    localization and its multiplicity is unchanged.
    """
    source = cycle.parent()
    assert source in AlgebraicCycleGroups(_own_ring(SageZZ)), (
        "flat cycle pullback starts with a represented algebraic cycle"
    )
    ambient = open_subscheme.inclusion().codomain()
    assert source.cycle_scheme() is ambient, "the cycle belongs to a different target scheme"
    assert open_subscheme.is_distinguished_open(), (
        "the represented flat cycle pullback is computed along a distinguished open "
        "immersion, where the pullback of a prime is the extension of its ideal to the "
        "localization; other open immersions are outside this computation"
    )
    target = open_subscheme.cycle_group(source.cycle_dimension())
    localization_map = open_subscheme.inclusion().coordinate_algebra_morphism()
    open_ring = open_subscheme.coordinate_algebra()
    open_spectrum = open_subscheme.underlying_space()
    coefficients = {}
    for point, coefficient in source.framing_coefficients(cycle).items():
        extended = localization_map.extension_of_ideal(point.ideal())
        if extended.contains_ambient_element(open_ring.one()):
            continue
        inverse_point = open_spectrum(extended)
        coefficients[inverse_point] = coefficients.get(
            inverse_point, target.base_ring().zero()
        ) + coefficient
    return target.linear_combination(coefficients)


def _fundamental_cycle(closed_subscheme):
    r"""Return the fundamental cycle of an affine closed subscheme.

    If ``Z = V(I)`` has dimension ``d``, its coefficient at a generic point
    ``eta`` of a ``d``-dimensional irreducible component is
    ``length(O_{Z,eta})``. Embedded components of smaller dimension are not
    generic points of the fundamental cycle; nilpotent thickness along a
    top-dimensional component is retained by the local length.
    """
    ambient = closed_subscheme.inclusion().codomain()
    dimension = int(closed_subscheme.dimension())
    cycles = ambient.cycle_group(dimension)
    ideal = closed_subscheme.defining_ideal_owned()
    spectrum = ambient.underlying_space()
    coefficients = {}
    for prime_ideal in ideal.associated_primes():
        point = spectrum(prime_ideal)
        if point.closure_dimension() != dimension:
            continue
        multiplicity = point.generic_local_length(ideal)
        if multiplicity:
            coefficients[point] = multiplicity
    return cycles.linear_combination(coefficients)


__all__ = [
    "AlgebraicCycleGroups",
    "ChowGroups",
    "TorusInvariantCycleGroups",
]
