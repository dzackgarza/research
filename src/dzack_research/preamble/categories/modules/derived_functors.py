r"""Tor and Ext of finitely presented modules, computed from a free resolution.

For a module ``M`` with free resolution ``F_• -> M`` and a second module
``N``, the derived functors of ``- ⊗ N`` and ``Hom(-, N)`` are

``Tor_n(M, N) = H_n(F_• ⊗ N)``  and  ``Ext^n(M, N) = H^n(Hom(F_•, N))``.

Both are read off cohomology modules of represented cochain complexes, so a
result remembers the complex it was computed in and its cycle
representatives.  ``F_• ⊗ N`` is a chain complex; it is stored as a cochain
complex with ``F_i ⊗ N`` in degree ``shift - i``, and ``Tor_n`` is its
cohomology in degree ``shift - n``.

Both read the resolution one term past the degree asked for, because homology
in degree ``n`` needs the map into ``F_n`` as well as the map out of it.  Over
a principal ideal domain the resolution stops in degree one however far it is
asked to go; over a polynomial ring it continues by syzygies.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.tensor_hom import TensorByFunctor
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.internal_hom import internal_hom_morphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.modules.tensor_products import tensor_product_morphism
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


def _common_base_ring(module, other):
    ring = _owned_ring(module.base_ring())
    assert _owned_ring(other.base_ring()) == ring, (
        "Tor and Ext are taken between modules over one common base ring"
    )
    return ring


@cached_function(key=lambda module, other, shift, steps: (id(module), id(other), shift, steps))
def _tensored_resolution(module, other, shift, steps):
    r"""``F_• ⊗ other`` as a cochain complex with ``F_i ⊗ other`` in degree ``shift - i``."""
    ring = _common_base_ring(module, other)
    resolution = module.free_resolution(steps)
    length = resolution.length()
    tensor = TensorByFunctor(other)
    return CochainComplexes(ring)(
        {shift - term: tensor(resolution.term(term)) for term in range(length + 1)},
        {
            shift - term: tensor(resolution.differential(term))
            for term in range(1, length + 1)
        },
        name=f"Free resolution of {module} tensored with {other}",
    )


def _tor(module, other, degree=0):
    r"""Return ``Tor_degree(module, other)``, the homology of ``F_• ⊗ other``."""
    degree = int(degree)
    assert degree >= 0, "a homological degree is nonnegative"
    # Homology in degree n reads the map out of F_n and the map into it, so
    # the resolution must reach one term past the degree asked for.
    steps = degree + 1
    length = module.free_resolution(steps).length()
    shift = max(length, degree)
    return _tensored_resolution(module, other, shift, steps).cohomology(shift - degree)


def _ext(module, other, degree=0):
    r"""Return ``Ext^degree(module, other)``, the cohomology of ``Hom(F_•, other)``."""
    degree = int(degree)
    assert degree >= 0, "a cohomological degree is nonnegative"
    ring = _common_base_ring(module, other)
    resolution = module.free_resolution(degree + 1)
    length = resolution.length()
    identity = module_homset(other, other).identity()
    dualized = CochainComplexes(ring)(
        {term: resolution.term(term).module_category().Mor(resolution.term(term), other) for term in range(length + 1)},
        {
            term - 1: internal_hom_morphism(
                resolution.term(term - 1).module_category().Mor(resolution.term(term - 1), other),
                resolution.term(term).module_category().Mor(resolution.term(term), other),
                resolution.differential(term),
                identity,
            )
            for term in range(1, length + 1)
        },
        name=f"Free resolution of {module} dualized into {other}",
    )
    return dualized.cohomology(degree)


def _tor_map(morphism, other, degree=0, *, argument=1, lift=None):
    r"""Return the map on ``Tor_degree`` induced by ``morphism`` in one argument.

    With ``argument=1`` this is the existing covariance in the resolved
    variable: a selected free-resolution lift gives a chain map
    ``F(M) -> F(M')``.  With ``argument=2`` the resolution of the fixed first
    variable is unchanged and the component is
    ``id_{F_n} tensor morphism``.  In both cases a represented homology class
    is sent through its selected cycle representative, so the map is induced
    on the same owned quotient that defines ``module.tor``.
    """
    degree = int(degree)
    if degree < 0:
        raise ValueError("a Tor degree is nonnegative")
    match int(argument):
        case 1:
            steps = degree + 1
            source_resolution = morphism.domain().free_resolution(steps)
            target_resolution = morphism.codomain().free_resolution(steps)
            lifted = (
                source_resolution.lift_morphism(morphism, target_resolution)
                if lift is None
                else lift
            )
            if lifted.domain() is not source_resolution or lifted.codomain() is not target_resolution:
                raise ValueError("the selected Tor lift uses different resolutions")
            if lifted.module_morphism() is not morphism:
                raise ValueError("the selected Tor lift lies over a different module morphism")
            tensor = TensorByFunctor(other)
            component = tensor(lifted.component(degree))
            source = morphism.domain().tor(other, degree=degree)
            target = morphism.codomain().tor(other, degree=degree)
        case 2:
            if lift is not None:
                raise ValueError("an explicit resolution lift applies only to Tor's first argument")
            steps = degree + 1
            resolution = other.free_resolution(steps)
            term = resolution.term(degree)
            identity = module_homset(term, term).identity()
            modules = Modules(term.base_ring())
            source_tensor = modules.tensor_product((term, morphism.domain()))
            target_tensor = modules.tensor_product((term, morphism.codomain()))
            component = tensor_product_morphism(
                identity,
                morphism,
                source=source_tensor,
                target=target_tensor,
            )
            source = other.tor(morphism.domain(), degree=degree)
            target = other.tor(morphism.codomain(), degree=degree)
        case _:
            raise ValueError("the Tor argument must be 1 or 2")
    return module_homset(source, target).elementwise(
        lambda class_: target.class_of_cycle(
            component(source.cycle_representative(class_))
        )
    )


def _ext_map(morphism, other, degree=0, *, argument=1, lift=None):
    r"""Return the map on ``Ext^degree`` induced by ``morphism`` in one argument.

    The first variable is contravariant and the second is covariant.  Both
    maps are induced on the owned cohomology quotient by the corresponding
    internal-Hom component, rather than by recomputing an abstract Ext group.
    """
    degree = int(degree)
    if degree < 0:
        raise ValueError("an Ext degree is nonnegative")
    match int(argument):
        case 1:
            steps = degree + 1
            source_resolution = morphism.domain().free_resolution(steps)
            target_resolution = morphism.codomain().free_resolution(steps)
            lifted = (
                source_resolution.lift_morphism(morphism, target_resolution)
                if lift is None
                else lift
            )
            if lifted.domain() is not source_resolution or lifted.codomain() is not target_resolution:
                raise ValueError("the selected Ext lift uses different resolutions")
            if lifted.module_morphism() is not morphism:
                raise ValueError("the selected Ext lift lies over a different module morphism")
            identity = module_homset(other, other).identity()
            source_internal = target_resolution.term(degree).module_category().Mor(target_resolution.term(degree), other)
            target_internal = source_resolution.term(degree).module_category().Mor(source_resolution.term(degree), other)
            component = internal_hom_morphism(
                source_internal,
                target_internal,
                lifted.component(degree),
                identity,
            )
            source = morphism.codomain().ext(other, degree=degree)
            target = morphism.domain().ext(other, degree=degree)
        case 2:
            if lift is not None:
                raise ValueError("an explicit resolution lift applies only to Ext's first argument")
            steps = degree + 1
            resolution = other.free_resolution(steps)
            term = resolution.term(degree)
            identity = module_homset(term, term).identity()
            source_internal = term.module_category().Mor(term, morphism.domain())
            target_internal = term.module_category().Mor(term, morphism.codomain())
            component = internal_hom_morphism(
                source_internal,
                target_internal,
                identity,
                morphism,
            )
            source = other.ext(morphism.domain(), degree=degree)
            target = other.ext(morphism.codomain(), degree=degree)
        case _:
            raise ValueError("the Ext argument must be 1 or 2")
    return module_homset(source, target).elementwise(
        lambda class_: target.class_of_cycle(
            component(source.cycle_representative(class_))
        )
    )


__all__ = []
