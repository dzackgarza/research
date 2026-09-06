r"""The affine quotient of a group action, as a functor.

For an affine ``G``-scheme ``X = Spec(A)`` the quotient ``X/G = Spec(A^G)``
comes with the quotient morphism ``q_X`` and its universal property: an
invariant morphism out of ``X`` factors uniquely through ``q_X``.  Both are
owned by the affine ``G``-scheme level already.  What this module adds is the
action on morphisms, which the universal property determines and nothing else
supplies.

Given an equivariant ``f: X -> Y``, the composite ``q_Y f`` is invariant
because ``f`` intertwines the two actions and ``q_Y`` is invariant, so it
factors uniquely through ``q_X`` as ``f/G: X/G -> Y/G``.  Uniqueness of that
factorization is what makes ``X -> X/G`` functorial: it forces
``(g f)/G = (g/G)(f/G)`` and ``id/G = id`` without either being computed
separately.  An equivariant automorphism of ``X`` therefore descends to an
automorphism of ``X/G``, which is how a symmetry compatible with the group
action reaches the quotient.

The regime is the one the invariant algebra is constructed in.  Compatibility
of the quotient with base change, and the corresponding statement for a
family over a base, are not constructed here: they need the invariant algebra
of a base-changed action, and forming invariants does not commute with
arbitrary base change without a flatness or reductivity hypothesis that
nothing in the preamble currently states.
"""

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.schemes import AffineSchemes, Schemes


class AffineQuotientFunctor(Functor):
    r"""``(-)/G: GObjects(G, Sch_R) -> AffSch_R`` on the affine actions it is defined for."""

    def __init__(self, group, base_ring) -> None:
        base = _own_ring(base_ring)
        self._group = group
        self._base_ring = base
        Functor.__init__(self, GObjects(group, Schemes(base)), AffineSchemes(base))

    def acting_group(self):
        return self._group

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, acted):
        return acted.affine_quotient()

    def _apply_morphism(self, arrow):
        source = arrow.domain()
        target = arrow.codomain()
        return source.factor_through_affine_quotient(
            target.quotient_morphism() * arrow.underlying_arrow()
        )

    def _repr_(self):
        return f"Affine quotient by {self.acting_group()}"


__all__ = ["AffineQuotientFunctor"]
