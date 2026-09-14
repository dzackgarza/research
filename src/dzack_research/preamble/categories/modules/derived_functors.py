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
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplex,
    Cohomology,
)
from dzack_research.preamble.categories.modules.internal_hom import (
    InternalHom,
    internal_hom_morphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules, free_resolution
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
    resolution = free_resolution(module, steps)
    length = resolution.length()
    tensor = TensorByFunctor(other)
    return CochainComplex(
        ring,
        {shift - term: tensor(resolution.term(term)) for term in range(length + 1)},
        {
            shift - term: tensor(resolution.differential(term))
            for term in range(1, length + 1)
        },
        name=f"Free resolution of {module} tensored with {other}",
    )


def Tor(degree, module, other):
    r"""Return ``Tor_degree(module, other)``, the homology of ``F_• ⊗ other``."""
    degree = int(degree)
    assert degree >= 0, "a homological degree is nonnegative"
    # Homology in degree n reads the map out of F_n and the map into it, so
    # the resolution must reach one term past the degree asked for.
    steps = degree + 1
    length = free_resolution(module, steps).length()
    shift = max(length, degree)
    return Cohomology(_tensored_resolution(module, other, shift, steps), shift - degree)


def Ext(degree, module, other):
    r"""Return ``Ext^degree(module, other)``, the cohomology of ``Hom(F_•, other)``."""
    degree = int(degree)
    assert degree >= 0, "a cohomological degree is nonnegative"
    ring = _common_base_ring(module, other)
    resolution = free_resolution(module, degree + 1)
    length = resolution.length()
    identity = module_homset(other, other).identity()
    dualized = CochainComplex(
        ring,
        {term: InternalHom(resolution.term(term), other) for term in range(length + 1)},
        {
            term - 1: internal_hom_morphism(
                InternalHom(resolution.term(term - 1), other),
                InternalHom(resolution.term(term), other),
                resolution.differential(term),
                identity,
            )
            for term in range(1, length + 1)
        },
        name=f"Free resolution of {module} dualized into {other}",
    )
    return Cohomology(dualized, degree)


def TorMap(degree, morphism, other, *, argument=1, lift=None):
    r"""Return the map on ``Tor_degree`` induced by ``morphism`` in one argument.

    With ``argument=1`` this is the existing covariance in the resolved
    variable: a selected free-resolution lift gives a chain map
    ``F(M) -> F(M')``.  With ``argument=2`` the resolution of the fixed first
    variable is unchanged and the component is
    ``id_{F_n} tensor morphism``.  In both cases a represented homology class
    is sent through its selected cycle representative, so the map is induced
    on the same owned quotient that defines :func:`Tor`.
    """
    degree = int(degree)
    if degree < 0:
        raise ValueError("a Tor degree is nonnegative")
    match int(argument):
        case 1:
            steps = degree + 1
            source_resolution = free_resolution(morphism.domain(), steps)
            target_resolution = free_resolution(morphism.codomain(), steps)
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
            source = Tor(degree, morphism.domain(), other)
            target = Tor(degree, morphism.codomain(), other)
        case 2:
            if lift is not None:
                raise ValueError("an explicit resolution lift applies only to Tor's first argument")
            steps = degree + 1
            resolution = free_resolution(other, steps)
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
            source = Tor(degree, other, morphism.domain())
            target = Tor(degree, other, morphism.codomain())
        case _:
            raise ValueError("TorMap argument must be 1 or 2")
    return module_homset(source, target).elementwise(
        lambda class_: target.class_of_cycle(
            component(source.cycle_representative(class_))
        )
    )


def ExtMap(degree, morphism, other, *, argument=1, lift=None):
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
            source_resolution = free_resolution(morphism.domain(), steps)
            target_resolution = free_resolution(morphism.codomain(), steps)
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
            source_internal = InternalHom(target_resolution.term(degree), other)
            target_internal = InternalHom(source_resolution.term(degree), other)
            component = internal_hom_morphism(
                source_internal,
                target_internal,
                lifted.component(degree),
                identity,
            )
            source = Ext(degree, morphism.codomain(), other)
            target = Ext(degree, morphism.domain(), other)
        case 2:
            if lift is not None:
                raise ValueError("an explicit resolution lift applies only to Ext's first argument")
            steps = degree + 1
            resolution = free_resolution(other, steps)
            term = resolution.term(degree)
            identity = module_homset(term, term).identity()
            source_internal = InternalHom(term, morphism.domain())
            target_internal = InternalHom(term, morphism.codomain())
            component = internal_hom_morphism(
                source_internal,
                target_internal,
                identity,
                morphism,
            )
            source = Ext(degree, other, morphism.domain())
            target = Ext(degree, other, morphism.codomain())
        case _:
            raise ValueError("ExtMap argument must be 1 or 2")
    return module_homset(source, target).elementwise(
        lambda class_: target.class_of_cycle(
            component(source.cycle_representative(class_))
        )
    )


__all__ = ["Ext", "ExtMap", "Tor", "TorMap"]
