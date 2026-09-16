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

The regime is the one the invariant algebra is constructed in.  For a scalar
field extension, both invariant algebras can be constructed independently and
the canonical base-change comparison is represented below.  It is promoted to
an isomorphism only under the Reynolds hypothesis that the finite group order
is invertible in the target field.  No such assertion is made for arbitrary
base change, and in residue characteristic dividing the group order this
constant-group comparison is deliberately not used as a substitute for
group-scheme geometry.
"""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineGSchemes,
    Schemes,
    _affine_morphism_from_pullback,
    _evaluate_polynomial_in_algebra,
)




class AffineInvariantQuotientBaseChangeComparison(SageObject):
    r"""Compare ``(X/G)_{k'}`` with ``X_{k'}/G`` for a scalar field extension.

    The comparison map

    ``X_{k'}/G -> (X/G)_{k'}``

    is forced by the universal property of the target invariant quotient: the
    base-changed quotient map ``X_{k'} -> (X/G)_{k'}`` remains invariant.  The
    map exists whenever both represented invariant algebras do.

    When ``|G|`` is invertible in ``k'``, Reynolds averaging makes invariants an
    exact direct summand and they commute with the field extension.  In that
    regime :meth:`reynolds_isomorphism` constructs the inverse explicitly by
    expressing every new invariant generator in the base-changed old invariant
    generators through the same maintained subalgebra-membership certificates
    used by the affine quotient universal property.
    """

    def __init__(self, acted_scheme, ring_map) -> None:
        source = acted_scheme.scheme_base_ring()
        target = _own_ring(ring_map.codomain())
        if ring_map.domain() is not source:
            raise ValueError("quotient base change starts at the acted scheme's scalar field")
        assert source in OwnedFields() and target in OwnedFields(), (
            "the represented invariant-quotient base-change comparison requires a field extension"
        )
        if acted_scheme not in AffineGSchemes(acted_scheme.acting_group(), source):
            raise TypeError("the represented quotient base-change comparison requires an affine G-scheme")

        group = acted_scheme.acting_group()
        change = acted_scheme.scheme_category().base_change_functor(ring_map)
        changed_carrier = change(acted_scheme)
        changed_actions = {
            group_element: change(acted_scheme.action_of(group_element))
            for group_element in group
        }
        changed_acted = AffineGSchemes(group, target)(
            changed_carrier,
            lambda group_element: changed_actions[group(group_element)],
        )
        changed_old_quotient = change(acted_scheme.affine_quotient())
        changed_old_quotient_map = change(acted_scheme.quotient_morphism())
        transported_quotient_map = _affine_morphism_from_pullback(
            changed_acted,
            changed_old_quotient,
            changed_old_quotient_map.coordinate_algebra_morphism(),
        )
        comparison = changed_acted.factor_through_affine_quotient(
            transported_quotient_map
        )

        self._acted_scheme = acted_scheme
        self._ring_map = ring_map
        self._changed_acted_scheme = changed_acted
        self._base_changed_old_quotient = changed_old_quotient
        self._comparison_morphism = comparison

    def source_acted_scheme(self):
        return self._acted_scheme

    def ring_map(self):
        return self._ring_map

    def base_changed_acted_scheme(self):
        return self._changed_acted_scheme

    def quotient_after_base_change(self):
        return self.base_changed_acted_scheme().affine_quotient()

    def base_change_after_quotient(self):
        return self._base_changed_old_quotient

    def comparison_morphism(self):
        return self._comparison_morphism

    def reynolds_hypothesis_holds(self) -> bool:
        source = _own_ring(self.ring_map().domain())
        target = _own_ring(self.ring_map().codomain())
        match source in OwnedFields() and target in OwnedFields():
            case False:
                return False
            case True:
                pass
        group = self.source_acted_scheme().acting_group()
        match group.is_finite():
            case True:
                return group.order_is_invertible_in(target)
            case _:
                return False

    @cached_method
    def reynolds_isomorphism(self):
        assert self.reynolds_hypothesis_holds(), (
            "invariant base change is promoted to an isomorphism here when the finite group order is invertible in the target field"
        )

        forward = self.comparison_morphism()
        source_quotient = self.quotient_after_base_change()
        target_quotient = self.base_change_after_quotient()
        changed_acted = self.base_changed_acted_scheme()
        changed_source_algebra = changed_acted.coordinate_algebra()
        changed_invariants = source_quotient.coordinate_algebra()
        changed_old_invariants = target_quotient.coordinate_algebra()
        comparison_pullback = forward.coordinate_algebra_morphism()
        invariant_inclusion = changed_acted.invariant_algebra_inclusion()

        engine_source = _engine_ring(changed_source_algebra)
        old_generator_images = tuple(
            engine_source(
                _engine_element(
                    changed_source_algebra,
                    invariant_inclusion(
                        comparison_pullback(
                            changed_old_invariants.algebra_generator(label)
                        )
                    ),
                )
            )
            for label in changed_old_invariants.algebra_generating_set()
        )

        inverse_images = {}
        for label in changed_invariants.algebra_generating_set():
            invariant = invariant_inclusion(
                changed_invariants.algebra_generator(label)
            )
            engine_invariant = engine_source(
                _engine_element(changed_source_algebra, invariant)
            )
            certificate = engine_invariant.in_subalgebra(
                old_generator_images,
                algorithm="groebner",
                certificate="invariant",
            )
            if certificate is None:
                raise ArithmeticError(
                    "Reynolds base-change theorem applies but the invariant backend failed to express a new invariant in the base-changed old generators"
                )
            inverse_images[label] = _evaluate_polynomial_in_algebra(
                certificate,
                changed_old_invariants,
            )

        inverse_pullback = changed_invariants.Mor(changed_old_invariants)(
            inverse_images
        )
        inverse = _affine_morphism_from_pullback(
            target_quotient,
            source_quotient,
            inverse_pullback,
        )
        return Schemes(source_quotient.scheme_base_ring()).Core().Mor(
            source_quotient, target_quotient
        )(forward, inverse)

    def _repr_(self) -> str:
        return f"Invariant-quotient base change along {self.ring_map()} for {self.source_acted_scheme()}"



class AffineQuotientFunctor(Functor):
    r"""``(-)/G: GObjects(G, Sch_R) -> AffSch_R`` on the affine actions it is defined for."""

    def __init__(self, group, base_ring) -> None:
        base = _own_ring(base_ring)
        self._group = group
        self._base_ring = base
        Functor.__init__(self, GObjects(group, Schemes(base)), Schemes(base).Affine())

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


class _AffineSectionModuleFunctor(Functor):
    r"""``Gamma: AffGSch_G^op -> Modules(R[G])`` on represented affine actions.

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
        schemes = AffineGSchemes(group, base)
        Functor.__init__(self, schemes.opposite(), Modules(base[group]))

    def acting_group(self):
        return self._group

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, opposite_acted):
        acted = opposite_acted.underlying_object()
        algebra = acted.coordinate_algebra()

        def action(group_element, section):
            pullback = acted.action_of(
                ~group_element
            ).coordinate_algebra_morphism()
            return pullback(algebra(section))

        return self.codomain()(algebra, action)

    def _apply_morphism(self, opposite_arrow):
        arrow = opposite_arrow.underlying_arrow()
        source = self(opposite_arrow.domain())
        target = self(opposite_arrow.codomain())
        pullback = arrow.underlying_arrow().coordinate_algebra_morphism()
        forget = source.forget_action_morphism()
        equip = target.equip_action_morphism()
        return source.Mor(target)(
            {
                label: equip(pullback(forget(source.module_generator(label))))
                for label in source.module_generating_set()
            }
        )

    def _repr_(self):
        return f"Sections with their {self.acting_group()}-action"


__all__ = [
    "AffineInvariantQuotientBaseChangeComparison",
    "AffineQuotientFunctor",
]
