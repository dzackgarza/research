r"""Owned algebraic-cycle and Chow-group roles."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
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
from dzack_research.preamble.categories.sets.set_categories import ConditionSet


class AlgebraicCycleGroups(OwnedCategoryOverBaseRing):
    r"""Sparse free abelian groups on prime cycle components of one dimension."""

    @classmethod
    def _repr_object_names(cls):
        return "algebraic cycle groups"

    def super_categories(self):
        return [FreeModules(self.base_ring())]

    class ParentMethods:
        def cycle_scheme(self):
            return self._preamble_cycle_scheme

        def cycle_dimension(self):
            return self._preamble_cycle_dimension

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

    class ParentMethods:
        def chow_scheme(self):
            return self._preamble_chow_scheme

        def cycle_dimension(self):
            return self._preamble_cycle_dimension

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


def AffineCycleGroup(scheme, cycle_dimension):
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
    locus = ConditionSet(
        spectrum,
        lambda point: point.closure_dimension() == cycle_dimension,
    )
    integers = _own_ring(SageZZ)
    return FreshFreeModuleOn(
        integers,
        locus,
        _extra_categories=(AlgebraicCycleGroups(integers),),
        _extra_construction_data={
            "cycle_scheme": scheme,
            "cycle_dimension": cycle_dimension,
            "cycle_prime_locus": locus,
        },
    )


def ClosedImmersionCyclePushforward(closed_subscheme, cycle):
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
    target = AffineCycleGroup(ambient, source.cycle_dimension())
    quotient_map = closed_subscheme.inclusion().coordinate_algebra_morphism()
    ambient_spectrum = ambient.underlying_space()
    coefficients = {}
    for point, coefficient in module_coefficients(cycle, source).items():
        contracted = quotient_map.contraction_of_ideal(point.ideal())
        image_point = ambient_spectrum(contracted)
        coefficients[image_point] = coefficients.get(
            image_point, target.base_ring().zero()
        ) + coefficient
    return target.linear_combination(coefficients)


def DistinguishedOpenCyclePullback(open_subscheme, cycle):
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
    target = AffineCycleGroup(open_subscheme, source.cycle_dimension())
    localization_map = open_subscheme.inclusion().coordinate_algebra_morphism()
    open_ring = open_subscheme.coordinate_algebra()
    open_spectrum = open_subscheme.underlying_space()
    coefficients = {}
    for point, coefficient in module_coefficients(cycle, source).items():
        extended = localization_map.extension_of_ideal(point.ideal())
        if extended.contains_ambient_element(open_ring.one()):
            continue
        inverse_point = open_spectrum(extended)
        coefficients[inverse_point] = coefficients.get(
            inverse_point, target.base_ring().zero()
        ) + coefficient
    return target.linear_combination(coefficients)


def FundamentalCycle(closed_subscheme):
    r"""Return the fundamental cycle of an affine closed subscheme.

    If ``Z = V(I)`` has dimension ``d``, its coefficient at a generic point
    ``eta`` of a ``d``-dimensional irreducible component is
    ``length(O_{Z,eta})``. Embedded components of smaller dimension are not
    generic points of the fundamental cycle; nilpotent thickness along a
    top-dimensional component is retained by the local length.
    """
    ambient = closed_subscheme.inclusion().codomain()
    dimension = int(closed_subscheme.dimension())
    cycles = AffineCycleGroup(ambient, dimension)
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


def ChowGroup(module, scheme, cycle_dimension):
    r"""Read ``module`` as ``A_cycle_dimension(scheme)`` without changing it."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _SelectedFinitePresentationModules,
    )

    ring = module.base_ring()
    if module not in _SelectedFinitePresentationModules(ring):
        raise TypeError(
            "a represented Chow group requires a selected finite presentation"
        )
    result = module._same_presentation_module(
        module.module_generating_set(),
        _extra_categories=(ChowGroups(ring),),
        _extra_construction_data={
            "chow_scheme": scheme,
            "cycle_dimension": int(cycle_dimension),
        },
    )
    return result


__all__ = [
    "AffineCycleGroup",
    "AlgebraicCycleGroups",
    "ChowGroup",
    "ClosedImmersionCyclePushforward",
    "DistinguishedOpenCyclePullback",
    "ChowGroups",
    "FundamentalCycle",
    "TorusInvariantCycleGroups",
]
