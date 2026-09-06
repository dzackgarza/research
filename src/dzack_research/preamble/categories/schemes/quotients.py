r"""The affine quotient of a group action and the sections it acts on, as functors.

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

Sections go the other way.  Taking the coordinate algebra of an affine
``G``-scheme with the action pullback induces on it is contravariant, and
lands in the ``R[G]``-modules; the invariants of that module are the sections
of the quotient, which is the statement the two functors make together.

The regime is the one the invariant algebra is constructed in.  Compatibility
of the quotient with base change, and the corresponding statement for a
family over a base, are not constructed here: they need the invariant algebra
of a base-changed action, and forming invariants does not commute with
arbitrary base change without a flatness or reductivity hypothesis that
nothing in the preamble currently states.
"""

from dzack_research.preamble.categories.abstract_categories.functors import (
    ContravariantFunctor,
)
from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebra
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    group_module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
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


class AffineSectionModuleFunctor(ContravariantFunctor):
    r"""``Gamma: GObjects(G, Sch_R)^op -> Modules(R[G])`` on affine actions.

    The sections of an affine ``G``-scheme ``X = Spec(B)`` carry one
    ``G``-action, and contravariance fixes which one.  Pullback composes the
    wrong way round, ``sigma_g^* sigma_h^* = sigma_{hg}^*``, so the left
    action is ``g . b = sigma_{g^{-1}}^*(b)`` and nothing else.

    This is the linearization of ``pi_* O_X`` along the structure morphism
    ``pi: X -> Spec(R)``, read as an ``R``-module with its ``G``-action.  For
    a cyclic cover it is where the grading of the cover algebra becomes
    representation theory: the deck generator multiplies the summand
    ``A z^i`` by ``zeta^{-i}``, so each summand is an eigen-submodule and the
    invariants are the summand of character one, which is what descends to
    the quotient.  Evaluating at a fixed point of the action is a morphism of
    this category, so the fibre over a fixed point inherits the action, and
    over a ramification point of a cover it is where the deck action stops
    being free.

    An equivariant ``f: X -> Y`` pulls sections back, and ``f^*`` is a
    morphism of ``R[G]``-modules because ``f`` intertwines the two actions.
    """

    def __init__(self, group, base_ring) -> None:
        base = _own_ring(base_ring)
        self._group = group
        self._base_ring = base
        ContravariantFunctor.__init__(
            self,
            GObjects(group, Schemes(base)),
            Modules(GroupAlgebra(base, group)),
        )

    def acting_group(self):
        return self._group

    def base_ring(self):
        return self._base_ring

    def _apply_contravariant_object(self, acted):
        algebra = acted.coordinate_algebra()

        def action(group_element, section):
            pullback = acted.action_of(
                ~group_element
            ).coordinate_algebra_morphism()
            return pullback(algebra(section))

        return self.codomain()(algebra, action)

    def _apply_contravariant_morphism(self, arrow):
        source = self.object_image(arrow.codomain())
        target = self.object_image(arrow.domain())
        pullback = arrow.underlying_arrow().coordinate_algebra_morphism()
        forget = source.forget_action_morphism()
        equip = target.equip_action_morphism()
        return group_module_homset(source, target)(
            {
                label: equip(pullback(forget(source.module_generator(label))))
                for label in source.module_generating_set()
            }
        )

    def _repr_(self):
        return f"Sections with their {self.acting_group()}-action"


__all__ = ["AffineQuotientFunctor", "AffineSectionModuleFunctor"]
