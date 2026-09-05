r"""Tor and Ext of finitely presented modules, computed from a free resolution.

For a module ``M`` with free resolution ``F_• -> M`` and a second module
``N``, the derived functors of ``- ⊗ N`` and ``Hom(-, N)`` are

``Tor_n(M, N) = H_n(F_• ⊗ N)``  and  ``Ext^n(M, N) = H^n(Hom(F_•, N))``.

Both are read off cohomology modules of represented cochain complexes, so a
result remembers the complex it was computed in and its cycle
representatives.  ``F_• ⊗ N`` is a chain complex; it is stored as a cochain
complex with ``F_i ⊗ N`` in degree ``shift - i``, and ``Tor_n`` is its
cohomology in degree ``shift - n``.  The resolution currently owned by the
presented modules has length at most one, over a principal ideal domain.
"""

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
from dzack_research.preamble.categories.modules.pure.modules import free_resolution
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


def _common_base_ring(module, other):
    ring = _owned_ring(module.base_ring())
    assert _owned_ring(other.base_ring()) == ring, (
        "Tor and Ext are taken between modules over one common base ring"
    )
    return ring


def Tor(degree, module, other):
    r"""Return ``Tor_degree(module, other)``, the homology of ``F_• ⊗ other``."""
    degree = int(degree)
    assert degree >= 0, "a homological degree is nonnegative"
    ring = _common_base_ring(module, other)
    resolution = free_resolution(module)
    length = resolution.length()
    shift = max(length, degree)
    tensor = TensorByFunctor(other)
    tensored = CochainComplex(
        ring,
        {shift - term: tensor(resolution.term(term)) for term in range(length + 1)},
        {
            shift - term: tensor(resolution.differential(term))
            for term in range(1, length + 1)
        },
        name=f"Free resolution of {module} tensored with {other}",
    )
    return Cohomology(tensored, shift - degree)


def Ext(degree, module, other):
    r"""Return ``Ext^degree(module, other)``, the cohomology of ``Hom(F_•, other)``."""
    degree = int(degree)
    assert degree >= 0, "a cohomological degree is nonnegative"
    ring = _common_base_ring(module, other)
    resolution = free_resolution(module)
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


__all__ = ["Ext", "Tor"]
