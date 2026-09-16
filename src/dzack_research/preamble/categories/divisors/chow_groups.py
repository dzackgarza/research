r"""Owned algebraic-cycle and Chow-group roles."""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    FreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedNoetherianRings,
    _own_ring,
)


class _CycleDegreeConstruction:
    r"""The selected scheme and dimension defining a cycle-theoretic role."""

    def __init__(self, scheme, cycle_dimension) -> None:
        self._scheme = scheme
        self._cycle_dimension = int(cycle_dimension)

    def scheme(self):
        return self._scheme

    def cycle_dimension(self):
        return self._cycle_dimension


class AlgebraicCycleGroups(OwnedCategoryOverBaseRing):
    r"""Sparse free abelian groups on prime cycle components of one dimension."""

    @classmethod
    def _repr_object_names(cls):
        return "algebraic cycle groups"

    def super_categories(self):
        return [FreeModules(self.base_ring())]

    class ParentMethods:
        def __init__(self, _cycle_degree_construction, **rest) -> None:
            if not isinstance(_cycle_degree_construction, _CycleDegreeConstruction):
                raise TypeError("an algebraic cycle group requires selected cycle-degree data")
            self._cycle_degree_construction = _cycle_degree_construction
            super().__init__(**rest)

        def cycle_degree_construction(self):
            return self._cycle_degree_construction

        def cycle_scheme(self):
            return self.cycle_degree_construction().scheme()

        def cycle_dimension(self):
            return self.cycle_degree_construction().cycle_dimension()

        def cycle_codimension(self):
            return int(self.cycle_scheme().dimension()) - int(self.cycle_dimension())

        def prime_cycle(self, point):
            return self.module_generator(point)


class ChowGroups(OwnedCategoryOverBaseRing):
    r"""Finitely presented ``ZZ``-modules carrying one scheme and cycle degree."""

    @classmethod
    def _repr_object_names(cls):
        return "Chow groups"

    def super_categories(self):
        return [FinitelyPresentedModules(self.base_ring())]

    def _call_(self, module, scheme, cycle_dimension):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _SelectedFinitePresentationModules,
        )

        if module.base_ring() is not self.base_ring():
            raise ValueError("a Chow group uses the base ring of its represented module")
        if module not in _SelectedFinitePresentationModules(self.base_ring()):
            raise TypeError(
                "a represented Chow group requires a selected finite presentation"
            )
        return module._same_presentation_module(
            module.module_generating_set(),
            _extra_categories=(self,),
            _extra_construction_data={
                "_cycle_degree_construction": _CycleDegreeConstruction(
                    scheme,
                    cycle_dimension,
                ),
            },
        )

    class ParentMethods:
        def __init__(self, _cycle_degree_construction, **rest) -> None:
            if not isinstance(_cycle_degree_construction, _CycleDegreeConstruction):
                raise TypeError("a Chow group requires selected cycle-degree data")
            self._cycle_degree_construction = _cycle_degree_construction
            super().__init__(**rest)

        def cycle_degree_construction(self):
            return self._cycle_degree_construction

        def chow_scheme(self):
            return self.cycle_degree_construction().scheme()

        def cycle_dimension(self):
            return self.cycle_degree_construction().cycle_dimension()

        def cycle_codimension(self):
            return int(self.chow_scheme().dimension()) - int(self.cycle_dimension())


class TorusInvariantCycleGroups(OwnedCategoryOverBaseRing):
    r"""Free ``ZZ``-modules on orbit closures in one fixed dimension."""

    @classmethod
    def _repr_object_names(cls):
        return "torus-invariant cycle groups"

    def super_categories(self):
        return [AlgebraicCycleGroups(self.base_ring())]

    class ParentMethods:
        pass


def _affine_cycle_group(scheme, cycle_dimension):
    r"""Return ``Z_k(X)`` for a represented Noetherian affine scheme ``X``.

    The framing is the condition set of *all* prime points whose closures have
    dimension ``k``. It is not enumerated; cycle elements remain finite-support
    sparse sums, as algebraic cycles do mathematically.
    """
    from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

    base = scheme.scheme_base_ring()
    if scheme not in AffineSchemes(base):
        raise TypeError(
            "this cycle-group construction requires a represented affine scheme"
        )
    ring = scheme.coordinate_algebra()
    if ring not in OwnedNoetherianRings():
        raise TypeError(
            "this cycle-group construction requires a Noetherian coordinate ring"
        )
    cycle_dimension = int(cycle_dimension)
    if cycle_dimension < 0 or cycle_dimension > int(scheme.dimension()):
        raise ValueError(
            "cycle dimension lies between zero and the scheme dimension"
        )
    spectrum = ring.spectrum()
    locus = spectrum.condition_set(lambda point: point.closure_dimension() == cycle_dimension)
    integers = _own_ring(SageZZ)
    return integers._fresh_free_module_on(
        locus,
        _extra_categories=(AlgebraicCycleGroups(integers),),
        _extra_construction_data={
            "_cycle_degree_construction": _CycleDegreeConstruction(
                scheme,
                cycle_dimension,
            ),
        },
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


class AffineCodimensionOneChowComparison(SageObject):
    r"""The selected comparison ``Cl(X) ~= CH_{dim(X)-1}(X)``.

    A finite Weil-divisor presentation is embedded into the full Weil group.
    Through the scheme-owned Weil/cycle isomorphism it becomes a finite presentation
    inside the full codimension-one cycle group.  The *same* principal-divisor
    morphism then presents both the class group and the Chow quotient.
    """

    def __init__(self, divisor_classes, presentation_into_full_weil) -> None:
        scheme = divisor_classes.scheme()
        finite_weil = divisor_classes.weil_divisor_group()
        if presentation_into_full_weil.domain() is not finite_weil:
            raise ValueError(
                "the Weil presentation embedding has the wrong source"
            )
        full_weil = presentation_into_full_weil.codomain()
        if full_weil.divisor_scheme() is not scheme:
            raise ValueError(
                "the full Weil-divisor group belongs to a different scheme"
            )

        divisor_cycle = scheme.weil_cycle_isomorphism()
        into_full_cycles = divisor_cycle.forward() * presentation_into_full_weil
        cycle_presentation = into_full_cycles.image()
        cycle_inclusion = cycle_presentation.inclusion()
        weil_to_cycles = finite_weil.module_category().Mor(finite_weil, cycle_presentation)(
            {
                label: cycle_inclusion.lift(
                    into_full_cycles(finite_weil.module_generator(label))
                )
                for label in finite_weil.module_generating_set()
            }
        )
        principal_to_cycles = (
            weil_to_cycles * divisor_classes.principal_to_weil_morphism()
        )
        chow_cokernel = principal_to_cycles.cokernel()
        chow = ChowGroups(chow_cokernel.base_ring())(
            chow_cokernel,
            scheme,
            int(scheme.dimension()) - 1,
        )
        equip_chow = chow_cokernel.module_category().Mor(chow_cokernel, chow)(
            {
                label: chow.module_generator(label)
                for label in chow_cokernel.module_generating_set()
            }
        )
        cycle_class_projection = (
            equip_chow * principal_to_cycles.cokernel_projection()
        )

        classes = divisor_classes.class_group()
        class_projection = divisor_classes.weil_class_projection()
        class_to_chow = classes.module_category().Mor(classes, chow)(
            {
                label: cycle_class_projection(
                    weil_to_cycles(finite_weil.module_generator(label))
                )
                for label in classes.module_generating_set()
            }
        )
        cycles_to_weil = weil_to_cycles.inverse()
        chow_to_class = chow.module_category().Mor(chow, classes)(
            {
                label: class_projection(
                    cycles_to_weil(cycle_presentation.module_generator(label))
                )
                for label in chow.module_generating_set()
            }
        )

        self._scheme = scheme
        self._divisor_classes = divisor_classes
        self._divisor_cycle_isomorphism = divisor_cycle
        self._cycle_presentation = cycle_presentation
        self._principal_to_cycles = principal_to_cycles
        self._chow_group = chow
        self._cycle_class_projection = cycle_class_projection
        self._class_to_chow = classes.module_category().Core().Mor(classes, chow)(
            class_to_chow, chow_to_class
        )

    def scheme(self):
        return self._scheme

    def divisor_class_comparison(self):
        return self._divisor_classes

    def divisor_cycle_isomorphism(self):
        return self._divisor_cycle_isomorphism

    def cycle_presentation(self):
        return self._cycle_presentation

    def rational_equivalence_morphism(self):
        return self._principal_to_cycles

    def chow_group(self):
        return self._chow_group

    def cycle_class_projection(self):
        return self._cycle_class_projection

    def class_to_chow_isomorphism(self):
        return self._class_to_chow

    def _repr_(self) -> str:
        return f"Codimension-one Chow comparison for {self.scheme()}"



class SerreIntersectionData(SageObject):
    r"""A supported local intersection represented by its Tor modules and lengths.

    For closed subschemes ``Y,Z`` of a smooth affine space ``X`` meeting only
    at the selected closed point ``p``, localization gives

    ``Tor_i^{O_X}(O_Y,O_Z)_p = Tor_i^{O_{X,p}}(O_{Y,p},O_{Z,p})``.

    Each global Tor module is then supported at ``p``, so its existing
    finite-length operation computes the local length.  The Serre intersection
    multiplicity is their alternating sum.
    """

    def __init__(self, left, right, point) -> None:
        from dzack_research.preamble.categories.schemes.schemes import AffineSpaces

        ambient = left.inclusion().codomain()
        if right.inclusion().codomain() is not ambient:
            raise ValueError("a local intersection is taken inside one ambient scheme")
        base = ambient.scheme_base_ring()
        if ambient not in AffineSpaces(base):
            raise TypeError(
                "the represented Serre intersection currently requires a smooth affine space"
            )
        spectrum = ambient.underlying_space()
        if getattr(point, "parent", lambda: None)() is not spectrum:
            point = spectrum(point)
        if not point.ideal().is_maximal():
            raise ValueError("the represented Serre intersection is supported at a closed point")
        meeting = left.intersection(right)
        if meeting.defining_ideal_owned().radical() != point.ideal():
            raise ValueError(
                "the represented Tor intersection must be supported only at the selected closed point"
            )

        left_module = left.defining_ideal_owned().inclusion().cokernel()
        right_module = right.defining_ideal_owned().inclusion().cokernel()
        maximum_degree = int(ambient.relative_dimension())
        tor_modules = tuple(
            left_module.tor(right_module, degree=degree)
            for degree in range(maximum_degree + 1)
        )
        lengths = tuple(
            _own_ring(SageZZ).zero()
            if module.is_zero()
            else module.finite_length_at_closed_point(point)
            for module in tor_modules
        )
        multiplicity = sum(
            (length if degree % 2 == 0 else -length)
            for degree, length in enumerate(lengths)
        )

        self._ambient = ambient
        self._left = left
        self._right = right
        self._point = point
        self._left_module = left_module
        self._right_module = right_module
        self._tor_modules = tor_modules
        self._tor_lengths = lengths
        self._multiplicity = _own_ring(SageZZ)(multiplicity)

    def ambient_scheme(self):
        return self._ambient

    def left_subscheme(self):
        return self._left

    def right_subscheme(self):
        return self._right

    def point(self):
        return self._point

    def left_structure_module(self):
        return self._left_module

    def right_structure_module(self):
        return self._right_module

    def tor_module(self, degree):
        degree = int(degree)
        if degree < 0 or degree >= len(self._tor_modules):
            raise ValueError("Tor degree lies between zero and the ambient dimension")
        return self._tor_modules[degree]

    def tor_length(self, degree):
        degree = int(degree)
        if degree < 0 or degree >= len(self._tor_lengths):
            raise ValueError("Tor degree lies between zero and the ambient dimension")
        return self._tor_lengths[degree]

    def multiplicity(self):
        return self._multiplicity

    def _repr_(self) -> str:
        return f"Serre intersection of {self.left_subscheme()} and {self.right_subscheme()} at {self.point()}: {self.multiplicity()}"



def _serre_intersection(left, right, point):
    r"""Return the supported local Serre intersection of two closed subschemes."""
    return SerreIntersectionData(left, right, point)


def _closed_immersion_cycle_pushforward(closed_subscheme, cycle):
    r"""Push a cycle forward along its represented closed immersion.

    A closed immersion is proper.  On a prime component it preserves dimension
    and residue field and sends the point by contraction along the quotient map;
    hence the coefficient is unchanged.
    """
    source = cycle.parent()
    if source not in AlgebraicCycleGroups(_own_ring(SageZZ)):
        raise TypeError("proper cycle pushforward starts with a represented algebraic cycle")
    if source.cycle_scheme() is not closed_subscheme:
        raise ValueError("the cycle belongs to a different source scheme")
    ambient = closed_subscheme.inclusion().codomain()
    target = ambient.cycle_group(source.cycle_dimension())
    quotient_map = closed_subscheme.inclusion().coordinate_algebra_morphism()
    ambient_spectrum = ambient.underlying_space()
    coefficients = {}
    for point, coefficient in source.framing_coefficients(cycle).items():
        contracted = quotient_map.contraction_of_ideal(point.ideal())
        image_point = ambient_spectrum(contracted)
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
    if source not in AlgebraicCycleGroups(_own_ring(SageZZ)):
        raise TypeError("flat cycle pullback starts with a represented algebraic cycle")
    ambient = open_subscheme.inclusion().codomain()
    if source.cycle_scheme() is not ambient:
        raise ValueError("the cycle belongs to a different target scheme")
    if not open_subscheme.is_distinguished_open():
        raise NotImplementedError(
            "the represented flat cycle pullback currently uses a distinguished open immersion"
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
    "AffineCodimensionOneChowComparison",
    "AlgebraicCycleGroups",
    "ChowGroups",
    "SerreIntersectionData",
    "TorusInvariantCycleGroups",
]
